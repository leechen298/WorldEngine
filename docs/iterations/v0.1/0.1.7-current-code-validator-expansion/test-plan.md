# Test Plan

## Unit Tests

Add or update frontend unit tests to verify selector stability without changing
component behavior:

- `frontend/src/components/WorldPanel.test.ts`
- `frontend/src/components/MemoryPanel.test.ts` if created or existing test
  coverage is extended.
- `frontend/src/components/TimelinePanel.test.ts`

Add or update validator tests:

- `tools/testing/test_validate_agent_smoke_result.py`

Required validator coverage:

- existing `valid-basic-runtime` fixture still passes.
- new `valid-params-flow` fixture passes.
- new `valid-invalid-param` fixture passes.
- `verdict_source = agent` still fails.
- direct API operation records still fail.
- missing scenario-required UI target fails.
- `result.json.scenario` / `api-summary.json.scenario` mismatch fails.
- missing checker evidence fails.
- incorrect params-flow observed value or counter event increment fails.
- incorrect invalid-param unchanged evidence fails.

## Regression Tests

- Existing backend runtime and API behavior must stay unchanged.
- Existing frontend unit tests must pass.
- Existing dashboard E2E scenarios must pass.
- Existing Agent smoke fixture validation must pass.
- Existing Codex skill validation must pass.

## Commands

Run these after implementation:

```bash
git diff --check
cd frontend && pnpm test
make test-e2e
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py -q
make validate-agent-smoke-fixtures
make validate-codex-skills
if git diff --name-only | rg '^(backend/worldengine/)'; then
  echo "Unexpected backend/worldengine change"
  exit 1
fi
```

Expected result for the final block: no output.

## Acceptance Criteria

- 0.1.7 package documents are reviewed before implementation starts.
- Only allowed files and surfaces change.
- The validator supports exactly:
  - `dashboard-basic-runtime`
  - `dashboard-params-flow`
  - `dashboard-invalid-param`
- Scenario-specific UI targets are enforced.
- Direct API operation logs remain rejected.
- `api-summary.json` scenario mismatch is rejected.
- The evidence helper can generate deterministic checker artifacts from real
  backend state.
- `docs/testing/agent-smoke/result-schema.json` accepts the three supported
  scenarios.
- Agent smoke scenario docs mark `dashboard-params-flow` and
  `dashboard-invalid-param` as validator-supported with no live run recorded
  only after implementation and tests pass.
- `review.md` records changed files, commands run, test results,
  compatibility review, scope review, unresolved findings, and final
  assessment.

## Not Run

Do not run in 0.1.7:

- live Agent smoke.
- `make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest`
  against new live evidence.
- Codex/test-runner autonomous scenarios.
- archive-summary E2E implementation or execution beyond existing E2E
  regression.
