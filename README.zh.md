# WorldEngine

WorldEngine 是一个世界生成与运行引擎。它负责：

- 把世界设定编译成可运行世界包。
- 推进世界的权威时间和历史。
- 运行 Agent 的感知、决策、行动和公开经验连续性。
- 在允许的窗口接收用户干预，并由规则判断是否接受。
- 向 Godot、网页或其他客户端发布通用公开投影。

当前工作只由 [`docs/current/MVP.zh.md`](docs/current/MVP.zh.md) 指导。
`docs/iterations/` 中的旧版本文件保留为历史参考，不再是开发门禁。

## 仓库结构

- `backend/app/`：当前 FastAPI 引擎和公开 API。
- `frontend/`：项目自己的后台管理界面。
- `backend/worldengine/`：legacy，不再新增运行时功能。
- Godot 等渲染器和验证客户端位于独立仓库，只使用公开接口。

## 启动

```bash
make setup
make dev
```

- 后端：<http://127.0.0.1:8000>
- 后台管理：<http://127.0.0.1:5173>
- 最小闭环页面：<http://127.0.0.1:5173/admin/runnable-anchor>

## 当前公开闭环

客户端可以通过 `/api/v1/capabilities` 动态发现接口，然后依次完成：

1. 创建可运行世界包。
2. 创建世界 Session。
3. 精确推进一个或多个 tick。
4. 读取公开投影和增量事件。
5. 查看 Agent 决策及其事件、diff、snapshot 证据。
6. 提交有边界的用户方向、客户端动作和结果反馈。
7. 导出公开 evidence bundle。

## 验证

```bash
make test-mvp
make smoke-mvp
make test
```

以上只能证明 WorldEngine 一侧。完整 MVP 还必须由外部 Godot 客户端真实运行，并由独立
checker 检查证据；客户端不能自行宣布 PASS。
