---
atlas_id: ATLAS-TEC-053
title: Home Island Vertical Slice Readiness Review
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-030
  - ATLAS-TEC-040
  - ATLAS-TEC-041
  - ATLAS-TEC-042
  - ATLAS-TEC-043
  - ATLAS-TEC-044
related:
  - IMP-HOM-009
  - ATLAS-AI-012
  - ATLAS-TEC-055
---

# Home Island Vertical Slice Readiness Review

## Objective

Answer one production question:

Can a developer build Home Island today using Atlas alone?

## Verdict

No.

Atlas has enough high-level structure to start Home Island implementation, but it does not yet contain enough unambiguous RPG Maker MZ production detail for an unfamiliar developer to build the vertical slice without inventing critical implementation decisions.

This review lists blockers only.

---

## Readiness Snapshot

| Area | Ready? | Blocker? | Notes |
|---|---:|---:|---|
| Screen inventory | Yes | No | Home Island screen registry defines all current core and optional Fogfen screens. |
| Transfers | Yes | No | Transfer registry defines critical and optional Fogfen routes. |
| State model | Yes | No | Switches and variables are traced in `ATLAS-TEC-044`. |
| Map dimensions | Mostly | No | All playable maps have dimensions or approximate dimensions; `SCR-HOM-RST-002` is cutscene-style and does not block map production. |
| NPC roster | Mostly | No | Ashford has a roster and placement guidance; schedules are not required by current Atlas scope. |
| Dialogue IDs | No | No | Stable line IDs are missing, but placeholder dialogue is explicitly allowed for the vertical slice. |
| Music IDs | Mostly | No | Location BGM placeholder names and cue directions exist. |
| Sound effect IDs | Mostly | No | Major story SFX cue IDs exist. |
| Encounter tables | Partial | Yes | Enemy and troop concepts exist, but RPG Maker-ready combat data is incomplete. |
| Tileset references | No | Yes | Maps lack concrete tileset assignments or placeholder tileset IDs. |
| Animation IDs | No | Yes | Required skill and story animations are not assigned. |
| RPG Maker event pages | Yes | No | `ATLAS-TEC-055` defines executable Home Island event pages for the current vertical slice. |

---

## Blocker Punch List

### BLK-HOM-001 — Add RPG Maker Event Page Specifications

Blocking question:

Can a developer implement critical events without deciding page conditions, triggers, command order, and fallback behavior?

Current answer:

Yes, for the current Home Island vertical slice.

Resolution:

`ATLAS-TEC-055` defines executable event specs for the current Home Island vertical slice, including map transfers, treasure, save/recovery pattern, core NPC interactions, trial entry/exit events, required story gates, boss event, relay event, Rustshore departure, and optional Fogfen events.

Former missing production data:

| Event Area | Missing Detail |
|---|---|
| Elara intro and Ashford progression | Exact event page matrix for intro, tremor, post-Sword, post-Node, and departure states |
| Skyreach gate | Page conditions, blocked text, opened transfer behavior, trigger type, and priority |
| Hidden Cave trials | Exact event pages for Body, Mind, and Heart trial success/failure states |
| Sword pedestal | Page conditions before/after all trials, command order, item grant behavior, SFX/flash/fade commands |
| Glassfield seal | Page conditions before Sword, after Sword, after seal opened, transfer behavior |
| Guardian encounter | Battle processing page, defeat branch, loss branch, post-defeat page |
| Relay core | Page conditions before guardian, shutdown command order, variable/switch updates, post-shutdown page |
| Rustshore dockmaster and boat | Locked page, unlocked page, confirmation flow, departure transfer page |

Required output:

- Complete. See `ATLAS-TEC-055`.

Do not add new story beats while fixing this.

---

### BLK-HOM-002 — Define Trial Mechanics Enough To Build

Blocking question:

Can a developer build the Body, Mind, and Heart trials without inventing gameplay?

Current answer:

No.

Missing production data:

| Trial | Missing Detail |
|---|---|
| Body Trial | Whether this is combat, movement, or interaction; success condition; failure/reset behavior; enemy/troop if combat |
| Mind Trial | Exact pattern/observation rule; interactable objects; success condition; reset behavior |
| Heart Trial | Exact choice or memory interaction; whether any choice can fail; success condition |

Required output:

- Add a structural trial specification for `SCR-HOM-HCV-002` that defines the eventable mechanic for each trial using existing Atlas story intent.

