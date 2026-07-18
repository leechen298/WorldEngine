# 评审

英文源文件：`review.md`。

状态：closed / WorldEngine 侧验证通过

implementation_authorized: yes
provider_live_call_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## 评估边界

本评审只记录 `0.13.0-worldengine-runnable-anchor` 的实现和本轮会话证据，支持的是
WorldEngine 侧可运行锚点结论。它不声明全仓回归全部通过，也不声明完整 v0.13 MVP PASS、
Godot 已运行或外部 checker 已给出裁决。

## 实现授权

Documentation/contract evaluator PASS 后，用户于 2026-07-18 明确批准
`0.13.0-worldengine-runnable-anchor` 开始实现。用户随后要求无需反复询问常规授权，但该指令
没有把 provider live call、外部仓库修改、Godot 或完整 v0.13 证据执行纳入本 child。

## 变更文件

本 package 负责的后端实现：

```text
backend/app/engine/__init__.py
backend/app/engine/models.py
backend/app/engine/generation.py
backend/app/engine/evidence.py
backend/app/engine/rules.py
backend/app/engine/agent_runtime.py
backend/app/engine/session.py
backend/app/schemas/engine_v1.py
backend/app/api/routes/engine_v1.py
backend/scripts/engine_v1_anchor_smoke.py
backend/app/tests/test_engine_v1_generation.py
backend/app/tests/test_engine_v1_session.py
backend/app/tests/test_engine_v1_agent.py
backend/app/tests/test_engine_v1_interventions.py
backend/app/tests/test_engine_v1_protocol.py
```

共享的后端集成文件：

```text
backend/app/api/app_factory.py
backend/app/api/routes/__init__.py
```

本 package 只负责其中 `engine_v1_router` 的导入和注册，以及 `EngineV1Service` 的应用状态
初始化。这两个脏文件中同时存在无关的 session-router 变更；本 package 没有创建、回退或
认领那些变更。

本 package 负责的前端实现：

```text
frontend/package.json
frontend/pnpm-lock.yaml
frontend/src/App.vue
frontend/src/main.ts
frontend/src/router/index.ts
frontend/src/api/engineV1.ts
frontend/src/api/engineV1.test.ts
frontend/src/pages/RunnableAnchorPage.vue
frontend/src/pages/RunnableAnchorPage.test.ts
frontend/src/components/runnable-anchor/ProjectionPanel.vue
frontend/src/components/runnable-anchor/EvidencePanel.vue
frontend/e2e/minimum-runnable-anchor.spec.ts
```

本轮视觉证据：

```text
output/playwright/worldengine-anchor-desktop.png
output/playwright/worldengine-anchor-mobile-top.png
output/playwright/worldengine-anchor-mobile-evidence.png
```

本 campaign 创建或更新的迭代文档：

```text
docs/iterations/v0.13/README.md
docs/iterations/v0.13/README.zh.md
docs/iterations/v0.13/CURRENT_STATE.md
docs/iterations/v0.13/CURRENT_STATE.zh.md
docs/iterations/v0.13/GOAL_RUNNER.md
docs/iterations/v0.13/GOAL_RUNNER.zh.md
docs/iterations/v0.13/CAMPAIGN_PLAN.md
docs/iterations/v0.13/CAMPAIGN_PLAN.zh.md
docs/iterations/v0.13/v0.13-plan.md
docs/iterations/v0.13/v0.13-plan.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/README.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/README.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/intent.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/intent.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/contract.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/contract.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/technical-design.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/technical-design.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/test-plan.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/test-plan.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/plan.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/plan.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/review.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/review.zh.md
docs/project-plan.md
docs/project-plan.zh.md
docs/roadmap.md
docs/roadmap.zh.md
```

## 已运行命令

在 `backend/` 运行聚焦后端验证：

```bash
.venv/bin/python -m pytest \
  app/tests/test_engine_v1_generation.py \
  app/tests/test_engine_v1_session.py \
  app/tests/test_engine_v1_agent.py \
  app/tests/test_engine_v1_interventions.py \
  app/tests/test_engine_v1_protocol.py -q
```

结果：退出码 `0`，`24 passed in 2.08s`。

在 `frontend/` 运行前端验证：

```bash
pnpm test
pnpm build
pnpm test:e2e --grep "minimum runnable anchor"
```

结果：

- `pnpm test`：退出码 `0`，9 个测试文件、50 个测试全部通过。
- `pnpm build`：退出码 `0`，类型检查和 Vite 生产构建通过。Vite 对 1.586 MB 主包给出
  不阻断收口的 chunk 大小警告。
