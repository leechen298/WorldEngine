# v0.11 MVP Rule-Bound World Evolution

Chinese mirror: `README.zh.md`.

Status: closeout complete / scoped PASS
Type: Codex `/goal` development campaign and iteration package root
parent_implementation_authorized: no
active_child_implementation_authorized: no
active_child_evidence_execution_authorized: no

## Goal

v0.11 builds on the v0.10 runnable session and makes the world change for
reasons that can be inspected.

In plain terms: a created world should not only tick counters forward. It
should have public parameters and rules, accept user natural-language guidance
as world-level pressure, generate or select events that are legal under those
rules, apply public diffs, and let validators see why the world changed.

## Handoff From v0.10

v0.10 is expected to hand off:

- public MVP manifest and checker handoff skeleton.
- world session identity and state store.
- worldview-to-session creation.
- bounded runtime controls.
- event/snapshot evidence.
- dashboard create/run/inspect flow.

v0.11 assumes that vertical slice exists. If it does not, v0.11 must record a
handoff blocker rather than bypassing session or evidence contracts.

## Scope

Allowed v0.11 scope after reviewed child authorization:

- WorldEngine-owned provider live preflight for world evolution inputs.
- provider-backed or clearly labeled fallback worldview generation.
- public structured world parameters, rules, constraints, and boundaries.
- natural-language direction queue that affects only world-level pressure,
  environment trends, event candidates, probabilities, or constraints.
- rule-compliant event candidate generation/evaluation/application.
- public diff/replay evidence linked to rules and parameters.
- immediate and bounded-run worldview fidelity checks.
- Validation Client discoverability and evidence fields for rule/evolution
  debugging.

Forbidden v0.11 scope:

- no direct final fact assignment from user guidance.
- no player item drops, direct detailed event triggers, or
  player-as-world-entity gameplay.
- no direct Agent private memory, goal, personality, skill, injury, death, or
  inventory mutation from user guidance.
- no user command such as "kill this Agent now" being copied into final world
  facts; a risk such as "this Agent may face lightning-strike danger" must
  still be evaluated through weather, location, probability, life state, and
  rules.
- no hidden rule execution or private evaluator oracle.
- no raw prompts, raw provider responses, provider traces, secrets, raw
  thought, private Agent memory, or hidden context in evidence.
- no full Agent autonomy implementation.
- no concrete demo-world seed data in this repository.
- no Validation Client implementation in this repository.

## Planned Package Roadmap

`v0.11-plan.md` is the detailed planned-package specification. Planned
packages are route-map specs only.

Planned sequence:

1. `0.11.0-rule-bound-evolution-planning-and-v0.10-handoff`
2. `0.11.1-provider-and-worldview-generation-preflight`
3. `0.11.2-structured-world-rules-and-parameters`
4. `0.11.3-natural-language-direction-queue-and-boundary`
5. `0.11.4-rule-compliant-event-generation-and-diffs`
6. `0.11.5-worldview-fidelity-and-v0.11-validation`

## Current State

Active child package:
none; v0.11 closeout complete.

Current route:

```text
v0.11-closeout-complete-handoff-to-v0.12-parent
```

Implementation authorization: no.

Evidence execution authorization: no.

Closeout result: scoped `PASS` for rule-bound world evolution. Handoff route:
v0.12 parent `v0.12-parent-documentation-ready-for-review`, starting with
`0.12.0-agent-validation-planning-and-v0.11-handoff`.

## Validation Boundary

v0.11 PASS proves rule-bound world evolution, not living Agent autonomy or
complete MVP closure. A valid v0.11 result should show:

```text
runnable session -> rules/params -> user direction -> legal event/diff -> bounded-run fidelity evidence
```

The direction boundary is part of the validation target. PASS requires
evidence that accepted user guidance remained world-level pressure and that
rejected guidance did not mutate final facts or Agent private state.
