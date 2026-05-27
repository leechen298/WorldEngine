# Plan

## Files

Create:

- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md`
- `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md`
- `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md`
- this package's English and Chinese package documents.

Modify:

- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`
- `docs/iterations/v0.3/findings.md` only if new or changed findings are
  discovered.
- this package's `review.md` and `review.zh.md`.

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

1. Read the repository guidance, v0.3 milestone docs, package templates,
   0.3.0 through 0.3.6 reviews, `evidence-index.md`, and
   `compatibility-audit.md`.
2. Build the release-candidate claim-to-evidence matrix from existing
   evidence.
3. Create the package docs and Chinese mirrors.
4. Create the release-candidate bundle and Chinese mirror.
5. Create the final-review bundle and Chinese mirror using the existing
   template structure.
6. Update v0.3 package status fields to `ready for review` / `待评审`.
7. Record new or changed findings if evidence gaps appear.
8. Run the documentation verification checks from `test-plan.md`.
9. Update this package's review evidence and final assessment.

## Verification

Required:

- `git diff --check`
- required file presence checks.
- package mirror presence checks.
- status consistency grep.
- release-status wording check.
- evidence traceability check.
- concrete demo anchor sweep.
- changed-file scope guard.

Not planned:

- backend tests.
- frontend tests.
- API smoke.
- E2E.
- Agent smoke.
- runtime, schema, fixture, migration, or build tests.

The not-planned tests remain valid only if changed files stay
documentation-only.

## Exit Criteria

- Release-candidate bundle is ready for human / ChatGPT review.
- Final review bundle is complete and mirrors the template.
- P1/P2 findings are visible and block final closeout unless resolved or
  explicitly accepted.
- Final release status is not declared.
- Changed files remain inside approved documentation scope.
