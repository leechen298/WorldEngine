# 完整产品验证场景矩阵

状态：计划中的场景矩阵

英文镜像：`scenario-matrix.md`。

## 目的

本矩阵命名完整 WorldEngine 验证套件应执行、标记为 planned，或分类为 out of scope 的
场景。已有 E2E、Agent smoke、saved-result autonomous scenario contracts 仍是各自实现层的
权威文档。本文件在产品级把它们串起来。

## Scenario Status Values

| Status | 含义 |
| --- | --- |
| `implemented` | 测试或 checker 已存在，可以执行。 |
| `checker_supported` | saved-result 或 fixture checker 已存在，但 live run 可能是独立步骤。 |
| `partially_covered` | 已有部分测试或 evidence，但缺完整 scenario-level PASS 来源。 |
| `planned_contract` | 场景已文档化，但 checker 或执行支持尚未实现。 |
| `blocked` | 因缺实现、环境或 artifact support，场景不能运行。 |
| `out_of_scope` | 场景属于未来路线图或当前验证明确排除的范围。 |

## 产品场景矩阵

| Scenario | 能力覆盖 | 测试层级 | 当前来源 | 必要 PASS 来源 | 当前状态 |
| --- | --- | --- | --- | --- | --- |
| `governance-scope-boundary-audit` | CPV-01 | docs audit | `AGENTS.md`、`docs/scope-boundaries.md`、iteration docs | reviewed docs audit 和 scope guard | planned_contract |
| `recursive-schema-contract` | CPV-02 | unit/schema | backend schema tests | pytest 和 schema validation | implemented |
| `worldspec-loader-runtime-bridge` | CPV-03 | backend integration | backend loader/runtime tests | pytest | implemented |
| `deterministic-world-generation` | CPV-04 | backend/API | v0.6 generation tests | pytest 和 API evidence | implemented |
| `structured-generation-plan-import` | CPV-04、CPV-19 | backend/API | plan import tests | pytest 和 redaction checks | implemented |
| `llm-backed-world-creation` | CPV-04、CPV-12、CPV-13 | autonomous/LLM-backed | `docs/testing/llm-backed-lifecycle-validation-plan.md` | checker 或 scorecard PASS | planned_contract |
| `runtime-core-lifecycle` | CPV-05、CPV-06 | backend/API/E2E | runtime、event、dashboard scenarios | pytest 加 Playwright assertions | implemented |
| `event-timeline-snapshot-replay` | CPV-06、CPV-07 | backend/E2E/external client | timeline/archive/replay docs 和 Validation Client evidence | command/checker evidence | partially_covered |
| `params-flow-and-diff` | CPV-08 | backend/E2E/Agent smoke | params tests、`dashboard-params-flow` | pytest、E2E、smoke checker | implemented |
| `agent-loop-step` | CPV-09 | backend/API/E2E | `agent-loop-step` E2E 和 backend tests | pytest 加 Playwright assertions | implemented |
| `agent-memory-context` | CPV-10 | backend/API | v0.5 memory tests | pytest | implemented |
| `agent-persistent-autonomy-evidence` | CPV-11、CPV-18 | autonomous/LLM-backed | LLM-backed plan | checker 或 scorecard PASS 加第二 Agent 复核 | planned_contract |
| `provider-live-smoke-deepseek` | CPV-12 | provider live smoke | LLM-backed plan | checker 或 scorecard PASS | blocked |
| `world-rule-parameter-evolution` | CPV-13 | autonomous/LLM-backed | LLM-backed plan | checker 或 scorecard PASS | planned_contract |
| `rule-compliant-event-generation` | CPV-14 | autonomous/LLM-backed | LLM-backed plan | checker 或 scorecard PASS | planned_contract |
| `projection-read-model-contract` | CPV-15 | contract/checker | v0.7 projection docs 和 checker | checker PASS | implemented |
| `dashboard-basic-runtime` | CPV-16 | E2E/Agent smoke | E2E 和 smoke scenarios | Playwright/checker PASS | implemented |
| `dashboard-generation-preview-readiness` | CPV-04、CPV-16 | E2E | E2E scenario | Playwright PASS | implemented |
| `worldengine-full-lifecycle-autonomous` | CPV-17、CPV-18、CPV-19 | autonomous saved-result | `agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md` | `make validate-agent-autonomous-result` | checker_supported |
| `llm-backed-full-lifecycle-autonomous` | CPV-11 到 CPV-19 | autonomous/LLM-backed | LLM-backed plan | checker 或 scorecard PASS 加第二 Agent 复核 | planned_contract |
| `redaction-integrity-scan` | CPV-19 | checker/docs audit | redaction rules、checker fixtures | checker 或 grep/probe evidence | partially_covered |
| `full-product-regression` | CPV-20 | command profile | product validation playbook | command matrix all pass | planned_contract |

## 最小完整运行场景集

后续完整验证至少应包含：

1. `governance-scope-boundary-audit`。
2. `recursive-schema-contract`。
3. `worldspec-loader-runtime-bridge`。
4. `deterministic-world-generation`。
5. `structured-generation-plan-import`。
6. `runtime-core-lifecycle`。
7. `event-timeline-snapshot-replay`。
8. `params-flow-and-diff`。
9. `agent-loop-step`。
10. `agent-memory-context`。
11. `projection-read-model-contract`。
12. `dashboard-basic-runtime`。
13. `dashboard-generation-preview-readiness`。
14. `worldengine-full-lifecycle-autonomous`。
15. `redaction-integrity-scan`。
16. `full-product-regression`。

如果 LLM-backed lifecycle 在范围内，还必须包含：

1. `provider-live-smoke-deepseek`。
2. `llm-backed-world-creation`。
3. `world-rule-parameter-evolution`。
4. `rule-compliant-event-generation`。
5. `agent-persistent-autonomy-evidence`。
6. `llm-backed-full-lifecycle-autonomous`。
