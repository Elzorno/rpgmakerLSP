# Ashford Exterior Reconciled Rebuild Candidate

Date: 2026-07-14  
Canon: `SCR-HOM-ASH-001` v0.2 / `IMP-HOM-017` v0.2  
Status: Review candidate; not installed in the production Game project

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

## Remaining Gate

Chris should judge the render before installation. If accepted visually, the
candidate can replace protected Map001 under the explicit rebuild authorization,
followed by full-project route auditing and live RPG Maker MZ playtesting. Until
then, production remains unchanged.
