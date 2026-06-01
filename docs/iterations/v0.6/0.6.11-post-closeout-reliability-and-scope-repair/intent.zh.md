# 意图

状态：review complete

## 问题

v0.6 reliability validation 初始结论是 `partial pass`，不是 clean pass。可执行命令矩阵
通过了，但 scope authorization 和 backend/API reliability findings 曾阻塞最终的
clean-pass evidence。

核心问题包括 governance 和两个窄行为缺口：

- `0.6.10` 是 documentation-only，不能授权当前 backend/frontend dirty files。
- 当无关的非 JSON 值导致 canonical digest 失败时，failed generation fallback digest 会丢掉
  有效 seed material。
- public preview API 没有直接覆盖 sensitive imported-plan provenance failure。

## 为什么现在处理

当前工作树已经包含 post-closeout review-fix changes。若只把它们放在 parent review
addendum 中，repo 会保持含混状态：部分文档声称 clean，reliability result 却写着 partial
pass。

## 与路线图的关系

这是 v0.6 repair package。它不启动 v0.7 external validation readiness，也不启动 v0.8
projection readiness。

## 非目标

- 不新增 generation capability。
- 不新增 public API route 或 schema。
- 不做 migrations、persistence、live provider behavior 或 concrete world content。
- 不执行新的 live Agent smoke 或 autonomous runner。

## 预期交接

本包通过后，v0.6 保持 final/closed，并新增 post-closeout reliability repair 记录。若未来重跑失败，
durable reliability result 必须降级并明确记录 blockers。
