# Lovable Build Prompts - Navigation Map

**Version:** v1.0
**Last Updated:** October 6, 2025
**Total Pages:** 7 (5 Phase 1 + 2 Phase 2)

---

## 🗺️ Complete Page Navigation Map

### **Public Pages (No Login Required)**

#### **Page 1: Homepage** → `01-homepage.md`
**URL:** `/`
**Links TO this page from:**
- Nowhere (this is the entry point)

**Links FROM this page to:**
- Agent Detail Page (clicking any agent card)
- Sign In page (navbar "Sign In" button)
- Browse Agents (navbar "Browse" link → same page, scrolls to grid)
- Pricing page (navbar "Pricing" → optional, can defer)
- Docs (navbar "Docs" → external link)

---

#### **Page 2: Agent Detail Page** → `02-agent-detail-page.md`
**URL:** `/agents/{agent-slug}`
**Links TO this page from:**
- Homepage (clicking agent cards)
- Dashboard (clicking "Browse More Agents" button)
- Search results (future)

**Links FROM this page to:**
- Homepage (breadcrumb "Home", navbar logo)
- Browse Agents (breadcrumb "Browse Agents" → back to homepage grid)
- Activation Wizard (clicking "Choose Your Tier" or "Activate" CTA)
- Sign In (if user not logged in, before activation)

---

### **Authenticated Pages (Login Required)**

#### **Page 3: Dashboard** → `03-dashboard.md`
**URL:** `/dashboard`
**Links TO this page from:**
- Activation Wizard Step 5 Success ("Go to Dashboard" CTA)
- Navbar user dropdown (after login, "My Agents" option)
- Agent Status Page (back button)
- Premium Dashboard (back button)
- Settings (sidebar "My Agents" nav item)

**Links FROM this page to:**
- Homepage (navbar logo, sidebar logo)
- Agent Status Page (clicking "Settings" button on Utility tier agents)
- Premium Dashboard (clicking "Dashboard" button on Premium tier agents)
- Homepage/Browse (clicking "Browse More Agents" CTA)
- Settings (clicking "Settings" button on any agent)
- Billing (sidebar "Billing" nav item)
- Settings (sidebar "Settings" nav item)
- User dropdown menu (navbar avatar)

---

#### **Page 4: Activation Wizard** → `04-activation-wizard.md`
**URL:** `/activate/{agent-slug}`
**Links TO this page from:**
- Agent Detail Page (clicking "Choose Your Tier" or "Activate" CTA)

**Links FROM this page to:**
- Dashboard (Step 5 Success: "Go to Dashboard" CTA)
- Homepage/Browse (Step 5 Success: "Activate Another Agent" button)

---

#### **Page 5: Agent Status Page (Utility)** → `05-agent-status-page.md`
**URL:** `/dashboard/agents/{agent-id}/status`
**Links TO this page from:**
- Dashboard (clicking "Settings" button on Utility tier agents)

**Links FROM this page to:**
- Dashboard (back button "← Back to Dashboard")
- Settings modal (clicking "⚙️ Settings" in Essential Controls)
- History modal (clicking "📜 History" in Essential Controls)
- Integrations modal (clicking "🔌 Integrations" in Essential Controls)

---

#### **Page 6: Premium Dashboard (Analytics)** → `06-premium-dashboard.md`
**URL:** `/dashboard/agents/{agent-id}/analytics`
**Links TO this page from:**
- Dashboard (clicking "📊 Dashboard" button on Premium tier agents)

**Links FROM this page to:**
- Dashboard (back button "← Back to Dashboard")
- Settings modal (clicking "⚙️ Settings" in Essential Controls)
- History modal (clicking "📜 History")
- Export Report (clicking "📊 Export Report")
- Alert Settings modal (clicking "🔔 Alert Settings")

---

#### **Page 7: Settings & Billing** → `07-settings-billing.md`
**URL:** `/dashboard/settings`
**Links TO this page from:**
- Dashboard (sidebar "Settings" nav item, sidebar "Billing" nav item)
- Navbar user dropdown ("Account Settings" option)
- Agent Status Page (clicking "⚙️ Settings" → goes to agent-specific settings tab)
- Premium Dashboard (clicking "⚙️ Settings")

**Links FROM this page to:**
- Dashboard (sidebar "My Agents" nav item)
- Stripe Customer Portal (clicking "Update Card" button → external)
- Invoice PDFs (clicking "Download PDF" in billing history)

---

## ✅ Navigation Verification Checklist

