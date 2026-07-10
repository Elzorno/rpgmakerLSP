# Overworld Promotion Implementation Report — Regenerate and Promote the Home Island Overworld

Screen: `SCR-HOM-OVW-001` | Map: `Map027` (`FLD_HomeIsland_Overworld`)
Date: 2026-07-10
Trigger: direct user request ("the overworld is still using the bad map... regenerate the overworld map based on the home island landmass preview"), not an `atlas.py next` work order.

## Completed

### 1. Found why three rejections never got fixed

Map027 had been rejected three times ("not even close to representing the reference image"). The reference is `AtlasStudio/references/a_detailed_illustrated_game_design_map_poster_wo.png`, a fourth sibling repo the Atlas compiler's own tooling flags as inaccessible from its own checkout. Separately, the Atlas repo already had a real generation pipeline for this screen (`atlas-tools/mapgen/compiler/`, implementing IMP-HOM-024–029) with a landmass generator, a tile painter, an automated quality scorer, and a review flow — WO-0042's candidate had already scored 97.5/100 and been **accepted by Chris on 2026-07-10**, but explicitly not promoted: `"production_promotion": "not_applied"`, `"The Game repo Map027.json is unchanged; promotion remains a separate explicit step."`

### 2. Found a real bug before promoting anything

Before writing the accepted candidate into the Game repo, I checked what it would actually look like rendered with the real tileset — the quality scorer and the human review had both operated on the landmass *plan* (a terrain-type diagram), not the final RPG Maker tile IDs. Decoding the candidate's actual `data` array: **88% of the ground layer was in the A1 (water) tileId range**, even though the terrain plan was correct and mostly land. Root cause in `atlas-tools/mapgen/compiler/tileset_world.py`: `autotile_id(kind, shape)` always added the `TILE_ID_A1` base offset regardless of whether the terrain's registry entry said `"sheet": "A1"` or `"A2"` — so every A2 (ground) terrain, including the majority-share `grassland`, got miscalculated into the A1 numeric range, where it collided with (and rendered as) literal ocean water. `tile_painter.py` called this same broken helper for grassland/marsh/hills/road/mountain/forest at 4 call sites.

Also found `WORLD_TILESET_ID` hardcoded to `1`, which is the legacy `rpgmakerLSP` repo's numbering for its "Overworld" tileset — the actual production target, `TheLastSwordProtocol-Game`, registers the equivalent sheet as **"World" at id 7**. Silently wrong once promoted into the real repo.

### 3. Fixed the compiler, not just the output

- `tileset_world.py`: `autotile_id()` now takes a `sheet` argument and picks `TILE_ID_A1` or `TILE_ID_A2` accordingly; added `resolve_world_tileset_id()` which looks up the tileset by name (`"World"` or `"Overworld"`) against whichever `Tilesets.json` is actually being targeted, instead of a hardcoded id. Reordered `TILESET_JSON_CANDIDATES` to check the Game repo first (the real production target) rather than the legacy repo.
- `tile_painter.py`: updated all 4 `tw.autotile_id(...)` call sites to pass `sheet=`.
- Added a regression test (`test_a2_sheet_terrain_lands_in_the_a2_tile_id_range`) asserting every A2-sheet terrain's painted tileId actually falls in the A2 range — nothing in the existing 44-test suite would have caught this bug.
- Re-ran `generate_production_candidate.py generate`: new candidate is 3373 A2(ground)/3539 A1(water) tiles (was 834/6078) — matches the terrain plan's actual land/water ratio. Quality score 92.5/100, `accept_for_review`, `tilesetId: 7` (was 1).
- Verified visually: wrote a from-scratch PIL compositor implementing `rmmz_core.js`'s exact `_addAutotile`/`_addNormalTile` math against the real `World_A1/A2/B/C.png` tileset images and rendered the candidate. The fixed version shows a coherent island — grassland, a mountain range with a switchback trail, scattered forest, sandy coastline, a marsh — matching the accepted preview's composition. See `overworld-promotion-map027-render.png`.

### 4. Promoted the candidate into the Game repo (the step WO-0042 explicitly left undone)

The compiler intentionally produces terrain only — no events (its own documented boundary: "Map generation must not... modify game repository files"). I added what promotion requires:

- Copied the fixed candidate's tile data (layers 0–3) and `tilesetId: 7` into `data/Map027.json` (96×72, was 34×30).
- Painted a region layer from the actual tile content: region 1 (light encounters, troops 1/3) on open grassland, region 2 (harder encounters, troops 4/5) on forest/mountain overlay tiles — the candidate ships with an empty region layer.
- Added the 9 events the old Map027.json had (7 landmark transfers `TRN-HOM-033`–`039`, the mainland-departure stub, the doc-reference comment), preserving their exact dialogue/switch/transfer logic verbatim, repositioned to the new landmass's real landmark coordinates from `home_island_landmass_plan.json`'s `anchor_zones` (unchanged by the tile-painting fix, since that data comes from an earlier, already-correct pipeline stage). Each transfer sits one tile below its landmark's icon stamp (the icon tile itself is intentionally impassable); confirmed all 7 landmark positions are otherwise open ground with a direct BFS check.
- Updated the 8 matching inbound transfers on `Map001.json` (×4: Skyreach/Rustshore/Glassfield/Fogfen routes), `Map004.json`, `Map008.json`, `Map013.json`, `Map015.json` to land two tiles below each landmark icon — one tile clear of the outbound trigger tile, so arriving doesn't immediately re-fire the "enter" event (matching the existing Ashford/Elara-House door convention already used elsewhere in this project).
- Verified end-to-end reachability: BFS from the Ashford landing tile reaches all 9 event tiles; the live-file quality re-score is **100/100, `accept_for_review`**.

