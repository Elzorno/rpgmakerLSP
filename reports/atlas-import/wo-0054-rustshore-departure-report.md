# WO-0054 Implementation Report — Build Rustshore Departure Production Map

## Completed

Hand-built Maps013–014 (Rustshore Docks, Mainland Departure) into production-ready screens, completing Journey I's critical path (the last remaining location in Chris's stated build order).

- Rendered the real tile output for both maps with a PIL compositor before making any changes, per the established render-first workflow for this project. That render caught a real bug in the pre-existing "generated" scaffold: tileId 1536 (`Outside_A5` kind0/shape0) was used throughout as border filler and to mark the north-sea, south-inlet, and boundary-strip footprints — but that exact tile position in this asset pack's `Outside_A5.png` is a blank, fully-opaque black square. It rendered as a literal black void on both maps, not something a schema/JSON check would ever catch.
- Fixed it by replacing the border ring on both maps with the already-proven grass tile (2816), and replacing the water footprints with a solid-interior water tile (2048, A1 kind0/shape0) empirically sampled from the already-validated Map027 overworld coastline — same "sample from a known-good map, don't hand-derive the shape table" technique used in WO-0052.
- Built the Dockmaster hut on Map013 by transplanting a known-good 7×6 building (roof/walls/door, tile IDs unmodified) from Map001's small hand-authored building, positioned so the door lands on the existing Dockmaster NPC event tile (17,13).
- Implemented dialogue for EVT-HOM-023 (Dockmaster locked/unlocked), EVT-HOM-024 (Lighthouse Examine first-look + repeat visit — the repeat page previously showed nothing at all), EVT-HOM-025/TRN-HOM-025 (Boat Transfer and Begin-departure choice results), and EVT-HOM-026 (Departure Sequence transition line). None of this text was covered by an approved Atlas dialogue packet, so it was authored to the Ashford Dialogue Packet's tone rules (short message-box lines, no modern tech vocabulary) and carries forward the lighthouse-signal motif already foreshadowed in the Dock Messenger's Ashford lines ("the lighthouse keeps flashing wrong" → "settled down... first time in years").
- Gave the boat-landing decorative marker on Map013 an actual small-boat sprite (`Vehicle.png`, index 0) instead of the generic `!Other2` placeholder graphic, addressing the screen spec's "wooden dock and small fishing boat" requirement.
- Marked both maps `hand_authored` in `map_ownership.json` with full WO-0054 notes.

## Files Modified

- `TheLastSwordProtocol-Game/data/Map013.json` — terrain (border/water/hut) and event dialogue text, boat sprite.
- `TheLastSwordProtocol-Game/data/Map014.json` — terrain (border/water) and event dialogue text.
- `TheLastSwordProtocol-Game/map_ownership.json` — Map013/Map014 flipped `generated` → `hand_authored`, ledger `updated` date bumped.

## Files Created

- `rpgmakerLSP/reports/atlas-import/rustshore-route-audit.md` (route audit output)
- `rpgmakerLSP/reports/atlas-import/wo-0054-map013-render.png`, `wo-0054-map014-render.png` (final tile-accurate renders for visual review)
- `TheLastSwordProtocol-Atlas/atlas-exports/home-island.json` (route audit export)
- `rpgmakerLSP/reports/atlas-import/wo-0054-rustshore-departure-report.md` (this report)

