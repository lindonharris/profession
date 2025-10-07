# Marketplace UI/UX Specifications

**Last Updated:** October 6, 2025 (v1.0)
**Purpose:** Reference document for buyanagent.ai marketplace UI/UX
**Tool:** Lovable (AI-powered React + Tailwind generator)

---

## ⚠️ IMPORTANT: All Prompts Moved to Dedicated Folder

**This document is now purely referential. All Lovable build prompts have been moved to individual files.**

📁 **Prompts Location:** `/lovable-prompts/` (root of project)

---

## 🚀 How to Build the Marketplace

### **Step 1: Start with the README**

**[lovable-prompts/00-README.md](../lovable-prompts/00-README.md)**

This navigation guide contains:
- Complete page-to-page navigation map
- Build order and dependencies
- Cross-link verification checklist
- Usage instructions

### **Step 2: Build in Order (Phase 1 → Phase 2)**

**Phase 1 - MVP (5 pages):**
1. [Homepage](../lovable-prompts/01-homepage.md)
2. [Agent Detail Page](../lovable-prompts/02-agent-detail-page.md)
3. [Dashboard](../lovable-prompts/03-dashboard.md)
4. [Activation Wizard](../lovable-prompts/04-activation-wizard.md)
5. [Agent Status Page](../lovable-prompts/05-agent-status-page.md)

**Phase 2 - Premium (2 pages):**
6. [Premium Dashboard](../lovable-prompts/06-premium-dashboard.md)
7. [Settings & Billing](../lovable-prompts/07-settings-billing.md)

---

## 📋 Design System Reference

All pages use consistent design system. See any prompt file for full specifications.

### Core Design Principles

1. **Approachable** - Not intimidating (unlike developer tools)
2. **Fast** - Instant clarity on what each agent does
3. **Trustworthy** - Social proof, clear pricing, no hidden fees
4. **Delightful** - Smooth animations, micro-interactions

### Brand Identity

**Colors:**
- Background: Navy-black (#0B0E13) with 2% noise texture
- Primary: Indigo gradient (#4F46E5 to #3730A3)
- Text: Off-white (#F9FAFB) primary, subtle gray hierarchy
- Cards: Elevated dark (#161B22)
- Feedback: Green (#10B981), Red (#EF4444), Amber (#F59E0B)

**Typography:**
- Font: Inter (clean, modern sans-serif)
- Headlines: Bold, 32-48px, #F9FAFB
- Body: Regular, 16-18px, #E5E7EB
- Labels: Medium, 14px, #D1D5DB

**Icons:**
- Set: Heroicons only (NO emojis)
- Agent icons: Heroicon glyphs (EnvelopeIcon, CurrencyDollarIcon, etc.)
- Colors: White for nav, Indigo for CTAs

**Vibe:**
- "Underground marketplace with tech legitimacy" - dark, exclusive, sophisticated
- NOT: "Shopify meets Stripe" (that's light mode thinking)
- Think: Premium developer tool meets secret club

---

## 🎯 What Each Page Does

### Public Pages (Pre-Login)

**Homepage** - Marketplace landing with agent grid, categories, hero
- Entry point for all visitors
- Browse 22 agents across 5 categories
- Links to: Agent Detail, Sign In

**Agent Detail Page** - Product page template
- What the agent does (3-step visual)
- Pricing tiers (Utility/Premium comparison)
- Reviews, FAQ, integrations
- Links to: Activation Wizard

### Authenticated Pages (Post-Login)

**Dashboard** - Agent management hub
- View all active agents
- Quick actions (Settings, Pause, Cancel, Upgrade)
- Links to: Status Page, Premium Dashboard, Settings

**Activation Wizard** - 5-step onboarding
- Connect integrations → Configure rules → Test → Subscribe → Success
- Links to: Dashboard

**Agent Status Page (Utility)** - Simple monitoring
- Health status, activity metrics
- Control panel (Essential + Agent-specific)
- Activity log
- Links to: Dashboard

**Premium Dashboard (Premium)** - Analytics & insights
- Charts, trends, AI insights
- Advanced control panel
- Detailed activity table
- Links to: Dashboard

**Settings & Billing** - Account management
- Profile, billing, notifications, security
- Subscription management
- Payment methods
- Links to: Dashboard

---

## 📊 Page Navigation Summary

See [lovable-prompts/00-README.md](../lovable-prompts/00-README.md) for complete navigation map.

**Key Navigation Patterns:**

- **Navbar** (all pages): Logo → Homepage, Browse, Pricing, Docs, Sign In/User Avatar
- **Sidebar** (authenticated pages): My Agents → Dashboard, Billing → Settings, Settings → Settings
- **Back buttons**: Status Page → Dashboard, Premium Dashboard → Dashboard
- **Breadcrumbs**: Agent Detail → Home > Browse > Agent

**Verification:**
✅ Every page is accessible through links from other pages
✅ No orphan pages exist
✅ All navigation documented in 00-README.md

---

## 🔗 Related Documentation

**For building the marketplace:**
- [lovable-prompts/](../lovable-prompts/) - All Lovable build prompts (7 files)
- [build-overview.md](../02-build/build-overview.md) - Complete 12-step build guide
- [vision.md](./vision.md) - Technical architecture (Lovable + Supabase + Stripe + n8n)

**For agent specifications:**
- [agent-catalog.md](./agent-catalog.md) - All 22 agents with control panel mockups
- [competitive-analysis.md](./competitive-analysis.md) - Market positioning

**For strategic context:**
- [start.md](../start.md) - Overall marketplace strategy
- [README.md](../README.md) - Project navigation guide

---

## 🛠️ Build Process

**Time Estimate:** 2-3 days (per build-overview.md)

**Steps:**
1. Copy-paste prompts from `/lovable-prompts/` into Lovable
2. Generate each page in sequence (01 → 07)
3. Export generated code
4. Verify navigation links work
5. Deploy to Vercel

**Tech Stack:**
- UI: Lovable (generates React + Tailwind)
- Database: Supabase
- Payments: Stripe
- Backend: n8n Cloud
- Hosting: Vercel

See [vision.md](./vision.md) for complete technical architecture.

---

## ✅ Version Control

**Current Version:** v1.0 (Production-Ready)
**Last Major Update:** October 6, 2025 (Tiered pricing model, control panels added)

**What Changed in v1.0:**
- Added tiered pricing (Utility $29-79, Premium $100-150)
- Added tier badges to all agent cards
- Added control panels to status pages
- Moved all prompts to dedicated `/lovable-prompts/` folder
- Created navigation map and cross-link verification

See [CHANGELOG.md](../CHANGELOG.md) for complete version history.

---

**This document is now purely referential. All actionable Lovable prompts are in `/lovable-prompts/` folder.**
