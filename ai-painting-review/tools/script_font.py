#!/usr/bin/env python3
"""Extract the EMS Allure single-stroke script font (SIL OFL; Sheldon B. Michaels /
Windell H. Oskay, derived from Allura by Rob Leuschke) into compact JSON used by the
presentation's handwriting animation.  Usage:
    python3 tools/script_font.py path/to/EMSAllure.svg > src/script-font.json
Output: {"adv": default advance, "g": {char: [advance, [[x,y,x,y,...], ...]]}} in font units (y up).
"""
import json, re, sys, html
svg = open(sys.argv[1], encoding="utf-8").read()
default_adv = int(re.search(r'<font [^>]*horiz-adv-x="([\d.]+)"', svg).group(1))
out = {}
for m in re.finditer(r'<glyph unicode="([^"]*)"[^>]*?horiz-adv-x="([\d.]+)"(?:[^>]*?d="([^"]*)")?', svg):
    ch = html.unescape(m.group(1))
    if len(ch) != 1 or not (32 <= ord(ch) < 127 or ch in "’–—"):
        continue
    adv = float(m.group(2)); d = m.group(3) or ""
    polys, cur = [], None
    for cmd, x, y in re.findall(r'([ML])\s*(-?[\d.]+)\s+(-?[\d.]+)', d):
        if cmd == "M":
            cur = []; polys.append(cur)
        cur += [round(float(x)), round(float(y))]
    out[ch] = [round(adv), polys]
print(json.dumps({"adv": default_adv, "g": out}, separators=(",", ":")))
