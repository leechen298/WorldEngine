# Contract

## Public Concepts

- v0.4 Agent Loop E2E: Playwright coverage that runs through the E2E harness
  and calls the public `POST /world/agent/loop/step` API via Playwright
  request assertions because no dashboard UI exists for this endpoint.
- Agent smoke scenario: an Agent-operated UI/CLI validation case whose PASS
  verdict comes from `make validate-agent-smoke-result`, not from Codex
  natural-language judgment.
- Deterministic checker evidence: API-derived evidence written to
  `api-summary.json` by the documented helper, separate from UI/CLI operation
  records.

## Allowed Changes

This package may modify or create only these surfaces:

- `frontend/e2e/agent-loop.spec.ts`
- `frontend/e2e/dashboard.spec.ts`
- `docs/testing/e2e-scenarios/agent-loop-step.md`
- `docs/testing/e2e-scenarios/README.md`
- `docs/testing/agent-smoke/README.md`
- `docs/testing/agent-smoke/README.zh.md`
- `docs/testing/agent-smoke/scenarios/dashboard-agent-autotune.md`
- `docs/testing/agent-smoke/result-schema.json`
- `tools/testing/agent_smoke_evidence.py`
- `tools/testing/validate_agent_smoke_result.py`
- `tools/testing/test_validate_agent_smoke_result.py`
- `tools/testing/fixtures/agent-smoke/valid-agent-autotune/**`
- `Makefile` only to ensure `validate-agent-smoke-fixtures` explicitly
  validates the new fixture.
- `test-results/agent-smoke/latest/**` only if a validated live run is
  intentionally mirrored for review.
- `docs/testing/results/*.md` for durable run summaries.
- this package's `review.md`.

## Forbidden Changes

- Do not modify runtime behavior, schema behavior, API implementation,
  frontend product components, backend implementation, migrations, fixtures
  outside the allowed Agent smoke fixture, external repositories, or
  `backend/worldengine/`.
- Do not add concrete world names, maps, characters, locations, resources,
  story rules, seed data, or private oracle details.
- Do not claim broader Codex autonomous PASS unless a scorecard checker exists
  and returns PASS. This package does not implement that broader checker.
- Do not record direct API calls as Agent operations in `operation-log.jsonl`.
  API state may be checker/helper evidence in `api-summary.json`.
- Do not update v0.4 final release status.

## Compatibility Constraints

- Existing E2E scenarios in `frontend/e2e/dashboard.spec.ts` must continue to
  pass.
- The dashboard Auto-Tune flow must remain the existing params-agent route
  behavior and must not be reinterpreted as `agent.loop`.
- Existing Agent smoke scenarios must continue to validate:
  `dashboard-basic-runtime`, `dashboard-params-flow`, and
  `dashboard-invalid-param`.
- Existing backend/API compatibility evidence for v0.4 must remain valid.
- New tests must be additive and must not depend on shared state left by
  another test unless the spec explicitly controls ordering.

## North Star Check

This package improves validation for generic runtime, params, event, and
Agent-in-World boundaries. It does not turn WorldEngine into a concrete
application backend or introduce demo-world content.

## Out-of-Scope Follow-ups

- Dashboard UI for the v0.4 Agent Loop endpoint.
- Scorecard-based broader Codex/test-runner autonomous suite.
- v0.5 memory/self-continuity tests.
- External validation runner readiness.
