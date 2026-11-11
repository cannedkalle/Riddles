#!/usr/bin/env python3
"""Riddle #2 page — Alphabet Song beats, built from Flat Dark elements
(Kai's workflow step 3: construct the riddle page from the elements).

Beat map is the CORRECTED one (concept-02-alphabet-beats.md): 48 beats,
28 blue / 20 grey. N and O share one beat in LMNOP, so bar 4 is all blue
and everything after shifts (Q R S T in bar 5, U V held in bar 6,
W X Y + "and" in bar 7, Z held in bar 8).

Outputs:
  riddle-02-square.svg  — the riddle itself, 984 x 984 (source of truth)
  riddle-02-page.svg    — TikTok page, 1080 x 1920: Navy frame + square
  riddle-02-page.png    — PNG preview of the page

Style tokens (STYLE.md): blue #93C5FD = a letter is sung (lit tile: blue
+ 35%-opacity glow halo, per the tile-lit library element); grey #D1D5DB
= rest (flat tile-rest). No text, no letters, no "?" in the square yet —
the question marker is still an open decision (concept note, Q3).
Frame: Navy gradient #080A1A -> #141B3D, panel #0E1330, border paper
40%, glow halo — context-neutral, reused verbatim from
style/build_frame.py so the frame stays identical. (The three dots that
used to sit under the square were removed 2026-11-07: invented decoration
with no good reason, and a coloured mark on a riddle page can be mistaken
for a clue.)

No-stretch rule (Kai, 2026-11-07): tiles keep their natural square shape
(62 x 62, as the library tile); the grid is centred in the square and the
leftover space stays empty. Never stretch shapes to fill the square —
empty space / padding is normal for riddles.
"""
import os
import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
STYLE = os.path.join(HERE, "style")

BEAT_MAP = [
    [1, 1, 1, 1],  # 1  A B C D
    [1, 1, 1, 0],  # 2  E F G (hold)
    [1, 1, 1, 1],  # 3  H I J K
    [1, 1, 1, 1],  # 4  L M N+O P  (LMNOP: N and O share one beat)
    [1, 1, 1, 1],  # 5  Q R S T
    [1, 1, 0, 0],  # 6  U V (hold, hold)
    [1, 1, 1, 0],  # 7  W X Y and
    [1, 0, 0, 0],  # 8  Z (hold, hold, hold)
    [0, 0, 0, 0],  # 9  Now I know my
    [1, 1, 1, 0],  # 10 A B C (hold)
    [0, 0, 0, 0],  # 11 Next time won't you
    [0, 0, 0, 0],  # 12 sing with me (hold)
]
assert len(BEAT_MAP) == 12 and all(len(r) == 4 for r in BEAT_MAP)
flat = [b for row in BEAT_MAP for b in row]
assert len(flat) == 48 and sum(flat) == 28, (len(flat), sum(flat))

BLUE, GREY = "#93C5FD", "#D1D5DB"
PANEL = "#0E1330"
PAPER, SUN, CORAL = "#FFF6E5", "#FACC15", "#FB7185"

# ---- square grid geometry (square-local coords, 0..984) ----
# Natural square tiles, grid centred; leftover space stays empty (no-stretch rule).
SQ = 984
TILE = 62                        # square tile, library proportions
RX = 11                          # ~18% of tile
GAP = 12
PHRASE_GAP = 18                  # extra gap between bar pairs (after bars 2,4,6,8,10)
GRID_W = 4 * TILE + 3 * GAP                        # 284
GRID_H = 12 * TILE + 6 * GAP + 5 * PHRASE_GAP     # 906
PAD_X = (SQ - GRID_W) / 2                          # 350
PAD_Y = (SQ - GRID_H) / 2                          # 39

def fmt(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")

def row_y(i):
    return PAD_Y + i * (TILE + GAP) + (i // 2) * (PHRASE_GAP - GAP)

def grid_tiles():
    out = ['<g id="beat-grid">']
    for i, row in enumerate(BEAT_MAP):
        out.append(f'  <!-- bar {i + 1} -->')
        y = row_y(i)
        for j, b in enumerate(row):
            x = PAD_X + j * (TILE + GAP)
            if b:
                # tile-lit: glow halo (blue, 35%) + solid blue tile
                out.append(
                    f'  <rect x="{fmt(x - 8)}" y="{fmt(y - 8)}" width="{fmt(TILE + 16)}" '
                    f'height="{fmt(TILE + 16)}" rx="18" fill="{BLUE}" opacity="0.35"/>')
                out.append(
                    f'  <rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(TILE)}" '
                    f'height="{fmt(TILE)}" rx="{RX}" fill="{BLUE}"/>')
            else:
                # tile-rest: flat grey
                out.append(
                    f'  <rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(TILE)}" '
                    f'height="{fmt(TILE)}" rx="{RX}" fill="{GREY}"/>')
    out.append('</g>')
    return "\n".join(out)

def square_svg():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{SQ}" height="{SQ}" viewBox="0 0 {SQ} {SQ}">']
    s.append('<style>:root { --blue: #93C5FD; --grey: #D1D5DB; }</style>')
    s.append(f'<rect width="{SQ}" height="{SQ}" rx="48" fill="{PANEL}"/>')
    s.append(grid_tiles())
    s.append('</svg>')
    return "\n".join(s)

# ---- frame (verbatim geometry from style/build_frame.py) ----
W, H = 1080, 1920
SQ_X, SQ_Y = 48, (H - SQ) // 2  # 48, 468

def page_svg():
    sq = square_svg()
    # strip the outer <svg> wrapper, keep the square's inner content
    body = sq.split(">", 1)[1].rsplit("</svg>", 1)[0]
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    p.append('<defs><linearGradient id="bg-navy" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0" stop-color="#080A1A"/><stop offset="1" stop-color="#141B3D"/>'
             '</linearGradient></defs>')
    p.append(f'<rect width="{W}" height="{H}" fill="url(#bg-navy)"/>')
    p.append(f'<rect x="{SQ_X - 20}" y="{SQ_Y - 20}" width="{SQ + 40}" height="{SQ + 40}" rx="64" fill="{BLUE}" opacity="0.14"/>')
    p.append(f'<svg x="{SQ_X}" y="{SQ_Y}" width="{SQ}" height="{SQ}" viewBox="0 0 {SQ} {SQ}">{body}</svg>')
    p.append(f'<rect x="{SQ_X}" y="{SQ_Y}" width="{SQ}" height="{SQ}" rx="48" fill="none" stroke="{PAPER}" stroke-width="6" stroke-opacity="0.4"/>')
    p.append('</svg>')
    return "\n".join(p)

sq_path = os.path.join(HERE, "riddle-02-square.svg")
pg_path = os.path.join(HERE, "riddle-02-page.svg")
png_path = os.path.join(HERE, "riddle-02-page.png")
open(sq_path, "w").write(square_svg() + "\n")
page = page_svg()
open(pg_path, "w").write(page + "\n")
cairosvg.svg2png(bytestring=page.encode(), write_to=png_path,
                 output_width=1080, output_height=1920)
print(f"beats: {len(flat)}, blue: {sum(flat)}, grey: {48 - sum(flat)}")
print(f"tile: {TILE} x {TILE}, grid {GRID_W} x {GRID_H} centred (pad {fmt(PAD_X)} x {fmt(PAD_Y)})")
print("riddle-02-square.svg, riddle-02-page.svg/.png written")
