# Lovable Prompt Update Guide
**Date**: 2025-10-07
**Purpose**: Align all 7 Lovable prompts with actual codebase reality after first build

---

## What Changed After First Build

### ✅ What Lovable Implemented CORRECTLY:
1. **CSS Custom Properties** - Fully implemented via Tailwind's HSL system (lines 10-131 in `src/index.css`)
2. **Noise Texture** - Implemented (had syntax bug, now fixed)
3. **Indigo Glow Shadows** - Implemented in dark mode (lines 91-94)
4. **Theme System** - Uses `data-theme` attribute with localStorage persistence
5. **Sharp Corners** - `--radius: 2px` configured globally
6. **Inter Font** - Properly loaded and applied
7. **Dark Mode Default** - System preference detection working

### ⚠️ Key Differences from Prompts:
1. **Icons**: Lovable used **Lucide React** (not Heroicons)
2. **UI Framework**: Lovable used **shadcn/ui** component library
3. **Variant System**: Uses **class-variance-authority** (cva) for Button/Badge variants
4. **Transition Utility**: Created `transition-fast` class (200ms) instead of inline
5. **Color Tokens**: Uses HSL-based semantic tokens (--background, --card, --primary, etc.)
6. **Component Architecture**: Modular components with props (AgentCard, CategoryPill, ThemeToggle)

---

## Universal Find-Replace Rules

Apply these changes to **ALL 7 prompts** (01-07):

### RULE 1: Icon Library
**FIND**:
```
- Icons: Heroicons only (NO emojis)
```

**REPLACE**:
```
- Icons: Lucide React only (NO emojis)
  Reference: https://lucide.dev/icons/
  Import pattern: `import { IconName } from "lucide-react"`
```

**Examples**:
- ❌ OLD: `BanknotesIcon from Heroicons`
- ✅ NEW: `Banknote from lucide-react`
- ❌ OLD: `EnvelopeIcon`
- ✅ NEW: `Mail`
- ❌ OLD: `Cog6ToothIcon`
- ✅ NEW: `Settings`
- ❌ OLD: `ChevronRightIcon`
- ✅ NEW: `ChevronRight`

---

### RULE 2: Component Library Reference
**ADD** after "USE SAME DARK DESIGN SYSTEM:" in ALL prompts:

```
UI COMPONENTS (shadcn/ui):
- Use existing components from @/components/ui/*
- Button variants: default, ghost, outline, destructive
  Example: <Button variant="ghost">Text</Button>
- Badge variants: default, utility, premium
  Example: <Badge variant="premium">PREMIUM</Badge>
- All components support className for additional styling
- Reference existing AgentCard, CategoryPill, ThemeToggle patterns
```

---

### RULE 3: Border Radius (Global Setting)
**FIND**:
```
- Border radius: 12px
- 8px border-radius
- rounded-lg
```

**REPLACE**:
```
- Border radius: Use rounded-sm (2px everywhere, configured globally via --radius)
```

**Note**: Don't specify pixel values for border-radius. Trust the global `--radius: 2px` setting.

---

### RULE 4: Transitions (Use Utility Class)
**FIND**:
```
- 200ms transitions
- transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1)
```

**REPLACE**:
```
- Use transition-fast utility class (200ms cubic-bezier, configured globally)
  Example: className="transition-fast hover:border-primary"
```

---

### RULE 5: Color Tokens (Semantic References)
**FIND** (manual hex codes):
```
#0B0E13, #161B22, #374151, #F9FAFB, #E5E7EB, #D1D5DB, #4F46E5, #3730A3
```

**REPLACE** (semantic tokens):
```
Use Tailwind semantic classes:
- bg-background (#0B0E13 dark, #F9FAFB light)
- bg-card (#161B22 dark, #FFFFFF light)
- border-border (#374151 dark, #E5E7EB light)
- text-foreground (#F9FAFB dark, #1F2937 light)
- text-muted-foreground (#9CA3AF)
- bg-primary (#4F46E5)
- bg-primary-dark (#3730A3)
```

**Note**: These are defined in `src/index.css` lines 10-131 and automatically switch with theme.

---

### RULE 6: Agent Routing (ID Field Required)
**ADD** to any prompt showing agent data structures:

```
AGENT DATA STRUCTURE:
Each agent object must include:
- id: string (kebab-case slug for routing, e.g., "email-classifier")
- icon: LucideIcon (from lucide-react)
- name: string (display name)
- description: string
- pricing: string
- tierInfo: string
- tier: "utility" | "premium"
- category: string

Example:
{
  id: "email-classifier",
  icon: Mail,
  name: "Email Classifier",
  description: "Auto-sort emails...",
  pricing: "$29-79/month",
  tierInfo: "Status page included",
  tier: "utility" as const,
  category: "Productivity"
}
```

---