Do not write new lore dialogue except minimal placeholder text required for event operation.

---

### BLK-HOM-003 — Complete RPG Maker Combat Database Data

Blocking question:

Can a developer create the Home Island enemy, skill, state, and troop database entries without guessing?

Current answer:

No.

Missing production data:

| Area | Missing Detail |
|---|---|
| Enemy stats | HP, MP, attack, defense, agility, luck, EXP, gold, hit/evasion assumptions |
| Skill effects | Exact RPG Maker formulas or effects for `Murk Bubble`, `Pulse Guard`, `Warning Tone`, and `Relay Burst` |
| States | Whether poison/debuff exists in Journey I; state ID/name/effects if used |
| Troops | Stable troop IDs, event pages if any, battleback guidance |
| Guardian | Final Journey I boss object behavior is still partly placeholder; final ID/name question remains open in `IMP-HOM-004` |

Required output:

- Create a Home Island combat database specification that turns `IMP-HOM-005` into RPG Maker-ready enemy, skill, state, and troop rows.

Keep balance first-pass and adjustable, but remove ambiguity.

---

### BLK-HOM-004 — Assign Tileset Or Placeholder Tileset References

Blocking question:

Can a developer create maps without choosing tilesets outside Atlas?

Current answer:

No.

Missing production data:

| Map Group | Missing Detail |
|---|---|
| Ashford exterior/interiors | Concrete RPG Maker tileset or placeholder tileset assignment |
| Skyreach / Hidden Cave | Concrete field/cave tileset assignment |
| Glassfield / Sealed Node | Concrete ruin/node tileset assignment |
| Rustshore | Concrete town/coastal tileset assignment |
| Fogfen | Concrete marsh tileset assignment |

Required output:

- Add a Home Island tileset assignment matrix mapping every `SCR-HOM-*` screen to an RPG Maker tileset name or approved placeholder tileset.

This can use existing RTP or prototype tilesets; it does not require final art.

---

### BLK-HOM-005 — Assign Animation IDs For Required Combat And Story Beats

Blocking question:

Can a developer wire battles and key story events without choosing animations outside Atlas?

Current answer:

No.

Missing production data:

| Required Beat | Missing Detail |
|---|---|
| Sword authentication | Animation ID or approved no-animation/fade/flash rule |
| Glassfield seal opening | Animation ID or approved no-animation/fade/flash rule |
| Node Seven shutdown | Animation ID or approved no-animation/fade/flash rule |
| `Murk Bubble` | Animation ID or approved placeholder animation |
| `Pulse Guard` | Animation ID or approved placeholder animation |
| `Warning Tone` | Animation ID or approved placeholder animation |
| `Relay Burst` | Animation ID or approved placeholder animation |

Required output:

- Add an animation assignment matrix for required Home Island story events and combat skills.

Use existing RPG Maker animations if final assets are not ready.

---

## Non-Blocking Missing Items

These are not blockers under the current vertical-slice rules:

| Item | Why It Is Not Blocking |
|---|---|
| Final dialogue | Placeholder dialogue is explicitly allowed. |
| Stable dialogue line IDs | Useful for tooling, but not required to build a playable first pass. |
| NPC schedules | Current Atlas scope uses placed NPCs, not schedules. |
| Final tileset art | Placeholder tilesets are acceptable. |
| Final music | Placeholder BGM/BGS names and directions exist. |
| Final SFX assets | Cue IDs and directions exist for major story beats. |
| Final balance tuning | First-pass combat can be adjusted after database rows exist. |
| Optional Fogfen reward item identity | Can use an existing early-game reward once item standards are available; it does not block the critical path. |

---

## Minimum To Become Build-Ready

Home Island becomes build-ready from Atlas alone when these four remaining blockers are resolved:

1. `BLK-HOM-002` trial mechanics.
2. `BLK-HOM-003` combat database data.
3. `BLK-HOM-004` tileset assignment matrix.
4. `BLK-HOM-005` animation assignment matrix.

After those are complete, a developer unfamiliar with Atlas should be able to build the Home Island vertical slice without inventing critical production decisions.

---

## Validation

Run:

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Expected result:

- 0 errors,
- 0 warnings.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island vertical slice readiness review |
| 0.2 | Marked event-page blocker cleared by ATLAS-TEC-055 |
