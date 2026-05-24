# Test Implementation Prerequisites

Status: current-code test expansion prerequisites

This document tracks implementation prerequisites for current-code test
execution work. 0.1.7 closes the selector and Agent smoke validator
prerequisites listed below, while later packages still own live Agent smoke
runs and autonomous scorecard support.

## Selector Prerequisites

### Agent Auto-Tune

Required stable selectors:

- `world-agent-goal-input`
- `world-agent-autotune-button`
- `world-agent-success`
- `world-agent-patches`
- `world-agent-error`

These selectors are needed before `dashboard-agent-autotune` can become a
stable E2E or Codex/test-runner scenario.

0.1.7 status: implemented as stable dashboard selectors.

0.1.9 status: current-code Playwright E2E implemented; Codex/test-runner
autonomous coverage remains future work.

### MemoryPanel / Summary

Required stable selectors:

- `memory-panel`
- `memory-summary-text`
- `memory-summary-stats`
- `memory-summary-empty`

These selectors are needed before `dashboard-archive-summary` can assert
latest archive summary display through the dashboard.

0.1.7 status: implemented as stable dashboard selectors.

0.1.8 status: current-code Playwright E2E implemented.

### Timeline Details

Required stable selectors:

- `timeline-row`
- `timeline-row-expand`
- `timeline-event-type`
- `timeline-event-payload`
- `timeline-event-source`

These selectors are needed before timeline navigation and autonomous timeline
investigation scenarios can assert expanded event details robustly.

0.1.7 status: implemented as stable dashboard selectors.

0.1.9 status: current-code Playwright timeline-navigation E2E implemented;
autonomous timeline investigation remains future work.

## Validator / Checker Prerequisites

### Agent Smoke Validator

Agent smoke validator support exists for:

- `dashboard-params-flow`
- `dashboard-invalid-param`

The validator must keep these existing invariants:

- `verdict_source` must be `deterministic_checker`.
- `operation-log.jsonl` may contain UI and CLI operations only.
- direct API calls must not be recorded as Agent operations.
- API evidence may appear only in `api-summary.json` or checker artifacts.

0.1.7 status: validator support and deterministic fixture coverage are
implemented.

0.1.8 status: `dashboard-params-flow` live Agent smoke recorded.

0.1.9 status: `dashboard-invalid-param` live Agent smoke recorded. The current
`test-results/agent-smoke/latest/` raw evidence points to invalid-param;
params-flow raw evidence remains available through commit `c6da552` and the
durable summary under `docs/testing/results/`.

### Codex/Test-Runner Autonomous Checker

Before any full Agent autonomous scenario can run, a later package must define:

- scorecard schema.
- result schema.
- operation log schema reuse or extension.
- verdict source rules.
- forbidden operation rules.
- required artifact rules.
- unverified item severity rules.

No Codex/test-runner autonomous scenario may be reported as passed until the
scorecard checker exists and returns PASS.

## Test Environment Prerequisites

`dashboard-archive-summary` needs a deterministic E2E environment for archive
intervals, such as:

- `WORLD_SUMMARY_INTERVAL_TICKS=2`
- `WORLD_SNAPSHOT_INTERVAL_TICKS=2`

0.1.8 status: implemented through Playwright web-server environment. Runtime
logic was not changed to make the scenario pass.
