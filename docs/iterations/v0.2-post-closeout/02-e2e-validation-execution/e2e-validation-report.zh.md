# E2E / Integration / API Smoke Validation Report

状态：`passed`（current campaign evidence）

重开说明：下方 2026-05-28 evidence 作为 historical evidence 保留。该次运行到达
`blocked`，因为旧 validation execution context 无法绑定 configured localhost
backend port。2026-05-29 在 `agent-iter` validation stages 已支持 host-capable
localhost binding 后，本 package 被重开。

当前 campaign 说明：当前 `/goal` run 已在 2026-05-29 重新执行本 package。
本 report 现在计入 `02-e2e-validation-execution` 的当前 campaign evidence。

## 元数据

- Reviewed branch：`v0.3-lcoal`
- Reviewed commit：`be5a48e48d950b88501ba0e68a80d35ab6f011b6`
- Execution date：2026-05-29
- Executor：Codex F
- Previous final assessment：`blocked`
- Current final assessment：`passed`

允许的 final assessment values：

- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`

## 当前执行摘要

当前 2026-05-29 rerun 记录了本 goal 产生的 docs-only working-tree changes，且
backend / frontend implementation 和 test paths 没有 diff。Backend deterministic
checks、API smoke、Playwright availability 和 configured browser E2E 都有
current-session command evidence，且均通过。

默认沙箱里的第一次 `make test-e2e` 尝试复现了 localhost bind blocker：
`127.0.0.1:8000` 上报 `operation not permitted`。随后 host-capable rerun 成功绑定
backend，并通过全部 configured browser E2E tests。

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
| `git status --short --branch` | 记录当前 campaign branch 和 worktree state | 0 | passed | branch 为 `v0.3-lcoal`；modified files 是 docs/rule files 和当前 `v0.2-post-closeout` docs；untracked `docs/iterations/v0.2-post-closeout.zip` 仍是无关文件。 |
| `git rev-parse HEAD` | 记录当前 campaign commit | 0 | passed | 输出：`be5a48e48d950b88501ba0e68a80d35ab6f011b6`。 |
| `git diff --check` | 当前 validation report 编辑前的 documentation 与 whitespace check | 0 | passed | 无输出。 |
| `test -f docs/releases/v0.2.md && test -f docs/iterations/v0.2/evidence-index.md && test -f docs/iterations/v0.2/compatibility-review.md && test -f docs/iterations/v0.2/boundary-audit.md` | 必需 v0.2 evidence docs 存在性检查 | 0 | passed | 无输出。 |
| `find backend/app/api/routes -maxdepth 1 -type f -name '*.py' -print \| sort` | Inspect configured backend API route files | 0 | passed | 找到 `__init__`、health、runtime、world、world_params、archive、world_agent route files。 |
| `make check-backend` | Backend dependency availability | 0 | passed | 无输出。 |
| `make check-frontend` | Frontend dependency availability | 0 | passed | 无输出。 |
| `rg -n "final / closeout complete\|0\.2\.12 verification is documentation-only\|does not rerun" docs/releases/v0.2.md` | Release status 和 limitation wording check | 0 | passed | 找到 `Status: final / closeout complete` 以及 documentation-only verification limitation lines。 |
| `test -f frontend/playwright.config.ts && test -f frontend/package.json` | E2E config file existence check | 0 | passed | 无输出。 |
| `cd backend && .venv/bin/python -m pytest tests app/tests -q` | Backend deterministic checks | 0 | passed | `115 passed in 0.89s`。 |
| `cd backend && .venv/bin/python - <<'PY' ...` | 使用 registered safe params payload 的 API smoke | 0 | passed | `GET /health`、`GET /runtime/state`、`POST /runtime/step`、`GET /world/events`、`GET /world/event-steps`、`GET /world/params`、`POST /world/params/apply`、`GET /world/snapshots` 和 `GET /world/summaries` 均返回 `200 code=0`。 |
| `cd frontend && pnpm exec playwright --version && pnpm exec playwright install --dry-run chromium` | E2E framework 和 browser availability check | 0 | passed | Playwright `1.60.0`；Chromium、headless shell 和 FFmpeg install targets 均可解析。 |
| `make test-e2e` | 默认沙箱内 configured browser E2E suite | 2 | blocked then rerun host-capable | Backend web server 绑定 `127.0.0.1:8000` 失败，错误为 `operation not permitted`；本次 sandbox attempt 没有执行 browser tests。 |
| `make test-e2e` | Host-capable configured browser E2E suite | 0 | passed | Backend 成功绑定 `127.0.0.1:8000`；configured browser E2E 结果为 `6 passed (7.2s)`。 |
| `git diff --name-only` | 记录当前 changed-file set | 0 | passed | 输出仅包含 docs/rule files 和 `v0.2-post-closeout` docs。 |
| `rg -n -i 'demo[- ]world\|concrete demo\|application-specific backend\|seed data\|story rules\|characters\|locations\|resources' docs/releases/v0.2.md docs/iterations/v0.2 docs/scope-boundaries.md docs/external-fixture-boundary.md backend/app frontend --glob '!frontend/node_modules/**' --glob '!test-results/**'` | Boundary wording / concrete demo regression sweep | 0 | passed | Matches 均为 boundary、future-scope 和 historical references。 |
| `rg -n -i 'demo[- ]world\|concrete demo\|application-specific backend\|seed data\|story rules\|characters\|locations\|resources' backend/app frontend --glob '!frontend/node_modules/**' --glob '!test-results/**'` | Active implementation concrete demo regression sweep | 1 | passed | 无匹配。 |
| `git diff --name-only -- backend/app frontend backend/tests backend/app/tests` | 确认当前 validation 没有修改 implementation 或 tests | 0 | passed | 无输出。 |
| `git status --short --branch && git rev-parse HEAD` | 记录 host-capable rerun 的 reviewed branch 和 commit | 0 | passed | 输出：`## v0.3-lcoal`；commit `dbffa069a5e74b6b1e6b60719152922595c60df6`。 |
| `git diff --check` | validation docs 编辑前的 documentation 与 whitespace check | 0 | passed | 无输出。 |
| `test -f docs/releases/v0.2.md && test -f docs/iterations/v0.2/evidence-index.md && test -f docs/iterations/v0.2/compatibility-review.md && test -f docs/iterations/v0.2/boundary-audit.md` | 必需 v0.2 evidence docs 存在性检查 | 0 | passed | 无输出。 |
| `find backend/app/api/routes -maxdepth 1 -type f -name '*.py' -print \| sort` | Inspect configured backend API route files | 0 | passed | 找到 health、runtime、world、world_params、archive、world_agent route files。 |
| `make check-backend` | Backend dependency availability | 0 | passed | 无输出。 |
| `make check-frontend` | Frontend dependency availability | 0 | passed | 无输出。 |
| `cd backend && .venv/bin/python -m pytest tests app/tests -q` | Backend deterministic checks | 0 | passed | `115 passed in 0.86s`。 |
| `cd backend && .venv/bin/python - <<'PY' ...` | API smoke，首次 payload 尝试 | 1 | failed smoke payload | 读接口返回 `200 code=0`；`POST /world/params/apply` 返回 422，因为 `validation.smoke` 不是 registered writable path。 |
| `cd backend && .venv/bin/python - <<'PY' ...` | 使用 registered safe params payload 的 API smoke | 0 | passed | 必需 endpoints 返回 `200 code=0`，包括使用 `counter.increment` 的 `POST /world/params/apply`。 |
| `cd frontend && pnpm exec playwright --version && pnpm exec playwright install --dry-run chromium` | E2E framework 和 browser availability check | 0 | passed | Playwright `1.60.0`；Chromium、headless shell 和 FFmpeg install targets 均可解析。 |
| `make test-e2e` | Configured browser E2E suite | 0 | passed | Backend 成功绑定 `127.0.0.1:8000`；`6 passed (7.5s)`。 |
| `git diff --name-only` | 更新 report 前确认没有 implementation files changed | 0 | passed | 更新 validation docs 前无输出。 |
| `rg -n -i 'demo[- ]world\|concrete demo\|application-specific backend\|seed data\|story rules\|characters\|locations\|resources' docs/releases/v0.2.md docs/iterations/v0.2 docs/scope-boundaries.md docs/external-fixture-boundary.md backend/app frontend --glob '!frontend/node_modules/**' --glob '!test-results/**'` | Boundary wording / concrete demo regression sweep | 0 | passed | Matches 均为 boundary、future-scope 和 historical references；没有 implementation change。 |
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
| `git rev-parse HEAD` | 记录第三次 validation-fix rerun commit | 0 | passed | 输出：`5da27c7f051ec21ad01486df78dd35656447cfb6`；本次 pass 前只修改了 validation findings documentation。 |
| `git status --short --branch` | 记录第三次 validation-fix worktree state | 0 | passed | 输出：`## v0.3-lcoal`，并显示 `docs/iterations/v0.2-post-closeout/findings.md` 已修改。 |
| `make test-e2e` | 第三次 validation-fix rerun blocking browser E2E command | 2 | blocked | 同一 blocker 复现：Playwright web server 启动后无法绑定 `127.0.0.1:8000`，错误为 `operation not permitted`；没有 browser tests 被执行。 |
| `git diff --check` | 第三次 validation-fix documentation whitespace check | 0 | passed | 更新 validation docs 后无输出。 |
| `git rev-parse HEAD` | 记录第四次 validation-fix rerun commit | 0 | passed | 输出：`6e9c7897e054e898d0854516c754202c9e2f91a8`；这是本次 validation-fix 前的最新 validation-review checkpoint。 |
| `git status --short --branch` | 记录第四次 validation-fix worktree state | 0 | passed | 输出：`## v0.3-lcoal`，并显示 `docs/iterations/v0.2-post-closeout/findings.md` 已修改。 |
| `make test-e2e` | 第四次 validation-fix rerun blocking browser E2E command | 2 | blocked | 同一 blocker 复现：Playwright web server 启动后无法绑定 `127.0.0.1:8000`，错误为 `operation not permitted`；没有 browser tests 被执行。 |
| `git diff --check` | 第四次 validation-fix documentation whitespace check | 0 | passed | 更新 validation docs 后无输出。 |
| `git rev-parse HEAD` | 记录第五次 validation-fix rerun commit | 0 | passed | 输出：`4a0c82ff74c30e86ef9b41b00f23fd7574b1fcde`；这是本次 validation-fix 前的最新 validation-review checkpoint。 |
| `git status --short --branch` | 记录第五次 validation-fix worktree state | 0 | passed | 输出：`## v0.3-lcoal`，并显示 `docs/iterations/v0.2-post-closeout/findings.md` 已修改。 |
| `make test-e2e` | 第五次 validation-fix rerun blocking browser E2E command | 2 | blocked | 同一 blocker 复现：Playwright web server 启动后无法绑定 `127.0.0.1:8000`，错误为 `operation not permitted`；没有 browser tests 被执行。 |
| `git diff --check` | 第五次 validation-fix documentation whitespace check | 0 | passed | 更新 validation docs 后无输出。 |
| `git rev-parse HEAD` | 记录第六次 validation-fix rerun commit | 0 | passed | 输出：`36234a82a82eeab196404888c33dc178c38850c8`；这是本次 validation-fix 前的最新 validation-review checkpoint。 |
| `git status --short --branch` | 记录第六次 validation-fix worktree state | 0 | passed | 输出：`## v0.3-lcoal`，并显示 `docs/iterations/v0.2-post-closeout/findings.md` 已修改。 |
| `make test-e2e` | 第六次 validation-fix rerun blocking browser E2E command | 2 | blocked | 同一 blocker 复现：Playwright web server 启动后无法绑定 `127.0.0.1:8000`，错误为 `operation not permitted`；没有 browser tests 被执行。 |
| `git diff --check` | 第六次 validation-fix documentation whitespace check | 0 | passed | 更新 validation docs 后无输出。 |
| `git rev-parse HEAD` | 记录第七次 validation-fix rerun commit | 0 | passed | 输出：`04ebbe50458e1845dba7104ed983fa89821ea417`；这是本次 validation-fix 前的最新 validation-review checkpoint。 |
| `git status --short --branch` | 记录第七次 validation-fix worktree state | 0 | passed | 输出：`## v0.3-lcoal`，并显示 `docs/iterations/v0.2-post-closeout/findings.md` 已修改。 |
| `make test-e2e` | 第七次 validation-fix rerun blocking browser E2E command | 2 | blocked | 同一 blocker 复现：Playwright web server 启动后无法绑定 `127.0.0.1:8000`，错误为 `operation not permitted`；没有 browser tests 被执行。 |
| `git diff --check` | 第七次 validation-fix documentation whitespace check | 0 | passed | 更新 validation docs 后无输出。 |

