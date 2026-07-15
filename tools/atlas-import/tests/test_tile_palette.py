from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve()
IMPORT_ROOT = HERE.parents[1]
REPO = HERE.parents[3]
WORKSPACE = REPO.parent
sys.path.insert(0, str(IMPORT_ROOT))

from validate_tile_palette import verify_palette  # noqa: E402


PALETTES = IMPORT_ROOT / "tile-palettes"
PROJECT = WORKSPACE / "TheLastSwordProtocol-Game"
STUDIO = WORKSPACE / "AtlasStudio"
CONTACTS = STUDIO / "atlas-tools/mapgen/compiler/style_study/wo0060/contact_sheets"
STYLES = STUDIO / "atlas-tools/mapgen/compiler/contract/examples/shared"
sys.path.insert(0, str(STUDIO / "atlas-tools/mapgen/compiler"))
from contract.validate_contract import validate  # noqa: E402


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def style_for(palette: dict) -> dict:
    name = {
        "STY-ASHFORD-COZY-INTERIOR": "style_pack_ashford_cozy_interior.json",
        "STY-COASTAL-SETTLEMENT-INTERIOR": "style_pack_coastal_settlement_interior.json",
    }[palette["style_pack_ref"]]
    return load(STYLES / name)


class PaletteTests(unittest.TestCase):
    def verify(self, palette: dict) -> list:
        return verify_palette(palette, style_pack=style_for(palette), project_root=PROJECT, contact_root=CONTACTS)

    def test_both_palettes_verify_against_clean_target(self) -> None:
        schema = load(STUDIO / "atlas-tools/mapgen/compiler/contract/schemas/tile_palette.schema.json")
        for path in sorted(PALETTES.glob("*.palette.json")):
            with self.subTest(path=path.name):
                palette = load(path)
                self.assertEqual([], validate(palette, schema))
                self.assertEqual([], self.verify(palette))

    def test_negative_fixture_suite_fails_for_expected_reason(self) -> None:
        suite = load(PALETTES / "negative-fixtures.json")
        base = load(PALETTES / suite["base_palette"])
        for case in suite["cases"]:
            with self.subTest(case=case["case_id"]):
                candidate = copy.deepcopy(base)
                binding = next(item for item in candidate["bindings"] if item["visual_tag"] == case["binding_tag"])
                target = binding
                parts = case["field"].split(".")
                for part in parts[:-1]:
                    target = target[part]
                target[parts[-1]] = case["value"]
                codes = {finding.code for finding in self.verify(candidate)}
                self.assertIn(case["expected_code"], codes)

    def test_approval_requires_live_rpg_maker_confirmation(self) -> None:
        palette = load(PALETTES / "temperate-village-interior.palette.json")
        palette["status"] = "approved"
        self.assertIn("approval_without_live_review", {finding.code for finding in self.verify(palette)})


if __name__ == "__main__":
    unittest.main()
