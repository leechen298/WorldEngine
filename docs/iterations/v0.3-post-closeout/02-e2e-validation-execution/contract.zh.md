# 契约

## 公开概念

- 证据 commit：被验证行为所在的 commit。
- 最终文档 commit：如果与证据 commit 分开，指包含完整验证文档的 commit。
- 后端确定性结果：选定命令集的 deterministic backend test 结果。
- API smoke 结果：通过 TestClient 或 curl 进行的轻量 API 验证结果。
- E2E 结果：浏览器 E2E 结果，或记录为 not configured / blocked。

## 允许修改

后续执行本包时，可以：

- 运行验证命令。
- 检查 docs、source code、route files、package scripts 和 E2E config。
- 更新 `e2e-validation-report.md`。
- 更新 `review.md`。
- 记录 P1/P2/P3 findings 和 blockers。

## 禁止修改

- 不修改 runtime、schema、API、frontend、backend tests、fixtures、migrations
  或外部仓库。
- 不添加 E2E tests 或 fixtures。
- 不修复实现。
- 不改变 v0.3 发布状态。
- 不包含 concrete demo-world details、UI selectors、seed data 或 private oracle details。
- 不把未运行检查写成成功。

## 兼容性要求

执行时必须专门检查或记录 blocker：

- WorldSpec loader behavior。
- runtime context bridge behavior。
- 惰性 `RuntimeEngine` context compatibility。
- Event.refs response compatibility。
- 既有 API response shapes。
- release claim 与 v0.3 文档的一致性。

## 范围外后续事项

任何修复或实现变更都属于单独的已评审 package。Codex autonomous review execution 属于 `04`。
