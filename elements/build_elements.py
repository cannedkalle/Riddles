#!/usr/bin/env python3
"""Generate individual SVG elements for Kai to craft riddles in an image editor.
(Kai, 2026-11-07: assistant generates elements only, no design decisions.)

Every file is standalone: no <use> references, no CSS variables, plain attributes
only — drag straight into Figma / Illustrator / Inkscape.

Theme colour (Kai, 2026-11-07): EMERALD GREEN — first try. Anchor #40BD7E,
with the 5-step ramp from Kai's screenshot as its family. Other colours are
used only when a puzzle needs them. (Gold was the assistant's earlier pick
and was rejected by Kai — gold files removed.)

Shapes are mainly SHARP-cornered (Kai, 2026-11-07; the 皆謎 language): no rounded
rectangles, no rounded joins. Curves appear only where the curve IS the shape
(circle, ring, heart, arc, sparkle).

Outputs under ~/workspace/single-image-riddle/elements/:
  backgrounds/  bg-<name>.svg        1080 x 1920, flat solid + tone-on-tone "?" pattern
  squares/      square-<name>.svg    984 x 984 empty riddle square, sharp corners
  squares/      square-<name>-1080.svg  1080 x 1080 full-width riddle square
  shapes/       <shape>-<colour>-<size>.svg   sizes s=120, m=240, l=480 (transparent bg)
  digits/       digit-<d>-<colour>-<size>.svg  digits 0-9 as paths, same 3 sizes
  indicators/   question-square-<size>.svg  coral square + white "?", same 3 sizes
  grids/        grid-canvas.svg      1080 x 1920 layout grid (construction aid)
  INDEX.md      file list + naming convention

Digits are DejaVu Sans Bold glyph outlines rendered as SVG paths (STYLE.md:
drafts render in DejaVu Sans Bold until fonts are embedded) — no font
dependency in the files. Each digit is 68 units tall in the 100 x 100
viewBox, centred by its bounding box, like the circle's 68-unit diameter.
"""
import math, os
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- palette (STYLE.md tokens + measured 皆謎 gold ramp) ----
COLORS = {
    "paper":      "#FFF6E5",
    "blue":       "#93C5FD",
    "yellow":     "#FACC15",
    "coral":      "#FB7185",
    "mint":       "#6EE7B7",
    "lilac":      "#C4B5FD",
    "grey":       "#D1D5DB",
    "ink":        "#101828",
    # theme emerald ramp (from Kai's screenshot, 2026-11-07)
    "emerald-pale":  "#E0F8E8",
    "emerald-light": "#94DEAF",
    "emerald":       "#40BD7E",
    "emerald-dark":  "#168654",
    "emerald-deep":  "#0D5038",
}
THEME = "emerald"  # anchor #40BD7E

BACKGROUNDS = [  # name, flat fill, tone-on-tone pattern colour (Kai, 2026-11-10)
    ("navy",   "#080A1A", "#141B3D"),
    ("indigo", "#1E1B4B", "#312E81"),
    ("teal",   "#062A2E", "#0B4B50"),
    ("plum",   "#2A1530", "#4A1D4D"),
    ("cream",  "#FFF6E5", "#FDEED3"),
    ("cream-emerald", "#E0F8E8", "#94DEAF"),  # theme ramp, pale end
    ("emerald", "#168654", "#0D5038"),         # dark step — keeps it distinct
                                              # from emerald-light (see below)
    ("emerald-light", "#40BD7E", "#168654"),   # the theme anchor — the page
                                              # background (Kai, 2026-11-07)
]

# empty riddle square: name, panel fill, border colour — SHARP corners (rx 0)
SQUARES = [
    ("navy",   "#0E1330", COLORS["paper"]),
    ("indigo", "#232052", COLORS["lilac"]),
    ("teal",   "#0A3338", COLORS["mint"]),
    ("plum",   "#331A3A", COLORS["coral"]),
    ("cream",  "#FFFFFF", COLORS["ink"]),
    ("paper",  "#FFF6E5", COLORS["ink"]),
    ("ink",    "#101828", COLORS["paper"]),
    ("emerald", "#40BD7E", COLORS["emerald-deep"]),
    ("cream-emerald", "#E0F8E8", COLORS["emerald-deep"]),
]

