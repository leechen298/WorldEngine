# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

`WorldDirectionRequest`

- Public request to submit natural-language world guidance.
- Includes `instruction_text`, optional `branch_id`, optional `apply_after_tick`,
  optional `expires_after_tick`, and optional `public_context`.
- Extra fields are rejected.
- The raw instruction must not be echoed into event payloads or public summaries
  when it contains private markers.

`WorldDirectionClassification`

- Public classification of submitted direction.
- Allowed categories:
  - `environment_trend`
  - `external_pressure`
  - `event_candidate_bias`
  - `probability_shift`
  - `rule_constraint`
  - `future_evaluation_hint`
- Forbidden categories:
  - `direct_final_fact`
  - `agent_private_state_mutation`
  - `agent_goal_mutation`
  - `inventory_injection`
  - `relationship_override`
  - `rule_bypass`
  - `private_marker_detected`

`WorldDirectionQueueItem`

- Public queued guidance item for future world-level consideration.
- Includes a public id, world id, classification, status, timing window,
  public summary, public context keys, redaction status, and optional future
  rule/adjudication references.
- It does not represent an event outcome, an Agent action, or an Agent memory.

`WorldDirectionResponse`

- Public response with status `queued`, `rejected`, `blocked`, or
  `unavailable`.
- Includes classification, queue item when accepted, public rejection reason
  when rejected, and no direct state mutation evidence.

`WorldDirectionSummary`

- Public summary of currently queued or rejected direction items.
- May be returned by a helper or endpoint if implementation chooses to expose
  queue inspection in this package.

## Allowed Changes

- Additive direction schemas in active backend schema files.
- Active backend helper code for deterministic direction classification,
  redaction, and in-memory queue storage.
- Additive world API route behavior for canonical direction submission.
- Compatibility wrapper or compatibility behavior for
  `/worlds/{world_id}/director-guidance`.
- Manifest/OpenAPI surface updates only if needed for the public API contract.
- Focused backend/API tests.
- Package-local review documentation and parent v0.9 status updates after
  closeout.

## Forbidden Changes

- No live provider calls or LLM interpretation.
- No generated-result creation.
- No checker execution or checker fixture changes.
- No external validation or autonomous validation.
- No frontend UI or Validation Client changes.
- No durable scheduler, background worker, queue service, deployment
  infrastructure, or cron-like behavior.
- No event legality implementation or final event adjudication.
- No rule-linked parameter evolution beyond storing future public references.
- No Agent continuity, private memory, goal, relationship, inventory,
  personality, skill, life/death, or location mutation.
- No direct final facts such as "Agent X is dead" becoming canonical state.
- No concrete demo-world fixtures or application-specific logic.
- No `backend/worldengine/` changes.

## Compatibility Requirements

- Existing `/worlds/{world_id}/director-guidance` accepted-guidance behavior
  must remain compatible for benign environmental guidance.
- Existing public handoff, world creation, event listing, runtime, generation,
  rule-parameter, and fidelity tests must continue to pass.
- Existing event payload redaction requirements for director guidance must be
  preserved.
- Existing `DirectorGuidanceRequest` / `DirectorGuidanceResponse` may be
  extended only additively unless this package explicitly documents a wrapper
  that preserves the old response surface.
- Direction classification must be deterministic and testable without provider
  calls.
- Rejected direction must not mutate state, enqueue an accepted item, or record
  a final outcome.

## Out-of-scope Follow-ups

- `0.9.7`: rule-linked evolution and event legality.
- `0.9.8`: brain-inspired Agent continuity and consolidation evidence.
- `0.9.10`: checker fixtures and scorecard support.
- `0.9.12`: live or blocked full lifecycle validation execution.

## Exit Criteria

This package may close only when:

- required package docs and mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- implementation authorization is recorded before code changes.
- focused tests prove allowed environmental direction is queued, direct final
  outcomes are rejected, private Agent mutation requests are rejected, timing
  windows are bounded, public summaries are redacted, extra fields are rejected,
  and existing director-guidance compatibility is preserved.
- relevant backend regressions pass in the current session.
- `review.md` records exact commands, changed files, subagent findings,
  compatibility review, scope review, unresolved findings, and final route.
