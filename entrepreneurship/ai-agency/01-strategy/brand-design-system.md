# buyanagent.ai - Brand & Design System

**Last Updated:** October 6, 2025 (v1.0)
**Purpose:** Source of truth for all brand, design, and UI decisions
**Status:** Production-Ready

---

## 🎨 Brand Identity

### Core Positioning

**Tagline:** "Pre-Built AI Agents. Activate in 1 Click."

**Brand Promise:**
- Zapier forces you to build. We sell it pre-built.
- 20-40x faster time to value (15-40 min activation vs 10+ hours building)
- Zero learning curve, zero complexity

**Brand Personality:**
1. **Approachable** - Not intimidating (unlike n8n/Zapier developer tools)
2. **Fast** - Instant clarity on what each agent does
3. **Trustworthy** - Social proof, clear pricing, no hidden fees
4. **Delightful** - Smooth animations, micro-interactions
5. **Democratic** - Automation for everyone, not just techies

**NOT:**
- ❌ Developer tool (avoid technical jargon)
- ❌ Complex automation platform (we're simple)
- ❌ All-in-one bloated suite (we're focused)

---

## 🎨 Visual Identity

### Design Philosophy

**"Underground Marketplace with Tech Legitimacy"**
- Dark, exclusive, sophisticated
- Professional + clean + hidden gem aesthetic
- Insider knowledge feeling, totally legitimate
- Premium SaaS with "you found something special" vibe

**NOT "Shopify meets Stripe"** - That's light mode thinking. We're darker, more exclusive.

---

### Aesthetic Overview (For Lovable Prompts)

**Visual Language:**

buyanagent.ai feels like discovering a secret marketplace that insiders know about - dark, sophisticated, and completely legitimate. The site uses a deep navy-black background (`#0B0E13`) that creates an exclusive, premium atmosphere. Elevated dark cards (`#161B22`) float above the background with subtle indigo glows, giving depth without being flashy.

The brand color is a monochromatic indigo gradient (`#4F46E5 → #3730A3`) - professional blue-purple that signals tech credibility and restraint. Unlike bright, saturated purples, this indigo feels mature and intentional. It appears on CTAs, interactive elements, and subtle glows around cards on hover.

Typography is clean off-white (`#F9FAFB`) for maximum readability on dark, with subtle hierarchy through barely-dimmed grays. The overall vibe is "you found something special that few people know about" - exclusive but welcoming, mysterious but trustworthy, underground but completely professional.

**Key Feelings:**
- **First impression:** "This isn't like other SaaS tools - it feels premium"
- **Interaction:** "Everything is smooth, intentional, and glows subtly when I hover"
- **Trust:** "Dark aesthetic but clearly legitimate - tech-forward, not sketchy"
- **Access:** "Request Access" feels exclusive, but approval is instant (psychological exclusivity)

**Design Restraint:**
- No flashy animations - just smooth 200ms transitions
- No bright colors except feedback states (green/red/amber for status)
- No technical jargon - plain English throughout
- No complexity - clean, spacious layout with generous breathing room (80px section spacing)

Think: High-end headphones site meets developer tool meets secret club. Dark, cool, confident.

### Core Color Foundation

**Background:**
- Page background: `#0B0E13` (Navy-black - custom blend between charcoal and navy)
- Elevated surfaces: `#161B22` (Slightly lighter - card backgrounds)

**Primary Gradient:**
- Indigo gradient: `#4F46E5 → #3730A3` (Monochromatic indigo, light to dark)
- Use for: CTAs, headlines, active states, brand elements
- **Philosophy:** Subtle depth, sophisticated restraint, tech credibility

**Text:**
- Primary: `#F9FAFB` (Off-white - excellent readability)
- Secondary: `#E5E7EB` (Barely dimmer - subtle hierarchy)
- Subtle/metadata: `#D1D5DB` (Still quite light - accessible)

### Extended Color Palette

**Neutrals (Cool Gray Scale):**
- Surface: `#1F2937` (Card backgrounds, elevated elements)
- Borders: `#374151` (Subtle separation)
- Secondary text: `#6B7280` (De-emphasized content)
- Disabled/placeholder: `#9CA3AF` (Inactive states)

**Feedback Colors:**
- Success: `#10B981` (Bright green - agent running, form success)
- Error: `#EF4444` (Bright red - agent error, validation failure)
- Warning: `#F59E0B` (Bright yellow/amber - alerts, paused states)

**Tier-Specific:**
- Utility tier badge: `#374151` background, `#D1D5DB` text (neutral gray)
- Premium tier badge: `#4F46E5` background, `#F9FAFB` text (indigo brand color)

---

### Typography

**Font Family:** Inter (Google Fonts)
- Clean, modern sans-serif
- Excellent readability at all sizes
- Professional without being corporate

**Type Scale:**

**Headlines:**
- H1: Inter Bold, 48px, line-height 1.2
- H2: Inter Bold, 32px, line-height 1.3
- H3: Inter Bold, 24px, line-height 1.4
- H4: Inter Bold, 20px, line-height 1.5

**Body Text:**
- Large: Inter Regular, 18px, line-height 1.6
- Regular: Inter Regular, 16px, line-height 1.6
- Small: Inter Regular, 14px, line-height 1.5

**Labels & UI:**
- Medium: Inter Medium, 14px (buttons, labels)
- Small: Inter Medium, 12px (badges, metadata)

**Code/Monospace:**
- Use Inter for all text (no monospace fonts for brand consistency)

---

### Icons

**Icon Set:** Heroicons (https://heroicons.com/)

**Icon Styles:**
- Outline: Inactive states, secondary actions
- Solid: Active states, primary actions

**Icon Sizes:**
- Small: 16px (inline with text)
- Medium: 24px (buttons, UI elements)
- Large: 48px (agent emojis, hero sections)

**Agent Icons:**
- Use emoji characters (not Heroicons) for agent representation
- Examples: 📧 💰 📰 💵 📊
- Size: 48px in agent cards

---

### Spacing & Layout

**Grid System:**
- Desktop: 3 columns (agent cards)
- Tablet: 2 columns
- Mobile: 1 column
- Gap: 24px between cards

**Container Widths:**
- Max width: 1280px (desktop)
- Padding: 32px horizontal (desktop), 16px (mobile)

**Vertical Rhythm (Increased for Premium Feel):**
- Section spacing: 80px (desktop), 64px (mobile) - *more breathing room*
- Element spacing: 32px (within sections) - *spacious, not cramped*
- Tight spacing: 16px (related elements)
- Micro spacing: 8px (labels to inputs)

**Border Radius:**
- Cards: 12px
- Buttons: 8px
- Badges: 4px
- Inputs: 8px
- Modals: 16px

---

### Shadows & Elevation

**Philosophy:** Hybrid approach - dark shadows for depth + subtle indigo glows for brand

**Card Shadows:**
- Default: `0 4px 12px rgba(0, 0, 0, 0.4), 0 0 1px rgba(79, 70, 229, 0.2)` (shadow + micro glow)
- Hover: `0 8px 24px rgba(0, 0, 0, 0.5), 0 0 20px rgba(79, 70, 229, 0.3)` (deeper shadow + stronger glow)

**Button Shadows:**
- Default: None (gradient provides depth)
- Hover (Primary only): `0 8px 16px rgba(79, 70, 229, 0.4)` (indigo glow)

**Modal Shadows:**
- `0 20px 40px rgba(0, 0, 0, 0.6), 0 0 2px rgba(79, 70, 229, 0.3)` (heavy shadow + subtle glow border)

**Input Shadows (Focus):**
- `0 0 0 3px rgba(79, 70, 229, 0.15)` (indigo ring glow)

---

## 🎯 Component Specifications

### Buttons

**Primary CTA (Indigo Gradient):**
- Background: Linear gradient `#4F46E5` → `#3730A3` (top to bottom)
- Text: `#FFFFFF` (pure white for maximum contrast), Inter Medium 14px
- Height: 44px (standard), 48px (hero CTAs)
- Padding: 24px horizontal
- Border radius: 8px
- Border: None
- Hover: `translateY(-2px)`, shadow `0 8px 16px rgba(79, 70, 229, 0.4)`
- Transition: 200ms ease

**Secondary CTA (Outline):**
- Border: `1px solid #4F46E5` (indigo)
- Text: `#4F46E5` (indigo), Inter Medium 14px
- Background: Transparent
- Hover: Background `#4F46E510` (10% indigo), text stays same
- Same sizing as Primary

**Ghost Button** (tertiary actions):
- Border: None
- Text: `#4F46E5` (indigo), Inter Medium 14px
- Background: Transparent
- Hover: Background `#4F46E508` (5% indigo)
- Padding: 12px 16px

**Disabled State:**
- Background: `#374151` (gray)
- Text: `#6B7280` (dimmed gray)
- Cursor: not-allowed
- No hover effects
- Opacity: 0.5

---

### Cards (Agent Cards)

**Structure:**
- Width: 320px (desktop), 100% (mobile)
- Height: Auto (min 400px)
- Padding: 24px
- Border: `1px solid #374151` (cool gray border)
- Border radius: 12px
- Background: `#161B22` (elevated dark surface)
- Shadow: `0 4px 12px rgba(0, 0, 0, 0.4), 0 0 1px rgba(79, 70, 229, 0.2)` (dark shadow + subtle indigo glow)

**Hover State:**
- Transform: `translateY(-4px)`
- Border: `1px solid #4F46E5` (indigo replaces gray)
- Shadow: `0 8px 24px rgba(0, 0, 0, 0.5), 0 0 20px rgba(79, 70, 229, 0.3)` (stronger glow)
- Transition: `200ms ease`

**Card Anatomy (Top to Bottom):**
1. Tier badge (top-right, absolute position)
   - Utility: `#374151` bg, `#D1D5DB` text
   - Premium: `#4F46E5` bg, `#F9FAFB` text
2. Agent emoji (48px, margin-bottom 16px)
3. Agent name (20px bold, `#F9FAFB`, margin-bottom 8px)
4. Description (16px regular, `#E5E7EB`, 3 lines max, ellipsis, margin-bottom 16px)
5. Pricing (18px bold, `#F9FAFB`, margin-bottom 4px)
6. Tier info (12px regular, `#D1D5DB`, margin-bottom 24px)
7. CTA button (full width, 44px height, indigo gradient)

---

### Forms & Inputs

**Input Fields:**
- Height: 44px
- Padding: 12px 16px
- Border: `1px solid #4F46E5` (indigo border - always visible)
- Border radius: 8px
- Background: Transparent or `#161B22`
- Font: Inter Regular 16px
- Text color: `#F9FAFB`
- Placeholder: `#6B7280`

**Focus State:**
- Border: `2px solid #4F46E5` (thicker indigo)
- Shadow: `0 0 0 3px rgba(79, 70, 229, 0.15)` (indigo glow ring)
- Outline: None

**Labels:**
- Font: Inter Medium 14px
- Color: `#E5E7EB` (light on dark)
- Margin-bottom: 8px

**Helper Text:**
- Font: Inter Regular 12px
- Color: `#9CA3AF`
- Margin-top: 4px

**Error State:**
- Border: `1px solid #EF4444` (red)
- Helper text: `#EF4444` (red)

---

### Navigation

**Navbar:**
- Height: 64px
- Background: `#0B0E13` (same as page - seamless)
- Border-bottom: `1px solid #374151` (subtle gray separator)
- Sticky: Yes (fixed at top on scroll)
- Shadow on scroll: `0 2px 8px rgba(0, 0, 0, 0.3)`

**Logo:**
- Text: "buyanagent.ai"
- Font: Inter Bold 24px
- Gradient: Indigo `#4F46E5` → `#3730A3`

**Nav Links:**
- Font: Inter Medium 14px
- Color: `#D1D5DB` (light gray, readable)
- Hover: `#4F46E5` (indigo)
- Active: `#4F46E5` with 2px bottom border

---

### Badges

**Tier Badges:**
- Utility: Gray-100 bg, Gray-700 text, "UTILITY"
- Premium: Purple-100 bg, Purple-700 text, "PREMIUM"
- Font: Inter Medium 10px, uppercase
- Padding: 4px 8px
- Border radius: 4px

**Status Badges:**
- Active: Green-100 bg, Green-700 text
- Paused: Yellow-100 bg, Yellow-700 text
- Error: Red-100 bg, Red-700 text
- Same sizing as tier badges

---

## 🎬 Animation & Interaction

### Timing

**Standard Transitions:**
- Duration: 200ms
- Easing: `ease` (CSS default)

**Fast Micro-interactions:**
- Duration: 150ms
- Easing: `ease-out`

**Slow Reveal Animations:**
- Duration: 300ms
- Easing: `ease-in-out`

### Hover Effects

**Cards:**
- Transform: `translateY(-4px)`
- Shadow: Enhanced
- Border color: Purple-300
- Transition: All 200ms ease

**Buttons:**
- Transform: `translateY(-2px)` (primary only)
- Brightness: 110% (gradients only)
- Background: Gray-100 (outline buttons)

**Links:**
- Color: Purple-600
- Underline: Animated slide-in from left (150ms)

---

### Loading States

**Spinners:**
- Color: Purple-600
- Size: 24px (buttons), 48px (page loading)
- Animation: Smooth rotation (1s linear infinite)

**Skeleton Screens:**
- Background: Gray-200
- Shimmer: Animated gradient Gray-200 → Gray-100 → Gray-200
- Use for: Agent cards, dashboard metrics

---

## 📐 Page-Specific Patterns

### Homepage

**Hero Section:**
- Background: Subtle animated purple/blue gradient mesh (10% opacity)
- Headline: Center-aligned, max-width 800px
- CTAs: Center-aligned, horizontal layout (primary + secondary)
- Trust badges: Below CTAs, center-aligned

**Agent Grid:**
- Show 6 agents initially
- "Load More" button (outline style) shows +6 more
- Infinite scroll optional (defer to post-MVP)

---

### Agent Detail Page

**Layout:**
- Breadcrumb navigation at top
- Left column (60%): Agent info, features, FAQ
- Right column (40%): Sticky pricing card

**Pricing Card:**
- Sticky position (follows scroll)
- Tier comparison table (Utility vs Premium)
- Single CTA: "Choose Your Tier" → Activation Wizard

---

### Dashboard (Authenticated)

**Sidebar:**
- Width: 240px (desktop), collapsible (mobile)
- Background: Gray-50
- Border-right: 1px solid Gray-200

**Main Content:**
- Background: Gray-50
- Padding: 32px

**Agent Cards (Dashboard variant):**
- Horizontal layout (not vertical like homepage)
- Shows: Icon, Name, Status badge, Last activity, Quick actions
- Height: 80px

---

### Utility Tier - Status Page

**Interface:**
- Simple status page (not dashboard)
- Health indicator: Green dot + "Running" text
- Activity metrics: Today's stats, This week stats
- Control panel: Essential controls + Agent-specific controls

**Control Panel Layout:**
- White card, 24px padding
- Two sections: Essential (common to all) + Agent-specific
- Buttons: Outline style, horizontal layout, wrap on mobile

---

### Premium Tier - Analytics Dashboard

**Interface:**
- Full dashboard with charts/trends
- Key metrics row (4 cards horizontally)
- Chart section (2 charts side-by-side)
- AI insights card (full width)
- Control panel (same as Utility + advanced controls)
- Detailed activity table

**Charts:**
- Library: Recharts or Chart.js
- Colors: Purple-600 primary, Blue-500 secondary
- Grid lines: Gray-200, dashed
- Tooltips: White background, gray-900 text, shadow

---

## 🚫 What NOT to Do

**Don't:**
- ❌ Use technical jargon ("webhooks", "nodes", "workflows")
- ❌ Show complexity (hide OAuth token exchange, API details)
- ❌ Intimidate users (avoid developer-focused language)
- ❌ Add unnecessary animations (keep smooth, not flashy)
- ❌ Use emojis excessively (agent icons only)
- ❌ Mix font families (Inter only)
- ❌ Use bright, saturated colors (subtle gradients only)
- ❌ Create multi-step wizards unnecessarily (keep simple)

**Do:**
- ✅ Use plain English ("Connect Gmail", not "Authenticate OAuth")
- ✅ Show value immediately ("Save 5 hours/week", not "Automate email")
- ✅ Build trust (social proof, clear pricing, transparent terms)
- ✅ Keep interactions smooth (200ms transitions everywhere)
- ✅ Maintain consistency (same button styles, same spacing)

---

## 📚 Design Tokens (For Developers)

**CSS Custom Properties:**

```css
:root {
  /* Background */
  --color-bg-primary: #0B0E13;
  --color-bg-elevated: #161B22;
  --color-bg-elevated-hover: #1F2937;

  /* Indigo Gradient */
  --color-primary: #4F46E5;
  --color-primary-dark: #3730A3;
  --color-secondary: #3B82F6;

  /* Semantic Colors */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;

  /* Text Hierarchy */
  --color-text-primary: #F9FAFB;
  --color-text-secondary: #E5E7EB;
  --color-text-tertiary: #D1D5DB;
  --color-text-muted: #9CA3AF;

  /* Borders */
  --color-border-default: #374151;
  --color-border-hover: #4F46E5;

  /* Spacing */
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 32px;
  --spacing-xl: 64px;

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.12);
  --shadow-lg: 0 10px 24px rgba(0, 0, 0, 0.15);

  /* Transitions */
  --transition-fast: 150ms ease-out;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease-in-out;
}
```

---

## 🔗 Related Documentation

**For building UI:**
- [lovable-prompts/](../lovable-prompts/) - All 7 page-specific prompts (reference this doc)
- [marketplace-ux.md](./marketplace-ux.md) - Page navigation and structure

**For strategy context:**
- [start.md](../start.md) - Overall marketplace positioning
- [competitive-analysis.md](./competitive-analysis.md) - "Shopify meets Stripe" rationale
- [agent-catalog.md](./agent-catalog.md) - Agent descriptions for UI copy

**For technical implementation:**
- [vision.md](./vision.md) - Tech stack (Lovable generates React + Tailwind)
- [build-overview.md](../02-build/build-overview.md) - Build roadmap

---

## ✅ Version Control

**Current Version:** v1.0 (Production-Ready)
**Last Major Update:** October 6, 2025 (Tiered pricing model)

**What Changed in v1.0:**
- Added tier-specific badges and colors (Utility gray, Premium purple)
- Defined control panel layouts for both tiers
- Added chart specifications for Premium dashboards
- Created design tokens for developer handoff

See [CHANGELOG.md](../CHANGELOG.md) for complete version history.

---

**This document is the single source of truth for all brand and design decisions. All Lovable prompts reference this document.**
