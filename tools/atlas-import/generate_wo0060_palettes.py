#!/usr/bin/env python3
"""Generate provenance-rich WO-0060 palettes from the clean target project."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from validate_tile_palette import expected_tile_id, layer, passage


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
WORKSPACE = REPO.parent
PROJECT = WORKSPACE / "TheLastSwordProtocol-Game"
ATLAS_STUDIO = WORKSPACE / "AtlasStudio"
CONTACT_ROOT = ATLAS_STUDIO / "atlas-tools/mapgen/compiler/style_study/wo0060/contact_sheets"
OUTPUT = HERE / "tile-palettes"
SOURCE_HASHES = {
    path.stem: hashlib.sha256(path.read_bytes()).hexdigest()
    for path in (PROJECT / "img/tilesets").glob("Inside_*.png")
}


def entry(tag: str, sheet: str, addressing: str, index: int, role: str, contact: str, notes: str, component: str | None = None) -> dict:
    value = {
        "visual_tag": tag,
        "asset_sheet": sheet,
        "source_index": {"addressing": addressing, "index": index},
        "role": role,
        "provenance": {"contact_sheet": contact, "notes": notes},
    }
    if component:
        value["component"] = component
    return value


COMMON = [
    entry("hearth_focal_feature", "Inside_B", "normal_tile", 195, "landmark", "inside_b_tiles.png", "Tile 195 is the brick hearth/fireplace identified in the labeled contact sheet."),
    entry("wall_mounted_flame", "Inside_B", "normal_tile", 104, "lighting", "inside_b_tiles.png", "Tile 104 is the isolated flame/sconce accent visible in the labeled contact sheet."),
    entry("shelf_wall_run", "Inside_B", "normal_tile", 157, "furniture", "inside_b_tiles.png", "Tile 157 is a wall-facing filled bookshelf in the labeled contact sheet."),
    entry("picture_and_cabinet_nook", "Inside_B", "normal_tile", 130, "furniture", "inside_b_tiles.png", "Tile 130 is the framed landscape furnishing identified in the labeled contact sheet."),
    entry("bed_alcove", "Inside_B", "normal_tile", 168, "furniture", "inside_b_tiles.png", "Tile 168 is the upper half of the quilted blue bed in the labeled contact sheet.", "top"),
    entry("bed_alcove", "Inside_B", "normal_tile", 176, "furniture", "inside_b_tiles.png", "Tile 176 is the lower half of the quilted blue bed in the labeled contact sheet.", "bottom"),
    entry("back_wall_shelf_run", "Inside_B", "normal_tile", 157, "furniture", "inside_b_tiles.png", "Tile 157 is the verified filled bookshelf reused for a back-wall shelf run."),
    entry("hearth_accent", "Inside_B", "normal_tile", 195, "landmark", "inside_b_tiles.png", "Tile 195 is the verified brick hearth reused for the optional hearth accent."),
    entry("counter_service_point", "Inside_B", "normal_tile", 112, "furniture", "inside_b_tiles.png", "Tile 112 is the left half of the plain wooden counter/table visible in the labeled contact sheet.", "left"),
    entry("counter_service_point", "Inside_B", "normal_tile", 113, "furniture", "inside_b_tiles.png", "Tile 113 is the right half of the plain wooden counter/table visible in the labeled contact sheet.", "right"),
    entry("display_table", "Inside_B", "normal_tile", 208, "furniture", "inside_b_tiles.png", "Tile 208 is a plain horizontal wooden display table visible in the labeled contact sheet."),
]

TEMPERATE = COMMON + [
    entry("floor_rug_focal_accent", "Inside_B", "normal_tile", 80, "edge_dressing", "inside_b_tiles.png", "Tile 80 is a red-gold rug panel visible in the labeled contact sheet."),
    entry("warm_wood_plank_floor", "Inside_A2", "autotile_kind", 16, "floor", "inside_a2_kinds.png", "Autotile kind 16 is the warm wood floor cited by the WO-0060 study."),
    entry("rustic_brick_wall", "Inside_A4", "autotile_kind", 85, "wall", "inside_a4_kinds.png", "Autotile kind 85 is the visibly brick member of the study's cited rustic 84-87 family, confirmed in the composited candidate render."),
    entry("warm_wood_paneling", "Inside_A4", "autotile_kind", 97, "wall", "inside_a4_kinds.png", "Autotile kind 97 is the warm-panel member of the study's cited 96-98 family."),
    entry("warm_wood_plank_threshold", "Inside_A5", "normal_tile", 1, "threshold", "inside_a5_tiles.png", "Normal tile 1 is the warm plank threshold cited by the WO-0060 study."),
    entry("quilted_wood_frame_bed", "Inside_B", "normal_tile", 168, "furniture", "inside_b_tiles.png", "Tile 168 is the quilted wood-frame bed top identified in the contact sheet."),
    entry("red_curtain_accent", "Inside_B", "normal_tile", 57, "edge_dressing", "inside_b_tiles.png", "Tile 57 is the deep red curtain panel visible in the labeled contact sheet."),
]

COASTAL = COMMON + [
    entry("pale_mosaic_tile_floor", "Inside_A2", "autotile_kind", 17, "floor", "inside_a2_kinds.png", "Autotile kind 17 is the pale mosaic floor cited by the WO-0060 study."),
    entry("whitewashed_plaster_wall", "Inside_A4", "autotile_kind", 101, "wall", "inside_a4_kinds.png", "Autotile kind 101 is a white-plaster wall/ceiling member explicitly cited by the WO-0060 study."),
    entry("pale_stone_threshold", "Inside_A5", "normal_tile", 20, "threshold", "inside_a5_tiles.png", "Normal tile 20 is the pale stone threshold cited by the WO-0060 study."),
    entry("striped_cabana_bed", "Inside_B", "normal_tile", 169, "furniture", "inside_b_tiles.png", "Tile 169 is the upper half of the orange-white striped bed.", "top"),
    entry("striped_cabana_bed", "Inside_B", "normal_tile", 177, "furniture", "inside_b_tiles.png", "Tile 177 is the lower half of the orange-white striped bed.", "bottom"),
    entry("pale_curtain_accent", "Inside_B", "normal_tile", 48, "edge_dressing", "inside_b_tiles.png", "Tile 48 is the pale curtain panel visible in the labeled contact sheet."),
    entry("blue_patterned_floor_accent", "Inside_A5", "normal_tile", 42, "edge_dressing", "inside_a5_tiles.png", "Normal tile 42 is the passable blue patterned floor accent confirmed in the WO-0061 composited render."),
]


def build(palette_id: str, style_pack_ref: str, bindings: list[dict]) -> dict:
    rows = json.loads((PROJECT / "data/Tilesets.json").read_text(encoding="utf-8"))
    tileset = next(row for row in rows if row and row.get("name") == "Inside")
    for binding in bindings:
        tile_id = expected_tile_id(binding)
        flags = int(tileset["flags"][tile_id])
        binding.update({
            "tile_id": tile_id,
            "flags": flags,
            "passage": passage(flags),
            "layer": layer(binding["asset_sheet"], flags),
            "adjacency": "autotile_48" if binding["source_index"]["addressing"] == "autotile_kind" else "none",
            "source_sha256": SOURCE_HASHES[binding["asset_sheet"]],
        })
    return {
        "schema_version": "0.1", "tile_palette_id": palette_id, "version": "0.1",
        "style_pack_ref": style_pack_ref, "target_engine": "rpg_maker_mz",
        "tileset_id": tileset["id"], "tileset_name": tileset["name"],
        "status": "generated_pending_live_review", "bindings": bindings,
        "owner_repo": "rpgmakerLSP",
        "provenance": {
            "target_tilesets_sha256": hashlib.sha256((PROJECT / "data/Tilesets.json").read_bytes()).hexdigest(),
            "contact_sheet_root": str(CONTACT_ROOT.relative_to(ATLAS_STUDIO)),
            "notes": "Generated from labeled WO-0060 contact-sheet selections and verified against the clean target project's exact Inside tileset flags. Not approved until Chris records live RPG Maker review.",
        },
        "human_review": {"rpg_maker_live_confirmed": False, "reviewer": None, "reviewed_at": None, "notes": None},
    }


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    outputs = {
        "temperate-village-interior.palette.json": build("PAL-TEMPERATE-VILLAGE-INTERIOR", "STY-ASHFORD-COZY-INTERIOR", TEMPERATE),
        "coastal-settlement-interior.palette.json": build("PAL-COASTAL-SETTLEMENT-INTERIOR", "STY-COASTAL-SETTLEMENT-INTERIOR", COASTAL),
    }
    for name, payload in outputs.items():
        (OUTPUT / name).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE {name}: {len(payload['bindings'])} bindings")


if __name__ == "__main__":
    main()
