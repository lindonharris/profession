# Lovable Prompt: Activation Wizard (5-Step Flow)

**Phase:** 1 - MVP Launch
**Page:** Activation Wizard
**URL:** `/activate/{agent-slug}`
**Build Order:** 4 of 7

---

## Copy-Paste This Into Lovable:

```
Create a multi-step activation wizard for purchasing and setting up an AI agent (buyanagent.ai).

REFERENCE EXISTING CODEBASE:
- Same design system from homepage (see src/index.css)
- Components: Button, Card, Input, Select, Checkbox from shadcn/ui
- Icons: Lucide React only (NO emojis)
- Use transition-fast utility
- Use rounded-sm for borders
- Success: text-green-500 / bg-green-500
- Same navbar (minimal - just logo)

LAYOUT:
- Background: #0B0E13
- Centered container (max-width 800px)
- Progress indicator at top showing 5 steps
- Main content area (#161B22 card, 32px padding, shadow-lg with indigo glow)
- Navigation buttons at bottom (Back + Next/Continue)

PROGRESS INDICATOR:
- 5 step circles horizontally aligned
- Completed: bg-primary text-primary-foreground
- Current: border-2 border-primary text-primary
- Future: border border-border text-muted-foreground
- Connecting lines: border-border (completed: border-primary)

STEP 1: CONNECT INTEGRATIONS
- Title (text-2xl font-bold)
- Subtitle (text-muted-foreground)
- Integration cards (grid, use Card component):
  - Service logo (48px)
  - Service name (font-semibold text-lg)
  - Purpose (text-sm text-muted-foreground)
  - Status: "Not Connected" or <CheckCircle className="text-green-500" />
  - <Button variant="default">Connect →</Button> or <Button variant="outline">Reconnect</Button>
- Example: Gmail, Google Sheets
- Next button disabled until all connected

STEP 2: CONFIGURE RULES
- Title (text-2xl font-bold)
- Subtitle (text-muted-foreground)
- Form fields (use shadcn/ui components):
  • <Checkbox /> for categories
  • <Select /> for dropdowns
  • <Input /> for text fields
- All form components from @/components/ui/*
- Validation handled by component state
- Error messages: text-destructive

STEP 3: TEST AGENT
- Title (text-2xl font-bold)
- Subtitle (text-muted-foreground)
- Loading: <Loader2 className="animate-spin text-primary" /> + "Testing agent..."
- Success state:
  • <CheckCircle className="h-12 w-12 text-green-500" />
  • "✓ Test successful!" (text-xl font-semibold text-green-500)
  • Results in Card component (text-muted-foreground)
  • <Button variant="default">Looks good!</Button>
- Error state: <XCircle className="text-destructive" /> + error + <Button variant="outline">Try Again</Button>

STEP 4: SUBSCRIBE
- Title (text-2xl font-bold)
- Two tier cards side-by-side (use Card component):

  UTILITY: bg-card border-border with <Badge variant="utility">
  PREMIUM: bg-card border-2 border-primary with <Badge variant="premium">

  Each card shows:
  - Header with tier name
  - Price (text-3xl font-bold text-primary)
  - Features list (text-muted-foreground)
  - <Button> for selection

- Stripe integration via modal
- Note about charging (text-xs text-muted-foreground italic)

STEP 5: SUCCESS
- <CheckCircle className="h-16 w-16 text-green-500" />
- Title: "🎉 Agent is Live!" (text-3xl font-bold)
- Message (text-lg text-muted-foreground max-w-2xl)
- <Button variant="default">Go to Dashboard →</Button>
- <Button variant="outline">Activate Another Agent</Button>

BOTTOM NAVIGATION:
- "← Back" button (outline, left side, #E5E7EB text, #374151 border) - disabled on Step 1
- "Continue →" or "Next Step →" button (indigo gradient #4F46E5 → #3730A3, right side, #F9FAFB text)
- On Step 4, button says "Complete Setup"
- Center-aligned on mobile

Use Tailwind CSS, add form validation, smooth step transitions (fade in/out), maintain dark design consistency.
```

---

## Sample Activation Flow for Expense Manager:

**Step 1: Connect Integrations**

Integration cards:
1. **Gmail**
   - Logo: Gmail icon (48px)
   - Purpose: "For scanning email receipts"
   - Status: Not Connected
   - Button: "Connect Gmail →"

2. **Google Sheets**
   - Logo: Google Sheets icon (48px)
   - Purpose: "For logging expenses"
   - Status: Not Connected
   - Button: "Connect Google Sheets →"

**Step 2: Configure Rules**

Form fields:
1. **Expense Categories** (checkboxes)
   - [ ] Travel
   - [ ] Meals & Entertainment
   - [ ] Office Supplies
   - [ ] Software & Tools
   - [ ] Professional Services
   - [ ] Other

2. **Notification Frequency** (dropdown)
   - Options: Real-time, Daily, Weekly, Monthly
   - Default: Daily

3. **Google Sheet URL** (text input)
   - Placeholder: "https://docs.google.com/spreadsheets/d/..."
   - Validation: Must be valid Google Sheets URL

4. **Auto-categorization** (toggle switch)
   - Label: "Let AI automatically categorize expenses"
   - Default: ON

**Step 3: Test Agent**

Test results box example:
```
✓ Test successful!

Found 1 receipt in your Gmail:
- Vendor: Starbucks
- Amount: $42.50
- Date: Today, 10:42 AM
- Auto-categorized as: Meals & Entertainment

This expense has been logged to your Google Sheet.
```

**Step 4: Subscribe**

For Expense Manager, show Utility tier only (no Premium option):

**Utility Tier Card:**
- Price: $69/month
- Features:
  • Status page
  • Unlimited receipt scans
  • Auto-categorization
  • Email support
  • Google Sheets integration

No tier comparison needed (Utility only agent).

**Step 5: Success**

Message:
"Your Expense Manager is now running in the background. Every time you receive an email receipt, it will automatically extract the details and log them to your Google Sheet. Check your dashboard to see activity."

---

## Next Step:

After Lovable generates this wizard, move to **05-agent-status-page.md** to build the Utility tier interface.
