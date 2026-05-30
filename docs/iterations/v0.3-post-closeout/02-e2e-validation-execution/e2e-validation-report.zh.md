# E2E / 集成验证报告

状态：`passed`

## 报告字段

- Review 分支：`v0.3`
- 执行分支：`v0.3`
- 证据 commit：`da63cb8f28b484fba22596eb44fa5f09a218e45a`
- 最终文档收口 commit：`6712123b402fa8d454ede7779cc6a401d82ce684`
- 从证据 commit 到收口 commit 的实现差异：无 runtime、schema、API、frontend、
  backend tests、fixtures 或 migrations 变更。
- 验证日期：2026-05-29
- 执行者：Codex

## 已运行命令

```text
git status --short --branch
git rev-parse HEAD
git diff --check
make check-backend
make check-frontend
cd backend && .venv/bin/python -m pytest app/tests
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_loader.py
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py
cd backend && .venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_step.py
make test-e2e
make test-e2e  # local port bind 被 sandbox 拒绝后，经批准在 sandbox 外重跑
```

## 结果

- 分支 / commit 记录：`git status --short --branch` 输出
  `## v0.3...origin/v0.3`；`git rev-parse HEAD` 输出
  `da63cb8f28b484fba22596eb44fa5f09a218e45a`。
- 文档检查：`git diff --check` exit `0`。
- 依赖检查：`make check-backend` 和 `make check-frontend` 都 exit `0`。
- 后端确定性检查：
  `cd backend && .venv/bin/python -m pytest app/tests` exit `0`，
  结果为 `112 passed in 0.80s`。
- WorldSpec loader 结果：
  `cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_loader.py`
  exit `0`，结果为 `7 passed in 0.04s`。
- Runtime context bridge 结果：
  `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py`
  exit `0`，结果为 `11 passed in 0.05s`。
- Event API compatibility 结果：
  `cd backend && .venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py`
  exit `0`，结果为 `12 passed in 0.18s`。
- API smoke 结果：
  `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_step.py`
  exit `0`，结果为 `16 passed in 0.28s`；该测试通过 FastAPI TestClient
  覆盖 health、runtime step、`/world/events` 和 `/world/event-steps`。
- E2E 结果：第一次 sandbox 内 `make test-e2e` 因绑定
  `127.0.0.1:8000` 被拒绝，报 `operation not permitted`。批准后在 sandbox
  外重跑同一命令，exit `0`，结果为 `6 passed (6.4s)`。
- Release claim 检查：当前证据支持 v0.3 作为 loader/runtime-bridge
  infrastructure 的 release claim，并保持 v0.3 `final / closeout complete`
  状态。
- Compatibility review：当前 campaign 中 backend、loader、bridge、runtime、
  Event.refs、API smoke 和浏览器 dashboard E2E 验证均通过。
- Concrete demo-world regression 检查：本执行包未修改 runtime、schema、API、
  frontend、backend tests、fixtures、migration 或外部仓库文件。

## P1/P2/P3 Findings

- P1：未发现。
- P2：未发现。
- P3：未发现。第一次 E2E 需要为 local port bind 升级权限，但批准后的重跑通过；
  这不是产品或仓库缺陷。

## Blockers

无。短暂的 sandbox local-port denial 已通过批准后重跑同一
`make test-e2e` 命令解决。

## 最终评估

当前值：`passed`。
