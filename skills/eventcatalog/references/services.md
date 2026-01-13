# Eventcatalog - Services

**Pages:** 25

---

## Function: getServices()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getServices

**Contents:**
- Function: getServices()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getServices(directory): (options?) => Promise<Service[]>

Defined in: services.ts:78

Returns all services from EventCatalog.

You can optionally specify if you want to get the latest version of the services.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getServices } = utils('/path/to/eventcatalog');// Gets all services (and versions) from the catalogconst services = await getServices();// Gets all services (only latest version) from the catalogconst services = await getServices({ latestOnly: true });
```

---

## schemas.txt

**URL:** https://www.eventcatalog.dev/docs/development/developer-tools/schemas.txt

**Contents:**
- schemas.txt
  - What is schemas.txt?​
  - schemas.txt and schemas-full.txt​
  - How to use schemas.txt?​

Enable tools like Claude, ChatGPT, GitHub Copilot, and Cursor to quickly fetch and understand your EventCatalog schemas.

Message schemas and service specifications can be fetched from your EventCatalog and used in your own applications.

Schemas.txt is very similar to LLMS.txt, but it is specifically for schemas in your EventCatalog.

Schemas.txt supports any schema format for your messages (e.g Avro, Protobuf, JSON Schema etc) and any specification for your services (e.g OpenAPI, AsyncAPI, GraphQL etc).

The schemas.txt file is automatically generated and maintained as part of your documentation pipeline, requiring no manual configuration. It organizes your schemas in a format optimized for machine reading.

The schemas.txt file includes your EventCatalog schemas in a simple format. Lists your schemas with a summary for each of them.

The EventCatalog MCP already uses the schemas.txt file to provide access to your schemas in your MCP clients (e.g Cursor, Windsurf, Claude Desktop etc).

If you want to use schemas.txt in your own application, you can query the urls:

---

## Routing messages through channels

**URL:** https://www.eventcatalog.dev/docs/development/guides/channels/adding-messages-to-services

**Contents:**
- Routing messages through channels
  - Publishing messages to channels​
  - Consuming messages from channels​
  - Channels visualized in EventCatalog​
- Chaining channels​
  - Example of publish/subscribe pattern​
  - Point to point messaging pattern​
  - Looking for previous channel documentation?​
- Adding messages to your channels​
  - Using semver versioning​

Services in EventCatalog can send and receive messages.

When you define this you can also specify how the message is transported using channels.

You do this using the to and from fields in your service frontmatter.

To publish a message through a channel you need to specify the channel in the to field in your service frontmatter.

In this example the OrderService sends an OrderPlaced message to the orders.events channel.

This assumes you have already defined the orders.events channel documentation.

To consume a message from a channel you need to specify the channel in the from field in your service frontmatter.

In this example the PaymentService consumes the OrderPlaced message from the orders.events channel.

When messages get added to your channels EventCatalog will visualize this for you through the visualizer.

You can turn off the channels in the visualizer by using the visualizer settings in the UI.

In some cases you may want to chain channels together. For example you may want to send a message from one channel to another channel before it is consumed by something downstream.

For example you may want to publish an event to a broker, then route/filter events to another channel (e.g Queue, Topic, etc) before it is consumed by something downstream.

This let's you model publish/subscribe patterns or point to point messaging patterns.

To model this, we define the OrdersService to send the OrderPlaced event to the orders.events channel.

Then we define the PaymentService to consume the OrderPlaced event from the orders.events channel.

Then we define the FraudDetectionService to consume the OrderPlaced event from the orders.events channel.

This will model that the OrderServices is publishing onto the broker, with many consumers consuming the event from the same channel.

First we define the OrdersService to publish an event to the orders.events event broker.

Next we define the PaymentService to consume the event from the payment.queue queue.

Next we setup the routing logic between the channels.

Here, we tell the broker (channel) that is can route to the orders.events.filtered topic.

Next, we tell the orders.events.filtered channel it can route to the payment.queue queue.

EventCatalog will understand the channel routes and relationships and create a visual representation of the channels and their relationships.

Find previous channel documentation below. If you are using EventCatalog 2.65.0 or greater you can skip this section.

EventCatalog supports different types of messages (commands, events and queries).

Any message can be added to one or many channels.

To add messages to a channel you first have to define your messages.

Once you define your message you can specify that channel/s it uses.

In the visualizer you can show and hide the channels.

To hide the channels in the visualizer you can use the visualizer settings in the UI

By default EventCatalog will render multiple nodes for your channels in the visualizer. This is to give you a better understanding of the relationship between your messages and channels.

If you prefer to only see a single node for your channels you can change the rendering mode in the visualizer settings.

To add a message to a channel, you need to add the channels information to your message.

Here is an example of adding channel information to an InventoryOutOfStockEvent.

The receives and sends fields in your service tell EventCatalog which messages this service either consumes or publishes.

Versioning for channels is optional. But if your message/channel relationship evolves over time, and you find value capturing this version/history then you can version your channels.

You can use semver syntax when referencing your channels in your messages.

When messages get added to your channels EventCatalog will visualize this for you through the visualizer.

**Examples:**

Example 1 (yaml):
```yaml
---id: OrderService# The messages this service sendssends:  # The id of the message this service sends  - id: OrderPlaced    to:      - id: orders.events      # You can also publish to many channels      - id: orders.events.filtered---
```

Example 2 (sql):
```sql
---id: PaymentService# The messages this service receivesreceives:  - id: OrderPlaced    from:      - id: orders.events      # You can also consume from many channels      - id: orders.events.filtered---
```

Example 3 (yaml):
```yaml
---id: OrderService# The messages this service sendssends:  - id: OrderPlaced    to:      - id: orders.events---
```

Example 4 (yaml):
```yaml
---id: PaymentService# The messages this service receivesreceives:  - id: OrderPlaced    from:      - id: orders.events---
```

---

## Function: getProducersAndConsumersForMessage()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getProducersAndConsumersForMessage

**Contents:**
- Function: getProducersAndConsumersForMessage()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getProducersAndConsumersForMessage(directory): (id, version?, options?) => Promise<{ consumers: Service[]; producers: Service[]; }>

Defined in: messages.ts:72

Returns the producers and consumers (services) for a given message.

Promise<{ consumers: Service[]; producers: Service[]; }>

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getProducersAndConsumersForMessage } = utils('/path/to/eventcatalog');// Returns the producers and consumers (services) for a given messageconst { producers, consumers } = await getProducersAndConsumersForMessage('InventoryAdjusted', '0.0.1');
```

