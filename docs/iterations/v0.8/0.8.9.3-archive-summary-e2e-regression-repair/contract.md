# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `Archive summary`: the public world-history summary generated from archived
  runtime events and rendered by the dashboard MemoryPanel.
- `Newer summary`: a summary whose identity or tick coverage is newer than the
  summary observed before the E2E stepping phase.
- `MemoryPanel evidence`: stable dashboard text and stats proving the latest
  archive summary is visible to a user.
- `Focused E2E repair`: a minimal repair that restores the failing archive
  summary scenario without weakening the user-visible assertion.

## Allowed Changes After Approval

Implementation may modify only the smallest required subset of these files or
surfaces:

```text
frontend/e2e/agent-loop.spec.ts
frontend/e2e/dashboard.spec.ts
frontend/playwright.config.ts
frontend/src/**
backend/app/**
backend/app/tests/**
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

The `frontend/src/**`, `backend/app/**`, and `backend/app/tests/**` allowances
are conditional. They may be used only if focused diagnosis proves the root
cause is frontend behavior, backend archive behavior, or missing focused
regression coverage.

## Forbidden Changes

- Do not modify `backend/worldengine/`.
- Do not modify the Validation Client repository.
- Do not skip or delete the failing Playwright test.
- Do not reduce the scenario to only checking that the dashboard loads.
- Do not remove the requirement that a newer summary is created after runtime
  steps.
- Do not extend the timeout as the only fix unless diagnostic evidence proves
  the application behavior is correct and the wait condition was under-sized.
- Do not rewrite, delete, or edit saved validation result directories to make
  historical evidence pass.
- Do not add live provider calls, DeepSeek smoke, provider abstractions, or
  LLM-backed world creation/evolution behavior.
- Do not add concrete validation-world content or app-specific backend logic.
- Do not claim external validation PASS, product readiness, or LLM-backed
  lifecycle readiness.

## Required Diagnostic Classification

Before implementation changes are chosen, `review.md` must classify the root
cause into one of these buckets:

```text
archive_generation_gap
summary_api_visibility_gap
memory_panel_refresh_gap
e2e_environment_gap
e2e_wait_or_state_isolation_gap
other_blocked
```

The classification must cite focused evidence, such as API responses, UI
state, Playwright trace observations, or backend logs available in the current
session.

## Compatibility Requirements

- Existing archive summary response shape must remain additive-compatible.
- Existing dashboard MemoryPanel selectors must remain stable unless the
  package records a selector-specific reason and updates E2E docs.
- Existing runtime step, event, snapshot, params, generation, Agent loop, and
  public handoff endpoints must keep their behavior unless the root cause is
  proven to be in a directly adjacent archive summary path.
- E2E web server configuration must not change backend runtime defaults outside
  the test environment.
- The repair must not introduce concrete world fixtures or external validation
  scenario data into WorldEngine core.

## Exit Criteria

- Documentation/contract review records no P0/P1 and no blocking P2.
- `implementation_authorized: yes` is recorded before code changes.
- Focused diagnosis records one root-cause bucket.
- The focused archive summary E2E scenario passes in the current session.
- `make test-e2e` passes in the current session.
- Any required adjacent backend/frontend tests pass in the current session.
- Latest basic full lifecycle saved-result checker passes in the current
  session, or a blocker is recorded with exact reason.
- `git diff --check` passes.
- `review.md` and `review.zh.md` record changed files, commands, results,
  compatibility review, scope review, unresolved findings, and final
  assessment.

## Out-of-Scope Follow-ups

- LLM-backed lifecycle validation execution.
- Provider live smoke endpoint or checker support.
- Agent persistent autonomy quality improvements.
- Archive summary quality, retention, compression, or durable persistence work
  beyond the failing E2E contract.
- Validation Client evidence exporter or UI work.
