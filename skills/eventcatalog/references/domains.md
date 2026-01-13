# Eventcatalog - Domains

**Pages:** 68

---

## <MermaidFileLoader />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/mermaid-file-loader

**Contents:**
- <MermaidFileLoader />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The MermaidFileLoader component is a EventCatalog component that will render a Mermaid file into your markdown page.

The <MermaidFileLoader/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Simply include the <MermaidFileLoader/> component in your markdown with a file path to your Mermaid file.

When you use the <MermaidFileLoader /> component, it will render the diagram in your EventCatalog page.

**Examples:**

Example 1 (jsx):
```jsx
---# event frontmatter---The User Registered event is triggered when a new user signs up for our platform.<MermaidFileLoader file="mermaid.mmd" />
```

Example 2 (sql):
```sql
sequenceDiagram  participant Customer  participant OrdersService  participant InventoryService  participant NotificationService  Customer->>OrdersService: Place Order  OrdersService->>InventoryService: Check Inventory  InventoryService-->>OrdersService: Inventory Available  OrdersService->>InventoryService: Reserve Inventory  OrdersService->>NotificationService: Send Order Confirmation  NotificationService-->>Customer: Order Confirmation  OrdersService->>Customer: Order Placed Successfully  OrdersService->>InventoryService: Update Inventory
```

---

## Data store changelogs

**URL:** https://www.eventcatalog.dev/docs/development/guides/data/versioning-and-lifecycle/changelog

**Contents:**
- Data store changelogs
  - Adding a changelog​
  - Why add changelogs?​

EventCatalog supports changelogs for domains, services, messages and data stores.

When you version a data store in EventCatalog, you can also attach a changelog.mdx to that data store or versioned data store.

Navigate to your change log page for your data store (example /docs/services/PaymentService/containers/PaymentDatabase/0.0.1/changelog) or click on the Changelog button on your data store page.

Changelogs are just markdown files, this allows you to add anything you want (e.g code blocks, tables)

EventCatalog code blocks supports diffs, code labels which are great features for changelogs. You can read more here.

Changelogs can provide your team with the context behind the reasons and choices for changes within your data store and also be used for auditing purposes.

**Examples:**

Example 1 (php):
```php
---createdAt: 2024-08-01badges:    - content: New table added      backgroundColor: green      textColor: green---### New Table added to the PaymentDatabaseThe PaymentDatabase now has a new table called `PaymentTransactions`.<!-- Other details about the change here -->
```

---

## Function: addUbiquitousLanguageToDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addUbiquitousLanguageToDomain

**Contents:**
- Function: addUbiquitousLanguageToDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addUbiquitousLanguageToDomain(directory): (id, ubiquitousLanguageDictionary, version?) => Promise<void>

Defined in: domains.ts:245

Adds a ubiquitous language dictionary to a domain.

Optionally specify a version to add a ubiquitous language dictionary to a specific version of the domain.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addUbiquitousLanguageToDomain } = utils('/path/to/eventcatalog');// Adds a ubiquitous language dictionary to the latest Payment domainawait addUbiquitousLanguageToDomain('Payment', { dictionary: [{ id: 'Order', name: 'Order', summary: 'All things to do with the payment systems', description: 'This is a description', icon: 'KeyIcon' }] });// Adds a ubiquitous language dictionary to a specific version of the domainawait addUbiquitousLanguageToDomain('Payment', { dictionary: [{ id: 'Order', name: 'Order', summary: 'All things to do with the payment systems', description: 'This is a description', icon: 'KeyIcon' }] }, '0.0.1');
```

---

## Flows

**URL:** https://www.eventcatalog.dev/docs/flows

**Contents:**
- Flows
- 📄️ What are flows?
- 📄️ Creating a flow
- 📄️ Flow nodes
- 📄️ Adding flows to services
- 📄️ Adding flows to domains
- 📄️ Versioning

A collection of guides to help you understand flows and how they work with EventCatalog.

What are flows? Why are they useful for event-driven architectures?

Creating and managing flows within EventCatalog.

Flow nodes types within EventCatalog.

Associate flows with services in EventCatalog

Associate flows with domains in EventCatalog

Learn how to version flows

---

## Function: domainHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/domainHasVersion

**Contents:**
- Function: domainHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

domainHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: domains.ts:300

Check to see if the catalog has a version for the given domain.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { domainHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given event and version (supports semver)await domainHasVersion('Orders', '0.0.1');await domainHasVersion('Orders', 'latest');await domainHasVersion('Orders', '0.0.x');*
```

---

## <Miro />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/embed-diagrams/miro

**Contents:**
- <Miro />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The <Miro /> component renders a Miro board in your documentation.

Each Miro board embedded can also be loaded in a full screen mode, letting your teams edit the board live (view demo).

The <Miro /> component is supported in domains, services, all messages and custom documentation.

Example with edit enabled and scroll to default widget in Miro

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<Miro boardId="uXjVIHCImos=/" edit={false} />
```

Example 2 (jsx):
```jsx
---#event frontmatter---<Miro boardId="uXjVIHCImos=/" moveToWidget="3074457347671667709" edit={false} />
```

---

## Function: addSubDomainToDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addSubDomainToDomain

**Contents:**
- Function: addSubDomainToDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addSubDomainToDomain(directory): (id, subDomain, version?) => Promise<void>

Defined in: domains.ts:368

Add a subdomain to a domain by it's id. Optionally specify a version to add the subdomain to a specific version of the domain

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';// Adds a subdomain to the given domainconst { addSubDomainToDomain } = utils('/path/to/eventcatalog');// Adds a subdomain (Payment Domain) to the domain (Orders)await addSubDomainToDomain('Orders', { service: 'Payment Domain', version: '2.0.0' });// Adds a subdomain (Inventory Domain) to the domain (Orders) with a specific versionawait addSubDomainToDomain('Orders', { service: 'Inventory Domain', version: '2.0.0' }, '1.0.0');
```

---

## Service changelogs

**URL:** https://www.eventcatalog.dev/docs/development/guides/channels/versioning-and-lifecycle/changelog

**Contents:**
- Service changelogs
  - Adding a changelog​
  - Why add changelogs?​

EventCatalog supports changelogs for domains, services, messages and channels.

When you version a channel in EventCatalog, you can also attach a changelog.mdx to that service or versioned service.

Navigate to your change log page for your channel or click on the Changelog button on your channel page.

Changelogs are just markdown files, this allows you to add anything you want (e.g code blocks, tables)

EventCatalog code blocks supports diffs, code labels which are great features for changelogs. You can read more here.

Changelogs can provide your team with the context behind the reasons and choices for changes within your channel and also be used for auditing purposes.

Changelogs are visualized by EventCatalog.

**Examples:**

Example 1 (julia):
```julia
---createdAt: 2024-08-01badges:    - content: New channel created      backgroundColor: green      textColor: green---### Channel protocol updateThe OrdersChannel now accepts messages using kafka.
```

---

## Function: getDomains()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getDomains

**Contents:**
- Function: getDomains()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getDomains(directory): (options?) => Promise<Domain[]>

Defined in: domains.ts:59

Returns all domains from EventCatalog.

You can optionally specify if you want to get the latest version of the domains.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getDomains } = utils('/path/to/eventcatalog');// Gets all domains (and versions) from the catalogconst domains = await getDomains();// Gets all domains (only latest version) from the catalogconst domains = await getDomains({ latestOnly: true });
```

---

## <MessageTable />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/message-table

**Contents:**
- <MessageTable />
  - Use case​
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The <MessageTable/> component renders a table of messages for a service or domain in EventCatalog.

The component renders a paginated table of messages, with the ability to filter by message type (event, command, query), and text search.

The <MessageTable/> component is supported in domains and services.

See the demo for a full example.

**Examples:**

Example 1 (jsx):
```jsx
---#domain frontmatter---<MessageTable limit={10} showChannels={true} />
```

---

## Ownership & components

**URL:** https://www.eventcatalog.dev/docs/channels/ownership-and-components

**Contents:**
- Ownership & components
- 📄️ Owners
- 📄️ Components

A collection of guides to help you understand entities and how they work with EventCatalog.

Adding owners to channels with EventCatalog.

Component list for domains

---

## Function: rmDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmDomain

**Contents:**
- Function: rmDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmDomain(directory): (path) => Promise<void>

Defined in: domains.ts:176

Delete a domain at it's given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmDomain } = utils('/path/to/eventcatalog');// Removes the domain at domains/Paymentawait rmDomain('/Payment');
```

---

## Ownership & components

**URL:** https://www.eventcatalog.dev/docs/ownership-and-components

**Contents:**
- Ownership & components
- 📄️ Owners
- 📄️ Components

A collection of guides to help you understand entities and how they work with EventCatalog.

Adding owners to services with EventCatalog.

Component list for domains

---

## Adding components

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-components/adding-components

**Contents:**
- Adding components
- Types of components​
- Astro components (.astro)​
  - Component structure​
    - Example​
  - Define variables inside your resources​
  - Reference frontmatter data in your components​
  - Reference eventcatalog.config.js data in your components​

The components directory is where your custom components will be created and stored.

If you don't have a components directory, you will need to create one in the root of your catalog (e.g /my-catalog/components)

EventCatalog supports astro components and markdown components.

Astro components are split into two parts the script and the template.

Read the full astro guide here.

EventCatalog allows you to define variables inside your domains, services and messages that can be used to pass through to your custom components.

If you want to reference your domain, service or message data, you can reference the frontmatter information.

If you want to reference your eventcatalog.config.js data you can import it within your component.

**Examples:**

Example 1 (php):
```php
---// Component Script (JavaScript)---<!-- Component Template (HTML + JS Expressions) -->
```

Example 2 (jsx):
```jsx
---# Import data from your eventcatalog.config.js fileimport config from "@config"# Access passed-in component props, like `<MyComponent title="Hello, World" />`const { subtitle } = Astro.props;---<main>    <span>This catalog belongs to the company:{config.organizationName}</span>    <span>Data given to this component {subtitle}</span></main>
```

