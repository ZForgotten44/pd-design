# Would You Still Call It Art? — AI-generated digital painting

A silent, presenter-controlled HTML presentation for Mahmoud Hafez's State of the Field literature review. The stage alternates between black and white to mark reveals and changes of perspective. Paintings, charts, a method strip and the ART | ARTIST word are persistent objects that move and change role, so each study is shown as participants met it before its result appears.

**Open `index.html`** in Chrome or Edge. It is one self-contained, offline file. Run `python3 build.py` after adding images (see **IMAGE-REQUESTS.md**).

| File | Purpose |
|---|---|
| `index.html` | The presentation (built; do not edit) |
| `src/index.src.html` | Source: layers, actors, per-beat layouts, data, narration |
| `src/title-glyphs.json`, `tools/title_glyphs.py` | Letter outlines for the opening (drawing → title) |
| `build.py` | Embeds fonts, glyphs and images; prints an image-readiness report |
| `IMAGE-REQUESTS.md` | **Exact list of images to supply:** paper, link, figure or file, scene, stimulus vs. illustration |
| `assets/manifest.json` | Where the supplied files and their provenance are recorded |
| `NARRATION.md` | Timed script, one line per click (≈ 4:32) |
| `EVIDENCE-MAP.md` | Final 12 sources (incl. two 2026 studies), claim-to-source map, verification status |
| `QA.md` | QA record and recording checklist |

**Sequence:**
1. A line drawing becomes the question.
2. ART stays solid while IST? hangs off it in outline.
3. You flag the paintings you think are AI. The reveal shows the sources, then asks what guided your guess and whether learning the source changed anything.
4. Five studies, each told the same way: the method strip (stimulus · label · order · task · measure), then a prediction, then the finding.
5. A synthesis where the studies' own charts and stimuli move into Converge, Differ and Cannot settle.
6. The interpretation: ART and ARTIST as two separate judgments.
7. Limitation cards turn into research questions, with two 2026 studies already investigating some of them.

**Keys:** → / Space / click next · ← back · 1–6 flag · 1–4 pick · F fullscreen · H record mode · P presenter · N notes · G overview · S sources · M reduced motion
