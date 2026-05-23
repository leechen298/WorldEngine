# Test Implementation Prerequisites

Status: current-code test expansion prerequisites

This document lists implementation prerequisites for future 0.1.7 or later
test execution work. 0.1.6 records these requirements only; it does not add
selectors, validators, checkers, fixtures, or tests.

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

### MemoryPanel / Summary

Required stable selectors:

- `memory-panel`
- `memory-summary-text`
- `memory-summary-stats`
- `memory-summary-empty`

These selectors are needed before `dashboard-archive-summary` can assert
latest archive summary display through the dashboard.

### Timeline Details

Required stable selectors:

- `timeline-row`
- `timeline-row-expand`
- `timeline-event-type`
- `timeline-event-payload`
- `timeline-event-source`

These selectors are needed before timeline navigation and autonomous timeline
investigation scenarios can assert expanded event details robustly.

## Validator / Checker Prerequisites

### Agent Smoke Validator

Future Agent smoke execution needs validator support for:

- `dashboard-params-flow`
- `dashboard-invalid-param`

The validator must keep these existing invariants:

- `verdict_source` must be `deterministic_checker`.
- `operation-log.jsonl` may contain UI and CLI operations only.
- direct API calls must not be recorded as Agent operations.
- API evidence may appear only in `api-summary.json` or checker artifacts.

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

Future implementation should set these through test web-server environment or
equivalent test configuration. It must not change runtime logic just to make
the scenario pass.