Example 3 (jsx):
```jsx
---id: OrderAcceptedname: Order Accepted# ... other event data---<!-- Import the component into your page -->import MyComponent from '@catalog/components/my-component.astro"# Overview This event represents when an order has been accepted on our system.<!-- Render the component and pass props into it --><MyComponent subtitle="This is a component" />
```

Example 4 (jsx):
```jsx
---id: OrderAcceptedname: Order Accepted# ... other event data---<!-- Define your custom variable to use on this page -->export const MyCustomVariable = "Hello world";<!-- Import the component into your page -->import MyComponent from '@catalog/components/my-component.astro"# Overview This event represents when an order has been accepted on our system.<!-- Render the component and pass custom variable to it --><MyComponent subtitle={MyCustomVariable} />
```

---

## Patterns for shared messages

**URL:** https://www.eventcatalog.dev/docs/development/guides/messages/common/shared-messages-across-boundaries

**Contents:**
- Patterns for shared messages
  - Messages defined by the service​
  - Define messages at a domain level​
  - Define messages at a system level​

You can store your events, commands and queries in any folder in your EventCatalog.

Here are some common usecases:

If you want to keep your message definition close to the service that producers or consumes it you can store them in the /services folder.

In the example below the OrderPlaced event, AddOrder command and GetOrder query are defined in the /services/Orders folder.

If you want to share messages across multiple services you can define them in the /domains folder.

In the example below the OrderPlaced event, AddOrder command and GetOrder query are defined in the /domains/Orders folder.

If you want to share messages across all your domains you can define them in the root of your catalog.

In the example below the OrderPlaced event, AddOrder command and GetOrder query are defined in the root of your catalog.

**Examples:**

Example 1 (unknown):
```unknown
services/  Orders/    events/      OrderPlaced/        index.mdx    commands/      AddOrder/        index.mdx    queries/      GetOrder/        index.mdx
```

Example 2 (php):
```php
domains/  Orders/     <!-- The domain documentation -->    index.mdx    <!-- Here we store our /events, /commands and /queries -->    events/      OrderPlaced/        index.mdx
```

Example 3 (unknown):
```unknown
events/  OrderPlaced/    index.mdxcommands/  AddOrder/    index.mdxqueries/  GetOrder/    index.mdx
```

---

## Creating changelogs

**URL:** https://www.eventcatalog.dev/docs/development/guides/changelogs/adding-changelogs

**Contents:**
- Creating changelogs
  - Viewing your changelog​

Changelogs are currently supported in domains, services and messages.

To add a changelog to your resources you need to create a changelog.mdx file.

Example of changelogs for resources

Domains, services and messages have a Changelog button. Clicking this button will take you to the changelog for that resource.

Domains, services and messages all have a changelog url.

See example changelog: https://demo.eventcatalog.dev/docs/events/InventoryAdjusted/1.0.1/changelog

**Examples:**

Example 1 (json):
```json
---createdAt: 2024-08-01badges: - content: ⭐️ JSON Schema   backgroundColor: purple   textColor: purple---### Added support for JSON SchemaInventoryAdjusted uses Avro but now also supports JSON Draft 7.```json title="Employee JSON Draft"// labeled-line-markers.jsx{"$schema": "http://json-schema.org/draft-07/schema#","type": "object","title": "Employee","properties": { "Name": {   "type": "string" }, "Age": {   "type": "integer" }, "Town": {   "type": "string" }},"required": ["Name", "Age", "Town"]}``
```

Example 2 (json):
```json
---createdAt: 2024-08-01---### Service receives additional eventsService now receives [OrderAmended](/docs/events/OrderAmended/0.0.1) and [UpdateInventory](/docs/commands/UpdateInventory/0.0.3) events.
```

Example 3 (json):
```json
---createdAt: 2024-08-01---### New service added to the Payment domainService now receives [OrderAmended](/docs/events/OrderAmended/0.0.1) and [UpdateInventory](/docs/commands/UpdateInventory/0.0.3) events.
```

---

## Function: getDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getDomain

**Contents:**
- Function: getDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getDomain(directory): (id, version?) => Promise<Domain>

Defined in: domains.ts:36

Returns a domain from EventCatalog.

You can optionally specify a version to get a specific version of the domain

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getDomain } = utils('/path/to/eventcatalog');// Gets the latest version of the domainconst domain = await getDomain('Payment');// Gets a version of the domainconst domain = await getDomain('Payment', '0.0.1');
```

---

## Creating services

**URL:** https://www.eventcatalog.dev/docs/development/guides/services/adding-services

**Contents:**
- Creating services
  - What do services look like in EventCatalog?​
- Adding a new service​
- Adding content​
- Adding specifications to your service​

Services in EventCatalog are a great way to document which parts of your systems send and receive messages.

You can also add specifications (OpenAPI, AsyncAPI, GraphQL) to your services.

View Demo of an Orders service →

To add a new service create a new folder within the /services folder with an index.mdx file.

You can also specify services in your domains folder.

Here is an example of what a service markdown file may look like.

With services you can write any Markdown you want and it will render on your page. Every service gets its own page.

Within your markdown content you can use components to add interactive components to your page.

You can add GraphQL, OpenAPI or AsyncAPI specifications to your service.

You can read more about adding specifications to your service here.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your service, used for slugs and references in EventCatalog.id: Orders# Display name of the Service, rendered in EventCatalogname: Orders# Version of the Serviceversion: 0.0.1# Short summary of your Servicesummary: |  Service that contains order related information# Optional owners, references teams or usersowners:    - dboyne# Optional messages this service receives and it's versionreceives:  - id: InventoryAdjusted    version: 0.0.3# Optional messages this service sends and it's versionsends:  - id: AddInventory    version: 0.0.3# Optional flows associated with this serviceflows:  - id: OrderProcessing    version: 1.0.0# Optional badges, rendered to UI by EventCatalogbadges:    - content: New service      backgroundColor: blue      textColor: blue---## OverviewThis orders service gives API consumers the ability to produce orders in the systems. Events are raised from this system for downstream consumption.<NodeGraph />
```

---

## <SchemaViewer />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/schema-viewer

**Contents:**
- <SchemaViewer />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​
- Rendering multiple schemas​

A Schema Viewer component for EventCatalog that supports JSON schemas and Avro schemas.

Renders the given schema (.json, .yaml, .avro, .avsc) into the page.

The <SchemaViewer/> component only works with JSON Schema and Avro schemas.

If you need to render other schema formats, please use the <Schema/> component.

Avro support was added in 2.64.0. Please upgrade to the latest version of EventCatalog to use this component.

The <SchemaViewer/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

You can use the SchemaViewer multiple times in your page.

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---The Inventory Adjusted event is triggered whenever there is a change in the inventory levels of a product. This could occur due to various reasons such as receiving new stock, sales, returns, or manual adjustments by the inventory management team.<!-- Renders the schema with search and expand options --><SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" search="true" expand="true" /><!-- Renders the Avro schema --><SchemaViewer file="schema.avro" title="Avro Schema" maxHeight="500" /><!-- Also supports YAML formats --><SchemaViewer file="schema.yaml" title="YAML Schema" maxHeight="500" />
```

Example 2 (jsx):
```jsx
---#event frontmatter---The Inventory Adjusted event is triggered whenever there is a change in the inventory levels of a product. This could occur due to various reasons such as receiving new stock, sales, returns, or manual adjustments by the inventory management team.<SchemaViewer file="schema.json" title="JSON Schema" maxHeight="500" id="json-schema" /><SchemaViewer file="old-schema.json" title="Another Version" maxHeight="500" id="json-schema2" /><SchemaViewer file="new-schema.yml" title="Another Version" maxHeight="500" id="yaml-schema" />
```

---

## Creating entities

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/entities/adding-entities

**Contents:**
- Creating entities
  - What do entities look like in EventCatalog?​
- Adding a new entity​
- Adding markdown content​
  - Tips for entity content​

Entities are markdown files in EventCatalog, they have unique ids and can be versioned.

Entities can be assigned to domains and/or services.

You can read the Entity API documentation here.

View Demo of an OrderItem entity for an Orders domain →

To add a new entity create a new folder within the /domains or /services folder with an index.mdx file.

Creating an entity in a domain:

Creating an entity in a service:

The index.mdx contents are split into two sections, frontmatter and the markdown content.

Here is an example of what a entity markdown file may look like.

Once you add you new entity, you need to add it to the domain.

Once your entity is defined and added to the domain, you can navigate to the entity through domain navigation.

To learn more about entities and how to use them, you can read the Entity API documentation here.

With entities you can write any Markdown you want and it will render on your page. Every entity gets its own page.

Think about writing a blog. EventCatalog is just markdown. Write and use it how you like, and the website will render your content!

Within your markdown content you can use components to add interactive components to your page.

To find out more read the entity components list.

It's entirely up to you what you want to add to your entities markdown content but here are a few things you might want to consider.

**Examples:**

Example 1 (jsx):
```jsx
---# the id of the entity (used in EventCatalog)id: Order# the name of the entityname: Order# the version of the entityversion: 1.0.0# whether the entity is an aggregate root (optional)aggregateRoot: true# a summary of the entity (optional)summary: Represents a customer's request to purchase products or services.# the properties of the entity (optional)properties:  - name: orderId    type: UUID    required: true    description: Unique identifier for the order  - name: customerId    type: UUID    required: true    description: Identifier for the customer placing the order  - name: orderDate    type: DateTime    required: true    description: Date and time when the order was placed  - name: status    type: string    required: true    description: Current status of the order (e.g., Pending, Processing, Shipped, Delivered, Cancelled)    enum: ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']  - name: orderItems    type: array    items:      type: OrderItem # Assuming an OrderItem entity exists    required: true    description: List of items included in the order  - name: totalAmount    type: decimal    required: true    description: Total monetary value of the order  - name: shippingAddress    type: Address # Assuming an Address value object or entity exists    required: true    description: Address where the order should be shipped---## OverviewThe Order entity captures all details related to a customer's purchase request. It serves as the central aggregate root within the Orders domain, coordinating information about the customer, products ordered, payment, and shipping.### Entity Properties<EntityPropertiesTable />## Relationships*   **Customer:** Each order belongs to one `Customer` (identified by `customerId`).*   **OrderItem:** An order contains one or more `OrderItem` entities detailing the specific products and quantities.*   **Payment:** An order is typically associated with a `Payment` entity (not detailed here).*   **Shipment:** An order may lead to one or more `Shipment` entities (not detailed here).## Examples*   **Order #12345:** A customer orders 2 units of Product A and 1 unit of Product B, to be shipped to their home address. Status is 'Processing'.*   **Order #67890:** A customer places a large order for multiple items, requiring special shipping arrangements. Status is 'Pending' until payment confirmation.
```

