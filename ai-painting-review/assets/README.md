# Images

`manifest.json` lists every embedded image with its credit and provenance. Every image comes from one of the reviewed sources (see `../IMAGE-REQUESTS.md`). `build.py` embeds them into `index.html`, so the file works offline.

- `images`: used in the talk.
- `study`: optional figures shown in a source's detail drawer.

To change an image: replace the file in `img/`, update its manifest entry, then run `python3 build.py` from the project folder. The report ends with `all talk images embedded: YES`.
