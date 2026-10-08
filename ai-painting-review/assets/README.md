# Images

**What to supply:** see `../IMAGE-REQUESTS.md`. It lists every image by request ID (R1a…R7), with the paper, the direct link, which figure or file to extract, the scene where it appears, and whether it is an actual study stimulus, a case artwork or an illustration.

**How:**
1. Put each file in this folder.
2. Name it in the matching `manifest.json` entry (`file`). For the six challenge paintings, also fill in `source` (`human` or `ai`), `title`, `creator` or `system`, `year`, and `provenance`.
3. Run `python3 build.py` from the project folder. Every image is embedded into `index.html`, so the file works offline.

The build report lists each image as `ok` or `pending` and ends with `recording-ready images: YES/NO`. YES requires three human and three AI challenge images, each with provenance, and `carry` set to an AI image.

**Labels on screen:**
- **Study stimulus** (gold): what participants actually saw.
- **Case artwork:** Allen's painting.
- **Illustration:** a challenge painting standing in to explain a method.
- **Challenge:** the audience gallery.

Until a file arrives, its frame shows "Placeholder · request R…" with the exact item needed.

The opening line drawing is generated in code and labelled as a conceptual animation. It is not a study image.