Example 2 (json):
```json
---# the id of the domain (used in EventCatalog)id: Orders# the name of the domainname: Orders# Add your entities hereentities:  - id: Order    # Optional, if not provided the latest version will be used    version: 1.0.0---This is your domain markdown....
```

---

## <Steps />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/steps

**Contents:**
- <Steps />
  - Key Features:​
  - Use Cases:​
  - Support​
  - Usage​
  - Rendered example in EventCatalog​
  - Props (<Steps>)​
  - Props (<Step>)​

The Steps component is a powerful tool for creating structured, sequential guides in EventCatalog. It's ideal for presenting step-by-step instructions, tutorials, or workflows, particularly when explaining processes, API integrations, or code implementations.

The <Steps/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Add Steps and Step component into your markdown of your page.

See example in the demo EventCatalog application.

**Examples:**

Example 1 (javascript):
```javascript
---# service frontmatter---The Inventory Service is a critical component of the system responsible for managing product stock levels, tracking inventory movements, and ensuring product availability. It interacts with other services to maintain accurate inventory records and supports operations such as order fulfillment, restocking, and inventory audits.<Steps title="How to connect to Inventory Service">  <Step title="Obtain API credentials">    Request API credentials from the Inventory Service team.  </Step>  <Step title="Install the SDK">    Run the following command in your project directory:    ```bash      npm install inventory-service-sdk    ```_  </Step>  <Step title="Initialize the client">  Use the following code to initialize the Inventory Service client:  ```js    const InventoryService = require('inventory-service-sdk');    const client = new InventoryService.Client({      clientId: 'YOUR_CLIENT_ID',      clientSecret: 'YOUR_CLIENT_SECRET',      apiUrl: 'https://api.inventoryservice.com/v1'    });  ```_  </Step>  <Step title="Make API calls">    You can now use the client to make API calls. For example, to get all products:  ```js  client.getProducts()    .then(products => console.log(products))    .catch(error => console.error(error));  ```_  </Step></Steps>
```

---

## Creating subdomains

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/creating-domains/subdomains

**Contents:**
- Creating subdomains
  - What do subdomains look like in EventCatalog?​
    - Domains Visualizer (with subdomains)​
- Adding subdomains​
  - Referencing subdomains​

Subdomains are optional in EventCatalog but can be a great way to group domains together.

Some organizations have multiple domains, and each domain may have multiple subdomains.

When you add a subdomain to a domain, your users will be able to see the relationship between the domain and subdomain, and be able to navigate between them.

See subdomain example in the EventCatalog Demo.

When you reference a subdomain from a domain, it will appear in the domains visualizer. You can use the legend to highlight resources that are part of a subdomain.

See subdomain example in the EventCatalog Demo.

A subdomain is just another domain resource. But a parent domain references the subdomains.

First you need to create your subdomain.

You can create a subdomain in the /domains folder or in a /subdomains folder.

Once you have created your subdomain, you can reference it from your parent domain.

To add a subdomain to a domain you need to reference the subdomain from the domain markdown file.

We do this using the domains property.

In this example we are adding the Orders and Customers subdomains to the Ecommerce domain.

Once you add the subdomains to the domain, it will now show in the docs, visualizer and discoverability table.

**Examples:**

Example 1 (jsx):
```jsx
---id: Ecommercename: Ecommerceversion: 0.0.1# List of subdomains (version is optional)domains:  # Here version is given, the latest version of Orders Domain is used.  - id: Orders    version: 0.0.1  # Here version is not given, the latest version of Customers Domain is used.  - id: Customers---## OverviewEcommerce domain contains all ecommerce related information for FakeCompany.<NodeGraph />
```

---

## <IcePanel />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/embed-diagrams/icepanel

**Contents:**
- <IcePanel />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The <IcePanel /> component renders an IcePanel diagram in your documentation.

Each IcePanel diagram embedded can also be loaded in a full screen mode, letting your teams explore the diagram in detail.

The <IcePanel /> component is supported in domains, services, all messages and custom documentation.

Example with title and description

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<IcePanel url="https://s.icepanel.io/OpQVdslrqhZkyb/0QfB" />
```

Example 2 (jsx):
```jsx
---#event frontmatter---<IcePanel  url="https://s.icepanel.io/OpQVdslrqhZkyb/0QfB"  title="System Architecture"  description="Overview of our microservices architecture and communication patterns."  height="800"/>
```

---

## @eventcatalog/sdk

**URL:** https://www.eventcatalog.dev/docs/sdk

**Contents:**
- @eventcatalog/sdk
- EventCatalog SDK​
- Installation​
- Usage​
- Functions​

The EventCatalog SDK provides methods to interact with domains, services, and messages.

**Examples:**

Example 1 (python):
```python
npm install @eventcatalog/sdk
```

Example 2 (python):
```python
import utils from '@eventcatalog/sdk';const { getEvent } = utils(PATH_TO_CATALOG);// Get an event by the idconst event = getEvent('event-name');// Get an event by the id and it's versionconst event = getEvent('event-name', '0.3.4');
```

---

## Versioning

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/versioning-and-changelogs/versioning

**Contents:**
- Versioning
- How to version a domain​
- How to navigate to versions​

All content in EventCatalog can be versioned.

This allows you to keep historic versions of content which can give context to users why things are changing.

Versioning in EventCatalog is a great way to track changes over time. At any point users using EventCatalog can look back in time and understand what changes have been made to domains, services and messages. This gives extra context that is usually missed.

Example would when new developers come on board, maybe they are interested in a particular domain, maybe they want to understand the history of this domain, where it started and how it came to be what it is today. Versioning allows you to capture this context.

EventCatalog will automatically create links for you within your latest version of your document. Users will also be able to navigate to any version by adding the version in the url (e.g /docs/domains/Orders/1.0.2 would load the 1.0.2 version of this domain).

---

## Function: addServiceToDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addServiceToDomain

**Contents:**
- Function: addServiceToDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addServiceToDomain(directory): (id, service, version?) => Promise<void>

Defined in: domains.ts:325

Add a service to a domain by it's id.

Optionally specify a version to add the service to a specific version of the domain.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';// Adds a service to the domainconst { addServiceToDomain } = utils('/path/to/eventcatalog');// Adds a service (Orders Service) to the domain (Orders)await addServiceToDomain('Orders', { service: 'Order Service', version: '2.0.0' });// Adds a service (Orders Service) to the domain (Orders) with a specific versionawait addServiceToDomain('Orders', { service: 'Order Service', version: '2.0.0' }, '1.0.0');
```

---

## Automated diffs

**URL:** https://www.eventcatalog.dev/docs/development/guides/changelogs/automated-changelogs

**Contents:**
- Automated diffs
  - How it works​

EventCatalog allows you to store schemas, API specifications and custom files along side your domains, services and messages. For example you can add specifications to a service.

When you version your resources, you can also version the files. When you do this, EventCatalog will match the current version to it's previous version and calculate if any diffs should be displayed in your changelog page.

Automated diffs only work with .json, .avro, .yml and .yaml files at the moment. If you would like to support more files please raise an issue on GitHub.

Let's say we have a service called Orders, this service has an OpenAPI file.

Let's now version this service, by added the versioned folder.

If any changes have been made to the openapi.yml file in this example, this changes will be shown in the service changelog page.

You can see the example in our demo.

---

## <Accordion />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/accordian

**Contents:**
- <Accordion />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The accordion component renders collapsable section in EventCatalog.

