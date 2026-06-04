# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Current State

`tools/testing/validate_agent_autonomous_result.py` accepts a fixed set of
dashboard saved-result scenarios. It validates required artifacts, operation
log shape, UI target coverage, score items, unresolved P1 findings, and
scorecard summary status.

It does not validate lifecycle-specific evidence such as world creation,
runtime tick progression, Agent autonomy, external direction boundaries, or
redaction scans.

## Contract Alignment and Invariants

- Agent operation logs stay UI/CLI only.
- WorldEngine API evidence is stored as redacted artifacts.
- Existing scenarios keep their current required UI target behavior.
- The new scenario is generic and does not include concrete world content.

## Proposed Implementation

Add `worldengine-full-lifecycle-autonomous` to:

- the autonomous scenario index.
- `result-schema.json`.
- the checker supported scenario set.
- required UI target coverage.

Add lifecycle-specific artifact validation for the new scenario:

- `artifacts.api_summary` must exist.
- `artifacts.world_lifecycle_summary` must exist.
- `world-lifecycle-summary.json` must contain passing sections for:
  - `world_creation`.
  - `runtime_progression`.
  - `agent_autonomy`.
  - `external_direction`.
  - `evidence_integrity`.

The checker should reject:

- missing lifecycle summary.
- non-advancing ticks.
- no events observed.
- no Agent actions observed.
- client-scripted Agent actions.
- direct Agent private-state mutation.
- failed redaction scan.

## Affected Surfaces

- autonomous validation docs.
- autonomous result schema.
- autonomous checker.
- checker tests and fixtures.
- Makefile fixture target.

## Data Model / Schema Changes

The result schema adds one scenario enum value. `additionalProperties` remains
true, so this is additive.

`world-lifecycle-summary.json` is a checker artifact, not a public API schema.

## Runtime / Service Design

No runtime or service behavior changes.

## Compatibility

Existing saved-result fixtures and scenarios must continue passing. Invalid
fixtures must continue failing.

## Risks

- The checker can only validate recorded evidence, not perform a live run.
  The scenario and review must state that distinction.
- Agent autonomy evidence is bounded: the checker can reject client scripting
  and missing WorldEngine evidence, but it cannot prove philosophical
  consciousness.
- The lifecycle summary must avoid private provider traces and private Agent
  state.
