# v0.10 MVP Debug Contract And Runnable World Session

Chinese mirror: `README.zh.md`.

Status: closeout PASS / handed off to v0.11
Type: Codex `/goal` development campaign and iteration package root
implementation_authorized: no
evidence_execution_authorized: no

## Goal

v0.10 starts the MVP delivery track. Its goal is to align the public debug and
checker handoff contract first, then turn WorldEngine from a set of
individually useful backend capabilities into one visible runnable world
session.

In plain terms: WorldEngine-Validation-Client should first be able to connect,
discover the MVP surfaces, and export an honest `blocked` or basic handoff
result. Then a user should be able to enter a basic worldview, create a world
session, run it for a bounded number of ticks, pause or continue it, see
events and snapshots, and inspect the state through the dashboard or an
external client.

v0.10 is deliberately narrower than the earlier v0.9 product-level ambition.
It does not try to prove high-quality LLM generation, deep Agent autonomy, a
finished game client, or full external autonomous validation. It establishes
the first vertical slice that later MVP versions can make alive and
validatable.

## Handoff From v0.9

v0.9 closed as blocked for full LLM-backed lifecycle validation. It left useful
foundation surfaces, including provider readiness, worldview generation
contracts, world rules and direction boundaries, bounded runtime controls,
event legality, Agent continuity evidence contracts, and checker/evidence
handoff ideas.

The v0.10 handoff decision is:

- use v0.9 as architecture input.
- do not require v0.9 full LLM-backed PASS before MVP work starts.
- do not turn every v0.9 long-term capability into a v0.10 requirement.
- prioritize one runnable session flow over broad capability completeness.
- fix MVP public manifest/version/discovery semantics before relying on client
  automation.

## Scope

Allowed v0.10 scope after reviewed child authorization:

- world session identity, lifecycle, public status, and in-memory persistence.
- MVP public manifest/version contract and external debug handoff fields.
- replay and worldline branch labels for external debugging, using
  code-branch-like branch terminology rather than parent/source semantics.
- creating a runnable session from user worldview input.
- labeled deterministic or mock fallback when live provider execution is not
  available.
- connecting generated public world model data into runtime state, parameters,
  initial Agent records, and visible world projection.
- bounded run controls exposed through backend and dashboard surfaces.
- event, diff, and snapshot evidence for each session.
- a simple MVP dashboard path: create world, run ticks, pause or continue,
  inspect world state, inspect timeline.
- public manifest and artifact naming needed by WorldEngine-Validation-Client
  to discover the MVP session surfaces and export honest `blocked`, `fail`,
  `pass`, or `not_run` status.

Forbidden v0.10 scope:

- no polished game UI, pixel-art asset production, Steam/native packaging, or
  app-specific distribution logic.
- no concrete demo-world seed data in this repository.
- no live provider quality claim without current-session provider and checker
  evidence.
- no Agent pseudo-self claim, deep memory/personality simulation, or
  autonomous validation PASS.
- no player-as-world-entity gameplay, item drops, or direct detailed event
  triggering.
- no parent/child/source-world semantics for replay or worldline branch labels.
- no Validation Client implementation inside this repository.
- no raw prompts, raw provider responses, secrets, raw thought, private Agent
  memory, or hidden context in evidence.
- no new runtime features under `backend/worldengine/`.

## Planned Package Roadmap

`v0.10-plan.md` is the detailed planned-package specification. Planned
packages are route-map specs only. They are not active implementation
authorization and they are not full child package documents.

Planned sequence:

1. `0.10.0-mvp-debug-session-planning-and-v0.9-handoff`
2. `0.10.1-mvp-public-manifest-and-debug-handoff`
3. `0.10.2-world-session-contract-and-state-store`
4. `0.10.3-worldview-to-runtime-session-creation`
5. `0.10.4-bounded-session-runtime-and-snapshot-evidence`
6. `0.10.5-dashboard-mvp-session-flow`
7. `0.10.6-v0.10-validation-and-handoff`

## Current State

Active child package:
none. v0.10 closeout is complete.

Current route:

```text
v0.10-closeout-pass-v0.11-handoff-ready
```

Implementation authorization: no.

Evidence execution authorization: no.

## Validation Boundary

v0.10 PASS is not a product-quality or LLM-quality claim. It only proves the
first debug-handoff and runnable-session slice:

```text
client discovery -> worldview input -> world session -> bounded runtime -> events/snapshots -> dashboard/client inspection
```

WorldEngine remains the verified object. WorldEngine-Validation-Client may
consume the public surfaces and evidence, but it must not own provider calls,
world generation, runtime mutation, or authoritative evaluation.

v0.10 may define the debug vocabulary that later clients use for replay and
branch inspection. That vocabulary must treat branches as comparable timeline
branches, not as parent/child worlds or source-world hierarchies.
