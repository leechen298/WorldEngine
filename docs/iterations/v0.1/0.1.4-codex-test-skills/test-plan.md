# Test Plan

## Required Verification

Run and record:

```bash
make validate-codex-skills
python3 tools/testing/sync_codex_skills.py --dry-run
/usr/bin/python3 /Users/leechen/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/worldengine-e2e-runner
/usr/bin/python3 /Users/leechen/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/worldengine-agent-smoke-runner
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py -q
make validate-agent-smoke-fixtures
git diff --check
```

If the local Codex skills directory is updated in this session, also run:

```bash
make sync-codex-skills
```

## Expected Results

- both project skill `SKILL.md` files are found.
- dry run lists the target copy operations.
- sync exits `0` when allowed to write to the configured local skills
  directory.
- no runtime tests are required because this package does not change runtime,
  UI behavior, E2E tests, or validator semantics.

## Reporting Rule

Do not report the skills as synced unless `make sync-codex-skills` actually ran
and exited `0` in the current session.
