# Images

`manifest.json` lists every embedded image with its credit and provenance. `build.py` embeds them into `index.html`, so the file works offline.

- `images`: used in the talk. All are present (see `../IMAGE-REQUESTS.md` for sources). Each is either an AI sample published by the model's developers or a public-domain human painting.
- `study`: optional study figures shown in the source drawer when supplied.

To change an image: replace the file in `img/`, update its manifest entry, then run `python3 build.py` from the project folder. The report ends with `all talk images embedded: YES`.

The opening easel and handwriting are drawn by code. Scene 12 tells the audience so.
