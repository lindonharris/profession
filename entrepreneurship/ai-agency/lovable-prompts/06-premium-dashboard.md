# Lovable Prompt: Premium Dashboard (Analytics & Insights)

**Phase:** 2 - Premium Tier
**Page:** Premium Agent Dashboard
**URL:** `/dashboard/agents/{agent-id}/analytics`
**Build Order:** 6 of 7

---

## Copy-Paste This Into Lovable:

```
Create a full-featured analytics dashboard for a Premium tier AI agent (buyanagent.ai).

REFERENCE EXISTING CODEBASE:
- Same design system from dashboard
- Icons: Lucide React (ChartBar, TrendingUp, Sparkles, etc.)
- Use Card, Button, Select components from shadcn/ui
- Charts: Use recharts library (common with shadcn/ui) or Chart component if available
- Same navbar and sidebar

LAYOUT:
- Sidebar (240px, #161B22 background, same as previous pages)
- Main content area (remaining width, #0B0E13 background)

PAGE HEADER:
- Back button: "← Back to Dashboard" (#9CA3AF, hover #4F46E5, 14px)
- Agent title row: Heroicon (48px, #4F46E5) + Agent name (Inter Bold 32px, #F9FAFB) + Tier badge ("PREMIUM", rgba(79,70,229,0.1) bg, #4F46E5 text)
- Subtitle: "Analytics dashboard" (16px, #9CA3AF)
- Date range selector (top-right): Dropdown with "Last 7 days", "Last 30 days", "Last 90 days", "All time", "Custom range"
  - Dropdown: #161B22 bg, #374151 border, #F9FAFB text
- Padding: 32px top/bottom

KEY METRICS ROW (use Card component):
- 4 metric cards in responsive grid
- Each card shows:
  • Lucide icon (BarChart, DollarSign, FileText, CheckCircle)
  • Label (text-sm text-muted-foreground)
  • Big number (text-4xl font-bold)
  • Change indicator with arrow (text-green-500 or text-red-500)
- Grid: 4 cols → 2 cols → 1 col responsive

CHARTS SECTION (use recharts or shadcn/ui Chart component):
- Two charts side-by-side in Cards
- Chart 1: Line chart for trends over time
  • Use <LineChart>, <Line>, <XAxis>, <YAxis>, <Tooltip>
  • Line stroke: hsl(var(--primary))
  • Grid: stroke-muted
- Chart 2: Bar chart for distribution
  • Use <BarChart>, <Bar>
  • Colors: hsl(var(--primary)) or conditional (green/amber/red)

INSIGHTS CARD (use Card component):
- Title with <Sparkles className="text-primary" /> icon
- Bullet list of insights (text-muted-foreground):
  • Each with <Lightbulb className="text-amber-500" /> icon
- Insights refresh daily

CONTROL PANEL SECTION:
- Background: #161B22, #374151 border, 24px padding, 12px border-radius, margin-top 24px
- Title: "Control Panel" (Inter Bold 20px, #F9FAFB, margin-bottom 16px)
- Divider (#374151)

ESSENTIAL CONTROLS (Same as Utility tier):
- Title: "Essential Controls" (Inter Medium 16px, #E5E7EB)
- Buttons: Pause Agent, Settings, History, Integrations (same styling as Status Page)
- Plus Premium-only controls:
  • "Export Report" (outline button, ArrowDownTrayIcon, with dropdown: CSV, PDF, Excel)
  • "Custom Date Range" (outline button, CalendarIcon)
  • "Alert Settings" (outline button, BellIcon)

AGENT-SPECIFIC CONTROLS (Premium Advanced):
- Title: "Invoice Chaser Advanced Controls" (Inter Medium 16px, #E5E7EB)
- Divider (#374151)

1. **Escalation Schedule Editor**
   - Visual timeline showing reminder schedule (#1F2937 background)
   - Draggable markers for Day -5, 0, +3, +7, +15, +30 (#4F46E5 markers)
   - Edit button (outline) opens modal with detailed schedule

2. **Email Template Customizer**
   - Buttons for each escalation stage: "Friendly", "Professional", "Firm", "Final"
   - Button styling: #374151 border, #E5E7EB text, hover #4F46E5 border
   - Click opens template editor modal (#161B22 background)

3. **VIP Client Rules**
   - Text: "Invoice threshold: $5,000+ requires manual approval" (14px, #9CA3AF)
   - Button: "Manage VIP List" (outline, opens modal)
   - Text: "VIP clients: 12 configured" (12px, #6B7280)

4. **Payment Behavior Tags**
   - Auto-tags clients: "Fast Payer" (#10B981), "Reliable" (#3B82F6), "Needs Follow-Up" (#F59E0B), "High Risk" (#EF4444)
   - Badge styling: transparent bg, colored text/border
   - Button: "Manage Tag Rules" (outline)

5. **Custom Metrics**
   - Dropdown: Select additional metrics to track (#161B22 bg, #374151 border)
   - Options: Average invoice value, Client lifetime value, Seasonal trends, etc.

DETAILED ACTIVITY TABLE (Bottom):
- Background: #161B22, #374151 border, 24px padding, 12px border-radius, margin-top 24px
- Title: "Detailed Activity" (Inter Bold 20px, #F9FAFB)
- Search bar (top-right): Filter by client, invoice #, date range (#1F2937 bg, #374151 border, #F9FAFB text)
- Table columns: Date | Client | Invoice # | Amount | Status | Days Open | Action
- Table styling:
  • Header: #1F2937 background, Inter Medium 14px, #E5E7EB
  • Rows: 14px, #F9FAFB, zebra striping (#161B22 / #1F2937)
  • Status badges: #10B981 (Paid), #F59E0B (Pending), #EF4444 (Overdue), hover with indigo glow
  • Action column: "View Details →" link (#4F46E5)
- Pagination at bottom: 10/25/50/100 rows per page (#9CA3AF text, #4F46E5 for active)
- Export button (top-right): "Export Table" (CSV/PDF, outline)

RESPONSIVE:
- Key metrics: 4 → 2 → 1 columns as screen shrinks
- Charts: side-by-side → stacked on mobile
- Table: horizontal scroll on mobile (preserve all columns)
- Control panel: buttons wrap on mobile

Use Tailwind CSS, add chart library (Recharts or Chart.js), smooth animations on data updates, maintain dark design consistency.
```

