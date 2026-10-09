# QA record (v5)

Tested with Chromium 141 (Playwright) on 2026-10-09 against the committed build. Every scene and step was captured at 1920×1080 and the interactions were checked at 1280×720. The whole deck was stepped forward and then back to the blank start.

| Check | Result | How it was checked |
|---|---|---|
| Opening | **Pass** | Starts blank, with no marks. The first press draws a 535-stroke pen landscape in overlapping passes (about 7 s): frame, sky, four mountain ranges with shading and a snowline, lake ripples and reflections, a sailboat, pines and grass. Then the question is handwritten and underlined in red, and the subtitle fades in. A press during the animation completes it rather than skipping it, and the title holds until the next press. Frames were captured at 1.5, 3.5, 6, 8.5 and 11 s. |
| Images from the research | **Pass** | All talk images come from Bellaiche, van Hees, Chiarella and the Allen case. The developer samples and the Turner and Kandinsky images were removed. |
| Game | **Pass** | Click or 1–4 marks "hang" with a red ring, then "which is AI?" with a handwritten "AI?". Neither advances the slide. The reveal shows the makers and a result line built only from the answers given. No answers means no line. |
| Data | **Pass** | Bellaiche bars carry each question's exact wording, and the headline matches the bars. Horton dots sit on a shared 1–7 axis (4.62 / 4.24 / 4.85, Table 2). The van Hees figure is the published one; the red marks only circle two existing points. The Rondini result is a rank order with no invented distances. |
| Colour coding | **Pass** | Five evidence-type hues pass the colour-blind validator (light and dark). Each is always printed beside its label, and red stays reserved for judgments. |
| Layout | **Pass** | Fixed in this round: shelf label collision, "AI?" tags spilling out of the paintings, figure annotation over a data point, cramped philosopher diagrams. ART \| ARTIST stays within the margins (measured). |
| Navigation and tools | **Pass** | Forward and back through all steps; deep links and hash changes; overview (G), sources (S), a book or citation opening the drawer, notes (N), presenter window (P), reduced motion (M). |
| JS errors | **Pass** | None. |
| Timing | **Pass (estimate)** | 547 spoken words, about 4:42 including the opening, the interaction pauses and 3 s on References. |
| Links | Format only | Publisher sites are blocked here; click each reference once. |

## Still to verify
See EVIDENCE-MAP.md, "Still to verify".

## Recording checklist
1. Open `index.html` in Chrome or Edge. Press `F`, then `H`. Open the presenter window (`P`) on a second screen.
2. Start recording on the blank canvas, then press → once.
3. *Your turn:* click one painting per pair, press →, then click again. *The label:* rate twice. *Artist?:* vote twice.
4. Stop about 3 s after References. Export as MP4 and confirm the length is 4:00–5:00.
