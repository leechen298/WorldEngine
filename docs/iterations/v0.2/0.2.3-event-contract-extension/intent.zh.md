# Intent

英文版本：`intent.md`。

## Problem

当前 Event schema 通过 `payload` 承载 flexible event-specific data，但没有一个轻量的
structured 位置用来标记某个事件引用的 world、cell、entity、agent、resource、memory record
或 external projection。

后续 recursive-world、agent、memory 和 projection 工作需要把 structured pointers 挂到事件上，
但现在不能强行引入 runtime coupling。

## Intended Outcome

在这个 gate 通过 review 和 approval 后，为 Event contract 增加一个最小 additive EventRef layer：

- `EventRef` 描述 event-local pointer。
- `Event.refs` 默认是 empty list。
- Existing Event construction 和 API response compatibility 保持不变。
- `payload` 保持不变并完全 backward compatible。

## Why EventRef Is Separate From EntityRef

`EntityRef` 属于 WorldSpec 和 WorldCell structure。它描述 schema-level world contents 和后续
loadable world structure。

`EventRef` 属于单个 event。它可以指向未来的 world specs、world cells、entities、agents、
resources、memory records 或 external projections，但现在不 import、不解析这些概念。

把两个概念分开，可以避免 event schema 在 runtime bridge 存在之前就和 recursive-world schemas
耦合。

## Non-Goals

- 本 documentation stage 不实现代码。
- 不改变 Event `payload` semantics。
- 不要求 existing events 必须有 `refs`。
- 不把 EventRef 接入 WorldCell runtime。
- 不 resolve refs，也不 enforce referential integrity。
- 不改变 runtime engine behavior、event log storage、API routes、modules、frontend 或
  `backend/worldengine/`。
- 不实现 WorldSpec loader、concrete demo runtime、agent memory、pseudo-self 或 0.2.4。

## North Star Fit

Event Contract extension 让未来 world、agent、memory 和 projection evidence 更容易结构化，符合
north star。它不会把 WorldEngine 变成 application-specific backend，也不会让 v0.2 越过
recursive-world foundation boundary。
