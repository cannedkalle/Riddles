#!/usr/bin/env python3
"""Riddle #4 — FISH diamond, three-row version v4 (Kai's idea, 2026-11-07).

v4: background FLAT (Kai, 2026-11-10 — the gradient was the assistant's
invention; backgrounds are now solid colours). bg-emerald-light is solid
#40BD7E (the theme anchor). Layout unchanged from v3 (grid-aligned).

v3: layout aligned to the grid element (Kai, 2026-11-07 — "Generate grid
(use and remove after finish) for consistent as well as manual layout
alignment as an element"). Every position is a multiple of 30 (the grid's
minor unit); the major 90px lines mark the 12 columns. The grid is used
to build and check this page, then REMOVED for the final — it is a
construction aid, never part of the design.

Formalized design, updated (Kai, 2026-11-07):
- riddle square is a FLAT colour plate — no outline (the 1080 square element
  has no stroke)
- question "?" optically centred in its coral square (ink centroid at the
  square's centre, not the bbox centre)
- top/bottom bands carry the series template, after 皆謎 / 一枚謎:
  top: series title 一枚謎 + quiz number No. 4 (+ English gloss)
  bottom: ANSWER box (write-in, 皆謎-style) + "by CannedKalle" credit
  All band text is Noto Serif CJK Bold — the Mincho-like serif 皆謎 uses
  for its title, number, ANSWER label and credit.

Rows (reading order clockwise from the top: red, yellow, white, blue;
each number indexes a letter of that quadrant's word):
  1/1/1/1     -> FISH (🐟)
  3/2/empty/5 -> ANT  (🐜)
  2/1/4/2     -> LICE (coral "?" square — the question)

Outputs: fish-diamond-rows-page-v4.svg/.png (1080x1920).
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
GRID = inner(os.path.join(EL, "grids", "grid-canvas.svg"))
OX, OY = 0, 420  # square spans the full width, centred vertically

SERIF = "Noto Serif CJK JP"
INK = "#101828"
PAPER = "#FFF6E5"
DEEP = "#0D5038"

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
    """Thick block arrow pointing right, ink. Shaft 30 tall, head 90 tall.
    Shaft x0 -> x0+120, head x0+120 -> x1 (both on the grid)."""
    hx = x0 + 120
    pts = [(x0, y - 15), (hx, y - 15), (hx, y - 45), (x1, y),
           (hx, y + 45), (hx, y + 15), (x0, y + 15)]
    points = " ".join(f"{OX + x:.0f},{OY + y:.0f}" for x, y in pts)
    return f'<polygon points="{points}" fill="#101828"/>'

def band_text(x, y, text, size, fill, spacing=None, opacity=None):
    attrs = (f'x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" '
             f'font-family="{SERIF}" font-weight="bold" font-size="{size}" fill="{fill}"')
    if spacing:
        attrs += f' letter-spacing="{spacing}"'
    if opacity:
        attrs += f' fill-opacity="{opacity}"'
    return f'<text {attrs}>{text}</text>'

ROWS = [
    (180, [1, 1, 1, 1], "🐟"),
    (540, [3, 2, None, 5], "🐜"),
    (900, [2, 1, 4, 2], None),
]
DIAG = 300
DX, AX = 360, 810  # 12u, 27u on the 30px grid

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
# ---- top band: series title + quiz number (皆謎-style) ----
S.append(band_text(540, 150, "一枚謎", 120, INK))
S.append(band_text(540, 270, "No. 4", 56, INK))
S.append(band_text(540, 330, "ONE-IMAGE RIDDLE", 30, INK, spacing=6, opacity=0.75))
# ---- riddle square ----
S.append(f'<g transform="translate({OX},{OY})">{SQUARE}</g>')
for row_y, numbers, emoji in ROWS:
    S += diamond(DX, row_y, DIAG, numbers)
    S.append(arrow(540, 720, row_y))
    if emoji is not None:
        S.append(f'<text x="{OX + AX}" y="{OY + row_y}" text-anchor="middle" '
                 f'dominant-baseline="central" font-family="Noto Color Emoji" '
                 f'font-size="100">{emoji}</text>')
    else:
        S.append(f'<g transform="translate({OX + AX - 60},{OY + row_y - 60}) scale(1.2)">{QSQ}</g>')
# ---- bottom band: ANSWER box + creator credit (皆謎-style) ----
S.append(band_text(540, 1560, "ANSWER", 36, PAPER, spacing=4))
S.append(f'<rect x="210" y="1620" width="660" height="90" fill="#FFFFFF" '
         f'stroke="{DEEP}" stroke-width="4"/>')
S.append(band_text(540, 1830, "by CannedKalle", 44, PAPER))
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "fish-diamond-rows-page-v4.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "fish-diamond-rows-page-v4.png"),
                 output_width=1080, output_height=1920)
print("fish-diamond-rows-page-v4 written (no grid, flat background)")
# check render: same page with the grid overlaid — verification only, not delivered
check = page.replace("</svg>", GRID + "</svg>")
cairosvg.svg2png(bytestring=check.encode(),
                 write_to=os.path.join(HERE, "fish-diamond-rows-page-v4-check.png"),
                 output_width=1080, output_height=1920)
print("check render with grid written (fish-diamond-rows-page-v4-check.png)")
