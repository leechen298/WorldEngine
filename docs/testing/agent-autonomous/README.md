# Agent Autonomous Test Protocol

Status: scenario contracts only

In this directory, "Agent" means a Codex/test-runner agent operating
WorldEngine as a tester. It does not mean a future WorldEngine in-world Agent.

WorldEngine currently does not have an executable full Agent autonomous test
suite. This directory defines the minimum protocol for future
Codex/test-runner autonomous tests. These contracts must not be executed until
a scorecard checker and scenario runner exist.

## Distinction From Agent Smoke

Agent smoke is basic UI/CLI operation smoke testing with deterministic checker
verdicts.

Codex/test-runner autonomous testing gives the tester agent a goal and allows
it to choose steps within documented boundaries, but PASS still comes from a
scorecard checker or deterministic verdict source. Codex natural language does
not decide PASS.

## Required Scenario Fields

Each autonomous scenario must define:

- status.
- goal.
- allowed operations.
- forbidden operations.
- required artifacts.
- scorecard items.
- PASS/FAIL source.
- unverified items.

## Execution Rule

Every current scenario in this directory has:

```text
Status: contract-only-do-not-execute
```

If a user asks to run broader autonomous tests before a checker exists, the
runner must stop and report that only contracts exist.
