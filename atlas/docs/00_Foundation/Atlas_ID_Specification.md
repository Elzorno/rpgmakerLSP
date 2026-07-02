---
atlas_id: ATLAS-FND-003
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-FND-001
related:
  - ATLAS-FND-004
---

# Atlas ID Specification

Every significant Atlas page, concept, character, location, monster family, system, and decision should receive a stable Atlas ID.

Atlas IDs make the knowledge base easier for humans and AI agents to reference.

---

## ID Format

```text
ATLAS-SECTION-NUMBER
```

Examples:

```text
ATLAS-FND-001
ATLAS-WLD-004
ATLAS-STY-010
ATLAS-MON-025
ATLAS-DDR-0001
```

---

## Section Codes

| Code | Section |
|---|---|
| FND | Foundation |
| PRJ | Project-level identity |
| WLD | World |
| STY | Story |
| GME | Gameplay |
| CHR | Characters |
| MON | Monsters |
| ART | Art |
| AUD | Audio |
| TEC | Technical / implementation |
| AI | AI workflow |
| REF | Reference |
| DDR | Design Decision Record |

---

## Numbering Rules

- Use three digits for normal documents: `ATLAS-WLD-001`.
- Use four digits for decision records: `ATLAS-DDR-0001`.
- Do not reuse retired IDs.
- If a page is renamed, keep the same Atlas ID.
- If a page is split, keep the old page as an index and assign new IDs to new pages.
- If a concept becomes important enough for repeated reference, give it an ID.

---

## ID Examples

| ID | Meaning |
|---|---|
| ATLAS-FND-001 | Atlas Operating System |
| ATLAS-FND-002 | Atlas Roadmap |
| ATLAS-FND-003 | Atlas ID Specification |
| ATLAS-WLD-001 | World overview |
| ATLAS-WLD-004 | Ashford |
| ATLAS-STY-001 | Story structure overview |
| ATLAS-GME-001 | Gameplay systems overview |
| ATLAS-CHR-001 | Kai |
| ATLAS-MON-001 | Slime family |
| ATLAS-DDR-0001 | Atlas is primary deliverable |

---

## Cross-Reference Standard

When referencing another Atlas page, include both the title and ID when possible:

```markdown
See [Atlas Operating System](../00_Foundation/Atlas_Operating_System.md) (`ATLAS-FND-001`).
```

AI agents should prefer IDs when summarizing or generating implementation tasks.

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Atlas ID system |
