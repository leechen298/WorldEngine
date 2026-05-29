# Execution Plan

状态：`archived evidence only / not executed in current campaign`

## 步骤

1. 确认 branch 和 commit：

   ```bash
   git status --short --branch
   git rev-parse HEAD
   ```

2. 运行 documentation checks：

   ```bash
   git diff --check
   test -f docs/releases/v0.2.md
   test -f docs/iterations/v0.2/evidence-index.md
   test -f docs/iterations/v0.2/compatibility-review.md
   test -f docs/iterations/v0.2/boundary-audit.md
   ```

3. 如果 dependencies 可用，运行 backend deterministic checks。

4. 检查 `backend/app/api/routes/` 下的 API route files。

5. 使用 TestClient 或 curl 运行 API smoke。

6. 通过检查 `frontend/package.json`、`frontend/playwright.config.ts`、installed
   dependencies、browser binaries、service start commands、ports 和 required
   environment variables 来确认 E2E framework availability。

7. 如果 configured 且 runnable，运行 browser E2E。

8. 如果不可用，把 E2E 记录为 not configured 或 blocked。不要把 config files 本身当成
   successful run。

9. 填写 `e2e-validation-report.md`。

10. 将 unresolved issues 分类为 P1/P2/P3。

## Required API Smoke Areas

- `GET /health`
- `GET /runtime/state`
- `POST /runtime/step`
- `GET /world/events`
- `GET /world/event-steps`
- `GET /world/params`，if available
- `POST /world/params/apply`，if available and safe test payload exists
- `GET /world/snapshots`，if available
- `GET /world/summaries`，if available

## 停止条件

出现以下情况时停止并记录 blocker：

- dependencies 缺失且无法在 execution context 安装。
- required services 无法启动。
- ports 不可用且没有 configured alternate port。
- browser dependencies 缺失。
- command 在产生 meaningful validation evidence 前失败。
- release claim 与 observed behavior 冲突。

## 输出

execution 输出是 `e2e-validation-report.md` 和更新后的 `review.md`。

2026-05-28 execution 已到达该输出状态；但 browser E2E 当时 blocked，因为 configured
backend web server 在旧 execution context 中无法绑定 `127.0.0.1:8000`。2026-05-29
在 `agent-iter` validation stages 已改为使用 host-capable localhost binding 后，本
package 被重开。rerun 已保留 prior evidence 可见，并追加新的 current-session
evidence。2026-05-29 host-capable rerun 已通过 configured backend、API smoke 和
browser E2E validation commands。
