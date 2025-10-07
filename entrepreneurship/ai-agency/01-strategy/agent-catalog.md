# AI Agent Catalog - buyanagent.ai

**Last Updated:** October 6, 2025 (Tiered Strategy Implemented)
**Total Agents:** 5 MVP agents (3 Utility + 2 Premium)
**Pricing Model:** Two-tier (Utility $29-79/mo, Premium $100-150/mo)
**Service Delivery:** Utility = Status Pages, Premium = Full Dashboards

---

## 🎯 MVP Agent Lineup (5 Agents)

### **Tier Classification**

**Utility Tier** - Invisible Automation ($29-79/month)
- Email Sweeper
- Newsletter Digester
- Expense Manager
- **Interface:** Simple status page (health + activity metrics)
- **Value Prop:** "Set it and forget it" automation

**Premium Tier** - Business Intelligence ($100-150/month)
- Invoice Chaser
- Lead Qualification
- **Interface:** Full analytics dashboard (charts, trends, controls)
- **Value Prop:** Measurable ROI + decision intelligence

---

## Utility Tier Agents

### 1. Email Sweeper 🗑️

**Tier:** Utility
**Price:** $29-39/month
**Category:** Productivity / Email Management
**Complexity:** Low
**Build Time:** 1-2 weeks

#### What It Does

Automatically scans your inbox for noise (spam, promotions, unread newsletters), unsubscribes from unwanted lists, deletes junk emails, and archives low-priority messages. Works invisibly in the background - you never see the clutter.

**Core Functionality:**
- Email scanning (every 2 hours)
- AI-powered spam/noise detection
- One-click unsubscribe from mailing lists
- Automatic deletion of promotional emails
- Smart archiving of low-priority messages
- Whitelist protection (VIP senders never touched)

#### Why This Agent

**Market Validation:**
- **Clean Email:** 500K+ users at $10/month
- **SaneBox:** 300K+ users at $7/month
- **Leave Me Alone:** 100K+ users at $19 one-time
- **Market gap:** No AI-powered solution combining all 3 features

**Customer Pain:**
- "I get 200 emails/day, 150 are noise"
- "I spend 30 min/day managing my inbox"
- "Unsubscribing manually takes forever"

#### Status Page + Control Panel (Utility Tier Interface)

```
Email Sweeper
─────────────────────────────────────────────

Status: ✓ Running
Last scan: 2 hours ago
Next scan: In 2 hours

Today's Activity:
─────────────────
47 emails processed
  • 23 unsubscribed
  • 18 archived
  • 6 deleted

This Week:
─────────────────
312 emails processed
167 hours saved (est.)

═══════════════════════════════════════════════
CONTROL PANEL
═══════════════════════════════════════════════

Essential Controls:
─────────────────
[⏸ Pause Agent]  [⚙️ Settings]  [📜 History]  [🔌 Integrations]

Agent-Specific Controls:
─────────────────────────
• ⭐ Manage VIP Senders (whitelist/never touch)
• 🎚️ Noise Filter Sensitivity (Low/Medium/High)
• ⚡ Action Preferences (Unsubscribe/Delete/Archive priority)
• 📊 Download Activity Report (CSV export)
• ⏱️ Scan Frequency (Every 1hr/2hr/4hr/Daily)

Quick Actions:
─────────────────
[+ Add VIP Sender]  [Adjust Filters]  [View Full Log]
```

#### Setup Time

**15-20 minutes**

#### Integrations Required

- Gmail or Outlook (email access via OAuth)
- Optional: Slack (daily summary notifications)

#### Setup Steps

1. Connect email account (Gmail/Outlook via OAuth)
2. Choose noise categories to filter (promotions, newsletters, updates)
3. Set VIP senders whitelist (never touch these)
4. Configure action preferences (unsubscribe vs delete vs archive)
5. Test with 10 sample emails
6. Activate

#### Value Proposition

- **Time savings:** 30 min/day → 5 min/day (83% reduction)
- **Mental clarity:** Inbox drops from 200 unread → 15 important
- **Unsubscribe automation:** AI handles what takes you hours manually
- **Set and forget:** No ongoing maintenance required

#### Pricing

