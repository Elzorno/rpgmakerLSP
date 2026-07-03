# WO-0002 — Atlas Validation Cleanup (Structural Only)

## Context

The Atlas validator has completed its first successful run.

The purpose of this work order is **NOT** to modify game design, story, dialogue, quests, NPCs, or worldbuilding.

The goal is only to correct structural Atlas documentation issues so the repository passes validation.

Repository root is already open in VS Code.

---

# Read First

Read these documents before making changes:

atlas/docs/09_Technical/Validation/Atlas_Build_System_Overview.md

atlas/docs/09_Technical/Validation/Atlas_Validation_Rules.md

---

# Validator Output

Current validator errors:

• Missing `title` field:

atlas/docs/index.md

atlas/docs/00_Foundation/index.md

atlas/docs/00_Foundation/Atlas_ID_Specification.md

atlas/docs/00_Foundation/Atlas_Operating_System.md

atlas/docs/00_Foundation/Atlas_Roadmap.md

atlas/docs/00_Foundation/Metadata_Schema.md

• Duplicate Atlas IDs

ATLAS-AI-000

ATLAS-AI-011

ATLAS-ART-000

ATLAS-AUD-000

ATLAS-CHR-000

ATLAS-GME-000

ATLAS-MON-000

ATLAS-STY-000

ATLAS-TEC-000

ATLAS-WLD-000

---

# Required Tasks

## Task 1

Add missing `title:` metadata to every canonical page listed above.

Do not modify page content.

Only update YAML frontmatter.

---

## Task 2

Investigate every duplicate Atlas ID.

Determine whether duplicates exist because:

• legacy folders remain after migration

OR

• IDs were accidentally reused.

---

## Task 3

If duplicate files are legacy copies:

Do NOT delete them.

Instead:

```yaml
canonical: false
```

or rename the Atlas ID using a LEGACY prefix.

The objective is preserving history while removing duplicate canonical IDs.

---

## Task 4

The following files currently share an Atlas ID:

Home_Island_Task_Breakdown.md

Home_Island_Implementation_Task_List.md

Assign a new unique Atlas ID to the newer Implementation Task List.

Update any references if necessary.

---

## Constraints

DO NOT

- rewrite dialogue

- change lore

- rename quests

- modify screen design

- alter implementation packets

- change gameplay

- reorganize folders

Only perform validation cleanup.

---

# Validation

Run

/usr/bin/python3 atlas-tools/cli/atlas.py validate

Continue making structural fixes until validation errors reach zero or no additional structural fixes remain.

---

# Deliverable

Produce an Implementation Report.

Format:

## Completed

## Files Modified

## Atlas IDs Changed

## Remaining Validation Errors

## Notes

Do not commit.