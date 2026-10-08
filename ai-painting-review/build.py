#!/usr/bin/env python3
"""Build index.html from src/index.src.html.

- Embeds the open-licence fonts (Archivo, Inter, IBM Plex Mono).
- Embeds every image listed in <assets>/manifest.json as a data URI, so the
  presentation works offline with no external files.
- Prints a readiness report: which paintings are present, and whether the
  audience challenge has exactly three human and three AI images with
  provenance recorded.

Usage:  python3 build.py                 # uses ./assets
        python3 build.py --assets DIR    # e.g. a folder of test images
        python3 build.py --out FILE
"""
import argparse
import base64
import json
import mimetypes
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
         "U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,"
         "U+2212,U+2215,U+FEFF,U+FFFD")
LATIN_EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,"
             "U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,"
             "U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")
FACES = [
    # family, file, weight, stretch, unicode-range
    ("Archivo", "archivo-latin-wdth-normal.woff2", "100 900", "62% 125%", LATIN),
    ("Archivo", "archivo-latin-ext-wdth-normal.woff2", "100 900", "62% 125%", LATIN_EXT),
    ("Inter", "inter-latin-wght-normal.woff2", "100 900", "100%", LATIN),
    ("Inter", "inter-latin-ext-wght-normal.woff2", "100 900", "100%", LATIN_EXT),
    ("IBM Plex Mono", "ibm-plex-mono-latin-400-normal.woff2", "400", "100%", LATIN),
    ("IBM Plex Mono", "ibm-plex-mono-latin-ext-400-normal.woff2", "400", "100%", LATIN_EXT),
    ("IBM Plex Mono", "ibm-plex-mono-latin-500-normal.woff2", "500", "100%", LATIN),
]
MAX_EDGE = 2600  # only images larger than this are downscaled (needs Pillow)


def font_css() -> str:
    out = []
    for family, fname, weight, stretch, urange in FACES:
        data = base64.b64encode((ROOT / "fonts" / fname).read_bytes()).decode()
        out.append("@font-face{font-family:'%s';font-style:normal;font-weight:%s;font-stretch:%s;"
                   "font-display:block;src:url(data:font/woff2;base64,%s) format('woff2');"
                   "unicode-range:%s;}" % (family, weight, stretch, data, urange))
    return "\n".join(out)


def data_uri(path: pathlib.Path) -> str:
    raw = path.read_bytes()
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    try:
        from PIL import Image  # optional
        import io
        im = Image.open(io.BytesIO(raw))
        if max(im.size) > MAX_EDGE:
            im.thumbnail((MAX_EDGE, MAX_EDGE))
            buf = io.BytesIO()
            im.convert("RGB").save(buf, "JPEG", quality=92)
            raw, mime = buf.getvalue(), "image/jpeg"
    except Exception:
        pass
    return "data:%s;base64,%s" % (mime, base64.b64encode(raw).decode())


def load_assets(folder: pathlib.Path):
    report, assets = [], {"challenge": [], "study": {}}
    mpath = folder / "manifest.json"
    if not mpath.exists():
        report.append("! no manifest.json in %s: every painting will show as pending" % folder)
        return assets, report, False
    man = json.loads(mpath.read_text(encoding="utf-8"))

    def embed(entry, label):
        e = {k: v for k, v in entry.items() if not k.startswith("_") and k != "file"}
        f = entry.get("file")
        if f and (folder / f).exists():
            e["src"] = data_uri(folder / f)
            report.append("  ok   %-10s %s" % (label, f))
        else:
            report.append("  --   %-10s pending (%s)" % (label, f or "no file named"))
        return e

    for entry in man.get("challenge", []):
        assets["challenge"].append(embed(entry, "challenge " + entry.get("id", "?")))
    for key, entry in (man.get("study") or {}).items():
        assets["study"][key] = embed(entry, key)
    for key in ("carry", "pair", "rooms"):
        if key in man:
            assets[key] = man[key]

    ch = assets["challenge"]
    humans = [c for c in ch if c.get("source") == "human" and c.get("src")]
    ais = [c for c in ch if c.get("source") == "ai" and c.get("src")]
    no_prov = [c.get("id") for c in ch if c.get("src") and not c.get("provenance")]
    ready = len(ch) == 6 and len(humans) == 3 and len(ais) == 3 and not no_prov
    if not ready:
        report.append("! challenge not ready: needs 6 images, 3 human + 3 ai, each with provenance "
                      "(have %d human, %d ai; missing provenance: %s)" % (len(humans), len(ais), no_prov or "none"))
    carry = assets.get("carry", "D")
    cobj = next((c for c in ch if c.get("id") == carry), None)
    if cobj and cobj.get("source") != "ai":
        report.append("! carry painting %s should be an AI image (the label demo mirrors Bellaiche, whose images were all AI)" % carry)
    return assets, report, ready


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--assets", default=str(ROOT / "assets"))
    ap.add_argument("--out", default=str(ROOT / "index.html"))
    a = ap.parse_args()
    src = (ROOT / "src" / "index.src.html").read_text(encoding="utf-8")
    for marker in ("/*@FONTS@*/", "/*@ASSETS@*/"):
        assert marker in src, "missing marker " + marker
    assets, report, ready = load_assets(pathlib.Path(a.assets))
    out = src.replace("/*@FONTS@*/", font_css()).replace(
        "/*@ASSETS@*/", "window.ASSETS=" + json.dumps(assets, ensure_ascii=False).replace("</", "<\\/") + ";")
    pathlib.Path(a.out).write_text(out, encoding="utf-8")
    print("wrote %s (%d KB)" % (a.out, len(out.encode()) // 1024))
    print("\n".join(report))
    print("recording-ready images: %s" % ("YES" if ready else "NO"))


if __name__ == "__main__":
    sys.exit(main())
