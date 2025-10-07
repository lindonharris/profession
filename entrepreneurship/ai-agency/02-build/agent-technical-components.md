# Agent Technical Components: Reusable n8n Building Blocks

**Date:** September 30, 2025
**Purpose:** Technical architecture for n8n workflow modules that power AI agents
**Scope:** This is about HOW to build the agents efficiently (reusable components)
**Related:** See `agent-development-plan.md` for what agents to build and when
**Strategy:** Build core modules once, reuse across multiple agents

---

## Executive Summary for Productized Model

**Key Insight:** The 3 top-scoring productized agents (Support Triage, Onboarding Coach, E-commerce Service) share **80% of their core components**.

**Winning Strategy:**
1. Build 8-10 **core modules** first (Weeks 1-4)
2. Combine modules into **3 productized agents** (Weeks 5-8)
3. Each new agent reuses 50-70% of existing modules
4. Time to build agent #2: 50% faster than agent #1
5. Time to build agent #3: 70% faster than agent #1

**Core Modules Priority (Build These First):**
1. **RAG Knowledge Base** (Qdrant + OpenAI) - Used in all 3 agents
2. **Smart Confidence Router** (Switch-based triage) - Used in all 3 agents
3. **Multi-Channel Notifier** (Email/Slack/SMS) - Used in all 3 agents
4. **Ticket/Event Intake** (Webhook + parsing) - Used in all 3 agents
5. **Analytics Tracker** (Postgres + metrics) - Used in all 3 agents

**ROI of Modular Approach:**
- Custom build for each agent: 6-8 weeks × 3 = 18-24 weeks
- Modular build: 4 weeks (modules) + 2 weeks (agent 1) + 1 week (agent 2) + 1 week (agent 3) = **8 weeks total**
- **Time saved:** 10-16 weeks (62-67% faster)
- **Cost saved:** $50K-80K in development time

---

## Philosophy: The Lego Approach

Instead of building 5 custom solutions, we build **15-20 modular components** that can be:
- **Sold individually** ($500-$5K per module)
- **Combined into solutions** (modules = Lego blocks)
- **Customized for industries** (same module, different data sources)
- **Reused across clients** (DRY principle)

**Business model:** Start with simple modules → gain experience → sell integrated solutions → monetize complex systems

---

## Category 1: Data Ingestion Modules

### Module 1.1: Multi-Channel Document Collector
**What it does:** Monitors and collects documents from email, Google Drive, Dropbox, webhooks

**n8n Components:**
- Email Trigger (IMAP)
- Google Drive Watch Trigger
- Dropbox Trigger
- Webhook Trigger
- Code node (file metadata extraction)
- HTTP Request (cloud storage upload)

**Outputs:**
- Standardized file object: `{id, filename, source, uploadedAt, fileType, size, url}`
- Stores in S3/GCS
- Triggers downstream processing

**Broader Applications:**
- **Legal firms:** Collect case documents
- **Real estate:** Property listing documents
- **HR:** Resume collection pipeline
- **Compliance:** Regulatory filing monitoring
- **Academia:** Research paper aggregation

**Pricing:** $1K-3K one-time + $50-100/month hosting

---

### Module 1.2: Email Intelligence Extractor
**What it does:** Parses emails and extracts structured data using AI

**n8n Components:**
- Email Trigger / Webhook
- OpenAI (GPT-4 for extraction)
- Code node (validation, formatting)
- Postgres (storage)

**Outputs:**
- Extracted entities: sender, subject, date, action items, mentioned companies, links
- Sentiment analysis
- Classification (deal flow, customer inquiry, internal, spam)

**Broader Applications:**
- **Sales teams:** Lead extraction from cold emails
- **Customer success:** Customer sentiment tracking
- **Executive assistants:** Action item extraction
- **Recruiters:** Candidate info from applications
- **Journalists:** Source tracking from tips

**Pricing:** $2K-5K setup + $200-500/month (based on volume)

---

### Module 1.3: API Poller with Rate Limit Handler
**What it does:** Safely poll multiple APIs on schedule, handles auth, rate limits, retries

