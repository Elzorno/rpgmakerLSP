# WO-0048 Implementation Report — Build Skyreach Hill Production Map

Work order: `WO-0048-build-skyreach-hill-production-map.md`
Screen: `SCR-HOM-SKY-001` | Map: `Map004` (`DGN_SkyreachHill_Path`)
Date: 2026-07-10

## Completed

1. **Hand-built Map004's terrain**, replacing the bare 30x40 generated scaffold with a winding stone path (south Ashford landing → north Hidden Cave mouth, with a westward jog for "winding hill path" character), a forest/cliff border enclosing the map, and a carved-out west overlook pocket for the `DEC-...-WEST-CLIFF-OVERLOOK` landmark — all per `SCR-HOM-SKY-001`'s Map Intent and the SVG layout guide's zone anchors (which the existing generated event positions already matched exactly; I verified this by decoding the SVG's pixel coordinates against the event table before building).
2. **Built a validated autotile-shape algorithm rather than guessing RPG Maker's internal shape IDs.** RPG Maker MZ's map-editor shape computation isn't in the shipped engine code (`rmmz_core.js` only renders precomputed shapes). Instead of reconstructing the algorithm from memory, I derived it empirically: parsed every ground-autotile tile in the already-verified `Map001.json`, recorded each tile's real 8-neighbor same/different pattern against its actual stored shape, and built a per-quadrant lookup table from that (72/74 patterns matched with zero ambiguity; the remaining 2 were a rare thin-strip corner case with a cosmetic-only mirror swap). Applied the same technique to Map004.
3. **Rendered the result with a custom PIL compositor implementing `rmmz_core.js`'s exact `_addAutotile`/`_addNormalTile` source-rect math** against the real `Outside_A2.png`/`Outside_B.png` tileset images, then visually inspected it. This caught a real bug on the first pass — I had passed my internal terrain-type enum (0/1/2) into the autotile-ID formula instead of the tileset's actual autotile kind numbers (16=grass, 19=stone path), which rendered as garbage (black fill, decorative furniture sprites instead of path). Fixed and re-rendered clean. See `wo-0048-map004-render.png`.
4. **Caught and fixed a second bug from visual inspection**: the west cliff overlook pocket was fully sealed by the surrounding forest border, making that landmark unreachable. Opened a 2-tile connector back to the main field.
5. **Verified collision programmatically**: BFS from the Ashford-side landing (15,38) reaches 907 of 909 interior-passable tiles, including every transfer and every landmark event's adjacent tile (the 2 unreached tiles are incidental single-cell pockets, not landmarks).
6. **Fixed `EVT-HOM-010` Skyreach Gate**, which had a real bug independent of terrain: it was a single-page event with `through: false`, meaning it would physically block the path forever, even after `J1_Skyreach_AccessOpen` turned on (the executable event spec calls for 2 pages, one of which removes the blocker). Split into a blocked page (authored text from `ATLAS-STY-012` `PH-DLG-SKY-GATE-BLOCKED`) and an open page (`through: true`, no interaction).
7. **Applied `ATLAS-STY-012` (Approved status) text** to every dialogue-bearing slot on this map: the Gate's blocked page, the Geometric Stones optional examine (`PH-DLG-SKY-CARVING`, given a proper one-time/repeat self-switch pair matching the pattern used elsewhere on Home Island), and `TRN-HOM-009`'s locked-page fallback (not covered by the packet's slot table since this transfer sits past the Gate and is only reachable off the intended path; authored a short consistent line and added it to `ATLAS-STY-012` as a documented addendum before applying it, per the "author in Atlas first" discipline).
8. **Found and fixed a WO-0046 gap while reading `ATLAS-STY-012`**: the Skyreach Joker (Map001) was missing the packet's `PH-DLG-ASH-JOKER-OPEN` middle page (access-open, before the Sword) — WO-0046 only read the Ashford packet's Joker scaffold and gave it 2 pages (intro / after-Sword) instead of the 3 the cross-screen packet actually defines. Now correctly 3 pages: intro (switch1 OFF) → access-open (`J1_Skyreach_AccessOpen`, switch 2) → after-Sword (`J1_Sword_Obtained`, switch 7).
9. **Region/encounters**: tagged a south-middle "tall grass" swath (already-existing troop list, region 1) off the path, matching the screen spec's "optional very light encounters only."
10. **Flipped Map004 to `hand_authored`** in the ledger with a certification note, matching the WO-0045/WO-0046 documentation pattern.

## Files Modified

- `TheLastSwordProtocol-Game/data/Map004.json` — full hand-authored terrain rebuild (tiles + regions); Skyreach Gate split to 2 pages; Geometric Stones given one-time/repeat text; TRN-HOM-009 locked text finalized.
- `TheLastSwordProtocol-Game/data/Map001.json` — Skyreach Joker fixed to 3 pages (WO-0046 gap).
- `TheLastSwordProtocol-Game/map_ownership.json` — Map004 `generated` → `hand_authored` with certification notes; Map001 note appended for the Joker fix.
- `TheLastSwordProtocol-Atlas/atlas/docs/03_Story/Dialogue/Home_Island/Skyreach_Hidden_Cave_Dialogue_Packet.md` — added the TRN-HOM-009 locked-page line as a documented addendum.
- `TheLastSwordProtocol-Atlas/atlas/planning/workorder_queue.json` — retired the `build-skyreach-hill-production-map` candidate with a completion note.

## Files Created

- `TheLastSwordProtocol-Atlas/atlas/workorders/WO-0048-build-skyreach-hill-production-map.md` (planner-generated).
- `rpgmakerLSP/reports/atlas-import/skyreach-map004-route-audit.md` (WO-required audit output).
- `rpgmakerLSP/reports/atlas-import/wo-0048-map004-render.png` (engine-faithful visual review render).
- `rpgmakerLSP/reports/atlas-import/wo-0048-skyreach-map004-report.md` (this report).
- Two one-off Python scripts (build + render) run from the session scratchpad, not left in either repo — they depend on a pickled autotile lookup table built at session time and aren't meant to be re-run standalone; the technique (derive shape mapping empirically from a known-good map, don't hardcode it) is worth reusing for future Home Island exterior builds, but the script itself isn't a durable tool yet.