**Every page is accessible from at least one other page:**
- ✅ Homepage: Entry point (no incoming links needed)
- ✅ Agent Detail: From Homepage agent cards, Dashboard "Browse More"
- ✅ Dashboard: From Activation Wizard success, navbar dropdown, all sidebar navs
- ✅ Activation Wizard: From Agent Detail Page CTAs
- ✅ Agent Status Page: From Dashboard "Settings" button (Utility agents)
- ✅ Premium Dashboard: From Dashboard "Dashboard" button (Premium agents)
- ✅ Settings: From Dashboard sidebar, navbar dropdown, any agent settings button

**No orphan pages exist.** ✅

---

## 📋 Build Order & Dependencies

### **Phase 1: MVP (Build in this order)**

1. **Homepage** (no dependencies)
   - Build first, establishes design system

2. **Agent Detail Page** (depends on: Homepage navbar/footer)
   - Reuses navbar/footer from Homepage

3. **Dashboard** (depends on: Homepage navbar, Agent Detail design)
   - Reuses navbar, adds sidebar navigation

4. **Activation Wizard** (depends on: Dashboard success redirect)
   - Reuses navbar (minimal version)

5. **Agent Status Page** (depends on: Dashboard sidebar)
   - Reuses Dashboard sidebar + navbar

### **Phase 2: Premium (Build after Phase 1)**

6. **Premium Dashboard** (depends on: Dashboard sidebar, Status Page structure)
   - Reuses sidebar, extends Status Page with charts

7. **Settings & Billing** (depends on: Dashboard sidebar)
   - Reuses sidebar, final page to build

---

## 🎯 Key Navigation Patterns

### **Navbar (Present on ALL pages):**
- Logo → Homepage
- Browse → Homepage agent grid
- Pricing → Pricing page (optional)
- Docs → External docs
- Sign In → Auth modal
- Start Free → Homepage "Browse Agents" or Dashboard (if logged in)
- User Avatar Dropdown (when logged in):
  - Account Settings → Settings page
  - Billing → Settings page (Billing tab)
  - Help & Support → External
  - Sign Out → Homepage (logged out)

### **Sidebar (Present on all AUTHENTICATED pages except Activation Wizard):**
- Logo → Dashboard
- My Agents → Dashboard
- Billing → Settings (Billing tab)
- Settings → Settings (Profile tab)

### **Breadcrumbs (Present on Agent Detail Page only):**
- Home → Homepage
- Browse Agents → Homepage grid
- {Agent Name} → Current page

### **Back Buttons:**
- Agent Status Page: "← Back to Dashboard"
- Premium Dashboard: "← Back to Dashboard"

---

## 🔗 Critical Cross-Links to Implement

**From Homepage:**
- Agent cards → Agent Detail Pages
- "Browse Agents" CTA → Scroll to grid (same page)
- Navbar "Sign In" → Auth modal

**From Agent Detail Page:**
- "Choose Your Tier" / "Activate" → Activation Wizard
- Breadcrumb → Homepage

**From Dashboard:**
- "Settings" button (Utility) → Agent Status Page
- "Dashboard" button (Premium) → Premium Dashboard
- "Browse More Agents" → Homepage
- Sidebar "Billing" → Settings (Billing tab)
- Sidebar "Settings" → Settings (Profile tab)

**From Activation Wizard:**
- Step 5 "Go to Dashboard" → Dashboard
- Step 5 "Activate Another Agent" → Homepage

**From Agent Status Page:**
- Back button → Dashboard

**From Premium Dashboard:**
- Back button → Dashboard

**From Settings:**
- Sidebar "My Agents" → Dashboard

---

## 📁 File Structure

```
lovable-prompts/
├── 00-README.md (this file)
├── 01-homepage.md
├── 02-agent-detail-page.md
├── 03-dashboard.md
├── 04-activation-wizard.md
├── 05-agent-status-page.md
├── 06-premium-dashboard.md
└── 07-settings-billing.md
```

---

## 🚀 Usage Instructions

1. **Build in order:** 01 → 02 → 03 → 04 → 05 (Phase 1) → 06 → 07 (Phase 2)
2. **Copy-paste prompts** directly into Lovable
3. **Export generated code** after each page
4. **Test navigation links** between pages as you build
5. **Verify all cross-links** work before moving to next page

Each prompt file contains:
- Complete Lovable prompt (copy-paste ready)
- Sample data for that page
- Navigation to/from that page
- Next step instructions

---

**Start with:** `01-homepage.md`
**End with:** `07-settings-billing.md`
**Total build time:** 2-3 days (per build-overview.md estimate)
