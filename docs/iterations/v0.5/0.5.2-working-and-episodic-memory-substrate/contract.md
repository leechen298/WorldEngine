# Contract

Status: review complete

## Public Concepts

This package implements only two concept families from `0.5.1`:

- `WorkingMemoryRecord`: bounded current-context memory with provenance.
- `EpisodicMemoryRecord`: event-linked experience memory with provenance and
  world-time/tick evidence.

The implementation may also define small support types such as a memory
source enum/value, evidence reference model, or bounded context model if they
remain generic and internal to backend schemas.

## Schema Semantics

Working memory records must include:

- stable `memory_id`.
- `agent_id` and `world_id`.
- textual `content`.
- `source` and provenance/evidence metadata.
- `created_at` and `updated_at`.
- bounded-context metadata such as `priority` and optional expiration/tick
  window.

Episodic memory records must include:

- stable `memory_id`.
- `agent_id` and `world_id`.
- textual `summary`.
- `event_refs`.
- `tick` and `world_time_seconds`.
- `source`, optional action/outcome references, and `created_at`.

The exact Python model names may vary if the technical design records the
equivalent semantics.

## Service Semantics

The in-memory substrate must:

- store records in process memory only.
- scope reads by `agent_id` and `world_id`.
- return deep copies or immutable copies so callers cannot mutate backing
  state.
- provide bounded working-memory selection with deterministic ordering.
- provide episodic listing by agent/world scope with deterministic ordering.
- avoid app wiring or route exposure in this package.

## Compatibility Requirements

- Existing v0.4 Agent Loop requests and responses remain unchanged.
- `PerceptionFrame`, `LoopStepRequest`, `ActionIntent`, `ActionResult`, and
  `POST /world/agent/loop/step` must not change in this package.
- Existing `/world/agent/params/propose-and-apply`, event routes, runtime
  state/step, params behavior, archive behavior, API envelope/error shape, and
  optional `Event.refs` serialization must remain compatible.
- Schema additions are additive and do not alter existing models.

## Allowed Changes

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_*.py`
- Package docs and mirrors under
  `docs/iterations/v0.5/0.5.2-working-and-episodic-memory-substrate/`
- Parent v0.5 status/review surfaces only for accurate handoff.

## Forbidden Changes

- Do not modify `backend/worldengine/**`.
- Do not modify frontend files.
- Do not add or change API routes.
- Do not modify `LoopStepRequest`, `ActionIntent`, `ActionResult`, action
  adapter semantics, `params.patch` validation semantics, event behavior,
  runtime tick behavior, or API envelope/error behavior.
- Do not add durable persistence, migrations, vector search, summarization,
  relationship state behavior, reflection automation, personality drift
  action modifiers, concrete world content, external validation internals, or
  application-specific backend logic.

## Implementation Authorization Criteria

Implementation may start only after:

- all package docs and Chinese mirrors exist.
- documentation/contract evaluator reports no P1 and no blocking P2.
- `review.md` records `implementation_authorized: yes`.
- the first production change is preceded by a failing focused backend test.

## North Star Check

The implementation is generic memory substrate work for agents living inside
worlds. It remains inspectable, scoped, and non-public; it does not add
demo-world behavior, projection application behavior, or consciousness claims.

## Out-of-Scope Follow-ups

- `0.5.3`: bounded read-only memory context in Agent Loop perception.
- `0.5.4`: relationship, self-summary, reflection, and drift contract
  follow-up.
- Later versions: durable persistence, retrieval indexing, generation,
  external validation readiness, and projection application readiness.
