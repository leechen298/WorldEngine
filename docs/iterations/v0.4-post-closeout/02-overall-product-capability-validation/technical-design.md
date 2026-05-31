# Technical Design

## Product Capability Matrix

Add `product-capability-test-matrix.md` in this package. It records current
capability coverage and gaps across:

- core user paths.
- API/backend behavior.
- frontend page interactions.
- data state, events, persistence, and logs.
- invalid inputs, permission/boundary, and failure paths.
- Agent UI/CLI/smoke/autonomous operation.
- existing test coverage and missing coverage.

## E2E Expansion

Extend `frontend/e2e/agent-loop.spec.ts` with additive tests for behavior that
already exists in backend/API coverage:

- `noop` with patches returns rejected result without mutation or event.
- empty `params.patch` returns rejected result without mutation or event.
- dry-run rejected patch returns metrics without mutation or event.
- `event_limit=0` and `event_limit=201` keep the 422 envelope and do not
  mutate params.
- multi-patch and remove flow validates state and event evidence.

Each case must cross-check `/world/params` and recent `params.applied` events.

## Autonomous Checker

Create `tools/testing/validate_agent_autonomous_result.py` with deterministic
artifact validation. The checker reads a result directory and validates:

- `result.json` required keys and status.
- allowed `verdict_source`.
- score items all pass and include evidence.
- no unresolved P1 item.
- required artifacts exist, are relative, and are non-empty.
- `operation-log.jsonl` contains only `ui` and `cli`, with integer `seq` and
  CLI `exit_code=0`.
- scenario-specific UI targets are present for supported scenarios.
- `scorecard-summary.json` matches the scenario and reports pass.

Add fixtures and tests in `tools/testing/fixtures/agent-autonomous/**` and
`tools/testing/test_validate_agent_autonomous_result.py`.

## Documentation Sync

Update testing docs so the latest Agent smoke and E2E/autonomous states agree
with current files:

- latest Agent smoke points to `dashboard-agent-autotune`.
- `agent-loop-step` is included in implemented E2E coverage.
- autonomous checker is now minimal executable support, not broad full-suite
  proof.

## Known Blocker Recording

`cd frontend && pnpm build` is part of validation and is expected to fail until
a later repair package fixes TypeScript errors. This package records the P1
and does not change `frontend/src/**` to repair it.
