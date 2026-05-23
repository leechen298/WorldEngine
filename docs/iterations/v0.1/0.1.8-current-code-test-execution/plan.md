# Plan

## Files

Create:

- `docs/iterations/v0.1/0.1.8-current-code-test-execution/README.md`
- `docs/iterations/v0.1/0.1.8-current-code-test-execution/intent.md`
- `docs/iterations/v0.1/0.1.8-current-code-test-execution/contract.md`
- `docs/iterations/v0.1/0.1.8-current-code-test-execution/technical-design.md`
- `docs/iterations/v0.1/0.1.8-current-code-test-execution/test-plan.md`
- `docs/iterations/v0.1/0.1.8-current-code-test-execution/plan.md`
- `docs/iterations/v0.1/0.1.8-current-code-test-execution/review.md`

Implementation may modify after review:

- `test-results/agent-smoke/latest/`
- `frontend/playwright.config.ts`
- `frontend/e2e/dashboard.spec.ts`
- `docs/testing/agent-smoke/README.md`
- `docs/testing/agent-smoke/README.zh.md`
- `docs/testing/agent-smoke/scenarios/dashboard-params-flow.md`
- `docs/testing/e2e-scenarios/README.md`
- `docs/testing/e2e-scenarios/dashboard-archive-summary.md`
- `docs/testing/v0.1-test-map.md`
- `docs/testing/v0.1-test-map.zh.md`
- this package `review.md`
- v0.1 iteration indexes and plans for status synchronization.

Do not touch:

- `backend/app/`
- `backend/worldengine/`
- Agent smoke validator implementation.
- Agent smoke fixtures unless an approved review correction explicitly
  requires it.
- `dashboard-invalid-param` live evidence.
- Codex/test-runner autonomous runner or scorecards.

## Steps

1. Complete this documentation package and get review approval for
   `contract.md`, `technical-design.md`, `test-plan.md`, and `plan.md`.
2. After approval, start 0.1.8-A by preparing
   `test-results/agent-smoke/latest/`.
3. Start backend and frontend services.
4. Run the evidence helper `baseline` command before UI actions.
5. Operate the dashboard UI for `dashboard-params-flow`, recording
   `operation-log.jsonl`, `transcript.md`, `console.log`, and screenshot
   evidence.
6. Run the evidence helper `collect --scenario dashboard-params-flow`.
7. Write `result.json` with `verdict_source: deterministic_checker`.
8. Validate the run with `make validate-agent-smoke-result
   RESULT_DIR=test-results/agent-smoke/latest`.
9. If validation fails, stop and record the blocker in `review.md`; do not
   start 0.1.8-B.
10. If validation succeeds, update Agent smoke docs to
    `dashboard-params-flow: live-smoke-recorded`.
11. Implement 0.1.8-B by adding low archive interval env vars to the
    Playwright backend web server only.
12. Add `dashboard-archive-summary` to `frontend/e2e/dashboard.spec.ts`.
13. Run the commands in `test-plan.md`.
14. If E2E passes, update E2E docs and test maps to mark
    `dashboard-archive-summary` as implemented.
15. Update `review.md` with actual changed files, commands, results,
    compatibility review, scope review, and unresolved findings.

## Verification

Required implementation verification:

```bash
git diff --check
find test-results/agent-smoke/latest -maxdepth 2 -type f | sort
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
make test-e2e
cd frontend && pnpm test -- DashboardPage.test.ts MemoryPanel.test.ts
if git diff --name-only | rg '^(backend/worldengine/|backend/app/)'; then
  echo "Unexpected backend runtime or legacy change"
  exit 1
fi
```

No implementation command should be run until this package is reviewed and
approved.
