# Plan

Status: review complete

## Objective

Create and review the `0.6.3` structured generation plan compiler package,
then implement only after the package records `implementation_authorized: yes`.

## Authoritative Inputs Read

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.1` contract
- `0.6.2` contract, technical design, and review evidence
- current `backend/app/schemas/world_generation.py`
- current `backend/app/core/world_generation.py`

## Execution Steps

1. Create this package's seven required documents and Chinese mirrors.
2. Keep the initial documentation draft at `planned / ready for review` and
   `implementation_authorized: no`; after evaluator PASS, record
   `ready for implementation` and `implementation_authorized: yes`.
3. Run documentation checks: diff check, required files, required terms,
   Chinese heading audit, and changed-file scope guard.
4. Request documentation/contract evaluator review.
5. If evaluator reports P1 or blocking P2, fix docs and rerun the checks.
6. Only after evaluator PASS, update this package to
   `ready for implementation`, record `implementation_authorized: yes`, and
   synchronize parent status surfaces.
7. Implement the approved schema/core/test files only.
8. Run focused tests, adjacent compatibility tests, and full backend tests.
9. Request implementation-scope, code-review, validation-evidence, and
   closeout consistency evaluators.
10. Close `0.6.3` only if no unresolved P1/P2 remains.

## Stop Conditions

- Required package documents or mirrors are missing.
- Implementation starts before `implementation_authorized: yes`.
- The design requires API, frontend, persistence, runtime, Agent/memory,
  external validation, projection, or `backend/worldengine/` changes.
- Plan compilation depends on free-form prompt execution or external provider
  calls.
- Generated data becomes concrete world/story or application-specific content.

## Handoff

After closeout, `0.6.4-ai-assisted-generation-boundary-and-plan-import`
receives reviewed structured plan input semantics and compiler evidence.