# full-width riddle square (Kai, 2026-11-07): as wide as the background,
# no margins — 1080 x 1080, panel is the brightest emerald tint
SQUARES_FULL = [
    ("emerald-pale", "#E0F8E8", COLORS["emerald-deep"]),
]

SIZES = {"s": 120, "m": 240, "l": 480}

def star_points(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return " ".join(pts)

# shape bodies in a 100 x 100 viewBox; {c} = colour. Sharp corners throughout.
SHAPES = {
    "circle":    '<circle cx="50" cy="50" r="34" fill="{c}"/>',
    "ring":      '<circle cx="50" cy="50" r="32" fill="none" stroke="{c}" stroke-width="10"/>',
    "square":    '<rect x="16" y="16" width="68" height="68" fill="{c}"/>',
    "rectangle": '<rect x="10" y="26" width="80" height="48" fill="{c}"/>',
    "triangle":  '<polygon points="50,14 88,84 12,84" fill="{c}"/>',
    "diamond":   '<polygon points="50,8 92,50 50,92 8,50" fill="{c}"/>',
    "pentagon":  '<polygon points="50,10 89.9,39 74.7,86 25.3,86 10.1,39" fill="{c}"/>',
    "hexagon":   '<polygon points="50,10 86.4,31 86.4,73 50,94 13.6,73 13.6,31" fill="{c}"/>',
    "plus":      '<polygon points="38,10 62,10 62,38 90,38 90,62 62,62 62,90 38,90 38,62 10,62 10,38 38,38" fill="{c}"/>',
    "star":      f'<polygon points="{star_points(50, 52, 42, 18)}" fill="{{c}}"/>',
    "sparkle":   '<path d="M50 6 Q58 42 94 50 Q58 58 50 94 Q42 58 6 50 Q42 42 50 6 Z" fill="{c}"/>',
    "heart":     '<path d="M50 84 C20 62 12 40 26 27 C36 18 48 25 50 35 C52 25 64 18 74 27 C88 40 80 62 50 84 Z" fill="{c}"/>',
    "arc":       '<path d="M14 78 Q50 14 86 78" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round"/>',
}

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content + "\n")

counts = {}

# ---- backgrounds: 1080 x 1920, FLAT solid colour + small tone-on-tone pattern ----
# Kai, 2026-11-10: the gradient was the assistant's invention — nobody asked
# for it, and it contradicts the flat-fill language (皆謎 uses flat fills; the
# riddle square is a flat colour plate). So: one solid colour, plus a small
# repeating pattern like 皆謎's tone-on-tone walking people — flat, but not
# boring. The motif is a small "?" (the riddle's own symbol), staggered in a
# brick layout (240 x 240 tile, "?" at (60,60) and (180,180)), in the next
# ramp step at 40% opacity. It shows only in the bands — the riddle square
# covers the middle, the way 皆謎's pattern lives in the sidebar, not the
# content area.
_font = TTFont("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
_glyphset = _font.getGlyphSet()

def _qmark_transform(target_h):
    """Scale/centre for the '?' glyph at target_h px tall, centred at (0,0)."""
    glyph = _glyphset["question"]
    bpen = BoundsPen(_glyphset)
    glyph.draw(bpen)
    x0, y0, x1, y1 = bpen.bounds
    cx, cy, h = (x0 + x1) / 2, (y0 + y1) / 2, y1 - y0
    spen = SVGPathPen(_glyphset)
    glyph.draw(spen)
    d = spen.getCommands()
    k = target_h / h
    return d, k, cx, cy

_QD, _QK, _QCX, _QCY = _qmark_transform(28)

def _pattern_def(pat):
    q = (f'<path d="{_QD}" fill="{pat}" fill-opacity="0.4" '
         f'transform="translate(60,60) scale({_QK:.4f},{-_QK:.4f}) '
         f'translate({-_QCX:.1f},{-_QCY:.1f})"/>')
    q2 = q.replace("translate(60,60)", "translate(180,180)")
    return (f'<defs><pattern id="pat" width="240" height="240" '
            f'patternUnits="userSpaceOnUse">{q}{q2}</pattern></defs>')

for name, fill, pat in BACKGROUNDS:
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'
           + _pattern_def(pat)
           + f'<rect width="1080" height="1920" fill="{fill}"/>'
           + f'<rect width="1080" height="1920" fill="url(#pat)"/></svg>')
    write(os.path.join(HERE, "backgrounds", f"bg-{name}.svg"), svg)
