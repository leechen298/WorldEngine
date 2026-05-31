# Technical Design

Status: review complete

## Current State

v0.4 provides the request-driven Agent-in-World minimal loop, including
bounded perception, action intent/result contracts, validated `noop` and
`params.patch`, and `POST /world/agent/loop/step`. v0.4 does not include
memory or self-continuity.

`0.5.0` created the v0.5 campaign root and kept implementation authorization
closed. No v0.5 memory implementation files exist yet.

## Contract Alignment And Invariants

This package is documentation-only. It preserves these invariants:

- no implementation file class changes.
- no runtime behavior changes.
- no public API changes.
- no test implementation changes.
- `implementation_authorized` remains `no`.
- working memory and episodic memory are the only concepts authorized for the
  next implementation slice, and only after `0.5.2` passes its own
  documentation/contract evaluator.
- relationship state, self-summary, reflection records, and personality drift
  signals remain contract/schema semantics only.

## Documentation Structure

The package documents are organized as:

- `README.md`: package goal, scope, deliverables, and document list.
- `intent.md`: problem, goal, non-goals, roadmap relationship, and handoff.
- `contract.md`: public concepts, authorization criteria, compatibility
  requirements, allowed changes, forbidden changes, and follow-ups.
- `technical-design.md`: documentation structure and semantic design.
- `test-plan.md`: docs-only verification commands and not-run rationale.
- `plan.md`: ordered execution steps and stop conditions.
- `review.md`: evidence, evaluator findings, compatibility review, scope
  review, unresolved findings, and final assessment.

Every file has a `.zh.md` mirror.

## Concept Model

The concept model separates record types from behavior:

- working memory: short-lived, bounded current-context record.
- episodic memory: event-linked experience record.
- relationship state: structured relationship semantics, no behavior yet.
- self-summary: continuity summary semantics, no generation yet.
- reflection record: self-assessment/feedback record semantics, no automatic
  reflection yet.
- personality drift signal: future behavior-drift signal semantics, no action
  modifier yet.

## Planned Schema Semantics

Later schema files should use additive optional models and generic identifiers.
The contract expects these fields or equivalents:

- common fields: `memory_id`, `agent_id`, `world_id`, `source`,
  `created_at`, `updated_at` where applicable, and evidence references.
- working memory fields: `content`, `priority`, `expires_at` or bounded
  lifetime metadata, and provenance.
- episodic memory fields: `summary`, `event_refs`, `tick`, `world_time`,
  optional action/outcome references, and provenance.
- follow-up concept fields: target references, summary facets, reflection
  triggers, drift dimensions, strengths, and evidence references.

The names above are planned semantics, not an implementation commitment for
this package. `0.5.2` must choose exact model names and fields in its reviewed
technical design.

## Compatibility Strategy

Because this package changes only docs, compatibility is preserved by scope.
The next implementation package must treat these surfaces as sensitive:

- `PerceptionFrame`
- `ActionIntent`
- `ActionResult`
- `LoopStep`
- `POST /world/agent/loop/step`
- params propose/apply route
- runtime tick/world time behavior
- event route serialization and optional `Event.refs`
- archive behavior
- API envelope/error shape

## Anti-Drift Rules

- Do not describe docs-only definitions as implemented runtime behavior.
- Do not describe v0.4 evidence as v0.5 pass evidence.
- Keep English and Chinese mirrors semantically equivalent.
- Keep future-version ownership explicit: v0.6 generation, v0.7 external
  validation readiness, v0.8 projection readiness.

## Risks

- Risk: concept language implies hidden behavior.
  Mitigation: each concept states whether it is record semantics only.
- Risk: first implementation widens into loop integration.
  Mitigation: authorization criteria confine `0.5.2` to working/episodic
  memory substrate and put loop integration in `0.5.3`.
- Risk: mirror drift.
  Mitigation: package requires Chinese mirrors and a mirror/file existence
  check.
