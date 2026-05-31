# Plan

## Objective

Implement and run v0.4 post-closeout E2E and Agent UI/CLI smoke coverage for
the current product surface.

## Authoritative Inputs Read

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.4/README.md`
- `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/final-closeout.md`
- `frontend/e2e/dashboard.spec.ts`
- `frontend/playwright.config.ts`
- `docs/testing/agent-smoke/README.md`
- `docs/testing/agent-smoke/README.zh.md`
- `tools/testing/agent_smoke_evidence.py`
- `tools/testing/validate_agent_smoke_result.py`
- `tools/testing/test_validate_agent_smoke_result.py`

## Files To Create Or Update

- Create `frontend/e2e/agent-loop.spec.ts`.
- Update `frontend/e2e/dashboard.spec.ts`.
- Create `docs/testing/e2e-scenarios/agent-loop-step.md`.
- Update `docs/testing/e2e-scenarios/README.md`.
- Create `docs/testing/agent-smoke/scenarios/dashboard-agent-autotune.md`.
- Update `docs/testing/agent-smoke/README.md`.
- Update `docs/testing/agent-smoke/README.zh.md`.
- Update `tools/testing/agent_smoke_evidence.py`.
- Update `tools/testing/validate_agent_smoke_result.py`.
- Update `tools/testing/test_validate_agent_smoke_result.py`.
- Create `tools/testing/fixtures/agent-smoke/valid-agent-autotune/**`.
- Update `Makefile` only if needed so `validate-agent-smoke-fixtures`
  explicitly validates the new fixture.
- Optionally update `test-results/agent-smoke/latest/**` only after a validated
  live run.
- Create `docs/testing/results/<date>-v0.4-e2e-agent-test-expansion.md` after
  commands run.
- Update this package's `review.md`.

## Files Explicitly Out Of Scope

- `backend/app/**` implementation files.
- `backend/app/tests/**` existing v0.4 backend tests unless a verification
  failure proves the test expectation is wrong and a separate package approves
  the repair.
- `frontend/src/**` product UI files.
- `backend/worldengine/**`.
- migrations, external repositories, concrete world fixtures, private oracle
  data.

## Ordered Steps

1. Run the missing E2E spec command to record the initial red state.
2. Add failing checker/fixture tests for `dashboard-agent-autotune`.
3. Run the checker tests and record the unsupported-scenario failure.
4. Implement `frontend/e2e/agent-loop.spec.ts`.
5. Strengthen `dashboard-agent-autotune` in `dashboard.spec.ts`.
6. Implement Agent smoke helper/checker support and valid fixture.
7. Add scenario docs and README index updates.
8. Run focused Playwright and checker tests.
9. Run `make validate-agent-smoke-fixtures`.
10. Run broad `make test-e2e`.
11. Execute and validate live `dashboard-agent-autotune` Agent smoke.
12. Record durable result summary and update `review.md`.
13. Use subagent/evaluator review before final status.

## Review Gates

- Documentation/contract evaluator before implementation starts.
- Implementation-scope evaluator before broad verification.
- Validation-evidence evaluator before claiming E2E or Agent smoke pass.
- Closeout consistency review before final assessment.

## Stop Conditions

- Package evaluator finds unresolved P1/P2 in contract/design/test-plan.
- New tests require product runtime or UI behavior changes.
- Agent smoke cannot validate without recording forbidden direct API
  operations.
- E2E cannot run because dependencies are missing and setup is not approved.
- Live smoke artifacts are incomplete or checker rejects them.

## Handoff After Plan Approval

After review approval, implementation should follow `worldengine-iteration-dev`
and keep changes limited to the allowed file set.
