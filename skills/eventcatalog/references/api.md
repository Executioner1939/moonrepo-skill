# Eventcatalog - Api

**Pages:** 21

---

## Code blocks

**URL:** https://www.eventcatalog.dev/docs/api/code-blocks

**Contents:**
- Code blocks
- Examples of code blocks​
  - Diff code blocks​
  - Word highlighting​
  - Labels to line markers​
  - Frames​

EventCatalog is powered by markdown files, this allows you to add custom code blocks.

EventCatalog is using expressive-code which provides a range of additional features for your code blocks.

Highlight diffs with your code, could be useful for your Schemas or any changes you want to show to your teams.

See https://expressive-code.com/key-features/text-markers/#using-diff-like-syntax

If you want to highlight words in your code blocks you can use this feature.

See https://expressive-code.com/key-features/text-markers/#marking-individual-text-inside-lines

Great way to give context to changes in your code. For example if your Schema has changed, then maybe use this to give context with additional labels.

See https://expressive-code.com/key-features/text-markers/#adding-labels-to-line-markers

Nice UI for your code blocks.

See https://expressive-code.com/key-features/frames/

---

## Service frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/service-api

**Contents:**
- Service frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
- Optional fields​
  - summary​
  - owners​
  - sends​

Services are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of the service frontmatter you will find in your /services folder.

Unqiue id of the service. EventCatalog uses this for references and slugs.

Name of the service this is used to display the name on the UI.

Version of the service.

Short summary of your service, shown on service summary pages.

An array of user ids that own the service.

An array of messages (ids) the service sends. These can be commands, queries or events ids.

An array of messages (ids) the service receives. These can be commands, queries or events ids.

An array of data stores ids that the service writes to.

An array of data stores ids that the service reads from.

An array of entities ids that belong to the this service. Which entities belong to this service.

An array of flows ids that are associated with this service.

An array of badges that get rendered on the page.

You can assign one or more specifications to a service.

Older versions of EventCatalog (< 2.39.0)

If you are using an older version of EventCatalog you will need to use the following syntax.

Turn off the visualiser for this resource. This means the resource will not be included in the visualiser or the navigation bar for the visualiser.

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your service, used for slugs and references in EventCatalog.id: Orders# Display name of the Service, rendered in EventCatalogname: Orders# Version of the Serviceversion: 0.0.1# Short summary of your Servicesummary: |  Service that contains order related information# Optional owners, references teams or usersowners:    - dboyne# Optional messages this service receives and it's versionreceives:  - id: InventoryAdjusted    version: 0.0.3# Optional messages this service sends and it's versionsends:  - id: AddInventory    version: 0.0.3# Optional flows associated with this serviceflows:  - id: OrderProcessing    version: 1.0.0# Optional details about the programming language and url for the coderepository:  language: JavaScript  url: https://github.com/event-catalog/pretend-shipping-service# Optional badges, rendered to UI by EventCatalogbadges:    - content: New service      backgroundColor: blue      textColor: blue      # Optional icon to display (from https://heroicons.com/)      # Or the name of the broker (e.g Kafka, EventBridge, etc)      icon: BoltIcon---## OverviewThis orders service gives API consumers the ability to produce orders in the systems. Events are raised from this system for downstream consumption.<NodeGraph />
```

Example 2 (yaml):
```yaml
---  id: Orders---
```

Example 3 (yaml):
```yaml
---  name: My orders service---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## Channel frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/channel-api

**Contents:**
- Channel frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
- Optional fields​
  - summary​
  - address​
  - protocols​

Channels are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of the channel frontmatter you will find in your /channels folder.

Unqiue id of the channel. EventCatalog uses this for references and slugs.

Name of the channel this is used to display the name on the UI.

Version of the channel.

Short summary of your channel.

Address of the channel.

Protocol/s of the channel.

Parameters for your channel.

An array of user ids that own the channel.

An array of badges that get rendered on the page.

Repository language and code url for the channel.

Override the default edit url for the page. This is used to navigate the user to the edit page for the page (e.g GitHub, GitLab url).

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your channel, used for slugs and references in EventCatalog.id: inventory.{env}.events# Display name of the channel, rendered in EventCatalogname: Inventory Events Channel# Version of the channelversion: 1.0.0# Short summary of your channelsummary: |  Central event stream for all inventory-related events including stock updates, allocations, and adjustments# Optional owners, references teams or usersowners:  - dboyne# address of the channel# supports parameters in the address  address: inventory.{env}.events# list of protocols for the channel# see https://eventcatalog.dev/docs/development/guides/channels/introduction#protocolsprotocols:   - kafka# Optional list of parameters for the channel# This example shows the `env` value in the channel name can be `dev, stg, prod`.parameters:  env:    enum:      - dev      - stg      - prod    description: 'Environment to use'---### OverviewThe Inventory Events channel is the central stream for all inventory-related events across the system. This includes stock level changes, inventory allocations, adjustments, and stocktake events. Events for a specific SKU are guaranteed to be processed in sequence when using productId as the partition key.<ChannelInformation />
```

Example 2 (yaml):
```yaml
---  id: inventory.{env}.events---
```

Example 3 (yaml):
```yaml
---  name: Inventory events---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## Configuration

