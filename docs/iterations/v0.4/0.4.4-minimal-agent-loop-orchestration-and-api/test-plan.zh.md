# 测试计划

## 要运行的精确命令

本包必需文档命令：

```bash
git status --short --branch
git diff --check
```

本包特定验证预期：

- `git status --short --branch`
- `git diff --check`
- 检查必需文档和镜像是否存在
- 按 active package contract 执行 changed-file scope guard
- 在 `backend/` 下运行聚焦 backend/API 测试：

```bash
.venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
```

- 实现变更后在 `backend/` 下运行全 backend 回归：

```bash
.venv/bin/python -m pytest app/tests tests -q
```

- 将 `app/tests/test_agent_loop_api.py` 作为新 route 的 FastAPI TestClient API smoke，并作为既有 `/world/agent/params/propose-and-apply` route 的兼容性检查。

如果本包在未来执行中修改 backend 实现文件，必须运行上面的聚焦 backend/API 命令，然后运行上面的全 backend 回归命令。

## 预期结果

- 文档检查退出 `0`。
- 必需文件和镜像存在。
- 没有变更文件超出 active package contract。
- 任何 backend/API/E2E/runtime pass claim 都有当前会话命令支撑，或记录为 not run。

## 未运行命令及原因

文档草拟期间不运行 backend、API smoke、runtime behavior 或 test implementation 命令，除非后续获授权执行中修改实现文件。除非本包意外触及对应 surface，否则不预期运行 frontend、E2E、Agent smoke、build、fixture 或 migration 命令；此类范围扩张必须先评审。

## Blocker 记录规则

如果命令无法运行、evaluator checkpoint 不可用或缺失必需文件，必须在 `review.md` 中记录 `blocked` 或 `needs-user-input`，并写明精确命令、缺失文件或不可用 checkpoint。

## 不得未验证声明规则

除非命令或评审在当前会话运行，或 active contract 带理由明确接受，否则不得把 tests、API smoke、E2E、backend checks、frontend checks、runtime behavior、migration、fixture behavior、release status 或 closeout status 标记为 passed。