The <Accordion/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Example with code as child

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<Accordion title="Learn how to raise this event">    This will be rendered as a child inside a collapsible section.</Accordion>
```

Example 2 (jsx):
```jsx
---#event frontmatter---<Accordion title="Learn how to raise this event">  You can run the following command to raise this event.  ```sh  bin/kafka-topics.sh --create --topic OrderAmended --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1  ``</Accordion>
```

---

## Getting Started

**URL:** https://www.eventcatalog.dev/docs/studio/getting-started

**Contents:**
- Getting Started
  - How does EventCatalog Studio work?​
  - EventCatalog Studio Workflow​
  - Core features​

If you want to skip straight into Studio, try our Playground.

Or, keep reading to learn more about how EventCatalog Studio works.

EventCatalog Studio lets you design using architecture primitives you already know — services, events, commands, queries, domains, and more.

It’s also privacy-first: you own your designs, and nothing is stored in the cloud.

To get started you can either:

EventCatalog Studio is designed for a GitOps workflow, where you can export your designs and store them in a Git repository. Your designs are owned by you, and you can share them with your teams and commit them to source control.

This let's you keep your designs versioned alongside your code and always own your data.

GitOps workflow Export your designs directly to a Git repository. Keep diagrams versioned alongside your code and always own your data.

Import & Export Save and load your designs locally.

Design with primitives Build diagrams using real software architecture concepts — services, events, commands, queries, and domains — not just generic boxes.

Add documentation Enrich your diagrams with notes, descriptions, and links to external resources, guiding users through the flow of your system. Reference any node in your documentation using the @ syntax.

Privacy-first Your designs stay local by default. Nothing is stored in the cloud unless you explicitly choose to.

Extensible formats (coming soon) Import/export diagrams in open standards like AsyncAPI, OpenAPI, or EventCatalog — making it easy to integrate with your workflows.

Version history (coming soon) Keep track of changes to your designs. Compare different iterations to see how your architecture evolves over time.

Self-hosting (coming soon) Run EventCatalog Studio on your own infrastructure for full control and compliance.

---

## Domains

**URL:** https://www.eventcatalog.dev/docs/domains

**Contents:**
- Domains
- 📄️ What are domains?
- 🗃️ Creating domains
- 🗃️ Creating domain entities
- 🗃️ Ownership & language
- 🗃️ Versioning & changelogs
- 📄️ Domain Integration Map

A collection of guides to help you understand domains and how they work with EventCatalog.

What are domains? Why are they useful for event-driven architectures?

Component list for domains

---

## Components

**URL:** https://www.eventcatalog.dev/docs/components/list

**Contents:**
- Components
- 📄️ <Attachments />
- 📄️ <Accordion />
- 📄️ <AccordionGroup />
- 📄️ Admonitions
- 📄️ <MessageTable />
- 📄️ <ResourceGroupTable />
- 📄️ <ResourceLink />
- 📄️ <Link />
- 📄️ <NodeGraph />

This section describes what components can be used in EventCatalog..

Learn how to add attachments to your EventCatalog resources

Component for EventCatalog

Component for EventCatalog

Component for EventCatalog

Component for displaying messages for services and domains in EventCatalog

Component for displaying EventCatalog grouped resources in EventCatalog

Create links in your documentation to resources in EventCatalog

Create links in your documentation

Component for EventCatalog

Component for EventCatalog

Component for EventCatalog

Component for EventCatalog

Render JSON schema in EventCatalog

Render a Flow in any EventCatalog page

Render tiles into EventCatalog

Render steps into EventCatalog

Render tabs in your EventCatalog pages

Render channel into EventCatalog

Component for fetching and rendering remote schemas in EventCatalog

Component for embedding EventCatalog Studio diagrams into your documentation

Component for embedding EventCatalog Studio diagrams into your documentation

---

## <ResourceGroupTable />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/resource-group-table

**Contents:**
- <ResourceGroupTable />
  - Why use ResourceGroupTable?​
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The <ResourceGroupTable/> component renders a table of resources for your page in EventCtalog.

The component renders a paginated table of (messages, services, domains, flows, channels), with the ability to filter by resource type, and text search.

Sometimes in your catalog you may want to link related resources together or group them in particular ways that EventCatalog does not naturally support.

The <ResourceGroupTable/> component is supported on all EventCatalog pages.

The <ResourceGroupTable/> component requires frontmatter property called resourceGroups defined in your resource, and then the component itself.

You can see the demo of this in the Orders domain page.

**Examples:**

Example 1 (json):
```json
---id: Ordersname: Ordersversion: 0.0.3owners:  - dboyne  - full-stack# Here we define the resourceGroups, in this example we create a group called core resources# We create a list called `related-resources` and we group these services.# Remember you can define any group of information you want, and link to any catalog resourceresourceGroups:  - id: related-resources    title: Core resources    items:      - id: InventoryService        type: service      - id: OrdersService        type: service      - id: NotificationService        type: service      - id: ShippingService        type: service---
```

Example 2 (jsx):
```jsx
---#domain frontmatter---<ResourceGroupTable id="related-resources" limit={4} showOwners={true} title="Core resources for the Orders domain" description="Resources that are related to the Orders domain, you may find them useful" />
```

---

## <Lucid />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/embed-diagrams/lucid

**Contents:**
- <Lucid />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The <Lucid /> component renders a Lucid diagram in your documentation.

The <Lucid /> component is supported in domains, services, all messages and custom documentation.

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<Lucid diagramId="e29f42a0-67e2-4f80-b0d7-6922bb7dd9c5" />
```

---

## <Flow />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/flow

**Contents:**
- <Flow />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

Renders a Flow diagram.

The <Flow/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Add Flow component into your markdown of your page.

**Examples:**

Example 1 (jsx):
```jsx
---# domain frontmatter---## OverviewThe Orders domain handles all operations related to customer orders, from creation to fulfillment. This documentation provides an overview of the events and services involved in the Orders domain, helping developers and stakeholders understand the event-driven architecture.## Flows### Cancel Subscription flowDocumented flow when a user cancels their subscription.<!-- semver support version property --><Flow id="CancelSubscription" version="latest" includeKey={false} />
```

---

## <Schema />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/schema

**Contents:**
- <Schema />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The schema component renders a given schema into the page.

Schemas can be any file format (.avro, .json etc).

The <Schema/> component renders any schema format.

If you need to render JSON Schema, you can also use the <SchemaViewer/> component.

The <Schema/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---The Inventory Adjusted event is triggered whenever there is a change in the inventory levels of a product. This could occur due to various reasons such as receiving new stock, sales, returns, or manual adjustments by the inventory management team.<Schema file="schema.avro" />
```

---

## Function: addFileToDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addFileToDomain

**Contents:**
- Function: addFileToDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addFileToDomain(directory): (id, file, version?) => Promise<void>

Defined in: domains.ts:222

Add a file to a domain by it's id.

Optionally specify a version to add a file to a specific version of the domain.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addFileToDomain } = utils('/path/to/eventcatalog');// adds a file to the latest Payment eventawait addFileToDomain('Payment', { content: 'Hello world', fileName: 'hello.txt' });// adds a file to a specific version of the Payment eventawait addFileToDomain('Payment', { content: 'Hello world', fileName: 'hello.txt' }, '0.0.1');
```

---

## Creating diagrams

**URL:** https://www.eventcatalog.dev/docs/development/guides/diagrams/creating-diagrams

**Contents:**
- Creating diagrams
- File structure​
- Creating a diagram​
- Frontmatter properties​
  - Required fields​
  - Optional fields​
- Adding content​
  - Example with PlantUML​
  - Example with embedded diagram​
- Next steps​

Diagrams in EventCatalog are created using MDX files with frontmatter. They can be placed at the root level or nested within any resource (domains, services, events, commands, queries, or containers) for better organization.

Diagrams live in a /diagrams folder. This folder can be placed at the root level or nested within any resource:

Organize diagrams close to where they're most relevant. System-wide diagrams can be placed at the root level, while resource-specific diagrams should live within that resource's folder.

To create a new diagram, create a folder with an index.mdx file. The file consists of two sections: frontmatter and markdown content.

Here is an example of a system architecture diagram:

Diagrams support the following frontmatter properties:

The content section of your diagram file supports full MDX, allowing you to:

EventCatalog provides built-in components to embed diagrams from popular tools like Miro, IcePanel, Lucidchart, draw.io, and FigJam. This lets you bring your existing collaborative diagrams directly into your catalog.

Check out the MDX components documentation to see all available embed components including <Miro>, <IcePanel>, <Lucid>, <DrawIO>, and <FigJam>.

Once you've created diagrams, you can:

**Examples:**

Example 1 (markdown):
```markdown
# Root level diagrams/diagrams/[diagram-name]/index.mdx# Nested within any resource (domains, services, events, commands, queries, containers)/[resource]/[resource-name]/diagrams/[diagram-name]/index.mdx
```

Example 2 (php):
```php
---id: system-overviewname: System Overviewversion: 1.0.0summary: High-level architecture showing all microservices and their interactions---## System ArchitectureThis diagram shows our microservices architecture:\`\`\`mermaidgraph TB    subgraph "Frontend"        WebApp[Web Application]        MobileApp[Mobile App]    end    subgraph "Backend Services"        Gateway[API Gateway]        OrderService[Order Service]        PaymentService[Payment Service]        InventoryService[Inventory Service]    end    subgraph "Data Layer"        OrderDB[(Orders DB)]        PaymentDB[(Payments DB)]        Kafka[Event Stream]    end    WebApp --> Gateway    MobileApp --> Gateway    Gateway --> OrderService    Gateway --> PaymentService    OrderService --> Kafka    PaymentService --> Kafka    OrderService --> OrderDB    PaymentService --> PaymentDB\`\`\`### Key Components- **API Gateway**: Single entry point for all client requests- **Order Service**: Handles order creation and management- **Payment Service**: Processes payments and refunds- **Event Stream**: Kafka for asynchronous communication
```

Example 3 (typescript):
```typescript
---id: order-flowname: Order Processing Flowversion: 1.0.0summary: Sequence diagram showing the complete order processing flow---\`\`\`plantuml@startumlactor Customerparticipant "Order Service" as Orderparticipant "Payment Service" as Paymentparticipant "Inventory Service" as InventoryCustomer -> Order: Create OrderOrder -> Inventory: Check StockInventory --> Order: Stock AvailableOrder -> Payment: Process PaymentPayment --> Order: Payment ConfirmedOrder --> Customer: Order Confirmed@enduml\`\`\`## Order Processing FlowThis sequence diagram illustrates the order processing workflow:1. Customer initiates order creation2. Order service validates inventory availability3. Payment is processed4. Order confirmation is sent to customer
```

Example 4 (jsx):
```jsx
---id: architecture-overviewname: Architecture Overviewversion: 1.0.0summary: Miro board showing our system architecture and design decisions---<Miro embedUrl="https://miro.com/app/board/..." />## Architecture OverviewThis Miro board captures our architecture decisions and system design.Key areas covered:- System context- Container architecture- Component relationships- Technology choices
```

---

## Creating domain entities

**URL:** https://www.eventcatalog.dev/docs/domains/entities

**Contents:**
- Creating domain entities
- 📄️ What are entities?
- 📄️ Creating an entity
- 📄️ Adding entities to domains
- 📄️ Visualizing entities

A collection of guides to help you understand entities and how they work with EventCatalog.

What are entities? Why are they useful for event-driven architectures?

Creating and managing entities within EventCatalog.

Creating and managing entities within EventCatalog.

Visualize and explore entity relationships within your domains using EventCatalog's Entity Map feature.

---

## Entity Maps

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/entities/domain-entity-map

**Contents:**
- Entity Maps
- What is the Entity Map?​
- Entity Map Views​
  - Entity Map in the Visualizer​
  - Embed Entity Map as Component​
- How to create references between entities​
  - 1. Create Your Entities​
  - 2. Use Reference Fields in Properties​
  - Example: OrderItem referencing Order​
  - Visual Output​