---

## Function: getServiceByPath()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getServiceByPath

**Contents:**
- Function: getServiceByPath()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getServiceByPath(directory): (path) => Promise<Service>

Defined in: services.ts:54

Returns a service from EventCatalog by it's path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getServiceByPath } = utils('/path/to/eventcatalog');// Returns a service from the catalog by it's pathconst service = await getServiceByPath('/services/InventoryService/index.mdx');
```

---

## Adding flows to services

**URL:** https://www.eventcatalog.dev/docs/development/guides/flows/adding-flows-to-services

**Contents:**
- Adding flows to services
- Adding flows using frontmatter​

Adding flows to your services helps document which business processes or workflows involve a particular service.

When adding flows to your service EventCatalog will:

To add flows to a service you need to add them to the flows array within your service frontmatter API.

The flows frontmatter in your service tells EventCatalog that these documented flows involve this service.

In the example above we can see that the flows OrderProcessing and PaymentFlow involve the OrdersService.

**Examples:**

Example 1 (php):
```php
---id: OrdersService... # other service frontmatterflows:    # id of the flow you want to add    - id: OrderProcessing    # (optional) The version of the flow you want to add.      version: 1.0.0    # Note: version is optional. If no version is given the latest version of the flow will be used.    - id: PaymentFlow---<!-- Markdown content... -->
```

---

## Function: serviceHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/serviceHasVersion

**Contents:**
- Function: serviceHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

serviceHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: services.ts:449

Check to see if the catalog has a version for the given service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { serviceHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given event and version (supports semver)await serviceHasVersion('InventoryService', '0.0.1');await serviceHasVersion('InventoryService', 'latest');await serviceHasVersion('InventoryService', '0.0.x');*
```

