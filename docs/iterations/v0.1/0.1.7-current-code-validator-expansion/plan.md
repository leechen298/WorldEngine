# Plan

## Files

- Create:
  - `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/README.md`
  - `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/intent.md`
  - `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/contract.md`
  - `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/technical-design.md`
  - `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/test-plan.md`
  - `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/plan.md`
  - `docs/iterations/v0.1/0.1.7-current-code-validator-expansion/review.md`
  - `tools/testing/agent_smoke_evidence.py`
  - Agent smoke valid fixtures for `dashboard-params-flow` and
    `dashboard-invalid-param`
- Modify:
  - `frontend/src/components/WorldPanel.vue`
  - `frontend/src/components/MemoryPanel.vue`
  - `frontend/src/components/TimelinePanel.vue`
  - relevant frontend component tests.
  - `tools/testing/validate_agent_smoke_result.py`
  - `tools/testing/test_validate_agent_smoke_result.py`
  - `docs/testing/agent-smoke/result-schema.json`
  - Agent smoke scenario docs and high-level test indexes after validation
    support is proven.
- Do not touch:
  - `backend/worldengine/`
  - backend runtime or API implementation.
  - `frontend/e2e/dashboard.spec.ts`, except if implementation discovers that
    E2E regression requires selector-only test adjustments. Do not add new
    archive-summary E2E in 0.1.7.
  - `test-results/agent-smoke/latest/`

## Steps

1. Read the approved 0.1.7 package documents in order:
   `intent.md`, `contract.md`, `technical-design.md`, `test-plan.md`,
   `plan.md`, and `review.md`.
2. Add failing frontend selector tests for WorldPanel, MemoryPanel, and
   TimelinePanel.
3. Add failing validator tests for the two new valid fixtures and the required
   negative cases.
4. Add the missing dashboard selectors only.
5. Add `agent_smoke_evidence.py` with `baseline` and `collect` commands.
6. Extend the validator scenario table, UI target checks, and
   scenario-specific API summary checks.
7. Update `result-schema.json` from one supported scenario to three.
8. Add valid fixture directories for `dashboard-params-flow` and
   `dashboard-invalid-param`.
9. Update Agent smoke scenario docs and indexes to
   `validator-supported / no live run recorded` only after tests pass.
10. Run every command in `test-plan.md`.
11. Update `review.md` with actual changed files, commands, results,
    compatibility review, scope review, unresolved findings, and final
    assessment.

## Verification

Required verification commands are defined in `test-plan.md`.

No live Agent smoke is part of this plan. A future 0.1.8 package must write and
review its own documents before generating live evidence.
