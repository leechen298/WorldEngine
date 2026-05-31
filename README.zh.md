# WorldEngine

状态：`v0.5 final / closeout complete`

英文版本：`README.md`。

WorldEngine 是递归世界生成与运行时引擎。

当前 `v0.5` 分支已完成 Memory and Self-Continuity Substrate 收口。它保留
v0.4 Agent-in-World Minimal Loop，并新增 additive generic working-memory 和
episodic-memory schemas、process-local in-memory memory substrate，以及接入
Agent Loop perception path 的 bounded read-only memory context。Action
semantics 保持不变。

WorldEngine 仍不是完整的递归世界引擎实现。Durable memory persistence、public
memory APIs、automatic reflection、self-summary generation、relationship
behavior、personality drift action modifiers、world generation、external
validation readiness、projection application readiness 和 concrete world/demo
content 仍属于后续版本范围。

优先阅读：

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/current-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/releases/v0.3.md`
- `docs/iterations/v0.5/README.zh.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.zh.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/README.md`

## 仓库结构

- `backend/` - FastAPI service。
- `frontend/` - Vue 3 + TypeScript dashboard。
- `docs/` - architecture、release、roadmap 和 iteration documents。
- `backend/app/` - active backend path。
- `backend/worldengine/` - legacy pre-v0.1 path；不要在那里新增 feature。

## 当前 v0.5 能力

v0.5 保留 v0.1 运行时脚手架、v0.3 loader/runtime bridge 和 v0.4
request-driven Agent-in-World loop，同时新增第一层 generic memory substrate。它可以：

- 从仓库根目录启动 backend 和 frontend development services。
- 暴露 health、runtime、world event、world params、archive 和 agent params routes。
- 推进 runtime ticks 与 world time。
- 把 runtime 和 module events 追加到 in-memory event log。
- 暴露 cursor-paginated event timelines 和 grouped event steps。
- 执行一个包含 heartbeat/counter 示例的小型 world module tree。
- 应用经过验证的 world parameter patches。
- 在应用前 dry-run world parameter patches。
- 按配置 interval 创建 in-memory snapshots 和 summaries。
- 使用 LLM-style params agent service interface 提出并应用 patches。
- 从 runtime state、recent events、world params 和可选 runtime context summary
  构建有界 agent perception frame。
- 校验可审查的 `ActionIntent` payload，并返回 `ActionResult` evidence。
- 通过小而经过检查的边界处理 `noop` 和已校验的 `params.patch` actions。
- 暴露 `POST /world/agent/loop/step`，执行一次 request-scoped perceive ->
  intent -> validate/apply -> result cycle。
- 使用可审查 provenance 表达 generic working-memory 和 episodic-memory records。
- 在有界 in-memory backend substrate 中保存 process-local working 和 episodic memory。
- 在不改变 action request、intent 或 result semantics 的前提下，为 Agent Loop
  perception frame 增加可选 bounded read-only memory context。
- 渲染 runtime controls、timeline、world params 和 agent params interactions 的 dashboard。
- 通过最小加载器加载并校验通用 `WorldSpec` 数据。
- 从已加载的 `WorldSpec` 数据派生可选、惰性的运行时上下文。
- 保持 runtime step 输出和 event payload 不暴露原始 `WorldSpec` 或 root tree 数据。

v0.5 仍不能：

- 把递归 `WorldCell` 结构作为活跃运行时状态运行。
- 把已加载的 `WorldSpec` 数据作为活跃递归世界状态运行。
- 从 templates 或 prompts 生成 worlds。
- 持久化保存 memory 或暴露 public memory APIs。
- 运行 automatic reflection、self-summary generation、relationship behavior 或
  personality drift action modifiers。
- 建模完整 Agent pseudo-self continuity。
- 以 engine consumer 形式运行 external projection applications。
- 提供 packaged external product surface。

## 根目录快速启动

```bash
make setup
make dev
```

有用的单服务命令：

```bash
make dev-backend
make dev-frontend
```

### 后端开发运行

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 前端开发运行

```bash
cd frontend
pnpm install
pnpm dev
```

默认 frontend API target 是 `http://localhost:8000`，可通过 `VITE_API_BASE_URL` 配置。

## 验证

已记录的 v0.3 closeout evidence 汇总在
`docs/iterations/v0.3/evidence-index.md`，并由 `docs/releases/v0.3.md` 总结。

v0.1 runtime closeout evidence 仍是兼容性基线，记录在
`docs/testing/v0.1-test-map.md`。

关键已记录证据包括：

- v0.5 final closeout evidence 见 `docs/iterations/v0.5/review.md` 和
  `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.zh.md`：
  focused backend memory/loop/action compatibility `33 passed`、full backend
  regression `145 passed`、required docs/mirrors `missing=0`、changed-file
  scope guard `out_of_scope=0`，以及 closeout consistency evaluator PASS。
- v0.4 final closeout evidence 见 `docs/iterations/v0.4/review.md` 和
  `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/final-closeout.md`：
  聚焦 backend/API `35 passed`、全 backend `139 passed`、最终文档镜像检查
  `missing=0`、最终范围检查 `out_of_scope=0`。
- v0.3 加载器和运行时桥接迭代包证据、兼容性审计与最终收口评审。
- `make check-backend` 和 `make check-frontend`。
- backend pytest: `63 passed`。
- frontend unit tests: `24 passed`；后续 focused frontend coverage 记录为
  `28 passed`。
- frontend production build: 成功，并保留已记录的 chunk-size warning。
- `make test-e2e`: `6 passed`。
- live Agent smoke：
  - `dashboard-params-flow`: 0.1.8 evidence 通过
    `docs/testing/results/2026-05-24-v0.1.8-params-flow-live-smoke.md` 和 commit
    `c6da552` 保留。
  - `dashboard-invalid-param`: 当前 validated evidence 位于
    `test-results/agent-smoke/latest/`。

这些是已经记录的 closeout results，不是本次 README 更新重新运行的测试。

实现文档：

- `docs/iterations/v0.5/README.zh.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.zh.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/releases/v0.3.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
