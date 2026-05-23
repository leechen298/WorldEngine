# Intent

## Problem

v0.1 already has executable runtime, dashboard, params, archive, and
params-agent surfaces, but the current evidence map is uneven:

- browser E2E currently covers dashboard runtime and params flows only.
- Agent smoke has a protocol and deterministic validator, but only the
  `dashboard-basic-runtime` scenario is executable today.
- broader Codex/test-runner autonomous testing has no scenario protocol,
  scorecard, or checker contract yet.

Without explicit current-code scenario contracts, future agents may invent test
flows, blur Agent smoke into full autonomous coverage, or report PASS from
natural-language observation instead of deterministic verdict sources.

## Goal

Define a documentation-only test case expansion package that records:

- implemented E2E scenarios.
- E2E scenario contracts that are not yet implemented.
- executable and non-executable Agent smoke scenarios.
- Codex/test-runner autonomous scenario contracts.
- operation boundaries, evidence requirements, selector prerequisites, checker
  prerequisites, and PASS/FAIL sources.

## Non-Goal

This package does not add tests or execute tests. It intentionally leaves
selector, validator, checker, and live-run implementation work to a later
reviewed package.

## North Star Alignment

The package supports WorldEngine as a runtime engine with inspectable evidence.
It does not add game-specific logic, WorldSpec behavior, recursive world
runtime behavior, or in-world Agent cognition behavior.
