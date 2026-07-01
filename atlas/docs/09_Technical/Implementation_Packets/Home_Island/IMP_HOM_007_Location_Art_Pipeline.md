---
object_id: IMP-HOM-007
atlas_id: IMP-HOM-007
title: Build Home Island Location Art Pipeline
object_type: ImplementationPacket
status: Draft
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Not Started
relationships:
  implements:
    - ATLAS-ART-011
  requires:
    - ATLAS-ART-001
    - REG-HOM-001
---

# Implementation Packet: Build Home Island Location Art Pipeline

## Objective

Create a practical workflow for turning Home Island visual prompts into usable RPG Maker MZ mapping references and eventual assets.

---

## Atlas References

| ID | Reference |
|---|---|
| ATLAS-ART-011 | Home Island Location Art Prompt Packet |
| ATLAS-ART-001 | Art Bible |
| REG-HOM-001 | Home Island |

---

## Scope

Included:

- Generate or collect first-pass visual references for Home Island locations.
- Store outputs in a predictable source-art folder.
- Identify which references become tileset work, map references, or parallax references.
- Keep implementation unblocked by allowing placeholders.

Out of scope:

- Final tileset production.
- Final image cleanup.
- Full parallax mapping workflow.

---

## Suggested Source Paths

```text
art/source/Home_Island/Ashford/
art/source/Home_Island/Rustshore_Docks/
art/source/Home_Island/Fogfen_Marsh/
art/source/Home_Island/Glassfield_Ruins/
art/source/Home_Island/Skyreach_Hill/
art/source/Home_Island/Hidden_Cave/
art/source/Home_Island/Sealed_Node/
```

---

## Required References

| Location | Minimum Reference Need |
|---|---|
| Ashford | town exterior concept |
| Rustshore Docks | dock / lighthouse concept |
| Fogfen Marsh | marsh tile mood concept |
| Glassfield Ruins | ruin field concept |
| Skyreach Hill | hill and cave entrance concept |
| Hidden Cave | cave sanctum concept |
| Sealed Node | cave-machine dungeon concept |

---

## Acceptance Criteria

- Each Home Island location has at least one visual reference target.
- References are organized by location.
- Codex can proceed with placeholder maps even if final art is not ready.
- Asset names avoid spaces when exported into implementation folders.

---

## Playtest / Review Steps

1. Confirm every Home Island location has a reference folder.
2. Confirm generated concepts match Atlas tone.
3. Confirm no reference visually contradicts hidden technology rules.
4. Confirm map work can begin with placeholders.

---

## Open Questions

- Should concept images live in the repo, or should the repo store prompts and final optimized assets only?
- Should each location get a final tileset or share a Home Island tileset?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Home Island location art pipeline packet |
