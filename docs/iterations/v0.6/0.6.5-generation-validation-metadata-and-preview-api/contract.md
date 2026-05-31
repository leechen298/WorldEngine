# Contract

Status: review complete

implementation_authorized: yes

## Public Concepts

- `GenerationPreviewSourceKind`: public discriminator for previewing a
  `template`, `plan`, or `imported_plan` source.
- `GenerationPreviewRequest`: API-facing request that carries one source
  payload, request id, optional seed material, and request constraints.
- `GenerationPreviewMetadata`: bounded response metadata derived from existing
  `GenerationMetadata` plus public preview counters and optional redacted
  import provenance.
- `GenerationPreviewResponse`: deterministic response containing source kind,
  validation status, diagnostics, bounded metadata, and a public
  `WorldSpec` preview only when generation validation passes.
- Preview diagnostics: existing `GenerationDiagnostic` records reused from
  template validation, plan validation, and import validation.

## API Contract

Implementation may add:

```text
POST /world/generation/preview
```

The route must return:

- success envelope: `ApiResponse[GenerationPreviewResponse]`.
- request validation errors: existing `ApiErrorResponse` from the application
  validation handler, including code `30`.
- generation validation failures: HTTP 200 success envelope with
  `data.validation_status == "failed"`, diagnostics, no `worldspec_preview`,
  and bounded metadata.

The route must not change any existing path, router, handler, response model,
or envelope.

## Request Semantics

`GenerationPreviewRequest` must:

- require `request_id` and `source_kind`.
- allow exactly one matching source payload:
  - `template_request: TemplateGenerationRequest` for `source_kind:
    "template"`.
  - `plan_request: PlanGenerationRequest` for `source_kind: "plan"`.
  - `import_request: PlanImportRequest` for `source_kind: "imported_plan"`.
- reject missing, mismatched, or multiple source payloads as request-shape
  validation errors.
- reject unexpected fields rather than ignoring them.

## Response Semantics

`GenerationPreviewResponse` must:

- include `request_id`, `source_kind`, `validation_status`, `metadata`,
  `diagnostics`, and optional `worldspec_preview`.
- include `worldspec_preview` only when validation passes.
- use the public `WorldSpec` schema as the only generated-world preview
  payload.
- include redacted import provenance only for successful imported-plan preview.
- not include raw prompts, provider traces, hidden retry state, credentials,
  private oracle details, or source payload echoes.

## Allowed Changes

Documentation stage:

- create and update this package under `docs/iterations/v0.6/`.
- update parent v0.6 status surfaces only for current child state and
  evidence.
- record subagent/evaluator evidence.

Implementation stage, only after `implementation_authorized: yes`:

- update `backend/app/schemas/world_generation.py`.
- update `backend/app/core/world_generation.py`.
- add `backend/app/api/routes/world_generation.py`.
- update `backend/app/api/routes/__init__.py`.
- update `backend/app/api/app_factory.py`.
- add focused tests:
  - `backend/app/tests/test_generation_preview_api.py`
- update existing focused generation/API tests only where needed for
  compatibility:
  - `backend/app/tests/test_world_generation_schema.py`
  - `backend/app/tests/test_deterministic_world_generation.py`
  - `backend/app/tests/test_generation_plan_schema.py`
  - `backend/app/tests/test_structured_generation_plan_compiler.py`
  - `backend/app/tests/test_plan_import_schema.py`
  - `backend/app/tests/test_plan_import_boundary.py`
  - `backend/app/tests/test_agent_loop_api.py`
  - `backend/app/tests/test_event_api_compat.py`
- update this package `review.md` / `review.zh.md`.
- update parent v0.6 status surfaces only for current child state and
  evidence.

If implementation needs frontend files, persistence files, migrations,
fixtures, generated result artifacts, new provider modules, or a different API
route shape, stop and return to documentation review before adding that path.

## Forbidden Changes

- Do not modify `frontend/**`, persistence/repository modules, migrations,
  fixtures, generated output files, external repositories, or
  `backend/worldengine/**`.
- Do not modify runtime tick/event semantics, Agent/memory semantics,
  archive/params behavior, loader/runtime-context behavior, or existing route
  response envelopes.
- Do not add live AI provider credentials, network calls, SDKs, prompt
  execution, prompt storage, hidden retries, background jobs, or model
  orchestration.
- Do not expose raw private prompts, unredacted provider traces, secrets,
  external application data, private validation oracle details, generated seed
  data, concrete maps, characters, locations, resources, story rules, or
  application-specific backend logic.
- Do not claim runtime readiness, regeneration readiness, dashboard behavior,
  E2E behavior, autonomous validation, external validation readiness,
  projection readiness, product readiness, release readiness, or generation
  quality.

## Compatibility Requirements

- Existing API success and error envelope behavior remains compatible.
- Existing routes remain compatible and keep their response shapes.
- Existing template generation, structured-plan compiler, and import boundary
  behavior remain compatible.
- Existing `WorldSpec`, loader, runtime-context, runtime, Agent/memory,
  archive, params, and frontend behavior remain unchanged.
- Schema additions are additive and request models reject unexpected fields
  where API safety requires it.

## Authorization Criteria

This package may record `implementation_authorized: yes` only after:

- all package docs and Chinese mirrors exist.
- documentation/contract evaluator reports PASS with no P0/P1 and no blocking
  unresolved P2.
- contract/design/test-plan/plan explicitly preserve API envelopes and forbid
  frontend UI, persistence, migrations, live AI, raw prompts, provider traces,
  concrete content, and `backend/worldengine/**`.
- planned tests cover successful template preview, successful plan preview,
  imported-plan preview, generation validation failure, import validation
  failure, request shape validation, preview payload shape, existing envelope
  compatibility, route wiring, full backend regression, and scope guard.

## North Star Check

This package exposes generic world generation preview without making
WorldEngine provider-specific or application-specific. It prepares generated
worlds to be inspected before later runtime-readiness work.

## Out-of-Scope Follow-ups

- `0.6.6`: regeneration and runtime-readiness integration.
- `0.6.7`: dashboard preview and E2E smoke.
- v0.7 external validation readiness.
- v0.8 projection application readiness.
