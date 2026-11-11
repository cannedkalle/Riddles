#!/usr/bin/env python3
"""Riddle #4 — FISH diamond, v3 (Kai, 2026-11-07).

v2 built the diamond from the element set (diamond-coral/yellow/paper/blue).
Kai: "For real things, we don't use elements." The NFPA diamond is a real
thing, so v3 draws it faithfully with its REAL colours — not the palette:
  red #ED1C24, blue #0057A8, yellow #FFD200, white #FFFFFF
(the standard digital rendering of NFPA 704; NFPA itself specifies the
colours, not exact hex). The frame stays the template (bg-emerald +
square-navy from elements) — the rule is about the riddle's content, not
the frame.

Quadrants marked 1-2-3-4 clockwise from the top (Kai): 1 Red (F),
2 Yellow (I), 3 White (S), 4 Blue (H) => FISH. Numbers are SVG text in the
NFPA manner (white on red/blue, black on yellow/white), not digit elements.
Thin white outline around the diamond, as on a real NFPA sign.

Outputs: fish-diamond-page-v4.svg/.png (1080x1920).
"""
import os
import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
EL = os.path.join(HERE, "elements")

def inner(path):
    s = open(path).read()
    return s.split(">", 1)[1].rsplit("</svg>", 1)[0]

W, H = 1080, 1920
BG = inner(os.path.join(EL, "backgrounds", "bg-emerald.svg"))
SQUARE = inner(os.path.join(EL, "squares", "square-navy.svg"))

OX, OY = 48, 468
CX, CY = OX + 492, OY + 492  # square centre on the page

def pt(x, y):
    return f"{OX + x},{OY + y}"

# quadrant rhombi (square-local coords), big diamond 600x600
quads = [
    # (points, fill, number, number fill)
    ([(492, 192), (642, 342), (492, 492), (342, 342)], "#ED1C24", "1", "#FFFFFF"),  # top red
    ([(642, 342), (792, 492), (642, 642), (492, 492)], "#FFD200", "2", "#000000"),  # right yellow
    ([(492, 492), (642, 642), (492, 792), (342, 642)], "#FFFFFF", "3", "#000000"),  # bottom white
    ([(342, 342), (492, 492), (342, 642), (192, 492)], "#0057A8", "4", "#FFFFFF"),  # left blue
]
centres = [(492, 342), (642, 492), (492, 642), (342, 492)]

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
S.append(f'<g transform="translate({OX},{OY})">{SQUARE}</g>')
for pts, fill, num, numfill in quads:
    points = " ".join(pt(x, y) for x, y in pts)
    S.append(f'<polygon points="{points}" fill="{fill}"/>')
# white outline around the big diamond (real NFPA sign)
outline = " ".join(pt(x, y) for x, y in [(492, 192), (792, 492), (492, 792), (192, 492)])
S.append(f'<polygon points="{outline}" fill="none" stroke="#FFFFFF" stroke-width="6"/>')
# reading-order numbers
for (cx, cy), (_, _, num, numfill) in zip(centres, quads):
    S.append(f'<text x="{OX + cx}" y="{OY + cy}" text-anchor="middle" '
             f'dominant-baseline="central" font-family="Liberation Sans" '
             f'font-weight="bold" font-size="108" fill="{numfill}">{num}</text>')
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "fish-diamond-page-v4.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "fish-diamond-page-v4.png"),
                 output_width=1080, output_height=1920)
print("fish-diamond-page-v4 written: real sign font (Liberation Sans Bold) and size (108)")
