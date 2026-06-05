# Review

英文镜像：`review.md`。

Status：implementation complete / PASS

## Documentation Stage Review

日期：2026-06-05

本 review 记录 `0.8.9.3-archive-summary-e2e-regression-repair` 的
documentation-stage 状态。

## Changed Files

创建：

```text
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/intent.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/intent.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/contract.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/contract.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/technical-design.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/technical-design.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/test-plan.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/test-plan.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/plan.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/plan.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.zh.md
```

更新 parent status/index documents：

```text
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

## Commands Run

```bash
find docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair -maxdepth 1 -type f -print | sort
```

结果：通过。Package 包含 required English files 和 Chinese mirrors：

```text
README.md
README.zh.md
contract.md
contract.zh.md
intent.md
intent.zh.md
plan.md
plan.zh.md
review.md
review.zh.md
technical-design.md
technical-design.zh.md
test-plan.md
test-plan.zh.md
```

```bash
rg -n "implementation_authorized: yes|evidence_execution_authorized: yes|Status: implementation complete|PASS" docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair docs/iterations/v0.8/CURRENT_STATE.md docs/iterations/v0.8/CURRENT_STATE.zh.md
```

结果：documentation-stage consistency 通过。`implementation_authorized: yes` 只作为未来
approval state、exit criterion 或推荐 approval target 出现。没有为 `0.8.9.3` 引入当前
`evidence_execution_authorized: yes` 或 implementation-complete package status。

```bash
git status --short --branch
```

结果：已检查。Working tree 中已有上一轮 testing-documentation 相关改动。本 package
只新增 `0.8.9.3` iteration directory，并更新 v0.8 parent status/index docs。

```bash
git diff --check
```

结果：通过，无输出。

## Product Tests

Documentation stage 未运行。本 package 尚未开始 implementation，不声明 E2E、backend、
frontend、runtime、API、autonomous validation 或 LLM-backed lifecycle PASS。

## Scope Review

当前仅 documentation scope：

- 未修改 runtime implementation files。
- 未修改 schema/API implementation files。
- 未修改 frontend implementation files。
- 未修改 E2E implementation files。
- 未修改 fixtures、migrations、generated results、external repositories 或
  `backend/worldengine/` files。

## Compatibility Review

Documentation stage 没有进行会影响 compatibility 的 code 或 schema changes。

Implementation contract 要求 archive summary response shape、stable MemoryPanel
selectors、existing runtime/API surfaces 和 E2E-only environment configuration 保持
additive compatibility。

## Findings

当前 documentation-stage findings：

- P0：none recorded。
- P1：none recorded。
- P2：none blocking。

Documentation/contract evaluator checkpoint：

- 日期：2026-06-05。
- Reviewer：read-only subagent/evaluator。
- 结果：contract、technical design 和 test plan 中没有 P0、P1 或 blocking P2。
- 已确认 required closeout checkpoints：implementation-scope evaluator、
  code-review evaluator、validation-evidence evaluator 和 closeout consistency
  evaluator。

## Authorization State

```text
implementation_authorized: yes
evidence_execution_authorized: yes, limited to test-plan.md commands
```

2026-06-05 已记录用户批准：

```text
批准 0.8.9.3-archive-summary-e2e-regression-repair 进入实现
```

Implementation 只能在本 package contract 内开始。

## Implementation Review Template

## Implementation Review

日期：2026-06-05

### Root Cause Bucket

```text
e2e_environment_gap
```

Focused evidence：

- 当 `8000` 端口没有已有 backend 时，focused scenario 使用 Playwright-managed
  servers 连续两次通过。
- `make test-e2e` 也在该 clean-server 状态下通过一次。
- 随后手动在 `127.0.0.1:8000` 启动普通 backend，未设置 E2E archive interval
  environment variables：

```bash
cd backend
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

- 在该 ordinary backend 已存在时运行 focused scenario，复现了历史症状：等待
  newer summary 超时。
