# Test Plan

## Required Commands

Run after implementation:

```bash
make validate-codex-skills
/usr/bin/python3 /Users/leechen/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/worldengine-iteration-docs
/usr/bin/python3 /Users/leechen/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/worldengine-iteration-dev
/usr/bin/python3 /Users/leechen/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/worldengine-e2e-runner
/usr/bin/python3 /Users/leechen/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/worldengine-agent-smoke-runner
/usr/bin/python3 /Users/leechen/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/worldengine-agent-autonomous-test-runner
find /Users/leechen/.agents/skills -maxdepth 1 -type d -name 'worldengine-*' -print
git diff --check
```

The `find` command should produce no output unless the user explicitly asked to
create personal WorldEngine skill copies.

## Acceptance Criteria

- all five project skill directories contain non-empty `SKILL.md` files.
- `make validate-codex-skills` exits `0` and includes all five skills.
- each `quick_validate.py` command exits `0`.
- no default validation or helper command recreates personal
  `/Users/leechen/.agents/skills/worldengine-*` directories.
- `worldengine-iteration-docs` is clearly documentation-stage only.
- `worldengine-iteration-dev` is clearly implementation-stage only and does not
  own iteration document creation or repair.
- `worldengine-agent-smoke-runner` is clearly basic Agent smoke only.
- `worldengine-agent-autonomous-test-runner` is clearly broader than smoke and
  stops when no explicit autonomous test contract exists.
- existing E2E and Agent smoke evidence rules are not weakened.
- no backend, frontend, runtime fixture, or validator file changes appear in
  the final diff.

## Not Required

Backend tests, frontend tests, browser E2E, and live Agent smoke are not
required for this package unless implementation changes those surfaces. The
package is workflow guidance and project skill validation metadata only.
