# Validation Master Plan

Status: executed / passed with P3
Type: post-closeout validation control plan

## Purpose

This document controls v0.3 post-closeout validation. v0.3 closeout is already
complete, and the approved 2026-05-29 campaign run has now added fresh
independent validation evidence.

Execution note: the approved 2026-05-29 campaign run added fresh independent
validation evidence and closed the campaign as `passed with P3`.

The campaign focuses on:

- WorldSpec loader validation.
- runtime context bridge validation.
- RuntimeEngine compatibility.
- Event.refs response compatibility.
- API smoke and integration behavior.
- E2E availability and execution, when configured.
- Codex autonomous validation.
- release-claim and compatibility-claim review.
- concrete demo-world regression boundaries.

## Required Reading

- `README.md`
- `README.zh.md`
- `docs/releases/v0.3.md`
- `docs/releases/v0.3.zh.md`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`
- `docs/iterations/v0.3/evidence-index.md`
- `docs/iterations/v0.3/compatibility-audit.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.md`
- `docs/scope-boundaries.md`
- `docs/external-fixture-boundary.md`
- `docs/validation-report-template.md`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/event.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`
- `backend/app/tests/test_event_api_compat.py`
- `backend/app/tests/test_event_schema_compat.py`

If a required file is missing, record it in the relevant `review.md` and do
not infer its content from memory or adjacent packages.

## Result States

- `planned`: validation docs exist, execution has not started.
- `ready for execution`: execution instructions are reviewable and complete.
- `executed`: execution ran and report fields were filled.
- `passed`: evidence supports the checked claims and no unresolved P1/P2/P3
  remains.
- `passed with P3`: evidence supports the checked claims with accepted
  non-blocking P3 findings.
- `blocked`: validation could not complete and the blocker is recorded.
- `failed`: validation ran and found a P1/P2 failure or claim conflict.
- `not executed`: no validation execution happened.
- `not executed in current campaign`: historical evidence may exist, but this
  campaign has not executed or re-accepted it.
- `archived evidence only`: historical evidence retained for audit, not
  current completion evidence.

## Stop Conditions

Stop validation and record `blocked` or `failed` when:

- backend deterministic tests fail.
- API smoke fails.
- loader validation fails.
- runtime context bridge validation fails.
- runtime compatibility claim conflicts with actual behavior.
- release claim conflicts with actual behavior.
- Codex autonomous reviewer reports P1.
- concrete demo-world regression appears.
- commands cannot run and no blocker is recorded.

## Severity Rules

- P1: invalidates a v0.3 release or compatibility claim, breaks loader/bridge
  behavior, breaks RuntimeEngine or Event.refs compatibility, or introduces a
  concrete demo-world regression.
- P2: missing required evidence, incomplete execution, unclear blocker, or
  unsupported claim that prevents reliable validation.
- P3: non-blocking documentation gap, polish issue, indirect evidence concern,
  or future handoff that does not alter the final assessment.

P1 blocks closeout. Unresolved P2 blocks a clean final result unless explicitly
accepted by the active package. P3 can be carried only with explicit handoff.

## E2E Availability Rule

If no runnable E2E setup is available, record E2E as `not configured` or
`blocked` and use API smoke plus backend integration tests as the fallback
validation line.

Presence of a Playwright or frontend config is an availability clue, not proof
that the suite is runnable.

## Branch And Commit Rule

Execution packages must record the real branch and commit from the worktree at
execution time. Do not hardcode a branch in templates.

Expected future commands:

```bash
git status --short --branch
git rev-parse HEAD
```

## Release Status Rule

This campaign does not change v0.3 release status. A failed, blocked, or not
executed campaign may identify follow-up validation work, but it must not
rewrite v0.3 final closeout documents as if v0.3 had been reopened.
