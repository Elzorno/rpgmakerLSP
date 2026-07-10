# WO-0052 Implementation Report — Hidden Cave Terrain (Maps005-007)

Work order: `WO-0052-build-hidden-cave-trials-mechanics.md` (queue candidate
`build-hidden-cave-trials-mechanics`, whose event-wiring half was already
delivered as WO-0051 last session; this pass covers the remaining terrain
tasks: hand-build Maps005-007, flip the ownership ledger, re-audit).

Screens: `SCR-HOM-HCV-001/002/003` | Maps: `Map005/006/007` (`DGN_HiddenCave_Entrance`,
`DGN_HiddenCave_Trials`, `DGN_HiddenCave_Sanctum`)
Date: 2026-07-10

## Completed

1. **Hand-built all three Hidden Cave maps' terrain**, replacing the bare
   generated scaffolds with real cave geometry derived from each screen's
   Map Intent and its SVG layout guide (SVG pixel coordinates decoded and
   cross-checked against the existing generated event positions before
   building, same discipline as WO-0048):
   - **Map005 (Entrance, 24x24)**: a winding corridor from the Skyreach-side
     exit up to the trials transfer, with a westward jog to a small alcove
     for the reflective-mineral-cluster landmark, and two chamber bulges
     matching the SVG's walkable rects.
   - **Map006 (Trials, 40x32)**: a wide cross-shaped hall connecting the
     Body/Mind/Heart trial alcoves (left/center/right) to a north spine
     (Sanctum Gate) and south spine (return to Entrance), matching the SVG's
     three walkable rects and the existing Body/Mind/Heart event clusters
     exactly.
   - **Map007 (Sanctum, 23x19)**: a square chamber around the Sword Pedestal
     with a south corridor down to the return transfer.
2. **Built and validated a fresh autotile-shape derivation** rather than
   reusing anything from memory: parsed every A2 ground-autotile placement
   in Map001 (kinds 0/1/2/3/14, chosen because they're the most-used ground
   kinds and cleanly single-kind), building a neighbor-signature -> shape
   lookup with **zero internal conflicts per kind**; cross-checked by
   merging in Map004 and Map008's own dominant kinds with **zero cross-kind
   conflicts** on the signatures they shared. (An earlier attempt that mixed
   all kinds/maps together first showed many spurious "conflicts" — turned
   out to be real RPG Maker behavior: some signatures, especially the
   fully-enclosed one, have multiple visually-interchangeable shape variants,
   and hand-authored maps occasionally have local artist overrides. Restricting
   to one kind at a time inside one already-verified map removed the noise.)
3. **Ported `_addAutotile`/`FLOOR_AUTOTILE_TABLE` directly from the shipped
   `TheLastSwordProtocol-Game/js/rmmz_core.js`** into a PIL compositor,
   rather than reconstructing the source-rect math from memory — this is
   the same file the running game engine actually uses, so the sub-tile
   sampling math is guaranteed correct, not approximated.
4. **Verified the Dungeon_A2 floor/wall kind choice by direct pixel
   inspection**, not by guessing kind numbers from the raw tileset image
   layout: built a labeled contact sheet rendering every kind 0-31 solid,
   caught that my first guess (kind 12) actually had a baked-in dirt band on
   its north edge (visible once rendered — not something you'd know from
   looking at the sheet thumbnail alone), and switched to kind 16 (clean gray
   cracked stone) paired with kind 22 (the matching gray-stone-to-black
   cave-void cliff edge), confirmed clean via direct crop-and-view of both
   kinds' source blocks.
5. **Rendered all three maps and visually confirmed clean results**: solid
   stone floor, jagged black cave-wall silhouette, no garbled tiles, no
   stray decorative-icon bleed-through. See the three render PNGs listed
   below.
6. **BFS-verified full reachability on all three maps** (every floor tile
   reachable from the map's south-side entrance; every existing event and
   transfer confirmed on or adjacent to floor) and **confirmed tileset
   passability flags**: kind16 (floor) tiles have a clear passage nibble
   (passable), kind22 (wall) tiles have all four passage bits set
   (impassable) — collision is handled correctly by the engine's own
   tileset flags, nothing extra needed.
7. **Did not touch any event data.** Map006 in particular carries the 20
   events from WO-0051 (Body/Mind/Heart trial mechanics, Sanctum Gate,
   transfers, decoration landmarks) — only the four tile layers (0-3) and
   the shadow layer (4) were replaced; the region layer (5, already region 5
   / no-random-encounter per `ATLAS-TEC-059`) and the full `events` array
   were left untouched and reverified reachable after the terrain change.
