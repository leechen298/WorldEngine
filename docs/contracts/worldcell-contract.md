# WorldCell Contract

Status: v0.2 schema contract

## Purpose

`WorldCell` is the recursive world-unit schema for v0.2. It describes generic
world structure at the schema layer so future packages can build loaders and
runtime bridges from a stable contract. In v0.2, a `WorldCell` is not loaded
into runtime state and does not change tick, event, API, or frontend behavior.

## Schema

Source of truth: `backend/app/schemas/world_cell.py`.

Fields:

- `id`: required non-empty string. Identifies the cell within the containing
  specification or future public contract context.
- `label`: optional string. Provides human-readable review or display text and
  has no identity semantics.
- `kind`: literal string with value `"world"`. This reserves the recursive
  cell shape for world cells only in v0.2.
- `entity_refs`: list of `EntityRef` objects, default `[]`. References
  generic entities associated with the cell. v0.2 does not resolve these
  references.
- `child_cells`: list of nested `WorldCell` objects, default `[]`. Defines
  recursive child world structure at the schema layer.
- `metadata`: optional free-form object with default `{}`. Carries
  domain-neutral annotation data. v0.2 does not interpret metadata keys.

## Recursive Semantics

Child cells validate recursively using the same `WorldCell` contract. Each
child must have a non-empty `id`, literal `kind = "world"` when provided, and
valid nested entity references and child cells.

This recursive shape is structural only. It does not define runtime ownership,
timeline inheritance, parent-child tick order, event propagation, persistence
layout, projection behavior, or generation rules.

## Validation

`WorldCell` must reject:

- empty `id` values.
- any `kind` other than `"world"`.
- child cell payloads that do not validate as `WorldCell`.
- entity reference payloads that do not validate as `EntityRef`.

`WorldCell` must accept omitted `label`, `entity_refs`, `child_cells`, and
`metadata`. Omitted collections validate as empty lists or an empty object.

## Compatibility

The v0.2 contract is additive:

- Existing valid world-cell payloads remain valid.
- Existing invalid generic values remain invalid.
- New metadata keys or additional child cells may be added by producers
  without changing runtime behavior in v0.2.

Future packages may define loader or runtime semantics only through a reviewed
iteration contract. Until then, `WorldCell` remains a schema object.

## Non-Goals

`WorldCell` does not implement:

- WorldSpec loading.
- RuntimeEngine migration.
- runtime bridges or tick behavior.
- persistence migrations.
- projection APIs or frontend behavior.
- world generation.
- event routing or causality.
- agent loop, memory, or self-continuity behavior.
- concrete external-world fixtures, roles, locations, resources, story rules,
  or seed data.