**n8n Components:**
- Schedule Trigger (configurable intervals)
- HTTP Request nodes (with retry logic)
- Code node (rate limit tracking, exponential backoff)
- Redis/Memory store (rate limit counters)
- Error handling branches

**Outputs:**
- Standardized API response data
- Error logs with retry history
- Success/failure metrics

**Broader Applications:**
- **Crypto traders:** Exchange API monitoring
- **SaaS analytics:** Pulling metrics from Stripe, Mixpanel, etc.
- **E-commerce:** Inventory sync across platforms
- **Marketing agencies:** Social media metrics aggregation
- **DevOps teams:** Service health monitoring

**Pricing:** $1K-2K setup + $100-300/month per 10 APIs

---

## Category 2: AI Processing Modules

### Module 2.1: Document Classification & Extraction Engine
**What it does:** Classifies document types and extracts structured data (the DD Assistant core)

**n8n Components:**
- OpenAI GPT-4 Turbo (classification)
- OpenAI Vision API (for scanned docs/images)
- Code node (extraction validation)
- Postgres (structured data)

**Outputs:**
- Document type label + confidence
- Extracted fields (customizable schema)
- Key-value pairs from forms/tables
- Summary of document content

**Broader Applications:**
- **Healthcare:** Medical record processing
- **Insurance:** Claims document extraction
- **Banking:** Loan application processing
- **Government:** Permit/license applications
- **Education:** Student records digitization
- **Accounting:** Invoice/receipt processing

**Pricing:** $5K-10K setup + $0.10-0.50 per document processed

---

### Module 2.2: RAG Knowledge Base (Q&A Agent)
**What it does:** Indexes documents in vector DB, enables natural language Q&A

**n8n Components:**
- Qdrant Vector Store (or Pinecone)
- OpenAI Embeddings
- OpenAI Chat (RAG retrieval)
- Code node (context assembly, citation formatting)
- Webhook (Q&A API endpoint)

**Outputs:**
- Answer to natural language question
- Source citations with page numbers
- Confidence score
- Related questions suggestions

**Broader Applications:**
- **Customer support:** Product documentation Q&A
- **HR:** Company policy chatbot
- **Legal:** Contract/precedent search
- **Healthcare:** Medical protocol assistant
- **Education:** Course material Q&A
- **Technical docs:** Developer documentation search

**Pricing:** $3K-8K setup + $100-500/month (based on document volume)

---

### Module 2.3: Anomaly Detection & Alert Engine
**What it does:** Monitors metrics, detects statistical anomalies, prioritizes alerts

**n8n Components:**
- Schedule Trigger (regular checks)
- Code node (statistical analysis - z-score, moving averages)
- OpenAI (anomaly explanation generation)
- Switch node (alert severity routing)
- Slack / Email / SMS nodes

**Outputs:**
- Anomaly detection (is this data point unusual?)
- Severity level (critical, warning, info)
- Plain-English explanation ("MRR dropped 25% vs last month")
- Recommended actions

**Broader Applications:**
- **E-commerce:** Sales spike/drop alerts
- **DevOps:** Performance degradation detection
- **Finance:** Fraud detection, unusual transactions
- **IoT:** Sensor malfunction alerts
- **Supply chain:** Inventory anomaly detection
- **Web apps:** User engagement drop alerts

**Pricing:** $2K-5K setup + $200-500/month per metric stream

---

### Module 2.4: Multi-Step AI Agent Orchestrator
**What it does:** Coordinates multiple AI tasks in sequence with decision routing

**n8n Components:**
- OpenAI Chat (task planning)
- Switch nodes (decision routing)
- Loop nodes (retry logic)
- Code node (state management)
- Webhook (progress updates)

**Outputs:**
- Executes multi-step AI workflows
- Handles conditional logic (if X then Y)
- Manages conversation context
- Logs decision trail

**Broader Applications:**
- **Any complex AI task** that requires:
  - Multiple LLM calls in sequence
  - Decision trees based on AI responses
  - Stateful conversations
  - Human-in-loop approvals

**Pricing:** $3K-6K setup + $300-800/month (based on complexity)

---

## Category 3: Decision & Routing Modules

