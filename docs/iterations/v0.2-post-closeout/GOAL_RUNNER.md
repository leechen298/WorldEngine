# GOAL_RUNNER.md

Purpose: provide Codex App `/goal` routing instructions for the WorldEngine
`v0.2-post-closeout` validation chain.

This file is a routing aid. It does not reopen v0.2 implementation and does not
change v0.2 release status.

## Authoritative Inputs

Before running any validation goal, read:

- `CURRENT_STATE.md`
- `validation-master-plan.md`
- `README.md`
- `findings.md`
- the active package `README.md`, `intent.md`, `contract.md`, `plan.md`, and
  `review.md`
- the active package `test-plan.md` when present
- the relevant execution report or template when the package has one
- `docs/iterations/AGENTS.md`
- root `AGENTS.md`

If these conflict with actual git state, stop as `NEEDS_USER_INPUT`.

## Execution Modes

Default mode: one validation package per `/goal`.

- Work on exactly one package.
- Stop after the package reaches a final route status.
- Do not continue to the next package unless the user explicitly asks for full
  campaign mode.

Full campaign mode:

- Continue only when the current package reaches `PACKAGE_COMPLETE`.
- Stop on `BLOCKED`, `FAILED`, `FOLLOW_UP_REQUIRED`, `NEEDS_USER_INPUT`,
  source conflict, or evidence insufficiency.

## Route Types

- `review-closeout-plan`
- `validation-execution`
- `autonomous-review-execution`
- `final-bundle-closeout`

## Runtime Authorization

This validation chain must not modify implementation files.

Forbidden during all packages:

- runtime code changes
- schema changes
- API changes
- frontend changes
- backend test changes
- fixture changes
- migration changes
- external repository changes

Validation execution may run commands and update validation documents only when
the active package owns that execution.

## Final Status Vocabulary

Use these exact route statuses:

- `PACKAGE_COMPLETE`
- `REVIEW_READY`
- `NOT_EXECUTED`
- `BLOCKED`
- `FAILED`
- `PASSED_WITH_P3`
- `NEEDS_USER_INPUT`
- `FOLLOW_UP_REQUIRED`

Do not convert `blocked`, `failed`, or `not executed` into `passed` by wording.
Evidence controls status.

## Package Routing

Current default route:

```text
03-codex-autonomous-validation-plan review-closeout-plan
```

Do not execute autonomous validation in `03`.

`03` only reviews whether the plan is sufficient for
`04-codex-autonomous-validation-execution`.

`04` owns independent Codex autonomous validation execution.

`05` owns final bundle synthesis and the v0.4 proceed decision.

## Hard Stops

Stop if:

- required files are missing;
- git state conflicts with package status;
- a package claims passed without command evidence;
- a command cannot run and no blocker is recorded;
- `findings.md` has unresolved P1/P2 and the current package tries to declare a
  clean final pass;
- execution would require implementation changes;
- the final bundle tries to allow v0.4 without completed E2E / API / backend
  and Codex autonomous validation evidence.

## Required Closeout Per Package

Before ending a package goal, update the package `review.md` with:

- changed files;
- files read;
- commands run;
- commands not run;
- test results;
- compatibility review;
- scope review;
- unresolved P1/P2/P3;
- final status.

Keep `CURRENT_STATE.md` aligned with the latest package status.
