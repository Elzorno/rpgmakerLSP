---
atlas_id: WO-0017
title: Split Atlas Specification From RPG Maker Implementation Repository
status: Active
version: 0.1
canonical: true
owner: Technical Director
implementation_status: Active
dependencies:
  - ATLAS-TEC-061
related:
  - ATLAS-FND-002
  - ATLAS-TEC-058
---

# WO-0017 - Split Atlas Specification From RPG Maker Implementation Repository

## Goal

Create a separate Atlas repository so the Atlas specification can remain the canonical source of truth while the RPG Maker MZ project stays focused on implementation.

The game should consume Atlas. Atlas should not depend on the game repository.

## Planning Rationale

Home Island has passed the production readiness gate in `ATLAS-TEC-061`. This is the right point to split specification ownership from implementation ownership before RPG Maker MZ production begins.

Keeping Atlas and the game in separate repositories gives the project cleaner versioning, clearer implementation contracts, and an easier path to future engine targets.

## Read First

- `atlas/docs/09_Technical/Playtest/Home_Island_Production_Readiness_Gate.md`
- `atlas/docs/09_Technical/Build_Pipeline/RPGMaker_MZ_Vertical_Slice_Build_Pipeline.md`
- `atlas/docs/00_Foundation/Atlas_Roadmap.md`
- `.agents/protocol.md`

## Required Tasks

1. Create a sibling repository named `TheLastSwordProtocol-Atlas`.
2. Copy Atlas-owned source material into the new repository:
   - `atlas/`
   - `atlas-tools/`
   - project documentation that is not RPG Maker runtime data
3. Exclude RPG Maker MZ implementation files from the Atlas repository:
   - `data/`
   - `img/`
   - `audio/`
   - `js/`
   - `effects/`
   - `fonts/`
   - `movies/`
   - `save/`
   - `game.rmmzproject`
4. Add lightweight repository documentation explaining that Atlas is canonical and the game repo is a downstream implementation target.
5. Validate Atlas in the new repository.
6. Initialize Git in the new repository and make an initial commit if validation passes.
7. Leave the current RPG Maker repository intact; do not delete Atlas from it in this work order.
8. Update agent tracking files with the split result.

## Constraints

- Do not modify RPG Maker project files.
- Do not delete Atlas from the current repository in this work order.
- Do not rewrite canon, story, gameplay, dialogue, maps, or assets.
- Do not copy generated RPG Maker runtime folders into the Atlas repository.
- Preserve Atlas IDs and validation behavior.

## Validation

Run in the current repository:

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Run in the new Atlas repository:

```bash
/usr/bin/python3 atlas-tools/cli/atlas.py validate
```

Expected result:

- 0 errors,
- 0 warnings.

## Deliverable / Implementation Report

Return:

- Work order path
- New repository path
- Files copied
- Files intentionally excluded
- Commands run
- Validation result in both repositories
- Git commit hash in the new Atlas repository
- Any remaining risks or next steps
