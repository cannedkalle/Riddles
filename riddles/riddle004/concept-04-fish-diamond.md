# Concept: FISH diamond (Kai's idea, 2026-11-07) — slot #4 candidate

## The idea (Kai)
Make the answer FISH from the NFPA 704 hazard-diamond colour code:
- Red — Flammability (also called Fire)
- Blue — Health
- Yellow — Instability (also called Reactivity)
- White — Special

## Mechanism (verified)
NFPA diamond layout: red top, blue left, yellow right, white bottom.
First letters of the meanings, read clockwise from the top:
- Red → **F**ire / Flammability → F
- Yellow → **I**nstability → I
- White → **S**pecial → S
- Blue → **H**ealth → H
→ **FISH**.

Robust to ordering: even read in Kai's listed order (Red, Blue, Yellow,
White → F, H, I, S), the letters anagram to FISH and nothing else — no
common English word besides FISH can be made from F, H, I, S. So the
answer does not depend on the solver finding the clockwise order.

## Review flags (for Kai)
1. **Knowledge load.** The riddle depends on knowing the NFPA colour code —
   specialised (fire safety / chemistry) knowledge, not general knowledge.
   The diamond shape is widely recognised (chemical containers, labs,
   trucks), but which colour means what is not common knowledge. Against
   the project's bar (light wordplay / common knowledge, no trivia or
   jargon), this is the main question. Kai's call.
2. **Instability vs Reactivity fork.** The answer needs Yellow =
   Instability (I). If a solver uses the other name, Reactivity (R), the
   letters are F, R, S, H — no word. The solver is steered only because
   FISH is the one word that fits; a solver who knows the code as
   "reactivity" gets stuck first. Instability is the NFPA official term
   and the name Kai listed first.
3. **No hint / validation case.** Unlike #1 (planet counts) and #2 (the
   ABC repeat), this is a single image with no internal validation case —
   the solver either recognises the code or doesn't. The structure is
   "recognise the symbol → read the letters", not "guess a rule → validate
   it against a hint".
