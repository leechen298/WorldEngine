# Contract

Chinese mirror: `contract.zh.md`.

## UI Contract

The dashboard must expose a visible MVP session flow:

- worldview premise input.
- create-session action backed by `POST /sessions/from-worldview`.
- current session id, world id, status, generation mode/status, and runtime ref.
- bounded run action backed by `POST /sessions/{session_id}/run`.
- pause and resume actions backed by session-scoped controls.
- snapshot evidence list backed by `GET /sessions/{session_id}/snapshots`.
- timeline refresh from existing public event-step APIs.

## API Client Contract

Frontend API methods must use public backend routes only. Request and response
types must model public session fields and avoid raw/private provider data.

## Evidence Contract

Tests must prove:

- dashboard renders the session shell.
- create-from-worldview calls the public API and displays returned session data.
- bounded run calls the session run API and refreshes runtime/timeline/snapshot
  state.
- pause/resume controls call session-scoped APIs.
- E2E smoke can drive create/run/inspect when the backend and dev server are
  available.

## Compatibility Contract

Existing dashboard panels should remain available or be integrated into the
session shell. Existing runtime step behavior must not be broken unless it is
explicitly superseded by session run controls in tests and UI.

## Forbidden Claims

The dashboard must not claim live provider quality, external Validation Client
PASS, Agent autonomy, product release readiness, or durable persistence.
