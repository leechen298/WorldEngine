# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Focused Tests

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
make validate-agent-autonomous-fixtures
```

Expected coverage:

- existing valid dashboard fixture still passes.
- existing invalid autonomous fixtures still fail.
- new full lifecycle scenario passes with complete lifecycle evidence.
- unsupported or incomplete lifecycle evidence fails.
- missing Agent action evidence fails.
- client-scripted Agent action evidence fails.
- non-advancing runtime evidence fails.
- failed redaction evidence fails.

## Regression Tests

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

If the checker change is broad or unexpected failures appear, also run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py tools/testing/test_validate_agent_autonomous_result.py -q
```

## Scenario Verification

The live validation run, outside this package, must later create a result
directory and run:

```bash
make validate-agent-autonomous-result RESULT_DIR=<worldengine-full-lifecycle-result-dir>
```

This package only makes that validation case executable.

## Acceptance Criteria

- The new scenario is documented.
- The checker supports `worldengine-full-lifecycle-autonomous`.
- The schema allows the new scenario.
- Positive and negative checker tests prove lifecycle evidence is enforced.
- Fixture validation passes.
- No runtime, provider, frontend, API route, or Validation Client code changes
  are introduced.

## Not Run

Live WorldEngine autonomous validation is not part of this package. It must be
run later with actual WorldEngine and Validation Client services.
