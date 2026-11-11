# Concept: Solar Letters (Kai's idea, 2026-10-23)

## Sketch as proposed
Dark background. A sun (yellow circle) and 8 orbits (slightly curved lines). Each orbit carries a few small circles — one per letter of that planet's name (Mercury 7, Venus 5, Earth 5, Mars 4, Jupiter 7, Saturn 6, Uranus 6, Neptune 7). "Find a theme-matching word using the letters above."

## Design decision (Kai, 2026-10-23) — supersedes the uniqueness debate
A unique/anagram-proof answer is NOT required. The designer picks a word first, then puts small numbers 1, 2, 3, … on the circles: the numbers say WHICH circles to take and in WHAT ORDER. The puzzle is decoding the representation (orbit = a planet identified by order from the sun + circle count; circle position = letter position in the name). Planet names are NOT printed — only the circles are shown.

(Note from earlier screening, kept for word choice: planet names contain no O, G, L, D, B, F, K, W, so answer words must avoid those letters — ASTEROID, GALAXY, MOONLIGHT etc. are unbuildable. Solar-order reading is irrelevant under the numbering design.)

## Final spec — UNIVERSE version (Kai approved the word)
Exactly one numbered circle per orbit; number k sits at the position of the k-th letter of UNIVERSE in that planet's name:
- 1 = Mercury, 5th circle → U
- 2 = Saturn, 6th circle → N
- 3 = Jupiter, 4th circle → I
- 4 = Venus, 1st circle → V
- 5 = Earth, 1st circle → E
- 6 = Mars, 3rd circle → R
- 7 = Uranus, 6th circle → S
- 8 = Neptune, 2nd circle → E

Demo built: `demo_solar_letters.py` → `demo-solar-letters-universe.png` (counts and numbered positions visually verified).

## Visual / readability notes
- Keep the arcs as stacked slightly-curved lines (user's sketch), not true concentric circles — legibility at phone size.
- Keep dark background, yellow sun, no text. Do NOT print planet names: that would leak "letters" and kill the guessing step.
