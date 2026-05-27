# Plan

## Files

Create:

- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.md`
- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.md`
- matching `*.zh.md` mirrors.

Modify during documentation stage:

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

Expected implementation-stage files after review:

- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`, only if optional inert context
  storage is required.
- `backend/app/tests/test_runtime_context_bridge.py`

Do not touch during documentation stage:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- implementation tests, fixtures, migrations, API routes, schemas, runtime
  services, archive, params, event, or persistence code.

## Steps

1. Read repository guidance, v0.3 milestone docs, 0.3.2 loader
   implementation/review, 0.3.3 bridge contract/review, and current runtime
   implementation files.
2. Draft full 0.3.4 package docs with assumptions, risks, acceptance
   criteria, implementation boundaries, and verification commands.
3. Synchronize English and Chinese mirrors.
4. Mark 0.3.4 as `ready for review` in package README and milestone index.
5. Run documentation and scope checks.
6. Record current-session documentation evidence in `review.md`.

## Implementation Plan After Review

1. Add the pure runtime context bridge module.
2. Add focused bridge unit tests.
3. Add optional inert runtime context storage only if the reviewed design
   requires it.
4. Run focused bridge tests and compatibility tests listed in `test-plan.md`.
5. Update `review.md` with changed files, commands, results, compatibility
   review, scope review, unresolved findings, and final assessment.

## Verification

Use the documentation-stage checks in `test-plan.md` before review.
Runtime and frontend behavior tests are not planned during documentation
stage because implementation files are not modified.
