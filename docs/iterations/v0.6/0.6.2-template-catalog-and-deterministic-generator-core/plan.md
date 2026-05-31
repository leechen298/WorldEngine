# Plan

Status: review complete

## Files

Documentation stage creates:

- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/README.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/README.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/intent.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/intent.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/contract.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/contract.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/technical-design.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/technical-design.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/test-plan.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/test-plan.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/plan.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/plan.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/review.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/review.zh.md`

After documentation/contract review authorizes implementation, implementation
may create:

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/tests/test_world_generation_schema.py`
- `backend/app/tests/test_template_catalog.py`
- `backend/app/tests/test_deterministic_world_generation.py`

Do not touch:

- `backend/app/api/**`
- `backend/app/schemas/api.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/entity.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/agent/**`
- `backend/app/world/**`
- `frontend/**`
- migrations, fixtures, generated result files, external repositories
- `backend/worldengine/**`

## Ordered Execution Steps

1. Read `CURRENT_STATE.md`, v0.6 parent docs, `0.6.1` reviewed contract and
   review evidence, current schema/loader/runtime-context code, and existing
   adjacent tests.
2. Draft this package's complete docs and Chinese mirrors with
   `implementation_authorized: no`.
3. Run documentation-stage checks from `test-plan.md`.
4. Dispatch documentation/contract evaluator.
5. If evaluator reports blocking P1/P2, fix inside documentation scope or stop.
6. If evaluator reports PASS, update package `review.md` and `.zh.md`, record
   `implementation_authorized: yes`, and synchronize parent status surfaces.
7. Only after authorization, write tests for generation schemas, template
   catalog validation, deterministic generation, loader compatibility, and
   runtime-context compatibility.
8. Implement only the authorized backend schema/service modules.
9. Run focused tests, adjacent compatibility tests, full backend regression,
   `git diff --check`, and implementation scope guard.
10. Dispatch implementation-scope, code-review, validation-evidence, and
    closeout consistency evaluators as required by `GOAL_RUNNER.md`.
11. Update package and parent review evidence. Hand off to `0.6.3` only if no
    unresolved P1/P2 remains.

## Phase Boundaries

- Documentation review must finish before implementation starts.
- `implementation_authorized: yes` belongs in this package `review.md` only
  after documentation/contract evaluator PASS.
- Implementation must not expand into API, frontend, persistence, runtime
  behavior, structured-plan compiler, AI import, regeneration, external
  validation, or projection readiness.

## Stop Conditions

Stop if:

- required docs or mirrors are missing.
- evaluator reports blocking P1/P2.
- implementation would need forbidden files.
- generated output requires concrete world content or story data.
- deterministic behavior cannot be tested from stable inputs.
- tests fail and cannot be fixed inside authorized scope.
- status surfaces drift between package and parent docs.

## Review Update Step

Record:

- changed files.
- commands run.
- exact test results.
- subagent/evaluator evidence.
- compatibility review.
- scope review.
- unresolved P1/P2/P3.
- implementation authorization state.
- final assessment and handoff.
