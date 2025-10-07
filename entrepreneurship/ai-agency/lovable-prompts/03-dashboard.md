wsl# Lovable Prompt: Dashboard (Agent Management Hub)

**Phase:** 1 - MVP Launch
**Page:** Dashboard
**URL:** `/dashboard`
**Build Order:** 3 of 7

---

## Copy-Paste This Into Lovable:

```
Create an authenticated dashboard for managing activated AI agents (buyanagent.ai).

REFERENCE EXISTING CODEBASE:
- Same design system from homepage (see src/index.css)
- Same components: Button, Badge, Card from shadcn/ui
- Icons: Lucide React only (NO emojis)
- Use transition-fast utility for all animations
- Use rounded-sm for 2px border radius
- Same navbar from homepage (but add user avatar dropdown on right)

LAYOUT:
- Sidebar navigation (left, 240px wide, #161B22 background)
- Main content area (right, full remaining width, #0B0E13 background)

SIDEBAR:
- Use bg-card background
- Logo at top with gradient text
- Navigation items (use Lucide icons):
  • "My Agents" (icon: LayoutGrid)
  • "Billing" (icon: CreditCard)
  • "Settings" (icon: Settings)
- Active state: bg-primary text-primary-foreground
- Inactive: text-muted-foreground hover:text-foreground
- Icons from lucide-react (20px)

MAIN CONTENT:
- Background: #0B0E13
- Header: "My Agents (3 active)" (Inter Bold 28px, #F9FAFB, margin-bottom 24px)

- Agent cards (vertically stacked, reference AgentCard pattern but expanded for dashboard):
  Cards are clickable links to /dashboard/agents/{id}/status

  Card structure:
  1. Top row: Lucide icon (32px text-primary) + Agent name (text-xl font-semibold) + <Badge variant={tier}>
  2. Metadata: Tier name • Price/month (text-muted-foreground)
  3. Metrics: Last run time + activity stats (text-muted-foreground text-sm)
  4. Action buttons row:
     - "Settings" (<Button variant="outline">)
     - "Upgrade to Premium" (Utility only, variant="outline")
     - "Dashboard" (Premium only, variant="outline")
     - "Pause" (variant="outline")
     - "Cancel" (variant="destructive outline")
     All buttons use stopPropagation() to prevent card navigation

- Show 3 sample agents:
  1. "Expense Tracker" (Utility, $69/month, Banknote from lucide-react)
  2. "Email Sweeper" (Utility, $29/month, Mail from lucide-react)
  3. "Invoice Chaser" (Premium, $100/month, FileText from lucide-react, show "Dashboard" button)

- Bottom CTA: <Button variant="default">+ Browse More Agents</Button> (centered)

RESPONSIVE:
- Sidebar collapses to hamburger menu on mobile
- Agent cards stack on all screen sizes
- Action buttons wrap on mobile

Use Tailwind CSS, add smooth hover states with indigo glows, maintain consistency with homepage dark design.
```

---

## Sample Agent Card Data:

**Card 1: Expense Tracker (Utility)**
- Icon: BanknotesIcon (Heroicons, 32px, #4F46E5)
- Name: Expense Tracker
- Tier: UTILITY (#374151 bg, #9CA3AF text)
- Price: $69/month
- Status: Active
- Last run: 2 hours ago
- Metrics: "Processed 3 receipts this week"
- Buttons: Settings, Upgrade to Premium, Pause, Cancel

**Card 2: Email Sweeper (Utility)**
- Icon: EnvelopeIcon (Heroicons, 32px, #4F46E5)
- Name: Email Sweeper
- Tier: UTILITY
- Price: $29/month
- Status: Active
- Last run: 1 hour ago
- Metrics: "Processed 47 emails today"
- Buttons: Settings, Upgrade to Premium, Pause, Cancel

**Card 3: Invoice Chaser (Premium)**
- Icon: DocumentTextIcon (Heroicons, 32px, #4F46E5)
- Name: Invoice Chaser
- Tier: PREMIUM (rgba(79,70,229,0.1) bg, #4F46E5 text)
- Price: $100/month
- Status: Active
- Last run: 30 min ago
- Metrics: "DSO: 28 days (37% improvement)"
- Buttons: Settings, Dashboard, Pause, Cancel

---

## User Avatar Dropdown (Top Right):

When user clicks their avatar, show dropdown menu (use DropdownMenu from shadcn/ui):
- Use Avatar component for profile picture
- User name + email (text-foreground + text-muted-foreground)
- Separator component
- "Account Settings" (with Settings icon from lucide-react)
- "Billing" (with CreditCard icon)
- "Help & Support" (with HelpCircle icon)
- Separator
- "Sign Out" (text-destructive with LogOut icon)

---

## Empty State (if user has no agents):

Replace agent cards with:
- Large Lucide icon (64px text-muted-foreground, use LayoutGrid or Inbox)
- Title: "No Active Agents Yet" (text-2xl font-bold)
- Subtitle: "Browse our marketplace to activate your first AI agent" (text-muted-foreground max-w-md)
- CTA: <Button variant="default">Browse Agents →</Button>

All centered vertically and horizontally in main content area.

---

## Next Step:

After Lovable generates this page, move to **04-activation-wizard.md** to build the 5-step onboarding flow.
