# Technical Design

## Current State

The active implementation map describes v0.1 as a runtime scaffold with:

- active FastAPI backend under `backend/app/`.
- active Vue dashboard under `frontend/`.
- in-memory runtime state, event log, snapshots, and summaries.
- params validation, dry-run validation, and params-agent proposal flow.
- legacy `backend/worldengine/` code that is not wired into the active app.

v0.2 added recursive schema and event reference foundations through completed
packages, but those contracts are not runtime loading behavior. v0.3 is the
first planned milestone that may bridge generic WorldSpec data into runtime
context.

## Contract Alignment and Invariants

- Treat `docs/current-implementation.md`, `docs/backend-implementation.md`,
  `docs/architecture.md`, package reviews, and current route/schema docs as
  documentation evidence, not as permission to change implementation.
- Treat `backend/app/` app wiring as active and `backend/worldengine/` as
  legacy unless a later reviewed contract says otherwise.
- Treat v0.2 schema/event contracts as additive foundations.
- Distinguish documented baseline from current-session verified behavior.
- Keep all examples domain-neutral.
- Do not edit code, tests, schemas, fixtures, migrations, API routes, or
  frontend files.

## Proposed Implementation

After documentation review approval:

1. Read current implementation, backend implementation, architecture, API,
   scope, roadmap, evidence, boundary, and completed v0.2 package review docs.
2. Inspect active and legacy path names with read-only commands to confirm
   documentation references.
3. Create `docs/legacy-boundary.md` / `.zh.md` with active path, legacy path,
   placeholder infrastructure, documentation, and future migration rules.
4. Create `docs/iterations/v0.2/compatibility-review.md` / `.zh.md` with a
   compatibility matrix for runtime, API, frontend, schema/event contracts,
   legacy paths, and v0.3 handoff constraints.
5. Update `findings.md` for unresolved compatibility evidence gaps, ambiguous
   boundaries, or status drift.
6. Run the documentation checks in `test-plan.md`.
7. Update this package's review files with exact commands, results,
   compatibility review, scope review, assumptions, and unresolved findings.

## Affected Surfaces

Documentation:

- `docs/legacy-boundary.md`
- `docs/legacy-boundary.zh.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/compatibility-review.zh.md`
- `docs/iterations/v0.2/findings.md`
- `docs/iterations/v0.2/0.2.10-legacy-boundary-and-compatibility-review/**`
- v0.2 milestone index and plan status fields.

No runtime, schema, API, frontend, fixture, migration, or test implementation
surface is affected.

## Data Model / Schema Changes

None.

## Runtime / Service Design

None.

## Compatibility

Runtime behavior, schema validation, event behavior, API response shapes,
frontend behavior, fixture behavior, migration behavior, and legacy
`backend/worldengine/` behavior remain unchanged.

The compatibility review may identify missing evidence or future bridge risks,
but it must not change implementation behavior to close those gaps.

## Assumptions

- Current implementation documentation is the correct baseline for v0.1
  behavior unless current-session verification proves drift.
- The compatibility review can use documentation evidence without rerunning
  backend/frontend tests, as long as it marks those claims accurately.
- Link/path checks can be performed with shell commands available in the
  repository environment.
- Backend/frontend tests are unnecessary unless implementation files change,
  which this package forbids.

## Risks

- Risk: compatibility language implies v0.2 schemas are already loaded by the
  runtime. Mitigation: every runtime-related statement must distinguish
  current v0.1 behavior from future v0.3 bridge work.
- Risk: legacy code inspection becomes refactor work. Mitigation: record
  boundaries and findings only.
- Risk: documentation evidence is stale. Mitigation: mark evidence source and
  verification status separately.
- Risk: English and Chinese status mirrors drift. Mitigation: status checks
  must cover both mirrors.
