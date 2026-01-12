# moonrepo-skill

A Claude Code plugin for working with [moonrepo](https://moonrepo.dev/) - a task runner and build system for monorepos.

## Features

- Comprehensive moonrepo command reference
- Configuration schema documentation
- CI/CD setup guides (GitHub Actions, GitLab CI, etc.)
- Docker integration patterns
- Framework-specific examples (Next.js, Vite, etc.)
- Utility scripts for common workflows

## Installation

Add the marketplace and install the plugin:

```bash
/plugin marketplace add Executioner/moonrepo-skill
/plugin install moonrepo-skill
```

Or for local development:

```bash
claude --plugin-dir /path/to/moonrepo-skill
```

## Usage

The skill triggers automatically when working with:
- `moon.yml` or `.moon/` configuration files
- Running moon commands
- Setting up CI/CD pipelines for monorepos
- Docker builds in moonrepo projects
- Managing multi-project workspaces

## Included Documentation

- **COMMANDS.md** - Complete command reference with all flags
- **CONFIG.md** - Full configuration schemas
- **CONCEPTS.md** - Core concepts (workspace, project, task, tokens, MQL)
- **CI.md** - CI/CD setup and best practices
- **DOCKER.md** - Docker integration guide
- **PROTO.md** - Proto toolchain manager
- **FRAMEWORKS.md** - Framework-specific examples
- **ADVANCED.md** - Advanced patterns and automation

## License

MIT
