# WorldEngine V1 Design Note

英文版本：`v1-design.md`。

## Scope

WorldEngine V1 是 experimental monorepo scaffold，包含：

- 用于 runtime orchestration endpoints 的 FastAPI backend。
- 用于 dashboard interaction 的 Vue 3 + TypeScript frontend。
- 面向 future expansion 的 placeholder domain 和 infrastructure modules。

## Backend Architecture (V1)

- `api`: app factory 和 HTTP route layer。
- `core`: runtime loop primitives（clock、scheduler、event bus、runtime engine）。
- `substrate`: runtime context abstractions。
- `schemas`: shared Pydantic models。
- `world`: world domain service boundary。
- `agent`: agent domain service boundary。
- `infra`: repository ports 和 adapter implementations（SQLite placeholder）。

## Runtime Loop (High-Level)

1. 从 `core.clock` 和 `substrate.runtime` 读取 current time/tick context。
2. 通过 repository ports 加载 current world 和 agent snapshots。
3. Execute scheduled tasks，并通过 `core.event_bus` publish events。
4. 在 `core.runtime_engine` 中 advance runtime state。
5. 通过 API endpoints 暴露 current status/state。
