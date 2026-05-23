from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_SKILLS = (
    "worldengine-iteration-docs",
    "worldengine-iteration-dev",
    "worldengine-e2e-runner",
    "worldengine-agent-smoke-runner",
    "worldengine-agent-autonomous-test-runner",
)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _validate_source(source_root: Path) -> list[str]:
    errors: list[str] = []
    for skill_name in PROJECT_SKILLS:
        skill_dir = source_root / skill_name
        skill_file = skill_dir / "SKILL.md"
        if not skill_dir.is_dir():
            errors.append(f"Missing skill directory: {skill_dir}")
        elif not skill_file.is_file():
            errors.append(f"Missing SKILL.md: {skill_file}")
        elif skill_file.stat().st_size == 0:
            errors.append(f"Empty SKILL.md: {skill_file}")
    return errors


def validate_project_skills() -> int:
    repo_root = _repo_root()
    source_root = repo_root / ".agents" / "skills"
    errors = _validate_source(source_root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("Project skill validation only. Personal sync is disabled.")
    for skill_name in PROJECT_SKILLS:
        print(f"OK: {source_root / skill_name / 'SKILL.md'}")

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate WorldEngine project Codex skills. Historical script name; "
            "personal skill sync is disabled."
        )
    )
    parser.add_argument(
        "--target",
        type=Path,
        help="Accepted for compatibility only; ignored because personal sync is disabled.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Accepted for compatibility only.")
    parser.parse_args(argv)

    return validate_project_skills()


if __name__ == "__main__":
    raise SystemExit(main())
