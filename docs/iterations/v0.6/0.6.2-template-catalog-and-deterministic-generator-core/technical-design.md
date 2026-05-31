# Technical Design

Status: review complete

## Current State

The current backend has `WorldSpec`, `WorldCell`, `EntityRef`,
`load_worldspec`, `build_runtime_context`, and backend tests for schema,
loader, and runtime-context compatibility. There is no generation schema,
template catalog, or deterministic generator implementation.

## Proposed Implementation

After authorization, add two backend modules:

```text
backend/app/schemas/world_generation.py
backend/app/core/world_generation.py
```

`backend/app/schemas/world_generation.py` owns data contracts:

- `TemplateCell`
- `WorldTemplate`
- `TemplateGenerationRequest`
- `GenerationDiagnostic`
- `GenerationMetadata`
- `TemplateGenerationResult`

`backend/app/core/world_generation.py` owns deterministic behavior:

- seed normalization and seed digest generation.
- template validation and diagnostics.
- stable traversal of template cells and entity refs.
- deterministic `WorldSpec` construction.
- no persistence, no wall-clock output identity, no external calls.

## Data Flow

```text
TemplateGenerationRequest
  -> validate template shape and constraints
  -> diagnostics on failure
  -> deterministic seed digest
  -> WorldSpec(schema_version="0.2")
  -> TemplateGenerationResult(worldspec, metadata, diagnostics)
  -> load_worldspec in tests for compatibility evidence
  -> build_runtime_context in tests for bounded bridge evidence
```

## Planned Schema Semantics

- Template ids, versions, cell ids, diagnostic codes, severities, and messages
  must be non-empty.
- Template cells are recursive and generic.
- Entity refs reuse existing `EntityRef` semantics.
- Generation metadata records request id, generation id, template id/version,
  seed digest, validation status, diagnostics count, and lineage fields.
- Generation result contains a `WorldSpec` only when validation status is
  passed.

## Determinism Strategy

- Normalize seed material and template data through stable JSON serialization
  with sorted keys.
- Use a deterministic digest for generation id, generated spec id, and seed
  metadata.
- Preserve stable ordering from template cells and entity refs.
- Do not mutate template inputs.
- Do not use random, wall-clock time, process-global counters, filesystem
  state, environment secrets, or network calls.

## Diagnostics Strategy

Diagnostics are data, not exceptions. Planned codes include:

- `duplicate_cell_id`
- `duplicate_entity_ref`
- `invalid_template_bounds`
- `entity_kind_not_allowed`
- `empty_template`
- `schema_validation_error`

Diagnostics use JSON Pointer-style paths where possible, such as
`/root/child_cells/0/id` or `/root/entity_refs/0/kind`.

## Affected Files

Allowed after authorization:

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/tests/test_world_generation_schema.py`
- `backend/app/tests/test_template_catalog.py`
- `backend/app/tests/test_deterministic_world_generation.py`
- this package's `review.md` and `review.zh.md`
- parent v0.6 status files for current child state only

Not affected:

- `backend/app/api/**`
- `backend/app/schemas/api.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/entity.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/agent/**`
- `backend/app/world/**` except no changes are planned there
- `frontend/**`
- migrations, fixtures, generated outputs, external repositories
- `backend/worldengine/**`

## Compatibility Strategy

Tests must prove:

- generated output validates as current `WorldSpec`.
- loader success remains a `WorldSpecLoaderResult` with existing source
  semantics.
- invalid generated mappings still fail through existing loader diagnostics.
- runtime-context summary remains bounded and does not expose raw `WorldSpec`
  or root payloads.
- existing schema, loader, and runtime-context tests still pass.

## Risks

- Risk: templates become concrete world fixtures.
  Mitigation: keep examples generic and add content guard tests.
- Risk: deterministic output accidentally depends on Python object ordering or
  mutable inputs.
  Mitigation: stable JSON digest and no input mutation tests.
- Risk: implementation drifts into API or runtime behavior.
  Mitigation: changed-file scope guard and explicit forbidden surfaces.
- Risk: generated structural validity is overstated as product readiness.
  Mitigation: review records only schema/loader/runtime-context compatibility,
  not release, runtime, E2E, or quality readiness.
