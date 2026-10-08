# QA record

Build: `index.html` (single self-contained file, 829 KB, fonts embedded, no network requests except the optional `assets/` images). Tested with Chromium 141 (Playwright 1.56) on 2026-10-08.

| Check | Result | How it was checked |
|---|---|---|
| Keyboard navigation | **Pass** | →, Space, Enter, PageDown, ↓ advance; ←, Backspace, PageUp, ↑ go back; Home and End jump. Stepping forward through all 41 builds and then back produced the identical state sequence in reverse. |
| Reversible builds | **Pass** | On scene 05, step 4 shows the bars (scaleX 1); one ← hides them again (scaleX 0). Every reveal is class-driven from `data-in`, so going back always undoes it. |
| Click to advance | **Pass** | Clicking the stage advances. Clicking a citation chip opens the source drawer and does not advance. |
| All reveals | **Pass** | Screenshots of all 41 builds at 1920×1080 were reviewed for overlap and overflow. Fixed during QA: the heading/subtitle overlap in scene 03, the divider crossing the philosophy cards in scene 09, the appendix overflow (split into A and B), and the drawer shadow bleeding onto the stage edge. |
| Fullscreen / viewport | **Pass** | The 1920×1080 stage is scaled to fit and letterboxed: at 1280×720 the stage fills the viewport exactly; at 1440×900 it sits at 1440×810, centred. `F` toggles fullscreen. Controls auto-hide after 2.2 s, and `H` (record mode) hides them entirely. |
| Presenter mode | **Pass** | `P` opens a second window showing the current line, the remaining lines, the next build, elapsed time vs. target, and pace. Keys pressed in that window drive the main window (verified). `N` shows notes in the page for single-screen rehearsal. |
| Reduced motion | **Pass** | `prefers-reduced-motion` is detected. In that mode the painting renders instantly, the chapter wipe is skipped and transitions shorten to 180 ms. `M` toggles the same mode manually. |
| Text and chart sharpness | **Pass** | All text is live, with fonts embedded. All charts are inline SVG built from data arrays in the source (`chartBellaiche`, `chartHorton`, `chartMazzone`, `waffle`). The painting canvas renders at up to 2× device resolution. |
| Image sharpness | **Open — needs your files** | The three study-image slots show labelled placeholders until the authentic files are added (see `assets/README.md`). No study image was generated or substituted. |
| Links | **Formatting pass; not resolved online** | All 12 reference URLs are well-formed DOIs or the original Smithsonian URL. This build environment's network policy blocked outbound requests (403 at the proxy), so the links could not be opened from here. Click each one once before submitting. |
| JS errors | **Pass** | No page errors. The only console messages are the expected "file not found" probes for the three empty image slots. |
| Timing | **Pass (estimate)** | 635 narrated words. At 145 wpm plus 0.5 s per build this comes to ≈ 4:43. Confirm with a rehearsal; the presenter window flags when you are more than 8 s behind. |
| No audio / no autoplay | **Pass** | There is no audio. The only automatic motion is the ~4 s opening paint stroke, which runs under your first sentence and blocks nothing. |

## Verification status (read before recording)

The handoff described a package of PDFs, a Source-Catalog, a Figure-Catalog, the assignment PDF and presentation tips. **Only three files reached this build:** the creative brief, the comparative analysis and START_HERE.md. Outbound access to the publishers was also blocked. As a result:

- **Checked against public abstracts and index records:** Bellaiche (Artbreeder, random labels, four criteria); Horton (six experiments, N = 2,965); Chiarella (art-fair setting, order-dependent penalty, EDA higher on second view, heart rate unchanged); Mikalonytė & Kneer (two experiments, N = 693, art vs. artist asymmetry, intention); van Hees (DALL·E 2, separate preference and discrimination tasks, both above chance); Oksanen (723 screened → 44 included).
- **Taken from the comparative analysis and still to be checked against the PDFs** (marked **A** in EVIDENCE-MAP.md): Bellaiche Study 1 *d* values (.17 / .22 / .47 / .61); Horton Experiment 4 means (4.24 / 4.62 / 4.85, and that the rated item is the second work); Chiarella p = .60 and p = .016; Mazzone & Elgammal 75% vs. 85%; Oksanen 37 and 24 of 44.
  - Note: one public summary of Bellaiche reports unstandardised regression coefficients of about .24 for liking, .23 for beauty and .52 for worth. These are a different statistic from Cohen's *d*. The ordering (worth > beauty ≈ liking) matches the chart, but confirm that the paper reports the *d* values exactly as charted.
- **Not checked against the assignment PDF.** The rubric points in the brief are covered (name, topic, significance, findings and disagreements, process, interpretation, next steps, 10–12 sources, ≥ 2 peer-reviewed, author–year citations beside evidence, references with URLs). Still, cross-check against `assignment/01-Major-Assignment.pdf` and the presentation tips.

To change a number, edit the data arrays in `src/index.src.html` (`chartBellaiche`, `chartHorton`, `chartMazzone`, `SOURCES`, `NOTES`) and run `python3 build.py`. Do not edit `index.html` directly, because the build overwrites it.

## Recording checklist
1. Add the three images to `assets/` (or leave the placeholders) and check them fullscreen.
2. Open `index.html` in Chrome or Edge, press `F` then `H`, and open the presenter window with `P` on a second screen.
3. Record the main display only (OBS or similar). Advance from the presenter window or a clicker.
4. Stop after about 3 s on References. Export as MP4 and confirm the runtime is between 4:00 and 5:00.
