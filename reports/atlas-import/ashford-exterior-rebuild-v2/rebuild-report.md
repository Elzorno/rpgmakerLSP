# Ashford Exterior Reconciled Rebuild Candidate

Date: 2026-07-14  
Canon: `SCR-HOM-ASH-001` v0.2 / `IMP-HOM-017` v0.2  
Status: Rejected by Chris on 2026-07-14; not installed in the production Game project

## Human Decision

Rejected. Chris found that the trees show only the bottom half of a two-tile
set, the buildings are too tall and do not match the references' building
style, and the overall style and feel remain wrong. Chris also found genuine
progress: the layout is better, less mechanical, and more organic.

This distinction is binding feedback for the replacement pipeline: structural
and compositional improvement does not constitute visual acceptance. This
candidate remains a negative-control fixture and must never be promoted.

## What Changed Visually

- Replaced the oversized rectangular paved area with a central worn well square
  and branching dirt-road hierarchy.
- Made the north/northwest Inn the largest public façade and retained distinct
  Shop and Elara House doors.
- Added two non-enterable cottage shells to make Ashford read as a village.
- Added west/southwest farm, garden, orchard, and cottage dressing.
- Added partial two-tile forest framing while preserving all canonical exits.
- Added a narrow segmented eastern old-facility drainage channel with clear
  crossings at the Glassfield and Fogfen routes.
- Added restrained Shop supply/repair-shed dressing and northern factory-frame
  fragments without creating a blacksmith role or event.

## Canon and Runtime Preservation

- Source events: 27; candidate events: 27.
- Every event page and command payload is unchanged from production Map001.
- Only event coordinates were adjusted to match the rebuilt geometry.
- Required Elara House, Shop, Inn, Skyreach, Rustshore, Glassfield, and Fogfen
  transfer identities and destinations remain intact.
- The warm-stone vent, old panel, NPCs, hidden item, tremor trigger, and four
  searchable objects remain present.
- Map remains 40x32, `Outside` tileset ID 2, Town1 BGM, and zero encounters.

## Automated Review

- Conservative authored-collision BFS: PASS.
- Reachable cells from south entry: 849.
- Event/interaction failures: 0.
- Event command payload preservation: PASS.
- Candidate JSON shape/render: PASS.
- Production `Map001.json`: not modified.

## Review Files

- `ashford-exterior-reconciled-render.png`
- `Map001.reconciled-candidate.json`
- `route-audit.json`

## Disposition

Do not install. Preserve the candidate as evidence for WO-0066, WO-0069,
WO-0072, and WO-0074. Production remains unchanged.
