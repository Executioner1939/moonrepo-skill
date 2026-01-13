# Eventcatalog - Getting Started

**Pages:** 18

---

## What are entities?

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/entities/introduction

**Contents:**
- What are entities?
  - How do entities work in EventCatalog?​

In Domain-Driven Design, an entity is an object with a unique identity that stays the same over time, even if its data changes. It’s defined by this identity, not just its properties. For example, a Customer with a unique ID is an entity, even if their name or address changes.

In Domain-Driven Design, entities are the core building blocks of a domain—they represent key concepts or things within that domain that have a unique identity. The domain defines the business logic and rules, and entities bring that logic to life by modeling real-world objects or roles, like Order, Customer, or Invoice. Each entity lives within a bounded context of the domain, ensuring it behaves consistently according to that part of the business.

In EventCatalog entities are optional., if you don't want to add entity documentation you can skip this resource.

Entities are a "optional" resource in EventCatalog and like every other resource in EventCatalog they are defined in markdown files.

Entities can be added to your domains and services.

---

## Understanding flows

**URL:** https://www.eventcatalog.dev/docs/development/guides/flows/introduction

**Contents:**
- Understanding flows
  - Example​

Flows are a way to document business workflows in your organization. You can reuse your documented resources (e.g services, messages, data stores) in your flows.

An example of a flow would be when a user makes a payment to an e-commence system, this interaction triggers many parts of the architecture (services, external services, commands, queries and events):

You can see a payment flow example here.

---

## Understanding diagrams

**URL:** https://www.eventcatalog.dev/docs/development/guides/diagrams/introduction

**Contents:**
- Understanding diagrams
  - What can you do with diagrams?​
  - How is this different from auto-generated diagrams?​
  - What do diagrams look like in EventCatalog?​
  - When to use custom diagrams​
  - Supported content formats​

EventCatalog automatically generates architecture diagrams based on your resources and how they relate to each other. These auto-generated visualizations help you understand your system's structure.

But what about your own diagrams?

Many teams have existing architecture diagrams - whether they're Mermaid flowcharts, PlantUML sequence diagrams, Miro boards, IcePanel views, or simple images. The diagrams feature lets you bring these into EventCatalog as first-class, versioned resources.

With diagrams in EventCatalog you can:

Both complement each other. Auto-generated diagrams show your system as documented in the catalog. Custom diagrams let you add context - migration plans, target architectures, sequence flows, event storming results, or embedded boards from your favorite diagramming tools.

Diagrams have their own dedicated pages with version switching and appear in the sidebar when assigned to resources.

View Demo of a Target Architecture diagram →

Use diagrams when you want to:

Diagrams support any content you can write in MDX:

---

## Understanding data stores

**URL:** https://www.eventcatalog.dev/docs/development/guides/data/introduction

**Contents:**
- Understanding data stores

In EventCatalog data stores (containers) represent data stores that are used in your architecture (e.g. databases, caches, objectStore, searchIndexes, etc).

Using the data store resource in EventCatalog you can define how your services read/write to data stores in your architecture, helping your teams understand how your services interact with data in your architecture. You can read more about how to add data stores to services here.

Rather than create a new data resource directly, we choose to call these containers.

This follows the C4 naming convention for containers (not docker containers!) in your architecture. To learn more about containers you can read the c4 model.

For now we only use the data store from c4 model.

---

## Understanding services

**URL:** https://www.eventcatalog.dev/docs/development/guides/services/introduction

**Contents:**
- Understanding services

In EventCatalog services represent systems that produce or receive messages. These messages can be commands, events or queries.

Services can have specifications (OpenAPI, AsyncAPI, GraphQL) attached to them.

Services can be part of a domain, subdomain or independent.

If your building microservices, think of a service as a microservice, or if you are building monolith applications, think of a service as that application. The term service is loosely defined by EventCatalog as flexible to what you need.

---

## Understanding events

**URL:** https://www.eventcatalog.dev/docs/development/guides/messages/events/introduction

**Contents:**
- Understanding events
  - Example of an event​
  - Events in EventCatalog​

Events are a type of message that represent immutable facts.

In EventCatalog Services may send (produce) or receive (consume) events in your architecture.

An example of an event would be OrderPlaced event.

---

## Getting started with schemas

**URL:** https://www.eventcatalog.dev/docs/development/guides/schemas/introduction

**Contents:**
- Getting started with schemas
- Why add schemas?​
- Adding schemas to messages​
- Adding specifications to services​

