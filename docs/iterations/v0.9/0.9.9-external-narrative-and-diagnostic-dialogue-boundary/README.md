# 0.9.9 External Narrative And Diagnostic Dialogue Boundary

Chinese mirror: `README.zh.md`.

Status: implementation complete / verification passed
Type: mixed implementation package

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no

## Goal

Define the first public boundary for external narrative projection and
out-of-world diagnostic Agent dialogue without treating either surface as
canonical world events, in-world dialogue, or Agent memory by default.

This package should let WorldEngine expose inspectable narrative or diagnostic
outputs derived from canonical public evidence while keeping canonical world
state, event timelines, Agent private memory, and Agent continuity artifacts
protected from projection-side mutation.

## Scope

After documentation review, this package may extend `backend/app/` with:

- additive public narrative projection schemas.
- additive public diagnostic dialogue schemas.
- deterministic helpers that build redacted projection or diagnostic artifacts
  from public events, snapshots, and Agent continuity summaries.
- optional additive public API/manifest surfaces for projection and diagnostic
  evaluation.
- focused backend/API tests proving projection and diagnostics do not mutate
  canonical world state, do not append in-world dialogue events by default, and
  do not write Agent memory by default.

This package must not execute live providers, create generated results,
execute checkers, modify checker fixtures, run external validation, implement
frontend or Validation Client features, create a player-in-world chat system,
write diagnostic conversations into Agent memory, or modify
`backend/worldengine/`.

## Deliverables

- Public narrative projection artifact contract.
- Public diagnostic dialogue artifact contract.
- Decision table distinguishing external projection/diagnostic evidence from
  canonical world state, canonical events, Agent memory, and in-world dialogue.
- Provenance and redaction rules for projection and diagnostics.
- Focused implementation plan and test plan for additive active-backend work.

Handoff after closeout goes to
`0.9.10-llm-backed-autonomous-checker-and-fixtures`.

## Current Authorization

Documentation/contract/design/test-plan review passed. Implementation is
complete for the scoped active-backend narrative projection and diagnostic
dialogue boundary work recorded in this package.

## Final Assessment State

Implementation complete for the scoped active-backend `0.9.9` work. Focused,
related, and backend regression verification passed in the current session,
and implementation re-review reported no P0/P1/P2/P3 findings after repairs.

Provider calls, generated-result creation, checker execution, external
validation, frontend UI, Validation Client work, durable scheduling, and
`backend/worldengine/` changes remain unauthorized.
