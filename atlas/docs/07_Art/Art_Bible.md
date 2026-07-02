---
atlas_id: ATLAS-ART-001
title: Art Bible
status: Draft
version: 0.1
canonical: true
owner: Art Director
implementation_status: Not Started
dependencies:
  - ATLAS-PRJ-001
  - ATLAS-CRT-001
  - ATLAS-WLD-001
  - ATLAS-MON-001
  - ATLAS-TEC-010
related:
  - ATLAS-GME-001
  - ATLAS-TEC-001
---

# Art Bible

The Art Bible defines the visual language for _The Last Sword Protocol_.

It guides map tiles, battlers, character sprites, portraits, UI, prompts, and future asset production.

---

## Purpose

This document answers:

> What should the game look like, and how should the hidden technology layer appear before the player understands it?

The visual direction must support the project’s emotional promise: wonder, curiosity, warmth, mystery, and hope.

---

## Core Visual Rule

_The Last Sword Protocol_ should look like a hopeful classic JRPG world built over forgotten technology.

Technology should rarely appear as clean science fiction early in the game.

Instead, it should appear as:

- ornament,
- ruin,
- shrine detail,
- strange metal,
- cracked glass,
- glowing runes,
- patterned stone,
- old machinery treated as furniture,
- sacred junk,
- misunderstood infrastructure.

---

## Visual Pillars

| Pillar | Meaning |
|---|---|
| Warmth | Towns should feel lived in, safe, and worth saving |
| Wonder | Ruins and relics should invite curiosity |
| Mystery | Old technology should be visible but not immediately legible |
| Hope | Even damaged places should contain life, color, and human care |
| Progression | The world should become more technological as the truth emerges |
| Readability | RPG Maker MZ maps and battlers must remain clear at game scale |

---

## Technology Visibility Curve

```text
Journey I: Technology appears as strange decoration or sacred ruins
Journey II: Technology appears as repeatable mechanisms
Journey III: Technology appears as old-world systems
Journey IV: Technology appears openly as infrastructure
Journey V: Technology and myth fully converge
```

---

## Regional Visual Language

| Region | Visual Identity | Hidden Tech Expression |
|---|---|---|
| Ashford | Warm village, fields, old factory bones | Pipes as fences, vents as warm stones, metal panels as village walls |
| Fogfen Marsh | Mist, reeds, wet earth | Submerged cables, faint glows, unnatural pools |
| Skyreach Hill | Sacred hill, cave, wind | Security geometry hidden as ancient carvings |
| Coalmouth | Soot, stone, lamps, rails | Industrial control panels mistaken as mine machinery |
| Athenaeum | Books, towers, quiet light | Terminals as reading desks, server racks as archive shelves |
| Irongate | Stone walls, banners, discipline | Defense systems as holy command relics |
| Driftlands | Tents, wagons, dust, trade | Relics sewn into tools and caravan charms |
| New Meridian | Grand civic ruins, canals, towers | Surviving lights, elevators, access doors, old transit lines |
| Dead Circuit | Gray scale, exposed infrastructure, eerie glow | Server farms, cables, antennas, broken machine sanctuaries |
| Vault | Data cathedral | Technology is no longer disguised |

---

## Character Art Principles

Characters should be expressive, readable, and grounded in their region.

### Kai

- Young, curious, sincere.
- Starts ordinary, not overdesigned.
- Visual growth can come from the Sword and later equipment.

### Vera

- Practical, mechanic-influenced design.
- Tools, gloves, belt, patched clothing.
- Should look capable rather than ornamental.

### Eldon

- Scholar silhouette.
- Books, satchel, layered robes or academic travel clothes.
- Should visually evolve from sheltered scholar to field archivist.

### Cipher

- Mobile, clever, guarded.
- Scarf, cloak, relic pouches, asymmetry.
- Should visually suggest hidden tools and escape routes.

---

## Monster Art Principles

Monsters should be family-based and variant-friendly.

Each family needs:

- recognizable silhouette,
- palette swap potential,
- clear threat behavior,
- optional corruption details,
- transparent-background battler compatibility.

Early monsters should be charming. Late monsters should become unsettling, but not visually incoherent.

---

## Old Technology as Myth

Old technology should initially use visual forms that support misinterpretation.

| Technology | Early Visual Interpretation |
|---|---|
| Terminal | Shrine tablet, altar, glowing inscription |
| Server rack | Sacred cabinet, archive wall, reliquary |
| Cable | Root, vine, serpent carving, buried chain |
| Antenna | Tower spire, prayer rod, lightning staff |
| Camera / sensor | Watching eye symbol, guardian jewel |
| Door scanner | Rune plate, hand shrine, judgment seal |
| Warning light | Curse glow, spirit pulse, divine anger |

---

## Color Language

Initial direction:

| Concept | Color Direction |
|---|---|
| Home / safety | Warm earth, soft greens, gold light |
| Mystery | Cyan, blue-white, pale violet accents |
| Corruption | Sickly magenta, red-black, harsh green sparingly |
| NEMESIS | Cold white, red signal, black glass, clinical blue |
| Restoration | Gold, soft cyan, clean white, living green |
| Archive | Blue-white, amber, gentle glow |

Do not overuse harsh red early. Save it for escalation.

---

## RPG Maker MZ Practical Rules

1. Assets must read clearly at RPG Maker scale.
2. Tilesets should avoid excessive micro-detail.
3. Battlers should have transparent backgrounds unless intentionally scene-based.
4. Reusable variants are preferred over one-off assets.
5. Art prompts should specify perspective, scale, background, and use case.
6. Avoid assets that require complex custom animation unless planned.

---

## Image Generation Prompt Standard

Prompts should include:

1. asset type,
2. RPG Maker MZ use case,
3. style target,
4. subject description,
5. color palette,
6. hidden technology cues,
7. transparency requirement,
8. exclusions.

Example prompt structure:

```text
Create a front-view RPG Maker MZ battler of [monster], [style], transparent background, readable silhouette, [palette], [region cues], subtle [hidden technology/corruption detail], no text, no UI, no background.
```

---

## Future Expansion

This document will later split into:

- Pixel Style Guide
- Tileset Guide
- Character Sprite Guide
- Portrait Guide
- Battler Guide
- UI Guide
- Color Language
- Image Generation Prompt Library
- Region Art Packets

---

## Open Questions

- Should the final visual style lean closer to NES-inspired simplicity, SNES detail, or modern pixel-painter RPG style?
- Should portraits be used for all major dialogue or only key scenes?
- Should NEMESIS visuals include explicit UI/glitch effects or remain mostly environmental?
- How much should existing RPG Maker RTP art influence the final style?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Art Bible foundation |
