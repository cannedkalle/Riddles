# Art style — "Flat Dark" (formalized 2026-11-06, Kai's direction; renamed 2026-11-07)

Flat, bold, children's-book pop on a dark background. Everything in the bank is built from the
elements in `elements.svg` — no new shapes per riddle, only new arrangements.

## Context-neutral (Kai, 2026-11-07)
The riddles are NOT all space-themed, so the sheets, the frame and the background carry no
theme: no star field, no sparkles, no scene. The dark background is a colour choice, not a
theme. Space motifs (`sun`, `moon`, `planet`, `star`, `sparkle`) exist in the library only as
*content* elements for riddles that need them — never as default decoration.

## Canvas
- Portrait 1080 × 1920 (TikTok). Safe area: 64 px margins.
- Background: dark `#080A1A` — plain, no star field, no decorative motifs. The background is
  a colour, never a scene.

## Palette (only these colours; max 3 accents per riddle page)
| Token | Hex | Use |
|---|---|---|
| `--bg` dark | `#080A1A` | page background |
| `--ink` | `#101828` | dark shapes on light surfaces only |
| `--paper` | `#FFF6E5` | cream — light surfaces, text on dark |
| `--blue` | `#93C5FD` | lit / a letter is sung / selected |
| `--yellow` | `#FACC15` | numbered circles, highlights |
| `--coral` | `#FB7185` | question badge, the "?" accent |
| `--mint` | `#6EE7B7` | third accent, validation / correct |
| `--lilac` | `#C4B5FD` | third accent, planets / mystery |
| `--grey` | `#D1D5DB` | neutral / rest / no letter |

## Shapes
- Flat fills, no gradients, no drop shadows (except the lit-tile glow halo, see below).
- Corners are round: radius ≈ 18% of the element's size.
- Line elements (arrows, checks, rings) use round caps/joins, stroke width ≈ 7 on a 100-unit box.
- No dark outlines on the night background (they vanish); elements separate by colour and by
  the cream outline where two bright fills touch.

## Fonts
- Display (numbers, single letters, titles): **Baloo 2** Bold — rounded, playful (Google Fonts, OFL).
- Body/labels: **Nunito** — same family feel, readable small.
- Drafts render in DejaVu Sans Bold until the fonts are embedded at production time; the
  geometry (sizes, spacing) does not depend on the font.

## Elements (`elements.svg` — one `<symbol>` each, 100 × 100 viewBox)
Shapes: `dot`, `circle-solid`, `ring`, `rounded-square`, `triangle`, `blob`, `star`, `sparkle`, `arc`.
Icons: `sun`, `moon`, `planet`, `note` (eighth note), `notes` (beamed pair), `question` (badge),
`arrow`, `heart`, `check`, `cross`, `cloud`.
States: `tile-lit` (blue + glow halo), `tile-rest` (grey, flat).
Lines & arrows (sheet 2): `line`, `line-dashed`, `line-dotted`, `line-wavy`, `line-zigzag`,
`line-double`, `line-thick`, `path-dots`, `arrow-right/left/up/down`, `arrow-curved`,
`arrow-uturn`, `arrow-double`, `arrow-elbow`, `arrow-circular`, `arrow-dashed`, `arrow-block`,
`chevron`, `chevron-double`, `spiral`, `swoosh`, `frame-rounded`, `frame-dashed`,
`frame-corners`, `bracket`, `divider-star`.

## Lines & arrows rule (added 2026-11-06)
Line weight 7 on a 100-unit box, round caps/joins. **Every arrowhead is computed from its
line's end tangent** (tip + direction → triangle), never hand-placed — the curved arrow
and music notes on sheet 1 were rebuilt for this after Kai flagged misaligned parts
(2026-11-06): the eighth-note flag now attaches along the stem's edge, beamed-note stems
meet the beam and the heads exactly, and the curved arrow's head sits on the curve.

## Composition rules
1. One idea per page; the puzzle's working elements are the biggest thing on it.
2. Colour means something: blue = "this one counts / is sung / is selected", grey = "rest",
   yellow = "look here / number", coral = the question. Never vary a colour decoratively
   inside the puzzle's working elements.
3. Nothing varies in a way that implies false information (no varying heights = pitch,
   no varying sizes = importance) unless that variation IS the encoding.
4. No text in the image except numbers that are part of the puzzle (e.g. Solar Letters
   numbering) and the "?" badge. The question lives in the video/caption.
5. Every riddle page is assembled from library elements only — if a page needs a new shape,
   add it to `elements.svg` first, then use it.

## Frame & background (Kai, 2026-11-07 — formalized design, supersedes the 984 frame;
flat + patterned, Kai 2026-11-10)
- Background: **emerald-light**, flat solid `#40BD7E` (element
  `bg-emerald-light.svg`; patterned version
  `bg-emerald-light-patterned.svg`).
