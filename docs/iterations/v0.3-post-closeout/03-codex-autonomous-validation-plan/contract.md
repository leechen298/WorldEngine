# Contract

## Public Concepts

- Independent reviewer: a Codex reviewer that reads the source inputs directly
  and does not depend on the implementer's summary.
- Unsupported claim: a release, compatibility, loader, bridge, API, runtime,
  or Event.refs statement that lacks current evidence or contradicts code.
- Autonomous recommendation: the final reviewer outcome recorded in `04`.

## Reviewer Inputs

The independent reviewer must read:

- `README.md`
- `docs/releases/v0.3.md`
- `docs/iterations/v0.3/evidence-index.md`
- `docs/iterations/v0.3/compatibility-audit.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.md`
- `docs/scope-boundaries.md`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/event.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`
- `backend/app/tests/test_event_api_compat.py`
- `backend/app/tests/test_event_schema_compat.py`

## Allowed Changes

- Create and update planning docs in this package.
- Define autonomous reviewer inputs and checks.
- Define commands the reviewer should run or block.
- Define the report shape for `04`.

## Forbidden Changes

- Do not execute the autonomous review in this package.
- Do not modify code or tests.
- Do not modify runtime, schema, API, frontend, fixtures, migrations, or
  external repositories.
- Do not add concrete demo-world details or private oracle details.
- Do not mark autonomous validation as successful.
- Do not change v0.3 release status.

## Compatibility Requirements

The future review must explicitly check:

- WorldSpec loader claim.
- runtime context bridge claim.
- RuntimeEngine compatibility.
- Event.refs response compatibility.
- API / schema / runtime compatibility.
- absence of concrete demo-world regression.

## Out-Of-Scope Follow-Ups

Autonomous validation execution belongs to `04`. Repairs belong to a separate
reviewed package.
