# Last Sword Protocol — Agent Handoff Note

**Last updated:** 2026-06-29  
**Session:** Act II Towns 1–2 implementation complete

---

## Where We Are

Act I is fully implemented. Act II has two towns complete.

### Relay Node Count
NEMESIS has 7 total relay nodes in its network.
- **Node 7 (Coalmouth mine):** OFFLINE — Sword shuts it down; Vera joins party
- **Node 6 (Athenaeum Signal Tower):** OFFLINE — Sword shuts it down; Eldon joins party
- **Nodes 1–5:** ACTIVE — locations are Towns 3–5 + two in Act III (Dead Circuit)

---

## Party

| Actor ID | Name | Class ID | Joins At |
|---|---|---|---|
| 1 | Kai | 1 (Swordsman) | Start |
| 2 | Vera | 7 (Hunter) | Coalmouth relay (Map 22 EV5) |
| 3 | Eldon | 3 (Priest) | Athenaeum relay (Map 28 EV2 page 3) |
| 4 | Cipher | 2 (Sorcerer) | The Drift, Town 4 — NOT BUILT YET |

All actor sprites are placeholders (Actor2/3/4). Custom assets needed.

---

## Switch Registry

| ID | Name | Set By |
|---|---|---|
| 1 | Chamber 1 Complete | Map 17 |
| 2 | Chamber 2 Complete | Map 18 |
| 3 | Chamber 3 Complete | Map 19 |
| 4 | All Chambers Complete | Map 17/18/19 (last to complete) |
| 5 | Sword Obtained | Map 9 EV12 |
| 21 | Mine Authorized | Map 23 EV2 (Briggs) |
| 22 | Mine Cleared / Relay Offline | Map 22 EV5 (Relay Node) |
| 25 | Iron Foreman Defeated | Map 22 EV4 |
| 31 | Signal Tower Authorized | Map 28 EV2 (Eldon) |
| 32 | Athenaeum Node Offline | Map 29 EV5 (Signal Node) |
| 35 | Broadcast Engine Defeated | Map 29 EV4 |

Reserve switches 41–45 for Town 3 (Irongate), 51–55 for Town 4 (The Drift), 61–65 for Town 5 (New Meridian).

---

## Map Registry

| ID | Name | Tileset | Parent | World Entrance |
|---|---|---|---|---|
| 1 | Overworld (World 1) | 1 | — | — |
| 2 | World Map (overworld travel layer) | 1 | — | — |
| 7 | Ashford Village | 2 | — | — |
| 8 | Kai's House | 3 | 7 | — |
| 9 | Sword Pedestal Chamber | 9 | — | — |
| 15 | Elder's House | 3 | 7 | — |
| 17 | Chamber 1 (Physical) | 7 | — | — |
| 18 | Chamber 2 (Mental) | 8 | — | — |
| 19 | Chamber 3 (Spiritual) | 9 | — | — |
| 21 | Coalmouth | 10 | 0 | Map 2 EV6 at (68,62) |
| 22 | Coalmouth Mine | 11 | 21 | — |
| 23 | Foreman's Hall | 12 | 21 | — |
| 24 | Soot and Steam Inn | 12 | 21 | — |
| 25 | Collier's Post (shop) | 12 | 21 | — |
| 26 | Vera's Workshop | 12 | 21 | — |
| 27 | The Athenaeum | 13 | 0 | Map 2 EV7 at (80,45) |
| 28 | Grand Archive | 14 | 27 | — |
| 29 | Signal Tower | 15 | 27 | — |
| 30 | Scholar's Rest (inn) | 14 | 27 | — |
| 31 | Eldon's Study | 14 | 27 | — |
| 32 | The Bookwright's (shop) | 14 | 27 | — |

Next maps start at **33**. Reserve 33–38 for Town 3 (Irongate).

---

## Tileset Registry