- **Utility Tier:** $29-39/month
- **No Premium tier** (simple automation doesn't need dashboard)

#### Technical Details

- **Trigger:** Cron job every 2 hours + webhook (new email arrival)
- **Data source:** Gmail/Outlook API (read inbox, scan headers)
- **AI:** GPT-4 for noise classification (spam, promotional, newsletter, important)
- **Logic:** Category detection → action routing (unsubscribe/delete/archive)
- **Actions:** Gmail/Outlook API (delete, archive, unsubscribe via List-Unsubscribe header)
- **Tracking:** Postgres (action history, whitelist, processing stats)
- **Frequency:** Every 2 hours + real-time webhook processing

#### Competitive Positioning

vs **Clean Email** ($10/month), **SaneBox** ($7/month), **Leave Me Alone** ($19 one-time)

**Our Differentiation:**
- AI-powered classification (vs rule-based filters)
- Combined unsubscribe + delete + archive (vs separate tools)
- Simple status page (vs bloated dashboards)
- $29-39 = 2-3x competitors but 10x smarter automation

---

### 2. Newsletter Digester 📰

**Tier:** Utility
**Price:** $49-59/month
**Category:** Productivity / Content Consumption
**Complexity:** Low
**Build Time:** 1-2 weeks

#### What It Does

Automatically identifies newsletters in your inbox, extracts key points using AI summarization, and delivers a single daily digest with highlights from all your subscriptions. Never miss important insights, never waste time reading full newsletters.

**Core Functionality:**
- Newsletter detection (Substack, Beehiiv, Medium, custom)
- AI summarization (GPT-4 extracts 3-5 key points per newsletter)
- Daily digest delivery (single email at 7am with all summaries)
- Link preservation (click to read full newsletter if interested)
- Archive original newsletters (declutter inbox)

#### Why This Agent

**Market Validation:**
- **Unroll.me:** 1M+ users (free/$5 month) - but no AI summarization
- **Substack app:** 1M+ installs - but no cross-platform digest
- **Market gap:** AI-powered newsletter summarization doesn't exist at consumer price

**Customer Pain:**
- "I subscribe to 20 newsletters but only read 2"
- "Important insights get lost in my inbox"
- "I feel guilty deleting newsletters without reading"

#### Status Page + Control Panel (Utility Tier Interface)

```
Newsletter Digester
─────────────────────────────────────────────

Status: ✓ Running
Last digest: Today 7:00 AM
Next digest: Tomorrow 7:00 AM

Today's Summary:
─────────────────
8 newsletters tracked
24 key points extracted
1 digest delivered to inbox

This Week:
─────────────────
56 newsletters processed
168 key points summarized
7 digests delivered

═══════════════════════════════════════════════
CONTROL PANEL
═══════════════════════════════════════════════

Essential Controls:
─────────────────
[⏸ Pause Agent]  [⚙️ Settings]  [📜 History]  [🔌 Integrations]

Agent-Specific Controls:
─────────────────────────
• 📬 Manage Subscriptions (add/remove newsletters)
  ☑ The Hustle  ☑ Morning Brew  ☑ Lenny's Newsletter
  ☐ TechCrunch Daily  ☑ First Round Review
• ⏰ Digest Schedule (Daily 7am / Custom time)
• 📝 Summary Length (Brief 2-3 points / Detailed 4-5 points)
• 📨 Delivery Method (Email / Slack / Both)
• 🔗 Include Full Links (Yes/No)
• 📊 Download Digest Archive (PDF export)

Quick Actions:
─────────────────
[+ Add Newsletter]  [Change Time]  [Preview Digest]
```

#### Setup Time

**15-20 minutes**

#### Integrations Required

- Gmail or Outlook (newsletter scanning + digest delivery)
- Optional: Slack (digest delivery alternative)

#### Setup Steps

1. Connect email account (Gmail/Outlook via OAuth)
2. AI scans inbox and detects newsletters (last 30 days)
3. Select which newsletters to track (checkboxes)
4. Choose digest schedule (daily 7am, or custom time)
5. Choose delivery method (email or Slack)
6. Test with sample digest
7. Activate

#### Value Proposition

- **Time savings:** 2 hours/week reading newsletters → 15 min/week reading digest
- **Information retention:** Never miss key insights from subscriptions
- **Guilt-free:** Stay subscribed, get summaries, read full newsletter if interested
- **Inbox clarity:** Newsletters archived automatically after processing

#### Pricing

- **Utility Tier:** $49-59/month
- **No Premium tier** (simple summarization doesn't need dashboard)

#### Technical Details

- **Trigger:** Daily cron (5am) + webhook (new newsletter arrival)
- **Data source:** Gmail/Outlook API (scan for newsletter senders)
- **AI:** GPT-4 for summarization (extract 3-5 key points per newsletter, max 100 words)
- **Logic:** Newsletter detection → summarization → digest assembly
- **Delivery:** SendGrid or Gmail API (send digest email)
- **Tracking:** Postgres (newsletter list, summary history, read receipts)
- **Frequency:** Daily at 7am (configurable)

#### Competitive Positioning

vs **Unroll.me** (Free/$5 month - no AI), **Substack app** (free - Substack only)

**Our Differentiation:**
- AI summarization (vs simple digest)
- Cross-platform (Substack, Beehiiv, Medium, custom newsletters)
- Single daily email (vs 20 separate newsletters)
- $49-59 = 10x Unroll.me BUT delivers AI-extracted insights, not just inbox organization

---

### 3. Expense Manager 💰

**Tier:** Utility
**Price:** $69-79/month
**Category:** Finance / Expense Tracking
**Complexity:** Low-Moderate
**Build Time:** 2-3 weeks

#### What It Does

Scans your Gmail inbox for receipts and invoices, uses GPT-4 to extract vendor name, amount, date, and category, then automatically logs everything to a Google Sheet with proper categorization. Never manually enter expenses again.

**Core Functionality:**
- Receipt detection (PDF attachments, email body receipts)
- OCR + AI extraction (vendor, amount, date, category)
- Auto-categorization (Travel, Meals, Office Supplies, Software, etc.)
- Google Sheets logging (one row per expense, real-time sync)
- Monthly expense reports (summary email)

#### Why This Agent

**Market Validation:**
- **Expensify:** 10M+ users ($5-20/month)
- **QuickBooks Self-Employed:** 2M+ users ($20/month)
- **Shoeboxed:** 500K+ users ($18-36/month)
- **Market gap:** AI-powered receipt extraction at low price point

**Customer Pain:**
- "I spend 2 hours/week manually entering expenses"
- "I lose receipts and can't deduct at tax time"
- "Expense apps are bloated accounting software - I just need simple tracking"

#### Status Page + Control Panel (Utility Tier Interface)

```
Expense Manager
─────────────────────────────────────────────

Status: ✓ Running
Last scan: 1 hour ago
Next scan: In 3 hours

Today's Activity:
─────────────────
5 receipts scanned
$427.83 logged
Categories: Travel (2), Meals (2), Software (1)

This Month:
─────────────────
68 receipts processed
$4,281.15 total expenses
Top category: Software ($1,450)

═══════════════════════════════════════════════
CONTROL PANEL
═══════════════════════════════════════════════

Essential Controls:
─────────────────
[⏸ Pause Agent]  [⚙️ Settings]  [📜 History]  [🔌 Integrations]

Agent-Specific Controls:
─────────────────────────
• 📁 Manage Categories
  - Travel  - Meals & Entertainment  - Office Supplies
  - Software & Subscriptions  - Professional Services
  [+ Add Custom Category]
• 📧 Receipt Forwarding Email (expenses@buyanagent.ai)
• 📊 Select Google Sheet (Current: "2025 Expenses" / Change)
• 🎯 Category Rules Editor (Auto-assign vendors to categories)
  Example: "Uber" → Travel, "Amazon" → Office Supplies
• 💵 Currency Settings (USD / Multi-currency)
• 📥 Download Monthly Report (CSV/PDF)

Quick Actions:
─────────────────
[+ Add Category]  [Edit Rules]  [View Sheet]  [Forward Receipt]
```

#### Setup Time

**20-25 minutes**

#### Integrations Required

- Gmail (receipt scanning)
- Google Sheets (expense logging)
- Optional: Slack (monthly expense report)

#### Setup Steps

1. Connect Gmail account (OAuth)
2. Connect Google Sheets account (OAuth)
3. Select expense categories (Travel, Meals, Office Supplies, Software, etc.)
4. Choose Google Sheet for logging (create new or use existing)
5. Set up custom categories (optional)
6. Test with 3 sample receipts
7. Activate

#### Value Proposition

- **Time savings:** 2 hours/week → 0 hours/week (100% automation)
- **Tax deduction protection:** Never miss a receipt
- **Real-time tracking:** Expenses logged same-day, not month-end
- **No accounting software:** Simple Google Sheet, not bloated platform

#### Pricing

- **Utility Tier:** $69-79/month
- **No Premium tier** (simple logging doesn't need dashboard)

#### Technical Details

- **Trigger:** Cron job every 4 hours + webhook (email with attachment)
- **Data source:** Gmail API (scan for receipt keywords, PDF attachments)
- **OCR:** Google Cloud Vision API (PDF text extraction)
- **AI:** GPT-4 for data extraction (vendor, amount, date, category)
- **Logic:** Receipt detection → OCR → AI extraction → categorization → Google Sheets append
- **Delivery:** Google Sheets API (append row with expense data)
- **Tracking:** Postgres (receipt history, processing status, category mappings)
- **Frequency:** Every 4 hours + real-time webhook

#### Competitive Positioning

vs **Expensify Lite** ($5/month), **QuickBooks Self-Employed** ($20/month), **Shoeboxed** ($18-36/month)

**Our Differentiation:**
- AI extraction (vs manual entry or basic OCR)
- Google Sheets integration (vs proprietary apps)
- Simple status page (vs bloated accounting interfaces)
- $69-79 = 3-4x Expensify BUT fully automated AI categorization + zero manual entry

---

## Premium Tier Agents

### 4. Invoice Chaser 💵

**Tier:** Premium
**Price:** $100/month
**Category:** Finance / Cash Flow Management
**Complexity:** Moderate
**Build Time:** 3-4 weeks

#### What It Does

Automatically monitors accounting software (QuickBooks, Xero, Stripe) for unpaid invoices, sends escalating payment reminders with AI-personalized tone, flags VIP customers for human review, and tracks Days Sales Outstanding (DSO) improvements with full analytics dashboard. Transforms cash conversion cycle from 45 days to 28 days average.

**Core Functionality:**
- Invoice monitoring (daily sync with accounting software)
- Automated reminder sequences (3-day, 7-day, 14-day, 30-day escalation)
- AI-personalized email tone (friendly → professional → firm → collections)
- VIP flagging (high-value invoices require manual approval)
- Payment tracking (webhook updates from Stripe/PayPal)
- DSO analytics dashboard (trends, velocity, client behavior)

#### Why This Agent

**Market Validation:**
- **19 explicit Reddit requests** ("I spend 4 hours/week chasing invoices")
- **Zapier #6 most installed workflow:** 1.1M+ installations
- **n8n #5 popular workflow:** 612 clones
- Proven willingness to pay (Bonsai, HoneyBook, Dubsado built businesses on this)

**Customer Pain:**
- "Clients pay 45-60 days late, killing my cash flow"
- "I hate chasing invoices - feels uncomfortable"
- "I waste 4+ hours/week on payment follow-ups"

**Business Impact:**
- **Cash conversion cycle improvement = measurable ROI**
- Direct impact on business survival (cash flow)
- Not just "nice to have" - it's **critical business infrastructure**

#### Dashboard + Advanced Control Panel (Premium Tier Interface)

```
═══════════════════════════════════════════════
INVOICE CHASER DASHBOARD
═══════════════════════════════════════════════

[📊 Analytics] [📄 Invoices] [⚙️ Settings] [📈 Reports] [🔔 Notifications]

Days Sales Outstanding (DSO) Trend
─────────────────────────────────
Jan: 52 days → Feb: 47 days → Mar: 38 days → Apr: 28 days ✓

Current DSO: 28 days (37% improvement vs Jan)
Target DSO: 30 days or less
Cash Flow Impact: +$12,400 this quarter

Overdue Invoices (5 total, $18,750)
─────────────────────────────────────────────
1. Acme Corp - $8,500 (22 days overdue)
   Last reminder: 7 days ago (opened, not paid)
   [Send Now] [Skip] [Mark Paid] [View History]

2. Widget Inc - $5,000 (14 days overdue)
   Last reminder: 3 days ago (not opened)
   [Send Now] [Skip] [Mark Paid] [View History]

[View All 5 Invoices →]

Client Payment Behavior
─────────────────────────────────
Fast Payers (< 10 days): 12 clients
On-Time (10-30 days): 28 clients
Slow Payers (> 30 days): 5 clients ⚠️

═══════════════════════════════════════════════
CONTROL PANEL
═══════════════════════════════════════════════

Essential Controls:
─────────────────
[⏸ Pause Agent]  [⚙️ Settings]  [📜 History]  [🔌 Integrations]
[📊 Export DSO Report]  [📅 Custom Date Range]  [🔔 Notifications]

Agent-Specific Controls:
─────────────────────────
• 📆 Escalation Schedule Editor (Visual Timeline)
  Day -5 → Friendly heads-up
  Day 0 → Payment due notice
  Day +3 → Professional follow-up
  Day +7 → Firm reminder
  Day +15 → Final notice
  Day +30 → Collections escalation
  [Edit Schedule] [Preview Emails]

• ✉️ Email Template Customizer (Per escalation stage)
  [Edit Friendly] [Edit Professional] [Edit Firm] [Edit Final]

• ⭐ VIP Client Rules
  - Invoice threshold: $5,000+ requires manual approval
  - VIP clients (never auto-send): [Manage List]
  - Approval workflow: Slack notification required

• 🏷️ Client Payment Behavior Tags
  - Auto-tag slow payers (>30 days average)
  - Auto-tag fast payers (<10 days average)
  - Custom tags: [Add Tag]

• 📧 Sender Email Settings (From name, signature, reply-to)

• 🔗 Payment Link Settings (Stripe, PayPal, ACH options)

Quick Actions:
─────────────────
[Send All Due Reminders]  [Export Client Report]  [Add VIP Client]
[Customize Template]  [View Sent History]  [Schedule Manual Send]
```

#### Setup Time

**30-40 minutes**

#### Integrations Required

- QuickBooks, Xero, or Stripe (invoice data)
- SendGrid or email provider (reminder sending)
- Slack (optional: VIP approval workflows)

#### Setup Steps

1. Connect accounting software (QuickBooks/Xero/Stripe via OAuth)
2. Configure escalation schedule:
   - Day 15 (5 days before due): Friendly reminder
   - Day 20 (due date): Payment due notice
   - Day 23 (3 days overdue): First follow-up
   - Day 27 (7 days overdue): Professional follow-up
   - Day 35 (15 days overdue): Firm notice
   - Day 50 (30 days overdue): Collections escalation
3. Set VIP thresholds (invoices >$5K require approval before sending)
4. Customize email tone (AI generates, you approve templates)
5. Test with 2 sample invoices
6. Activate dashboard + automation

#### Value Proposition

- **Cash flow improvement:** Get paid 17 days faster (DSO: 45 → 28 days)
- **Time savings:** 4 hours/week → 30 min/week (87% reduction)
- **Late payment reduction:** 40% → 15% (62% improvement)
- **Business-critical:** Cash conversion cycle = survival for small businesses
- **Dashboard intelligence:** See which clients pay late, optimize reminder timing

#### Pricing

- **Premium Tier:** $100/month (includes full dashboard + automation)
- **No Utility tier** (dashboard = core value, not optional)

#### Technical Details

- **Trigger:** Daily cron (9am) + webhook (invoice created/paid)
- **Data source:** QuickBooks/Xero/Stripe API (pull unpaid invoices)
- **AI:** GPT-4 for personalized email tone generation (friendly → firm escalation)
- **Logic:** Days overdue calculation, escalation stage routing, VIP flagging
- **Approval:** Slack interactive messages for VIP/high-amount invoices
- **Delivery:** SendGrid (email sending with open/click tracking)
- **Dashboard:** React + Recharts (DSO trends, payment velocity, client behavior)
- **Tracking:** Postgres (reminder history, payment updates, DSO metrics)
- **Frequency:** Daily checks at 9am + real-time payment webhook updates

#### Competitive Positioning

vs **Bonsai** ($25-50/month), **HoneyBook** ($40-80/month), **Dubsado** ($35-75/month)

**Our Differentiation:**
- Standalone invoice reminder agent (vs full accounting/CRM platform)
- AI-powered escalation tone (vs static templates)
- DSO analytics dashboard (vs basic reports)
- $100 = 2-3x Bonsai BUT no bloated CRM features you don't need + intelligent dashboard

**Key Message:**
"You don't need a full accounting platform. You need invoice reminders that work + analytics that show improvement."

---

### 5. Lead Qualification 📊

**Tier:** Premium
**Price:** $100-150/month
**Category:** Sales / Lead Management
**Complexity:** Moderate
**Build Time:** 3-4 weeks

#### What It Does

Automatically scores and qualifies inbound leads using AI analysis of company size, budget signals, intent keywords, and LinkedIn data. Routes hot leads to sales immediately, nurtures warm leads, and archives cold leads. Includes full dashboard with lead pipeline, scoring breakdown, conversion metrics, and enrichment data.

**Core Functionality:**
- Lead scoring (0-100 scale based on AI analysis)
- Data enrichment (LinkedIn, Clearbit, Hunter.io APIs)
- Automatic routing (hot → sales alert, warm → nurture, cold → archive)
- Lead pipeline dashboard (conversion funnel, time-to-contact, scoring trends)
- Scoring transparency (see why each lead got their score)

#### Why This Agent

**Market Validation:**
- **16 explicit Reddit requests** ("Need AI to qualify leads before I waste time")
- **Low competition** (only 2-3 specialized tools vs 10+ CRM filters)
- **High-value use case** (sales time = most expensive resource)
- **Complements Invoice Agent** (lead → qualify → win → invoice → get paid workflow)

**Customer Pain:**
- "I waste 5 hours/week researching leads that won't buy"
- "I respond to everyone the same - should prioritize hot leads"
- "CRM filters are basic - need AI to detect buying intent"

**Business Impact:**
- Save 5+ hours/week on manual lead research
- 30%+ close rate improvement (focus on qualified prospects only)
- Faster response to hot leads (5 min vs 2 hours average)

#### Dashboard + Advanced Control Panel (Premium Tier Interface)

```
═══════════════════════════════════════════════
LEAD QUALIFICATION DASHBOARD
═══════════════════════════════════════════════

[📊 Pipeline] [🎯 Scoring] [📈 Conversion] [⚙️ Settings] [📋 Sources]

Lead Pipeline (Last 30 Days)
─────────────────────────────────────────────
Total Leads: 127

Hot (80-100):   18 leads (14%) → 12 contacted, 6 pending
Warm (50-79):   52 leads (41%) → In nurture sequence
Cold (0-49):    57 leads (45%) → Archived

Conversion Rate: 38% (hot leads → customers)
Avg Time-to-Contact: 8 minutes (hot leads)

Latest Lead: Acme Corp (Score: 85/100) 🔥
─────────────────────────────────────────────
Scoring Breakdown:
✓ Company size: 50-200 employees (+25 points)
✓ Budget signals: "enterprise plan" in email (+20 points)
✓ Job title: VP of Sales (decision maker) (+20 points)
✓ Website: Fortune 1000 company (+15 points)
⚠ Location: International (-5 points)

Enrichment Data:
- LinkedIn: 180 employees, Series B funded
- Industry: SaaS (target vertical)
- Tech stack: Salesforce, HubSpot

[Route to Sales] [Add to Nurture] [Archive] [View Full Profile]

Lead Source Performance
─────────────────────────────────
1. Website form: 68 leads (avg score 62)
2. LinkedIn InMail: 32 leads (avg score 74) 🔥
3. Referrals: 18 leads (avg score 81) 🔥

═══════════════════════════════════════════════
CONTROL PANEL
═══════════════════════════════════════════════

Essential Controls:
─────────────────
[⏸ Pause Agent]  [⚙️ Settings]  [📜 History]  [🔌 Integrations]
[📊 Export Pipeline]  [📅 Custom Date Range]  [🔔 Notifications]

Agent-Specific Controls:
─────────────────────────
• 🎯 Scoring Criteria Editor (Weight sliders)
  Company size (10-500 employees): 25% weight [████████░░]
  Budget signals ($500-5K/mo): 20% weight [██████░░░░]
  Job title (VP/Director/C-suite): 20% weight [██████░░░░]
  Industry match (SaaS/Ecommerce): 15% weight [█████░░░░░]
  Geography (US/Canada): 10% weight [███░░░░░░░]
  Tech stack compatibility: 10% weight [███░░░░░░░]
  [Reset to Defaults] [Save Custom]

• 🚦 Threshold Settings
  Hot leads (auto-route to sales): 80-100 points
  Warm leads (nurture sequence): 50-79 points
  Cold leads (auto-archive): 0-49 points
  [Adjust Thresholds]

• 🔍 Enrichment Data Sources
  ☑ LinkedIn Sales Navigator (enabled)
  ☑ Clearbit API (enabled)
  ☑ Hunter.io email validation (enabled)
  ☐ ZoomInfo (disabled - upgrade required)
  [Manage API Keys]

• 📨 Routing Rules
  Hot leads → Slack alert + Assign to: [Sales Rep ▼]
  Warm leads → Add to: [Nurture Campaign ▼]
  Cold leads → Archive with reason
  [Edit Routing Workflow]

• 🏷️ Lead Tagging & Filters
  - Auto-tag by source (Website, LinkedIn, Referral, etc.)
  - Auto-tag by industry (SaaS, Ecommerce, Agency, etc.)
  - Custom tags: [Add Tag]

• ⏱️ Time-to-Contact Alerts
  Alert if hot lead not contacted within: [5 minutes ▼]
  Escalation if still pending after: [30 minutes ▼]

Quick Actions:
─────────────────
[Score All Pending]  [Export Hot Leads]  [Adjust Criteria]
[Test Scoring]  [View Conversion Report]  [Manage Tags]
```

#### Setup Time

**35-45 minutes**

#### Integrations Required

- HubSpot, Salesforce, or Pipedrive (CRM)
- LinkedIn Sales Navigator (optional: enrichment)
- Email or Slack (hot lead alerts)

#### Setup Steps

1. Connect CRM (HubSpot/Salesforce/Pipedrive via OAuth)
2. Define qualification criteria:
   - Company size range (e.g., 10-500 employees)
   - Budget range (e.g., $500-5000/month)
   - Target industries (e.g., SaaS, E-commerce, Agencies)
   - Decision maker job titles (e.g., VP, Director, C-suite)
3. Set scoring thresholds:
   - 80-100 = Hot (immediate sales contact)
   - 50-79 = Warm (nurture sequence)
   - 0-49 = Cold (archive)
4. Configure routing rules:
   - Hot → Slack alert + CRM assignment to sales rep
   - Warm → Add to nurture sequence
   - Cold → Archive with reason
5. Optional: Connect LinkedIn for profile enrichment
6. Test with 5 sample leads
7. Activate dashboard + automation

#### Value Proposition

- **Time savings:** 5 hours/week saved on manual lead research
- **Sales efficiency:** Focus only on qualified prospects (30%+ close rate improvement)
- **Revenue impact:** Faster response to hot leads (within 5 minutes vs 2 hours)
- **Data enrichment:** Automatic LinkedIn profile scraping adds context
- **Pipeline intelligence:** See which sources produce best leads

#### Pricing

- **Premium Tier:** $100-150/month (includes full dashboard + enrichment APIs)
- **No Utility tier** (scoring intelligence + dashboard = core value)

#### Technical Details

- **Trigger:** CRM webhook (new lead created) + daily batch scoring (existing leads)
- **Enrichment:** LinkedIn Sales Navigator API + Clearbit API + Hunter.io (email validation)
- **AI:** GPT-4 for qualification scoring:
  - Analyzes company size, industry, job title, email content, website, intent signals
  - Outputs 0-100 score + reasoning breakdown
- **Scoring:** Configurable weighted criteria (company size 25%, budget signals 20%, etc.)
- **Routing:** CRM API (update lead stage, assign owner, add tags)
- **Alerts:** Slack/email for hot leads (score 80+) within 2 minutes
- **Dashboard:** React + Recharts (pipeline funnel, scoring trends, conversion metrics)
- **Tracking:** Postgres (lead history, scoring data, conversion tracking)
- **Frequency:** Real-time (processes within 2 minutes of lead creation)

#### Competitive Positioning

vs **Clearbit** ($200+/month), **MadKudu** ($300+/month), **Zapier + Make** (10+ hours to build)

**Our Differentiation:**
- AI scoring (vs rule-based filters)
- Transparent scoring breakdown (see why each lead scored X/100)
- Full dashboard (vs API-only tools like Clearbit)
- $100-150 = 50% less than Clearbit BUT includes dashboard + AI intelligence

**Key Message:**
"You don't need an enterprise lead scoring platform. You need AI that tells you which leads to call first + shows you why."

---

## 📊 Agent Comparison Matrix

| Agent | Tier | Price | Build Time | Setup Time | Interface | Value Metric |
|-------|------|-------|------------|------------|-----------|--------------|
| Email Sweeper | Utility | $29-39 | 1-2 weeks | 15-20 min | Status Page | 83% time saved |
| Newsletter Digester | Utility | $49-59 | 1-2 weeks | 15-20 min | Status Page | 87% reading time saved |
| Expense Manager | Utility | $69-79 | 2-3 weeks | 20-25 min | Status Page | 100% automation |
| Invoice Chaser | Premium | $100 | 3-4 weeks | 30-40 min | Full Dashboard | 37% DSO improvement |
| Lead Qualification | Premium | $100-150 | 3-4 weeks | 35-45 min | Full Dashboard | 30% conversion lift |

---

## 🎯 Customer Journey by Tier

### Entry Point 1: Utility Tier (Productivity Optimizer)

**Profile:** [TBD - Customer segmentation under development]

**Entry Agent:** Email Sweeper ($29-39)
- Lowest price point, immediate value, 15-min setup
- **Upsell path:** Newsletter Digester → Expense Manager

**Average LTV:** $78/month (Email + Newsletter) × 18 months = $1,404

---

### Entry Point 2: Premium Tier (Cash Flow Manager)

**Profile:** [TBD - Customer segmentation under development]

**Entry Agent:** Invoice Chaser ($100)
- Business-critical pain, measurable ROI, dashboard value
- **Upsell path:** Lead Qualification (if they have sales process)

**Average LTV:** $100/month × 24 months = $2,400

---

### Entry Point 3: Premium Tier (Sales Efficiency Hunter)

**Profile:** [TBD - Customer segmentation under development]

**Entry Agent:** Lead Qualification ($100-150)
- Sales-driven businesses, high-value time savings
- **Upsell path:** Invoice Chaser (close loop: qualify → win → get paid)

**Average LTV:** $125/month × 24 months = $3,000

---

## 🚀 Build Roadmap

### Phase 1A: Utility Tier Validation (Weeks 1-4)

**Build:** Expense Manager + Newsletter Digester
- Focus: Prove "invisible automation" concept
- Goal: 30-50 customers, validate $49-79 pricing
- Status page UX testing

### Phase 1B: Utility Tier Completion (Week 5)

**Build:** Email Sweeper
- Focus: Complete Utility tier portfolio
- Goal: Test multi-agent adoption (2-3 agents per customer)

### Phase 2: Premium Tier Launch (Weeks 6-10)

**Build:** Invoice Chaser + Lead Qualification (with full dashboards)
- Focus: Prove "business intelligence" value prop
- Goal: 50+ Premium tier customers, validate $100-150 pricing
- Dashboard analytics feedback

**Total Timeline:** 10 weeks to full 5-agent MVP

---

## 💡 Future Agent Ideas (Post-MVP)

**Utility Tier Candidates:**
- Meeting Notes & Action Items (Zoom/Meet → Slack summary)
- Social Media Content Repurposer (LinkedIn → Twitter thread)
- Document Organizer & Renamer (Email attachments → Dropbox)

**Premium Tier Candidates:**
- Competitive Intelligence Monitor (Track competitor pricing, features, content)
- Customer Churn Predictor (Analyze usage patterns, predict cancellations)
- Sales Pipeline Forecaster (Predict close rates, revenue projections)

**See 04-decisions/MVP-AGENTS-FINAL.md for complete agent prioritization rationale.**

---

## 📞 Quick Reference

| Question | Answer |
|----------|--------|
| How many agents at launch? | 5 (3 Utility + 2 Premium) |
| Cheapest agent? | Email Sweeper ($29-39/mo) |
| Most expensive agent? | Lead Qualification ($100-150/mo) |
| Fastest setup? | Email Sweeper (15 min) |
| Longest setup? | Lead Qualification (35-45 min) |
| Dashboard agents? | Invoice Chaser + Lead Qualification (Premium tier) |
| Status page agents? | Email Sweeper + Newsletter + Expense (Utility tier) |
| Which agent first? | Depends on customer segment (TBD) |

---

**All agents designed for businesses without AI or high-end dev talent. Activate in minutes, see value immediately.**
