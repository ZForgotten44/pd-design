# Living Centennial — Cross-Platform Design Spec

**Design vision:** A child-centered, intergenerational memory ecosystem that lives in print, web, mobile, and physical space.

---

## 1. Memory Layers (Apply Across Platforms)

| Layer | Purpose | Expression |
|-------|--------|------------|
| **Children's Voice** | Creative, expressive | Rounded sans, hand-drawn icons, kid quotes, “If I Built the Church Again…” |
| **Historical** | Archival, structured | Serif typography, captions, dates, “Grandma Told Me…” |
| **Living Community** | Ongoing, interactive | Map, timeline, QR → audio/video, Memory Walk, future gallery |

Every platform should express one or more of these layers.

---

## 2. Platform Breakdown

### A. Print — The Collective Memoir

- **Format:** Hardcover, cathedral-inspired typography, gold-foil spine (centennial).
- **Sections:**  
  - “If I Built the Church Again…” (kids redesign)  
  - “Grandma Told Me…” (oral history retold by children)  
  - “A Letter to the Next 100 Years”
- **Cross-platform hook:** Each spread includes **QR codes** to:
  - Audio of the child reading their story
  - Time-lapse restoration footage
  - Interactive map location
- **Design tokens:** Use `design-system/tokens.css` hex values and font names in InDesign (Cormorant Garamond, Nunito).

---

### B. Web — Digital Companion (“Living Parish Map”)

- **Concept:** Web-first, mobile-responsive. Illustrated interactive map of Olive Street, church, school, Heritage Center, historic parish houses.
- **Features:**
  - **Interactive map:** Each building clickable → story, media, or archive.
  - **Timeline slider:** 1905 → 2025. Dragging updates:
    - Church visual (construction → open-air mass → restored cathedral)
    - Children’s reflections for recent years
    - Archival photos fade in/out
- **Homepage:** Soft sunrise + stained-glass feel; children’s line: *“This is our church.”*
- **Tech:** CMS-editable content, exportable/archivable, screen-reader friendly. See `web/` for prototype.

---

### C. Mobile — Intentional Mobile Experience

- **Not just responsive:** Dedicated “Memory Walk” mode.
- **On parish grounds:** GPS triggers stories:
  - At cornerstone → audio from students
  - At school → drawing gallery
- **Touch targets:** ≥ 44px. Same design tokens as web.
- **Audio layer:** Children narrating drawings, “what faith means,” church in 2125; Polish heritage phrases; multi-generational voices.

---

### D. Audio Layer (Critical for Kids)

- Children narrating: their drawings, what “faith” means, church in 2125.
- Include: Polish heritage phrases (Krakow origins), multi-generational voices.
- **Ethics:** Parental consent, pseudonym option, audio-only option, editorial review.

---

## 3. Advanced / Optional

- **AR:** Scan church facade → child-drawn overlay; scan printed photo in book → historical reconstruction animation.
- **“Build the Church” (web):** Kid-friendly drag-and-drop (stained glass, roof, towers); save to “Future Gallery.”
- **Intergenerational portal:** Split-screen — left: archival image; right: child interpretation; slider to fade between.

---

## 4. Design Language (All Platforms)

- **Colors:** Cathedral stone beige, parchment, stained-glass blue/red/gold, sunrise warmth.
- **Typography:** Serif (historic elegance), rounded sans (children’s voice).
- **UI:** Rounded corners, hand-drawn iconography where appropriate.
- **Accessibility:** WCAG AA, reduced-motion support, semantic HTML and ARIA.

---

## 5. Sustainability & Ethics

- **Low maintenance:** CMS so parish can add content later.
- **Archivable:** Exportable backup (e.g. static export, PDF, or WARC).
- **Youth-centered:** Parental consent framework, pseudonym options, editorial review; workshops: storyboard, collage, drawing, first reactions to church photos.

---

## 6. Role Alignment

| Role | Focus |
|------|--------|
| **Project & Community Lead** | Workshops, consent/ethics, archival interviews, partner communication |
| **Digital Developer** | Interactive map, timeline, media hosting, CMS, responsive design |
| **Design Strategist** | Book layout, typography system, QR placement, visual identity, workshop kits |

---

## 7. Optional Titles / Taglines

- “100 Years Seen Through Small Eyes”
- “The Cathedral Through Children”
- “Nickels, Dimes, and Dreams” (historical $402.10 collection)

---

## 8. File Overview

- `design-system/` — Tokens (colors, type, spacing), README.
- `web/` — Prototype: homepage, Living Parish Map, timeline slider.
- `cross-platform-spec.md` — This document.
