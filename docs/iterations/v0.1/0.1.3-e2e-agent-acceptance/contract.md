# Contract

## Public Semantics

This package is a post-closeout verification hardening package. It may add
tests, test selectors, test tooling, and evidence protocols, but it must not
expand v0.1 runtime, product, WorldSpec, agent, or village capabilities.

## Allowed Changes

- Add Playwright E2E setup under `frontend/`.
- Add deterministic dashboard E2E tests.
- Add stable `data-test` selectors to existing dashboard controls and status
  values.
- Add Make targets for E2E and agent smoke result validation.
- Add `tools/testing/` scripts, fixtures, and tests for agent smoke validation.
- Add `docs/testing/agent-smoke/` protocol documentation and result schema.
- Ignore local `test-results/` artifacts.
- Add durable verification summaries under `docs/testing/results/`.

## Forbidden Changes

- Do not change backend runtime behavior.
- Do not change API response semantics.
- Do not add WorldSpec, WorldCell, recursive runtime, generation, village, or
  game-surface behavior.
- Do not modify `backend/worldengine/`.
- Do not add `LLM Auto-Tune` E2E coverage in this first package.
- Do not claim Agent smoke passed unless `result.json` exists and the validation
  script exits `0`.

## Anti-Self-Reporting Rules

1. No structured `result.json`, no PASS.
2. Non-zero command exit code, no PASS.
3. Agent observation is not final evidence.
4. PASS/FAIL must come from Playwright assertions or
   `tools/testing/validate_agent_smoke_result.py`.
5. Agent smoke requires `result.json`, `transcript.md`, `console.log`,
   `api-summary.json`, and at least one screenshot artifact.
6. Agent smoke `trace.zip` is optional in the first package.
7. `verdict_source` must be `deterministic_checker`; `agent` is invalid.
8. Codex summaries may cite evidence paths, but must not replace evidence.

## Compatibility

The dashboard selectors are non-user-visible attributes. They must not change
layout, styling, API calls, runtime state, or business behavior.
