# WorldEngine V1 Design Note

## Scope

WorldEngine V1 is an experimental monorepo scaffold with:

- FastAPI backend for runtime orchestration endpoints
- Vue 3 + TypeScript frontend for dashboard interaction
- Placeholder domain and infrastructure modules for future expansion

## Backend Architecture (V1)

- `api`: app factory and HTTP route layer
- `core`: runtime loop primitives (clock, scheduler, event bus, runtime engine)
- `substrate`: runtime context abstractions
- `schemas`: shared Pydantic models
- `world`: world domain service boundary
- `agent`: agent domain service boundary
- `infra`: repository ports and adapter implementations (SQLite placeholder)

## Runtime Loop (High-Level)

1. Read current time/tick context from `core.clock` and `substrate.runtime`.
2. Load current world and agent snapshots via repository ports.
3. Execute scheduled tasks and publish events through `core.event_bus`.
4. Advance runtime state in `core.runtime_engine`.
5. Expose current status/state via API endpoints.
