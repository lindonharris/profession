# Lovable Prompt: Dashboard (Agent Management Hub)

**Phase:** 1 - MVP Launch
**Page:** Dashboard
**URL:** `/dashboard`
**Build Order:** 3 of 7

---

## Copy-Paste This Into Lovable:

```
I need a dashboard where users manage their activated AI agents. Think Notion or Linear dashboard - clean, organized, easy to see what's running.

This should use the same navbar/footer components we created for the homepage and detail page. Same dark theme, same design system.

**Layout:**
The dashboard has two parts - a sidebar on the left for navigation, and the main content area showing active agents.

**Sidebar navigation:**
- Company logo at top
- Three menu items: "My Agents", "Billing", "Settings"
- Use icons from Lucide React (LayoutGrid, CreditCard, Settings)
- Highlight the active section
- On mobile, this collapses to a hamburger menu

**Top bar:**
- Same navbar as other pages, but add a user avatar dropdown on the right
- Clicking avatar shows menu: Account Settings, Billing, Help & Support, Sign Out
- Use the Avatar and DropdownMenu components from shadcn/ui

**Main content - Agent cards:**
Each activated agent shows as a card (similar to the homepage cards but expanded with more info):
- Agent icon and name at top
- Badge showing tier (UTILITY or PREMIUM)
- Price per month
- Last time it ran (e.g., "2 hours ago")
- Quick metric (like "Processed 3 receipts this week" or "DSO: 28 days")
- Action buttons at bottom:
  - Settings (everyone gets this)
  - "Upgrade to Premium" (only for Utility tier agents)
  - "Dashboard" (only for Premium tier agents - links to analytics)
  - Pause
  - Cancel (use red/destructive styling)

The whole card should be clickable and go to that agent's status page, but the buttons should NOT trigger the card click (use stopPropagation).

**Sample agents to show:**
1. Expense Tracker (Utility, $69/month, Banknote icon) - "Processed 3 receipts this week"
2. Email Sweeper (Utility, $29/month, Mail icon) - "Processed 47 emails today"
3. Invoice Chaser (Premium, $100/month, FileText icon) - "DSO: 28 days (37% improvement)"

**Bottom of page:**
- Big "+ Browse More Agents" button that goes back to the marketplace

**If user has no agents yet:**
- Show empty state with large icon
- "No Active Agents Yet" heading
- "Browse our marketplace to activate your first AI agent" subtext
- "Browse Agents →" button

**Design notes:**
- Use Card components from shadcn/ui
- Use Badge component for tier labels (same variants as homepage)
- Buttons should use the Button component with appropriate variants
- Keep all the indigo accent colors from our design system
- Make it responsive - sidebar becomes hamburger on mobile
- Smooth transitions on hover states
```

---

## Sample Agent Card Data:

**Card 1: Expense Tracker (Utility)**
- Icon: Banknote (Lucide React)
- Name: Expense Tracker
- Tier: UTILITY
- Price: $69/month
- Status: Active
- Last run: 2 hours ago
- Metrics: "Processed 3 receipts this week"
- Buttons: Settings, Upgrade to Premium, Pause, Cancel

**Card 2: Email Sweeper (Utility)**
- Icon: Mail (Lucide React)
- Name: Email Sweeper
- Tier: UTILITY
- Price: $29/month
- Status: Active
- Last run: 1 hour ago
- Metrics: "Processed 47 emails today"
- Buttons: Settings, Upgrade to Premium, Pause, Cancel

**Card 3: Invoice Chaser (Premium)**
- Icon: FileText (Lucide React)
- Name: Invoice Chaser
- Tier: PREMIUM
- Price: $100/month
- Status: Active
- Last run: 30 min ago
- Metrics: "DSO: 28 days (37% improvement)"
- Buttons: Settings, Dashboard, Pause, Cancel

---

## Next Step:

After Lovable generates this page, move to **04-activation-wizard.md** to build the 5-step onboarding flow.
