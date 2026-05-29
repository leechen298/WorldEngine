# v0.2 Post-Closeout Goal Campaign

Status: campaign complete / passed
Type: goal campaign package

## Goal

Make `v0.2-post-closeout` runnable from one durable Codex App `/goal`
objective, with clear first-read files, child-package routing, verification
loops, stop conditions, and closeout evidence.

v0.2 feature and documentation closeout remains complete. This campaign is a
post-closeout validation and goal-running package. It does not change v0.2
release status.

## Goal Entry

Natural-language goal:

```text
完成 v0.2-post-closeout
```

Interpretation:

Run this package as a full campaign goal according to `GOAL_RUNNER.md`,
`CURRENT_STATE.md`, and `CAMPAIGN_PLAN.md`.

Start from the current active child package in `CURRENT_STATE.md`. For each
child package, select the gates defined in `GOAL_RUNNER.md` according to child
type, contract, and risk. Typical gates include documentation work, read-only
review, implementation authorization when the child contract allows it,
implementation if authorized, focused verification, evaluator or code review,
repair loops, broader regression / E2E when required, Codex autonomous
validation when required, closeout consistency, and `review.md` update.

Stop on `BLOCKED`, `FAILED`, `FOLLOW_UP_REQUIRED`, `NEEDS_USER_INPUT`, source
conflict, evidence insufficiency, or any attempt to modify files outside the
active child package contract.

This aligns the package with the Codex `/goal` model: one durable objective,
verifiable stopping conditions, first-read files, proof commands / artifacts,
checkpointed progress, and explicit pause conditions.

Reference: <https://developers.openai.com/codex/use-cases/follow-goals#introduction>

## Current Routing Note

This package was originally created as a documentation-only post-closeout
validation chain. A previous `02-e2e-validation-execution` run records
`passed` with 2026-05-29 evidence.

That evidence remains archived for audit, but this package has been reset to
`campaign ready / unverified restart` so `/goal 完成 v0.2-post-closeout` can
start from the beginning of the child sequence instead of inheriting earlier
completion claims.

The active restart sequence is now:

1. `01-e2e-validation-plan` is re-accepted as `PACKAGE_COMPLETE`;
2. `02-e2e-validation-execution` has passed with current-campaign evidence;
3. `03-codex-autonomous-validation-plan` has been accepted for handoff;
4. `04-codex-autonomous-validation-execution` has passed;
5. `05-final-validation-bundle` has passed and closed the campaign.

Use `CURRENT_STATE.md` as the current route source, `GOAL_RUNNER.md` as the
execution state machine, and `CAMPAIGN_PLAN.md` as the campaign-level child
sequence and closeout contract.

## Governance

This validation documentation follows the evidence, review, and post-closeout
validation rules defined in `docs/iterations/AGENTS.md` as files under
`docs/iterations/v0.2-post-closeout/`.

## Validation Chain

0. Master validation planning.
1. E2E / integration / API smoke validation plan.
2. E2E / integration / API smoke execution report.
3. Codex autonomous validation plan.
4. Codex autonomous validation execution and review template.
5. Final validation bundle template.

## Package Index

| Package | Type | Status | Purpose |
|---|---|---|---|
| `01-e2e-validation-plan` | validation-planning | package complete / planning re-accepted | Define / re-accept v0.2 post-closeout E2E, integration, and API smoke validation scope. |
| `02-e2e-validation-execution` | validation-execution | package complete / passed current campaign | Execute v0.2 post-closeout E2E, integration, and API smoke validation. |
| `03-codex-autonomous-validation-plan` | validation-planning | package complete / plan accepted | Define independent Codex autonomous validation scope. |
| `04-codex-autonomous-validation-execution` | validation-execution | package complete / passed current campaign | Execute independent Codex autonomous validation. |
| `05-final-validation-bundle` | validation-bundle | package complete / passed current campaign | Summarize final v0.2 post-closeout validation result. |

## Result States

Validation documents may use these states:

- `planned`
- `ready for execution`
- `executed`
- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`
- `not executed in current campaign`
- `archived evidence only`

Execution reports start as `not executed` until a validation run fills them
with current-session evidence. Historical results may remain visible in package
reports, but after this restart they are `archived evidence only` unless the
current campaign explicitly reruns or re-accepts them.

## Scope

Allowed:

- Define post-closeout validation workflow.
- Define report templates and evidence requirements.
- Define E2E / integration / API smoke execution expectations.
- Define Codex autonomous validation expectations.
- Define final validation bundle requirements.
- Define full-campaign `/goal` routing and restart semantics.

Forbidden:

- Do not run backend, frontend, E2E, API smoke, runtime, schema execution,
  fixture, migration, or autonomous validation commands while updating planning
  or routing documents.
- Do not run validation commands outside the package that explicitly owns that
  validation execution.
- Do not modify runtime, schema, API, frontend, backend tests, fixtures, or
  external repositories unless a child package contract explicitly authorizes
  implementation and the `GOAL_RUNNER.md` implementation gate has passed.
- Do not add concrete demo-world names, locations, characters, resources,
  story rules, seed data, UI selectors, or private oracle details.
- Do not declare a completed v0.2 final validation result before `04` and `05`
  are closed with evidence.
- Do not change v0.2 final / complete status.

## Deliverables

- `CURRENT_STATE.md`
- `CURRENT_STATE.zh.md`
- `GOAL_RUNNER.md`
- `GOAL_RUNNER.zh.md`
- `CAMPAIGN_PLAN.md`
- `CAMPAIGN_PLAN.zh.md`
- `validation-master-plan.md`
- `validation-master-plan.zh.md`
- `validation-report-template.md`
- `validation-report-template.zh.md`
- `review.md`
- `review.zh.md`
- `01-e2e-validation-plan/`
- `02-e2e-validation-execution/`
- `03-codex-autonomous-validation-plan/`
- `04-codex-autonomous-validation-execution/`
- `05-final-validation-bundle/`

## Final Assessment State

The Codex App `/goal` campaign is complete. Final assessment: `passed`.

v0.4 may proceed only through a separate reviewed v0.4 planning or iteration
package. This package does not reopen v0.2 implementation and does not change
v0.2 release status.
