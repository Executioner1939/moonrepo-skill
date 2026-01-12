#!/usr/bin/env python3
"""
Generate CI configuration for moon workspaces.

Usage:
    python generate_ci.py --provider github|gitlab|circleci
"""

import argparse
import sys
from pathlib import Path


def generate_github_actions() -> str:
    """Generate GitHub Actions workflow."""
    return """# Moon CI Pipeline
# https://moonrepo.dev/docs/guides/ci

name: CI

on:
  push:
    branches: ['main']
  pull_request:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  ci:
    name: CI
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for affected detection

      - name: Setup moon toolchain
        uses: moonrepo/setup-toolchain@v0
        with:
          auto-install: true

      - name: Cache dependencies
        uses: actions/cache@v4
        with:
          path: |
            ~/.proto
            node_modules
            .moon/cache
          key: ${{ runner.os }}-moon-${{ hashFiles('**/package-lock.json', '**/pnpm-lock.yaml', '.moon/**/*.yml') }}
          restore-keys: |
            ${{ runner.os }}-moon-

      - name: Run CI
        run: moon ci

      - name: Upload run report
        uses: moonrepo/run-report-action@v1
        if: success() || failure()
        with:
          access-token: ${{ secrets.GITHUB_TOKEN }}

  # Optional: Parallel job distribution
  # ci-parallel:
  #   name: CI (Job ${{ matrix.index }})
  #   runs-on: ubuntu-latest
  #   strategy:
  #     fail-fast: false
  #     matrix:
  #       index: [0, 1, 2, 3]
  #   steps:
  #     - uses: actions/checkout@v4
  #       with:
  #         fetch-depth: 0
  #     - uses: moonrepo/setup-toolchain@v0
  #     - run: moon ci --job ${{ matrix.index }} --job-total 4
"""


def generate_gitlab_ci() -> str:
    """Generate GitLab CI configuration."""
    return """# Moon CI Pipeline
# https://moonrepo.dev/docs/guides/ci

stages:
  - ci

variables:
  GIT_DEPTH: 0  # Required for affected detection

.moon-setup:
  before_script:
    - curl -fsSL https://moonrepo.dev/install/moon.sh | bash
    - export PATH="$HOME/.moon/bin:$PATH"
    - moon setup

ci:
  stage: ci
  extends: .moon-setup
  image: node:22
  script:
    - moon ci
  cache:
    key: moon-$CI_COMMIT_REF_SLUG
    paths:
      - .moon/cache
      - node_modules
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

# Optional: Parallel job distribution
# ci-parallel:
#   stage: ci
#   extends: .moon-setup
#   image: node:22
#   parallel:
#     matrix:
#       - JOB_INDEX: [0, 1, 2, 3]
#   script:
#     - moon ci --job $JOB_INDEX --job-total 4
"""


def generate_circleci() -> str:
    """Generate CircleCI configuration."""
    return """# Moon CI Pipeline
# https://moonrepo.dev/docs/guides/ci

version: 2.1

orbs:
  node: circleci/node@5

executors:
  default:
    docker:
      - image: cimg/node:22.0

commands:
  setup-moon:
    steps:
      - run:
          name: Install moon
          command: curl -fsSL https://moonrepo.dev/install/moon.sh | bash
      - run:
          name: Setup toolchain
          command: |
            export PATH="$HOME/.moon/bin:$PATH"
            moon setup

jobs:
  ci:
    executor: default
    steps:
      - checkout
      - restore_cache:
          keys:
            - moon-{{ checksum "pnpm-lock.yaml" }}-{{ checksum ".moon/workspace.yml" }}
            - moon-
      - setup-moon
      - run:
          name: Run CI
          command: |
            export PATH="$HOME/.moon/bin:$PATH"
            moon ci
      - save_cache:
          key: moon-{{ checksum "pnpm-lock.yaml" }}-{{ checksum ".moon/workspace.yml" }}
          paths:
            - .moon/cache
            - node_modules
            - ~/.proto

workflows:
  main:
    jobs:
      - ci:
          filters:
            branches:
              only:
                - main
                - /pull\/.*/
"""


def generate_azure_pipelines() -> str:
    """Generate Azure Pipelines configuration."""
    return """# Moon CI Pipeline
# https://moonrepo.dev/docs/guides/ci

trigger:
  branches:
    include:
      - main

pr:
  branches:
    include:
      - main

pool:
  vmImage: ubuntu-latest

variables:
  npm_config_cache: $(Pipeline.Workspace)/.npm

steps:
  - checkout: self
    fetchDepth: 0  # Required for affected detection

  - task: Cache@2
    inputs:
      key: 'moon | "$(Agent.OS)" | pnpm-lock.yaml | .moon/workspace.yml'
      restoreKeys: |
        moon | "$(Agent.OS)"
      path: |
        $(npm_config_cache)
        .moon/cache
    displayName: Cache dependencies

  - script: curl -fsSL https://moonrepo.dev/install/moon.sh | bash
    displayName: Install moon

  - script: |
      export PATH="$HOME/.moon/bin:$PATH"
      moon setup
    displayName: Setup toolchain

  - script: |
      export PATH="$HOME/.moon/bin:$PATH"
      moon ci
    displayName: Run CI
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate CI configuration for moon workspace"
    )
    parser.add_argument(
        "--provider",
        choices=["github", "gitlab", "circleci", "azure"],
        required=True,
        help="CI provider"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing configuration"
    )

    args = parser.parse_args()

    # Validate workspace
    if not Path(".moon").exists():
        print("Error: Not in a moon workspace. Run from workspace root.")
        return 1

    # Generate configuration based on provider
    if args.provider == "github":
        output_path = Path(".github/workflows/ci.yml")
        content = generate_github_actions()
    elif args.provider == "gitlab":
        output_path = Path(".gitlab-ci.yml")
        content = generate_gitlab_ci()
    elif args.provider == "circleci":
        output_path = Path(".circleci/config.yml")
        content = generate_circleci()
    elif args.provider == "azure":
        output_path = Path("azure-pipelines.yml")
        content = generate_azure_pipelines()
    else:
        print(f"Error: Unsupported provider: {args.provider}")
        return 1

    # Check if file exists
    if output_path.exists() and not args.force:
        print(f"Error: {output_path} already exists. Use --force to overwrite.")
        return 1

    # Create directory and write file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)

    print(f"Created: {output_path}")
    print()
    print("CI configuration generated successfully!")
    print()
    print("Features included:")
    print("  - Checkout with full history (for affected detection)")
    print("  - Moon toolchain setup")
    print("  - Dependency caching")
    print("  - moon ci command execution")
    if args.provider == "github":
        print("  - Run report action (PR comments)")
        print("  - Concurrency control")
    print()
    print("Customize the configuration as needed for your workflow.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
