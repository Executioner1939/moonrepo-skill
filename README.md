# Claude Code Skills

A curated collection of Claude Code skills for modern development workflows. This repository contains high-quality documentation and reference materials for various tools and frameworks.

## 📦 Available Skills

### 🌙 moonrepo
**Monorepo Task Runner & Build System**

Comprehensive documentation for [moonrepo](https://moonrepo.dev/) - build, run, and manage monorepo tasks efficiently.

**Features:**
- Complete command reference with all flags
- Configuration schemas and best practices
- CI/CD setup guides (GitHub Actions, GitLab CI, etc.)
- Docker integration patterns
- Framework-specific examples (Next.js, Vite, etc.)
- Proto toolchain manager integration

**Use when:** Working with `moon.yml`, `.moon/` configs, monorepo builds, or CI/CD pipelines.

---

### 🦀 utoipa
**Rust OpenAPI Documentation Generator**

Auto-generate OpenAPI 3.1 documentation from Rust code using procedural macros.

**Features:**
- Complete macro reference (`#[utoipa::path]`, `ToSchema`, etc.)
- Request/response schema documentation
- Framework integration (Axum, Actix-web, Rocket)
- Security scheme configuration
- Advanced patterns and examples

**Use when:** Building REST APIs in Rust, documenting endpoints, generating OpenAPI specs.

---

### 📚 EventCatalog
**Event-Driven Architecture Documentation**

Document and visualize event-driven architectures with [EventCatalog](https://www.eventcatalog.dev/).

**Features:**
- Complete API reference for all resource types
- Domain modeling and service documentation
- Event, Command, and Query specifications
- Channel and Flow documentation
- Entity and Data schema definitions
- CLI commands and configuration

**Use when:** Documenting EDA systems, AsyncAPI specs, event sourcing, or microservices architectures.

## 📥 Installation

### Install Individual Skills

```bash
# Add the marketplace
/plugin marketplace add Executioner1939/claude-code-skills

# Install specific skills
/plugin install moonrepo
/plugin install utoipa
/plugin install eventcatalog
```

### Local Development

```bash
git clone https://github.com/Executioner1939/claude-code-skills.git
claude --plugin-dir /path/to/claude-code-skills/skills/moonrepo
```

## 🎯 Skill Structure

Each skill follows a consistent structure:

```
skills/
├── moonrepo/
│   ├── SKILL.md          # Main skill entry point
│   ├── COMMANDS.md       # Command reference
│   ├── CONFIG.md         # Configuration docs
│   └── scripts/          # Helper scripts
├── utoipa/
│   ├── SKILL.md
│   └── references/       # Detailed reference docs
└── eventcatalog/
    ├── SKILL.md
    └── references/       # API documentation
```

## 🤝 Contributing

Contributions are welcome! To add a new skill or improve existing ones:

1. Fork the repository
2. Create a feature branch
3. Add/update skills following the existing structure
4. Update marketplace.json with skill metadata
5. Submit a pull request

## 📄 License

MIT

## 🔗 Links

- [moonrepo](https://moonrepo.dev/)
- [utoipa](https://github.com/juhaku/utoipa)
- [EventCatalog](https://www.eventcatalog.dev/)

---

**Author:** Executioner1939  
**Repository:** https://github.com/Executioner1939/claude-code-skills
