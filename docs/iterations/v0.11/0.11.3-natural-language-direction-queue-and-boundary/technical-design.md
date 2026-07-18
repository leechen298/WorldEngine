# Technical Design

Chinese mirror: `technical-design.zh.md`.

Status: documentation drafted / review pending

## Implementation Structure

The package adds an additive session-scoped wrapper around the existing world
direction classifier.

Expected endpoint shape:

```text
POST /sessions/{session_id}/directions
GET  /sessions/{session_id}/directions
```

`POST` receives the existing `WorldDirectionRequest`. It resolves the session,
classifies the instruction through `classify_world_direction`, and returns a
public response. If allowed, it stores a `WorldDirectionQueueItem` tied to the
session's `world_id`; if rejected, it increments rejected evidence without
creating a queued item.

`GET` returns a public session direction summary with queued items and rejected
count.

Both accepted and rejected submissions also create public operation evidence.
The evidence may use the existing event log style, but it must be redaction
safe and replayable by clients:

```text
world.session_direction.queued
world.session_direction.rejected
```

The payload includes session id, world id, instruction text length,
classification/status, `direct_state_mutation_applied: false`, timing metadata,
and public context keys only when classification is not redacted. Accepted
records include the generated direction id. Rejected records do not create a
queued item.

## Affected Files

Allowed implementation files:

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_session_direction_queue_api.py`
- existing focused compatibility tests when needed

Allowed documentation/status files:

- this package directory.
- `docs/iterations/v0.11/CURRENT_STATE.md`
- `docs/iterations/v0.11/CURRENT_STATE.zh.md`
- `docs/iterations/v0.11/README.md`
- `docs/iterations/v0.11/README.zh.md`
- `docs/iterations/v0.11/v0.11-plan.md`
- `docs/iterations/v0.11/v0.11-plan.zh.md`
- `docs/iterations/v0.11/review.md`
- `docs/iterations/v0.11/review.zh.md`

## Data / Control Flow

```text
client
  -> POST /sessions/{session_id}/directions
  -> session store resolves WorldSession
  -> classify_world_direction(...)
  -> if allowed:
       create WorldDirectionQueueItem
       append to session direction queue
       record public queued operation evidence
     else:
       increment rejected count
       record public rejected operation evidence
  -> return public response with direct_state_mutation_applied false
```

The public summary must never include raw instruction text. Redacted
classification results must suppress branch id and context keys, matching the
existing world-direction behavior.

## Compatibility Strategy

- Reuse existing direction request/classification/response models as much as
  possible.
- Keep all session changes additive.
- Keep existing world-direction endpoint behavior unchanged.
- Keep unknown-session handling aligned with existing session endpoints.
- Keep manifest additions additive and discoverable.
- Keep operation evidence replayable through public event/log inspection without
  raw instruction echo.
- Keep client status classification visible through public response and summary
  fields.

## Anti-Drift Rules

- Do not consume direction queue items in this package.
- Do not use direction guidance as an event result.
- Do not add concrete world content or demo story facts.
- Do not store raw instruction text.
- Do not add provider, Validation Client, persistence, migration, or
  `backend/worldengine/` work.
