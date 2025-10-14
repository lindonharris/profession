# Lovable Prompt: Agent Status Page (Utility Tier Interface)

**Phase:** 1 - MVP Launch
**Page:** Agent Status Page
**URL:** `/dashboard/agents/{agent-id}/status`
**Build Order:** 5 of 7

---

## Copy-Paste This Into Lovable:

```
I need a simple status page for Utility tier agents. This is what users see when they click on an agent from their dashboard.

Think of it like a home security app - you just want to know "is it working?" and see basic activity. No fancy charts, just clear status and simple controls.

Use the same sidebar navigation from the dashboard page.

**Top of page:**
- "← Back to Dashboard" link
- Agent icon and name with tier badge
- Current status with a colored indicator:
  - Running: green checkmark
  - Paused: yellow pause icon
  - Error: red X icon
- When it last ran or when it runs next

**Activity summary card:**
Simple 2x2 grid showing key metrics from the last 7 days.

For Email Sweeper, show:
- 47 Emails processed
- 23 Archived
- 12 Unsubscribed
- 8 Deleted

Just big numbers with small labels. Use icons from Lucide React to make it visual.

**Control panel card:**
Two sections:

1. Essential controls (every agent has these):
   - Pause Agent button
   - Settings button
   - History button
   - Manage Integrations button

2. Agent-specific controls (unique to each agent type):

   For Email Sweeper example:
   - "Manage VIP Senders" button (whitelist certain emails)
   - Dropdown for noise filter sensitivity (Low/Medium/High)
   - Dropdown for action preferences (Unsubscribe vs Delete vs Archive priority)
   - "Download Activity Report" button
   - Dropdown for scan frequency (Every 1hr/2hr/4hr/Daily)

**Recent activity table:**
Simple table showing last 10 actions.

Columns: Time | What it did | Details

Example rows:
- "2 min ago | Archived | Newsletter from TechCrunch"
- "15 min ago | Unsubscribed | Promotional email from Amazon"
- "1 hour ago | Deleted | Spam from unknown sender"

Add "View All →" link at bottom.

**Design notes:**
- Use the same sidebar from dashboard
- Use Card component for each section
- Use Table component from shadcn/ui for activity log
- Icons from Lucide React (CheckCircle, PauseCircle, Settings, Clock, etc.)
- Keep it simple - this is NOT the Premium dashboard
- Metrics should stack to 1 column on mobile
```

---

## Sample Data for Email Sweeper:

**Status:**
- Current: Running (green checkmark)
- Last run: 2 minutes ago
- Next run: In 58 minutes

**Activity Metrics (Last 7 Days):**
- 47 Emails processed
- 23 Archived
- 12 Unsubscribed
- 8 Deleted

**Agent-Specific Controls:**
- VIP Senders: Gmail Team, PayPal, Bank notifications
- Noise Filter: Medium
- Primary Action: Archive
- Scan Frequency: Every 1 hour

**Recent Activity:**
1. 2 min ago | Archived | Newsletter from TechCrunch
2. 15 min ago | Unsubscribed | Promotional email from Amazon
3. 1 hour ago | Deleted | Spam from unknown sender
4. 1 hour ago | Archived | Weekly digest from Substack
5. 2 hours ago | Archived | GitHub notification

---

## Next Step:

After Lovable generates this page, move to **06-premium-dashboard.md** to build the Premium tier analytics interface.
