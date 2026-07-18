# Contract

Chinese mirror: `contract.zh.md`.

Status: documentation drafted / review pending

## Public Concepts

- **Session direction**: a user-provided natural-language instruction attached
  to a WorldSession and evaluated as world-level guidance.
- **Queued direction**: an accepted public guidance item that may influence
  later event candidate generation, probability, environmental trend, rule
  constraint, or future evaluation.
- **Rejected direction**: a disallowed instruction that attempted direct final
  facts, Agent private-state mutation, Agent goal mutation, inventory
  injection, relationship override, rule bypass, or private marker exposure.
- **Direction boundary**: the rule that user guidance never directly mutates
  world state, final facts, Agent private state, Agent goals, inventory,
  relationships, or event results.
- **Replayable operation record**: a public, redacted operation-log/event-style
  record that lets a client reconstruct that a direction was queued or rejected
  without exposing raw instruction text or private context.
- **Client status classification**: the public queued/rejected direction status,
  classification category, and direct-mutation flag that external consumers can
  inspect without running hidden logic.

## Allowed Changes

After review approval, this package may change:

- `backend/app/schemas/session.py` for additive session direction summary
  response models or session fields.
- `backend/app/core/world_session.py` for in-memory session direction queue
  storage and summary helpers.
- `backend/app/api/routes/session.py` for additive
  `POST /sessions/{session_id}/directions` and
  `GET /sessions/{session_id}/directions` endpoints.
- `backend/app/api/routes/world.py` only for public manifest/discovery entries.
- focused backend tests for session direction queue behavior, existing world
  direction compatibility, manifest compatibility, and redaction.
- public operation evidence for accepted and rejected session directions, using
  redacted event-style records that include session id, world id, direction id
  when accepted, status/classification, timing metadata, public context keys
  when not redacted, instruction length, and
  `direct_state_mutation_applied: false`.
- client-readable status classification in session direction responses and
  summaries.
- active package docs and v0.11 route/review status docs.

The implementation must reuse the existing `WorldDirectionRequest`,
`WorldDirectionResponse`, `WorldDirectionQueueItem`, and
`classify_world_direction` semantics unless a review-approved design update
explicitly changes that.

## Forbidden Changes

This package must not:

- implement rule-compliant event generation, state diffs, or event application.
- allow direct final fact commands such as "kill this Agent now".
- turn lightning-risk guidance into an outcome; it may only become external
  pressure.
- mutate Agent private memory, goals, self-state, relationships, inventory,
  injury, death, or location from direction guidance.
- add player item drops, direct detailed event triggers, or
  player-as-world-entity gameplay.
- bypass public rules, state, probability, time, location, or legality checks.
- expose raw instruction text in public event payloads or summaries.
- expose secrets, raw provider traces, raw prompts, raw responses, hidden
  context, or private evaluator data.
- add provider calls, external Validation Client calls, persistence, migrations,
  concrete demo-world fixtures, or `backend/worldengine/` changes.

## Compatibility Requirements

- Existing `/worlds/{world_id}/direction` behavior and tests must remain
  compatible.
- Existing session create, worldview-to-session, rule attach/read, run, status,
  events, and snapshot APIs must remain additive-compatible.
- Direction queue responses must remain public and redaction-safe.
- Rejected directions must not create queued items and must report
  `direct_state_mutation_applied: false`.
- Accepted and rejected session directions must produce replayable public
  operation evidence without raw instruction echo.
- Client consumers must be able to distinguish queued and rejected guidance from
  public status/classification fields.
- Unknown sessions must return the existing session 404 behavior.

## Out-Of-Scope Follow-Ups

- `0.11.4` owns event candidate generation, legality evaluation, diff
  application, direction consumption, and replay evidence.
- `0.11.5` owns worldview fidelity validation and v0.11 closeout.
- `v0.12` owns Agent continuity and external automated validation integration.
