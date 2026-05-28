# WorldEngine

状态：`v0.3 final / closeout complete`

英文版本：`README.md`。

WorldEngine 是递归世界生成与运行时引擎。当前 `v0.3` 分支是 WorldSpec Loader
and Runtime Bridge 里程碑：它新增最小通用 `WorldSpec` 加载器和可选的惰性运行时
上下文桥接层，同时保持 v0.1 运行时脚手架兼容。它还不是完整的递归世界引擎实现。

优先阅读：

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/current-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/releases/v0.3.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/README.md`

## 仓库结构

- `backend/` - FastAPI service。
- `frontend/` - Vue 3 + TypeScript dashboard。
- `docs/` - architecture、release、roadmap 和 iteration documents。
- `backend/app/` - active backend path。
- `backend/worldengine/` - legacy pre-v0.1 path；不要在那里新增 feature。

## 当前 v0.3 能力

v0.3 保留 v0.1 运行时脚手架，并且可以：

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
- 渲染 runtime controls、timeline、world params 和 agent params interactions 的 dashboard。
- 通过最小加载器加载并校验通用 `WorldSpec` 数据。
- 从已加载的 `WorldSpec` 数据派生可选、惰性的运行时上下文。
- 保持 runtime step 输出和 event payload 不暴露原始 `WorldSpec` 或 root tree 数据。

v0.3 仍不能：

- 把递归 `WorldCell` 结构作为活跃运行时状态运行。
- 把已加载的 `WorldSpec` 数据作为活跃递归世界状态运行。
- 从 templates 或 prompts 生成 worlds。
- 运行 Agent perception/action/memory loop。
- 建模 Agent pseudo-self continuity。
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

- `docs/iterations/v0.3/README.zh.md`
- `docs/releases/v0.3.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
