# Technical Design

Status: review complete

## Design Boundary

`0.6.5` adds a local API preview boundary. The route accepts an API-facing
preview request, delegates source validation and generation to existing core
functions, and returns a standard API envelope. It does not persist generated
worlds, load generated worlds into runtime, call providers, or expose a
dashboard workflow.

## Planned Schema Additions

`backend/app/schemas/world_generation.py` may add:

- `GenerationPreviewSourceKind` as a literal/discriminator for `template`,
  `plan`, and `imported_plan`.
- `GenerationPreviewRequest` with `request_id`, `source_kind`, and exactly one
  of `template_request`, `plan_request`, or `import_request`.
- `GenerationPreviewMetadata` with bounded fields:
  - `generation_id`
  - `request_id`
  - `source_kind`
  - source ids and versions already present in public generation metadata
  - `seed_digest`
  - `validation_status`
  - `diagnostics_count`
  - bounded `preview_summary`
  - optional redacted import source summary
- `GenerationPreviewResponse` with `request_id`, `source_kind`,
  `validation_status`, `metadata`, `diagnostics`, and optional
  `worldspec_preview`.

Preview request and response schemas should reject unexpected fields where
that prevents prompt/provider/private data from being silently accepted.

## Planned Core Additions

`backend/app/core/world_generation.py` may add:

- `preview_generation(request: GenerationPreviewRequest)`.

The helper should:

1. Route `template` requests to `generate_worldspec_from_template`.
2. Route `plan` requests to `generate_worldspec_from_plan`.
3. Route `imported_plan` requests to `import_generation_plan`; only a passed
   import may then call `generate_worldspec_from_plan`.
4. Convert generation results to `GenerationPreviewResponse`.
5. Return failed preview results with diagnostics and no `worldspec_preview`.
6. Return successful preview results with public `WorldSpec` preview and
   bounded metadata.

The helper must not reimplement template, plan, or import validation.

## Planned API Route

`backend/app/api/routes/world_generation.py` may define:

```text
POST /world/generation/preview
```

The route should:

- accept `GenerationPreviewRequest`.
- call `preview_generation`.
- return `ApiResponse(data=result)`.
- rely on the existing application validation exception handler for malformed
  request payloads.

`backend/app/api/routes/__init__.py` and `backend/app/api/app_factory.py` may
only export and include this router. Shared handlers and existing routers must
not be changed except for route inclusion.

## Preview Summary

The preview summary should be deterministic and bounded, for example:

- root world id.
- root label.
- total world-cell count.
- maximum child-cell depth.
- entity reference count.

It must not include raw source payload echoes, prompts, provider traces,
private oracle data, external app data, or concrete fixture content.

## Error And Status Model

Malformed API request shape:

- HTTP status: 422.
- envelope: existing `ApiErrorResponse`.
- code: existing validation error code `30`.

Generation/import validation failure:

- HTTP status: 200.
- envelope: `ApiResponse`.
- `data.validation_status`: `failed`.
- no `data.worldspec_preview`.
- deterministic diagnostics.

Unexpected server errors:

- existing FastAPI behavior and app-level handlers remain unchanged.

## Determinism And Safety

No wall-clock time, random identity, external network, environment secret,
provider SDK, prompt execution, or background job may participate in preview
results. Generation ids and seed digests must come from existing deterministic
generation behavior.

## Compatibility

Existing template generation, plan compilation, import behavior, API envelope,
runtime, loader, Agent/memory, params, archive, frontend, and
`backend/worldengine/` behavior remain unchanged.

## Out Of Scope

- Regeneration.
- Runtime-readiness checks.
- Persistence.
- Frontend UI or client work.
- Live AI generation.
- Prompt execution or storage.
- E2E smoke.
- External validation or projection readiness.
