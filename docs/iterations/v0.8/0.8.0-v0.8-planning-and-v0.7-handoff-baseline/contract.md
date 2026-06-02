# Contract

## Public Concepts

This package may establish or confirm these documentation-level concepts:

- `parent review complete`: the v0.8 parent package can route to its first
  child. This is not implementation authorization.
- `active child package`: the concrete child package selected in
  `CURRENT_STATE.md` for the next goal step.
- `current v0.7 checker/docs handoff evidence`: `0.7.9` and
  `2026-06-02-v0.7-overall-validation.md` clear the V07-CR checker/docs
  blocker gate for v0.7. They do not prove v0.8 readiness.
- `historical handoff evidence`: v0.7 and v0.6 evidence informs v0.8 scope but
  does not count as current v0.8 pass evidence.
- `minimum working-state boundary`: v0.8 must define the core slices required
  for a minimum normally working WorldEngine state before claiming it.
- `external validation boundary`: external validation consumes public,
  redacted, generic core-side surfaces without becoming part of this
  repository.

## Compatibility Constraints

- Existing runtime, schema, API, frontend, event, archive, params, Agent loop,
  memory, generation, fixture, migration, checker, and legacy behavior remain
  unchanged.
- Parent v0.8 planned-package semantics remain compatible: planned package
  specs are route-map inputs, not implementation authorization.
- Current v0.7 checker/docs clean pass remains handoff context only.
- Any future schema/API/checker changes must be additive unless the active
  future child explicitly allows a breaking change.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/`.
- Create or update Chinese mirrors for this child package.
- Update parent v0.8 status and route surfaces:
  - `docs/iterations/v0.8/README.md`
  - `docs/iterations/v0.8/README.zh.md`
  - `docs/iterations/v0.8/v0.8-plan.md`
  - `docs/iterations/v0.8/v0.8-plan.zh.md`
  - `docs/iterations/v0.8/GOAL_RUNNER.md`
  - `docs/iterations/v0.8/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.8/CURRENT_STATE.md`
  - `docs/iterations/v0.8/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.8/review.md`
  - `docs/iterations/v0.8/review.zh.md`
- Record documentation checks and subagent/evaluator findings.
- Update v0.7 handoff wording inside v0.8 documentation to reflect the
  current `0.7.9` repair status.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, external repository, generated result,
  or `backend/worldengine/` implementation files.
- Do not implement or edit minimum working-state schemas, external-validation
  handoff schemas, redaction checkers, contract bundle generators, readiness
  manifest generators, projection endpoints, API handlers, frontend UI,
  persistence, migrations, or product packaging.
- Do not add concrete external validation world data, concrete world names,
  maps, characters, locations, resources, story rules, seed data, private
  transcripts, UI selectors, private fixture paths, hidden reset APIs, private
  validation oracle behavior, or private external repository paths.
- Do not mark v0.8 final, release-ready, product-ready, external-suite-passed,
  external-consumer-passed, minimum-working-state-passed, Agent-smoke-passed,
  autonomous-passed, E2E-passed, API-passed, frontend-passed, or
  runtime-passed.

## North Star Check

This package keeps WorldEngine generic. It prepares core-side readiness and
external-validation handoff boundaries without adding consumer-specific state,
private validation fixtures, product UI, or application backend logic.

## Out-of-Scope Follow-ups

- `0.8.1`: minimum working-state contract and claim taxonomy.
- `0.8.2`: core observable surface boundary.
- `0.8.3`: generation, runtime, and Agent-loop readiness.
- `0.8.4`: external-validation handoff contract.
- `0.8.5`: core-side working-state smoke evidence.
- `0.8.6` through `0.8.8`: audit, release-candidate, and final closeout.
