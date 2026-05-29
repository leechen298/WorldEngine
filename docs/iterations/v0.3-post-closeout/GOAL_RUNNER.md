# GOAL_RUNNER.md

Purpose: define Codex App `/goal` prompt and campaign guidance for
`v0.3-post-closeout`.

This is not WorldEngine runtime behavior. It is not an automation-controller
implementation. Scheduling, orchestration, retry infrastructure, and Codex
role assignment belong to the Codex environment or other external tools.

This file only defines the readable entrypoint, state machine, stop
conditions, evidence rules, and review update rules for this validation
campaign.

## Campaign Entry

When the user says:

```text
完成 v0.3-post-closeout
```

Codex should run the campaign according to this file, `CURRENT_STATE.md`, and
`CAMPAIGN_PLAN.md`.

Default behavior:

- Start from the active child package in `CURRENT_STATE.md`.
- Read the child package documents before choosing any route.
- Advance only after the active child reaches its required exit state.
- Stop on blocker, failed evidence, missing required files, source conflict,
  or out-of-scope change.

## First-Read Files

Read these parent files first:

- `README.md`
- `CURRENT_STATE.md`
- `CAMPAIGN_PLAN.md`
- `validation-master-plan.md`
- `validation-report-template.md`
- `review.md`
- `docs/iterations/AGENTS.md`
- root `AGENTS.md`

Then read the active child package:

- `README.md`
- `intent.md`
- `contract.md`
- `plan.md` or `execution-plan.md`
- `test-plan.md` when present
- the relevant report or review template when present
- `review.md`

For validation execution and autonomous review, also read the v0.3 source
inputs listed in `validation-master-plan.md`.

## Child Package Order

1. `01-e2e-validation-plan`
2. `02-e2e-validation-execution`
3. `03-codex-autonomous-validation-plan`
4. `04-codex-autonomous-validation-execution`
5. `05-final-validation-bundle`

`03` plans autonomous validation. `04` owns autonomous validation execution.
`05` synthesizes only evidence that is current, explicitly accepted, or
recorded as blocked.

## Allowed Route Types

- `goal-entry`
- `documentation-planning`
- `human-review`
- `validation-execution`
- `autonomous-review-planning`
- `autonomous-review-execution`
- `repair-loop`
- `blocker-recording`
- `final-bundle-synthesis`
- `needs-user-input`

The parent campaign does not authorize runtime, schema, API, frontend,
fixture, migration, backend test, or external repository changes.

## Stop Conditions

Stop and record `blocked` or `failed` when:

- backend deterministic tests fail.
- API smoke fails.
- loader validation fails.
- runtime context bridge validation fails.
- runtime compatibility claim conflicts with actual behavior.
- release claim conflicts with actual behavior.
- Codex autonomous reviewer reports P1.
- concrete demo-world regression appears.
- commands cannot run and no blocker is recorded.
- a required file is missing.
- the active package would need implementation changes not authorized by its
  contract.
- validation evidence is missing but a report tries to make a pass claim.
- git state shows out-of-scope modifications.

## Evidence Requirements

Any future execution claim must record:

- reviewed branch.
- execution branch.
- evidence commit.
- final documentation commit, when available.
- validation date.
- executor.
- exact commands run.
- command outputs or summarized results.
- checks not run and why.
- P1/P2/P3 findings.
- blockers.
- final assessment using the vocabulary allowed by the active report.

Historical v0.3 package evidence may be cited as archived context, but it does
not count as fresh validation for this campaign unless explicitly rerun or
accepted with rationale.

## Review Update Rules

Every child closeout must update its `review.md` with:

- changed files.
- files read.
- commands run.
- commands not run.
- test results.
- compatibility review.
- scope review.
- unresolved P1/P2/P3.
- final assessment.

The parent `CURRENT_STATE.md` may be updated only when a child reaches a
reviewed route status. The parent `review.md` records the documentation
creation pass and later campaign-level changes.

## Repair Loop Rules

If validation execution finds a P1 or P2:

- classify the finding.
- do not modify implementation unless a future reviewed repair package
  explicitly authorizes it.
- record the blocker or failure in the active execution report.
- update the child `review.md`.
- stop before advancing to the next child unless the child contract explicitly
  allows a documented carry.

P3 findings may be carried only with an explicit handoff target and rationale.

## No Unverified Claims Rule

Do not say a test, API smoke, E2E run, Codex autonomous review, backend
regression, frontend build, migration, fixture run, loader validation, bridge
validation, or compatibility claim succeeded unless it was run in the current
campaign or explicitly recorded as accepted historical evidence.

Templates must start as `not executed` and must not prefill successful results.

## No Scope Expansion Rule

This campaign must not:

- reopen v0.3 implementation.
- change v0.3 release status.
- implement v0.4 work.
- add demo-world content.
- create an external repository.
- add private validation oracle details.
- change runtime, schema, API, frontend, backend tests, fixtures, migrations,
  or legacy `backend/worldengine/` files.
