# v0.5 Memory And Self-Continuity Substrate

Status: final / closeout complete
Type: Codex `/goal` development campaign and iteration package root

## Goal

v0.5 defines and then incrementally implements the first generic memory and
self-continuity substrate for agents living inside WorldEngine worlds.

The version starts from the reviewed v0.4 request-driven Agent-in-World loop
and keeps the memory/self-continuity boundary generic, inspectable, and
evidence-driven. It must not turn WorldEngine into a demo-specific backend or
application surface.

## Goal Entry

Natural-language goal:

```text
完成 v0.5
```

Interpretation:

- Start from `CURRENT_STATE.md`.
- Follow `GOAL_RUNNER.md` for route selection, subagent/evaluator checkpoints,
  implementation authorization, verification, and stop conditions.
- Follow `CAMPAIGN_PLAN.md` and `v0.5-plan.md` for child sequence,
  deliverables, compatibility constraints, and handoff rules.
- Read the active child package docs before doing any child work.

This is not an automation-controller implementation. Scheduling,
orchestration, retry infrastructure, and Codex role assignment remain outside
WorldEngine.

## Scope

Allowed v0.5 scope:

- working memory concept, provenance, bounded read/write semantics, and later
  additive generic implementation.
- episodic memory concept, event-linked semantics, and later additive generic
  implementation.
- relationship state schema semantics before behavior.
- self-summary schema semantics before summarization behavior.
- reflection record schema semantics before automatic reflection behavior.
- personality drift signal schema semantics before action modification
  behavior.
- additive backend schemas, in-memory substrate services, and focused backend
  tests only when a reviewed child package explicitly authorizes them.

Forbidden v0.5 scope:

- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7
  owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources,
  story rules, seed data, UI-specific app behavior, or private validation
  oracle details.
- Do not add frontend product behavior unless a later reviewed v0.5 child
  explicitly authorizes it.
- Do not add migrations or durable persistence unless a later reviewed v0.5
  child explicitly authorizes it.
- Do not add new runtime features under `backend/worldengine/`.

## Deliverables

- Parent goal-campaign documents: `README.md`, `v0.5-plan.md`,
  `GOAL_RUNNER.md`, `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, and `review.md`,
  with Chinese mirrors.
- First child package:
  `0.5.0-v0.5-planning-and-continuity-boundary-baseline`, with README,
  intent, contract, technical design, test plan, plan, review, and Chinese
  mirrors.
- Planned child package sequence through final closeout.
- Explicit subagent/evaluator checkpoint rules for `/goal` execution.
- Documentation-stage review evidence proving no runtime, schema, API,
  frontend, test implementation, fixture, migration, external repository, or
  `backend/worldengine/` file changed in `0.5.0`.

## Package Index

### `0.5.0-v0.5-planning-and-continuity-boundary-baseline`

- Type: documentation-only
- Status: review complete
- Purpose: create the v0.5 documentation root, goal-campaign controls,
  version plan, memory/self-continuity boundary, compatibility baseline, and
  v0.4 handoff mapping without changing implementation files.

### `0.5.1-memory-self-continuity-contracts`

- Type: documentation-only
- Status: review complete
- Purpose: define public memory/self-continuity concepts and schema semantics
  before implementation.

### `0.5.2-working-and-episodic-memory-substrate`

- Type: mixed or code
- Status: review complete
- Purpose: implement only additive generic working-memory and episodic-memory
  schemas, an in-memory substrate, and focused backend tests.

### `0.5.3-memory-context-loop-integration`

- Type: mixed or code
- Status: review complete
- Purpose: add bounded read-only memory context into the Agent Loop perception
  path without changing action semantics.

### `0.5.4-reflection-relationship-and-drift-contract-followup`

- Type: documentation-only or mixed
- Status: review complete
- Purpose: refine relationship state, self-summary, reflection record, and
  personality drift signal contracts before any behavior affects action.

### `0.5.5-v0.5-evidence-and-compatibility-audit`

- Type: documentation-only
- Status: review complete
- Purpose: audit v0.5 implementation evidence, compatibility surfaces,
  unresolved findings, and handoff readiness for release-candidate review.

### `0.5.6-v0.5-release-candidate-bundle`

- Type: documentation-only
- Status: review complete
- Purpose: prepare a v0.5 release-candidate bundle from reviewed
  implementation and audit evidence without declaring final release.

### `0.5.7-v0.5-final-closeout`

- Type: documentation-only
- Status: final / closeout complete
- Purpose: mark v0.5 final / closeout complete only after release-candidate
  review approval, evidence consistency checks, and unresolved finding
  classification.

## Current State

Active child package:
none.

Current route: `final-closeout-complete`.

Implementation authorization: no.

## Handoff Baseline

- v0.4 status: `final / closeout complete`.
- v0.4 post-closeout status: validation clean pass after frontend build
  repair.
- v0.4 and post-closeout command evidence are baseline and handoff evidence
  only. They are not current v0.5 implementation pass claims.
- v0.5 final current-session evidence: `git diff --check` passed; required
  docs/mirrors `missing=0`; changed-file scope guard `out_of_scope=0`;
  focused backend memory/loop/action compatibility `33 passed`; full backend
  regression `145 passed`; closeout consistency evaluator PASS.
- No frontend, E2E, Agent smoke, autonomous, external validation, projection
  readiness, or product readiness pass claim is made.

## Final Assessment State

Current value: `final / closeout complete`.
