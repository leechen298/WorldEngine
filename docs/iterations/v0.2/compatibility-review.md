# v0.2 Compatibility Review

Status: 0.2.10 compatibility evidence

This review maps v0.1 runtime scaffold compatibility to v0.2 foundation work.
It distinguishes documented baseline, reviewed evidence, current-session path
checks, planned future work, non-implemented behavior, legacy code, and
findings. It does not change code.

## Status Key

- `documented`: described by current implementation, backend, API, architecture,
  contract, or boundary docs.
- `reviewed`: covered by completed package review evidence.
- `current-session verified`: checked by read-only commands in this 0.2.10
  session.
- `planned`: future roadmap or package scope.
- `not implemented`: explicitly outside current implementation.
- `legacy`: present only outside active wiring.
- `finding`: unresolved risk recorded in `docs/iterations/v0.2/findings.md`.

## Evidence Inputs

- `AGENTS.md`
- `CLAUDE.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/architecture.md`
- `docs/scope-boundaries.md`
- `docs/external-fixture-boundary.md`
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/boundary-audit.md`
- completed v0.2 package reviews through 0.2.9
- current-session path checks for `backend/app/`, `frontend/`, and
  `backend/worldengine/`

## Compatibility Matrix

| Surface | Compatibility claim | Evidence | Status | 0.2.10 result |
|---|---|---|---|---|
| Active backend path | `backend/app/` remains the active backend. | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md`; current-session file listing. | documented / reviewed / current-session verified | Preserved. No backend files changed. |
| Runtime state | Runtime keeps `tick_id`, `world_time_seconds`, `step_seconds`, and `updated_at` as the current scaffold state. | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`; completed code-package reviews. | documented / reviewed | Preserved as documented baseline. Not rerun in this docs-only package. |
| Runtime step behavior | `/runtime/step` manually advances one step, appends `tick.advanced`, runs modules, may trigger archive callbacks, and returns runtime state. | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`. | documented / reviewed | Preserved. No runtime implementation changed. |
| Event timeline | `/world/events` and `/world/event-steps` keep current newest-first pagination and grouped tick behavior. | `docs/api-reference-v0.1.md`, `docs/backend-implementation.md`, 0.2.3 and 0.2.8 event compatibility reviews. | documented / tested / reviewed | Preserved. v0.2 event refs remain optional additive schema data. |
| World params | `/world/params` and `/world/params/apply` keep current writable path, reserved prefix, static validation, dry-run validation, and event behavior. | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`. | documented / reviewed | Preserved. No params code or tests changed. |
| Params-agent scaffold | `/world/agent/params/propose-and-apply` remains a params proposal and validation loop, not an agent-in-world cognition loop. | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`. | documented / reviewed | Preserved. Agent pseudo-self and memory remain future scope. |
| Archive snapshots and summaries | Archive remains callback-driven with in-memory snapshot and summary stores. | `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`. | documented / reviewed | Preserved. No archive implementation changed. |
| API envelope | Successful responses keep `{ "code": 0, "data": ..., "msg": "ok" }`; error mappings remain documented v0.1 behavior. | `docs/backend-implementation.md`, `docs/api-reference-v0.1.md`. | documented | Preserved as documented baseline. Current-session endpoint smoke was not run. |
| Frontend expectations | Dashboard consumes health, runtime state, grouped event steps, world params, params-agent flow, placeholder agent state, and latest summary. | `docs/current-implementation.md`; current-session `frontend/` path check. | documented / current-session verified | Preserved. No frontend files changed. |
| Schema foundations | EntityRef, WorldCell, and WorldSpec are additive schema contracts, not runtime loading behavior. | `docs/contracts/entity-ref-contract.md`, `docs/contracts/worldcell-contract.md`, `docs/contracts/worldspec-contract.md`, 0.2.7 review. | implemented / documented / tested / reviewed | Preserved. No schema files changed. |
| Event reference foundations | EventRef and optional `Event.refs` remain additive event-local references. | `docs/contracts/event-ref-contract.md`, 0.2.3 and 0.2.8 reviews. | implemented / documented / tested / reviewed | Preserved. No resolver, causality engine, or runtime binding added. |
| Legacy backend | `backend/worldengine/` remains legacy and unwired. | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/architecture.md`; current-session path check. | documented / legacy / current-session verified | Preserved. No legacy files changed. |
| Placeholder infrastructure | `backend/app/infra/ports` and `backend/app/infra/sqlite` remain placeholder repository infrastructure. | `docs/backend-implementation.md`; current-session path check. | documented / current-session verified | Preserved. Not active persistence. |
| External fixtures | Concrete external fixture and validation worlds remain outside core. | `docs/external-fixture-boundary.md`, 0.2.5 review, 0.2.9 boundary audit. | documented / reviewed / tested | Preserved. No external repository or fixture internals added. |

## v0.3 Handoff Constraints

Future bridge work must not use v0.2 contracts as implicit runtime behavior.
A v0.3 loader or bridge package must explicitly cover:

- WorldSpec loading entry points and failure behavior.
- Runtime state compatibility and migration rules.
- API envelope and endpoint compatibility.
- Event append, storage, pagination, grouping, and optional refs
  compatibility.
- World params coexistence or migration behavior.
- Archive snapshot and summary compatibility.
- Frontend-facing behavior and dashboard regression evidence.
- Legacy `backend/worldengine/` handling.
- Persistence expectations if placeholder infrastructure becomes active.

The current-session docs-only review did not run backend, frontend, API, or E2E
tests. That evidence gap is tracked as `v0.2-P3-003` for the first v0.3 bridge
package that proposes behavior changes.

## Compatibility Assessment

0.2.10 preserves v0.1 compatibility by making documentation-only changes. It
does not edit runtime, schema, API, frontend, fixture, migration, test, or
legacy implementation files.

Current-session verification is limited to documentation checks and read-only
path inspection. Runtime and frontend behavior remain documented and previously
reviewed, but not re-executed during this package.

## Scope Assessment

The package stays inside v0.2 Recursive World Foundation scope:

- active runtime behavior remains v0.1 scaffold behavior.
- v0.2 schema and event contracts remain additive.
- `backend/worldengine/` remains legacy.
- v0.3 bridge work remains planned and unimplemented.
- no concrete external-world anchors are introduced.
