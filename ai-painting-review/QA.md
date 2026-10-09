# QA record (v4)

Tested with Chromium 141 (Playwright) on 2026-10-09 against the committed build, at 1920×1080 and 1280×720. Every scene and step was captured forward and then stepped back to the start.

| Check | Result | How it was checked |
|---|---|---|
| Opening | **Pass** | The page loads on a blank canvas. The first →/Space/click starts the drawing; it does not skip it. The easel draws first, then "Would you still call it art?" is handwritten stroke by stroke, then a red underline and the subtitle appear. A second press during the animation completes it instead of advancing. The title holds until the next press. Frames were captured at 0.7, 2.5, 5 and 8 s. |
| Stray marks | **Pass** | Zero-length strokes are hidden until drawn, so the blank canvas shows no dots. |
| Layout | **Pass** | All 40 steps were reviewed. Fixed in this round: the title overlapping the easel, easel legs showing through the canvas, the shelf baseline and labels, a choice ring touching the captions, colliding ruler labels (now one dot-plot row per order), the interpretation question overlapping text, and empty placeholder boxes in van Hees (now an illustrative pair, labelled). |
| Morphs only where meaningful | **Pass** | Morphs appear in four places: the label card flips on the same painting; the two works swap order on an arc; ART separates from ARTIST; limitation cards flip to questions. Everything else cuts or fades. |
| Data | **Pass** | Bellaiche bars use one scale with small/medium/large ticks; the headline matches the bars (worth .61 > profundity .47 > beauty .22 > liking .17). Horton's means appear on a shared 1–7 axis. Rondini's result is labelled "rank order only". In the Allen grid, each square is one reported rendering, which the slide states. |
| Interaction | **Pass** | Choose (click / 1–4) draws a ring and does not advance; the reveal reports the choice. Rate (click / 1–5) before and after the label flip; both values are shown. Yes/No votes echo on the next step. All steps work with no input. |
| Navigation | **Pass** | Forward and back through all steps; back returns to the blank start. Deep links (`#ord.1`) and hash changes work. Overview (G), sources drawer (S), notes (N) and the presenter window (P) were all tested. |
| Reduced motion | **Pass** | With `prefers-reduced-motion` or the M key, each step renders its final frame. |
| JS errors | **Pass** | None. |
| Timing | **Pass (estimate)** | 535 spoken words, about 4:32 including the opening and interaction pauses (target 4:00–5:00). |
| Links | Format only | Outbound access to publishers was blocked here, so click each reference once before submitting. |

## Still to verify against full texts
- Bellaiche *d* values.
- Horton Experiment 4 means.
- Chiarella p-values.
- Oksanen 37 of 44.
- Kuta case details.
- The Rondini author list.
- The Turner painting's title and collection.

To correct any of these, edit `SOURCES`, `buildBars` or `buildRuler` in `src/index.src.html`, then run `python3 build.py`.

## Recording checklist
1. Open `index.html` in Chrome or Edge. Press `F` (fullscreen), then `H` (record mode). Open the presenter window (`P`) on a second screen.
2. Start recording on the blank canvas, then press → once.
3. *Your choice:* click a painting. *The label:* rate twice. *Artist?:* vote twice.
4. Stop about 3 s after reaching References. Export as MP4 and confirm the length is 4:00–5:00.
