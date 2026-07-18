# Contract

Chinese mirror: `contract.zh.md`.

Status: documentation drafted / review pending

## Public Concepts

- **Rule-bound event candidate**: a public event proposal that references
  public rule ids, parameter ids, direction ids, public cause refs, probability
  evidence, causality evidence, and a public summary.
- **Legality gate**: the existing public evaluator that accepts or rejects a
  candidate before any state mutation.
- **Public state diff**: a redaction-safe list of parameter changes that were
  legal under public rules and constraints.
- **Session evolution step**: a bounded session API that deterministically
  selects or generates a public candidate from attached rules, queued
  directions, runtime state, and current public parameters.
- **Replay evidence**: event-log records and response evidence that let a
  client reconstruct accepted/rejected legality and applied public diffs.

## Allowed Changes

After review approval, this package may change:

- `backend/app/schemas/world_evolution.py` for additive session evolution
  request/response/evidence models.
- `backend/app/core/rule_linked_evolution.py` for deterministic public
  candidate selection helpers that still use the existing legality evaluator.
- `backend/app/core/world_session.py` for retaining accepted public rule sets
  needed by session evolution.
- `backend/app/api/routes/session.py` for an additive session evolution step
  endpoint.
- `backend/app/api/routes/world.py` for additive manifest/discovery entries and
  compatibility fixes on existing evolution evidence only.
- focused backend tests for session evolution, existing world evolution
  compatibility, manifest compatibility, redaction, and replay evidence.
- active package docs and v0.11 route/review status docs.

## Forbidden Changes

This package must not:

- bypass the existing legality evaluator.
- apply rejected or blocked candidates.
- generate hidden-random or provider-derived candidates.
- mutate Agent private memory, goals, self-state, relationships, inventory,
  injury, death, or private location.
- turn "lightning-strike risk" guidance into direct Agent injury/death; it may
  only influence public event probability/candidate evidence.
- add player item drops, direct detailed event triggers, or
  player-as-world-entity gameplay.
- expose raw direction instructions, raw provider data, secrets, hidden
  context, raw prompts, raw responses, private evaluator data, or private Agent
  memory.
- implement Validation Client behavior or run external validation.
- add persistence/migrations, frontend changes, concrete demo fixtures, or
  `backend/worldengine/` changes.

## Compatibility Requirements

- Existing `/worlds/{world_id}/evolution/evaluate-event` tests and behavior
  must remain additive-compatible.
- Existing session create/from-worldview/rules/directions/run/status APIs must
  remain additive-compatible.
- Event log and event-step replay outputs must remain additive-compatible.
- Rejected candidates must not mutate public state.
- Accepted candidates must include rule refs, parameter refs, direction refs
  when present, public diff evidence, and `direct_state_mutation_applied:
  false`.
- Unknown sessions or missing accepted rules must return public blocked/not
  ready responses rather than crashes.

## Out-Of-Scope Follow-Ups

- `0.11.5` owns worldview fidelity scoring, v0.11 validation closeout, and
  Validation Client handoff evidence.
- `v0.12` owns Agent continuity and external autonomous validation automation.