8. **Flipped Maps005-007 to `hand_authored`** in `map_ownership.json` with
   `wo_0052_certification` blocks matching the WO-0048/WO-0050 documentation
   pattern, appending to (not replacing) each map's existing WO-0049 dialogue
   notes.
9. **Retired the `build-hidden-cave-trials-mechanics` queue candidate** now
   that both halves (WO-0051 event wiring, WO-0052 terrain) are done.

## Files Modified

- `TheLastSwordProtocol-Game/data/Map005.json` — terrain layers 0-4 replaced (events/regions untouched).
- `TheLastSwordProtocol-Game/data/Map006.json` — terrain layers 0-4 replaced (events/regions untouched).
- `TheLastSwordProtocol-Game/data/Map007.json` — terrain layers 0-4 replaced (events/regions untouched).
- `TheLastSwordProtocol-Game/map_ownership.json` — Map005/006/007 `generated` -> `hand_authored` with certification notes.
- `TheLastSwordProtocol-Atlas/atlas/planning/workorder_queue.json` — retired the `build-hidden-cave-trials-mechanics` candidate.

## Files Created

- `rpgmakerLSP/reports/atlas-import/hidden-cave-trials-route-audit.md` (WO-required audit output).
- `rpgmakerLSP/reports/atlas-import/wo-0052-map005-render.png`, `wo-0052-map006-render.png`, `wo-0052-map007-render.png` (engine-faithful visual review renders).
- `rpgmakerLSP/reports/atlas-import/wo-0052-hidden-cave-terrain-report.md` (this report).
- One-off Python scripts (autotile-shape derivation, per-map terrain builder, PIL renderer, kind-verification contact sheet) run from the session scratchpad, not left in either repo — same disposition as WO-0048's build/render scripts; the technique is worth reusing, the scripts themselves depend on a session-local shape-table JSON and aren't a durable tool yet.

## Player-Visible Progress

The Hidden Cave is no longer three bare gray rectangles. It now reads as a
real cave route: a winding entrance passage down from Skyreach with a side
nook, a wide natural trials hall where the Body/Mind/Heart mechanics
(wired last session) actually take place in a legible space instead of an
empty box, and a proper enclosed sanctum chamber around the Sword Pedestal.
Combined with WO-0051's mechanics and WO-0049's dialogue, the full Hidden
Cave route (Entrance -> Trials -> Sanctum) is now readable, mechanically
playable, and terrain-complete.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/hidden-cave-trials-route-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
grep -o '\[Placeholder\][^"]*' ../TheLastSwordProtocol-Game/data/Map005.json data/Map006.json data/Map007.json
```

Plus the scratchpad autotile-derivation, terrain-build, and render scripts, and
standalone BFS reachability checks, all run from the session shell.

## Validation Result

- Atlas validation: **0 errors, 0 warnings**.
- Map ownership audit: 19 maps; `hand_authored=9` now (Map001-004, Map005-008,
  Map026); Map005/006/007 pipeline may write: **NO** (correctly protected).
- Route audit: **found=228, missing=21, warning=9** — identical totals to the
  pre-terrain baseline (confirmed via the WO-0051 report), so nothing regressed;
  this auditor checks transfers/reachability at the route level, not terrain, so
  it can't independently confirm the tile art — that's what the BFS check and
  renders are for.
- Reachability: Map005 189/189, Map006 450/450, Map007 145/145 floor tiles
  reachable; every event and transfer on all three maps confirmed on or
  adjacent to floor.
- `grep [Placeholder]`: zero matches across Map005-007.

## Remaining Issues / Questions

- Human runtime playtest is still the actual acceptance gate, same as every
  prior Home Island map certification (WO-0045/0046/0048/0050) — this pass is
  a thorough data-level + rendered-visual audit, not a substitute for walking
  the route in the engine and trying the trials.
- Terrain is intentionally plain (a clean stone-floor cave with a black-void
  wall silhouette) rather than richly decorated — the screen specs also call
  for "reflective stone patches," "subtle geometric wall carvings," and
  "blue-white accent light," which are handled today by the existing
  character-graphic decoration events (mineral cluster, wall carvings, floor
  markers) sitting on top of this terrain, not by tile-level dressing. Adding
  tile-level decorative accents (the blue crystal patterns spotted in
  `Dungeon_B.png` during tileset inspection) would be a reasonable next polish
  pass but isn't required for first-playable.
- The same Dungeon_A2 kind16/kind22 floor/wall pairing was used on all three
  maps for visual consistency across the cave route; if a future pass wants
  Sanctum to read as more distinct/sacred than Entrance/Trials, that's a
  separate kind choice, not a blocker.
- Not committed, per the work order.