---

## Function: getService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getService

**Contents:**
- Function: getService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getService(directory): (id, version?) => Promise<Service>

Defined in: services.ts:37

Returns a service from EventCatalog.

You can optionally specify a version to get a specific version of the service

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getService } = utils('/path/to/eventcatalog');// Gets the latest version of the eventconst service = await getService('InventoryService');// Gets a version of the eventconst service = await getService('InventoryService', '0.0.1');
```

---

## Function: addMessageToService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addMessageToService

**Contents:**
- Function: addMessageToService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addMessageToService(directory): (id, direction, event, version?) => Promise<void>

Defined in: services.ts:388

Add an event/command to a service by it's id.

Optionally specify a version to add the event to a specific version of the service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';// Adds an event to the service or command to the serviceconst { addEventToService, addCommandToService } = utils('/path/to/eventcatalog');// Adds a new event (InventoryUpdatedEvent) that the InventoryService will sendawait addEventToService('InventoryService', 'sends', { event: 'InventoryUpdatedEvent', version: '2.0.0' });* // Adds a new event (OrderComplete) that the InventoryService will receiveawait addEventToService('InventoryService', 'receives', { event: 'OrderComplete', version: '1.0.0' });// Adds a new command (UpdateInventoryCommand) that the InventoryService will sendawait addCommandToService('InventoryService', 'sends', { command: 'UpdateInventoryCommand', version: '2.0.0' });// Adds a new command (VerifyInventory) that the InventoryService will receiveawait addCommandToService('InventoryService', 'receives', { command: 'VerifyInventory', version: '1.0.0' });
```

---

## Function: toService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/toService

**Contents:**
- Function: toService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

toService(directory): (file) => Promise<Service>

Defined in: services.ts:497

Takes a given raw file and converts it to a service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { toService } = utils('/path/to/eventcatalog');// Read the file from somewhereconst file = fs.readFileSync('/path/to/services/InventoryService/index.mdx', 'utf8');// Converts the raw file to a serviceawait toService(file);
```

---

## Schema MCP

**URL:** https://www.eventcatalog.dev/docs/development/guides/schemas/schema-mcp

**Contents:**
- Schema MCP

The EventCatalog MCP server allows you to get access to your documentation and context in your MCP clients (e.g Cursor, Windsurf, Claude Desktop etc).

Your documented schemas for your Events, Queries, Commands and Services can be accessed via the EventCatalog MCP server.

This allows you to ask questions about your schemas, get schema information for your services and messages, directly in your code editor or LLM.

To get started, you can follow the guide to get started with the EventCatalog MCP server.

---

## Function: addDataStoreToService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addDataStoreToService

**Contents:**
- Function: addDataStoreToService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addDataStoreToService(directory): (id, operation, dataStore, version?) => Promise<void>

Defined in: services.ts:571

Add a data store to a service by it's id.

Optionally specify a version to add the data store to a specific version of the service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';// Adds an data store to the serviceconst { addDataStoreToService } = utils('/path/to/eventcatalog');// Adds a new data store (orders-db) that the InventoryService will write toawait addDataStoreToService('InventoryService', 'writesTo', { id: 'orders-db', version: '2.0.0' });* // Adds a new data store (OrderComplete) that the InventoryService will read fromawait addDataStoreToService('InventoryService', 'readsFrom', { id: 'orders-db', version: '1.0.0' });
```

---

## Services

**URL:** https://www.eventcatalog.dev/docs/services

**Contents:**
- Services
- 📄️ What are services?
- 📄️ Creating a service
- 🗃️ Adding to services
- 🗃️ Ownership & components
- 🗃️ Versioning & lifecycle

A collection of guides to help you understand services and how they work with EventCatalog.

What are services? Why are they useful for event-driven architectures?

