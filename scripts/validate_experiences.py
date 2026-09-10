#!/usr/bin/env python3
"""Validate Virtual Experience scenario files against the accepted MVP schema."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPERIENCES_ROOT = ROOT / "experiences"

REQUIRED_FIELDS = {
    "title",
    "domain",
    "area",
    "topic",
    "difficulty",
    "provenance",
    "concepts",
}

ALLOWED_DIFFICULTIES = {"beginner", "intermediate", "advanced"}
ALLOWED_PROVENANCE = {"real", "adapted", "illustrative"}
ALLOWED_DOMAINS = {"programming"}
ALLOWED_AREAS = {
    "concurrency",
    "databases",
    "api-and-integration",
    "distributed-systems",
    "production-and-reliability",
    "security",
    "git-and-collaboration",
    "testing",
    "performance",
    "architecture-and-design",
}
KEBAB_CASE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ValidationError(Exception):
    pass


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        raise ValidationError("missing YAML front matter opening delimiter '---'")

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValidationError("missing YAML front matter closing delimiter '---'") from exc

    raw_yaml = "\n".join(lines[1:end])
    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as exc:
        raise ValidationError(f"invalid YAML front matter: {exc}") from exc

    if not isinstance(data, dict):
        raise ValidationError("front matter must be a YAML mapping/object")

    body = "\n".join(lines[end + 1 :]).strip()
    return data, body


def validate_kebab(value: Any, field: str) -> list[str]:
    if not isinstance(value, str) or not KEBAB_CASE.fullmatch(value):
        return [f"{field} must be a lowercase kebab-case string"]
    return []


def scenario_relative_parts(path: Path) -> tuple[str, ...] | None:
    try:
        return path.resolve().relative_to(EXPERIENCES_ROOT.resolve()).parts
    except ValueError:
        return None


def validate_path_matches_metadata(data: dict[str, Any], path: Path) -> list[str]:
    """Expected scenario path: experiences/<domain>/<area>/<topic>/scenarios/<file>.md."""
    parts = scenario_relative_parts(path)
    if parts is None:
        return []

    if len(parts) != 5 or parts[3] != "scenarios" or path.suffix.lower() != ".md":
        return [
            "scenario file must live at experiences/<domain>/<area>/<topic>/scenarios/<name>.md"
        ]

    errors: list[str] = []
    expected_domain, expected_area, expected_topic = parts[0], parts[1], parts[2]
    if data.get("domain") != expected_domain:
        errors.append(f"domain metadata must match path value '{expected_domain}'")
    if data.get("area") != expected_area:
        errors.append(f"area metadata must match path value '{expected_area}'")
    if data.get("topic") != expected_topic:
        errors.append(f"topic metadata must match path value '{expected_topic}'")
    return errors


def validate_overview_chain(path: Path) -> list[str]:
    """Require README.md at Domain, Area, and Topic for real repository scenarios."""
    parts = scenario_relative_parts(path)
    if parts is None:
        return []
    if len(parts) != 5 or parts[3] != "scenarios":
        return []

    domain, area, topic = parts[0], parts[1], parts[2]
    required = [
        ("domain", EXPERIENCES_ROOT / domain / "README.md"),
        ("area", EXPERIENCES_ROOT / domain / area / "README.md"),
        ("topic", EXPERIENCES_ROOT / domain / area / topic / "README.md"),
    ]

    errors: list[str] = []
    for level, overview in required:
        if not overview.is_file():
            errors.append(
                f"missing required {level} overview: {overview.relative_to(ROOT).as_posix()}"
            )
    return errors


def validate_metadata(data: dict[str, Any], path: Path) -> list[str]:
    errors: list[str] = []

    missing = sorted(REQUIRED_FIELDS - data.keys())
    for field in missing:
        errors.append(f"missing required metadata field: {field}")

    if "title" in data and (not isinstance(data["title"], str) or not data["title"].strip()):
        errors.append("title must be a non-empty string")

    domain = data.get("domain")
    if domain is not None:
        errors.extend(validate_kebab(domain, "domain"))
        if isinstance(domain, str) and domain not in ALLOWED_DOMAINS:
            errors.append(f"unknown domain '{domain}'; allowed: {', '.join(sorted(ALLOWED_DOMAINS))}")

    area = data.get("area")
    if area is not None:
        errors.extend(validate_kebab(area, "area"))
        if isinstance(area, str) and area not in ALLOWED_AREAS:
            errors.append(f"unknown area '{area}'")

    topic = data.get("topic")
    if topic is not None:
        errors.extend(validate_kebab(topic, "topic"))

    difficulty = data.get("difficulty")
    if difficulty is not None and difficulty not in ALLOWED_DIFFICULTIES:
        errors.append(
            f"difficulty must be one of: {', '.join(sorted(ALLOWED_DIFFICULTIES))}"
        )

    provenance = data.get("provenance")
    if provenance is not None:
        if not isinstance(provenance, dict):
            errors.append("provenance must be a mapping with a 'type' field")
        else:
            provenance_type = provenance.get("type")
            if provenance_type not in ALLOWED_PROVENANCE:
                errors.append(
                    f"provenance.type must be one of: {', '.join(sorted(ALLOWED_PROVENANCE))}"
                )

    concepts = data.get("concepts")
    if concepts is not None:
        if not isinstance(concepts, list) or not concepts:
            errors.append("concepts must be a non-empty YAML list")
        else:
            for index, concept in enumerate(concepts):
                errors.extend(validate_kebab(concept, f"concepts[{index}]"))

    contributor = data.get("contributor")
    if contributor is not None:
        if not isinstance(contributor, dict):
            errors.append("contributor must be a mapping")
        elif "github" in contributor and (
            not isinstance(contributor["github"], str) or not contributor["github"].strip()
        ):
            errors.append("contributor.github must be a non-empty string when provided")

    errors.extend(validate_path_matches_metadata(data, path))
    errors.extend(validate_overview_chain(path))
    return errors


def validate_body(body: str) -> list[str]:
    errors: list[str] = []
    if not body:
        errors.append("scenario body must not be empty")
    elif not re.search(r"^#\s+\S+", body, flags=re.MULTILINE):
        errors.append("scenario body must contain a top-level '# ' heading")
    return errors


def validate_file(path: Path) -> list[str]:
    try:
        metadata, body = parse_front_matter(path)
    except (OSError, ValidationError) as exc:
        return [str(exc)]

    return validate_metadata(metadata, path) + validate_body(body)


def discover_scenarios(root: Path) -> list[Path]:
    """Discover Markdown files placed anywhere below a scenarios directory.

    Broad discovery is intentional: malformed hierarchy paths must be discovered so
    path validation can reject them rather than silently skipping them.
    """
    if not root.exists():
        return []
    return sorted(
        path
        for path in root.rglob("*.md")
        if "scenarios" in path.relative_to(root).parts
    )


def run(paths: list[Path]) -> int:
    failures = 0
    for path in paths:
        errors = validate_file(path)
        if errors:
            failures += 1
            print(f"::error file={path.as_posix()}::{len(errors)} validation error(s)")
            print(f"FAIL {path.as_posix()}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path.as_posix()}")

    if failures:
        print(f"\nValidation failed: {failures} file(s) invalid.")
        return 1

    print(f"\nValidation passed: {len(paths)} scenario file(s) checked.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="scenario files to validate")
    args = parser.parse_args()

    paths = args.paths or discover_scenarios(EXPERIENCES_ROOT)
    return run(paths)


if __name__ == "__main__":
    sys.exit(main())
