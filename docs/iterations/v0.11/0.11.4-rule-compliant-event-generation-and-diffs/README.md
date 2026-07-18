# 0.11.4 Rule-Compliant Event Generation And Diffs

Chinese mirror: `README.zh.md`.

Status: review complete
Type: mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Generate or select a public world event candidate for a session, evaluate it
through public rules and current state, apply only legal public diffs, and
record replayable evidence that explains why the world changed.

## Scope

Allowed scope after review approval:

- retain the existing manual `/worlds/{world_id}/evolution/evaluate-event`
  legality/apply path.
- add a small session-scoped rule-bound evolution step that builds a
  deterministic public candidate from an attached public rule set, current
  public parameters, runtime tick/time, and queued public direction refs.
- require every generated/selected candidate to pass the existing public
  legality evaluator before state mutation.
- record accepted/rejected legality evidence, public diffs, direction refs,
  rule refs, parameter refs, and replayable event-log records.
- expose additive manifest discovery for the session evolution step.
- add focused backend tests for legal/illegal candidates, direction influence,
  lightning-risk-as-pressure, diff application, replay evidence, redaction,
  and runtime/session compatibility.

Forbidden scope:

- no hidden random oracle or unexplainable selection.
- no illegal final outcomes.
- no direct death, injury, inventory, relationship, Agent goal, Agent private
  memory, or Agent private-state mutation.
- no direct user-imposed final facts.
- no player item drops, direct detailed event triggers, or
  player-as-world-entity gameplay.
- no provider calls, raw prompts, raw responses, provider traces, secrets,
  hidden context, or private evaluator data.
- no Validation Client implementation or external validation execution.
- no concrete demo-world seed data.
- no persistence/migrations.
- no frontend work.
- no `backend/worldengine/` changes.

## Deliverables

- session-scoped rule-bound evolution step API.
- deterministic public event candidate selection/generation.
- legality result and public state diff evidence.
- replayable accepted/rejected event records.
- tests proving lightning-risk guidance stays external pressure and cannot
  directly create Agent injury/death.
- focused verification and review evidence.

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
