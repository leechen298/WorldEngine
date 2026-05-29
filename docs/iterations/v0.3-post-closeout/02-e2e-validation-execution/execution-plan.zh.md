# 执行计划

状态：`template / not executed`

后续执行必须按以下步骤进行：

1. 确认 branch / commit。
2. 分别记录 evidence commit 和 final documentation commit。
3. 运行文档检查。
4. 运行后端确定性检查。
5. 运行聚焦 WorldSpec loader 测试。
6. 运行聚焦 runtime context bridge 测试。
7. 运行 event API compatibility 测试。
8. 检查 API route files。
9. 使用 TestClient 或 curl 运行 API smoke。
10. 检查 E2E framework 可用性。
11. 如果已配置，运行 E2E。
12. 如果不可用，记录 not configured / blocked。
13. 填写 `e2e-validation-report.md`。
14. 分类 P1/P2/P3。

## 文档检查

必需命令：

```bash
git status --short --branch
git diff --check
```

## 后端和聚焦检查

使用 `../01-e2e-validation-plan/test-plan.md` 中的命令形式；只有 active backend
environment 需要不同 venv 路径时，才调整命令并说明原因。

## API route 检查

API smoke 前先读取 route files 和 app factory。报告中必须记录实际读取的文件。

## API smoke

优先使用 TestClient，因为它不依赖长期运行的服务。只有本地 backend 已运行，或执行包明确启动了
backend 时，才使用 curl。

## E2E 处理

执行 E2E 前先检查配置和可运行命令。如果 E2E 未配置或无法运行，记录具体原因，并使用计划中的
fallback line。

## Finding 分类

- P1：claim conflict、compatibility break、loader / bridge failure、Event.refs
  response regression，或 concrete demo-world regression。
- P2：缺少必需证据、blocker 不清楚，或执行不完整。
- P3：非阻塞文档或信心缺口，并有明确交接。
