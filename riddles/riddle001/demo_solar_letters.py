#!/usr/bin/env python3
"""Solar Letters — UNIVERSE version (Kai's design, 2026-10-23).
Dark background, yellow sun, 8 slightly curved orbits.
Orbit i (top->bottom) = planet i in solar order; circle count = name length:
MERCURY 7, VENUS 5, EARTH 5, MARS 4, JUPITER 7, SATURN 6, URANUS 6, NEPTUNE 7.
No planet names printed. Numbered circles 1..8 mark which letters, in order:
1:U= MERCURY[5]  2:N= SATURN[6]  3:I= JUPITER[4]  4:V= VENUS[1]
5:E= EARTH[1]    6:R= MARS[3]    7:S= URANUS[6]   8:E= NEPTUNE[2]
Spells UNIVERSE, exactly one numbered circle per orbit.
"""
import math, random
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
BG = (8, 10, 26)
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
random.seed(7)

# star speckles
for _ in range(220):
    x, y = random.randint(0, W - 1), random.randint(0, H - 1)
    r = random.choice([1, 1, 1, 2])
    b = random.randint(90, 200)
    d.ellipse([x - r, y - r, x + r, y + r], fill=(b, b, int(b * 1.05)))

def font(size):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

# sun at top centre
cx, cy, R = W // 2, 235, 105
for rr, col in [(R + 30, (46, 38, 12))]:
    d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col)
d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(250, 204, 21))

counts = [7, 5, 5, 4, 7, 6, 6, 7]  # MERCURY..NEPTUNE
numbered = {0: (5, "1"),   # orbit idx, (letter position 1-based, digit)
            5: (6, "2"),
            4: (4, "3"),
            1: (1, "4"),
            2: (1, "5"),
            3: (3, "6"),
            6: (6, "7"),
            7: (2, "8")}

top, row_h = 520, 168
margin_x = 110
for i, n in enumerate(counts):
    y0 = top + i * row_h
    # quadratic bezier arc, slight downward bow
    x_start, x_end = margin_x, W - margin_x
    bow = 64  # control-point drop -> gentle curve
    pts = []
    steps = 120
    for s in range(steps + 1):
        t = s / steps
        x = (1 - t) ** 2 * x_start + 2 * (1 - t) * t * (W / 2) + t ** 2 * x_end
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (y0 + bow) + t ** 2 * y0
        pts.append((x, y))
    d.line(pts, fill=(120, 132, 180), width=3)
    # circles spread along the arc
    for j in range(n):
        t = (j + 1) / (n + 1)
        x = (1 - t) ** 2 * x_start + 2 * (1 - t) * t * (W / 2) + t ** 2 * x_end
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (y0 + bow) + t ** 2 * y0
        mark = numbered.get(i)
        if mark and mark[0] == j + 1:
            r = 37
            d.ellipse([x - r, y - r, x + r, y + r], fill=(250, 204, 21), outline=(255, 240, 190), width=3)
            f = font(40)
            tb = d.textbbox((0, 0), mark[1], font=f)
            d.text((x - (tb[2] - tb[0]) / 2 - tb[0], y - (tb[3] - tb[1]) / 2 - tb[1]),
                   mark[1], font=f, fill=(20, 16, 4))
        else:
            r = 24
            d.ellipse([x - r, y - r, x + r, y + r], outline=(210, 218, 245), width=3)

img.save("/home/hatch/workspace/single-image-riddle/demo-solar-letters-universe.png")
print("saved")
