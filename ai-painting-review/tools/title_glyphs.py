#!/usr/bin/env python3
"""Regenerate src/title-glyphs.json (outlines of the title letters for the opening morph).
Usage: python3 tools/title_glyphs.py 190 330 > src/title-glyphs.json   (needs: pip install fonttools brotli)"""
import json, sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
f = TTFont(__import__('pathlib').Path(__file__).resolve().parent.parent/'fonts'/'archivo-latin-wdth-normal.woff2')
f = instancer.instantiateVariableFont(f, {"wdth": 66, "wght": 800})
gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
hmtx = f['hmtx']
lines = ["WOULD YOU", "STILL CALL", "IT ART?"]
size = float(sys.argv[1]); x0 = 120; base0 = float(sys.argv[2]); lead = size*0.92
sc = size/upm
out = []; widths=[]
for li, text in enumerate(lines):
    x = x0; y = base0 + li*lead
    for ci, ch in enumerate(text):
        g = cmap[ord(ch)]; adv = hmtx[g][0]
        if ch != ' ':
            pen = SVGPathPen(gs)
            tp = TransformPen(pen, (sc, 0, 0, -sc, x, y))
            gs[g].draw(tp)
            d = pen.getCommands()
            word = 'ART' if (li == 2 and ci >= 3) else ''
            out.append({"d": d, "w": word})
        x += adv*sc
        # simple kerning skip
    widths.append(x - x0)
print(json.dumps({"glyphs": out, "widths": widths}))
