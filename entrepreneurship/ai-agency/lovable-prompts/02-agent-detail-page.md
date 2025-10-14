# Lovable Prompt: Agent Detail Page

**Phase:** 1 - MVP Launch
**Page:** Agent Product Page (Template)
**URL:** `/agents/{agent-slug}`
**Build Order:** 2 of 7

---

## Copy-Paste This Into Lovable:

```
I need a product detail page for an AI agent marketplace. This should match the homepage we already built (same dark theme, same navbar/footer, same design system).

The page should work like a premium product page - think Stripe or Linear. Clean, focused, shows value immediately.

Here's what I need on the page:

**Top of page:**
- Breadcrumb trail showing "Home > Browse Agents > {Agent Name}" so people know where they are
- Big hero section with the agent's icon (use Lucide icons like we did on homepage) next to the agent name
- 2-3 paragraphs explaining what it does and why it's valuable
- Quick stats line like "From $100/month • 15 min setup • 127 members using"
- Two buttons: primary "Request Access" and secondary "Watch Demo"

**How it works section:**
- Show 3 steps in a visual flow (Connect → Configure → Activate)
- Use cards with icons for each step
- Put arrow icons between them to show the flow
- Should stack nicely on mobile

**Integrations section:**
- Grid showing which apps this agent connects to (Gmail, Sheets, QuickBooks, etc.)
- Logo placeholders for each integration
- 6 columns on desktop, 3 on mobile

**Pricing section (for Premium tier agents only):**
- Two pricing cards side by side comparing "Utility Tier" vs "Premium Tier"
- Show what you get at each level (status page vs full dashboard, etc.)
- Highlight the Premium tier with a subtle indigo glow
- Buttons to activate at either tier

**Social proof section:**
- Customer testimonial with quote
- Star rating (use Star icons from Lucide, not emoji)
- Attribution with customer name and title

**FAQ section:**
- Collapsible accordion with 5-7 common questions
- Use the Collapsible component from shadcn/ui
- Chevron icon that rotates when expanded

**Design notes:**
- Match homepage exactly (same colors, same fonts, same components)
- Use shadcn/ui components: Button, Card, Badge, Collapsible
- Use Lucide React for all icons
- Keep it responsive - should look great on phone and desktop
- Dark mode optimized

The URL pattern should be /agents/{agent-id} and pull the agent data based on which one they clicked from the homepage.
```

---

## Sample Content for Invoice Chaser (Premium Agent):

**Hero Section:**
- Icon: Banknote (lucide-react)
- Title: Invoice Chaser
- Description:
  "Never chase late payments again. Invoice Chaser automatically sends smart payment reminders on your behalf, tracks which clients pay fastest, and shows you exactly where your cash is stuck.

  Get paid 17 days faster on average. See DSO trends, payment velocity by client, and identify chronic late payers before they become a problem.

  Integrates with your existing invoicing system (QuickBooks, FreshBooks, Xero, or send invoices via email). Set it up once, forget about it forever."

**How It Works:**
1. **Connect** (Icon: Link from lucide-react)
   - Title: Connect Your Invoicing System
   - Description: OAuth connection to QuickBooks, Xero, or Stripe in under 2 minutes

2. **Configure** (Icon: Settings from lucide-react)
   - Title: Set Reminder Schedule
   - Description: Choose when reminders go out: 5 days before, day of, 3 days after, 7 days after, etc.

3. **Activate** (Icon: CheckCircle from lucide-react)
   - Title: Let It Run
   - Description: Invoice Chaser monitors invoices 24/7 and sends reminders automatically

**Integrations Required:**
- QuickBooks, Xero, FreshBooks, Stripe, Gmail (for manual invoices), Slack (optional notifications)

**Pricing Comparison:**
- **Premium Tier Only:** $100/month
  - Full analytics dashboard
  - DSO tracking & trends
  - Client payment behavior tagging
  - Email template customization
  - Priority support
  - Export reports (CSV/PDF)

**Reviews:**
"Invoice Chaser reduced our DSO from 45 days to 28 days in just 2 months. The dashboard shows exactly which clients are slow to pay - game changer."
— Sarah Chen, Design Studio Owner

**FAQ:**
- Q: What invoicing systems work with this?
  A: QuickBooks, Xero, FreshBooks, Stripe, or any system that sends invoices via email.

- Q: Can I customize reminder emails?
  A: Yes, full template editor with tone controls (friendly → professional → firm).

- Q: What if I have VIP clients who shouldn't get auto-reminders?
  A: Set invoice thresholds (e.g., >$5K requires manual approval) and manage VIP lists.

---

## Navigation FROM This Page:

- "Request Access" button → Request Access Modal
- Breadcrumb "Home" → Homepage (01-homepage.md)
- Breadcrumb "Browse Agents" → Homepage agent grid
- Navbar links → Same as homepage

---

## Next Step:

After Lovable generates this template, move to **03-dashboard.md**
