import importlib.util
import tempfile
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

    def test_overview_chain_requires_domain_area_and_topic_readmes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            original_root = validator.EXPERIENCES_ROOT
            try:
                experiences = Path(temp_dir) / "experiences"
                validator.EXPERIENCES_ROOT = experiences
                scenario = (
                    experiences
                    / "programming"
                    / "concurrency"
                    / "race-condition"
                    / "scenarios"
                    / "example.md"
                )
                scenario.parent.mkdir(parents=True)

                errors = validator.validate_overview_chain(scenario)
                self.assertEqual(3, len(errors))
                self.assertIn("missing required domain overview", errors[0])
                self.assertIn("missing required area overview", errors[1])
                self.assertIn("missing required topic overview", errors[2])

                (experiences / "programming" / "README.md").write_text("# Programming\n")
                (experiences / "programming" / "concurrency" / "README.md").write_text(
                    "# Concurrency\n"
                )
                (
                    experiences
                    / "programming"
                    / "concurrency"
                    / "race-condition"
                    / "README.md"
                ).write_text("# Race Condition\n")

                self.assertEqual([], validator.validate_overview_chain(scenario))
            finally:
                validator.EXPERIENCES_ROOT = original_root

    def test_discovery_finds_malformed_scenario_path_but_ignores_topic_readme(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            experiences = Path(temp_dir) / "experiences"
            malformed = experiences / "programming" / "scenarios" / "wrong.md"
            malformed.parent.mkdir(parents=True)
            malformed.write_text("# malformed\n")

            topic_readme = (
                experiences
                / "programming"
                / "concurrency"
                / "race-condition"
                / "README.md"
            )
            topic_readme.parent.mkdir(parents=True)
            topic_readme.write_text("# Race Condition\n")

            discovered = validator.discover_scenarios(experiences)
            self.assertEqual([malformed], discovered)

            original_root = validator.EXPERIENCES_ROOT
            try:
                validator.EXPERIENCES_ROOT = experiences
                errors = validator.validate_path_matches_metadata({}, malformed)
                self.assertIn(
                    "scenario file must live at experiences/<domain>/<area>/<topic>/scenarios/<name>.md",
                    errors,
                )
            finally:
                validator.EXPERIENCES_ROOT = original_root


if __name__ == "__main__":
    unittest.main()
