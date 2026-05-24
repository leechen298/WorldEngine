# Technical Design

## Current State

The active backend path is `backend/app/`. Existing shared schemas in
`backend/app/schemas/` use Pydantic `BaseModel` and `Field` with small,
focused models. `backend/worldengine/` is legacy and is not an active runtime
path for this package.

There is currently no `EntityRef`, `WorldCell`, or `WorldSpec` schema. v0.1
runtime services, modules, event storage, and API routes do not consume
recursive world schema data.

## Contract Alignment and Invariants

- The implementation must add schemas without wiring them into runtime.
- The implementation must not change existing API response shapes.
- The implementation must not change current event behavior.
- The implementation must not add loaders, fixtures, generators, or dashboard
  changes.
- `EntityRef`, `WorldCell`, and `WorldSpec` must remain schema-level concepts.

## Proposed Implementation

Add `backend/app/schemas/entity.py` with `EntityRef`.

Add `backend/app/schemas/world_cell.py` with `WorldCell` and `WorldSpec`.
Use Pydantic v2-compatible models and local imports. Use forward references
for recursive child cells if required by the implementation.

Add `backend/app/tests/test_world_cell_schema.py` with focused schema tests.
Tests should construct models directly and avoid app factory, HTTP routes,
runtime stepping, fixtures, or external services.

## Affected Surfaces

- Schemas: new `EntityRef`, `WorldCell`, and `WorldSpec`.
- Tests: new focused schema test file.
- Runtime services: not affected.
- API routes: not affected.
- Events: not affected.
- Frontend: not affected.
- Fixtures: not affected.
- Legacy backend: not affected.

## Data Model / Schema Changes

`EntityRef` fields:

```python
id: str
kind: str
label: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldCell` fields:

```python
id: str
label: Optional[str] = None
kind: Literal["world"] = "world"
entity_refs: List[EntityRef] = Field(default_factory=list)
child_cells: List["WorldCell"] = Field(default_factory=list)
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldSpec` fields:

```python
schema_version: Literal["0.2"] = "0.2"
id: str
label: Optional[str] = None
root: WorldCell
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`label` is optional on all three schema concepts. `id` is required and stable.
`kind` on `WorldCell` and `schema_version` on `WorldSpec` are literals so tests
can enforce the contract.

## Runtime / Service Design

No runtime or service design changes are included. The schemas are inert until
later packages connect WorldSpec data to fixtures, loaders, event contracts, or
runtime bridges.

## Compatibility

Existing data remains valid because no current persistence format is changed.
Existing API clients remain compatible because no route response changes. v0.1
runtime behavior remains compatible because the new schemas are not imported
into runtime flow.

## Risks

- Risk: schema additions accidentally become runtime migration. Detection:
  changed-file scope check and regression test command.
- Risk: literals are documented but not enforced. Detection: invalid `kind`
  and invalid `schema_version` tests.
- Risk: recursive child cells fail to validate or serialize. Detection: nested
  construction and `model_dump()` / `model_validate()` round-trip tests.
- Risk: future 0.2.4 fixture lacks a top-level container. Detection: `WorldSpec`
  is included in this package contract.
