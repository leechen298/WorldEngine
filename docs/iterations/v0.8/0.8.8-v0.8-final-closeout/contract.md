# Contract

## Public Concepts

- `FinalCloseout`: the documentation decision that v0.8 package evidence and
  final verification are sufficient to mark the v0.8 campaign final.
- `FinalVerification`: current-session commands authorized by this package
  review and recorded before final status changes.
- `FinalExclusion`: surfaces that remain explicitly not claimed by final
  v0.8 closeout.
- `FinalDisposition`: one of `final_ready`, `blocked`, or
  `defer_pending_review`.

## Allowed Changes

Documentation stage:

- Create or update this package's docs and Chinese mirrors.
- Create `final-closeout-summary.md` and `final-closeout-summary.zh.md`.
- Record final evidence references, compatibility review, scope review,
  exclusions, unresolved findings, and review gates.
- Update parent v0.8 status surfaces to ready-for-review for this package.

After documentation review explicitly authorizes final verification:

- Run only final verification commands listed in `test-plan.md` or approved by
  the evaluator.
- Fill final verification results and final disposition.
- Update parent v0.8 status to final only if final verification and evaluator
  approval pass.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  external validator, external application, deployment, or `backend/worldengine/`
  files.
- Do not repair failures inside final closeout.
- Do not claim external validation PASS, external consumer PASS, product
  readiness, frontend/E2E PASS, Agent smoke PASS, autonomous PASS,
  generation-quality PASS, deployment readiness, external app implementation,
  or external validator implementation.
- Do not convert v0.7 handoff evidence into v0.8 product or external
  validation evidence.
- Do not authorize v0.9 or future implementation work.

## Required Closeout Surfaces

The final closeout summary must include:

- status matrix for `0.8.0` through `0.8.8`.
- final verification command matrix.
- compatibility matrix.
- exclusions and non-claims.
- unresolved finding matrix.
- final disposition.

## Closeout Rule

v0.8 may be marked final only if:

- final verification commands pass or are explicitly classified as skipped or
  out of scope without affecting the final claim.
- no unresolved P1 or blocking P2 remains.
- parent and child status surfaces are synchronized.
- evaluator review approves final closeout.
