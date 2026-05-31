# 技术设计

状态：review complete

## 设计类型

Documentation-only contract refinement。

`0.5.4` 不授权 runtime、schema、service、API、frontend、migration、fixture 或 test
implementation。

## 概念边界

四个概念保持分离，以避免隐藏 behavior coupling：

- relationship state 描述 agent-to-target relationship facts。
- self-summary 用可审计摘要描述 agent continuity state。
- reflection record 捕获一次 review 或 self-assessment event。
- personality drift signal 捕获可能的 tendency change signal。

后续 schema package 可以共享 evidence-reference patterns，但本 package 不选择具体 Python
model names、modules、storage、routes 或 persistence behavior。

## 未来 Schema 形态指导

后续 schema package 应保持以下设计约束：

- 使用 generic identifiers 和 references，而不是 world-specific entities。
- 在适用处包含 evidence references、source、timestamps 和 review status。
- 对 summaries 和看似 mutable 的 continuity state 显式表达 supersession/versioning。
- 将 proposed updates 与 applied state 分开。
- 将 drift 建模为 reviewable signal data，而不是 behavior。

## Loop 边界

`0.5.3` 已把 bounded read-only memory context 加入 perception。`0.5.4` 不把
relationship、self-summary、reflection 或 drift data 加入该 context。

本 package 不改变：

- loop request fields。
- `ActionIntent`。
- `ActionResult`。
- action adapter behavior。
- params patch semantics。
- memory ranking 或 selection。

## 证据边界

`0.5.4` 只产生 documentation evidence。`0.5.2` 和 `0.5.3` 的当前 code evidence
仍属于那些 package，并会进入 `0.5.5` audit，但本 package 不把它扩展成新 behavior。

## 未来实现说明

如果后续 package 实现 schemas，可能 surface 是 `backend/app/schemas/` 下的 additive
schema models 和 `backend/app/tests/` 下的 focused tests。该 package 必须有自己的
technical design、执行 TDD，并为任何 touched loop/API surface 更新 compatibility evidence。
