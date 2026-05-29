# 契约

## 公开概念

- 独立 review：reviewer 直接读取 source docs 和 code。
- 证据命令：review session 中真实运行，并记录结果或 blocker 的命令。
- Unsupported claim：没有当前证据支撑，或与实际代码行为冲突的 statement。
- 最终建议：review template 中允许的结果之一。

## 允许修改

后续执行本包时，可以：

- 填写 `codex-autonomous-review.md`。
- 更新 `review.md`。
- 记录 files read、commands run、blockers、unsupported claims、findings 和 recommendation。

## 禁止修改

- 不修改实现代码。
- 不修改测试。
- 不修改 runtime、schema、API、frontend、fixtures、migrations 或外部仓库。
- 不添加 demo-world details、UI selectors、seed data 或 private oracle details。
- 不在本包修复 findings。
- 不改变 v0.3 发布状态。
- 不声称未运行命令成功。

## 兼容性要求

后续 review 必须检查：

- WorldSpec loader findings。
- runtime context bridge findings。
- API / schema / runtime compatibility findings。
- Event.refs compatibility findings。
- concrete demo-world regression check。
- unsupported claims。
- unresolved P1/P2/P3。

## 范围外后续事项

最终综合属于 `05`。任何修复都属于未来已评审 repair package。
