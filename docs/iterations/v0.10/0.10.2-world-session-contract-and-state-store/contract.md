# Contract

## Public Concepts

- `world_session`: a public MVP runtime unit with stable `session_id`,
  associated `world_id`, public lifecycle status, runtime reference, event
  count, snapshot count, and timestamps.
- `session_status`: one of `created`, `ready`, `blocked`, or `closed`.
- `session_runtime_ref`: public reference to the current runtime tick/time,
  not a private runtime object.
- `session_evidence_refs`: public counts or ids for events and snapshots
  associated with the session.

## Compatibility Requirements

- Existing `/worlds`, `/runtime/*`, `/world/events`, `/manifest`, and provider
  surfaces remain additive-compatible.
- Session payloads must not expose raw prompts, provider traces, secrets,
  private Agent memory, hidden context, or private evaluator data.
- Session store is process-local in-memory only; no persistence guarantee.
- Manifest updates must honestly describe session runtime/run/snapshot
  capabilities that remain future scope.

## Allowed Changes

- Add session schema/store/router and focused tests in the allowed file list.
- Register the session router in the app factory.
- Update manifest surfaces for session create/list/read/status.
- Update package and parent v0.10 docs/reviews.

## Forbidden Changes

- Do not implement session run controls, bounded runtime wrappers, snapshot
  generation, worldview generation, dashboard UI, durable storage, migrations,
  checker fixtures, provider live calls, Validation Client code, generated
  results, external validation, or `backend/worldengine/`.
- Do not claim runnable session flow PASS beyond create/list/read/status.

## North Star Check

This package keeps WorldEngine generic by defining a reusable public session
unit rather than application-specific state or external-client-owned behavior.

## Out-of-Scope Follow-ups

- `0.10.3`: create sessions from worldview input.
- `0.10.4`: run sessions and collect snapshot evidence.
- `0.10.5`: dashboard session flow.
