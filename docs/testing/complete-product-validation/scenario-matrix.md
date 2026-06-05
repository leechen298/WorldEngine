# Complete Product Validation Scenario Matrix

Status: planned scenario matrix

Chinese mirror: `scenario-matrix.zh.md`.

## Purpose

This matrix names the scenarios that a complete WorldEngine validation suite
should either execute, mark as planned, or classify as out of scope. Existing
scenario contracts remain authoritative for implemented E2E, Agent smoke, and
saved-result autonomous checks. This document ties them together at the product
level.

## Scenario Status Values

| Status | Meaning |
| --- | --- |
| `implemented` | Test or checker exists and can be executed. |
| `checker_supported` | Saved-result or fixture checker exists, but live run may be separate. |
| `partially_covered` | Some tests or evidence exist, but a complete scenario-level PASS source is missing. |
| `planned_contract` | Scenario is documented but checker or execution support is not implemented yet. |
| `blocked` | Scenario cannot run because required implementation, environment, or artifact support is missing. |
| `out_of_scope` | Scenario belongs to future roadmap or an explicitly excluded validation scope. |

## Product Scenario Matrix

| Scenario | Capability coverage | Test level | Current source | Required PASS source | Current status |
| --- | --- | --- | --- | --- | --- |
| `governance-scope-boundary-audit` | CPV-01 | docs audit | `AGENTS.md`, `docs/scope-boundaries.md`, iteration docs | reviewed docs audit and scope guard | planned_contract |
| `recursive-schema-contract` | CPV-02 | unit/schema | backend schema tests | pytest and schema validation | implemented |
| `worldspec-loader-runtime-bridge` | CPV-03 | backend integration | backend loader/runtime tests | pytest | implemented |
| `deterministic-world-generation` | CPV-04 | backend/API | v0.6 generation tests | pytest and API evidence | implemented |
| `structured-generation-plan-import` | CPV-04, CPV-19 | backend/API | plan import tests | pytest and redaction checks | implemented |
| `llm-backed-world-creation` | CPV-04, CPV-12, CPV-13 | autonomous/LLM-backed | `docs/testing/llm-backed-lifecycle-validation-plan.md` | checker or scorecard PASS | planned_contract |
| `runtime-core-lifecycle` | CPV-05, CPV-06 | backend/API/E2E | runtime, event, dashboard scenarios | pytest plus Playwright assertions | implemented |
| `event-timeline-snapshot-replay` | CPV-06, CPV-07 | backend/E2E/external client | timeline/archive/replay docs and Validation Client evidence | command/checker evidence | partially_covered |
| `params-flow-and-diff` | CPV-08 | backend/E2E/Agent smoke | params tests, `dashboard-params-flow` | pytest, E2E, smoke checker | implemented |
| `agent-loop-step` | CPV-09 | backend/API/E2E | `agent-loop-step` E2E and backend tests | pytest plus Playwright assertions | implemented |
| `agent-memory-context` | CPV-10 | backend/API | v0.5 memory tests | pytest | implemented |
| `agent-persistent-autonomy-evidence` | CPV-11, CPV-18 | autonomous/LLM-backed | LLM-backed plan | checker or scorecard PASS plus second-Agent review | planned_contract |
| `provider-live-smoke-deepseek` | CPV-12 | provider live smoke | LLM-backed plan | checker or scorecard PASS | blocked |
| `world-rule-parameter-evolution` | CPV-13 | autonomous/LLM-backed | LLM-backed plan | checker or scorecard PASS | planned_contract |
| `rule-compliant-event-generation` | CPV-14 | autonomous/LLM-backed | LLM-backed plan | checker or scorecard PASS | planned_contract |
| `projection-read-model-contract` | CPV-15 | contract/checker | v0.7 projection docs and checker | checker PASS | implemented |
| `dashboard-basic-runtime` | CPV-16 | E2E/Agent smoke | E2E and smoke scenarios | Playwright/checker PASS | implemented |
| `dashboard-generation-preview-readiness` | CPV-04, CPV-16 | E2E | E2E scenario | Playwright PASS | implemented |
| `worldengine-full-lifecycle-autonomous` | CPV-17, CPV-18, CPV-19 | autonomous saved-result | `agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md` | `make validate-agent-autonomous-result` | checker_supported |
| `llm-backed-full-lifecycle-autonomous` | CPV-11 through CPV-19 | autonomous/LLM-backed | LLM-backed plan | checker or scorecard PASS plus second-Agent review | planned_contract |
| `redaction-integrity-scan` | CPV-19 | checker/docs audit | redaction rules, checker fixtures | checker or grep/probe evidence | partially_covered |
| `full-product-regression` | CPV-20 | command profile | product validation playbook | command matrix all pass | planned_contract |

## Minimum Full-Run Scenario Set

A future complete validation run should include at least:

1. `governance-scope-boundary-audit`.
2. `recursive-schema-contract`.
3. `worldspec-loader-runtime-bridge`.
4. `deterministic-world-generation`.
5. `structured-generation-plan-import`.
6. `runtime-core-lifecycle`.
7. `event-timeline-snapshot-replay`.
8. `params-flow-and-diff`.
9. `agent-loop-step`.
10. `agent-memory-context`.
11. `projection-read-model-contract`.
12. `dashboard-basic-runtime`.
13. `dashboard-generation-preview-readiness`.
14. `worldengine-full-lifecycle-autonomous`.
15. `redaction-integrity-scan`.
16. `full-product-regression`.

If LLM-backed lifecycle is in scope, also include:

1. `provider-live-smoke-deepseek`.
2. `llm-backed-world-creation`.
3. `world-rule-parameter-evolution`.
4. `rule-compliant-event-generation`.
5. `agent-persistent-autonomy-evidence`.
6. `llm-backed-full-lifecycle-autonomous`.
