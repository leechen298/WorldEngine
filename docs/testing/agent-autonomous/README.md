# Agent Autonomous Test Protocol

Status: minimal saved-result checker available

In this directory, "Agent" means a Codex/test-runner agent operating
WorldEngine as a tester. It does not mean a future WorldEngine in-world Agent.

WorldEngine currently does not have a broad executable Agent autonomous runner
or full autonomous scenario suite. This directory defines the protocol for
Codex/test-runner autonomous tests, and the repository now has a minimal
saved-result scorecard checker for recorded evidence.

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

Autonomous PASS requires a checker command such as:

```bash
make validate-agent-autonomous-result RESULT_DIR=<dir>
make validate-agent-autonomous-fixtures
```

The checker validates saved result artifacts. It is not a scenario runner and
does not prove that every autonomous scenario has been live-run.
