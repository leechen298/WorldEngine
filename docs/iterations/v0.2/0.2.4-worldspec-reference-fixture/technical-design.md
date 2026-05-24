# Technical Design

## Current State

The active backend path is `backend/app/`. 0.2.2 added:

- `backend/app/schemas/entity.py` with `EntityRef`.
- `backend/app/schemas/world_cell.py` with `WorldCell` and `WorldSpec`.
- `backend/app/tests/test_world_cell_schema.py` with focused schema tests.

`WorldSpec` currently validates a top-level `schema_version`, `id`, optional
`label`, `root: WorldCell`, and `metadata`. `WorldCell` validates recursive
`child_cells` and `entity_refs`. There is no checked-in reference WorldSpec
fixture yet.

## Contract Alignment and Invariants

- 0.2.4 adds data and tests only after review approval.
- The fixture must validate through the existing 0.2.2 schema models.
- Test-only JSON reading is allowed.
- Production loading behavior is not allowed.
- Existing schema files must remain unchanged.
- Runtime, event log, modules, API routes, frontend, and `backend/worldengine/`
  must remain unchanged.
- The fixture is not a runtime world and not a game-specific backend feature.

## Proposed Implementation

After review approval, add:

- `backend/data/world_specs/tiny_village.world.json`
- `backend/app/tests/test_worldspec_fixture.py`

The JSON fixture should be small and deterministic. It should include:

- `schema_version: "0.2"`
- `id: "tiny-village"`
- `label: "Tiny Village"`
- top-level metadata with `purpose: "reference-fixture"` and `version: "0.2"`
- a root `WorldCell` with `id: "root"`, `label: "Tiny Village Root"`, and
  `kind: "world"`
- at least one root `entity_ref`
- at least two nested child cells, such as `village-square` and `workshop`
- at least one nested child cell with an `entity_ref`
- fixture-specific metadata only

The test file should load the JSON directly:

```python
import json
from pathlib import Path

from app.schemas.world_cell import WorldCell, WorldSpec


FIXTURE_PATH = Path(__file__).resolve().parents[2] / "data" / "world_specs" / "tiny_village.world.json"


def load_fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text())
```

The implementation may choose an equivalent path expression if it remains
local to the test and does not become production loader logic.

## Affected Surfaces

- Fixture data: one JSON file under `backend/data/world_specs/`.
- Tests: one focused test file under `backend/app/tests/`.
- Schemas: not affected.
- Runtime engine / `RuntimeEngine`: not affected.
- Event log storage: not affected.
- Modules: not affected.
- API routes: not affected.
- Frontend: not affected.
- `backend/worldengine/`: not affected.

## Runtime / Service Design

No runtime or service design changes are included. The package must not add a
WorldSpec loader, runtime bridge, API route, app factory dependency,
projection integration, persistence/restart behavior, or village runtime.

## Compatibility

Compatibility is preserved because the fixture is additive data and the test
uses existing schema validation. Existing runtime behavior, event contract,
API behavior, frontend behavior, and legacy backend behavior remain
unchanged.

## Risks

- Risk: the fixture starts to encode runtime state rather than schema shape.
  Detection: review fixture fields for memory, inventory, behavior,
  schedules, self data, persistence, or runtime-only state.
- Risk: the test becomes a production loader. Detection: changed-file review
  must confirm no loader module, service API, CLI loader, runtime bridge, or
  dashboard integration was added.
- Risk: implementation modifies schemas to satisfy the fixture. Detection:
  changed-file scope checks must confirm `entity.py`, `world_cell.py`, and
  `event.py` were not modified.
- Risk: Tiny Village becomes game-specific backend logic. Detection: scope
  review must confirm no runtime, API, frontend, generator, or game-specific
  behavior was added.
