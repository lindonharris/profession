# BUILD-PLAN.md - buyanagent.ai Implementation Roadmap

**Last Updated:** October 8, 2025 (v1.2 - All 7 Pages Complete)
**Purpose:** Single source of truth for what to build, how to build it, and current status
**Status:** Active - Updated with each milestone

---

## 🎯 Current Status (v1.2)

### **Product Overview**
**buyanagent.ai** - Two-tier self-service AI agent marketplace
**Tagline:** "Zapier is for building automation. buyanagent.ai is for buying it pre-built."

### **Business Model**
- **Utility Tier:** $29-79/month (invisible automation + status pages)
- **Premium Tier:** $100-150/month (business intelligence + full dashboards)
- **Target Market:** 20M+ small businesses
- **Revenue Target:** $420K ARR Year 1

### **Build Progress**
```
Phase 1 (MVP - Utility):   ███████░░░ 71% (7/7 pages ✅, 0/3 agents)
Phase 2 (Premium):         ░░░░░░░░░░  0% (0/2 agents - pages done ✅)
Phase 3 (Scale):           ░░░░░░░░░░  0% (not started)

Overall:                   ████████░░ 50%
```

**Completed:**
- ✅ Strategic planning (v1.0)
- ✅ Domain purchased (buyanagent.ai, expires Oct 6, 2027)
- ✅ Repository (lindonharris/agentium-genesis on GitHub)
- ✅ Homepage live (preview--agentium-genesis.lovable.app)
- ✅ Design system (shadcn/ui + Lucide React + Tailwind)
- ✅ All 7 Lovable prompts ready
- ✅ **ALL 7 PAGES BUILT** (Homepage, Agent Detail, Dashboard, Activation Wizard, Agent Status, Premium Analytics, Settings/Billing)
  - Build 1: Homepage ✅
  - Build 2: Agent Detail Page ✅
  - Build 3: Dashboard (My Agents) ✅
  - Build 4: Activation Wizard (5 steps) ✅
  - Build 5: Agent Status Page (Utility tier) ✅
  - Build 6: Premium Analytics Dashboard ✅
  - Build 7: Settings & Billing ✅

**Next Up (v1.2 → v1.3): AGENT-FIRST STRATEGY** ⭐
**Priority:** Prove we can build valuable agents BEFORE worrying about infrastructure

**Phase A - Build First Agent (THIS WEEK):**
- 🚧 Set up n8n Cloud account (free trial)
- 🚧 Build Email Classifier agent workflow
  - **📘 Build Guide:** `EMAIL_CLASSIFIER_BUILD_GUIDE.md` (in agentium-genesis repo)
  - **Workflow Template:** Option A (keyword-based, 4 nodes, 4-6 hours)
  - **Reference:** n8n-sandbox email workflows + proven patterns
- 🚧 Test with personal Gmail account
- 🚧 Validate agent actually works and provides value

**Phase B - Deploy & Test (WEEK 2):**
- 🚧 Deploy current pages to Vercel (buyanagent.ai domain)
- 🚧 Get feedback from 3-5 beta testers
- 🚧 Iterate on agent based on feedback

**Phase C - Infrastructure (WEEK 3 - only after agent proven):**
- ✅ Supabase schema ready (6 tables, RLS policies, 7 agents seeded)
- 🚧 Run Supabase migrations (when needed for real users)
- 🚧 Stripe integration (when ready to charge)
- 🚧 Connect activation flow (Stripe → Supabase → n8n)

