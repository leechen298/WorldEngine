# 0.9.7 Rule Linked Evolution And Event Legality

Chinese mirror: `README.zh.md`.

Status: implementation complete / verification passed
Type: mixed implementation package

## Goal

Make world parameter evolution and selected events traceable to public rules,
current public state, constraints, probability, causality, location, and time.

This package turns generated rule/parameter artifacts, bounded runtime state,
and queued world direction into deterministic public evidence that an event is
legal before it can be accepted as a world-evolution event.

## Scope

This package may extend the active backend path under `backend/app/` with:

- public event-candidate and event-legality schemas.
- deterministic rule-linked legality checks over public generated
  rule/parameter sets.
- public state-diff summaries for accepted parameter changes.
- public rejection diagnostics for illegal, unresolved, out-of-bounds,
  private, direct-final, or unsupported event candidates.
- additive event payload evidence when a legal event is accepted.
- focused backend/API tests for accepted legal events, rejected illegal events,
  direction-biased but rule-compliant candidates, redaction, and diff
  consistency.

This package must not execute live providers, create generated results, execute
checkers, change checker fixtures, run external validation, add frontend or
Validation Client work, implement Agent continuity, implement narrative
projection, implement diagnostic dialogue, add durable scheduling, or modify
`backend/worldengine/`.

## Deliverables

- Event candidate contract for public rule-linked evolution.
- Event legality result contract with public rule/state evidence.
- State-diff artifact contract for accepted parameter changes.
- Deterministic helper or API behavior for checking and accepting legal
  event candidates in active backend scope.
- Focused tests proving legal acceptance, illegal rejection, redaction, and
  compatibility with existing event, runtime, rule-parameter, direction, and
  public handoff surfaces.

Handoff after closeout goes to
`0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence`.

## Current Authorization

Documentation/contract/design/test-plan review passed. Implementation is
authorized only for the scoped active-backend rule-linked evolution and event
legality work recorded in this package.

Provider live calls, generated-result creation, checker execution, checker
fixture changes, external validation, Validation Client changes, frontend UI,
Agent continuity, narrative projection, diagnostic dialogue, durable
scheduling, and `backend/worldengine/` changes remain unauthorized.

## Final Assessment State

Implementation complete for the scoped active-backend `0.9.7` work. Focused,
related public-surface, and backend regression verification passed in the
current implementation session. Handoff goes to
`0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence`
documentation-package creation/review.
