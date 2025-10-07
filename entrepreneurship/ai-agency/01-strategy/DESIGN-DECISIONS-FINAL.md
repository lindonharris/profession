# Final Design Decisions - buyanagent.ai

**Date:** October 7, 2025
**Status:** Locked and ready for Lovable implementation

---

## Core Foundation

**Background:** `#0B0E13` (navy-black) with 2% noise texture overlay
**Primary Gradient:** `#4F46E5 → #3730A3` (indigo, top to bottom)
**Text:** `#F9FAFB` primary, `#E5E7EB` secondary, `#D1D5DB` tertiary
**Cards:** `#161B22` background with `#374151` borders

---

## Iconography

- **Library:** Heroicons only
- **NO emojis** anywhere on the site
- **Agent icons:** Heroicon glyphs (EnvelopeIcon, CurrencyDollarIcon, etc.) at 48px
- **Colors:** White `#F9FAFB` for nav, Indigo `#4F46E5` for CTAs

---

## Background Treatment

- Base: Pure `#0B0E13`
- Effect: 2% opacity film grain/noise texture (static)
- **No** animated gradients, glows, or meshes

---

## Loading States

- **Spinner:** Indigo `#4F46E5` rotating ring
- **Skeleton:** Gray `#1F2937` shimmer (no color tint)
- **Empty states:** Text only, no illustrations

---

## Micro-interactions

- **Links:** Indigo underline always visible (not animated slide-in)
- **Buttons:** `scale(0.98)` on press
- **Card selection:** `2px solid #4F46E5` border

---

## Mobile Adaptations

- **Background:** Same `#0B0E13`
- **Spacing:** 64px sections (vs 80px desktop)
- **Touch targets:** 48px minimum
- **Modals:** Centered (same as desktop)

---

## Tier Differentiation

**Visual distinction via badge ONLY:**
- Utility: `#374151` bg, `#D1D5DB` text
- Premium: `#4F46E5` bg, `#F9FAFB` text

**Everything else identical:**
- Same card styling
- Same indigo gradient CTA buttons
- Same hover effects

**Pricing display:**
- Utility: "$29-79/month"
- Premium: "From $100/month"

---

## Request Access Modal

**Background:** `#0B0E13` (matches page)
**Border:** `1px solid #4F46E5` (indigo)
**Shadow:** `0 20px 40px rgba(0, 0, 0, 0.6), 0 0 2px rgba(79, 70, 229, 0.3)`

**Copy:**
- Title: "Request Access"
- Subtext: "Limited spots available"
- Button: "Request Access" (indigo gradient)

**Fields:**
- Name (text input)
- Email (email input)
- Both with indigo borders `#4F46E5`

**Post-submission:**
- Instant approval
- Email sent with login link
- Success message: "Check your email - you're in!"

---

## Key Principles for Lovable

**Keep prompts simple and high-level:**
- Describe vibe ("dark, exclusive marketplace")
- Specify core colors only (background, gradient, text)
- Reference "Heroicons for all icons, no emojis"
- Don't over-specify pixel-perfect details
- Let Lovable interpret within guardrails

**Example good prompt fragment:**
> "Dark navy-black background (#0B0E13), elevated dark cards (#161B22), indigo gradient CTAs (#4F46E5 → #3730A3), off-white text (#F9FAFB). Vibe: Underground marketplace, exclusive but legitimate. Use Heroicons for agent icons (EnvelopeIcon, CurrencyDollarIcon, etc.) - no emojis."

---

**All decisions made. Ready to update Lovable prompts with dark theme.**
