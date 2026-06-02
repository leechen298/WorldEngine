# E2E Scenario: agent-loop-step

Status: implemented

## Purpose

Verify the v0.4 Agent Loop API under the Playwright E2E harness. The current
dashboard has no UI for `POST /world/agent/loop/step`, so this scenario uses
Playwright request assertions against the public API while the normal E2E
backend server is running.

## Coverage

Implemented in `frontend/e2e/agent-loop.spec.ts`.

The scenario covers:

- default loop step returns deterministic `noop`, bounded perception, and no
  params mutation.
- valid `params.patch` returns accepted result, updates world params, and emits
  `params.applied` with `source="agent.loop"`.
- unsupported action returns HTTP 200 with rejected `ActionResult` and no
  mutation.
- strict request and nested patch schemas return the existing 422 API envelope
  with `code=30` and no mutation.
- `noop` with unexpected patches returns rejected result and no mutation.
- empty `params.patch` returns rejected result and no mutation.
- dry-run rejected patches return metrics and no mutation.
- `event_limit` lower and upper boundary errors keep the existing 422 envelope.
- multi-patch and remove operations update params and event evidence
  consistently.

## Verdict Source

PASS comes only from Playwright assertion exit status:

```bash
cd frontend && pnpm exec playwright test e2e/agent-loop.spec.ts
```

This scenario is not Agent smoke and is not scorecard-based autonomous
validation.

## Failure-Path Assertions

- Noop mutating params or emitting a new applied event is a no-mutation failure.
- Accepted patch without params mutation or `source="agent.loop"` event evidence
  is an Agent Loop event failure.
- Rejected action, empty patch, noop-with-patch, dry-run duplicate, unsupported
  action, or schema-invalid request mutating params is a failure.
- HTTP 422 cases must preserve the existing API envelope `code=30`.

## Artifact Expectations

- HTML report: `test-results/e2e/html-report/index.html`
- Playwright artifacts: `test-results/e2e/artifacts/`
- Failure screenshot and trace are retained under the artifact directory when
  Playwright keeps them.
