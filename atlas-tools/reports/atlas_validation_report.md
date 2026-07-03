# Atlas Validation Report

## Summary

- Files scanned: 144
- Canonical pages: 134
- Object pages: 65
- Screen pages: 14
- Unique atlas IDs: 134
- Unique object IDs: 65
- Errors: 16
- Warnings: 0

## Errors

- atlas/docs/00_Foundation/Atlas_ID_Specification.md: canonical page missing `title`
- atlas/docs/00_Foundation/Atlas_Operating_System.md: canonical page missing `title`
- atlas/docs/00_Foundation/Atlas_Roadmap.md: canonical page missing `title`
- atlas/docs/00_Foundation/Metadata_Schema.md: canonical page missing `title`
- atlas/docs/00_Foundation/index.md: canonical page missing `title`
- atlas/docs/index.md: canonical page missing `title`
- duplicate atlas_id `ATLAS-AI-000` in atlas/docs/09_AI/index.md, atlas/docs/10_AI/index.md
- duplicate atlas_id `ATLAS-AI-011` in atlas/docs/10_AI/Codex_Handoff/Home_Island_Implementation_Task_List.md, atlas/docs/10_AI/Codex_Handoff/Home_Island_Task_Breakdown.md
- duplicate atlas_id `ATLAS-ART-000` in atlas/docs/06_Art/index.md, atlas/docs/07_Art/index.md
- duplicate atlas_id `ATLAS-AUD-000` in atlas/docs/07_Audio/index.md, atlas/docs/08_Audio/index.md
- duplicate atlas_id `ATLAS-CHR-000` in atlas/docs/04_Characters/index.md, atlas/docs/05_Characters/index.md
- duplicate atlas_id `ATLAS-GME-000` in atlas/docs/03_Gameplay/index.md, atlas/docs/04_Gameplay/index.md
- duplicate atlas_id `ATLAS-MON-000` in atlas/docs/05_Monsters/index.md, atlas/docs/06_Monsters/index.md
- duplicate atlas_id `ATLAS-STY-000` in atlas/docs/02_Story/index.md, atlas/docs/03_Story/index.md
- duplicate atlas_id `ATLAS-TEC-000` in atlas/docs/08_Technical/index.md, atlas/docs/09_Technical/index.md
- duplicate atlas_id `ATLAS-WLD-000` in atlas/docs/01_World/index.md, atlas/docs/02_World/index.md

## Warnings

None.

## Scope

- Scans Markdown files under `atlas/docs`.
- Parses YAML frontmatter scalar fields only.
- Checks duplicate `atlas_id` and `object_id` values.
- Checks required v0.1 metadata for canonical, object, and screen pages.
