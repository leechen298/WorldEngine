# Test Plan

## Unit Tests

Add `backend/app/tests/test_world_cell_schema.py` with tests for:

- `EntityRef` construction with required `id` and `kind`, optional `label`,
  and default empty `metadata`.
- `WorldCell` construction with default `kind="world"`, default empty
  `entity_refs`, default empty `child_cells`, and optional `label`.
- Nested `WorldCell` construction through `child_cells`.
- `WorldSpec` construction with `schema_version="0.2"` and a `root`
  `WorldCell`.
- Invalid empty id-like fields for `EntityRef`, `WorldCell`, and `WorldSpec`.
- Invalid `WorldCell(kind="concrete demo")`.
- Invalid `WorldSpec(schema_version="0.3")`.
- Invalid child cell input that does not validate as `WorldCell`.
- Invalid entity ref input that does not validate as `EntityRef`.
- `model_dump()` serialization of a nested `WorldSpec`.
- `model_validate()` reconstruction from a dumped nested `WorldSpec`
  dictionary.
- Import smoke for `EntityRef`, `WorldCell`, and `WorldSpec`.

## Regression Tests

Existing backend tests must continue to pass because this package must not
change runtime behavior, API route behavior, event behavior, or frontend
behavior.

## Commands

Documentation-stage commands for this package:

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.2-recursive-world-contract -maxdepth 1 -type f | sort
rg -n "0.2.2-recursive-world-contract|ready for implementation|WorldCell|EntityRef|WorldSpec" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|concrete demo|migration|agent memory|pseudo-self" docs/iterations/v0.2/0.2.2-recursive-world-contract docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
```

Implementation-stage commands to run after this documentation gate is approved
and code is added:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
cd backend && .venv/bin/python - <<'PY'
from app.schemas.entity import EntityRef
from app.schemas.world_cell import WorldCell, WorldSpec
print(EntityRef, WorldCell, WorldSpec)
PY
```

## Acceptance Criteria

- The documentation gate changes only `docs/iterations/v0.2/`.
- The package directory contains the complete English seven-file set and
  complete `.zh.md` mirrors.
- v0.2 README and plan documents show 0.2.2 as `ready for implementation`.
- `review.md` and `review.zh.md` record documentation-stage evidence and state
  that implementation has not started.
- No backend, frontend, runtime, test implementation, fixture, or legacy
  backend file is changed during the documentation stage.
- Implementation may start only after this package is reviewed and approved.

## Not Run

Backend, frontend, runtime, E2E, UI smoke, Agent smoke, and implementation
tests are not run during the documentation stage because no code, runtime,
schema implementation, API, UI, fixture, or test implementation files change.
