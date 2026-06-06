# 0.9.6 Natural Language World Direction Boundary

Chinese mirror: `README.zh.md`.

Status: implementation complete / focused verification passed / evaluator PASS
Type: mixed implementation package

## Goal

Convert user natural-language direction into bounded world-level guidance that
can influence environment trends, external pressure, event candidate bias, and
future rule evaluation without directly mutating Agent private state, Agent
goals, inventory, relationships, life/death state, or final world facts.

## Scope

This package may extend the active backend path under `backend/app/` with:

- public world-direction request and response schemas.
- deterministic classification of allowed world-level guidance versus
  forbidden direct outcomes.
- a bounded in-memory direction queue or summary attached to the active world
  API surface.
- public rejection reasons for direct final facts, private Agent mutation,
  inventory injection, rule bypass, or private-marker leakage.
- compatibility behavior for the existing `/worlds/{world_id}/director-guidance`
  public endpoint.
- focused backend and API tests for allowed guidance, rejected direct outcomes,
  delayed application windows, public summaries, and redaction.

This package must not implement event legality, rule-linked event generation,
Agent continuity, private memory mutation, live provider calls, generated
result creation, checker execution, external validation, frontend UI, durable
scheduling, or Validation Client changes.

## Deliverables

- Public direction intake contract.
- Public direction classification and rejection taxonomy.
- In-memory queued-guidance semantics with bounded timing fields.
- Public direction summary evidence that does not expose raw private internals.
- Focused tests proving allowed guidance is queued and forbidden direct
  outcomes are blocked without mutating Agent private state or final facts.

## Current Authorization

Documentation/contract/design/test-plan review passed. Implementation is
complete for the scoped active-backend natural-language world direction
boundary work recorded in this package.

Provider live calls, generated-result creation, checker execution, external
validation, Validation Client changes, frontend UI, event legality, Agent
continuity, durable scheduling, and `backend/worldengine/` changes remain
unauthorized.

## Final Assessment State

Complete for the reviewed `0.9.6` scope. Focused, related public-surface, and
backend regression verification passed, and implementation-scope evaluator
re-review passed with no P0/P1/P2/P3 findings.