The Entity Map is a powerful visualization feature in EventCatalog that helps you understand the relationships between entities within your domains. Since entities represent the core building blocks of your domain model, visualizing their connections provides valuable insights into your domain architecture.

The Entity Map is a visual representation that shows how entities are connected within your EventCatalog domains. It displays:

This visualization helps teams understand the domain model at a glance and identify potential architectural improvements.

EventCatalog provides two main ways to view and interact with Entity Maps:

The Entity Map Visualizer is a dedicated page that provides a comprehensive view of all entities within a domain (see demo).

Entities that are referenced in another domain will be shown as yellow.

This full-screen visualization offers:

You can embed the Entity Map of a domain on any page in your catalog using the <EntityMap id="domain-name" /> component (see demo).

This compact version provides:

To define relationships between entities in EventCatalog, follow these steps:

Start by creating your entities in your EventCatalog.

Refer to the entity creation guide for detailed instructions, or you can read the Entity API documentation for more details.

Once your entities are created, you can use optional fields in your entity properties to define relationships between them.

The supported fields are:

More information on the reference fields can be found in the Entity API documentation.

Let’s say you have an OrderItem entity that needs to reference an Order entity:

This configuration generates an entity map that visually shows the relationship between OrderItem and Order.

If you are using Backstage, you can embed the entity map in your Backstage entity page using the <EventCatalogEntityEntityMapCard /> component.

You can read more about how to embed the entity map in Backstage in the Backstage plugin documentation.

**Examples:**

Example 1 (yaml):
```yaml
---id: OrderItemname: OrderItemversion: 1.0.0identifier: orderItemIdsummary: Represents a single item within a customer's order.properties:  - name: orderItemId    type: UUID    required: true    description: Unique identifier for the order item  - name: orderId    type: UUID    required: true    description: Identifier for the parent Order    references: Order    relationType: hasOne    referencesIdentifier: orderId---
```

---

## Creating domains

**URL:** https://www.eventcatalog.dev/docs

**Contents:**
- Creating domains
- 📄️ Creating a domain
- 📄️ Creating subdomains
- 📄️ Adding services to domains

A collection of guides to help you understand domains and how they work with EventCatalog.

Creating and managing domains within EventCatalog.

Creating and managing subdomains within EventCatalog.

Creating and managing domains within EventCatalog.

---

## Adding domain owners

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/ownership-and-language/owners

**Contents:**
- Adding domain owners
- Adding owners to a domain​

You can assign owners to your domains to provide context of who owns this domain and how to contact them.

Owners in EventCatalog are either users or teams and are optional.

To add owners to a domain you need to add them to the owners array within your domain frontmatter API.

Assigning owners to your domains can provide others with context of who owns this domain and how to contact them.

**Examples:**

Example 1 (php):
```php
---id: PaymentDomain... # other domain frontmatterowners:    - dboyne # represents a user    - webTeam # represents a team---<!-- Markdown contents... -->
```

---

## Adding services to domains

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/creating-domains/adding-services-to-domains

**Contents:**
- Adding services to domains
- Adding services using frontmatter​
  - Using semver versioning​
  - Visualizing services within a domain​
- Making changes and versioning​

Adding services to your domains is a great way to group services within a particular domain.

When adding services to your domain EventCatalog will:

To add services within a domain you need to add them to the services array within your domain frontmatter API.

The services frontmatter in your domain tells EventCatalog that these documented services belong to this domain.

In the example above we can see that the services PaymentsService and NotificationsService belong to the PaymentDomain.

You can also use semver to match the version of the service you want to add.

Although it's recommended to link to a version of a service it is now optional. If no version is given latest is used by default.

When you view your domain in EventCatalog, the services will be visualized for you.

You can make as many changes as you want, but if you are adding/removing services you may want to consider versioning your domain. This allows you to keep historic changes, and let others understand why services are coming in/out of a particular domain.

**Examples:**

Example 1 (php):
```php
---id: PaymentDomain... # other domain frontmatterservices:    # id of the service you want to add    - id: PaymentsService    # (optional) The version of the service you want to add.      version: 0.0.1    # Note: version is optional. If no version is given the latest version of the service will be used.    - id: NotificationsService---<!-- Markdown content... -->
```

Example 2 (php):
```php
---id: PaymentDomain... # other domain frontmatterservices:  # Latest minor version of PaymentsService will be added  - id: PaymentsService    version: 0.x.1  # Minor and patches of this version will be linked  - id: NotificationsService    version: ^1.0.1  # Latest version of this service will be shown by default.  - id: PaymentsService---<!-- Markdown contents... -->
```

---

## Ubiquitous language

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/ownership-and-language/adding-ubiquitous-language

**Contents:**
- Ubiquitous language
- Using ubiquitous language in EventCatalog​
  - Viewing the ubiquitous language in EventCatalog​

Ubiquitous Language is a shared language that is used by all stakeholders in a project/domain to improve communication and reduce misunderstandings.

In EventCatalog you can define a dictionary of ubiquitous language terms for your domain, this can help your teams understand the language used in your domain and models used in your architecture.

To add a ubiquitous language dictionary, create a new file within your domain folder with the name ubiquitous-language.mdx.

The contents of the file should be a list of terms used in your domain.

Each term should have a name, summary, description and icon. The icon is optional and can be used to visually represent the term. You can find a list of icons here.

When you add a ubiquitous language dictionary to your domain, it will automatically appear in the sidebar of the domain.

Clicking on a term in the Domain Language explorer will open that term in a new page.

**Examples:**

Example 1 (json):
```json
---dictionary:  - id: Purchase Order    name: Purchase Order    summary: "A mystical document issued by a buyer to a seller, here indicating the types, quantities, and agreed prices for enchanted products or services."    description: |      A purchase order (PO) is a magical document that initiates the buying process between mystical entities. It protects both buyer and seller by clearly documenting the transaction details. Key components include:      - Unique PO number for tracking      - Detailed item specifications and quantities      - Agreed prices and payment terms      - Delivery requirements and timelines      - Terms and conditions of the purchase      POs are essential for budget control, audit trails, and inventory management. They help prevent unauthorized purchases and provide a clear record for accounting and reconciliation purposes.    icon: FileText   - id: Order Line    name: Order Line    summary: "An individual enchanted item within a purchase order, representing a specific magical product or service being ordered."    description: |      Order lines are the fundamental building blocks of any purchase order. Each line represents a distinct item or service and contains critical information for order fulfillment:      - Product identifier (SKU or part number)      - Quantity ordered      - Unit price and total line value      - Special handling instructions      - Required delivery date      Order lines drive warehouse picking operations, shipping processes, and financial calculations. They are essential for tracking partial shipments and managing order modifications.    icon: ListOrdered---
```

---

## Referencing diagrams from resources

**URL:** https://www.eventcatalog.dev/docs/development/guides/diagrams/referencing-diagrams

**Contents:**
- Referencing diagrams from resources
- How diagram references work​
- Referencing diagrams in frontmatter​
- Examples​
  - Referencing diagrams from a domain​
  - Referencing diagrams from a service​
  - Referencing diagrams from a message​
  - Referencing diagrams from a container​
- Diagram versioning in references​
- Organizing diagram references​

One of the key benefits of diagrams in EventCatalog is that they can be referenced from multiple resources. This allows you to create reusable visual documentation that appears in the sidebar of your domains, services, messages, and containers.

When you reference a diagram from a resource, EventCatalog automatically:

To reference diagrams from any resource, use the diagrams field in the frontmatter:

The version field is optional and defaults to latest if not specified.

Domain-level diagrams often show the overall architecture, domain boundaries, or integration patterns.

When users view the E-Commerce domain, they'll see a "Diagrams" section in the sidebar with links to both the "Target Architecture" and "Order Flow" diagrams.

Service-level diagrams typically show API flows, service interactions, or internal component architecture.

Message-level diagrams can show sequence flows, event propagation, or payload structures.

Container-level diagrams often illustrate data models, schema relationships, or access patterns.

You can reference specific versions of diagrams or use latest to always point to the most recent version:

Use specific versions when you want to preserve historical accuracy (e.g., showing the architecture as it was at that resource version). Use latest when the diagram is continuously updated and you always want to show the current state.

For resources with multiple diagrams, organize them logically:

The diagrams will appear in the sidebar in the order you list them.

When viewing a resource that references diagrams, users will see:

The same diagram can be referenced from multiple resources. For example, a "System Context" diagram might be referenced from:

This reusability ensures consistency and reduces duplication while allowing teams to organize documentation in the way that makes most sense for their use case.

**Examples:**

Example 1 (yaml):
```yaml
diagrams:  - id: diagram-id    # version is optional and defaults to latest if not specified    version: 1.0.0
```

Example 2 (powershell):
```powershell
---id: E-Commercename: E-Commerce Domainversion: 1.0.0summary: Core business domain for our e-commerce platformdiagrams:  - id: target-architecture    version: 1.0.0  - id: order-flow    version: 1.0.0---## OverviewThe E-Commerce domain handles all order processing...
```

Example 3 (json):
```json
---id: OrderServicename: Order Serviceversion: 2.0.0summary: Manages order lifecycle and orchestrationdiagrams:  - id: order-api-flow    version: 2.0.0  - id: order-state-machine    version: 1.0.0---## OverviewThe Order Service is responsible for...
```

Example 4 (json):
```json
---id: OrderCreatedname: Order Createdversion: 1.0.0summary: Published when a new order is createddiagrams:  - id: order-creation-flow    version: 1.0.0---## Event DetailsThis event is published when...
```

---

## Using components

**URL:** https://www.eventcatalog.dev/docs/development/components/using-components

**Contents:**
- Using components
  - Example​

EventCatalog uses MDX under the hood. This gives you the ability to include predefined components inside your contents.

You can add components to your domains, services or messages.

You can include any component inside the markdown content. This example renders an Accordion component within an event.

**Examples:**

