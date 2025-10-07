# Lovable Prompt: Agent Detail Page

**Phase:** 1 - MVP Launch
**Page:** Agent Product Page (Template)
**URL:** `/agents/{agent-slug}`
**Build Order:** 2 of 7

---

## Copy-Paste This Into Lovable:

```
Create a detailed product page for an AI agent in a dark, exclusive marketplace (buyanagent.ai).

REFERENCE EXISTING CODEBASE:
- Same design system from homepage (see src/index.css)
- Same components: Button, Badge, ThemeToggle from shadcn/ui
- Icons: Lucide React only (NO emojis) - https://lucide.dev/icons/
- Transitions: Use transition-fast utility
- Border radius: Use rounded-sm (2px)
- Same navbar from homepage
- Same footer from homepage

ROUTING:
- URL pattern: /agents/{agent-id} (use agent.id field from homepage)
- Example: /agents/email-classifier
- Fetch agent data based on route parameter

BREADCRUMB:
- "Home > Browse Agents > {Agent Name}" (14px, #9CA3AF)
- Separator: ">" (#6B7280)
- Current page: #F9FAFB bold
- Hover: #4F46E5
- Margin bottom: 24px

HERO SECTION:
- Layout: Horizontal - Lucide icon (64px, text-primary) + Title (text-4xl font-bold)
- Description: 2-3 paragraphs (text-lg text-muted-foreground, max-w-3xl)
- Metadata: "From ${PRICE}/month • 15-20 min setup • 127 members using"
- CTAs: <Button variant="default">Request Access →</Button> + <Button variant="outline">Watch Demo</Button>

HOW IT WORKS (3-STEP VISUAL):
- Section title (text-2xl font-bold mb-10)
- Three cards in grid, use Card component from shadcn/ui
- Each card: Lucide icon (48px text-primary) → Title (font-semibold) → Description (text-muted-foreground)
- Arrow icons between cards (ChevronRight from lucide-react)
- Responsive grid (3 columns → stack on mobile)

INTEGRATIONS SECTION:
- Section title: "Required Integrations" (Inter Bold 24px, #F9FAFB)
- Grid: 80x80px cards, #1F2937 background, integration logo centered, name below (#D1D5DB, 14px)
- 6 columns desktop, 3 mobile
- Examples: Gmail, Google Sheets, Slack, QuickBooks

PRICING COMPARISON (for Premium tier agents):
- Two columns: "Utility Tier" vs "Premium Tier"
- Utility card: #161B22 bg, #374151 border
  - Price, "Status page", "Email support", "Unlimited runs"
- Premium card: #4F46E520 bg (10% indigo tint), #4F46E5 border (highlighted)
  - Price, "Full dashboard", "Analytics", "Priority support", "Export reports"
- CTA buttons below each: Both use indigo gradient
- All text: #F9FAFB headlines, #E5E7EB body

REVIEWS SECTION:
- Section title (text-3xl font-bold text-center)
- Testimonial card using Card component
- Quote (italic text-lg text-muted-foreground)
- Attribution (text-sm text-right)
- Star rating: Use Star icon from lucide-react (NO emoji stars)

FAQ ACCORDION:
- Use Collapsible component from shadcn/ui (@/components/ui/collapsible)
- Section title (text-2xl font-bold)
- Each item: Question (font-medium) + expandable answer (text-muted-foreground)
- Expand icon: ChevronDown from lucide-react (rotates on open)
- Include 5-7 questions

Use Tailwind CSS, fully responsive, 200ms transitions, dark mode optimized.
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