- 聚焦 Playwright E2E：退出码 `0`，1 个测试通过，总耗时 3.7 秒。

原 test plan 在 `--grep` 前多写了一层参数分隔符，Playwright 因而把该选项解释为文件过滤
条件并报告没有测试。中英文 test plan 现已改成上方可复现的成功命令；那次错误调用不计为
测试通过。

在 `backend/` 运行黑盒 HTTP smoke：

```bash
.venv/bin/python scripts/engine_v1_anchor_smoke.py
```

结果：退出码 `0`，分类为 `WORLDENGINE_SIDE_ANCHOR_PASS`，
`complete_v0_13_claimed=false`，11 项检查全部通过，`missing_checks=[]`。最终投影为
tick `2`、revision `7`、event cursor `10`，证据完整。检查覆盖 manifest discovery、
确定性 package、package/session hash 交接、同窗口方向判定、方向延后应用、精确步进、Agent
因果链、action、feedback、事件完整轮询和 evidence completeness。

在 `backend/` 运行全量后端回归：

```bash
.venv/bin/python -m pytest -q
```

结果：退出码 `1`，`484 passed, 1 failed`。失败用例为
`app/tests/test_agent_continuity_consolidation_evidence.py::test_manifest_exposes_agent_continuity_endpoint`。
本评审不声明全后端回归全部通过。

补充检查：

```bash
env PYTHONPYCACHEPREFIX=/tmp/worldengine-pycache \
  .venv/bin/python -m py_compile \
  scripts/engine_v1_anchor_smoke.py \
  app/engine/session.py \
  app/engine/evidence.py \
  app/schemas/engine_v1.py
git diff --check
```

两条命令退出码均为 `0`。此前直接运行 `py_compile` 时，文件系统沙箱不允许写入 macOS 用户
缓存目录；改为显式使用临时缓存目录后通过，后者才是记录的语法检查结果。

## 验收结果

| 验收项 | 结果 | 本轮证据 |
| --- | --- | --- |
| AC-01 确定性世界包 | PASS | 规范化后等价的 brief 生成相同 ready hash；允许的输入变化会改变对应公开字段和 hash。 |
| AC-02 Session 来源和初始状态 | PASS | Package hash、Session source hash、初始 snapshot、projection revision 和 state hash 一致。 |
| AC-03 精确锁步推进 | PASS | `step N` 精确推进 N 个 tick，时间、revision 和 event sequence 单调。 |
| AC-04 Agent 因果链 | PASS | 感知、决策、请求、判定、结果、事件、diff 和 experience 引用形成一条公开链。 |
| AC-05 经历影响后续决策 | PASS | 后续决策引用先前公开经历，并暴露机器可观察的决策模式变化。 |
| AC-06 接受有界方向 | PASS | 有界方向在明确窗口中被接受，只能由后续规则关联事件和非空 diff 应用。 |
| AC-07 拒绝直接最终事实 | PASS | 同窗口的 direct-final-fact 请求得到稳定语义拒绝，没有 diff，也没有目标状态变更。 |
| AC-08 幂等和 revision 冲突 | PASS | 重复 ID 只重放匹配 payload；不同 payload 复用 ID 和过期 revision 均失败且不修改状态。 |
| AC-09 可重放证据 | PASS | 检查 snapshot/diff/state-hash 重放；篡改 diff、event、Agent decision 或跨窗口方向证据后 completeness 会变为 incomplete。 |
| AC-10 只用 manifest 的黑盒客户端 | PASS | 独立服务进程只通过公共 HTTP 和 manifest discovery 完成流程。 |
| 项目管理控制台 | PASS | 单测、构建、E2E 和真实浏览器流程证明控制台只走 API，并一致刷新权威状态。 |
| 全后端回归 | FAIL | 实际结果是 484 passed、1 个无关 legacy manifest 断言失败。 |
| Godot 和外部 checker | NOT_RUN | 由 `0.13.1`、`0.13.2` 负责，本 child 禁止实施。 |
| 完整 v0.13 验证 | NOT_RUN | 必须等待当前运行的外部 Godot/checker 证据。 |
| Provider live 路径 | NOT_RUN | 本 package 禁止且不依赖该路径。 |

## 真实浏览器验证

管理控制台在真实浏览器中走通了世界包生成、Session boot、同窗口 accepted/rejected 方向
提交、精确两 tick 步进、通用客户端 action、typed feedback、投影刷新和证据检查。

