# Plan

## Files

Create after review:

- `docs/iterations/v0.2/v0.2-release-candidate-bundle.md`
- `docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md`
- `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md`
- `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md`

Modify after review:

- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- `docs/iterations/v0.2/findings.md` if new or changed findings are found.
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`
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

1. Read the approved package documents.
2. Read v0.2 package reviews, evidence index, boundary audit, compatibility
   review, findings, release docs, roadmap, and scope boundaries.
3. Build the release-candidate claim-to-evidence matrix.
4. Create the release-candidate bundle and Chinese mirror.
5. Create the final review bundle and Chinese mirror using the existing
   template structure.
6. Update the v0.2 release draft with release-candidate evidence while
   preserving not-final status.
7. Record new or changed findings if evidence gaps appear.
8. Run the documentation verification checks from `test-plan.md`.
9. Update this package's review evidence and status docs honestly.

## Verification

Required:

- `git diff --check`
- required file presence checks.
- package mirror presence checks.
- status consistency grep.
- release-status wording check.
- evidence traceability check.
- concrete demo anchor sweep with abstract classification only.
- changed-file scope guard.

Not planned:

- backend tests.
- frontend tests.
- API smoke.
- E2E.
- Agent smoke.
- runtime or schema execution tests.

The not-planned tests remain valid only if the changed-file set stays
documentation-only.

## Exit Criteria

- Release-candidate bundle is ready for human / ChatGPT review.
- Final review bundle is complete and mirrors the template.
- Release docs state candidate evidence without final release claims.
- P1/P2 findings are clearly listed and block final closeout unless resolved
  or explicitly accepted.
- Changed files remain inside approved documentation scope.