Creating and managing services within EventCatalog.

---

## Versioning & lifecycle

**URL:** https://www.eventcatalog.dev/docs/versioning-and-lifecycle

**Contents:**
- Versioning & lifecycle
- 📄️ Versioning
- 📄️ Adding a changelog
- 📄️ Deprecating services

A collection of guides to help you understand entities and how they work with EventCatalog.

Learn how to version services

Adding changelogs to your services

Deprecating services with EventCatalog.

---

## Function: rmService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmService

**Contents:**
- Function: rmService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmService(directory): (path) => Promise<void>

Defined in: services.ts:261

Delete a service at it's given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmService } = utils('/path/to/eventcatalog');// Removes the service at services/InventoryServiceawait rmService('/InventoryService');
```

---

## Adding to services

**URL:** https://www.eventcatalog.dev/docs/adding-to-services

**Contents:**
- Adding to services
- 📄️ Messages
- 📄️ Data stores
- 📄️ Entities
- 📄️ OpenAPI specifications
- 📄️ AsyncAPI specifications
- 📄️ GraphQL schemas

Understanding how to add messages to services.

Adding data stores to services

Creating and managing entities within EventCatalog.

Attach an OpenAPI specification to your service and render them in your documentation

Attach an AsyncAPI specification to your service and render them in your documentation

Add a GraphQL schema to your service and render them in your documentation

---

## Function: rmServiceById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmServiceById

**Contents:**
- Function: rmServiceById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmServiceById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: services.ts:283

Delete a service by it's id.

Optionally specify a version to delete a specific version of the service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmServiceById } = utils('/path/to/eventcatalog');// deletes the latest InventoryService eventawait rmServiceById('InventoryService');// deletes a specific version of the InventoryService eventawait rmServiceById('InventoryService', '0.0.1');
```

---

## Function: versionService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionService

**Contents:**
- Function: versionService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

versionService(directory): (id) => Promise<void>

Defined in: services.ts:246

Version a service by it's id.

Takes the latest service and moves it to a versioned directory. All files with this service are also versioned. (e.g /services/InventoryService/openapi.yml)

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionService } = utils('/path/to/eventcatalog');// moves the latest InventoryService service to a versioned directory// the version within that service is used as the version number.await versionService('InventoryService');
```

---

## Flow nodes types

**URL:** https://www.eventcatalog.dev/docs/development/guides/flows/flow-nodes

**Contents:**
- Flow nodes types
- Flow node types​
  - default node type​
  - actor​
  - externalSystem​
  - message​
  - service​
  - flow​
  - custom​

Flow nodes are the building blocks of flows. They are used to represent the different steps in a flow.

With flow nodes you can reference your services, events, commands and queries, external systems, users (actors) or even create your own custom nodes.

EventCatalog (> 2.34.2) you can also reference flows as a node type.

A blank node type with just a title in your flow

Actor represents a person in your flow diagram.

Represents an external system in your flow diagram

Represents and refers to an event, command or query resource in EventCatalog.

Represents and refers to an service resource in EventCatalog.

Represents and refers to an flow resource in EventCatalog.

Useful for reusing flows in your flow diagrams.

The custom node allows you to define any custom node you want in your flow diagram.

Use cases could include:

Custom nodes can be anything you want.

You can view a UI example of a custom nodes here.

This example shows a custom node that represents a scheduler.

You can find a full example on GitHub here.

**Examples:**

Example 1 (yaml):
```yaml
steps:  - id: "step-1"    title: "This value will be shown in the node on the flow diagram"
```

Example 2 (swift):
```swift
steps:  - id: "step-1"    title: "Example Step of a Actor"    # here we define the actor type and the name    actor:      name: "Dave"      # optional, summary added in EventCatalog 2.55.6      summary: "This is a summary of the actor"
```

Example 3 (yaml):
```yaml
steps:  - id: "step-1"    title: "Example Step of a externalSystem"    # here we define the externalSystem, its summary and a url    externalSystem:      name: "Google"      summary: "Search engine"      href:"https://google.com"
```

Example 4 (yaml):
```yaml
steps:  - id: "step-1"    title: "Example Step of a Event"    # here we define the id and version of the event we want to use in the flow diagram    message:      id: "order-placed"      version: 0.0.1
```

---

## Function: getSpecificationFilesForService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getSpecificationFilesForService

**Contents:**
- Function: getSpecificationFilesForService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getSpecificationFilesForService(directory): (id, version?) => Promise<any>

Defined in: services.ts:328

Returns specification files for a service

Optionally specify a version to of the service

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getSpecificationFilesForService } = utils('/path/to/eventcatalog');// returns a list of specification files for a serviceawait getSpecificationFilesForService('InventoryService', '0.0.1');
```