Example 1 (jsx):
```jsx
---id: OrderAmendedname: Order amendedversion: 0.0.1summary: |  Indicates an order has been changedowners:    - dboyne    - msmithbadges:    - content: Recently updated!      backgroundColor: green      textColor: green    - content: Channel:Apache Kafka      backgroundColor: yellow      textColor: yellow---## OverviewEvent is raised when an order has been changed.<Accordion title="Learn how to raise this event">  You can run the following command to raise this event.  ```sh  bin/kafka-topics.sh --create --topic OrderAmended --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1  ``</Accordion>
```

---

## Diagrams

**URL:** https://www.eventcatalog.dev/docs/category/diagrams

**Contents:**
- Diagrams
- 📄️ Understanding diagrams
- 📄️ Creating diagrams
- 📄️ Referencing diagrams
- 📄️ Versioning diagrams
- 📄️ Comparing diagrams
- 📄️ Diagrams with LLMs

Learn how to document your architecture with reusable diagrams

Bring your own diagrams to EventCatalog - version them, compare them, and assign them to any resource

How to create and organize diagrams in EventCatalog

How to link diagrams to domains, services, messages, and other resources

How to create and manage versioned diagrams in EventCatalog

Side-by-side version comparison for diagrams with EventCatalog Scale

How to use your diagrams with AI assistants and LLM tools

---

## <FigJam />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/embed-diagrams/figjam

**Contents:**
- <FigJam />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The <FigJam /> component renders a FigJam diagram in your documentation.

The <FigJam /> component is supported in domains, services, all messages and custom documentation.

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<FigJam url="{embed_url_from_figjam}" />
```

---

## <DrawIO />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/embed-diagrams/drawio

**Contents:**
- <DrawIO />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The <DrawIO /> component renders a DrawIO diagram in your documentation.

The <DrawIO /> component is supported in domains, services, all messages and custom documentation.

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<DrawIO url="https://viewer.diagrams.net/?border=0&tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20id%3D%22yPxyJZ8AM_hMuL3Unpa9%22%20name%3D%22complex%20gitflow%22%3E7V1dm6I2FP41c6kP4ZvL0dHd7bbbbWf7tNubPhmJSheIhTjj7K9vwoeiiRgREGfZi1kJECDvez5yzoHcaeNg8y6Cq%2BUv2EX%2Bnaq4mzvt4U5VgaIq9D%2FW8pq2mEBLGxaR52YH7Roeve8oPzNrXXsuivcOJBj7xFvtN85wGKIZ2WuDUYRf9g%2BbY3%2F%2Fqiu4QFzD4wz6fOufnkuWWStQlN2O98hbLLNL20a2I4D5wVlDvIQufik0aZM7bRxhTNJfwWaMfDZ4%2Bbik502P7N3eWIRCInPC%2Bs8%2Fwk%2BTB%2FP9xFfhR2Puwg9PAyvt5Rn66%2ByB32My9za0bYyDwCPZvZPXfEAI2tDLjZYk8GkDoD9jEuFvaIx9HNGWEIf0yNHc8%2F2DJuh7i5BuzugNI9o%2BekYR8ehQ32c7As912WVGL0uPoMcVnLFrvlBi0TZMj577yQAu6XGInjDihyAbFdYz2hSasiF5h3CASPRKD8n26qo1VI30rIyilKTp9ssOcDsDcVmAWsvaYEaxxbbzHQr0RwbEGaDYHCgcCsilLM02cUSWeIFD6E92raMIr0MXscso%2B3D9iwh5zQQNrglmY7vt4WeMV9lxKx964eApuYcRCt17Jk07NGnL1GPPlfSfciCXEJ1jxR0dreRfciYdpL%2ByE5ONr2xjaOSbD5vizofX4tZnFHl0lBl%2FksajFIjxOpqhklHONQyB0QJl5zrL0cfPD9%2BxR15WH0bu9%2BnDb9YAZHRgYy5DKdVROUoBcJwrWUefsUcfYUdM%2FXQv6a1nJx6Qbntf1XnoVKDdbB09J6wDZRxEG4%2F8VfhdIADdOsT4JGH4E8rZKisCPKvnOCTZicConX7iAw1J%2BkXIh8R73jdctSun%2FL7LtFOu2H%2BGT8j%2FjGOPeJgp%2BCdMCA4Emp%2BwIedtyp4%2BWcIV6z7YLJinMWS2YLaEERnicMCs8D8RmiOKAxv1feVFT3A9ClCJiaL6aWRMtCkq1Vw12BvV5MQaOLy90Vq1NxKQXiT5QuESCGFRQ5xtcLpiVnIv9aRcK07dgi22JJamD3Vn9%2B%2B6RgUoxvXJVWp%2BdjxhG6%2BFjbMN0zmUO5%2FxzBhNYeD5rN8xJaZHO1OVT%2Bgl27mnwxynXIfVyWy9WyYr19I3b7KOmyaRMZvUY7JMtXsma6s83yCmGkUV3DeLqW2C7mGq1uGGXDzvFXkW5Zr5KB4SmlJSUeag1jK1BHmM6lgXqSlozgXQOKADKicc2F0KNRUnftuJYHar4JQtrkNgtQNhVThhNQTCqqtNCaterxd3QXDgBub6hqw%2BsLrlOBm3Y2RX62jl1%2BE6PRgTO7mLGqRW05yhdaCvbXBlM2t2RnLfYljPkhX12mf%2Fl7GCzwT1on5WIkk3uyfqdi%2FqDYq6IyvqoFuifkNT506KuqF3z6qrfAwfDMFQGVBOIRijBiZXPpqTNzG1snk0%2BVCIqgvgVJuC05IIWZ4bC2klC1NdnZqy6tSSDZq0o06tKvmMGpDJLOp2o9XUw56T0ALmHUuCOzVHP%2FocVks5LGnC2WqnCGf2PtuF0zPATc8088o%2Bm1VLod%2B16y6qC6MlWwJldSssat1QCVQnhdEAeueEMc9%2B3rYwtmxOLdlop9Mt%2F83qo50XSrDTPQkGSs3hzkumZT%2BEN%2B1I5zUV2Rr6luZvfWLzwpowp4PuNG%2FBXfSMfApLH%2Fw8Gvy0eBx1DkcH8Dg2FvvMQ%2Bk%2FUOwzjzacDkt0q7I2v%2B9ej1b1oxTlUP50nS%2FtancmZF3fjeqDm1W0iC6pRTo2G8vvu9ciVb0xADqnRWzeG%2Fvpw%2B%2F3A80YDNAGBmwUVWWOIFlHfXa61EE7RNbgkG03OW3z0ZMvS4Zm5m4HKKk2x2wc4lWU1p4%2FRTCcLW8UaKWKvj4DY4Nzwm3eCW8ZZD458ZWyuyizPaZnYaqbVxdcPouYCu62SKiHtPSlKU5MlWsXCjl8LiqFNH2jZoun6bPRf6Lyay7Idjh6hLlSMO5jMLwfBQqlvu2ALBMR2c1OZj6MY29W5v6e9FzOHuSTc4kTbyrlbRe%2B7E4lktO7hp67UCdecOM%2FwmIIejvoq%2BmPsEiEWHrs0xMECtrSqyGvWaf7ahp5%2FjXJHnkxWipf3aPmCf1zkVf51AbXV%2BPfyOAV%2Fhe4uNPuaVtS1t2A%2BW7uXdkaDLPhKNz76pbAMoM2fS%2Bg8BJagEn58WBS%2BY%2BWiWCy2kVJotijr%2Bw59g2Xm8vtb%2B%2B8DydXlGJBcv%2Fq7zcBUOU1i7645xINYEprgI69y6xI1HL2GqBEA1j8TKoDGoBHteBtqT%2Bet2UD3tsy7Ws7xTJfEmhp2pqXEexKB77eFSoHhGUEUgpz%2Fhj%2BbTyHX7%2FE%2Ftj4BKOPQfTPQDap3s6U2ALcF75MzagaCBP0piuNhUOEw9vHQGWhtxWuHECzKgIv6kttLAIqBF7kzqfpjHgFwz0GmP%2Bt2ef0R0zxDzIdzsxDpsa3%2B%2FMsyBQlyxXMI8RSJtTfow%2FluvRviAmKE3SSRCd8wms2KCRJrawiPEMx243n9E%2BAooUXLthjhEkXRJhTG4qSMGkLHZb0UW4qN6PK5Gbq%2B3KyJYrI8hlVYGpbTVWULdM8LkayBq9M7Qvo6XrPQnbyPNwndCPcPMzao3h4lH7b5uQJelKW1W%2BqQ3P%2F03y6zZNSB7aQlFpTpJR4XbiFEmoRMHWuCFHdV8u8ZImprSZp2i%2FNYAg%2Bsmsf%2BOhH7Cx1eeBr4bAVOyCudKmjOZGTp9Af6X3UavpFL0hXM%2F2MLArj3yBOCJlMGsFqI1THE8hKJig7FgmwqwjFKBlSBaYq1l3PknDB1sof16U3oTVBu1rT0Q9qGoEhmLaqouiCfbbC%2FCNG0a9P%2F7LFoVTFZ9Ge9NTJtgjV9eAigkFCkCgD%2BQVH35IRo%2Bh5dH4Ao9wI7%2BjyziOD9JgdgZSEWuwWfS%2F8ll5pSQhbreqe3aE6DZ89NJxhernpCseMVVM4iNczZrbna3%2BwoL2mJpoa7kGQrqg1TfvMhUW4To1aGPNMuHjiidhxqLEPqltzkpg1RS04VSL4li1blqmmEhu6WaBAKSVyIWYEWEZovqdY6kHxUNXU1Guue%2BC%2B4mmdg1oNHKyBY9tswevBdjF4abTOr0eErqcerG5Aw4u%2FEBy1QfHnfA%2Fxsl8SacQ%2B4JRiavGL6B06r9IBJ0FfupwjXMHrFCN%2FfEr%2FViJOfQyqmvIy%2BPUXBHkxYIq9F7tEsmSn%2B2LXrxuvTB9%2BW%2FcWFvEqXfLxCp%2F2FWtFw%2BTq3xpcuKt0TG4hqX5kxR2qDSb35sg0Oe3FltexDd0Q5NWn9ngyHtejP3Ref7S57I4QV5PXHXtFjIBD%2BY2n1XXVPgxPNFfDSDd3S0CnorpbSFub%2FA8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E" />
```

---

## Domain changelogs

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/versioning-and-changelogs/changelog

**Contents:**
- Domain changelogs
  - Adding a changelog​
  - Why add changelogs?​

EventCatalog supports changelogs for domains, services and messages.

When you version a domain in EventCatalog, you can also attach a changelog.mdx to that domain or version.

Navigate to your change log page for your domain (example /docs/domains/Orders/0.0.2/changelog) or click on the Changelog button on your domain page.

Changelogs are just markdown files, this allows you to add anything you want (e.g code blocks, tables)

EventCatalog code blocks supports diffs, code labels which are great features for changelogs. You can read more here.

Changelogs can provide your team with the context behind the reasons and choices for changes within your domain and also be used for auditing purposes.

Changelogs are visualized by EventCatalog.

**Examples:**

Example 1 (json):
```json
---createdAt: 2024-08-01badges:    - content: ⭐️ JSON Schema      backgroundColor: purple      textColor: purple---### Added new service to the domainAdded the Payment service into the domain.
```

---

## Domain Integration Map

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/domain-integration-map

**Contents:**
- Domain Integration Map
- How it works?​
- How to see the Global Domain Integration Map​

The GlobalDomain Integration Map (see demo) is a powerful visualization feature in EventCatalog that provides a high-level view of your domains, services and messages. It displays domains containing their services, with cross-domain message flows clearly visualized as connections between domains.

This feature is particularly valuable for organizations practicing Domain-Driven Design (DDD) and event-driven architecture, where understanding the interactions between domains is crucial for system design and evolution.

EventCatalog will visualize messages that are being sent between domains in EventCatalog.

As you write domains, services and messages in EventCatalog, some of these communications will be cross domain and boundary. This can be intentional or accidental.

Using the Domain Integration Map, you can see these cross-domain communications and understand the dependencies between domains.

To see the Domain integration map, you need at least one domain in your EventCatalog.

You can a demo of the Domain Integration Map in the EventCatalog Demo.

---

## Adding entities to domains

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/entities/adding-entities-to-domains

**Contents:**
- Adding entities to domains

Once you have created your entities you can add them to your domains.

To add an entity to a domain you need to add the entity to the entities array in the domain's markdown file.

**Examples:**

Example 1 (json):
```json
---id: OrderItemname: OrderItemversion: 1.0.0entities:  - id: OrderItem    version: 1.0.0---Your domain markdown...
```

---

## Common to all messages

**URL:** https://www.eventcatalog.dev/docs/messages/common

**Contents:**
- Common to all messages
- 📄️ Map to producers and consumers
- 📄️ Adding schemas to messages
- 📄️ Deprecating messages
- 📄️ Creating a draft message
- 📄️ Assigning Owners
- 📄️ Versioning messages
- 📄️ Message changelogs
- 📄️ Components
- 📄️ Patterns for shared messages

A collection of guides to help you understand queries and how they work with EventCatalog.

Understanding how to link events to services

Understand how to add schemas to your messages.

Deprecating messages with EventCatalog.

Creating and managing draft messages within EventCatalog.

Adding owners to events with EventCatalog.

Learn how to version events

Adding changelogs to your events

Component list for domains

Understand the patterns for shared messages in EventCatalog.

---

## <Tiles />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/tiles

**Contents:**
- <Tiles />
  - Support​
  - Usage​
  - Rendered example in EventCatalog​
  - Props (<Tiles>)​
  - Props (<Tile>)​

Renders Tiles in EventCatalog, can be great for internal and external links.

The <Tiles/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Add Tiles and Tile component into your markdown of your page.

Tile icons are from hero icons, you can find a list of them here.

See example in the demo EventCatalog application.

**Examples:**

Example 1 (jsx):
```jsx
---# service frontmatter---## OverviewThe subscription Service is responsible for handling customer subscriptions in our system. It handles new subscriptions, cancelling subscriptions and updating them.<Tiles columns={2} >    <!-- Basic example -->    <Tile icon="DocumentIcon" href="/docs"  title="View the docs" description="Dive deeper and view our docs" />    <Tile icon="DocumentIcon" href="/visualiser"  title="View the docs" description="Dive deeper and view our docs" />    <!-- External links and open in new tab -->    <Tile icon="UserGroupIcon" href="https://eventcatalog.dev" openWindow="true" title="Contact EventCatalog" description="Any questions? Visit our website!" />    <!-- Dynamic Link with frontmatter in file -->    <Tile icon="BoltIcon"  href={`/visualiser/services/${frontmatter.id}/${frontmatter.version}`} title={`Receives ${frontmatter.receives.length} messages`} description="This service receives messages to downstream consumers" /></Tiles>
```

---

## <NodeGraph />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/nodegraph

**Contents:**
- <NodeGraph />
- Usage​
  - Single NodeGraph​
    - Output example in EventCatalog​
    - Props​
  - Multiple NodeGraphs​
    - Output example in EventCatalog​
    - Props​

A component to visually render your information.

The <NodeGraph/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

You can add multiple NodeGraphs to your document by using the NodeGraph component multiple times.

Here is an example of how to add multiple NodeGraphs to your document:

You can see a demo of this here

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<NodeGraph/>
```

