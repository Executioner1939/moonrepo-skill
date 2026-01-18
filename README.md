# Skunkworks

Claude Code skills collection for modern development workflows.

## Available Skills

### clickhouse
**Solana DEX Analytics with ClickHouse**

Design high-performance ClickHouse tables for blockchain analytics.

- Table patterns for trades, pools, tokens, wallets
- OHLCV aggregations with AggregatingMergeTree
- Materialized views and cascaded rollups
- Deduplication with ReplacingMergeTree
- Skip indexes, PREWHERE, query optimization
- Time series patterns (gap fill, trends, histograms)

**Use when:** Designing ClickHouse schemas for Solana DEX data, OHLCV candles, or blockchain analytics.

---

### moonrepo
**Monorepo Task Runner & Build System**

Comprehensive documentation for [moonrepo](https://moonrepo.dev/).

- Complete command reference
- Configuration schemas and best practices
- CI/CD setup guides
- Docker integration patterns

**Use when:** Working with `moon.yml`, `.moon/` configs, or monorepo builds.

---

### utoipa
**Rust OpenAPI Documentation Generator**

Auto-generate OpenAPI 3.1 documentation from Rust code.

- Complete macro reference (`#[utoipa::path]`, `ToSchema`)
- Framework integration (Axum, Actix-web, Rocket)
- Security scheme configuration

**Use when:** Building REST APIs in Rust, documenting endpoints.

---

### eventcatalog
**Event-Driven Architecture Documentation**

Document and visualize event-driven architectures with [EventCatalog](https://www.eventcatalog.dev/).

- Complete API reference for all resource types
- Domain modeling and service documentation
- Event, Command, and Query specifications

**Use when:** Documenting EDA systems, AsyncAPI specs, event sourcing.

## Installation

```bash
# Add the marketplace
/plugin marketplace add Executioner1939/claude-code-skills

# Install specific skills
/plugin install clickhouse@skunkworks
/plugin install moonrepo@skunkworks
/plugin install utoipa@skunkworks
/plugin install eventcatalog@skunkworks
```

## License

MIT

---

**Marketplace:** skunkworks
**Author:** Executioner1939
**Repository:** https://github.com/Executioner1939/claude-code-skills
