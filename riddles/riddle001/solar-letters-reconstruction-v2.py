#!/usr/bin/env python3
"""Reconstruction v2 — riddle #1 (Solar Letters -> UNIVERSE) in the CURRENT
system (Kai, 2026-11-07): TikTok page 1080x1920, riddle in the 984x984
square, theme colour emerald as the frame.

v1 rebuilt the old full-page demo (no square, no emerald) — wrong. v2 fixes
that:
  page background  bg-emerald.svg  (theme colour = the frame)
  riddle square    square-navy.svg at (48, 468) — the riddle itself stays
                   DARK: yellow sun + grey rings need a dark panel. The theme
                   colour frames the riddle; it does not recolour its content.
  content          same elements as v1 (circle-yellow sun, ring-grey letter
                   circles, circle-yellow numbered discs), REFLOWED into the
                   square: sun smaller (dia 150), rows compressed
                   (spacing 98, bow 38), circles SAME size (dia 48 / discs 74)
                   so legibility is kept. No shape is stretched.

Still missing (same as v1): orbit lines (no line element) and digits 1-8
(no numeral element) — the gold discs are still blank.

Outputs: solar-letters-reconstruction-v2.svg/.png (1080x1920).
"""
import os
import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
EL = os.path.join(HERE, "elements")

def inner(path):
    s = open(path).read()
    return s.split(">", 1)[1].rsplit("</svg>", 1)[0]

def place(body, cx, cy, scale, opacity=None):
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<g transform="translate({cx - 50 * scale:.1f},{cy - 50 * scale:.1f}) '
            f'scale({scale:.3f})"{op}>{body}</g>')

W, H = 1080, 1920
BG = inner(os.path.join(EL, "backgrounds", "bg-emerald.svg"))
SQUARE = inner(os.path.join(EL, "squares", "square-navy.svg"))
SUN_HALO = inner(os.path.join(EL, "shapes", "circle-ink-m.svg"))
SUN = inner(os.path.join(EL, "shapes", "circle-yellow-m.svg"))
RING_GREY = inner(os.path.join(EL, "shapes", "ring-grey-m.svg"))
DISC_YELLOW = inner(os.path.join(EL, "shapes", "circle-yellow-m.svg"))

counts = [7, 5, 5, 4, 7, 6, 6, 7]  # MERCURY..NEPTUNE
numbered = {0: 5, 5: 6, 4: 4, 1: 1, 2: 1, 3: 3, 6: 6, 7: 2}  # orbit idx -> letter pos

# square-local coords; page offset (48, 468)
OX, OY = 48, 468

def arc_point(y0, t, x_start=62, x_end=922, bow=38):
    cx = 492  # square centre x
    x = (1 - t) ** 2 * x_start + 2 * (1 - t) * t * cx + t ** 2 * x_end
    y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (y0 + bow) + t ** 2 * y0
    return OX + x, OY + y

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
S.append(f'<g transform="translate({OX},{OY})">{SQUARE}</g>')
# sun halo (dia 193, 50%) + sun (dia 150) at square-local (492, 110)
S.append(place(SUN_HALO, OX + 492, OY + 110, 193 / 68, opacity=0.5))
S.append(place(SUN, OX + 492, OY + 110, 150 / 68))
# 8 orbit rows of circles (no orbit lines, no digits — missing elements)
for i, n in enumerate(counts):
    y0 = 210 + i * 98
    for j in range(n):
        t = (j + 1) / (n + 1)
        x, y = arc_point(y0, t)
        if numbered.get(i) == j + 1:
            S.append(place(DISC_YELLOW, x, y, 74 / 68))
        else:
            S.append(place(RING_GREY, x, y, 48 / 74))
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "solar-letters-reconstruction-v2.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "solar-letters-reconstruction-v2.png"),
                 output_width=1080, output_height=1920)
print("v2 written: emerald frame + navy square + 47 circles (digits/lines still missing)")
