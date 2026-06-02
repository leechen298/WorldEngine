# Agent Autonomous Test Protocol

Status: minimal saved-result checker available; full user-style contracts planned

In this directory, "Agent" means a Codex/test-runner agent operating
WorldEngine as a tester. It does not mean a future WorldEngine in-world Agent.

WorldEngine currently does not have a broad executable Agent autonomous runner
or full autonomous scenario suite. This directory defines the protocol for
Codex/test-runner autonomous tests, and the repository now has a minimal
saved-result scorecard checker for recorded evidence.

For v0.7 planning, full Agent autonomous testing means Codex/test-runner acts
as an ordinary user: it receives a goal, chooses its own bounded steps, operates
the dashboard, calls public APIs when those APIs are part of the product
contract, records artifacts, and then relies on a checker or scorecard for the
verdict. This is broader than the current saved-result checker, which only
accepts existing UI/CLI operation logs and rejects direct API operations as
Agent operations.

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
- ordinary user perspective or API-user perspective.
- allowed operations.
- forbidden operations.
- preconditions.
- autonomous steps or required coverage.
- expected assertions.
- required artifacts.
- scorecard items.
- PASS/FAIL source.
- unverified items.

Full user-style autonomous scenario contracts must also define public API
cross-checks where applicable and must state whether their PASS source is
currently implemented or future checker/runner work.

## Operation Boundary

Current saved-result scenarios:

- may record UI and CLI operations in `operation-log.jsonl`.
- may use API evidence only as checker/helper summary evidence.
- must not record direct API calls as Agent operations.
- are validated by `make validate-agent-autonomous-result RESULT_DIR=<dir>`.

Full user-style scenario contracts:

- may use public APIs such as `/runtime/state`, `/world/events`,
  `/world/params`, `/world/agent/loop/step`, and `/world/generation/*`.
- should record public API use in `api-log.jsonl` and `api-summary.json`, not
  as hidden/private evidence.
- must not use hidden reset APIs, private fixtures, database internals, private
  oracles, unredacted transcripts, external validation world internals, or
  private projection app state.
- require result-schema/checker extension before they can produce an automated
  PASS verdict.

## Execution Rule

Autonomous PASS requires a checker command such as:

```bash
make validate-agent-autonomous-result RESULT_DIR=<dir>
make validate-agent-autonomous-fixtures
```

The checker validates saved result artifacts. It is not a scenario runner and
does not prove that every autonomous scenario has been live-run.

## Scenario Index

| Scenario | Status | Current State |
| --- | --- | --- |
| `autonomous-dashboard-basic-runtime` | `saved-result-checker-supported` | Current minimal saved-result checker scenario. |
| `autonomous-dashboard-params-flow` | `saved-result-checker-supported` | Current minimal saved-result checker scenario. |
| `autonomous-dashboard-invalid-param` | `saved-result-checker-supported` | Current minimal saved-result checker scenario. |
| `autonomous-dashboard-agent-autotune` | `saved-result-checker-supported` | Current minimal saved-result checker scenario. |
| `autonomous-dashboard-timeline-investigation` | `saved-result-checker-supported` | Current minimal saved-result checker scenario. |
| `AUTO-FULL-V07-001 runtime-evidence` | `contract-only / checker-extension-required` | Full ordinary-user scenario using dashboard runtime plus public API evidence. |
| `AUTO-FULL-V07-002 params-flow` | `contract-only / checker-extension-required` | Full ordinary-user scenario using dashboard params plus public API evidence. |
| `AUTO-FULL-V07-003 agent-loop-api` | `contract-only / checker-extension-required` | Full public API user scenario for Agent Loop accepted/rejected/schema paths. |
| `AUTO-FULL-V07-004 generation-readiness` | `contract-only / checker-extension-required` | Full ordinary-user scenario for GenerationPanel and public generation API evidence. |
| `AUTO-FULL-V07-005 v0.7-readiness-contracts` | `contract-only / checker-extension-required` | Full integrator scenario for readiness/report/projection checker surfaces. |
| `AUTO-FULL-V07-006 product-exploration-regression` | `contract-only / full-runner-required` | Future full-suite scenario that classifies every selected capability layer. |