## Player-Visible Progress

Skyreach Hill Path is no longer a bare gray rectangle — it's a readable uphill route: forest and a cliff edge (with one lookout pocket) contain a winding stone path from the Ashford-side landing up to a visible cave mouth, passing a carved-stone landmark and warning stones off to the side. The rope-gate now actually stops the player before `J1_Skyreach_AccessOpen`, shows real "inherited warning" text, and — critically — actually lets the player through once the switch flips, which the previous single-page version would not have done. The Skyreach Joker back in Ashford now has the middle "the rope's down" beat that was missing. Combined with Gate A, the player can now walk a continuous, non-placeholder route from Ashford through the tremor, up Skyreach Hill, to the (not-yet-built) Hidden Cave entrance.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py next        # generated WO-0048
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/skyreach-map004-route-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
grep -o '\[Placeholder\][^"]*' ../TheLastSwordProtocol-Game/data/Map001.json ../TheLastSwordProtocol-Game/data/Map004.json
```

Plus the scratchpad build/render scripts (empirical autotile-shape derivation, terrain generation, PIL compositing) and a standalone BFS reachability check, all run from the session shell.

## Validation Result

- Atlas validation: **0 errors, 0 warnings**.
- Map ownership audit: 19 maps; `hand_authored=5` now (Map001, Map002, Map003, Map004, Map026); Map004 pipeline may write: **NO** (correctly protected).
- Route audit: **found=228, missing=21, warning=9** — identical totals to the WO-0045/0046 baseline. The two Skyreach-relevant "missing" entries (`TRN-HOM-005-CMD`, `TRN-HOM-006-CMD`) are the pre-existing WO-0024 overworld-routing gap (both transfers correctly route through the not-yet-built Map027 hub rather than directly between Map001/Map004, matching WO-0024's design) — confirmed pre-existing, not a regression, by the unchanged totals. TRN-HOM-009 and TRN-HOM-010 (Skyreach ↔ Hidden Cave) are both fully `found`.
- Collision: BFS reachability 907/909 interior tiles; every transfer and landmark event confirmed reachable.
- `grep [Placeholder]`: zero matches across Map001-004.

## Remaining Issues / Questions

- Human runtime playtest is still the actual acceptance gate, same as WO-0045/0046 — this pass is a thorough data-level + rendered-visual audit, not a substitute for walking the route in the engine.
- The autotile-shape lookup table was derived from Map001's kind16 (grass) and kind19 (path) usage; it covers the two ground types this map needed. If a future Home Island exterior needs a ground type Map001 doesn't use (sand, water, etc.), the same derivation technique will need to run against whichever map first established that type, or fall back to the 2 conflict-prone thin-strip cases noted above.
- The Geometric Stones optional examine used a self-switch (one-time detailed text, then a shorter repeat), matching the pattern established for other Home Island examine points, even though `ATLAS-STY-012` didn't explicitly specify the self-switch mechanic for it — this is a reasonable extrapolation from the pattern, not new lore, but worth a quick confirm.
- Not committed, per the work order.
