# Plan

## Files

Create during documentation stage:

- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/README.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/intent.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/intent.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/contract.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/contract.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/technical-design.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/technical-design.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/test-plan.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/test-plan.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/plan.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/plan.zh.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/review.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/review.zh.md`

Modify during documentation stage:

- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

Potential implementation-stage files after review approval:

- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`
- `docs/iterations/v0.2/findings.md`
- this package's `README.md`, `README.zh.md`, `review.md`, and `review.zh.md`.

Do not touch:

- runtime implementation files.
- schema implementation files.
- API route files.
- frontend implementation files.
- fixture files.
- migration files.
- test implementation files.
- `backend/worldengine/`.
- external repository paths or private validation internals.

## Steps

1. Read repository guidance, iteration standards, v0.2 milestone index, v0.2
   detailed plan, 0.2.11 release-candidate bundle, and findings ledger.
2. Draft the 0.2.12 package docs with explicit approval gates, blocker rules,
   assumptions, risks, and verification commands.
3. Create synchronized Chinese mirrors.
4. Set 0.2.12 status to `ready for review` in the package README, milestone
   index, and detailed plan mirrors.
5. Run documentation-stage checks from `test-plan.md`.
6. Record documentation-stage evidence in `review.md` and `review.zh.md`.

## Verification

Required during documentation stage:

- `git diff --check`
- package mirror presence check.
- status consistency grep.
- closeout gate wording grep.
- changed-file scope guard.
- trailing whitespace grep.
- package file listing.

Not planned:

- backend tests.
- frontend tests.
- API smoke.
- E2E.
- Agent smoke.
- runtime or schema execution tests.

The not-planned checks remain valid only if the changed-file set stays
documentation-only.

## Exit Criteria

- 0.2.12 package docs are complete.
- Acceptance and verification requirements are testable.
- Assumptions and open risks are explicit.
- English and Chinese mirrors are synchronized.
- Package README and v0.2 milestone index mark 0.2.12 `ready for review`.
- No runtime, schema, API, frontend, fixture, migration, or test
  implementation files are changed.
