# Reconstruction test — riddle #1 Solar Letters, from elements only

Kai, 2026-11-07. Builder: `solar-letters-reconstruction.py` →
`solar-letters-reconstruction.svg/.png` (1080×1920). Geometry copied verbatim
from the original demo (`demo_solar_letters.py`): same sun position, same
Bézier arcs, same circle positions, same numbered spots (1=Mercury#5 …
8=Neptune#2). Only the drawing uses elements — no custom shapes.

## What worked (smart use)
- **Background**: `bg-navy` as-is.
- **Sun**: `circle-yellow` — exact colour match (`#FACC15`).
- **Sun halo**: `circle-ink` at 50% opacity behind the sun. Compromise: the
  original halo was dark olive; this is a dark navy glow. Reads fine.
- **Letter circles**: `ring-grey` — colour near-exact (`#D1D5DB` vs the
  original `#D2DAF5`). Compromise: the ring's stroke is proportionally thick
  (~6.5px at this size vs the original 3px outline). Reads as hollow circles,
  just bolder.
- **Numbered discs**: `circle-yellow` — exact colour, right size. They stay
  yellow even under the emerald theme: per the style system yellow means
  "look here / numbering", and emerald is the frame/template colour. No conflict.

## What's missing
1. **Orbit lines — the 8 thin slightly-bowed lines.** No line element exists
   in `elements/` at all. Design sheet 2 defined lines and arrows, but they
   were never exported as individual elements. The rows still read (the eye
   connects the circles), but the original has lines. Expand: export the
   design-sheet-2 lines as elements (straight, curved, dashed…), or at least
   one thin curved line.
2. **Digits 0–9 — CRITICAL.** The gold discs need 1–8; without digits the
   riddle cannot be solved — the discs mark *which* circles but give no
   *order*. No text or numeral element exists in the set. This cannot be
   faked with shapes. Expand: digit elements 0–9 (ink and paper, to sit on
   gold discs), plus the "?" badge from the library.
3. **(Minor) Thin-outline circle.** The ring's fixed stroke ratio makes small
   hollow circles chunky. A dedicated thin-ring would match the original.
   Acceptable as-is — judgement call, not a blocker.

## Layout note (not an element gap)
The original is a full 1080×1920 portrait page, not a 984×984 square.
Fitting it into the square would shrink everything ~40% and hurt legibility
on a phone. Square framing is a separate decision from the element set.

## Decision for Kai
- **Expand**: add lines + digits (and optionally thin-ring + "?" badge).
  Then riddle #1 is fully buildable from elements.
- **Use smartly**: accept rows-without-lines — but digits cannot be skipped;
  without them the riddle is unsolvable from elements alone.

## v2 (2026-11-07) — the frame was missing
Kai: "Where is even our theme color? Where is even our riddle square?"
v1 had rebuilt the OLD full-page demo, not the current system. v2
(`solar-letters-reconstruction-v2.py` → `-v2.svg/.png`) fixes it:
- Page background `bg-emerald` — the theme colour is the frame.
- Riddle square `square-navy` at (48, 468) — the riddle stays dark; the
  theme colour frames it, it does not recolour its content (yellow sun and
  grey rings on emerald would be unreadable).
- Content reflowed into the square: sun smaller (dia 150), rows compressed
  (spacing 98, bow 38), circles the SAME size (dia 48 / discs 74) so
  legibility is kept. No shape stretched. (First v2 render had the sun halo
  crossing the square's top border; sun moved down 20px, now clean.)
- Digits and orbit lines still missing — unchanged from v1.

## v3 (2026-11-07) — digits close the gap
Kai: generate digits 0-9. `elements/digits/` now holds 210 files
(10 digits x 7 colours x 3 sizes). v3
(`solar-letters-reconstruction-v3.py`) places digit-black 1-8 on the gold
discs — the riddle is now fully buildable from elements except the orbit
lines, which are still missing (no line element).