**URL:** https://www.eventcatalog.dev/docs/development/ask-your-architecture/eventcatalog-assistant/configuration

**Contents:**
- Configuration
  - Enabling the feature​
  - Installing your model and configuring eventcatalog.chat.js file​
    - Configuring eventcatalog.chat.js​

EventCatalog Assistant is turned off by default.

To enable the assistant feature, you need to set the following:

To turn on the assistant feature, you need to set the following:

First you have to install your model of choice (list of models) and configure the relevant secrets in your .env file.

Example of installing the OpenAI model:

This file will provide the model and any model configuration to EventCatalog.

In the example below we are using the OpenAI model gpt-4.1-nano and configuring the model with some additional parameters.

Once you have enabled the feature and configured your model, restart EventCatalog and you can start asking questions about your architecture.

**Examples:**

Example 1 (css):
```css
module.exports = {  // Enable the chat feature in your catalog  chat: {    enabled: true,  },  // AI integrations require you to run eventcatalog as as server  output: 'server'};
```

Example 2 (php):
```php
<!-- in the root of your project -->npm install @ai-sdk/openai
```

Example 3 (javascript):
```javascript
import { openai } from '@ai-sdk/openai';// Export your model using the default exportexport default async () => {    return openai('gpt-4.1-nano');}// Export the configuration for the model (optional)export const configuration = {    topP: 0.9,    topK: 40,    frequencyPenalty: 0.0,    presencePenalty: 0.0,    temperature: 0.7,    maxTokens: 10000,}
```

---

## Configure RSS feeds

**URL:** https://www.eventcatalog.dev/docs/development/configuration/rss-feed

**Contents:**
- Configure RSS feeds
- How to enable RSS feeds​
  - Messages​
  - Services and Domains​
  - Flows​
  - Everything​

EventCatalog supports RSS feeds for your messages, services, domains and flows.

RSS feeds are disabled by default.

To enable RSS feeds, you need to add the rss property to the eventcatalog.config.js file.

Items returned from the RSS feed are ordered by the last updated date of the file.

When you enable the RSS feed you will have RRS feeds at the following paths:

Returns the latest messages that have changed in your Catalog.

Returns the latest services and domains that have changed in your Catalog.

Returns the latest flows that have changed in your Catalog.

Returns the latest items that have changed in your Catalog.

**Examples:**

Example 1 (json):
```json
//.. rest of filerss: {  // Turn rss on or off  enabled: true,  // The number of items to return in each feed (default 15)  limit: 20},
```

---

## Adding OpenAPI specifications

**URL:** https://www.eventcatalog.dev/docs/development/guides/services/adding-to-services/openapi

**Contents:**
- Adding OpenAPI specifications
- Adding OpenAPI files to EventCatalog​
- Reference the OpenAPI file from a remote URL​
- Multiple OpenAPI Files​

Services in EventCatalog allow you to render OpenAPI specifications (see demo).

You have two options for adding OpenAPI specifications to your service:

Did you know you can automate your documentation, visualizations and owners using your OpenAPI Files?

We have a OpenAPI plugin that can generate your catalog from your OpenAPI files, transforming your operations into commands, queries and events. You can assign these to services and domains and much more...

This option is useful if you want to keep your OpenAPI files in your EventCatalog.

To add an OpenAPI file to your service you will need to include the file itself inside the service directory.

Then you need to reference the file in the service frontmatter.

This can be useful if you want to keep your OpenAPI files in a remote repository and render them in EventCatalog.

The pages will be built at build time, so the URL needs to be accessible by the build machine.

If your specifications changes you need to rebuild your EventCatalog as the pages are built at build time.

If your service exposes multiple APIs or versions of the same API, you can assign multiple OpenAPI files to a single service.

This will render a list of specification files on your service page and navigation bar.

**Examples:**

Example 1 (yaml):
```yaml
---  specifications:    - type: openapi      # Path to the OpenAPI file relative to the service directory      path: openapi.yml      # Friendly name for the specification      name: OpenAPI Specification---
```

