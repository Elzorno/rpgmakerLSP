---
object_id: REG-HOM-001
atlas_id: REG-HOM-001
title: Home Island
object_type: Region
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
journey:
  - JRN-001
relationships:
  contains:
    - LOC-ASH-001
    - LOC-RST-001
    - LOC-FOG-001
    - LOC-GLS-001
    - LOC-SKY-001
    - LOC-HCV-001
    - LOC-SND-001
  related_to:
    - REL-007
    - CHR-KAI-001
    - NPC-ELA-001
---

# Home Island

Home Island is the starting region of _The Last Sword Protocol_ and the full playable space for Journey I.

It should feel small, warm, mysterious, and self-contained. The island must teach the player the emotional and mechanical language of the game before the world opens.

---

## Purpose

Home Island introduces:

- Kai,
- Ashford,
- Grandmother Elara,
- old technology misunderstood as folklore,
- first exploration rewards,
- first ruins,
- the Sword / Project Excalibur,
- Relay Node Seven,
- the idea that home was built over something much older.

---

## Player-Facing Summary

A quiet island of fields, marshes, docks, old stones, and a forbidden northern hill.

Most people believe the island is ordinary, except for old stories about Skyreach Hill and the sealed curse beneath Glassfield.

---

## Hidden Reality

Home Island is a secure old-world enclave designed to hide or protect Project Excalibur and Relay Node Seven.

The island's isolation is not accidental. It served as physical segmentation and containment.

---

## Major Locations

| ID | Location | Role |
|---|---|---|
| LOC-ASH-001 | Ashford | Starting village and emotional home |
| LOC-RST-001 | Rustshore Docks | Exit point and first hint of wider world |
| LOC-FOG-001 | Fogfen Marsh | Early danger and signal-disturbed nature |
| LOC-GLS-001 | Glassfield Ruins | Visible old-world mystery and path to Node Seven |
| LOC-SKY-001 | Skyreach Hill | Forbidden northern landmark |
| LOC-HCV-001 | Hidden Cave / Excalibur Vaultlet | Sword awakening trial site |
| LOC-SND-001 | Sealed Node | Journey I climax dungeon and Relay Node Seven site |

---

## Travel Routes

Initial route should guide the player naturally:

```text
Ashford → local fields → Fogfen Marsh / Glassfield Ruins → Skyreach Hill → Hidden Cave → Sealed Node → Rustshore Docks
```

Rustshore Docks should not allow full departure until Node Seven is resolved.

---

## Encounter Philosophy

Early encounters should be charming, readable, and low complexity.

Recommended families:

- Gel family,
- Rat family,
- Crow family,
- local wolf/predator,
- early construct near ruins.

---

## Story Role

Home Island answers Journey I's central question:

> Who am I?

By the end, Kai learns that the Sword recognizes him and that the island's old stories were warnings about real systems.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| contains | LOC-ASH-001 | Starting village |
| contains | LOC-SKY-001 | Forbidden hill |
| contains | REL-007 | Relay Node Seven hidden beneath island systems |
| appears_in | CHR-KAI-001 | Kai begins here |
| appears_in | NPC-ELA-001 | Elara lives in Ashford |

---

## Implementation Notes

Home Island should be implementable as a compact overworld island with transfer points to local maps.

Keep scope manageable. The island should feel complete but not oversized.

---

## Open Questions

- Should Ashford be central/southwest or central on the island overworld?
- Should Rustshore Docks be visible from the start but unusable until after Node Seven?
- Should Fogfen Marsh be optional before the Sword or required?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island region object |
