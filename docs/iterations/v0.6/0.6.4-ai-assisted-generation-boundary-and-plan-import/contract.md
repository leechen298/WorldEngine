# Contract

Status: review complete

implementation_authorized: yes

## Public Concepts

- `PlanImportSource`: provider-independent provenance describing where an
  imported structured plan came from. It may record source kind, source id,
  provider label, model label, redaction flag, and generic metadata.
- `PlanImportRequest`: untrusted import envelope carrying import id,
  `GenerationPlan`, `PlanImportSource`, and optional metadata.
- `PlanImportResult`: import validation result containing an accepted
  `GenerationPlan` plus redacted provenance, or diagnostics without an
  accepted plan.
- Import diagnostics: stable `GenerationDiagnostic` records for malformed
  provenance, non-JSON import metadata, rejected prompt fields, and any
  invalid plan diagnostics from `0.6.3`.

## Allowed Changes

Documentation stage:

- create and update this package under `docs/iterations/v0.6/`.
- update parent v0.6 status surfaces only for current child state and evidence.
- record subagent/evaluator evidence.

Implementation stage, only after `implementation_authorized: yes`:

- update `backend/app/schemas/world_generation.py`.
- update `backend/app/core/world_generation.py`.
- add focused tests:
  - `backend/app/tests/test_plan_import_schema.py`
  - `backend/app/tests/test_plan_import_boundary.py`
- update existing focused plan/compiler tests only where needed:
  - `backend/app/tests/test_generation_plan_schema.py`
  - `backend/app/tests/test_structured_generation_plan_compiler.py`
- update this package `review.md` / `review.zh.md`.
- update parent v0.6 status surfaces only for current child state and evidence.

If implementation needs a new module or API route, stop and return to
documentation review before adding that path.

## Forbidden Changes

- Do not modify `backend/app/api/**`, `backend/app/schemas/api.py`,
  `frontend/**`, persistence/repository modules, migrations, fixtures,
  generated output files, external repositories, or `backend/worldengine/**`.
- Do not modify runtime, Agent/memory, archive/params, loader, runtime-context,
  `WorldSpec`, `WorldCell`, or `EntityRef` behavior.
- Do not add live provider credentials, network calls, model orchestration,
  background jobs, hidden retry loops, prompt libraries, prompt storage, or
  prompt execution.
- Do not persist private prompts, secrets, external application data, private
  validation oracle details, generated seed data, or concrete world/story
  content.
- Do not claim generation quality, external validation readiness, projection
  readiness, product readiness, release readiness, API behavior, or frontend
  behavior.

## Implementation Requirements

- Import validation must treat every imported plan as untrusted structured
  data.
- Import must not bypass `validate_generation_plan()`.
- Accepted imports must carry redacted provenance that is JSON-compatible and
  provider-independent.
- Rejected imports must return deterministic diagnostics and no accepted plan.
- Extra free-form prompt fields must be rejected rather than ignored.
- Static/mock tests must not require network, credentials, environment
  secrets, or provider SDKs.

## Compatibility Requirements

- Existing template generation and structured-plan compiler behavior remain
  compatible.
- Existing `WorldSpec`, loader, runtime-context, API envelope, runtime,
  Agent/memory, and frontend behavior remain unchanged.
- Historical v0.5 evidence remains handoff context only.

## Authorization Criteria

This package may record `implementation_authorized: yes` only after:

- all package docs and Chinese mirrors exist.
- documentation/contract evaluator reports PASS with no P0/P1 and no blocking
  unresolved P2.
- contract/design/test-plan/plan explicitly forbid live providers, prompts,
  API, frontend, persistence, and concrete content.
- planned tests cover accepted import, invalid imported plan, malformed
  provenance, non-JSON import metadata, prompt field rejection, and compiler
  compatibility.

## North Star Check

This package advances AI-assisted world generation safely by keeping AI output
as reviewable structured data. It does not make WorldEngine provider-specific
or application-specific.

## Out-of-Scope Follow-ups

- `0.6.5`: generation validation, metadata, and preview API.
- `0.6.6`: regeneration and runtime-readiness integration.
- `0.6.7`: dashboard preview and E2E smoke.
- v0.7 external validation readiness.
- v0.8 projection application readiness.
