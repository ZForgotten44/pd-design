# Claim-to-source map and final source selection (v4)

Scene numbers follow the overview (`G`) and NARRATION.md:

| # | Scene | # | Scene |
|---|---|---|---|
| 1 | Opening | 10 | Human practice (Allen) |
| 2 | Three questions | 11 | Synthesis |
| 3 | What is an AI painting? | 12 | Interpretation |
| 4 | Review process | 13 | Next steps |
| 5 | Your choice | 14 | Close |
| 6 | Q1 · Value | 15 | References |
| 7 | Q3 · The label | 16 | Appendix A |
| 8 | Q3 · Context | 17 | Appendix B |
| 9 | Q2 · Artist? | | |

## Final selection: 12 sources (the assignment allows 10–12)

There are at least 2 peer-reviewed sources (11 of the 12 are), drawn from several disciplines.

| # | Source | Evidence type | Discipline | Peer-reviewed | Scenes (all also in 4 and 15) |
|---|---|---|---|---|---|
| 1 | Bellaiche et al., 2023 | Controlled label experiment | Cognitive psychology | Yes | 7, 11 |
| 2 | Horton et al., 2023 | Controlled label experiment | Behavioural science | Yes | 8, 11 |
| 3 | Chiarella et al., 2022 | Label experiment (field, physiological) | Cognitive neuroscience | Yes | 8, 11 |
| 4 | van Hees et al., 2025 | Preference & detection experiment | Psychology | Yes | 6, 11 |
| 5 | Mikalonytė & Kneer, 2022 | Folk-judgment scenario experiments | Experimental philosophy / HRI | Yes | 9, 11 |
| 6 | Rondini et al., 2026 | Controlled creativity experiment | Cognitive science | Yes | 6, 13 |
| 7 | Oksanen et al., 2023 | Systematic scoping review | Social psychology | Yes | 11, 13 |
| 8 | de Rooij, 2025 | Meta-analysis | Psychology of aesthetics | Yes | 8, 11 |
| 9 | Hertzmann, 2018 | Philosophical account | Computer science / philosophy of art | Yes | 9, 11 |
| 10 | Coeckelbergh, 2017 | Philosophical account | Philosophy of technology | Yes | 9, 11 |
| 11 | Taylor et al., 2026 | Algorithm audit & trace ethnography (FAccT) | Computer science / HCI | Yes (conference) | 13 |
| 12 | Kuta, 2022 (*Smithsonian*) | Journalism (one case) | Journalism | No | 10 |

**Image credits are not counted as sources.** These are the CompVis Latent Diffusion and Stable Diffusion repositories, Turner, Kandinsky, and the EMS Allure font. They are listed under References as "Images" because they supply pictures, not evidence. If your instructor counts every cited item, the total is 12 + 4 image credits; dropping Kuta or Taylor would bring it back within range.

## Claims → source → status

Status codes:
- **V**: matches the working analysis *and* a public abstract, record or university release.
- **A**: from the working analysis only; re-check against the full text.
- **I**: Mahmoud's interpretation, presented on screen as "My interpretation".
- **D**: demonstration or illustration, not data.

| Scene | Claim on screen or in narration | Source | Status |
|---|---|---|---|
| 1 | Hand-drawn easel and handwritten title (drawn by code; revealed as such in scene 12) | — | D |
| 3 | Two outputs for "A painting of a squirrel eating a burger"; noise-to-image shown as simplified | CompVis latent-diffusion (image credit) | V (prompt and images as published by the developers) |
| 5 | 2 human paintings + 2 Stable Diffusion v1 samples; the viewer chooses; sources revealed | Image manifest | D ("a classroom question, not a study") |
| 6 | Same pairs, two separate groups (prefer / which is AI); both above chance; easier-to-spot images also preferred | van Hees 2025 | V (design, both above chance) / A (correlation). The pictured pair is labelled illustrative. |
| 6 | Visual artists > non-artists > AI with human guidance > AI on its own; 255 raters; GPT-4o judged differently; rank only | Rondini 2026 | V (university release, preprint abstract) |
| 7 | AI-made Artbreeder images, random labels; *d*: liking .17, beauty .22, profundity .47, worth .61 → "most for worth and profundity" | Bellaiche 2023 | V (design) / **A (d values)** |
| 7 | Study 2 added emotion, story (narrativity), effort and personal meaning | Bellaiche 2023 | V |
| 7 | The viewer's own two ratings | — | D (the coffee image is a Stable Diffusion sample, stated on screen) |
| 8 | Saw two works, rated the second; Exp. 4 means 4.85 / 4.62 / 4.24 on a 1–7 composite; six experiments, N = 2,965 | Horton 2023 | **A (means)** / V (N) |
| 8 | Two human abstract canvases at an art fair; AI label lowered liking only when it came second; p = .60 overall, p = .016 order | Chiarella 2022 | V (design, order result) / **A (p-values)** |
| 8 | Average penalty small for sensory and emotional responses, moderate for meaning | de Rooij 2025 | A (qualitative only; no numbers shown) |
| 9 | Stories only; robot's painting judged art about as readily (varied by story); robot much less often an artist, partly via intention | Mikalonytė & Kneer 2022 | V (direction) / A (condition detail) |
| 9 | Hertzmann: art is social exchange between agents; software is a tool. Coeckelbergh: verdict depends on outcome, process or relations | as cited | A |
| 10 | Midjourney; about 80 hours; 900+ renderings; select, edit; Colorado State Fair 2022 digital-art prize. Squares stand for renderings, not his images | Kuta 2022 | A |
| 11 | Agree: a human label raises judgments; people can like AI paintings | Bellaiche, Horton, de Rooij, van Hees | I (synthesis) |
| 11 | Differ: worth .61 vs liking .17; order and medium; 37 of 44 single-country | Bellaiche; Chiarella; Oksanen | **A (37/44)** |
| 11 | Still open: liking, spotting, originality and artistry are separate; can a model be an artist? | van Hees; Horton; Mikalonytė & Kneer; Hertzmann; Coeckelbergh | I |
| 12 | Can count as art through people; a model as independent artist is not established; no inference to consciousness | — | I |
| 13 | Trust, credit, whose taste. Next questions: current models, documented workflows (Rondini), other cultures (Taylor: the predictor favours realistic landscapes, cities and portraits by Western and Japanese artists) | Rondini; Taylor; Oksanen | V / I (the questions are proposals) |

## Version notes
- **de Rooij (2025):** the supplied PDF reports inconsistent domain counts between abstract and body, so the paper is used qualitatively only.
- **Hertzmann** and **Mikalonytė & Kneer:** the packet copies are author manuscripts. The citations point to the published versions.
- **Taylor et al.:** the title changed between arXiv versions. The citation uses the later title and the FAccT '26 venue.
- **Rondini et al.:** confirm the full author list on the journal page.
- **van Hees et al.:** published January 2025 in volume 15 (dated 2024).
