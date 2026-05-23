# Technical Design

## Project Skills

The package adds two repository-owned skills:

```text
.agents/skills/worldengine-e2e-runner/SKILL.md
.agents/skills/worldengine-agent-smoke-runner/SKILL.md
```

They are intentionally small and procedural. The validator and Playwright tests
remain the source of truth for PASS/FAIL.

## Sync Script

`tools/testing/sync_codex_skills.py` copies selected project skills into a local
Codex skills directory.

Default target:

```text
~/.agents/skills/
```

Override target:

```bash
python3 tools/testing/sync_codex_skills.py --target /path/to/skills
```

Dry run:

```bash
python3 tools/testing/sync_codex_skills.py --dry-run
```

## Make Targets

```bash
make validate-codex-skills
make sync-codex-skills
```

`validate-codex-skills` checks that the project skill directories are readable
and syncable without writing outside the repository.

`sync-codex-skills` performs the local copy.

## Why Not Plugin

A plugin is not needed for this package because there is no MCP server, app,
hook, marketplace distribution, or bundled external capability. The requirement
is project-specific execution guidance, which fits Codex skills directly.