The PIL compositor script and the terrain/dialogue edit scripts were run from the session scratchpad and are not left in either repo, same disposition as prior WOs — the technique (direct port of `rmmz_core.js`'s `_addAutotile`/`_addNormalTile`/`_addTableEdge` source-rect math, extended here to also cover A3/A4 wall autotiles) is worth reusing but isn't a durable checked-in tool yet.

## Player-Visible Progress

- Rustshore Docks now reads as a coastal harbor: open sea to the north, a small inlet near the boat landing, a proper wooden hut with a tiled roof for the Dockmaster, a boat sprite at the landing, and sea-grass/path terrain matching the screen spec's required visual elements. Previously the same map rendered with three large black holes where the sea and the hut should have been.
- Dockmaster now has real locked/unlocked dialogue reflecting `J1_Mainland_TravelUnlocked` instead of `[Placeholder]` text.
- Lighthouse Examine has a real first-look line and — new — a real repeat-visit line (previously silent on second interaction).
- Boat Transfer / Begin Departure choice outcomes (Depart / Stay / locked) have real text.
- Mainland Departure (Map014) now reads as a short dock corridor with sea on both sides instead of two black void strips; the Departure Sequence has a real transition line and still correctly sets `Current_Journey = 2` before handing off to the Journey II placeholder transfer.
- Note: the queue candidate's rationale called Rustshore "the last location in Chris's stated Journey I build order," but Sealed Node (Maps009-012: Upper/CorePath/Guardian/RelayCore) is confirmed still `generated` in `map_ownership.json` as of this report — it was not touched by WO-0054 and remains the one outstanding bare-scaffold gap in the Journey I build order, ahead of Rustshore's dockside departure in the actual story sequence (Node Seven must resolve before `J1_Mainland_TravelUnlocked` even turns on).

## Commands Run

```bash
cd TheLastSwordProtocol-Atlas && /usr/bin/python3 atlas-tools/cli/atlas.py validate
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/rustshore-route-audit.md \
  --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

Plus scratchpad-only: a PIL tile compositor (rendered Map013/014 before and after every terrain edit), a terrain-fix script, a dialogue-fix script, and a BFS passability/reachability check from each map's entrance transfer to every Dockmaster/Lighthouse/Boat/Departure event tile.

## Validation Result

- `atlas.py validate`: **0 errors, 0 warnings.**
- `audit_map_ownership.py`: ledger OK, 19 maps listed, Map013/Map014 both `hand_authored` and correctly reported as pipeline-non-writable.
- `audit_all_map_routes.py`: found=228, missing=21, warning=9. Every Rustshore/Departure-specific check (TRN-HOM-023 through TRN-HOM-026, TRN-HOM-008, TRN-HOM-025, TRN-HOM-026 sources/targets/destinations/event tiles) reports **found**, all landing on concrete (non-void) tiles. The 21 missing / 9 warning entries are pre-existing and unrelated to this work order — stale `TRN-HOM-005/006/007/008/015/016/027/028` command-ID expectations and `SCR-HOM-*` reachability checks from before the Home Island overworld (Map027) routing restructure, plus `ORPHAN-27-*` warnings about overworld transfers not yet registered in the Atlas export. None reference Map013/014 or any EVT-HOM-023–026 event.
- BFS passability check (scratchpad): every key event tile (Dockmaster NPC, Lighthouse Examine, Boat Transfer, Begin Departure, both return transfers, Departure Sequence) is reachable and passable; the hut interior is correctly impassable (736 reachable cells on Map013, 347 on Map014).

## Remaining Issues / Questions

- Shoreline edge/corner autotile shaping is not done — the water footprints use a uniform interior tile rather than proper shoreline transition shapes, so the grass/water boundary is a sharp rectangle rather than a tapered coastline. Same "close enough for manual fixes" call as WO-0052's Hidden Cave terrain, made deliberately rather than risk a hand-derived shape-table bug; flagged here as a manual-polish follow-up.
- Lighthouse structure is represented via the existing character-sprite decorative events (`!Door1` base marker, `!$ SP CONTROL PANEL-V1-LIGHT` examine sprite) standing on open dock terrain, not a tile-built tower — matches IMP-HOM-014's instruction to keep the harbor readable without a custom plugin, but is a thinner visual than the hut.
- WO-0047's human runtime playtest is still open/blocked on Chris; that same playtest gate now applies to Rustshore Docks and Mainland Departure as well, alongside Gate A and Hidden Cave.
- Journey II's actual destination (Coalmouth vs. a landing screen) remains an open question already logged on SCR-HOM-RST-002 — TRN-HOM-026 still targets the pre-existing "Journey II start placeholder" (Map050), unchanged by this WO.
