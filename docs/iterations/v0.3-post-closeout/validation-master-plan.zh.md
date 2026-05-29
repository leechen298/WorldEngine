# 主验证计划

状态：`executed / passed with P3`
类型：收口后验证控制计划

## 用途

本文件控制 v0.3 收口后的验证工作。v0.3 已经完成最终收口。2026-05-29 批准后的
campaign run 已补充 fresh independent validation evidence，并以
`passed with P3` 收口。

本 campaign 重点检查：

- WorldSpec loader 验证。
- runtime context bridge 验证。
- `RuntimeEngine` 兼容性。
- `Event.refs` 响应兼容性。
- API smoke 和集成行为。
- E2E 可用性，以及在已配置时的 E2E 执行。
- Codex 自主验证。
- release claim 和 compatibility claim review。
- 具体 demo-world regression 边界。

## 必读文件

- `README.md`
- `README.zh.md`
- `docs/releases/v0.3.md`
- `docs/releases/v0.3.zh.md`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`
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

如果必读文件缺失，必须记录到相关 `review.md`，不能靠记忆或相邻包推断内容。

## 结果状态

- `planned`：验证文档已存在，执行尚未开始。
- `ready for execution`：执行说明已经足够清楚，可以被 review。
- `executed`：执行已经发生，报告字段已经填写。
- `passed`：证据支持被检查的 claims，且没有未解决的 P1/P2/P3。
- `passed with P3`：证据支持被检查的 claims，但保留已接受的非阻塞 P3。
- `blocked`：验证无法完成，且 blocker 已记录。
- `failed`：验证已完成，但发现 P1/P2 failure 或 claim conflict。
- `not executed`：没有执行验证。
- `not executed in current campaign`：历史证据可能存在，但当前 campaign 没有执行或重新接受。
- `archived evidence only`：历史证据保留用于审计，不作为当前完成证据。

## 停止条件

出现下列情况时停止验证，并记录为 `blocked` 或 `failed`：

- 后端确定性测试失败。
- API smoke 失败。
- loader 验证失败。
- runtime context bridge 验证失败。
- runtime compatibility claim 与实际行为冲突。
- release claim 与实际行为冲突。
- Codex autonomous reviewer 报告 P1。
- 出现具体 demo-world regression。
- 命令无法运行且没有记录 blocker。

## 严重级别

- P1：推翻 v0.3 release 或 compatibility claim，破坏 loader / bridge 行为，破坏
  `RuntimeEngine` 或 `Event.refs` 兼容性，或引入具体 demo-world regression。
- P2：缺少必需证据、执行不完整、blocker 不清楚，或 unsupported claim 导致验证不可靠。
- P3：非阻塞文档缺口、打磨项、间接证据顾虑，或不影响最终评估的后续交接。

P1 阻塞收口。未解决 P2 会阻塞 clean final result，除非 active package 明确接受。
P3 只有在写明交接目标时才能 carry。

## E2E 可用性规则

如果没有可运行的 E2E setup，必须把 E2E 记录为 `not configured` 或 `blocked`，
并使用 API smoke 加后端集成测试作为 fallback validation line。

存在 Playwright 或 frontend 配置只能说明可能可用，不能证明测试套件可运行。

## Branch 和 commit 规则

执行包必须记录执行时 worktree 的真实 branch 和 commit。模板里不要硬编码 branch。

后续预期命令：

```bash
git status --short --branch
git rev-parse HEAD
```

## 发布状态规则

本 campaign 不改变 v0.3 发布状态。失败、阻塞或未执行的 campaign 可以指出后续验证工作，
但不能把 v0.3 final closeout 文档改写成重新打开 v0.3。
