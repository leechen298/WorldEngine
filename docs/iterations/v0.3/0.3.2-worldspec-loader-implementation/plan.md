# Plan

## Files

Create during documentation stage:

- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.md`
- matching `*.zh.md` mirrors.

Modify during documentation stage:

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

Create during implementation stage after review approval:

- `backend/app/core/worldspec_loader.py`
- `backend/app/tests/test_worldspec_loader.py`

Do not touch:

- `backend/app/core/runtime_engine.py`
- API route modules.
- schema modules unless documentation review explicitly revises this package.
- persistence, archive, params, event, frontend, fixture, migration, and legacy
  runtime implementation files.
- concrete external validation-world or demo-world data.

## Steps

Documentation stage:

1. Read the v0.3 milestone docs, 0.3.1 loader contract, and iteration standard.
2. Draft the full 0.3.2 package docs with assumptions, risks, acceptance
   criteria, and verification commands.
3. Synchronize English and Chinese mirrors.
4. Mark 0.3.2 as `ready for review` in package README and milestone index.
5. Run documentation and scope checks.
6. Record current-session documentation evidence in `review.md`.

Implementation stage, after documentation review approval:

1. Re-read `intent.md`, `contract.md`, `technical-design.md`,
   `test-plan.md`, `plan.md`, and `review.md`.
2. Add the smallest loader module satisfying the reviewed contract.
3. Add focused loader tests with neutral input data.
4. Run focused and regression commands from `test-plan.md`.
5. Update `review.md` with changed files, command results, compatibility
   review, scope review, unresolved findings, and final assessment.

## Verification

Documentation-stage verification uses the documentation checks in
`test-plan.md`.

Implementation-stage verification must include focused loader tests, existing
schema smoke tests, whitespace checks, import/coupling checks, concrete-anchor
sweeps, and any broader backend regression required by the actual blast
radius.
