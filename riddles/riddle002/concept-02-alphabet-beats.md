# Riddle #2 — Alphabet Song beats (Kai's idea, 2026-11-06)

## Layout
One box per beat of the alphabet song (Twinkle melody, 4/4). 12 bars × 4 beats = 48 boxes, one bar per row, phrase pairs (2 bars) separated by a slightly larger gap. No text, no letters, no numbers in the image — only box colour.

## Colour rule (Kai)
- Light blue (`#93c5fd`): a letter is sung on that beat.
- Light grey (`#d1d5db`): no letter is sung on that beat (a word syllable, or a held note).

## Beat map (verified: 48 beats, 28 blue, 20 grey)
| Bar | Sung | Boxes |
|-----|------|-------|
| 1 | A B C D | blue blue blue blue |
| 2 | E F G (G held) | blue blue blue grey |
| 3 | H I J K | blue blue blue blue |
| 4 | L M N+O P | blue blue blue blue |
| 5 | Q R S T | blue blue blue blue |
| 6 | U V (V held 2 beats) | blue blue grey grey |
| 7 | W X Y and | blue blue blue grey |
| 8 | Z (Z held 3 beats) | blue grey grey grey |
| 9 | Now I know my | grey grey grey grey |
| 10 | A B C (C held) | blue blue blue grey |
| 11 | Next time won't you | grey grey grey grey |
| 12 | sing with me (me held) | grey grey grey grey |

Blue count cross-check: 29 letters sung (26 + A B C repeated in bar 10) on 28 blue beats — N and O share one beat in LMNOP. ✓

### Correction (Kai, 2026-11-06: "Isn't it LMNOP?")
The first version wrongly put a held N at the end of bar 4 and O P in bar 5. LMNOP is compressed — "elemenopee": N and O share a beat — so bar 4 is all blue and everything after shifts one slot: Q R S T in bar 5, U V held in bar 6, W X Y and in bar 7, Z (held three beats) in bar 8. The shared beat stays one blue box: a box is a beat, and a letter is sung on it — two letters, in fact.

## Why it works as a riddle
The solver must guess that a colour pattern = a song's rhythm. The tells: the repeating `blue blue blue grey` cadence at the end of bars 2/4/6 (held notes), the lone blue in bar 8 (Z after the non-letter "and"), and the isolated blue triplet in bar 10 — the repeated A B C — sitting in a grey tail. The grey tail (bars 9–12) is what says "a song, not just the alphabet".

## Files
- SVG (source of truth): `riddle-02-alphabet-beats.svg` — colours/radius/background live as CSS tokens (`--bg`, `--blue`, `--grey`, `--radius`) in its `<style>` block, so the whole set can be restyled together at the alignment review.
- Generator: `riddle-02-alphabet-beats.py` (data-driven from BEAT_MAP; also writes the PNG preview).
- PNG preview: `riddle-02-alphabet-beats.png`.
- **Page build (2026-11-06, Flat Dark): `riddle-02-page.py` → `riddle-02-square.svg` (984×984, the riddle itself) + `riddle-02-page.svg/.png` (1080×1920 TikTok page: Navy frame + square).** Lit tiles use the library `tile-lit` element (blue + 35% glow halo); rest tiles are flat `tile-rest` grey. Grid (rebuilt 2026-11-07, no-stretch rule): natural square tiles 62×62, 12px gaps + 18px extra after every 2 bars, grid 284×906 centred in the square (350px side padding, 39px top/bottom) — leftover space stays empty, never stretched. No text / no "?" in the square yet (open Q3). Verified: 48 beats, 28 blue / 20 grey; sampled pixels match #93C5FD (lit) and #D1D5DB (rest).

## Drawing method (Kai's choice, 2026-11-06)
SVG, built programmatically from the beat map — not an AI image generator. AI generators miscount boxes; the SVG is exact, and its shared style tokens (`--bg` etc.) are the mechanism for keeping art style consistent across all 10 riddles at the alignment review.

## Open questions for Kai
1. Full song (48 boxes, drawn) vs alphabet only (bars 1–8, 32 boxes)? The full song is drawn because the grey tail + ABC repeat are the strongest identifiers.
2. Bar 7–8: "and" sits on the last beat of bar 7 (grey), Z opens bar 8 and is held three beats. If you sing "and" as a pickup into Z, bar 8 stays blue-first; the alternative phrasing would move Z — confirm.
3. No "?" marker in the image yet — the question ("what song is this?") currently lives in the video/caption, as with a pure 一枚謎 fingerprint. Decide at the style review whether the set gets a uniform question marker.
