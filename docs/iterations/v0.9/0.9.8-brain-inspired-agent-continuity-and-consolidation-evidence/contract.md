# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

`AgentContinuityArtifact`

- Public artifact describing one Agent's continuity state at a runtime tick.
- Includes world id, agent id, tick, world time, perception summary refs,
  working or short-term memory summary, long-term memory summary refs,
  personality summary refs, skill summary refs, current state, event reaction
  refs, redaction status, and evidence refs.
- It must not include raw thoughts, chain-of-thought, private memory payloads,
  private goals, hidden context, raw prompts, raw provider responses, provider
  traces, API keys, authorization headers, or private evaluator data.

`AgentConsolidationArtifact`

- Public artifact describing a sleep/rest/low-activity consolidation phase.
- Includes phase id, world id, agent id, start/end tick or active tick window,
  consolidation status, source short-term summary refs, emitted long-term
  summary refs, personality/skill summary stability or bounded-drift markers,
  event refs, and redaction status.
- Consolidation may span multiple ticks. It must not imply mandatory per-tick
  personality, long-term memory, or skill mutation.

`AgentContinuityState`

- Public state vocabulary:
  - `observe`
  - `intent`
  - `action`
  - `no_intent`
  - `wait`
  - `rest`
  - `sleep`
  - `consolidating`
  - `reacting`
- States are public evidence classifications, not private cognition dumps.

`AgentEventReactionEvidence`

- Public evidence that an Agent reacted to a canonical public world event.
- Includes public event refs, reaction summary, selected public state,
  continuity artifact refs, and redaction status.
- It must not create a fake in-world dialogue, private memory mutation, or
  final world fact.

`AgentAutonomousActionEvidence`

- Public evidence that an Agent action was selected by WorldEngine-backed
  Agent loop behavior rather than directly supplied by a client, fixture, or
  external validation script.
- Includes action event refs, action result refs, continuity artifact refs,
  public action summary, input provenance classification, and redaction
  status.
- It must not expose raw prompts, raw thoughts, private goals, private memory,
  hidden context, provider traces, or private evaluator data.

`ClientScriptedAutonomyRejection`

- Public diagnostic that rejects evidence claiming autonomy when the action is
  directly supplied by a client, fixture, or external validation script.
- Rejection diagnostics must be public and must not echo unsafe client input.

## Required Checks

Continuity evidence must deterministically reject or diagnose:

- raw thought or chain-of-thought.
- private memory payloads, private goals, hidden context, private evaluator
  data, raw prompts, raw provider traces, API keys, authorization headers, and
  secrets.
- client-scripted action represented as Agent autonomy.
- personality, long-term memory, or skill changes represented as automatic
  per-tick mutation.
- consolidation phases without bounded tick/time evidence.
- event reactions without public event refs.
- accepted autonomous action evidence without public action event refs,
  action result refs, or WorldEngine-owned provenance.
- continuity artifacts without public Agent id, tick/time, state, or evidence
  refs.

Continuity evidence may be accepted only when:

- all evidence is public and redacted.
- state vocabulary is one of the allowed public states.
- event reactions point to public canonical event refs.
- action state evidence points to public canonical Agent action/result event
  refs and is not client-scripted.
- short-term, long-term, personality, and skill summaries are represented as
  public summaries or public refs, not private payloads.
- consolidation cadence is explicit and may span multiple ticks.

## Allowed Changes

After documentation review authorization, this package may modify:

- additive schemas in `backend/app/schemas/` for public Agent continuity,
  consolidation, autonomous action, event reaction, and scripted-autonomy
  rejection evidence.
- narrow deterministic helpers under `backend/app/core/` or
  `backend/app/agent/` for public continuity/consolidation artifact
  construction.
- additive active-backend route behavior or manifest/OpenAPI exposure if
  needed for public inspection.
- additive public event payload evidence for Agent continuity and
  consolidation records.
- focused backend tests under `backend/app/tests/`.
- package `review.md` and `review.zh.md`.
- v0.9 parent status/review docs only for route/status handoff after review
  or implementation closeout.

## Forbidden Changes

This package must not:

- modify `backend/worldengine/`.
- modify frontend code.
- modify Validation Client or external repositories.
- execute live provider calls or LLM interpretation.
- create generated worlds or generated-result artifacts.
- execute checkers or modify checker fixtures.
- run external validation or autonomous validation.
- implement durable scheduling, background workers, cron, queue services, or
  deployment infrastructure.
- implement narrative projection or diagnostic dialogue.
- store or export raw thought, chain-of-thought, private memory payloads,
  private goals, hidden context, raw prompts, raw provider requests, raw
  provider responses, provider traces, API keys, authorization headers,
  secrets, or private evaluator data.
- claim consciousness, human-quality simulation, full selfhood, checker PASS,
  external validation PASS, product readiness, or full v0.9 closeout.

## Compatibility Requirements

- Existing Agent loop APIs must remain additive-compatible unless this
  package review explicitly approves a narrow additive extension.
- Existing v0.5 memory schemas and stores must remain compatible and may only
  be extended additively.
- Existing event, runtime, snapshot/archive, world direction, and
  rule-linked event legality surfaces must remain compatible.
- Public handoff manifest behavior must remain compatible.
- New schemas must reject extra fields and private markers.
- Continuity evidence must not require checker support to be useful.
- Continuity evidence should be checker-consumable by later `0.9.10`
  checker/schema/fixture work, but this package does not implement checker
  fixtures or execute checkers.
- Rejected scripted-autonomy evidence must not append canonical accepted
  Agent autonomy events.

## North Star Check

This package supports engineered pseudo-self continuity while keeping the
model inspectable, testable, and explicitly non-consciousness-claiming.

## Out-of-Scope Follow-ups

- `0.9.9`: external narrative projection and diagnostic dialogue boundaries.
- `0.9.10`: LLM-backed checker fixtures, schema, scorecard support, and
  checker execution.
- `0.9.12`: live or blocked full lifecycle validation execution.

## Exit Criteria

This package may close only when:

- required package docs and mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- implementation authorization is recorded before code changes.
- focused tests prove continuity artifacts, consolidation artifacts,
  multi-tick cadence, accepted autonomous action evidence, no-intent/rest
  states, event reactions, scripted-action rejection, redaction, extra-field
  rejection, and compatibility with Agent loop, memory, event, runtime, and
  public handoff surfaces.
- relevant backend regressions pass in the current session.
- `review.md` records exact commands, changed files, subagent findings,
  compatibility review, scope review, unresolved findings, and final route.
