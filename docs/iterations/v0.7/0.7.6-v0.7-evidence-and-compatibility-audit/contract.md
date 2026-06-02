# Contract

## Audit Inputs

The audit must inspect or trace these evidence surfaces:

- parent v0.7 docs and review.
- `0.7.0` review.
- `0.7.1` review.
- `0.7.2` review and checker evidence.
- `0.7.3` review and manifest evidence.
- `0.7.4` review and projection read-model evidence.
- `0.7.5` review and evidence matrix.
- current changed-file set.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.6-v0.7-evidence-and-compatibility-audit/`.
- Update parent v0.7 status and route surfaces after audit closeout.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, tests, checkers, fixtures,
  migrations, external repositories, generated results, or `backend/worldengine/`.
- Do not add new validation behavior.
- Do not mark v0.7 final.
- Do not accept unresolved P1/P2 without explicit blocker status.

## Required Audit Questions

- Are all child package reviews present and internally consistent?
- Does command evidence from `0.7.5` support only checker/schema/manifest
  compatibility claims?
- Are runtime/API/frontend/E2E/live Agent/full autonomous/external suite/
  projection app/product/generation/release checks excluded where unrun?
- Did any implementation file outside approved v0.7 scope change?
- Are unresolved findings P1/P2/P3 classified?

## Closeout Gate

Closeout may happen only when:

- audit report exists.
- traceability checks pass.
- `git diff --check` passes.
- changed-file scope guard passes.
- documentation/audit and closeout consistency evaluators report no blocking
  findings.