EventCatalog supports any schema or specification format, including (but not limited to):

Schemas are optional, but they add valuable context to your messages and services by making data structures explicit and discoverable.

By adding schemas to your messages and services, you unlock several benefits:

You can attach one or more schemas to any message type:

Get started by following the relevant guide:

In addition to message-level schemas, services can render full API and messaging specifications, including:

Use the guides below to add specifications to your services:

---

## Why EventCatalog?

**URL:** https://www.eventcatalog.dev/docs/development/getting-started/introduction

**Contents:**
- Why EventCatalog?
- What is EventCatalog?​
    - What can EventCatalog do for you?​
- Why we built this​
- Join the community​
- Something missing?​

Many companies adopting event-driven architectures end up in a distributed big ball of mud.

There can be many reasons for this...but one overlooked reason is that teams are not documenting their architectures, they lack standards, governance and discoverability.

Your teams start to ask questions like:

Time is lost hunting through multiple tools to find the answers to these questions.

What if you could answer these questions in minutes?

EventCatalog is designed to help you avoid the chaos, by providing a way to document your architecture, visualize it, and provide tools to help your teams and AI tools to save time and get answers to the questions when they need them.

EventCatalog is a self-hosted open source project to help you bring discoverability to your architecture through documentation, visualization, and design for both humans and AI.

EventCatalog is technology agnostic, you can use it and integrate with any broker, schema format, or stack.

EventCatalog is self-hosted. You own your data and host it wherever you want.

Event-driven architectures start simple but grow complex fast. More services, more events, more teams — and suddenly nobody knows how anything connects.

EventCatalog brings discoverability, documentation, and visualization to EDA — so your architecture stays understandable as it scales.

If you find issues with the documentation or have suggestions on how to improve the documentation or the project in general, please file an issue for us.

---

## Understanding domains

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/introduction

**Contents:**
- Understanding domains

Domain-Driven Design (DDD) is a software development approach that focuses on deeply understanding and accurately modelling the business domain. This methodology aims to enhance software quality by ensuring it aligns closely with the business requirements it supports. Eric Evans introduced DDD to the software development community in 2003 through his influential book, Domain-Driven Design: Tackling Complexity in the Heart of Software.

The essence of domain-driven design lies in managing complexity by centering software development around the ‘domain,’ which is the specific business context where the software is used. DDD promotes the use of a ubiquitous language, a shared vocabulary between developers and business stakeholders. This common language is used throughout the design and implementation process, ensuring that the software accurately represents the business domain it is designed to serve.

Domain-driven design has some core building blocks including entities, value objects, bounded context and aggregates.

EventCatalog uses domains as a way to group services into a bounded context.

Using domains in EventCatalog gives you a better way to manage your services and define their bounded context.

---

## MCP server

**URL:** https://www.eventcatalog.dev/docs/development/ask-your-architecture/mcp-server/introduction

**Contents:**
- MCP server

Every EventCatalog instance automatically includes a Model Context Protocol (MCP) server.

---

## Installation

**URL:** https://www.eventcatalog.dev/docs/development/getting-started/installation

**Contents:**
- Installation
  - System Requirements​
  - Create with the CLI​
  - Start the dev server​
- Next steps​

Create a new EventCatalog and run it locally.

The quickest way to create a new EventCatalog is using create-eventcatalog, which sets up everything automatically for you. To create a project, run:

This creates a my-catalog directory with everything you need.

Once the project is created, navigate to the project directory and start the development server.

Open http://localhost:3000 to see your catalog.

**Examples:**

Example 1 (bash):
```bash
npx @eventcatalog/create-eventcatalog@latest my-catalog
```

Example 2 (bash):
```bash
cd my-catalognpm run dev
```

---

## Introduction

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-documentation/introduction

**Contents:**
- Introduction
  - How custom documentation can help​
  - What can I do with custom documentation in EventCatalog?​
  - Roadmap for custom documentation​

EventCatalog provides the ability to add any custom documentation to your catalog.

This can be a great way to extend your catalog beyond what is provided, and bring your own documentation to EventCatalog, rather than having documentation spread across multiple tools.

Custom documentation is not limited, here are some examples of what you can do:

It's really up to you what you add here.

EventCatalog provides the ability to document your architecture with domains, services and messages.

Users still have third party tools to document other parts of their architecture (e.g confluence, Google docs, etc), so this is an option to help you keep all your documentation in one place.

