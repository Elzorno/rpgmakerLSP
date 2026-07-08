# WO-0035 Implementation Report — Gate A Elara House Production Map

Work order: `WO-0035-build-gate-a-elara-house-production-map.md`
Packet: `IMP-HOM-018` | Screen: `SCR-HOM-ASH-002` | Map: `Map002` (`INT_Ashford_ElaraHouse`)
Date: 2026-07-05

## Completed

1. Ledger flipped first: `map_ownership.json` map 2 set to `hand_authored` before any map edit (game-repo AGENTS.md rule 4).
2. Map002 rebuilt as a production interior (17x13, `Inside` tileset, Region 0 only, no encounters, Town1 BGM placeholder retained):
   - Wood-wall room (A4 Wall H face + ceiling strip) surrounded by A5 darkness; wood-stripe floor; 3x3 red rug centering the start/Elara cluster.
   - Landmarks per SVG guide adjacency: Kai's bed lower-left (3,8-9); Elara's table (11-12,8) with two chairs and a teapot; brick hearth on the north wall (4,2-3); family keepsake bookshelf right of Elara against the north wall (13,2-3); windows (2,1-2) and (12,1-2); clock as the small old-world decoration (7,2); pot and barrel corner clutter; entrance mat + door graphic at the exit (8,12).
   - Collision verified programmatically: walls/furniture block; player start (8,6) has free movement in all four directions; BFS confirms walkable paths start→Elara, start→keepsake examine tile, start→exit; ceiling strip unreachable.
   - Autotile shapes computed with the engine's own FLOOR/WALL autotile tables (`rmmz_core.js`); full-map render written to `reports/atlas-import/wo-0035-map002-render.png` for review.
3. Atlas event anchors preserved/repaired:
   - `EVT-HOM-001` Player Start (8,6): autorun page 1 (Current_Journey=1, Archive_Recovery_Percent=0, sets `J1_Ashford_IntroComplete` ON per executable spec ATLAS-TEC-054 §3.8), inert page 2 gated on that switch. Placeholder text/self-switch pattern removed.
   - `EVT-HOM-002` Elara (8,4): five story-state pages per SCR-HOM-ASH-002, gated on `J1_Tremor_Event`, `J1_Sword_Obtained`, `J1_Node07_Offline`, `J1_Mainland_TravelUnlocked` (default page = Intro). Dialogue text taken verbatim from ATLAS-STY-010 (Ashford Dialogue Packet) Elara states 01-05; no new canon written.
   - `TRN-HOM-001` (8,12): player-touch transfer now lands beside the Elara House door on Map001 at (17,28), facing down, instead of the placeholder (8,6) mid-map drop. Registry "always open" condition kept (free-start design question remains open per packet non-goals).
   - `INT-ASH-ELARA-KEEPSAKE` examine moved onto the shelf's solid tile (13,3); placeholder lore line kept (registry ID not yet assigned).
   - Six `DEC-*` landmark anchors kept as invisible comment-only anchors, repositioned onto the built landmarks; placeholder marker graphics removed; duplicate-tile collisions with the start and keepsake events resolved.
4. `System.json`: switches 15 `J1_Ashford_IntroComplete` and 16 `J1_Node07_Offline` added (required by the five Elara states and start event; both defined in IMP-HOM-002's required-switch list but previously absent).
5. Ownership audit, Atlas validation, and full route audit run (results below).

## Files Modified

- `TheLastSwordProtocol-Game/data/Map002.json` — full hand-authored rebuild (tiles + events + note).
- `TheLastSwordProtocol-Game/data/System.json` — added switches 15 and 16 (names only).
- `TheLastSwordProtocol-Game/map_ownership.json` — map 2 `generated` → `hand_authored`; `updated` date.

## Files Created

- `rpgmakerLSP/reports/atlas-import/gate-a-map002-route-audit.md` (WO-required audit output).
- `rpgmakerLSP/reports/atlas-import/wo-0035-map002-render.png` (review render of the built map).
- `rpgmakerLSP/reports/atlas-import/wo-0035-gate-a-map002-build-report.md` (this report).
- A one-shot build script stood in for the RPG Maker editor session and was deleted after the build so it can never be re-run over the now-hand-authored map.

## Player-Visible Progress

The first thing a player ever sees is now a real room instead of placeholder geometry: a readable, cozy single-room interior with bed, hearth, table and chairs, keepsake shelf, and a clear sightline from wake-up spot to both Elara and the door. New game starts here with free movement; Elara answers with the correct one of five story states across the whole Journey I arc; the exit walks out to Ashford Exterior beside the house door rather than teleporting to a random tile. Estimated playable-minutes impact: the opening 1–2 minutes of Journey I (wake → talk to Elara → leave the house) are now production-quality — the first nonzero production-ready playable minutes for Gate A.

## Commands Run

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate                      # in TheLastSwordProtocol-Atlas
python3 tools/atlas-import/audit_map_ownership.py --project-root ../TheLastSwordProtocol-Game   # in rpgmakerLSP
python3 tools/atlas-import/audit_all_map_routes.py reports/atlas-import/gate-a-map002-route-audit.md
```

(Note: the WO's positional-argument form of the ownership audit is not accepted by the script; `--project-root` is the supported flag.)

Plus a scripted collision/reachability check (BFS over layered-tile passability with priority-1 events as blockers) and an engine-faithful tile render for visual review.

## Validation Result

- Atlas validation: **0 errors, 0 warnings**.
- Map ownership audit: ledger OK, 17 maps; Map002 `hand_authored`, pipeline may write: **NO**; 16 maps remain `generated`.
- Route audit (`gate-a-map002-route-audit.md`): **found=258, missing=0, warning=0** — TRN-HOM-001/002 verified both directions, all screens still reachable from start.
- Acceptance criteria (IMP-HOM-018): new game starts in-room with free movement ✔; Elara interactable with correct story state ✔; keepsake shelf distinct and beside Elara ✔; collision matches visible boundaries ✔; exit transfers to SCR-HOM-ASH-001 near the entrance anchor ✔; zero random encounters (Region 0, empty encounter list) ✔; tone: small/cozy/safe ✔ (see render).

## Remaining Issues / Questions

- SCR-HOM-ASH-002 open design questions remain unresolved by design (packet non-goals): must-talk-before-leaving, starting item, keepsake foreshadowing. TRN-HOM-001 is built "always open"; if the must-talk gate is chosen later, add a switch condition page to event 3.
- The older executable event spec (ATLAS-TEC-054 §3.4) describes EVT-HOM-002 as 4 pages using `NPC_Ashford_PostNode07`; the newer packet/screen use five states with `J1_Node07_Offline`. This build follows the packet. The spec doc may want a reconciliation pass.
- Keepsake examine text is still the approved placeholder; registry ID and final lore line pending.
- Runtime playtest in the actual engine (Gate A certification) still needs a human pass — everything here was verified against data, flags, and an engine-faithful render, not a live playthrough.
- Map002 was left `hand_authored` (not `locked`) so the editor pass for Gate A certification can still adjust it; lock after certification if no further edits are expected.

Not committed, per the work order.
