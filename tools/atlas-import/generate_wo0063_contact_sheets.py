#!/usr/bin/env python3
"""Generate labeled Outside tileset sheets for WO-0063 evidence."""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[2]
STUDIO_TOOL = WORKSPACE / "AtlasStudio/atlas-tools/mapgen/compiler/style_study/wo0060"
sys.path.insert(0, str(STUDIO_TOOL))
from contact_sheet import contact_sheet_autotile, contact_sheet_normal  # noqa: E402

GAME = WORKSPACE / "TheLastSwordProtocol-Game"
OUT = HERE.parents[1] / "reports/atlas-import/wo0063/contact_sheets"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    tiles = GAME / "img/tilesets"
    contact_sheet_autotile(str(tiles / "Outside_A1.png"), str(OUT / "outside_a1_kinds.png"), 0, range(0, 16), "Outside_A1 kinds")
    contact_sheet_autotile(str(tiles / "Outside_A2.png"), str(OUT / "outside_a2_kinds.png"), 1, range(16, 48), "Outside_A2 kinds")
    contact_sheet_normal(str(tiles / "Outside_B.png"), str(OUT / "outside_b_tiles.png"), "Outside_B normal tiles", max_tiles=256, set_number=5, id_base=0)
    contact_sheet_normal(str(tiles / "Outside_C.png"), str(OUT / "outside_c_tiles.png"), "Outside_C normal tiles", max_tiles=256, set_number=6, id_base=256)


if __name__ == "__main__":
    main()
