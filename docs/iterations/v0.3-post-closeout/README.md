# v0.3 Post-Closeout Validation Campaign

Status: campaign executed / passed with P3
Type: post-closeout validation goal campaign

## Goal

Execute the documentation-controlled independent v0.3 post-closeout validation
campaign. This campaign focuses on the WorldSpec loader, runtime context
bridge, API/runtime compatibility, browser E2E readiness, and Codex autonomous
validation after v0.3 final closeout.

v0.3 feature / documentation closeout is complete.
v0.3 independent E2E / integration validation has current-session evidence in
this campaign.
v0.3 Codex autonomous validation has current-session review evidence in this
campaign.
This campaign does not reopen v0.3 implementation.
This campaign does not change v0.3 release status.
This pass updates validation campaign documents with execution evidence.

## Goal Entry

Natural-language goal:

```text
完成 v0.3-post-closeout
```

Interpretation:

Use this package as Codex App `/goal` campaign guidance. Start from
`CURRENT_STATE.md`, follow `GOAL_RUNNER.md`, and advance through
`CAMPAIGN_PLAN.md` only when each child package has the required evidence or a
recorded blocker.

This is not WorldEngine runtime behavior. It is not an external automation
controller implementation. It only defines repository-local validation
documents, routing, stop conditions, and evidence requirements.

## Boundary

Allowed:

- Define post-closeout validation workflow.
- Define E2E / integration / API smoke planning.
- Fill validation execution reports with current-session evidence.
- Fill Codex autonomous validation reviews with direct source/evidence review.
- Fill final validation bundle documents from current evidence.
- Preserve v0.3 final / closeout complete status while making missing fresh
  validation explicit when not run.

Forbidden:

- Do not run or claim checks outside the approved validation campaign scope.
- Do not modify runtime, schema, API, frontend, backend tests, fixtures, or
  external repositories.
- Do not add concrete demo-world names, characters, locations, resources,
  story rules, seed data, UI selectors, or private oracle details.
- Do not write validation plans as validation results.
- Do not change v0.3 release status.

## Required Reading For Future Execution

- `README.md`
- `docs/releases/v0.3.md`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/evidence-index.md`
- `docs/iterations/v0.3/compatibility-audit.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.md`
- `docs/scope-boundaries.md`
- `docs/external-fixture-boundary.md`
- `docs/validation-report-template.md`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/event.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`
- `backend/app/tests/test_event_api_compat.py`
- `backend/app/tests/test_event_schema_compat.py`

If any required file is missing in a future execution run, record that in the
active package `review.md` and stop or downgrade according to
`validation-master-plan.md`.

## Validation Chain

0. Master validation planning.
1. E2E / integration / API smoke validation plan.
2. E2E / integration / API smoke execution template.
3. Codex autonomous validation plan.
4. Codex autonomous validation execution and review template.
5. Final validation bundle template.

## Package Index

| Package | Type | Initial status | Purpose |
|---|---|---|---|
| `01-e2e-validation-plan` | validation-planning | review complete | Defined E2E, integration, API smoke, loader, bridge, compatibility, and release-claim validation scope. |
| `02-e2e-validation-execution` | validation-execution | passed | Ran backend, focused loader/bridge/Event/runtime checks, API smoke coverage, and browser E2E. |
| `03-codex-autonomous-validation-plan` | validation-planning | review complete | Defined independent Codex reviewer inputs, constraints, and required checks. |
| `04-codex-autonomous-validation-execution` | autonomous-review | passed with P3 | Completed direct source/evidence review with non-blocking P3 handoffs. |
| `05-final-validation-bundle` | validation-bundle | passed with P3 | Synthesized current campaign evidence, P3 handoffs, and v0.4 proceed status. |

## Final Assessment State

Final assessment: passed with P3.

The campaign has current-session backend, API smoke, E2E, loader, bridge,
Event.refs, and Codex autonomous review evidence. It carries non-blocking P3
handoffs. v0.4 may proceed only through its own reviewed iteration package.