### Module 3.1: Smart Router (Confidence-Based Triage)
**What it does:** Routes items to auto-handle, human review, or escalation based on AI confidence

**n8n Components:**
- OpenAI (classification with confidence)
- Code node (confidence threshold logic)
- Switch node (routing)
- Slack (human approval interface)
- Postgres (audit trail)

**Outputs:**
- Routing decision (auto / review / escalate)
- Confidence score
- Human approval workflow (if needed)
- Decision log

**Broader Applications:**
- **Content moderation:** Auto-approve, flag for review, ban
- **Loan processing:** Auto-approve, manual review, auto-reject
- **Lead scoring:** Hot lead alert, nurture, disqualify
- **Hiring:** Phone screen, in-person, reject
- **Customer support:** See Support Autopilot
- **Quality control:** Pass, inspect, fail

**Pricing:** $2K-4K setup + $150-400/month

---

### Module 3.2: Deduplication & Merge Engine
**What it does:** Finds duplicate records using fuzzy matching, merges with conflict resolution

**n8n Components:**
- Code node (fuzzy matching algorithms - Levenshtein distance)
- OpenAI (semantic similarity for text)
- Qdrant (vector similarity for embeddings)
- Postgres (dedupe tracking)
- HTTP Request (update source systems)

**Outputs:**
- Duplicate groups with confidence scores
- Merged record (canonical version)
- Conflict resolution logic
- Audit trail of merges

**Broader Applications:**
- **CRM cleanup:** Merge duplicate contacts/companies
- **E-commerce:** Product catalog deduplication
- **Data warehouses:** Entity resolution across sources
- **Marketing:** Email list deduplication
- **Healthcare:** Patient record matching
- **Finance:** Transaction reconciliation

**Pricing:** $3K-7K setup + $0.01-0.05 per record processed

---

## Category 4: User Interaction Modules

### Module 4.1: Multi-Channel Notification Orchestrator
**What it does:** Sends notifications via email, Slack, SMS, webhooks with delivery tracking

**n8n Components:**
- Email Send node
- Slack node
- Twilio SMS node
- HTTP Request (webhook, push notifications)
- Code node (template rendering, personalization)
- Postgres (delivery log)

**Outputs:**
- Notification sent to user's preferred channel
- Delivery confirmation
- Click/open tracking (if applicable)
- Retry logic for failures

**Broader Applications:**
- **Any application** that needs to notify users
- Alerts, reminders, reports, confirmations
- Escalation workflows (try email → Slack → SMS)

**Pricing:** $1K-2K setup + $0.01-0.10 per notification

---

### Module 4.2: Conversational Workflow Manager (Chatbot State Machine)
**What it does:** Manages multi-turn conversations with context, handles user intent, maintains state

**n8n Components:**
- Webhook (chat interface integration)
- OpenAI Chat (intent detection, response generation)
- Redis (conversation state storage)
- Code node (state machine logic)
- Switch node (intent routing)

**Outputs:**
- Contextual response to user message
- State updates (where in workflow)
- Action triggers (based on user intent)
- Conversation history

**Broader Applications:**
- **Onboarding bots:** See Onboarding Coach
- **Survey bots:** Conversational surveys
- **Appointment booking:** Natural language scheduling
- **Ordering bots:** E-commerce via chat
- **Troubleshooting wizards:** Step-by-step support
- **Form filling:** Conversational data collection

**Pricing:** $2K-5K setup + $200-600/month

---

### Module 4.3: Approval Workflow Engine (Human-in-Loop)
**What it does:** Sends items to humans for approval via Slack, tracks decisions, executes actions

**n8n Components:**
- Slack (approval buttons)
- Webhook (approval responses)
- Code node (timeout handling)
- Postgres (pending approvals tracking)
- Switch node (approved/rejected routing)

**Outputs:**
- Approval request sent to human
- Approval/rejection captured
- Timeout handling (auto-approve or escalate after X hours)
- Decision audit trail

**Broader Applications:**
- **Expense approvals:** Manager reviews purchases
- **Content publishing:** Editorial review before publish
- **Code deployments:** Production deploy approvals
- **Marketing campaigns:** Review before sending
- **Legal contracts:** Review before signing
- **Any AI output** that needs human validation

