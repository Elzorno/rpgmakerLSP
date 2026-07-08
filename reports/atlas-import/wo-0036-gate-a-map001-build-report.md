# WO-0036 Implementation Report — Gate A Ashford Exterior Production Map

Work order: `WO-0036-build-gate-a-ashford-exterior-production-map.md`
Packet: `IMP-HOM-017` | Screen: `SCR-HOM-ASH-001` | Map: `Map001` (`TWN_Ashford_Exterior`)
Date: 2026-07-06

## Completed

1. Ledger flipped first: `map_ownership.json` map 1 set to `hand_authored` before any map edit.
2. Map001 rebuilt as a production village exterior (40x32, `Outside` tileset, Region 0 only, no encounters, Town1 BGM retained), following the SVG guide's anchor adjacency:
   - Dense forest border enclosing the village, with four readable route openings: north gate funnel to Skyreach (x20), south road to Rustshore (x18), and two east roads to Glassfield (y9) and Fogfen (y23).
   - Road network: north road from plaza to the Skyreach gate (tremor trigger sits invisibly at the y9 junction), south road past Elara's house, east branches to both island routes, cobblestone village plaza as the common center.
   - Elara/Kai house (orange roof, wood walls, x12-18) with its door at (17,27) exactly on the TRN-HOM-002 anchor; door path joins the south road; the WO-0035 exit landing at (17,28) is directly outside the door.
   - Shop (yellow roof, brick, x27-33) with carved door at the (30,18) anchor, general-store sign tile, barrels/crates.
   - Elder house (x22-26) with placeholder door event ("visually present but not required to function" per IMP-HOM-017); Village Elder placeholder NPC outside at the (25,15) anchor.
   - Old humming panel: reused-metal-panel fence wall (Fencepost B Metal autotile) x3-11 y9 with the control-panel sprite examine at (7,9); child anchor two tiles south.
   - Fenced garden (metal panels again) with dirt patch, farmer at (11,18), warm-stone vent (rock fire pit + steam sprite) at (9,16), and the hidden item exactly four steps south at (9,20) — now truly hidden (chest sprite removed, logic untouched).
   - Village dressing: well, two streetlights, route signs at both gates, flowers, rocks, stumps, single and large trees.
3. All Atlas event/transfer anchors preserved; event logic untouched except:
   - TRN-HOM-002 destination repaired: now lands just inside the hand-built Elara House at Map002 (8,11) facing up (was mid-room placeholder (8,6)).
   - Dock Messenger moved (17,25) → (21,28): its anchor tile fell inside the new house footprint; packet placement is "near the southern road".
   - Tremor Trigger priority set to Below so the invisible autorun does not block the road junction; switches/self-switch logic unchanged.
   - Placeholder marker sprites removed from route transfers and decorative anchors; doors got `!Door1` graphics; elder placeholder got a person sprite.
   - Decorative DEC-* anchors repositioned onto their built landmarks; duplicate-tile overlaps (vent/steam, panel/fence anchors) resolved.
4. Collision verified programmatically: BFS from the Elara House exit landing reaches all four route transfers, the shop door, and every NPC/examine interaction tile; buildings, fences, vent, and forest border all block; the north gate remains a single gated tile with its locked-message page until `J1_Skyreach_AccessOpen`.
5. Engine-faithful render written to `reports/atlas-import/wo-0036-map001-render.png` (A2/A3/A4/B autotile rendering per `rmmz_core.js` tables).

## Files Modified

- `TheLastSwordProtocol-Game/data/Map001.json` — full hand-authored rebuild (tiles + event positions/graphics + note; event logic preserved).
- `TheLastSwordProtocol-Game/map_ownership.json` — map 1 `generated` → `hand_authored`; `updated` date.
- `TheLastSwordProtocol-Atlas/atlas/planning/workorder_queue.json` — retired the WO-0036 candidate with a completion note (plan Operating Rule 3).

## Files Created

- `TheLastSwordProtocol-Atlas/atlas/workorders/WO-0036-build-gate-a-ashford-exterior-production-map.md` (planner-generated).
- `rpgmakerLSP/reports/atlas-import/gate-a-map001-route-audit.md` (WO-required audit output).
- `rpgmakerLSP/reports/atlas-import/wo-0036-map001-render.png` (review render).
- `rpgmakerLSP/reports/atlas-import/wo-0036-gate-a-map001-build-report.md` (this report).
- One-shot build script ran from the session scratchpad (not left in any repo), so it cannot be re-run over the hand-authored map.

## Player-Visible Progress

Stepping out of Elara's house now shows a real village: three distinct buildings with working doors, a cobblestone commons with a well and streetlights, a fenced garden hiding the warm-stone vent and the four-steps-south secret, a hulking line of reused metal panels with the humming panel the children play at, and four clearly readable exits — gated north hill path, south dock road, and two east island routes. Combined with WO-0035, the entire Gate A Ashford loop (wake → Elara → village → tremor → gated north route) is now on production maps. Estimated playable-minutes impact: roughly 3–5 production-quality minutes of village exploration and QST-HOM-001 setup, up from zero placeholder-free exterior minutes.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py next        # generated WO-0036
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/gate-a-map001-route-audit.md
```

Plus the scripted BFS collision/reachability check and the engine-faithful render.

## Validation Result

- Atlas validation: **0 errors, 0 warnings**.
- Map ownership audit: 17 maps; `hand_authored=2` (Map001, Map002); pipeline-writable: 15; Map001 pipeline may write: **NO**.
- Route audit (`gate-a-map001-route-audit.md`): **found=258, missing=0, warning=0**.
- IMP-HOM-017 acceptance criteria: readability of all four exits + both doors ✔; vent and panel landmarks distinct and beside their events ✔; collision correct with no unintended dead ends (BFS-verified) ✔; all required events present with registry logic intact (hidden item self-switch, tremor switch sets, north gate switch gating) ✔; transfers correctly gated ✔; zero random encounters ✔; tone: warm village with subtle old-world remnants (metal-panel fences, humming panel, steam vent) ✔.

## Remaining Issues / Questions

- Live engine playtest for Gate A certification still needs a human pass; lock Map001 (and Map002) after certification.
- Elder house door is a message-only placeholder by design (no interior screen exists); when an elder interior screen is specced, replace with a real transfer.
- TRN-HOM-003/005/007/015/027 destination coordinates still point at (8,6) in their target maps — correct while those maps remain generated placeholders; revisit as each target map is hand-built (as done here for TRN-HOM-002).
- The Skyreach Joker's "hill taboo" placement is near the north road per the SVG; if the tremor cutscene later needs him repositioned for staging, that's a dialogue-pass concern (WO "Apply Gate A Final Ashford Dialogue").
- Not committed, per the work order.
