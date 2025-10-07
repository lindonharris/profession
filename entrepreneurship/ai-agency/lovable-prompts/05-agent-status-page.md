# Lovable Prompt: Agent Status Page (Utility Tier Interface)

**Phase:** 1 - MVP Launch
**Page:** Agent Status Page
**URL:** `/dashboard/agents/{agent-id}/status`
**Build Order:** 5 of 7

---

## Copy-Paste This Into Lovable:

```
Create a simple status page for monitoring a Utility tier AI agent (buyanagent.ai).

REFERENCE EXISTING CODEBASE:
- Same design system and components from dashboard
- Icons: Lucide React (CheckCircle, PauseCircle, XCircle, Settings, etc.)
- Use Card, Button, Table components from shadcn/ui
- Same navbar and sidebar from dashboard

LAYOUT:
- Sidebar (240px, #161B22 background, same as Dashboard)
- Main content area (remaining width, #0B0E13 background)

PAGE HEADER:
- Back button: "← Back to Dashboard" (#9CA3AF, hover #4F46E5, 14px)
- Agent title row: Heroicon (48px, #4F46E5) + Agent name (Inter Bold 32px, #F9FAFB) + Tier badge ("UTILITY", #374151 bg, #9CA3AF text)
- Subtitle: "Status page" (16px, #9CA3AF)
- Padding: 32px top/bottom

STATUS CARD (use Card component):
- Title (text-xl font-bold)
- Status with Lucide icons:
  • Running: <CheckCircle className="text-green-500" />
  • Paused: <PauseCircle className="text-amber-500" />
  • Error: <XCircle className="text-red-500" />
- Last/next run times (text-sm text-muted-foreground)

ACTIVITY METRICS CARD:
- Background: #161B22, 24px padding, below status card, 24px margin-top, #374151 border
- Title: "Activity (Last 7 Days)" (Inter Bold 20px, #F9FAFB)
- Simple metrics grid (2x2 on desktop, 1 column on mobile):
  Each metric:
  - Big number (Inter Bold 36px, #F9FAFB): "47"
  - Label below (14px, #9CA3AF): "Emails processed"
  - Heroicon above number (24px, #6B7280)
- Example metrics for Email Sweeper:
  • 47 Emails processed (EnvelopeIcon)
  • 23 Archived (ArchiveBoxIcon)
  • 12 Unsubscribed (XCircleIcon)
  • 8 Deleted (TrashIcon)
- All in simple card with #1F2937 background, 16px padding, 8px border-radius

CONTROL PANEL CARD (use Card component):
- Title (text-xl font-bold)
- Separator from shadcn/ui

- Essential Controls:
  Buttons with Lucide icons:
  • <Button variant="outline"><Pause /> Pause Agent</Button>
  • <Button variant="outline"><Settings /> Settings</Button>
  • <Button variant="outline"><Clock /> History</Button>
  • <Button variant="outline"><Link /> Integrations</Button>

- Divider (#374151, 24px margin top/bottom)

- Agent-Specific Controls section:
  Title: "Email Sweeper Controls" (Inter Medium 16px, #E5E7EB, margin-bottom 16px)

  Example controls for Email Sweeper:
  • "Manage VIP Senders" (outline button with StarIcon from Heroicons, no emoji)
  • "Noise Filter Sensitivity" (dropdown: Low/Medium/High, 44px height, #1F2937 bg, #374151 border)
  • "Action Preferences" (dropdown: Unsubscribe/Delete/Archive priority)
  • "Download Activity Report" (outline button, ArrowDownTrayIcon)
  • "Scan Frequency" (dropdown: Every 1hr/2hr/4hr/Daily)

  Layout: Stack vertically, 12px gap between items
  Labels: 14px, #E5E7EB, margin-bottom 8px
  Dropdowns: #1F2937 background, #374151 border, #F9FAFB text

- Divider (#374151)

- Quick Actions section:
  Title: "Quick Actions" (Inter Medium 16px, #E5E7EB, margin 16px top/bottom)
  Buttons:
  • "[+ Add VIP Sender]" (outline, PlusIcon from Heroicons)
  • "Adjust Filters" (outline)
  • "View Full Log" (outline)

ACTIVITY LOG (use Table component from shadcn/ui):
- Title (text-xl font-bold)
- <Table> with <TableHead>, <TableBody>, <TableRow>, <TableCell>
- Columns: Time | Action | Details
- Zebra striping handled by component
- "View All →" link (text-primary hover:underline)

RESPONSIVE:
- Metrics grid: 2x2 on desktop → 1 column on mobile
- Control panel buttons: horizontal on desktop → stack on mobile
- All cards full width, proper padding maintained

Use Tailwind CSS, add loading states (pulse animation), maintain consistency with dark dashboard design.
```

