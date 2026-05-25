# Contract

## Public Concepts

- Reference WorldSpec fixture: a small deterministic JSON document that
  demonstrates a valid `WorldSpec` shape.
- historical concrete fixture: the first named reference fixture for the recursive
  world schema language.
- Fixture validation test: a focused test that reads the JSON fixture and
  validates it through `WorldSpec.model_validate(...)`.

The fixture is a reference data fixture, not a runtime world, not a generated
world, and not an application-specific backend.

## Allowed Changes

After this documentation gate is reviewed and approved, implementation may
only:

- Add `backend/data/world_specs/historical concrete fixture path`.
- Add `backend/app/tests/test_worldspec_fixture.py`.
- Update this package's `review.md` and `review.zh.md` during closeout.

## Forbidden Changes

- Do not implement code in this documentation stage.
- Do not create `backend/data/world_specs/historical concrete fixture path` yet.
- Do not create `backend/app/tests/test_worldspec_fixture.py` yet.
- Do not modify `backend/app/schemas/entity.py`.
- Do not modify `backend/app/schemas/world_cell.py`.
- Do not modify `backend/app/schemas/event.py`.
- Do not modify runtime engine behavior or `RuntimeEngine`.
- Do not modify event log storage.
- Do not modify modules.
- Do not modify API routes.
- Do not modify frontend.
- Do not modify `backend/worldengine/`.
- Do not implement a WorldSpec loader.
- Do not implement a runtime bridge.
- Do not implement concrete demo runtime.
- Do not implement application-specific backend logic.
- Do not implement world generation.
- Do not implement agent memory, pseudo-self, or agent behavior loops.
- Do not add persistence/restart logic.
- Do not start 0.2.5.

## Fixture Contract

The fixture must use the 0.2.2 `WorldSpec` schema.

Recommended shape:

```json
{
  "schema_version": "0.2",
  "id": "historical-concrete-fixture",
  "label": "historical concrete fixture",
  "metadata": {
    "purpose": "reference-fixture",
    "version": "0.2"
  },
  "root": {
    "id": "root",
    "label": "historical concrete fixture root",
    "kind": "world",
    "entity_refs": [
      {
        "id": "historical child cell",
        "kind": "location",
        "label": "Historical Child Cell"
      }
    ],
    "child_cells": [
      {
        "id": "historical child cell",
        "label": "Historical Child Cell",
        "kind": "world",
        "entity_refs": [
          {
            "id": "historical-nested-entity",
            "kind": "resource",
            "label": "Historical Entity"
          }
        ],
        "child_cells": [],
        "metadata": {
          "fixture_role": "public-location"
        }
      },
      {
        "id": "historical-child-cell",
        "label": "Historical Child Cell",
        "kind": "world",
        "entity_refs": [],
        "child_cells": [],
        "metadata": {
          "fixture_role": "work-location"
        }
      }
    ],
    "metadata": {
      "fixture_role": "root"
    }
  }
}
```

The exact implementation may adjust labels or metadata, but it must preserve
these constraints:

- `schema_version` is `"0.2"`.
- `id` is `"historical-concrete-fixture"`.
- `label` is `"historical concrete fixture"`.
- `metadata.purpose` is `"reference-fixture"`.
- `metadata.version` is `"0.2"`.
- `root.id` is `"root"`.
- `root.label` is `"historical concrete fixture root"`.
- `root.kind` is `"world"`.
- `root.entity_refs` has at least one `EntityRef`-like entry.
- `root.child_cells` has at least two nested `WorldCell` examples, including
  examples such as `historical child cell` and `historical-child-cell`.
- At least one child cell may contain an `entity_ref`.
- Metadata is fixture-specific only.

## EntityRef Usage

Fixture entries in `entity_refs` must use `EntityRef`-like dictionaries:

```json
{
  "id": "historical-nested-entity",
  "kind": "resource",
  "label": "Historical Entity",
  "metadata": {
    "fixture_role": "example-resource"
  }
}
```

Entity kinds remain strings such as `location`, `agent`, `resource`, `rule`,
or `building`. The fixture must not define runtime entity state, memory,
inventory, behavior, schedules, agent self data, or any reference resolution
semantics.

## Test Contract

The implementation-stage test must directly read the JSON fixture using the
Python standard library `json` and `pathlib`, then validate the parsed
dictionary with `WorldSpec.model_validate(...)`.

Test-only JSON reading is allowed. A production WorldSpec loader is forbidden
in this package.

Implementation-stage tests must verify:

- fixture file exists at `backend/data/world_specs/historical concrete fixture path`.
- JSON parses successfully.
- `WorldSpec.model_validate(fixture_dict)` succeeds.
- `schema_version` is `"0.2"`.
- `root` is a `WorldCell` with `kind == "world"`.
- `root` has at least one child cell.
- `root` has at least one entity ref.
- nested `child_cells` validate recursively.
- `entity_refs` validate as `EntityRef` through `WorldCell` / `WorldSpec`
  validation.
- `model_dump()` / `model_validate()` round-trip works for the fixture.
- the fixture does not require runtime engine, app factory, API route, or
  frontend.

## Compatibility Constraints

This package must not change existing schema behavior. It uses the existing
0.2.2 models as validation targets and does not extend `EntityRef`,
`WorldCell`, `WorldSpec`, or `Event`.

The JSON file is additive fixture data. It must not change runtime behavior,
event log storage, module behavior, API response shape, frontend behavior, or
legacy `backend/worldengine/` behavior.

## North Star Check

The fixture gives recursive world work a concrete schema example while keeping
WorldEngine aligned with its engine north star. It supports future generation,
loading, runtime bridge, projection, and agent work without implementing those
systems in 0.2.4.

## Out-of-Scope Follow-ups

- v0.3 WorldSpec loader and runtime bridge.
- Runtime reference resolution and referential integrity.
- Concrete demo runtime and product surface.
- Full world generation.
- Agent memory, pseudo-self, or agent behavior loops.
- 0.2.5 legacy boundary cleanup.
