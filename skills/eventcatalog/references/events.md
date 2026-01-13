# Eventcatalog - Events

**Pages:** 154

---

## Queries

**URL:** https://www.eventcatalog.dev/docs/queries

**Contents:**
- Queries
- 📄️ What are queries?
- 📄️ Creating a query

A collection of guides to help you understand queries and how they work with EventCatalog.

What are queries? Why are they useful for event-driven architectures?

Creating and managing queries within EventCatalog.

---

## Overview

**URL:** https://www.eventcatalog.dev/docs/development/guides/messages/overview

**Contents:**
- Overview
  - Linking messages to services and channels​

EventCatalog supports different types of messages (commands, events and queries).

---

## Getting started

**URL:** https://www.eventcatalog.dev/docs/development/ask-your-architecture/mcp-server/getting-started

**Contents:**
- Getting started
  - Prerequisites​
  - Quick start​
  - Verify the server​
  - Connect clients​
- Available tools​
  - 15 built-in tools​
  - 12 resources​
- Add custom tools​
- Use standalone server​

Your MCP server is available at:

For local development:

Visit the endpoint in your browser to verify. It returns available tools and resources:

See full API documentation →

Extend the MCP server with custom tools in eventcatalog.chat.js:

Custom tools appear alongside built-in tools automatically.

For catalogs without SSR mode, use the standalone @eventcatalog/mcp-server package. We plan to deprecate this in a future release, so we recommend migrating to the built-in server when possible.

For local development and testing, you can use the MCP Server on stdio. This is useful for single-client, low-latency tools.

Run the MCP Server over HTTP for production deployments.

This starts the MCP Server over HTTP on port 3000 with root path /mcp.

See instructions on the GitHub repository.

**Examples:**

Example 1 (yaml):
```yaml
https://your-eventcatalog.com/docs/mcp/
```

Example 2 (yaml):
```yaml
http://localhost:3000/docs/mcp/
```

Example 3 (json):
```json
{  "name": "EventCatalog MCP Server",  "version": "1.0.0",  "status": "running",  "tools": ["getResources", "getResource", ...],  "resources": ["eventcatalog://all", "eventcatalog://events", ...]}
```

Example 4 (bash):
```bash
claude mcp add --transport http <name> <url>
```

---

## Function: getCustomDoc()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getCustomDoc

**Contents:**
- Function: getCustomDoc()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getCustomDoc(directory): (filePath) => Promise<CustomDoc>

Defined in: custom-docs.ts:24

Returns a custom doc from EventCatalog by the given file path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getCustomDoc } = utils('/path/to/eventcatalog');// Gets the custom doc by the given file pathconst customDoc = await getCustomDoc('/guides/inventory-management.mdx');
```

---

## Function: writeCommand()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/writeCommand

**Contents:**
- Function: writeCommand()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

writeCommand(directory): (command, options) => Promise<void>

Defined in: commands.ts:121

Write a command to EventCatalog.

You can optionally override the path of the command.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { writeCommand } = utils('/path/to/eventcatalog');// Write a command to the catalog// Command would be written to commands/UpdateInventoryawait writeCommand({  id: 'UpdateInventory',  name: 'Update Inventory',  version: '0.0.1',  summary: 'This is a summary',  markdown: '# Hello world',});// Write a command to the catalog but override the path// Command would be written to commands/Inventory/UpdateInventoryawait writeCommand({   id: 'UpdateInventory',   name: 'Update Inventory',   version: '0.0.1',   summary: 'This is a summary',   markdown: '# Hello world',}, { path: "/Inventory/UpdateInventory"});// Write a command to the catalog and override the existing content (if there is any)await writeCommand({   id: 'UpdateInventory',   name: 'Update Inventory',   version: '0.0.1',   summary: 'This is a summary',   markdown: '# Hello world',}, { override: true });// Write a command to the catalog and version the previous version// only works if the new version is greater than the previous versionawait writeCommand({   id: 'UpdateInventory',   name: 'Update Inventory',   version: '0.0.1',   summary: 'This is a summary',   markdown: '# Hello world',}, { versionExistingContent: true });
```

---

## Customize Visualizer

**URL:** https://www.eventcatalog.dev/docs/customize-visualizer

**Contents:**
- Customize Visualizer
- 📄️ Customize nodes

A collection of guides to help you customize the visualizer in your catalog.

Customize the color, label and icon of the visualizer nodes.

---

## Function: getChannels()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getChannels

**Contents:**
- Function: getChannels()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getChannels(directory): (options?) => Promise<Channel[]>

Defined in: channels.ts:52

Returns all channels from EventCatalog.

You can optionally specify if you want to get the latest version of the channels.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getChannels } = utils('/path/to/eventcatalog');// Gets all channels (and versions) from the catalogconst channels = await getChannels();// Gets all channels (only latest version) from the catalogconst channels = await getChannels({ latestOnly: true });
```

---

## Function: queryHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/queryHasVersion

**Contents:**
- Function: queryHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

queryHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: queries.ts:313

Check to see if the catalog has a version for the given query.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { queryHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given event and version (supports semver)await queryHasVersion('GetOrder', '0.0.1');await queryHasVersion('GetOrder', 'latest');await queryHasVersion('GetOrder', '0.0.x');*
```

---

## Enabling authentication

**URL:** https://www.eventcatalog.dev/docs/development/authentication/enabling-authentication

**Contents:**
- Enabling authentication
  - Setup Environment​
    - AUTH_TRUST_HOST​
  - Enable EventCatalog Server Side Rendering (SSR)​
  - Create your eventcatalog.auth.js file​
  - Setting up your authentication providers​
  - Setting up GitHub
  - Setting up Google
  - Setting up Azure AD
  - Setting up Okta

To enable authentication for your site, you will need to do three things:

Authentication is a paid feature, and is available on EventCatalog Scale and Enterprise plans.

You can get a 14 day free trial of EventCatalog Scale and Enterprise here.

You will need to set your license key in your .env file.

EventCatalog uses Auth.js to handle the authentication flow.

Auth.js libraries require you to set an AUTH_SECRET environment variable. This is used to encrypt cookies and tokens. It should be a cryptographically secure random string of at least 32 characters:

This is the only strictly required environment variable. It is the secret used to encode the JWT and encrypt things in transit. We recommend at least a 32 character random string. This can be generated via openssl with openssl rand -base64 33.

When deploying your application behind a reverse proxy, you’ll need to set AUTH_TRUST_HOST equal to true. This tells Auth.js to trust the X-Forwarded-Host header from the reverse proxy. Auth.js will automatically infer this to be true if we detect the environment variable indicating that your application is running on one of the supported hosting providers. Currently VERCEL and CF_PAGES (Cloudflare Pages) are supported.

To learn more about Auth.js, please refer to the Auth.js documentation.

Authentication requires EventCatalog to be SSR enabled. This is because EventCatalog needs to be able to access the user's session to determine if they are authenticated.

To enable SSR, you will need to add the following to your eventcatalog.config.js file:

This will ensure that EventCatalog is rendered on the server side, and that the user's session is available to the client.

You will be running EventCatalog in SSR mode when you deploy your site. This means the output of your site will require a server to be running. You can use EventCatalog Docker file to deploy your site or read our deployment guide for more information.

The eventcatalog.auth.js file is used to configure the authentication for your site, and is created in the root of your EventCatalog project.

Once you have these three things, you can start setting up your authentication providers.

EventCatalog supports a range of authentication providers, and you can find the documentation for each provider below.

Missing a provider? Let us know and we'll add it to the list.

**Examples:**

Example 1 (unknown):
```unknown
EVENTCATALOG_LICENSE_KEY=your-license-key
```

Example 2 (unknown):
```unknown
AUTH_SECRET=your-secret
```

Example 3 (unknown):
```unknown
module.exports = {  // ... other config options  output: 'server',};
```

Example 4 (css):
```css
module.exports = {  // Enable debug mode for development  debug: false,  // List of providers you want to enable  providers: {    github: {      clientId: process.env.GITHUB_CLIENT_ID,      clientSecret: process.env.GITHUB_CLIENT_SECRET,    },  },  // Optional session configuration  session?: {    // 30 days default    maxAge?: number;  };};
```

---

## Using nodes

**URL:** https://www.eventcatalog.dev/docs/studio/diagrams/using-nodes

**Contents:**
- Using nodes
  - How to add nodes to your diagram​
  - Editing node values​
  - Editing label between nodes​
  - Quickly finding nodes in your diagram​
  - Node Definitions​

Nodes in EventCatalog Studio are the building blocks of your diagram.

To add a node to your diagram, click the highlighted button in the diagram. This will open a sidebar with all the available nodes.

Then you can drag and drop the node onto your diagram, and start to connect nodes together.

To edit the values of a node, click on the node on the canvas, and click the Edit button.

Each node has a different set of values that can be edited, once you made your changes, click the Save button to save your changes.

We are working on adding more node types, and more values that can be edited (e.g Schemas to Message nodes)

If we are missing a node type or a value that you need, please raise an issue or join our Discord community to let us know.

By default, the label between nodes is created by EventCatalog Studio, based on the node types and values.

To edit the label between nodes, click on the text between the nodes, and start typing.

To quickly find a node in your diagram, you can use the canvas selector from the sidebar.

List of nodes and what they are used for.

---

## Deployment guides

**URL:** https://www.eventcatalog.dev/docs/development/deployment

**Contents:**
- Deployment guides
- 📄️ Build (Static Mode)
- 📄️ Build (SSR Mode)
- 📄️ Deployment Workflows
- 📄️ License Validation
- 📄️ Hosting

This section contains deployment tutorials for developers. This includes tutorials for deploying to Heroku, AWS, and other cloud providers.

This document describes step by step how to deploy EventCatalog.

This document describes step by step how to deploy EventCatalog.

This document describes different deployment workflows for EventCatalog.

This document describes how EventCatalog licenses work online and offline.

This document describes hosting options for EventCatalog.

---

## Providers

**URL:** https://www.eventcatalog.dev/docs/development/authentication/providers

**Contents:**
- Providers
- 📄️ GitHub
- 📄️ Google
- 📄️ Azure AD (Entra ID)
- 📄️ Okta
- 📄️ Auth0

Authentication for EventCatalog

Setting up GitHub authentication for EventCatalog

Setting up Google authentication for EventCatalog

Setting up Microsoft Entra ID authentication for EventCatalog

Setting up Okta authentication for EventCatalog

Setting up Auth0 authentication for EventCatalog

---

## Function: getQuery()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getQuery

**Contents:**
- Function: getQuery()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getQuery(directory): (id, version?, options?) => Promise<Query>

Defined in: queries.ts:37

Returns a query from EventCatalog.

You can optionally specify a version to get a specific version of the query

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getQuery } = utils('/path/to/eventcatalog');// Gets the latest version of the eventconst event = await getQuery('GetOrder');// Gets a version of the eventconst event = await getQuery('GetOrder', '0.0.1');// Gets the query with the schema attachedconst event = await getQuery('GetOrder', '0.0.1', { attachSchema: true });
```

---

## Creating users

**URL:** https://www.eventcatalog.dev/docs/development/guides/owners/users/adding-users

**Contents:**
- Creating users
  - What do users look like in EventCatalog?​
- Adding a new user​
- Adding content​
  - Tips for user content​

Adding a user to your Catalog is a great way to add an owner for a domain, service or message.

To add a new user, create a new file within the /users folder with an md file.

The md contents are split into two sections, frontmatter and the markdown content.

Here is an example of what a user markdown file may look like.

Once you add your new user to EventCatalog, it will now show in the docs.

With users you can write any Markdown you want and it will render on your page. Every command gets its own page.

Users do not support custom components.

It's entirely up to you what you want to add to your users markdown content but here are a few things you might want to consider.

**Examples:**

Example 1 (php):
```php
---# id of the userid: dboyne# display name for the username: David Boyne# URL path for a profile imageavatarUrl: "https://pbs.twimg.com/profile_images/1262283153563140096/DYRDqKg6_400x400.png"# users role in the companyrole: Lead developer# optional user email addressemail: test@test.com# optional slack link to DM the userslackDirectMessageUrl: https://yourteam.slack.com/channels/boyney123---## Overview<!-- Contents about the user -->
```

---

## Function: versionCommand()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionCommand

**Contents:**
- Function: versionCommand()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

versionCommand(directory): (id) => Promise<void>

Defined in: commands.ts:231

Version a command by it's id.

Takes the latest command and moves it to a versioned directory. All files with this command are also versioned (e.g /commands/UpdateInventory/schema.json)

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionCommand } = utils('/path/to/eventcatalog');// moves the latest UpdateInventory command to a versioned directory// the version within that command is used as the version number.await versionCommand('UpdateInventory');
```

---

## Ownership & components

**URL:** https://www.eventcatalog.dev/docs/data/ownership-and-components

**Contents:**
- Ownership & components
- 📄️ Owners
- 📄️ Components

A collection of guides to help you understand entities and how they work with EventCatalog.

Adding owners to data stores with EventCatalog.

Component list for data stores

---

## Function: getMessageBySchemaPath()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getMessageBySchemaPath

**Contents:**
- Function: getMessageBySchemaPath()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getMessageBySchemaPath(directory): (path, options?) => Promise<Message>

Defined in: messages.ts:24

Returns a message from EventCatalog by a given schema path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getMessageBySchemaPath } = utils('/path/to/eventcatalog');// Get the message by the schema pathconst message = await getMessageBySchemaPath('/path/to/eventcatalog/messages/InventoryAdjusted/schema.json');const message = await getMessageBySchemaPath('/path/to/eventcatalog/messages/InventoryAdjusted/schema.avro');
```

---

## <ChannelInformation />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/channel-information

**Contents:**
- <ChannelInformation />
  - Support​
  - Usage​
  - Rendered example in EventCatalog​

The ChannelInformation component is a EventCatalog component that will render a table into your markdown page that contains information about the Channel.

The <ChannelInformation/> component is supported in channels.

Add ChannelInformation into your markdown file.

See example in the demo EventCatalog application.

**Examples:**

Example 1 (jsx):
```jsx
---# channel frontmatter---<ChannelInformation />
```

---

## Building Eventcatalog

**URL:** https://www.eventcatalog.dev/docs/development/deployment/build-ssr-mode

**Contents:**
- Building Eventcatalog
  - How it works​
- Building your EventCatalog (SSR)​
- Deployment​

You can also use EventCatalog in SSR mode, which means you can use EventCatalog as a server-side rendered application.

This can be useful for large catalogs, or for users with slow deployment times.

Certain features like Authentication and EventCatalog Chat require SSR mode.

Rather than building the entire catalog into HTML files, EventCatalog will render the pages on the fly (using server-side rendering).

This means you can use EventCatalog as a server-side rendered application.

First you need to update your eventcatalog.config.js file to use SSR mode.

Next you need to build your EventCatalog

This will output one directory

You will need to deploy your EventCatalog to a server that can run Node.js.

The easiest way to do this is to use a docker container.

**Examples:**

Example 1 (vue):
```vue
export default {  // defaults to static  output: 'server', }
```

Example 2 (bash):
```bash
npm run build
```

---

## Adding comments

**URL:** https://www.eventcatalog.dev/docs/studio/diagrams/adding-comments

**Contents:**
- Adding comments
  - How to add comments to your diagram​
  - Closing threads​
  - Deleting comments​

EventCatalog Studio allows you to add comments to your diagram, and create threads between you and your team.

Comments can be used to capture conversations, thoughts, and feedback on your diagram.

To add a comment to your diagram, drag the Comment node onto your diagram.

After the initial comment is made, anyone can reply to the comment, and create a thread of conversation.

Comments are stored against your design, which are local and can be exported when you export your design.

EventCatalog Studio is privacy-first, and your designs stay local by default. Nothing is stored in the cloud.

You can click the Tick icon on the top right of the comment thread to close the thread.

You may want to close a thread if the conversation is complete, or if the comment is no longer relevant.

You can delete a comment by hovering over a comment and clicking the Trash icon.

---

## Function: getConsumersOfSchema()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getConsumersOfSchema

**Contents:**
- Function: getConsumersOfSchema()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getConsumersOfSchema(directory): (path) => Promise<Service[]>

Defined in: messages.ts:142

Returns the consumers of a given schema path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getConsumersOfSchema } = utils('/path/to/eventcatalog');// Returns the consumers of a given schema pathconst consumers = await getConsumersOfSchema('events/InventoryAdjusted/schema.json');
```

---

## Upgrading EventCatalog

**URL:** https://www.eventcatalog.dev/docs/development/upgrading

**Contents:**
- Upgrading EventCatalog
- Upgrade to latest version​
  - Manual upgrade​
  - Having problems?​
- Upgrading from v1 to v2​
- Migrating to version 2​
- Resources now require ids​
    - Example​
- Resources require a flat structure​
- Change to build output​

To upgrade your EventCatalog to the latest version you can run the following command in your catalog directory.

To upgrade your EventCatalog you can find the packages @eventcatalog/core your package.json file.

Once you upgrade the version number, run npm install to install the latest updates.

If you don't see the changes you expect, try removing the .eventcatalog-core folder, node_modules folder and install fresh again.

Trying to upgrade and having issues? Try these steps

If you are upgrading from EventCatalog v1 to v2 you can follow the instructions below.

If you are using v1.x.x then this guide can help you.

Still using v1 of EventCatalog? V1 documentation can be found at https://v1.eventcatalog.dev/

You can find the code for v1 on the branch https://github.com/event-catalog/eventcatalog/tree/v1

We recommended to upgrade to v2 as support for v1 changes will be reduced.

EventCatalog v2 has been rewritten from the ground up. The easiest way to migrate to version 2 is following these steps:

If you are still having issues upgrading your catalog, then please raise an issue on our GitHub repo..

All domains, services and events need an id property in the frontmatter. EventCatalog uses this id as the slug of the page and uses it as internal references.

In EventCatalog v1 you could nest your resources for example have your events or services within your domains folder. (Example /domains/services/MyService/index.mdx)

This feature is not currently supported in version 2.

Version 2 requires your domains, services and messages (commands, and events) to be in the root directory.

The build output has changed from v1 from being out directory to dist directory in version 2.

Customizing your catalog is not currently supported in v2, although this is on our roadmap (July 2024).

EventCatalog v1 supports generators (from EventBridge and AsyncAPI).

EventCatalog v2 does not support these yet and are on the roadmap (July 2024).

Components from v1 has not yet been implemented.

If you have any issues or questions please feel free to reach us on Discord.

**Examples:**

Example 1 (bash):
```bash
npm install @eventcatalog/core@latest
```

Example 2 (json):
```json
{  "name": "my-catalog",  "version": "0.0.1",  "private": true,  "scripts": {    ...  },  "dependencies": {    // Using "latest" will install the latest version of EventCatalog keeping you up to date    // or you can specify a specific version like "@eventcatalog/core": "2.4.0"    "@eventcatalog/core": "latest"  }}
```

Example 3 (php):
```php
---# id is now required on all resources (domains, services and messages)id: order-servicename: Order Service# rest of frontmatter..---<!-- Your markdown content -->
```

---

## Versioning & lifecycle

**URL:** https://www.eventcatalog.dev/docs/channels/versioning-and-lifecycle

**Contents:**
- Versioning & lifecycle
- 📄️ Versioning
- 📄️ Adding a changelog

A collection of guides to help you understand entities and how they work with EventCatalog.

Learn how to version channels

Adding changelogs to your channels

---

## AI Reviewer

**URL:** https://www.eventcatalog.dev/docs/development/developer-tools/github-action

**Contents:**
- AI Reviewer
  - Functionality​
  - Task: Automated schema reviews​
    - Setup​
    - Configuration options​
    - Got an issue?​

The EventCatalog GitHub Action brings AI-powered insight into your Git workflows. It uses large language models (LLMs) to automatically review changes to your EventCatalog, helping you catch issues early—before they reach production. You can pick from OpenAI, Anthropic, or Google.

Think of it as a smart assistant for your pull requests. It doesn't just lint code—it understands the implications of your changes.

By automating the review process, this GitHub Action saves your team hours of manual effort, reduces human error, and brings consistency to your EventCatalog maintenance.

You’re always in control—the final merge decision is still up to you. But now, you’ll have the insights to make it with confidence.

The GitHub action supports many different tasks, and you can use the same action for multiple tasks.

More tasks will be added in the future

The schema review task is used to review schemas for breaking changes. This task let's you catch breaking changes in your schemas before they are deployed.

The schema review supports any schema format, including (JSON, Avro, Protobuf, Thrift, etc.).

Why use the schema review task?

The GitHub action requires an EventCatalog Scale License. You can get a 14 day free trial from EventCatalog Cloud.

Set your EventCatalog Scale License key in the license_key parameter. We recommend storing the license_key value as a GitHub secret.

To use the EventCatalog GitHub Action, create a new .github/workflows/eventcatalog-ci.yaml file in your repository with the following content:

If you have any issues with the GitHub action, please open an issue on the GitHub action repository.

**Examples:**

Example 1 (yaml):
```yaml
name: EventCatalog CIon:  push:  pull_request:    types: [opened, synchronize, reopened, labeled, unlabeled]  delete:permissions:  contents: read  pull-requests: writejobs:  schema_review:    runs-on: ubuntu-latest    steps:      - uses: actions/checkout@v4      - uses: event-catalog/github-action@main        with:          # The task to run, currently only schema_review is supported          task: schema_review          # The AI LLM provider to use (openai, anthropic, google)          provider: openai          # The model to use for the task, defaults to o4-mini          # Find the models in the documentation below          model: o4-mini          # Your API KEY for the LLM provider          api_key: ${{ secrets.OPENAI_API_KEY }}                    # Your EventCatalog Scale License key          license_key: ${{ secrets.EVENT_CATALOG_LICENSE_KEY }}          # Your GitHub token          github_token: ${{ secrets.GITHUB_TOKEN }}
```

---

## Function: versionChannel()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionChannel

**Contents:**
- Function: versionChannel()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

versionChannel(directory): (id) => Promise<void>

Defined in: channels.ts:179

Version a channel by it's id.

Takes the latest channel and moves it to a versioned directory.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionChannel } = utils('/path/to/eventcatalog');// moves the latest inventory.{env}.events channel to a versioned directory// the version within that channel is used as the version number.await versionChannel('inventory.{env}.events');
```

---

## Documenting your architecture

**URL:** https://www.eventcatalog.dev/docs/guides

**Contents:**
- Documenting your architecture
- 🗃️ Domains
- 🗃️ Services
- 🗃️ Messages
- 🗃️ Channels
- 🗃️ Schemas & Specifications
- 🗃️ Diagrams
- 🗃️ Data Stores
- 🗃️ Flows
- 🗃️ Teams & Users

A collection of guides for EventCatalog.

Bring your own documentation to EventCatalog

Customize your docs sidebar to show your own content.

---

## Function: rmQuery()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmQuery

**Contents:**
- Function: rmQuery()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmQuery(directory): (path) => Promise<void>

Defined in: queries.ts:187

Delete a query at it's given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmQuery } = utils('/path/to/eventcatalog');// removes an query at the given path (queries dir is appended to the given path)// Removes the query at queries/GetOrdersawait rmQuery('/GetOrders');
```