counts["backgrounds"] = len(BACKGROUNDS)

# ---- empty riddle squares: 984 x 984, sharp corners, transparent outside ----
for name, fill, border in SQUARES:
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="984" height="984" viewBox="0 0 984 984">'
           f'<rect x="0" y="0" width="984" height="984" fill="{fill}" '
           f'stroke="{border}" stroke-width="6" stroke-opacity="0.4"/></svg>')
    write(os.path.join(HERE, "squares", f"square-{name}.svg"), svg)
counts["squares"] = len(SQUARES)

# ---- full-width riddle square: 1080 x 1080, flat colour plate, NO outline ----
# (Kai, 2026-11-07: remove the outline — the square is only a colour plate.)
for name, fill, border in SQUARES_FULL:
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1080 1080">'
           f'<rect x="0" y="0" width="1080" height="1080" fill="{fill}"/></svg>')
    write(os.path.join(HERE, "squares", f"square-{name}-1080.svg"), svg)
counts["squares_full"] = len(SQUARES_FULL)

# ---- shapes: every shape x every colour x 3 sizes ----
n_shapes = 0
for shape, body in SHAPES.items():
    for colour, hexv in COLORS.items():
        for size, px in SIZES.items():
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}" viewBox="0 0 100 100">'
                   + body.format(c=hexv) + '</svg>')
            write(os.path.join(HERE, "shapes", f"{shape}-{colour}-{size}.svg"), svg)
            n_shapes += 1
counts["shapes"] = n_shapes

# ---- digits: 0-9 as paths, white/black + emerald shades, same 3 sizes ----
# Colours as Kai asked (2026-11-07): white and black are literal #FFFFFF /
# #000000 (not the system's paper/ink) — swap if he meant the system neutrals.
DIGIT_COLORS = {
    "white": "#FFFFFF",
    "black": "#000000",
    "emerald-pale": "#E0F8E8",
    "emerald-light": "#94DEAF",
    "emerald": "#40BD7E",
    "emerald-dark": "#168654",
    "emerald-deep": "#0D5038",
}
DIGIT_NAMES = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]

def digit_body(glyph_name):
    """SVG path body for one digit, 68 units tall, centred in the 100 box."""
    glyph = _glyphset[glyph_name]
    bpen = BoundsPen(_glyphset)
    glyph.draw(bpen)
    x0, y0, x1, y1 = bpen.bounds
    cx, cy, h = (x0 + x1) / 2, (y0 + y1) / 2, y1 - y0
    k = 68 / h
    spen = SVGPathPen(_glyphset)
    glyph.draw(spen)
    d = spen.getCommands()
    return (f'<path d="{d}" fill="{{c}}" '
            f'transform="translate(50,50) scale({k:.4f},{-k:.4f}) '
            f'translate({-cx:.1f},{-cy:.1f})"/>')

n_digits = 0
for i, gname in enumerate(DIGIT_NAMES):
    body = digit_body(gname)
    for colour, hexv in DIGIT_COLORS.items():
        for size, px in SIZES.items():
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}" viewBox="0 0 100 100">'
                   + body.format(c=hexv) + '</svg>')
            write(os.path.join(HERE, "digits", f"digit-{i}-{colour}-{size}.svg"), svg)
            n_digits += 1
counts["digits"] = n_digits

