# QA record (rebuild, v2)

Tested with Chromium 141 (Playwright 1.56) on 2026-10-08. Each check was run twice: on the committed build, where all images are pending, and on a **local test build** with stand-in images (public-domain paintings plus synthetic images). The test build was only used to check layout and motion. It is not committed and not published.

| Check | Result | How it was checked |
|---|---|---|
| Navigation | **Pass** | →, Space, Enter, PageDown and click advance; ←, Backspace and PageUp go back; Home and End jump. Deep links (`#vh-2` etc.) open on that beat. |
| Reversible builds | **Pass** | Stepped through all 37 beats forward and then back. Every visible object's position, size, opacity and state was identical in both directions. |
| Morph continuity | **Pass** | Mid-transition frames (about 0.5 s in) show the same painting objects moving and scaling, not crossfading: challenge → reveal, reveal → label demo, the Horton swap (arcs), the gallery splitting into the van Hees rooms, the dot growing into the painting, and limitation cards becoming proposals. |
| Audience interaction | **Pass** | Clicking a painting (or pressing 1–6) flags it with an outline and "Your guess: AI" without advancing. The reveal groups the flagged paintings, then shows sources one at a time with "Caught it" or "Surprised?". The rating pick (click or 1–4) is echoed against the finding. Clicking empty stage advances. |
| Honesty labels | **Pass** | On screen: the challenge is "not data / not a replication"; the label demo and Horton/Chiarella paintings are stand-ins; the scenario card is a paraphrase; the Art/Artist scale is "schematic, not plotted values"; the opening is a conceptual animation. |
| Layout at 1920×1080 | **Pass after fixes** | All 37 beats were screenshotted and reviewed. Fixed during QA: reveal headers colliding with badges; the "rated" tag colliding with a column label; Chiarella stats overflowing; the meta-analysis bracket labels overlapping the de Rooij panel. |
| Viewport and fullscreen | **Pass** | The 16:9 stage fills a 1280×720 viewport exactly and letterboxes on other ratios. `F` toggles fullscreen; `H` hides all controls. |
| Presenter mode | **Pass** | `P` opens a window showing the line, the next line, flag and pick state, and elapsed vs. target time. Its keys drive the main window. Where pop-ups are blocked (e.g. the claude.ai preview), `P` opens in-page notes instead. |
| Reduced motion | **Pass** | `prefers-reduced-motion` (or `M`) shortens morphs to 240 ms, skips the arc paths and draws the painting instantly. |
| Charts | **Pass** | Every chart is SVG or HTML built from data arrays in the source; there are no images of charts. Scales, samples and conditions are stated beside each. |
| JS errors | **Pass** | None. |
| Timing | **Pass (estimate)** | 610 words ≈ 4:42 including the challenge and reveal pauses. Confirm with a rehearsal. |
| **Images** | **Open: needs your files** | `assets/manifest.json` is empty, so every painting tile shows "image pending" and `build.py` reports `recording-ready images: NO`. See `assets/README.md`. |
| Links | Formatting pass; not opened | Outbound access was blocked in this environment. Click each reference once. |

## Still to verify against the PDFs (unchanged from v1)
These figures come from the handoff analysis (marked **A** in EVIDENCE-MAP.md): Bellaiche *d* values; Horton Experiment 4 means and the rated item; Chiarella p-values; Mazzone & Elgammal 75 % vs. 85 %; Oksanen 37 and 24 of 44. To change a number, edit `BEL`, `chartHorton`, `chartMazzone` or `SOURCES` in `src/index.src.html`, then run `python3 build.py`.

## Recording checklist
1. Fill `assets/manifest.json` and add the files, then run `python3 build.py` until it says `recording-ready images: YES`.
2. Open `index.html` in Chrome or Edge, press `F` then `H`, and put the presenter window (`P`) on a second screen.
3. On beat 7, flag about three paintings; on beat 12, commit a rating pick.
4. Stop after about 3 s on References. Export as MP4 and confirm the runtime is 4:00–5:00.
