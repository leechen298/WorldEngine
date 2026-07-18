# Technical Design

## Implementation Structure

Add:

- `backend/app/schemas/session.py`: pydantic session request/response models.
- `backend/app/core/world_session.py`: in-memory store and session construction
  helpers.
- `backend/app/api/routes/session.py`: public session endpoints.
- Router registration in `backend/app/api/routes/__init__.py` and
  `backend/app/api/app_factory.py`.

Update:

- `backend/app/api/routes/world.py` manifest surfaces.
- focused tests in `backend/app/tests/`.

## API Shape

```text
POST /sessions
GET /sessions
GET /sessions/{session_id}
GET /sessions/{session_id}/status
```

`POST /sessions` accepts optional `world_id` and optional public label. It
does not accept worldview prompts or provider data.

## Data / Control Flow

```text
POST /sessions
-> read current runtime state, event count, snapshot count
-> create in-memory WorldSessionRecord
-> return redacted public session payload
```

No tick runs, no snapshot is created, and no provider call happens.

## Compatibility Strategy

- Session APIs are additive new routes.
- Existing runtime/world APIs remain unchanged.
- Manifest keeps future run/snapshot surfaces as planned/not_run until later
  packages implement them.

## Anti-Drift Rules

- If implementation needs runtime execution, stop for `0.10.4`.
- If implementation needs worldview input, stop for `0.10.3`.
- If implementation needs frontend/dashboard, stop for `0.10.5`.
- If implementation needs persistence/migrations, stop as out of scope.