# ---- question indicator: coral square with a white "?" (Kai, 2026-11-07) ----
# Standard indicator for the thing to answer. The "?" is a DejaVu Sans Bold
# outline (like the digits — no font dependency), 68 units tall, centred in
# the 100 box; the coral tile fills the whole 100 x 100.
def question_body():
    glyph = _glyphset["question"]
    bpen = BoundsPen(_glyphset)
    glyph.draw(bpen)
    x0, y0, x1, y1 = bpen.bounds
    cx, cy, h = (x0 + x1) / 2, (y0 + y1) / 2, y1 - y0
    k = 68 / h
    spen = SVGPathPen(_glyphset)
    glyph.draw(spen)
    d = spen.getCommands()
    # Optical centring (Kai, 2026-11-07: the "?" was not well centred).
    # Bbox-centring leaves the ink centroid ~7 units high in the 100 box:
    # the hook carries most of the ink and the dot is small, so the glyph
    # reads top-heavy. Shift down 7 units so the ink centroid sits at 50.
    return (f'<rect x="0" y="0" width="100" height="100" fill="{COLORS["coral"]}"/>'
            f'<path d="{d}" fill="#FFFFFF" '
            f'transform="translate(50,57) scale({k:.4f},{-k:.4f}) '
            f'translate({-cx:.1f},{-cy:.1f})"/>')

_qbody = question_body()
for size, px in SIZES.items():
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}" viewBox="0 0 100 100">'
           + _qbody + '</svg>')
    write(os.path.join(HERE, "indicators", f"question-square-{size}.svg"), svg)
counts["indicators"] = len(SIZES)

# ---- layout grid: 1080 x 1920 construction aid (Kai, 2026-11-07) ----
# Use it to align a page (overlay it while building, remove it for the
# final), and in an editor for manual alignment. Minor lines every 30px,
# major lines every 90px (the 12-column grid), and the riddle-square
# boundary (y 420–1500) emphasized. Emerald-deep, low opacity — visible
# on the pale square and the emerald background, never part of the design.
def _grid_path(coords, vertical):
    d = []
    for c in coords:
        if vertical:
            d.append(f"M{c} 0V1920")
        else:
            d.append(f"M0 {c}H1080")
    return " ".join(d)

_minor_v = _grid_path(range(30, 1080, 30), True)
_minor_h = _grid_path(range(30, 1920, 30), False)
_major_v = _grid_path(range(90, 1080, 90), True)
_major_h = _grid_path(range(90, 1920, 90), False)
_grid = COLORS["emerald-deep"]
_grid_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'
    f'<path d="{_minor_v}" stroke="{_grid}" stroke-width="1" stroke-opacity="0.12" fill="none"/>'
    f'<path d="{_minor_h}" stroke="{_grid}" stroke-width="1" stroke-opacity="0.12" fill="none"/>'
    f'<path d="{_major_v}" stroke="{_grid}" stroke-width="1.5" stroke-opacity="0.3" fill="none"/>'
    f'<path d="{_major_h}" stroke="{_grid}" stroke-width="1.5" stroke-opacity="0.3" fill="none"/>'
    f'<rect x="0" y="420" width="1080" height="1080" fill="none" '
    f'stroke="{_grid}" stroke-width="2" stroke-opacity="0.5"/></svg>')
write(os.path.join(HERE, "grids", "grid-canvas.svg"), _grid_svg)
counts["grids"] = 1

# ---- INDEX.md ----
lines = ["# Elements — individual SVGs for image editors",
         "",
         "Generated by `elements/build_elements.py`. Every file is standalone (no `<use>`,",
         "no CSS variables) — drag straight into Figma / Illustrator / Inkscape.",
         "",
         f"Theme colour: **emerald green** (`{COLORS['emerald']}`), first try — the",
         "5-step ramp from Kai's screenshot is its family: `#E0F8E8` → `#94DEAF` →",
         "`#40BD7E` → `#168654` → `#0D5038`. Other colours are used only when a",
         "puzzle needs them.",
         "",
         "Shapes are mainly sharp-cornered (no rounded rectangles, no rounded joins).",
         "Curves appear only where the curve IS the shape: circle, ring, heart, arc, sparkle.",
         "",
         "## Backgrounds (`backgrounds/`, 1080 × 1920)",
         "",
         "Flat solid colour, plus a small tone-on-tone `?` pattern (Kai,",
         "2026-11-10 — after 皆謎's tone-on-tone walking-person pattern). The",
         "pattern shows only in the bands; the riddle square covers the middle.",
         "",
         "| file | fill | pattern |",
         "|---|---|---|"]
