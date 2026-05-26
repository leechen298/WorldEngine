# Plan

## Files

Create during documentation stage:

- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/README.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/README.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/intent.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/intent.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/contract.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/contract.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/technical-design.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/test-plan.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/plan.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/plan.zh.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/review.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/review.zh.md`

Modify during documentation stage:

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Planned implementation-stage creates:

- `docs/contracts/entity-ref-contract.md`
- `docs/contracts/worldcell-contract.md`
- `docs/contracts/worldspec-contract.md`

Planned implementation-stage may modify:

- `backend/app/tests/test_world_cell_schema.py`
- `backend/app/tests/test_worldspec_schema_smoke.py`
- `backend/app/schemas/entity.py` only for approved additive clarifications.
- `backend/app/schemas/world_cell.py` only for approved additive
  clarifications.
- this package's `review.md` and `review.zh.md`.

Do not touch:

- runtime services.
- API routes.
- frontend files.
- fixtures or fixture data.
- migrations.
- `backend/worldengine/`.
- external repositories.
- unrelated iteration packages.

## Documentation-Stage Steps

1. Read required repository, milestone, template, schema, test, and boundary
   documents.
2. Create the 0.2.7 package documents with English and Chinese mirrors.
3. Make acceptance and verification requirements concrete and testable.
4. Mark assumptions and open risks.
5. Set 0.2.7 status to `ready for review` in this README and the v0.2
   milestone index.
6. Run documentation checks.
7. Record documentation-stage evidence in `review.md` and `review.zh.md`.

## Implementation-Stage Steps After Approval

1. Re-read this package in order: `intent.md`, `contract.md`,
   `technical-design.md`, `test-plan.md`, `plan.md`, `review.md`.
2. Add EntityRef, WorldCell, and WorldSpec contract docs.
3. Map current schema tests to acceptance criteria.
4. Add only missing domain-neutral tests.
5. Make schema code changes only if required by the approved contract.
6. Run the command matrix in `test-plan.md`.
7. Run the concrete demo anchor sweep for touched docs and tests.
8. Update `review.md` and `review.zh.md` with actual implementation evidence.

## Verification

Documentation-stage verification:

- `git status --short --branch`
- `git diff --check`

Implementation-stage verification:

- focused schema pytest commands from `test-plan.md`.
- `make check-backend`.
- full backend app tests if schema code changes.
- concrete demo anchor sweep for touched docs and tests.
