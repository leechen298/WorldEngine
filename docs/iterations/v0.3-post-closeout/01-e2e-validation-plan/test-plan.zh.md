# 测试计划

状态：`planned / not executed`

本文件是后续验证计划。本包不运行这些命令。

## 后续精确命令

仓库和文档检查：

```bash
git status --short --branch
git diff --check
```

记录 branch 和 commit：

```bash
git rev-parse HEAD
```

后端确定性检查：

```bash
cd backend
.venv/bin/python -m pytest app/tests
```

如果仓库实际 backend venv 路径不同，必须记录实际命令和变化原因。

聚焦 WorldSpec loader 测试：

```bash
cd backend
.venv/bin/python -m pytest app/tests/test_worldspec_loader.py
```

聚焦 runtime context bridge 测试：

```bash
cd backend
.venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py
```

Event API compatibility 测试：

```bash
cd backend
.venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py
```

API smoke 检查：

- 检查 route files 和 app factory。
- 使用 FastAPI `TestClient`，或对本地运行的 backend 使用 `curl`。
- 覆盖 health、runtime step、`/world/events` 和 `/world/event-steps`。

E2E framework 可用性：

- 检查 package scripts、Playwright config、dependencies 和 browser availability。
- 没有可运行 setup 时，记录 `not configured` 或 `blocked`。

浏览器 E2E 执行：

- 只有 dependencies、services、ports 和 browsers 都可用时，才运行已配置的 E2E 命令。

## 预期结果

- 文档检查没有 whitespace 或必需文件问题。
- 后端确定性检查完成，或记录 blocker。
- Loader 测试覆盖有效 mapping / JSON 输入、malformed JSON、不支持输入、schema errors
  和 pointer paths。
- Runtime context bridge 测试覆盖 context derivation、invalid inputs、惰性 runtime
  storage，以及 event 中不暴露 raw WorldSpec / root payload。
- Event compatibility 测试覆盖 empty refs omission 和 non-empty refs presence。
- API smoke 校验当前响应形状，不改变 routes。
- E2E 要么有执行证据，要么记录为 not configured / blocked。
- Release claim validation 区分历史证据和当前 campaign 证据。
- Concrete demo-world regression check 确认 validation campaign 变更的 core docs 或 code
  没有新增具体 demo-world details。

## 未运行命令及原因

`01-e2e-validation-plan` 是 planning-only 包，因此不运行本测试计划中的命令。

## Blocker 记录规则

如果后续任何命令无法运行，必须记录：

- 完整命令。
- 工作目录。
- 如可用，记录 exit code。
- stderr 或失败摘要。
- 结果属于 `blocked` 还是 `failed`。
- 后续 owner 或 package。

## 不得声明未验证结果

除非后续执行包记录当前会话证据，或明确记录接受历史证据的理由，否则不要把任何检查写成成功。
