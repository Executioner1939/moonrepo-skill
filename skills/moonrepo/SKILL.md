---
name: moonrepo
description: Build, run, and manage monorepo tasks with moon. Use when working with moon.yml, .moon/ configuration, running moon commands, setting up CI/CD pipelines, Docker builds, or managing multi-project workspaces. Trigger on "moon run", "moon ci", "monorepo", "workspace tasks", or project orchestration.
allowed-tools: Read, Bash, Glob, Grep, Edit, Write
---

# Moonrepo - Monorepo Task Orchestration

moon is a task runner and build system for monorepos written in Rust. It provides workspace management, task orchestration, incremental builds, and toolchain management via proto.

## Quick Reference

### Essential Commands

```bash
# Initialize workspace
moon init

# Run tasks
moon run <project>:<task>      # Run specific task
moon run :build                 # Run task in all projects
moon run app:build lib:build    # Run multiple tasks
moon run ~:test                 # Run in closest project

# CI/CD
moon ci                         # Run affected tasks with runInCI enabled
moon ci :build :test            # Run specific affected tasks

# Project info
moon project <id>               # Show project details
moon projects                   # List all projects
moon task <target>              # Show task details
moon tasks                      # List all tasks

# Query system
moon query projects             # Query all projects
moon query tasks                # Query all tasks
moon query affected             # Get affected projects/tasks
moon query changed-files        # Get changed files
```

### Configuration Files

| File | Location | Purpose |
|------|----------|---------|
| `workspace.yml` | `.moon/` | Workspace settings, projects, VCS, pipeline |
| `toolchains.yml` | `.moon/` | Language/runtime versions (Node, Rust, etc.) |
| `tasks/*.yml` | `.moon/tasks/` | Inherited task definitions |
| `moon.yml` | Project root | Project-specific tasks and config |

### Basic Task Configuration

```yaml
# moon.yml
tasks:
  build:
    command: 'npm run build'
    inputs:
      - 'src/**/*'
    outputs:
      - 'dist'

  test:
    command: 'jest'
    deps:
      - '~:build'

  dev:
    command: 'npm run dev'
    preset: 'server'  # Long-running process
```

### Target Syntax

| Pattern | Description |
|---------|-------------|
| `app:build` | Specific project task |
| `:build` | Task in all projects |
| `~:build` | Task in closest project |
| `#tag:build` | Task in projects with tag |
| `^:build` | Dependencies (in deps only) |

## When to Use Each Command

**Development:**
- `moon run <target>` - Run any task with caching
- `moon check [project]` - Run all build/test tasks

**CI/CD:**
- `moon ci` - Run affected tasks (auto-detects changes)
- `moon ci --base main` - Compare against specific branch

**Debugging:**
- `moon task <target> --json` - Inspect task config
- `moon hash <hash>` - Inspect cache hash
- `MOON_LOG=trace moon run <target>` - Verbose logging

**Docker:**
- `moon docker scaffold <project>` - Generate Docker skeleton
- `moon docker file <project>` - Generate Dockerfile

## Additional Resources

For detailed information, see these reference files:

- [COMMANDS.md](COMMANDS.md) - Complete command reference with all flags
- [CONFIG.md](CONFIG.md) - Full configuration schemas
- [CONCEPTS.md](CONCEPTS.md) - Core concepts (workspace, project, task, tokens, MQL)
- [CI.md](CI.md) - CI/CD setup and best practices
- [DOCKER.md](DOCKER.md) - Docker integration guide
- [PROTO.md](PROTO.md) - Proto toolchain manager
- [FRAMEWORKS.md](FRAMEWORKS.md) - Framework-specific examples (Next.js, Vite, etc.)
- [ADVANCED.md](ADVANCED.md) - Advanced patterns and automation

## Utility Scripts

Run these scripts for common workflows:

```bash
# Initialize new workspace
python scripts/init_workspace.py

# Add a new project
python scripts/add_project.py <name> <path>

# Generate CI configuration
python scripts/generate_ci.py --provider github

# Setup Docker
python scripts/docker_setup.py <project>
```
