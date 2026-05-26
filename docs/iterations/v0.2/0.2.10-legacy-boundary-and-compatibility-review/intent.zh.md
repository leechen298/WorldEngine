# Intent

英文版本：`intent.md`

## 问题

v0.2 在保留 v0.1 runtime scaffold 的同时增加了 recursive schema 和 additive
event reference foundations。v0.3 开始 loader 或 runtime bridge 设计前，项目
需要一个清晰的 compatibility boundary，说明哪些是 active，哪些是 legacy，
哪些行为要保留，以及哪些内容不能被意外改变。

如果没有这个边界，后续 bridge work 可能会混淆 additive schema contracts 与当前
runtime behavior，重新启用 legacy code paths，或把 v0.2 文档误认为 runtime
loading 已经存在的证据。

## 期望结果

评审通过后，本 package 将产出：

- legacy boundary document，覆盖 active、legacy、placeholder 和 future paths。
- v0.2 compatibility review，将当前 runtime/API/frontend compatibility
  expectations 映射到 evidence 和 handoff constraints。
- unresolved compatibility gaps 或 status drift 的 findings。
- package review evidence，证明文档工作保持在范围内。

## 用户

- 准备 v0.2 release-candidate 文档的 Codex A。
- 准备 v0.3 bridge work 的 Codex B 或未来 implementation agents。
- 检查 v0.2 是否保留 v0.1 行为的 human / ChatGPT reviewers。
- 需要知道哪些 contracts 已 active、哪些 bridge behavior 属于 future scope 的
  external consumers。

## 非目标

- 不实现 WorldSpec loader。
- 不把 RuntimeEngine 迁移到 WorldCell。
- 不实现 runtime bridge。
- 不修改 runtime behavior。
- 不改变 API response shapes。
- 不修改 frontend behavior。
- 不重构或重新启用 `backend/worldengine/`。
- 不增加 tests、fixtures、migrations 或 concrete external-world anchors。

## 成功定义

当 documentation package ready for review，并且评审通过后 implementation pass
可以在不修改代码的情况下创建 legacy boundary 和 compatibility review docs，
本 package 即达到目标。
