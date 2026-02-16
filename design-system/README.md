# Living Centennial — Design System

Design language for the cross-platform **“Living Centennial”** memory ecosystem: print, web, mobile, and physical space.

## Memory Layers (Concept)

| Layer | Use Case | Typography | Tone |
|-------|----------|------------|------|
| **Children's Voice** | Creative, expressive | Rounded sans (Nunito) | Warm, friendly |
| **Historical** | Archival, structured | Serif (Cormorant Garamond) | Elegant, timeless |
| **Living Community** | Ongoing, interactive | Mix; hand-drawn icons | Inviting |

## Color Palette

- **Cathedral stone**: `#e8e2d8`, `#d4ccbe`, `#f5f0e6` (parchment)
- **Stained glass**: Blue `#4a6fa5`, Red `#8b3a3a`, Gold `#b8860b`
- **Sunrise / warmth**: `#f4e4c1`, `#faf3e0`

## Typography

- **Serif** (historic): Cormorant Garamond — headings, archival captions, “Grandma Told Me…”
- **Sans** (children’s voice): Nunito — body, kid quotes, UI, “If I Built the Church Again…”

## Usage

- **Web**: Import `tokens.css`; use CSS variables for all color, type, and spacing.
- **Print**: Export same hex values and font names into InDesign/print styles.
- **Mobile**: Same tokens; ensure touch targets ≥ 44px and contrast ≥ 4.5:1.

## Accessibility

- All text meets WCAG AA where possible.
- `prefers-reduced-motion` respected in `tokens.css`.
- Screen-reader–friendly structure and labels on all interactive elements.
