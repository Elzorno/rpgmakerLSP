# WO-0001 — Home Island Validation Cleanup

## Goal

Run the Atlas validator and clean up the first round of validation errors without changing story canon.

## Steps

1. Run `python atlas-tools/cli/atlas.py validate`.
2. Review `atlas-tools/reports/atlas_validation_report.md`.
3. Fix only structural issues:
   - missing `atlas_id`
   - duplicate IDs
   - missing screen metadata
   - malformed frontmatter
4. Do not rewrite story, dialogue, or worldbuilding.
5. Re-run validation.

## Done When

- Validator runs successfully.
- Report exists.
- Remaining errors, if any, are documented.