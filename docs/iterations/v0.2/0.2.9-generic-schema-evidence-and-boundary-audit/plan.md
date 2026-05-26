# Plan

## Files

Create during documentation stage:

- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/README.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/intent.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/intent.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/contract.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/contract.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/technical-design.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/test-plan.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/plan.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/plan.zh.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/review.md`
- `docs/iterations/v0.2/0.2.9-generic-schema-evidence-and-boundary-audit/review.zh.md`

Modify during documentation stage:

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Planned audit-stage creates after review:

- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/evidence-index.zh.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/boundary-audit.zh.md`

Planned audit-stage may modify after review:

- `docs/iterations/v0.2/findings.md`
- this package's `review.md` and `review.zh.md`
- v0.2 status docs if the audit closes or updates status findings.

Do not touch:

- runtime implementation.
- schema implementation.
- API routes or response code.
- frontend files.
- tests or fixtures.
- migrations.
- `backend/worldengine/`.
- external repositories.
- unrelated iteration packages except read-only evidence inspection.

## Documentation-Stage Steps

1. Read repository guidance, v0.2 plan/index docs, templates, boundary docs,
   current implementation docs, completed package reviews, contracts, and
   findings.
2. Create the 0.2.9 package documents with English and Chinese mirrors.
3. Make acceptance and verification requirements concrete and testable.
4. Mark assumptions and open risks.
5. Set 0.2.9 status to `ready for review` in this README and the v0.2
   milestone index.
6. Synchronize the detailed v0.2 plan and Chinese mirrors.
7. Run documentation checks.
8. Record documentation-stage evidence in `review.md` and `review.zh.md`.

## Audit-Stage Steps After Approval

1. Re-read this package in order: `intent.md`, `contract.md`,
   `technical-design.md`, `test-plan.md`, `plan.md`, `review.md`.
2. Build the evidence index from completed v0.2 packages and current
   milestone documents.
3. Build the boundary audit from scope, external fixture, current
   implementation, backend implementation, and package review evidence.
4. Run status consistency checks across English and Chinese mirrors.
5. Run concrete demo anchor sweep with an untracked temporary pattern file.
6. Update findings for missing evidence, boundary concerns, and status drift.
7. Update review evidence with exact commands and results.

## Verification

Documentation-stage verification:

- `git status --short --branch`
- `git diff --check`
- required package mirror file check.
- status consistency grep for package README and v0.2 index/plan docs.

Audit-stage verification:

- documentation checks from `test-plan.md`.
- link/path sanity checks using shell commands.
- changed-file scope guard.
- concrete demo anchor sweep.
