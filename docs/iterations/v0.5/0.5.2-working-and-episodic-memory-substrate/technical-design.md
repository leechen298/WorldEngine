# Technical Design

Status: review complete

## Current State

Relevant current backend files:

- `backend/app/schemas/agent_loop.py` defines `PerceptionFrame`,
  `ActionIntent`, `ActionResult`, `LoopStepRequest`, and `LoopStepResponse`.
- `backend/app/agent/perception.py` builds bounded read-only perception frames.
- `backend/app/agent/loop_service.py` builds perception before applying action.
- `backend/app/agent/action_adapter.py` accepts only `noop` and `params.patch`.
- `backend/app/api/routes/world_agent.py` exposes
  `POST /world/agent/loop/step`.
- `backend/app/tests/test_agent_perception.py`,
  `test_agent_loop_service.py`, and `test_agent_loop_api.py` cover adjacent
  compatibility behavior.

No memory schema or substrate module exists yet.

## Contract Alignment And Invariants

This package must preserve:

- no changes to existing loop schemas.
- no changes to action semantics.
- no new API route.
- no app factory wiring requirement.
- no durable persistence.
- no `backend/worldengine/` changes.

## Proposed Implementation

Add `backend/app/schemas/agent_memory.py` with Pydantic models:

- `MemoryEvidenceRef`: generic evidence reference with `type`, `id`, and
  optional metadata.
- `WorkingMemoryRecord`: agent/world-scoped current-context record.
- `EpisodicMemoryRecord`: agent/world-scoped event-linked record.

Add `backend/app/agent/memory.py` with:

- `InMemoryAgentMemoryStore`.
- `add_working_memory(record)`.
- `add_episodic_memory(record)`.
- `list_working_memory(agent_id, world_id, limit=None)`.
- `list_episodic_memory(agent_id, world_id, limit=None)`.
- deterministic ordering and copy isolation.

The store should be intentionally simple. It is not wired into app state in
this package because there is no public consumer until `0.5.3`.

## Affected Surfaces

Implementation surfaces:

- new schema module: `backend/app/schemas/agent_memory.py`.
- new service module: `backend/app/agent/memory.py`.
- new focused tests: `backend/app/tests/test_agent_memory_substrate.py`.

Adjacent verification surfaces:

- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_service.py`
- `backend/app/tests/test_agent_loop_api.py`
- `backend/app/tests/test_agent_action_adapter.py`

## Data Model / Schema Changes

All schema changes are additive because they introduce a new module and do not
modify existing models.

Record identifiers are strings, timestamps are strings compatible with the
existing schema style, and evidence references are generic dictionaries or
typed models. The substrate must not store concrete world data.

## Runtime / Service Design

The in-memory store keeps separate internal lists for working and episodic
records. Reads filter by `agent_id` and `world_id`.

Working memory deterministic ordering:

1. higher `priority` first.
2. newer `updated_at`/`created_at` first where comparable.
3. stable `memory_id` tie-breaker.

Episodic memory deterministic ordering:

1. higher `tick` first.
2. higher `world_time_seconds` first.
3. newer `created_at` first.
4. stable `memory_id` tie-breaker.

The store returns deep model copies to protect backing state.

## Compatibility

Because the package adds modules without wiring them into the loop/API, old
requests and old responses remain unchanged. Adjacent tests must confirm
perception, loop service, loop API, and action adapter behavior still pass.

## Anti-Drift Rules

- Keep implementation limited to the new memory schema, new memory store, and
  focused memory tests.
- Do not introduce API routes, app factory wiring, loop integration, or request
  schema fields in this package.
- Do not describe the substrate as durable persistence, vector retrieval, or
  summarization.
- Keep relationship state, self-summary, reflection, and personality drift as
  follow-up contract work unless a later reviewed package authorizes code.
- Treat previously closed `0.5.0` and `0.5.1` status updates as campaign
  handoff context, not as implementation scope for `0.5.2`.

## Risks

- Risk: memory substrate becomes public API.
  Detection: changed-file review and API tests.
- Risk: store exposes mutable backing state.
  Detection: focused copy-isolation test.
- Risk: deterministic bounds are unstable.
  Detection: ordered bounded-list tests.
- Risk: action behavior changes accidentally.
  Detection: adjacent loop/action tests.
