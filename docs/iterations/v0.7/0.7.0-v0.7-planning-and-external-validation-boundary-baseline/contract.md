# Contract

## Public Concepts

This package may establish or confirm these documentation-level concepts:

- `parent review complete`: the v0.7 parent package can route to its first
  child. This is not implementation authorization.
- `active child package`: the concrete child package selected in
  `CURRENT_STATE.md` for the next goal step.
- `historical handoff evidence`: v0.6 evidence that informs v0.7 scope but
  does not count as current v0.7 pass evidence.
- `external validation boundary`: external suites consume public contracts,
  schemas, exported bundles, redacted reports, or APIs without importing
  private validation worlds into this repository.
- `projection consumer boundary`: projection applications consume generic
  WorldEngine read models and contracts without product-specific backend
  behavior in the core repository.

## Compatibility Constraints

- Existing runtime, schema, API, frontend, event, archive, params, Agent loop,
  memory, generation, fixture, migration, checker, and legacy behavior remain
  unchanged.
- Parent v0.7 planned-package semantics remain compatible: planned package
  specs are route-map inputs, not implementation authorization.
- Historical v0.6 evidence remains handoff context only.
- Any future schema/API/checker changes must be additive unless the active
  future child explicitly allows a breaking change.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/`.
- Create or update Chinese mirrors for this child package.
- Update parent v0.7 status and route surfaces:
  - `docs/iterations/v0.7/README.md`
  - `docs/iterations/v0.7/README.zh.md`
  - `docs/iterations/v0.7/v0.7-plan.md`
  - `docs/iterations/v0.7/v0.7-plan.zh.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.7/CURRENT_STATE.md`
  - `docs/iterations/v0.7/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.7/review.md`
  - `docs/iterations/v0.7/review.zh.md`
- Record documentation checks and subagent/evaluator findings.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, external repository, generated result,
  or `backend/worldengine/` implementation files.
- Do not implement or edit report schemas, redaction checkers, contract bundle
  generators, readiness manifest generators, projection endpoints, API
  handlers, frontend UI, persistence, migrations, or product packaging.
- Do not add concrete external validation world data, concrete world names,
  maps, characters, locations, resources, story rules, seed data, private
  transcripts, UI selectors, private fixture paths, hidden reset APIs, or
  private validation oracle behavior.
- Do not mark v0.7 final, release-ready, product-ready, projection
  application-ready, external-suite-passed, Agent-smoke-passed,
  autonomous-passed, E2E-passed, API-passed, frontend-passed, or
  runtime-passed.

## North Star Check

This package keeps WorldEngine generic. It defines the campaign boundary for
external consumers without adding consumer-specific state, private validation
fixtures, product UI, or application backend logic.

## Out-of-Scope Follow-ups

- `0.7.1`: public validation and projection contract semantics.
- `0.7.2`: report schema and redaction checker.
- `0.7.3`: contract bundle and readiness manifest.
- `0.7.4`: projection consumer read model contracts and any approved read-only
  implementation.
- `0.7.5`: quality regression and compatibility evidence.
- `0.7.6` through `0.7.8`: audit, release-candidate, and final closeout.
