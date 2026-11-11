#!/usr/bin/env python3
"""Riddle #4 — FISH diamond, three-row version (Kai's idea, 2026-11-07).

Formalized design (Kai, 2026-11-07):
- background one tint brighter: bg-emerald-light (#94DEAF -> #40BD7E)
- riddle square = brightest emerald tint (#E0F8E8), as wide as the
  background — 1080 x 1080, no side margins, centred vertically
- coral square with "?" = the standard indicator for the thing to answer
- three rows, same format: diamond -> arrow -> emoji / question square

Rows (reading order clockwise from the top: red, yellow, white, blue;
each number indexes a letter of that quadrant's word):
  1/1/1/1     -> FISH (🐟)
  3/2/empty/5 -> ANT  (🐜)
  2/1/4/2     -> LICE (coral "?" square — the question)

Numerals keep the standard proportion (NFPA 704 Fig. 9.1(b): numeral height
= 0.40 x placard side), scaled to each diamond's size. The arrow is a thick
block arrow (the 皆謎 language), ink on the pale square.

Outputs: fish-diamond-rows-page.svg/.png (1080x1920).
"""
import math, os
import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
EL = os.path.join(HERE, "elements")

def inner(path):
    s = open(path).read()
    return s.split(">", 1)[1].rsplit("</svg>", 1)[0]

W, H = 1080, 1920
BG = inner(os.path.join(EL, "backgrounds", "bg-emerald-light.svg"))
SQUARE = inner(os.path.join(EL, "squares", "square-emerald-pale-1080.svg"))
QSQ = inner(os.path.join(EL, "indicators", "question-square-s.svg"))
OX, OY = 0, 420  # square spans the full width, centred vertically

QUADS = [
    ("#ED1C24", "#FFFFFF"),  # red, top
    ("#FFD200", "#000000"),  # yellow, right
    ("#FFFFFF", "#000000"),  # white, bottom
    ("#0057A8", "#FFFFFF"),  # blue, left
]

def diamond(cx, cy, diag, numbers):
    """One NFPA diamond, square-local coords. numbers = [red, yellow, white,
    blue] in reading order; None = empty quadrant (no number)."""
    h = diag / 2.0
    verts = [
        [(cx, cy - h), (cx + h / 2, cy - h / 2), (cx, cy), (cx - h / 2, cy - h / 2)],
        [(cx + h, cy), (cx + h / 2, cy + h / 2), (cx, cy), (cx + h / 2, cy - h / 2)],
        [(cx, cy + h), (cx - h / 2, cy + h / 2), (cx, cy), (cx + h / 2, cy + h / 2)],
        [(cx - h, cy), (cx - h / 2, cy - h / 2), (cx, cy), (cx - h / 2, cy + h / 2)],
    ]
    centres = [(cx, cy - h / 2), (cx + h / 2, cy), (cx, cy + h / 2), (cx - h / 2, cy)]
    out = []
    for pts, (fill, _) in zip(verts, QUADS):
        points = " ".join(f"{OX + x:.0f},{OY + y:.0f}" for x, y in pts)
        out.append(f'<polygon points="{points}" fill="{fill}"/>')
    outline = " ".join(f"{OX + x:.0f},{OY + y:.0f}" for x, y in
                       [(cx, cy - h), (cx + h, cy), (cx, cy + h), (cx - h, cy)])
    out.append(f'<polygon points="{outline}" fill="none" stroke="#FFFFFF" '
               f'stroke-width="{max(2, diag / 100):.1f}"/>')
    font_size = round(0.40 * (diag / math.sqrt(2)) / 0.716)
    for (nx, ny), num, (_, numfill) in zip(centres, numbers, QUADS):
        if num is None:
            continue
        out.append(f'<text x="{OX + nx:.0f}" y="{OY + ny:.0f}" text-anchor="middle" '
                   f'dominant-baseline="central" font-family="Liberation Sans" '
                   f'font-weight="bold" font-size="{font_size}" '
                   f'fill="{numfill}">{num}</text>')
    return out

def arrow(x0, x1, y):
    """Thick block arrow pointing right, ink. Shaft 30 tall, head 90 tall."""
    hx = x0 + (x1 - x0) * 0.625  # where the head starts
    pts = [(x0, y - 15), (hx, y - 15), (hx, y - 45), (x1, y),
           (hx, y + 45), (hx, y + 15), (x0, y + 15)]
    points = " ".join(f"{OX + x:.0f},{OY + y:.0f}" for x, y in pts)
    return f'<polygon points="{points}" fill="#101828"/>'

ROWS = [
    # (row centre y, diamond numbers, answer: emoji or None for the question)
    (180, [1, 1, 1, 1], "🐟"),
    (540, [3, 2, None, 5], "🐜"),
    (900, [2, 1, 4, 2], None),
]
DIAG = 300
DX, AX = 360, 820  # diamond centre x, answer centre x

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
S.append(f'<g transform="translate({OX},{OY})">{SQUARE}</g>')
for row_y, numbers, emoji in ROWS:
    S += diamond(DX, row_y, DIAG, numbers)
    S.append(arrow(560, 720, row_y))
    if emoji is not None:
        S.append(f'<text x="{OX + AX}" y="{OY + row_y}" text-anchor="middle" '
                 f'dominant-baseline="central" font-family="Noto Color Emoji" '
                 f'font-size="100">{emoji}</text>')
    else:
        # coral "?" square element (120x120, viewBox 100x100 -> scale 1.2)
        S.append(f'<g transform="translate({OX + AX - 60},{OY + row_y - 60}) scale(1.2)">{QSQ}</g>')
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "fish-diamond-rows-page.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "fish-diamond-rows-page.png"),
                 output_width=1080, output_height=1920)
print("fish-diamond-rows-page written")
