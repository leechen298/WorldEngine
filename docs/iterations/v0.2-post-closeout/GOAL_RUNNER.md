# GOAL_RUNNER.md

Purpose: provide Codex App `/goal` routing instructions for the WorldEngine
`v0.2-post-closeout` goal campaign.

This file is the campaign state machine. It does not change v0.2 release
status. Implementation is controlled by each child package contract, not by
the parent campaign alone.

## Authoritative Inputs

Before running any campaign goal, read:

- `CURRENT_STATE.md`
- `CAMPAIGN_PLAN.md`
- `validation-master-plan.md`
- `README.md`
- `findings.md`
- the active package `README.md`, `intent.md`, `contract.md`, `plan.md`, and
  `review.md`
- the active package `technical-design.md` and `test-plan.md` when present
- the relevant execution report or template when the package has one
- `docs/iterations/AGENTS.md`
- root `AGENTS.md`

If these conflict with actual git state, stop as `NEEDS_USER_INPUT`, except
when the only conflict is archived pre-reset evidence that
`CURRENT_STATE.md` explicitly marks as non-current.

## Execution Modes

Default mode: full campaign when the user says `完成 v0.2-post-closeout`.

- Start from `CURRENT_STATE.md`.
- Execute the active child package according to `CAMPAIGN_PLAN.md`.
- Continue to the next child only when the current child reaches
  `PACKAGE_COMPLETE` or another exit status explicitly accepted by the next
  child contract.
- Stop on `BLOCKED`, `FAILED`, `FOLLOW_UP_REQUIRED`, `NEEDS_USER_INPUT`,
  source conflict, evidence insufficiency, or out-of-scope changes.

Single child mode:

- Use only when the user names one child package or explicitly says not to run
  full campaign mode.
- Work on exactly one package.
- Stop after the package reaches a final route status.

Full child-package cycle mode:

- The user may request `full child-package cycle` for a child package goal.
- In that mode, Codex may run all gates selected by the adaptive child package
  cycle inside one goal: documentation work, read-only evaluator or subagent
  review, `implementation_authorized: yes` when allowed, implementation,
  verification, code review, repair loops, and closeout.
- This does not allow skipping gates. It means the gates are executed inside
  the same goal instead of requiring separate user-driven prompts.
- If the package contract, current routing state, or Implementation
  Authorization forbids implementation, the goal must stop before
  implementation or route as `NEEDS_USER_INPUT`.

## Route Types

- `campaign-restart`
- `goal-entry`
- `gate-selection`
- `documentation-review`
- `review-closeout-plan`
- `implementation-execution`
- `validation-execution`
- `code-review`
- `evaluator-review`
- `repair-loop`
- `verification-escalation`
- `autonomous-review-execution`
- `final-bundle-closeout`

## Adaptive Child Package Cycle

Do not run a fixed phase list blindly. For each child package, classify the
package shape and risk first, then select the simplest gate set that satisfies
the child contract, evidence requirements, and stop conditions.

Always run these baseline gates:

1. Read parent routing docs and the active child package docs.
2. Confirm package type, allowed files, forbidden files, required commands, and
   final status vocabulary.
3. Compare requested work with the child contract and current git state.
4. Record command evidence, blockers, and final status truthfully in
   `review.md`.
5. Run the Closeout Consistency Gate before any final status is written.

Gate selection:

| Package shape | Required gates |
|---|---|
| Documentation-only or planning | Documentation update, read-only documentation review when routing or contract quality is material, P0 / P1 documentation repair, closeout evidence. No implementation. |
| Validation-only | Environment and command readiness check, required validation commands or concrete blockers, findings classification, closeout evidence. No implementation unless a separate child contract explicitly authorizes repair. |
| Code or mixed | Documentation / contract gate, implementation authorization, scoped implementation, focused tests, code review or evaluator review, P0 / P1 repair loop, broader regression or E2E only when the contract or blast radius requires it, closeout evidence. |
| Autonomous validation | Independent review execution, command evidence or blocker evidence, P0 / P1 classification, recommendation, closeout evidence. Do not fix implementation unless the child contract authorizes repair. |
| Final bundle | Synthesize current evidence and findings disposition. Rerun commands only to resolve evidence conflicts or missing required proof. Do not create new implementation scope. |

