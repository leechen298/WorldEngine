# Technical Design

## Documentation Structure

This package adds a concrete child package under:

```text
docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/
```

The package includes the standard seven English documents and matching Chinese
mirrors. The package is documentation-only but still includes
`technical-design.md` and `test-plan.md` because it changes goal routing,
status semantics, evidence rules, and mirror obligations.

## Affected Files

Allowed child package files:

- `README.md` and `README.zh.md`
- `intent.md` and `intent.zh.md`
- `contract.md` and `contract.zh.md`
- `technical-design.md` and `technical-design.zh.md`
- `test-plan.md` and `test-plan.zh.md`
- `plan.md` and `plan.zh.md`
- `review.md` and `review.zh.md`

Allowed parent status files:

- `docs/iterations/v0.8/README.md`
- `docs/iterations/v0.8/README.zh.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/v0.8-plan.zh.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/CURRENT_STATE.zh.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.8/review.md`
- `docs/iterations/v0.8/review.zh.md`

No runtime, schema, API, frontend, backend test, checker implementation,
fixture, migration, generated result, external repository, or legacy
implementation files are affected.

## Control Flow

1. User starts `/goal` development for v0.8.
2. Agent reads parent `CURRENT_STATE.md`, `GOAL_RUNNER.md`,
   `CAMPAIGN_PLAN.md`, `v0.8-plan.md`, and `review.md`.
3. Agent confirms no active child exists and parent route is documentation
   review.
4. Agent verifies current v0.7 handoff state from `docs/iterations/v0.7/`.
5. Agent creates this package, updates parent status to route to `0.8.1`, and
   records documentation-only evidence.
6. Future work starts `0.8.1` by creating or confirming that child's full
   package document set.

## Compatibility Strategy

- Treat `0.7.9` checker/docs clean pass as handoff evidence only.
- Preserve v0.8 non-claims for runtime/API/frontend/E2E/Agent/autonomous,
  external validation, external consumer, product readiness, and minimum
  working-state readiness.
- Keep planned package entries as route-map specs until each child package is
  created and reviewed.
- Keep implementation authorization closed.

## Anti-Drift Rules

- Parent and child status surfaces must agree on `0.8.0` as review complete
  and `0.8.1` as selected / child docs not created.
- English and Chinese mirrors must preserve status, authorization, scope,
  forbidden changes, findings, and final assessment semantics.
- Current v0.7 checker/docs clean pass must not be converted into v0.8 PASS
  evidence.
- No external validator implementation or concrete external application detail
  may be introduced.