**Deferred (not blocking MVP):**
- ⏸️ Install Supabase client (wait until Phase C)
- ⏸️ Connect frontend to database (wait until Phase C)
- ⏸️ OAuth flows (wait until Phase C)
- ⏸️ Agents 2-3 (wait until agent #1 validated)

**Timeline:** 3-4 weeks to MVP launch

---

## 📊 Version-Aligned Build Phases

### **Phase 1: MVP Launch - Utility Tier (v1.1 → v1.5)**
**Timeline:** Weeks 1-5
**Goal:** Validate marketplace with $29-79 entry point
**Revenue Target:** $4,950/month (150 customers)

**What to Build:**
- **5 Marketplace Pages:** Homepage ✅, Agent Detail ✅, Dashboard ✅, Wizard ✅, Status ✅
- **3 Utility Agents:** Email Sweeper ($29-39), Newsletter Digester ($49-59), Expense Manager ($69-79)
- **Infrastructure:** Supabase DB, Stripe checkout, OAuth flows

**Success Metrics:**
- ✅ First paying customer
- ✅ 30+ Email Sweeper customers (entry point validation)
- ✅ 30% activate 2+ agents (cross-sell working)
- ✅ <10% churn

**Version Milestones:**
- **v1.1:** Homepage live ✅
- **v1.2:** All 7 marketplace pages built ✅ **← NOW**
- **v1.3:** Infrastructure (Supabase + Stripe + OAuth) + First agent live (Email Sweeper)
- **v1.4:** Utility tier complete (3 agents)
- **v1.5:** Utility validated (30+ customers, metrics green)

---

### **Phase 2: Premium Tier Launch (v1.5 → v2.0)**
**Timeline:** Weeks 6-10
**Goal:** Prove dashboard value justifies $100-150 pricing
**Revenue Target:** $15K+ MRR

**What to Build:**
- **2 Pages:** Premium Dashboard (analytics/charts) ✅, Settings/Billing ✅
- **2 Premium Agents:** Invoice Chaser ($100), Lead Qualification ($100-150)
- **Dashboards:** recharts components ✅, analytics pipelines

**Success Metrics:**
- ✅ First Premium customer
- ✅ 50+ Premium customers
- ✅ Dashboard engagement > status pages
- ✅ <5% churn
- ✅ Organic referrals

**Version Milestones:**
- **v1.6:** Premium dashboard pages
- **v1.7:** Invoice Chaser live
- **v1.8:** Premium tier complete (2 agents)
- **v1.9:** Premium validated (50+ customers)
- **v2.0:** Full marketplace operational 🎉

---

### **Phase 3: Scale & Expand (v2.0+)**
**Timeline:** Weeks 11-24
**Goal:** Reach $35K MRR, 12-15 agents
**Revenue Target:** $420K ARR (250+ customers)

**What to Build:**
- **7-10 More Agents** (based on demand)
- **Marketing:** SEO, content, email automation, retargeting
- **Features:** Bundles, referrals, API access

**Success Metrics:**
- ✅ 250+ customers (150 Utility + 100 Premium)
- ✅ $35K+ MRR
- ✅ <5% churn
- ✅ 40%+ multi-agent customers
- ✅ Product-market fit

---

## 🛠️ How to Build It

### **TRACK 1: Marketplace (How Customers Buy)**
**Tools:** Lovable + Supabase + Stripe
**Timeline:** 4 weeks

#### **Step 1: Build UI Pages (Lovable)**

**Build 1: Homepage ✅ DONE**
- Already live with hero, agent grid, pricing, footer
- Dark indigo design system implemented

**Build 2: Agent Detail Page ✅ DONE**
- Lucide icon + name + description
- "How It Works" 3-step visual
- Integration list with logos
- Pricing (Utility: single price, Premium: tier selector)
- CTA: "Activate Agent" / "Choose Your Tier"
- Reviews + FAQ accordion

**Build 3: Customer Dashboard (My Agents) ✅ DONE**
- Sidebar: My Agents, Billing, Settings
- Agent cards: icon, tier, price, status, last run, metrics
- Actions per card: Settings, Upgrade (Utility only), Pause, Cancel
- CTA: "Browse More Agents"

**Build 4: Activation Wizard ✅ DONE**
- 5-step wizard with progress indicator
- Step 1: Connect integrations (Gmail, Sheets via OAuth)
- Step 2: Configure rules (dynamic form with validation)
- Step 3: Test agent (loading → success/error states)
- Step 4: Subscribe (tier selection, Stripe checkout simulation)
- Step 5: Success screen (navigation to dashboard)

**Build 5: Agent Status Page (Utility Tier) ✅ DONE**
- Simple status dashboard per agent
- Last run time, activity count, health status
- Control panel: Pause/Resume, Settings, History, Integrations
- Agent-specific controls (whitelists, filters, rules)
- **Upgrade prompt for Utility users** (blurred preview + CTA)

**Build 6: Premium Analytics Dashboard ✅ DONE**
- Full analytics with recharts library
- 4 KPI cards with trend indicators (green/red based on isImprovement)
- Line chart (DSO trend) + Bar chart (invoice status)
- AI Insights card (5 insights sorted by priority)
- Timeline visualization (6 reminder nodes with connecting line)
- Extended activity table (6 columns with color-coded days outstanding)
- Export dropdown, date range selector, advanced controls

**Build 7: Settings/Billing ✅ DONE**
- 4-tab interface (Profile, Billing, Notifications, Security)
- Profile: Personal info + preferences (language, date format, email digest)
- Billing: Active subscriptions table + payment method + invoice history
- Notifications: 5 toggle switches with descriptions
- Security: Password, 2FA, active sessions, danger zone (delete account)

**How to Use Lovable:**
1. Copy prompt from `lovable-prompts/` folder
2. Paste into Lovable.dev chat
3. Review generated code
4. Export to GitHub repo
5. Deploy via Vercel

---

#### **Step 2: Database Setup (Supabase)**

**Create Account:** supabase.com
**Create Project:** "buyanagent-marketplace"

**Tables to Create:**
1. `users` - Customer accounts (Supabase Auth)
2. `agent_templates` - 22 agents catalog with pricing
3. `user_agents` - Which agents each customer activated
4. `oauth_integrations` - Connected services (Gmail, Sheets, etc.)
5. `subscriptions` - Stripe subscription tracking
6. `agent_activity_logs` - For dashboard analytics

**SQL Schema:** See `01-strategy/vision.md` for complete schema
**Row Level Security:** Enable RLS policies for data isolation
**Time:** 2-3 hours

---

#### **Step 3: Payments (Stripe)**

**Create Account:** stripe.com
**Create Product:** "AI Agent Subscription"

**Pricing Strategy:**
- Use dynamic pricing (not fixed price IDs)
- Store agent-specific pricing in `agent_templates` table
- Utility agents: $29-79/month
- Premium agents: $100-150/month

**Checkout Flow:**
1. User clicks "Activate Agent" or "Choose Tier"
2. Stripe Checkout modal opens
3. User enters card → Stripe creates subscription
4. Stripe webhook → Activate agent in backend
5. Redirect to Activation Wizard

**Webhooks to Handle:**
- `customer.subscription.created` → Activate agent, update DB
- `customer.subscription.deleted` → Cancel agent, delete n8n workflow
- `invoice.payment_failed` → Pause agent, notify user

**Testing:** Use Stripe test cards before going live
**Time:** 1-2 days

---

#### **Step 4: Activation Wizard (OAuth + Config)**

**OAuth Integration (Supabase Auth):**
- Connect Gmail, Google Sheets, other services
- Store tokens in `oauth_integrations` table
- Refresh tokens automatically

**Configuration Form:**
- Agent-specific settings (categories, rules, filters)
- Store in `user_agents.config` (JSONB column)

**Test Agent:**
- Clone n8n template
- Inject user's OAuth tokens + config
- Run test execution
- Show results to user

**Activate:**
- Save n8n workflow permanently
- Mark `user_agents.status = 'active'`
- Redirect to dashboard

**Time:** 4-5 days

---

#### **Step 5: Agent Deployment (n8n Backend)**

**Create Account:** n8n.io (n8n Cloud, $50/month)

**How It Works:**
1. Build agent workflow once in n8n visual editor (template)
2. When user activates → backend clones template
3. Backend injects user's OAuth tokens + config
4. Backend saves & activates workflow
5. Workflow runs automatically

**API Operations Needed:**
- Clone template workflow
- Create credentials (inject OAuth tokens)
- Update workflow parameters (user config)
- Save & activate workflow
- Store `workflow_id` in database

**Time:** 3-4 days per agent initially (faster with reuse)

---

### **TRACK 2: Agents (What Customers Buy)**
**Tools:** n8n Cloud + GPT-4
**Timeline:** 10 weeks (phased)

#### **Phased Rollout:**

**Weeks 1-4: Utility Tier Validation**

**Email Sweeper ($29-39) - Week 5**
- Gmail trigger → Detect promotional/newsletter emails
- Unsubscribe + Archive + Delete automation
- Status page: emails processed, archived, deleted
- **Build:** 1 week (simplest agent)

**Newsletter Digester ($49-59) - Week 2-3**
- Daily cron → Scan Gmail for newsletters
- GPT-4 summarize all newsletters
- Send daily digest email
- Status page: newsletters tracked, summaries sent
- **Build:** 1-2 weeks

**Expense Manager ($69-79) - Week 1-2**
- Gmail trigger → Watch for receipts/invoices
- GPT-4 extract vendor, amount, date, category
- Auto-categorize → Append to Google Sheets
- Status page: receipts scanned, expenses logged
- **Build:** 1-2 weeks

**Weeks 6-10: Premium Tier Launch**

**Invoice Chaser ($100) - Week 6-8**
- Sync unpaid invoices from QuickBooks/Stripe
- Escalating reminder sequences (Day 15/30/45)
- GPT-4 personalized emails
- **Full dashboard:** DSO trends, payment velocity, client behavior charts
- **Build:** 3-4 weeks (dashboard adds 2 weeks)

**Lead Qualification ($100-150) - Week 8-10**
- Capture leads from forms/integrations
- GPT-4 scoring based on criteria
- Enrichment (email verification, company lookup)
- Auto-routing to sales CRM
- **Full dashboard:** Pipeline metrics, scoring breakdown, conversion funnel
- **Build:** 3-4 weeks (dashboard adds 2 weeks)

**For Each Agent:**
1. Build workflow in n8n visual editor
2. Test with your own accounts
3. Document config options
4. Build status page (Utility) or dashboard (Premium)
5. Save as template
6. Add to `agent_templates` table
7. Create marketplace detail page

**Agent Specs:** See `01-strategy/agent-catalog.md` for complete details

---

### **TRACK 3: Launch & Market**
**Timeline:** Week 6 onwards
**Strategy:** Agentic inbound flywheel (we use AI agents to market AI agents)

#### **Marketing Ethos**

**Core Philosophy:**
- **Eat Your Own Dog Food** - Marketing automation built with our own agents (n8n workflows)
- **Anti-Bloat Positioning** - Stand against bloated SaaS, advocate standalone agents
- **Founder Transparency** - Build in public, share wins AND failures for trust
- **Zero Corporate Speak** - Direct, anti-fluff, tactical content (3-5 sentences max)
- **Practical AI** - No hype, show real metrics and ROI

**Shadow Persona Strategy:**
- Anonymous brand spokesperson (e.g., "Alex Automate" - Chief Automation Officer)
- Voice: Technical practitioner who escaped the grind
- Format: Threads, before/afters, micro-case studies
- Authenticity: Share both successes and flops

**5 Content Pillars:**
1. **Automation Wins** (30%) - Customer transformations with real metrics (DSO 45→28 days, 4 hrs→30 min saved)
2. **Anti-Bloat Philosophy** (20%) - "You don't need 90% of SaaS features. You need the 10% that works."
3. **Founder Transparency** (20%) - Revenue milestones, what's working/not working, agent build logs
4. **AI Practicality** (15%) - What AI can actually do for you today (no hype)
5. **Small Business Empowerment** (15%) - Right tools vs enterprise bloat

---

#### **Soft Launch (Week 1)**
- Send to 10 friends for feedback
- Watch user sessions (Zoom screen share)
- Fix critical bugs, collect UX feedback
- Document first customer journey for content

#### **Public Launch (Week 2)**
- **LinkedIn/Twitter:** Customer transformation threads with dashboard screenshots
- **Reddit:** r/entrepreneur, r/solopreneur (soft pitch: "Built this to escape the grind")
- **Product Hunt:** Launch with founder story + first customer win
- **Google Ads ($500):** "zapier alternative", "buy ai automation" (test only)

#### **Content Flywheel (Months 2-3)**
- **Blog Posts:** "Zapier vs buyanagent.ai", "How I Cut DSO by 37% with AI", "3 Agents Launched, 1 Flopped"
- **Social Threads:** Before/after case studies, anti-bloat hot takes, building in public updates
- **Engagement:** Reply to SaaS complaints, share customer wins, quote-tweet automation pain points
- **SEO:** "pre-built ai agents", "standalone agents vs zapier", "automate [X] without platform bloat"

#### **Agentic Marketing Automation (Months 3-4)**
**Build n8n Agent for Content Generation:**
- GPT-4 generates posts based on 5 pillars + performance data
- Platform optimization (LinkedIn long-form vs Twitter hot takes)
- Auto-posting at optimal times
- Engagement monitoring + weekly performance reports
- Strategy iteration based on what's working

**Email Sequences:**
- Abandoned activation: "Need help getting started?"
- Cross-sell: "Customers using Expense Manager also love Newsletter Digester"
- Founder updates: Monthly transparency report with revenue milestones

**Retargeting (Optional):**
- Facebook/Google Display: Show customer testimonials to visitors

#### **Agent Expansion & Viral Loop (Months 4-6)**
- Build 3-5 agents/month based on demand + social feedback
- Launch as "Beta" with founder story
- Share build logs publicly (thread breakdowns, n8n workflows)
- Customer win spotlight series (before/after transformations)
- Goal: 20 agents by Month 6, self-sustaining inbound flywheel

**Success = Content Marketing Runs Itself (Built with Our Own Agents)**

---

## 🤝 Division of Labor

**Lovable (AI Code Generator):**
- Generate all 7 marketplace pages from prompts
- Implement shadcn/ui components
- Responsive layouts
- Accessibility patterns

**Claude (Technical Assistant):**
- Fix generated code issues
- Database schema (Supabase SQL)
- Stripe webhooks
- n8n deployment logic
- OAuth flows

**You (Product Owner):**
- Strategic decisions
- Copy prompts to Lovable
- Test features
- Customer feedback

---

## 📈 Success Milestones

**Week 4: Marketplace Foundation**
- ✅ All 7 pages live
- ✅ Stripe checkout works (all price points tested)
- ✅ Activation wizard works
- ✅ Database deployed

**Week 5: Utility Validation**
- ✅ 2 Utility agents live (Expense + Newsletter)
- ✅ 30-50 Utility customers
- ✅ Pricing validated, UX feedback collected

**Week 6: Utility Complete**
- ✅ Email Sweeper live ($29 entry point)
- ✅ 50+ total customers
- ✅ 30%+ activate 2+ agents

**Week 10: Premium Launch**
- ✅ Invoice + Lead agents live with dashboards
- ✅ 50+ Premium customers
- ✅ $100-150 validated, dashboards justify premium

**Month 6: Product-Market Fit**
- ✅ 250+ customers (150 Utility + 100 Premium)
- ✅ $35K+ MRR ($420K ARR)
- ✅ <5% churn
- ✅ Organic referrals

---

## 🏗️ Tech Stack

| Component | Tool | Cost | Purpose |
|-----------|------|------|---------|
| UI Generator | Lovable | $20/mo | AI React code |
| Frontend | Vercel | $20/mo | Hosting |
| Database | Supabase | $25/mo | Postgres + Auth |
| Payments | Stripe | 2.9% + $0.30 | Subscriptions |
| Agents | n8n Cloud | $50/mo | Workflows |
| AI | OpenAI GPT-4 | ~$100/mo | Agent logic |
| Email | Resend | $20/mo | Transactional |
| Domain | Namecheap | $12/yr | buyanagent.ai |

**Total Fixed:** $255/month (scales to 100+ customers)

---

## 📚 Reference Docs

**Strategy:**
- [start.md](start.md) - Executive summary
- [01-strategy/vision.md](01-strategy/vision.md) - Full architecture (DB schema, API flows)
- [01-strategy/agent-catalog.md](01-strategy/agent-catalog.md) - All 22 agent specs
- [01-strategy/competitive-analysis.md](01-strategy/competitive-analysis.md) - vs Zapier/Make/n8n
- [01-strategy/brand-design-system.md](01-strategy/brand-design-system.md) - Dark indigo design
- [01-strategy/marketplace-ux.md](01-strategy/marketplace-ux.md) - UI/UX details

**Implementation:**
- [lovable-prompts/](lovable-prompts/) - All 7 page prompts (copy-paste ready)
- [02-build/agent-technical-components.md](02-build/agent-technical-components.md) - Reusable n8n modules
- [agent-workshops/n8n/](agent-workshops/n8n/) - n8n development guide

**Decisions:**
- [CHANGELOG.md](CHANGELOG.md) - Version history (what was built)
- [04-decisions/MVP-AGENTS-FINAL.md](04-decisions/MVP-AGENTS-FINAL.md) - Agent selection
- [04-decisions/PRICING-DECISION-FINAL.md](04-decisions/PRICING-DECISION-FINAL.md) - Pricing rationale

---

## ⚠️ Avoid These Pitfalls

1. **Building too many agents before customers** → Launch with 5, build based on demand
2. **Over-engineering wizard** → Basic first, improve from feedback
3. **Ignoring mobile** → Test iPhone/Android from Day 1
4. **No analytics** → Set up tracking before launch
5. **Trying to be Zapier** → Stay focused on pre-built only

---

## 🧪 Testing Checklist

Track all tests that need to be run before launch. Check off as you complete them.

### **Phase 1: Marketplace Pages (v1.1 → v1.5)**

**Homepage (✅ DONE)**
- [x] Loads at root URL
- [x] Hero section displays correctly
- [x] Agent grid shows all agents
- [x] Pricing section visible
- [x] Footer links work
- [x] Theme toggle works
- [x] Mobile responsive (375px, 768px, 1440px)
- [x] All Lucide icons render (no emoji)
- [x] Agent cards link to detail pages

**Agent Detail Page**
- [ ] Loads at /agents/{agent-id}
- [ ] Breadcrumb navigation works
- [ ] Hero section shows agent info
- [ ] "How It Works" 3-step visual displays
- [ ] Integrations grid shows required services
- [ ] Pricing comparison (Premium agents only)
- [ ] FAQ accordion expands/collapses
- [ ] Reviews section displays
- [ ] "Request Access" button works
- [ ] "Watch Demo" button works
- [ ] Invalid agent ID redirects to 404
- [ ] Mobile responsive
- [ ] Theme toggle works

**Customer Dashboard**
- [ ] Loads at /dashboard
- [ ] Sidebar navigation displays
- [ ] Sidebar highlights active section
- [ ] Sidebar collapses on mobile (hamburger)
- [ ] User avatar dropdown functions
- [ ] Agent cards display all info
- [ ] Card click navigates to status page
- [ ] Button clicks DON'T trigger card navigation (stopPropagation tested)
- [ ] "Upgrade to Premium" only shows for Utility agents
- [ ] "Dashboard" only shows for Premium agents
- [ ] Empty state displays when no agents
- [ ] "+ Browse More Agents" button works
- [ ] Mobile responsive (buttons wrap correctly)
- [ ] Theme toggle works

**Activation Wizard**
- [ ] Loads at /activate/{agent-slug}
- [ ] Progress indicator shows 5 steps
- [ ] Step 1: Integration cards display
- [ ] Step 1: "Next" disabled until all connected
- [ ] Step 1: OAuth popups work
- [ ] Step 2: Form fields work (checkboxes, dropdowns, inputs)
- [ ] Step 2: Validation errors show in red
- [ ] Step 3: Loading spinner displays
- [ ] Step 3: Test results show correctly
- [ ] Step 3: Error state displays if test fails
- [ ] Step 4: Pricing cards display
- [ ] Step 4: Stripe checkout opens
- [ ] Step 5: Success screen displays
- [ ] "Back" button disabled on Step 1
- [ ] "Back" button works on Steps 2-5
- [ ] Step transitions smooth (fade in/out)
- [ ] Mobile responsive

**Agent Status Page (Utility)**
- [ ] Loads at /dashboard/agents/{id}/status
- [ ] "← Back to Dashboard" link works
- [ ] Status indicator shows correct color (green/yellow/red)
- [ ] Activity metrics display (2x2 grid)
- [ ] Control panel buttons work
- [ ] Agent-specific controls display
- [ ] Recent activity table shows last 10 actions
- [ ] "View All →" link works
- [ ] Metrics stack to 1 column on mobile
- [ ] Mobile responsive

**Premium Dashboard (Analytics)**
- [ ] Loads at /dashboard/agents/{id}/analytics
- [ ] Date range selector works
- [ ] 4 KPI cards display correctly
- [ ] Change indicators show (green/red arrows)
- [ ] Line chart renders (recharts)
- [ ] Bar chart renders (recharts)
- [ ] AI Insights card displays
- [ ] "Export Report" dropdown works (CSV/PDF/Excel)
- [ ] Control panel buttons work
- [ ] Advanced controls display
- [ ] Activity table shows enhanced columns
- [ ] Charts responsive on mobile
- [ ] Empty states if no data

**Settings/Billing Page**
- [ ] Loads at /dashboard/settings
- [ ] Tab navigation works (4 tabs)
- [ ] Profile tab: Avatar upload works
- [ ] Profile tab: Form inputs work
- [ ] Profile tab: Save button works
- [ ] Billing tab: Subscriptions table displays
- [ ] Billing tab: Total cost correct
- [ ] Billing tab: Payment method displays
- [ ] Billing tab: Update/Remove card buttons work
- [ ] Billing tab: Billing history table shows
- [ ] Billing tab: Download PDF links work
- [ ] Notifications tab: Toggle switches work
- [ ] Security tab: All sections display
- [ ] Security tab: Sessions table shows
- [ ] Security tab: Danger zone styled red
- [ ] Tables scroll horizontally on mobile if needed

---

### **Phase 2: Infrastructure (v1.1 → v1.5)**

**Supabase Database**
- [ ] Account created (supabase.com)
- [ ] Project "buyanagent-marketplace" created
- [ ] SQL schema executed successfully
- [ ] All 6 tables created (users, agent_templates, user_agents, oauth_integrations, subscriptions, agent_activity_logs)
- [ ] Row Level Security enabled
- [ ] RLS policies tested
- [ ] API keys obtained
- [ ] Connection from frontend tested

**Stripe Integration**
- [ ] Account created (stripe.com)
- [ ] Product "AI Agent Subscription" created
- [ ] Test API keys obtained
- [ ] Webhook endpoints configured
- [ ] Test checkout with $29 (Email Sweeper)
- [ ] Test checkout with $79 (Expense Manager)
- [ ] Test checkout with $100 (Invoice Chaser)
- [ ] Webhook: customer.subscription.created fires
- [ ] Webhook: customer.subscription.deleted fires
- [ ] Webhook: invoice.payment_failed fires
- [ ] Stripe test cards work (4242 4242 4242 4242)
- [ ] Failed payment handling tested

**End-to-End Flow**
- [ ] Browse agents on homepage
- [ ] Click agent → View detail page
- [ ] Click "Activate Agent" → Stripe checkout
- [ ] Enter test card → Payment succeeds
- [ ] Redirect to Activation Wizard
- [ ] Complete all 5 wizard steps
- [ ] Land on dashboard showing active agent
- [ ] Click agent card → View status page
- [ ] Agent appears in database
- [ ] Subscription appears in Stripe

---

### **Phase 3: Agent Development (v1.3 → v1.5)**

**n8n Setup**
- [ ] n8n Cloud account created ($50/month)
- [ ] First workflow template created
- [ ] API credentials obtained
- [ ] Clone template operation tested
- [ ] Credential injection tested
- [ ] Workflow activation tested

**Email Sweeper ($29-39) - Utility**
- [ ] Workflow built in n8n
- [ ] Gmail trigger configured
- [ ] Email detection logic works
- [ ] Unsubscribe automation tested
- [ ] Archive automation tested
- [ ] Delete automation tested
- [ ] Status page displays metrics
- [ ] Tested with your Gmail account
- [ ] Template saved for cloning
- [ ] Added to agent_templates table
- [ ] Detail page created

**Newsletter Digester ($49-59) - Utility**
- [ ] Workflow built in n8n
- [ ] Daily cron trigger configured
- [ ] Gmail scanning works
- [ ] GPT-4 summarization tested
- [ ] Digest email sends correctly
- [ ] Status page displays metrics
- [ ] Tested with your Gmail account
- [ ] Template saved
- [ ] Added to database
- [ ] Detail page created

**Expense Manager ($69-79) - Utility**
- [ ] Workflow built in n8n
- [ ] Gmail trigger configured
- [ ] Receipt detection works
- [ ] GPT-4 extraction tested (vendor, amount, date, category)
- [ ] Google Sheets append works
- [ ] Auto-categorization tested
- [ ] Status page displays metrics
- [ ] Tested with your accounts
- [ ] Template saved
- [ ] Added to database
- [ ] Detail page created

---

### **Phase 4: Premium Agents (v1.6 → v2.0)**

**Invoice Chaser ($100) - Premium**
- [ ] Workflow built in n8n
- [ ] QuickBooks/Stripe sync works
- [ ] Escalation sequence tested (Day 15/30/45)
- [ ] GPT-4 email personalization tested
- [ ] Premium dashboard displays DSO trends
- [ ] Payment velocity chart works
- [ ] Client behavior analytics work
- [ ] Tested with real invoices
- [ ] Template saved
- [ ] Added to database
- [ ] Detail page created

**Lead Qualification ($100-150) - Premium**
- [ ] Workflow built in n8n
- [ ] Lead capture tested
- [ ] GPT-4 scoring works
- [ ] Email verification tested
- [ ] Company lookup tested
- [ ] CRM routing works
- [ ] Premium dashboard displays pipeline
- [ ] Scoring breakdown chart works
- [ ] Conversion funnel works
- [ ] Tested with real leads
- [ ] Template saved
- [ ] Added to database
- [ ] Detail page created

---

### **Phase 5: Launch Readiness (v1.5 - Public Launch)**

**Pre-Launch Checks**
- [ ] All pages work on Chrome
- [ ] All pages work on Safari
- [ ] All pages work on Firefox
- [ ] All pages work on Mobile Safari (iPhone)
- [ ] All pages work on Mobile Chrome (Android)
- [ ] Domain buyanagent.ai points to Vercel
- [ ] SSL certificate valid
- [ ] All images optimized (<100KB)
- [ ] Page load times <2 seconds
- [ ] Lighthouse score >90
- [ ] No console errors
- [ ] No broken links

**Soft Launch (10 Friends)**
- [ ] 10 test accounts created
- [ ] Each friend activates 1+ agent
- [ ] Collect feedback via Zoom sessions
- [ ] Document all bugs found
- [ ] Fix critical bugs (P0)
- [ ] Fix high-priority bugs (P1)
- [ ] Collect UX improvement ideas

**Public Launch Preparation**
- [ ] Google Analytics installed
- [ ] PostHog installed (optional)
- [ ] Privacy policy page created
- [ ] Terms of service page created
- [ ] Support email set up (support@buyanagent.ai)
- [ ] Product Hunt post drafted
- [ ] LinkedIn post drafted
- [ ] Twitter post drafted
- [ ] Reddit posts drafted (r/entrepreneur, r/solopreneur)
- [ ] Google Ads campaign created ($500 budget)

**Launch Day**
- [ ] Product Hunt post published
- [ ] LinkedIn post published
- [ ] Twitter post published
- [ ] Reddit posts published
- [ ] Google Ads campaign activated
- [ ] Monitor for errors (check logs every hour)
- [ ] Respond to all comments/questions within 1 hour
- [ ] Track signups in real-time

---

### **Phase 6: Post-Launch (Week 2+)**

**Metrics Tracking**
- [ ] First paying customer ✅
- [ ] 30+ Email Sweeper customers
- [ ] 30% activate 2+ agents
- [ ] <10% churn rate (Utility)
- [ ] First Premium customer
- [ ] 50+ Premium customers
- [ ] <5% churn rate (Premium)
- [ ] $10K MRR milestone
- [ ] $35K MRR milestone

**Ongoing Tests**
- [ ] Weekly: Test all agent workflows still running
- [ ] Weekly: Test all payment flows
- [ ] Weekly: Check error logs in Supabase
- [ ] Weekly: Check Stripe for failed payments
- [ ] Monthly: Run full regression test suite
- [ ] Monthly: Test on new devices/browsers

---

## 📊 Progress Tracker

### **Marketplace Pages (7)**
- [x] Homepage ✅
- [ ] Agent Detail
- [ ] Customer Dashboard
- [ ] Activation Wizard
- [ ] Agent Status (Utility)
- [ ] Premium Dashboard
- [ ] Settings/Billing

**1/7 complete (14%)**

### **Agents (5 for MVP)**

**Utility (3):**
- [ ] Email Sweeper ($29-39)
- [ ] Newsletter Digester ($49-59)
- [ ] Expense Manager ($69-79)

**Premium (2):**
- [ ] Invoice Chaser ($100)
- [ ] Lead Qualification ($100-150)

**0/5 complete (0%)**

### **Infrastructure**
- [x] Strategy complete ✅
- [x] Domain purchased ✅
- [x] Repository created ✅
- [x] Design system ✅
- [ ] Supabase deployed
- [ ] Stripe integrated
- [ ] n8n account setup
- [ ] OAuth flows

**4/8 complete (50%)**

---

## 🚦 Next Actions (This Week)

**v1.1 → v1.2 (Marketplace Foundation):**

1. **Build Pages 2-4 with Lovable**
   - Agent Detail page (copy prompt from `lovable-prompts/02`)
   - Customer Dashboard (copy prompt from `lovable-prompts/03`)
   - Activation Wizard (copy prompt from `lovable-prompts/04`)

2. **Set Up Supabase**
   - Create project "buyanagent-marketplace"
   - Run SQL schema from `01-strategy/vision.md`
   - Enable Row Level Security

3. **Create Stripe Products**
   - Sign up for Stripe
   - Create "AI Agent Subscription" product
   - Set up webhook endpoints
   - Test with test cards

4. **Test End-to-End Flow**
   - Browse agents → Click activate → Checkout → Wizard → Success
   - Fix any bugs

**Time estimate:** 1 week
**Goal:** Marketplace foundation complete (all pages working, payment flow tested)

---

## 📞 Quick Reference

| Question | Answer |
|----------|--------|
| **What's the product?** | Two-tier AI agent marketplace |
| **Who's it for?** | All small businesses (20M+ TAM) |
| **How's it different?** | Pre-built (not DIY like Zapier) |
| **What's the pricing?** | $29-150/month per agent |
| **What do I build next?** | See "Next Actions" above |
| **Where are the prompts?** | lovable-prompts/ folder |
| **Where's the full architecture?** | 01-strategy/vision.md |
| **What's the version?** | v1.1 (First Build Complete) |

---

## 🎯 Summary

**Current:** v1.1 - Homepage live, 14% complete
**Next:** v1.2 - Marketplace foundation (pages 2-4, DB, Stripe)
**Timeline:** 3-4 weeks to MVP launch
**Repository:** https://github.com/lindonharris/agentium-genesis
**Live:** https://preview--agentium-genesis.lovable.app/

**Start with "Next Actions" and update this doc with each milestone.**
