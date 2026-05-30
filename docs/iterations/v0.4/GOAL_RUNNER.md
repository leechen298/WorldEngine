# GOAL_RUNNER.md

Purpose: define Codex App `/goal` prompt and campaign guidance for v0.4.

This file is not WorldEngine runtime behavior and not an automation-controller implementation. It defines the readable entrypoint, state machine, implementation authorization rule, subagent/evaluator checkpoints, stop conditions, evidence rules, and review update rules for the v0.4 development campaign.

## Campaign Entry

When the user says:

```text
完成 v0.4
```

Codex should run the campaign according to this file, `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, and the active child package documents.

Default behavior:

- Start from the active child package in `CURRENT_STATE.md`.
- Read parent docs, then read the active child package docs.
- Advance only after the active child reaches its required exit state.
- Stop on blocker, failed evidence, missing required file, source conflict, out-of-scope change, or missing required evaluator checkpoint.

## First-Read Files

- `README.md`
- `CURRENT_STATE.md`
- `CAMPAIGN_PLAN.md`
- `v0.4-plan.md`
- `review.md`
- `docs/iterations/AGENTS.md`
- root `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/v0.3-post-closeout/05-final-validation-bundle/final-validation-bundle.md`

Then read the active child package: `README.md`, `intent.md`, `contract.md`, `technical-design.md`, `test-plan.md`, `plan.md`, and `review.md`.

## Child Package Order

1. `0.4.0-v0.4-planning-and-compatibility-baseline`
2. `0.4.1-agent-in-world-loop-contract`
3. `0.4.2-agent-perception-and-schemas`
4. `0.4.3-action-intent-validation-and-result-adapter`
5. `0.4.4-minimal-agent-loop-orchestration-and-api`
6. `0.4.5-agent-loop-evidence-and-compatibility-audit`
7. `0.4.6-v0.4-release-candidate-bundle`
8. `0.4.7-v0.4-final-closeout`

## Allowed Route Types

- `goal-entry`
- `documentation-planning`
- `contract-review`
- `human-review`
- `implementation-authorization-review`
- `schema-implementation`
- `action-validation-implementation`
- `loop-orchestration-implementation`
- `evidence-audit`
- `release-candidate-review`
- `final-closeout`
- `repair-loop`
- `blocker-recording`
- `needs-user-input`

## Implementation Authorization Rule

A child package may record `implementation_authorized: yes` only when the child package contains the full seven-file set, contract/design/test-plan/plan have been reviewed, a documentation / contract evaluator reports no P1 or unresolved P2 findings, the active package contract explicitly allows the relevant file classes, and `review.md` records authorization plus findings.

Documentation-only children never authorize runtime implementation unless a later implementation-bearing child repeats this rule.

## Mandatory Subagent / Evaluator Checkpoints

Implementation-bearing child packages must include:

1. Documentation / contract evaluator before `implementation_authorized: yes`.
2. Implementation-scope evaluator after files are changed and before broad verification.
3. Code-review subagent or evaluator after focused tests and before final status.
4. Validation-evidence evaluator before marking tests, API smoke, E2E, backend checks, or runtime behavior as passed.
5. Closeout consistency review before `review.md` records a final route status.

Documentation-only children require a read-only documentation evaluator when they change goal routing, process rules, evidence rules, package sequencing, validation templates, release status, automation-consumption contracts, or English / Chinese mirror obligations.

Subagents are read-only by default. A subagent may edit files only when the active child contract explicitly allows worker implementation and the main agent records the delegated write scope.

## Stop Conditions

Stop and record `blocked`, `failed`, or `needs-user-input` when:

- a required parent or child document is missing.
- a required evaluator checkpoint is unavailable.
- a required evaluator reports P1 or unresolved P2.
- implementation would touch files not allowed by the active child contract.
- runtime, schema, API, frontend, fixture, migration, or backend test changes are needed from a documentation-only package.
- tests fail and the active package does not authorize repair.
- command evidence is missing but a report tries to claim pass.
- implementation tries to add out-of-scope later-version work or concrete world/application behavior.
- git state shows out-of-scope modifications.

## Evidence Requirements

Any future execution claim must record branch, commit, active child package, executor, changed files, files read when relevant, exact commands run, summarized command results, checks not run and why, subagent/evaluator checkpoints, P1/P2/P3 findings, compatibility review, scope review, and final assessment.

Historical v0.3 evidence is handoff context. It does not count as fresh v0.4 implementation or validation evidence unless a child contract explicitly accepts it with rationale.

## Review Update Rules

Every child closeout must update its `review.md` with changed files, commands run, commands not run, test results, compatibility review, scope review, subagent/evaluator findings, unresolved P1/P2/P3, and final assessment.

Parent `CURRENT_STATE.md` may be updated only when a child reaches a reviewed route status.

## No Scope Expansion Rule

This campaign must not bypass iteration package review gates, implement v0.5 memory/self-continuity, implement v0.6 world generation, implement v0.7 external validation readiness, implement v0.8 projection readiness, add concrete world content, add application-specific backend logic, or add new runtime features under `backend/worldengine/`.
