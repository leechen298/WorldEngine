# 01 E2E Validation Plan

Status: planned / ready for review
Type: validation-planning package

## Goal

Define the future E2E, integration, API smoke, WorldSpec loader, runtime
context bridge, Event.refs, release-claim, and concrete demo-world regression
validation scope for v0.3 post-closeout.

This package does not execute validation.

## Scope

The plan covers:

- repository / documentation checks.
- backend deterministic checks.
- focused WorldSpec loader tests.
- focused runtime context bridge tests.
- event API compatibility tests.
- API smoke checks.
- E2E framework availability check.
- browser E2E execution if configured.
- fallback if E2E framework is unavailable.
- v0.3 release claim validation.
- concrete demo-world regression check.

If no runnable E2E setup is available, record E2E as not configured or blocked
and use API smoke + backend integration tests as fallback.

## Deliverables

- `README.md`
- `intent.md`
- `contract.md`
- `test-plan.md`
- `plan.md`
- `review.md`

Each file has a `.zh.md` mirror.

## Boundary

Allowed: planning documents only.

Forbidden: running backend/frontend/E2E/API smoke/runtime/schema/fixture/
migration/build/Agent smoke/Codex autonomous checks, editing code or tests,
adding fixtures, creating external repositories, and changing v0.3 release
status.

## Final Assessment State

Final assessment: planned / ready for review.
