# Campaign Plan

Status: campaign complete / passed
Type: Codex `/goal` campaign plan

## Purpose

`CAMPAIGN_PLAN.md` defines the child-package sequence for the durable goal:

```text
完成 v0.2-post-closeout
```

The campaign follows the Codex `/goal` pattern: one objective, authoritative
inputs, a repeatable validation loop, checkpointed evidence, and explicit stop
conditions. The goal runner is `GOAL_RUNNER.md`; the current route source is
`CURRENT_STATE.md`.

## Current Restart Position

This campaign is running from the `unverified_restart` reset.

Historical validation evidence remains in package reports. The current `/goal`
run has rerun `02-e2e-validation-execution` and accepted
`03-codex-autonomous-validation-plan`. Independent Codex autonomous validation
has passed in `04-codex-autonomous-validation-execution`; the campaign now
closed with `05-final-validation-bundle`.

## Campaign Objective

Complete the `v0.2-post-closeout` validation campaign from the current active
child package through final bundle closeout.

The campaign must:

- preserve v0.2 release status as final / closeout complete;
- avoid application-specific or demo-world implementation drift;
- keep historical evidence visible;
- produce current-session command evidence for any current pass claim;
- use read-only subagent or evaluator reviews where the active child requires
  review or where risk justifies independent evaluation;
- repair P0 / P1 findings before advancing;
- either fix, downgrade with rationale, or explicitly carry unresolved P2/P3;
- stop instead of inventing success when evidence is missing.

## Child Sequence

| Order | Child package | Current status | Required exit before next child |
|---|---|---|---|
| 1 | `01-e2e-validation-plan` | `PACKAGE_COMPLETE` | current-campaign planning review re-accepted |
| 2 | `02-e2e-validation-execution` | `PACKAGE_COMPLETE` | current-campaign backend, API smoke, Playwright availability, and host-capable E2E evidence passed |
| 3 | `03-codex-autonomous-validation-plan` | `PACKAGE_COMPLETE` | autonomous validation plan accepted; no autonomous validation executed here |
| 4 | `04-codex-autonomous-validation-execution` | `PACKAGE_COMPLETE` | independent Codex autonomous validation passed |
| 5 | `05-final-validation-bundle` | `PACKAGE_COMPLETE` | final campaign status recorded as `passed` |

Default campaign progression advances only when the active child reaches
`PACKAGE_COMPLETE` or an explicitly accepted status that the next child
contract allows. Stop on `BLOCKED`, `FAILED`, `FOLLOW_UP_REQUIRED`,
`NEEDS_USER_INPUT`, evidence insufficiency, or source conflict.

## Adaptive Child Cycle

For each child package, Codex must select gates by package type, contract, and
risk instead of following a rigid phase list. The goal is to keep the campaign
autonomous without adding unnecessary agent complexity.

Baseline gates for every child:

1. Read parent `CURRENT_STATE.md`, `GOAL_RUNNER.md`, this file, parent
   `README.md`, `findings.md`, and the active child package documents.
2. Confirm the child contract, package type, allowed files, forbidden files,
   required commands, and exit criteria.
3. Compare the requested work with current git state.
4. Run the Closeout Consistency Gate from `GOAL_RUNNER.md`.
5. Update child `review.md`, parent `CURRENT_STATE.md`, and `findings.md` as
   needed.

Workflow selection:

| Child type | Selected workflow |
|---|---|
| Planning or documentation-only | Draft / update docs, run read-only documentation review when the contract or routing evidence is material, fix P0 / P1 documentation findings, close out. |
| Validation execution | Run required commands or record concrete blockers, classify findings, avoid implementation unless separately authorized, close out. |
| Code or mixed implementation | Pass documentation / contract gate, record `implementation_authorized: yes`, implement within scope, run focused verification, run evaluator or code review, fix P0 / P1, escalate to broader tests or E2E when required, close out. |
| Autonomous validation | Run independent Codex review and required commands, record findings and recommendation, do not repair implementation unless the contract authorizes it, close out. |
| Final validation bundle | Synthesize current evidence and findings disposition, rerun only to resolve evidence conflicts or missing proof, decide final campaign result. |

Subagents are mandatory checkpoints for `/goal` development-mode child work
that is implementation-bearing or full child-package cycle. Use the mandatory
documentation / contract, implementation-scope, code-review,
validation-evidence, and closeout consistency checkpoints from
`docs/iterations/AGENTS.md`.

Subagents remain non-ceremonial: do not use them to bypass contract gates,
write final status without evidence, or expand scope beyond the active child
package. Trivial docs-only edits may skip subagents only when they do not affect
any gate, contract, status, claim, automation route, or mirror obligation.

The campaign may loop through review, repair, and verification more than once.
It may reorder selected gates when evidence requires it, but it must not skip a
required gate by wording.

## Implementation Authorization

The parent campaign does not globally authorize implementation changes.

Implementation is allowed only when all are true:

- the active child package contract allows implementation;
- required documentation gates have passed;
- `review.md` records `implementation_authorized: yes`;
- changed files stay within the child contract;
- verification and review evidence are recorded before closeout.

If any condition is false, the child must remain documentation-only or stop as
`NEEDS_USER_INPUT`.

## Current Campaign Exit Criteria

The campaign is complete. `05-final-validation-bundle` records:

- `passed`

The final bundle must summarize:

- current `02` validation evidence or accepted blocker;
- current `04` Codex autonomous validation evidence or accepted blocker;
- open `findings.md` rows and their final disposition;
- whether v0.4 may proceed;
- commands run and commands not run;
- changed-file consistency check results;
- compatibility and scope review.

## Required Proof Commands

Each child closeout must run:

```bash
git status --short
git diff --name-only
git diff --check
```

Execution-bearing child packages must also run the commands specified by their
own `test-plan.md`, execution plan, or review template, unless the package
records a concrete blocker.

## Hard Stops

Stop the campaign if:

- a required child package file is missing;
- the active child contract conflicts with the requested action;
- a command cannot run and no blocker is recorded;
- a package claims passed without current-session command evidence or explicit
  re-acceptance rationale;
- unlisted runtime, test, eval, external result, fixture, schema, API, worker,
  frontend, or out-of-scope files appear;
- implementation would be required but the child package has not authorized it;
- `findings.md` has unresolved P0 / P1 or unaccepted P2 at final bundle time.
