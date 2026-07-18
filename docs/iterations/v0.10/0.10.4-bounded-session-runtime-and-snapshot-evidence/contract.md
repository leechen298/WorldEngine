# Contract

Chinese mirror: `contract.zh.md`.

## Public API Contract

Additive endpoints:

- `POST /sessions/{session_id}/run`
- `POST /sessions/{session_id}/pause`
- `POST /sessions/{session_id}/resume`
- `GET /sessions/{session_id}/snapshots`

`POST /sessions/{session_id}/run` accepts the existing bounded
`RuntimeRunRequest` shape. Requests remain invalid when they omit both
`ticks` and `duration_seconds`, supply both, or exceed guard fields.

Unknown session ids return the existing public 404 envelope.

## Session Evidence Contract

Run responses must include public evidence only:

- session id.
- run status and stop reason.
- runtime start/end tick and world time.
- ticks executed.
- event count before/after and event delta count.
- snapshot count before/after and snapshot delta count.
- snapshot ids created or visible for the run window.
- timeline label using branch-ready wording without parent/source hierarchy.
- guard summary and cost counters inherited from runtime summary.

Snapshot list responses must be public, bounded, and redacted. They may expose
snapshot ids, tick ids, world time, created_at, runtime state, and public params.

## Compatibility Contract

Existing `/runtime/state`, `/runtime/step`, `/runtime/run`, `/runtime/pause`,
and `/runtime/resume` endpoints must remain compatible. Session-scoped routes
wrap the same in-memory runtime engine; they do not create a durable or
multi-runtime architecture in this package.

## Forbidden Claims

The package must not claim:

- live provider pass.
- external checker pass.
- dashboard pass.
- durable persistence.
- Agent autonomous behavior.
- replay hierarchy with parent/source worlds.
