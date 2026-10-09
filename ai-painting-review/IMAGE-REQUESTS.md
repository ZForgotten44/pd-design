# Images: what is in the talk, and what is optional

## Already embedded (v4): no action needed before recording

Every painting on screen is an authentic file with documented provenance. None was generated for this talk.

| Key | Where | What it is | Provenance |
|---|---|---|---|
| `squirrel1`, `squirrel2` | 3 What is an AI painting? | Two Latent Diffusion outputs for "A painting of a squirrel eating a burger" | Published by the model's developers: CompVis, `latent-diffusion` repository, `assets/txt2img-preview.png` |
| `tower`, `coffee`, `courtyard` | 5 Your choice · 6 (example pair) · 7 The label · 8 Context | Stable Diffusion v1 samples | Published by CompVis, `stable-diffusion` README samples (`merged-0005.png` tiles 1 and 5; `merged-0007.png` tile 3) |
| `turner` | 5 · 6 · 8 | J. M. W. Turner, *The Shipwreck of the Minotaur* (as commonly titled), c. 1810, public domain | File from `lengstrom/fast-style-transfer`. **Verify the museum title and holding collection before submission.** |
| `kandinsky` | 5 | Wassily Kandinsky, *Composition VII*, 1913, State Tretyakov Gallery, public domain | File from `jcjohnson/fast-neural-style` |

Paintings that only illustrate a study's design are labelled on screen in one short line (for example, "an illustrative pair … not the study's stimuli").

## Optional: study figures for the source drawer (`S`, or click any citation)

If supplied, each figure appears inside that study's detail drawer, so the audience can see the real stimuli. The talk does not depend on them.

| Manifest key | Paper | What to extract |
|---|---|---|
| `study.bellaiche` | Bellaiche et al. (2023), Fig. 1 (CC BY); full set at https://osf.io/cgw8v | Fig. 1, both sample paintings |
| `study.vanhees` | van Hees et al. (2025), https://doi.org/10.3389/fpsyg.2024.1497469; materials at https://osf.io/n7w32 | One human/DALL·E 2 pair from the same trial |
| `study.chiarella` | Chiarella et al. (2022), https://doi.org/10.1016/j.chb.2022.107406 | The two abstract canvases (one is *Test Verbovisivi*, D. M. Gagliardi, 2015), if reproduced in the paper |
| `study.allen` | Kuta (2022), Smithsonian | *Théâtre D'opéra Spatial*, Jason M. Allen (2022), lead image, credited to Allen |

To add one: save it in `assets/img/`, put the path in the entry's `file`, then run `python3 build.py`.
