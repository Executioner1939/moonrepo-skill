#!/usr/bin/env python3
"""
Initialize a new moon workspace with best-practice configuration.

Usage:
    python init_workspace.py [--minimal] [--node] [--rust] [--typescript]
"""

import argparse
import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def check_moon_installed() -> bool:
    """Check if moon is installed."""
    result = run_command(["moon", "--version"], check=False)
    return result.returncode == 0


def init_moon(minimal: bool = False) -> None:
    """Initialize moon in the current directory."""
    cmd = ["moon", "init"]
    if minimal:
        cmd.append("--minimal")
    cmd.append("--yes")
    run_command(cmd)


def create_workspace_config(
    node: bool = False,
    rust: bool = False,
    typescript: bool = False
) -> str:
    """Generate workspace.yml content."""
    config = """# Moon workspace configuration
# https://moonrepo.dev/docs/config/workspace

$schema: './cache/schemas/workspace.json'

# Define projects in the workspace
projects:
  - 'apps/*'
  - 'packages/*'

# VCS configuration
vcs:
  defaultBranch: 'main'
  provider: 'github'
  hooks:
    pre-commit:
      - 'moon run :lint :format --affected --status=staged'

# Pipeline configuration
pipeline:
  cacheLifetime: '7 days'
  inheritColorsForPipedTasks: true

# Code owners (optional)
# codeowners:
#   sync: true
#   globalPaths:
#     '*': ['@team']
"""
    return config


def create_toolchains_config(
    node: bool = False,
    rust: bool = False,
    typescript: bool = False
) -> str:
    """Generate toolchains.yml content."""
    config = """# Moon toolchain configuration
# https://moonrepo.dev/docs/config/toolchain

$schema: './cache/schemas/toolchains.json'
"""

    if node or typescript:
        config += """
# JavaScript/Node.js configuration
javascript:
  packageManager: 'pnpm'
  syncPackageManagerField: true
  syncProjectWorkspaceDependencies: true

node:
  version: '22.14.0'

pnpm:
  version: '9.0.0'
"""

    if typescript:
        config += """
# TypeScript configuration
typescript:
  syncProjectReferences: true
  syncProjectReferencesToPaths: true
"""

    if rust:
        config += """
# Rust configuration
rust:
  version: 'stable'
  components:
    - 'clippy'
    - 'rustfmt'
"""

    return config


def create_tasks_config(
    node: bool = False,
    rust: bool = False,
    typescript: bool = False
) -> str:
    """Generate tasks/all.yml content."""
    config = """# Inherited tasks for all projects
# https://moonrepo.dev/docs/config/tasks

$schema: '../cache/schemas/tasks.json'

fileGroups:
  sources:
    - 'src/**/*'
  tests:
    - 'tests/**/*'
    - '**/*.test.*'
    - '**/*.spec.*'
  configs:
    - '*.config.*'
    - '*.json'

implicitInputs:
  - 'package.json'
"""

    if node or typescript:
        config += """
tasks:
  lint:
    command: 'eslint'
    args:
      - '--ext'
      - '.js,.jsx,.ts,.tsx'
      - '--no-error-on-unmatched-pattern'
      - '.'
    inputs:
      - '@group(sources)'
      - '.eslintrc.*'
      - '/.eslintrc.*'

  format:
    command: 'prettier'
    args:
      - '--check'
      - '.'
    inputs:
      - '@group(sources)'
      - '.prettierrc.*'
      - '/.prettierrc.*'

  test:
    command: 'vitest run'
    inputs:
      - '@group(sources)'
      - '@group(tests)'
    options:
      retryCount: 2
"""

    if typescript:
        config += """
  typecheck:
    command: 'tsc'
    args:
      - '--build'
      - '--pretty'
    inputs:
      - '@group(sources)'
      - 'tsconfig.json'
      - '/tsconfig.options.json'
"""

    if rust:
        config += """
  # Rust tasks (add to rust-specific projects)
  # cargo-build:
  #   command: 'cargo build'
  #   inputs:
  #     - 'src/**/*'
  #     - 'Cargo.toml'
  #   outputs:
  #     - 'target'
"""

    return config


def create_directory_structure() -> None:
    """Create standard directory structure."""
    directories = [
        "apps",
        "packages",
        ".moon/tasks",
    ]
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")


def write_config_file(path: str, content: str) -> None:
    """Write content to a configuration file."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)
    print(f"Created: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Initialize a moon workspace with best practices"
    )
    parser.add_argument(
        "--minimal",
        action="store_true",
        help="Generate minimal configuration"
    )
    parser.add_argument(
        "--node",
        action="store_true",
        help="Include Node.js toolchain"
    )
    parser.add_argument(
        "--rust",
        action="store_true",
        help="Include Rust toolchain"
    )
    parser.add_argument(
        "--typescript",
        action="store_true",
        help="Include TypeScript configuration (implies --node)"
    )

    args = parser.parse_args()

    # TypeScript implies Node
    if args.typescript:
        args.node = True

    # Check if moon is installed
    if not check_moon_installed():
        print("Error: moon is not installed. Install with:")
        print("  curl -fsSL https://moonrepo.dev/install/moon.sh | bash")
        return 1

    # Check if already initialized
    if Path(".moon").exists():
        print("Error: .moon directory already exists. Workspace already initialized.")
        return 1

    print("Initializing moon workspace...")
    print()

    # Create directory structure
    create_directory_structure()

    # Initialize moon
    init_moon(minimal=args.minimal)

    # Write configuration files
    write_config_file(
        ".moon/workspace.yml",
        create_workspace_config(args.node, args.rust, args.typescript)
    )

    write_config_file(
        ".moon/toolchains.yml",
        create_toolchains_config(args.node, args.rust, args.typescript)
    )

    write_config_file(
        ".moon/tasks/all.yml",
        create_tasks_config(args.node, args.rust, args.typescript)
    )

    print()
    print("Workspace initialized successfully!")
    print()
    print("Next steps:")
    print("  1. Create a project: moon generate <template> --to apps/<name>")
    print("  2. Or manually add a moon.yml to your project directory")
    print("  3. Run tasks: moon run <project>:<task>")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
