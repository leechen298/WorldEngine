# Intent

英文版本：`intent.md`。

## Background

0.2.2 通过新增 `EntityRef`、`WorldCell` 和 `WorldSpec`，定义了 recursive worlds 的结构化
schema language。0.2.3 通过 `EventRef` 和 `Event.refs` 增加了 event-local reference layer。

0.2.4 现在应提供第一份小型 reference `WorldSpec` fixture，让 schema language 有一个稳定、
可 review 的 data example 和未来 test input。这个 fixture 是 schema-focused reference data
fixture，不是 runtime world，也不是 application implementation。

## User Outcome

未来维护者应该能够查看一个小型、确定性的 world spec，理解 valid recursive `WorldSpec` 的
预期形状，而不需要启动 runtime engine、添加 loader 或解释 application behavior。

## Engineering Outcome

通过 review approval 后，implementation 应新增：

- 单个 JSON fixture：`backend/data/world_specs/historical concrete fixture path`。
- 聚焦的 Python test：`backend/app/tests/test_worldspec_fixture.py`。

该 test 应使用 `json` 和 `pathlib` 读取 JSON，通过 `WorldSpec.model_validate(...)` validate，
并通过现有 schema models 验证 recursive `WorldCell` / `EntityRef`。

## Why Now

- 0.2.2 创建了最小 schema structure。
- 0.2.3 增加了 event-local refs，但没有连接 runtime behavior。
- 0.2.4 可以用稳定 fixture 验证 schema language。
- v0.3 后续可以决定如何把 validated `WorldSpec` load into runtime。
- v0.7 或更晚 roadmap work 可以把 historical-concrete-fixture ideas 发展为完整 historical concrete fixture direction 或
  product-facing projection。

## Non-Goals

- 本 documentation stage 不实现代码。
- 暂不创建 JSON fixture 或 fixture test。
- 不实现 production WorldSpec loader。
- 不实现 runtime bridge。
- 不让 historical concrete fixture 在 0.2.4 变成 runnable。
- 不增加 concrete demo runtime、application-specific backend logic、world generation、agent memory、
  pseudo-self 或 frontend behavior。
