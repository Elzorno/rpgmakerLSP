from __future__ import annotations

import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path


HERE = Path(__file__).resolve()
IMPORT_ROOT = HERE.parents[1]
REPO = HERE.parents[3]
WORKSPACE = REPO.parent
STUDIO = WORKSPACE / "AtlasStudio"
GAME = WORKSPACE / "TheLastSwordProtocol-Game"
sys.path.insert(0, str(IMPORT_ROOT))

from mapplan_candidate_compiler import CandidateError, compile_candidate  # noqa: E402


PLAN = STUDIO / "atlas-tools/mapgen/compiler/prototypes/wo0059/shop-compact-seed-1.map_plan.json"
PALETTE = IMPORT_ROOT / "tile-palettes/temperate-village-interior.palette.json"
STYLE = STUDIO / "atlas-tools/mapgen/compiler/contract/examples/shared/style_pack_ashford_cozy_interior.json"
CONTACTS = STUDIO / "atlas-tools/mapgen/compiler/style_study/wo0060/contact_sheets"
RENDERER = STUDIO / "atlas-tools/mapgen/compiler/style_study/wo0060/render_map.py"


def write_ledger(root: Path, state: str) -> None:
    (root / "data").mkdir(parents=True)
    (root / "map_ownership.json").write_text(json.dumps({
        "schema_version": "1.0", "maps": {"1": {"state": state, "atlas_screen": None, "name": "test"}}
    }), encoding="utf-8")


def args(root: Path) -> Namespace:
    return Namespace(map_plan=PLAN, palette=PALETTE, style_pack=STYLE, source_project=GAME,
                     target_project=root, map_id=1, output_dir=root / "candidate", contact_root=CONTACTS,
                     renderer=RENDERER)


class CandidateCompilerTests(unittest.TestCase):
    def test_candidate_has_valid_rpg_maker_shape_and_routes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_ledger(root, "generated")
            result = compile_candidate(args(root))
            payload = json.loads(result["map"].read_text(encoding="utf-8"))
            self.assertEqual(payload["width"] * payload["height"] * 6, len(payload["data"]))
            self.assertEqual(3, payload["tilesetId"])
            self.assertEqual([None, "GEN-exit_transfer-entry_threshold", "GEN-npc_service_point-service_point"],
                             [event if event is None else event["name"] for event in payload["events"][:3]])
            self.assertTrue(all(event["note"].startswith("Adapter shell collision") for event in payload["events"][3:]))
            self.assertEqual("pass", result["route_audit"]["result"])
            self.assertTrue(result["manifest"].is_file())
            self.assertTrue(result["diagnostics"].is_file())
            self.assertTrue(result["render"].is_file())

    def test_hand_authored_target_is_refused_without_write(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_ledger(root, "hand_authored")
            with self.assertRaises(CandidateError) as caught:
                compile_candidate(args(root))
            self.assertIn("hand_authored", str(caught.exception))
            self.assertFalse((root / "data/Map001.json").exists())

    def test_locked_and_missing_ledgers_fail_closed(self) -> None:
        for state in ("locked", None):
            with self.subTest(state=state), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                if state:
                    write_ledger(root, state)
                with self.assertRaises(CandidateError):
                    compile_candidate(args(root))


if __name__ == "__main__":
    unittest.main()
