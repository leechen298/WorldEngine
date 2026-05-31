# Testing and Evidence

Status: testing evidence guide

英文版本：`README.md`。

本目录记录 WorldEngine iterations 的 testing standards 和 evidence。

## Evidence Rules

- 没有在当前 work session 运行命令时，不要声称 tests passed。
- Code packages 必须在 package `review.md` 中列出 exact commands 和 results。
- Runtime、UI、E2E 或 live smoke claims 必须包含可 review 的 evidence。
- Docs-only packages 可以跳过 code tests，但必须在 `review.md` 说明 no-test rationale。

## Result Files

使用 `docs/testing/results/` 存放 durable evidence summaries，适用于 package 运行 broader
verification 或 manual/runtime checks 的场景。

建议命名格式：

```text
YYYY-MM-DD-<version-package>-<slug>.md
```

每个 result file 应包含：

- command 或 workflow。
- environment assumptions。
- output summary。
- failures 或 skipped checks。
- 回链到 iteration package。

## Product Capability Validation

当用户询问某个 version、release candidate 或当前产品状态是否真的通过时，使用
`docs/testing/product-capability-validation-playbook.zh.md`。一句话请求可以触发
playbook，但 PASS 仍然必须来自当前会话命令或 checker evidence。

## Test Documentation

当用户要求编写、补充、整理或 review 测试文档、测试方案、测试场景或测试用例时，使用
`docs/testing/test-documentation-playbook.zh.md`。一句话请求可以触发 playbook，但产物是
test-documentation artifact，不是 PASS verdict。

版本级测试方案文档：

- `docs/testing/v0.4-overall-test-plan.zh.md`
- `docs/testing/v0.5-overall-test-plan.zh.md`

## Agent Smoke

Agent-assisted smoke tests 必须遵循 `docs/testing/agent-smoke/`。Codex 或其他 agent
可以执行和观察，但 PASS/FAIL 必须来自 deterministic Playwright assertions 或
`tools/testing/validate_agent_smoke_result.py`。

历史 raw Agent smoke artifacts 应放在 ignored `test-results/agent-smoke/<timestamp>/`
下。最新一次已 review 的原始记录可以提交到 `test-results/agent-smoke/latest/`，用于审计。
Durable summaries 应放在 `docs/testing/results/` 下。

当前 Agent smoke scenario contracts 位于 `docs/testing/agent-smoke/scenarios/`。
`dashboard-basic-runtime` 可执行。`dashboard-params-flow` 和
`dashboard-invalid-param`、`dashboard-agent-autotune` 都是 `live-smoke-recorded`。
当前 raw `latest/` 目录指向 `dashboard-agent-autotune`；更早的 params-flow 和
invalid-param raw evidence 通过 durable summaries 和历史提交保留。

## E2E Scenario Contracts

当前代码对应的 E2E scenario contracts 位于 `docs/testing/e2e-scenarios/`。

已实现的当前 E2E 覆盖：

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`
- `dashboard-agent-autotune`
- `dashboard-timeline-navigation`
- `dashboard-archive-summary`
- `agent-loop-step`

E2E PASS 仍必须来自当前会话的 Playwright assertion result。

## Codex/Test-Runner Autonomous Contracts

Codex/test-runner autonomous test contracts 位于 `docs/testing/agent-autonomous/`。

该目录中的 "Agent" 指 Codex/test-runner agent 作为测试执行者操作 WorldEngine，
不是未来 WorldEngine 世界里的 in-world Agent。

当前 autonomous scenarios 是 scorecard contracts。本仓库现在提供最小 saved-result
checker：

```bash
make validate-agent-autonomous-result RESULT_DIR=<dir>
make validate-agent-autonomous-fixtures
```

该 checker 可以验证已记录的 Codex/test-runner autonomous evidence。它不是 broad
autonomous runner、调度器，也不代表每个 autonomous scenario 都已经 live-run。

## Future Implementation Prerequisites

Selector、validator、checker 和 test-environment 前置条件记录在
`docs/testing/test-implementation-prerequisites.md`。