- Playwright 通过 `/health` probe 复用了已有 backend，没有执行带有
  `WORLD_SUMMARY_INTERVAL_TICKS=2` 的 E2E backend command。
- Error context 显示 runtime `tick_id 4`，timeline 已有 ticks 1-4 的 event rows，
  但 MemoryPanel 仍显示 `No summaries yet`。
- API probes against reused ordinary backend 显示：

```text
/runtime/state -> tick_id: 4
/world/summaries?limit=5&order=desc -> items: [], total: 0
```

因此失败不属于 archive generation、summary API ordering 或 MemoryPanel refresh。
真正问题是 test environment 会静默复用非 E2E backend，而 default summary interval
不会在四步内生成 summary。

### Repair

最终修复：

- `frontend/playwright.config.ts` 使用 E2E-specific default ports：backend
  `18000`、frontend `15173`。
- Playwright web servers 设置 `reuseExistingServer: false`，避免 local E2E 静默
  复用 stale 或 ordinary dev server。
- Backend web server command 设置 `CORS_ORIGINS` 为当前 E2E frontend origin。
- 最终配置使用 `appUrl.origin` 设置 `CORS_ORIGINS`，因此带 path 或尾部斜杠的自定义
  `E2E_APP_BASE_URL` 不会造成 browser origin mismatch。
- `frontend/e2e/agent-loop.spec.ts` 和 `frontend/e2e/dashboard.spec.ts` 使用相同
  E2E backend default URL。
- `dashboard-archive-summary` scenario 仍然只 step 四次，并继续断言 API 创建
  newer summary 且 MemoryPanel 渲染该 summary。

Rejected intermediate change：

- 曾临时加入最多 step 24 次的 helper；code-review evaluator 指出它会让普通
  backend 也通过，从而掩盖 environment gap。该 helper 已移除，不属于最终修复。

### Files Changed For This Package