### RULE 7: Clickable Card Pattern
**FIND** (in Agent Detail, Dashboard, etc.):
```
<div className="card">
  {/* Card content */}
  <Button>View Details</Button>
</div>
```

**REPLACE**:
```
<a
  href={`/agents/${agent.id}`}
  aria-label={`View ${agent.name} details`}
  className="card cursor-pointer block"
>
  {/* Card content */}
  <Button onClick={(e) => e.stopPropagation()}>
    Request Access
  </Button>
</a>
```

**Pattern**: Entire card clickable, nested button uses `stopPropagation()` for separate action.

---

### RULE 8: Theme Toggle Implementation
**REPLACE** detailed theme toggle specs with:

```
THEME SYSTEM:
- Already implemented via ThemeToggle component
- Uses data-theme attribute on <html>
- Persists to localStorage
- Auto-detects system preference (prefers-color-scheme)
- Manual toggle available in navbar
- No need to reimplement - reference existing component
```

---

### RULE 9: Noise Texture (Already Fixed)
**REMOVE** prescriptive CSS noise texture code.

**REPLACE** with:
```
- Noise texture: Already implemented in src/index.css (lines 143-152)
- No action needed - works automatically in dark mode
```

---

### RULE 10: Form Components
**ADD** when prompts specify forms:

```
FORM COMPONENTS:
- Use shadcn/ui Input component (@/components/ui/input)
- Use shadcn/ui Select component (@/components/ui/select)
- Use shadcn/ui Checkbox component (@/components/ui/checkbox)
- All inputs: 44px height minimum (touch-friendly)
- Focus states: ring-2 ring-primary
- Error states: ring-destructive text-destructive
```

---

## Prompt-Specific Updates

### 01-homepage.md ✅ COMPLETED
**Status**: Already used for first build
**Next**: Update with learnings from actual build
**Changes needed**:
1. Switch Heroicons → Lucide React
2. Add shadcn/ui component references
3. Simplify color specifications (use semantic tokens)
4. Note that CSS vars, noise texture, theme system already work

---

### 02-agent-detail-page.md
**Specific additions**:

**ADD after "BREADCRUMB:" section**:
```
ROUTING:
- URL pattern: /agents/{agent-id} (use agent.id field, not slug)
- Example: /agents/email-classifier
- Back navigation preserves previous filter/search state
```

**UPDATE "REVIEWS SECTION:"**:
```
- Star rating: Use Rating component if available, or custom SVG stars
- NO emoji stars (⭐) - use Lucide Star icon
```

**UPDATE "FAQ ACCORDION:"**:
```
- Use shadcn/ui Collapsible component (@/components/ui/collapsible)
- Expand icon: ChevronDown from lucide-react (rotates on open)
- Transitions handled by component
```

---

### 03-dashboard.md
**Specific additions**:

**UPDATE "SIDEBAR:" section**:
```
SIDEBAR NAVIGATION:
- Use existing sidebar pattern from homepage (if applicable)
- Active state handled via React Router or similar
- Icons: lucide-react (LayoutGrid, CreditCard, Settings, etc.)
```

**UPDATE "Agent cards" structure**:
```
AGENT CARD PROPS:
- Pass full agent object with id field
- Reference AgentCard component pattern from homepage
- Cards should be clickable (wrap in <a> tag) to /dashboard/agents/{id}/status
- Action buttons use stopPropagation() pattern
```

**ADD**:
```
EMPTY STATE:
- Use Lucide icons: LayoutGrid or Inbox (64px, text-muted-foreground)
- Center using Tailwind flex utilities
- Button uses variant="default" with indigo gradient
```

---

### 04-activation-wizard.md
**Specific additions**:

**UPDATE "PROGRESS INDICATOR:"**:
```
STEP INDICATOR:
- Consider using shadcn/ui Stepper pattern (if available)
- OR custom implementation with Tailwind flex
- Completed: bg-primary text-primary-foreground
- Current: border-2 border-primary text-primary
- Future: border border-border text-muted-foreground
```

**UPDATE "STEP 1: CONNECT INTEGRATIONS"**:
```
INTEGRATION CARDS:
- Each card is a button or clickable div
- Use Card component (@/components/ui/card) as base
- Status indicator:
  * Not Connected: text-muted-foreground
  * Connected: text-green-500 with CheckCircle icon (lucide-react)
```

**UPDATE "STEP 2: CONFIGURE RULES"**:
```
FORM FIELDS:
- Checkboxes: Use Checkbox component with Label
- Dropdowns: Use Select component
- Text inputs: Use Input component
- All form components from shadcn/ui
- Validation handled via react-hook-form or similar
```

**UPDATE "STEP 3: TEST AGENT"**:
```
LOADING STATE:
- Use Lucide Loader2 icon with animate-spin
- Text: text-muted-foreground
- Consider shadcn/ui Skeleton component for placeholder content
```