---

## Sample Control Panels by Agent:

### **Email Sweeper (Utility)**

Agent-Specific Controls:
1. **Manage VIP Senders** (button with StarIcon)
   - Opens modal with list of whitelisted senders
   - Add/remove email addresses

2. **Noise Filter Sensitivity** (dropdown)
   - Options: Low (keeps more), Medium (balanced), High (aggressive)
   - Default: Medium

3. **Action Preferences** (dropdown)
   - Options: Prioritize Unsubscribe, Prioritize Archive, Prioritize Delete
   - Default: Prioritize Unsubscribe

4. **Download Activity Report** (button with ArrowDownTrayIcon)
   - Downloads CSV with all processed emails

5. **Scan Frequency** (dropdown)
   - Options: Every 1 hour, Every 2 hours, Every 4 hours, Daily
   - Default: Every 2 hours

---

### **Expense Manager (Utility)**

Agent-Specific Controls:
1. **Manage Categories** (button with FolderIcon)
   - Opens modal to add/edit/delete expense categories

2. **Category Rules** (button with AdjustmentsHorizontalIcon)
   - Opens modal to set auto-categorization rules
   - Example: "Starbucks → Meals"

3. **Select Google Sheet** (dropdown)
   - Shows list of user's Google Sheets
   - Change destination sheet

4. **Scan Frequency** (dropdown)
   - Options: Real-time, Hourly, Daily
   - Default: Hourly

5. **Download Expense Report** (button with ArrowDownTrayIcon)
   - Downloads CSV of all expenses

---

### **Newsletter Digester (Utility)**

Agent-Specific Controls:
1. **Manage Subscriptions** (button with NewspaperIcon)
   - List of all detected newsletters
   - Pause/resume individual newsletters

2. **Digest Schedule** (dropdown)
   - Options: Daily (8am), Daily (6pm), Weekly (Monday 8am)
   - Default: Daily (8am)

3. **Summary Length** (dropdown)
   - Options: Brief (1-2 points), Medium (3-5 points), Detailed (5-7 points)
   - Default: Medium

4. **Scan Frequency** (dropdown)
   - Options: Every 2 hours, Daily, Manual only
   - Default: Daily

5. **Download Digest Archive** (button with ArrowDownTrayIcon)
   - Downloads all past digests

---

## Sample Activity Metrics by Agent:

### **Email Sweeper:**
- Emails processed: 47
- Archived: 23
- Unsubscribed: 12
- Deleted: 8

### **Expense Manager:**
- Receipts scanned: 15
- Expenses logged: 15
- Total amount: $1,247.50
- Categories: 6

### **Newsletter Digester:**
- Newsletters tracked: 18
- Summaries generated: 126
- Digests sent: 18
- Time saved: 4.2 hours

---

## This Completes Phase 1!

**Phase 1 Summary:**
✅ 5 pages built (Homepage, Agent Detail, Dashboard, Activation Wizard, Status Page)
✅ Complete MVP user journey
✅ Ready to launch Utility tier

**Next:** Phase 2 prompts (Premium Dashboard + Settings)
