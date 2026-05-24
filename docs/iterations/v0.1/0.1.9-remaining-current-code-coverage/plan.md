# Plan

## Files

Create:

- `docs/iterations/v0.1/0.1.9-remaining-current-code-coverage/README.md`
- `docs/iterations/v0.1/0.1.9-remaining-current-code-coverage/intent.md`
- `docs/iterations/v0.1/0.1.9-remaining-current-code-coverage/contract.md`
- `docs/iterations/v0.1/0.1.9-remaining-current-code-coverage/technical-design.md`
- `docs/iterations/v0.1/0.1.9-remaining-current-code-coverage/test-plan.md`
- `docs/iterations/v0.1/0.1.9-remaining-current-code-coverage/plan.md`
- `docs/iterations/v0.1/0.1.9-remaining-current-code-coverage/review.md`

Implementation may modify after review:

- `frontend/e2e/dashboard.spec.ts`
- `test-results/agent-smoke/latest/`
- `docs/testing/e2e-scenarios/README.md`
- `docs/testing/e2e-scenarios/dashboard-agent-autotune.md`
- `docs/testing/e2e-scenarios/dashboard-timeline-navigation.md`
- `docs/testing/agent-smoke/README.md`
- `docs/testing/agent-smoke/README.zh.md`
- `docs/testing/agent-smoke/scenarios/dashboard-invalid-param.md`
- `docs/testing/v0.1-test-map.md`
- `docs/testing/v0.1-test-map.zh.md`
- this package `review.md`
- v0.1 iteration indexes and plans for status synchronization.

Do not touch:

- `backend/app/`
- `backend/worldengine/`
- Agent smoke validator implementation.
- Agent smoke fixtures.
- Codex/test-runner autonomous runner or scorecards.
- v0.2 iteration packages.

## Steps

1. Complete this documentation package and get review approval for
   `contract.md`, `technical-design.md`, `test-plan.md`, and `plan.md`.
2. After approval, implement `dashboard-agent-autotune` E2E in
   `frontend/e2e/dashboard.spec.ts`.
3. Implement `dashboard-timeline-navigation` E2E in
   `frontend/e2e/dashboard.spec.ts`.
4. Run focused E2E checks for the two new scenarios.
5. Prepare `test-results/agent-smoke/latest/` for live
   `dashboard-invalid-param` evidence, replacing the 0.1.8 params-flow latest
   raw evidence only after the new run is complete.
6. Run helper `baseline` before invalid-param UI actions.
7. Record the helper `baseline` command in both `result.json.commands` and
   `operation-log.jsonl` as a `cli` operation with `exit_code: 0`.
8. Operate the dashboard UI for `dashboard-invalid-param`, recording UI
   targets, transcript, console, and screenshot evidence.
9. Run helper `collect --scenario dashboard-invalid-param`.
10. Record the helper `collect` command in both `result.json.commands` and
    `operation-log.jsonl` as a `cli` operation with `exit_code: 0`.
11. Write `result.json` with `verdict_source: deterministic_checker`.
12. Validate the run with `make validate-agent-smoke-result
    RESULT_DIR=test-results/agent-smoke/latest`.
13. Record the validator command in both `result.json.commands` and
    `operation-log.jsonl` as a `cli` operation with `exit_code: 0`.
14. If validation fails, stop and record the blocker in `review.md`.
15. If validation succeeds, update Agent smoke docs to
    `dashboard-invalid-param: live-smoke-recorded`.
16. Update E2E scenario docs and test maps to mark Auto-Tune and timeline
    navigation as implemented after `make test-e2e` passes.
17. Run the commands in `test-plan.md`.
18. Update `review.md` with actual changed files, commands, results,
    compatibility review, scope review, and unresolved findings.

## Verification

Required implementation verification:

```bash
git diff --check
find test-results/agent-smoke/latest -maxdepth 2 -type f | sort
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
make test-e2e
cd frontend && pnpm test -- WorldPanel.test.ts TimelinePanel.test.ts DashboardPage.test.ts
make check-backend
make check-frontend
if git diff --name-only | rg '^(backend/worldengine/|backend/app/)'; then
  echo "Unexpected backend runtime or legacy change"
  exit 1
fi
```

No implementation command should be run until this package is reviewed and
approved.