**Pricing:** $1K-3K setup + $100-300/month

---

## Category 5: Data Output Modules

### Module 5.1: Report Generation Engine
**What it does:** Generates formatted reports (PDF, Excel, Slides) from data with AI summaries

**n8n Components:**
- Code node (data aggregation, calculations)
- OpenAI (narrative summary generation)
- HTTP Request (Google Docs API, PowerPoint API)
- PDF generation node
- Email Send (delivery)

**Outputs:**
- Formatted report document
- AI-generated executive summary
- Visualizations (charts, tables)
- Distribution via email/Slack

**Broader Applications:**
- **Financial reports:** Monthly P&L summaries
- **Sales reports:** Weekly pipeline reviews
- **Marketing reports:** Campaign performance
- **Operations reports:** KPI dashboards
- **Portfolio reports:** See Portfolio Dashboard
- **Academic reports:** Student progress summaries

**Pricing:** $2K-5K setup + $50-200/month

---

### Module 5.2: Dashboard Feed API
**What it does:** Exposes processed data via webhook API for external dashboards

**n8n Components:**
- Webhook (API endpoint)
- Postgres (data queries)
- Code node (API response formatting, pagination)
- Redis (caching for performance)

**Outputs:**
- REST API with standardized JSON responses
- Filtering, sorting, pagination support
- Authentication (API keys)
- Rate limiting

**Broader Applications:**
- **Any internal dashboard** (Grafana, Tableau, Retool)
- Mobile apps needing backend data
- Third-party integrations
- Custom web applications

**Pricing:** $1K-3K setup + $100-400/month

---

### Module 5.3: CRM/Database Sync Engine
**What it does:** Bidirectional sync between n8n workflows and CRM/database systems

**n8n Components:**
- Webhook (updates from external system)
- HTTP Request (CRM APIs - Salesforce, HubSpot, Airtable)
- Code node (field mapping, transform logic)
- Postgres (local cache for offline capability)
- Schedule Trigger (batch sync jobs)

**Outputs:**
- Real-time or scheduled sync
- Conflict resolution (last-write-wins or custom)
- Sync status logs
- Error handling with retry

**Broader Applications:**
- **Sales ops:** Sync deal data to Salesforce
- **Marketing ops:** Sync leads to HubSpot
- **Customer success:** Sync support tickets to Zendesk
- **Operations:** Sync inventory to ERP
- **Finance:** Sync transactions to QuickBooks

**Pricing:** $2K-6K setup + $200-800/month per CRM

---

## Implementation Strategy: Build → Sell → Learn → Scale

### Phase 1: Foundation Modules (Weeks 1-4)
**Build these first** (most reusable, least complex):
1. Multi-Channel Document Collector ($1K-3K)
2. Multi-Channel Notification Orchestrator ($1K-2K)
3. API Poller with Rate Limit Handler ($1K-2K)

**Sell to:** SaaS startups, small agencies, internal tools teams
**Revenue potential:** $3K-7K per customer (bundle)

### Phase 2: AI Processing Modules (Weeks 5-10)
**Build next** (higher value, moderate complexity):
4. Email Intelligence Extractor ($2K-5K)
5. RAG Knowledge Base ($3K-8K)
6. Smart Router ($2K-4K)

**Sell to:** Customer support teams, sales teams, operations teams
**Revenue potential:** $7K-17K per customer

### Phase 3: Complex Integrated Solutions (Weeks 11-20)
**Combine modules** into full solutions:
7. Support Autopilot = Modules 1.2 + 2.2 + 3.1 + 4.1 + 4.3
8. DD Assistant = Modules 1.1 + 2.1 + 2.2 + 3.2 + 5.1

**Sell to:** Mid-market companies, PE/VC firms, enterprise pilots
**Revenue potential:** $20K-100K per customer

### Phase 4: Industry-Specific Packages (Month 6+)
**Verticalize** for specific industries:
- **Legal Tech Package:** Document processing + RAG + approval workflows
- **Healthcare Package:** Medical record extraction + compliance alerts
- **Finance Package:** Document DD + anomaly detection + reporting

**Sell to:** Industry-specific buyers with bigger budgets
**Revenue potential:** $50K-250K per customer

