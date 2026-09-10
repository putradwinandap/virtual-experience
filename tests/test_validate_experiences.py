import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_experiences.py"
SPEC = importlib.util.spec_from_file_location("validate_experiences", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class ExperienceValidatorTests(unittest.TestCase):
    def test_valid_fixture_passes(self):
        errors = validator.validate_file(ROOT / "tests" / "fixtures" / "valid-scenario.md")
        self.assertEqual([], errors)

    def test_invalid_fixture_fails_with_actionable_errors(self):
        errors = validator.validate_file(ROOT / "tests" / "fixtures" / "invalid-scenario.md")
        self.assertTrue(errors)
        combined = "\n".join(errors)
        self.assertIn("domain must be a lowercase kebab-case string", combined)
        self.assertIn("topic must be a lowercase kebab-case string", combined)
        self.assertIn("difficulty must be one of", combined)
        self.assertIn("provenance.type must be one of", combined)
        self.assertIn("concepts must be a non-empty YAML list", combined)


if __name__ == "__main__":
    unittest.main()
