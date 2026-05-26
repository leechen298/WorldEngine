# Legacy Boundary

Status: v0.2 compatibility boundary

This document defines which repository paths are active, legacy, placeholder,
documentation-only, or future bridge scope after 0.2.10. It does not change
runtime behavior.

## Status Key

- `active`: used by the current v0.1 runtime or dashboard path.
- `legacy`: retained code that is not wired into the active app.
- `placeholder`: structural interfaces or adapters that exist but are not the
  active persistence or runtime path.
- `documentation`: contracts, process, implementation maps, and review
  evidence.
- `future`: allowed only through a later reviewed package.

## Boundary Map

| Surface | Status | Evidence | Boundary |
|---|---|---|---|
| `backend/app/` | active | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md` | Active FastAPI backend, runtime scaffold, event log, world params flow, archive service, params-agent scaffold, schemas, and API routes. New runtime features must target this path unless a later contract says otherwise. |
| `frontend/` | active | `AGENTS.md`, `docs/current-implementation.md` | Active Vue dashboard. v0.2.10 does not change dashboard behavior. |
| `docs/` | documentation | iteration standard, contracts, implementation maps, review evidence | Source of project direction, current implementation descriptions, contracts, release drafts, and package evidence. Documentation can describe boundaries but does not itself prove runtime behavior unless backed by command evidence. |
| `backend/app/infra/ports` and `backend/app/infra/sqlite` | placeholder | `docs/backend-implementation.md` | Repository interfaces and SQLite adapters are present, but v0.1 runtime state, events, snapshots, and summaries remain in-memory. Do not treat these adapters as active persistence without a reviewed implementation package. |
| `backend/worldengine/` | legacy | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/architecture.md` | Pre-v0.1 code retained as historical implementation material. It is not wired into the active FastAPI app and must not receive new runtime features during v0.2. |
| `docs/contracts/*` | documentation / additive contracts | 0.2.7 and 0.2.8 reviews | EntityRef, WorldCell, WorldSpec, EventRef, and Event.refs contracts define schema/event foundations. They are not runtime loader or bridge behavior in v0.2. |
| external fixture or validation repositories | future external consumers | `docs/external-fixture-boundary.md` | May consume public APIs, schemas, CLI contracts, exported contracts, or redacted reports in future work. They are not part of the core repository. |

## Active Backend Boundary

The active backend is assembled by `backend/app/api/app_factory.py` and entered
through `backend/app/main.py`. The current v0.1 runtime model uses in-memory
singletons on `app.state`:

- event log.
- runtime state and engine.
- world params state.
- default world module tree.
- params validation and dry-run validation.
- snapshot and summary stores.
- archive service.
- params-agent scaffold.

0.2.10 does not add loaders, repositories, migrations, persistence behavior, or
runtime bridge wiring.

## Active Dashboard Boundary

The active dashboard is under `frontend/`. Current implementation docs describe
it as a Vue dashboard for health, runtime state, grouped event steps, world
params, params-agent proposals, placeholder agent state, snapshots, and
summaries.

0.2.10 does not change frontend files, UI behavior, API selectors, E2E tests,
or dashboard expectations.

## Legacy Backend Boundary

`backend/worldengine/` remains legacy. It may be read as historical context,
but it is not active runtime behavior and is not a source for new v0.2 features.

Rules:

- Do not add new runtime features under `backend/worldengine/`.
- Do not migrate or delete legacy files during v0.2.10.
- Do not infer active API behavior from legacy modules.
- Do not revive legacy NPC, environment, scheduler, HTTP server, or world state
  code without a later reviewed package.
- Future migration work must name the source behavior, compatibility target,
  and test evidence before moving anything into active paths.

## Placeholder Infrastructure Boundary

`backend/app/infra/ports` and `backend/app/infra/sqlite` are placeholders. They
show intended repository boundaries but are not active persistence for v0.1
runtime state, event storage, snapshots, or summaries.

Future persistence work must be additive or compatibility-preserving unless a
later reviewed contract explicitly approves a breaking change.

## v0.2 Foundation Boundary

v0.2 schema and event work is additive:

- `EntityRef` describes neutral references.
- `WorldCell` describes recursive world units.
- `WorldSpec` wraps a versioned recursive world specification.
- `EventRef` and optional `Event.refs` describe event-local references.

These contracts do not load WorldSpec data, replace `RuntimeEngine`, bind event
references to runtime objects, resolve causality, or create agent memory.

## Future Bridge Boundary

v0.3 may design WorldSpec loading or runtime bridge behavior only through a
separate reviewed package. That work must preserve or explicitly review:

- current runtime state and step behavior.
- current API response envelopes and endpoint shapes.
- current event storage, pagination, and grouped step behavior.
- world params validation and dry-run behavior.
- archive snapshot and summary behavior.
- frontend-facing compatibility.
- legacy path handling.

0.2.10 records the boundary. It does not approve the bridge.
