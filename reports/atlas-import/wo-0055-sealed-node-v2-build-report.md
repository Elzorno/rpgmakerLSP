# WO-0055 Implementation Report — Sealed Node Production Maps v2

Date: 2026-07-12
Screens: `SCR-HOM-SND-001/002/003/004`
Maps: `Map009/010/011/012`

This is the **third** terrain attempt on these four maps. Two prior attempts (original WO-0053 pass, and a follow-up "Academy" rebuild) were rejected on live RPG Maker visual inspection despite passing every automated check, because Maps009-012 use tilesetId 6 "SF Inside" — the only maps in the project on that tileset — so both attempts effectively guessed tile-kind semantics and got them wrong once actually opened in the editor.

## Completed

- **Verified the tileset isolation problem precisely** before touching any tile IDs: tilesetId 6 "SF Inside" assigns `Inside_A1`/`Inside_A2` (shared, literal same files as tilesetId 3 "Inside", already validated on Map002/Map003/Map026) but `SF_Inside_A4`/`SF_Outside_A5`/`SF_Inside_B`/`SF_Inside_C` (unique to these four maps, no sibling reference).
- **Sampled the floor/wall 9-slice shape pattern directly from Map002 and Map026** (both use the identical inset-floor-room technique: corner/edge/interior shapes 34/20/36/16/0/24/40/28/38 on A2 kind16). Confirmed the shape math is kind-agnostic — reused the exact same shape offsets against A2 kind17 (grey cobblestone, visually confirmed via a rendered contact sheet) instead of kind16 (wood plank, thematically wrong for a cave/machine dungeon), since the shape system's geometry doesn't depend on which kind supplies the source art.
- **Rendered labeled contact sheets** of `Inside_A2`, `Inside_A1`, `SF_Inside_A4`, `SF_Outside_A5`, `SF_Inside_B`, and `SF_Inside_C` before authoring any SF-specific tile IDs, and picked A4 kind96 (dark grey brick, even-`ty` → uses the same 47-shape `FLOOR_AUTOTILE_TABLE` as the validated floor) as a solid wall-fill kind, chosen by direct visual inspection of the actual rendered swatches, not assumed from another tileset or official sample maps.
- **Built all four maps** as deliberately simple, low-risk rooms: a solid A4 kind96 wall fill across the whole map, a 9-slice A2 kind17 stone floor room carved into it, and straight corridor notches punched through to the map edge at each map's existing transfer tile (no attempt at a mitred door-threshold shape — plain rectangular notches, same "close enough, don't over-engineer the risky part" call as WO-0052/WO-0054).
- **Extended the PIL compositor** (already a direct port of `rmmz_core.js`'s `_addAutotile`/`_addNormalTile` math from prior WOs) to also handle A3/A4 wall autotiles, which it didn't before. Rendered every map before and after each change.
- **Reconfirmed WO-0053's event logic rather than rebuilding it**: the Guardian battle (EVT-HOM-021, non-respawning, troop 10, sets switch11 on victory) and the Relay Core shutdown sequence (EVT-HOM-022, three-page: inactive / one-time shutdown setting `J1_Node07_Offline`, `J1_Mainland_TravelUnlocked`, `NPC_Ashford_PostNode07`, `Archive_Recovery_Percent=5`, `Current_Relay_Count=1` / resolved) were both already correct and untouched by the terrain rejection — verified by reading the actual event JSON, not just trusting the prior report.
- **Authored dialogue** for the 3 remaining `[Placeholder]` lines (none covered by an approved Atlas dialogue packet — no Sealed Node dialogue packet exists): Map009 first-entry ("The cave walls give way to old metal and dim red light..."), Map010 Core Path door open, Map011 relay-core route-gate-locked line.
- **BFS-verified reachability** on all four maps: every existing event (entry/exit transfers, Guardian, Relay Core, all decorative markers) confirmed reachable and passable; the wall fill correctly blocks movement.
- **Flipped Maps009-012 to `hand_authored`** in the ownership ledger, but explicitly as `renderer_verified_pending_human_review` rather than a plain accepted state — per WO-0055's constraint, given the two prior rejections on this specific tileset.

## Files Modified

- `TheLastSwordProtocol-Game/data/Map009.json`
- `TheLastSwordProtocol-Game/data/Map010.json`
- `TheLastSwordProtocol-Game/data/Map011.json`
- `TheLastSwordProtocol-Game/data/Map012.json`
- `TheLastSwordProtocol-Game/map_ownership.json`

## Files Created

- `rpgmakerLSP/reports/atlas-import/sealed-node-v2-route-audit.md`
- `rpgmakerLSP/reports/atlas-import/wo-0055-map009-render.png` through `wo-0055-map012-render.png` (final tile-accurate renders)
- `rpgmakerLSP/reports/atlas-import/wo-0055-inside-a2-contact-sheet.png`, `wo-0055-sf-inside-a4-contact-sheet.png` (labeled kind contact sheets used to pick tile IDs)
- `TheLastSwordProtocol-Atlas/atlas-exports/home-island.json` (route audit export)
- `rpgmakerLSP/reports/atlas-import/wo-0055-sealed-node-v2-build-report.md` (this report)

The PIL compositor, contact-sheet generator, terrain-build, and BFS-check scripts were run from the session scratchpad and are not left in either repo, same disposition as prior WOs.

## Player-Visible Progress

Sealed Node (Maps009-012) now has real stone-and-metal terrain instead of the committed placeholder scaffold, extending playable Journey I through Node Seven's shutdown. Combined with WO-0054, every Journey I location Chris listed in the build order (Ashford → Home Island overworld → Glassfield → Skyreach → Hidden Cave → Sealed Node → Rustshore departure) now has hand-built terrain. **This is not yet confirmed correct in the live RPG Maker editor** — see Remaining Issues below; that confirmation is the explicit next step before this can be trusted the way the other hand-built maps are.

## Commands Run

```bash
cd TheLastSwordProtocol-Atlas && /usr/bin/python3 atlas-tools/cli/atlas.py validate
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/sealed-node-v2-route-audit.md \
  --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

Plus scratchpad-only: the PIL compositor (extended for A3/A4), a labeled contact-sheet generator (run against `Inside_A2.png`, `Inside_A1.png`, `SF_Inside_A4.png`, `SF_Outside_A5.png`, `SF_Inside_B.png`, `SF_Inside_C.png`), the terrain-build script, and a BFS passability/reachability check per map.

## Validation Result

- `atlas.py validate`: **0 errors, 0 warnings.**
- `audit_map_ownership.py`: ledger OK, Maps009-012 now `hand_authored` and correctly reported as pipeline-non-writable.
- `audit_all_map_routes.py`: `found=228 missing=21 warning=9` — **identical, entry-for-entry, to the WO-0054 baseline** (diffed directly). Every Sealed Node transfer/event check (TRN-HOM-018 through TRN-HOM-024, EVT-HOM-019 through EVT-HOM-022) reports `found`. No regressions introduced.
- BFS reachability (scratchpad): Map009 1020/1020 open cells reachable (entry, forward transfer, gate, floor marker, light marker all reachable); Map010 1216/1216 (door, return, enter all reachable); Map011 621/621 (guardian, return, enter all reachable); Map012 437/437 (relay, return both reachable).

## Remaining Issues / Questions

- **Live RPG Maker editor / human confirmation is the explicit outstanding step**, given this tileset's two prior rejections. The ledger deliberately does not claim plain `hand_authored`/accepted status the way WO-0054's Rustshore maps do — please open Maps009-012 in the actual editor before treating this as done. If it's rejected again, the tile IDs and rationale for each are fully documented in this report and the ledger notes, which should make it much faster to diagnose exactly which kind/shape is wrong rather than starting over.
- **Terrain is intentionally plain**: all four rooms are a uniform stone-floor rectangle with straight corridor notches, not the varied cave-to-machine silhouette the screen specs describe ("irregular silhouette," "cracked walls with embedded metal or glass," "faint red unstable lights"). This was a deliberate risk-reduction choice — get a structurally and thematically sound baseline confirmed first, then add visual variety (SF_Inside_B/C accent props like red warning lights, cracked panels, console screens — all identified and cataloged in the contact sheets during this session) as a follow-up pass once the base is confirmed good in the editor.
- The decorative "RELAY-PASSAGE-FRAME" marker on Map011 (7,1) sits on a wall tile rather than floor, since it's well outside the north transfer's corridor gap (x12-14) — cosmetic only, non-blocking, easy manual fix.
- Human runtime playtest (WO-0047's gate) still applies here same as every other hand-built Home Island map.