4. **Materials.** Built from elements only: four `diamond` shapes tile the
   big diamond (top coral, right yellow, bottom paper, left blue). Two
   gaps: there is no true red in the element set — coral `#FB7185` is the
   closest (reads pink-red); and there is no "?" badge element, so the
   demo has no question marker (same open Q3 as riddle #2).

## Demo
`fish-diamond.py` → `fish-diamond-page.svg/.png` (TikTok page: bg-emerald
frame, square-navy, diamond centred, 600 × 600). Schematic only — Kai
crafts the final art.

## v2 (2026-11-07) — quadrants marked 1-2-3-4
Kai: "Mark 1,2,3,4". Numbers placed clockwise from the top, giving the
reading order: 1 Red (F), 2 Yellow (I), 3 White (S), 4 Blue (H). Built
from the digit elements — superseded by v3, never shown.

## v3 (2026-11-07) — real things don't use elements
Kai: "For real things, we don't use elements." The NFPA diamond is a real
thing, so v3 (`fish-diamond-v3.py` → `fish-diamond-page-v3.svg/.png`)
draws it faithfully with its REAL colours — red `#ED1C24`, blue `#0057A8`,
yellow `#FFD200`, white `#FFFFFF` (standard digital NFPA rendering) — not
the palette's coral / light blue / paper approximations. Numbers are plain
text in the NFPA manner (white on red/blue, black on yellow/white), with a
thin white outline as on a real sign. The frame stays the template
(bg-emerald + square-navy from elements); the rule is about the riddle's
content, not the frame. Standing rule: real objects are shown as they are,
never recoloured to fit the palette (same as the 皆謎 finding).

## v4 (2026-11-07) — numbers in the real sign's font and size
Kai: "Numbers should be in the same font and size as the real sign."
Measured from a photo of a real NFPA label (hydrofluosilicic acid sign,
Wikimedia): the red quadrant's "0" is 71px tall against a quadrant
diagonal (vertex → centre) of 272px — ratio 0.26. Font is a grotesque
bold sans (Arial/Helvetica Bold style); the local match is Liberation
Sans Bold (metrically identical to Arial Bold). Applied: font-size 108
on our 300px quadrants → digits ~78px (rendered 73px, ratio 0.24 —
measured on the v4 PNG). v3's DejaVu Sans Bold at 72 (~52px) was too
small and the wrong face. `fish-diamond-v4.py` →
`fish-diamond-page-v4.svg/.png`. SUPERSEDED by v5: the photo was a small
container LABEL, whose numbers are proportionally reduced — the wrong
reference (Kai's correction).

## v5 (2026-11-07) — dimensions from the standard itself
Kai: "You should find a real sign. Understand the dimension compared to
the sign." Source: NFPA 704 (2007 Edition), Figure 9.1(b) "Dimensions of
NFPA 704 Placard and Numerals" (full text via archive.org). Its dimension
table (mm, five sizes, H = numeral height, W = numeral width,
T = stroke, A = placard side, B = quadrant side):
  25/18/4/64/32 · 51/36/8/127/64 · 76/53/12/191/95 · 102/71/16/254/127 ·
  152/107/24/381/191.
Ratios constant across all five rows: H = 0.40 × A (= 0.80 × B
= 0.56 × quadrant diagonal); W = 0.70 × H; T = 0.16 × H. The standard
also says "Style of numerals shown is optional" (no mandated font) and
Figure 9.1(c) gives only legibility MINIMUMS (e.g. 1" numerals at 50 ft),
which are much smaller than the design proportion — not the target.
Applied to our diamond (overall diagonal 600, placard side
A = 600/√2 = 424): numeral height H = 0.40 × 424 = 170px, font-size
237 (Liberation Sans Bold cap height 0.716 em). Rendered "1" measures
163px (ratio 0.54) — verified on the v5 PNG. `fish-diamond-v5.py` →
`fish-diamond-page-v5.svg/.png`.

## Validations (2026-11-07) — numbers become indices
Kai: "Can we add validations? E.g. 1/1/1/1 is fish. E.g. 3/2/empty/5 is
ant. Then ask - 2/1/4/2. Fish and ant use emojis."
The numbers change role: they are no longer reading-order markers, they
are INDICES. The four slots are in the diamond's reading order (clockwise
from the top: red, yellow, white, blue). Each number indexes a letter of
that quadrant's meaning word; an empty quadrant contributes no letter:
  red = FLAMMABILITY, yellow = INSTABILITY, white = SPECIAL, blue = HEALTH.
  1/1/1/1     -> F(1) I(1) S(1) H(1) = FISH
  3/2/empty/5 -> A(3) N(2) - T(5)    = ANT
  2/1/4/2     -> L(2) I(1) C(4) E(2) = LICE (the question)
This settles all three review flags: the ANT case pins the words
(FLAMMABILITY not FIRE — 3rd letter A; INSTABILITY not REACTIVITY —
2nd letter N), and the two validations together teach the rule, so the
solver no longer needs to already know the NFPA code — the hint cases
are the teacher. All three answers are animals (fish, ant, lice).
Layout (one 984 square): two validation diamonds on top, each with its
answer emoji below it (🐟, 🐜 — Noto Color Emoji, rendered as text);
the question diamond below, larger, with a coral "?" beside it. No "="
signs — pairing is by vertical alignment. Numerals keep the standard
proportion (H = 0.40 × placard side) scaled to each diamond's size.
Open: no lice emoji exists, so the question's reveal would be the word
LICE (or 🐛 as a stand-in — Kai's call). `fish-diamond-validations.py` →
`fish-diamond-validations-page.svg/.png`. SUPERSEDED by the three-row
version below.

## Formalized design + three rows (2026-11-07)
Kai: "Let's formalize design: background go one tint brighter; riddle
square is brightest emerald tint in elements; riddle square is as wide as
the background, no margins; generate a coral square with questionmark as
the standard indicator to answer. Make them in three rows same format.
Use diamond, arrow, emoji design."
- Background: bg-emerald-light (`#94DEAF → #40BD7E`), one tint brighter
  than bg-emerald. New element in the library.
- Riddle square: `square-emerald-pale-1080.svg` — panel `#E0F8E8`
  (brightest emerald tint), 1080 × 1080, full width, no side margins,
  centred vertically on the 1080 × 1920 canvas (bands 420 each). New
  element in the library. This supersedes the old 984 frame (r=48, glow
  halo) in STYLE.md; riddles #1/#2 pages still use the old frame and will
  need rebuilding at the bank review.
- Question indicator: `indicators/question-square-<size>.svg` (120/240/480)
  — coral `#FB7185` square, white "?" (DejaVu Sans Bold outline, no font
  dependency). The standard indicator for the thing to answer; never a
  bare "?" on its own. New element in the library.
- Three rows, same format: diamond → thick block arrow (ink, the 皆謎
  language) → emoji / question square. Row centres y = 180/540/900
  (square-local); diamonds 300 diagonal, arrows 560–720, answers at x=820.
  `fish-diamond-rows.py` → `fish-diamond-rows-page.svg/.png`. SUPERSEDED
  by the v2 page below.

## Style control v2 (2026-11-07)
Kai: "Remove outlines of riddle square. Make it flat as only color
plates. Question mark is not well centered in the coral square.
Top/bottom space: by CannedKalle, Quiz number, other sensible elements.
Please refer to 皆谜 and 一枚謎."
- Riddle square: flat colour plate, no outline (the 1080 square element
  lost its stroke; generator + INDEX.md + STYLE.md updated).
- "?" optical centring: bbox-centring left the ink centroid ~7 units high
  (the hook carries the ink, the dot is small), so the "?" read top-heavy.
  The element now shifts the glyph down 7 units so the ink centroid sits
  at the square's centre — measured on the v2 page: centroid (820.9, 1320.5)
  vs square centre (820, 1320).
- Bands carry the series template, after 皆謎 (title, number, ANSWER box,
  organizer credit) and 一枚謎 (the number): top band — series title 一枚謎
  + "No. 4" + gloss "ONE-IMAGE RIDDLE" (ink); bottom band — "ANSWER" label
  + white write-in ANSWER box (emerald-deep border) + "by CannedKalle"
  (paper). All band text in Noto Serif CJK Bold (Mincho-like, as 皆謎
  uses serif for these). The 一枚謎 title uses the JP/TC form 謎 (not the
  simplified 谜). `fish-diamond-rows-v2.py` →
  `fish-diamond-rows-page-v2.svg/.png`. SUPERSEDED by the grid-aligned v3
  below.

## Layout grid (2026-11-07)
Kai: "Generate grid (use and remove after finish) for consistent as well
as manual layout alignment as an element."
- Element `grids/grid-canvas.svg` (1080 × 1920, in the library): minor lines
  every 30 px, major lines every 90 px (the 12-column grid), riddle-square
  boundary (y 420–1500) emphasized; emerald-deep, low opacity. Overlay it
  while building (or in an editor for manual alignment), remove it for the
  final — it is a construction aid, never part of the design.
- v3 re-aligned every position to the grid (all multiples of 30): diamond
  centres x=360, arrows 540–720 (shaft 540–660, head 660–720), answers
  x=810, row centres y=180/540/900; band text at y=150/270/330 (top) and
  1560/1620–1710/1830 (bottom); the ANSWER box narrowed to 660 wide so it
  spans exactly the row content (x 210–870). Verified on the check render
  (grid overlaid), then the grid was removed for the final.
  `fish-diamond-rows-v3.py` → `fish-diamond-rows-page-v3.svg/.png`
  (final, no grid) + `fish-diamond-rows-page-v3-check.png` (check render,
  grid overlaid — verification only, not delivered). SUPERSEDED by the
  flat + patterned v5 below.

## Flat background + pattern (2026-11-10)
Kai: "Why does the background has gradient?" / "Who told you to do that?"
— the gradient was the assistant's invention, never Kai's direction, and it
contradicted the style's own "flat fills, no gradients" rule. Flattened.
Kai: "Besides — background of 皆謎 has small patterns. We should do similar
things to make the background flat but not boring."
- Backgrounds are now one flat solid colour + a small tone-on-tone `?`
  pattern (the riddle's own symbol), staggered in a brick layout (240 x 240
  tile, `?` at (60,60) and (180,180), 28px tall, next ramp step at 40%
  opacity) — after 皆謎's tone-on-tone walking-person pattern. The pattern
  shows only in the bands; the riddle square covers the middle.
- bg-emerald-light is solid `#40BD7E` (the theme anchor) with the pattern in
  `#168654`. bg-emerald flattened to the dark step `#168654` so it stays
  distinct from emerald-light. All 8 backgrounds distinct, all flat.
  `fish-diamond-rows-v5.py` → `fish-diamond-rows-page-v5.svg/.png`
  (final, no grid) + check render. v3/v4 superseded, never shown.