Example 2 (sql):
```sql
---  specifications:    - type: openapi      # Path to the OpenAPI file from a remote URL (accessible by the build machine)      path: https://raw.githubusercontent.com/event-catalog/generator-openapi/refs/heads/main/examples/product-api/openapi.yml      # Friendly name for the specification      name: Product API---
```

Example 3 (yaml):
```yaml
---  specifications:    - type: openapi      path: openapi-v1.yml      name: v1    - type: openapi      path: openapi-v2.yml      name: v2---
```

---

## <OpenAPI />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/openapi

**Contents:**
- <OpenAPI />

This component is now deprecated. Please read the frontmatter API documentation here.

You can add specifications to any service in EventCatalog using the specifications frontmatter API. You can read more about it here.

If you are interested in automating your EventCatalog with OpenAPI files, you can use the OpenAPI plugin.

---

## Query frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/query-api

**Contents:**
- Query frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
- Optional fields​
  - summary​
  - owners​
  - badges​

Queries are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of the query frontmatter you will find in your /queries folder.

Unqiue id of the query. EventCatalog uses this for references and slugs.

Name of the query this is used to display the name on the UI.

Version of the query.

Short summary of your query, shown on query summary pages.

An array of user ids that own the query.

An array of badges that get rendered on the page.

Specifications to include on the page

Current supports AsyncAPI and OpenAPI files. When including the specifications the page will render badges and buttons for the specifications.

You can assign one or more specifications to a query.

Older versions of EventCatalog (< 2.39.0)

If you are using an older version of EventCatalog you will need to use the following syntax.

Repository language and code url for the query.

Configure the event label and message in the docs sidebar.

Turn off the visualiser for this resource. This means the resource will not be included in the visualiser or the navigation bar for the visualiser.

Mark the query as a draft. This will show the query as a draft in the UI.

You can also specify a title and summary for your draft to help you communicate the status of the draft.

Override the default edit url for the page. This is used to navigate the user to the edit page for the page (e.g GitHub, GitLab url).

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your query, used for slugs and references in EventCatalog.id: GetOrder# Display name of the query, rendered in EventCatalogname: Out of stock# Version of the queryversion: 0.0.3# Short summary of your querysummary: |  Query that is raised when an inventory item goes out of stock.# Optional owners, references teams or usersowners:    - dboynerepository:  language: JavaScript  url: https://github.com/event-catalog/pretend-shipping-service# Optional badges, rendered to UI by EventCatalogbadges:    - content: New query      backgroundColor: blue      textColor: blue---## OverviewQuery is published when the inventory is out of stock.<NodeGraph />
```

Example 2 (yaml):
```yaml
---  id: GetOrder---
```

Example 3 (yaml):
```yaml
---  name: Out of stock---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## Data frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/data-api

**Contents:**
- Data frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
  - container_type​
- Optional fields​
  - summary​
  - technology​

Data stores are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of of a basic data store.

Unique id of the data store. EventCatalog uses this for references and slugs.

Name of the data store this is used to display the name on the UI.

Version of the data store.

Type of the data store.

Options: database, cache, objectStore, searchIndex, dataWarehouse, dataLake, other

Short summary of your data store, shown on data store summary pages.

Technology of the data store.

Classification of the data store.

Options: internal, external, confidential, regulated

Retention of the data store.

Residency of the data store.

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (php):
```php
---# id of your data store, used for slugs and references in EventCatalog.id: orders-db# Display name of the data store, rendered in EventCatalog.name: Orders DB# Version of the data storeversion: 1.0.0# Type of the data store (e.g. database, cache, objectStore, searchIndex)container_type: database# Technology of the data store (e.g. postgres@14, redis@7, etc)technology: postgres@14# Classification of the data store (e.g. internal, external, etc)classification: internal# Retention of the data store (e.g. 7y, 10y, etc)retention: 7y# Residency of the data store (e.g. eu-west-1, us-east-1, etc)residency: eu-west-1# Badges to displaybadges:  - content: "Core Data Store"    backgroundColor: "blue"    textColor: "white"---The orders database is a core data store for the orders domain.<!-- Add any markdown you want, the data store will render in its own page /docs/containers/{Data Store}/{version} -->
```

Example 2 (yaml):
```yaml
---  id: orders-db---
```

