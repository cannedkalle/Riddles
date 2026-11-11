#!/usr/bin/env python3
"""Riddle #4 — FISH diamond, validations version (Kai's idea, 2026-11-07).

Kai: "Can we add validations? E.g. 1/1/1/1 is fish. E.g. 3/2/empty/5 is
ant. Then ask - 2/1/4/2. Fish and ant use emojis."

The numbers are now INDICES, not reading-order markers. The four slots are
in the diamond's reading order (clockwise from the top: red, yellow,
white, blue). Each number indexes a letter of that quadrant's meaning word:
  red = FLAMMABILITY, yellow = INSTABILITY, white = SPECIAL, blue = HEALTH.
An empty quadrant contributes no letter.
  1/1/1/1    -> F(1) I(1) S(1) H(1) = FISH   (🐟)
  3/2/empty/5 -> A(3) N(2) - T(5)   = ANT    (🐜)
  2/1/4/2    -> L(2) I(1) C(4) E(2) = LICE   (the question)
This also settles the old flags: the ANT case pins the words
(FLAMMABILITY not FIRE — 3rd letter A; INSTABILITY not REACTIVITY —
2nd letter N) and the two validations together teach the rule, so the
riddle no longer needs the solver to already know the NFPA code.

Layout (one 984x984 riddle square): two validation diamonds on top, each
with its answer emoji below it; the question diamond below, larger, with
a coral "?" beside it. All diamonds in real NFPA colours; numerals in
Liberation Sans Bold at the standard proportion (NFPA 704 Fig. 9.1(b):
numeral height = 0.40 x placard side), scaled to each diamond's size.

Outputs: fish-diamond-validations-page.svg/.png (1080x1920).
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

# quadrant colours and number colours, in reading order (red, yellow, white, blue)
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
    # quadrant rhombi: big vertex + two adjacent edge-midpoints + centre
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
    # numerals at the standard proportion: H = 0.40 x placard side (A = diag/√2)
    font_size = round(0.40 * (diag / math.sqrt(2)) / 0.716)
    for (nx, ny), num, (_, numfill) in zip(centres, numbers, QUADS):
        if num is None:
            continue
        out.append(f'<text x="{OX + nx:.0f}" y="{OY + ny:.0f}" text-anchor="middle" '
                   f'dominant-baseline="central" font-family="Liberation Sans" '
                   f'font-weight="bold" font-size="{font_size}" '
                   f'fill="{numfill}">{num}</text>')
    return out

S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
S.append(f'<g transform="translate({OX},{OY})">{SQUARE}</g>')
# validations: 1/1/1/1 -> FISH, 3/2/empty/5 -> ANT
S += diamond(250, 210, 300, [1, 1, 1, 1])
S += diamond(734, 210, 300, [3, 2, None, 5])
for ex, emoji in [(250, "🐟"), (734, "🐜")]:
    S.append(f'<text x="{OX + ex}" y="{OY + 420}" text-anchor="middle" '
             f'dominant-baseline="central" font-family="Noto Color Emoji" '
             f'font-size="84">{emoji}</text>')
# question: 2/1/4/2 -> LICE
S += diamond(492, 710, 420, [2, 1, 4, 2])
S.append(f'<text x="{OX + 800}" y="{OY + 710}" text-anchor="middle" '
         f'dominant-baseline="central" font-family="Liberation Sans" '
         f'font-weight="bold" font-size="140" fill="#FB7185">?</text>')
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "fish-diamond-validations-page.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "fish-diamond-validations-page.png"),
                 output_width=1080, output_height=1920)
print("fish-diamond-validations-page written")
