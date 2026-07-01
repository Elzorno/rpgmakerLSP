---
object_id: IMP-HOM-001
atlas_id: IMP-HOM-001
title: Build Ashford
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - LOC-ASH-001
  requires:
    - REG-HOM-001
    - CHR-KAI-001
    - NPC-ELA-001
    - QST-HOM-001
---

# Implementation Packet: Build Ashford

## Objective

Create the first playable version of Ashford in RPG Maker MZ as the starting village for Journey I.

This packet should produce a functional, testable town map with Kai's starting location, Elara's house, basic NPCs, a hidden item, and story-state-ready events.

---

## Atlas References

| ID | Reference |
|---|---|
| REG-HOM-001 | Home Island |
| LOC-ASH-001 | Ashford |
| CHR-KAI-001 | Kai |
| NPC-ELA-001 | Grandmother Elara |
| QST-HOM-001 | Home Island Opening |
| ATLAS-TEC-020 | RPG Maker MZ Bible |

---

## Scope

Included:

- Ashford exterior map.
- Kai / Elara house interior.
- Basic shop or storage hut placeholder.
- 6–8 NPC placeholder events.
- Elara event with story-state dialogue scaffold.
- Hidden item south of old warm-stone vent.
- Transfer events between town and interiors.
- Starting player position.

Out of scope:

- Final tileset polish.
- Final NPC portraits.
- Full dialogue writing.
- Combat balance.
- Mainland departure.

---

## Required Maps

Draft map names:

```text
TWN_Ashford_Exterior
INT_Ashford_ElaraHouse
INT_Ashford_Shop
INT_Ashford_ElderHouse
```

---

## Required Switches

```text
J1_Ashford_IntroComplete
J1_Tremor_Event
J1_Sword_Obtained
J1_Node07_Offline
NPC_Ashford_PostNode07
```

---

## Required Variables

None required for the first Ashford pass.

Optional later:

```text
Current_Journey
Archive_Recovery_Percent
```

---

## Required Events

### Player Start

Place Kai inside Elara's house or just outside it.

Recommended first pass: inside Elara's house.

### Elara Event

Create pages for:

1. Intro state.
2. After village intro.
3. After tremor.
4. After Sword obtained.
5. After Node Seven offline.

Use placeholder dialogue if final writing is not available.

### Hidden Item Event

Location: four steps south of old warm-stone vent behind Elara's house.

Reward: minor healing item or old coin placeholder.

### Village NPC Events

Create placeholder NPCs for:

- elder,
- shopkeeper,
- child near old metal panel,
- farmer using warm vent stones,
- villager joking about Skyreach Hill,
- traveler or dock messenger.

---

## Visual Requirements

Ashford should look warm and lived in.

Include:

- gardens,
- wooden homes,
- warm-stone vents,
- old metal panels reused as fences/walls,
- flowers or grass around ruins,
- visible path out of town.

---

## Audio Requirements

Use a warm town BGM placeholder.

Final Ashford theme will be defined later in Audio Atlas.

---

## Acceptance Criteria

- Player can start in Ashford.
- Player can enter and exit Elara's house.
- Player can talk to Elara.
- Player can talk to at least six villagers.
- Hidden item can be found once.
- Ashford has clear exits reserved for Home Island overworld or local routes.
- Switch-ready dialogue structure exists even if final dialogue is placeholder.

---

## Playtest Steps

1. Start new game.
2. Confirm player begins in correct place.
3. Talk to Elara.
4. Explore town.
5. Enter and exit each interior.
6. Find hidden item.
7. Verify NPCs do not block critical paths.
8. Toggle story switches manually and confirm Elara's event pages can support later states.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ashford implementation packet |
