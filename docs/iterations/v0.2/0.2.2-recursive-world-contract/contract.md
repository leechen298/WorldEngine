# Contract

## Public Concepts

- `EntityRef`: a lightweight reference or declaration for entities, agents,
  resources, rules, locations, and future memory links. It is not runtime
  entity state.
- `WorldCell`: the minimal recursive world unit. A cell may contain entity
  references and child cells.
- `WorldSpec`: the minimal top-level container for a generated or loadable
  recursive world. It is a schema container, not a loader or runtime bridge.

## Compatibility Constraints

- Existing runtime behavior must not change.
- Existing API response shapes must not change.
- Existing event schema behavior must not change.
- Existing frontend behavior must not change.
- Existing v0.1 tests must remain compatible.
- Schema additions must be additive and isolated to the allowed schema files.

## Allowed Changes

Implementation after this documentation gate is approved may only:

- Add `backend/app/schemas/entity.py`.
- Add `backend/app/schemas/world_cell.py`.
- Add `backend/app/tests/test_world_cell_schema.py`.

## Forbidden Changes

- Do not implement code in this documentation stage.
- Do not modify runtime services, modules, event storage, API routes, or app
  factory behavior.
- Do not modify `backend/app/schemas/event.py`.
- Do not modify `frontend/`.
- Do not modify `backend/worldengine/`.
- Do not add `backend/data/world_specs/historical concrete fixture path`.
- Do not implement a WorldSpec loader.
- Do not migrate `RuntimeEngine` to `WorldCell`.
- Do not implement concrete demo runtime.
- Do not implement world generation.
- Do not implement agent memory, agent inner-world, or pseudo-self continuity.
- Do not start 0.2.3.
- Do not modify the 0.2.1 package wording.

## Schema Contract

`EntityRef` must use the current backend Pydantic style and provide:

```python
id: str
kind: str
label: Optional[str] = None
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldCell` must provide:

```python
id: str
label: Optional[str] = None
kind: Literal["world"] = "world"
entity_refs: List[EntityRef] = Field(default_factory=list)
child_cells: List["WorldCell"] = Field(default_factory=list)
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`WorldSpec` must provide:

```python
schema_version: Literal["0.2"] = "0.2"
id: str
label: Optional[str] = None
root: WorldCell
metadata: Dict[str, Any] = Field(default_factory=dict)
```

`label` fields are optional display labels. They are not stable identifiers.
`id` is the stable identifier field for refs, cells, and specs.

## Validation Contract

- Required id-like fields must reject empty strings.
- `WorldCell.kind` must only accept `"world"`.
- `WorldSpec.schema_version` must only accept `"0.2"`.
- Nested `child_cells` must recursively validate as `WorldCell`.
- `entity_refs` must validate as `EntityRef`.
- Serialization must support `model_dump()`.
- Round-trip reconstruction must support `model_validate()` from a dumped
  nested `WorldSpec` dictionary.

This package must not validate unique ids, detect graph cycles, resolve
references, load files, or connect schemas to runtime execution.

## North Star Check

The contract defines the first structural bone for recursive worlds without
making the engine demo-specific. It creates schema language for future
generation, loading, runtime bridge, and projection work while keeping those
follow-ups out of this package.

## Out-of-Scope Follow-ups

- 0.2.3 Event Contract Extension.
- 0.2.4 WorldSpec Reference Fixture.
- v0.3 WorldSpec loader and runtime bridge.
- Agent memory and pseudo-self continuity.
- Reference concrete demo runtime and product surface.
