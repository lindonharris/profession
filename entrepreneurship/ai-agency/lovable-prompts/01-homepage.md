# Lovable Prompt: Homepage (Main Landing Page)

**Phase:** 1 - MVP Launch
**Page:** Homepage
**URL:** `/`
**Build Order:** 1 of 7

---

## Copy-Paste This Into Lovable:

```
Create a dark, exclusive marketplace homepage for buyanagent.ai - underground but legitimate premium SaaS.

PRIMARY DESIGN REFERENCE: Linear.app
Study Linear.app (linear.app) as the PRIMARY visual and interaction model. This is the aesthetic foundation.

WHY LINEAR:
- Sharp, minimal border radius (2-3px max) creates technical precision
- Dark mode executed with sophistication (not gimmicky)
- Typography hierarchy is clear without being loud (Inter font, restrained sizing)
- Shadows are subtle and purposeful (depth without drama)
- Spacing breathes without wasting space (tight but not cramped)
- Interactive states are smooth but fast (200ms transitions, not slow)
- Color palette is restrained (few accent colors, mostly grayscale + one primary)
- Components feel modular and systematic (design system thinking)
- Overall vibe: Professional tool for serious work, not a consumer app

APPLY LINEAR'S PRINCIPLES TO:
- Border radius strategy: 2px everywhere (match Linear's sharp aesthetic)
- Card design: Clean elevation, subtle borders, minimal shadows
- Typography scale: Don't go too big or too playful
- Button styles: Solid primary actions, ghost secondary actions
- Navigation: Clean, horizontal, minimal chrome
- Spacing system: Consistent, not arbitrary
- Color restraint: Indigo gradient is our ONLY decorative color (like Linear's purple)

SECONDARY REFERENCES (for specific elements):
- Vercel's dark mode for sophisticated navy-black backgrounds
- Raycast's marketplace for product grid layout inspiration

AVOID:
- Stripe's friendly rounded corners (too soft, too consumer)
- Framer's animated gradients (too flashy, too marketing-y)
- Notion's playful illustrations (wrong tone)

UI COMPONENTS (shadcn/ui):
- Use shadcn/ui component library from @/components/ui/*
- Button variants: default (indigo gradient), ghost, outline, destructive
  Example: <Button variant="ghost">Text</Button>
- Badge variants: default, utility, premium
  Example: <Badge variant="premium">PREMIUM</Badge>
- Reference existing components: AgentCard, CategoryPill, ThemeToggle
- All components support className for additional Tailwind styling

ARCHITECTURE:
- Build modular components with configurable props using class-variance-authority (cva)
- CSS custom properties already implemented via Tailwind's HSL system (see src/index.css)
- Auto-detect system theme (prefers-color-scheme) with manual toggle
- Light mode: Off-white #F9FAFB bg, dark text
- Dark mode (default): Navy-black #0B0E13 bg, off-white text
- Theme toggle persists to localStorage, applies via data-theme attribute
- Noise texture already implemented and working in dark mode

DESIGN LANGUAGE:
- Border radius: 2px everywhere via rounded-sm (sharp, technical aesthetic)
- Typography: Inter font family
- Icons: Lucide React only (NO emojis)
  Reference: https://lucide.dev/icons/
  Import pattern: `import { IconName } from "lucide-react"`
- Indigo gradient: #4F46E5 → #3730A3 (stays same in both modes)
- Transitions: Use transition-fast utility class (200ms cubic-bezier)
- Vibe: "Underground marketplace with tech legitimacy"

DARK MODE COLORS:
- Background: Navy-black #0B0E13 with 2% noise texture
- Cards: #161B22, border #374151
- Text: #F9FAFB (primary), #E5E7EB (secondary), #D1D5DB (tertiary)
- Shadows: Dark with subtle indigo glow

LIGHT MODE COLORS:
- Background: Off-white #F9FAFB
- Cards: White #FFFFFF, border #E5E7EB
- Text: #1F2937 (primary), #374151 (secondary), #6B7280 (tertiary)
- Shadows: Subtle, no glow

NAVBAR:
- Logo: "buyanagent.ai" with indigo gradient text
- Links: "Browse", "Pricing", "Docs"
- CTA: "Request Access" button (variant="default")
- Theme toggle: Sun/Moon icons from lucide-react

HERO:
- Headline: "Pre-Built AI Agents. Activate in 1 Click."
- Subheadline: "Stop spending 10 hours building automations in Zapier. Buy them pre-built from us."
- CTA: "Request Access"
- Trust badge: "247 members"

CATEGORY FILTER:
- Pills: "All (9)", "Productivity (9)", "Finance (5)", "Marketing (5)", "Operations (3)"
  Note: Use dynamic count (agents.length) not hardcoded numbers
- Use Lucide icons for categories (Layers, Zap, DollarSign, TrendingUp, Settings)
- Active state with indigo background (bg-primary)
- Reference CategoryPill component pattern

AGENT GRID:
- 3 columns desktop, 2 tablet, 1 mobile
- Each agent MUST include id field for routing (kebab-case, e.g., "email-classifier")
- Cards are fully clickable (<a href="/agents/{id}"> wrapper)
- Each card shows:
  1. Tier badge (top-right): <Badge variant="utility"> or <Badge variant="premium">
  2. Agent icon (Lucide icon, 48px, e.g., Mail, Calendar, MessageSquare)
  3. Agent name
  4. Description (3 lines max with line-clamp-3)
  5. Pricing: "$29-79/month" or "From $100/month"
  6. Tier info: "Status page included" or "Dashboard + Analytics"
  7. "Request Access" button (uses stopPropagation() for separate action)
- Hover: lift card (-translate-y-1), indigo border (border-primary), enhanced shadow
- Reference AgentCard component pattern

FOOTER:
- Three columns: "Product", "Company", "Resources"
- Copyright: "© 2025 buyanagent.ai • Terms • Privacy"

COMPONENT EXAMPLES:
- <Button variant="default|ghost|outline|destructive" size="sm|default|lg" />
- <Badge variant="utility|premium" />
- <AgentCard {...agentProps} />
- <CategoryPill icon={Icon} label="Category" count={5} active={bool} />
- <ThemeToggle />

AGENT DATA STRUCTURE (Required):
Each agent object must include:
{
  id: "email-classifier",              // kebab-case for routing
  icon: Mail,                           // Lucide icon component
  name: "Email Classifier",             // display name
  description: "Auto-sort emails...",   // 2-3 sentences
  pricing: "$29-79/month",              // pricing display
  tierInfo: "Status page included",     // tier features
  tier: "utility" as const,             // "utility" | "premium"
  category: "Productivity"              // for filtering
}

CSS CUSTOM PROPERTIES (Already Implemented):
- Located in src/index.css lines 10-131
- Uses Tailwind's HSL-based semantic tokens
- Theme switching via [data-theme="light|dark"] attribute
- Auto-detection via @media (prefers-color-scheme: dark)
- No need to reimplement - use semantic classes:
  * bg-background, bg-card, bg-primary
  * text-foreground, text-muted-foreground
  * border-border
  * All colors auto-switch with theme

Use Tailwind CSS, fully responsive, transition-fast utility for all animations.
```

