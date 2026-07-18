# Contract

## Public Concepts

- `worldview_session_creation`: creating a session from public worldview input
  and redacted generation output.
- `session_generation_summary`: public generation status, mode, provider
  class, fallback labels, generation id, and premise digest.
- `runtime_ready_session`: a session whose public generated model is attached
  enough for later runtime packages to inspect, not a session that has run.

## Compatibility Requirements

- Existing `/sessions` create/list/read/status behavior remains compatible.
- Existing `/world/generation/worldview` behavior remains compatible.
- Provider configured states that would require live calls must remain
  `blocked`, not silently executed.
- Fallback must be labeled deterministic or safe mock and non-live.

## Allowed Changes

- Extend session schemas/store/routes for worldview session creation.
- Reuse existing worldview generation helper.
- Update manifest and focused tests.
- Update package and parent v0.10 docs/reviews.

## Forbidden Changes

- Do not execute live provider calls.
- Do not run runtime ticks, create snapshots, write generated results, add
  dashboard UI, modify checker fixtures, implement Validation Client behavior,
  add persistence/migrations, or change `backend/worldengine/`.

## North Star Check

This keeps WorldEngine as provider/generation owner while exposing only
redacted public session evidence to clients.

## Out-of-Scope Follow-ups

- `0.10.4`: bounded runtime and snapshot evidence.
- `0.10.5`: dashboard MVP session flow.
