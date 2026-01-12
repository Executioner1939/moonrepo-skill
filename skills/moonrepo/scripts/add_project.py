#!/usr/bin/env python3
"""
Add a new project to the moon workspace.

Usage:
    python add_project.py <name> <path> [--type app|lib] [--language typescript|javascript|rust]
"""

import argparse
import sys
from pathlib import Path


def create_moon_yml(
    name: str,
    project_type: str,
    language: str,
    tags: list[str]
) -> str:
    """Generate moon.yml content for a project."""
    layer = "application" if project_type == "app" else "library"
    stack = "frontend" if project_type == "app" else "unknown"

    config = f"""# Project configuration
# https://moonrepo.dev/docs/config/project

$schema: '../../.moon/cache/schemas/project.json'

language: '{language}'
layer: '{layer}'
stack: '{stack}'

project:
  title: '{name}'
  description: 'TODO: Add description'

tags:
"""
    for tag in tags:
        config += f"  - '{tag}'\n"

    config += """
fileGroups:
  sources:
    - 'src/**/*'
  tests:
    - 'tests/**/*'
    - '**/*.test.*'

tasks:
"""

    if project_type == "app":
        config += """  dev:
    command: 'npm run dev'
    preset: 'server'
    options:
      runInCI: false

  build:
    command: 'npm run build'
    inputs:
      - '@group(sources)'
    outputs:
      - 'dist'
    deps:
      - '^:build'

  start:
    command: 'npm run start'
    preset: 'server'
    deps:
      - '~:build'
"""
    else:  # library
        config += """  build:
    command: 'tsc --build'
    inputs:
      - '@group(sources)'
      - 'tsconfig.json'
    outputs:
      - 'dist'
    deps:
      - '^:build'
"""

    return config


def create_package_json(name: str, project_type: str) -> str:
    """Generate package.json content."""
    pkg = {
        "name": f"@workspace/{name}",
        "version": "0.0.0",
        "private": True,
        "type": "module",
    }

    if project_type == "app":
        pkg["scripts"] = {
            "dev": "vite",
            "build": "vite build",
            "start": "vite preview"
        }
    else:
        pkg["main"] = "./dist/index.js",
        pkg["types"] = "./dist/index.d.ts",
        pkg["exports"] = {
            ".": {
                "types": "./dist/index.d.ts",
                "import": "./dist/index.js"
            }
        }

    import json
    return json.dumps(pkg, indent=2)


def create_tsconfig(project_type: str) -> str:
    """Generate tsconfig.json content."""
    if project_type == "app":
        return """{
  "extends": "../../tsconfig.options.json",
  "compilerOptions": {
    "noEmit": true
  },
  "include": ["src"],
  "references": []
}
"""
    else:
        return """{
  "extends": "../../tsconfig.options.json",
  "compilerOptions": {
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src"],
  "references": []
}
"""


def create_src_files(name: str, project_type: str, language: str) -> dict[str, str]:
    """Generate source files."""
    files = {}

    ext = "ts" if language == "typescript" else "js"

    if project_type == "app":
        files[f"src/main.{ext}"] = f"""// {name} application entry point

console.log('Hello from {name}!');
"""
    else:
        files[f"src/index.{ext}"] = f"""// {name} library exports

export function hello(): string {{
  return 'Hello from {name}!';
}}
"""

    return files


def write_file(path: Path, content: str) -> None:
    """Write content to a file, creating directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    print(f"Created: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add a new project to the moon workspace"
    )
    parser.add_argument("name", help="Project name")
    parser.add_argument("path", help="Project path (e.g., apps/web or packages/utils)")
    parser.add_argument(
        "--type",
        choices=["app", "lib"],
        default="lib",
        help="Project type (default: lib)"
    )
    parser.add_argument(
        "--language",
        choices=["typescript", "javascript", "rust"],
        default="typescript",
        help="Primary language (default: typescript)"
    )
    parser.add_argument(
        "--tags",
        nargs="*",
        default=[],
        help="Project tags"
    )

    args = parser.parse_args()

    # Validate workspace
    if not Path(".moon").exists():
        print("Error: Not in a moon workspace. Run from workspace root.")
        return 1

    project_path = Path(args.path)

    if project_path.exists():
        print(f"Error: Path already exists: {project_path}")
        return 1

    # Determine tags based on type
    tags = args.tags or []
    if args.language == "typescript" and "typescript" not in tags:
        tags.append("typescript")

    print(f"Creating project: {args.name}")
    print(f"  Path: {project_path}")
    print(f"  Type: {args.type}")
    print(f"  Language: {args.language}")
    print(f"  Tags: {tags}")
    print()

    # Create project directory
    project_path.mkdir(parents=True, exist_ok=True)

    # Create moon.yml
    write_file(
        project_path / "moon.yml",
        create_moon_yml(args.name, args.type, args.language, tags)
    )

    # Create package.json for JS/TS projects
    if args.language in ["typescript", "javascript"]:
        write_file(
            project_path / "package.json",
            create_package_json(args.name, args.type)
        )

    # Create tsconfig.json for TypeScript
    if args.language == "typescript":
        write_file(
            project_path / "tsconfig.json",
            create_tsconfig(args.type)
        )

    # Create source files
    for file_path, content in create_src_files(args.name, args.type, args.language).items():
        write_file(project_path / file_path, content)

    print()
    print(f"Project '{args.name}' created successfully!")
    print()
    print("Next steps:")
    print(f"  1. cd {project_path}")
    print(f"  2. Install dependencies: moon run {args.name}:install (or npm/pnpm install)")
    print(f"  3. Run tasks: moon run {args.name}:<task>")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
