#!/usr/bin/env python3
"""Riddle #2 — Alphabet Song beats (Kai's idea, 2026-11-06).
One box per beat of the alphabet song (Twinkle melody, 4/4, 12 bars x 4 beats = 48 beats).
1 = a letter is sung on this beat (light blue); 0 = no letter (word syllable or held note, light grey).
Bars (lyrics mapped to the Twinkle melody):
  1: A B C D            4: L M N(hold)
  2: E F G(hold)        5: O P Q R
  3: H I J K            6: S T U(hold)
  7: W X Y and          8: Z(hold, hold, hold)
  9: Now I know my     10: A B C(hold)     <- the repeat: 3 blues in a sea of grey
 11: Next time won't you 12: sing with me(hold)
Blue total = 28 (29 letters sung — 26 + A B C repeated — on 28 blue beats, because
N and O share one beat in LMNOP), grey = 20, total 48.
CORRECTION 2026-11-06 (Kai: "Isn't it LMNOP?"): the first version wrongly put a held N
at the end of bar 4 and O P in bar 5. LMNOP is compressed — N and O share a beat —
so bar 4 is all blue and everything after shifts: Q R S T in bar 5, U V held in bar 6,
W X Y and in bar 7, Z held in bar 8.
Generates both the SVG (source of truth, reusable style tokens in <style>)
and a PNG preview with identical geometry.
"""
from PIL import Image, ImageDraw

BEAT_MAP = [
    [1, 1, 1, 1],  # 1  A B C D
    [1, 1, 1, 0],  # 2  E F G (hold)
    [1, 1, 1, 1],  # 3  H I J K
    [1, 1, 1, 1],  # 4  L M N+O P  <- LMNOP: N and O share one beat ("elemenopee"); no held N
    [1, 1, 1, 1],  # 5  Q R S T
    [1, 1, 0, 0],  # 6  U V (hold, hold)
    [1, 1, 1, 0],  # 7  W X Y and  ("and" is not a letter: grey)
    [1, 0, 0, 0],  # 8  Z (hold, hold, hold)
    [0, 0, 0, 0],  # 9  Now I know my
    [1, 1, 1, 0],  # 10 A B C (hold)
    [0, 0, 0, 0],  # 11 Next time won't you
    [0, 0, 0, 0],  # 12 sing with me (hold)
]
assert len(BEAT_MAP) == 12 and all(len(r) == 4 for r in BEAT_MAP)
flat = [b for row in BEAT_MAP for b in row]
assert len(flat) == 48 and sum(flat) == 28, (len(flat), sum(flat))

# ---- layout (shared by SVG and PNG) ----
W, H = 1080, 1920
BOX_W, BOX_H = 200, 120
GAP_X, GAP_Y = 28, 18
PHRASE_GAP = 26            # extra gap after every 2 bars (one lyric phrase)
MARGIN_X = (W - (4 * BOX_W + 3 * GAP_X)) // 2
MARGIN_TOP = 76
BG, BLUE, GREY = "#080a1a", "#93c5fd", "#d1d5db"

def row_y(i):
    return MARGIN_TOP + i * (BOX_H + GAP_Y) + (i // 2) * PHRASE_GAP

def box_xy(i, j):
    return MARGIN_X + j * (BOX_W + GAP_X), row_y(i)

# ---- SVG ----
svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
svg.append('<style>')
svg.append('  :root { --bg: #080a1a; --blue: #93c5fd; --grey: #d1d5db; --radius: 18px; }')
svg.append('  .bg { fill: var(--bg); }')
svg.append('  .beat { rx: var(--radius); ry: var(--radius); }')
svg.append('  .letter { fill: var(--blue); }')
svg.append('  .rest { fill: var(--grey); }')
svg.append('</style>')
svg.append(f'<rect class="bg" width="{W}" height="{H}"/>')
svg.append('<g id="beat-grid">')
for i, row in enumerate(BEAT_MAP):
    svg.append(f'  <!-- bar {i + 1} -->')
    for j, b in enumerate(row):
        x, y = box_xy(i, j)
        cls = "letter" if b else "rest"
        svg.append(f'  <rect class="beat {cls}" x="{x}" y="{y}" width="{BOX_W}" height="{BOX_H}"/>')
svg.append('</g>')
svg.append('</svg>')
open("/home/hatch/workspace/single-image-riddle/riddle-02-alphabet-beats.svg", "w").write("\n".join(svg) + "\n")

# ---- PNG preview (same geometry) ----
img = Image.new("RGB", (W, H), (8, 10, 26))
d = ImageDraw.Draw(img)
for i, row in enumerate(BEAT_MAP):
    for j, b in enumerate(row):
        x, y = box_xy(i, j)
        col = (147, 197, 253) if b else (209, 213, 219)
        d.rounded_rectangle([x, y, x + BOX_W, y + BOX_H], radius=18, fill=col)
img.save("/home/hatch/workspace/single-image-riddle/riddle-02-alphabet-beats.png")
print(f"beats: {len(flat)}, blue: {sum(flat)}, grey: {48 - sum(flat)}")
print("svg + png written")