Example 3 (yaml):
```yaml
---  name: Orders DB---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## EventCatalog CLI

**URL:** https://www.eventcatalog.dev/docs/api/overview

**Contents:**
- EventCatalog CLI
- EventCatalog CLI commands​
  - eventcatalog dev​
  - eventcatalog start/preview​
  - eventcatalog build​

EventCatalog provides a set of scripts to help you generate, serve, and deploy your catalog.

Once your catalog is bootstrapped, the source will contain the EventCatalog scripts that you can invoke with your package manager:

Below is a list of EventCatalog CLI commands and their usages:

Runs your catalog in development mode.

This will start the dev server and watch for changes to your catalog. You will use this as you develop your catalog.

Runs EventCatalog in production mode, requires a build first. This will serve the built catalog from the dist folder.

Can be used to preview your catalog before deploying.

Builds your catalog for production, and outputs the catalog to the dist folder.

**Examples:**

Example 1 (json):
```json
{  // ...  "scripts": {    // Runs the dev server locally    "dev": "eventcatalog dev",    // Builds the catalog    "build": "eventcatalog build",    // start/preview both run the built catalog locally.    "start": "eventcatalog start",    "preview": "eventcatalog preview",  }}
```

---

## Customize tables

**URL:** https://www.eventcatalog.dev/docs/development/customization/customize-tables

**Contents:**
- Customize tables
  - How to customize tables​
  - Configuration​

EventCatalog allows you to customize the columns and names on the Explore page, Teams and Users pages.

You can customize the tables in EventCatalog by configuring them in your eventcatalog.config.js file.

Example of how to customize the tables for the events table page:

List of available configuration options for the table columns:

The key property is either events, queries, commands.

In this example we set the events table configuration.

You can read the eventcatalog.config.js API reference for more information on the table configuration.

**Examples:**

Example 1 (css):
```css
events: {  tableConfiguration: {    columns: {      name: { visible: true, label: 'Name' },      summary: { visible: true, label: 'Summary' },      producers: { visible: true, label: 'Producers' },      consumers: { visible: true, label: 'Consumers' },      badges: { visible: true, label: 'Badges' },      actions: { visible: true, label: 'Actions' },    }  },},
```

Example 2 (css):
```css
// ... other configuration ...// change property to `events`, `queries`, `commands`events: {  tableConfiguration: {    columns: {      name: { visible: true, label: 'Name' },      summary: { visible: true, label: 'Summary' },      producers: { visible: true, label: 'Producers' },      consumers: { visible: true, label: 'Consumers' },      badges: { visible: true, label: 'Badges' },      actions: { visible: true, label: 'Actions' },    },  },}// ... other configuration ...
```

Example 3 (css):
```css
// ... other configuration ...services: {  tableConfiguration: {    columns: {      name: { visible: true, label: 'Name' },      summary: { visible: true, label: 'Summary' },      receives: { visible: true, label: 'Receives' },      sends: { visible: true, label: 'Sends' },      badges: { visible: true, label: 'Badges' },      actions: { visible: true, label: 'Actions' },    }  },}// ... other configuration ...
```

Example 4 (css):
```css
// ... other configuration ...domains: {  tableConfiguration: {    columns: {      name: { visible: true, label: 'Name' },      summary: { visible: true, label: 'Summary' },      services: { visible: true, label: 'Owners' },      badges: { visible: true, label: 'Badges' },      actions: { visible: true, label: 'Actions' },    }  },}// ... other configuration ...
```

---

## Domain frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/domain-api

**Contents:**
- Domain frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
- Optional fields​
  - summary​
  - owners​
  - services​

Domains are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of the domain frontmatter you will find in your domain files.

Unqiue id of the domain. EventCatalog uses this for references and slugs.

Name of the domain this is used to display the name on the UI.

Version of the domain.

Short summary of your domain, shown on domain summary pages.

An array of user ids that own the domain.

An array of services ids that belong to the this domain. Which services belong to this domains bounded context.

An array of entities ids that belong to the this domain. Which entities belong to this domains bounded context.

An array of flows ids that are associated with this domain.

An array of badges that get rendered on the page.

Specifications to include on the page

You can assign one or more specifications to a domain.

Older versions of EventCatalog (< 2.39.0)

If you are using an older version of EventCatalog you will need to use the following syntax.

Turn off the visualiser for this resource. This means the resource will not be included in the visualiser or the navigation bar for the visualiser.

Override the default edit url for the page. This is used to navigate the user to the edit page for the page (e.g GitHub, GitLab url).

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your domain, used for slugs and references in EventCatalog.id: Orders# Display name of the domain, rendered in EventCatalogname: Orders# Version of the domainversion: 0.0.1# Short summary of your domainsummary: |  Domain that contains order related information# Optional owners, references teams or usersowners:    - dboyne# Optional services. Groups services into this domain.services:    - id: PaymentService      version: 0.0.1# Optional flows associated with this domainflows:    - id: OrderProcessing      version: 1.0.0# Optional badges, rendered to UI by EventCatalogbadges:    - content: New domain      backgroundColor: blue      textColor: blue      # Optional icon to display (from https://heroicons.com/)      # Or the name of the broker (e.g Kafka, EventBridge, etc)      icon: BoltIcon---## OverviewDomain that contains all services that are related to the orders domain within FakeCompany.<NodeGraph />
```

Example 2 (yaml):
```yaml
---  id: Orders---
```

Example 3 (yaml):
```yaml
---  name: My orders domain---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## Command frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/command-api

**Contents:**
- Command frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
- Optional fields​
  - summary​
  - owners​
  - badges​

Commands are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of the command frontmatter you will find in your /commands folder.

Unqiue id of the command. EventCatalog uses this for references and slugs.

Name of the command this is used to display the name on the UI.

Version of the command.

Short summary of your command, shown on command summary pages.

An array of user ids that own the command.

An array of badges that get rendered on the page.

You can assign one or more specifications to a command.

Older versions of EventCatalog (< 2.39.0)

If you are using an older version of EventCatalog you will need to use the following syntax.

Repository language and code url for the command.

Configure the event label and message in the docs sidebar.

Turn off the visualiser for this resource. This means the resource will not be included in the visualiser or the navigation bar for the visualiser.

Mark the command as a draft. This will show the command as a draft in the UI.

You can also specify a title and summary for your draft to help you communicate the status of the draft.

Override the default edit url for the page. This is used to navigate the user to the edit page for the page (e.g GitHub, GitLab url).

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your command, used for slugs and references in EventCatalog.id: UpdateInventory# Display name of the command, rendered in EventCatalogname: Update inventory# Version of the commandversion: 0.0.3# Short summary of your commandsummary: |  Command with the intent to update the inventory# Optional owners, references teams or usersowners:    - dboyne# Optional details about the programming language and url for the coderepository:  language: JavaScript  url: https://github.com/event-catalog/pretend-shipping-service# Optional badges, rendered to UI by EventCatalogbadges:    - content: New service      backgroundColor: blue      textColor: blue      # Optional icon to display (from https://heroicons.com/)      icon: BoltIcon---## OverviewThe `Update Inventory` command represents intent to update the inventory of a given item over HTTP.<NodeGraph />
```

Example 2 (yaml):
```yaml
---  id: UpdateInventory---
```

Example 3 (sql):
```sql
---  name: Update Inventory---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## Entity frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/entity-api

**Contents:**
- Entity frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
- Optional fields​
  - summary​
  - aggregateRoot​
  - identifier​

Entities are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of of a basic entity.

Unique id of the entity. EventCatalog uses this for references and slugs.

Name of the entity this is used to display the name on the UI.

Version of the entity.

Short summary of your entity, shown on entity summary pages.

Indicates whether this entity is an aggregate root in Domain-Driven Design terms.

The unique identifier property for this entity.

List of properties that define the structure of the entity.

Each property can have the following fields:

An array of badges that get rendered on the page.

Override the default edit url for the page. This is used to navigate the user to the edit page for the page (e.g GitHub, GitLab url).

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (typescript):
```typescript
---# id of the entityid: "User"# Display name of the entity, rendered in EventCatalogname: "User"# version for your entity version: "1.0.0"# Short summary of your entitysummary: "Represents a user in the system"# Whether this entity is an aggregate rootaggregateRoot: true# The unique identifier for this entityidentifier: "userId"# Properties of the entityproperties:  - name: "userId"    type: "string"    required: true    description: "Unique identifier for the user"  - name: "email"    type: "string"    required: true    description: "User's email address"  - name: "firstName"    type: "string"    required: true    description: "User's first name"  - name: "lastName"    type: "string"    required: true    description: "User's last name"  - name: "dateOfBirth"    type: "date"    required: false    description: "User's date of birth"  - name: "profileId"    type: "string"    required: false    description: "Reference to user's profile"    references: "Profile"    referencesIdentifier: "profileId"    relationType: "one-to-one"# Badges to displaybadges:  - content: "Core Entity"    backgroundColor: "blue"    textColor: "white"---The User entity represents a user in our system and serves as an aggregate root for user-related operations.This entity contains core user information and is referenced by multiple services across the platform.<!-- Add any markdown you want, the entity will render in its own page /docs/entities/{Entity}/{version} -->
```

Example 2 (yaml):
```yaml
---  id: User---
```

Example 3 (yaml):
```yaml
---  name: User---
```

Example 4 (json):
```json
---  version: 1.0.0---
```

---

## Configuration

**URL:** https://www.eventcatalog.dev/docs/development/configuration

**Contents:**
- Configuration
- eventcatalog.config.js​
- Configuring environment variables​
  - Configuring EventCatalog Linter​

EventCatalog is a flexible, technology agnostic, unopinionated documentation tool.

EventCatalog focuses on documenting your architecture primitives, and letting you add the technical or implementation details as needed.

If you have complex CI/CD requirements, or various different workflows patterns in your organization and teams, EventCatalog is flexible to your needs.

You can configure EventCatalog using the eventcatalog.config.js file.

The eventcatalog.config.js file is the heart of your application. It allows you to define overrides for EventCatalog.

See the API documentation to override defaults for EventCatalog.

Some features in EventCatalog require environment variables to be set.

If you need to set environment variables, you can do so in your .env file.

When EventCatalog is running or builds it will load the environment variables from your .env file.

EventCatalog has a linter that can be used to validate your EventCatalog documentation.

You can read more about the EventCatalog Linter in the EventCatalog Linter documentation.

**Examples:**

Example 1 (unknown):
```unknown
EVENTCATALOG_SCALE_LICENSE_KEY=your-api-key
```

---

## eventcatalog.config.js

**URL:** https://www.eventcatalog.dev/docs/api/config

**Contents:**
- eventcatalog.config.js
- Overview​
- Required fields​
  - cId​
  - title​
  - organizationName​
- Optional fields​
  - base​
  - output​
  - outDir​

eventcatalog.config.js contains configurations for your site and is placed in the root directory of your site.

An automated generated ID for your catalog. EventCatalog will generate this for you.

Title for your website.

Your organization name.

The base path to deploy to. EventCatalog will use this path as the root for your pages and assets both in development and in production build.

The output type for your EventCatalog, choose from static or server.

The output path of your EventCatalog. By default it will output to the dist folder.

Set the route matching behavior of the dev server. Choose from the following options:

'true' - Only match URLs that include a trailing slash (ex: “/foo/“) 'false' - Match URLs regardless of whether a trailing ”/” exists

Use this configuration option if your production host has strict handling of how trailing slashes work or do not work.

Configure the port EventCatalog is running on.

Set which network IP addresses the dev server should listen on (i.e. non-localhost IPs).

A list of hostnames that Astro is allowed to respond to. When the value is set to true, any hostname is allowed.

You can read more on the Astro documentation here.

Generators are the foundation of plugins with EventCatalog. EventCatalog will call your generators on build.

Optional configuration for EventCatalog environments.

When environments are set, a dropdown will be shown in the top right of the EventCatalog allowing your users to switch between environments.

Configure the landing page URL your EventCatalog loads. By default EventCatalog loads / (the default or custom landing page).

Clicking on the EventCatalog logo (or your custom logo), will also go to this URL.

If you set this value the Home icon in the vertical navigation will not be shown and your users will be redirected to this default URL.

You can set this to any EventCatalog page URL.

Configure the application sidebar in EventCatalog.

Show/hide items in the sidebar, see list of options.

Configuration for the EventCatalog visualiser.

Configure the documentation sidebar in EventCatalog.

Configuration for the documentation sidebar.

You can choose between LIST_VIEW or TREE_VIEW to render your documentation.

Any messages that do not belong to a service will be shown as orphaned messages in the sidebar (LIST_VIEW only).

If you wish to hide orphaned messages you can set the showOrphanedMessages to false.

Configuration for EventCatalog Changelog.

Changelogs are disabled by default.

You can enable changelogs by setting enabled to true.

URL used when people want to edit the documentation. For example your GitHub repo and branch.

For Stater or Scale plans. This gives you the ability to show your own GitHub repository in EventCatalog (in the header bar).

URL to your repository for EventCatalog.

Logo, alt and text for your company logo.

Add your logo to your /public directory.

URL used when people want to link the logo & title in the top navigation to the homepage of a website.

This is an optional configuration setting to optimize the MDX output for faster builds. This may be useful if you have many catalog files and notice slow builds. However, this option may generate some unescaped HTML, so make sure your catalog interactive parts still work correctly after enabling it.

This is disabled by default.

Read Astro documentation on optimize for MDX for more information.

Setting this to true will automatically compress all your CSS, HTML, SVG, JavaScript, JSON and image files in the Astro outDir folder.

This is disabled by default from EventCatalog v2.61.9.

This only works for static builds.

EventCatalog will render your AsyncAPI files into their own pages. By default EventCatalog will read your AsyncAPI files and parse your schemas to render them on the screen. Part of this process is validating your schemas and also adding metadata onto them (default).

If you want to keep your schemas as they are then you can set the asyncAPI.renderParsedSchemas to false.

If you are having issues seeing or rendering your AsyncAPI file try setting the renderParsedSchemas to false

EventCatalog uses mermaid to render diagrams.

Using mermaid you can render icons in your diagrams (e.g AWS architecture icons).

You can choose from over 200,000 icons from icones.js.org.

Enable RSS feeds for messages, services, domains and flows.

RSS feeds are disabled by default.

See the RSS documentation for more information and examples.

Enable tools like Claude, ChatGPT, GitHub Copilot, and Cursor to quickly understand your EventCatalog.

See the LLMs documentation for more information, how you can use it and examples.

Enables the ability to get the full catalog dump in the /api/catalog endpoint.

This is enabled by default.

Configuration for the domains table.

See the Customize tables documentation for more information and examples.

Configuration for the events table.

See the Customize tables documentation for more information and examples.

Configuration for the queries table.

Configuration for the commands table.

See the Customize tables documentation for more information and examples.

Configuration for the services table.

See the Customize tables documentation for more information and examples.

Configuration for the containers table.

See the Customize tables documentation for more information and examples.

Configuration for the flows table.

See the Customize tables documentation for more information and examples.

Configuration for the users table.

See the Customize tables documentation for more information and examples.

Configuration for the teams table.

See the Customize tables documentation for more information and examples.

**Examples:**

Example 1 (css):
```css
module.exports = {  cId: '107fdebb-7c68-42cc-975d-413b1d30d758',};
```

Example 2 (css):
```css
module.exports = {  title: 'EventCatalog',};
```

Example 3 (css):
```css
module.exports = {  organizationName: 'Your Company',};
```

Example 4 (css):
```css
module.exports = {  base: '/',};
```

---

## Flow frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/flow-api

**Contents:**
- Flow frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
  - steps​
    - Actor Nodes  ​
    - External Services Nodes​
    - Message Nodes​

Flows are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of of a basic flow.

Unqiue id of the flow. EventCatalog uses this for references and slugs.

Name of the flow this is used to display the name on the UI.

List of steps for your flow.

Flows allow you to create Actor nodes. Actors represent A person who executes a command or flow.

Flows allow you to create External Service. These services tend to be other external services you may interact with that are not part of your business domain. (e.g Stripe API)

See example of Actor node in a workflow.

Flows allow you to create message nodes. Messages link to your commands or events.

See example of Message node in a workflow.

Flows allow you to create service nodes. Services link to your defined services in EventCatalog.

See example of Message node in a workflow.

Short summary of your flow, shown on flow summary pages.

An array of badges that get rendered on the page.

Override the default edit url for the page. This is used to navigate the user to the edit page for the page (e.g GitHub, GitLab url).

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---# id of the flowid: "CancelSubscriptionFlow"# Display name of the flow, rendered in EventCatalogname: "User Cancels Subscription"# version for your flow version: "0.0.1"# Short summary of your eventsummary: "Flow for when a user has cancelled a subscription"# A list of steps for your flowsteps:    # id of your step, required for linking between stages in your flow  - id: "cancel_subscription_initiated"    # rendered title of your step    title: "Cancels Subscription"    # Short summary of a step    summary: "User cancels their subscription"    # Defining an actor will render an actor node in the graph.    actor:      name: "User"    # What happens next? Define the next step      next_step:       id: "cancel_subscription_request"      label: "Initiate subscription cancellation"  - id: "cancel_subscription_request"    title: "Cancel Subscription"    # This step is a message, include the message and version    message:      id: "CancelSubscription"      version: "0.0.1"    next_step:       id: "subscription_service"      label: "Proceed to subscription service"  - id: "stripe_integration"    title: "Stripe"    # This is an external system (e.g Stripe)    externalSystem:      name: "Stripe"      summary: "3rd party payment system"      url: "https://stripe.com/"    next_step:       id: "subscription_service"      label: "Return to subscription service"  - id: "subscription_service"    title: "Subscription Service"    # This node is a service, include that.    service:      id: "SubscriptionService"      version: "0.0.1"    # Define multiple steps    next_steps:      - id: "stripe_integration"        label: "Cancel subscription via Stripe"      - id: "subscription_cancelled"        label: "Successful cancellation"      - id: "subscription_rejected"        label: "Failed cancellation"  - id: "subscription_cancelled"    title: "Subscription has been Cancelled"    message:      id: "UserSubscriptionCancelled"      version: "0.0.1"    next_step:      id: "notification_service"      label: "Email customer"  - id: "subscription_rejected"    title: "Subscription cancellation has been rejected"  - id: "notification_service"    title: "Notifications Service"    service:      id: "NotificationService"      version: "0.0.2"---This flow documents what happens when a User Cancels Subscription in our system. <NodeGraph /><!-- Add any markdown you want, the workflow will also render in its own page /docs/flows/{Flow}/{version} -->
```

Example 2 (yaml):
```yaml
---  id: InventoryOutOfStock---
```

Example 3 (yaml):
```yaml
---  name: User Cancels Subscription---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## Function: getEventCatalogConfigurationFile()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getEventCatalogConfigurationFile

**Contents:**
- Function: getEventCatalogConfigurationFile()
- Parameters​
- Returns​
  - Returns​

getEventCatalogConfigurationFile(directory): () => Promise<any>

Defined in: eventcatalog.ts:70

Returns the event catalog configuration file. The event catalog configuration file is the file that contains the configuration for the event catalog.

A JSON object with the configuration for the event catalog.

---

## Configuration

**URL:** https://www.eventcatalog.dev/docs/configuration/getting-started

**Contents:**
- Configuration
- 📄️ Configuration overview
- 📄️ Configure RSS feeds

Learn how to configure EventCatalog.

Configure EventCatalog

Configure RSS feeds for EventCatalog

---

## Event frontmatter API

**URL:** https://www.eventcatalog.dev/docs/api/event-api

**Contents:**
- Event frontmatter API
- Overview​
- Required fields​
  - id​
  - name​
  - version​
- Optional fields​
  - summary​
  - owners​
  - badges​

Events are just markdown files, with this comes the use of Content, MDX components and also front-matter.

Here is an example of the event frontmatter you will find in your /events folder.

Unqiue id of the event. EventCatalog uses this for references and slugs.

Name of the event this is used to display the name on the UI.

Version of the event.

Short summary of your event, shown on event summary pages.

An array of user ids that own the event.

An array of badges that get rendered on the page.

You can assign one or more specifications to a event.

Older versions of EventCatalog (< 2.39.0)

If you are using an older version of EventCatalog you will need to use the following syntax.

Repository language and code url for the event.

Configure the event label and message in the docs sidebar.

Turn off the visualiser for this resource. This means the resource will not be included in the visualiser or the navigation bar for the visualiser.

Mark the event as a draft. This will show the event as a draft in the UI.

You can also specify a title and summary for your draft to help you communicate the status of the draft.

Override the default edit url for the page. This is used to navigate the user to the edit page for the page (e.g GitHub, GitLab url).

Override the default details panel for the page. You can use this show/hide areas of the details panel.

An array of attachments for this resource type.

The attachments can be a url (string) or an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your event, used for slugs and references in EventCatalog.id: InventoryOutOfStock# Display name of the event, rendered in EventCatalogname: Out of stock# Version of the eventversion: 0.0.3# Short summary of your eventsummary: |  Event that is raised when an inventory item goes out of stock.# Optional owners, references teams or usersowners:    - dboynerepository:  language: JavaScript  url: https://github.com/event-catalog/pretend-shipping-service# Optional badges, rendered to UI by EventCatalogbadges:    - content: New event      backgroundColor: blue      textColor: blue      # Optional link to display (optional)      link: https://github.com/event-catalog/pretend-shipping-service---## OverviewEvent is published when the inventory is out of stock.<NodeGraph />
```

Example 2 (yaml):
```yaml
---  id: InventoryOutOfStock---
```

Example 3 (yaml):
```yaml
---  name: Out of stock---
```

Example 4 (json):
```json
---  version: 0.0.1---
```

---

## Schema API

**URL:** https://www.eventcatalog.dev/docs/development/guides/schemas/schema-api

**Contents:**
- Schema API
  - Message Schemas​
  - Service Specifications​

Your EventCatalog schemas for your Events, Queries, Commands and Services can be accessed via API (GET requests).

You can find the OpenAPI specification for the Schema API here.

The Message Schemas API allows you to get the schema for a specific event, query or command.

You can also get the latest version of the schema by omitting the version parameter.

The Service Specifications API allows you to get the specification for a specific service.

**Examples:**

Example 1 (unknown):
```unknown
GET /api/schemas/events/{eventId}/{version}GET /api/schemas/queries/{queryId}/{version}GET /api/schemas/commands/{commandId}/{version}
```

Example 2 (unknown):
```unknown
GET /api/schemas/events/{eventId}/latestGET /api/schemas/queries/{queryId}/latestGET /api/schemas/commands/{commandId}/latest
```

Example 3 (unknown):
```unknown
GET /api/schemas/services/{serviceId}/{version}/{type}
```

---
