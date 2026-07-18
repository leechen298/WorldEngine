# v0.12 MVP Agent Continuity And Validation Automation

Chinese mirror: `README.zh.md`.

Status: closeout complete / PARTIAL
Type: Codex `/goal` development campaign and iteration package root
implementation_authorized: no
evidence_execution_authorized: no

## Goal

v0.12 completes the MVP by adding a minimal living-Agent loop and closing the
external validation path through WorldEngine-Validation-Client.

In plain terms: after a world can run and evolve by rules, at least one Agent
should visibly observe, decide to act or not act, react to events, keep public
memory summaries, rest or sleep across ticks, and produce evidence that an
external validation client can export and a checker can classify.

## Handoff From v0.11

v0.11 is expected to hand off:

- runnable session with public manifest/debug contract.
- bounded runtime, events, diffs, and snapshots.
- structured rules and parameters.
- natural-language direction as world-level guidance.
- rule-compliant event generation and bounded-run fidelity evidence.

v0.12 assumes that the world can already change through public rules. If that
handoff is absent, v0.12 must record a blocker instead of scripting Agent
behavior in the client.

## User-Facing Inspection Model

Novel-style narrative projection lets a user request a readable summary of a
session, tick range, worldline branch, or Agent-focused public history. The
projection is generated from public events, diffs, snapshots, Agent summaries,
and provenance.

Diagnostic conversation lets a user ask out-of-world questions such as "why
did this event happen," "what does this Agent appear to remember publicly,"
or "does the run still fit the worldview." The transcript is inspection
evidence only. It is not in-world dialogue, not player participation, not
Agent memory, and not a way to steer future events. Any request that should
affect the world must go through the direction queue.

## Scope

Allowed v0.12 scope after reviewed child authorization:

- public Agent state, needs, intent state, behavior, and event reactions.
- minimal Agent loop integrated with session runtime.
- valid no-intent, wait, rest, and sleep states.
- short-term memory summaries and long-term memory/consolidation summaries.
- sleep/rest/low-activity consolidation that may span multiple ticks.
- novel-style narrative projection and out-of-world diagnostic conversation
  as read-only inspection surfaces.
- WorldEngine-owned public evidence artifacts for Agent autonomy and
  validation.
- checker scenarios, scorecards, result schema, and read-only external
  evaluator review protocol for the MVP full lifecycle.
- WorldEngine-to-Validation-Client handoff prompt and required artifact list.
- explicit terminology separating in-world Agents from external validation
  agents such as Codex or OpenClaw.

Forbidden v0.12 scope:

- no claim of real consciousness.
- no raw thought, raw chain-of-thought, private memory, private goals, hidden
  context, secrets, raw prompts, raw provider responses, or provider traces in
  evidence.
- no client-scripted action represented as Agent autonomy.
- no automatic per-tick personality, skill, or long-term memory mutation.
- no diagnostic conversation inserted into world timeline or Agent memory by
  default.
- no narrative projection mutating canonical world state.
- no out-of-world diagnostic conversation represented as in-world player
  dialogue by default.
- no external validation agent represented as an in-world Agent.
- no concrete game content or product-specific backend behavior in this
  repository.
- no Validation Client implementation inside this repository.

## Planned Package Roadmap

`v0.12-plan.md` is the detailed planned-package specification. Planned
packages are route-map specs only.

Planned sequence:

1. `0.12.0-agent-validation-planning-and-v0.11-handoff`
2. `0.12.1-agent-public-state-and-runtime-loop`
3. `0.12.2-agent-memory-and-rest-consolidation-mvp`
4. `0.12.3-narrative-and-diagnostic-inspection-surfaces`
5. `0.12.4-validation-client-mvp-evidence-handoff`
6. `0.12.5-full-lifecycle-checker-and-autonomous-validation`
7. `0.12.6-mvp-release-candidate-and-closeout`

## Current State

Active child package: none.

Current route:

```text
v0.12-closeout-complete-partial
```

Implementation authorization: no.

Evidence execution authorization: no.

Final classification: PARTIAL. WorldEngine-side Agent continuity, memory,
inspection, handoff, and deterministic checker evidence are present. Complete
MVP PASS remains blocked by the missing current v0.12 external Validation
Client export/result directory.

## Validation Boundary

v0.12 PASS is the first complete MVP validation claim. It must come from
checker, scorecard, and read-only review evidence, not from UI smoke or human
impression.

Required MVP lifecycle:

```text
client discovery -> create world -> run bounded ticks -> rule-linked events/diffs -> Agent observe/intent/action-or-rest/memory -> evidence export -> checker/scorecard/review
```

In this lifecycle, "Agent" means an in-world Agent. The external validation
agent that operates the client and reviews evidence stays outside the world and
must not be recorded as a world participant.
