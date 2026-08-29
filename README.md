<div align="center">

# 🚀 Awesome ServerKit Templates

### One-click, self-hosted apps for [ServerKit](https://github.com/jhd3197/ServerKit) — the official template registry

[![Templates](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjhd3197%2Fserverkit-templates%2Fmaster%2Findex.json&query=%24.count&label=templates&color=6d5df6)](https://serverkit.ai/templates)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-contributing)

Every entry is a small YAML file describing how to run an application — a Docker
Compose stack, the variables to ask for, ports, volumes, and post-install steps.
Install any of them in one click from a ServerKit panel, or browse the whole
catalog at **[serverkit.ai/templates](https://serverkit.ai/templates)**.

</div>

---

## ⚡ Use this registry

Templates ship inside every ServerKit panel, and this repo is the live layer on
top — merged templates reach every connected panel **without a panel release**.
Point a panel at it under *Templates → Repositories*, or via the API:

```bash
curl -X POST https://your-panel/api/v1/templates/repos \
  -H 'Authorization: Bearer <token>' \
  -d '{"name":"serverkit-official",
       "url":"https://raw.githubusercontent.com/jhd3197/serverkit-templates/master"}'
```

No ServerKit yet? [Install it in one line](https://github.com/jhd3197/ServerKit#quick-start).

## 📚 Contents

<!-- BEGIN TEMPLATE TOC -->
- [🤖 AI & LLM](#-ai--llm) — 12
- [📊 Analytics](#-analytics) — 5
- [💼 Business & ERP](#-business--erp) — 10
- [📝 CMS & Websites](#-cms--websites) — 9
- [🤝 Collaboration & Chat](#-collaboration--chat) — 7
- [👥 Community & Forums](#-community--forums) — 1
- [🗄️ Databases](#-databases) — 13
- [🛠️ Development](#-development) — 14
- [⚙️ DevOps & Containers](#-devops--containers) — 10
- [📄 Documents & E-Signing](#-documents--e-signing) — 7
- [💰 Finance](#-finance) — 5
- [🎮 Gaming](#-gaming) — 1
- [🏠 Home Automation](#-home-automation) — 6
- [🎬 Media & Downloads](#-media--downloads) — 26
- [📈 Monitoring & Status](#-monitoring--status) — 16
- [🌐 Networking & DNS](#-networking--dns) — 9
- [📰 News & RSS](#-news--rss) — 2
- [🗒️ Notes & Wikis](#-notes--wikis) — 5
- [🔔 Notifications](#-notifications) — 3
- [✅ Productivity](#-productivity) — 29
- [🔍 Search](#-search) — 3
- [🔒 Security & Auth](#-security--auth) — 8
- [💾 Storage & Files](#-storage--files) — 12
<!-- END TEMPLATE TOC -->

## 📦 The Templates

<!-- BEGIN TEMPLATE CATALOG -->
**213 templates** and counting — grouped by primary category.

### 🤖 AI & LLM

| App | Description | Links |
|---|---|---|
| **[AgentSite](https://github.com/jhd3197/AgentSite)** 🚀 | AI-powered website builder with multi-agent orchestration, deployed straight from its Git repository. | [Install](https://serverkit.ai/templates/agentsite) · [YAML](templates/agentsite.yaml) |
| **[AnythingLLM](https://anythingllm.com)** | All-in-one private ChatGPT-style app with built-in RAG, AI agents, and document workspaces. | [Install](https://serverkit.ai/templates/anythingllm) · [YAML](templates/anythingllm.yaml) |
| **[Chroma](https://www.trychroma.com)** | Open-source vector database for embeddings and semantic search in AI and RAG applications. | [Install](https://serverkit.ai/templates/chroma) · [YAML](templates/chroma.yaml) |
| **[Flowise](https://flowiseai.com)** | Low-code drag-and-drop builder for LLM agents and chains. | [Install](https://serverkit.ai/templates/flowise) · [YAML](templates/flowise.yaml) |
| **[Langflow](https://www.langflow.org)** | Visual framework for building multi-agent and RAG applications. | [Install](https://serverkit.ai/templates/langflow) · [YAML](templates/langflow.yaml) |
| **[LibreChat](https://librechat.ai)** | Open-source multi-model chat UI (OpenAI, Anthropic, Google, local) with conversation search. | [Install](https://serverkit.ai/templates/librechat) · [YAML](templates/librechat.yaml) |
| **[LiteLLM](https://litellm.ai)** | OpenAI-compatible proxy and gateway that routes requests across 100+ LLM providers. | [Install](https://serverkit.ai/templates/litellm) · [YAML](templates/litellm.yaml) |
| **[Ollama](https://ollama.com)** | Run Llama, Gemma, Mistral, Qwen, and other open LLMs locally with a simple API | [Install](https://serverkit.ai/templates/ollama) · [YAML](templates/ollama.yaml) |
| **[Ollama + Open WebUI](https://openwebui.com)** | Local LLM inference with Ollama and a friendly chat interface (Open WebUI). | [Install](https://serverkit.ai/templates/ollama-webui) · [YAML](templates/ollama-webui.yaml) |
| **[Open WebUI](https://openwebui.com)** | Feature-rich self-hosted ChatGPT-style interface for Ollama and any OpenAI-compatible API, with RAG and multi-user support | [Install](https://serverkit.ai/templates/open-webui) · [YAML](templates/open-webui.yaml) |
| **[Prompture Hub](https://github.com/jhd3197/prompture-hub)** | Self-hosted LLM gateway. Hold real provider keys server-side, issue scoped hub keys, and meter every call. Drop-in OpenAI-compatible API. | [Install](https://serverkit.ai/templates/prompture-hub) · [YAML](templates/prompture-hub.yaml) |
| **[Qdrant](https://qdrant.tech)** | Vector similarity search engine for AI/LLM and semantic-search applications. | [Install](https://serverkit.ai/templates/qdrant) · [YAML](templates/qdrant.yaml) |

### 📊 Analytics

| App | Description | Links |
|---|---|---|
| **[Matomo](https://matomo.org)** | Google Analytics alternative that protects your data and your customers' privacy | [Install](https://serverkit.ai/templates/matomo) · [YAML](templates/matomo.yaml) |
| **[Metabase](https://www.metabase.com)** | Open-source business intelligence and dashboards tool for exploring your data. | [Install](https://serverkit.ai/templates/metabase) · [YAML](templates/metabase.yaml) |
| **[Plausible Analytics](https://plausible.io)** | Privacy-friendly, lightweight alternative to Google Analytics | [Install](https://serverkit.ai/templates/plausible) · [YAML](templates/plausible.yaml) |
| **[PostHog](https://posthog.com)** | Open-source product analytics with session replay, feature flags, A/B testing, and event autocapture. | [Install](https://serverkit.ai/templates/posthog) · [YAML](templates/posthog.yaml) |
| **[Umami](https://umami.is)** | Simple, fast, privacy-focused alternative to Google Analytics | [Install](https://serverkit.ai/templates/umami) · [YAML](templates/umami.yaml) |

### 💼 Business & ERP

| App | Description | Links |
|---|---|---|
| **[Chatwoot](https://www.chatwoot.com)** | Open-source customer engagement suite with live chat and a shared inbox. | [Install](https://serverkit.ai/templates/chatwoot) · [YAML](templates/chatwoot.yaml) |
| **[Documenso](https://documenso.com)** | Open-source document signing platform for sending and signing documents online. | [Install](https://serverkit.ai/templates/documenso) · [YAML](templates/documenso.yaml) |
| **[EspoCRM](https://www.espocrm.com)** | Full-featured open-source CRM — leads, opportunities, accounts, email campaigns, and workflows | [Install](https://serverkit.ai/templates/espocrm) · [YAML](templates/espocrm.yaml) |
| **[GLPI](https://glpi-project.org)** | Full-featured IT service management — asset inventory, helpdesk tickets, and license tracking | [Install](https://serverkit.ai/templates/glpi) · [YAML](templates/glpi.yaml) |
| **[Kimai](https://www.kimai.org)** | Professional time-tracking for teams and freelancers with invoicing, projects, and detailed reports | [Install](https://serverkit.ai/templates/kimai) · [YAML](templates/kimai.yaml) |
| **[listmonk](https://listmonk.app)** | High-performance self-hosted newsletter and mailing list manager with a modern dashboard | [Install](https://serverkit.ai/templates/listmonk) · [YAML](templates/listmonk.yaml) |
| **[Odoo](https://www.odoo.com)** | All-in-one open-source business suite — CRM, accounting, inventory, e-commerce, HR, and 40+ apps | [Install](https://serverkit.ai/templates/odoo) · [YAML](templates/odoo.yaml) |
| **[Peppermint](https://peppermint.sh)** | Modern open-source ticket management and helpdesk — a lightweight Zendesk alternative | [Install](https://serverkit.ai/templates/peppermint) · [YAML](templates/peppermint.yaml) |
| **[Snipe-IT](https://snipeitapp.com)** | IT asset management for tracking hardware, licenses, accessories, and consumables across your organization | [Install](https://serverkit.ai/templates/snipe-it) · [YAML](templates/snipe-it.yaml) |
| **[Twenty](https://twenty.com)** | Modern open-source CRM — a community-driven Salesforce alternative with a Notion-like feel | [Install](https://serverkit.ai/templates/twenty) · [YAML](templates/twenty.yaml) |

### 📝 CMS & Websites

| App | Description | Links |
|---|---|---|
| **[Directus](https://directus.io)** | Open-source data platform with instant REST and GraphQL API for any SQL database | [Install](https://serverkit.ai/templates/directus) · [YAML](templates/directus.yaml) |
| **[Drupal](https://www.drupal.org)** | Enterprise-grade open-source CMS for ambitious digital experiences | [Install](https://serverkit.ai/templates/drupal) · [YAML](templates/drupal.yaml) |
| **[Ghost](https://ghost.org)** | Professional publishing platform for blogs and newsletters | [Install](https://serverkit.ai/templates/ghost) · [YAML](templates/ghost.yaml) |
| **[Grav CMS](https://getgrav.org)** | Modern flat-file CMS that is fast, simple, and flexible | [Install](https://serverkit.ai/templates/grav) · [YAML](templates/grav.yaml) |
| **[Joomla](https://www.joomla.org)** | Award-winning open-source CMS powering millions of websites, with thousands of extensions and templates | [Install](https://serverkit.ai/templates/joomla) · [YAML](templates/joomla.yaml) |
| **[Payload CMS](https://payloadcms.com)** | Modern TypeScript headless CMS with powerful admin panel and customization | [Install](https://serverkit.ai/templates/payload) · [YAML](templates/payload.yaml) |
| **[Strapi](https://strapi.io)** | Open-source headless CMS with customizable API and admin panel | [Install](https://serverkit.ai/templates/strapi) · [YAML](templates/strapi.yaml) |
| **[WordPress](https://wordpress.org)** | World's most popular content management system for blogs and websites | [Install](https://serverkit.ai/templates/wordpress) · [YAML](templates/wordpress.yaml) |
| **[WordPress (External Database)](https://wordpress.org)** | WordPress CMS connecting to an existing external MySQL database. Use this for dev/prod setups sharing the same database with different table prefixes. | [Install](https://serverkit.ai/templates/wordpress-external-db) · [YAML](templates/wordpress-external-db.yaml) |

### 🤝 Collaboration & Chat

| App | Description | Links |
|---|---|---|
| **[Element](https://element.io)** | Glossy Matrix web client — secure decentralized chat with E2E encryption | [Install](https://serverkit.ai/templates/element) · [YAML](templates/element.yaml) |
| **[Jitsi Meet](https://jitsi.org)** | Secure, fully featured, and completely free video conferencing | [Install](https://serverkit.ai/templates/jitsi) · [YAML](templates/jitsi.yaml) |
| **[Matrix Synapse](https://matrix.org)** | Decentralized communication server for secure, federated messaging | [Install](https://serverkit.ai/templates/matrix-synapse) · [YAML](templates/matrix-synapse.yaml) |
| **[Mattermost](https://mattermost.com)** | Open-source Slack alternative for secure team collaboration and messaging | [Install](https://serverkit.ai/templates/mattermost) · [YAML](templates/mattermost.yaml) |
| **[Penpot](https://penpot.app)** | Open-source design and prototyping platform for teams — the self-hosted Figma alternative | [Install](https://serverkit.ai/templates/penpot) · [YAML](templates/penpot.yaml) |
| **[Rocket.Chat](https://rocket.chat)** | Open-source team communication platform with chat, video, and file sharing | [Install](https://serverkit.ai/templates/rocketchat) · [YAML](templates/rocketchat.yaml) |
| **[The Lounge](https://thelounge.chat)** | Modern always-on web IRC client — stay connected and never miss a message | [Install](https://serverkit.ai/templates/thelounge) · [YAML](templates/thelounge.yaml) |

### 👥 Community & Forums

| App | Description | Links |
|---|---|---|
| **[NodeBB](https://nodebb.org)** | Modern, real-time forum and community platform built on Node.js. | [Install](https://serverkit.ai/templates/nodebb) · [YAML](templates/nodebb.yaml) |

### 🗄️ Databases

| App | Description | Links |
|---|---|---|
| **[Baserow](https://baserow.io)** | Open-source no-code database and Airtable alternative with real-time collaboration | [Install](https://serverkit.ai/templates/baserow) · [YAML](templates/baserow.yaml) |
| **[Grist](https://www.getgrist.com)** | Modern relational spreadsheet that combines the flexibility of a spreadsheet with the robustness of a database | [Install](https://serverkit.ai/templates/grist) · [YAML](templates/grist.yaml) |
| **[InfluxDB](https://www.influxdata.com)** | Purpose-built time series database for metrics, events, and IoT data | [Install](https://serverkit.ai/templates/influxdb) · [YAML](templates/influxdb.yaml) |
| **[MariaDB](https://mariadb.org)** | Community-developed fork of MySQL — fast, stable, and drop-in compatible | [Install](https://serverkit.ai/templates/mariadb) · [YAML](templates/mariadb.yaml) |
| **[Mongo Express](https://github.com/mongo-express/mongo-express)** | Web-based MongoDB admin interface for managing databases and collections | [Install](https://serverkit.ai/templates/mongo-express) · [YAML](templates/mongo-express.yaml) |
| **[MongoDB](https://www.mongodb.com)** | Popular document database for modern applications — flexible JSON-like storage with powerful queries | [Install](https://serverkit.ai/templates/mongodb) · [YAML](templates/mongodb.yaml) |
| **[MySQL](https://www.mysql.com)** | The world's most popular open-source relational database | [Install](https://serverkit.ai/templates/mysql) · [YAML](templates/mysql.yaml) |
| **[NocoDB](https://nocodb.com)** | Open-source Airtable alternative — turns any database into a smart spreadsheet with forms, kanban, and APIs | [Install](https://serverkit.ai/templates/nocodb) · [YAML](templates/nocodb.yaml) |
| **[pgAdmin 4](https://www.pgadmin.org)** | Web-based PostgreSQL administration and development platform | [Install](https://serverkit.ai/templates/pgadmin) · [YAML](templates/pgadmin.yaml) |
| **[phpMyAdmin](https://www.phpmyadmin.net)** | Web-based MySQL and MariaDB administration tool | [Install](https://serverkit.ai/templates/phpmyadmin) · [YAML](templates/phpmyadmin.yaml) |
| **[PostgreSQL](https://www.postgresql.org)** | The world's most advanced open-source relational database | [Install](https://serverkit.ai/templates/postgres) · [YAML](templates/postgres.yaml) |
| **[Redis](https://redis.io)** | In-memory data store for caching, queues, sessions, and pub/sub | [Install](https://serverkit.ai/templates/redis) · [YAML](templates/redis.yaml) |
| **[Redis Commander](https://github.com/joeferner/redis-commander)** | Web-based Redis management tool for viewing and editing data | [Install](https://serverkit.ai/templates/redis-commander) · [YAML](templates/redis-commander.yaml) |

### 🛠️ Development

| App | Description | Links |
|---|---|---|
| **[Appsmith](https://www.appsmith.com)** | Open-source low-code platform to build internal tools, admin panels, and dashboards on any datasource | [Install](https://serverkit.ai/templates/appsmith) · [YAML](templates/appsmith.yaml) |
| **[Code Server](https://coder.com/code-server)** | VS Code in the browser with full IDE features and extensions support | [Install](https://serverkit.ai/templates/code-server) · [YAML](templates/code-server.yaml) |
| **[Flask - Hello World](https://flask.palletsprojects.com)** | Simple Flask app for testing and debugging. Shows server info, port, and connection status. No database needed. | [Install](https://serverkit.ai/templates/flask-hello-world) · [YAML](templates/flask-hello-world.yaml) |
| **[Forgejo](https://forgejo.org)** | Self-hosted lightweight software forge — the community fork of Gitea powering Codeberg | [Install](https://serverkit.ai/templates/forgejo) · [YAML](templates/forgejo.yaml) |
| **[GitLab CE](https://about.gitlab.com)** | Complete DevOps platform — git hosting, CI/CD, issues, registry, and more (heavy, needs 4GB+ RAM) | [Install](https://serverkit.ai/templates/gitlab) · [YAML](templates/gitlab.yaml) |
| **[GlitchTip](https://glitchtip.com)** | Open-source error tracking, compatible with Sentry SDKs — simple to run, easy on resources | [Install](https://serverkit.ai/templates/glitchtip) · [YAML](templates/glitchtip.yaml) |
| **[IT-Tools](https://it-tools.tech)** | Collection of 80+ handy developer tools — JWT decoder, hash generators, converters, and more, all offline | [Install](https://serverkit.ai/templates/it-tools) · [YAML](templates/it-tools.yaml) |
| **[Kestra](https://kestra.io)** | Event-driven declarative orchestration platform — build, schedule, and monitor workflows in YAML | [Install](https://serverkit.ai/templates/kestra) · [YAML](templates/kestra.yaml) |
| **[Mailpit](https://mailpit.axllent.org)** | Email testing tool with a modern web UI — catch outgoing mail from your apps via SMTP | [Install](https://serverkit.ai/templates/mailpit) · [YAML](templates/mailpit.yaml) |
| **[Node.js Application](https://nodejs.org)** | Custom Node.js application. Supports Node 18-21. Perfect for Express, Next.js, or any Node.js project. | [Install](https://serverkit.ai/templates/node-app) · [YAML](templates/node-app.yaml) |
| **[PHP Application](https://www.php.net)** | Custom PHP application with Apache. Supports PHP 8.0-8.3. Perfect for Laravel, WordPress themes, or any PHP project. | [Install](https://serverkit.ai/templates/php-app) · [YAML](templates/php-app.yaml) |
| **[Python Application](https://www.python.org)** | Custom Python application. Supports Python 3.9-3.12. Perfect for Flask, FastAPI, Django, or any Python project. | [Install](https://serverkit.ai/templates/python-app) · [YAML](templates/python-app.yaml) |
| **[Verdaccio](https://verdaccio.org)** | Lightweight private npm proxy registry — cache packages and publish private modules | [Install](https://serverkit.ai/templates/verdaccio) · [YAML](templates/verdaccio.yaml) |
| **[Windmill](https://www.windmill.dev)** | Developer platform to turn scripts into workflows, UIs, and scheduled jobs — an open-source Retool and Airflow alternative | [Install](https://serverkit.ai/templates/windmill) · [YAML](templates/windmill.yaml) |

### ⚙️ DevOps & Containers

| App | Description | Links |
|---|---|---|
| **[Docker Registry](https://docs.docker.com/registry/)** | Private Docker container image registry for storing and distributing container images | [Install](https://serverkit.ai/templates/registry) · [YAML](templates/registry.yaml) |
| **[Dockge](https://dockge.kuma.pet)** | Reactive self-hosted Docker Compose stack manager from the maker of Uptime Kuma | [Install](https://serverkit.ai/templates/dockge) · [YAML](templates/dockge.yaml) |
| **[Drone CI](https://www.drone.io)** | Container-native continuous integration platform with simple pipeline configuration | [Install](https://serverkit.ai/templates/drone) · [YAML](templates/drone.yaml) |
| **[Gitea](https://gitea.io)** | Lightweight self-hosted Git service | [Install](https://serverkit.ai/templates/gitea) · [YAML](templates/gitea.yaml) |
| **[GitLab Runner](https://docs.gitlab.com/runner/)** | Application that works with GitLab CI/CD to run jobs in a pipeline | [Install](https://serverkit.ai/templates/gitlab-runner) · [YAML](templates/gitlab-runner.yaml) |
| **[HashiCorp Vault](https://www.vaultproject.io)** | Secrets management and data protection platform for securing sensitive data | [Install](https://serverkit.ai/templates/vault) · [YAML](templates/vault.yaml) |
| **[Jenkins](https://www.jenkins.io)** | Leading open-source automation server for building, deploying, and automating projects | [Install](https://serverkit.ai/templates/jenkins) · [YAML](templates/jenkins.yaml) |
| **[Portainer](https://www.portainer.io)** | Lightweight Docker management UI with container visualization | [Install](https://serverkit.ai/templates/portainer) · [YAML](templates/portainer.yaml) |
| **[SonarQube](https://www.sonarqube.org)** | Continuous inspection of code quality and security vulnerabilities | [Install](https://serverkit.ai/templates/sonarqube) · [YAML](templates/sonarqube.yaml) |
| **[Watchtower](https://containrrr.dev/watchtower/)** | Automatically update running Docker containers when new images are published | [Install](https://serverkit.ai/templates/watchtower) · [YAML](templates/watchtower.yaml) |

### 📄 Documents & E-Signing

| App | Description | Links |
|---|---|---|
| **[Docmost](https://docmost.com)** | Open-source collaborative wiki and documentation software — an alternative to Confluence and Notion | [Install](https://serverkit.ai/templates/docmost) · [YAML](templates/docmost.yaml) |
| **[DocuSeal](https://www.docuseal.com)** | Open-source document signing — create fillable PDF forms and collect legally-binding e-signatures | [Install](https://serverkit.ai/templates/docuseal) · [YAML](templates/docuseal.yaml) |
| **[DokuWiki](https://www.dokuwiki.org)** | Simple, versatile wiki that needs no database — clean syntax and easy file-based backups | [Install](https://serverkit.ai/templates/dokuwiki) · [YAML](templates/dokuwiki.yaml) |
| **[MediaWiki](https://www.mediawiki.org)** | The wiki software that powers Wikipedia — battle-tested collaborative knowledge bases | [Install](https://serverkit.ai/templates/mediawiki) · [YAML](templates/mediawiki.yaml) |
| **[ONLYOFFICE Docs](https://www.onlyoffice.com)** | Office suite server for collaborative editing of documents, spreadsheets, and presentations — integrates with Nextcloud and Seafile | [Install](https://serverkit.ai/templates/onlyoffice) · [YAML](templates/onlyoffice.yaml) |
| **[Paperless-ngx](https://docs.paperless-ngx.com)** | Document management system that scans, OCRs, indexes and archives your documents into a searchable online archive. | [Install](https://serverkit.ai/templates/paperless-ngx) · [YAML](templates/paperless-ngx.yaml) |
| **[Stirling PDF](https://www.stirlingpdf.com)** | Local web toolkit for splitting, merging, converting and OCR-ing PDF files. | [Install](https://serverkit.ai/templates/stirling-pdf) · [YAML](templates/stirling-pdf.yaml) |

### 💰 Finance

| App | Description | Links |
|---|---|---|
| **[Actual Budget](https://actualbudget.org)** | Privacy-first personal budgeting app using envelope budgeting with optional bank sync. | [Install](https://serverkit.ai/templates/actualbudget) · [YAML](templates/actualbudget.yaml) |
| **[Firefly III](https://www.firefly-iii.org)** | Self-hosted personal finance manager for budgeting, accounts, and money tracking. | [Install](https://serverkit.ai/templates/firefly-iii) · [YAML](templates/firefly-iii.yaml) |
| **[Ghostfolio](https://ghostfol.io)** | Open-source wealth management software to track stocks, ETFs, and crypto across your portfolio | [Install](https://serverkit.ai/templates/ghostfolio) · [YAML](templates/ghostfolio.yaml) |
| **[Securo](https://usesecuro.com)** | Privacy-first personal finance manager with bank sync, budgets, goals, multi-currency, and optional self-hosted AI agents | [Install](https://serverkit.ai/templates/securo) · [YAML](templates/securo.yaml) |
| **[Wallos](https://wallosapp.com)** | Personal subscription tracker — monitor recurring costs, renewal dates, and spending by category | [Install](https://serverkit.ai/templates/wallos) · [YAML](templates/wallos.yaml) |

### 🎮 Gaming

| App | Description | Links |
|---|---|---|
| **[Minecraft Server](https://www.minecraft.net)** | Dedicated Minecraft Java Edition server with automatic version management (itzg image) | [Install](https://serverkit.ai/templates/minecraft-server) · [YAML](templates/minecraft-server.yaml) |

### 🏠 Home Automation

| App | Description | Links |
|---|---|---|
| **[Eclipse Mosquitto](https://mosquitto.org)** | Lightweight MQTT message broker for IoT and home automation | [Install](https://serverkit.ai/templates/mosquitto) · [YAML](templates/mosquitto.yaml) |
| **[ESPHome](https://esphome.io)** | Create custom firmwares for ESP32/ESP8266 smart-home devices with simple YAML configuration | [Install](https://serverkit.ai/templates/esphome) · [YAML](templates/esphome.yaml) |
| **[Frigate](https://frigate.video)** | Complete local NVR with realtime AI object detection for your IP cameras — no cloud required | [Install](https://serverkit.ai/templates/frigate) · [YAML](templates/frigate.yaml) |
| **[Home Assistant](https://www.home-assistant.io)** | Open-source home automation platform with focus on local control and privacy | [Install](https://serverkit.ai/templates/homeassistant) · [YAML](templates/homeassistant.yaml) |
| **[Node-RED](https://nodered.org)** | Flow-based programming tool for wiring together hardware devices and APIs | [Install](https://serverkit.ai/templates/nodered) · [YAML](templates/nodered.yaml) |
| **[Zigbee2MQTT](https://www.zigbee2mqtt.io)** | Bridge Zigbee devices to MQTT without proprietary bridges or gateways | [Install](https://serverkit.ai/templates/zigbee2mqtt) · [YAML](templates/zigbee2mqtt.yaml) |

### 🎬 Media & Downloads

| App | Description | Links |
|---|---|---|
| **[Audiobookshelf](https://www.audiobookshelf.org)** | Self-hosted server for managing and streaming your audiobooks, podcasts, and ebooks. | [Install](https://serverkit.ai/templates/audiobookshelf) · [YAML](templates/audiobookshelf.yaml) |
| **[Bazarr](https://www.bazarr.media)** | Companion to Sonarr and Radarr that downloads and manages subtitles for your media library | [Install](https://serverkit.ai/templates/bazarr) · [YAML](templates/bazarr.yaml) |
| **[Calibre-Web](https://github.com/janeczku/calibre-web)** | Clean web interface for browsing, reading, and downloading books from a Calibre ebook library. | [Install](https://serverkit.ai/templates/calibre-web) · [YAML](templates/calibre-web.yaml) |
| **[FlareSolverr](https://github.com/FlareSolverr/FlareSolverr)** | Proxy server that solves Cloudflare challenges — companion service for Prowlarr and the *arr stack | [Install](https://serverkit.ai/templates/flaresolverr) · [YAML](templates/flaresolverr.yaml) |
| **[God's Eye View](https://github.com/bilawalsidhu/gods-eye-view)** 🚀 | Spy-satellite simulator in your browser — live aircraft, ships, satellites, earthquakes, and public cameras on a photorealistic 3D globe, with AI voice control | [Install](https://serverkit.ai/templates/gods-eye-view) · [YAML](templates/gods-eye-view.yaml) |
| **[Immich](https://immich.app)** | High-performance self-hosted photo and video backup solution with mobile apps | [Install](https://serverkit.ai/templates/immich) · [YAML](templates/immich.yaml) |
| **[Jellyfin](https://jellyfin.org)** | Free and open-source media server for streaming movies, TV shows, music, and more | [Install](https://serverkit.ai/templates/jellyfin) · [YAML](templates/jellyfin.yaml) |
| **[Jellyseerr](https://github.com/Fallenbagel/jellyseerr)** | Media request and discovery portal for Jellyfin/Plex and the PVR apps | [Install](https://serverkit.ai/templates/jellyseerr) · [YAML](templates/jellyseerr.yaml) |
| **[Kavita](https://www.kavitareader.com)** | Fast and friendly self-hosted digital library for manga, comics, and ebooks with cross-device reading | [Install](https://serverkit.ai/templates/kavita) · [YAML](templates/kavita.yaml) |
| **[Komga](https://komga.org)** | Media server for comics, mangas, BDs, and magazines with OPDS support and a slick web reader | [Install](https://serverkit.ai/templates/komga) · [YAML](templates/komga.yaml) |
| **[Lidarr](https://lidarr.audio)** | Music collection manager that monitors, grabs, sorts, and renames albums automatically | [Install](https://serverkit.ai/templates/lidarr) · [YAML](templates/lidarr.yaml) |
| **[Lychee](https://lycheeorg.dev)** | Beautiful self-hosted photo management — upload, organize, tag, and share your photos | [Install](https://serverkit.ai/templates/lychee) · [YAML](templates/lychee.yaml) |
| **[MeTube](https://github.com/alexta69/metube)** | Web UI for yt-dlp — download videos and audio from YouTube and hundreds of other sites | [Install](https://serverkit.ai/templates/metube) · [YAML](templates/metube.yaml) |
| **[Navidrome](https://www.navidrome.org)** | Modern music server and streamer compatible with Subsonic/Airsonic | [Install](https://serverkit.ai/templates/navidrome) · [YAML](templates/navidrome.yaml) |
| **[Overseerr](https://overseerr.dev)** | Request management and media discovery tool for Plex that integrates with Sonarr and Radarr | [Install](https://serverkit.ai/templates/overseerr) · [YAML](templates/overseerr.yaml) |
| **[PhotoPrism](https://photoprism.app)** | AI-powered photo management application with face recognition and auto-tagging | [Install](https://serverkit.ai/templates/photoprism) · [YAML](templates/photoprism.yaml) |
| **[PiGallery2](https://bpatrik.github.io/pigallery2/)** | Fast directory-first photo gallery — point it at your existing photo folders, no imports needed | [Install](https://serverkit.ai/templates/pigallery2) · [YAML](templates/pigallery2.yaml) |
| **[Pinchflat](https://github.com/kieraneglin/pinchflat)** | Your own YouTube media manager — auto-download channels and playlists for Plex and Jellyfin | [Install](https://serverkit.ai/templates/pinchflat) · [YAML](templates/pinchflat.yaml) |
| **[Plex Media Server](https://www.plex.tv)** | Organize and stream your personal media collection to any device | [Install](https://serverkit.ai/templates/plex) · [YAML](templates/plex.yaml) |
| **[Prowlarr](https://wiki.servarr.com/prowlarr)** | Indexer manager and proxy that integrates your indexers with the PVR apps | [Install](https://serverkit.ai/templates/prowlarr) · [YAML](templates/prowlarr.yaml) |
| **[qBittorrent](https://www.qbittorrent.org)** | Open-source BitTorrent client with a full-featured web UI | [Install](https://serverkit.ai/templates/qbittorrent) · [YAML](templates/qbittorrent.yaml) |
| **[Radarr](https://radarr.video)** | PVR for movies that monitors, grabs, sorts, and renames films automatically | [Install](https://serverkit.ai/templates/radarr) · [YAML](templates/radarr.yaml) |
| **[SABnzbd](https://sabnzbd.org)** | Free and easy binary newsreader — automated Usenet downloading with a full API | [Install](https://serverkit.ai/templates/sabnzbd) · [YAML](templates/sabnzbd.yaml) |
| **[Sonarr](https://sonarr.tv)** | PVR for TV series that monitors, grabs, sorts, and renames episodes automatically | [Install](https://serverkit.ai/templates/sonarr) · [YAML](templates/sonarr.yaml) |
| **[Tautulli](https://tautulli.com)** | Monitoring and statistics dashboard for your Plex Media Server with notifications and history | [Install](https://serverkit.ai/templates/tautulli) · [YAML](templates/tautulli.yaml) |
| **[Transmission](https://transmissionbt.com)** | Fast, easy, and free BitTorrent client with a lightweight web UI | [Install](https://serverkit.ai/templates/transmission) · [YAML](templates/transmission.yaml) |

### 📈 Monitoring & Status

| App | Description | Links |
|---|---|---|
| **[Beszel](https://beszel.dev)** | Lightweight server monitoring hub with historical metrics and alerts. | [Install](https://serverkit.ai/templates/beszel) · [YAML](templates/beszel.yaml) |
| **[changedetection.io](https://changedetection.io)** | Website change detection and monitoring with notifications to 90+ services | [Install](https://serverkit.ai/templates/changedetection) · [YAML](templates/changedetection.yaml) |
| **[Dozzle](https://dozzle.dev)** | Realtime log viewer for Docker containers — no database, just a fast web UI over the Docker socket | [Install](https://serverkit.ai/templates/dozzle) · [YAML](templates/dozzle.yaml) |
| **[Gatus](https://gatus.io)** | Automated developer-oriented status page — monitor HTTP, TCP, ICMP, and DNS with alerting | [Install](https://serverkit.ai/templates/gatus) · [YAML](templates/gatus.yaml) |
| **[Glances](https://nicolargo.github.io/glances/)** | Cross-platform system monitoring — CPU, memory, disks, network, and containers in one web view | [Install](https://serverkit.ai/templates/glances) · [YAML](templates/glances.yaml) |
| **[Grafana](https://grafana.com)** | Open-source analytics and interactive visualization platform for metrics, logs, and traces | [Install](https://serverkit.ai/templates/grafana) · [YAML](templates/grafana.yaml) |
| **[Grafana Loki](https://grafana.com/oss/loki/)** | Horizontally scalable, highly available log aggregation system inspired by Prometheus | [Install](https://serverkit.ai/templates/loki) · [YAML](templates/loki.yaml) |
| **[Healthchecks](https://healthchecks.io)** | Cron job and scheduled task monitoring — get alerted when your background jobs do not run on time | [Install](https://serverkit.ai/templates/healthchecks) · [YAML](templates/healthchecks.yaml) |
| **[Jaeger](https://www.jaegertracing.io)** | Open-source distributed tracing system for monitoring and troubleshooting microservices | [Install](https://serverkit.ai/templates/jaeger) · [YAML](templates/jaeger.yaml) |
| **[LibreSpeed](https://librespeed.org)** | Lightweight self-hosted speed test — measure download, upload, ping, and jitter from any browser | [Install](https://serverkit.ai/templates/librespeed) · [YAML](templates/librespeed.yaml) |
| **[Netdata](https://netdata.cloud)** | Real-time performance and health monitoring for systems and applications | [Install](https://serverkit.ai/templates/netdata) · [YAML](templates/netdata.yaml) |
| **[Prometheus](https://prometheus.io)** | Open-source monitoring and alerting toolkit designed for reliability and scalability | [Install](https://serverkit.ai/templates/prometheus) · [YAML](templates/prometheus.yaml) |
| **[SigNoz](https://signoz.io)** | OpenTelemetry-native observability platform for traces, metrics, and logs (an open-source APM alternative to Datadog). | [Install](https://serverkit.ai/templates/signoz) · [YAML](templates/signoz.yaml) |
| **[SmokePing](https://oss.oetiker.ch/smokeping/)** | Network latency monitoring with beautiful interactive graphs — see jitter and packet loss over time | [Install](https://serverkit.ai/templates/smokeping) · [YAML](templates/smokeping.yaml) |
| **[Uptime Kuma](https://uptime.kuma.pet)** | A fancy self-hosted monitoring tool for websites and services | [Install](https://serverkit.ai/templates/uptime-kuma) · [YAML](templates/uptime-kuma.yaml) |
| **[VictoriaMetrics](https://victoriametrics.com)** | Fast, cost-effective time series database and monitoring solution — a drop-in Prometheus alternative | [Install](https://serverkit.ai/templates/victoriametrics) · [YAML](templates/victoriametrics.yaml) |

### 🌐 Networking & DNS

| App | Description | Links |
|---|---|---|
| **[AdGuard Home](https://adguard.com/en/adguard-home/overview.html)** | Network-wide ad and tracker blocking DNS server with parental controls and per-client settings | [Install](https://serverkit.ai/templates/adguard-home) · [YAML](templates/adguard-home.yaml) |
| **[Caddy](https://caddyserver.com)** | Fast, multi-platform web server with automatic HTTPS | [Install](https://serverkit.ai/templates/caddy) · [YAML](templates/caddy.yaml) |
| **[NetBox](https://netboxlabs.com/community/)** | The source of truth for your network — IPAM and DCIM for racks, devices, cables, VLANs, and prefixes | [Install](https://serverkit.ai/templates/netbox) · [YAML](templates/netbox.yaml) |
| **[Nginx Proxy Manager](https://nginxproxymanager.com)** | Easy-to-use reverse proxy with SSL management | [Install](https://serverkit.ai/templates/nginx-proxy-manager) · [YAML](templates/nginx-proxy-manager.yaml) |
| **[Pi-hole](https://pi-hole.net)** | Network-wide ad-blocking DNS sinkhole with a web dashboard. | [Install](https://serverkit.ai/templates/pihole) · [YAML](templates/pihole.yaml) |
| **[RustDesk Server](https://rustdesk.com)** | Self-hosted signaling and relay server for RustDesk — the open-source TeamViewer alternative | [Install](https://serverkit.ai/templates/rustdesk-server) · [YAML](templates/rustdesk-server.yaml) |
| **[Technitium DNS](https://technitium.com/dns/)** | Authoritative and recursive DNS server with ad blocking, DNS-over-HTTPS, and a full web console | [Install](https://serverkit.ai/templates/technitium) · [YAML](templates/technitium.yaml) |
| **[Traefik](https://traefik.io)** | Modern HTTP reverse proxy and load balancer with automatic HTTPS | [Install](https://serverkit.ai/templates/traefik) · [YAML](templates/traefik.yaml) |
| **[WG-Easy](https://github.com/wg-easy/wg-easy)** | The easiest way to run WireGuard VPN with a web admin UI. | [Install](https://serverkit.ai/templates/wg-easy) · [YAML](templates/wg-easy.yaml) |

### 📰 News & RSS

| App | Description | Links |
|---|---|---|
| **[FreshRSS](https://freshrss.org)** | Free, self-hosted RSS and Atom feed aggregator for following news and websites in one place. | [Install](https://serverkit.ai/templates/freshrss) · [YAML](templates/freshrss.yaml) |
| **[Miniflux](https://miniflux.app)** | Minimalist and fast self-hosted RSS feed reader backed by PostgreSQL. | [Install](https://serverkit.ai/templates/miniflux) · [YAML](templates/miniflux.yaml) |

### 🗒️ Notes & Wikis

| App | Description | Links |
|---|---|---|
| **[Etherpad](https://etherpad.org)** | Real-time collaborative document editing in the browser — the classic shared notepad | [Install](https://serverkit.ai/templates/etherpad) · [YAML](templates/etherpad.yaml) |
| **[HedgeDoc](https://hedgedoc.org)** | Collaborative real-time markdown editor — write, present, and share notes with your team | [Install](https://serverkit.ai/templates/hedgedoc) · [YAML](templates/hedgedoc.yaml) |
| **[Joplin Server](https://joplinapp.org)** | Sync server for Joplin — the open-source note-taking app with end-to-end encryption | [Install](https://serverkit.ai/templates/joplin-server) · [YAML](templates/joplin-server.yaml) |
| **[Memos](https://www.usememos.com)** | Lightweight, privacy-first note-taking and micro-blogging app. | [Install](https://serverkit.ai/templates/memos) · [YAML](templates/memos.yaml) |
| **[Trilium Notes](https://github.com/TriliumNext/Notes)** | Hierarchical note-taking application with rich editing, scripting, and knowledge-base features | [Install](https://serverkit.ai/templates/trilium) · [YAML](templates/trilium.yaml) |

### 🔔 Notifications

| App | Description | Links |
|---|---|---|
| **[Apprise API](https://github.com/caronc/apprise-api)** | One API to send notifications to 100+ services — Telegram, Discord, Slack, email, ntfy, and more | [Install](https://serverkit.ai/templates/apprise-api) · [YAML](templates/apprise-api.yaml) |
| **[Gotify](https://gotify.net)** | Self-hosted push notification server with Android client support. | [Install](https://serverkit.ai/templates/gotify) · [YAML](templates/gotify.yaml) |
| **[ntfy](https://ntfy.sh)** | Simple HTTP-based pub/sub service that pushes notifications to your phone or desktop via a POST. | [Install](https://serverkit.ai/templates/ntfy) · [YAML](templates/ntfy.yaml) |

### ✅ Productivity

| App | Description | Links |
|---|---|---|
| **[Activepieces](https://www.activepieces.com)** | Open-source no-code automation platform — a Zapier alternative with 280+ integrations and AI pieces | [Install](https://serverkit.ai/templates/activepieces) · [YAML](templates/activepieces.yaml) |
| **[Baïkal](https://sabre.io/baikal/)** | Lightweight CalDAV and CardDAV server — sync calendars and contacts across all your devices | [Install](https://serverkit.ai/templates/baikal) · [YAML](templates/baikal.yaml) |
| **[BookStack](https://www.bookstackapp.com)** | Simple, self-hosted platform for organizing and storing information | [Install](https://serverkit.ai/templates/bookstack) · [YAML](templates/bookstack.yaml) |
| **[Cal.com](https://cal.com)** | Open-source scheduling infrastructure — the self-hosted Calendly alternative | [Install](https://serverkit.ai/templates/cal-com) · [YAML](templates/cal-com.yaml) |
| **[Dashy](https://dashy.to)** | Self-hosted startpage with status checking, themes, widgets, and a built-in UI config editor | [Install](https://serverkit.ai/templates/dashy) · [YAML](templates/dashy.yaml) |
| **[draw.io](https://www.drawio.com)** | Self-hosted diagrams.net — flowcharts, network diagrams, UML, and whiteboards in the browser | [Install](https://serverkit.ai/templates/drawio) · [YAML](templates/drawio.yaml) |
| **[Excalidraw](https://excalidraw.com)** | Virtual whiteboard for sketching hand-drawn like diagrams | [Install](https://serverkit.ai/templates/excalidraw) · [YAML](templates/excalidraw.yaml) |
| **[Grocy](https://grocy.info)** | ERP for your fridge — groceries, chores, and household management with stock tracking and barcode support | [Install](https://serverkit.ai/templates/grocy) · [YAML](templates/grocy.yaml) |
| **[Homarr](https://homarr.dev)** | Sleek customizable dashboard for your homelab with drag-and-drop widgets and app integrations | [Install](https://serverkit.ai/templates/homarr) · [YAML](templates/homarr.yaml) |
| **[HomeBox](https://homebox.software)** | Inventory and organization system for your home — track items, locations, warranties, and maintenance | [Install](https://serverkit.ai/templates/homebox) · [YAML](templates/homebox.yaml) |
| **[Homepage](https://gethomepage.dev)** | Modern, fast, fully static-generated dashboard with 100+ service widgets and Docker integration | [Install](https://serverkit.ai/templates/homepage) · [YAML](templates/homepage.yaml) |
| **[Kanboard](https://kanboard.org)** | Minimalist kanban project management — simple, fast, and self-contained | [Install](https://serverkit.ai/templates/kanboard) · [YAML](templates/kanboard.yaml) |
| **[Karakeep](https://karakeep.app)** | Self-hosted bookmark-everything app (formerly Hoarder) that saves links, notes, and images with AI tagging and full-text search. | [Install](https://serverkit.ai/templates/karakeep) · [YAML](templates/karakeep.yaml) |
| **[Leantime](https://leantime.io)** | Goals-oriented project management for non-project managers — built with ADHD and neurodiversity in mind | [Install](https://serverkit.ai/templates/leantime) · [YAML](templates/leantime.yaml) |
| **[linkding](https://linkding.link)** | Minimal, fast self-hosted bookmark manager. | [Install](https://serverkit.ai/templates/linkding) · [YAML](templates/linkding.yaml) |
| **[Linkwarden](https://linkwarden.app)** | Collaborative bookmark manager that archives full copies of every page you save | [Install](https://serverkit.ai/templates/linkwarden) · [YAML](templates/linkwarden.yaml) |
| **[Mealie](https://mealie.io)** | Self-hosted recipe manager and meal planner with one-click recipe import from any URL | [Install](https://serverkit.ai/templates/mealie) · [YAML](templates/mealie.yaml) |
| **[Monica](https://www.monicahq.com)** | Personal CRM to remember everything about your friends, family, and business relationships | [Install](https://serverkit.ai/templates/monica) · [YAML](templates/monica.yaml) |
| **[n8n](https://n8n.io)** | Extendable workflow automation tool for connecting apps and services | [Install](https://serverkit.ai/templates/n8n) · [YAML](templates/n8n.yaml) |
| **[Outline](https://www.getoutline.com)** | Beautiful, real-time collaborative team wiki and knowledge base | [Install](https://serverkit.ai/templates/outline) · [YAML](templates/outline.yaml) |
| **[Plane](https://plane.so)** | Open-source project management and issue tracking with cycles, modules, and views (a Jira/Linear alternative). | [Install](https://serverkit.ai/templates/plane) · [YAML](templates/plane.yaml) |
| **[Planka](https://planka.app)** | Elegant open-source kanban board for workgroups — a realtime Trello alternative | [Install](https://serverkit.ai/templates/planka) · [YAML](templates/planka.yaml) |
| **[Rallly](https://rallly.co)** | Schedule group meetings without back-and-forth emails — an open-source Doodle alternative | [Install](https://serverkit.ai/templates/rallly) · [YAML](templates/rallly.yaml) |
| **[Roundcube](https://roundcube.net)** | Browser-based multilingual IMAP webmail client with a modern responsive interface | [Install](https://serverkit.ai/templates/roundcube) · [YAML](templates/roundcube.yaml) |
| **[Shlink](https://shlink.io)** | Self-hosted URL shortener with detailed visit analytics, QR codes, and a full REST API | [Install](https://serverkit.ai/templates/shlink) · [YAML](templates/shlink.yaml) |
| **[Tandoor Recipes](https://tandoor.dev)** | Smart recipe manager with meal planning, shopping lists, and cookbook imports for your household | [Install](https://serverkit.ai/templates/tandoor) · [YAML](templates/tandoor.yaml) |
| **[Vikunja](https://vikunja.io)** | Self-hosted to-do list and task and project manager. | [Install](https://serverkit.ai/templates/vikunja) · [YAML](templates/vikunja.yaml) |
| **[Wallabag](https://wallabag.org)** | Save and classify articles to read later — a self-hosted alternative to Pocket | [Install](https://serverkit.ai/templates/wallabag) · [YAML](templates/wallabag.yaml) |
| **[Wiki.js](https://js.wiki)** | Modern and powerful wiki app built on Node.js | [Install](https://serverkit.ai/templates/wikijs) · [YAML](templates/wikijs.yaml) |

### 🔍 Search

| App | Description | Links |
|---|---|---|
| **[Meilisearch](https://www.meilisearch.com)** | Lightning-fast, typo-tolerant search engine that many apps rely on for instant full-text search. | [Install](https://serverkit.ai/templates/meilisearch) · [YAML](templates/meilisearch.yaml) |
| **[SearXNG](https://docs.searxng.org)** | Privacy-respecting metasearch engine that aggregates results from many sources without tracking you. | [Install](https://serverkit.ai/templates/searxng) · [YAML](templates/searxng.yaml) |
| **[Typesense](https://typesense.org)** | Typo-tolerant search engine optimized for fast, instant search-as-you-type experiences. | [Install](https://serverkit.ai/templates/typesense) · [YAML](templates/typesense.yaml) |

### 🔒 Security & Auth

| App | Description | Links |
|---|---|---|
| **[2FAuth](https://docs.2fauth.app)** | Web app to manage and generate your two-factor authentication (2FA) codes — a self-hosted authenticator | [Install](https://serverkit.ai/templates/2fauth) · [YAML](templates/2fauth.yaml) |
| **[Authelia](https://www.authelia.com)** | Authentication and authorization server providing 2FA and SSO | [Install](https://serverkit.ai/templates/authelia) · [YAML](templates/authelia.yaml) |
| **[Authentik](https://goauthentik.io)** | Open-source identity provider for single sign-on with OIDC, SAML, and LDAP. | [Install](https://serverkit.ai/templates/authentik) · [YAML](templates/authentik.yaml) |
| **[CrowdSec](https://www.crowdsec.net)** | Collaborative security engine for detecting and blocking threats | [Install](https://serverkit.ai/templates/crowdsec) · [YAML](templates/crowdsec.yaml) |
| **[Keycloak](https://www.keycloak.org)** | Open-source identity and access management for modern applications | [Install](https://serverkit.ai/templates/keycloak) · [YAML](templates/keycloak.yaml) |
| **[Passbolt](https://www.passbolt.com)** | Open-source password manager built for team collaboration, with browser extensions and granular sharing | [Install](https://serverkit.ai/templates/passbolt) · [YAML](templates/passbolt.yaml) |
| **[Pocket ID](https://pocket-id.org)** | Simple OIDC provider with passkey-first authentication for your self-hosted services | [Install](https://serverkit.ai/templates/pocket-id) · [YAML](templates/pocket-id.yaml) |
| **[Vaultwarden](https://github.com/dani-garcia/vaultwarden)** | Lightweight Bitwarden-compatible password manager server | [Install](https://serverkit.ai/templates/vaultwarden) · [YAML](templates/vaultwarden.yaml) |

### 💾 Storage & Files

| App | Description | Links |
|---|---|---|
| **[Backrest](https://github.com/garethgeorge/backrest)** | Web UI and orchestrator for restic — scheduled, encrypted, deduplicated backups to local or cloud storage | [Install](https://serverkit.ai/templates/backrest) · [YAML](templates/backrest.yaml) |
| **[Duplicati](https://www.duplicati.com)** | Free backup software to store encrypted backups online | [Install](https://serverkit.ai/templates/duplicati) · [YAML](templates/duplicati.yaml) |
| **[File Browser](https://filebrowser.org)** | Web-based file manager with upload, download, and file sharing features | [Install](https://serverkit.ai/templates/filebrowser) · [YAML](templates/filebrowser.yaml) |
| **[Filestash](https://www.filestash.app)** | Modern web file manager that connects to SFTP, S3, FTP, WebDAV, Git, and more — a Dropbox-like UI over your existing storage | [Install](https://serverkit.ai/templates/filestash) · [YAML](templates/filestash.yaml) |
| **[Kopia](https://kopia.io)** | Fast and secure backup tool with encryption, deduplication, and cloud storage support — managed from a web UI | [Install](https://serverkit.ai/templates/kopia) · [YAML](templates/kopia.yaml) |
| **[MinIO](https://min.io)** | High-performance, S3-compatible object storage for cloud-native applications | [Install](https://serverkit.ai/templates/minio) · [YAML](templates/minio.yaml) |
| **[Nextcloud](https://nextcloud.com)** | Self-hosted productivity platform with file sync and collaboration | [Install](https://serverkit.ai/templates/nextcloud) · [YAML](templates/nextcloud.yaml) |
| **[PairDrop](https://pairdrop.net)** | AirDrop for the web — share files between devices on your network directly in the browser | [Install](https://serverkit.ai/templates/pairdrop) · [YAML](templates/pairdrop.yaml) |
| **[Pingvin Share](https://github.com/stonith404/pingvin-share)** | Self-hosted file sharing platform — a WeTransfer alternative with links, expiry, and password protection | [Install](https://serverkit.ai/templates/pingvin-share) · [YAML](templates/pingvin-share.yaml) |
| **[Seafile](https://www.seafile.com)** | Open-source file sync and share platform with built-in collaboration | [Install](https://serverkit.ai/templates/seafile) · [YAML](templates/seafile.yaml) |
| **[SFTPGo](https://sftpgo.com)** | Full-featured SFTP, FTP/S, and WebDAV server with a web admin UI and virtual folders | [Install](https://serverkit.ai/templates/sftpgo) · [YAML](templates/sftpgo.yaml) |
| **[Syncthing](https://syncthing.net)** | Continuous file synchronization for decentralized, peer-to-peer sync | [Install](https://serverkit.ai/templates/syncthing) · [YAML](templates/syncthing.yaml) |

🚀 = deployed straight from its Git repository (repo template) rather than a Docker Compose stack.
<!-- END TEMPLATE CATALOG -->

---

## 🤝 Contributing

Adding an app takes one YAML file:

1. Write `templates/<id>.yaml`. Copy the closest existing template — that is
   more reliable than any spec, and every file here is a working example.
   `id` must be a lowercase slug matching the filename, and the template must
   declare at least one of `compose`, `dockerfile` or `ports` (or be a
   `kind: repo` template with a `repo.url`).
2. Regenerate and validate:

   ```bash
   python3 scripts/generate_index.py     # rebuild index.json  (needs PyYAML)
   python3 scripts/generate_readme.py    # rebuild this README's catalog
   python3 scripts/validate.py           # the review gate (no dependencies)
   ```

3. Open a PR.

The authoritative semantic rules live in the panel's
`TemplateService.validate_template()` — this repo's validator deliberately
checks only the registry contract (index ↔ files ↔ hashes), so it stays
dependency-free.

## 🔧 Registry internals

<details>
<summary><strong>How a panel consumes this repo</strong></summary>

The contract is two files on any static host:

```
<repo_url>/index.json              ← the catalog
<repo_url>/templates/<id>.yaml     ← fetched on demand, when opened or installed
```

The panel lists `index.json` alongside its bundled templates, and only downloads
the full YAML when someone opens or installs one. `<id>` comes straight from the
index entry, so **`id` must equal the filename stem**.

</details>

<details>
<summary><strong>Bundled vs registry</strong></summary>

ServerKit **ships these same templates inside the panel**. This repo is not a
replacement for that bundle — it is the layer on top:

| | Bundled in the panel | This registry |
|---|---|---|
| Works offline / air-gapped | yes | no |
| Available on a fresh install | yes | needs network |
| Updated without a panel release | no | **yes** |
| Community submissions | no | **yes** |

The bundle is the known-good floor and stays useful when this repo (or GitHub)
is unreachable; the registry is where new templates land and where fixes ship
between releases.

</details>

<details>
<summary><strong><code>version</code> vs <code>revision</code></strong></summary>

- **`version`** — the version of the *upstream application* (`"1.23"` for
  Uptime Kuma). User-facing.
- **`revision`** — the version of *this template*, for a compose fix, a wrong
  port, or a bad healthcheck that ships no new upstream release.

⚠️ **`revision` is reserved and not yet consumed.** Current panels compare
`version` to decide "update available", so today a template-only fix cannot be
published without also implying an app upgrade. Bump `version` for now; the
field is emitted so the index is ready when panel support lands.

</details>

<details>
<summary><strong><code>sha256</code></strong></summary>

Every index entry carries the SHA-256 of the file the panel will download. Not
yet verified panel-side — it is published so verification can be enabled
without reindexing, and so a PR diff names exactly which templates changed
rather than just showing a churned index.

</details>

<details>
<summary><strong>Icons</strong></summary>

`icon` is an `https://` URL or a `data:image/` URI. Icon files live in this
repo's `icons/` directory and templates reference them through jsDelivr, which
serves proper image content types and CORS headers (raw.githubusercontent does
not, and would break `<img>` rendering):

```
https://cdn.jsdelivr.net/gh/jhd3197/serverkit-templates@master/icons/<id>.svg
```

Add the logo (SVG preferred, PNG fallback — [dashboard-icons](https://github.com/homarr-labs/dashboard-icons)
and [selfh.st/icons](https://selfh.st/icons/) cover most self-hosted apps) as
`icons/<id>.*` in the same PR as the template. Merging to `master` publishes
both together. Only templates with no public logo inline a data URI.

</details>

<details>
<summary><strong>Layout</strong></summary>

```
index.json         generated catalog — never hand-edit
templates/         one <id>.yaml per template
schema/            JSON Schema for index.json
scripts/
  generate_index.py   rebuild index.json from templates/ (needs PyYAML)
  generate_readme.py  rebuild the README catalog from templates/ (needs PyYAML)
  validate.py         check the registry contract (no dependencies)
```

</details>

See [RELEASING.md](RELEASING.md) for publishing — merging to `master` **is**
publishing.

## 📄 License

MIT — see [LICENSE](LICENSE).
