# Paintings: what to add and how

Every painting is **embedded** into `index.html` at build time, so the finished file works offline with nothing to upload. Until a file is added, its tile shows a dark frame with the letter and "image pending". Nothing generated or substituted ever stands in for a real image.

## 1. The audience challenge: six paintings, A–F (required)

The challenge needs **exactly three human-made and three AI-generated paintings, each with verified provenance**. `build.py` refuses to call the build recording-ready otherwise.

| Field in `manifest.json` | What to enter |
|---|---|
| `file` | Image file name in this folder (JPG, PNG or WebP). Use at least 1200 px on the long edge for sharp fullscreen display. |
| `source` | `human` or `ai`. This is hidden on screen until the reveal. |
| `title`, `creator`, `system`, `year` | Shown under the painting after the reveal and in the image-credits drawer. For AI images, put the model in `system` (e.g. "DALL·E 2"). |
| `provenance` | A URL that documents who or what made the image: the study's stimulus file, a museum record or the developer's page. |
| `license` | The licence or permission you are relying on. |

`carry` names the painting that travels on into the authorship-label demo and the closing view. **It must be an AI image**, because Bellaiche et al. labelled AI-made images. The two paintings used as stand-ins in the Horton and Chiarella beats, and the four in the van Hees "two rooms", are chosen automatically: one human and one AI per pair. Override with `"pair": ["A","B"]` (human, AI) or `"rooms": [["C","F"],["E","D"]]` if you prefer.

**Recommended sources, which keep the source count at 12:** take the AI images from the cited studies themselves (van Hees DALL·E 2 stimuli, Bellaiche Artbreeder stimuli, Mazzone & Elgammal AICAN figures). If van Hees pairs are used, **keep their pairing** and take the human artworks from the same published set. Images from outside the twelve sources are image credits. If your rubric counts figure sources toward the 10–12 limit, adjust the selection.

## 2. Study images (optional except Allen)

| Key | Used in | Notes |
|---|---|---|
| `allen` | Beats 26–29: the dot that grows into the painting, then the interpretation | *Théâtre D'opéra Spatial* as reproduced in Kuta (2022). Shown large, so use a sharp copy. |
| `bellaiche` | Bellaiche source drawer | One original Artbreeder stimulus. |
| `vanhees` | van Hees source drawer | The article's example-pair figure (CC BY), with its figure number in `credit`. |
| `aican` | Originality beat, beside the 75 % / 85 % chart | An AICAN image from Mazzone & Elgammal (2019). |

When a study image is missing, the optional insets are simply left out. Only `allen` shows a pending tile.

## 3. Build

```
python3 build.py            # embeds fonts + every image named in manifest.json
```

The report lists each image as `ok` or `pending` and ends with `recording-ready images: YES/NO`. Pillow is optional: with it, images larger than 2600 px are downscaled before embedding.

The opening and closing brush animation is **not** a study image. Seeded code draws it live, and it carries an on-screen label saying so.