```text
frontend/playwright.config.ts
frontend/e2e/agent-loop.spec.ts
frontend/e2e/dashboard.spec.ts
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.zh.md
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

Working tree 中已有 unrelated `docs/testing/**` dirty files；它们不属于本 package，
不得作为本 package staged/closeout scope。

### Commands Run

Baseline and diagnosis：

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

结果：初次 sandbox run 在 test execution 前失败，因为 sandbox 阻止绑定
`127.0.0.1:8000`。Elevated rerun 通过：`1 passed`。

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

结果：第二次 elevated focused rerun 通过：`1 passed`。

```bash
make test-e2e
```

结果：修复前 clean-server 状态通过：`17 passed`。

```bash
git diff --check
```

结果：最终 CORS origin hardening 后通过，无输出。

```bash
make test-e2e
```

结果：最终 CORS origin hardening 后 `17 passed`。

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

结果：最终 CORS origin hardening 后 `PASS`。

```bash
cd backend
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

结果：已启动未设置 E2E summary interval environment 的 ordinary backend。

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

结果：against reused ordinary backend 失败，等待 newer summary 超时。Artifact path：

```text
test-results/e2e/artifacts/dashboard-dashboard-archiv-20000-ers-a-newer-archive-summary/trace.zip
```

```bash
curl -s http://127.0.0.1:8000/runtime/state
curl -s 'http://127.0.0.1:8000/world/summaries?limit=5&order=desc'
```

结果：runtime reached `tick_id: 4`；summary list empty。

Final verification：

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

结果：通过，`1 passed`。

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts
```

结果：通过，`6 passed`。

```bash
make test-e2e
```

结果：通过，`17 passed`。

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

结果：通过。

```bash
git diff --check
```

结果：通过，无输出。

```bash
git status --short --branch
```

结果：已检查。Branch 为 `v0.8...origin/v0.8`。Unrelated dirty `docs/testing/**`
files 仍在 working tree 中，并从本 package 排除。

### Adjacent Regression Decision

未修改 backend archive/API code，因此 `uv run pytest backend/app/tests` 按
`test-plan.md` 不需要运行。

未修改 `frontend/src/**` frontend source code，因此 `pnpm test` 和 `pnpm build`
按 `test-plan.md` 不需要运行。

仅修改 Playwright config/spec files，因此 required adjacent command 是
`cd frontend && pnpm exec playwright test e2e/dashboard.spec.ts`，已通过 `6 passed`。

### Subagent / Evaluator Findings

Documentation/contract evaluator：

- P0：none。
- P1：none。
- Blocking P2：none。
- Verdict：记录 authorization 后可进入 implementation。

Implementation-scope evaluator：

- P0：none。
- P1：none。
- P2：unrelated `docs/testing/**` dirty files 不属于 package scope，必须排除。
- P2：`review.md` closeout 前需要 root-cause evidence。已在本 implementation
  review 中处理。

Code-review evaluator：

- Initial P1：temporary 24-step helper 可能掩盖 E2E environment gap。
- Resolution：已移除 helper，改为修复 E2E environment configuration。
- Final rerun：无 P0/P1。P2 stale final assessment 已通过本 closeout update 解决。

Validation-evidence evaluator：

- P0：none。
- P1：none。
- P2：`frontend/e2e/agent-loop.spec.ts` 需要加入 allowed contract scope，因为所有
  E2E specs 必须共享同一个 E2E backend default。已通过更新 `contract.md` 和
  `contract.zh.md` 解决。
- P2：stale closeout/status text 需要更新。已通过本 final review 和 parent/package
  status updates 解决。
- Verdict：current-session commands 支持 scoped functional PASS evidence。

Closeout consistency：

- Final status text 和 parent route 已在 validation-evidence review 后更新。
- `docs/testing/**` dirty files 明确保持在本 package scope 外。

### Compatibility Review

- 未修改 archive summary API response shape。
- 未修改 backend archive generation behavior。
- 未修改 MemoryPanel selectors 或 rendering behavior。
- 未修改 runtime step、event、snapshot、params、generation 或 Agent loop behavior。
- E2E environment defaults 仅在 Playwright test environment 内变化。

### Scope Review

- 未修改 `backend/worldengine/`。
- 未修改 Validation Client repository。
- 未重写 generated validation result directories。
- 未加入 live provider、DeepSeek、LLM-backed world generation、concrete validation
  world content 或 app-specific backend logic。
- 不声明 product readiness、external validation PASS 或 LLM-backed lifecycle PASS。

### Unresolved Findings

- P0：none。
- P1：temporary helper 移除后 none。
- P2：unrelated dirty `docs/testing/**` files 仍在 working tree 中，已从本 package 排除。
- P3：none。

## Implementation Review Template

保留历史 template 作为 reference：

```text
Root cause bucket:
Focused diagnosis evidence:
Files changed:
Commands run:
Focused E2E result:
make test-e2e result:
Adjacent regression result:
Saved-result checker result:
Subagent/evaluator findings:
Compatibility review:
Scope review:
Unresolved findings:
Final assessment:
```

## Final Assessment

PASS。

`0.8.9.3-archive-summary-e2e-regression-repair` 已将
`dashboard-archive-summary` regression 作为 `e2e_environment_gap` 修复。最终实现保留
四步 newer-summary 强断言，并通过 E2E-specific default ports、禁用 silent
existing-server reuse、对齐 E2E CORS/API defaults，让 Playwright environment
deterministic。

Current-session verification 已通过：

- focused archive-summary E2E：`1 passed`。
- dashboard E2E adjacent regression：`6 passed`。
- full E2E suite：`17 passed`。
- saved-result checker：
  `PASS: validated agent autonomous result at test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle`。
- `git diff --check`：passed。

不声明 external validation PASS、product-readiness PASS 或 LLM-backed lifecycle
PASS。