---

## Data Stores

**URL:** https://www.eventcatalog.dev/docs/data

**Contents:**
- Data Stores
- 📄️ What are data stores?
- 📄️ Creating a data store
- 📄️ Adding schemas to data stores
- 🗃️ Ownership & components
- 🗃️ Versioning & lifecycle

A collection of guides to help you understand data resources and how they work with EventCatalog.

What are data resources in EventCatalog?

Creating and managing services within EventCatalog.

Adding schemas to data stores

---

## Deprecating services

**URL:** https://www.eventcatalog.dev/docs/development/guides/services/versioning-and-lifecycle/deprecating

**Contents:**
- Deprecating services
- Deprecating services using frontmatter​
    - Rendered output​
    - Demo​

Any resource in EventCatalog can be deprecated or marked as deprecated.

This will show a banner on the page indicating that the resource is deprecated.

To deprecate a service you need to add the deprecated field to the service frontmatter API.

This accepts a boolean or an object with the following properties:

Deprecated as an object is recommended, as it gives your users more information to why the resource is deprecated and a date in the past or future.

Example of resource that will be deprecated:

Example of resource that is deprecated:

You can see a demo of deprecating resources in the EventCatalog demo site.

**Examples:**

Example 1 (typescript):
```typescript
---id: OrderService... # other service frontmatter# deprecatd as an object (Recommended)deprecated:  # Date the service will be or was deprecated (YYYY-MM-DD)  date: 2025-01-01  # Reason the service is deprecated, supports markdown (optional)  message: |     This service has been deprecated and replaced by the new service **InventoryServiceV2**.    Please contact the [team for more information](mailto:inventory-team@example.com) or visit our [website](https://eventcatalog.dev).# deprecated as a boolean deprecated: true---
```

---

## Function: isService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/isService

**Contents:**
- Function: isService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

isService(directory): (path) => Promise<any>

Defined in: services.ts:467

Check to see if the path is a service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { isService } = utils('/path/to/eventcatalog');// returns true if the path is a serviceawait isService('/services/InventoryService/index.mdx');
```

---

## Function: addEntityToService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addEntityToService

**Contents:**
- Function: addEntityToService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addEntityToService(directory): (id, entity, version?) => Promise<void>

Defined in: services.ts:517

Add an entity to a service by its id.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addEntityToService } = utils('/path/to/eventcatalog');// adds a new entity (User) to the InventoryServiceawait addEntityToService('InventoryService', { id: 'User', version: '1.0.0' });// adds a new entity (Product) to a specific version of the InventoryServiceawait addEntityToService('InventoryService', { id: 'Product', version: '1.0.0' }, '2.0.0');
```

---

## Function: addFileToService()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addFileToService

**Contents:**
- Function: addFileToService()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addFileToService(directory): (id, file, version?) => Promise<void>

Defined in: services.ts:308

Add a file to a service by it's id.

Optionally specify a version to add a file to a specific version of the service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addFileToService } = utils('/path/to/eventcatalog');// adds a file to the latest InventoryService eventawait addFileToService('InventoryService', { content: 'Hello world', fileName: 'hello.txt' });// adds a file to a specific version of the InventoryService eventawait addFileToService('InventoryService', { content: 'Hello world', fileName: 'hello.txt' }, '0.0.1');
```

---