**UPDATE "STEP 4: SUBSCRIBE"**:
```
TIER CARDS:
- Use Card component as base
- Badge for "Popular" tag
- Button variants match existing pattern
- Stripe integration via placeholder modal (or actual Stripe Elements)
```

---

### 05-agent-status-page.md
**Specific additions**:

**UPDATE "STATUS CARD"**:
```
STATUS INDICATOR:
- Use Lucide icons:
  * Running: CheckCircle (text-green-500)
  * Paused: PauseCircle (text-amber-500)
  * Error: XCircle (text-red-500)
- Dot indicator: 16px rounded-full with matching color
```

**UPDATE "ACTIVITY METRICS CARD"**:
```
METRICS GRID:
- Use Card as wrapper
- Icons from lucide-react (Mail, Archive, Trash, Clock, etc.)
- Number: text-4xl font-bold text-foreground
- Label: text-sm text-muted-foreground
```

**UPDATE "CONTROL PANEL CARD"**:
```
BUTTONS:
- Use Button component with variant="outline"
- Icons from lucide-react (Pause, Settings, Clock, Link)
- All buttons same height (h-10 or size="default")
```

**UPDATE "ACTIVITY LOG"**:
```
TABLE:
- Use Table component (@/components/ui/table)
- OR custom table with TableHead, TableBody, TableRow, TableCell
- Zebra striping handled by component
```

---

### 06-premium-dashboard.md
**Specific additions**:

**UPDATE "CHARTS SECTION"**:
```
CHARTS:
- Use shadcn/ui Chart component (@/components/ui/chart) if available
- OR integrate Recharts library (common with shadcn)
- Line chart: <LineChart>, <Line>, <XAxis>, <YAxis>, <Tooltip>
- Bar chart: <BarChart>, <Bar>
- Colors: use CSS custom properties (hsl(var(--primary)))
```

**UPDATE "INSIGHTS CARD"**:
```
AI INSIGHTS:
- Icon: Sparkles from lucide-react
- List items use Lucide Lightbulb icon
- Text: text-muted-foreground for insights
```

---

### 07-settings-billing.md
**Specific additions**:

**UPDATE "TAB NAVIGATION"**:
```
TABS:
- Use shadcn/ui Tabs component (@/components/ui/tabs)
- <Tabs>, <TabsList>, <TabsTrigger>, <TabsContent>
- Active state handled by component
```

**UPDATE "PROFILE" tab**:
```
PROFILE PICTURE:
- Use Avatar component (@/components/ui/avatar)
- Upload handled via file input or drag-drop
```

**UPDATE "BILLING" tab**:
```
PAYMENT METHOD CARD:
- Icons for card types: CreditCard from lucide-react
- Use Card component as base
- Buttons for update/remove use appropriate variants
```

**UPDATE "BILLING HISTORY"**:
```
INVOICES TABLE:
- Use Table component
- Download link uses Lucide Download icon
- Status badge uses Badge component (variant based on status)
```

---

## Summary of Changes

### Global Changes (All 7 Prompts):
1. ✅ Heroicons → Lucide React
2. ✅ Add shadcn/ui component references
3. ✅ Use semantic color tokens instead of hex codes
4. ✅ Reference `transition-fast` utility
5. ✅ Specify `rounded-sm` for border radius
6. ✅ Reference existing theme system
7. ✅ Add `id` field requirement for agents
8. ✅ Reference clickable card pattern where applicable

### Prompt-Specific Changes:
- **01-homepage**: Update with actual build learnings
- **02-agent-detail**: Add routing pattern, update icons
- **03-dashboard**: Reference AgentCard pattern, update sidebar
- **04-activation-wizard**: Update form components, stepper
- **05-agent-status**: Update status indicators, table component
- **06-premium-dashboard**: Add chart component references
- **07-settings-billing**: Update tabs, form components

---

## Implementation Order

1. **First**: Update 01-homepage.md with learnings ✅
2. **Then**: Batch update all 7 prompts with global find-replace rules
3. **Finally**: Add prompt-specific enhancements individually

**Estimated time**: ~2 hours to systematically update all prompts

---

## Verification Checklist

After updates, each prompt should:
- [ ] Use "Lucide React" not "Heroicons"
- [ ] Reference shadcn/ui components
- [ ] Use semantic color tokens (bg-background, text-foreground, etc.)
- [ ] Mention `transition-fast` utility
- [ ] Use `rounded-sm` for border radius
- [ ] Reference existing theme system (data-theme attribute)
- [ ] Include `id` field in agent data structures
- [ ] Use clickable card pattern where cards navigate
- [ ] Avoid prescriptive pixel values where components handle it
- [ ] Match tone and structure of successful 01-homepage.md build

---

**End of Update Guide**