Example 2 (jsx):
```jsx
---#document frontmatter---<!-- Without any properties, this will render the current pages NodeGraph like you see in the above example --><NodeGraph/><!--  --><div class="grid grid-cols-2 gap-4 not-prose">  <!-- We tell EventCatalog to render the Orders Domain version 0.0.3 NodeGraph -->  <NodeGraph id="Orders" version="0.0.3" type="domain" />  <!-- We tell EventCatalog to render the Subscription Domain version 0.0.1 NodeGraph -->  <NodeGraph id="Subscription" version="0.0.1" type="domain" /></div>
```

---

## Creating channels

**URL:** https://www.eventcatalog.dev/docs/development/guides/channels/adding-channels

**Contents:**
- Creating channels
  - What do channels look like in EventCatalog?​
- Adding a new channel​
  - Creating the channel file​
- Using parameters in channel names​
    - Example output using the <ChannelInformation /> component​
- Using protocols in channels​

Adding a channel to your Catalog is a great way for you to document how messages are transported between producers and consumers.

To add a new channel create a new folder called channels and then add your channel files to it.

Channels can be defined in any folder you like. This let's you group channels by domains, service, teams anything you want.

Within your channel folder you will need to create an index.mdx file.

The index.mdx contents are split into two sections, frontmatter and the markdown content.

Here is an example of what a channel markdown file may look like. You can read the API docs for the channel front matter API

Once you add your new channel to EventCatalog, it will now show in the catalog.

With channels you can write any Markdown you want and it will render on your page. Every channel gets its own page.

Within your markdown content you can use components to add interactive components to your page.

If you want to see some examples you can look at the EventCatalog demo on GitHub.

You may have some channel names/addresses that are dynamic. For example address: inventory.{env}.events.

The channel address: inventory.{env}.events shows us the channel name is dynamic with the given parameter env.

In your channel you can document your parameters, give them values, default values and descriptions.

Once this information is defined, it can then be rendered on your page using the <ChannelInformation /> component.

Your channel can have one or many protocols. To define a protocol you add the property to your channel.

These protocols will be displayed on your channel page and the visualizer.

You can get the list of protocols here.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your channel, used for slugs and references in EventCatalog.# this channel is using dynamic naming using parametersid: inventory.{env}.events# Display name of the Channel, rendered in EventCatalogname: Inventory channel# Version of the Channelversion: 0.0.1# Short summary of your Channelsummary: |  Central event stream for all inventory-related events including stock updates, allocations, and adjustments# Optional owners, references teams or usersowners:    - dboyne# Address of the channel, this example shows a kafka address with parameters, but it can be anythingaddress: inventory.{env}.events# optionally document the params for your channel name# here we know that the channel address "env" value can be "dev,stg,or prod"parameters:  env:    enum:      - dev      - stg      - prod    description: 'Environment to use'---### OverviewThe Inventory Events channel is the central stream for all inventory-related events across the system. This includes stock level changes, inventory allocations, adjustments, and stocktake events. Events for a specific SKU are guaranteed to be processed in sequence when using productId as the partition key.<!-- Shows channel information on the page including a table of all your params and their values --><ChannelInformation /><!-- Rest of markdown -->
```

Example 2 (yaml):
```yaml
---# channel markdown file.# The dynamic addressaddress: inventory.{env}.events# optionally document the params for your channel name# here we know that the channel address "env" value can be "dev,stg,or prod"parameters:  env:    # What values for the parameter? (optional)    enum:      - dev      - stg      - prod    # what is the default value (optional)    default: dev    # Any examples if you want to list them    examples:       - dev      - stg      - prod    # Describe the channel information (optional)    description: 'Environment to use'---
```

Example 3 (yaml):
```yaml
---id: inventory.{env}.events# rest of channel markdown...# You can define one or many protocols# list of protocols: https://eventcatalog.dev/docs/development/guides/channels/introduction#protocolsprotocols:  - http  - kafka  - mqtt---
```

---

## Adding flows to domains

**URL:** https://www.eventcatalog.dev/docs/development/guides/flows/adding-flows-to-domains

**Contents:**
- Adding flows to domains
- Adding flows using frontmatter​

Adding flows to your domains helps document which business processes or workflows belong to a particular domain.

When adding flows to your domain EventCatalog will:

To add flows to a domain you need to add them to the flows array within your domain frontmatter API.

The flows frontmatter in your domain tells EventCatalog that these documented flows belong to this domain.

In the example above we can see that the flows OrderProcessing and PaymentFlow belong to the OrdersDomain.

**Examples:**

Example 1 (php):
```php
---id: OrdersDomain... # other domain frontmatterflows:    # id of the flow you want to add    - id: OrderProcessing    # (optional) The version of the flow you want to add.      version: 1.0.0    # Note: version is optional. If no version is given the latest version of the flow will be used.    - id: PaymentFlow---<!-- Markdown content... -->
```

---

## Function: getUbiquitousLanguageFromDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getUbiquitousLanguageFromDomain

**Contents:**
- Function: getUbiquitousLanguageFromDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getUbiquitousLanguageFromDomain(directory): (id, version?) => Promise<{ markdown: any; }>

Defined in: domains.ts:269

Returns the ubiquitous language dictionary from a domain.

Optionally specify a version to get the ubiquitous language dictionary from a specific version of the domain.

Promise<{ markdown: any; }>

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getUbiquitousLanguageFromDomain } = utils('/path/to/eventcatalog');const ubiquitousLanguage = await getUbiquitousLanguageFromDomain('Payment');// Returns the ubiquitous language dictionary from a specific version of the domainconst ubiquitousLanguage = await getUbiquitousLanguageFromDomain('Payment', '0.0.1');
```

