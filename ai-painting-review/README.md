# Would You Still Call It Art? AI-generated digital painting

A silent, presenter-controlled HTML presentation for Mahmoud Hafez's State of the Field literature review. The review asks three questions:

1. Can an AI-generated painting have aesthetic or emotional value?
2. Does art need a human artist, with intention or consciousness?
3. Does knowing a picture came from AI change how we judge it?

**Art direction, "critic's sketchbook":** paper-white and ink-black scenes, with one red-pencil accent reserved for judgments (a choice, a label, a finding). The title is drawn and handwritten on screen. Paintings are real: developer-published AI samples and public-domain human works.

**Open `index.html`** in Chrome or Edge. It is one self-contained, offline file. To rebuild after edits, run `python3 build.py`.

| File | Purpose |
|---|---|
| `index.html` | The presentation (built; do not edit) |
| `src/index.src.html` | Source: scenes, steps, narration, data |
| `src/script-font.json`, `tools/script_font.py` | Single-stroke handwriting glyphs (EMS Allure) |
| `build.py` | Embeds fonts, glyphs and images; reports which images are present |
| `assets/manifest.json`, `assets/img/` | Images with credits and provenance |
| `NARRATION.md` | Timed script, one line per press (about 4:32) |
| `EVIDENCE-MAP.md` | The 12 sources and a claim-to-source map with verification status |
| `QA.md` | QA record and recording checklist |
| `IMAGE-REQUESTS.md` | Image provenance, plus optional study figures |

**Sequence:**
1. Blank canvas. The first press draws an easel, then handwrites the question.
2. The three questions, and a definition shown with a real prompt and its outputs.
3. Review process: a shelf of 12 sources sorted by evidence type.
4. **You choose** a painting to hang, and the source is revealed.
5. **Value:** van Hees (prefer vs. spot), Rondini (creativity ranking).
6. **Label:** you rate a painting, its label flips, you rate again; then Bellaiche's effects.
7. **Context:** Horton's order swap, with a dot plot; Chiarella's order effect; de Rooij.
8. **Artist?:** you vote on a robot story; ART separates from ARTIST; two philosophers.
9. Allen's 900+ renderings → select → edit.
10. Synthesis: agree, differ, still open. Then the interpretation, next steps, and the close.

**Keys:** → / Space / click to go forward (finishes a running animation first) · ← back · 1–4 choose · 1–5 rate · F fullscreen · H record mode · P presenter · N notes · G overview · S sources · M reduced motion · deep links such as `#lab.2`
