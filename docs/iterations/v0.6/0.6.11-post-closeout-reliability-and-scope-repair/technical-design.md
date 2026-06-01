# Technical Design

Status: review complete

## Structure

The repair has two code-level changes and one evidence-level reconciliation.

| Area | Design |
| --- | --- |
| Failed generation fallback | In template and plan generation, keep valid `seed_material` in fallback digest payloads by using `_json_compatible_or_none(request.seed_material)` instead of always dropping the seed. |
| Preview API coverage | Add a FastAPI TestClient test that posts an imported-plan preview request with sensitive redacted provenance metadata and asserts a failed, redacted public response. |
| Evidence reconciliation | Add this package and update parent review, implementation summaries, and durable reliability result after verification. |

## Affected Files

Code/test files:

- `backend/app/core/world_generation.py`
- `backend/app/tests/test_deterministic_world_generation.py`
- `backend/app/tests/test_structured_generation_plan_compiler.py`
- `backend/app/tests/test_generation_preview_api.py`

Existing frontend/E2E repair files remain in scope only because the current
post-closeout dirty set already contains the reviewed dashboard diagnostics
repair:

- `frontend/src/components/GenerationPanel.vue`
- `frontend/src/components/GenerationPanel.test.ts`
- `frontend/e2e/dashboard-generation.spec.ts`

Documentation/evidence files are listed in `contract.md`.

## Data Flow

1. Validation collects diagnostics for non-JSON metadata or constraints.
2. Digest creation tries the full canonical payload.
3. If the full payload is not canonical, fallback digesting keeps stable ids,
   versions, canonical request constraints if available, and canonical seed
   material if available.
4. If seed material itself is not canonical, the existing
   `unsupported_seed_material` diagnostic remains and fallback seed material is
   `None`.

## Compatibility Strategy

The fix changes only failed-result metadata for fallback digest cases. Passed
generation behavior and public schema shape stay unchanged.

## Anti-Drift Rules

- Do not add new generation behavior while repairing diagnostics.
- Do not use `0.6.10` as authority for implementation edits.
- Keep the reliability result aligned with package review evidence.