---

## Sample Data for Invoice Chaser Dashboard:

**Key Metrics:**
1. DSO: 28 days (was 45 days, ▼ 37%)
2. Cash Flow Impact: $12,400 (was $8,700, ↑ 42%)
3. Invoices Tracked: 127 (was 117, ↑ 8%)
4. Payment Rate: 94% (was 88%, ↑ 6%)

**Chart 1: DSO Trend (Last 90 days)**
- Data points showing gradual decline from 45 → 28 days
- Annotation on chart: "Agent activated" (arrow pointing to start of decline)

**Chart 2: Payment Velocity by Client**
Top 10 clients ranked by average days to payment:
1. Acme Corp: 15 days (green bar)
2. Widget Inc: 18 days (green)
3. Design Co: 22 days (yellow)
4. Marketing Pro: 28 days (yellow)
5. Startup XYZ: 35 days (yellow)
6. Agency 123: 42 days (red)
7. Consulting LLC: 48 days (red)
8. Freelance Co: 52 days (red)
9. Creative Partners: 58 days (red)
10. Slow Payer Inc: 67 days (red)

**AI Insights:**
- "3 clients consistently pay late (>40 days). Consider requiring upfront deposits from: Agency 123, Consulting LLC, Freelance Co."
- "Friday invoices get paid 12% faster than Monday invoices. Optimize send timing to Thursday/Friday."
- "Clients with payment terms >Net 30 have 2.3x higher DSO. Tighten terms to Net 15 or Net 30 maximum."
- "Invoice amounts >$10K take 2x longer to pay. Consider breaking large projects into milestone invoices."

**Detailed Activity Table (Last 10 rows):**
| Date | Client | Invoice # | Amount | Status | Days Open | Action |
|------|--------|-----------|--------|--------|-----------|--------|
| Oct 5 | Acme Corp | #1027 | $2,400 | Paid | 12 | View Details → |
| Oct 4 | Widget Inc | #1026 | $5,800 | Pending | 2 | View Details → |
| Oct 3 | Design Co | #1025 | $1,200 | Paid | 18 | View Details → |
| Oct 2 | Startup XYZ | #1024 | $3,600 | Pending | 4 | View Details → |
| Oct 1 | Agency 123 | #1023 | $8,200 | Overdue | 45 | View Details → |
| Sep 30 | Marketing Pro | #1022 | $4,100 | Paid | 25 | View Details → |
| Sep 29 | Consulting LLC | #1021 | $6,700 | Overdue | 52 | View Details → |
| Sep 28 | Creative Partners | #1020 | $2,900 | Pending | 8 | View Details → |
| Sep 27 | Freelance Co | #1019 | $1,500 | Overdue | 38 | View Details → |
| Sep 26 | Slow Payer Inc | #1018 | $9,200 | Paid | 63 | View Details → |

---

## Premium Dashboard for Lead Qualification Agent:

**Key Metrics:**
1. Leads Scored: 342 (↑ 15%)
2. Hot Leads: 47 (score >80, ↑ 22%)
3. Close Rate: 32% (↑ 8%)
4. Pipeline Value: $487K (↑ 18%)

**Charts:**
1. **Lead Score Distribution** (Bar chart)
   - Buckets: 0-20 (Cold), 21-40 (Cool), 41-60 (Warm), 61-80 (Hot), 81-100 (On Fire)
   - Shows majority of leads in 41-80 range (good distribution)

2. **Conversion Funnel** (Funnel chart)
   - All Leads (342) → Qualified (189) → Contacted (124) → Proposal (68) → Closed (47)
   - Conversion rate at each stage

**AI Insights:**
- "Leads from LinkedIn convert 3x better than cold outreach. Prioritize LinkedIn sourcing."
- "Company size 50-200 employees = sweet spot (42% close rate vs 18% for <50 employees)."
- "Leads that respond within 24 hours have 5x higher close rate. Set up instant notifications."

---

## Next Step:

After Lovable generates this dashboard, move to **07-settings-billing.md** to build the account settings page.
