# Intent

英文版本：`intent.md`。

## Problem

WorldEngine 已有 v0.1 runtime/event scaffold 和 v0.2 方向文档，但还没有经过 review
的 recursive world structure schema contract。没有这个 contract，后续工作容易过早跳到
runtime migration、demo-specific behavior、loader design 或 agent memory，而不是先稳定
最小 world structure。

## Goal

创建 implementation-ready documentation gate，用于后续添加 additive Pydantic schemas：

- `EntityRef`：轻量 reference 或 declaration entry。
- `WorldCell`：最小 recursive world unit。
- `WorldSpec`：recursive world 的最小顶层容器。

成功状态是：下一阶段可以按照已 review 的计划添加这些 schemas 和 focused tests，同时不改变
v0.1 runtime behavior。

## Non-goals

- 本 documentation stage 不实现代码。
- 不迁移 `RuntimeEngine` 到 `WorldCell`。
- 不实现 WorldSpec loader。
- 不添加 reference WorldSpec fixture。
- 不实现 concrete demo runtime 或 application-specific logic。
- 不修改 dashboard 或 frontend。
- 不实现 world generation。
- 不实现 agent memory、agent inner-world 或 pseudo-self continuity。
- 不修改 `backend/worldengine/`。
- 不启动 0.2.3 event contract work。

## Why Now

0.2.1 已建立 project direction 和 iteration governance。0.2.2 是 v0.2 的第一个 code
package，应该先定义 recursive world structure，再进入 event extension、reference fixture、
loader work 或 runtime bridge。

## North Star Alignment

本包通过定义 world 如何包含 child worlds 来支持 recursive world structures。它保持 first
concrete demo surface 只是未来 projection，避免把 WorldEngine 收窄成 demo-specific backend。