| ID | Name | Use |
|---|---|---|
| 1 | Overworld | World map |
| 2 | Outside | Generic exterior |
| 3 | Inside | Generic interior |
| 4 | Dungeon | Generic dungeon |
| 7 | Gauntlet (Chamber 1) | Act I |
| 8 | LSP Chamber 2 Terminal Lab | Act I |
| 9 | Chambers | Act I |
| 10 | Coalmouth Town | Act II Town 1 exterior |
| 11 | Coalmouth Mine | Act II Town 1 dungeon |
| 12 | Coalmouth Interior | Act II Town 1 interiors |
| 13 | Athenaeum Exterior | Act II Town 2 exterior |
| 14 | Athenaeum Interior | Act II Town 2 interiors |
| 15 | Signal Tower | Act II Town 2 dungeon |

Next tilesets start at **16**. Reserve 16–18 for Town 3 (Irongate).

---

## Known TODOs (Manual Editor Work Required)

### Coalmouth
- [ ] Iron Foreman troop: create troop ID 1 with Iron Foreman MK-VII + Survey Drone reinforcements, Drill Charge, Signal Pulse, Reinforcement Call mechanics
- [ ] Mine Gate Guard (Map 21 EV7): add page 2 with Switch 21 condition (guard steps aside)
- [ ] Pip (Map 21 EV9): add page 2 with Self-Switch A condition (already gave schematic)
- [ ] CUTTER-9 side quest (Map 21 EV8): add page 2 for after Vera joins (purify option available)
- [ ] Verify item IDs: Mine Map = item 3, Schematic Fragment = item 5

### Athenaeum
- [ ] Data Wraith troop: create troop ID 2 with signal-manifestation enemies
- [ ] Broadcast Engine troop: create troop ID 3 with Broadcast Engine boss + Phantom Receivers
- [ ] Inn recovery (Map 30 EV2): add HP/MP restore — currently only does a fadeout/fadein; need code 314 (Recover All) before the fadein
- [ ] Ancestor's Notes: create as key item in database (referenced in Eldon join scene)
- [ ] Custom sprites: replace Actor2/3/4 placeholders when VERA, ELDON, CIPHER art is ready

### Both Towns
- [ ] All maps need tile painting in editor (ground, walls, structures)

---

## What to Build Next

### Option A — Town 3: Irongate (recommended next)
Military settlement. The commander takes orders from "The Voice" (NEMESIS via Herald). Kai exposes the Herald for the first time. The Herald escapes.

Story beats:
1. Arrival at a walled fortress-town, soldiers on edge
2. Commander Aldric is acting strange — issuing orders that make no strategic sense
3. Investigation reveals a receiver hidden in the command tower
4. First encounter with The Herald (NEMESIS's human avatar) — named antagonist, believes NEMESIS is a god
5. Boss: something military — corrupted war-machine or Herald-summoned construct
6. Relay Node 5 goes offline
7. Herald escapes before Kai can stop him — sets up recurring antagonist

Characters to introduce: Commander Aldric (compromised), The Herald (first appearance, escapes), soldiers who are divided

No party member joins at Irongate.

### Option B — Kai's Skill Tree
Kai learns data-elemental abilities as Ancestor memories are processed. Currently he only has Swordsman skills. Could build out a custom skill tree with:
- Data Strike (single target, data-elemental)
- Signal Break (disrupts enemy state/buff)
- Protocol Override (boss-only: stun for one turn)
- Memory Surge (unlocked mid-fight at Coalmouth — now retroactively available)

### Option C — Data Element Setup
Add "Data" as a custom element in the database (currently not in elements list). All NEMESIS constructs should be weak to Data, resistant to physical. Required for Kai's skill tree to work correctly.

---

## Story Bible
Full scene-by-scene breakdowns exist for:
- Act I (all scenes)
- Act II Town 1: Coalmouth (11 scenes, lines 108–320)
- Act II Town 2: The Athenaeum (11 scenes, lines 323–510 approx.)

Towns 3–5 and Acts III–IV have summary-level content only. Expand before implementing.
