# buyanagent.ai - Project Documentation

**Last Updated:** October 7, 2025 (v1.1 First Build Complete)
**Current Version:** v1.1 ([See CHANGELOG.md](./CHANGELOG.md))
**Project Status:** Homepage Live + 6 Prompts Updated ✅
**Business Model:** Two-tier AI agent marketplace (Utility + Premium)
**Domain:** buyanagent.ai (purchased, expires Oct 6, 2027)
**Repository:** [lindonharris/agentium-genesis](https://github.com/lindonharris/agentium-genesis)
**Target:** 20M+ small businesses (Utility tier) + 5-8M service businesses (Premium tier)

---

## 🚀 Quick Start

**New to this project? Read these docs in order:**

1. **[start.md](./start.md)** - What we're building and why (15 min read)
2. **[BUILD-PLAN.md](./BUILD-PLAN.md)** ⭐ - Implementation roadmap & current status (10 min read)
3. **[01-strategy/agent-catalog.md](./01-strategy/agent-catalog.md)** - 22 agents we'll build (10 min read)
4. **[01-strategy/competitive-analysis.md](./01-strategy/competitive-analysis.md)** - How we beat Zapier/Make/n8n (15 min read)
5. **[02-build/build-overview.md](./02-build/build-overview.md)** - Step-by-step build guide (20 min read)
6. **[01-strategy/vision.md](./01-strategy/vision.md)** - Technical architecture (25 min read)

**After that, you'll understand the complete marketplace strategy.**

---

## 📖 Folder Structure

### **BUILD-PLAN.md** ⭐ - Implementation Roadmap
Single source of truth for build status, roadmap, and execution plan
- Version-aligned phases (v1.1 → v2.0)
- Progress tracking (14% complete)
- Success metrics & milestones
- References all tactical docs

### **01-strategy/** - WHAT We're Building
Strategic vision, competitive positioning, and agent specifications
- `vision.md` - Technical architecture and system design
- `agent-catalog.md` - All 22 agents with full specifications
- `competitive-analysis.md` - Market positioning vs Zapier/Make/n8n
- `brand-design-system.md` - Complete dark indigo design system (underground marketplace aesthetic)
- `marketplace-ux.md` - UI/UX reference (points to `/lovable-prompts/`)

### **02-build/** - HOW to Build It
Practical implementation guides and technical components
- `build-overview.md` - 12-step plain-English build guide (tactical details)
- `agent-technical-components.md` - Reusable n8n modules

### **03-research/** - WHY These Decisions
Research validation that informed current strategy
- `README-RESEARCH.md` - Research evolution guide
- `phase2-validation/` - Q4-Q9 validation (pricing, agents, positioning)
- `competitive-intelligence/` - Competitor deep dives (Enso, HubDocs, Lindy)
- `archive/` - Phase 1 research (old boutique service model)

### **04-decisions/** - Decision Logs
Historical context for strategic choices
- `MVP-AGENTS-FINAL.md` - Why 5-agent tiered strategy was chosen
- `PRICING-DECISION-FINAL.md` - Why $29-150 tiered pricing
- `MVP-LAUNCH-STRATEGY.md` - Phased rollout rationale
- `RESEARCH-SUMMARY.md` - Phase 2 validation summary

### **05-operations/** - Execution Tools
Project management and research planning
- `research-directives.md` - Research planning templates
- `research-execution-prompts.md` - Research execution guides

---

## 📖 How to Use This Folder

### **Three Parallel Build Tracks:**

#### **TRACK 1: Build the MARKETPLACE** (Steps 1-8)
- **01-strategy/marketplace-ux.md** - Complete UI/UX specifications for Lovable
- **01-strategy/vision.md** - Database schema, Stripe integration, agent deployment
- **02-build/build-overview.md** - Step-by-step implementation guide
- **Outcome:** buyanagent.ai goes live, customers can browse and purchase

#### **TRACK 2: Build the AGENTS** (Step 9)
- **01-strategy/agent-catalog.md** - Specifications for all 22 agents
- **02-build/build-overview.md Step 9** - Build 5 launch agents in n8n
- **Outcome:** 5 internal automation agents ready to sell

#### **TRACK 3: Launch & Market** (Steps 10-12)
- **01-strategy/competitive-analysis.md** - SEO strategy and positioning
- **02-build/build-overview.md Steps 10-12** - Marketing automation and expansion
- **Outcome:** Customer acquisition and agent portfolio growth

---

## 📁 Quick Navigation

### **First-Time Readers:**
```
start.md → BUILD-PLAN.md → 01-strategy/ → 02-build/
```
**Time:** 95 minutes | **Outcome:** Full understanding of strategy and implementation roadmap

### **Ready to Build? START HERE:**
```
BUILD-PLAN.md → lovable-prompts/ → 02-build/build-overview.md
```
**Time:** 45 minutes | **Outcome:** Know exactly what to build next and how

### **Want Decision Context?**
```
CHANGELOG.md → 04-decisions/ → 03-research/README-RESEARCH.md
```
**Time:** 40 minutes | **Outcome:** Understand evolution and key decisions

### **Ready to Build the UI?**
```
BUILD-PLAN.md → 01-strategy/brand-design-system.md → lovable-prompts/00-README.md → lovable-prompts/01-07
```
**Time:** 25 minutes to understand | **Outcome:** Ready to copy-paste into Lovable with complete design system

### **Ready to Build the Backend?**
```
BUILD-PLAN.md → 01-strategy/marketplace-ux.md → 02-build/build-overview.md → 01-strategy/vision.md
```
**Time:** 80 minutes | **Outcome:** Understand full technical architecture

---

## 📊 Core Strategy Summary

| File | Purpose | Location |
|------|---------|----------|
| **BUILD-PLAN.md** ⭐ | Implementation roadmap, status, milestones | Root (single source of truth) |
| **start.md** | Executive summary, positioning vs Zapier | Root (for visibility) |
| **vision.md** | Technical architecture (DB, Stripe, n8n) | 01-strategy/ |
| **agent-catalog.md** | All 22 agents with specifications | 01-strategy/ |
| **competitive-analysis.md** | Market intelligence | 01-strategy/ |
| **brand-design-system.md** | Dark indigo design system (all colors, typography, shadows) | 01-strategy/ |
| **marketplace-ux.md** | UI/UX specs for Lovable | 01-strategy/ |
| **build-overview.md** | 12-step tactical build guide | 02-build/ |

---

## 🎯 Key Decisions (Aligned Across All Docs)

### **Strategic Positioning**
- **Tagline:** "Zapier is for building automation. buyanagent.ai is for buying it pre-built."
- **Value Prop:** Activate in 1 click vs 10 hours building in Zapier
- **Competitive Edge:** Pre-built agents (not DIY), 30-min setup (not 10 hours), zero learning curve

### **Target Customer**
- **Primary:** All productivity-focused small businesses (freelancers, agencies, startups)
- **Why Changed:** Marketplace scales better than niche (agencies only)
- **Activation Pattern:** Solo freelancers (1-2 agents), Agencies (3-5 agents), SaaS companies (5-10 agents)

### **Business Model**
- **What:** Self-service marketplace (buyanagent.ai) selling pre-built AI agents
- **How:** Browse agents → 1-click purchase → Setup wizard → Agent activates
- **Tech:** Lovable (UI) + Supabase (DB) + Stripe (payments) + n8n Cloud (agents) + Vercel (hosting)

### **Pricing**
**Two-Tier Model:** (Value-Based, Not Cost-Based)

**Utility Tier:** $29-79/month per agent
- Email Sweeper ($29-39), Newsletter Digester ($49-59), Expense Manager ($69-79)
- **Interface:** Simple status pages (health + activity metrics)
- **Value Prop:** "Set it and forget it" invisible automation
- **vs Competitors:** 2-4x Clean Email/SaneBox/Unroll.me/Expensify BUT AI-powered

**Premium Tier:** $100-150/month per agent
- Invoice Chaser ($100), Lead Qualification ($100-150)
- **Interface:** Full analytics dashboards (charts, trends, insights)
- **Value Prop:** Business intelligence + measurable ROI
- **vs Competitors:** 50% less than Bonsai/Clearbit BUT includes dashboard + no bloat

**No Bundling Initially:** Validate individual agent pricing first (revisit post-MVP)

### **Launch Product Lineup** (5 Agents - Two Tiers)

**Utility Tier** (Invisible Automation - $29-79/month):
1. **Email Sweeper** ($29-39) - Unsubscribe + delete + archive email noise
2. **Newsletter Digester** ($49-59) - AI summarizes newsletters daily
3. **Expense Manager** ($69-79) - Scans receipts, auto-categorizes to Google Sheets

**Premium Tier** (Dashboard + Intelligence - $100-150/month):
4. **Invoice Chaser** ($100) - Payment reminders + DSO analytics dashboard
5. **Lead Qualification** ($100-150) - AI scoring + pipeline dashboard

**Phased Rollout:** Utility tier first (Weeks 1-5), Premium tier second (Weeks 6-10)

### **Domain**
- **Primary:** buyanagent.ai (available)
- **Why:** Perfect CTA ("Buy an Agent"), .ai domain credibility, marketplace positioning

---

## 🚫 What NOT to Confuse

### **Strategic Pivot - OLD vs NEW:**

**OLD Strategy (Archived):**
- ❌ Boutique service model with sales calls
- ❌ Customer-facing agents (Invoice & Collections for agency clients)
- ❌ Pricing: $12K setup + $2K/month
- ❌ Target: Marketing/creative agencies only
- ❌ 7 complex agents requiring extensive onboarding

**NEW Strategy (Current):**
- ✅ Self-service marketplace (100% self-serve)
- ✅ Internal agents (Expense Tracker for the business owner themselves)
- ✅ Pricing: $100/month per agent (no setup fee)
- ✅ Target: All productivity-focused small businesses
- ✅ 22 simple agents with 30-min activation

### **Common Misunderstandings:**

**❌ WRONG:** "This is like Zapier (build your own)"
**✅ RIGHT:** "This is the OPPOSITE of Zapier - buy it pre-built, activate in 1 click"

**❌ WRONG:** "We're targeting agencies because of Google Trends research"
**✅ RIGHT:** "We're targeting ALL small businesses now - agencies are just one customer segment"

**❌ WRONG:** "Agents interact with customer's customers (like AR automation)"
**✅ RIGHT:** "Agents are internal tools (like expense tracking, meeting notes) - no customer-facing"

**❌ WRONG:** "This is a high-touch consulting model"
**✅ RIGHT:** "This is a no-touch product model (like buying a Shopify app)"

---

## 📊 Document Alignment Check

| Topic | start.md | agent-catalog.md | competitive-analysis.md | build-overview.md | vision.md |
|-------|----------|------------------|------------------------|-------------------|-----------|
| **Positioning** | vs Zapier | Pre-built agents | Beat Zapier on time | Marketplace | Self-service |
| **Target** | All SMBs | All SMBs | All SMBs | All SMBs | All SMBs |
| **Pricing** | $100/mo | $100/mo | $100/mo | $100/mo | $100/mo |
| **Model** | Marketplace | Marketplace | Marketplace | Marketplace | Marketplace |
| **Launch Agents** | 5 agents | 5 agents | Internal agents | 5 agents | 5 agents |
| **Tech Stack** | Lovable+Supabase | n8n Cloud | n8n vs Zapier | Lovable+n8n | Full architecture |

**Aligned:** ✅ All documents now consistent (October 5, 2025)
**Note:** All phase1 research (agencies-only focus, $12K pricing) has been archived to research-archive/

---

## 🔄 Reading Order (Recommended)

### **For First-Time Understanding (Start Here):**
```
start.md → 01-strategy/agent-catalog.md → 01-strategy/competitive-analysis.md
```
**Time:** 40 minutes | **Outcome:** Understand the complete marketplace strategy

### **For Building the Marketplace:**
```
01-strategy/marketplace-ux.md → 02-build/build-overview.md → 01-strategy/vision.md
```
**Time:** 70 minutes | **Outcome:** Understand exactly how to build buyanagent.ai

### **For Building Individual Agents:**
```
01-strategy/agent-catalog.md (find your agent) → 02-build/build-overview.md Step 9
```
**Time:** 20 minutes per agent | **Outcome:** Build agent in n8n with specifications

### **For Understanding Strategic Evolution:**
```
CHANGELOG.md → 03-research/archive/README-ARCHIVE.md → start.md
```
**Time:** 25 minutes | **Outcome:** Understand complete strategic evolution (v0.1 → v2.1)

### **For Decision Context:**
```
CHANGELOG.md → 04-decisions/ → 03-research/README-RESEARCH.md
```
**Time:** 40 minutes | **Outcome:** Understand strategic decisions and research validation

---

## ✅ Complete Strategic Alignment

All documents have been completely rewritten and aligned as of October 5, 2025:

- ✅ **Pricing:** $100/month per agent (consistent across all docs)
- ✅ **Target:** All productivity-focused small businesses (not agencies only)
- ✅ **Positioning:** Pre-built alternative to Zapier (not boutique service)
- ✅ **Model:** Self-service marketplace (not sales-led)
- ✅ **Agents:** 22 internal tools (not 7 customer-facing)
- ✅ **Tech Stack:** Lovable + Supabase + Stripe + n8n Cloud + Vercel
- ✅ **Old Research:** Archived to 03-research/archive/ with explanation
- ✅ **Folder Structure:** Reorganized for intuitive navigation (October 6, 2025)

---

## 🎯 Current Status

**What's Done:**
- ✅ Strategic pivot completed (boutique service → marketplace)
- ✅ All documentation rewritten and aligned (v1.0)
- ✅ 22 agents planned with full specifications
- ✅ Competitive analysis completed (Zapier/Make/n8n positioning)
- ✅ Technical architecture designed (Lovable + Supabase + Stripe + n8n)
- ✅ Complete dark indigo design system (underground marketplace aesthetic)
- ✅ 7 Lovable prompts aligned with codebase (ready to copy-paste)
- ✅ Complete navigation map (all pages linked)
- ✅ Folder structure reorganized into logical categories
- ✅ Version control established (CHANGELOG.md)
- ✅ Domain purchased (buyanagent.ai - expires Oct 6, 2027)
- ✅ **Homepage built and deployed** (Lovable v1, dark mode working)
- ✅ **Repository created** (lindonharris/agentium-genesis on GitHub)
- ✅ **Design system implemented** (shadcn/ui + Lucide React + Tailwind)
- ✅ **Code fixes applied** (agent count, noise texture, clickable cards)
- ✅ **Review methodology created** (7-step Playwright-based process)
- ✅ **All prompts updated** (Heroicons → Lucide, shadcn/ui references, codebase patterns)

**What's Next:**
- ⏳ Build pages 2-7 with Lovable (agent detail, dashboard, wizard, status, analytics, settings)
- ⏳ Build first 5 agents in n8n Cloud (Step 9)
- ⏳ Launch with SEO and email marketing (Steps 10-12)

**Timeline:** 3-4 weeks to MVP launch (homepage done, 6 pages remaining)

**See [02-build/build-overview.md](./02-build/build-overview.md) for complete 12-step build roadmap.**

---

## 💡 Why We Pivoted Strategy

**OLD Strategy Problems (research-archive/):**
- ❌ Customer-facing agents = high complexity (email, collections, WISMO)
- ❌ $12K setup + $2K/month = hard to sell without sales team
- ❌ Agencies-only = limited market (niche too narrow)
- ❌ Boutique service = doesn't scale (custom work for each customer)

**NEW Strategy Advantages:**
- ✅ Internal agents = simple (expense tracking, meeting notes)
- ✅ $100/month = impulse purchase (no sales call needed)
- ✅ All small businesses = massive market (freelancers, agencies, startups)
- ✅ Marketplace = scales infinitely (same 22 agents for all customers)

**Competitive Insight (01-strategy/competitive-analysis.md):**
- Zapier/Make/n8n force users to spend 10 hours building
- We save them 10 hours by selling pre-built
- Compete on TIME and SIMPLICITY, not price or features

---

## 📞 Quick Reference

| Question | Answer | See Document |
|----------|--------|--------------|
| What are we building? | Self-service marketplace selling pre-built AI agents | start.md |
| Who are we targeting? | All productivity-focused small businesses | start.md |
| How is this different from Zapier? | We sell pre-built (they force DIY) | 01-strategy/competitive-analysis.md |
| What agents will we sell? | 22 agents (5 at launch) | 01-strategy/agent-catalog.md |
| What's the pricing? | $29-150/month per agent (tiered) | start.md, 04-decisions/PRICING-DECISION-FINAL.md |
| What's the tech stack? | Lovable + Supabase + Stripe + n8n Cloud + Vercel | 01-strategy/vision.md |
| How do customers buy? | Browse → 1-click purchase → Setup wizard → Activate | 02-build/build-overview.md |
| What does the UI look like? | "Underground marketplace with tech legitimacy" dark indigo theme | 01-strategy/brand-design-system.md |
| When do we launch? | 10 weeks (phased rollout) | 02-build/build-overview.md |
| Why did we change strategies? | Old model didn't scale, new model does | CHANGELOG.md, 03-research/archive/README-ARCHIVE.md |
| What's our version history? | v0.1 (Boutique) → v2.1 (Tiered Marketplace) | CHANGELOG.md |

---

**New here? Start with:** [start.md](./start.md) → [BUILD-PLAN.md](./BUILD-PLAN.md) → [01-strategy/agent-catalog.md](./01-strategy/agent-catalog.md)

**Ready to build? Go to:** [BUILD-PLAN.md](./BUILD-PLAN.md) → [lovable-prompts/00-README.md](./lovable-prompts/00-README.md) → [02-build/build-overview.md](./02-build/build-overview.md)