---

## What is MDX?

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-components/what-is-mdx

**Contents:**
- What is MDX?
- How to refer to frontmatter in your documentation​
- How to use variables in your documentation​

EventCatalog uses MDX file format for documentation.

Markdown is what powers EventCatalog, we encourage and follow a docs-as-code approach. This lets you write documentation in your favorite IDE and version control system, review changes, merge and deploy them.

Using MDX gives you powerful features like:

You can refer to your frontmatter in your documentation using the frontmatter variable.

MDX supports using the export statements to add variables to your documentation.

For example you can export a title field from an MDX page or component and use it as a heading.

**Examples:**

Example 1 (php):
```php
---id: MyEventname: My Eventversion: 1.0.0summary: My Event Summary---<!-- This will render My Event --># {frontmatter.name}<!-- This will render My Event Summary -->{frontmatter.summary}
```

Example 2 (javascript):
```javascript
---id: MyEventname: My Eventversion: 1.0.0summary: My Event Summary---<!-- This will export the variable title -->export const title = "My Event"<!-- This will render the title --># {title}
```

---

## Commands

**URL:** https://www.eventcatalog.dev/docs/commands

**Contents:**
- Commands
- 📄️ What are commands?
- 📄️ Creating a command

A collection of guides to help you understand commands and how they work with EventCatalog.

What are commands? Why are they useful for event-driven architectures?

Creating and managing commands within EventCatalog.

---

## Setting up Azure AD (Entra ID)

**URL:** https://www.eventcatalog.dev/docs/development/authentication/providers/setting-up-azure-ad

**Contents:**
- Setting up Azure AD (Entra ID)
- Create a new Azure app registration​
- Configure the Azure app in EventCatalog​
- Test the authentication​
- Found an issue?​

This guide takes your through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you've first gone through Enabling authentication.

To setup your EventCatalog site with visitor authentication using Microsoft Entra ID (formerly Azure Active Directory), the process looks as follows:

First, you will need to create a new app registration in the Azure portal.

Add your Azure AD Client ID, Client Secret, and Tenant ID to your .env file.

Your Azure AD tenant ID can be found in your app registration's Overview page in the Azure portal.

In your eventcatalog.auth.js file, add the following:

Restart your EventCatalog server and test the authentication.

All pages should now be protected and require a Microsoft account to access.

Remember to setup the prerequisites for this guide:

If you still have problems, please let us know.

**Examples:**

Example 1 (unknown):
```unknown
AUTH_MICROSOFT_ENTRA_ID_ID={YOUR_AZURE_CLIENT_ID}AUTH_MICROSOFT_ENTRA_ID_SECRET={YOUR_AZURE_CLIENT_SECRET}AUTH_MICROSOFT_ENTRA_ID_ISSUER=https://login.microsoftonline.com/{YOUR_AZURE_TENANT_ID}/v2.0
```

Example 2 (vue):
```vue
export default {  enabled: true,  providers: {    entra: {      clientId: process.env.AUTH_MICROSOFT_ENTRA_ID_ID,      clientSecret: process.env.AUTH_MICROSOFT_ENTRA_ID_SECRET,      issuer: process.env.AUTH_MICROSOFT_ENTRA_ID_ISSUER,    },  },};
```

Example 3 (bash):
```bash
npm run dev
```

---

## Using mermaid

**URL:** https://www.eventcatalog.dev/docs/development/components/mermaid

**Contents:**
- Using mermaid
- Using mermaid in EventCatalog​
  - Using the mermaid code block in any markdown file.​
    - Example​
  - Loading Mermaid files into your EventCatalog page.​
- Architecture diagrams with mermaid​
    - Example​
- Architecture diagrams with icons​
- Mermaid with ELK (Eclipse Layout Kernel) layout algorithm​
- Interactive controls​

EventCatalog supports mermaid (v11.x) in all your markdown files.

This let's you create Class Diagrams, Sequence Diagrams, Entity Relationship Diagrams, Architecture Diagrams and much more.

There are two ways to use mermaid in EventCatalog.

To use mermaid you need to use the mermaid code block in any markdown file.

This example will output the following in the markdown file.

You can load Mermaid files using the <MermaidFileLoader /> component, if you prefer to use a file instead of a code block.

Add your .mmd or .mermaid file to your folder (e.g /events/MyEvent/mermaid.mmd)

This example will load a mermaid file (.mmd or .mermaid) into your EventCatalog page.

The file must be in the same directory as the markdown file.

Mermaid 11 introduced the ability to create architecture diagrams.

You can use these diagrams to document your architecture.

This example will output the following in the markdown file.

EventCatalog supports over 200,000 icons from icones.js.org.

To add icon support you need to add the icon pack into your eventcatalog.config.js file.

In this example above we import the icon pack logos from icones.js.org, but you can import any icon pack you like from icones.js.org.

To use the icons in your mermaid diagrams you need to prefix the icon name with pack name.

In this example we are using the logos pack, so we prefix the icon name with logos:.

EventCatalog will then import the icons from the icon pack and render them in the diagram.

EventCatalog supports the ELK (Eclipse Layout Kernel) layout algorithm for mermaid diagrams.

To add support for the ELK layout algorithm you need to add the following to your eventcatalog.config.js file.

After you set the value, mermaid will be configured to use the ELK layout algorithm.

All Mermaid diagrams include interactive controls for better viewing and exploration.

Click and drag to pan around the diagram, or use the zoom controls in the bottom-left corner to zoom in and out. Double-click the diagram to zoom in quickly.

Click the presentation button in the top-left corner to view the diagram in fullscreen. In presentation mode, mouse wheel zooming is enabled for precise control.

Press Escape to exit presentation mode.

Click the copy button in the top-right corner to copy the diagram code to your clipboard.

Useful for copying diagrams into LLM prompts.

**Examples:**

Example 1 (markdown):
```markdown
```mermaidsequenceDiagram    participant Customer    participant OrdersService    participant InventoryService    participant NotificationService    Customer->>OrdersService: Place Order    OrdersService->>InventoryService: Check Inventory    InventoryService-->>OrdersService: Inventory Available    OrdersService->>InventoryService: Reserve Inventory    OrdersService->>NotificationService: Send Order Confirmation    NotificationService-->>Customer: Order Confirmation    OrdersService->>Customer: Order Placed Successfully    OrdersService->>InventoryService: Update Inventory```_
```

Example 2 (jsx):
```jsx
---#event frontmatter---<!-- Using the .mmd file extension --><MermaidFileLoader file="mermaid.mmd" /><!-- Using the .mermaid file extension --><MermaidFileLoader file="my-second-mermaid-file.mermaid" />
```

Example 3 (markdown):
```markdown
```mermaidarchitecture-beta    group api(cloud)[API]    service db(database)[Database] in api    service disk1(disk)[Storage] in api    service disk2(disk)[Storage] in api    service server(server)[Server] in api    db:L -- R:server    disk1:T -- B:server    disk2:T -- B:db```_
```

Example 4 (css):
```css
// eventcatalog.config.jsmermaid: {  iconPacks: ['logos'] // will load https://icones.js.org/collection/logos into eventcatalog}
```

---

## Function: getTeam()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getTeam

**Contents:**
- Function: getTeam()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getTeam(catalogDir): (id) => Promise<Team>

Defined in: teams.ts:27

Returns a team from EventCatalog.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getTeam } = utils('/path/to/eventcatalog');// Gets the team with the given idconst team = await getTeam('eventcatalog-core-team');
```

---

## Function: addFileToQuery()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addFileToQuery

**Contents:**
- Function: addFileToQuery()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addFileToQuery(directory): (id, file, version?, options?) => Promise<void>

Defined in: queries.ts:253

Add a file to a query by it's id.

Optionally specify a version to add a file to a specific version of the query.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addFileToQuery } = utils('/path/to/eventcatalog');// adds a file to the latest GetOrder queryawait addFileToQuery('GetOrder', { content: 'Hello world', fileName: 'hello.txt' });// adds a file to a specific version of the GetOrder queryawait addFileToQuery('GetOrder', { content: 'Hello world', fileName: 'hello.txt' }, '0.0.1');
```

---

## Function: addMessageToChannel()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addMessageToChannel

**Contents:**
- Function: addMessageToChannel()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addMessageToChannel(directory, collection): (id, _message, version?) => Promise<void>

Defined in: channels.ts:233

Add an event/command/query to a channel by it's id.

Optionally specify a version to add the message to a specific version of the service.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';// Adds an event to the service or command to the serviceconst { addEventToChannel, addCommandToChannel, addQueryToChannel } = utils('/path/to/eventcatalog');// Adds a new event (InventoryUpdatedEvent) that the InventoryService will sendawait addEventToChannel('InventoryService', 'sends', { event: 'InventoryUpdatedEvent', version: '2.0.0' });* // Adds a new event (OrderComplete) that the InventoryService will receiveawait addEventToChannel('InventoryService', 'receives', { event: 'OrderComplete', version: '1.0.0' });// Adds a new command (UpdateInventoryCommand) that the InventoryService will sendawait addCommandToChannel('InventoryService', 'sends', { command: 'UpdateInventoryCommand', version: '2.0.0' });// Adds a new command (VerifyInventory) that the InventoryService will receiveawait addCommandToChannel('InventoryService', 'receives', { command: 'VerifyInventory', version: '1.0.0' });// Adds a new query (GetInventoryQuery) that the InventoryService will sendawait addQueryToChannel('InventoryService', 'sends', { query: 'GetInventoryQuery', version: '2.0.0' });// Adds a new query (GetOrder) that the InventoryService will receiveawait addQueryToChannel('InventoryService', 'receives', { query: 'GetOrder', version: '1.0.0' });
```

---

## Customize landing page

**URL:** https://www.eventcatalog.dev/docs/development/customization/customize-landing-page

**Contents:**
- Customize landing page
  - Example of a custom landing page​
- How to customize your landing page​
  - Using components​

EventCatalog provides a landing page for your catalog, this is the first page that users see when they visit your catalog. See the demo here.

You can customize the landing page with your own content, HTML and EventCatalog components.

Landing page customization is only available for customers on paid plans. You can get a 14 day free trial of EventCatalog Starter Plan on EventCatalog Cloud.

You can add any HTML you want to your landing page, in this example we have added custom content using EventCatalog components, which includes the visualizer for a domains, subdomains and flows.

Astro is a static site builder that powers EventCatalog. You can learn more about Astro here.

Example of homepage.astro

See the example output here

You can use EventCatalog components in your custom landing page.

These include embedding visuals, flows, and more.

You can get a list of components here.

**Examples:**

Example 1 (jsx):
```jsx
---# Import EventCatalog components to use in your landing pageconst { Tile, Tiles, Flow, NodeGraph, Admonition } = Astro.props.components;---<div class="p-8 pt-2 max-w-8xl mx-auto">  <h1 class="text-4xl font-bold text-gray-800 mb-4">Welcome to FlowMart's EventCatalog</h1>  <p class="text-lg text-gray-600 mb-8">Explore the events, services, and domains that power the FlowMart ecosystem. This catalog provides a centralized place to discover and understand our asynchronous architecture.</p>  <Admonition type="info" title="Demo application">    <p>This is a demo of the EventCatalog and what it can do. The company is called FlowMart and they are an e-commerce company.</p>    <p>Using EventCatalog, we documented their systems (domains, services, events, commands, flows) and how they fit together.</p>  </Admonition>  <div class="grid grid-cols-2 gap-4 border-b border-gray-200 pb-8 pt-4">    <div class="col-span-1">      <h2 class="text-2xl font-semibold text-gray-700 mb-2">E-Commerce Domain</h2>      <p class="text-gray-500 mb-2">The core domain of FlowMart, responsible for all e-commerce operations.</p>      <NodeGraph id="E-Commerce" version="1.0.0" type="domain" />    </div>    <div class="col-span-1">      <h2 class="text-2xl font-semibold text-gray-700 mb-2">Orders Domain</h2>      <p class="text-gray-500 mb-2">The sub-domain responsible for all orders.</p>      <NodeGraph id="Orders" version="0.0.3" type="domain" />    </div>    <div class="col-span-1">      <h2 class="text-2xl font-semibold text-gray-700 mb-2">Payment Domain</h2>      <p class="text-gray-500 mb-2">The sub-domain responsible for all payments.</p>      <NodeGraph id="Payment" version="0.0.1" type="domain" />    </div>    <div class="col-span-1">      <h2 class="text-2xl font-semibold text-gray-700 mb-2">Subscription Domain</h2>      <p class="text-gray-500 mb-2">The sub-domain responsible for all subscriptions.</p>      <NodeGraph id="Subscription" version="0.0.1" type="domain" />    </div>  </div>  <div class="bg-blue-50 p-6 rounded-lg shadow-md mb-12">    <h2 class="text-2xl font-semibold text-blue-800 mb-3">Discover Our Architecture</h2>    <p class="text-gray-700 mb-4">      Navigate through our Domains to understand the different business capabilities, explore Services to see the microservices involved, and dive into Events and Commands to see how they communicate.    </p>    <p class="text-gray-700">      Use the search bar above or browse the sections in the sidebar to get started.    </p>  </div>  <div class="grid grid-cols-2 gap-4 border-b border-gray-200 pb-8">    <div class="col-span-1">      <h2 class="text-2xl font-semibold text-gray-700 mb-2">Cancel Subscription Flow</h2>      <p class="text-gray-500 mb-2">This flow is triggered when a user cancels their subscription.</p>      <Flow id="CancelSubscription" version="latest" includeKey={false} />    </div>    <div class="col-span-1">      <h2 class="text-2xl font-semibold text-gray-700 mb-2">Payment Flow</h2>      <p class="text-gray-500 mb-2">This flow documents how a payment is processed at FlowMart.</p>      <Flow id="PaymentFlow" version="latest" includeKey={false} />    </div>  </div>  <div class="border-b border-gray-200 pb-8 py-4">    <h2 class="text-3xl font-semibold text-gray-700 py-4">Quick Links</h2>    <p class="text-gray-700 mb-4">Learn how to get started with EventCatalog, create domains, services, events, and commands.</p>    <Tiles columns={3}>      <Tile icon="BookOpenIcon" href="https://eventcatalog.dev/docs/development/getting-started" title="Getting started with EventCatalog" description="How to get started with EventCatalog" />      <Tile icon="RectangleGroupIcon" href="https://eventcatalog.dev/docs/development/guides/domains/creating-domains/adding-domains" title="Creating domains" description="Learn how to create domains in your event catalog" />      <Tile icon="ServerIcon" href="https://eventcatalog.dev/docs/development/guides/services/adding-services" title="Creating services" description="Learn how to create services in your event catalog" />      <Tile icon="ChatBubbleLeftIcon" iconColor="text-blue-500" href="https://eventcatalog.dev/docs/development/guides/messages/commands/introduction" title="Creating commands" description="Learn how to create commands in your event catalog" />      <Tile icon="BoltIcon" iconColor="text-orange-500" href="https://eventcatalog.dev/docs/development/guides/messages/events/introduction" title="Creating events" description="Learn how to create events in your event catalog" />      <Tile icon="UserGroupIcon" iconColor="text-green-500" href="https://eventcatalog.dev/docs/owners" title="Assigning owners to resources" description="Learn how to assign owners to resources in your event catalog" />    </Tiles>  </div>  <div class="pb-8 py-4">    <h2 class="text-3xl font-semibold text-gray-700 mb-6 pt-4">Join the community</h2>    <p class="text-gray-700 mb-4">Our project and community is growing fast. We have over 1000+ members in our <a href="https://discord.gg/3rjaZMmrAm" class="text-blue-500 hover:text-blue-600">Discord community</a>.</p>    <Tiles columns={2}>      <Tile icon="UserGroupIcon" iconColor="text-green-500" href="https://discord.gg/3rjaZMmrAm" title="Join the Discord community" description="Join the community to get help and support" />      <Tile icon="StarIcon"  iconColor="text-yellow-500" href="https://github.com/event-catalog/eventcatalog/stargazers" title="Star EventCatalog on GitHub" description="If you like the project, please star it on GitHub to show your support ❤️" />    </Tiles>  </div></div>
```

Example 2 (jsx):
```jsx
<Tiles columns={3}>  <Tile icon="BookOpenIcon" href="https://eventcatalog.dev/docs/development/getting-started" title="Getting started with EventCatalog" description="How to get started with EventCatalog" /></Tiles>
```

---

## Function: getCustomDocs()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getCustomDocs

**Contents:**
- Function: getCustomDocs()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getCustomDocs(directory): (options?) => Promise<CustomDoc[]>

Defined in: custom-docs.ts:52

Returns all custom docs for the project.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getCustomDocs } = utils('/path/to/eventcatalog');// Gets all custom docs from the catalogconst customDocs = await getCustomDocs();// Gets all custom docs from the given pathconst customDocs = await getCustomDocs({ path: '/guides' });
```

