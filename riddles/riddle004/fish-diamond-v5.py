#!/usr/bin/env python3
"""Riddle #4 — FISH diamond, v5 (Kai's idea, 2026-11-07).

v5: numbers sized from the REAL sign — the NFPA 704 standard itself, not
a photo. (Kai, 2026-11-07: "You should find a real sign. Understand the
dimension compared to the sign.") v4 measured a photo of a small container
LABEL, whose numbers are proportionally reduced — the wrong reference.

Source: NFPA 704 (2007 Edition), Figure 9.1(b) "Dimensions of NFPA 704
Placard and Numerals" (full text via archive.org). The figure's dimension
table (mm, all rows consistent):
  numeral height H | numeral width W | stroke T | placard side A | quadrant side B
  25 (1")  18 (0.7")  4   64 (2.5")   32 (1.25")
  51 (2")  36 (1.4")  8   127 (5")    64 (2.5")
  76 (3")  53 (2.1")  12  191 (7.5")  95 (3.75")
  102 (4") 71 (2.8")  16  254 (10")   127 (5")
  152 (6") 107 (4.2") 24  381 (15")   191 (7.5")
Ratios, constant across all five rows:
  H = 0.40 x placard side A   (= 0.80 x quadrant side B
                                = 0.56 x quadrant diagonal)
  W = 0.70 x H,  T = 0.16 x H.
The standard also says "Style of numerals shown is optional" — no mandated
font; real signs use a Helvetica/Arial Bold grotesque, matched here by
Liberation Sans Bold (metrically identical to Arial Bold).

Applied to our diamond (overall diagonal 600, so placard side
A = 600 / sqrt(2) = 424): numeral height H = 0.40 x 424 = 170px.
Liberation Sans Bold cap height = 0.716 em, so font-size = 170 / 0.716 = 237.

Outputs: fish-diamond-page-v5.svg/.png (1080x1920).
"""
import math, os
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

# diamond geometry (square-local): overall diagonal 600 -> placard side 424
DIAG = 600
A = DIAG / math.sqrt(2)          # placard side
NUM_H = 0.40 * A                 # standard numeral height
FONT_SIZE = round(NUM_H / 0.716) # Liberation Sans Bold cap height = 0.716 em
print(f"placard side A={A:.0f}px, numeral height H={NUM_H:.0f}px, font-size={FONT_SIZE}")

def pt(x, y):
    return f"{OX + x},{OY + y}"

quads = [
    ([(492, 192), (642, 342), (492, 492), (342, 342)], "#ED1C24", "1", "#FFFFFF"),
    ([(642, 342), (792, 492), (642, 642), (492, 492)], "#FFD200", "2", "#000000"),
    ([(492, 492), (642, 642), (492, 792), (342, 642)], "#FFFFFF", "3", "#000000"),
    ([(342, 342), (492, 492), (342, 642), (192, 492)], "#0057A8", "4", "#FFFFFF"),
]
centres = [(492, 342), (642, 492), (492, 642), (342, 492)]

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
S.append(f'<g transform="translate({OX},{OY})">{SQUARE}</g>')
for pts, fill, num, numfill in quads:
    points = " ".join(pt(x, y) for x, y in pts)
    S.append(f'<polygon points="{points}" fill="{fill}"/>')
outline = " ".join(pt(x, y) for x, y in [(492, 192), (792, 492), (492, 792), (192, 492)])
S.append(f'<polygon points="{outline}" fill="none" stroke="#FFFFFF" stroke-width="6"/>')
for (cx, cy), (_, _, num, numfill) in zip(centres, quads):
    S.append(f'<text x="{OX + cx}" y="{OY + cy}" text-anchor="middle" '
             f'dominant-baseline="central" font-family="Liberation Sans" '
             f'font-weight="bold" font-size="{FONT_SIZE}" fill="{numfill}">{num}</text>')
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "fish-diamond-page-v5.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "fish-diamond-page-v5.png"),
                 output_width=1080, output_height=1920)
print("fish-diamond-page-v5 written")
