# CURRENT_STATE.md

This file is the current routing snapshot for Codex App `/goal` campaign work
on `v0.2-post-closeout`.

It is intentionally short. Historical evidence remains in package reports, but
the current campaign state below is authoritative for new `/goal` runs.

## Snapshot

current_mode: full_campaign_restart
parent_package: v0.2-post-closeout
parent_status: CAMPAIGN_READY
campaign_verification_status: unverified_restart
v0.2_release_status: final / closeout complete
reopens_v0.2_implementation: no
implementation_changes_allowed: child_contract_controlled
one_sentence_goal: 完成 v0.2-post-closeout

## Current Progress

| Package | Current route status | Next action |
|---|---|---|
| `01-e2e-validation-plan` | `RESTART_READY` | rerun planning review as the first child campaign checkpoint |
| `02-e2e-validation-execution` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | rerun after `01` reaches `PACKAGE_COMPLETE` |
| `03-codex-autonomous-validation-plan` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | review-closeout after `02` reaches `PACKAGE_COMPLETE` or records accepted blocker |
| `04-codex-autonomous-validation-execution` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | execute only after `03` reaches `PACKAGE_COMPLETE` |
| `05-final-validation-bundle` | `NOT_EXECUTED_CURRENT_CAMPAIGN` | fill only after `04` reaches `PACKAGE_COMPLETE`, `BLOCKED`, or `FAILED` |

## Active Package

active_package: 01-e2e-validation-plan
next_action: restart-child-campaign-from-01
goal_mode: full_campaign
handoff_target: 02-e2e-validation-execution

## Evidence Policy

evidence_package: 02-e2e-validation-execution
archived_status: passed
evidence_date: 2026-05-29
evidence_branch: v0.3-lcoal
evidence_commit: dbffa069a5e74b6b1e6b60719152922595c60df6
current_campaign_counts_this_as_passed: no

archived_results:

- backend deterministic: passed, 115 passed
- API smoke: passed
- Playwright availability: passed
- configured browser E2E: passed, 6 passed

historical_blockers:

- prior localhost bind blocker resolved by host-capable rerun

Restart rule:

- Do not count archived results as current campaign completion evidence.
- Keep archived evidence visible for audit and comparison.
- New `/goal` work must rerun or explicitly re-accept each child package gate
  according to `GOAL_RUNNER.md` and `CAMPAIGN_PLAN.md`.

## Known Open Findings

- `v0.2-post-closeout-P2-001`: Chinese mirrors are too English-heavy.
  Must resolve, downgrade with rationale, or explicitly carry into the final
  bundle before clean final closeout.

## Conflict Rule

If this file conflicts with package `review.md`, an execution report,
`findings.md`, or actual git state, prefer the current campaign state in this
file only when the conflict is caused by archived pre-reset evidence. For any
other conflict, stop as `NEEDS_USER_INPUT`.
