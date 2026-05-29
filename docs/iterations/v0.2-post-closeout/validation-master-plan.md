# Validation Master Plan

Status: planned / ready for review
Type: post-closeout validation control plan

## Purpose

This document controls v0.2 post-closeout validation. It exists because v0.2
closeout is complete and remaining validation must be evidence-bearing rather
than assumed from release status.

This validation chain does not reopen v0.2. It creates and routes evidence
channels for validation runs.

## Current Routing Snapshot

The current short routing source is `CURRENT_STATE.md`; Codex App `/goal`
routing instructions live in `GOAL_RUNNER.md`.

As of 2026-05-29:

- `01-e2e-validation-plan` is complete.
- `02-e2e-validation-execution` is `passed` with backend deterministic, API
  smoke, Playwright availability, and configured browser E2E evidence.
- `03-codex-autonomous-validation-plan` is the active next package and needs
  review-closeout only.
- `04-codex-autonomous-validation-execution` is not executed.
- `05-final-validation-bundle` is not executed.
- `v0.2-post-closeout-P2-001` remains open in `findings.md`.

## Required Reading

Validation planning and later execution must read:

- `docs/iterations/AGENTS.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/evidence-index.md`
- `docs/iterations/v0.2/boundary-audit.md`
- `docs/iterations/v0.2/compatibility-review.md`
- `docs/iterations/v0.2/v0.2-release-candidate-bundle.md`
- `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/review.md`
- `docs/scope-boundaries.md`
- `docs/external-fixture-boundary.md`
- `docs/validation-report-template.md`
- `README.md`

If a required file is missing during execution, record it in the relevant
review instead of assuming its content.

## Process

0. Master validation planning: define status taxonomy, stop conditions,
   severity rules, and handoff order.
1. E2E / integration / API smoke plan: define what should be checked without
   executing checks.
2. E2E / integration / API smoke execution: record branch, commit, commands,
   results, blockers, and P1/P2/P3 findings.
3. Codex autonomous validation plan: define independent reviewer instructions.
4. Codex autonomous validation execution and review: collect the independent
   review and verify whether it is evidence-bearing.
5. Final validation bundle: summarize both validation lines and decide whether
   unresolved findings block later v0.4 work.

## Codex App Goal Routing Rule

Default `/goal` work is one validation package at a time. Do not continue from
one package to the next unless the user explicitly asks for full campaign mode.

The default next route is:

```text
03-codex-autonomous-validation-plan review-closeout-plan
```

`03` must not execute autonomous validation. `04` owns autonomous validation
execution, and `05` owns final bundle synthesis.

## Result States

- `planned`: docs exist, execution has not started.
- `ready for execution`: execution instructions are reviewable and complete.
- `executed`: execution ran and report fields were filled.
- `passed`: validation evidence supports the checked claims and no unresolved
  P1/P2/P3 remains.
- `passed with P3`: validation evidence supports the checked claims, with only
  accepted non-blocking P3 findings.
- `blocked`: validation could not complete and the blocker is recorded.
- `failed`: validation completed and found a P1/P2 failure or claim conflict.
- `not executed`: no validation execution happened.

## Severity Rules

- P1: invalidates a v0.2 release claim, exposes concrete demo-world regression,
  breaks compatibility, or proves a required validation report is unsupported.
- P2: missing required evidence, incomplete execution, unclear blocker, or
  unsupported claim that prevents reliable validation.
- P3: non-blocking documentation gap, polish issue, or future handoff that does
  not change the final assessment.

P1 and unresolved P2 block a clean validation result. P3 may be accepted only
when explicitly listed and assigned to a follow-up owner or version.

## Stop Conditions

Stop validation and record `blocked` or `failed` when:

- backend deterministic tests fail.
- API smoke fails.
- release claim conflicts with actual behavior.
- Codex autonomous reviewer reports P1.
- concrete demo-world regression appears.
- commands cannot run and no blocker is recorded.
- the execution package cannot identify the branch and commit.
- a report claims success without current-session command evidence.

## Branch and Commit Rule

Do not hardcode a branch name. The execution package must record the actual
branch and commit from:

```bash
git status --short --branch
git rev-parse HEAD
```

## E2E Availability Rule

Presence of Playwright configuration is only an E2E availability hint. It does
not prove the E2E suite is runnable.

Execution must discover the actual install, start, and test commands and
record blockers if dependencies, browser binaries, ports, services, or
environment variables prevent the suite from running.

If no runnable E2E framework is available, record E2E as not configured or
blocked, then use API smoke plus backend integration tests as the fallback
validation line.

## v0.4 Proceed Rule

v0.4 may proceed only if the final validation bundle records one of these
states:

- `passed`
- `passed with P3`

If the final validation bundle records `blocked`, `failed`, or `not executed`,
the bundle must explain whether v0.4 is blocked, conditionally allowed, or
requires separate approval.