- 桌面视口：1440 x 1000。
- 手机视口：390 x 844。
- 检查过程中发现页面级手机横向溢出，已通过约束 projection 网格子项修复。最终测量为
  `documentScrollWidth=innerWidth=390`，宽表只在自身容器内滚动。
- 保存的图片中没有不合理重叠或空白渲染。
- 浏览器控制台只有一个 `favicon.ico` 404，没有应用或运行时错误。

## 独立 evaluator 链

- Documentation/contract evaluator
  `019f74b5-e8a5-7870-81c9-38e86284454a`：PASS，无 P1/P2/P3。
- Implementation-scope evaluator
  `019f7531-b80c-7d62-a0d9-232b01a700e6`：PASS。
- Code-review evaluator
  `019f7532-e3a4-7e22-b2d4-58900d4ed416`：修复 idempotency payload 绑定、证据重放和
  completeness、隐私边界、原子 mutation、revision 一致性、rollback 和同窗口防拼接后，
  最终 PASS，无 P1/P2/P3。
- Validation-evidence evaluator
  `019f755d-6a3a-7350-9ee8-cb7c27673669`：WorldEngine 侧 package 边界 PASS；同时明确
  把全后端回归判为 FAIL，把 Godot、外部 checker 和完整 v0.13 验证判为 NOT_RUN。
- Closeout-consistency evaluator
  `019f756e-50c6-7913-8784-e9597e47e676`：PASS。它确认只关闭 `0.13.0` 并路由到
  `0.13.1` 文档准备，可以保留全回归失败和外部路径 NOT_RUN 的真实边界，不改变授权字段，
  也不会误报完整 v0.13。
- Post-transition consistency evaluator
  `019f7575-5f19-7683-b710-7e40d90e65a0`：PASS，无 P1/P2。它重新读取最终中英文状态文件，
  确认 child 已关闭、`0.13.1` 仅进入文档准备、父级三项授权均为 `no`，且没有全仓、Godot
  或完整 v0.13 完成声明。

此前超时、在读取更新文件前被中断或被关闭的 evaluator 没有给出可用结论，因此没有被当成
PASS；以上已完成 evaluator 才是本评审记录的 gate 证据。

## 兼容性审查

- Engine V1 以 `/api/v1` 增量加入，没有替换历史 world、runtime、provider、archive 和
  dashboard 路由。
- 管理端外壳新增 Vue Router，同时在 `/` 保留历史控制台，把锚点放在
  `/admin/runnable-anchor`。
- 进程内状态是本最小 package 的明确设计，没有引入 migration 或生产持久化 contract。
- 全回归失败来自未修改的 legacy 测试中的精确字典成员断言。用户原有的脏改
  `backend/app/schemas/world.py` 和 `backend/app/api/routes/world.py` 会给 `PublicSurface`
  序列化额外的 `maturity`、`validation_status` 和 `notes` 字段。当前证据不能把该失败归因
  给 Engine V1；本 package 也没有为强行全绿而修改或回退这些无关 surface。

## 范围审查

实现只落在 `backend/app/`、`backend/scripts/`、`frontend/`、迭代文档和生成的视觉证据。
没有向 `backend/worldengine/` 新增代码，没有修改外部 Validation Client 仓库，没有加入
Godot 内容，没有调用 provider live，没有暴露 Agent 私有状态，没有在 core 中创建具体
验证世界，没有加入生产持久化，也没有允许客户端直接写 canonical facts。

Smoke 分类被明确命名为 `WORLDENGINE_SIDE_ANCHOR_PASS`，并输出
`complete_v0_13_claimed=false`。它不是外部裁决，不能替代独立 checker。

## 未解决问题

- P1：无。
- P2：无。
- P3：由于上面说明的无关脏 legacy manifest/test 不匹配，全后端回归仍是
  `484 passed, 1 failed`；本评审不声明全仓 PASS。
- P3：前端生产构建报告主包 chunk 大小警告。
- P3：手工浏览器检查存在仅 favicon 的 404；没有观察到可见或功能性应用错误。

## 最终评估

Validation-evidence 和 closeout-consistency gate 均已通过，`0.13.0` 自有验收项已经由当前
证据证明。本 package 按 WorldEngine 侧范围正式关闭，只向 `0.13.1` 的文档准备阶段交接；
下一 child 不继承实现授权或外部仓库修改授权。

即使 `0.13.0` 收口，完整 v0.13 MVP PASS 仍然禁止声明；必须等 `0.13.1` 提供 Godot 和可由
独立 checker 检查的外部证据，再由 `0.13.2` 执行相关联的最终验证。
