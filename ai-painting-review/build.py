#!/usr/bin/env python3
"""Inline the open-licence fonts into src/index.src.html -> index.html.

The output is a single self-contained file that works offline (file://).
Study images are NOT embedded: they load from assets/ (see assets/README.md)
so authentic, provenance-checked files can be dropped in without rebuilding.
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
         "U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,"
         "U+2212,U+2215,U+FEFF,U+FFFD")
LATIN_EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,"
             "U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,"
             "U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")

FACES = [
    # family, file, style, weight, unicode-range
    ("Fraunces", "fraunces-latin-full-normal.woff2", "normal", "100 900", LATIN),
    ("Fraunces", "fraunces-latin-ext-full-normal.woff2", "normal", "100 900", LATIN_EXT),
    ("Fraunces", "fraunces-latin-full-italic.woff2", "italic", "100 900", LATIN),
    ("Inter", "inter-latin-wght-normal.woff2", "normal", "100 900", LATIN),
    ("Inter", "inter-latin-ext-wght-normal.woff2", "normal", "100 900", LATIN_EXT),
    ("IBM Plex Mono", "ibm-plex-mono-latin-400-normal.woff2", "normal", "400", LATIN),
    ("IBM Plex Mono", "ibm-plex-mono-latin-ext-400-normal.woff2", "normal", "400", LATIN_EXT),
    ("IBM Plex Mono", "ibm-plex-mono-latin-500-normal.woff2", "normal", "500", LATIN),
]


def font_css() -> str:
    rules = []
    for family, fname, style, weight, urange in FACES:
        data = base64.b64encode((ROOT / "fonts" / fname).read_bytes()).decode()
        rules.append(
            "@font-face{font-family:'%s';font-style:%s;font-weight:%s;"
            "font-display:block;src:url(data:font/woff2;base64,%s) format('woff2');"
            "unicode-range:%s;}" % (family, style, weight, data, urange))
    return "\n".join(rules)


def main() -> None:
    src = (ROOT / "src" / "index.src.html").read_text(encoding="utf-8")
    marker = "/*@FONTS@*/"
    assert marker in src, "font marker missing"
    out = src.replace(marker, font_css())
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print("wrote index.html (%d KB)" % (len(out.encode()) // 1024))


if __name__ == "__main__":
    main()
