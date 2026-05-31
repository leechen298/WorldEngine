# Contract

Status: review complete

## Package Decision

`0.5.4` is documentation-only. It refines schema semantics and authorization
criteria, but it does not add schema files or backend behavior.

Implementation authorization remains `no`.

## Relationship State

Relationship state is an inspectable description of how an agent is related to
another generic target reference.

Required semantics for any future schema:

- identify `agent_id`, `world_id`, stable relationship record id, and generic
  `target_ref`.
- use generic relationship dimensions such as familiarity, trust, obligation,
  alignment, conflict, or affinity without encoding concrete characters,
  locations, factions, resources, or story rules.
- include provenance and evidence references for observed events, operator
  review, imported state, or derived analysis.
- include `created_at`, `updated_at`, source, optional confidence, and optional
  observation window.
- remain inspectable data until a later reviewed behavior package explicitly
  authorizes use in action selection.

Forbidden in v0.5.4:

- relationship state must not modify action choice, params patches, runtime
  events, memory selection, or API behavior.

## Self-Summary

Self-summary is an inspectable summary of an agent's continuity state.

Required semantics for any future schema:

- identify `agent_id`, `world_id`, stable summary id, summary text or generic
  facets, source, created/updated time, and evidence references.
- distinguish operator-authored, imported, and derived summaries.
- include version or supersession semantics so summaries are auditable rather
  than silently overwritten.
- avoid claiming consciousness, sentience, or true selfhood. The record is an
  engineering summary of continuity state.

Forbidden in v0.5.4:

- no self-summary generation, LLM summarization, automatic compression,
  automatic memory rewrite, or action modifier is authorized.

## Reflection Record

Reflection record is an auditable record of self-assessment, feedback
processing, or decision review.

Required semantics for any future schema:

- identify `agent_id`, `world_id`, stable reflection id, trigger, source,
  created time, content, and evidence references.
- distinguish observation, critique, hypothesis, and proposed follow-up
  sections if structured facets are used.
- keep proposed updates separate from applied changes.
- preserve the evidence trail that caused the reflection.

Forbidden in v0.5.4:

- no automatic reflection loop, memory rewrite, relationship update,
  self-summary update, or action behavior change is authorized.

## Personality Drift Signal

Personality drift signal is an inspectable signal about a possible change in
behavioral tendency, preference, or decision pattern.

Required semantics for any future schema:

- identify `agent_id`, `world_id`, stable signal id, dimension, direction,
  strength, source, created time, and evidence references.
- include a baseline reference or observation window when possible.
- represent uncertainty explicitly through confidence or review status.
- remain a signal, not a direct behavior rule.

Forbidden in v0.5.4:

- drift signals must not alter action choice, action validation, params
  patches, memory ranking, or loop output.

## Future Authorization Criteria

A later package may implement schema-only support only after:

- the package is explicitly typed as mixed or code before implementation.
- all required package docs and mirrors exist.
- a documentation/contract evaluator reports no P1 and no blocking P2.
- `review.md` records `implementation_authorized: yes`.
- the first production change is preceded by a focused failing test.
- the contract keeps changes additive and generic.
- validation includes focused schema tests, compatibility checks for touched
  loop/API surfaces, docs/mirror checks, and changed-file scope guard.

Any behavior that affects action selection, memory ranking, summaries,
relationships, reflection, or drift requires a later behavior-specific package
and cannot be smuggled in as schema-only work.

## Compatibility Requirements

- `PerceptionFrame.memory_context` remains read-only perception data.
- `LoopStepRequest`, `ActionIntent`, `ActionResult`, action adapter semantics,
  params behavior, event routes, runtime tick/time, archive behavior, and API
  envelope/error shape remain unchanged.
- Existing v0.5 memory substrate and memory context tests remain current
  evidence for their own packages, not a license to widen behavior here.

## Allowed Changes

- Package docs and mirrors under this directory.
- Parent v0.5 status/review surfaces for accurate handoff only.

## Forbidden Changes

- No backend code, backend tests, frontend files, migrations, generated
  results, fixtures, external repositories, or `backend/worldengine/**`
  changes.
- No public memory APIs, loop request selectors, persistence, vector retrieval,
  LLM summarization, automatic reflection, relationship behavior, self-summary
  generation, drift action modifiers, concrete world content, private
  validation oracle details, or application-specific backend logic.

## North Star Check

This package advances the north-star pseudo-self direction by making the
remaining continuity concepts inspectable and bounded before behavior. It does
not claim agent consciousness and does not turn WorldEngine into a
world-specific application backend.
