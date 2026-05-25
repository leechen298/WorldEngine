# Contract

## Public Concepts

This package introduces or stabilizes these documentation-level concepts:

- North Star.
- recursive world generation and runtime.
- agent-in-world continuity.
- pseudo-self as an engineered continuity model.
- product surface as projection, not engine goal.
- version/package documentation workflow.
- review evidence requirement.

## Compatibility Constraints

- No backend runtime behavior may change.
- No frontend behavior may change.
- No API schema may change.
- No tests or runtime fixtures may change.
- Existing `docs/v1-design.md` remains in place.
- v0.2 is planned, not implemented and not released.

## Allowed Changes

- Add `AGENTS.md`.
- Add documentation under `docs/`.
- Add iteration templates under `docs/iterations/templates/`.
- Add v0.2 planning documents under `docs/iterations/v0.2/`.
- Add release entry documents under `docs/releases/`.
- Add testing documentation under `docs/testing/`.

## Forbidden Changes

- Do not modify `backend/`.
- Do not modify `frontend/`.
- Do not add `backend/app/schemas/entity.py`.
- Do not add `backend/app/schemas/world_cell.py`.
- Do not modify `backend/app/schemas/event.py`.
- Do not add `backend/data/world_specs/historical concrete fixture path`.
- Do not create an application repository or application runtime.
- Do not mark v0.2 as released.

## North Star Check

This package explicitly prevents the concrete demo surface from replacing the
engine goal. It defines future product surfaces as projections over recursive world
runtime, not as the core product model.

## Out-of-Scope Follow-ups

- 0.2.2 Recursive World Contract.
- 0.2.3 Event Contract Extension.
- 0.2.4 WorldSpec Reference Fixture.
- 0.2.5 Legacy Boundary Cleanup.
- 0.2.6 iteration workflow and plan reset.
