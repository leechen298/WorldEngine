from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


PROJECT_SKILLS = (
    "worldengine-e2e-runner",
    "worldengine-agent-smoke-runner",
)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _default_target() -> Path:
    configured = os.environ.get("CODEX_SKILLS_DIR")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".agents" / "skills"


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


def sync_skills(target_root: Path, dry_run: bool) -> int:
    repo_root = _repo_root()
    source_root = repo_root / ".agents" / "skills"
    errors = _validate_source(source_root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    for skill_name in PROJECT_SKILLS:
        source_dir = source_root / skill_name
        target_dir = target_root / skill_name
        print(f"{'DRY-RUN' if dry_run else 'SYNC'}: {source_dir} -> {target_dir}")
        if dry_run:
            continue

        target_root.mkdir(parents=True, exist_ok=True)
        if target_dir.exists():
            shutil.rmtree(target_dir)
        shutil.copytree(source_dir, target_dir)

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Sync WorldEngine project Codex skills.")
    parser.add_argument(
        "--target",
        type=Path,
        default=_default_target(),
        help="Codex skills target directory. Defaults to CODEX_SKILLS_DIR or ~/.agents/skills.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate and print sync operations only.")
    args = parser.parse_args(argv)

    return sync_skills(args.target.expanduser(), args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
