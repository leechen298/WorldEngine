# Contract

## Final Closeout Inputs

- all v0.7 child package reviews from `0.7.0` through `0.7.7`.
- `0.7.5` evidence matrix.
- `0.7.6` audit report.
- `0.7.7` release-candidate summary.
- current final verification commands.
- current changed-file scope.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.8-v0.7-final-closeout/`.
- Update parent v0.7 README, current state, campaign plan, goal runner,
  version plan, and review status after final evaluator approval.

## Forbidden Changes

- Do not modify implementation files.
- Do not mark unrun surfaces as passed.
- Do not start v0.8 or create v0.8 package docs.
- Do not remove explicit exclusions.

## Required Final Claims

Final closeout may claim:

- v0.7 public contract/readiness documentation, schemas, checkers, manifest,
  projection read-model contract, evidence matrix, audit, and release-candidate
  package are review complete.
- in-scope checker/schema verification passed in the current session.
- changed-file scope stayed inside approved v0.7 surfaces.

Final closeout must not claim:

- external suite PASS.
- projection application readiness.
- product readiness.
- runtime/API/frontend/E2E/live Agent/full autonomous/generation-quality PASS.
- v0.8 readiness.

## Closeout Gate

Closeout may happen only when final commands pass, final evaluator checks pass,
and no unresolved P1/P2 remains.
