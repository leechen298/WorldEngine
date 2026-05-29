# v0.3 收口后验证 campaign

状态：`campaign executed / passed with P3`
类型：`post-closeout validation goal campaign`

## 目标

执行由文档控制的 v0.3 收口后独立验证 campaign。本 campaign 的重点是
WorldSpec 加载器、运行时上下文桥接、API / runtime 兼容性、浏览器 E2E
可用性，以及 Codex 自主验证。

v0.3 的功能和文档收口已经完成。
本 campaign 已记录 v0.3 独立 E2E / 集成验证的当前会话证据。
本 campaign 已记录 v0.3 Codex 自主验证的当前会话评审证据。
本 campaign 不重新打开 v0.3 实现。
本 campaign 不改变 v0.3 发布状态。
本轮只用执行证据更新验证 campaign 文档。

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
- 用当前会话证据填写验证执行报告。
- 用直接源码/证据 review 填写 Codex 自主验证评审。
- 用当前证据填写最终验证汇总。
- 保持 v0.3 `final / closeout complete` 状态，同时明确未运行项。

禁止：

- 不运行或声称超出本验证 campaign 授权范围的检查。
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
| `01-e2e-validation-plan` | 验证规划 | `review complete` | 已定义 E2E、集成、API smoke、loader、bridge、兼容性和 release claim 验证范围。 |
| `02-e2e-validation-execution` | 验证执行 | `passed` | 已运行 backend、聚焦 loader/bridge/Event/runtime 检查、API smoke 覆盖和浏览器 E2E。 |
| `03-codex-autonomous-validation-plan` | 验证规划 | `review complete` | 已定义独立 Codex reviewer 的输入、约束和必检项。 |
| `04-codex-autonomous-validation-execution` | 自主评审 | `passed with P3` | 已完成直接源码/证据 review，并记录非阻塞 P3 handoff。 |
| `05-final-validation-bundle` | 验证汇总 | `passed with P3` | 已汇总当前 campaign 证据、P3 handoff 和 v0.4 proceed 状态。 |

## 最终评估状态

最终评估：`passed with P3`。

本 campaign 已记录当前会话 backend、API smoke、E2E、loader、bridge、
Event.refs 和 Codex autonomous review 证据，并延续非阻塞 P3 handoff。v0.4
只能通过自己的已评审迭代包继续。
