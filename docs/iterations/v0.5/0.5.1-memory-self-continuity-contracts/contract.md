# Contract

Status: review complete

## Public Concepts

### Working Memory

Working memory is a bounded, current-context memory record for an agent inside
a world. It is intended for short-lived facts, observations, intentions, or
operator-provided notes that may be useful during near-term loop perception.

Required semantics:

- every record has `agent_id`, `world_id`, stable `memory_id`, `content`,
  `source`, `created_at`, and `updated_at` semantics.
- records must carry provenance that explains whether the memory came from an
  observed event, action result, operator input, system import, or derived
  process.
- records must have explicit bounded-lifetime semantics such as priority,
  ttl/tick window, expiration, or max-context selection. The first
  implementation may use simple in-memory bounded selection, but it must not
  imply durable persistence.
- records are generic. They must not encode concrete world names, characters,
  maps, resources, story rules, or validation-oracle details.

### Episodic Memory

Episodic memory is an event-linked record of an agent experience. It captures
what happened, when it happened, which world/event/action evidence it is tied
to, and why the episode is available for later review.

Required semantics:

- every record has `agent_id`, `world_id`, stable `memory_id`, `summary`,
  `event_refs`, `tick`, `world_time`, `source`, `created_at`, and optional
  outcome or action-result references.
- event and action references must use generic identifiers and optional
  `Event.refs`-compatible references when available.
- episodes are inspectable evidence records, not hidden behavior modifiers.
- the first implementation may store episodes in memory only. Durable
  persistence, indexing, vector retrieval, summarization, and external
  validation automation are out of scope.

### Relationship State

Relationship state is a structured, inspectable representation of an agent's
relationship to another agent, entity, or world reference.

Required semantics:

- planned records identify subject agent, target reference, relationship
  dimensions, provenance, and updated time.
- relationship state is contract/schema semantics only in v0.5 until a later
  reviewed package explicitly authorizes behavior.
- relationship state must not change action semantics in this package or in
  `0.5.2`.

### Self-Summary

Self-summary is an inspectable summary of an agent's continuity state, such as
stable identity notes, current goals, memory-derived themes, or operator
review notes.

Required semantics:

- planned records identify agent, world, summary text or structured facets,
  provenance, created/updated time, and evidence references.
- self-summary generation is not implemented in this package.
- no automatic summarization, LLM call, or action modifier is authorized.

### Reflection Record

Reflection record is a reviewable record of self-assessment, feedback
processing, or decision review for an agent.

Required semantics:

- planned records identify agent, world, trigger, reflection content, evidence
  references, created time, and source.
- automatic reflection behavior is not implemented in this package.
- reflection records must be auditable and must not silently rewrite memory or
  action behavior.

### Personality Drift Signal

Personality drift signal is an inspectable signal that may later describe a
change in behavioral tendency, preference, or decision pattern.

Required semantics:

- planned records identify agent, world, signal dimension, direction,
  strength, evidence references, source, and created time.
- drift signals do not change action selection in this package.
- any future action-modifier behavior requires a later reviewed package.

## Authorization Criteria For `0.5.2`

`0.5.2-working-and-episodic-memory-substrate` may implement only after all of
these are true:

- its package contains README, intent, contract, technical-design, test-plan,
  plan, review, and Chinese mirrors.
- its contract limits implementation to additive generic working-memory and
  episodic-memory schemas, a generic in-memory substrate, and focused backend
  tests.
- a documentation/contract evaluator reports no P0/P1 and no blocking P2.
- `0.5.2/review.md` records `implementation_authorized: yes`.
- the planned tests include focused memory tests, adjacent v0.4 loop/API
  compatibility tests, docs/mirror checks, and changed-file scope guard.

## Compatibility Requirements

- Preserve v0.4 `PerceptionFrame`, `ActionIntent`, `ActionResult`,
  request-scoped `LoopStep`, and `POST /world/agent/loop/step` behavior.
- Preserve `/world/agent/params/propose-and-apply`, runtime tick/time,
  event routes, params behavior, archive behavior, API envelope/error shape,
  and optional `Event.refs` serialization.
- Planned schema changes must be additive.
- Historical v0.4 evidence remains handoff context only and is not current
  v0.5 pass evidence.

## Allowed Changes

- Create and update docs under
  `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/`.
- Update parent v0.5 status surfaces only for accurate child status handoff.
- Define public concept contracts, planned schema semantics, compatibility
  requirements, and implementation authorization criteria.
- Record read-only evaluator findings and documentation verification evidence.

## Forbidden Changes

- Do not modify `backend/app/**`, `backend/worldengine/**`, `frontend/**`,
  migrations, fixtures, generated results, external repositories, or backend
  tests.
- Do not create `backend/app/schemas/agent_memory.py`,
  `backend/app/agent/memory.py`, or any `test_agent_memory_*.py` file.
- Do not add runtime APIs, persistence, vector search, LLM summarization,
  reflection automation, relationship behavior, personality drift action
  modifiers, frontend behavior, or world generation.
- Do not add concrete world content or private validation oracle details.

## North Star Check

This package advances the north-star pseudo-self direction by making memory,
relationship, reflection, self-summary, and drift inspectable engineering
contracts. It keeps the engine generic and does not narrow the repository into
a game, demo, or projection application backend.

## Out-of-Scope Follow-ups

- `0.5.2`: implement working/episodic memory schemas and in-memory substrate.
- `0.5.3`: add bounded read-only memory context to loop perception.
- `0.5.4`: refine relationship/self-summary/reflection/drift contracts and
  decide whether schema-only implementation is still deferred.
- v0.6: world generation.
- v0.7: external validation readiness and report automation.
- v0.8: projection application readiness.
