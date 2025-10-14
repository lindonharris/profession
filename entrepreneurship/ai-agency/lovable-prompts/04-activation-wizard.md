# Lovable Prompt: Activation Wizard (5-Step Flow)

**Phase:** 1 - MVP Launch
**Page:** Activation Wizard
**URL:** `/activate/{agent-slug}`
**Build Order:** 4 of 7

---

## Copy-Paste This Into Lovable:

```
I need a multi-step wizard that walks users through activating an AI agent after they purchase it. Think of how Stripe onboarding works - clear progress, one step at a time, can't proceed until current step is complete.

This should feel smooth and reassuring - like "we've got you, just follow these 5 simple steps."

Use the same dark theme and components from our other pages.

**Progress indicator at top:**
Show 5 steps with circles connected by lines. Completed steps are filled with indigo, current step has an indigo border, future steps are gray. As they move forward, the connecting lines turn indigo too.

**Step 1: Connect Integrations**
Show cards for each service they need to connect (like Gmail, Google Sheets, QuickBooks, etc.)

Each card shows:
- Service logo/icon
- Service name
- Why we need it ("For scanning email receipts")
- Connection status (either "Not Connected" or a green checkmark)
- "Connect" button (opens OAuth in popup)

The "Next" button stays disabled until all required integrations are connected.

**Step 2: Configure Rules**
This is where they set up how the agent should work. Use form components from shadcn/ui.

For example, for Expense Manager:
- Checkboxes to select expense categories (Travel, Meals, Software, etc.)
- Dropdown for how often they want notifications
- Text input for their Google Sheet URL
- Toggle switch for auto-categorization

Show validation errors in red if they miss required fields.

**Step 3: Test Agent**
Run a test to make sure everything works before going live.

Show a loading spinner (use Loader2 from Lucide React with spin animation) with "Testing agent..." text.

Then show results in a card:
- Green checkmark icon if successful
- What the test found (like "Found 1 receipt from Starbucks for $42.50")
- "Looks good!" button to continue

If test fails, show error message with "Try Again" button.

**Step 4: Subscribe**
Show the pricing tier options side by side (only if agent has multiple tiers).

For Utility-only agents, just show the one tier.
For Premium agents, show both Utility and Premium cards with the Premium one highlighted.

Each card shows price, features list, and a button to select that tier.

When they click, open Stripe checkout modal (we'll integrate this later, for now just simulate it).

**Step 5: Success!**
Big celebration screen:
- Large green checkmark icon
- "🎉 Agent is Live!" heading
- Explanation of what happens next
- "Go to Dashboard" button (primary)
- "Activate Another Agent" button (secondary)

**Navigation:**
- "Back" button on left (disabled on step 1)
- "Continue" or "Next Step" button on right
- On step 4, button says "Complete Setup"
- Buttons stack on mobile

**Design notes:**
- Use Card, Button, Input, Select, Checkbox components from shadcn/ui
- Use Loader2 and CheckCircle icons from Lucide React
- Green for success states (text-green-500)
- Smooth fade transitions between steps
- Center the whole wizard (max-width 800px)
- Add subtle indigo glow to the main card
```

---

## Sample Activation Flow for Expense Manager:

**Step 1: Connect Integrations**

Integration cards:
1. **Gmail**
   - Icon: Mail (Lucide React)
   - Purpose: "For scanning email receipts"
   - Status: Not Connected
   - Button: "Connect Gmail →"

2. **Google Sheets**
   - Icon: Sheet icon placeholder
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

Test results example:
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

For Expense Manager (Utility tier only):
- Price: $69/month
- Features:
  • Status page
  • Unlimited receipt scans
  • Auto-categorization
  • Email support
  • Google Sheets integration

**Step 5: Success**

Message:
"Your Expense Manager is now running in the background. Every time you receive an email receipt, it will automatically extract the details and log them to your Google Sheet. Check your dashboard to see activity."

---

## Next Step:

After Lovable generates this wizard, move to **05-agent-status-page.md** to build the Utility tier interface.
