#!/usr/bin/env python3
"""Riddle #4 candidate — FISH diamond (Kai's idea, 2026-11-07).
v2: quadrants marked 1-2-3-4 clockwise from the top (Kai, 2026-11-07) —
the numbers give the reading order: 1 Red (F), 2 Yellow (I),
3 White (S), 4 Blue (H).

NFPA 704 hazard diamond built from four `diamond` elements, tiling the big
diamond exactly: top coral (= red), right yellow, bottom paper (= white),
left blue. Reading the meanings clockwise from the top:
  Red -> Fire/Flammability (F) | Yellow -> Instability (I)
  White -> Special (S) | Blue -> Health (H)  =>  FISH.

TikTok page: bg-emerald frame, square-navy at (48, 468). Diamond 600x600
centred in the square. No numbers, no "?" (no question-badge element yet).

Outputs: fish-diamond-page-v2.svg/.png (1080x1920).
"""
import os
import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
EL = os.path.join(HERE, "elements")

def inner(path):
    s = open(path).read()
    return s.split(">", 1)[1].rsplit("</svg>", 1)[0]

def place(body, cx, cy, scale):
    return (f'<g transform="translate({cx - 50 * scale:.1f},{cy - 50 * scale:.1f}) '
            f'scale({scale:.3f})">{body}</g>')

W, H = 1080, 1920
BG = inner(os.path.join(EL, "backgrounds", "bg-emerald.svg"))
SQUARE = inner(os.path.join(EL, "squares", "square-navy.svg"))
DIGITS = {d: inner(os.path.join(EL, "digits", f"digit-{d}-black-m.svg")) for d in "1234"}
D = {
    "red":    inner(os.path.join(EL, "shapes", "diamond-coral-m.svg")),   # no true red; coral closest
    "yellow": inner(os.path.join(EL, "shapes", "diamond-yellow-m.svg")),
    "white":  inner(os.path.join(EL, "shapes", "diamond-paper-m.svg")),
    "blue":   inner(os.path.join(EL, "shapes", "diamond-blue-m.svg")),
}

OX, OY = 48, 468
CX, CY = OX + 492, OY + 492  # square centre on the page
# small diamond diagonal 300 -> scale 300/84; centres 150 from big centre
s = 300 / 84
S = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
S.append(BG)
S.append(f'<g transform="translate({OX},{OY})">{SQUARE}</g>')
S.append(place(D["red"],    CX,      CY - 150, s))  # top
S.append(place(D["yellow"], CX + 150, CY,      s))  # right
S.append(place(D["white"],  CX,      CY + 150, s))  # bottom
S.append(place(D["blue"],   CX - 150, CY,      s))  # left
# reading-order numbers 1-4 clockwise from the top, digit height ~70px
for num, (dx, dy) in {"1": (0, -150), "2": (150, 0), "3": (0, 150), "4": (-150, 0)}.items():
    S.append(place(DIGITS[num], CX + dx, CY + dy, 70 / 68))
S.append("</svg>")

page = "\n".join(S)
open(os.path.join(HERE, "fish-diamond-page-v2.svg"), "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(),
                 write_to=os.path.join(HERE, "fish-diamond-page-v2.png"),
                 output_width=1080, output_height=1920)
print("fish-diamond-page-v2.svg/.png written: F-I-S-H clockwise from top")
