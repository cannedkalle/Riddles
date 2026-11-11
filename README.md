# Riddles — elements

The reusable SVG element library for the single-image riddle series
(一枚謎, "one-image mystery") — the building blocks Kai's riddles are
crafted from. No riddles are stored here; only the elements.

## What's here

- `elements/` — the library. Every file is a standalone SVG (no `<use>`,
  no CSS variables), so it opens directly in Figma, Illustrator or
  Inkscape.
  - `backgrounds/` — 16 full-page backgrounds, 1080 × 1920: 8 plain
    (flat solid colour) + 8 patterned (flat solid + tone-on-tone key
    tessellation, Kai's own Figma arrangement — see
    `elements/figma-pattern-template.svg`).
  - `motifs/` — the key motif behind the patterned backgrounds (bow of
    3 small solid circles, shaft, 2 teeth): `motif-key.svg` (default,
    emerald-deep) plus one tint per background, `motif-key-<name>.svg`,
    in that background's pattern colour (only slightly darker/lighter
    than the fill).
  - `squares/` — 11 full-width 1080 × 1080 riddle-square plates
    (one per background fill, plus white and a very light emerald
    `#EEFBF3`; the 984 × 984 squares were removed, Kai 2026-11-10).
  - `shapes/` — 507 shapes (13 shapes × 13 colours × 3 sizes).
  - `digits/` — 210 digits (0–9 × 7 colours × 3 sizes), drawn as
    outlines so they need no font.
  - `indicators/` — the coral square + white `?`, the standard
    "answer here" marker, in 3 sizes.
  - `grids/` — `grid-canvas.svg`, the 1080 × 1920 layout grid. A
    construction aid only: overlay it while building a page (or in an
    editor for manual alignment), then **remove it for the final**.
  - `build_elements.py` — the generator. `INDEX.md` — the file list.
- `STYLE.md` — the style guide: the Flat Dark palette and its colour
  meanings, the frame and the top/bottom band template, the question
  indicator, and the layout grid.

## Rules the elements carry

- **Real things are shown as they are**, never recoloured to fit the
  palette (an NFPA diamond keeps its real red, blue, yellow and white).
- **Colour means something**: blue = this one counts, grey = rest,
  yellow = look here, coral = the question. Nothing varies in a way
  that implies false information.
- **Shapes are mainly sharp-cornered**; curves only where the curve
  *is* the shape. Nothing on a page without a reason. Never stretch
  a shape.
- **Theme colour is emerald green** (anchor `#40BD7E`); other colours
  only when a puzzle needs them.

## Regenerating

```sh
cd elements
python3 build_elements.py   # needs fonttools (pip install fonttools)
```

This rebuilds every SVG and `INDEX.md` from the single generator, so
the library stays consistent. The contact-sheet PNG previews are not
stored here — regenerate them from the SVGs when needed.
