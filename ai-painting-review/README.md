# Would You Still Call It Art? AI-generated digital painting

A silent, presenter-controlled HTML presentation for Mahmoud Hafez's State of the Field literature review. Four questions guide it:

1. Can an AI-generated painting have aesthetic or emotional value?
2. Does art need a human artist, with intention or consciousness?
3. Does knowing a picture came from AI change how we judge it?
4. Where is the field now, and what should it study next?

**Art direction, "critic's sketchbook":**
- Paper-white and ink-black scenes, with one red pencil reserved for judgments (choices, labels, findings).
- Five validated evidence-type colours mark the kinds of source.
- Every picture comes from the reviewed studies. The only exception is the opening drawing, which code generates in front of the audience; the talk later reveals this.

**Open `index.html`** in Chrome or Edge. It is one self-contained, offline file. To rebuild after edits, run `python3 build.py`.

| File | Purpose |
|---|---|
| `index.html` | The presentation (built; do not edit) |
| `src/index.src.html` | Source: scenes, steps, narration, data, the generative drawing |
| `src/script-font.json`, `tools/script_font.py` | Single-stroke handwriting glyphs (EMS Allure) |
| `build.py` | Embeds fonts, glyphs and images; reports which images are present |
| `assets/manifest.json`, `assets/img/` | Study images with credits |
| `NARRATION.md` | Timed script (about 4:42) and plain-language definitions of every measure |
| `EVIDENCE-MAP.md` | 12 sources, claim-to-source map, verification status |
| `QA.md` | QA record and recording checklist |
| `IMAGE-REQUESTS.md` | Image provenance, plus the remaining optional files |

**Sequence:**
1. A pen landscape draws itself and the question is handwritten.
2. The four questions.
3. A definition shown with two real study paintings.
4. A colour-coded shelf of sources and the five review stages.
5. **Your turn:** two real van Hees pairs, "hang" and then "which is AI?".
6. **Value:** van Hees's 50-pair design and its scatter plot, with your pairs circled.
7. **Creativity:** Rondini's shared starting lines and the creativity ranking.
8. **The label:** you rate a Bellaiche stimulus, the label flips, you rate again, then Bellaiche's effects with the exact questions.
9. **Context:** Horton's three label orders and painting 2's scores.
10. **Real setting:** Chiarella's canvases and procedure, the order result, then de Rooij.
11. **Artist?:** you vote on a robot story; ART separates from ARTIST.
12. **Philosophy:** two philosophers, two diagrams.
13. **Human practice:** Allen's 900+ renderings, then select, then edit, then the real work.
14. **Synthesis:** agree, differ, still open.
15. **Interpretation**, and the reveal that the drawing was made by code.
16. **Next questions:** each limitation flips into a next question.
17. **Close.**

**Keys:** → / Space / click to go forward (finishes a running animation first) · ← back · 1–4 pick · 1–5 rate · F fullscreen · H record mode · P presenter · N notes · G overview · S sources · M reduced motion · deep links such as `#lab.2`