for name, fill, pat in BACKGROUNDS:
    lines.append(f"| `bg-{name}.svg` | `{fill}` | `{pat}` at 40% |")
lines += ["",
          "## Empty riddle squares (`squares/`, 984 × 984, sharp corners, transparent outside)",
          "",
          "| file | panel | border |",
          "|---|---|---|"]
for name, fill, border in SQUARES:
    lines.append(f"| `square-{name}.svg` | `{fill}` | `{border}` at 40% |")
lines += ["",
          "## Full-width riddle square (`squares/`, 1080 × 1080, sharp corners)",
          "",
          "The riddle square (Kai, 2026-11-07): as wide as the background, no",
          "margins — panel is the brightest emerald tint. Flat colour plate,",
          "no outline (Kai, 2026-11-07).",
          "",
          "| file | panel |",
          "|---|---|"]
for name, fill, border in SQUARES_FULL:
    lines.append(f"| `square-{name}-1080.svg` | `{fill}` |")
lines += ["",
          "## Shapes (`shapes/`, transparent background)",
          "",
          "Naming: `<shape>-<colour>-<size>.svg` — sizes `s` = 120, `m` = 240, `l` = 480.",
          "SVG scales losslessly, so any size works in the editor; the three sizes are",
          "just ready-made starting points.",
          "",
          "| shape | colours |",
          "|---|---|"]
for shape in SHAPES:
    lines.append(f"| `{shape}` | paper, blue, yellow, coral, mint, lilac, grey, ink, emerald-pale, emerald-light, emerald, emerald-dark, emerald-deep |")
lines += ["",
          "## Digits (`digits/`, transparent background)",
          "",
          "Naming: `digit-<d>-<colour>-<size>.svg` — sizes `s` = 120, `m` = 240, `l` = 480.",
          "Glyphs are DejaVu Sans Bold outlines as paths (no font needed); each digit",
          "is 68 units tall in the 100 × 100 viewBox, centred by its bounding box.",
          "",
          "Colours: white `#FFFFFF`, black `#000000`, emerald-pale `#E0F8E8`,",
          "emerald-light `#94DEAF`, emerald `#40BD7E`, emerald-dark `#168654`,",
          "emerald-deep `#0D5038`.",
          "",
          "## Question indicator (`indicators/`, transparent background)",
          "",
          "Naming: `question-square-<size>.svg` — sizes `s` = 120, `m` = 240, `l` = 480.",
          "A coral `#FB7185` square with a white `?` — the standard indicator for",
          "the thing to answer (Kai, 2026-11-07). The `?` is a DejaVu Sans Bold",
          "outline (no font needed), 68 units tall in the 100 × 100 viewBox.",
          "",
          "## Layout grid (`grids/`, transparent background)",
          "",
          "`grid-canvas.svg` — 1080 × 1920. A construction aid, not part of any",
          "design: overlay it while building a page (or in an editor for manual",
          "alignment), then remove it for the final. Minor lines every 30 px,",
          "major lines every 90 px (the 12-column grid), riddle-square boundary",
          "(y 420–1500) emphasized. Emerald-deep `#0D5038`, low opacity.",
          "",
          f"Counts: {counts['backgrounds']} backgrounds, {counts['squares']} squares, "
          f"{counts['squares_full']} full-width riddle square, "
          f"{counts['shapes']} shapes "
          f"({len(SHAPES)} shapes × {len(COLORS)} colours × {len(SIZES)} sizes), "
          f"{counts['digits']} digits "
          f"(10 digits × {len(DIGIT_COLORS)} colours × {len(SIZES)} sizes), "
          f"{counts['indicators']} question indicators, "
          f"{counts['grids']} layout grid.",
          ""]
open(os.path.join(HERE, "INDEX.md"), "w").write("\n".join(lines))

# ---- validate: every file parses as XML ----
bad = []
for root, _, files in os.walk(HERE):
    for fn in files:
        if fn.endswith(".svg"):
            try:
                ET.parse(os.path.join(root, fn))
            except ET.ParseError as e:
                bad.append((os.path.join(root, fn), str(e)))
print(counts)
print("BAD:", bad if bad else "none — all SVGs parse")
