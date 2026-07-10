# Autotile Shape Fix Implementation Report — Real Autotile Shape Algorithm for the Overworld Compiler

Follows: the Overworld Promotion work (2026-07-10) (overworld promotion). Same map: `Map027` / `SCR-HOM-OVW-001`.
Date: 2026-07-10
Trigger: user feedback on the the Overworld Promotion work (2026-07-10) render — "the shape and layout are good, the tile flow is wrong," correctly guessing the automatic edge system wasn't really blending tiles.

## Completed

Checked `tile_painter.py`'s `autotile_shape()` and found its own docstring already admitted the problem: it was "NOT a reproduction of the engine's official 48-shape FLOOR_AUTOTILE_TABLE... could not be verified against a running RPG Maker MZ instance from this environment," and instead computed a bounded-but-arbitrary shape id from a 4-direction bitmask that doesn't correspond to the engine's real quadrant composition (e.g. "no neighbors" landed on shape 0, which the real engine reserves for "fully surrounded"). the Overworld Promotion work (2026-07-10)'s sheet-offset fix got tiles into the right numeric range, but the actual edge art each tile displayed was still essentially uncorrelated with its real neighbors.

Separately, `paint()`'s forest/mountain/road overlay layer always wrote a single fixed shape (31) regardless of neighbors — fine for sparse scattered decoration, but it's why the dense mountain range read as a repeated grid of identical stamps instead of a blended mass.

Fixed both, reusing the exact technique already validated earlier this session for the hand-built Skyreach map (Map004): rather than guess the engine's neighbor-pattern-to-shape mapping, derive it empirically from a real, already-correct, engine-rendered map (`Map001.json`) by sampling every tile's actual 8-neighbor same/different pattern against its real stored shape, then reconstructing a per-quadrant (NW/NE/SW/SE) lookup from those observations. 72 of 74 real observed patterns round-trip exactly through the real `FLOOR_AUTOTILE_TABLE`; the 2 mismatches are a rare 1-tile-wide-strip corner case that only swaps between two visually similar mirrored shapes.

- New file `atlas-tools/mapgen/compiler/autotile_shapes.py`: the real `FLOOR_AUTOTILE_TABLE` (engine constant, verbatim from `rmmz_core.js`) plus the empirically-derived quadrant lookup and a `shape_for_neighbors(...)` function, fully documented (including how to re-derive it if a tileset image is ever replaced).
- `tile_painter.py`: `autotile_shape()` now delegates to the real algorithm instead of the fake one. Overlay painting restructured into two passes — pass 1 decides which cells get road/mountain/forest overlay (unchanged logic), pass 2 computes each overlay tile's real neighbor-aware shape from the now-final membership set, instead of stamping shape 31 everywhere.
- Added `tests/test_autotile_shapes.py` (5 tests: fully-surrounded is shape 0, fully-isolated uses the dedicated island shape, a 1-wide strip differs from solid fill, every possible 8-neighbor combination produces a valid 0-47 shape, and a solid 3x3 overlay block uses more than one shape instead of collapsing to a repeated stamp).
- Regenerated the candidate and re-promoted into `Map027.json` (terrain only changed; landmark positions, events, and passability are identical to the Overworld Promotion work (2026-07-10), so no cross-map coordinate changes were needed this time).

## Files Modified

- `TheLastSwordProtocol-Atlas/atlas-tools/mapgen/compiler/tile_painter.py` — real shape algorithm; two-pass overlay painting.
- `TheLastSwordProtocol-Game/data/Map027.json` — re-promoted with correctly-blended terrain.
- `TheLastSwordProtocol-Game/map_ownership.json` — the Autotile Shape Fix work (2026-07-10) note.

## Files Created

- `TheLastSwordProtocol-Atlas/atlas-tools/mapgen/compiler/autotile_shapes.py`.
- `TheLastSwordProtocol-Atlas/atlas-tools/mapgen/compiler/tests/test_autotile_shapes.py`.
- `rpgmakerLSP/reports/atlas-import/autotile-shape-fix-map027-render.png` (visual confirmation — coastline now shows real scalloped edge/corner variation, the mountain interior blends instead of grid-stamping, forest clusters read as organic blobs; supersedes `overworld-promotion-map027-render.png`).
- `rpgmakerLSP/reports/atlas-import/autotile-shape-fix-autotile-shape-fix-report.md` (this report).

## Player-Visible Progress

The overworld's terrain now actually looks like terrain instead of a technically-correct-but-visually-broken tile grid — coastlines have natural rounded variation, the mountain range reads as one blended landmass with a visible switchback trail instead of a checkerboard of identical rock stamps, and forest patches look like organic clusters. Layout, landmark placement, and all transfers are unchanged from the Overworld Promotion work (2026-07-10).

## Commands Run

```bash
python3 -m unittest discover -s tests          # 45 -> 50 passing (5 new tests)
python3 generate_production_candidate.py generate
# promotion: rerun the same scratchpad script from the Overworld Promotion work (2026-07-10) against the regenerated candidate
# verification: BFS reachability (unchanged, 3267 tiles / all 9 events reachable),
# quality re-score, atlas.py validate
```

## Validation Result

- Compiler test suite: **50/50 passing**.
- Live `Map027.json` quality re-score: **100/100, `accept_for_review`** (unchanged from the Overworld Promotion work (2026-07-10) — the scorer doesn't currently penalize the old approximate shapes, which is itself a gap worth noting: the automated score never caught this, only a human looking at the actual render did).
- Atlas validation: **0 errors, 0 warnings**.
- BFS reachability: unchanged, all 9 events still reachable (terrain passability didn't change, only visual blending).

## Remaining Issues / Questions

- The quality scorer's `visual_density`/`terrain_naturalness` categories didn't catch the fake-shape problem either time (the Overworld Promotion work (2026-07-10)'s 88%-water bug or this shape-flow bug) — both were only caught by a human looking at an actual render. Worth a future pass adding a scorer check that samples painted shape diversity against a known-good baseline, so this class of bug gets caught automatically next time.
- Still needs a human runtime playtest, same as everything else this session.
- Not committed.