---

## Function: addEntityToDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addEntityToDomain

**Contents:**
- Function: addEntityToDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addEntityToDomain(directory): (id, entity, version?) => Promise<void>

Defined in: domains.ts:410

Add an entity to a domain by its id. Optionally specify a version to add the entity to a specific version of the domain.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';// Adds an entity to the domainconst { addEntityToDomain } = utils('/path/to/eventcatalog');// Adds an entity (User) to the domain (Orders)await addEntityToDomain('Orders', { id: 'User', version: '1.0.0' });// Adds an entity (Product) to the domain (Orders) with a specific versionawait addEntityToDomain('Orders', { id: 'Product', version: '2.0.0' }, '1.0.0');
```

---

## Documentation to Design

**URL:** https://www.eventcatalog.dev/docs/development/design/intro

**Contents:**
- Documentation to Design
  - How EventCatalog Studio works​

When you document your architecture with EventCatalog, you can use your architecture primitives (your domains, services, messages, channels, schemas, etc) to create designs of business workflows, and explore new ideas with your teams using our drag and drop editor (EventCatalog Studio).

This can be useful if you want to share new ideas with your teams, or document end to end business workflows in your organization using a drag and drop interface. This means your developers, architects and business stakeholders can all work together to create workflows or designs together and embed them back into your documentation.

EventCatalog Studio is a drag and drop editor that lets you create designs (.ecstudio files) with your architecture primitives.

You can embed these designs back into your documentation using the <Design /> component.

---

## Function: rmDomainById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmDomainById

**Contents:**
- Function: rmDomainById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmDomainById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: domains.ts:198

Delete a domain by it's id.

Optionally specify a version to delete a specific version of the domain.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmDomainById } = utils('/path/to/eventcatalog');// deletes the latest Payment eventawait rmDomainById('Payment');// deletes a specific version of the Payment eventawait rmDomainById('Payment', '0.0.1');
```

---

## <EntityMap />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/03a-entitymap

**Contents:**
- <EntityMap />
- Usage​
    - Output example in EventCatalog​
    - Props​
    - Filter Entities​

A component to visually render a domain's entity map.

The <EntityMap/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

To visualize entities you need to create entities in EventCatalog and assign them to your services or domains.

The <EntityMap/> component will render all entities by default for a given domain.

If you want to render a subset of the entities in the map, you can use the entities prop.

In this example, only the Order and Customer entities will be chosen to be rendered in the map.

If the Order or Customer entity references other entities, they will also be rendered in the map

**Examples:**

Example 1 (jsx):
```jsx
---id: OrdersDomainversion: 1.0.0// rest of your domain frontmatter---## Entity MapThis is an entity map for the Orders domain. It shows the entities and their relationships with external entities in this domain.<EntityMap title="Orders Domain Entity Map" />
```

Example 2 (jsx):
```jsx
---# event frontmatter---<EntityMap id="OrdersDomain" title="Orders Domain Entity Map" entities={["Order", "Customer"]} />
```

---

## <AccordionGroup />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/accordian-group

**Contents:**
- <AccordionGroup />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The accordion group component renders a collection of accordions.

The <AccordionGroup/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Add code inside the Accordion to render code snippets.

**Examples:**

Example 1 (jsx):
```jsx
---#event frontmatter---<AccordionGroup>  <Accordion title="Example 1">Hello</Accordion>  <Accordion title="Example 2">Hello this is an example</Accordion>  <Accordion title="Example 3">Another example</Accordion>  <Accordion title="Example 4">Final example</Accordion></AccordionGroup>
```

Example 2 (jsx):
```jsx
---#event frontmatter---<AccordionGroup>  <Accordion title="Code snippet 1">    ```js    console.log('My code here');    ``  </Accordion>  <Accordion title="Code snippet 2">  ```js    console.log('My other code snippet');  ``  </Accordion>  <Accordion title="Schema example">  ```json  { "test": true}  ``  </Accordion></AccordionGroup>
```

---

## <Design />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/design

**Contents:**
- <Design />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​

The Design component is a EventCatalog component that will render a EventCatalog Studio diagram into your markdown page.

The <Design/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Simply include the <Design/> component in your markdown with a file path to your EventCatalog Studio diagram.

With Custom Title and Height

When you use the <Design /> component, it will render the diagram in your EventCatalog page.

**Examples:**

Example 1 (jsx):
```jsx
---# event frontmatter---The User Registered event is triggered when a new user signs up for our platform.<Design file="event-stream-example" search={false} />
```

Example 2 (jsx):
```jsx
---# event frontmatter---Here's our payment schema fetched directly from our API gateway:<Design   file="event-stream-example"   title="Event Stream Example"  maxHeight="600"/>
```

---

## <Tabs />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/tabs

**Contents:**
- <Tabs />
  - Support​
  - Usage​
  - Rendered example in EventCatalog​

The <Tabs /> component is a EventCatalog component that will render a tabs into your markdown page.

The <Tabs/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Add Tabs and TabItems into your markdown file.

Example with code as child

See example in the demo EventCatalog application.

**Examples:**

Example 1 (jsx):
```jsx
---# channel frontmatter---<Tabs>  <TabItem title="Tab 1">    This is the content for tab 1  </TabItem>  <TabItem title="Tab 2">    This is the content for tab 2  </TabItem></Tabs>
```

Example 2 (jsx):
```jsx
---# channel frontmatter---<Tabs>  <TabItem title="Tab 1">    ``sh    This is the content for tab 1    ``  </TabItem>  <TabItem title="Tab 2">    ``js    console.log('This is the content for tab 2');    ``  </TabItem></Tabs>
```

---

## Fundamentals

**URL:** https://www.eventcatalog.dev/docs/development/getting-started/fundamentals

**Contents:**
- Fundamentals
  - Docs-as-code​
- Ready to build?​

EventCatalog allows you to document your domains, services, messages (events, commands, queries), data stores, diagrams, schemas, specifications and more.

You can manually document these resources or you can automate the documentation process using EventCatalog integrations (e.g. OpenAPI, AsyncAPI, GraphQL or schema registries), it's up to you.

EventCatalog is flexible and can fit any workflow you have. Deploy it once a day, or 100 times a day. Connect it to external systems like schema registries, API management platforms, or your own custom integrations.

EventCatalog is powered by markdown files (MDX) and can be used in any markdown editor or IDE.

EventCatalog is a docs-as-code tool. This means you can store your documentation in your existing Git repository, version it, and use your existing workflows to review and merge changes.

EventCatalog does not force you to use a specific broker, schema format, or stack. You can use it with any broker, schema format, or stack and can fit into any workflow you have. EventCatalog fits your workflow, not the other way around.

Now that you understand the fundamentals, get started with EventCatalog.

---

## Creating domains

**URL:** https://www.eventcatalog.dev/docs/development/guides/domains/creating-domains/adding-domains

**Contents:**
- Creating domains
  - What do domains look like in EventCatalog?​
- Adding a new domain​
- Adding content​
- Using components​

Domains are a great way to group your documentation into logical units that can be represented in your organization.

EventCatalog Domains are inspired by the Domain-Driven Design approach.

In EventCatalog a domain is a logical unit that contains related services, entities and other resources.

To add a new domain create a new folder within the /domains folder with an index.mdx file.

The index.mdx contents are split into two sections, frontmatter and the markdown content.

Here is an example of what a domain markdown file may look like.

Once you add your domain it will appear in your catalog.

Your domain page will render the markdown content you add to the file. To add content to your domain page, add markdown to the file.

EventCatalog supports MDX under the hood. This gives you the ability to use components inside your domain page.

You can find a list of EventCatalog components you can use here: EventCatalog components.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your domain, used for slugs and references in EventCatalog.id: Orders# Display name of the domain, rendered in EventCatalogname: Orders# Version of the domainversion: 0.0.1# Short summary of your domainsummary: |  Domain that contains order related information# Optional owners, references teams or usersowners:    - dboyne# Optional services. Groups services into this domain.services:    - id: PaymentService      version: 0.0.1# Optional flows associated with this domainflows:    - id: OrderProcessing      version: 1.0.0# Optional badges, rendered to UI by EventCatalogbadges:    - content: New domain      backgroundColor: blue      textColor: blue---## OverviewDomain that contains all services that are related to the orders domain within FakeCompany.<NodeGraph />
```

Example 2 (jsx):
```jsx
---id: Ordersversion: 0.0.1name: Orders---## OverviewThis is your domain markdown....You can add anything here...Including EventCatalog components<NodeGraph />
```

---

## Function: versionDomain()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionDomain

**Contents:**
- Function: versionDomain()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

versionDomain(directory): (id) => Promise<void>

Defined in: domains.ts:161

Version a domain by it's id.

Takes the latest domain and moves it to a versioned directory. All files with this domain are also versioned. (e.g /domains/Payment/openapi.yml)

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionDomain } = utils('/path/to/eventcatalog');// moves the latest Payment domain to a versioned directory// the version within that domain is used as the version number.await versionDomain('Payment');
```

---

## Versioning & changelogs

**URL:** https://www.eventcatalog.dev/docs/ownership-and-language

**Contents:**
- Versioning & changelogs
- 📄️ Adding domain owners
- 📄️ Ubiquitous language

Adding owners to domains with EventCatalog.

Creating a Ubiquitous-language dictionary for your domain

---
