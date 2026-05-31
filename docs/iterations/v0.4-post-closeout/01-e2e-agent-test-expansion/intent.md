# Intent

## Problem

v0.4 has backend/API evidence for the minimal Agent-in-World loop, and the
repository has existing dashboard E2E and basic Agent smoke infrastructure.
However, the current browser E2E suite does not directly exercise
`POST /world/agent/loop/step`, and the Agent UI/CLI smoke checker does not yet
cover the dashboard Auto-Tune flow as an executable Agent-operated scenario.

The user wants the practical validation path, not only a plan:

- add E2E tests.
- write Agent-operated UI/CLI test cases.
- run the tests and report whether the current product passes.
- use subagents for review/evaluation.

## Desired Outcome

After this package is implemented and verified:

- Playwright has executable v0.4 Agent Loop API coverage under the E2E harness.
- Agent smoke has an executable dashboard Auto-Tune scenario with deterministic
  checker support.
- The new tests and adjacent suites are run in the current session.
- `review.md` records commands, pass/fail results, artifacts, scope review, and
  unresolved findings.

## Non-Goals

- Do not add a dashboard UI for `POST /world/agent/loop/step`.
- Do not implement v0.5 memory, reflection, relationship state, self-summary,
  or personality drift.
- Do not implement a full broader autonomous scorecard suite.
- Do not change runtime, schema, API behavior, frontend product UI behavior, or
  world logic to make tests pass.
