# Technical Design

Chinese mirror: `technical-design.zh.md`.

Status: documentation drafted / review pending

## Implementation Structure

The package keeps the existing manual event evaluator and adds a session-scoped
evolution step:

```text
POST /sessions/{session_id}/evolution/step
```

The session step is deterministic. It uses the accepted public rule set
attached to the session, the session direction queue, current runtime tick/time,
and current public parameters to build one public `WorldEventCandidate`. The
candidate then goes through `evaluate_world_event_candidate`. Only an accepted
candidate with a public `state_diff` may be applied.

## Affected Files

Allowed implementation files:

- `backend/app/schemas/world_evolution.py`
- `backend/app/core/rule_linked_evolution.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_session_rule_bound_evolution_api.py`
- existing focused compatibility tests when required

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
  -> POST /sessions/{session_id}/evolution/step
  -> resolve WorldSession
  -> require accepted public rule set
  -> inspect queued public directions
  -> deterministically build/select one public candidate
  -> evaluate_world_event_candidate(...)
  -> if accepted and apply=true:
       apply public ParamPatchItem list to WorldState
       append world.session_evolution.accepted event
     else:
       append world.session_evolution.rejected or blocked evidence
  -> return public result with candidate, legality, diff, and replay refs
```

Candidate selection must be simple and explainable. It may choose the highest
priority accepted rule and its first public target parameter, derive the next
bounded public value from current state and rule constraints, and attach the
first currently applicable queued direction id. It must not use unbounded
randomness, provider output, hidden evaluator data, or raw instruction text.

## Compatibility Strategy

- Reuse existing `WorldEventCandidate`, `WorldEventEvaluationRequest`, and
  `evaluate_world_event_candidate` semantics.
- Keep manual world-level evaluation compatible.
- Keep session changes additive.
- Keep event-log replay records additive.
- Use public blocked/not-ready responses when a session lacks attached accepted
  rules or no legal candidate can be generated.

## Anti-Drift Rules

- Do not implement multiple-step narrative simulation.
- Do not consume/dequeue directions unless the contract is updated and reviewed.
- Do not mutate private Agent state.
- Do not introduce provider calls or external validation.
- Do not add concrete world fixtures.