---

## Function: getUsers()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getUsers

**Contents:**
- Function: getUsers()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getUsers(catalogDir): (options?) => Promise<User[]>

Defined in: users.ts:56

Returns all users from EventCatalog.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getUsers } = utils('/path/to/eventcatalog');// Gets all users from the catalogconst channels = await getUsers();
```

---

## Function: dumpCatalog()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/dumpCatalog

**Contents:**
- Function: dumpCatalog()
- Parameters​
- Returns​
  - Parameters​
  - Returns​

dumpCatalog(directory): (options?) => Promise<EventCatalog>

Defined in: eventcatalog.ts:90

Dumps the catalog to a JSON file.

A JSON file with the catalog.

Promise<EventCatalog>

---

## Teams

**URL:** https://www.eventcatalog.dev/docs/teams

**Contents:**
- Teams
- 📄️ What are teams?
- 📄️ Creating a team

A collection of guides to help you understand teams and how they work with EventCatalog.

What are teams in EventCatalog?

Creating and managing teams within EventCatalog.

---

## Function: rmQueryById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmQueryById

**Contents:**
- Function: rmQueryById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmQueryById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: queries.ts:209

Delete a query by it's id.

Optionally specify a version to delete a specific version of the query.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmQueryById } = utils('/path/to/eventcatalog');// deletes the latest InventoryAdjusted queryawait rmQueryById('GetOrder');// deletes a specific version of the GetOrder queryawait rmQueryById('GetOrder', '0.0.1');
```

---

## Function: rmEntityById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmEntityById

**Contents:**
- Function: rmEntityById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmEntityById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: entities.ts:155

Delete an entity by its id.

Optionally specify a version to delete a specific version of the entity.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmEntityById } = utils('/path/to/eventcatalog');// deletes the latest User entityawait rmEntityById('User');// deletes a specific version of the User entityawait rmEntityById('User', '0.0.1');
```

---

## Client side scripts

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-components/javascript-components

**Contents:**
- Client side scripts

EventCatalog allows you to add client side JavaScript to your components.

Read the astro documentation for more information.

**Examples:**

Example 1 (jsx):
```jsx
---# component template scripts.---<button class="alert">Click me!</button><!-- This script will get called in the browser --><script>  // Find all buttons with the `alert` class on the page.  const buttons = document.querySelectorAll('button.alert');  // Handle clicks on each button.  buttons.forEach((button) => {    button.addEventListener('click', () => {      alert('Button was clicked!');    });  });</script>
```

---

## Ask your architecture

**URL:** https://www.eventcatalog.dev/docs/ask-your-architecture

**Contents:**
- Ask your architecture
- 📄️ Using AI with EventCatalog
- 🗃️ EventCatalog Assistant
- 🗃️ EventCatalog MCP Server

Learn how to integrate your LLM models with EventCatalog.

Architecture documentation for humans and AI

---

## Users

**URL:** https://www.eventcatalog.dev/docs/users

**Contents:**
- Users
- 📄️ What are users?
- 📄️ Creating a user

A collection of guides to help you understand users and how they work with EventCatalog.

What are users in EventCatalog?

Creating and managing users within EventCatalog.

---

## Function: rmEvent()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmEvent

**Contents:**
- Function: rmEvent()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmEvent(directory): (path) => Promise<void>

Defined in: events.ts:186

Delete an event at it's given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmEvent } = utils('/path/to/eventcatalog');// removes an event at the given path (events dir is appended to the given path)// Removes the event at events/InventoryAdjustedawait rmEvent('/InventoryAdjusted');
```

---

## Adding custom documentation

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-documentation/adding-custom-docs

**Contents:**
- Adding custom documentation
- Getting started​
- Adding custom documentation​
  - Creating documentation​
    - Structure of markdown files​
    - Sidebar configuration​
    - Rendered output​
  - Custom HTML attributes​
    - Rendered output​

Custom documentation requires a Starter or Scale plan, you can get a 14 day free trial to test it out at EventCatalog Cloud. Once you have a license key you can start to use the feature.

Custom documentation is split into two parts:

Custom documentation is stored in the /docs folder in your catalog (see example on GitHub), and can be accessed via the url /docs/custom/.

All documentation is a .mdx (markdown ) file. You can organize these however you want, for example:

In this example we have a custom documentation for:

We added numbers (01, 02, 03) to the files to help with maintenance, you can configure the order of the files in your configuration.

Each markdown file is split into two parts:

Frontmatter properties

You need to configure the sidebar to include your custom documentation, we do this by using the customDocs property in your eventcatalog.config.js file.

We have two options for the sidebar:

The autogenerated sidebar is the easiest option, it will render all the files in the directory and subdirectories. If you want to choose which files and order they are displayed in, you can manually map the files and paths to the sidebar.

The rendered output will be the content of the markdown file, with the frontmatter properties.

Links can also include an attrs property to add custom HTML attributes to the link element.

In the following example, attrs is used to add a target="_blank" attribute, so that the link opens in a new tab, and to apply a custom style attribute to italicize the link label:

**Examples:**

Example 1 (unknown):
```unknown
docs/├── architecture-decision-records/│   ├── drafts/│   │   ├── 01-introduction.mdx│   │   ├── 02-example-record.mdx│   ├── published/│   │   ├── 01-introduction.mdx│   │   ├── 02-example-record.mdx│   ├── examples/│   │   ├── 01-introduction.mdx│   │   ├── 02-example-record.mdx├── runbooks/│   ├── 01-introduction.mdx│   ├── 02-deployment-procedure.mdx│   ├── 03-disaster-recovery.mdx│   ├── 04-incident-response.mdx
```

Example 2 (yaml):
```yaml
---title: Creating new microservicessummary: A comprehensive guide to creating new microservices at FlowMart following our best practices and standardsowners:   - dboynebadges:  - content: 'Guide'    backgroundColor: 'teal'    textColor: 'teal'---This is your content for your file.
```

Example 3 (vue):
```vue
export default {  // rest of your config  customDocs: {    sidebar: [      {        label: 'architecture Decision Records',        badge: {          text: 'New', color: 'green'        },        collapsed: false,        items: [          {            // Here we map the directory, and use autogenerated to generate the sidebar items            // Any item added to the folder will be rendered automatically in EventCatalog            label: 'Drafts', autogenerated: { directory: '/architecture-decision-records/drafts' }          },          {            label: 'Published', autogenerated: { directory: '/architecture-decision-records/published' }          },          {            label: 'Examples', autogenerated: { directory: '/architecture-decision-records/examples' }          }        ]      },      {        label: 'Runbooks',        badge: {          text: 'New', color: 'green'        },        collapsed: false,        items: [          {            // Here we create custom pages in the sidebar            // We can manually map the slug to a file, or use the autogenerated to generate the sidebar items            label: 'Creating a new runbook', items: [              { label: 'Introduction', slug: 'runbooks/01-introduction' },              { label: 'Deployment Procedure', slug: 'runbooks/02-deployment-procedure' },              { label: 'Disaster Recovery', slug: 'runbooks/03-disaster-recovery' },              { label: 'Incident Response', slug: 'runbooks/04-incident-response' },            ]          },        ]      }    ]  }};
```

Example 4 (vue):
```vue
export default {  // rest of your config  customDocs: {    sidebar: [      {        label: 'My Links',        items: [          {            label: 'Read more on GitHub',            link: 'https://github.com/event-catalog/eventcatalog',            attrs: { target: '_blank', style: 'font-style: italic;' },          },        ]      },    ]  }};
```

---

## Development and build

**URL:** https://www.eventcatalog.dev/docs/development/getting-started/develop-and-build

**Contents:**
- Development and build
- Edit your project​
- Starting the development server​
- Build and preview your catalog​
- EventCatalog static vs server output​
- Next Steps​

To make changes to your project, open your project folder in your code editor. Working in development mode with the dev server running allows you to see updates to your site as you edit the code.

EventCatalog comes with a built-in development server that has everything you need for project development. The eventcatalog dev CLI command will start the local development server so that you can see your new website in action for the very first time.

Every starter template comes with a pre-configured script that will run eventcatalog dev for you. After navigating into your project directory, run this command and start the EventCatalog development server:

If all goes well, EventCatalog will now be serving your project on http://localhost:3000/. Visit that link in your browser and see your new site!

To check the version of your site that will be created at build time, quit the dev server (Ctrl + C) and run the appropriate build command in your terminal:

EventCatalog will build a deploy-ready version of your site in a separate folder (dist/ by default) and you can watch its progress in the terminal. This will alert you to any build errors in your project before you deploy to production.

When the build is finished, run the appropriate preview command (e.g. npm run preview) in your terminal and you can view the built version of your site locally in the same browser preview window.

Note that this previews your code as it existed when the build command was last run. This is meant to give you a preview of how your site will look when it is deployed to the web. Any later changes you make to your code after building will not be reflected while you preview your site until you run the build command again.

Use (Ctrl + C) to quit the preview and run another terminal command, such as restarting the dev server to go back to working in development mode which does update as you edit to show a live preview of your code changes.

By default, EventCatalog will build a static website. This means you can host this website anywhere you like.

Some features of EventCatalog (e.g SSO) require a to run EventCatalog as a server.

You can opt into which build mode you want to use by setting the output property in your eventcatalog.config.js file.

Success! You are now ready to start building with EventCatalog! 🥳

Here are a few things that we recommend exploring next. You can read them in any order. You can even leave our documentation for a bit and go play in your new EventCatalog project codebase, coming back here whenever you run into trouble or have a question.

**Examples:**

Example 1 (bash):
```bash
npm run dev
```

Example 2 (bash):
```bash
npm run build
```

---

## Function: addSchemaToEvent()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addSchemaToEvent

**Contents:**
- Function: addSchemaToEvent()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addSchemaToEvent(directory): (id, schema, version?, options?) => Promise<void>

Defined in: events.ts:291

Add a schema to an event by it's id.

Optionally specify a version to add a schema to a specific version of the event.

**Examples:**

Example 1 (json):
```json
import utils from '@eventcatalog/utils';const { addFileToEvent } = utils('/path/to/eventcatalog');// JSON schema exampleconst schema = {   "$schema": "http://json-schema.org/draft-07/schema#",   "type": "object",   "properties": {       "name": {       "type": "string"   },   "age": {     "type": "number"   } }, "required": ["name", "age"]};// adds a file to the latest InventoryAdjusted eventawait addFileToEvent('InventoryAdjusted', { schema, fileName: 'schema.json' });// adds a file to a specific version of the InventoryAdjusted eventawait addFileToEvent('InventoryAdjusted', { schema, fileName: 'schema.json' }, '0.0.1');
```

---

## Function: getDataStores()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getDataStores

**Contents:**
- Function: getDataStores()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Examples​

getDataStores(directory): (options?) => Promise<Container[]>

Defined in: data-stores.ts:43

Returns all data stores (e.g. databases, caches, etc.) from EventCatalog.

You can optionally specify if you want to get the latest version of the data stores.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getDataStores } = utils('/path/to/eventcatalog');// Gets all data stores (and versions) from the catalogconst containers = await getDataStores();// Gets all data stores (only latest version) from the catalogconst containers = await getDataStores({ latestOnly: true });
```

Example 2 (python):
```python
import utils from '@eventcatalog/utils';const { getContainers } = utils('/path/to/eventcatalog');// Gets all containers (and versions) from the catalogconst containers = await getContainers();// Gets all entities (only latest version) from the catalogconst containers = await getContainers({ latestOnly: true });
```

---

## Function: getEntity()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getEntity

**Contents:**
- Function: getEntity()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getEntity(directory): (id, version?) => Promise<Entity>

Defined in: entities.ts:27

Returns an entity from EventCatalog.

You can optionally specify a version to get a specific version of the entity

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getEntity } = utils('/path/to/eventcatalog');// Gets the latest version of the entityconst entity = await getEntity('User');// Gets a version of the entityconst entity = await getEntity('User', '0.0.1');
```

---

## Hosting

**URL:** https://www.eventcatalog.dev/docs/development/deployment/hosting-options

**Contents:**
- Hosting
  - Hosting Options​
  - Hosting a static website​
  - Hosting static website with Docker​
  - Hosting as a server​

EventCatalog can be hosted in two ways:

By default EventCatalog will build a static website.

Here are some guides and places you can host static content

EventCatalog comes with a DockerFile you can build the image and deploy the container. The container exposes ports 3000.

To build the docker container you need to run:

First you need to update your eventcatalog.config.js file to use SSR mode.

A server output is required if you are using any EventCatalog feature that requires a server, these include:

You can use the server Docker image to run the server, this is the recommended way to run the server.

