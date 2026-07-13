# Ashford Inn (Map026) Rebuild — Implementation Report

Date: 2026-07-13

Chris chose "rebuild Ashford Inn" as the next priority after the WO-0047 playtest pass and the Glassfield/Skyreach remediation. Map026 was the only map with a formal prior Academy grade (`GRD-ASHFORDINN-003`, outcome `rejected`), documenting an incomplete fireplace, three mismatched bed styles, and floor-placed picture frames with no base.

## A Real Complication, Surfaced and Corrected Mid-Pass

The first rebuild attempt trusted `OBS-ASHFORDINN-001`'s tile identification (fireplace at tiles 126/127/142/143, picture frames at tiles 24-28, beds at tiles 88-92/104-108) and placed replacement/repaired furniture accordingly. Rendering the result showed grey pillars, rock piles, and a wooden crate where picture frames and a wardrobe were supposed to appear — clearly wrong.

Root cause: `Inside_B.png` (and every RPG Maker MZ B/C tileset sheet) is addressed by `rmmz_core.js`'s real formula (`sx_col = (tileId // 128) % 2 * 8 + tileId % 8`, `sy_row = (tileId % 256) // 8 % 16`), not a simple 16-tiles-per-row grid. A manual verification crop written during this pass used the naive row-major formula instead, produced confident-looking but wrong answers, and the resulting mis-identification was trusted without cross-checking against the one tool in this session already known to compute tile addressing correctly (the render compositor, built from the real formula weeks earlier). The error was only caught because the render didn't match intent — exactly the discipline `academy/knowledge/classic-jrpg-feel.md` and this session's whole render-first workflow exist to enforce.

Re-verifying by cropping precisely from the render compositor's own coordinate math (not a hand-rolled shortcut) produced a different, and more interesting, picture: the original map's "three mismatched bed styles" were actually five pieces of one connected red sofa (corner/straight/straight/straight/corner), scattered at three disconnected positions with gaps between them. The "incomplete fireplace" was a wall mirror and a blank frame sitting over a shelf of bowls — no multi-column fireplace-pediment object exists anywhere on this sheet. The "picture frames" were pillars, a crate, and rock-pile graphics.

This also corrects the project record in a more consequential way: the original 2026-07-08 human rejection ("rocks appear in the room", "sofa/furniture rendering is poor") was accurate the whole time. `OBS-ASHFORDINN-001`'s 2026-07-09 conclusion that the rocks claim was "not corroborated" was itself the error, and that error propagated silently through `GRD-ASHFORDINN-002` and `GRD-ASHFORDINN-003` for four days because nobody had rendered the tiles to check.

## Completed

- Filed `AtlasStudio/academy/observations/OBS-ASHFORDINN-003.json`, correcting `OBS-ASHFORDINN-001`'s structural_object findings with the verified tile identities and root cause above.
- Rebuilt Map026's furniture using only zoom-crop-verified tile IDs:
  - A single, complete fireplace tile (195) placed at (8,3), the exact position of the pre-existing `!Flame` hearth event, so the flame animation now sits on an actual fireplace rather than a mirror/shelf.
  - A picture-and-cabinet nook (landscape/portrait paintings over matching dresser/cabinet furniture) at (3-5, 2-3), replacing the pillar/crate/rubble tiles that were mistakenly labeled picture frames.
  - Two consistent bed alcoves (same tile used twice, not three different styles) at (11, 4-5) and (13, 4-5), replacing the scattered sofa pieces.
  - Border `tileId 1536` (Inside_A5 kind0, confirmed solid black by direct pixel sampling — the same bug class found repeatedly this session on other maps) replaced with this file's own already-in-use wall-body tile (7048), on the left/right columns and the rows below the floor.
- Repositioned/removed the bed-alcove blocker events to match the new two-bed footprint (the middle blocker's array slot was set to `null`, not spliced out, preserving every other event's id-to-index correspondence).
- Filed `AtlasStudio/academy/grades/GRD-ASHFORDINN-004.json`, moving the outcome from `rejected` to `accepted_with_notes` — deliberately not a bare `accepted`, since this rebuild has not yet had a live-editor human look.

## Files Modified

- `TheLastSwordProtocol-Game/data/Map026.json`
- `TheLastSwordProtocol-Game/map_ownership.json` — notes updated with the full correction; `review_status` set to `renderer_verified_pending_human_review`.

## Files Created

- `AtlasStudio/academy/observations/OBS-ASHFORDINN-003.json`
- `AtlasStudio/academy/grades/GRD-ASHFORDINN-004.json` (+ README updates in both directories)
- `rpgmakerLSP/reports/atlas-import/ashford-inn-rebuild-render.png`
- `rpgmakerLSP/reports/atlas-import/ashford-inn-rebuild-route-audit.md`
- This report.

## Player-Visible Progress

Ashford Inn now reads as a real inn common room: a lit fireplace as the dominant landmark, a furnished picture-and-dresser corner, and two matching guest beds — instead of a room with a broken fireplace, three clashing bed styles, and picture frames floating unsupported in the middle of the floor.

## Commands Run

```bash
cd TheLastSwordProtocol-Atlas && /usr/bin/python3 atlas-tools/cli/atlas.py validate
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
cd rpgmakerLSP && /usr/bin/python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/ashford-inn-rebuild-route-audit.md \
  --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

Plus scratchpad-only: the PIL compositor (unchanged, already correct), a zoomed-crop verification tool built and then corrected mid-pass, the terrain rebuild script, and a BFS reachability check.

## Validation Result

- `atlas.py validate`: 0 errors, 0 warnings.
- Ownership audit: Map026 remains `hand_authored`, correctly pipeline-protected.
- Route audit: `found=228 missing=21 warning=9`, identical to the existing project baseline — no regressions.
- BFS reachability: 80 reachable cells from the entry tile; all 8 events (Innkeeper, exit, both counter blockers, both bed blockers, hearth, entry marker) reachable/adjacent.

## Remaining Issues / Questions

- Not yet confirmed by a live editor/human look — the ledger says so explicitly. Given this exact map's history of an undetected tile-identification error surviving two prior grading passes, that confirmation matters more here than on most maps this session.
- No visible counter/desk graphic was added (the counter remains functionally correct via invisible blocker events only); a small further art pass could add one plus a searchable object to satisfy `dragon_quest_exploration_feel`, which remains unscored for this map.
- Not committed, per this session's standing practice.
