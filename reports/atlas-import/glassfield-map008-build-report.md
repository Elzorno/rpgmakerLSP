# WO-0050 Implementation Report — Build Glassfield Ruins Production Map

Work order: `WO-0050-build-glassfield-ruins-production-map.md`
Screen: `SCR-HOM-GLS-001` | Map: `Map008` (`DGN_Glassfield_Ruins_Exterior`)
Date: 2026-07-10

## Completed

1. **Hand-built Map008's terrain**: a 42x34 open ruin field (grassland fill, `Outside_A2` kind 16) scattered with cracked-glass-panel patches (kind 19, reused as "cracked glass-like ground panels" per the screen spec's required visual elements) and a rubble/tree border, matching the existing generated event positions I verified against the SVG layout guide's decoded pixel anchors before building (all 10 events already sat exactly on their guide anchors, same pattern as WO-0048/WO-0049).
2. **Reused this session's validated autotile-shape algorithm directly from its new home** (`atlas-tools/mapgen/compiler/autotile_shapes.py`, the real engine algorithm fixed earlier today) rather than re-deriving it — first practical payoff of moving it into the compiler as a proper module.
3. **Discovered mid-build that `SF_Outside_B.png` (Map008's tileset-5 "B" decoration sheet) is a different image than `Outside_B.png`** (used for Map001/Map004's forest border) — tile IDs 165/165 that meant "tree trunk/canopy" there mean something else entirely here (a red lamp post, not a trunk). Sampled the actual sheet, found a proper single-tile pine stamp (tileId 29) and used that instead of assuming the old ID pair carried over.
4. **Rendered the result with a PIL compositor** (same technique as WO-0048/WO-0049) against the real `Outside_A2.png` and `SF_Outside_B.png` images and inspected it before finalizing — clean autotile blending, correctly distinct glass-panel patches, border trees close enough together to read as a continuous line.
5. **Verified collision via BFS**: 1285 reachable tiles, all 10 events reachable.
6. **Found and fixed a real bug in the Glassfield Seal event** (`EVT-HOM-017`): its single page set `J1_Glassfield_SealOpened` ON unconditionally on first interaction — with no check for `J1_Sword_Obtained` at all. Per the screen spec ("Before `J1_Sword_Obtained`, the lower entrance should not open"), a player could have opened the seal to Sealed Node before ever getting the Sword. Rebuilt as 3 pages: locked (Sword OFF, no state change) / opens (Sword ON, first interaction, sets the seal switch) / already-resolved (self-switch A).
7. **Authored missing dialogue**: no dialogue packet existed for Glassfield. Created `atlas/docs/03_Story/Dialogue/Home_Island/Glassfield_Dialogue_Packet.md` (`ATLAS-STY-013`) with the seal's locked/opens text, authored in Atlas first per this session's established discipline, then applied. For the Surface Fragment, found that `ATLAS-STY-011` (Home Island Memory Fragment Standards) already has an approved, explicitly-Glassfield-triggered fragment — "Fragment 03 — Human Detail" ("optional Glassfield terminal/surface ruin") — and used it verbatim rather than inventing new text; it also nicely calls back to the warm-stone vent examine text I wrote for Ashford earlier this session. Authored a short repeat-visit line myself since Fragment 03 doesn't define one.
8. Also finalized `TRN-HOM-017`'s locked-page text (was `[Placeholder]`), reusing the same seal-locked line for consistency.

## Files Modified

- `TheLastSwordProtocol-Game/data/Map008.json` — full terrain rebuild; Glassfield Seal fixed to 3 pages; Surface Fragment and TRN-HOM-017 text finalized.
- `TheLastSwordProtocol-Game/map_ownership.json` — Map008 `generated` → `hand_authored` with certification notes.
- `TheLastSwordProtocol-Atlas/atlas/planning/workorder_queue.json` — retired the candidate with a completion note.

## Files Created

- `TheLastSwordProtocol-Atlas/atlas/docs/03_Story/Dialogue/Home_Island/Glassfield_Dialogue_Packet.md` (`ATLAS-STY-013`).
- `TheLastSwordProtocol-Atlas/atlas/workorders/WO-0050-build-glassfield-ruins-production-map.md` (planner-generated).
- `rpgmakerLSP/reports/atlas-import/glassfield-map008-route-audit.md`.
- `rpgmakerLSP/reports/atlas-import/glassfield-map008-render.png` (visual review render).
- `rpgmakerLSP/reports/atlas-import/glassfield-map008-build-report.md` (this report).

## Player-Visible Progress

Glassfield Ruins is now a real, walkable open field with visually distinct cracked-glass ground patches, a rubble/tree border, and a sealed lower entrance the player can see and approach before the Sword — matching the screen's intent ("player can explore ruins before the Sword"). Interacting with the seal now correctly refuses before the Sword and correctly opens the route to Sealed Node after, instead of the previous unconditional open. The Surface Fragment gives the first "ordinary people lived here" beat of the game, tying back to Ashford's warm-stone vent.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py next        # generated WO-0050
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/glassfield-map008-route-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
grep -o '\[Placeholder\][^"]*' ../TheLastSwordProtocol-Game/data/Map008.json
```

Plus a scratchpad build script (terrain generation, importing `autotile_shapes.py` from the Atlas compiler), a PIL render script, and a standalone BFS reachability check.

## Validation Result

- Atlas validation: **0 errors, 0 warnings** (including the new Glassfield Dialogue Packet).
- Map ownership audit: 19 maps; `hand_authored=6` now (adds Map008).
- Route audit: **found=228, missing=21, warning=9** — identical totals to every prior baseline this session; no regression.
- BFS reachability: 1285 tiles; all 10 events reachable.
- `grep [Placeholder]`: zero matches.

## Remaining Issues / Questions

- Human runtime playtest is still the actual gate, same caveat as every map this session.
- The cracked-glass-panel patches are rectangular for simplicity; a more irregular/organic shape would read more like "ruins" and less like tidy garden beds — worth revisiting in a polish pass, not a blocker.
- `SF_Outside_B.png`'s content differs meaningfully from `Outside_B.png` at the same tile IDs — worth remembering for Sealed Node and Rustshore if they use a similarly-numbered tileset sharing A1/A2 with `Outside` but a different B/C sheet; don't assume tile-ID meaning carries across tilesets, sample the actual sheet first.
- Not committed.
