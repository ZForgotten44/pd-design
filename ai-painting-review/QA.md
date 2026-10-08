# QA record (v3)

Tested with Chromium 141 (Playwright 1.56) on 2026-10-08. Each check ran on the committed build (images pending) and on a local test build with stand-in images (public-domain paintings plus synthetic images), which was used only to check layout and motion and is neither committed nor published.

| Check | Result | How it was checked |
|---|---|---|
| Chart headlines match the data | **Pass** | Beat 12 reads "Worth moved most. Liking moved least." (worth .61 > profundity .47 > beauty .22 > liking .17). The pick echo compares the viewer's choice with that order. The v2 errors "depth moved most" and "beauty moved least" are gone. |
| Stimulus vs. illustration | **Pass** | Each painting carries a badge: **Study stimulus** (gold), **Illustration**, **Case artwork** or **Challenge**. Study frames (Bellaiche, Chiarella, van Hees, Allen, Rondini, Taylor) show request-ID placeholders until the files arrive (see IMAGE-REQUESTS.md). |
| Reveal layout | **Pass** | The two-row gallery is kept. Flagged paintings move to the first positions, and each tile keeps 510×290 px with its source, verdict and credit underneath, revealed one at a time. |
| Light/dark alternation | **Pass** | 19 light and 17 dark beats. Inversions mark the reveal, predictions and findings, the synthesis and the interpretation; dark scenes carry setup, method and the ART \| ARTIST split. The accent is a single muted gold (darker gold on light scenes). |
| Morph continuity | **Pass** | Mid-transition frames reviewed: line drawing → letters (the spiral becomes "ART?"); challenge → reveal → reflect thumbnails; the illustration flips its label on the same pixels; the Horton swap on arcs; the method strip swapping slot contents per study; the painting → scenario card; ARTIST separating from ART; a dot → the Allen painting; the study charts and stimuli moving into the synthesis columns; limitation cards → questions. |
| Reversibility | **Pass** | Stepped through all 36 beats forward and then back: every visible object's position, size, opacity and state was identical. |
| Interaction | **Pass** | Flagging (click / 1–6) does not advance. Reflection answers produce a conditional sentence. The rating pick (click / 1–4) is echoed. Clicking empty stage advances. The presenter window drives the main window; where pop-ups are blocked, in-page notes open instead. |
| Viewport, fullscreen, reduced motion | **Pass** | The stage fills 1280×720 exactly and letterboxes on other ratios. `F` and `H` work. With reduced motion, the opening renders its final frame and morphs shorten to 240 ms. |
| JS errors | **Pass** | None. |
| Timing | **Pass (estimate)** | 578 words ≈ 4:32 including the challenge and reflection pauses. |
| **Images** | **Open** | `build.py` reports `recording-ready images: NO` until IMAGE-REQUESTS.md items are supplied. |
| Links | Format only | Outbound access was blocked here. Click each reference once. |

## Still to verify against full texts
Bellaiche d values; Horton Experiment 4 means; Chiarella p-values; Oksanen 37/44; Mikalonytė & Kneer condition-level art-status results; the Rondini author list. Edit `BEL`, `chartHorton` or `SOURCES` in `src/index.src.html`, then run `python3 build.py`.

## Recording checklist
1. Supply the images in IMAGE-REQUESTS.md and run `python3 build.py` until it reports `recording-ready images: YES`.
2. Open `index.html` in Chrome or Edge; press `F` then `H`; put the presenter window (`P`) on a second screen.
3. Beat 6: flag about three paintings. Beat 8: answer both prompts. Beat 11: commit a pick.
4. Stop after about 3 s on References. Export as MP4 and confirm 4:00–5:00.
