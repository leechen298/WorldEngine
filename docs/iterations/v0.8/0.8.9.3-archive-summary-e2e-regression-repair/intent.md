# Intent

Chinese mirror: `intent.zh.md`.

## Problem

The latest validation of the current WorldEngine product surface produced a
mixed result:

- basic full lifecycle saved-result checker: PASS.
- Validation Client UI smoke: PASS only for smoke evidence, not authoritative
  full validation.
- WorldEngine E2E: FAIL, with one failing dashboard archive summary scenario.

The failing E2E scenario is important because archive summaries are part of the
observable memory/history surface. If the dashboard cannot reliably prove that
a newer archive summary is created and rendered after runtime steps, then the
current validation baseline is not clean enough to start reporting stronger
LLM-backed lifecycle evidence.

## Why This Package Exists

This is a small repair iteration, not a new product capability milestone. Its
purpose is to restore a clean basic E2E baseline by fixing the precise
regression discovered during validation.

The repair belongs in a concrete package because it can modify frontend,
backend, or E2E implementation files after approval. The documentation gate
must define allowed files, forbidden shortcuts, diagnostics, verification, and
claim boundaries before code changes start.

## User Intent Captured

The user wants failure states to remain visible and wants validation issues
handled through small, reviewable iterations when they require repair. The user
does not want to act as a manual dispatcher for every sub-step, but also does
not want broad unrelated implementation hidden inside a validation pass.

This package therefore gives one approval target for the full repair flow:
reproduce, diagnose, fix the smallest proven cause, verify, review, and close.

## Non-Goals

- Do not implement LLM-backed world creation or evolution.
- Do not test DeepSeek live provider calls.
- Do not change Validation Client behavior.
- Do not improve archive summary quality beyond the failing E2E contract.
- Do not make archive persistence durable.
- Do not claim product readiness or LLM-backed lifecycle readiness.
- Do not convert this regression into a broad dashboard refactor.

## Expected Outcome

At closeout, one of these outcomes must be recorded:

- `PASS`: focused E2E passes, `make test-e2e` passes, required adjacent
  regressions pass, and the saved-result checker for the latest basic full
  lifecycle autonomous result still passes.
- `BLOCKED`: the root cause requires a broader design or external dependency
  outside this package.
- `FAIL`: the repair was attempted but verification did not pass.