## Files Modified

- `TheLastSwordProtocol-Atlas/atlas-tools/mapgen/compiler/tileset_world.py` — sheet-aware `autotile_id()`; dynamic `resolve_world_tileset_id()`; `TILESET_JSON_CANDIDATES` reordered.
- `TheLastSwordProtocol-Atlas/atlas-tools/mapgen/compiler/tile_painter.py` — 4 call sites pass `sheet=`.
- `TheLastSwordProtocol-Atlas/atlas-tools/mapgen/compiler/tests/test_tile_painter.py` — added the A2-range regression test.
- `TheLastSwordProtocol-Atlas/atlas-tools/mapgen/compiler/tests/test_quality_score.py` — flipped `test_negative_control_real_production_map027_fails` to `test_live_production_map027_passes`; the live file is no longer the intentionally-bad fixture it used to encode.
- `TheLastSwordProtocol-Game/data/Map027.json` — full terrain + region + event rebuild.
- `TheLastSwordProtocol-Game/data/Map001.json`, `Map004.json`, `Map008.json`, `Map013.json`, `Map015.json` — inbound transfer destination coordinates updated to the new landmark positions.
- `TheLastSwordProtocol-Game/map_ownership.json` — Map027 promotion notes (state stays `generated`, pipeline-owned); brief notes on Map001/Map004.

## Files Created

- `atlas-tools/mapgen/compiler/out/Map027.production_candidate.json`, `home_island_production_candidate_plan.json`, `home_island_production_candidate_preview.png`, `home_island_production_candidate_quality_report.md` (regenerated by the fixed compiler).
- `TheLastSwordProtocol-Atlas/reports/home-island-production-overworld-review.md` (regenerated).
- `rpgmakerLSP/reports/atlas-import/overworld-promotion-overworld-route-audit.md`.
- `rpgmakerLSP/reports/atlas-import/overworld-promotion-map027-render.png` (engine-faithful visual review render, from a custom compositor written this session).
- `rpgmakerLSP/reports/atlas-import/overworld-promotion-overworld-promotion-report.md` (this report).

## Player-Visible Progress

The Home Island overworld hub is playable for the first time — a real irregular island (grassland, a mountainous north with a visible trail, scattered forest, sandy coast, a marsh) connecting all seven Journey I locations, instead of a rejected flat/void/water map. Walking out of any boundary transfer (Ashford's north/south/east routes, Skyreach's return path, Glassfield's, Rustshore's, Fogfen's) now lands you at a real, walkable spot on the island; each landmark transfer leads to its correct destination map with the same story-gate logic as before (Skyreach/Hidden Cave/Sealed Node still properly locked behind their switches, mainland departure still gated behind Node Seven).

## Commands Run

```bash
# investigation
python3 -m json / ad hoc Python to decode Map027.production_candidate.json's tile IDs

# compiler fix + regeneration
python3 -m unittest discover -s tests          # 44 passing before touching anything
python3 generate_production_candidate.py generate
python3 -m unittest discover -s tests          # 45 passing after the fix + new test

# promotion (scratchpad scripts): build region/event data, write Map027.json,
# update the 8 sub-map inbound transfer coordinates, BFS reachability check

# validation
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/overworld-promotion-overworld-route-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

## Validation Result

- Atlas validation: **0 errors, 0 warnings**.
- Compiler test suite: **45/45 passing** (44 pre-existing + 1 new regression test), including the flipped live-file quality test.
- Live `Map027.json` quality re-score: **100/100, `accept_for_review`**.
- Map ownership audit: 19 maps; Map027 still `generated` (pipeline-owned by design — a future compiler re-run is the intended revision path, not manual edits).
- BFS reachability: all 9 Map027 events reachable from the Ashford landing tile; no position collisions among the 9 events.
- Route audit: **found=228, missing=21, warning=9** — unchanged totals. The remaining Reachability "missing" entries (`REACH-SCR-HOM-*`) and Transfer Hygiene "orphan" warnings for `TRN-HOM-033`–`039` are a pre-existing Atlas *registry* gap, not a map defect: these seven transfer IDs were never added to the Home Island Transfer Registry / re-exported to `atlas-exports/home-island.json`, so the audit tool's reachability graph doesn't know they exist. This predates the Overworld Promotion work (2026-07-10) (same transfer IDs, same gap, before and after) and is a separate, real follow-up (see below).

## Remaining Issues / Questions

- **Register `TRN-HOM-033`–`039` and the overworld screen in Atlas canon.** `SCR-HOM-OVW-001` has no `atlas/docs/02_World/Screens/Home_Island/` page at all (confirmed absent), and its seven transfers aren't in the Home Island Transfer Registry export. Until that's done, the audit tooling's reachability checks can't verify the overworld end-to-end even though it now functions correctly in-engine. This is documentation debt, not a runtime bug.
- **Human runtime playtest is still the actual gate**, same caveat as every other promoted map this session — walk the real routes before locking anything.
- The `landmarks_too_close` warning from the original WO-0042 quality report (closest two landmarks 3 cells apart, recommend ≥6) persists — Glassfield and Sealed Node sit close together by design ("beneath Glassfield"), not a defect, but worth a second look during playtest for visual crowding.
- Region 2 (harder encounters) currently covers every forest/mountain-overlay tile uniformly; no attempt was made to tune encounter difficulty by proximity to landmarks — reasonable first pass, not final balance.
- Not committed, per this session's established practice (no other work this session has been committed either).
