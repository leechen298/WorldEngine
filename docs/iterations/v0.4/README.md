# v0.4 Agent-in-World Minimal Loop

Status: final / closeout complete
Type: Codex `/goal` development campaign and iteration package root

## Goal

v0.4 establishes the minimal Agent-in-World loop. The version lets agents perceive world events, produce action intents, receive action results, and affect world state through a small validated boundary.

This campaign has completed the implementation-bearing children, evidence audit, release-candidate bundle, and final closeout. Runtime, schema, API, frontend, test, fixture, migration, or legacy code changes are closed unless a later reviewed package explicitly reopens them.

## Goal Entry

Natural-language goal:

```text
完成 v0.4
```

Interpretation:

- Start from `CURRENT_STATE.md`.
- Follow `GOAL_RUNNER.md` for route selection, subagent/evaluator checkpoints, implementation authorization, verification, and stop conditions.
- Follow `CAMPAIGN_PLAN.md` and `v0.4-plan.md` for child sequence, deliverables, compatibility constraints, and handoff rules.
- Read the active child package docs before doing any child work.

This is not an automation-controller implementation. Scheduling, orchestration, retry infrastructure, and Codex role assignment belong to the Codex environment or external tools.

## Scope

Allowed v0.4 scope:

- minimal perception frame from runtime state, recent events, current world params, and optional runtime context summary.
- minimal action intent and action result contracts.
- validated `noop` and `params.patch` action effects.
- request-driven loop orchestration.
- additive backend schemas, internal services, API route only when a child package contract explicitly authorizes it, and focused tests.

Forbidden v0.4 scope:

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

## Deliverables

- Parent goal-campaign documents: `README.md`, `v0.4-plan.md`, `GOAL_RUNNER.md`, `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, and `review.md`, with Chinese mirrors.
- Eight child package document sets, each with README, intent, contract, technical design, test plan, plan, review, and Chinese mirrors.
- Explicit subagent/evaluator checkpoint rules for `/goal` execution.
- Documentation-stage/root review evidence plus final implementation, compatibility, and closeout evidence.

## Package Index

### `0.4.0-v0.4-planning-and-compatibility-baseline`

- Type: documentation-only
- Status: review complete
- Purpose: create the v0.4 documentation root, goal-campaign controls, version plan, compatibility baseline, and v0.3 handoff mapping without changing implementation files.

### `0.4.1-agent-in-world-loop-contract`

- Type: documentation-only
- Status: review complete
- Purpose: define the public v0.4 Agent-in-World loop concepts, event semantics, API boundary, error model, and implementation authorization criteria before code changes.

### `0.4.2-agent-perception-and-schemas`

- Type: mixed or code
- Status: review complete
- Purpose: add generic Agent-in-World schema models and a bounded perception builder that reads runtime state, recent events, world params, and optional runtime-context summary without mutating state.

### `0.4.3-action-intent-validation-and-result-adapter`

- Type: mixed or code
- Status: review complete
- Purpose: implement the minimal generic action intent validator and result adapter for noop and validated params.patch, reusing existing param validation and dry-run safeguards.

### `0.4.4-minimal-agent-loop-orchestration-and-api`

- Type: mixed or code
- Status: review complete
- Purpose: wire a request-driven minimal Agent-in-World loop that builds perception, obtains or accepts an intent, validates and applies the intent, emits inspectable result evidence, and returns a stable API response.

### `0.4.5-agent-loop-evidence-and-compatibility-audit`

- Type: documentation-only
- Status: review complete
- Purpose: audit v0.4 implementation evidence, changed files, compatibility surfaces, unresolved findings, and handoff readiness for release-candidate review.

### `0.4.6-v0.4-release-candidate-bundle`

- Type: documentation-only
- Status: review complete
- Purpose: prepare a v0.4 release-candidate bundle from reviewed implementation and audit evidence without declaring final release or adding implementation changes.

### `0.4.7-v0.4-final-closeout`

- Type: documentation-only
- Status: final / closeout complete
- Purpose: mark v0.4 final / closeout complete only after release-candidate review approval, evidence consistency checks, and unresolved finding classification.

## Current State

Active child package: none - v0.4 final / closeout complete.

Current route: final-closeout-complete. v0.4 is final / closeout complete after evidence and evaluator checks passed.

## Final Assessment State

Current value: `final / closeout complete`.

Future packages must record their own evidence before making runtime, API, test, E2E, or release claims.
