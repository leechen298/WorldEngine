# Technical Design

## Implementation Structure

- Add request/summary models in `backend/app/schemas/session.py`.
- Add a store method that creates a session from a supplied world id and
  public generation metadata.
- Add `POST /sessions/from-worldview` in `backend/app/api/routes/session.py`.
- Reuse `generate_worldview_response()` and `provider_readiness_from_env()`
  without changing the generation route.
- Update `/manifest` session-from-worldview discovery metadata.

## Affected Files

Implementation files:

- `backend/app/schemas/session.py`: add worldview-session request and public
  generation summary fields.
- `backend/app/core/world_session.py`: add creation helper that stores
  generation summary metadata on a session.
- `backend/app/api/routes/session.py`: add `POST /sessions/from-worldview`
  route that reuses existing generation helpers.
- `backend/app/api/routes/world.py`: update manifest discovery, blockers, and
  unsupported-item metadata for session-from-worldview availability.

Focused test files:

- `backend/app/tests/test_world_session_api.py`: add worldview-to-session
  creation, redaction, blocked-provider, and no-runtime-run assertions.
- `backend/app/tests/test_public_handoff_contract_api.py`: update manifest
  discovery expectations for the new session-from-worldview surface.

Package / route documentation:

- `docs/iterations/v0.10/0.10.3-worldview-to-runtime-session-creation/*`
- v0.10 parent route/review files as needed for closeout handoff.

## API Shape

```text
POST /sessions/from-worldview
```

Request includes `worldview_premise`, optional public constraints, and
`allow_deterministic_fallback`. It must not accept raw provider payloads.

## Data / Control Flow

```text
request
-> provider_readiness_from_env()
-> generate_worldview_response()
-> create in-memory session using generated world_id
-> return session with redacted generation summary
```

No runtime tick, snapshot, provider live call, checker result, or external
client action occurs.

## Compatibility Strategy

Keep existing session creation and generation APIs unchanged. New behavior is
additive.

## Anti-Drift Rules

Stop if implementation requires runtime run, dashboard, provider live calls,
checker fixtures, persistence, or external repositories.