First you need to create a Dockerfile for the server (if you don't already have one).

Then you can build the docker image with:

Then you can run the server with:

Some features of EventCatalog require a server to run (e.g. EventCatalog Chat and EventCatalog Authentication).

If you have a large catalog, you may want to use SSR mode to reduce build times.

**Examples:**

Example 1 (bash):
```bash
# Builds the containerdocker build -t eventcatalog .# Runs the container locallydocker run -p 3000:80 -it eventcatalog
```

Example 2 (vue):
```vue
export default {  // defaults to static  output: 'server', }
```

Example 3 (bash):
```bash
FROM node:lts AS runtimeWORKDIR /app# Install dependenciesCOPY package.json package-lock.json ./RUN npm installCOPY . .# Fix for Astro in Docker: https://github.com/withastro/astro/issues/2596ENV NODE_OPTIONS=--max_old_space_size=2048RUN npm run buildENV HOST=0.0.0.0ENV PORT=3000EXPOSE 3000# Start the serverCMD npm run start
```

Example 4 (bash):
```bash
docker build -f Dockerfile.server -t eventcatalog-server .
```

---

## Setting up Okta

**URL:** https://www.eventcatalog.dev/docs/development/authentication/providers/setting-up-okta

**Contents:**
- Setting up Okta
- Create a new Okta OAuth app​
- Configure the OAuth app in EventCatalog​
- Test the authentication​
- Found an issue?​

This guide takes your through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you've first gone through Enabling authentication.

To setup your EventCatalog site with visitor authentication using Okta, the process looks as follows:

First, you will need to create a new Okta OAuth app in your Okta Admin Console.

Add your Okta Client ID, Client Secret, and Issuer to your .env file.

Your Okta issuer URL should be in the format: https://your-domain.okta.com (without /oauth2/default unless you're using a custom authorization server). In your eventcatalog.auth.js file, add the following:

Restart your EventCatalog server and test the authentication.

All pages should now be protected and require an Okta account to access.

Remember to setup the prerequisites for this guide:

If you still have problems, please let us know.

**Examples:**

Example 1 (unknown):
```unknown
AUTH_OKTA_CLIENT_ID={YOUR_OKTA_CLIENT_ID}AUTH_OKTA_CLIENT_SECRET={YOUR_OKTA_CLIENT_SECRET}AUTH_OKTA_ISSUER=https://{YOUR_OKTA_DOMAIN}
```

Example 2 (vue):
```vue
export default {  enabled: true,  providers: {    okta: {      clientId: process.env.AUTH_OKTA_CLIENT_ID,      clientSecret: process.env.AUTH_OKTA_CLIENT_SECRET,      issuer: process.env.AUTH_OKTA_ISSUER,    },  },};
```

Example 3 (bash):
```bash
npm run dev
```

---

## Using Structurizr

**URL:** https://www.eventcatalog.dev/docs/development/components/structurizr

**Contents:**
- Using Structurizr
- How to export your Structurizr diagrams into mermaid files​

You can embed your Structurizr diagrams into your EventCatalog pages using the <MermaidFileLoader /> component.

You will need to export your Structurizr diagrams into mermaid files and then use the <MermaidFileLoader /> component to embed them into your EventCatalog pages.

You will need to use the Structurizr CLI to export your diagrams into mermaid files.

---

## Customize visualizer nodes

**URL:** https://www.eventcatalog.dev/docs/development/customization/customize-visualizer/visualizer-nodes

**Contents:**
- Customize visualizer nodes
    - Rendered output​
  - Configuration​

Every node in the visualizer has a color, label and icon.

The example below shows the default node for a Service resource.

By default the icon, color and label in the node is generated by EventCatalog. Helping you maintain consistency across your catalog.

You can use the styles property to customize the icon, color and label of the node, if you want to customize the node to be more specific to your use case.

**Examples:**

Example 1 (json):
```json
---id: NotificationServiceversion: 0.0.2name: Notification Servicesummary: |  Service that handles ordersstyles:  icon: "BellIcon"  node:     color: purple    label: "Custom"---
```

---

## Customize Sidebars

**URL:** https://www.eventcatalog.dev/docs/customize-sidebars

**Contents:**
- Customize Sidebars
- 📄️ Application Sidebar
- 📄️ Documentation Sidebar

A collection of guides to help you customize the sidebars in your catalog.

Pick and customize the application sidebar.

Pick and customize the documentation sidebar.

---

## Messages

**URL:** https://www.eventcatalog.dev/docs/messages

**Contents:**
- Messages
- 📄️ Overview
- 🗃️ Events
- 🗃️ Commands
- 🗃️ Queries
- 🗃️ Common to all messages

A collection of guides to help you understand commands and how they work with EventCatalog.

What are messags in EventCatalog?

---

## Reusable snippets

**URL:** https://www.eventcatalog.dev/docs/development/components/snippets

**Contents:**
- Reusable snippets
- Creating a Snippet​
- Basic Usage​
- Passing Variables to Snippets​
- Exporting Variables​
- JSX-Based Snippets​

Keep your documentation consistent and maintainable with reusable snippets.

In EventCatalog, staying DRY (Don't Repeat Yourself) isn't just for code—it's for documentation too. If you're repeating the same content across multiple pages, consider using a snippet to centralize it. This makes your docs easier to manage and keeps everything in sync.

Snippets must live in the /snippets directory to be recognized by EventCatalog. Files in this folder won’t generate standalone pages—they’re designed to be imported wherever needed.

Snippets can accept props for dynamic content. Here's how:

You can also export constants or objects from a snippet for use elsewhere.

Need something more dynamic? Use a snippet as a JSX component:

Then import and use it like this:

**Examples:**

Example 1 (unknown):
```unknown
Hello world! This is my content I want to reuse across pages.
```

Example 2 (markdown):
```markdown
---id: E-Commercename: E-Commerceversion: 1.0.0---<!-- Import the snippet from the snippets directory -->import MySnippet from '@eventcatalog/snippets/my-snippet.mdx';<!-- Use the snippet anywhere on your page --><MySnippet />
```

Example 3 (unknown):
```unknown
Hello {props.name}! This is my content I want to reuse across pages.
```

Example 4 (jsx):
```jsx
---id: E-Commercename: E-Commerceversion: 1.0.0---<!-- Import the snippet from the snippets directory -->import MySnippet from '@eventcatalog/snippets/my-snippet.mdx';<!-- Use the snippet with props --><MySnippet name="John" />
```

---

## Schemas & Specifications

**URL:** https://www.eventcatalog.dev/docs/schemas

**Contents:**
- Schemas & Specifications
- 📄️ Getting started
- 📄️ EventCatalog Schema Explorer
- 📄️ Get access to your schemas via API
- 📄️ Connect schemas to your LLMs

A collection of guides to help you understand schemas and how they work with EventCatalog.

Getting started with schemas in EventCatalog

Explore your schemas in the Schema Explorer

Get API (GET) access to your schemas for mocking or testing

Get access to your schemas for your MCP clients (e.g Cursor, Windsurf, Claude Desktop etc)

---

## Import & Export

**URL:** https://www.eventcatalog.dev/docs/studio/diagrams/import-export

**Contents:**
- Import & Export
  - How to import and export your diagram​
  - How to export your diagram​
  - How to import your diagram​

EventCatalog Studio is privacy-first, and your designs stay local by default. Nothing is stored in the cloud.

This means you can import and export your designs, share them with your team and keep them in version control next to your code.

Once you are happy with your diagram, you can export it by clicking the Actions then Save in the navigation bar.

This will let you choose the name of the file and store it as a .ecstudio file on your local machine.

EventCatalog Studio uses the .ecstudio file format to store your diagrams. This is a standard format for EventCatalog Studio.

To import your diagram, click on the Actions then Open in the navigation bar or click the Open Design on your dashboard.

This will let you load .ecstudio files from your local machine into EventCatalog Studio.

When you import a design, you can only import designs that are from the same organization or team.

You can invite other users to your organization to help you import your designs. Read more about managing your organization.

---

## Using diagrams with LLMs

**URL:** https://www.eventcatalog.dev/docs/development/guides/diagrams/diagrams-with-llms

**Contents:**
- Using diagrams with LLMs
- How it works​
- Using with EventCatalog Assistant​
- Using with external LLM tools​
  - Claude, ChatGPT, or other assistants​
  - MCP servers​
  - Custom integrations​
- All versions are accessible​
- Tips for LLM-friendly diagrams​
  - Add context in markdown​

EventCatalog makes your diagrams accessible to AI assistants and LLM tools, enabling you to ask questions about your architecture and get contextual answers.

Every diagram in EventCatalog is available as a markdown file at a .mdx endpoint. This follows the llms.txt convention, making your diagrams consumable by AI tools.

The markdown export includes:

With EventCatalog's AI assistant (Starter/Scale), you can ask questions about your diagrams directly from the diagram page.

Click the "Ask about this diagram" button to open the assistant with context about the current diagram. Example questions:

You can use the .mdx endpoints with any LLM tool that supports fetching content:

Share the .mdx URL directly:

If you're using EventCatalog's MCP server, your diagrams are automatically available to compatible AI tools like Claude Desktop.

Fetch diagram content programmatically:

Every version of your diagram has its own .mdx endpoint:

This lets you ask AI tools to compare versions or explain how your architecture evolved:

To get the most out of AI interactions with your diagrams:

Don't just include the diagram - add explanations:

In your diagrams, use clear, descriptive names:

Explain why components connect, not just that they do:

Markdown export is enabled by default. To disable it, update your eventcatalog.config.js:

When enabled, all resources (including diagrams) are accessible via .mdx endpoints.

**Examples:**

Example 1 (markdown):
```markdown
# Diagram page (rendered)/diagrams/system-overview/1.0.0# Markdown version (for LLMs)/diagrams/system-overview/1.0.0.mdx
```

Example 2 (unknown):
```unknown
Here's my system architecture diagram:https://your-catalog.com/diagrams/system-overview/1.0.0.mdxCan you explain the data flow?
```

Example 3 (bash):
```bash
curl https://your-catalog.com/diagrams/system-overview/1.0.0.mdx
```

Example 4 (unknown):
```unknown
/diagrams/architecture/2.0.0.mdx  # Latest/diagrams/architecture/1.5.0.mdx  # Previous/diagrams/architecture/1.0.0.mdx  # Initial
```

---

## LLMS.txt

**URL:** https://www.eventcatalog.dev/docs/development/developer-tools/llms.txt

**Contents:**
- LLMS.txt
  - What is LLMS.txt?​
  - llms.txt and llms-full.txt​
  - Enable in EventCatalog​
  - How to use LLMS.txt?​

Enable tools like Claude, ChatGPT, GitHub Copilot, and Cursor to quickly understand your EventCatalog.

LLMS.txt is a proposed standard that helps AI-powered development tools better understand and interact with your documentation. Similar to how robots.txt guides web crawlers, LLMS.txt provides structured information that makes it easier for AI assistants like Claude, ChatGPT, and GitHub Copilot to process your EventCatalog documentation.

The file is automatically generated and maintained as part of your documentation pipeline, requiring no manual configuration. It organizes your documentation's key concepts, structures, and relationships in a format optimized for machine reading.

The llms.txt file includes your EventCatalog resources in a simple format. Lists your resources with a summary for each of them.

The llms-full.txt file includes your EventCatalog resources in a more detailed format. All the contents of your Catalog resources are included in the file.

llms.txt is enabled by default in EventCatalog.

You can disable it by turning it off in your eventcatalog.config.js file.

Once you enable llms.txt you can query both the urls:

Once you deploy your EventCatalog you can use your tools to ask questions about your Catalog.

**Examples:**

Example 1 (css):
```css
llmsTxt: {    enabled: false,},
```

---

## Function: rmEntity()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmEntity

**Contents:**
- Function: rmEntity()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmEntity(directory): (path) => Promise<void>

Defined in: entities.ts:133

Delete an entity at its given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmEntity } = utils('/path/to/eventcatalog');// removes an entity at the given path (entities dir is appended to the given path)// Removes the entity at entities/Userawait rmEntity('/User');
```

---

## Bring your own documentation

**URL:** https://www.eventcatalog.dev/docs/development/guides/bring-your-own-documentation

**Contents:**
- Bring your own documentation

EventCatalog provides the ability to extend your catalog and bring your own documentation to EventCatalog.

This allows you to keep all your documentation in one place, rather than having documentation spread across multiple tools.

Some common use cases for custom documentation are:

If you are interested in learning more about custom documentation, you can read the documentation here.

---

## Authentication

**URL:** https://www.eventcatalog.dev/docs/development/guides/auth

**Contents:**
- Authentication
- 📄️ Introduction
- 📄️ Enabling authentication
- 📄️ Role-Based Access Control
- 🗃️ Providers

Authentication for EventCatalog

Introduction to EventCatalog Authentication

Enabling authentication for EventCatalog

Implementing role-based access control with custom middleware in EventCatalog

---

## Documenting your architecture

**URL:** https://www.eventcatalog.dev/docs/guides/

**Contents:**
- Documenting your architecture
- 🗃️ Domains
- 🗃️ Services
- 🗃️ Messages
- 🗃️ Channels
- 🗃️ Schemas & Specifications
- 🗃️ Diagrams
- 🗃️ Data Stores
- 🗃️ Flows
- 🗃️ Teams & Users

A collection of guides for EventCatalog.

Bring your own documentation to EventCatalog

Customize your docs sidebar to show your own content.

---

## Events

**URL:** https://www.eventcatalog.dev/docs/events

**Contents:**
- Events
- 📄️ What are events?
- 📄️ Creating an event

A collection of guides to help you understand events and how they work with EventCatalog.

What are events? Why are they useful for event-driven architectures?

Creating and managing events within EventCatalog.

---

## Function: rmEventById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmEventById

**Contents:**
- Function: rmEventById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmEventById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: events.ts:208

Delete an event by it's id.

Optionally specify a version to delete a specific version of the event.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmEventById } = utils('/path/to/eventcatalog');// deletes the latest InventoryAdjusted eventawait rmEventById('InventoryAdjusted');// deletes a specific version of the InventoryAdjusted eventawait rmEventById('InventoryAdjusted', '0.0.1');
```

---

## Write your own components

**URL:** https://www.eventcatalog.dev/docs/custom-components

**Contents:**
- Write your own components
- 📄️ What is MDX?
- 📄️ What are custom components?
- 📄️ Adding components
- 📄️ Component styling
- 📄️ Client side scripts

A collection of guides to help your understand and build custom components inside your catalog.

Add custom components to your catalog

Adding custom components to your catalog

Adding custom components to your catalog

Adding client side scripts to EventCatalog components

---

## Function: dataStoreHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/dataStoreHasVersion

**Contents:**
- Function: dataStoreHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Examples​

dataStoreHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: data-stores.ts:122

Check to see if the catalog has a version for the given data store (e.g. database, cache, etc.).

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { dataStoreHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given data store and version (supports semver)await dataStoreHasVersion('orders-db', '0.0.1');await dataStoreHasVersion('orders-db', 'latest');await dataStoreHasVersion('orders-db', '0.0.x');
```

Example 2 (python):
```python
import utils from '@eventcatalog/utils';const { containerHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given entity and version (supports semver)await containerHasVersion('orders-db', '0.0.1');await containerHasVersion('orders-db', 'latest');await containerHasVersion('orders-db', '0.0.x');
```

---

## <RemoteSchema />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/remote-schema

**Contents:**
- <RemoteSchema />
  - Support​
  - Usage​
  - Output example in EventCatalog​
  - Props​
  - Environment Variable Support​
  - JSONPath Examples​
  - Error Handling​
  - Benefits for Teams​

The RemoteSchema component fetches and renders schemas from remote URLs at runtime, keeping your documentation automatically synchronized with external schema sources.

Schemas can be fetched from any accessible URL and support authentication headers for private APIs.

The <RemoteSchema/> component fetches schemas at runtime.

This ensures your documentation stays up-to-date with the latest schema versions without manual updates.

The <RemoteSchema/> component only works in Server-Side Rendering (SSR) mode. Make sure your EventCatalog is configured to run in SSR mode to use this component. You can read more about how to configure your EventCatalog to run in SSR mode here.

The <RemoteSchema/> component is supported in domains, services, and all messages, changelogs, and custom documentation pages.

Simply include the <RemoteSchema/> component in your markdown with a URL pointing to your schema.

With Custom Title and Height

Fetching from Private APIs

For private APIs requiring authentication, you can provide headers:

Add your environment variables to the .env file in the root of your EventCatalog project.

The RemoteSchema component will automatically map the environment variables to the template string.

Using JSONPath to Extract Specific Schema Parts

When your API returns nested schemas, use JSONPath to extract specific parts:

Rendering as Raw JSON

Force rendering as raw JSON instead of the schema viewer:

The component automatically detects JSON Schema format and renders an interactive Schema Viewer, or displays raw content for other formats.

The url and headers props support environment variable templating using ${VARIABLE_NAME} syntax:

Add your environment variables to the .env file in the root of your EventCatalog project.

The RemoteSchema component will automatically map the environment variables to the template string.

Extract specific schema definitions from complex API responses using JSONPath.

The component provides clear error messages for common issues:

This component bridges the gap between your live APIs and documentation, ensuring your EventCatalog always reflects the current state of your systems.

**Examples:**

Example 1 (jsx):
```jsx
---# event frontmatter---The User Registered event is triggered when a new user signs up for our platform.<RemoteSchema url="https://api.example.com/schemas/user-registered.json" />
```

Example 2 (jsx):
```jsx
---# event frontmatter---Here's our payment schema fetched directly from our API gateway:<RemoteSchema   url="https://api.example.com/schemas/payment.json"   title="Payment Schema"  maxHeight="600"/>
```

Example 3 (json):
```json
---# event frontmatter---<RemoteSchema   url="https://private-api.example.com/schemas/order.json"  headers={{    "Authorization": "Bearer ${API_TOKEN}",    "X-API-Key": "${API_KEY}"  }}  title="Order Schema"/>
```

Example 4 (jsx):
```jsx
---# event frontmatter---<RemoteSchema   url="https://api.example.com/openapi.json"  jsonPath="$.components.schemas.UserEvent"  title="User Event Schema"/>
```

---

## EventCatalog Licenses

**URL:** https://www.eventcatalog.dev/docs/development/deployment/licenses

**Contents:**
- EventCatalog Licenses
  - How to set up a license keys​
  - How EventCatalog validates licenses keys​
      - Online License Validation (recommended)​
      - Offline License Validation​

EventCatalog is an open source project with a community edition and a commercial edition and also supports a range of integrations (plugins) which have their own licenses.

If you are using the commercial edition of EventCatalog, then you don't need to worry about licenses and can skip this page.

If you are using EventCatalog Starter, EventCatalog Scale, EventCatalog Enterprise or any of the integrations (plugins) you will need to set up a license key.

All licenses have a 14 day free trial. You can get a free trial license key by going to EventCatalog Cloud.

If you wish to continue using the commercial features after the trial period, you will need to purchase a license.

You can email us at hello@eventcatalog.dev to enquire about a license.

By default, EventCatalog will validate your license key online.

Your keys are read from your .env file and verified against our API.

If you are behind a firewall or can't access the EventCatalog API, then your license keys can be validated offline.

To get offline validation working you will need to:

Your key will expire after a year of purchase, and you will need to get a new license key.

---

## Function: rmTeamById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmTeamById

**Contents:**
- Function: rmTeamById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmTeamById(catalogDir): (id) => Promise<void>

Defined in: teams.ts:138

Delete a team by it's id.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmTeamById } = utils('/path/to/eventcatalog');// deletes the EventCatalogCoreTeam teamawait rmTeamById('eventcatalog-core-team');
```

---

## Changelogs

**URL:** https://www.eventcatalog.dev/docs/changelogs

**Contents:**
- Changelogs
- 📄️ What are changelogs?
- 📄️ Creating a changelog
- 📄️ Automated diffs

A collection of guides to help you understand changelogs and how they work with EventCatalog.

Creating and managing changelogs within EventCatalog.

Understanding how EventCatalog automates diffs for your files

---

## Starting a new project

**URL:** https://www.eventcatalog.dev/docs/starting-a-new-project/getting-started

**Contents:**
- Starting a new project
- 📄️ Upgrading EventCatalog
- 📄️ v3
- 📄️ v2

Learn how to install EventCatalog.

How to upgrade EventCatalog.

How to upgrade to EventCatalog v3.

How to upgrade to EventCatalog v2.

---

## Design

**URL:** https://www.eventcatalog.dev/docs/design

**Contents:**
- Design
- 📄️ Documentation to Design
- 📄️ Import Resources into Studio
- 📄️ Embed Designs into EventCatalog
- 📄️ Further Reading

This section describes how to use EventCatalog to design workflows and new ideas.

Documentation to Design with EventCatalog

Import Resources into Studio with EventCatalog

Embed Designs into EventCatalog with EventCatalog

Further Reading with EventCatalog

---

## Upgrade to EventCatalog v2

**URL:** https://www.eventcatalog.dev/docs/development/upgrading/v2

**Contents:**
- Upgrade to EventCatalog v2
- Migrating to version 2​
- Resources now require ids​
    - Example​
- Resources require a flat structure​
- Change to build output​
- Any other issues?​

This guide will help you upgrade from v1 to v2 of EventCatalog.

EventCatalog v2 comes with some small breaking changes to your EventCatalog.

Still using v1 of EventCatalog? V1 documentation can be found at https://v1.eventcatalog.dev/

You can find the code for v1 on the branch https://github.com/event-catalog/eventcatalog/tree/v1

We recommended to upgrade to v2 as support for v1 changes will be reduced.

EventCatalog v2 has been rewritten from the ground up. The easiest way to migrate to version 2 is following these steps:

If you are still having issues upgrading your catalog, then please raise an issue on our GitHub repo..

All domains, services and events need an id property in the frontmatter. EventCatalog uses this id as the slug of the page and uses it as internal references.

In EventCatalog v1 you could nest your resources for example have your events or services within your domains folder. (Example /domains/services/MyService/index.mdx)

This feature is not currently supported in version 2.

Version 2 requires your domains, services and messages (commands, and events) to be in the root directory.

The build output has changed from v1 from being out directory to dist directory in version 2.

If you have any issues or questions please feel free to reach us on Discord.

**Examples:**

Example 1 (php):
```php
---# id is now required on all resources (domains, services and messages)id: order-servicename: Order Service# rest of frontmatter..---<!-- Your markdown content -->
```

---

## Function: getCommand()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getCommand

**Contents:**
- Function: getCommand()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getCommand(directory): (id, version?, options?) => Promise<Command>

Defined in: commands.ts:38

Returns a command from EventCatalog.

You can optionally specify a version to get a specific version of the command

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getCommand } = utils('/path/to/eventcatalog');// Gets the latest version of the commandconst command = await getCommand('UpdateInventory');// Gets a version of the commandconst command = await getCommand('UpdateInventory', '0.0.1');// Gets the command with the schema attachedconst command = await getCommand('UpdateInventory', '0.0.1', { attachSchema: true });
```

---

## Using plantuml

**URL:** https://www.eventcatalog.dev/docs/development/components/plantuml

**Contents:**
- Using plantuml
- Using plantuml in EventCatalog​
    - Example​
  - How it works?​
- Interactive controls​
  - Zoom and pan​
  - Presentation mode​
  - Copy diagram code​
  - More resources​

EventCatalog supports plantuml in all your markdown files.

This let's you create Class Diagrams, Sequence Diagrams, Class Diagrams, State Diagrams and much more.

To use plantuml you need to use the plantuml code block in any markdown file.

This example will output the following in the markdown file.

The PlantUML implementation takes your content and converts it to a PNG image using https://www.plantuml.com/plantuml/svg.

All PlantUML diagrams include interactive controls for better viewing and exploration.

Click and drag to pan around the diagram, or use the zoom controls in the bottom-left corner to zoom in and out. Double-click the diagram to zoom in quickly.

Click the presentation button in the top-left corner to view the diagram in fullscreen. In presentation mode, mouse wheel zooming is enabled for precise control.

Press Escape to exit presentation mode.

Click the copy button in the top-right corner to copy the diagram code to your clipboard.

Useful for copying diagrams into LLM prompts.

**Examples:**

Example 1 (markdown):
```markdown
```plantuml@startuml!define Table(name,desc) class name as "desc" << (T,#E5E7EB) >>!define PK(x) <u>x</u>!define FK(x) <i>x</i>' ===== Core Tables =====Table(Customers, "Customers") {  PK(customerId): UUID  firstName: VARCHAR  lastName: VARCHAR  email: VARCHAR  phone: VARCHAR  dateRegistered: TIMESTAMP}Table(Orders, "Orders") {  PK(orderId): UUID  FK(customerId): UUID  orderDate: TIMESTAMP  status: VARCHAR  totalAmount: DECIMAL}Table(Products, "Products") {  PK(productId): UUID  name: VARCHAR  description: TEXT  price: DECIMAL  stockQuantity: INT}Table(OrderItems, "Order Items") {  PK(id): UUID  FK(orderId): UUID  FK(productId): UUID  quantity: INT  unitPrice: DECIMAL}Table(Payments, "Payments") {  PK(paymentId): UUID  FK(orderId): UUID  amount: DECIMAL  method: VARCHAR  status: VARCHAR  paidAt: TIMESTAMP}Table(InventoryEvents, "Inventory Events") {  PK(eventId): UUID  FK(productId): UUID  eventType: VARCHAR  quantityChange: INT  eventTime: TIMESTAMP}Table(Subscription, "Subscriptions") {  PK(subscriptionId): UUID  FK(customerId): UUID  plan: VARCHAR  status: VARCHAR  startDate: TIMESTAMP  endDate: TIMESTAMP}' ===== Relationships =====Customers ||--o{ Orders : placesOrders ||--o{ OrderItems : containsProducts ||--o{ OrderItems : includesOrders ||--o{ Payments : paid_byProducts ||--o{ InventoryEvents : logsCustomers ||--o{ Subscription : subscribes@enduml```_
```

---

## Setting up GitHub

**URL:** https://www.eventcatalog.dev/docs/development/authentication/providers/setting-up-github

**Contents:**
- Setting up GitHub
- Create a new GitHub OAuth app​
- Configure the OAuth app in EventCatalog​
- Test the authentication​
- Found an issue?​

This guide takes your through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through Enabling authentication.

To setup your EventCatalog site with visitor authentication using GitHub, the process looks as follows:

First, you will need to create a new GitHub OAuth app.

Add your GitHub Client ID and Client Secret to your .env file.

In your eventcatalog.auth.js file, add the following:

Restart your EventCatalog server and test the authentication.

All pages should now be protected and require a GitHub account to access.

Remember to setup the prerequisites for this guide:

If you still have problems, please let us know.

**Examples:**

Example 1 (unknown):
```unknown
AUTH_GITHUB_CLIENT_ID={YOUR_GITHUB_CLIENT_ID}AUTH_GITHUB_CLIENT_SECRET={YOUR_GITHUB_CLIENT_SECRET}
```

Example 2 (vue):
```vue
export default {  providers: {    github: {      clientId: process.env.AUTH_GITHUB_CLIENT_ID,      clientSecret: process.env.AUTH_GITHUB_CLIENT_SECRET,    },  },};
```

Example 3 (bash):
```bash
npm run dev
```

---

## <ResourceLink />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/resource-link

**Contents:**
- <ResourceLink />
  - Support​
  - Usage​
  - Props​

The <ResourceLink/> component renders a link to a resource in EventCatalog.

The <ResourceLink/> component is supported on all EventCatalog pages.

**Examples:**

Example 1 (jsx):
```jsx
---#domain frontmatter---<!-- No version specified, so the latest version is used --><ResourceLink id="InventoryService" type="service" /><!-- Specifying a version, will link to that version of the resource --><ResourceLink id="InventoryService" type="service" version="1.0.0" /><!-- Specifying a child element will render that element as the link text --><ResourceLink id="InventoryService" type="service">This is a custom link</ResourceLink>
```

---

## Teams & Users

**URL:** https://www.eventcatalog.dev/docs/owners

**Contents:**
- Teams & Users
- 🗃️ Teams
- 🗃️ Users

A collection of guides to help you understand owners and how they work with EventCatalog.

---

## Role-Based Access Control (RBAC) Middleware

**URL:** https://www.eventcatalog.dev/docs/development/authentication/rbac-middleware

**Contents:**
- Role-Based Access Control (RBAC) Middleware
- How it works​
- Prerequisites​
- Setting up RBAC Middleware​
  - 1. Create the middleware file​
  - 2. Configure your access rules​
  - 3. Available helper functions​
    - hasRole(role: string)​
    - hasGroup(group: string)​
    - findMatchingRule(rules, pathname)​

EventCatalog supports Role-Based Access Control (RBAC) through custom middleware, allowing you to control user access to specific pages and sections based on their roles and groups.

The RBAC middleware integrates with EventCatalog's authentication system to provide fine-grained access control:

Before setting up RBAC middleware, ensure you have:

Create a middleware.ts file in the root of your EventCatalog project:

The accessRules object defines path-based access control:

The middleware provides several helper functions through locals:

Checks if the user has a specific role:

Checks if the user belongs to a specific group:

Finds the first matching rule for a given pathname using glob patterns:

Control access to specific pages or sections using exact paths or wildcard patterns.

Define access permissions based on user roles with single or multiple role requirements.

Manage access using group membership with inclusion, exclusion, or complex group logic.

Organize access control around your organizational structure, ensuring teams only see documentation relevant to their department.

Create layered access levels where higher privilege users can access all lower-level content.

Control access to specific EventCatalog features based on user roles and responsibilities.

With RBAC middleware configured, you can:

Need help? Join our Discord community for support and best practices from other EventCatalog users.

**Examples:**

Example 1 (typescript):
```typescript
import type { MiddlewareHandler } from 'astro';interface Locals {  hasRole: (role: string) => boolean;  hasGroup: (group: string) => boolean;  findMatchingRule: (rules: Record<string, () => boolean>, pathname: string) => (() => boolean) | null;}export const rbacMiddleware: MiddlewareHandler = async (context, next) => {  const { locals, url } = context;  const pathname = url.pathname;  // Utility functions are available in the locals object  const { hasRole, hasGroup, findMatchingRule } = locals as Locals;  // Define your access rules  // Maps page routes to a function that returns true if the user has access, false otherwise  // You can use wildcards to match multiple paths  const accessRules = {    '/docs/domains/E-Commerce/*': () => !hasGroup('Viewer'),    '/visualiser/domains/E-Commerce/*': () => !hasGroup('Viewer'),    '/docs/services/payment/*': () => hasRole('Developer') || hasRole('Admin'),    '/admin/*': () => hasRole('Admin'),  };  if (findMatchingRule) {    // Find matching rule for the current path    const rule = findMatchingRule(accessRules, pathname);    if (rule && !rule()) {      return new Response('Forbidden', { status: 403 });    }  }  return next();};
```

Example 2 (typescript):
```typescript
const accessRules = {  // Block 'Viewer' group from E-Commerce domain docs  '/docs/domains/E-Commerce/*': () => !hasGroup('Viewer'),    // Require 'Developer' or 'Admin' role for payment services  '/docs/services/payment/*': () => hasRole('Developer') || hasRole('Admin'),    // Admin-only sections  '/admin/*': () => hasRole('Admin'),    // Multiple conditions  '/docs/sensitive/*': () => hasRole('Admin') && !hasGroup('External'),};
```

Example 3 (typescript):
```typescript
hasRole('Admin')        // Returns true if user has Admin rolehasRole('Developer')    // Returns true if user has Developer role
```

Example 4 (typescript):
```typescript
hasGroup('Viewer')      // Returns true if user is in Viewer grouphasGroup('External')    // Returns true if user is in External group
```

---

## Adding schemas to data stores

**URL:** https://www.eventcatalog.dev/docs/development/guides/data/03a-adding-schemas-to-data-stores

**Contents:**
- Adding schemas to data stores
- Using codeblocks to render your schema​
- Using the <Schema/> component to render your schema from a file​

EventCatalog supports any schema format.

When you document your data stores, you may want to also include schemas, queries, or other files that are relevant to your data store.

You can attach this information in two ways:

You can use codeblocks to render your schema in your markdown files.

Here is an example of a SQL codeblock:

You can learn more about codeblocks and configuring them in the codeblocks documentation.

If you prefer to have your schemas, or information about your data store in a file, you can use the <Schema/> component to render your schema from a file.

First you need to add your file in the directory of your data store

You can an example of this in the EventCatalog Demo.

Remember everything in EventCatalog can be versioned. So when your data store changes you can version your data stores, and write changes logs to help your teams understand what has changed.

**Examples:**

Example 1 (sql):
```sql
```sql  CREATE TABLE users (    id INT PRIMARY KEY,    name VARCHAR(255),    email VARCHAR(255)  );```_
```

Example 2 (jsx):
```jsx
<!-- Render the file into your page --><Schema file="schema.sql" lang="sql" title="Users Table" /><!-- Render the schemas separately in an AccordionGroup --><AccordionGroup>  <Accordion title="Users Table">    <!-- Load the schema from the file -->    <Schema file="schema.sql" lang="sql" title="Users Table" />  </Accordion>  <Accordion title="Common Queries">    <!-- Load the queries from the file -->    <Schema file="queries.sql" lang="sql" title="Common Queries" />  </Accordion></AccordionGroup>
```

---

## Schema Explorer

**URL:** https://www.eventcatalog.dev/docs/development/guides/schemas/schema-explorer

**Contents:**
- Schema Explorer
  - How to use the Schema Explorer?​
      - Filters​
      - Schema Preview​
      - API Access​
      - Producers and Consumers​
  - Turn off the Schema Explorer​

The Schema Explorer is a powerful tool that allows your team to quickly find, filter and understand your schemas in your Architecture (see demo).

Your teams can quickly find the schema, who owns it, who is producing or consuming it and get API (GET) access to your schemas for mocking or testing.

The schema explorer supports any schema format, including JSON, YAML, Avro, Protobuf, GraphQL, OpenAPI, AsyncAPI, etc.

Using the Schema Explorer, you can:

You can access the Schema Explorer from the sidebar, or by going to the /schemas/explorer page.

The page will take all the schemas from your EventCatalog and render them in a searchable list.

You need to set the schemaPath in your schema frontmatter to the path to your schema file for Events, Queries and Commands.

For services you need to specify the path to your specification file in the specifications frontmatter.

The Schema Explorer is a powerful tool that allows your team to quickly find and understand your schemas in your Architecture (see demo). The schema explorer supports any schema format, including JSON, YAML, Avro, Protobuf, GraphQL, OpenAPI, AsyncAPI, etc.

You can use the filters to quickly find schemas in your Architecture. You can filter by name, message type and schema format.

The schema preview will show you a preview of the schema in a readable format, you can use the Schema button to switch between different views of your schema (if they are supported, JSON or Avro).

For EventCatalog Scale users, you can get API (GET) access to your schemas for mocking or testing.

The producers and consumers section will show you who is producing or consuming the schema. You can click on the producer or consumer to see more information about them.

You can hide the Schema Explorer by setting the it's visibility to false in your eventcatalog.config.js file.

**Examples:**

Example 1 (css):
```css
module.exports = {  sidebar: [    {        id: '/schemas/explorer',        visible: false,    }  ]};
```

---

## Function: rmCustomDoc()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmCustomDoc

**Contents:**
- Function: rmCustomDoc()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmCustomDoc(directory): (filePath) => Promise<void>

Defined in: custom-docs.ts:122

Delete a custom doc by its' path

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmCustomDoc } = utils('/path/to/eventcatalog');// removes a custom doc at the given path// Removes the custom doc at docs/guides/inventory-management/introduction.mdxawait rmCustomDoc('/guides/inventory-management/introduction');
```

---

## Function: addFileToCommand()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addFileToCommand

**Contents:**
- Function: addFileToCommand()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addFileToCommand(directory): (id, file, version?, options?) => Promise<void>

Defined in: commands.ts:253

Add a file to a command by it's id.

Optionally specify a version to add a file to a specific version of the command.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addFileToCommand } = utils('/path/to/eventcatalog');// adds a file to the latest UpdateInventory commandawait addFileToCommand('UpdateInventory', { content: 'Hello world', fileName: 'hello.txt' });// adds a file to a specific version of the UpdateInventory commandawait addFileToCommand('UpdateInventory', { content: 'Hello world', fileName: 'hello.txt' }, '0.0.1');
```

---

## Function: getUser()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getUser

**Contents:**
- Function: getUser()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getUser(catalogDir): (id) => Promise<User>

Defined in: users.ts:24

Returns a user from EventCatalog.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getUser } = utils('/path/to/eventcatalog');// Gets the user with the given idconst user = await getUser('eventcatalog-core-user');
```

---

## AI with EventCatalog

**URL:** https://www.eventcatalog.dev/docs/development/ask-your-architecture/intro

**Contents:**
- AI with EventCatalog

EventCatalog helps you document your architecture for both teams and your AI tools. Your team gets a visual catalog to explore your system. Your AI tools get structured access to query and reason about your architecture.

---

## Function: channelHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/channelHasVersion

**Contents:**
- Function: channelHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

channelHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: channels.ts:197

Check to see if the catalog has a version for the given channel.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { channelHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given event and version (supports semver)await channelHasVersion('inventory.{env}.events', '0.0.1');await channelHasVersion('inventory.{env}.events', 'latest');await channelHasVersion('inventory.{env}.events', '0.0.x');*
```

---

## Comparing diagram versions (Scale)

**URL:** https://www.eventcatalog.dev/docs/development/guides/diagrams/comparing-diagrams

**Contents:**
- Comparing diagram versions (Scale)
- When to use diagram comparison​
- Accessing diagram comparison​
  - Steps to compare​
- Example use cases​
  - Comparing migration states​
  - Tracking architectural evolution​
  - Reviewing sequence flow changes​
- Comparison UI features​
- Best practices​

Diagram comparison is available exclusively with the EventCatalog Scale license. This feature enables side-by-side visualization of different diagram versions.

The diagram comparison feature allows you to view two versions of a diagram side-by-side, making it easy to understand architectural changes and evolution over time.

Diagram comparison is valuable for:

When viewing a diagram that has multiple versions, you'll see a "Compare diagram versions" button in the header (only available with Scale license).

Compare your current monolithic architecture with your target microservices architecture:

Version 1.0.0 (Current State):

Version 2.0.0 (Target State):

Viewing these side-by-side helps teams understand the scope of the migration and communicate the changes to stakeholders.

Compare different iterations of your architecture as it evolves:

Compare how a business flow has changed between versions:

Version 1.0.0 - Synchronous Order Flow: Shows direct HTTP calls between services

Version 2.0.0 - Event-Driven Order Flow: Shows asynchronous event-based communication

This makes it clear how the system's behavior and coupling has evolved.

The comparison view provides:

When creating diagrams you plan to compare:

In your diagram content, call out the key differences:

**Examples:**

Example 1 (php):
```php
---id: order-flowname: Order Processing Flowversion: 2.0.0summary: Event-driven order processing (updated for async architecture)---## What Changed in v2.0.0Compared to version 1.0.0, this flow now uses event-driven architecture:- **Removed**: Synchronous HTTP calls between services- **Added**: Kafka event stream for service communication- **Changed**: Order Service now publishes OrderCreated event instead of calling downstream services directly- **Benefit**: Improved resilience and scalability_```mermaidsequenceDiagram    Customer->>OrderService: Place Order    OrderService->>Kafka: Publish OrderCreated    Kafka->>InventoryService: OrderCreated Event    Kafka->>PaymentService: OrderCreated Event```_
```

---

## Project structure

**URL:** https://www.eventcatalog.dev/docs/development/getting-started/project-structure

**Contents:**
- Project structure
- Directories and Files​
- Project structure options​

Your new EventCatalog project generated from the create eventcatalog CLI wizard already includes some files and folders. Others, you will create yourself and add to EventCatalog’s existing file structure.

---

## Components

**URL:** https://www.eventcatalog.dev/docs/components

**Contents:**
- Components
- 📄️ Introduction
- 📄️ Embed Mermaid Diagrams
- 📄️ Embed PlantUML Diagrams
- 📄️ Embed Structurizr Diagrams
- 📄️ Embed IcePanel Diagrams
- 📄️ Reusable snippets
- 🗃️ Components

This section describes what components can be used in EventCatalog..

Understanding components

Understanding how to use mermaid with EventCatalog

Understanding how to use plantuml with EventCatalog

Understanding how to use Structurizr with EventCatalog

Understanding how to embed IcePanel diagrams in EventCatalog

Understanding how to use snippets with EventCatalog

---

## Custom Tools

**URL:** https://www.eventcatalog.dev/docs/development/ask-your-architecture/eventcatalog-assistant/bring-your-own-tools

**Contents:**
- Custom Tools
- Why custom tools?​
- How it works​
- Creating custom tools​
  - Basic example​
  - The AI uses tools automatically​
- Example tools​
  - Production metrics​
  - On-call information​
  - Queue depth and consumer lag​

EventCatalog Assistant comes with built-in tools that allow the AI to search and understand your architecture documentation. But what if you could go beyond static documentation and bring real-time data directly into your conversations?

With custom tools, you can extend the assistant to query your production metrics, check service health, look up on-call engineers, fetch data from your databases, and much more.

Your architecture documentation tells part of the story, but the real value often lies in the runtime data:

Custom tools transform EventCatalog from a static documentation site into a live knowledge hub where developers can ask questions like:

"Is OrderService healthy and who should I contact if there's an issue?"

And get real answers based on live data.

Custom tools are defined in your eventcatalog.chat.js file alongside your model configuration. Each tool has:

The AI automatically decides when to use your tools based on the user's question and the tool descriptions.

Here's a simple tool that returns service health information:

Once configured, the AI will automatically use your tools when relevant. If a user asks:

"Is the OrderService healthy?"

Query real-time metrics from your observability platform:

Look up who's on-call for a service:

Monitor your message brokers:

Look up entity state from your databases:

The AI uses tool descriptions to decide when to call them. Be specific about:

Return well-structured objects that the AI can easily interpret:

Always handle potential errors in your tools:

Remember that tools execute server-side. Keep security in mind:

Here's a complete eventcatalog.chat.js with multiple tools:

Users can see all available tools (including custom ones) by clicking the wrench icon in the chat panel. Custom tools are labeled with a "Custom" badge to distinguish them from built-in tools.

The possibilities are endless. Here are some ideas:

Custom tools turn EventCatalog into your organization's single pane of glass for architecture knowledge—combining static documentation with live operational data.

Have questions about custom tools? Join our Discord community to share ideas and get help.

**Examples:**

Example 1 (javascript):
```javascript
import { anthropic } from '@ai-sdk/anthropic';import { tool } from 'ai';import { z } from 'zod';// Export your modelexport default async () => {    return anthropic('claude-haiku-4-5');}// Export custom toolsexport const tools = {    getServiceHealth: tool({        description: 'Get the current health status of a service including uptime and active instances. Use this when users ask if a service is up, healthy, or having issues.',        inputSchema: z.object({            serviceName: z.string().describe('The name of the service to check health for'),        }),        execute: async ({ serviceName }) => {            // In production, query your monitoring system (Datadog, Prometheus, etc.)            const response = await fetch(`https://your-monitoring-api.com/health/${serviceName}`);            const health = await response.json();            return {                serviceName,                status: health.status,                uptime: health.uptime,                instances: health.activeInstances,                lastIncident: health.lastIncident,            };        },    }),};
```

Example 2 (javascript):
```javascript
getEventMetrics: tool({    description: 'Get real-time production metrics for an event including throughput, latency, and error rates. Use this when users ask about event performance, traffic, or production health.',    inputSchema: z.object({        eventId: z.string().describe('The event ID to get metrics for'),        timeRange: z.enum(['1h', '24h', '7d', '30d']).default('24h').describe('Time range for metrics'),    }),    execute: async ({ eventId, timeRange }) => {        // Query Datadog, Prometheus, CloudWatch, etc.        const metrics = await datadogClient.getMetrics(eventId, timeRange);        return {            eventId,            timeRange,            throughput: `${metrics.eventsPerSecond.toLocaleString()} events/sec`,            latency: {                p50: `${metrics.p50}ms`,                p99: `${metrics.p99}ms`,            },            errorRate: `${metrics.errorRate}%`,            status: metrics.errorRate > 0.1 ? 'degraded' : 'healthy',        };    },}),
```

Example 3 (javascript):
```javascript
getOnCall: tool({    description: 'Get the current on-call engineer and escalation contacts for a service. Use this when users ask who to contact, who owns a service, or who is on-call.',    inputSchema: z.object({        serviceName: z.string().describe('The name of the service to get on-call info for'),    }),    execute: async ({ serviceName }) => {        // Query PagerDuty, OpsGenie, or your internal system        const oncall = await pagerdutyClient.getOnCall(serviceName);        return {            serviceName,            team: oncall.team,            primary: {                name: oncall.primary.name,                email: oncall.primary.email,                slack: oncall.primary.slack,            },            secondary: oncall.secondary,            slackChannel: oncall.slackChannel,            escalationPolicy: oncall.escalationUrl,        };    },}),
```

Example 4 (javascript):
```javascript
getQueueDepth: tool({    description: 'Get the current queue depth, consumer lag, and processing rate for an event. Use this when users ask about event backlogs, processing delays, or queue health.',    inputSchema: z.object({        eventId: z.string().describe('The event ID to check queue depth for'),        environment: z.enum(['production', 'staging', 'development']).default('production'),    }),    execute: async ({ eventId, environment }) => {        // Query Kafka, RabbitMQ, SQS, etc.        const queue = await kafkaClient.getConsumerLag(eventId, environment);        return {            eventId,            environment,            status: queue.lag > 30 ? 'critical' : queue.lag > 5 ? 'warning' : 'healthy',            queue: {                depth: queue.depth.toLocaleString(),                oldestMessage: `${queue.lag.toFixed(1)} seconds ago`,            },            consumers: {                active: queue.consumers,                processingRate: `${queue.rate.toLocaleString()} events/sec`,            },        };    },}),
```

---

## Function: versionEvent()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionEvent

**Contents:**
- Function: versionEvent()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

versionEvent(directory): (id) => Promise<void>

Defined in: events.ts:230

Version an event by it's id.

Takes the latest event and moves it to a versioned directory. All files with this event are also versioned (e.g /events/InventoryAdjusted/schema.json)

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionEvent } = utils('/path/to/eventcatalog');// moves the latest InventoryAdjusted event to a versioned directory// the version within that event is used as the version number.await versionEvent('InventoryAdjusted');
```

---

## Creating flows

**URL:** https://www.eventcatalog.dev/docs/development/guides/flows/adding-flows

**Contents:**
- Creating flows
- Writing flow content​
- Adding child flows / reusable flows​
  - Tips for flow content​
  - What do flows look like in EventCatalog?​

Flows live in a /flows folder. This folder can be placed:

Here is an example of what a flow file may look like.

Once this file is added, the event will automatically appear across EventCatalog.

You can write any Markdown inside a flow.

Each flow gets its own page, so use this space to fully explain how it works.

You can also use interactive components to enrich your documentation.

You can reference a flow from another flow. This lets you reuse flows in your flow diagrams, useful if you have complex flows that reuse information from another flow.

To reference a flow from another flow, use the flow node type.

This will render the order-flow within the described flow. Right clicking on the order-flow node will let you navigate to the referenced flow.

It's entirely up to you what you want to add to your flows markdown content but here are a few things you might want to consider.

**Examples:**

Example 1 (jsx):
```jsx
---id: "CancelSubscription"name: "User Cancels Subscription"version: "0.0.1"summary: "Flow for when a user has cancelled a subscription"steps:  - id: "cancel_subscription_initiated"    title: "Cancels Subscription"    summary: "User cancels their subscription"    # define the actor for, in this case it's a user.    actor:      name: "User"    # What happens next? Define the next step      next_step:       id: "cancel_subscription_request"      label: "Initiate subscription cancellation"  - id: "cancel_subscription_request"    title: "Cancel Subscription"    # This step is a message, include the message and version    message:      id: "CancelSubscription"      version: "0.0.1"    next_step:       id: "subscription_service"      label: "Proceed to subscription service"  - id: "stripe_integration"    title: "Stripe"    # This is an external system (e.g Stripe)    externalSystem:      name: "Stripe"      summary: "3rd party payment system"      url: "https://stripe.com/"    next_step:       id: "subscription_service"      label: "Return to subscription service"  - id: "subscription_service"    title: "Subscription Service"    # This node is a service, include that.    service:      id: "SubscriptionService"      version: "0.0.1"    # Define multiple steps    next_steps:      - id: "stripe_integration"        label: "Cancel subscription via Stripe"      - id: "subscription_cancelled"        label: "Successful cancellation"      - id: "subscription_rejected"        label: "Failed cancellation"  - id: "subscription_cancelled"    title: "Subscription has been Cancelled"    message:      id: "UserSubscriptionCancelled"      version: "0.0.1"    next_step:      id: "notification_service"      label: "Email customer"  - id: "subscription_rejected"    title: "Subscription cancellation has been rejected"  - id: "notification_service"    title: "Notifications Service"    service:      id: "NotificationService"      version: "0.0.2"---This flow documents what happens when a User Cancels Subscription in our system. <NodeGraph /><!-- Add any markdown you want, the workflow will also render in its own page /docs/flows/{Flow}/{version} -->
```

Example 2 (yaml):
```yaml
steps:  - id: "step-1"    title: "Example Step of a Event"    flow:      id: "order-flow"      version: 0.0.1
```

---

## Documentation sidebar

**URL:** https://www.eventcatalog.dev/docs/development/customization/customize-sidebars/documentation-sidebar

**Contents:**
- Documentation sidebar
- What is a context aware sidebar?​
- Customizing the documentation sidebar​
  - How to customize the documentation sidebar​
    - Available navigation configuration​
    - Top level options:​
    - List all resources (by type):​
    - Chose which resources to show:​
  - Custom groups and links​

The documentation sidebar is a context aware sidebar that is shown on the /docs/ pages.

Clicking on any resource in the sidebar will show you related information to that selected resource (see demo).

Many documentation tools use a flat navigation structure, which can be overwhelming and difficult to navigate.

EventCatalog's documentation sidebar is a context aware sidebar that shows you related information to the selected resource.

This can help you navigate your documentation and find the information you need quickly, as you go deeper into the hierarchy of your architecture.

For example, selecting a domain will show you the subdomains, related services, ubiquitous language, etc, where as selecting a message will show you the producers, consumers and schemas.

By default EventCatalog will show you a list of all the resources in your catalog, but you can customize the navigation bar to show any resource you want.

This can be useful if you want to show a specific resource or a group of resources in the sidebar, helping your teams find the information they need quickly.

To customize the documentation sidebar you need to set the navigation.pages property in your eventcatalog.config.js file.

The example below will show you a list of the top-level domains and all resources in your catalog.

You can specify the following options in the navigation.pages property:

You can specify any resource you want to show in the sidebar using the following key structure

<resource-type>:<resource-id> or <resource-type>:<resource-id>:<resource-version>

If no version is specified, the latest version will be used.

Available resource types:

You can also create custom groups and links to external pages in the sidebar.

**Examples:**

Example 1 (json):
```json
module.exports = {  // ... rest of your config  navigation: {    // pick any key you want to show in the sidebar    pages: ['list:top-level-domains', 'list:all'],  },};
```

Example 2 (css):
```css
module.exports = {  navigation: {    pages: ['list:top-level-domains'],  },};
```

Example 3 (css):
```css
module.exports = {  navigation: {    pages: ['list:domains', 'list:services'],  },};
```

Example 4 (css):
```css
module.exports = {  navigation: {    // Show the MyDomain domain, MyService service and the 0.0.1 version of the MyEvent event    pages: [      // Show the latest version of the MyDomain domain      'domain:MyDomain',      // Show the latest version of the MyService service      'service:MyService',      // Show the 0.0.1 version of the MyMessage message      'message:MyMessage:0.0.1',    ],  },};
```

---

## <Link />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/link

**Contents:**
- <Link />
  - Support​
  - Usage​
  - Props​

The <Link/> component renders a link to a resource in EventCatalog.

EventCatalog handles links depending on your configuration file (e.g trailing slashes, etc), using this component creates links that are consistent with your EventCatalog configuration.

The <Link/> component is supported on all EventCatalog pages.

**Examples:**

Example 1 (jsx):
```jsx
---#domain frontmatter---<Link href="/my/awesome/page">My Awesome Page</Link>
```

---

## Function: addFileToEvent()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addFileToEvent

**Contents:**
- Function: addFileToEvent()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addFileToEvent(directory): (id, file, version?, options?) => Promise<void>

Defined in: events.ts:252

Add a file to an event by it's id.

Optionally specify a version to add a file to a specific version of the event.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addFileToEvent } = utils('/path/to/eventcatalog');// adds a file to the latest InventoryAdjusted eventawait addFileToEvent('InventoryAdjusted', { content: 'Hello world', fileName: 'hello.txt' });// adds a file to a specific version of the InventoryAdjusted eventawait addFileToEvent('InventoryAdjusted', { content: 'Hello world', fileName: 'hello.txt' }, '0.0.1');
```

---

## Function: getCommands()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getCommands

**Contents:**
- Function: getCommands()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getCommands(directory): (options?) => Promise<Command[]>

Defined in: commands.ts:64

Returns all commands from EventCatalog.

You can optionally specify if you want to get the latest version of the events.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getCommands } = utils('/path/to/eventcatalog');// Gets all commands (and versions) from the catalogconst commands = await getCommands();// Gets all commands (only latest version) from the catalogconst commands = await getCommands({ latestOnly: true });// Gets all commands with the schema attachedconst commands = await getCommands({ attachSchema: true });
```

---

## Creating data stores

**URL:** https://www.eventcatalog.dev/docs/development/guides/data/adding-data

**Contents:**
- Creating data stores
- Writing data store content​
- Assign read/write relationships to data stores​
  - What do data stores look like in EventCatalog?​

Data stores live in a /containers folder. This folder can be placed anywhere in your catalog.

The contents are split into two sections, frontmatter and the markdown content.

Here is an example of what a data store markdown file may look like.

Once this file is added, the event will automatically appear across EventCatalog.

You can write any Markdown inside a data store.

Each data store gets its own page, so use this space to fully explain how it works.

You can also use interactive components to enrich your documentation.

You can assign read/write relationships to data stores in EventCatalog. You can read more about how to do this here.

You can see an example of a data store in the EventCatalog demo.

**Examples:**

Example 1 (jsx):
```jsx
---# id of your data store, used for slugs and references in EventCatalog.id: orders-db# Display name of the data store, rendered in EventCatalog.name: Orders DB# Version of the data storeversion: 0.0.1# Type of the data store (e.g. database, cache, objectStore, searchIndex)container_type: database# Technology of the data store (e.g. postgres@14, redis@7, etc)technology: postgres@14# Classification of the data store (e.g. internal, external, etc)classification: internal# Retention of the data store (e.g. 7y, 10y, etc)retention: 7y# Residency of the data store (e.g. eu-west-1, us-east-1, etc)residency: eu-west-1---## OverviewThis orders database stores all orders and order lines for the orders domain.<NodeGraph />
```

---

## EventCatalog Linter

**URL:** https://www.eventcatalog.dev/docs/development/developer-tools/eventcatalog-linter

**Contents:**
- EventCatalog Linter
- Use cases​
- Features​
  - Supported Resource Types​
- Quick Start​
  - 1. Run the Linter​
  - 2. Configure Rules (Optional)​
  - 3. Integrate with CI/CD​
- Installation​
  - Use with npx (Recommended)​

A comprehensive linter for EventCatalog that validates frontmatter schemas and resource references to ensure your architecture documentation is correct and consistent.

The EventCatalog Linter helps you catch issues early in your development process, ensuring your documentation maintains high quality and accuracy across all your EventCatalog resources.

The linter validates all EventCatalog resource types:

Get started with the EventCatalog Linter in three simple steps:

Start linting your EventCatalog immediately with npx:

Create a .eventcatalogrc.js file in your EventCatalog root to customize validation:

Add to your CI/CD pipeline for automated validation:

Run the linter in your EventCatalog directory:

The EventCatalog Linter supports optional configuration through a .eventcatalogrc.js file in your catalog root directory. This allows you to:

Create a .eventcatalogrc.js file in your EventCatalog root directory:

Core resource reference validation (services, domains, entities) is always enabled and cannot be disabled, ensuring referential integrity of your EventCatalog.

The configuration file allows you to have different validation rules for different environments:

If no .eventcatalogrc.js file is found, the linter uses default rules where all validations are set to 'error'. This ensures strict validation out of the box, making it easy to get started with quality documentation practices.

Add to your package.json scripts:

The linter supports flexible version patterns for resource references:

The linter provides descriptive rule names in parentheses to help identify and fix issues quickly. Each error shows the specific rule that was violated:

The linter distinguishes between errors (critical issues) and warnings (suggestions for improvement):

Use --fail-on-warning to treat warnings as errors in CI/CD pipelines:

If you have any issues or feedback, please let us know by opening an issue on GitHub or joining our Discord server.

**Examples:**

Example 1 (bash):
```bash
npx @eventcatalog/linter
```

Example 2 (javascript):
```javascript
module.exports = {  rules: {    'best-practices/summary-required': 'warn',    'refs/owner-exists': 'error'  },  ignorePatterns: ['**/drafts/**']};
```

Example 3 (yaml):
```yaml
# GitHub Actions- run: npx @eventcatalog/linter --fail-on-warning
```

Example 4 (bash):
```bash
npx @eventcatalog/linter
```

---

## Deployment Workflows

**URL:** https://www.eventcatalog.dev/docs/development/deployment/deployment-workflows

**Contents:**
- Deployment Workflows
  - Keeping EventCatalog up to date​
  - CI/CD workflow to keep your documentation up to date​

Many people are deploying EventCatalog in different ways, as it's self hosted you can rebuild and redeploy your catalog as often as you want.

Keeping documentation up to date is a challenge, as it's easy to forget to update the documentation when you make changes to your code.

One way to keep your documentation up to date, is to redeploy your catalog whenever changes are made to your code, specifications or schemas.

EventCatalog has companies redeploying their catalogs hundreds of times a day.... it really depends on how often you make changes to your code, specifications or schemas, and how often you want to update your documentation. You are in control of how often you redeploy your catalog.

Many folks using EventCatalog have information scattered across multiple repositories, schema registries and other systems.

Users of EventCatalog either use our integrations (e.g AsyncAPI, OpenAPI, Schema Registry) or have built their own automated systems using our SDK.

EventCatalog is docs-as-code solution. This means you can store EventCatalog next to your code and in git repositories.

You can setup your CI/CD pipeline to build and deploy your catalog whenever changes are made to your code, specifications or schemas.

EventCatalog is flexible. And you can redeploy your catalog in various ways.

This can let you setup automation to ensure your documentation can stay up to date with any changes to your code, specifications or schemas.

---

## Function: writeChannel()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/writeChannel

**Contents:**
- Function: writeChannel()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

writeChannel(directory): (channel, options) => Promise<void>

Defined in: channels.ts:116

Write a channel to EventCatalog.

You can optionally override the path of the channel.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { writeChannel } = utils('/path/to/eventcatalog');// Write a channel to the catalog// channel would be written to channels/inventory.{env}.eventsawait writeChannel({  id: 'inventory.{env}.events',  name: 'Inventory channel',  version: '0.0.1',  summary: 'This is a summary',  markdown: '# Hello world',  address: inventory.{env}.events,protocols: ['http'],});// Write a channel to the catalog but override the path// channel would be written to channels/Inventory/InventoryChannelawait writeChannel({   id: 'InventoryChannel',   name: 'Update Inventory',   version: '0.0.1',   summary: 'This is a summary',   markdown: '# Hello world',   address: inventory.{env}.events,   protocols: ['http'],}, { path: "/channels/Inventory/InventoryChannel"});// Write a channel to the catalog and override the existing content (if there is any)await writeChannel({   id: 'InventoryChannel',   name: 'Update Inventory',   version: '0.0.1',   summary: 'This is a summary',   markdown: '# Hello world',   address: inventory.{env}.events,   protocols: ['http'],}, { override: true });// Write a channel to the catalog and version the previous version// only works if the new version is greater than the previous versionawait writeChannel({   id: 'InventoryChannel',   name: 'Update Inventory',   version: '0.0.1',   summary: 'This is a summary',   markdown: '# Hello world',   address: inventory.{env}.events,   protocols: ['http'],}, { versionExistingContent: true });
```

---

## Function: eventHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/eventHasVersion

**Contents:**
- Function: eventHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

eventHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: events.ts:312

Check to see if the catalog has a version for the given event.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { eventHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given event and version (supports semver)await eventHasVersion('InventoryAdjusted', '0.0.1');await eventHasVersion('InventoryAdjusted', 'latest');await eventHasVersion('InventoryAdjusted', '0.0.x');*
```

---

## Function: getProducersOfSchema()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getProducersOfSchema

**Contents:**
- Function: getProducersOfSchema()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getProducersOfSchema(directory): (path) => Promise<Service[]>

Defined in: messages.ts:164

Returns the producers of a given schema path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getProducersOfSchema } = utils('/path/to/eventcatalog');// Returns the producers of a given schema pathconst producers = await getProducersOfSchema('events/InventoryAdjusted/schema.json');
```

---

## Function: getChannel()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getChannel

**Contents:**
- Function: getChannel()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getChannel(directory): (id, version?) => Promise<Channel>

Defined in: channels.ts:29

Returns a channel from EventCatalog.

You can optionally specify a version to get a specific version of the channel

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getChannel } = utils('/path/to/eventcatalog');// Gets the latest version of the channelconst channel = await getChannel('InventoryChannel');// Gets a version of the channelconst channel = await getChannel('InventoryChannel', '0.0.1');
```

---

## Function: getEntities()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getEntities

**Contents:**
- Function: getEntities()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getEntities(directory): (options?) => Promise<Entity[]>

Defined in: entities.ts:51

Returns all entities from EventCatalog.

You can optionally specify if you want to get the latest version of the entities.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getEntities } = utils('/path/to/eventcatalog');// Gets all entities (and versions) from the catalogconst entities = await getEntities();// Gets all entities (only latest version) from the catalogconst entities = await getEntities({ latestOnly: true });
```

---

## Further Reading

**URL:** https://www.eventcatalog.dev/docs/development/design/further-reading

**Contents:**
- Further Reading

If you want to learn more about EventCatalog Studio you can read our documentation here or click on the links below to learn more.

---

## Adding custom page owners

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-documentation/owners

**Contents:**
- Adding custom page owners
- Adding owners using frontmatter​

Owners in EventCatalog are either users or teams and are optional.

To add an owner or a team, you need to add the user or team to the owners field of the custom page.

To add owners within a custom page you need to add them to the owners array within your custom page frontmatter API.

You need to add the id of the owner.

Assigning owners to your custom pages can provide others with context of who owns this custom page and how to contact them.

EventCatalog gives you the ability to create users and teams. You can read the documentation to get started.

**Examples:**

Example 1 (php):
```php
---id: OrderChannel... # other custom page frontmatterowners:    - dboyne # represents a user    - webTeam # represents a team---<!-- Markdown contents... -->
```

---

## Admonitions

**URL:** https://www.eventcatalog.dev/docs/development/components/components/admonitions

**Contents:**
- Admonitions
  - Support​
  - Usage​
  - Output example in EventCatalog​

The admonitions syntax is used to render a block of text with a specific style. You can use it to highlight important information, warnings, or other types of content.

The markdown syntax is supported in all pages in EventCatalog.

**Examples:**

Example 1 (julia):
```julia
---#event frontmatter---:::noteSome content with _Markdown_ syntax. Check [this api](https://eventcatalog.dev/).::::::tipSome content with _Markdown_ syntax. Check [this api](https://eventcatalog.dev/).::::::warningSome content with _Markdown_ syntax. Check [this api](https://eventcatalog.dev/).::::::dangerSome content with _Markdown_ syntax. Check [this api](https://eventcatalog.dev/).:::
```

---

## Components

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-documentation/components

**Contents:**
- Components
  - Embed EventCatalog Visualizer (NodeGraph)​
    - NodeGraph props​

You can add custom EventCatalog components to your custom pages.

See the list of components and how to use them.

You can also added components designed specifically for custom documentation.

In your custom documentation pages you can embed the EventCatalog Visualizer (NodeGraph) using the NodeGraph component.

This let's you embed any visualization (domain, service, message) into your custom documentation page.

To embed the NodeGraph component, you need to use the component, and pass in the id of the resource, version and type.

**Examples:**

Example 1 (jsx):
```jsx
This is my custom documentation page, here is a NodeGraph:<!-- Here we embed the NodeGraph component, passing in the id, version and type of the resource --><!-- This exammple will render a domain called "Orders" with the version "1.0.0" --><NodeGraph id="Orders" version="1.0.0" type="domain" />## Getting StartedRest of my markdown content...
```

---

## What is EventCatalog Assistant?

**URL:** https://www.eventcatalog.dev/docs/development/ask-your-architecture/eventcatalog-assistant/what-is-eventcatalog-assistant

**Contents:**
- What is EventCatalog Assistant?

EventCatalog Assistant allows users to ask questions about your documentation using natural language. It is embedded directly into your documentation site, enabling users to quickly find answers, understand your system, and succeed without manually searching through pages.

You can bring your own model to EventCatalog and your data is owned by you and never shared.

The assistant integrates with your preferred AI models using the AI SDK, giving you full control over which models power the experience.

---

## Function: rmUserById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmUserById

**Contents:**
- Function: rmUserById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmUserById(catalogDir): (id) => Promise<void>

Defined in: users.ts:137

Delete a user by it's id.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmUserById } = utils('/path/to/eventcatalog');// deletes the user with id eventcatalog-core-userawait rmUserById('eventcatalog-core-user');
```

---

## Function: getTeams()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getTeams

**Contents:**
- Function: getTeams()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getTeams(catalogDir): (options?) => Promise<Team[]>

Defined in: teams.ts:58

Returns all teams from EventCatalog.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getTeams } = utils('/path/to/eventcatalog');// Gets all teams from the catalogconst channels = await getTeams();
```

---

## EventCatalog Assistant

**URL:** https://www.eventcatalog.dev/docs/development/guides/eventcatalog-assistant

**Contents:**
- EventCatalog Assistant
- 📄️ What is EventCatalog Assistant?
- 📄️ Configuration
- 📄️ Custom Tools

EventCatalog Assistant

Learn how EventCatalog Assistant helps users explore documentation using natural language.

Configure EventCatalog Assistant

Extend EventCatalog Assistant with custom tools to bring real-time data, metrics, and integrations into your architecture conversations

---

## Customization Documentation

**URL:** https://www.eventcatalog.dev/docs/development/customization

**Contents:**
- Customization Documentation
- 📄️ Custom landing page
- 📄️ Customize tables
- 🗃️ Bring your own documentation
- 📄️ Themes
- 🗃️ Write your own components
- 🗃️ Customize Sidebars
- 🗃️ Customize Visualizer

Learn how to customize EventCatalog.

Customize landing pages in EventCatalog

Customize tables in EventCatalog

Customize the look and feel of your catalog with built-in themes, dark/light mode, and custom themes

---

## Function: entityHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/entityHasVersion

**Contents:**
- Function: entityHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

entityHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: entities.ts:195

Check to see if the catalog has a version for the given entity.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { entityHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given entity and version (supports semver)await entityHasVersion('User', '0.0.1');await entityHasVersion('User', 'latest');await entityHasVersion('User', '0.0.x');
```

---

## Upgrade to EventCatalog v3

**URL:** https://www.eventcatalog.dev/docs/development/upgrading/v3

**Contents:**
- Upgrade to EventCatalog v3
- Upgrade EventCatalog​
- Deprecated​
  - Deprecated: Visualizer sidebar icon​
  - Deprecated: /architecture/ pages​
  - Deprecated: Resource sidebars​
  - Deprecated: @eventcatalog/generator-ai package​
    - What do I need to do?​
- Removed​
  - Removed: LIST_VIEW and SIDE_VIEW navigation options​

This guide will help you upgrade from v2 to v3 of EventCatalog. (Missed the announcement? Read the blog post to find out what's new.)

Need to see the v2 docs? Visit this older version of the docs site. EventCatalog V2 will continue to get security updates, but new features and improvements will only be available in v3.

Update your project’s version of EventCatalog to the latest version using your package manager:

Problems upgrading? Try resetting your project.

The following deprecated features are no longer supported and are no longer documented. Please update your project accordingly.

Some deprecated features may temporarily continue to function until they are completely removed. Others may silently have no effect, or throw an error prompting you to update your code.

The visualizer vertical sidebar icon has been removed and replaced with the new navigation system.

To get to the visualizer for a resource, you will now click on the Visualizer link in the new navigation system.

The general /architecture/domains, /architecture/services and /architecture/messages pages have been removed and replaced with architecture pages per domains and service.

To get to the architecture, you will now click on the Architecture Diagram link in the new navigation system.

The resource sidebar (sidebar on the right of the page) has been removed and replaced with On this page section.

We have moved the resource information into the new navigation system.

The AI package has been removed and replaced with the EventCatalog Assistant.

Remove the @eventcatalog/generator-ai package from your project (if you have one) and any references to it in your generator configuration.

The following features have now been entirely removed from the code base and can no longer be used. Some of these features may have continued to work in your project even after deprecation. Others may have silently had no effect.

Projects now containing these removed features will be unable to build, and there will no longer be any supporting documentation prompting you to remove these features.

EventCatalog v3 introduces a new navigation sidebar.

For maintainability reasons going forward we have removed the old LIST_VIEW and SIDE_VIEW navigation options.

Remove the sidebar.type property from your eventcatalog.config.js file.

In EventCatalog v2 we had two homepages, one for / and one for /docs (both could be customized).

You can removed the /pages/index.mdx file from your project (if you have one).

If you still need to customize the homepage you can create a /pages/homepage.astro file and add your own content to it.

In EventCatalog v2 we used Pagefind for search, this would run after you build your catalog and index your resources.

We have now moved to nanostores to share state across the catalog, and users no longer have to build their catalog to search.

We have removed the EventCatalog Chat feature as it was in EventCatalog v2, and any model npm packages used.

We have replaced EventCatalog Chat with the EventCatalog Assistant.

Remove the @eventcatalog/generator-ai plugin from your project (if you have one)

Remove the chat configuration from your eventcatalog.config.js file (if you have one)

The model and provider configuration has been moved to the eventcatalog.chat.js file.

You can read more about the new AI assistant in the AI assistant documentation.

We have removed the EventCatalog Chat prompts in EventCatalog.

Remove the chat-prompts directory from your project (if you have one)

We plan to support custom prompts and tools in the future.

We have removed the Governance Reports feature which used EventCatalog with AI to generate reports on your architecture. We will be reviewing better ways to support governance reports in the future but for now we have decided to remove the feature.

The following changes are considered breaking changes in EventCatalog v3. Breaking changes may or may not provide temporary backwards compatibility. If you were using these features, you may have to update your code as recommended in each entry.

Previously in EventCatalog v2 domains would show all resources within it's subdomains and services including all the messages in that service. A cascading approach was used to show the resources.

In EventCatalog v3 domains are now more explicit about what resources are within it and you have to specify the resources you want to include in the domain.

This allows us to move forward to support domain level specifications and events (in this RFC)

In EventCatalog v3 we introduced a new configuration variable to enable authentication, which fixes the need for catalogs running on the server without authentication required.

If you are using authentication you will need to update your eventcatalog.config.js file to enable authentication.

EventCatalog v3 no longer supports .md files and only supports .mdx files.

EventCatalog v2 would transform any .md files found in your catalog to .mdx files during the migration to v2, we have removed this going forward.

If you have any .md files in your catalog, you will need to convert them to .mdx files. You can use the eventcatalog convert command to convert your .md files to .mdx files.

In EventCatalog v3 changelogs are now disabled by default. If you want to enable changelogs for your resources you will need to update your eventcatalog.config.js file.

If you want to enable changelogs, add the changelog configuration to your eventcatalog.config.js file:

The following new features and improvements have been added to EventCatalog v3.

EventCatalog v2 sidebars were restricting in the way users could navigate their resources. With a growing number of resources this became a bottleneck.

To solve this we have introduced a new navigation system that introduces new benefits:

You can read more about the new context aware navigation in the documentation sidebar documentation.

In EventCatalog v3 we have introduced a new caching system that will cache the information for your resources.

We also introduced nanostores to the code base, this will help us with performance and caching of information across pages.

Catalogs now have better lighthouse scores (demo has 100/100).

In EventCatalog v3 you can now assign flows to your services and domains.

This can help you document business workflows and features that are relevant to your services and domains.

To get started, you can add the flows property to your domain frontmatter.

In EventCatalog v3 we have introduced a new homepage for your catalog.

If you want to customize the homepage you can create a /pages/homepage.astro file and add your own content to it.

We have enabled llms.txt by default in EventCatalog v3, as this is a common use case for EventCatalog and helps with AI integrations.

Remove the llmsTxt property from your eventcatalog.config.js file (if you have one)

If you want to disable llms.txt you can set the enabled property to false.

Please check EventCatalog issues on GitHub for any reported issues, or to file an issue yourself.

**Examples:**

Example 1 (bash):
```bash
npm install @eventcatalog/core@latest
```

Example 2 (bash):
```bash
npm uninstall @eventcatalog/generator-ai
```

Example 3 (css):
```css
module.exports = {   docs: {-    sidebar: {-       type: 'LIST_VIEW'-    }  }};
```

Example 4 (bash):
```bash
npm uninstall @eventcatalog/generator-ai
```

---

## Function: getEvent()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getEvent

**Contents:**
- Function: getEvent()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getEvent(directory): (id, version?, options?) => Promise<Event>

Defined in: events.ts:37

Returns an event from EventCatalog.

You can optionally specify a version to get a specific version of the event

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getEvent } = utils('/path/to/eventcatalog');// Gets the latest version of the eventconst event = await getEvent('InventoryAdjusted');// Gets a version of the eventconst event = await getEvent('InventoryAdjusted', '0.0.1');// Get the event with the schema attachedconst event = await getEvent('InventoryAdjusted', '0.0.1', { attachSchema: true });
```

---

## Function: addSchemaToQuery()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addSchemaToQuery

**Contents:**
- Function: addSchemaToQuery()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addSchemaToQuery(directory): (id, schema, version?, options?) => Promise<void>

Defined in: queries.ts:292

Add a schema to a query by it's id.

Optionally specify a version to add a schema to a specific version of the query.

**Examples:**

Example 1 (json):
```json
import utils from '@eventcatalog/utils';const { addSchemaToQuery } = utils('/path/to/eventcatalog');// JSON schema exampleconst schema = {   "$schema": "http://json-schema.org/draft-07/schema#",   "type": "object",   "properties": {       "name": {       "type": "string"   },   "age": {     "type": "number"   } }, "required": ["name", "age"]};// adds a schema to the latest GetOrder queryawait addSchemaToQuery('GetOrder', { schema, fileName: 'schema.json' });// adds a file to a specific version of the GetOrder queryawait addSchemaToQuery('GetOrder', { schema, fileName: 'schema.json' }, '0.0.1');
```

---

## Function: versionDataStore()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionDataStore

**Contents:**
- Function: versionDataStore()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Examples​

versionDataStore(directory): (id) => Promise<void>

Defined in: data-stores.ts:68

Version an data store (e.g. database, cache, etc.) by its id.

Takes the latest data store and moves it to a versioned directory. All files with this data store are also versioned (e.g /containers/orders-db/schema.json)

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionDataStore } = utils('/path/to/eventcatalog');// moves the latest orders-db data store to a versioned directory// the version within that data store is used as the version number.await versionDataStore('orders-db');
```

Example 2 (python):
```python
import utils from '@eventcatalog/utils';const { versionContainer } = utils('/path/to/eventcatalog');// moves the latest orders-db container to a versioned directory// the version within that container is used as the version number.await versionContainer('orders-db');
```

---

## Function: getEvents()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getEvents

**Contents:**
- Function: getEvents()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getEvents(directory): (options?) => Promise<Event[]>

Defined in: events.ts:63

Returns all events from EventCatalog.

You can optionally specify if you want to get the latest version of the events.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getEvents } = utils('/path/to/eventcatalog');// Gets all events (and versions) from the catalogconst events = await getEvents();// Gets all events (only latest version) from the catalogconst events = await getEvents({ latestOnly: true });// Get all events with the schema attachedconst events = await getEvents({ attachSchema: true });
```

---

## Function: rmChannelById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmChannelById

**Contents:**
- Function: rmChannelById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmChannelById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: channels.ts:159

Delete a channel by it's id.

Optionally specify a version to delete a specific version of the channel.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmChannelById } = utils('/path/to/eventcatalog');// deletes the latest InventoryChannel channelawait rmChannelById('inventory.{env}.events');// deletes a specific version of the InventoryChannel channelawait rmChannelById('inventory.{env}.events', '0.0.1');
```

---

## Function: addSchemaToCommand()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addSchemaToCommand

**Contents:**
- Function: addSchemaToCommand()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

addSchemaToCommand(directory): (id, schema, version?, options?) => Promise<void>

Defined in: commands.ts:292

Add a schema to a command by it's id.

Optionally specify a version to add a schema to a specific version of the command.

**Examples:**

Example 1 (json):
```json
import utils from '@eventcatalog/utils';const { addSchemaToCommand } = utils('/path/to/eventcatalog');// JSON schema exampleconst schema = {   "$schema": "http://json-schema.org/draft-07/schema#",   "type": "object",   "properties": {       "name": {       "type": "string"   },   "age": {     "type": "number"   } }, "required": ["name", "age"]};// adds a schema to the latest UpdateInventory commandawait addSchemaToCommand('UpdateInventory', { schema, fileName: 'schema.json' });// adds a file to a specific version of the UpdateInventory commandawait addSchemaToCommand('UpdateInventory', { schema, fileName: 'schema.json' }, '0.0.1');
```

---

## <Attachments />

**URL:** https://www.eventcatalog.dev/docs/development/components/components/01a-attachments

**Contents:**
- <Attachments />
- Support​
- Usage​
  - Output example in EventCatalog​
  - Props​

The Attachments component allows you to link related documents, diagrams, and resources to any EventCatalog resource. This is perfect for connecting Architecture Decision Records (ADRs), design documents, external diagrams, or any other relevant documentation.

Attachments can be a url (string) or an object with additional properties.

The <Attachments /> component is supported in all EventCatalog resources, and custom documentation pages.

Here we have a domain with two attachments, one is a simple url and the other is an object with additional properties.

**Examples:**

Example 1 (jsx):
```jsx
---id: E-Commercename: E-Commerce Domainattachments:  - https://example.com/adr/001-microservices-architecture  - url: https://example.com/adr/001    title: ADR-001 - Use Kafka for asynchronous messaging    description: Learn more about why we chose Kafka for asynchronous messaging in this architecture decision record.    type: 'architecture-decisions'    icon: FileTextIcon---## Domain OverviewThis domain handles all e-commerce operations.<Attachments />
```

---

## Component styling

**URL:** https://www.eventcatalog.dev/docs/development/customization/custom-components/component-styling

**Contents:**
- Component styling

EventCatalog uses Tailwind. This means your custom components can be styled with tailwind.

Read the full astro guide here.

**Examples:**

Example 1 (jsx):
```jsx
---# Import data from your eventcatalog.config.js fileimport config from "@config"# Access passed-in component props, like `<MyComponent title="Hello, World" />`const { subtitle } = Astro.props;---<main class="flex justify-center">    <span class="block bg-red-500">This catalog belongs to the company:{config.organizationName}</span>    <span class="block bg-yellow-500">Data given to this component {subtitle}</span></main>
```

---

## Function: versionEntity()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionEntity

**Contents:**
- Function: versionEntity()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

versionEntity(directory): (id) => Promise<void>

Defined in: entities.ts:177

Version an entity by its id.

Takes the latest entity and moves it to a versioned directory. All files with this entity are also versioned (e.g /entities/User/schema.json)

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionEntity } = utils('/path/to/eventcatalog');// moves the latest User entity to a versioned directory// the version within that entity is used as the version number.await versionEntity('User');
```

---

## Function: getQueries()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getQueries

**Contents:**
- Function: getQueries()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

getQueries(directory): (options?) => Promise<Query[]>

Defined in: queries.ts:128

Returns all queries from EventCatalog.

You can optionally specify if you want to get the latest version of the queries.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getQueries } = utils('/path/to/eventcatalog');// Gets all queries (and versions) from the catalogconst queries = await getQueries();// Gets all queries (only latest version) from the catalogconst queries = await getQueries({ latestOnly: true });// Gets all queries with the schema attachedconst queries = await getQueries({ attachSchema: true });
```

---

## Using IcePanel

**URL:** https://www.eventcatalog.dev/docs/development/components/icepanel

**Contents:**
- Using IcePanel
- Using IcePanel in EventCatalog​
  - Getting your IcePanel share URL​
  - Basic Example​
  - Example with title and description​
  - Full screen mode​
  - Props​
  - More resources​

EventCatalog supports embedding IcePanel diagrams in all your markdown files.

IcePanel is a collaborative diagramming tool designed for visualizing software architecture using the C4 model. It helps teams create interactive system context, container, and component diagrams that can be shared and explored.

To embed an IcePanel diagram, use the <IcePanel /> component in any markdown file.

Each embedded IcePanel diagram includes a full screen button, allowing your teams to explore the diagram in detail without leaving EventCatalog.

**Examples:**

Example 1 (markdown):
```markdown
---# your frontmatter---<IcePanel url="https://s.icepanel.io/OpQVdslrqhZkyb/0QfB" />
```

Example 2 (markdown):
```markdown
---# your frontmatter---<IcePanel  url="https://s.icepanel.io/OpQVdslrqhZkyb/0QfB"  title="System Architecture"  description="Overview of our microservices architecture showing how services communicate."  height="800"/>
```

---

## Bring your own documentation

**URL:** https://www.eventcatalog.dev/docs/custom-pages/documentation

**Contents:**
- Bring your own documentation
- 📄️ Introduction
- 📄️ Adding custom documentation
- 📄️ Components
- 📄️ Owners

Bring your own documentation to EventCatalog, add custom pages and organize your documentation.

Customize documentation in EventCatalog

Adding custom documentation to your EventCatalog

Component list for custom pages

Adding owners to custom pages with EventCatalog.

---

## Import Resources into Studio

**URL:** https://www.eventcatalog.dev/docs/development/design/import-resources

**Contents:**
- Import Resources into Studio

To import your resources into EventCatalog Studio, click on the EventCatalog Studio button in the navigation bar, then click on the Open EventCatalog Studio button.

Then click on Copy resources to clipboard to copy your architecture primitives to the clipboard, then click on Open EventCatalog Studio to open the drag and drop editor.

Then you can paste your resources into the drag and drop editor, and click Import resources to import your resources into the drag and drop editor.

Once you have imported your resources, you can start to use them to create new designs or workflows for your architecture.

---

## Function: versionQuery()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/versionQuery

**Contents:**
- Function: versionQuery()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

versionQuery(directory): (id) => Promise<void>

Defined in: queries.ts:231

Version a query by it's id.

Takes the latest query and moves it to a versioned directory. All files with this query are also versioned (e.g /queries/GetOrder/schema.json)

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { versionQuery } = utils('/path/to/eventcatalog');// moves the latest GetOrder query to a versioned directory// the version within that query is used as the version number.await versionQuery('GetOrder');
```

---

## Function: commandHasVersion()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/commandHasVersion

**Contents:**
- Function: commandHasVersion()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

commandHasVersion(directory): (id, version?) => Promise<boolean>

Defined in: commands.ts:313

Check to see if the catalog has a version for the given command.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { commandHasVersion } = utils('/path/to/eventcatalog');// returns true if version is found for the given event and version (supports semver)await commandHasVersion('InventoryAdjusted', '0.0.1');await commandHasVersion('InventoryAdjusted', 'latest');await commandHasVersion('InventoryAdjusted', '0.0.x');*
```

---

## Getting Started Documentation

**URL:** https://www.eventcatalog.dev/docs/development/getting-started

**Contents:**
- Getting Started Documentation
- 📄️ Why EventCatalog?
- 📄️ Fundamentals
- 📄️ Installation
- 📄️ Project structure
- 📄️ Development and build

Learn how to install EventCatalog.

EventCatalog is an open source project to help you bring discoverability to your event-driven architecture.

Understanding the fundamentals of EventCatalog

Understanding how to install EventCatalog locally

Understanding how to structure your EventCatalog project

Understanding how to develop and build EventCatalog

---

## Function: rmDataStoreById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmDataStoreById

**Contents:**
- Function: rmDataStoreById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Examples​

rmDataStoreById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: data-stores.ts:104

Delete an data store (e.g. database, cache, etc.) by its id.

Optionally specify a version to delete a specific version of the data store.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmDataStoreById } = utils('/path/to/eventcatalog');// deletes the latest orders-db data storeawait rmDataStoreById('orders-db');// deletes a specific version of the orders-db data storeawait rmDataStoreById('orders-db', '0.0.1');
```

Example 2 (python):
```python
import utils from '@eventcatalog/utils';const { rmContainerById } = utils('/path/to/eventcatalog');// deletes the latest orders-db containerawait rmContainerById('orders-db');// deletes a specific version of the orders-db containerawait rmContainerById('orders-db', '0.0.1');
```

---

## Function: rmCommandById()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmCommandById

**Contents:**
- Function: rmCommandById()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmCommandById(directory): (id, version?, persistFiles?) => Promise<void>

Defined in: commands.ts:210

Delete a command by it's id.

Optionally specify a version to delete a specific version of the command.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmCommandById } = utils('/path/to/eventcatalog');// deletes the latest UpdateInventory commandawait rmCommandById('UpdateInventory');// deletes a specific version of the UpdateInventory commandawait rmCommandById('UpdateInventory', '0.0.1');
```

---

## Setting up Google

**URL:** https://www.eventcatalog.dev/docs/development/authentication/providers/setting-up-google

**Contents:**
- Setting up Google
- Create a new Google OAuth app​
- Configure the OAuth app in EventCatalog​
- Test the authentication​
- Found an issue?​

This guide takes your through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you've first gone through Enabling authentication.

To setup your EventCatalog site with visitor authentication using Google, the process looks as follows:

First, you will need to create a new Google OAuth app in the Google Cloud Console.

Add your Google Client ID and Client Secret to your .env file.

In your eventcatalog.auth.js file, add the following:

Restart your EventCatalog server and test the authentication.

All pages should now be protected and require a Google account to access.

Remember to setup the prerequisites for this guide:

If you still have problems, please let us know.

**Examples:**

Example 1 (unknown):
```unknown
AUTH_GOOGLE_CLIENT_ID={YOUR_GOOGLE_CLIENT_ID}AUTH_GOOGLE_CLIENT_SECRET={YOUR_GOOGLE_CLIENT_SECRET}
```

Example 2 (vue):
```vue
export default {  enabled: true,  google: {    clientId: process.env.AUTH_GOOGLE_CLIENT_ID,    clientSecret: process.env.AUTH_GOOGLE_CLIENT_SECRET,  },}
```

Example 3 (bash):
```bash
npm run dev
```

---

## Building Eventcatalog

**URL:** https://www.eventcatalog.dev/docs/development/deployment/build-and-deploy

**Contents:**
- Building Eventcatalog
- Building your EventCatalog (Static)​
  - Passing custom options​
  - Compression​
  - Memory limits​

By default, EventCatalog exports a static HTML site. This means you can deploy your application anywhere you want.

Some users have large catalogs, and slow deployments. This is because the static mode builds the entire catalog into HTML files.

If you have a large catalog you may want to use SSR mode, this will give you a server-side rendered application. This reduces build times, and renders pages on the fly.

To build your Catalog you will need to run:

This will output one directory

EventCatalog uses Astro to build the application. You can pass custom options to the build command by using the -- prefix.

You can opt into our build step which will compress your static assets.

You can enable this by setting the compress option to true in your eventcatalog.config.js file.

Compression can increase your build time and the amount of memory required to build your catalog.

If you want to enable this feature, you might also want to increase your build memory using the max_old_space_size value.

If you get any JavaScript heap out of memory errors, you can increase the memory limit by setting the NODE_OPTIONS environment variable. This gives astro more memory to work with.

If you are still experiencing issues, you can try:

**Examples:**

Example 1 (bash):
```bash
npm run build
```

Example 2 (bash):
```bash
npx eventcatalog dev --debug -- --env=production --port=3000
```

Example 3 (bash):
```bash
NODE_OPTIONS=--max_old_space_size=8196 npm run build
```

---

## Function: rmChannel()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmChannel

**Contents:**
- Function: rmChannel()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmChannel(directory): (path) => Promise<void>

Defined in: channels.ts:137

Delete a channel at it's given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmChannel } = utils('/path/to/eventcatalog');// removes a channel at the given path (channels dir is appended to the given path)// Removes the channel at channels/InventoryChannelawait rmChannel('/InventoryChannel');
```

---

## Function: getDataStore()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getDataStore

**Contents:**
- Function: getDataStore()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Examples​

getDataStore(directory): (id, version?) => Promise<Container>

Defined in: data-stores.ts:22

Returns a data store (e.g. database, cache, etc.) from EventCatalog.

You can optionally specify a version to get a specific version of the data store

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { getContainer } = utils('/path/to/eventcatalog');// Gets the latest version of the data storeconst container = await getDataStore('orders-db');// Gets a version of the entityconst container = await getDataStore('orders-db', '0.0.1');
```

Example 2 (python):
```python
import utils from '@eventcatalog/utils';const { getContainer } = utils('/path/to/eventcatalog');// Gets the latest version of the containerconst container = await getContainer('User');// Gets a version of the entityconst container = await getContainer('User', '0.0.1');
```

---

## Embed Diagrams

**URL:** https://www.eventcatalog.dev/docs/embed-diagrams

**Contents:**
- Embed Diagrams
- 📄️ <Miro />
- 📄️ <Lucid />
- 📄️ <DrawIO />
- 📄️ <FigJam />
- 📄️ <IcePanel />

This section describes what components can be used in EventCatalog..

Embed a Miro board in your documentation

Embed a Lucid diagram in your documentation

Embed a DrawIO diagram in your documentation

Embed a FigJam diagram in your documentation

Embed an IcePanel diagram in your documentation

---

## Themes

**URL:** https://www.eventcatalog.dev/docs/development/customization/themes

**Contents:**
- Themes
- Choosing a theme​
  - Available themes​
- Light and dark mode​
  - How it works​
  - Theme persistence​
- Creating custom themes​
  - Step 1: Create your theme CSS​
  - Step 2: Set the theme in config​
  - Step 3: Test both modes​

EventCatalog comes with a selection of built-in themes and supports both light and dark modes out of the box.

To set a theme, add the theme property to your eventcatalog.config.js file:

EventCatalog includes the following built-in themes:

EventCatalog supports both light and dark modes. Users can toggle between modes using the theme switcher in the header.

When a user manually selects light or dark mode, their preference is stored in localStorage under the key eventcatalog-theme. This ensures their choice persists across page reloads and browser sessions.

If no preference is stored, EventCatalog automatically follows the user's system preference using the prefers-color-scheme media query.

Custom themes allow you to fully brand EventCatalog with your organization's colors. You define your theme in eventcatalog.styles.css using CSS variables.

Add your custom theme to eventcatalog.styles.css in your project root. Your theme needs to define CSS variables for both light and dark modes.

Reference your custom theme name in eventcatalog.config.js:

Start your catalog and test both light and dark modes to ensure all colors look correct:

Toggle between light and dark mode using the theme switcher in the header.

Use Tailwind CSS colors as a reference for your RGB values. For example, red-600 is 220 38 38.

CSS variables must use space-separated RGB values (e.g., 220 38 38) without the rgb() wrapper. This allows EventCatalog to apply opacity modifiers like rgb(var(--ec-accent) / 0.5).

Here are all available CSS variables you can customize:

For custom themes, you may want to customize how markdown content (prose) appears in dark mode:

Here's a complete example of a custom "ruby" red theme you can use as a starting point:

**Examples:**

Example 1 (vue):
```vue
export default {  // ... other config  theme: 'sapphire',};
```

Example 2 (css):
```css
/** * Custom "ruby" theme - Red accent colors *//* Light Mode */:root[data-catalog-theme="ruby"],:root[data-catalog-theme="ruby"][data-theme="light"] {  /* Accent colors */  --ec-accent: 220 38 38;           /* red-600 */  --ec-accent-hover: 185 28 28;     /* red-700 */  --ec-accent-subtle: 254 226 226;  /* red-100 */  --ec-accent-text: 153 27 27;      /* red-800 */  /* Buttons */  --ec-button-bg: 185 28 28;        /* red-700 */  --ec-button-bg-hover: 153 27 27;  /* red-800 */  --ec-button-text: 255 255 255;  /* Sidebar */  --ec-sidebar-active-bg: 185 28 28;  --ec-sidebar-active-text: 255 255 255;  --ec-sidebar-hover-bg: 185 28 28;  /* You can override any CSS variable here */}/* Dark Mode */:root[data-catalog-theme="ruby"][data-theme="dark"] {  /* Accent colors - use lighter shades for dark mode */  --ec-accent: 248 113 113;         /* red-400 */  --ec-accent-hover: 239 68 68;     /* red-500 */  --ec-accent-subtle: 127 29 29 / 0.3;  --ec-accent-text: 252 165 165;    /* red-300 */  /* Buttons */  --ec-button-bg: 220 38 38;        /* red-600 */  --ec-button-bg-hover: 239 68 68;  /* red-500 */  --ec-button-text: 255 255 255;  /* Sidebar */  --ec-sidebar-active-bg: 220 38 38;  --ec-sidebar-active-text: 255 255 255;}
```

Example 3 (vue):
```vue
export default {  // ... other config  theme: 'ruby',  // Matches data-catalog-theme="ruby" in your CSS};
```

Example 4 (bash):
```bash
npm run dev
```

---

## Embed Designs into EventCatalog

**URL:** https://www.eventcatalog.dev/docs/development/design/embed-designs-into-eventcatalog

**Contents:**
- Embed Designs into EventCatalog

You can embed any diagram directly into your documentation using the <Design /> component.

To embed your diagrams you need to:

Our vision to to allow users to be embed diagrams anywhere, letting them embed diagrams into their tools they already use.

This is currently on our roadmap, and we will be adding more support for this in the future.

---

## Function: addFileToDataStore()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/addFileToDataStore

**Contents:**
- Function: addFileToDataStore()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Examples​

addFileToDataStore(directory): (id, file, version?) => Promise<void>

Defined in: data-stores.ts:143

Add a file to a data store (e.g. database, cache, etc.) by it's id.

Optionally specify a version to add a file to a specific version of the data store.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { addFileToDataStore } = utils('/path/to/eventcatalog');// adds a file to the latest InventoryAdjusted data storeawait addFileToDataStore('InventoryAdjusted', { content: 'Hello world', fileName: 'hello.txt' });// adds a file to a specific version of the InventoryAdjusted data storeawait addFileToDataStore('InventoryAdjusted', { content: 'Hello world', fileName: 'hello.txt' }, '0.0.1');
```

Example 2 (python):
```python
import utils from '@eventcatalog/utils';const { addFileToContainer } = utils('/path/to/eventcatalog');// adds a file to the latest InventoryAdjusted eventawait addFileToContainer('InventoryAdjusted', { content: 'Hello world', fileName: 'hello.txt' });// adds a file to a specific version of the InventoryAdjusted eventawait addFileToContainer('InventoryAdjusted', { content: 'Hello world', fileName: 'hello.txt' }, '0.0.1');
```

---

## Application Sidebar

**URL:** https://www.eventcatalog.dev/docs/development/customization/customize-sidebars/application-sidebar

**Contents:**
- Application Sidebar
  - Show/hide items in the application sidebar​

The application sidebar is the sidebar that is rendered on every page in EventCatalog.

You can show or hide items in the application sidebar by using the sidebar property in your eventcatalog.config.js file.

By default, all items is the sidebar are shown.

Options for the sidebar property:

**Examples:**

Example 1 (css):
```css
// rest of the configsidebar: [  {    id: '/schemas/explorer',    // This will hide the Schema Explorer    visible: false,  },]
```

---

## Versioning

**URL:** https://www.eventcatalog.dev/docs/development/guides/flows/versioning

**Contents:**
- Versioning
- How to version a flow​
- How to navigate to versions​

All content in EventCatalog can be versioned. This allows you to keep historic versions of content which can give context to users why things are changing.

EventCatalog will automatically create links for you within your latest version of your document. Users will also be able to navigate to any version by adding the version in the url (e.g /docs/flows/ProcessingPayments/1.0.2 would load the 1.0.2 version of this flow).

---

## Function: getOwnersForResource()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/getOwnersForResource

**Contents:**
- Function: getOwnersForResource()
- Parameters​
- Returns​
  - Parameters​
  - Returns​

getOwnersForResource(catalogDir): (id, version?) => Promise<Team[]>

Defined in: teams.ts:148

Returns the owners for a given resource (e.g domain, service, event, command, query, etc.)

---

## Setting up Auth0

**URL:** https://www.eventcatalog.dev/docs/development/authentication/providers/setting-up-auth0

**Contents:**
- Setting up Auth0
- Create a new Auth0 application​
- Configure the Auth0 app in EventCatalog​
- Test the authentication​
- Found an issue?​

This guide takes your through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you've first gone through Enabling authentication.

To setup your EventCatalog site with visitor authentication using Auth0, the process looks as follows:

First, you will need to create a new Auth0 application in your Auth0 Dashboard.

Add your Auth0 Domain, Client ID, and Client Secret to your .env file.

Your Auth0 issuer URL should be in the format: https://your-tenant.auth0.com (this is the Domain from your Auth0 application settings).

In your eventcatalog.auth.js file, add the following:

Restart your EventCatalog server and test the authentication.

All pages should now be protected and require an Auth0 account to access.

Remember to setup the prerequisites for this guide:

If you still have problems, please let us know.

**Examples:**

Example 1 (unknown):
```unknown
AUTH_AUTH0_ID={YOUR_AUTH0_CLIENT_ID}AUTH_AUTH0_SECRET={YOUR_AUTH0_CLIENT_SECRET}AUTH_AUTH0_ISSUER=https://{YOUR_AUTH0_DOMAIN}
```

Example 2 (vue):
```vue
export default {  enabled: true,  providers: {    auth0: {      clientId: process.env.AUTH_AUTH0_ID,      clientSecret: process.env.AUTH_AUTH0_SECRET,      issuer: process.env.AUTH_AUTH0_ISSUER,    },  },};
```

Example 3 (bash):
```bash
npm run dev
```

---

## Function: rmCommand()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmCommand

**Contents:**
- Function: rmCommand()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Example​

rmCommand(directory): (path) => Promise<void>

Defined in: commands.ts:188

Delete a command at it's given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmCommand } = utils('/path/to/eventcatalog');// removes a command at the given path (commands dir is appended to the given path)// Removes the command at commands/UpdateInventoryawait rmCommand('/UpdateInventory');
```

---

## Channels

**URL:** https://www.eventcatalog.dev/docs/channels

**Contents:**
- Channels
- 📄️ What are channels?
- 📄️ Creating a channel
- 📄️ Routing messages through channels
- 🗃️ Ownership & components
- 🗃️ Versioning & lifecycle

A collection of guides to help you understand channels and how they work with EventCatalog.

What are channels? Why are they useful for event-driven architectures?

Creating and managing channels within EventCatalog.

Understanding how to route messages through channels

---

## Customize your docs sidebar

**URL:** https://www.eventcatalog.dev/docs/development/guides/customize-your-sidebar

**Contents:**
- Customize your docs sidebar

EventCatalog provides the ability to customize the documentation sidebar to show your own content.

You can read and follow the guide on how to customize the documentation sidebar.

---

## Versioning diagrams

**URL:** https://www.eventcatalog.dev/docs/development/guides/diagrams/versioning-diagrams

**Contents:**
- Versioning diagrams
- Why version diagrams?​
- Creating versioned diagrams​
  - File structure​
  - Example: Current state vs. target state​
  - Current Limitations​
- Best practices​
  - Version numbering​
  - When to create new versions​
  - Keep versions aligned​

Diagrams in EventCatalog support versioning, allowing you to track how your architecture visualizations evolve over time. This is particularly valuable for maintaining historical accuracy and showing architectural progression.

Versioning diagrams helps you:

Similar to other resources in EventCatalog, diagrams use a versioned folder structure to maintain multiple versions.

The diagram at the root level (/diagrams/system-architecture/index.mdx) represents the latest version. Older versions are stored in the versioned folder, each in their own version directory.

A common use case is documenting both your current architecture and your target architecture as different versions:

As you update your domain to newer versions, you can update the diagram reference to match:

Follow semantic versioning principles:

Create a new diagram version when:

When possible, align diagram versions with the resources they document:

All diagram versions support markdown export, making them accessible to LLM tools and AI assistants. Each version has its own .mdx endpoint:

This allows AI tools to understand the full context of your architectural evolution.

**Examples:**

Example 1 (unknown):
```unknown
/diagrams/  └── system-architecture/      ├── index.mdx                    # Latest version (e.g., 2.0.0)      └── versioned/          ├── 1.0.0/          │   └── index.mdx            # Version 1.0.0          └── 1.5.0/              └── index.mdx            # Version 1.5.0
```

Example 2 (php):
```php
---id: architecturename: System Architectureversion: 2.0.0summary: Target microservices architecture we are migrating towards---## Target State (v2.0.0)This is our target architecture - the event-driven microservices platform we are actively migrating towards.\`\`\`mermaidgraph TB    WebApp[Web Application]    Gateway[API Gateway]    subgraph "Microservices"        OrderService[Order Service]        PaymentService[Payment Service]        InventoryService[Inventory Service]    end    Kafka[Event Stream]    WebApp --> Gateway    Gateway --> OrderService    Gateway --> PaymentService    Gateway --> InventoryService    OrderService --> Kafka    PaymentService --> Kafka    InventoryService --> Kafka\`\`\`### Expected Outcomes- 10x faster deployments- 99.9% availability- 50% cost reduction through auto-scaling
```

Example 3 (php):
```php
---id: architecturename: System Architectureversion: 1.0.0summary: Current monolithic architecture (legacy system)---## Current State (v1.0.0)This represents our current monolithic architecture that we are migrating away from._```mermaidgraph TB    WebApp[Web Application]    Monolith[Monolithic Application]    Database[(Single Database)]    WebApp --> Monolith    Monolith --> Database
```

Example 4 (sql):
```sql
## Version switchingWhen viewing a diagram that has multiple versions, EventCatalog displays a version dropdown in the header. Users can:1. See all available versions in the dropdown2. Switch between versions to compare changes3. The URL updates to reflect the selected version (e.g., `/diagrams/architecture/2.0.0`)The latest version is clearly marked in the dropdown with a "(latest)" indicator.## Referencing specific versionsWhen referencing diagrams from resources, you can specify which version to link to:```yaml title="Domain referencing specific diagram versions"---id: E-Commercename: E-Commerce Domainversion: 1.0.0diagrams:  # Reference the current state  - id: architecture    version: 1.0.0---
```

---

## Function: rmDataStore()

**URL:** https://www.eventcatalog.dev/docs/sdk/functions/rmDataStore

**Contents:**
- Function: rmDataStore()
- Parameters​
- Returns​
  - Parameters​
  - Returns​
- Examples​

rmDataStore(directory): (path) => Promise<void>

Defined in: data-stores.ts:84

Delete an data store (e.g. database, cache, etc.) at its given path.

**Examples:**

Example 1 (python):
```python
import utils from '@eventcatalog/utils';const { rmDataStore } = utils('/path/to/eventcatalog');// removes an data store at the given path (containers dir is appended to the given path)// Removes the data store at containers/orders-dbawait rmDataStore('/orders-db');
```

Example 2 (python):
```python
import utils from '@eventcatalog/utils';const { rmContainer } = utils('/path/to/eventcatalog');// removes an container at the given path (containers dir is appended to the given path)// Removes the container at containers/orders-dbawait rmContainer('/orders-db');
```

---

## MCP Server

**URL:** https://www.eventcatalog.dev/docs/development/developer-tools/mcp-server

**Contents:**
- MCP Server
- 📄️ Introduction
- 📄️ Installation

This section contains tutorials for the EventCatalog MCP Server.

Connect AI tools to your architecture catalog

Connect MCP clients to your EventCatalog

---
