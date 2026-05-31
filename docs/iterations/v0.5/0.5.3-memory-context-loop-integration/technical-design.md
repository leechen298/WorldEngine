# Technical Design

Status: review complete

## Current State

`0.5.2` added:

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`

Current loop/perception code:

- `PerceptionFrame` has runtime, params, recent events, and optional runtime
  context summary.
- `PerceptionBuilder` builds a read-only frame from runtime state, world params,
  recent events, and runtime context.
- `AgentLoopService.step` builds perception before applying the action intent.
- `ActionResultAdapter` owns action semantics and must stay unchanged.

## Contract Alignment And Invariants

- Memory context is read-only perception data.
- Loop action selection and action result behavior do not change.
- No public API route is added.
- No loop request field is added.
- No memory write occurs inside the loop step.
- Existing request validation and API envelope behavior remain compatible.

## Proposed Implementation

Add schema models in `backend/app/schemas/agent_loop.py`:

- `MemoryContextSummary` or equivalent containing bounded lists of working and
  episodic memory records.
- Optional `memory_context` field on `PerceptionFrame`.

Extend `PerceptionBuilder`:

- accept optional `memory_store`, `agent_id`, `world_id`, and memory limits.
- call `list_working_memory` and `list_episodic_memory` when a store is
  available.
- deep-copy model data into the perception frame.
- default to empty context or `None` without requiring callers to seed memory.

Wire `InMemoryAgentMemoryStore` in `create_app()` as internal state so the
route can expose seeded memory context in tests without adding a route.

## Affected Surfaces

- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_api.py`
- possibly `backend/app/tests/test_agent_loop_service.py`

## Data Model / Schema Changes

The only existing schema change is additive: `PerceptionFrame` gains optional
memory context. Existing request schemas and action/result schemas do not
change.

## Runtime / Service Design

Perception reads memory from the in-memory store using a deterministic default
agent/world scope. For this package, scope may be fixed to generic identifiers
unless the test design proves a safer existing source. The scope must be
documented and must not become a new public request parameter.

## Compatibility

Old loop requests remain valid. Old clients that ignore extra response fields
remain compatible. Strict validation for unknown loop request fields remains
unchanged.

## Anti-Drift Rules

- Do not add write paths.
- Do not change action adapter behavior.
- Do not introduce a public memory route.
- Keep memory context bounded by constants or constructor defaults.
- Keep `0.5.4` concepts contract-only in this package.

## Risks

- Risk: memory context changes action semantics.
  Detection: action adapter and loop service tests.
- Risk: mutable backing store leaks into perception.
  Detection: perception copy-isolation test.
- Risk: response shape changes become breaking.
  Detection: loop API compatibility tests.
