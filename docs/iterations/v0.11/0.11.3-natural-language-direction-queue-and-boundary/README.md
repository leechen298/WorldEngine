# 0.11.3 Natural-Language Direction Queue And Boundary

Chinese mirror: `README.zh.md`.

Status: review complete
Type: mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Let users guide a session's world evolution through natural language while
keeping that guidance outside direct world mutation. Accepted guidance is queued
as public world-level pressure, probability shift, event-candidate bias,
environment trend, rule constraint, or future evaluation hint. Rejected
guidance must not mutate final facts, Agent private state, Agent goals,
relationships, or inventories.

## Scope

Allowed scope after review approval:

- add session-scoped direction queue/read surfaces.
- reuse the existing public world-direction classifier and redaction boundary.
- record accepted/rejected direction evidence without raw instruction echo.
- expose public queue summaries for later event generation.
- add focused backend tests for session direction behavior and manifest
  discoverability.

Forbidden scope:

- no direct death, injury, healing, inventory, relationship, location,
  private memory, private goal, or final-fact mutation from user guidance.
- no player item drops, player-as-world-entity gameplay, or direct detailed
  event triggering.
- no rule bypass, hidden evaluator oracle, raw provider trace, raw prompt,
  raw response, secret, private Agent memory, or hidden context exposure.
- no rule-compliant event generation or diff application; that belongs to
  `0.11.4`.
- no Validation Client implementation or external validation execution.
- no persistence or migrations.
- no `backend/worldengine/` changes.

## Deliverables

- session-scoped direction queue API.
- session-scoped direction summary API.
- additive manifest discovery entries.
- replayable public operation records for accepted and rejected guidance.
- client-readable status classification for queued/rejected direction outcomes.
- public accepted/rejected evidence with `direct_state_mutation_applied: false`.
- examples proving direct final-fact commands are rejected while
  lightning-risk guidance remains queued as external pressure only.
- focused backend tests and review evidence.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Implementation authorized
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## Final Assessment

PASS. Implementation complete for reviewed scope.
