# v0.3 收口后验证 campaign

状态：`campaign planned / ready for review`
类型：`post-closeout validation goal campaign`

## 目标

为 v0.3 收口后的独立验证创建文档体系。本 campaign 的重点是 WorldSpec 加载器、
运行时上下文桥接、API / runtime 兼容性、浏览器 E2E 可用性，以及 Codex 自主验证。

v0.3 的功能和文档收口已经完成。
本 campaign 尚未执行 v0.3 独立 E2E / 集成验证。
本 campaign 尚未执行 v0.3 Codex 自主验证。
本 campaign 不重新打开 v0.3 实现。
本 campaign 不改变 v0.3 发布状态。
本轮只创建验证 campaign 文档。

## 目标入口

自然语言目标：

```text
完成 v0.3-post-closeout
```

含义：

把本目录作为 Codex App `/goal` 的 campaign 指引。执行时先看
`CURRENT_STATE.md`，按 `GOAL_RUNNER.md` 路由，并只在每个子包已有所需证据或
记录了阻塞原因后，才按 `CAMPAIGN_PLAN.md` 推进到下一步。

这不是 WorldEngine 运行时行为，也不是外部自动化控制器实现。它只定义本仓库内的
验证文档、路由、停止条件和证据要求。

## 边界

允许：

- 定义收口后验证流程。
- 定义 E2E / 集成 / API smoke 规划。
- 定义后续验证执行报告模板。
- 定义 Codex 自主验证规划和评审模板。
- 定义最终验证汇总模板。
- 保持 v0.3 `final / closeout complete` 状态，同时明确尚未补充 fresh validation。

禁止：

- 本轮文档创建期间，不运行 backend、frontend、runtime、API smoke、schema、
  fixture、migration、build、E2E、Agent smoke、Codex autonomous 或 regression 检查。
- 不修改 runtime、schema、API、frontend、backend tests、fixtures 或外部仓库。
- 不加入具体 demo world 名称、角色、地点、资源、剧情规则、seed data、UI selector
  或 private oracle details。
- 不把验证计划写成验证结果。
- 不改变 v0.3 发布状态。

## 后续执行前必读

- `README.md`
- `docs/releases/v0.3.md`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/evidence-index.md`
- `docs/iterations/v0.3/compatibility-audit.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/review.md`
- `docs/scope-boundaries.md`
- `docs/external-fixture-boundary.md`
- `docs/validation-report-template.md`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/event.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`
- `backend/app/tests/test_event_api_compat.py`
- `backend/app/tests/test_event_schema_compat.py`

如果后续执行时发现必读文件缺失，必须记录到当前子包的 `review.md`，并按
`validation-master-plan.md` 停止或降级处理。

## 验证链路

0. 主验证规划。
1. E2E / 集成 / API smoke 验证计划。
2. E2E / 集成 / API smoke 执行模板。
3. Codex 自主验证计划。
4. Codex 自主验证执行与评审模板。
5. 最终验证汇总模板。

## 子包索引

| 子包 | 类型 | 初始状态 | 用途 |
|---|---|---|---|
| `01-e2e-validation-plan` | 验证规划 | `planned` | 定义 E2E、集成、API smoke、loader、bridge、兼容性和 release claim 验证范围。 |
| `02-e2e-validation-execution` | 验证执行模板 | `not started` | 提供后续执行步骤和报告模板；本轮不执行。 |
| `03-codex-autonomous-validation-plan` | 验证规划 | `not started` | 定义独立 Codex reviewer 的输入、约束和必检项。 |
| `04-codex-autonomous-validation-execution` | 自主评审模板 | `not started` | 提供独立评审模板和初始 `not executed` 报告。 |
| `05-final-validation-bundle` | 验证汇总模板 | `not started` | 提供最终综合模板，但不写最终结论。 |

## 最终评估状态

最终评估：`not executed`。

本 campaign 已规划，等待人工 / ChatGPT review。只有后续执行包填入当前会话证据或
明确阻塞原因后，v0.4 才能把它当作 fresh validation evidence 参考。
