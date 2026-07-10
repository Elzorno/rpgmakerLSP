# WO-0045 Implementation Report — Gate A Ashford Shop Certification

Work order: `WO-0045-build-gate-a-ashford-shop-production-map.md`
Packet: `IMP-HOM-019` | Screen: `SCR-HOM-ASH-003` | Map: `Map003` (`INT_Ashford_Shop`)
Date: 2026-07-10

## Completed

Map003 was already hand-authored and repaired in an earlier session (ledger `last_repair`, 2026-07-09: EVT-HOM-008's customer-side proxy carries the shopkeeper dialogue and Shop Processing command). No prior session had produced a formal WO-style certification report for it, unlike Map001/Map002 (`wo-0035`/`wo-0036`). This work order closed that gap: audited the existing hand-authored build against every IMP-HOM-019 acceptance criterion and recorded the result, rather than re-building an already-functional map.

1. **Entry/exit transfers (criteria 1, 7)** — `audit_all_map_routes.py` confirms TRN-HOM-003 (enter, lands at Map003 (8,6)) and TRN-HOM-004 (exit, returns to Map001 (30,19)) both `found` with valid event, position, and tile checks. Round-trip pair intact.
2. **Shopkeeper interactable across the counter (criterion 2)** — Event 1 (`EVT-HOM-008 Shopkeeper`, real NPC, position (8,3)) and Event 10 (`EVT-HOM-008 Activate Shopkeeper`, invisible customer-side proxy, position (8,5)) both carry identical two-page dialogue/shop logic. Traced the tileset passability flags for the counter tiles (`Tilesets.json` flags for tileset 3): the tile graphics themselves are not blocking (low nibble `0x0F` clear on every counter-row tile), so collision comes entirely from the placed blocker events (`Counter left block` at (7,4), `Counter right block` at (9,4), the shopkeeper NPC itself at (8,3), and the proxy at (8,5)). Every neighbor of the one nominally-passable gap tile (8,4) is blocked, so it is unreachable in practice — the counter fully encloses the shopkeeper's side.
3. **Shop menu opens (criterion 3)** — Both dialogue pages end in a `302` Shop Processing command (item 1, price 50G, `purchaseOnly=false`), not a placeholder message.
4. **Inventory is early-game safe (criterion 4)** — Item 1 in `Items.json` is "Potion", price 50, confirmed a minor consumable; nothing else is stocked.
5. **Landmarks present and visually distinct (criterion 5)** — Confirmed via full 4-layer tile dump, not just the (invisible) collision events: layer 1 carries distinct autotile IDs for the counter front (`2844/3193`, `2844/3185` variants) and a shelf/cabinet decoration cluster (`3194` at two points along the back wall), matching the SVG guide's adjacency (cabinet up-right of the shopkeeper). This is real tile art, not a flat repeated placeholder tile.
6. **Collision correct (criterion 6)** — See point 2; BFS-by-hand of the door → counter approach is clear, no unintended dead ends, no way to walk in behind the counter.
7. **No random encounters (criterion 8)** — `encounterList` empty in Map003.json; Region 0 only.
8. **Story states (criterion 9)** — Page 0 is the default (Intro) page with no switch condition; page 1 is gated on switch 16 (`J1_Node07_Offline`/`NPC_Ashford_PostNode07` per IMP-HOM-019), each with distinct dialogue text (`ATLAS-STY-010 STATE_01_INTRO` / `STATE_04_AFTER_NODE07`) and the same inventory, per the packet's instruction not to resolve the open post-Node-Seven inventory question in this pass.

## Files Modified

- `TheLastSwordProtocol-Game/map_ownership.json` — Map003 `review_status` updated from `pending_atlas_review` to `data_audit_passed_pending_human_playtest`; added `wo_0045_certification` block recording the audit method and the one non-blocking finding (unreachable tile (8,4)).
- `TheLastSwordProtocol-Atlas/atlas/planning/workorder_queue.json` — retired the `build-gate-a-ashford-shop-production-map` candidate with a completion note.

## Files Created

- `TheLastSwordProtocol-Atlas/atlas/workorders/WO-0045-build-gate-a-ashford-shop-production-map.md` (planner-generated).
- `rpgmakerLSP/reports/atlas-import/gate-a-map003-route-audit.md` (WO-required audit output).
- `rpgmakerLSP/reports/atlas-import/wo-0045-gate-a-map003-certification-report.md` (this report).

No engine-faithful render was produced this pass (no renderer script is currently checked into either repo — the Map001/Map002 renders were one-shot scripts run from a prior session's scratchpad and were not preserved). The tile-layer audit in point 5 above substitutes for it at the data level; a pixel render remains a nice-to-have for the still-pending human visual playtest.

## Player-Visible Progress

No change to what the player sees — Map003 was already playable going into this work order. What changed is confidence: Ashford Shop is now confirmed, by the same rigor applied to Map001/Map002, to be a real functional shop (readable counter/shelf/cabinet room, working shopkeeper across the counter, working buy menu, clean round-trip to the village) rather than an unreviewed hand-edit. This closes the last open item in the Gate A map set (Map001 exterior, Map002 Elara House, Map003 Shop all now certified at the data level); Map026 Inn remains rejected and out of scope for Gate A per its ledger note.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py next        # generated WO-0045
/usr/bin/python3 atlas-tools/cli/atlas.py validate
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/gate-a-map003-route-audit.md \
    --project-root ../TheLastSwordProtocol-Game --export ../TheLastSwordProtocol-Atlas/atlas-exports/home-island.json
```

Plus ad hoc Python against `Map003.json`, `Tilesets.json`, and `Items.json` to trace event pages, tile-layer contents, and passability flags (see Completed section).

## Validation Result

- Atlas validation: **0 errors, 0 warnings**.
- Map ownership audit: 19 maps listed; `hand_authored=4` (Map001, Map002, Map003, Map026); Map003 pipeline may write: **NO** (correctly protected).
- Route audit (`gate-a-map003-route-audit.md`): **found=228, missing=21, warning=9**; all 21 missing and all 9 warnings belong to the Inn (Map001/Map026) and the not-yet-built Overworld hub (Map027) transfers — none are Map003 findings. TRN-HOM-003/TRN-HOM-004 (Map003's own transfers) both `found` clean.
- IMP-HOM-019 acceptance criteria 1–9: all confirmed at the data level (see Completed section). No criterion requires an engine runtime that isn't available in this session.

## Remaining Issues / Questions

- **Human runtime playtest is still the actual gate.** This report is a thorough data-level audit, not a substitute for someone opening the project in RPG Maker MZ (or the web build at `index.html`) and walking through the shop. Do not flip Map003 to `locked` until that happens.
- Non-blocking: tile (8,4) is technically tile-passable but fully enclosed by blocking events on all four sides — cosmetically harmless, flagged in the ledger for awareness, no fix applied (fixing an unreachable no-op tile isn't a narrowly-scoped need).
- The open design questions IMP-HOM-019 explicitly defers (antidote stocking, post-Node-Seven inventory change) remain unresolved by design — not a gap in this work order.
- Next unblocked Gate A items per the workorder queue: "Apply Gate A Final Ashford Dialogue" (priority 40) and "Gate A Ashford Lives Playtest Fix Pass" (priority 50) — the latter is likely where the human playtest pass above should actually happen.
- Not committed, per the work order.
