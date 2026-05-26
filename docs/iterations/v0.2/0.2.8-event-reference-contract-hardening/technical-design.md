# Technical Design

## Current State

`backend/app/schemas/event.py` defines EventRef as a Pydantic model with
non-empty `id`, non-empty `kind`, optional `role`, and default empty metadata.

`Event` includes `refs: List[EventRef] = Field(default_factory=list)`,
alongside existing event identity, tick, world time, type, source, payload,
and created-at fields.

`EventPage`, `EventStep`, and `EventStepPage` nest Event objects and therefore
carry Event.refs through paginated and grouped event response schemas.

`backend/app/tests/test_event_schema_compat.py` already covers imports,
existing event construction without refs, refs with role and metadata, empty
EventRef identity rejection, optional role, default metadata, model dump /
validate round trips, EventPage validation, and EventStepPage validation.

## Contract Alignment and Invariants

- Keep EventRef generic and event-local.
- Keep `id`, `kind`, and `role` as strings without v0.2 runtime enum
  semantics.
- Keep `metadata` free-form and uninterpreted by v0.2 runtime code.
- Preserve existing event dictionaries without refs.
- Preserve existing payload behavior, event log behavior, API response
  shapes, frontend behavior, fixtures, migrations, and legacy code behavior.
- Keep examples and tests domain-neutral.

## Proposed Implementation

After documentation review approval, implement the smallest scoped hardening
pass:

1. Add `docs/contracts/event-ref-contract.md` describing EventRef fields,
   Event.refs semantics, validation behavior, compatibility guarantees, and
   non-goals.
2. Compare existing event schema compatibility tests against the accepted
   coverage list in `test-plan.md`.
3. Add only missing domain-neutral tests to
   `backend/app/tests/test_event_schema_compat.py`.
4. Make schema code changes only if a reviewed acceptance requirement cannot
   be satisfied by the current additive schema.
5. Update `review.md` and `review.zh.md` with actual changed files, commands,
   results, compatibility review, scope review, and unresolved findings.

## Affected Surfaces

Documentation:

- `docs/contracts/event-ref-contract.md`
- `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/**`

Possible tests:

- `backend/app/tests/test_event_schema_compat.py`

Possible schema, only if additive clarification is required:

- `backend/app/schemas/event.py`

## Data Model / Schema Changes

No schema change is required by default. The expected implementation is
contract documentation plus any missing focused compatibility tests.

If implementation finds a real schema ambiguity, allowed schema changes are
limited to additive validation clarifications approved by `contract.md`.
Breaking changes require returning to documentation review.

## Runtime / Service Design

None. This package must not add resolver behavior, causality evaluation,
runtime bridge flow, persistence changes, service wiring, background tasks,
API routes, or frontend behavior.

## Compatibility

Existing v0.1 runtime behavior, event log behavior, payload behavior, API
response shapes, frontend behavior, fixtures, migrations, and legacy
`backend/worldengine/` behavior remain unchanged.

Existing valid Event payloads without refs must continue to validate.
Existing valid Event payloads with refs must continue to validate. Existing
invalid empty EventRef identity fields must continue to fail validation.

## Assumptions

- Pydantic remains the event schema validation layer for this package.
- Contract docs can clarify semantics without requiring schema code changes.
- Current focused tests may already satisfy some or all acceptance criteria.
- `EventRef.kind` values are generic producer-provided categories in v0.2.

## Risks

- Risk: tests duplicate existing coverage instead of hardening meaningful
  gaps. Mitigation: implementation must first map current tests to acceptance
  criteria and add only missing tests.
- Risk: contract docs imply refs are resolved or causally ordered. Mitigation:
  the EventRef contract must explicitly state v0.2 non-goals.
- Risk: examples drift into concrete external-world details. Mitigation: use
  neutral identifiers and run a concrete demo anchor sweep on touched docs and
  tests.
- Risk: schema clarifications could alter API behavior. Mitigation: avoid
  schema changes by default and run focused compatibility checks if schema or
  tests change.
