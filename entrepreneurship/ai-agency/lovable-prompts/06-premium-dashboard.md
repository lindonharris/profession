# Lovable Prompt: Premium Dashboard (Analytics & Insights)

**Phase:** 2 - Premium Tier
**Page:** Premium Agent Dashboard
**URL:** `/dashboard/agents/{agent-id}/analytics`
**Build Order:** 6 of 7

---

## Copy-Paste This Into Lovable:

```
I need a full analytics dashboard for Premium tier agents. This is what justifies the $100-150/month price - real business intelligence, not just status monitoring.

Think Stripe analytics or Mixpanel - clean charts, key metrics at a glance, actionable insights.

Use the same sidebar from other dashboard pages.

**Top of page:**
- "← Back to Dashboard" link
- Agent icon and name with PREMIUM tier badge
- Date range selector on the right (Last 7 days, Last 30 days, Last 90 days, All time, Custom)

**Key metrics row:**
Show 4 big KPI cards across the top.

For Invoice Chaser example:
- Average DSO (Days Sales Outstanding): 28 days ↓ 37% improvement
- Total Invoices Tracked: 147
- Payment Success Rate: 89%
- Time Saved: 12.5 hours this month

Each card shows:
- Icon from Lucide React
- Label
- Big number
- Green/red arrow showing if it improved or got worse

Grid should go 4 columns → 2 columns → 1 column on mobile.

**Charts section:**
Two charts side by side (stack on mobile).

Chart 1: Line chart showing DSO trend over time
- X-axis: dates
- Y-axis: days
- Line color: indigo from our design system
- Show the downward trend visually

Chart 2: Bar chart showing invoice status distribution
- Categories: Paid On Time, Paid Late, Outstanding, Overdue
- Color code: green, amber, blue, red

Use recharts library (it works well with shadcn/ui) or the Chart component if available.

**AI Insights card:**
Show 3-5 bullet points with insights generated from the data.

For Invoice Chaser:
- "Client XYZ consistently pays 15 days late - consider adjusting terms"
- "Invoices sent on Monday get paid 8 days faster than Friday invoices"
- "Your DSO improved 12% this month compared to last month"

Add a Sparkles icon from Lucide React next to "AI Insights" heading.

**Control panel section:**
Same essential controls as Utility tier (Pause, Settings, History), but add Premium-only controls:
- "Export Report" button with dropdown (CSV, PDF, Excel)
- "Custom Date Range" button
- "Alert Settings" button (get notified when DSO spikes)

**Agent-specific advanced controls:**
For Invoice Chaser:
- Visual timeline showing when reminders go out (Day -5, 0, +3, +7, +15, +30)
- Ability to edit the reminder schedule
- Client tagging system (VIP, Slow Payer, New Client)
- Email template editor with tone controls
- DSO target setter with alerts

**Recent activity table:**
Same as Utility tier but with more columns:
- Time | Action | Client | Invoice Amount | Days Outstanding | Result

**Design notes:**
- Use Card components for everything
- Use recharts for charts (LineChart, BarChart components)
- Icons from Lucide React (TrendingUp, TrendingDown, Sparkles, BarChart, etc.)
- Keep the indigo accent colors
- Make sure charts are responsive
- Show empty states if no data yet
```

---

## Sample Data for Invoice Chaser:

**Key Metrics:**
- Average DSO: 28 days (↓ 37% from 45 days)
- Total Invoices Tracked: 147
- Payment Success Rate: 89%
- Time Saved: 12.5 hours

**DSO Trend Chart (Last 30 Days):**
Week 1: 42 days
Week 2: 38 days
Week 3: 32 days
Week 4: 28 days

**Invoice Status Distribution:**
- Paid On Time: 87 invoices (green)
- Paid Late: 34 invoices (amber)
- Outstanding: 18 invoices (blue)
- Overdue: 8 invoices (red)

**AI Insights:**
- Client "ABC Design Studio" consistently pays 15 days late - consider adjusting payment terms
- Invoices sent on Monday get paid 8 days faster on average than those sent on Friday
- Your DSO improved 12% this month (28 days vs 32 days last month)
- 3 clients account for 60% of your late payments - focus collection efforts here

**Advanced Controls:**
- Reminder Schedule: Day -5 (friendly), Day 0 (reminder), Day +3 (follow-up), Day +7 (firm), Day +15 (urgent), Day +30 (final notice)
- Tagged Clients: 12 VIPs, 8 Slow Payers, 23 New Clients
- DSO Target: 25 days (currently 28, need 3-day improvement)

---

## Next Step:

After Lovable generates this dashboard, move to **07-settings-billing.md** to build the account management page.
