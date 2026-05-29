# 测试计划

状态：`planned / not executed`

本文件是后续独立 reviewer 的命令和证据计划。本包不运行命令。

## 后续命令

仓库状态：

```bash
git status --short --branch
git rev-parse HEAD
git diff --check
```

聚焦 loader 验证：

```bash
cd backend
../.venv/bin/python -m pytest app/tests/test_worldspec_loader.py
```

聚焦 bridge 验证：

```bash
cd backend
../.venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py
```

Event compatibility 验证：

```bash
cd backend
../.venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py
```

可选的更宽后端验证：

```bash
cd backend
../.venv/bin/python -m pytest app/tests
```

## Reviewer 预期检查

- 对比 v0.3 release claims 与 docs / code。
- 检查 `load_worldspec` 是否通用且由 schema 支撑。
- 检查 runtime context bridge 输出是否有边界且惰性。
- 检查 `RuntimeEngine` context storage 是否不改变 step output。
- 检查 Event.refs empty responses 是否保持 legacy API shape。
- 检查 non-empty refs 是否仍然序列化。
- 检查 validation package 中没有 concrete demo-world content。
- 检查未运行的验证没有被写成证据。

## 未运行命令及原因

本包是 planning-only，因此不运行命令。

## Blocker 记录规则

如果后续 reviewer 无法运行命令，review 必须记录完整命令、工作目录、失败字符串，
并说明最终建议是 `blocked` 还是 `failed`。

## 不得声明未验证结果

Reviewer 不能在没有当前会话命令证据，或没有明确接受历史证据理由的情况下，把检查写成成功。