## 未运行检查

当前 2026-05-29 campaign rerun：无。Sandbox E2E attempt 被阻断，但 required
host-capable rerun 已完成并通过。

历史 2026-05-28 blocked run：

| Check | Reason | Blocker |
|---|---|---|
| Browser E2E test cases | Playwright web server 在 test execution 前失败。 | `make test-e2e` 无法将 backend server 绑定到 `127.0.0.1:8000`，错误为 `operation not permitted`。 |

## Release Claim Checks

| Claim | Evidence checked | Result | Finding |
|---|---|---|---|
| v0.2 closeout status remains final / complete | `docs/releases/v0.2.md` 写明 `Status: final / closeout complete`。 | passed | 无 |
| v0.2 does not claim product UI | `docs/releases/v0.2.md` 写明 v0.2 不提供 product client，并把 product UI 列为 future scope。 | passed | 无 |
| v0.2 does not claim WorldSpec runtime loading | `docs/releases/v0.2.md` 写明 v0.2 不把 WorldSpec 加载到 runtime，并把 loader/runtime bridge 列为 future scope。 | passed | 无 |
| v0.2 preserves existing runtime behavior | Backend tests 已通过；API smoke 覆盖 runtime state、step、events、event steps、params、snapshots 和 summaries；host-capable browser E2E 6 个 tests 已通过。 | passed | 无 |

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
- Result：passed；未观察到 runtime implementation regression。
- Finding：wording sweep 只发现 boundary、future-scope 和 historical references。
  对 `backend/app` 与 `frontend` 的 active implementation sweep 无匹配；`git diff
  --name-only -- backend/app frontend backend/tests backend/app/tests` 无输出。因此
  validation 期间没有修改 runtime、fixture、frontend、backend implementation 或
  test files。

## 未解决 P1/P2/P3

- P1：无。
- P2：无。Sandbox browser E2E bind blocker 已由 2026-05-29 host-capable rerun
  为 required evidence 解除；`make test-e2e` 退出码为 `0`，结果为
  `6 passed (7.2s)`。
- P3：无。

## 最终评估

`passed`

Backend deterministic checks、API smoke、Playwright availability 和 configured
browser E2E 均已用 current-session evidence 证明通过。Sandbox browser E2E bind
blocker 仍作为 environment evidence 保留在上文，但对本次 host-capable validation
run 不再是 unresolved blocker。
