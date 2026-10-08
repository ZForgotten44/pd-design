# Would You Still Call It Art? — AI-generated digital painting

A silent, presenter-controlled HTML presentation for Mahmoud Hafez's State of the Field literature review. Paintings are persistent objects on a black stage. They move, scale and change role from beat to beat, so each experiment is shown as participants met it before its finding is revealed.

**Open `index.html`** in Chrome or Edge. It is one self-contained file that works offline. Fonts and every image named in `assets/manifest.json` are embedded at build time.

| File | Purpose |
|---|---|
| `index.html` | The presentation (built output, do not edit) |
| `src/index.src.html` | Source: layers, actors, per-beat layouts, data, narration |
| `build.py` | Embeds fonts and images, then prints an image-readiness report |
| `assets/manifest.json` | The six challenge paintings (3 human, 3 AI) and the study images, with provenance |
| `assets/README.md` | What images to add, and where they appear |
| `NARRATION.md` | Timed script, one line per click (≈ 4:42) |
| `EVIDENCE-MAP.md` | Final 12 sources and the claim-to-source map with verification status |
| `QA.md` | QA record, open items, recording checklist |
| `fonts/` | Archivo (variable width), Inter, IBM Plex Mono (SIL Open Font License) |

**How it moves (the main morphs):**
- **Challenge → reveal → carry.** The audience flags paintings. The flagged ones move into a comparison row, and their sources appear one at a time. One AI painting then travels into the label experiment.
- **Bellaiche.** The pixels stay fixed while the label flips from Human to AI. The rating options become the chart's bars, and the bars regroup into the cross-study meta-analysis view.
- **Horton and Chiarella.** The same two paintings swap order on arcs to show which one was rated, then shrink into the chart.
- **van Hees.** The gallery splits into two rooms for the two separate participant groups.
- **Mikalonytė & Kneer.** The painting turns into a written scenario card, and ART and ARTIST become two separate judgments.
- **Allen.** One of 900 dots grows into the painting.
- **Next steps.** Each limitation card travels across the screen and becomes its proposed next step.

**Keys:** → / Space / click next · ← back (everything reverses) · 1–6 flag paintings · 1–4 pick a rating · F fullscreen · H record mode · P presenter window · N notes · G overview · S sources · M reduced motion
