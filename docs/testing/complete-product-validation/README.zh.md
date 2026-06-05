# 完整产品验证文档套件

状态：计划中的完整测试文档套件，仅文档

英文镜像：`README.md`。

## 目的

本目录是 WorldEngine 完整产品验证的入口。它把测试全部当前功能和路线图相关能力所需的
文档组织成一套可执行体系，避免把所有内容塞进一个难以审核的超大测试方案。

这套文档用于后续验证时回答：

```text
WorldEngine 是否可以生成世界、随时间运行世界、暴露 events、snapshots、replay evidence，
支持具备 memory 和 continuity 的 Agent，把 public state 投影给外部消费者，并通过
redacted evidence 和 checkers 证明 lifecycle？
```

这不是 PASS 记录，不是产品迭代，也不授权修改 runtime、API、checker、fixture、
frontend、provider 或 Validation Client 代码。

## 当前基线

- `0.8.9` basic full lifecycle autonomous validation 已通过 saved-result checker。
- 该 PASS 证明了最低外部客户端 lifecycle：创建世界、推进 ticks、观察 events 和
  snapshots、捕获一个 WorldEngine-backed Agent action、提交 director guidance、
  导出 evidence，并通过 redaction。
- 该 PASS 不证明 LLM-backed provider calls、LLM-backed world creation、generated
  world rules、规则约束下的 event legality，或 Agent 持续性 pseudo-self behavior。
- LLM-backed 验证合同已定义在
  `docs/testing/llm-backed-lifecycle-validation-plan.md`，本套文档引用它，而不是把它
  作为孤立文档重复一遍。

## 文档地图

| 文档 | 作用 |
| --- | --- |
| `README.md` / `README.zh.md` | 套件索引、状态和使用方式。 |
| `coverage-map.md` / `coverage-map.zh.md` | 完整产品能力分类，以及从 North Star 到测试面的 traceability。 |
| `validation-spec.md` / `validation-spec.zh.md` | PASS/FAIL 权威来源、验证层级、角色、verdict rules 和硬边界。 |
| `scenario-matrix.md` / `scenario-matrix.zh.md` | 所有主要能力区的 scenario catalog，包括现有 E2E、Agent smoke、autonomous 和 LLM-backed lifecycle scenarios。 |
| `runbook.md` / `runbook.zh.md` | 后续完整验证执行顺序，包括 preflight、分阶段检查、第二 Agent 复核和结果记录。 |
| `evidence-contract.md` / `evidence-contract.zh.md` | artifact layout、required summaries、operation logs、redaction rules 和 evidence bundle 预期。 |
| `result-template.md` / `result-template.zh.md` | 写入 `docs/testing/results/` 的 durable result summary 模板。 |
| `gap-routing.md` / `gap-routing.zh.md` | 如何分类失败，并判断应该开 testing-asset 工作、WorldEngine 实现迭代、Validation Client milestone，还是环境修复。 |

## 与现有测试文档的关系

本套文档不替代现有测试文档，而是组合它们：

- `docs/testing/product-capability-validation-playbook.md` 定义通用产品验证流程。
- `docs/testing/test-documentation-playbook.md` 定义测试文档写法。
- `docs/testing/e2e-scenarios/` 定义浏览器 E2E scenario contracts。
- `docs/testing/agent-smoke/` 定义 Agent-assisted smoke contracts。
- `docs/testing/agent-autonomous/` 定义 Codex/test-runner autonomous saved-result
  contracts 和 checker expectations。
- `docs/testing/llm-backed-lifecycle-validation-plan.md` 定义 LLM-backed lifecycle
  validation contract。
- `docs/testing/results/` 记录实际验证运行后的 durable evidence。

## 使用方式

当用户提出以下请求时，使用本套文档：

```text
/goal 对当前产品能力做完整验证
/goal 完整测试 WorldEngine 全部功能
/goal 运行完整 LLM-backed lifecycle 验证
/goal 生成完整测试文档
```

如果请求是 documentation-only，只生成或更新本套文档，不声明 PASS。

如果请求是 validation execution，使用 `runbook.md`，生成 result directory，运行
documented commands/checkers，按需要做第二 Agent 复核，并在 `docs/testing/results/`
下写 durable result。

如果验证发现缺实现，先使用 `gap-routing.md` 分类，再决定是否开 WorldEngine iteration
或 Validation Client milestone。

## 完成标准

完整产品验证只有在 `coverage-map.md` 中每个 in-scope capability 都有以下状态和证据时才算完成：

- `pass`。
- `fail`。
- `blocked`。
- `skipped`。
- `out_of_scope`。

`pass` 必须来自 `validation-spec.md` 定义的 checker output、command output、scorecard
evidence 或第二 Agent 只读复核。计划、人工印象、只有 UI smoke、只有 provider readiness、
只有 deterministic mock behavior 都不足以通过。
