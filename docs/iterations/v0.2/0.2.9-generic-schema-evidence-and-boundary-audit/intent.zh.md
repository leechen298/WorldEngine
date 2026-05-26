# Intent

英文版本：`intent.md`

## 问题

v0.2 已有多个 completed schema、event、workflow、boundary 和 contract packages。
在 legacy compatibility review 和 release-candidate packaging 前，milestone
需要一个 evidence map，明确区分 implemented、documented、tested、reviewed、
planned 和 explicitly out-of-scope claims。

如果缺少该 audit，future automation 可能把 planned work 当成 implemented
capability，遗漏 stale status drift，或模糊 external consumer boundaries。

## 目标

创建 documentation-only audit package；review approval 后它会：

- 把 active v0.2 capability claims 映射到 contract、review 和 verification
  evidence。
- 审计 external fixture、validation、concrete-demo 和 legacy boundaries。
- 将 missing evidence 记录为 explicit findings。
- 解决或记录 deferred 0.2.7 milestone status inconsistency。
- 保持 runtime、schema、API、frontend、fixture、migration 和 test
  implementation files untouched。

## 非目标

- 不实现 code。
- 不改变 schema behavior 或 tests。
- 不 opportunistically fix schema or event gaps。
- 不实现 WorldSpec loading、runtime bridge、generation、projection、agent
  loop、memory、self-continuity、external repositories 或 frontend behavior。
- 不恢复 concrete external-world fixtures、seed data、roles、locations、
  resources、story rules、product UI 或 application-specific backend logic。
- 不声明 v0.2 release-candidate 或 final status。

## 为什么现在做

0.2.7 和 0.2.8 已加固 recursive schema 与 event reference contracts。0.2.10
将 review v0.1 runtime compatibility 和 legacy boundaries。0.2.9 位于二者
之间，负责在 compatibility 和 release-candidate documentation 依赖当前 evidence
之前，把 evidence 显式化。

## North Star 对齐

本 package 通过让 evidence、boundaries 和 status claims 可检查，支撑 recursive
world foundation。它防止 WorldEngine 漂移为 application-specific 或
demo-specific behavior，同时保留未来 runtime、agent、memory 和 projection 工作
所需的 event 与 schema foundations。