You can add any custom documentation to your catalog, this also gives you access to the EventCatalog components. Your custom documentation is powered by markdown, meaning you can use EventCatalog components within your documentation.

This is the initial version of custom documentation in EventCatalog.

We plan to add the following features:

---

## Introduction

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-components/introduction

**Contents:**
- Introduction
  - Why create components?​

EventCatalog provides the ability to add custom components to your domains, services and messages within your catalog. These features include:

Components are a great way to customize your EventCatalog and write shared snippets of code or content you can reuse across your EventCatalog.

Components can be either markdown files (component.mdx) or astro files (component.astro).

Custom components are powered by Astro Components. Read the Astro documentation to learn more about what you can include in your components. Custom components can be very powerful and allow some great customization.

---

## Understanding channels

**URL:** https://www.eventcatalog.dev/docs/development/guides/channels/introduction

**Contents:**
- Understanding channels
  - Example of a channels are visualized in EventCatalog​
  - Routing messages through multiple channels​
  - Supported Channel Protocols​

In EventCatalog a channel represents the organization and transmission of messages.

Channels in EventCatalog describe how a messages transport between producers and consumers. You can use the channels resource to help your team understand how your messages are transported.

Channels are resources in EventCatalog that you can define in a /channels directory. The channel directory can be defined anywhere in your EventCatalog or you can have many channel directories in your EventCatalog.

Here is an example of the Orders Service publishing an event Order amended over a Kafka channel.

In some cases you may want to model how messages are routed through multiple channels, you can do this using channel routes.

In the example below:

This is just an example, but a channel can be any protocol you like. For example if you are using Kafka then this channel could be a Kafka topic. Or if you are using an Event Bus this channel could be your bus, queue or topic.

You can model as many channels as you like, and you can route messages through multiple channels.

EventCatalog is technology agnostic, so can work with any protocol.

Using channels you can define the protocol used, this can be one or many protocols.

Here is a list of protocols that are supported by EventCatalog (with icons)

If you are using a protocol that is not on this list, please raise on issue on GitHub so we can get the icon supported.

---

## Understanding commands

**URL:** https://www.eventcatalog.dev/docs/development/guides/messages/commands/introduction

**Contents:**
- Understanding commands
  - Example of a command​
  - Commands in EventCatalog​

Commands are messages that represent intent, commands can be rejected in distributed systems.

In EventCatalog Services may invoke (send) or accept (receive) commands in your architecture.

An example of a command would be PlaceOrder message over HTTP.

---

## Understanding changelogs

**URL:** https://www.eventcatalog.dev/docs/development/guides/changelogs/introduction

**Contents:**
- Understanding changelogs
  - Features​
    - Example​

In your architecture, various resources like domains, services, schemas, and boundaries are constantly evolving. Unfortunately, the context or reason behind these changes often gets lost.

EventCatalog changelogs allow you to capture these changes and help your team understand the history of your architecture.

You can see a changelog example here.

---

## Authentication Guide

**URL:** https://www.eventcatalog.dev/docs/development/authentication/introduction

**Contents:**
- Authentication Guide
- How it works​
- Authentication by Plan​
    - Scale Plan​
    - Enterprise Plan​
- Why EventCatalog Authentication?​
- Getting Started​
- Next steps​

EventCatalog provides secure authentication to control access to your event-driven architecture documentation. Whether you're a small team getting started or a large enterprise with complex identity requirements, EventCatalog's flexible authentication system grows with your needs.

EventCatalog uses industry-standard OpenID Connect (OIDC) and OAuth 2.0 protocols to integrate with your identity provider. Here's the authentication flow:

EventCatalog runs in SSR mode to handle authentication sessions and uses Auth.js to manage the authentication flow securely.

EventCatalog Authentication is a paid feature available in Scale and Enterprise plans.

Perfect for growing teams that need secure collaboration with popular business providers:

Designed for large organizations with dedicated identity management systems:

Ready to secure your EventCatalog with authentication?

New to EventCatalog? Start your 14-day free trial at EventCatalog.cloud to explore all authentication features.

Ready to get started? Let's enable authentication in your EventCatalog project:

→ Enabling Authentication

Questions? Join our Discord community for support and guidance.

---

## Understanding queries

**URL:** https://www.eventcatalog.dev/docs/development/guides/messages/queries/introduction

**Contents:**
- Understanding queries
  - Queries in EventCatalog​

Queries are a type of message that represent requests for information.

In EventCatalog Services may query (send) or accept (receive) queries in your architecture.

---
