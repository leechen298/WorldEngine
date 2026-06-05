# 0.8.9.3 Archive Summary E2E Regression Repair

Chinese mirror: `README.zh.md`.

Status: implementation complete / PASS
implementation_authorized: yes
evidence_execution_authorized: yes, limited to `test-plan.md` commands
Type: mixed repair package

## Goal

Diagnose and repair the current `dashboard-archive-summary` E2E regression so
WorldEngine has a clean basic dashboard E2E baseline again before any
LLM-backed lifecycle validation is treated as executable evidence.

This package exists because the latest current-product validation found that
basic full lifecycle saved-result validation passed, but the WorldEngine E2E
suite did not have a clean pass:

```text
make test-e2e
16 passed / 1 failed
frontend/e2e/dashboard.spec.ts:292
dashboard-archive-summary creates and renders a newer archive summary
```

The failure was a timeout waiting for a newer archive summary after runtime
steps. This package must determine whether the issue is archive summary
generation, summary API ordering/visibility, frontend MemoryPanel refresh, E2E
environment setup, or the Playwright wait condition.

## Scope

Allowed after approval:

- reproduce the focused failing E2E scenario.
- inspect archive summary API state before and after runtime steps.
- repair the smallest proven root cause in backend archive behavior, frontend
  MemoryPanel behavior, or E2E harness logic.
- preserve the assertion that a newer archive summary is created and rendered.
- rerun focused and broad E2E verification.
- rerun the latest basic full lifecycle saved-result checker to confirm the
  previous autonomous PASS evidence still validates.

Forbidden:

- do not skip, delete, or weaken the failing E2E into a smoke-only check.
- do not rewrite generated validation result directories.
- do not modify the Validation Client repository.
- do not add DeepSeek, provider live smoke, or LLM-backed world generation
  behavior.
- do not add concrete validation-world names, characters, locations, story
  rules, seed data, private oracle logic, or app-specific backend behavior.
- do not implement new runtime features under `backend/worldengine/`.

## Deliverables

- focused diagnosis evidence that identifies the failing layer.
- a narrow implementation repair after review approval.
- current-session verification evidence for focused E2E and `make test-e2e`.
- current-session verification evidence for any backend or frontend regression
  commands required by the touched files.
- current-session saved-result checker evidence for the latest basic full
  lifecycle autonomous result.
- completed `review.md` and `review.zh.md` with changed files, commands,
  findings, scope review, compatibility review, and final assessment.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

Chinese mirrors are included.

## Current Gate

Documentation/contract review passed on 2026-06-05 after explicit user
approval. Implementation and verification are complete for this package scope.
No further evidence execution is authorized by this package beyond the
completed `test-plan.md` commands recorded in `review.md`.

```text
implementation_authorized: yes
```

## Handoff

This package closes with clean current-session evidence. WorldEngine may treat
the basic dashboard E2E baseline as repaired for this package scope.
LLM-backed lifecycle validation remains a separate testing plan and must not
be claimed by this package.
