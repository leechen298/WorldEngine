# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

`NarrativeProjectionArtifact`

- Public artifact describing an external narrative projection of current world
  evidence.
- Includes projection id, world id, source event refs, snapshot refs, Agent
  continuity refs, public narrative summary or redacted narrative text,
  provenance, redaction status, and mutation flags.
- It is external projection evidence, not canonical world state.

`DiagnosticDialogueArtifact`

- Public artifact describing an out-of-world diagnostic question and public
  answer summary about an Agent.
- Includes dialogue id, world id, optional Agent id, question summary,
  response summary, evidence refs, provenance, redaction status, and mutation
  flags.
- It is diagnostic inspection evidence, not in-world dialogue by default.

`ProjectionBoundaryDecision`

- Public decision record explaining whether a projection or diagnostic artifact
  is allowed, rejected, or redacted.
- It must record why the artifact is outside or inside canonical state. This
  package only allows outside-canonical-state behavior by default.

## Boundary Table

| Surface | Default classification | May mutate canonical events | May write Agent memory | May become in-world dialogue |
| --- | --- | --- | --- | --- |
| Narrative projection | external projection | no | no | no |
| Diagnostic Agent question | out-of-world diagnostic | no | no | no |
| Canonical world event | in-world event | yes, through event API only | only through reviewed future bridge | maybe, if event type says so |
| Agent continuity artifact | public Agent evidence | no direct state mutation | no private memory write | no |

## Required Checks

Projection and diagnostic evidence must reject or diagnose:

- raw thought or chain-of-thought.
- private memory payloads, private goals, hidden context, private evaluator
  data, raw prompts, raw provider traces, API keys, authorization headers, and
  secrets.
- narrative text that claims to directly mutate canonical state.
- projection artifacts that append canonical events by default.
- diagnostic conversation represented as in-world dialogue by default.
- diagnostic conversation represented as Agent memory by default.
- artifacts without public provenance or redaction status.

Accepted artifacts must record:

- `canonical_state_mutation_applied: false`.
- `canonical_event_appended: false` unless a later reviewed bridge explicitly
  authorizes event writing.
- `agent_memory_write_applied: false`.
- `in_world_dialogue_recorded: false`.
- public evidence refs and redaction status.

## Allowed Changes

After documentation review authorization, this package may modify:

- additive schemas in `backend/app/schemas/` for public narrative projection,
  diagnostic dialogue, boundary decisions, provenance, and redaction status.
- narrow deterministic helpers under `backend/app/core/` for projection and
  diagnostic artifact construction.
- additive active-backend route behavior or manifest/OpenAPI exposure if
  needed for public inspection.
- focused backend tests under `backend/app/tests/`.
- package `review.md` and `review.zh.md`.
- v0.9 parent status/review docs only for route/status handoff after review or
  implementation closeout.

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
- implement player-in-world chat, product chat UI, or narrative game content.
- write diagnostic conversations into canonical world timeline or Agent memory
  by default.
- store or export raw thought, chain-of-thought, private memory payloads,
  private goals, hidden context, raw prompts, raw provider requests, raw
  provider responses, provider traces, API keys, authorization headers,
  secrets, or private evaluator data.

## Compatibility Requirements

- Existing event, runtime, snapshot/archive, world direction, rule-linked
  event legality, and Agent continuity surfaces must remain compatible.
- Existing Agent memory stores must not receive diagnostic writes.
- Existing public handoff manifest behavior must remain compatible.
- New schemas must reject extra fields and private markers.
- Projection and diagnostic artifacts should be checker-consumable by later
  `0.9.10` checker/schema/fixture work, but this package does not implement
  checker fixtures or execute checkers.

## North Star Check

This package supports inspectable external projection while preserving
WorldEngine's canonical event/state spine.

## Out-of-Scope Follow-ups

- `0.9.10`: LLM-backed checker fixtures, schema, scorecard support, and
  checker execution.
- A future bridge may explicitly authorize diagnostic-to-memory behavior, but
  this package forbids it by default.

## Exit Criteria

This package may close only when:

- required package docs and mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- implementation authorization is recorded before code changes.
- focused tests prove projection/diagnostic artifacts remain outside
  canonical state, do not append canonical events by default, do not write
  Agent memory by default, reject private markers, and preserve compatibility.
- relevant backend regressions pass in the current session.
- `review.md` records exact commands, changed files, subagent findings,
  compatibility review, scope review, unresolved findings, and final route.