---

## Module Dependency Map

```
Foundation Modules (no dependencies):
├─ Document Collector
├─ Notification Orchestrator
└─ API Poller

Intermediate Modules (depend on foundation):
├─ Email Extractor (uses Notification)
├─ RAG Knowledge Base (uses Document Collector)
├─ Smart Router (uses Notification)
├─ Deduplication Engine (standalone)
└─ Report Generator (uses Notification)

Advanced Modules (depend on intermediate):
├─ Anomaly Detection (uses Smart Router + Notification)
├─ Multi-Step AI Orchestrator (uses Smart Router + Notification)
├─ Conversational Manager (uses Smart Router)
└─ Approval Workflow (uses Notification + Smart Router)

Complete Solutions (combine multiple modules):
├─ Support Autopilot
├─ DD Assistant
├─ Deal Intelligence Hub
├─ Onboarding Coach
└─ Portfolio Dashboard
```

---

## Pricing Strategy

### Individual Modules
- **Simple modules:** $1K-3K setup + $50-300/month
- **Moderate modules:** $2K-5K setup + $200-600/month
- **Complex modules:** $3K-8K setup + $300-1K/month

### Bundled Solutions
- **3-module bundle:** $5K-15K (20% discount)
- **5-module bundle:** $10K-30K (30% discount)
- **Complete solution:** $20K-100K (custom pricing)

### Revenue Models
1. **One-time setup** + monthly SaaS (recurring)
2. **Usage-based** ($0.01-0.50 per transaction)
3. **White-label** (agencies resell at 2-5x markup)
4. **Enterprise license** (unlimited use, annual contract)

---

## Marketing Approach

### Entry Point: "Free Audit"
1. Offer free process audit (1 hour consultation)
2. Identify 3-5 automation opportunities
3. Propose modular solution (not custom build)
4. Start with 1-2 modules ($5K-10K)
5. Expand based on success

### Content Marketing
- **Blog:** "10 AI Workflow Modules Every SaaS Needs"
- **YouTube:** Build each module tutorial
- **GitHub:** Open-source simple versions (lead magnet)
- **Newsletter:** Weekly automation tips

### Sales Strategy
1. **Inbound:** Content → demo → pilot → expand
2. **Outbound:** Target early adopters (SaaS, VC/PE)
3. **Partnerships:** Agencies white-label our modules
4. **Marketplace:** List on n8n community templates

---

## Success Metrics

### Per Module
- **Time to build:** <1 week
- **Time to sell:** <2 weeks (after first)
- **Setup time:** <1 day
- **Customer ROI:** >5x within 6 months

### Business Goals
- **Month 1-3:** Build 6 foundation modules
- **Month 4-6:** 10 customers @ $5K-15K each = $50K-150K
- **Month 7-12:** 30 customers @ $10K-50K each = $300K-1.5M
- **Year 2:** Enterprise deals $50K-250K each

---

## Key Insight: The Module Advantage

**Traditional agency model:**
- Custom build every project (doesn't scale)
- Start from scratch each time
- High cost = high price = small market
- Knowledge doesn't transfer

**Module model:**
- Build once, sell 100x
- Each sale improves the module
- Low marginal cost = flexible pricing = bigger market
- Expertise compounds

**Example:**
- Custom DD solution: 8 weeks @ $200/hr = $64K (one customer)
- Module-based DD solution: 8 weeks build, then sell to 20 firms @ $30K each = $600K

**The math:** Same 8 weeks of work, 10x the revenue.

---

## Next Steps

1. **Build MVP of Module 1.1** (Document Collector) - 3-5 days
2. **Create demo video** - 1 day
3. **Launch landing page** - 1 day
4. **Run pilot with 3 customers** (free) - get testimonials
5. **Iterate based on feedback**
6. **Build Module 1.2** (Email Extractor)
7. **Bundle Modules 1.1 + 1.2** = "Data Ingestion Suite" ($5K)
8. **Repeat**

**Timeline to first dollar:** 4-6 weeks (if moving fast)

---

*This modular approach transforms you from "custom developer" to "product company" while maintaining flexibility for client needs.*