---

## Sample Agent Data:

**Agent 1: Email Classifier (Utility)**
- ID: email-classifier
- Icon: Mail (lucide-react)
- Name: Email Classifier
- Description: Auto-sort emails by priority, sender type, and urgency. Never miss important messages buried in noise.
- Pricing: $29-79/month
- Tier Info: Status page included
- Tier: utility
- Category: Productivity

**Agent 2: Meeting Scheduler Pro (Premium)**
- ID: meeting-scheduler-pro
- Icon: Calendar (lucide-react)
- Name: Meeting Scheduler Pro
- Description: AI coordinates across timezones, finds optimal slots, sends invites. Works with Google Calendar, Outlook, and Calendly.
- Pricing: From $100/month
- Tier Info: Dashboard + Analytics
- Tier: premium
- Category: Productivity

**Agent 3: Support Ticket Router (Utility)**
- ID: support-ticket-router
- Icon: MessageSquare (lucide-react)
- Name: Support Ticket Router
- Description: Routes customer support tickets to the right team member based on content, urgency, and expertise.
- Pricing: $29-79/month
- Tier Info: Status page included
- Tier: utility
- Category: Operations

Note: Reference existing agents array in src/pages/Index.tsx for more examples

---

## Navigation FROM This Page:

- "Request Access" button → Request Access Modal (name + email form)
- Agent cards → Individual Agent Detail Pages (02-agent-detail-page.md)
- "Browse" nav link → Scrolls to agent grid (same page)
- "Pricing", "Docs" → External/future pages
- Theme toggle → Switches between light/dark mode (persisted to localStorage)

---

## Technical Notes:

**Theme System:**
- Detects system preference with `window.matchMedia('(prefers-color-scheme: dark)')`
- Manual override via SunIcon/MoonIcon button
- Persists to localStorage as `theme: "light" | "dark"`
- Applies via `data-theme` attribute on `<html>` element

**Border Radius:**
- 2px for all UI elements (cards, buttons, inputs, badges)
- Creates sharp, technical aesthetic
- Only avatars/profile images use rounded-full

**CSS Variables:**
- All theme colors as CSS custom properties
- Enables easy theme switching and future customization
- Both auto (prefers-color-scheme) and manual ([data-theme]) variants

---

## Next Step:

After Lovable generates homepage, move to **02-agent-detail-page.md**
