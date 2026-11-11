#!/usr/bin/env python3
"""Reconstruct riddle #1 (Solar Letters -> UNIVERSE) using ONLY the generated
elements in elements/. Test of the element set (Kai, 2026-11-07).

Original design (demo_solar_letters.py, Kai 2026-10-23): full 1080x1920 page,
sun top-centre, 8 stacked slightly-bowed orbit lines, circles along each arc
(count = planet name length), one gold numbered circle per orbit (digits 1-8).
Geometry below is copied verbatim from the original demo (same Bezier math,
same positions) — only the DRAWING uses elements.

Element mapping (only elements/ files):
  background  bg-navy.svg            (whole file, as the base)
  sun halo    circle-gold-deep       (opacity 0.5, behind the sun)
  sun         circle-yellow          (diameter 210)
  letter circles (unnumbered)  ring-grey  (outer diameter 48)
  numbered circles (gold discs) circle-yellow (diameter 74) — DIGITS MISSING,
              see report: no numerals exist in the element set.

Deliberately NOT drawn (missing elements, see solar-letters-reconstruction.md):
  orbit lines (thin curved lines) — no line element exists in elements/.
  The circles are placed along the original arcs, so the orbits are implied
  by the rows, but no line is drawn.
  digits 1-8 on the gold discs — no numeral elements exist.

Outputs: solar-letters-reconstruction.svg/.png (1080x1920).
"""
import math, os
import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
EL = os.path.join(HERE, "elements")

def inner(path):
    """Inner SVG content of a standalone element file."""
    s = open(path).read()
    return s.split(">", 1)[1].rsplit("</svg>", 1)[0]

def place(body, cx, cy, scale, opacity=None):
    """Place an element (100x100 viewBox space) centred at (cx, cy)."""
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<g transform="translate({cx - 50 * scale:.1f},{cy - 50 * scale:.1f}) '
            f'scale({scale:.3f})"{op}>{body}</g>')

W, H = 1080, 1920
BG = inner(os.path.join(EL, "backgrounds", "bg-navy.svg"))
SUN_HALO = inner(os.path.join(EL, "shapes", "circle-ink-m.svg"))  # gold-deep gone with the gold theme; ink = dark glow
SUN = inner(os.path.join(EL, "shapes", "circle-yellow-m.svg"))
RING_GREY = inner(os.path.join(EL, "shapes", "ring-grey-m.svg"))
DISC_YELLOW = inner(os.path.join(EL, "shapes", "circle-yellow-m.svg"))

counts = [7, 5, 5, 4, 7, 6, 6, 7]  # MERCURY..NEPTUNE
numbered = {0: 5, 5: 6, 4: 4, 1: 1, 2: 1, 3: 3, 6: 6, 7: 2}  # orbit idx -> letter pos

def arc_point(y0, t, x_start=110, x_end=970, bow=64):
    x = (1 - t) ** 2 * x_start + 2 * (1 - t) * t * (W / 2) + t ** 2 * x_end
    y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (y0 + bow) + t ** 2 * y0
    return x, y

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
# sun halo (gold-deep disc, 270px, 50%) + sun (yellow disc, 210px) at (540, 235)
S.append(place(SUN_HALO, 540, 235, 270 / 68, opacity=0.5))
S.append(place(SUN, 540, 235, 210 / 68))
# 8 orbit rows of circles (no orbit lines — missing element)
top, row_h = 520, 168
for i, n in enumerate(counts):
    y0 = top + i * row_h
    for j in range(n):
        t = (j + 1) / (n + 1)
        x, y = arc_point(y0, t)
        if numbered.get(i) == j + 1:
            # gold disc, diameter 74 — DIGIT MISSING (no numeral element)
            S.append(place(DISC_YELLOW, x, y, 74 / 68))
        else:
            # grey ring, outer diameter 48
            S.append(place(RING_GREY, x, y, 48 / 74))
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "solar-letters-reconstruction.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "solar-letters-reconstruction.png"),
                 output_width=1080, output_height=1920)
print("circles: 47 (39 rings + 8 gold discs, digits missing), orbit lines: 0 (missing)")
print("solar-letters-reconstruction.svg/.png written")
