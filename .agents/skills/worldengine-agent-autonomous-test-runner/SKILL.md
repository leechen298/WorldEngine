---
name: worldengine-agent-autonomous-test-runner
description: Use when running, validating, or reporting WorldEngine Agent autonomous tests beyond basic smoke, including scenario suites, scorecards, live autonomous runs, or multi-step evidence packages.
---

# WorldEngine Agent Autonomous Test Runner

Use this skill only inside the WorldEngine repository.

This workflow is for Agent autonomous tests broader than basic Agent smoke.
Basic smoke remains covered by `worldengine-agent-smoke-runner`.

## Gate

Before running anything, locate an authoritative scenario, protocol, scorecard,
or iteration `test-plan.md` for the requested autonomous test.

Likely places to search:

- `docs/testing/`
- `docs/testing/results/`
- `docs/iterations/`
- `test-results/`

If no broader autonomous test contract exists, stop and report that only Agent
smoke is currently defined. Do not treat `docs/testing/agent-smoke/` evidence
as full Agent autonomous coverage.

## Required Distinctions

State which mode the requested work belongs to:

- fixture or checker validation.
- live autonomous execution.
- UI smoke or basic Agent smoke.
- scorecard-based autonomous evaluation.

Run only documented entry points from the located contract. Do not invent
scenario steps, scorecards, or PASS criteria.

## Evidence

When a broader autonomous test is defined and run, record:

- invocation surface and exact command or UI entry point.
- run id or result directory.
- verdict source.
- scorecard or checker status when available.
- raw evidence paths such as logs, transcripts, screenshots, or artifacts.
- unverified or skipped items.

## Reporting

- Report PASS only from the documented checker, scorecard, or accepted verdict
  source.
- If only Agent smoke ran, call it basic Agent smoke only.
- If the autonomous contract is missing, report the missing contract instead of
  running smoke as a substitute.
