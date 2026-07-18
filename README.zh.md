# WorldEngine

状态：`v0.12 closeout complete / PARTIAL`

英文版本：`README.md`。

WorldEngine 是递归世界生成与运行时引擎。

当前 v0.12 closeout 完成 WorldEngine-side MVP campaign slice：runnable sessions、
rule-bound evolution、public Agent continuity、public memory/rest consolidation、
read-only narrative/diagnostic inspection surfaces、Validation Client evidence handoff，
以及 deterministic checker fixture evidence。最终 MVP classification 为 PARTIAL，因为
complete MVP PASS 仍需要 current external WorldEngine-Validation-Client export/result
directory，加 checker/scorecard/read-only review evidence。

WorldEngine 仍不是完整的递归世界引擎实现。Provider live behavior、fresh external
Validation Client validation、product readiness、subjective generation-quality approval、
durable persistence、更丰富的 self-continuity，以及 concrete world/demo content 均不属于当前
closeout。

优先阅读：

- `docs/project-north-star.md`
- `docs/project-plan.zh.md`
- `docs/product-model.md`
- `docs/scope-boundaries.zh.md`
- `docs/roadmap.zh.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.12/CURRENT_STATE.zh.md`
- `docs/iterations/v0.12/0.12.6-mvp-release-candidate-and-closeout/mvp-closeout-report.zh.md`
- `docs/iterations/v0.12/0.12.6-mvp-release-candidate-and-closeout/review.zh.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/api-reference-v0.6.zh.md`
- `docs/releases/v0.6.zh.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.zh.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.zh.md`
- `docs/iterations/v0.6/review.zh.md`

## 仓库结构

- `backend/` - FastAPI service。
- `frontend/` - Vue 3 + TypeScript dashboard。
- `docs/` - architecture、release、roadmap 和 iteration documents。
- `backend/app/` - active backend path。
- `backend/worldengine/` - legacy pre-v0.1 path；不要在那里新增 feature。

## 历史 v0.6 能力基线

v0.6 保留 v0.1 运行时脚手架、v0.3 loader/runtime bridge、v0.4 request-driven
Agent-in-World loop 和 v0.5 memory substrate，同时新增 World Generation v1。它可以：

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
- 定义 generic world-generation request、template、plan、validation 和 provenance
  schemas。
- 从已评审 templates 生成 deterministic generic `WorldSpec` 数据。
- 将 structured generation plans 编译为可审查 generation material。
- 通过严格边界导入 AI-assisted plan JSON，不接入 live provider 或 runtime AI。
- 在 `/world/generation` 下暴露 preview、regeneration 和 runtime-readiness generation
  APIs。
- 渲染带 validation/readiness diagnostics 的 dashboard generation preview workflow。

v0.6 仍不能：

- 把递归 `WorldCell` 结构作为活跃运行时状态运行。
- 把已加载的 `WorldSpec` 数据作为活跃递归世界状态运行。
- 声明 external validation-world readiness 或 projection application readiness。
- 声明 full product readiness、new live Agent smoke、full autonomous runner、
  live provider 或 generation-quality validation。
- 持久化保存 memory 或暴露 public memory APIs。
- 运行 automatic reflection、self-summary generation、relationship behavior 或
  personality drift action modifiers。
- 建模完整 Agent pseudo-self continuity。
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

当前 v0.12 closeout evidence 汇总在：

- `docs/iterations/v0.12/0.12.6-mvp-release-candidate-and-closeout/mvp-closeout-report.zh.md`
- `docs/iterations/v0.12/0.12.6-mvp-release-candidate-and-closeout/review.zh.md`
- `docs/iterations/v0.12/0.12.5-full-lifecycle-checker-and-autonomous-validation/full-lifecycle-validation-result.zh.md`
- `docs/iterations/v0.12/0.12.5-full-lifecycle-checker-and-autonomous-validation/scorecard-summary.zh.md`
- `docs/iterations/v0.12/review.zh.md`

v0.12 final classification 为 PARTIAL。WorldEngine-side Agent continuity、memory、
inspection、handoff 和 deterministic checker evidence 已存在。Complete MVP PASS 仍被缺失的
current v0.12 external Validation Client export/result directory 阻断。

历史 v0.6 closeout 和 post-closeout repair evidence 汇总在：

- `docs/releases/v0.6.zh.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.zh.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.zh.md`
- `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`
- `docs/iterations/v0.6/review.zh.md`

早期 v0.1/v0.3/v0.6 closeout evidence 仍是兼容性基线材料，不是当前 MVP closeout result。

关键已记录证据包括：

- v0.6 0.6.11 reliability repair evidence 见
  `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`：focused
  backend/API repair suite `59 passed`、full backend regression `233 passed`、
  frontend unit `36 passed`、frontend build 通过且仅有既有 Vite large-chunk
  warning、full E2E `17 passed`、saved Agent smoke checker PASS、minimal
  autonomous saved-result checker PASS、0.6.11 scope guard `out_of_scope=0`，
  以及 forbidden implementation sentinel 对 `backend/worldengine`、
  `backend/app/alembic`、`backend/migrations` 和 `test-results` 无输出。
- v0.6 final closeout evidence 见 `docs/iterations/v0.6/review.md` 和
  `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.zh.md`：
  full backend regression `220 passed`、frontend unit `36 passed`、frontend build
  通过且仅有 Vite large-chunk warning、E2E `16 passed`、required docs/mirrors
  `missing=0`、changed-file scope guard `out_of_scope=0`，以及 closeout
  consistency evaluator PASS。
- v0.6 明确不声明 external validation readiness、projection readiness、product
  readiness、new live Agent smoke、full autonomous runner、live provider 或
  generation-quality pass。

- v0.5 final closeout evidence 见 `docs/iterations/v0.5/review.md` 和
  `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.zh.md`：
  focused backend memory/loop/action compatibility `33 passed`、full backend
  regression `145 passed`、required docs/mirrors `missing=0`、changed-file
  scope guard `out_of_scope=0`，以及 closeout consistency evaluator PASS。
- v0.5 overall validation 见
  `docs/testing/results/2026-05-31-v0.5-overall-validation.md`：focused memory
  substrate `7 passed`、focused perception/loop API `16 passed`、focused
  memory/loop/action compatibility `33 passed`、full backend regression
  `145 passed`、frontend unit `28 passed`、focused Agent Loop E2E `9 passed`、
  full E2E `15 passed`、Agent smoke saved-result checker PASS，以及 minimal
  autonomous saved-result checker PASS。
- v0.4 final closeout evidence 见 `docs/iterations/v0.4/review.md` 和
  `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/final-closeout.md`：
  聚焦 backend/API `35 passed`、全 backend `139 passed`、最终文档镜像检查
  `missing=0`、最终范围检查 `out_of_scope=0`。
- v0.3 加载器和运行时桥接迭代包证据、兼容性审计与最终收口评审。

这些是已经记录的 closeout results，不是本次 README 更新重新运行的测试。

实现文档：

- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.zh.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.zh.md`
- `docs/releases/v0.6.zh.md`
- `docs/iterations/v0.5/README.zh.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.zh.md`
- `docs/releases/v0.5.zh.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.6.zh.md`
- `docs/api-reference-v0.5.md`，作为 v0.5 compatibility API baseline
- `docs/api-reference-v0.1.md`，作为 legacy v0.1 API reference
- `docs/testing/v0.1-test-map.md`

## 许可证

Copyright 2025 leechen298。

WorldEngine 采用 Apache License, Version 2.0。详见 `LICENSE` 和 `NOTICE`。
