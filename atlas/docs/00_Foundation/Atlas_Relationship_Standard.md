---
atlas_id: ATLAS-FND-007
title: Atlas Relationship Standard
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-FND-006
  - ATLAS-FND-008
related:
  - ATLAS-FND-009
---

# Atlas Relationship Standard

The Atlas Relationship Standard defines how Atlas objects reference one another.

This turns Atlas from a folder of Markdown files into a lightweight knowledge graph.

---

## Purpose

This document answers:

> How do Atlas objects connect to each other in a consistent, machine-readable way?

---

## Prime Rule

Relationships should be explicit.

Do not rely only on prose when a stable relationship can be declared in metadata or a relationship table.

---

## Relationship Format

Preferred object relationship format:

```yaml
relationships:
  contains:
    - LOC-ASH-001
  located_in:
    - REG-HOM-001
  related_to:
    - REL-007
```

For prose sections, include relationship tables:

| Relationship | Target ID | Meaning |
|---|---|---|
| located_in | REG-HOM-001 | This object belongs to Home Island |
| contains | NPC-ELA-001 | This location contains Grandmother Elara |

---

## Core Relationship Types

| Relationship | Meaning | Example |
|---|---|---|
| contains | Parent object includes child object | REG-HOM-001 contains LOC-ASH-001 |
| located_in | Object physically belongs to region/location | LOC-ASH-001 located_in REG-HOM-001 |
| appears_in | Character, monster, or item appears in location/quest | CHR-KAI-001 appears_in LOC-ASH-001 |
| starts_quest | NPC/location starts a quest | NPC-ELA-001 starts_quest QST-HOM-001 |
| advances_quest | Object advances quest state | LOC-SKY-001 advances_quest QST-HOM-001 |
| completes_quest | Object or event completes a quest | REL-007 completes_quest QST-HOM-003 |
| requires | Object requires another object/state | LOC-HCV-001 requires ITM-SWD-001 |
| unlocks | Object unlocks another object/system | REL-007 unlocks SYS-ARCHIVE-001 |
| rewards | Quest or encounter rewards item/gold/ability | QST-HOM-001 rewards ITM-KEY-001 |
| drops_item | Monster may drop item | MON-GEL-001 drops_item ITM-CNS-001 |
| guards | Monster or boss guards location/item/relay | MON-BOS-007 guards REL-007 |
| belongs_to_family | Monster belongs to family | MON-GEL-001 belongs_to_family FAM-GEL-001 |
| teaches | Object teaches system/concept | LOC-GLS-001 teaches SYS-ACCESS-001 |
| foreshadows | Object hints at later reveal | LOC-GLS-001 foreshadows TEC-AUTH-001 |
| implements | Implementation packet implements object | IMP-HOM-001 implements LOC-ASH-001 |
| uses_asset | Object requires asset | MON-GEL-001 uses_asset AST-BTR-GEL-001 |
| references | Document/object references another | ATLAS-STY-001 references ATLAS-WLD-001 |

---

## Relationship Direction

Relationships should be directional when direction matters.

Example:

```text
REG-HOM-001 contains LOC-ASH-001
LOC-ASH-001 located_in REG-HOM-001
```

Both may be declared if useful.

---

## Canonical Relationship Sections

Every object page should include a relationship section:

```markdown
## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | REG-HOM-001 | Home Island |
| contains | NPC-ELA-001 | Grandmother Elara lives here |
```

---

## Metadata Relationship Block

When practical, include relationships in front matter:

```yaml
relationships:
  located_in:
    - REG-HOM-001
  contains:
    - NPC-ELA-001
    - QST-HOM-001
  related_to:
    - REL-007
```

If YAML becomes too large, keep relationships in the page body table instead.

---

## Relationship Naming Rules

- Use lowercase snake_case.
- Prefer verbs or verb phrases.
- Do not invent new relationship types unless existing types fail.
- Add new relationship types to this standard before widespread use.

---

## Validation Questions

When adding a relationship, ask:

1. Is this connection useful to a future human or AI contributor?
2. Is the direction clear?
3. Is the target ID stable?
4. Should this be metadata, body table, or both?
5. Does this relationship avoid duplicating canon elsewhere?

---

## Future Expansion

This standard may later support automatic graph rendering, orphan object detection, implementation traceability, and missing asset reports.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Atlas OS relationship standard |
