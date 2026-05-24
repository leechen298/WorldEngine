# Test Plan

## Unit Tests

After this documentation gate is reviewed and approved, add
`backend/app/tests/test_worldspec_fixture.py` with tests for:

- fixture file exists at `backend/data/world_specs/tiny_village.world.json`.
- JSON parses successfully using Python standard library `json` and `pathlib`.
- `WorldSpec.model_validate(fixture_dict)` succeeds.
- `spec.schema_version == "0.2"`.
- `spec.root` is a `WorldCell`.
- `spec.root.kind == "world"`.
- `spec.root.child_cells` has at least one child cell.
- `spec.root.entity_refs` has at least one entity ref.
- nested `child_cells` validate recursively.
- `entity_refs` validate as `EntityRef` through `WorldCell` / `WorldSpec`
  validation.
- `model_dump()` / `model_validate()` round-trip works for the fixture.
- import smoke for `WorldSpec`, `WorldCell`, and `EntityRef`.

## Regression Tests

Existing backend tests must continue to pass because this package must not
change runtime behavior, schema implementation behavior, event log storage,
modules, API routes, frontend behavior, or `backend/worldengine/`.

## Commands

Documentation-stage commands for this package:

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.4-worldspec-reference-fixture -maxdepth 1 -type f | sort
rg -n "0.2.4-worldspec-reference-fixture|review complete|WorldSpec|tiny_village|reference fixture|model_validate|WorldCell|EntityRef|schema_version" docs/iterations/v0.2/0.2.4-worldspec-reference-fixture docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "WorldSpec loader|runtime bridge|RuntimeEngine|backend/worldengine|village runtime|game-specific|world generation|agent memory|pseudo-self|frontend|API route|event log" docs/iterations/v0.2/0.2.4-worldspec-reference-fixture docs/iterations/v0.2/v0.2-plan.md
rg -n '^Status: (implementation complete|review complete)$' docs/iterations/v0.2/0.2.4-worldspec-reference-fixture
rg -n '^\| `0\.2\.4-worldspec-reference-fixture` \| code \| (implementation complete|review complete) \|' docs/iterations/v0.2/README.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'
```

Implementation-stage commands to document but not run until code is added
after review approval:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_fixture.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
cd backend && .venv/bin/python - <<'PY'
import json
from pathlib import Path
from app.schemas.world_cell import WorldSpec

path = Path("data/world_specs/tiny_village.world.json")
spec = WorldSpec.model_validate(json.loads(path.read_text()))
print(spec.id, spec.schema_version, spec.root.id)
PY
```

## Acceptance Criteria

- The documentation gate changes only `docs/iterations/v0.2/`.
- The package directory contains the complete English seven-file set and
  complete `.zh.md` mirrors.
- v0.2 README and plan documents show 0.2.4 as `review complete`.
- 0.2.4 implementation, tests/evidence, and review closeout are complete.
- `review.md` and `review.zh.md` record documentation-stage evidence and
  state that implementation has not started.
- No backend, frontend, runtime, schema implementation, API, UI, fixture,
  loader, generator, or test implementation file is changed during the
  documentation stage.
- Implementation may start only after this package is reviewed and approved.

## Not Run

Backend, frontend, runtime, E2E, UI smoke, Agent smoke, and implementation
tests are not run during the documentation stage because no code, runtime,
schema implementation, API, UI, fixture, loader, generator, or test
implementation files change.
