# Contract

## Public Concepts

- `minimum working-state`: a bounded core-side claim that generation, runtime,
  event evidence, Agent loop, memory context, projection/read-model
  observability, and blocker classification are coherent enough to be proven
  by later current-session evidence.
- `required core slice`: a domain that must either pass, be blocked, be
  skipped with rationale, or be out of scope before a claim is made.
- `claim taxonomy`: the allowed status vocabulary that prevents contract,
  observable surface, evidence, handoff, and external validation PASS from
  being conflated.
- `evidence class`: documentation, schema/checker, API, backend, frontend,
  E2E, Agent smoke, autonomous, external validation, or manual review evidence,
  each with its own authorization and non-claim boundary.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.8/0.8.1-minimum-working-state-contract/`.
- Create or update Chinese mirrors for this package.
- Update parent v0.8 status and route surfaces.
- Define claim taxonomy, required core slices, evidence classes, exclusions,
  and authorization criteria for `0.8.2` through `0.8.5`.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  or `backend/worldengine/` implementation files.
- Do not implement schemas, checkers, services, APIs, UI, persistence, tests,
  smoke runners, external validation behavior, external application behavior,
  or evidence artifacts.
- Do not add concrete world content, private external repository paths, UI
  selectors, hidden reset APIs, private transcripts, oracle internals,
  provider traces, secrets, or product-specific backend logic.
- Do not mark runtime, API, frontend, E2E, Agent smoke, autonomous, external
  validation, projection readiness, product readiness, minimum working-state,
  or release behavior as passed.

## Compatibility Requirements

- Existing runtime, event, archive, params, Agent loop, memory, generation,
  API envelope, dashboard, readiness manifest, and projection read-model
  behavior remain unchanged.
- v0.7 `0.7.9` checker/docs repair evidence remains handoff context only.
- Future implementation must be additive unless a later reviewed child package
  explicitly authorizes a breaking change.

## Out-of-Scope Follow-Ups

- `0.8.2`: define observable public surfaces.
- `0.8.3`: implement or harden core readiness slices only if reviewed.
- `0.8.4`: define external-validation handoff contract.
- `0.8.5`: run core-side smoke evidence.
