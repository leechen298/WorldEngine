# E2E / Integration / API Smoke Validation Report

状态：`blocked`

## 元数据

- Reviewed branch：`v0.3-lcoal`
- Reviewed commit：`47b2dac6a08fdf7c249844b1f5447af17ab37d86`
- Execution date：2026-05-28
- Executor：Codex F
- Final assessment：`blocked`

允许的 final assessment values：

- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`

## 已读取文件

- Release docs：`docs/releases/v0.2.md`
- Evidence docs：`docs/iterations/v0.2/evidence-index.md`、
  `docs/iterations/v0.2/compatibility-review.md`、
  `docs/iterations/v0.2/boundary-audit.md`
- Backend route files：`backend/app/api/routes/health.py`、
  `backend/app/api/routes/runtime.py`、`backend/app/api/routes/world.py`、
  `backend/app/api/routes/world_params.py`、`backend/app/api/routes/archive.py`、
  `backend/app/api/routes/world_agent.py`
- Test files：`backend/tests/`、`backend/app/tests/`、
  `frontend/e2e/dashboard.spec.ts`
- E2E config files：`frontend/package.json`、`frontend/playwright.config.ts`

## 已运行命令

| Command | Purpose | Exit code | Result | Notes |
|---|---|---:|---|---|
| `git status --short --branch` | 记录 reviewed branch 和 worktree state | 0 | passed | 输出：`## v0.3-lcoal`。 |
| `git rev-parse HEAD` | 记录 reviewed commit | 0 | passed | 输出：`47b2dac6a08fdf7c249844b1f5447af17ab37d86`。 |
| `git diff --check` | Documentation 与 whitespace 检查 | 0 | passed | 无输出。 |
| `test -f docs/releases/v0.2.md && test -f docs/iterations/v0.2/evidence-index.md && test -f docs/iterations/v0.2/compatibility-review.md && test -f docs/iterations/v0.2/boundary-audit.md` | 必需 v0.2 evidence docs 存在性检查 | 0 | passed | 无输出。 |
| `make check-backend` | Backend dependency availability | 0 | passed | 无输出。 |
| `make check-frontend` | Frontend dependency availability | 0 | passed | 无输出。 |
| `backend/.venv/bin/python -m pytest backend/tests backend/app/tests -q` | Backend deterministic check，首次从 repo root 调用 | 2 | failed command invocation | Collection 因 `ModuleNotFoundError: No module named 'app'` 失败；已在 `backend/` 下重新运行，见下一行。 |
| `cd backend && .venv/bin/python -m pytest tests app/tests -q` | Backend deterministic checks | 0 | passed | `115 passed in 0.86s`。 |
| `cd backend && .venv/bin/python - <<'PY' ...` | API smoke，首次 payload 尝试 | 1 | failed smoke payload | 读接口返回 `200 code=0`；`POST /world/params/apply` 返回 422，因为 test payload 缺少必需的 `op`。 |
| `cd backend && .venv/bin/python - <<'PY' ...` | 使用 safe params payload 的 API smoke | 0 | passed | 必需 endpoints 返回 `200 code=0`，包括 `POST /world/params/apply`。 |
| `cd frontend && pnpm exec playwright --version && pnpm exec playwright install --dry-run chromium` | E2E framework 和 browser availability 检查 | 0 | passed | Playwright `1.60.0`；dry-run 输出包含 Chromium install target。 |
| `make test-e2e` | 已配置的 browser E2E suite | 2 | blocked | Playwright backend web server 绑定 `127.0.0.1:8000` 失败：`operation not permitted`。没有 browser tests 被执行。 |
| `git diff --name-only` | 在更新 report 前确认未修改 implementation files | 0 | passed | 更新 validation docs 前无输出。 |
| `git rev-parse HEAD` | 记录 validation-fix rerun commit | 0 | passed | 输出：`f1c99fc94f46b04e9286450bf0af7ebfb17253d3`；相对 original reviewed commit 的变化只有 validation docs。 |
| `make test-e2e` | validation-fix rerun blocking browser E2E command | 2 | blocked | 同一 blocker 复现：backend web server 无法绑定 `127.0.0.1:8000`，错误为 `operation not permitted`；没有 browser tests 被执行。 |
| `git diff --check` | validation-fix documentation whitespace check | 0 | passed | 更新 validation docs 后无输出。 |
| `git rev-parse HEAD` | 记录第二次 validation-fix rerun commit | 0 | passed | 输出：`9be4dc8d2d2696dadf625bd254386b0ad1b292d9`；这是本次 validation-fix 前的最新 review checkpoint。 |
| `make test-e2e` | 第二次 validation-fix rerun blocking browser E2E command | 2 | blocked | 同一 blocker 复现：Playwright web server 启动后无法绑定 `127.0.0.1:8000`，错误为 `operation not permitted`；没有 browser tests 被执行。 |
| `git diff --check` | 第二次 validation-fix documentation whitespace check | 0 | passed | 更新 validation docs 后无输出。 |

