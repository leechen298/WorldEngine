# Contract

## Public Concepts

This package defines documentation-level public concepts:

- external validation readiness.
- projection consumer readiness.
- readiness claim taxonomy.
- redacted validation report semantics.
- projection read-only consumer boundary.
- authorization criteria for schema/checker implementation.

## Compatibility Constraints

- Existing runtime, event, archive, params, Agent loop, memory, generation,
  API envelope, and dashboard behavior remain unchanged.
- Existing `docs/contracts/external-fixture-runner-contract.md` remains
  compatible and is extended only by documentation-level readiness semantics.
- Future schema/checker implementation must be additive and must not require
  private consumer details.
- Projection consumer contracts must not imply v0.8 projection application
  readiness.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/`.
- Create or update Chinese mirrors for this child package.
- Create documentation-only public contract files:
  - `docs/contracts/external-validation-readiness-contract.md`
  - `docs/contracts/projection-consumer-contract.md`
- Update parent v0.7 status and route surfaces after review:
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

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, external repository, generated result,
  or `backend/worldengine/` implementation files.
- Do not implement JSON schemas, validators, command-line checkers, services,
  routes, stores, UI, persistence, migrations, fixtures, or test code.
- Do not add concrete validation worlds, consumer-specific examples, seed
  data, private transcripts, UI selectors, private runner imports, private
  fixture paths, hidden reset APIs, or oracle internals.
- Do not claim external suite PASS, projection application readiness,
  generation-quality PASS, product readiness, runtime/API/frontend behavior,
  E2E, Agent smoke, autonomous, or release readiness.

## Authorization Criteria For 0.7.2

`0.7.2` may implement report schema/checker support only after review confirms:

- `docs/contracts/external-validation-readiness-contract.md` is review
  complete.
- status values are explicit: `pass`, `fail`, `blocked`, `skipped`, and
  `out_of_scope`.
- forbidden leaked details are testable by a generic checker.
- redaction confirmation is required for accepted `pass` reports.
- no private fixture path, UI selector, oracle internal, seed data, or
  non-redacted transcript is required.
- implementation authorization is recorded in the `0.7.2` child review before
  code changes begin.

## North Star Check

The package keeps WorldEngine generic by defining public consumer contracts,
not application behavior. External suites and projection applications remain
consumers.

## Out-of-Scope Follow-ups

- `0.7.2`: report schema and redaction checker implementation.
- `0.7.3`: readiness manifest and contract bundle.
- `0.7.4`: projection read-model contracts and any approved implementation.
- `v0.8`: first external projection application readiness.
