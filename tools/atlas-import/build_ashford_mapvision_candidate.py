#!/usr/bin/env python3
"""WO-0073: build a review-only Ashford Exterior candidate through the new
MapVision/TileAssembly compiler pipeline (WO-0071/0072), instead of hand-
authoring tile placement the way build_ashford_exterior_candidate.py (the
2026-07-14 v2 rebuild, human-rejected) did.

Geometry comes from SemanticAssembler + the real, human-approved
MV-HOM-ASH-001 MapVision and Ashford TileAssembly catalog (contract/examples/
ashford_production in AtlasStudio) -- every building/landmark placement is a
verified, catalog-enabled TileAssembly, not hand-drawn tiles. All 27 current
Map001 events are preserved byte-for-byte (deep-copied pages/lists); only
their x/y coordinates move to match the new geometry, via an explicit,
auditable per-event mapping table (EVENT_RECONCILIATION below), not inferred.

Never writes TheLastSwordProtocol-Game/data/Map001.json. Output is entirely
disposable, under reports/atlas-import/ashford-mapvision-v3/, mirroring the
v2 rebuild's own review-only convention. Installing over production Map001
requires Chris's explicit acceptance per WO-0073's own constraints -- this
script does not attempt it and never will.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import sys
from collections import deque
from pathlib import Path

from autotile import paint_region

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORKSPACE = REPO.parent
GAME = WORKSPACE / "TheLastSwordProtocol-Game"
ATLAS = WORKSPACE / "TheLastSwordProtocol-Atlas"
ATLASSTUDIO = WORKSPACE / "AtlasStudio"
COMPILER_DIR = ATLASSTUDIO / "atlas-tools" / "mapgen" / "compiler"
KIT_DIR = ATLASSTUDIO / "atlas-tools" / "mapgen" / "tile_assembly" / "kits" / "ashford"
SOURCE = GAME / "data" / "Map001.json"
OUTPUT = REPO / "reports" / "atlas-import" / "ashford-mapvision-v3"
RENDERER = COMPILER_DIR / "style_study" / "wo0060" / "render_map.py"
WIDTH, HEIGHT = 40, 32
GRASS_KIND = 16
PATH_KIND = 32

sys.path.insert(0, str(COMPILER_DIR))
from assembler import AssemblyBudget, SemanticAssembler  # noqa: E402
from generation_manifest import GenerationManifest  # noqa: E402
from quality_gate import record_gate_evidence, run_dual_gate  # noqa: E402
from seed_streams import SeedStreams, derive_root_seed  # noqa: E402
from structural_preview import render_ascii  # noqa: E402
from tile_assembly_catalog import (  # noqa: E402
    load_custom_extension_manifest,
    load_tile_assembly_kit_index,
    merge_catalogs,
)

EXAMPLES = COMPILER_DIR / "contract" / "examples" / "ashford_production"
SHARED = COMPILER_DIR / "contract" / "examples" / "shared"


# Every current Map001 event, mapped to how its new position is derived.
# "anchor" -> a MapPlan transfer_point/event_anchor id (zone-center anchor).
# "landmark" -> a MapVision landmark_tag (vent/panel), anchored by its own
#   bound TileAssembly, not a zone center.
# "door" -> a building's own bound TileAssembly door anchor (more precise
#   than the zone-center anchor for an actual entrance event).
# "offset" -> a fixed canon-required offset from another event's final
#   position (used only for the hidden item, CA-ASH-HIDDEN: "exactly four
#   steps south of the warm-stone vent").
EVENT_RECONCILIATION = {
    1: ("anchor", "GEN-service_point_child_old_panel-old_panel_edge"),
    2: ("anchor", "GEN-service_point_farmer_warm_stones-cultivation_edge"),
    3: ("anchor", "GEN-service_point_skyreach_joker-route_north"),
    4: ("anchor", "GEN-service_point_dock_messenger-arrival_domestic"),
    5: ("offset", (14, 0, 4)),  # 4 steps south of event 14 (warm-stone vent)
    6: ("anchor", "GEN-event_anchor_tremor_trigger-route_north"),
    7: ("door", "elara_house"),
    8: ("door", "ashford_shop"),
    9: ("anchor", "GEN-exit_transfer_north-route_north"),
    10: ("anchor", "GEN-exit_transfer_south-arrival_domestic"),
    11: ("anchor", "GEN-exit_transfer_glassfield-route_glassfield"),
    12: ("anchor", "GEN-exit_transfer_fogfen-route_fogfen"),
    13: ("anchor", "GEN-service_point_village_elder-well_square"),
    14: ("landmark", "warm_vent"),
    15: ("landmark", "humming_panel"),
    16: ("anchor", "GEN-event_anchor_elara_house_exterior_dec-arrival_domestic"),
    17: ("anchor", "GEN-event_anchor_shop_exterior_dec-shop_frontage"),
    18: ("anchor", "GEN-event_anchor_warm_stone_vent_dec-cultivation_edge"),
    19: ("anchor", "GEN-event_anchor_reused_metal_fence_dec-cultivation_edge"),
    20: ("anchor", "GEN-event_anchor_village_ground_dec-well_square"),
    21: ("anchor", "GEN-event_anchor_garden_patch_dec-cultivation_edge"),
    22: ("anchor", "GEN-event_anchor_route_edge_dec-route_north"),
    23: ("door", "ashford_inn"),
    24: ("anchor", "GEN-treasure_anchor_pot_elara-arrival_domestic"),
    25: ("anchor", "GEN-treasure_anchor_crate_shop-shop_frontage"),
    26: ("anchor", "GEN-treasure_anchor_barrel_farmyard-cultivation_edge"),
    27: ("anchor", "GEN-treasure_anchor_jug_well-well_square"),
}


def load_example(name: str) -> dict:
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


def load_modules() -> dict[str, dict]:
    result = {}
    for path in sorted(SHARED.glob("module_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        result[payload["module_id"]] = payload
    return result


def load_catalog() -> dict:
    return merge_catalogs(
        load_tile_assembly_kit_index(KIT_DIR / "index.json"),
        load_tile_assembly_kit_index(KIT_DIR / "authored" / "index.json"),
        load_custom_extension_manifest(KIT_DIR / "custom_extension" / "manifest.json"),
    )


def load_map_vision() -> dict:
    return json.loads(
        (ATLAS / "atlas/docs/09_Technical/Map_Generation/Instances/MV-HOM-ASH-001.json").read_text(encoding="utf-8")
    )


def load_constraint_profile() -> dict:
    return json.loads(
        (ATLAS / "atlas/docs/09_Technical/Map_Generation/Academy/ASHFORD-VISUAL-CONSTRAINT-PROFILE-001.json").read_text(
            encoding="utf-8"
        )
    )


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    temp.replace(path)


def _assembly_file_for(assembly_id: str) -> Path | None:
    for index_path in (KIT_DIR / "index.json", KIT_DIR / "authored" / "index.json"):
        payload = json.loads(index_path.read_text(encoding="utf-8"))
        for entry in payload["assemblies"]:
            if entry["tile_assembly_id"] == assembly_id:
                return index_path.parent / entry["file"]
    return None


def _door_anchor(assembly_id: str) -> dict | None:
    path = _assembly_file_for(assembly_id)
    if path is None:
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    for anchor in payload.get("anchors", []):
        if anchor.get("role") == "entry":
            return anchor
    return None


def composite_assembly(
    data: list[int],
    collision: set[tuple[int, int]],
    assembly_id: str,
    origin_x: int,
    origin_y: int,
    *,
    width: int,
    height: int,
    pending_custom_tileset: list[str],
) -> None:
    """Copy an already-verified TileAssembly's real layered_cells/collision
    mask onto the map at (origin_x, origin_y), by offset only -- no tile IDs
    are computed or guessed here, only relocated.

    Custom-extension-bound assemblies (the roofed well, humming panel, and
    patched fence) have no TileAssembly file: their art lives on
    Ashford_Custom_B.png, which is not yet registered as a tileset B-sheet in
    the production Game's Tilesets.json. Registering a new tileset slot is a
    real production configuration change and deliberately out of scope for a
    disposable candidate build -- this function marks the object's known,
    approved footprint as blocked (conservative: the eventual real art will
    block movement) without guessing at B-sheet tile IDs, and records the
    gap in ``pending_custom_tileset`` for the report.
    """

    path = _assembly_file_for(assembly_id)
    if path is None:
        pending_custom_tileset.append(assembly_id)
        for ly in range(height):
            for lx in range(width):
                collision.add((origin_x + lx, origin_y + ly))
        return

    payload = json.loads(path.read_text(encoding="utf-8"))

    def put(x: int, y: int, layer: int, tile: int) -> None:
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            data[(layer * HEIGHT + y) * WIDTH + x] = tile

    for cell in payload["layered_cells"]:
        wx, wy = origin_x + cell["x"], origin_y + cell["y"]
        for layer_entry in cell["layers"]:
            tile_id = layer_entry["tile_id"]
            if tile_id:
                put(wx, wy, layer_entry["layer"], tile_id)
    mask = payload.get("collision_mask", [])
    for ly, row in enumerate(mask):
        for lx, blocked in enumerate(row):
            if blocked:
                collision.add((origin_x + lx, origin_y + ly))


def build() -> tuple[dict, dict, dict, dict]:
    map_intent = load_example("map_intent.json")
    gameplay_graph = load_example("gameplay_graph.json")
    archetype = load_example("building_archetype.json")
    layout_family = load_example("layout_family.json")
    modules = load_modules()
    catalog = load_catalog()
    map_vision = load_map_vision()
    constraint_profile = load_constraint_profile()

    seed = derive_root_seed(("wo0073-ashford-mapvision-candidate", "seed-1"))
    manifest_id = "GEN-WO0073-ASHFORD-MAPVISION-CANDIDATE-001"
    result = SemanticAssembler(budget=AssemblyBudget(20000, 20)).assemble(
        map_intent=map_intent,
        gameplay_graph=gameplay_graph,
        archetype=archetype,
        layout_family=layout_family,
        modules=modules,
        streams=SeedStreams(seed),
        manifest_id=manifest_id,
        required_beats=tuple(map_intent["required_gameplay_beats"]),
        assembly_catalog=catalog,
        map_vision=map_vision,
        visual_constraint_profile=constraint_profile,
    )
    plan = result.map_plan.to_dict()

    manifest = GenerationManifest.create(
        manifest_id=manifest_id,
        map_intent_id=map_intent["map_intent_id"],
        generator_id="atlas-reusable-map-compiler",
        generator_version="0.1.0",
        archetype_id=archetype["archetype_id"],
        archetype_version=archetype["version"],
        layout_family_id=layout_family["layout_family_id"],
        layout_family_version=layout_family["version"],
        variant_id=result.variant_id,
        style_pack_id="STY-NONE-EXTERIOR-VISUAL-PIPELINE",
        style_pack_version="0.1",
        salt="wo-0073-ashford-mapvision-candidate",
        generated_at="2026-07-15",
        map_vision_id=map_vision["map_vision_id"],
        map_vision_version=map_vision["version"],
        tile_assembly_bindings=list(result.tile_assembly_bindings),
        output_map_plan_ref=result.map_plan.blueprint_id,
    ).to_dict()

    gate_result = run_dual_gate(plan, manifest)

    # --- Tile data ---
    data = [0] * (WIDTH * HEIGHT * 6)

    def put(x: int, y: int, layer: int, tile: int) -> None:
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            data[(layer * HEIGHT + y) * WIDTH + x] = tile

    all_cells = {(x, y) for y in range(HEIGHT) for x in range(WIDTH)}
    paint_region(put, all_cells, GRASS_KIND, 0, treat_off_map_as_same=True)

    zone_rects = {item["terrain_id"].removeprefix("ZONE-"): item["area"] for item in plan["terrain"]}
    zone_center = {zid: (area["x"] + area["w"] // 2, area["y"] + area["h"] // 2) for zid, area in zone_rects.items()}
    path_cells: set[tuple[int, int]] = set()
    for edge in plan["traversable_areas"]:
        (ax, ay), (bx, by) = zone_center[edge["from_zone"]], zone_center[edge["to_zone"]]
        for x in range(min(ax, bx), max(ax, bx) + 1):
            path_cells.add((x, ay))
        for y in range(min(ay, by), max(ay, by) + 1):
            path_cells.add((bx, y))
    if path_cells:
        paint_region(put, path_cells, PATH_KIND, 0)

    collision: set[tuple[int, int]] = set()
    pending_custom_tileset: list[str] = []
    for obstacle in plan["obstacles"]:
        ref = obstacle.get("tile_assembly_ref")
        if ref is None:
            continue
        area = obstacle["area"]
        composite_assembly(
            data, collision, ref, area["x"], area["y"],
            width=obstacle["tile_assembly_width"], height=obstacle["tile_assembly_height"],
            pending_custom_tileset=pending_custom_tileset,
        )

    landmark_world_anchor: dict[str, tuple[int, int]] = {}
    for slot in plan["landmark_slots"]:
        ref = slot.get("tile_assembly_ref")
        if ref is None:
            continue
        width = slot["tile_assembly_width"]
        height = slot["tile_assembly_height"]
        ax, ay = slot["anchor"]["x"], slot["anchor"]["y"]
        origin_x, origin_y = ax - width // 2, ay - height // 2
        composite_assembly(
            data, collision, ref, origin_x, origin_y,
            width=width, height=height, pending_custom_tileset=pending_custom_tileset,
        )
        landmark_world_anchor[slot["landmark_tag"]] = (origin_x, origin_y)

    door_world_anchor: dict[str, tuple[int, int]] = {}
    for obstacle in plan["obstacles"]:
        tag = obstacle["name"]
        ref = obstacle.get("tile_assembly_ref")
        if ref is None:
            continue
        anchor = _door_anchor(ref)
        if anchor is None:
            continue
        area = obstacle["area"]
        door_world_anchor[tag] = (area["x"] + anchor["x"], area["y"] + anchor["y"])

    # --- Event reconciliation: preserve pages/lists verbatim, move x/y only ---
    anchor_points: dict[str, tuple[int, int]] = {}
    for point in plan["transfer_points"]:
        anchor_points[point["transfer_id"]] = (point["anchor"]["x"], point["anchor"]["y"])
    for point in plan["event_anchors"]:
        anchor_points[point["local_anchor_id"]] = (point["anchor"]["x"], point["anchor"]["y"])

    positions: dict[int, tuple[int, int]] = {}
    for event_id, (kind, ref) in EVENT_RECONCILIATION.items():
        if kind == "anchor":
            positions[event_id] = anchor_points[ref]
        elif kind == "landmark":
            positions[event_id] = landmark_world_anchor[ref]
        elif kind == "door":
            positions[event_id] = door_world_anchor[ref]
        # "offset" entries are resolved in the second pass below.
    for event_id, (kind, ref) in EVENT_RECONCILIATION.items():
        if kind == "offset":
            base_id, dx, dy = ref
            bx, by = positions[base_id]
            positions[event_id] = (bx + dx, by + dy)

    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    candidate = copy.deepcopy(source)
    for event in candidate["events"]:
        if event and event["id"] in positions:
            event["x"], event["y"] = positions[event["id"]]
    candidate["data"] = data
    candidate["width"], candidate["height"] = WIDTH, HEIGHT
    candidate["note"] = (
        "WO-0073 review candidate only: built through the MapVision/TileAssembly "
        "compiler pipeline (WO-0071/0072), not hand-authored tiles. Production "
        "Map001 not overwritten; installation requires Chris's explicit acceptance."
    )

    missing_ids = {e["id"] for e in source["events"] if e} - set(EVENT_RECONCILIATION)
    start = door_world_anchor.get("elara_house", zone_center["arrival_domestic"])
    seen = {start}
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for point in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= point[0] < WIDTH and 0 <= point[1] < HEIGHT and point not in collision and point not in seen:
                seen.add(point)
                queue.append(point)
    event_failures = []
    for event in candidate["events"]:
        if not event:
            continue
        point = (event["x"], event["y"])
        ring = {(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)}
        if point not in seen and not ring & seen:
            event_failures.append({"id": event["id"], "name": event["name"], "position": list(point)})
    route_audit = {
        "result": "pass" if not (event_failures or missing_ids) else "fail",
        "origin": list(start),
        "reachable_cells": len(seen),
        "event_failures": event_failures,
        "unreconciled_event_ids": sorted(missing_ids),
        "source_event_count": len([e for e in source["events"] if e]),
        "candidate_event_count": len([e for e in candidate["events"] if e]),
        "event_command_payloads_preserved": all(
            source["events"][i]["pages"] == candidate["events"][i]["pages"]
            for i in range(1, len(source["events"]))
            if source["events"][i]
        ),
    }

    return candidate, plan, manifest, {
        "gate": gate_result.to_dict(),
        "route_audit": route_audit,
        "bindings": list(result.tile_assembly_bindings),
        "pending_custom_tileset_registration": sorted(set(pending_custom_tileset)),
    }


def render(map_path: Path, output: Path) -> None:
    spec = importlib.util.spec_from_file_location("ashford_renderer", RENDERER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    module.GAME = str(GAME)
    module.render_map(str(map_path), str(GAME / "data/Tilesets.json"), str(output))


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    candidate, plan, manifest, evidence = build()

    map_path = OUTPUT / "Map001.mapvision-candidate.json"
    atomic_json(map_path, candidate)
    atomic_json(OUTPUT / "map_plan.json", plan)
    atomic_json(OUTPUT / "generation_manifest.json", manifest)
    atomic_json(OUTPUT / "route_audit.json", evidence["route_audit"])
    atomic_json(
        OUTPUT / "pending_custom_tileset_registration.json",
        {"assembly_ids": evidence["pending_custom_tileset_registration"]},
    )
    (OUTPUT / "structural_preview.txt").write_text(render_ascii_from_dict(plan), encoding="utf-8")

    gate_evidence = record_gate_evidence(
        _DualGateResultView(evidence["gate"]),
        concept_refs=[
            "TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Map_Generation/Concepts/Ashford/ashford-overhead-composition-v2.png",
            "TheLastSwordProtocol-Atlas/atlas/docs/09_Technical/Map_Generation/Concepts/Ashford/ashford-orthographic-town-v2.png",
        ],
        render_refs=[
            "rpgmakerLSP/reports/atlas-import/ashford-mapvision-v3/ashford-mapvision-candidate-render.png",
            "rpgmakerLSP/reports/atlas-import/ashford-mapvision-v3/structural_preview.txt",
        ],
        output_path=OUTPUT / "gate_evidence.json",
    )

    render(map_path, OUTPUT / "ashford-mapvision-candidate-render.png")

    print(f"candidate={map_path}")
    print(f"route_audit={evidence['route_audit']['result']} reachable={evidence['route_audit']['reachable_cells']}")
    print(f"dual_gate={gate_evidence['recommendation']}")
    if evidence["pending_custom_tileset_registration"]:
        print(f"pending custom-tileset registration (footprint reserved, no art composited): {evidence['pending_custom_tileset_registration']}")
    print("Production Map001.json was not read for writing and was not modified.")


def render_ascii_from_dict(plan: dict) -> str:
    from map_plan import MapPlan

    return render_ascii(MapPlan.from_dict(plan))


class _DualGateResultView:
    """Adapts an already-computed DualGateResult.to_dict() payload back into
    the shape record_gate_evidence expects, without recomputing the gate."""

    def __init__(self, payload: dict):
        self._payload = payload

    def to_dict(self) -> dict:
        return self._payload


if __name__ == "__main__":
    main()