## 未运行检查

| Check | Reason | Blocker |
|---|---|---|
| Browser E2E test cases | Playwright web server 在 test execution 前失败。 | `make test-e2e` 无法将 backend server 绑定到 `127.0.0.1:8000`，错误为 `operation not permitted`。 |

## Release Claim Checks

| Claim | Evidence checked | Result | Finding |
|---|---|---|---|
| v0.2 closeout status remains final / complete | `docs/releases/v0.2.md` 写明 `Status: final / closeout complete`。 | passed | 无 |
| v0.2 does not claim product UI | `docs/releases/v0.2.md` 写明 v0.2 不提供 product client，并把 product UI 列为 future scope。 | passed | 无 |
| v0.2 does not claim WorldSpec runtime loading | `docs/releases/v0.2.md` 写明 v0.2 不把 WorldSpec 加载到 runtime，并把 loader/runtime bridge 列为 future scope。 | passed | 无 |
| v0.2 preserves existing runtime behavior | Backend tests 已通过；API smoke 覆盖 runtime state、step、events、event steps、params、snapshots 和 summaries。 | passed with E2E blocker | Browser E2E 仍 blocked。 |

## Compatibility Findings

- API envelope：API smoke 的 successful responses 返回 `code=0` 和 `data`。
- Runtime step：`POST /runtime/step` 返回 `200 code=0`；backend tests 已通过。
- World events：`GET /world/events` 返回 `200 code=0`；backend tests 已通过。
- Event steps：`GET /world/event-steps` 返回 `200 code=0`；backend tests 已通过。
- Params：`GET /world/params` 和 safe `POST /world/params/apply` 返回
  `200 code=0`；首次 malformed smoke payload 正确返回 422。
- Archive：`GET /world/snapshots` 和 `GET /world/summaries` 返回
  `200 code=0`；backend tests 已通过。
- Schema smoke：backend deterministic suite 已通过，其中包括 schema smoke tests。
- Event refs：backend deterministic suite 已通过，其中包括 event compatibility tests。

## Concrete Demo-World Regression Check

- Files checked：`docs/releases/v0.2.md`、`docs/iterations/v0.2/**`、
  `docs/scope-boundaries.md`、`docs/external-fixture-boundary.md`、
  `backend/app`、`frontend`
- Result：整体为 blocked，未观察到 runtime implementation regression。
- Finding：wording sweep 只发现 boundary、future-scope 和 historical references。
  更新 report 前 `git diff --name-only` 无输出，因此 validation 期间没有修改
  runtime、fixture、frontend 或 backend implementation files。

## 未解决 P1/P2/P3

- P1：无。
- P2：Browser E2E blocked，因为 `make test-e2e` 在本 execution context 中无法将
  backend web server 绑定到 `127.0.0.1:8000`。validation-fix reruns 在 commits
  `f1c99fc94f46b04e9286450bf0af7ebfb17253d3` 和
  `9be4dc8d2d2696dadf625bd254386b0ad1b292d9` 复现同一 blocker；implementation
  或 test-infrastructure changes 仍不属于本 package scope。
- P3：无。

## Final Assessment

`blocked`

Backend deterministic checks 和 API smoke 已用 current-session evidence 证明通过。
Configured browser E2E 没有运行，因为 Playwright 执行任何 tests 前 server startup
已被阻塞。validation-fix reruns 已确认同一 blocker。除非后续 validation bundle 明确
接受该 blocker，或在可绑定 configured backend port 的环境中重新运行 browser E2E，
否则本 package 不能记录 clean validation pass。
