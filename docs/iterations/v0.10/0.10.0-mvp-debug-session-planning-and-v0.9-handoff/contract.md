# Contract

## Public Concepts

This package may establish or confirm these documentation-level concepts:

- `parent review complete`: the v0.10 parent package can route to its first
  child. This is not implementation authorization.
- `active child package`: the concrete child package selected in
  `CURRENT_STATE.md` for the next goal step.
- `v0.9 BLOCKED handoff`: v0.9 closed as BLOCKED for full LLM-backed lifecycle
  validation, but its architecture and evidence contracts may inform v0.10.
- `MVP debug-session baseline`: v0.10 starts with discoverability and a
  runnable session slice rather than complete Agent autonomy or product
  validation.
- `implementation closed`: runtime, schema, API, frontend, provider,
  Validation Client, checker, fixture, migration, and evidence execution work
  remain unauthorized until a later reviewed child package opens them.

## Compatibility Requirements

- Existing runtime, schema, API, frontend, event, archive, params, Agent loop,
  memory, generation, fixture, migration, checker, provider, Validation
  Client, generated-result, and legacy behavior remain unchanged.
- v0.9 final BLOCKED closeout remains historical handoff context only.
- v0.10 planned-package semantics remain compatible: planned package specs are
  route-map inputs, not implementation authorization.
- Future v0.10 schema/API/checker changes must be additive unless the active
  future child explicitly allows a breaking change.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.10/0.10.0-mvp-debug-session-planning-and-v0.9-handoff/`.
- Create or update Chinese mirrors for this child package.
- Update parent v0.10 status and route surfaces:
  - `docs/iterations/v0.10/README.md`
  - `docs/iterations/v0.10/README.zh.md`
  - `docs/iterations/v0.10/v0.10-plan.md`
  - `docs/iterations/v0.10/v0.10-plan.zh.md`
  - `docs/iterations/v0.10/GOAL_RUNNER.md`
  - `docs/iterations/v0.10/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.10/CURRENT_STATE.md`
  - `docs/iterations/v0.10/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.10/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.10/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.10/review.md`
  - `docs/iterations/v0.10/review.zh.md`
- Record documentation checks and subagent/evaluator findings.
- Preserve v0.9 BLOCKED handoff facts and v0.10 non-claims.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, external repository, generated result,
  provider configuration, Validation Client, or `backend/worldengine/`
  implementation files.
- Do not implement or edit manifest handlers, session APIs, session stores,
  worldview creation flow, runtime controls, snapshot/diff logic, dashboard UI,
  validation repair, Agent continuity, provider configuration, checker
  fixtures, scorecards, evidence bundle exporters, persistence, migrations, or
  product packaging.
- Do not run live provider calls, API smoke, E2E, autonomous validation,
  generated-result rewrites, checker result generation, or external
  Validation Client flows as part of this documentation-only package.
- Do not add concrete demo worlds, maps, characters, locations, resources,
  story rules, seed data, private transcripts, private fixture paths, hidden
  reset APIs, private validation oracle behavior, UI selectors, or
  application-specific backend logic.
- Do not store, display, log, or export API keys, authorization headers, raw
  prompts, raw provider requests, raw provider responses, raw provider traces,
  raw thought, private Agent memory, private goals, hidden context, or private
  evaluator data.
- Do not mark v0.10 manifest, session creation, bounded runtime, dashboard
  flow, Validation Client automation, provider readiness, external validation,
  product readiness, Agent autonomy, or full MVP lifecycle as passed.

## North Star Check

This package keeps WorldEngine generic. It prepares the route toward a
debuggable MVP session without adding concrete worlds, product-client
behavior, external validator implementation, or application-specific backend
logic.

## Out-of-Scope Follow-ups

- `0.10.1`: MVP public manifest and debug handoff.
- `0.10.2`: world session contract and state store.
- `0.10.3`: worldview to runtime session creation.
- `0.10.4`: bounded session runtime and snapshot evidence.
- `0.10.5`: dashboard MVP session flow.
- `0.10.6`: v0.10 validation and handoff.
