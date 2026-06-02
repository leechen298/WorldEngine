# Contract

## Release-Candidate Inputs

The bundle must trace:

- parent v0.7 docs and review.
- all child package reviews from `0.7.0` through `0.7.6`.
- `0.7.5` evidence matrix.
- `0.7.6` audit report.
- current changed-file scope.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle/`.
- Update parent v0.7 status and route surfaces after release-candidate closeout.

## Forbidden Changes

- Do not mark final release or final closeout.
- Do not modify implementation files.
- Do not add tests, checkers, schemas, runtime behavior, API behavior,
  frontend behavior, migrations, fixtures, generated results, or external
  repositories.
- Do not change readiness claims beyond evidence already recorded.

## Required Release-Candidate Contents

- completed child package table.
- current evidence map.
- explicit exclusions.
- unresolved findings.
- final-closeout recommendation.

## Closeout Gate

Closeout may happen only when:

- release-candidate summary exists.
- evidence link checks pass.
- `git diff --check` passes.
- changed-file scope guard passes.
- evaluators report no blocking findings.
