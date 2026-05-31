# Test Plan

## Red / Coverage-Gap Checks

Before adding new coverage, run:

```bash
cd frontend && pnpm exec playwright test e2e/agent-loop.spec.ts -g "noop intent rejects patches"
```

Expected before implementation: no matching test.

After adding autonomous checker tests but before checker implementation, run:

```bash
cd backend && .venv/bin/python -m pytest ../tools/testing/test_validate_agent_autonomous_result.py -q
```

Expected before implementation: import or unsupported-checker failure.

## Required Validation Commands

Run and record:

```bash
make check-backend
make check-frontend
cd backend && .venv/bin/python -m pytest app/tests/test_agent_perception.py app/tests/test_agent_action_adapter.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py -q
cd backend && .venv/bin/python -m pytest app/tests tests -q
cd frontend && pnpm test
cd frontend && pnpm build
cd frontend && pnpm exec playwright test e2e/agent-loop.spec.ts
make test-e2e
make validate-agent-smoke-fixtures
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/<timestamp>
git diff --check
```

If sandbox restrictions prevent local port binding for E2E, rerun the same
command outside the sandbox and record both outcomes.

## Acceptance Criteria

- Agent Loop E2E boundary coverage passes.
- Autonomous checker unit tests and fixture command pass, including expected
  negative fixture failures.
- A timestamped autonomous result validates with the deterministic checker.
- Existing backend, frontend unit, E2E, and smoke commands are recorded.
- Frontend build failure is recorded as P1 if still present.
- Final assessment is `partial` unless every required command, including build,
  passes.
