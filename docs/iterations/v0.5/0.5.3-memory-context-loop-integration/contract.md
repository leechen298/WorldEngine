# Contract

Status: review complete

## Public Concepts

- `MemoryContext`: bounded, read-only perception data assembled from
  working-memory and episodic-memory records.
- `working_memory`: current-context memory entries included in perception.
- `episodic_memory`: event-linked memory entries included in perception.

The memory context is perception data only. It is not an action modifier.

## Allowed Changes

- Add additive memory context schema models or fields in
  `backend/app/schemas/agent_loop.py`.
- Extend `backend/app/agent/perception.py` to accept an optional memory store
  and build bounded read-only memory context.
- Wire `InMemoryAgentMemoryStore` into `backend/app/api/app_factory.py` only as
  internal app state used by perception.
- Update loop/perception/API tests under `backend/app/tests/`.
- Update package docs and parent v0.5 status/review surfaces for handoff.

## Forbidden Changes

- Do not modify `ActionIntent`, `ActionResult`, accepted action types, action
  adapter behavior, or params patch semantics.
- Do not add public memory APIs.
- Do not add loop request memory selectors.
- Do not write memory during `AgentLoopService.step`.
- Do not add durable persistence, migrations, frontend behavior, concrete
  world content, external validation internals, relationship behavior,
  self-summary generation, automatic reflection, or personality drift action
  modifiers.
- Do not modify `backend/worldengine/**`.

## Compatibility Requirements

- Existing loop callers must continue to work without sending new fields.
- Existing loop request validation remains strict for unknown request fields.
- Existing action and result schemas remain unchanged.
- API envelope and error behavior remain unchanged.
- Memory context must be bounded and must not expose mutable backing store
  state.
- The default app may expose an empty memory context unless tests seed the
  store directly.

## Implementation Authorization Criteria

Implementation may start only after:

- all package docs and Chinese mirrors exist.
- documentation/contract evaluator reports no P1 and no blocking P2.
- `review.md` records `implementation_authorized: yes`.
- a focused failing test exists and is run before production code changes.

## North Star Check

This package supports memory-shaped perception while keeping WorldEngine
generic. It does not add concrete world data, application behavior, or
consciousness claims.

## Out-of-Scope Follow-ups

- `0.5.4`: relationship, self-summary, reflection, and drift contract follow-up.
- Later packages: behavior changes based on memory, persistence, retrieval
  indexing, generation, validation readiness, and projection readiness.
