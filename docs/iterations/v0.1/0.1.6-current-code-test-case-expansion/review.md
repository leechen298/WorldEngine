# Review

Status: review complete

## Changed Files

| File | Change |
|---|---|
| `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/README.md` | Added package overview, status, delivered documentation, and boundary. |
| `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/intent.md` | Defined the current-code test case expansion problem, goal, non-goal, and north-star alignment. |
| `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/contract.md` | Defined allowed changes, forbidden changes, scenario status rules, verdict rules, Agent operation rules, compatibility, and Chinese mirror requirements. |
| `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/technical-design.md` | Documented current testing state, documentation architecture, invariants, affected surfaces, prerequisites, and risks. |
| `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/test-plan.md` | Added docs-only verification commands and commands that must not run in this package. |
| `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/plan.md` | Added execution steps and completion boundary. |
| `docs/iterations/v0.1/0.1.6-current-code-test-case-expansion/review.md` | Recorded documentation-stage evidence. |
| `docs/testing/e2e-scenarios/README.md` | Added E2E scenario index and verdict-source rule. |
| `docs/testing/e2e-scenarios/dashboard-basic-runtime.md` | Documented implemented dashboard runtime E2E scenario. |
| `docs/testing/e2e-scenarios/dashboard-params-flow.md` | Documented implemented valid params E2E scenario. |
| `docs/testing/e2e-scenarios/dashboard-invalid-param.md` | Documented implemented invalid params E2E scenario. |
| `docs/testing/e2e-scenarios/dashboard-agent-autotune.md` | Added contract-only Auto-Tune E2E scenario and selector blockers. |
| `docs/testing/e2e-scenarios/dashboard-timeline-navigation.md` | Added contract-only timeline navigation E2E scenario and selector blockers. |
| `docs/testing/e2e-scenarios/dashboard-archive-summary.md` | Added contract-only archive summary E2E scenario and selector/test-env blockers. |
| `docs/testing/agent-smoke/README.md` | Added Agent smoke scenario index and non-executable scenario warning. |
| `docs/testing/agent-smoke/README.zh.md` | Synced the Agent smoke scenario index in Chinese. |
| `docs/testing/agent-smoke/scenarios/dashboard-basic-runtime.md` | Marked the current basic runtime scenario executable and clarified PASS source. |
| `docs/testing/agent-smoke/scenarios/dashboard-params-flow.md` | Expanded planned params-flow smoke scenario into a defined-but-not-executable contract. |
| `docs/testing/agent-smoke/scenarios/dashboard-invalid-param.md` | Added defined-but-not-executable invalid-param smoke scenario contract. |
| `docs/testing/agent-autonomous/README.md` | Added Codex/test-runner autonomous protocol and Agent naming disambiguation. |
| `docs/testing/agent-autonomous/scorecard.md` | Added contract-only scorecard requirements and PASS rules. |
| `docs/testing/agent-autonomous/scenarios/autonomous-dashboard-basic-runtime.md` | Added contract-only autonomous runtime scenario. |
| `docs/testing/agent-autonomous/scenarios/autonomous-dashboard-params-flow.md` | Added contract-only autonomous params-flow scenario. |
| `docs/testing/agent-autonomous/scenarios/autonomous-dashboard-invalid-param.md` | Added contract-only autonomous invalid-param scenario. |
| `docs/testing/agent-autonomous/scenarios/autonomous-dashboard-agent-autotune.md` | Added contract-only autonomous Auto-Tune scenario. |
| `docs/testing/agent-autonomous/scenarios/autonomous-dashboard-timeline-investigation.md` | Added contract-only autonomous timeline investigation scenario. |
| `docs/testing/test-implementation-prerequisites.md` | Added future selector, validator, checker, and test-env prerequisites. |
| `docs/testing/README.md` | Added links and rules for E2E, Agent smoke, autonomous contracts, and prerequisites. |
| `docs/testing/README.zh.md` | Synced the high-level Chinese testing guide. |
| `docs/testing/v0.1-test-map.md` | Added current-code scenario contract matrix and autonomous/checker gaps. |
| `docs/testing/v0.1-test-map.zh.md` | Synced the Chinese v0.1 test map with current E2E, Agent smoke, and autonomous status. |
| `docs/iterations/v0.1/README.md` | Added 0.1.6 package to the v0.1 index. |
| `docs/iterations/v0.1/README.zh.md` | Synced the Chinese v0.1 package index. |
| `docs/iterations/v0.1/v0.1-plan.md` | Added 0.1.6 package summary and status. |
| `docs/iterations/v0.1/v0.1-plan.zh.md` | Synced the Chinese v0.1 plan through 0.1.6. |

## Commands Run

```bash
git status --short --branch
git diff --check
find docs/testing/e2e-scenarios -maxdepth 1 -type f | sort
find docs/testing/agent-smoke/scenarios -maxdepth 1 -type f | sort
find docs/testing/agent-autonomous -maxdepth 2 -type f | sort
rg -n "direct API|verdict_source|deterministic_checker|operation-log|Playwright assertion|full Agent autonomous|curl smoke|scorecard" docs/testing docs/iterations/v0.1/0.1.6-current-code-test-case-expansion
git diff --name-only | rg -v '^(docs/)'
```

## Test Results

- `git status --short --branch`: passed; branch was
  `## v0.1...origin/v0.1`, and changed paths were documentation files only.
- `git diff --check`: passed with no output.
- `find docs/testing/e2e-scenarios -maxdepth 1 -type f | sort`: passed and
  listed the README plus six E2E scenario files.
- `find docs/testing/agent-smoke/scenarios -maxdepth 1 -type f | sort`:
  passed and listed `dashboard-basic-runtime.md`,
  `dashboard-invalid-param.md`, and `dashboard-params-flow.md`.
- `find docs/testing/agent-autonomous -maxdepth 2 -type f | sort`: passed and
  listed the protocol README, scorecard, and five autonomous scenario files.
- `rg -n "direct API|verdict_source|deterministic_checker|operation-log|Playwright assertion|full Agent autonomous|curl smoke|scorecard" docs/testing docs/iterations/v0.1/0.1.6-current-code-test-case-expansion`:
  passed and found the required operation-boundary, verdict-source, E2E, curl
  smoke, and scorecard terms.
- `git diff --name-only | rg -v '^(docs/)'`: expected no output; no non-doc
  changed path matched the boundary check.

No backend tests, frontend unit tests, E2E tests, live Agent smoke, API curl
smoke, or Codex/test-runner autonomous tests were run. This is intentional for
this documentation-only package.

## Compatibility Review

No runtime behavior, backend code, frontend code, API semantics, schemas,
fixtures, Playwright E2E implementation, Agent smoke validator behavior,
skills, or `backend/worldengine/` files changed.

The package records current E2E coverage and future test contracts only.
Contract-only scenarios are explicitly marked as not executable until future
selector, validator, checker, or test-environment prerequisites are satisfied.

## Scope Review

The work stayed inside `docs/`. It added the 0.1.6 iteration package, current
testing scenario contracts, autonomous protocol contracts, prerequisites, and
English/Chinese high-level index sync.

No new test was implemented, no live Agent smoke was run, and no Codex
autonomous test was run or reported as passed.

## Unresolved Findings

- P1: none.
- P2: none.
- P3: Future 0.1.7 work must add selectors and extend validators/checkers
  before blocked scenarios can execute.

## Final Assessment

Review complete. 0.1.6 defines current-code test case contracts only; test
implementation and execution remain future-package work.
