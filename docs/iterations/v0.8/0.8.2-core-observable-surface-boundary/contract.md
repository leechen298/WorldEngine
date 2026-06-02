# Contract

## Public Concepts

- `observable surface family`: a generic group of public, read-only,
  redacted evidence or state summaries that future validators may inspect.
- `public source boundary`: an existing API, contract, report, manifest, or
  evidence surface that may be referenced without exposing private details.
- `allowed observable summary`: the bounded summary class a future payload may
  expose.
- `forbidden exposure`: data or behavior that must not appear in public
  surfaces.
- `implementation authorization criteria`: the conditions a later package
  must satisfy before adding schemas, checkers, APIs, or helpers.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.8/0.8.2-core-observable-surface-boundary/`.
- Create or update Chinese mirrors for this package.
- Update parent v0.8 status and route surfaces.
- Define observable surface families, public source boundaries, allowed
  summaries, forbidden exposure, compatibility rules, and implementation
  authorization criteria for later packages.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  or `backend/worldengine/` implementation files.
- Do not add `docs/contracts/` schemas, `tools/testing` checkers, API routes,
  frontend UI, E2E tests, generated artifacts, or report templates.
- Do not implement write APIs, reset APIs, persistence, migrations, product UI,
  external validation behavior, projection application behavior, or
  consumer-specific backend behavior.
- Do not expose raw memory, prompt traces, private transcripts, provider
  secrets, UI selectors, private app data, oracle internals, or concrete world
  content.
- Do not mark runtime, API, frontend, E2E, Agent smoke, autonomous, external
  validation, projection readiness, product readiness, minimum working-state,
  or release behavior as passed.

## Compatibility Requirements

- Existing runtime, event, archive, params, Agent loop, memory, generation,
  API envelope, dashboard, readiness manifest, and projection read-model
  behavior remain unchanged.
- v0.7 projection read-model and external-validation readiness contracts remain
  the public redaction and read-only baseline.
- Future observable surfaces must be additive, versioned, redacted, and
  read-only unless a later reviewed package explicitly authorizes otherwise.

## Implementation Authorization Criteria

A later package may implement observable schemas, checkers, helpers, or API
surfaces only when its reviewed contract records:

- exact surface family ids.
- exact file classes and paths allowed to change.
- payload fields and redaction rules.
- no-write/no-reset side-effect rules.
- focused tests and adjacent compatibility checks.
- explicit non-claims for external validation PASS, product readiness, and
  projection application readiness.

## Out-of-Scope Follow-Ups

- `0.8.3`: generation/runtime/Agent-loop readiness implementation planning and
  hardening if reviewed.
- `0.8.4`: external-validation handoff contract.
- `0.8.5`: core-side working-state smoke evidence.
