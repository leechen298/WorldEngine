# Technical Design

Status: review complete

## Design Boundary

`0.6.4` adds a local, provider-independent import boundary. It accepts
structured `GenerationPlan` data plus redacted provenance, validates the
import envelope, then delegates plan validation to `validate_generation_plan`.

This design does not call providers, parse prompts, open API routes, persist
data, or compile/run the imported plan by itself.

## Planned Schema Additions

`backend/app/schemas/world_generation.py` may add:

- `PlanImportSource` with source kind, optional source id, provider label,
  model label, redaction flag, and generic metadata.
- `PlanImportRequest` with import id, `GenerationPlan`, provenance, and
  optional import metadata.
- `PlanImportResult` with optional accepted plan, provenance, diagnostics, and
  validation status.

Import schemas should reject unexpected fields so prompt text cannot be
silently accepted.

## Planned Core Additions

`backend/app/core/world_generation.py` may add:

- `validate_plan_import(request)`.
- `import_generation_plan(request)`.

Import validation should check provenance JSON compatibility, import metadata
JSON compatibility, prompt-field rejection, and all diagnostics from
`validate_generation_plan`.

## Determinism And Safety

No wall-clock time, random identity, external network, environment secret, or
provider SDK may participate in import results. Diagnostics must be stable and
pathful.

## Compatibility

Existing template generation and structured-plan compilation must remain
compatible. Runtime, API, frontend, loader, persistence, and
`backend/worldengine/` behavior remain unchanged.

## Out Of Scope

- Live AI generation.
- Prompt execution or storage.
- API exposure.
- Preview, regeneration, persistence, external validation, projection, and UI.