Subagent and evaluator use:

- Use read-only subagents or evaluator passes when independent review improves
  confidence: broad code changes, security / compatibility risk, mirror
  quality, release claims, or autonomous validation.
- Use orchestrator-worker style only when independent subtasks can be separated
  cleanly. Keep one controlling goal responsible for synthesis and final
  status.
- Do not spawn subagents for trivial docs-only changes unless the package
  contract requires a review record.
- Subagent findings must be classified as P0 / P1 / P2 / P3 and either fixed,
  downgraded with rationale, carried where allowed, or recorded as blockers.

Verification escalation:

- Start with focused checks named by the child `test-plan.md`, execution plan,
  or review template.
- Escalate to broader backend, API smoke, E2E, or autonomous validation only
  when required by the child contract, changed-file blast radius, or unresolved
  evidence conflict.
- Never claim an unrun check passed. If a required check cannot run, record the
  exact blocker and route as `BLOCKED`, `FAILED`, or `NEEDS_USER_INPUT`.

The goal may loop through review, repair, and verification multiple times. It
may change the order of selected gates when evidence requires it, but it must
not skip a required gate by wording.

## Implementation Authorization

The parent campaign does not globally authorize implementation changes.

Implementation is allowed only when all are true:

- the active child package contract allows implementation;
- required documentation gates have passed;
- the relevant `review.md` records `implementation_authorized: yes`;
- changed files stay within the child contract;
- verification and review evidence are recorded before closeout.

Forbidden unless the child contract and implementation gate explicitly allow
the change:

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

- `CAMPAIGN_READY`
- `RESTART_READY`
- `PACKAGE_COMPLETE`
- `REVIEW_READY`
- `NOT_EXECUTED_CURRENT_CAMPAIGN`
- `NOT_EXECUTED`
- `BLOCKED`
- `FAILED`
- `PASSED_WITH_P3`
- `NEEDS_USER_INPUT`
- `FOLLOW_UP_REQUIRED`
- `ARCHIVED_EVIDENCE_ONLY`

Do not convert `blocked`, `failed`, `not executed`, or archived evidence into
`passed` by wording. Evidence controls status.

## Package Routing

Current default route:

```text
01-e2e-validation-plan campaign-restart
```

The campaign was reset to `unverified_restart`. Historical results remain
archived, but they do not count as current campaign completion evidence unless
the current goal reruns or explicitly re-accepts the relevant gate.

Restart sequence:

1. `01-e2e-validation-plan`
2. `02-e2e-validation-execution`
3. `03-codex-autonomous-validation-plan`
4. `04-codex-autonomous-validation-execution`
5. `05-final-validation-bundle`

Do not execute autonomous validation in `03`.

`03` only reviews whether the plan is sufficient for
`04-codex-autonomous-validation-execution`.

`04` owns independent Codex autonomous validation execution.

`05` owns final bundle synthesis and the v0.4 proceed decision.

## Hard Stops

Stop if:

- required files are missing;
- git state conflicts with package status, except for explicitly archived
  pre-reset evidence;
- a package claims passed without command evidence or explicit re-acceptance
  rationale;
- a command cannot run and no blocker is recorded;
- `findings.md` has unresolved P1/P2 and the current package tries to declare a
  clean final pass;
- implementation is required but the child contract has not authorized it;
- the final bundle tries to allow v0.4 without completed E2E / API / backend
  and Codex autonomous validation evidence.

## Closeout Consistency Gate

Before any child goal may write a final status, it must compare actual changed
files with the changed-files list in the relevant `review.md`.

Required checks:

- `git status --short`
- `git diff --name-only`
- `git diff --check`

Rules:

- Every created, modified, or deleted in-scope file must be listed in the
  relevant `review.md` changed-files section.
- If an in-scope docs-only support file is missing from `review.md`, update
  `review.md` in the same goal and continue.
- If an unlisted runtime, test, eval, external result, fixture, schema, API,
  worker, frontend, or out-of-scope file appears, stop as `NEEDS_USER_INPUT`.
- Do not ask the user to manually repair docs-only changed-file omissions.

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
- implementation authorization state;
- final status.

Keep `CURRENT_STATE.md` aligned with the latest package status.
