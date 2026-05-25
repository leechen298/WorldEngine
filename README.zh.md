# WorldEngine

Status: v0.1 scaffold complete, v0.2 planned.

英文版本：`README.md`。

WorldEngine 是 recursive world generation 与 runtime engine。当前 `v0.1` 分支是一个实验性
monorepo scaffold，用来验证第一组 runtime、Event、params、archive、agent-assist 和
dashboard surface。它还不是 recursive world engine implementation。

优先阅读：

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/current-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/releases/v0.1.md`
- `docs/iterations/README.md`

## Repository Structure

- `backend/` - FastAPI service。
- `frontend/` - Vue 3 + TypeScript dashboard。
- `docs/` - architecture、release、roadmap 和 iteration documents。
- `backend/app/` - active backend path。
- `backend/worldengine/` - legacy pre-v0.1 path；不要在那里新增 feature。

## Current v0.1 Capability

v0.1 可以：

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

v0.1 不能：

- 表达 recursive `WorldCell` structures。
- 加载结构化 `WorldSpec`。
- 从 templates 或 prompts 生成 worlds。
- 运行 Agent perception/action/memory loop。
- 建模 Agent pseudo-self continuity。
- 以 engine consumer 形式运行 external projection applications。
- 提供 packaged external product surface。

## Root-Level Quick Start

```bash
make setup
make dev
```

有用的单服务命令：

```bash
make dev-backend
make dev-frontend
```

### Backend Dev Run

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Dev Run

```bash
cd frontend
pnpm install
pnpm dev
```

默认 frontend API target 是 `http://localhost:8000`，可通过 `VITE_API_BASE_URL` 配置。

## Verification

已记录的 v0.1 closeout evidence 汇总在
`docs/testing/v0.1-test-map.md`。

关键已记录证据包括：

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

Implementation docs：

- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
