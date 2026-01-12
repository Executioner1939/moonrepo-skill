#!/usr/bin/env python3
"""
Generate Docker configuration for moon projects.

Usage:
    python docker_setup.py <project> [--type node|bun|rust] [--minimal]
"""

import argparse
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def generate_dockerfile_node(project: str, minimal: bool = False) -> str:
    """Generate Dockerfile for Node.js projects."""
    if minimal:
        return f"""# Minimal Node.js Dockerfile
FROM node:22-alpine
WORKDIR /app

RUN npm install -g @moonrepo/cli

COPY . .
RUN moon run {project}:build

CMD ["node", "apps/{project}/dist/index.js"]
"""

    return f"""# Multi-stage Node.js Dockerfile with moon
# https://moonrepo.dev/docs/guides/docker

# Base stage - install moon
FROM node:22-alpine AS base
WORKDIR /app
RUN npm install -g @moonrepo/cli

# Skeleton stage - generate Docker scaffolds
FROM base AS skeleton
COPY . .
RUN moon docker scaffold {project}

# Build stage
FROM base AS build

# Copy workspace skeleton (manifests, configs)
COPY --from=skeleton /app/.moon/docker/configs .

# Install dependencies (cached layer)
RUN moon docker setup

# Copy source files
COPY --from=skeleton /app/.moon/docker/sources .

# Build the project
RUN moon run {project}:build

# Prune dev dependencies
RUN moon docker prune

# Production stage
FROM node:22-alpine AS production
WORKDIR /app

ENV NODE_ENV=production

# Copy built application
COPY --from=build /app .

# Run the application
CMD ["node", "apps/{project}/dist/index.js"]
"""


def generate_dockerfile_bun(project: str, minimal: bool = False) -> str:
    """Generate Dockerfile for Bun projects."""
    if minimal:
        return f"""# Minimal Bun Dockerfile
FROM oven/bun:latest
WORKDIR /app

RUN bun add -g @moonrepo/cli

COPY . .
RUN moon run {project}:build

CMD ["bun", "run", "apps/{project}/dist/index.js"]
"""

    return f"""# Multi-stage Bun Dockerfile with moon
# https://moonrepo.dev/docs/guides/docker

# Base stage - install moon
FROM oven/bun:latest AS base
WORKDIR /app
RUN bun add -g @moonrepo/cli

# Skeleton stage
FROM base AS skeleton
COPY . .
RUN moon docker scaffold {project}

# Build stage
FROM base AS build
COPY --from=skeleton /app/.moon/docker/configs .
RUN moon docker setup
COPY --from=skeleton /app/.moon/docker/sources .
RUN moon run {project}:build
RUN moon docker prune

# Production stage
FROM oven/bun:latest AS production
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app .
CMD ["bun", "run", "apps/{project}/dist/index.js"]
"""


def generate_dockerfile_rust(project: str, minimal: bool = False) -> str:
    """Generate Dockerfile for Rust projects."""
    if minimal:
        return f"""# Minimal Rust Dockerfile
FROM rust:1.75-alpine AS builder
WORKDIR /app

RUN apk add --no-cache musl-dev curl bash
RUN curl -fsSL https://moonrepo.dev/install/moon.sh | bash
ENV PATH="/root/.moon/bin:$PATH"

COPY . .
RUN moon run {project}:build

FROM alpine:latest
COPY --from=builder /app/target/release/{project} /usr/local/bin/
CMD ["{project}"]
"""

    return f"""# Multi-stage Rust Dockerfile with moon
# https://moonrepo.dev/docs/guides/docker

# Build stage
FROM rust:1.75-alpine AS builder
WORKDIR /app

# Install dependencies
RUN apk add --no-cache musl-dev curl bash

# Install moon
RUN curl -fsSL https://moonrepo.dev/install/moon.sh | bash
ENV PATH="/root/.moon/bin:$PATH"

# Copy source
COPY . .

# Build with moon
RUN moon run {project}:build --release

# Production stage
FROM alpine:latest AS production

# Install runtime dependencies
RUN apk add --no-cache ca-certificates

# Copy binary
COPY --from=builder /app/target/release/{project} /usr/local/bin/

# Run
CMD ["{project}"]
"""


def generate_dockerignore() -> str:
    """Generate .dockerignore content."""
    return """# Moon cache
.moon/cache

# Dependencies
node_modules
target

# Build outputs
dist
build

# VCS
.git
.gitignore

# IDE
.vscode
.idea
*.swp
*.swo

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# OS
.DS_Store
Thumbs.db

# Testing
coverage
.nyc_output

# Environment
.env
.env.*
!.env.example
"""


def write_file(path: Path, content: str) -> None:
    """Write content to a file."""
    path.write_text(content)
    print(f"Created: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Docker configuration for moon projects"
    )
    parser.add_argument("project", help="Project name")
    parser.add_argument(
        "--type",
        choices=["node", "bun", "rust"],
        default="node",
        help="Project type (default: node)"
    )
    parser.add_argument(
        "--minimal",
        action="store_true",
        help="Generate minimal Dockerfile without multi-stage"
    )
    parser.add_argument(
        "--output",
        default="Dockerfile",
        help="Output Dockerfile name (default: Dockerfile)"
    )
    parser.add_argument(
        "--scaffold",
        action="store_true",
        help="Also run moon docker scaffold"
    )

    args = parser.parse_args()

    # Validate workspace
    if not Path(".moon").exists():
        print("Error: Not in a moon workspace. Run from workspace root.")
        return 1

    print(f"Generating Docker configuration for: {args.project}")
    print(f"  Type: {args.type}")
    print(f"  Minimal: {args.minimal}")
    print()

    # Generate Dockerfile
    if args.type == "node":
        dockerfile_content = generate_dockerfile_node(args.project, args.minimal)
    elif args.type == "bun":
        dockerfile_content = generate_dockerfile_bun(args.project, args.minimal)
    elif args.type == "rust":
        dockerfile_content = generate_dockerfile_rust(args.project, args.minimal)
    else:
        print(f"Error: Unsupported type: {args.type}")
        return 1

    # Write Dockerfile
    write_file(Path(args.output), dockerfile_content)

    # Generate .dockerignore if it doesn't exist
    dockerignore_path = Path(".dockerignore")
    if not dockerignore_path.exists():
        write_file(dockerignore_path, generate_dockerignore())

    # Run scaffold if requested
    if args.scaffold:
        print()
        result = run_command(["moon", "docker", "scaffold", args.project], check=False)
        if result.returncode != 0:
            print(f"Warning: scaffold failed: {result.stderr}")

    print()
    print("Docker configuration generated successfully!")
    print()
    print("Next steps:")
    print(f"  1. Review and customize {args.output}")
    print(f"  2. Run: docker build -t {args.project} .")
    print(f"  3. Run: docker run {args.project}")
    print()

    if not args.minimal:
        print("Multi-stage build features:")
        print("  - Optimized layer caching")
        print("  - Smaller production image")
        print("  - moon docker scaffold integration")
        print("  - Dev dependency pruning")

    return 0


if __name__ == "__main__":
    sys.exit(main())
