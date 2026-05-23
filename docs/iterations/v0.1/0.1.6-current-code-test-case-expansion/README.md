# 0.1.6 Current-Code Test Case Expansion

Status: ready for review

Type: documentation-only

## Goal

Define current-code test case contracts for the v0.1 dashboard, E2E,
Agent smoke, and Codex/test-runner autonomous testing surfaces before adding
new tests or running broader scenarios.

This package turns already implemented v0.1 behavior into reviewable scenario
contracts. It does not implement new tests, run live Agent smoke, run Codex
autonomous tests, or change runtime behavior.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Delivered Documentation

- E2E scenario contracts under `docs/testing/e2e-scenarios/`.
- Agent smoke scenario contracts under `docs/testing/agent-smoke/scenarios/`.
- Codex/test-runner autonomous protocol and scorecard contracts under
  `docs/testing/agent-autonomous/`.
- Test implementation prerequisites under
  `docs/testing/test-implementation-prerequisites.md`.
- Updated English and Chinese high-level testing and v0.1 iteration indexes.

## Boundary

0.1.6 only draws the current-code test map. Future package 0.1.7 or later may
extend validators, add selectors, implement missing E2E scenarios, or run live
Agent smoke after those changes are reviewed.
