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
  - ATLAS-TEC-056
  - ATLAS-TEC-057
  - ATLAS-TEC-059
  - ATLAS-TEC-060
---

# Home Island Vertical Slice Readiness Review

## Objective

Answer one production question:

Can a developer build Home Island today using Atlas alone?

## Verdict

Yes, for first playable implementation.

Atlas now contains enough RPG Maker MZ production detail for an unfamiliar developer to build the Home Island vertical slice without inventing critical implementation decisions.

Final art, final animation, final audio, final dialogue polish, and balance tuning remain production polish, not readiness blockers.

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
| Encounter tables | Yes | No | `ATLAS-TEC-056` defines RPG Maker-ready enemies, skills, states, troops, and first-pass encounter placement. |
| Trial mechanics | Yes | No | `ATLAS-TEC-057` defines eventable Body, Mind, and Heart trial mechanics. |
| Tileset references | Yes | No | `ATLAS-TEC-059` assigns every Home Island screen to an approved first-playable placeholder tileset with passability and region guidance. |
| Animation IDs | Yes | No | `ATLAS-TEC-060` assigns every required Home Island combat, story, trial, feedback, and recovery beat to an approved placeholder animation or no-animation fallback. |
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

Yes, for the current Home Island vertical slice.

Resolution:

`ATLAS-TEC-057` defines first-playable RPG Maker MZ event mechanics for the Body, Mind, and Heart trials, including variables, event pages, success conditions, and harmless reset behavior.

Former missing production data:

| Trial | Missing Detail |
|---|---|
| Body Trial | Whether this is combat, movement, or interaction; success condition; failure/reset behavior; enemy/troop if combat |
| Mind Trial | Exact pattern/observation rule; interactable objects; success condition; reset behavior |
| Heart Trial | Exact choice or memory interaction; whether any choice can fail; success condition |

Required output:

- Complete. See `ATLAS-TEC-057`.

Do not write new lore dialogue except minimal placeholder text required for event operation.

---

### BLK-HOM-003 — Complete RPG Maker Combat Database Data

Blocking question:

Can a developer create the Home Island enemy, skill, state, and troop database entries without guessing?

Current answer:

Yes, for the current Home Island vertical slice.

Resolution:

`ATLAS-TEC-056` defines first-playable RPG Maker MZ rows for Home Island enemies, actor/class values, skills, states, troops, starting equipment, item rows, and encounter placement. Final balance tuning remains non-blocking.

Former missing production data:

| Area | Missing Detail |
|---|---|
| Enemy stats | HP, MP, attack, defense, agility, luck, EXP, gold, hit/evasion assumptions |
| Skill effects | Exact RPG Maker formulas or effects for `Murk Bubble`, `Pulse Guard`, `Warning Tone`, and `Relay Burst` |
| States | Whether poison/debuff exists in Journey I; state ID/name/effects if used |
| Troops | Stable troop IDs, event pages if any, battleback guidance |
| Guardian | Final Journey I boss object behavior is still partly placeholder; final ID/name question remains open in `IMP-HOM-004` |

Required output:

- Complete. See `ATLAS-TEC-056`.

Keep balance first-pass and adjustable, but remove ambiguity.

---

### BLK-HOM-004 — Assign Tileset Or Placeholder Tileset References

Blocking question:

Can a developer create maps without choosing tilesets outside Atlas?

Current answer:

Yes, for the current Home Island vertical slice.

Resolution:

`ATLAS-TEC-059` maps every Home Island screen to an approved RPG Maker MZ placeholder tileset and documents terrain, passability, region IDs, encounter zones, transfer placement, missing final assets, and first-playable placeholder rules.

Former missing production data:

| Map Group | Missing Detail |
|---|---|
| Ashford exterior/interiors | Concrete RPG Maker tileset or placeholder tileset assignment |
| Skyreach / Hidden Cave | Concrete field/cave tileset assignment |
| Glassfield / Sealed Node | Concrete ruin/node tileset assignment |
| Rustshore | Concrete town/coastal tileset assignment |
| Fogfen | Concrete marsh tileset assignment |

Required output:

- Complete. See `ATLAS-TEC-059`.

This can use existing RTP or prototype tilesets; it does not require final art.

---

### BLK-HOM-005 — Assign Animation IDs For Required Combat And Story Beats

Blocking question:

Can a developer wire battles and key story events without choosing animations outside Atlas?

Current answer:

Yes, for the current Home Island vertical slice.

Resolution:

`ATLAS-TEC-060` maps every required Home Island combat, story, trial, feedback, item/recovery, encounter, victory, and reward beat to an RPG Maker MZ animation database ID or approved no-animation fallback.

Former missing production data:

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

- Complete. See `ATLAS-TEC-060`.

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
| Final combat balance tuning | `ATLAS-TEC-056` supplies first-playable values; numeric tuning can proceed after implementation. |
| Final animation/VFX assets | `ATLAS-TEC-060` supplies first-playable placeholder animation IDs; custom VFX can replace them later. |

---

## Minimum To Become Build-Ready

Home Island is build-ready from Atlas alone for first playable testing.

A developer unfamiliar with Atlas should be able to build the Home Island vertical slice without inventing critical production decisions.

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
| 0.3 | Marked combat database blocker cleared by ATLAS-TEC-056 |
| 0.4 | Marked trial mechanics blocker cleared by ATLAS-TEC-057 |
| 0.5 | Marked tileset assignment blocker cleared by ATLAS-TEC-059 |
| 0.6 | Marked animation assignment blocker cleared by ATLAS-TEC-060 |
