"""RPG Maker MZ floor-autotile shape compositor.

Implements the same tile addressing scheme as the engine's own
``Tilemap.getAutotileKind`` / ``Tilemap.getAutotileShape`` / ``Tilemap.makeAutotileId``
(see ``rpgmakerLSP/js/rmmz_core.js``), plus a neighbor -> shape lookup for the 11
shapes a simple filled region actually needs: solid interior, four straight
edges, four convex corners, and two opposite-edge bands. This is a deliberate
subset of the engine's full 48-shape ``FLOOR_AUTOTILE_TABLE`` (which also
covers concave/notched corners a simply-connected filled region never
produces) - each of the 11 shapes below was cross-checked against real,
already-accepted autotile placements in ``TheLastSwordProtocol-Game/data/Map001.json``
(Ashford Exterior, hand-authored) before being trusted, not derived from the
shape table alone.

Concave corners (an L-shaped or notched region boundary) are intentionally
unsupported: callers should build regions as simple filled shapes (rects,
unions of rects, or blob/noise masks without single-cell notches) so every
boundary cell only ever needs one of the 11 shapes here. A boundary cell
whose neighbor pattern doesn't match any of the 11 falls back to the solid
interior shape (SHAPE_FULL) rather than raising, so a stray concave notch
degrades to a visible seam rather than a crash - callers should treat that as
a sign to smooth the offending mask, not as expected behavior.
"""

from __future__ import annotations

TILE_ID_A1 = 2048
TILE_ID_A2 = 2816
TILE_ID_A5 = 1536

SHAPES_PER_KIND = 48

# Empirically-confirmed shape indices (validated against Map001.json's real,
# accepted autotile placements - see the derivation in this module's tests).
SHAPE_FULL = 0
SHAPE_N_OPEN = 20
SHAPE_S_OPEN = 28
SHAPE_W_OPEN = 16
SHAPE_E_OPEN = 24
SHAPE_NS_OPEN = 33
SHAPE_EW_OPEN = 42
SHAPE_CORNER_TL = 34  # N and W both open (top-left convex corner)
SHAPE_CORNER_TR = 36  # N and E both open (top-right convex corner)
SHAPE_CORNER_BL = 40  # S and W both open (bottom-left convex corner)
SHAPE_CORNER_BR = 38  # S and E both open (bottom-right convex corner)
SHAPE_ISOLATED = 47  # all 8 neighbors open (single-tile island)


def autotile_kind(tile_id: int) -> int:
    return (tile_id - TILE_ID_A1) // SHAPES_PER_KIND


def make_autotile_id(kind: int, shape: int) -> int:
    return TILE_ID_A1 + kind * SHAPES_PER_KIND + shape


def shape_for_neighbors(n: bool, s: bool, e: bool, w: bool) -> int:
    """Return the autotile shape for a cell given which of its 4 orthogonal
    neighbors belong to the same region. Diagonal neighbors are not needed:
    every shape this function returns was confirmed (see module docstring)
    to hold regardless of diagonal state for a simply-connected region."""
    if n and s and e and w:
        return SHAPE_FULL
    if not n and s and e and w:
        return SHAPE_N_OPEN
    if n and not s and e and w:
        return SHAPE_S_OPEN
    if n and s and not e and w:
        return SHAPE_E_OPEN
    if n and s and e and not w:
        return SHAPE_W_OPEN
    if not n and not s and e and w:
        return SHAPE_NS_OPEN
    if n and s and not e and not w:
        return SHAPE_EW_OPEN
    if not n and s and not w and e:
        return SHAPE_CORNER_TL
    if not n and s and not e and w:
        return SHAPE_CORNER_TR
    if n and not s and not w and e:
        return SHAPE_CORNER_BL
    if n and not s and not e and w:
        return SHAPE_CORNER_BR
    # Isolated (0 neighbors) or an unsupported concave/notched configuration:
    # fall back to solid fill rather than guessing. See module docstring.
    return SHAPE_ISOLATED if not any((n, s, e, w)) else SHAPE_FULL


def paint_region(
    set_tile,
    cells: set[tuple[int, int]],
    kind: int,
    layer: int,
    *,
    treat_off_map_as_same: bool = False,
) -> None:
    """Paint every cell in ``cells`` with the correctly-shaped autotile id of
    ``kind`` on ``layer``, using ``set_tile(x, y, layer, value)`` to write.

    ``treat_off_map_as_same``: when True, a neighbor that isn't in ``cells``
    but is also off any bound the caller enforces (map edge) is treated as
    same-region, so the region reads as continuing past the map border
    instead of showing a hard edge there. Callers pass this as True only for
    regions deliberately meant to touch the map's outer edge (e.g. a coastal
    water ring); ``cells`` itself is the only thing this function checks, so
    "off-map" here just means "not in cells" - map-edge clamping is the
    caller's responsibility via what it puts in ``cells``.
    """
    for x, y in cells:

        def same(nx: int, ny: int) -> bool:
            if (nx, ny) in cells:
                return True
            return treat_off_map_as_same

        n = same(x, y - 1)
        s = same(x, y + 1)
        e = same(x + 1, y)
        w = same(x - 1, y)
        shape = shape_for_neighbors(n, s, e, w)
        set_tile(x, y, layer, make_autotile_id(kind, shape))