- The background is **flat, never a gradient** (Kai, 2026-11-10 — the gradient
  was the assistant's invention; the style already said "flat fills, no
  gradients"). The patterned version carries a tone-on-tone key tessellation
  instead, after 皆謎's tone-on-tone walking-person pattern in its sidebar:
  a basketweave tessellation of 1×2 rectangles, each holding one key
  big-as-possible (Kai, 2026-11-10), the whole tessellation rotated 23.1°
  so no key is horizontal or vertical. Half the keys are mirrored so all
  teeth face up or right, never down or left. Pattern colour is a solid one
  shade from the fill — no transparency (a transparent overlay darkens where
  the 3 bow circles overlap). Flat, but not boring. The pattern shows only
  in the bands — the riddle square covers the middle, the way 皆謎's pattern
  lives in the sidebar, not the content area.
- The riddle square is the **brightest emerald tint** in the elements,
  `#E0F8E8` (element `square-emerald-pale-1080.svg`), and it is **as wide as
  the background — 1080 × 1080, no side margins**. TikTok canvas 1080 × 1920:
  square centred vertically, top/bottom bands 420 each.
- Square corners are sharp (r=0) and the square is a **flat colour plate —
  no outline** (Kai, 2026-11-07). No glow halo — the square, not the frame,
  is what the eye reads.
- For other ratios (16:9, 4:5, 1:1) the same square recentres and the bands shrink;
  the square never crops.
- Background palette (each colour in plain + patterned): **Navy**
  `#080A1A`, **Indigo** `#1E1B4B`, **Teal** `#062A2E`, **Plum** `#2A1530`,
  **Cream** `#FFF6E5` (light option), **Cream-emerald** `#E0F8E8`,
  **Emerald** `#168654`, **Emerald-light** `#40BD7E`.
- Key motif (element `motifs/motif-key.svg`): a minimal flat key — bow of 3
  small solid circles, shaft, 2 teeth — in emerald-deep `#0D5038`. One tint
  per background, `motifs/motif-key-<name>.svg`, in that background's pattern
  colour (one shade darker).

## Top / bottom bands — the series template (Kai, 2026-11-07; after 皆謎 / 一枚謎)
The bands carry the fixed series elements, the way 皆謎's sidebar does
(title, number, ANSWER box, organizer credit). All band text is
**Noto Serif CJK Bold** — the Mincho-like serif 皆謎 uses for its title,
number, ANSWER label and credit.
- Top band (ink on the light band): series title **一枚謎**, quiz number
  (**No. N**), English gloss **ONE-IMAGE RIDDLE** below.
- Bottom band (paper on the emerald band): **ANSWER** label + a white
  write-in **ANSWER box** (emerald-deep border), then the creator credit
  **by CannedKalle**.

## Question indicator (Kai, 2026-11-07)
The standard indicator for the thing to answer is a **coral square with a
white "?"** (element `indicators/question-square-<size>.svg`, sizes 120 / 240 /
480). Coral already means "the question" in the palette; the square makes it a
reusable element instead of a bare "?" glyph. Use it wherever an answer is
asked for — never a plain "?" on its own.

## Layout grid (Kai, 2026-11-07)
Element `grids/grid-canvas.svg` (1080 × 1920) — a construction aid, never part
of a design. Minor lines every 30 px, major lines every 90 px (the 12-column
grid), riddle-square boundary (y 420–1500) emphasized. Overlay it while
building a page (or in an editor for manual alignment), then **remove it for
the final**. Every position on a finished page sits on the grid: in riddle
#4, diamond centres x=360, arrows 540–720, answers x=810, row centres
y=180/540/900 (square-local), band text on 30 px steps, and the ANSWER box
spans exactly the row content's width (x 210–870).

## Theme colour (Kai, 2026-11-07)
EMERALD GREEN — first try. Anchor `#40BD7E`; ramp `#E0F8E8` → `#94DEAF` →
`#40BD7E` → `#168654` → `#0D5038` (from Kai's 5-option list; described there
as 'fresh, intellectual, and calm, without feeling dull'). One theme colour
for all riddles — it is the frame/template colour, the same in every riddle.
Other colours are used only when a puzzle needs them. (Gold was the
assistant's earlier pick, rejected by Kai; the measured 皆謎 ramp — cream
`#FFF1CA` → `#FDD961` → `#F2BA03` → `#B58B01` → `#785E01` — remains valid
as a reference, not as the decision.)

## Shapes are mainly sharp-cornered (Kai, 2026-11-07)
No rounded rectangles, no rounded joins — the 皆謎 language. Curves appear only
where the curve IS the shape (circle, ring, heart, arc, sparkle). The empty
riddle square in the elements set is sharp-cornered too.

## Do not invent without good reason (Kai, 2026-11-07)
Nothing on a riddle page exists without a reason. No invented decoration — the three dots
under the square were removed for this: they filled space, meant nothing, and a coloured
mark on a riddle page can be mistaken for a clue. If an element has no job (it does not
encode, frame, or explain), it does not go on the page. Empty space is the alternative,
and empty space is fine.

## No-stretch rule (Kai, 2026-11-07)
Never stretch shapes to fit the riddle square. Elements keep their natural proportions;
the content is centred in the square and the leftover space stays empty. Empty space /
padding is very common for riddles — it is not a flaw to fill. (Riddle #2's beat tiles were
rebuilt for this: 62 × 62 square tiles in a centred 284 × 906 grid, instead of 203 × 56
tiles stretched to fill the square.)

## Workflow (Kai, 2026-11-06)
1. Formalize style (this file) → 2. Generate basic elements as SVG → 3. Construct each
   riddle page from the elements → 4. When the bank reaches 10, review all pages together
   against this sheet and align → 5. Produce videos.
- Rendering note: the build scripts use `cairosvg` to make PNG previews; it lives in
  `/usr/local` (ephemeral) — reinstall with `pip install --break-system-packages cairosvg`
  if a fresh session reports it missing.
