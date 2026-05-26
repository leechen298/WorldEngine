# WorldSpec Contract

Status: v0.2 schema contract

## Purpose

`WorldSpec` is the versioned recursive world specification schema for v0.2. It
wraps a required root `WorldCell` with schema-version and specification-level
identity metadata. It is a validated specification object, not a runtime
loader interface in this milestone.

## Schema

Source of truth: `backend/app/schemas/world_cell.py`.

Fields:

- `schema_version`: literal string with value `"0.2"`, default `"0.2"`.
  Identifies the schema contract version accepted by the v0.2 model.
- `id`: required non-empty string. Identifies the specification in a generic
  producer or consumer context.
- `label`: optional string. Provides human-readable review or display text and
  has no identity semantics.
- `root`: required `WorldCell`. Defines the recursive root cell for the
  specification.
- `metadata`: optional free-form object with default `{}`. Carries
  domain-neutral annotation data. v0.2 does not interpret metadata keys.

## Serialization

`WorldSpec.model_dump()` must produce a dictionary that can be passed back to
`WorldSpec.model_validate()` to reconstruct an equivalent specification,
including nested child cells and entity references.

Serialization compatibility in v0.2 is schema-local. It does not define file
formats, loader paths, persistence records, API response shapes, or frontend
payloads.

## Validation

`WorldSpec` must reject:

- unsupported `schema_version` values.
- empty `id` values.
- missing or invalid `root` payloads.
- nested root content that fails the `WorldCell` or `EntityRef` contracts.

`WorldSpec` must accept omitted `schema_version`, `label`, and `metadata`.
Omitted `schema_version` defaults to `"0.2"` and omitted `metadata` validates
as an empty object.

## Compatibility

The v0.2 contract is additive:

- Existing valid `WorldSpec` payloads with `schema_version = "0.2"` and a
  valid root remain valid.
- Existing unsupported schema versions remain invalid.
- Runtime behavior, API response shapes, frontend behavior, event contracts,
  fixture behavior, and legacy `backend/worldengine/` behavior remain
  unchanged.

Future v0.3 loader work may consume validated `WorldSpec` data only through a
separate reviewed package. Loader behavior must not be inferred from this
contract alone.

## Non-Goals

`WorldSpec` does not implement:

- a loader.
- RuntimeEngine integration.
- runtime state creation.
- event log persistence.
- API routes or response shape changes.
- frontend projection.
- generation.
- external fixture repositories.
- concrete validation-world data.
- agent loop, memory, or self-continuity behavior.
