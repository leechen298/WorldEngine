# Contract

## Public Concepts

- Product capability test matrix: a durable matrix that maps current v0.4
  capabilities to backend/API, E2E, Agent smoke, autonomous, evidence, and
  known gaps.
- Agent Loop E2E boundary coverage: Playwright request assertions for current
  public API behavior that already exists.
- Agent autonomous checker: a deterministic scorecard validator for
  Codex/test-runner Agent result artifacts. It validates test evidence only and
  is not a WorldEngine runtime feature.

## Allowed Changes

This package may modify or create only:

- `docs/iterations/v0.4-post-closeout/02-overall-product-capability-validation/**`
- parent `docs/iterations/v0.4-post-closeout/{README.md,CURRENT_STATE.md,CAMPAIGN_PLAN.md,GOAL_RUNNER.md,review.md}`
- `frontend/e2e/agent-loop.spec.ts`
- `docs/testing/**` documentation and autonomous schema files
- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/**`
- `Makefile` entries for autonomous validation
- `docs/testing/results/*.md`
- ignored raw result directories under `test-results/agent-autonomous/**` and
  `test-results/agent-smoke/<timestamp>/**` when produced by live runs

## Forbidden Changes

- No `backend/app/**` product implementation changes.
- No `frontend/src/**` product implementation or test build repair changes.
- No `backend/worldengine/**` changes.
- No public API, runtime schema, migration, external repo, concrete world,
  seed data, or private oracle changes.
- No reclassification of smoke PASS as autonomous PASS.

## Compatibility Requirements

- Existing Agent smoke validator and fixtures must keep passing.
- Existing E2E dashboard and Agent Loop coverage must keep passing.
- The autonomous checker must reject direct API operations in operation logs,
  `verdict_source: "agent"`, missing required artifacts, failed score items,
  and unresolved P1 items.
- PASS must come from `scorecard_checker` or `deterministic_checker`, never
  natural-language Agent self-judgment.

## Out-of-Scope Follow-Ups

- frontend build TypeScript repair.
- broader autonomous runner orchestration.
- v0.5+ product behavior.
