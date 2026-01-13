---
name: utoipa
description: Rust library for auto-generating OpenAPI documentation from code annotations
---

# utoipa

**Simple, Fast, Code-first OpenAPI Documentation for Rust**

Pronounced **/u:ˈtoʊ:i.pɑ/** - Auto-generate OpenAPI 3.1 documentation from your Rust code using procedural macros. Framework-agnostic with first-class support for Axum, Actix-web, and Rocket.

**Repository:** [juhaku/utoipa](https://github.com/juhaku/utoipa) | **Version:** 5.4.0 | **MSRV:** 1.75

## When to Use This Skill

Use this skill when working on:

- **Adding OpenAPI documentation** to Rust REST APIs
- **Documenting request/response schemas** with `ToSchema` derive macro
- **Annotating API endpoints** with `#[utoipa::path]` macro
- **Setting up Swagger UI**, Redoc, RapiDoc, or Scalar for API visualization
- **Integrating with web frameworks**: Axum (`utoipa-axum`), Actix-web (`utoipa-actix-web`), Rocket
- **Generating OpenAPI JSON/YAML** from Rust types
- **Configuring security schemes** (JWT, API keys, OAuth2)
- **Working with generic types** in OpenAPI schemas

**Trigger conditions:**
- User mentions "utoipa", "OpenAPI in Rust", or "Swagger for Rust"
- User needs to document a Rust REST API
- User is working with Axum/Actix-web/Rocket and needs API docs
- User asks about deriving `ToSchema` or `OpenApi`

## Quick Reference

### Installation

```toml
[dependencies]
utoipa = "5"
utoipa-swagger-ui = { version = "9", features = ["axum"] }
```

### Basic Schema Definition

Define types that appear in your OpenAPI spec:

```rust
use utoipa::ToSchema;

#[derive(ToSchema)]
struct Pet {
    id: u64,
    name: String,
    age: Option<i32>,
}
```

### Documenting an Endpoint

Use `#[utoipa::path]` to document handlers:

```rust
/// Get pet by id
///
/// Get pet from database by pet id
#[utoipa::path(
    get,
    path = "/pets/{id}",
    responses(
        (status = 200, description = "Pet found successfully", body = Pet),
        (status = NOT_FOUND, description = "Pet was not found")
    ),
    params(
        ("id" = u64, Path, description = "Pet database id to get Pet for"),
    )
)]
async fn get_pet_by_id(pet_id: u64) -> Result<Pet, NotFound> {
    // handler implementation
}
```

### Creating the OpenAPI Document

Derive `OpenApi` and register paths:

```rust
use utoipa::OpenApi;

#[derive(OpenApi)]
#[openapi(paths(pet_api::get_pet_by_id))]
struct ApiDoc;

// Generate JSON
println!("{}", ApiDoc::openapi().to_pretty_json().unwrap());
```

### Customizing OpenAPI Info

```rust
#[derive(OpenApi)]
#[openapi(
    info(description = "My Api description"),
)]
struct ApiDoc;

// Modify at runtime
let mut doc = ApiDoc::openapi();
doc.info.title = String::from("My Api");
```

### Axum Integration with utoipa-axum

```rust
use utoipa_axum::{router::OpenApiRouter, routes};

let (router, api) = OpenApiRouter::new()
    .routes(routes!(get_pet_by_id, create_pet))
    .split_for_parts();
```

### Swagger UI Setup (Axum)

```rust
use utoipa_swagger_ui::SwaggerUi;

let app = Router::new()
    .merge(SwaggerUi::new("/swagger-ui")
        .url("/api-docs/openapi.json", ApiDoc::openapi()));
```

### Query Parameters with IntoParams

```rust
use utoipa::IntoParams;

#[derive(IntoParams)]
struct PetQuery {
    /// Filter by pet name
    name: Option<String>,
    /// Filter by age range
    #[param(minimum = 0, maximum = 20)]
    age: Option<i32>,
}
```

### Enum Schemas

```rust
#[derive(ToSchema)]
enum PetStatus {
    Available,
    Pending,
    Sold,
}
```

### Generated Output Example

The above code generates OpenAPI 3.1 JSON:

```json
{
  "openapi": "3.1.0",
  "paths": {
    "/pets/{id}": {
      "get": {
        "summary": "Get pet by id",
        "parameters": [{
          "name": "id",
          "in": "path",
          "required": true,
          "schema": { "type": "integer", "format": "int64" }
        }],
        "responses": {
          "200": {
            "description": "Pet found successfully",
            "content": {
              "application/json": {
                "schema": { "$ref": "#/components/schemas/Pet" }
              }
            }
          }
        }
      }
    }
  }
}
```

## Key Concepts

### Core Derives

| Derive | Purpose |
|--------|---------|
| `ToSchema` | Generate OpenAPI schema for types (request/response bodies) |
| `OpenApi` | Create the root OpenAPI document, register paths and schemas |
| `IntoParams` | Document query/path parameters from structs |
| `IntoResponses` | Define reusable response types |

### Crate Ecosystem

| Crate | Purpose |
|-------|---------|
| `utoipa` | Core library with macros and OpenAPI types |
| `utoipa-axum` | Axum router integration for automatic path registration |
| `utoipa-actix-web` | Actix-web integration |
| `utoipa-swagger-ui` | Serve Swagger UI for API visualization |
| `utoipa-redoc` | Redoc documentation viewer |
| `utoipa-rapidoc` | RapiDoc documentation viewer |
| `utoipa-scalar` | Scalar documentation viewer |
| `utoipa-config` | Rust type aliases for OpenAPI |

### Feature Flags

- **`macros`** (default): Enable derive macros
- **`yaml`**: YAML serialization via `serde_norway`
- **`actix_extras`**: Actix-web request body/response parsing
- **`axum_extras`**: Axum request body/response parsing
- **`rocket_extras`**: Rocket framework support

## Working with This Skill

### For Beginners

1. Start with `ToSchema` on your request/response types
2. Add `#[utoipa::path]` to your handlers with basic `responses`
3. Create an `OpenApi` struct and register your paths
4. Set up Swagger UI to visualize your docs

### For Intermediate Users

1. Use `IntoParams` for complex query parameter documentation
2. Configure security schemes for authentication
3. Use `utoipa-axum` or `utoipa-actix-web` for automatic path registration
4. Customize OpenAPI info, tags, and external docs

### For Advanced Users

1. Implement `ToSchema` manually for external types
2. Use runtime modification via `OpenApiBuilder`
3. Create nested/modular API documentation
4. Configure type aliases via `utoipa-config`

### Common Patterns

**External type workaround** (see issue #790):
```rust
#[derive(ToSchema)]
#[schema(as = ExternalType)]
struct MyExternalTypeSchema {
    // mirror the external type's fields
}
```

**Generic types limitation**: Tuples, arrays, and slices cannot be used as generic arguments on types deriving `ToSchema`.

## Reference Files

| File | Contents |
|------|----------|
| `references/README.md` | Complete setup guide, feature list, examples, FAQ |
| `references/CHANGELOG.md` | Version history (per-crate changelogs linked) |
| `references/issues.md` | 60 recent GitHub issues - known bugs and feature requests |
| `references/releases.md` | 205 releases with detailed changelogs |
| `references/file_structure.md` | 616 files - examples directory especially useful |

### Key Examples in Repository

- `examples/simple-axum/` - Minimal Axum setup
- `examples/todo-axum/` - Full CRUD example
- `examples/axum-utoipa-bindings/` - utoipa-axum integration
- `examples/todo-actix/` - Actix-web example
- `examples/rocket-todo/` - Rocket framework example

## Recent Updates (v5.4.0)

- Support for `jiff` v0.2 date/time library
- OpenAPI extensions support in `#[utoipa::path]`
- Enhanced HashMap/HashSet schema generation with custom hashers
- YAML serialization now uses `serde_norway`

## Known Issues

- `#[serde(flatten)]` not fully supported with `IntoParams` (#841)
- Type-aliased struct fields may cause issues with `ToSchema` (#1495)
- Large structs may trigger Clippy warnings about stack allocation (#1454)

---

**Generated by Skill Seekers** | [GitHub Repository](https://github.com/juhaku/utoipa) | [docs.rs](https://docs.rs/utoipa)
