# Contract

## Public Concepts

- Legacy boundary: the documented split between active `backend/app/` and
  legacy `backend/worldengine/` code.
- Compatibility baseline: the v0.1 runtime, API envelope, dashboard-facing
  behavior, params flow, event timeline, archive behavior, and params-agent
  scaffold that v0.2 must preserve.
- v0.2 foundation boundary: EntityRef, WorldCell, WorldSpec, EventRef, and
  Event.refs are additive schema/event contracts, not active runtime loading
  behavior.
- v0.3 handoff constraint: a documented requirement or risk that future bridge
  work must satisfy before changing runtime behavior.
- Compatibility finding: an unresolved documentation, evidence, or behavior
  ambiguity recorded with priority and target package.

## Compatibility Constraints

- Runtime behavior must not change.
- Schema behavior and validation behavior must not change.
- Event storage, event pagination, and current event response behavior must
  not change.
- API response envelopes and endpoint shapes must not change.
- Frontend behavior must not change.
- Fixture, migration, and test implementation files must not change.
- `backend/app/` remains the active backend code path.
- `frontend/` remains the active dashboard code path.
- `backend/worldengine/` remains legacy and unwired unless a later reviewed
  package explicitly changes that boundary.
- Documentation must distinguish implemented v0.1 behavior, additive v0.2
  contracts, and future v0.3 bridge work.

## Allowed Changes

- Add `docs/legacy-boundary.md`.
- Add `docs/legacy-boundary.zh.md`.
- Add `docs/iterations/v0.2/compatibility-review.md`.
- Add `docs/iterations/v0.2/compatibility-review.zh.md`.
- Update `docs/iterations/v0.2/findings.md` to add, close, or retarget
  compatibility findings.
- Update this package's `review.md` and `review.zh.md` with evidence.
- Update v0.2 milestone index and plan status fields for 0.2.10.
- Run read-only repository searches, path checks, and documentation sanity
  checks.

## Forbidden Changes

- Do not modify runtime services, world state, modules, event log behavior,
  archive behavior, agent behavior, persistence, API routes, or app assembly.
- Do not modify schema implementation files.
- Do not modify frontend files.
- Do not modify tests or fixtures.
- Do not add migrations.
- Do not modify `backend/worldengine/`.
- Do not implement WorldSpec loading, RuntimeEngine-to-WorldCell migration,
  runtime bridge, generation, projection, agent loop, memory,
  self-continuity, resolver, or causality behavior.
- Do not add external repositories or external validation internals.
- Do not add concrete external-world names, characters, locations, roles,
  resources, story rules, seed data, UI selectors, private runner state, or
  application-specific backend logic.
- Do not claim tests, builds, runtime behavior, API behavior, or frontend
  behavior passed unless the command or flow is run in the current session.

## Acceptance Requirements

- `docs/legacy-boundary.md` and `.zh.md` exist and document active backend,
  active dashboard, legacy backend, placeholder infrastructure, documentation,
  and future bridge boundaries.
- `docs/iterations/v0.2/compatibility-review.md` and `.zh.md` exist and cover
  runtime state, runtime step behavior, event timeline behavior, world params,
  params-agent scaffold, archive summaries/snapshots, API envelope, frontend
  expectations, schema/event additive contracts, and v0.3 handoff constraints.
- The compatibility review marks each claim as documented, reviewed,
  current-session verified, planned, not implemented, legacy, or finding.
- Any missing evidence, ambiguous active path, or v0.3 bridge risk is recorded
  in `docs/iterations/v0.2/findings.md` instead of being fixed with code.
- Documentation checks pass.
- Changed files are limited to approved documentation paths.
- English and Chinese mirrors are synchronized for package docs and new
  boundary/review docs.

## North Star Check

This package protects WorldEngine as a generic recursive world engine by
separating current runtime compatibility from future bridge work. It does not
introduce concrete worlds, product-specific backend logic, application-specific
fixtures, or runtime behavior.

## Out-of-Scope Follow-ups

- 0.2.11 prepares the v0.2 release-candidate bundle.
- v0.3 may design and implement WorldSpec loader and runtime bridge work only
  after v0.2 closeout.
- Any compatibility-preserving regression tests require a later reviewed mixed
  or code package.
