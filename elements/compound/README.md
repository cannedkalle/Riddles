# Compound / reusable elements

Compound elements combine several single elements into one reusable unit.
Each is a single standalone SVG (1080 × 1920 unless noted), built from
Kai's handcrafted standard — refer to Kai's files, not to assistant
designs. Element sizing rule applies: preferred dimensions are multiples
of 60 px; smaller elements multiples of 20 px; any exception (not a
multiple of 20 px) needs Kai's approval.

## page-frame-standard-A.svg

The standard riddle page frame as one element — not tied to one riddle.
Background + riddle square + title + subtitle + riddle title + by
CannedKalle + ANSWER label + answer box. The riddle content
(diamonds, arrows, emojis, coral `?`) goes on top of it, in the empty
square.

- Source: Kai's handcrafted `riddle004_standard-2.svg` (2026-11-11),
  which added the answer box and moved the byline. Built by removing
  only the riddle content from Kai's file; the frame is pixel-identical
  to Kai's standard (top and bottom bands: 0 differing pixels).
- Contents:
  - Background: cream-emerald `#E0F8E8` full page with the key pattern
    (`#C7F2D5`, masked to the top/bottom bands).
  - Riddle square: emerald-palest `#EEFBF3`, 1080 × 1080, `y 420–1500`.
  - Title `Riddlegram`: serif, emerald-deep `#0D5038`, left-aligned,
    ink `x 44–747`, `y 76–195`.
  - Subtitle `SINGLE-IMAGE RIDDLE/一枚謎`: sage `#54836B`,
    right-aligned, right edge `x≈1037–1048`, top band.
  - Riddle title `#004 Biohazard`: serif, emerald `#168654`,
    left-aligned, ink `x 43–572`, `y 250–304`.
  - `by CannedKalle`: sage `#54836B`, RIGHT-aligned, ink `x 763–1041`,
    `y 323–352` (top band, right side — moved here from the bottom
    band in `riddle004_standard-2.svg`; right edge aligns with the
    subtitle). Same text and width (279 px) as the old bottom-left
    byline, repositioned.
  - `ANSWER` label: emerald `#168654`, left-aligned, ink `x 81–260`,
    `y 1557–1585` (bottom band, just above the box).
  - Answer box: emerald-palest `#EEFBF3` fill, `x 80–1000`,
    `y 1597–1797` (920 × 200), with an emerald `#168654` border
    (5 px stroke, rect `x 82.5`, `y 1599.5`, 915 × 195).
  - The riddle square is empty — no riddle content.
- The riddle title (`#004 Biohazard`) is the variable part: swap it
  for the next riddle's `#NNN Name` (position fixed on the left).
  The rest of the frame is fixed across riddles.
- Text is outlined paths (from Kai's file), so the glyphs and positions
  are exact. To change the riddle title, replace those paths in an
  editor; do not re-typeset the fixed texts.

## info-page.svg

The TikTok carousel info page (Kai, 2026-11-15) — page 2 of every
post, identical for all riddles. Users who solved the riddle stop
here; users who want help swipe on to the hint page.

- Source: built from `page-frame-standard-A.svg` by removing the
  riddle title, ANSWER label, and answer box, then adding live
  `<text>` (Noto Serif CJK SC Bold for the title slot, Noto Sans
  for the rest). Frame texts stay Kai's outlined paths.
- Contents:
  - Title slot: "Before You Swipe" (serif, emerald `#168654`,
    left-aligned, same position as riddle titles).
  - Square: "Solved it? Stop here." / "Need a hint? Swipe →"
    (Noto Sans Bold, emerald-deep `#0D5038`, centred), then
    "The last riddle's answer is on the final page." (Noto Sans,
    sage `#54836B`, smaller, two lines).
  - The swipe arrow is a drawn path, not a glyph — Noto Sans has
    no U+2192.
  - Bottom band: no answer box. "Follow for the next riddle."
    (Noto Sans, emerald `#168654`, centred).
- The file is the finished page — post as-is. Built by
  `tiktok-pages/build_pages.py` (local working copy, not in repo).

## hint-page-template.svg

The TikTok carousel hint page template (Kai, 2026-11-15) — page 3
of a post. Same template for every riddle; the hint text is
replaced per riddle.

- Source: built from `page-frame-standard-A.svg` the same way as
  `info-page.svg` (riddle title, ANSWER label, answer box removed;
  live `<text>` added).
- Contents:
  - Title slot: "#NNN Name" placeholder (serif, emerald `#168654`,
    left-aligned) — replace with the riddle's number and title.
  - Square: "HINT" label (serif, emerald `#168654`, same style as
    the ANSWER label, top-left of the square) + hint text (Noto
    Sans Bold, emerald-deep `#0D5038`, centred; the template holds
    the placeholder "Your hint goes here" — replace with 1–3 lines
    per riddle). No coral `?` square — the `?` stays on the riddle
    page only.
  - Bottom band: no answer box. "Answer in the next post."
    (Noto Sans, emerald `#168654`, centred).
- Built by `tiktok-pages/build_pages.py` (local working copy, not
  in repo).

## info-page.svg

The TikTok carousel info page (Kai, 2026-11-15) — page 2 of every
post, identical for all riddles. Users who solved the riddle stop
here; users who want help swipe on to the hint page.

- Source: built from `page-frame-standard-A.svg` by removing the
  riddle title, ANSWER label, and answer box, then adding live
  `<text>` (Noto Serif CJK SC Bold for the title slot, Noto Sans
  for the rest). Frame texts stay Kai's outlined paths.
- Contents:
  - Title slot: "Before You Swipe" (serif, emerald `#168654`,
    left-aligned, same position as riddle titles).
  - Square: "Solved it? Stop here." / "Need a hint? Swipe →"
    (Noto Sans Bold, emerald-deep `#0D5038`, centred), then
    "The last riddle's answer is on the final page." (Noto Sans,
    sage `#54836B`, smaller, two lines).
  - The swipe arrow is a drawn path, not a glyph — Noto Sans has
    no U+2192.
  - Bottom band: no answer box. "Follow for the next riddle."
    (Noto Sans, emerald `#168654`, centred).
- The file is the finished page — post as-is. Built by
  `tiktok-pages/build_pages.py` (local working copy, not in repo).

## hint-page-template.svg

The TikTok carousel hint page template (Kai, 2026-11-15) — page 3
of a post. Same template for every riddle; the hint text is
replaced per riddle.

- Source: built from `page-frame-standard-A.svg` the same way as
  `info-page.svg` (riddle title, ANSWER label, answer box removed;
  live `<text>` added).
- Contents:
  - Title slot: "#NNN Name" placeholder (serif, emerald `#168654`,
    left-aligned) — replace with the riddle's number and title.
  - Square: "HINT" label (serif, emerald `#168654`, same style as
    the ANSWER label, top-left of the square) + hint text (Noto
    Sans Bold, emerald-deep `#0D5038`, centred; the template holds
    the placeholder "Your hint goes here" — replace with 1–3 lines
    per riddle). No coral `?` square — the `?` stays on the riddle
    page only.
  - Bottom band: no answer box. "Answer in the next post."
    (Noto Sans, emerald `#168654`, centred).
- Built by `tiktok-pages/build_pages.py` (local working copy, not
  in repo).
