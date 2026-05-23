# Contract

Status: review complete

英文版本：`contract.md`。

## Public Concepts

- v0.1 current implementation map。
- active backend path。
- active dashboard path。
- current API reference。
- current test map。

## Compatibility Constraints

- 不改变 runtime behavior。
- 不改变 API behavior。
- 不改变 frontend behavior。
- 不改变 tests。
- v0.1 必须继续明确不是 recursive world engine implementation。

## Allowed Changes

- 新增 `docs/current-implementation.md`。
- 新增 `docs/backend-implementation.md`。
- 新增 `docs/frontend-implementation.md`。
- 新增 `docs/api-reference-v0.1.md`。
- 新增 `docs/testing/v0.1-test-map.md`。
- 更新 `README.md`。
- 更新 `backend/README.md`。
- 更新 `frontend/README.md`。
- 更新 v0.1 release/iteration docs links。

## Forbidden Changes

- 不修改 backend code。
- 不修改 frontend code。
- 不修改 tests。
- 不实现 WorldCell、WorldSpec、world generation、Agent memory 或 game surface。
- 不把 `backend/worldengine/` 重新写成 active path。

## North Star Check

- Current implementation docs 必须支持 north star，而不是重定义 north star。
- Docs 必须明确 v0.1 还没有 recursive world、world generation 或 Agent pseudo-self。
- Docs 必须保留 village surface 只是 future surface/reference world 的定位。

## Out-of-Scope Follow-ups

- WorldCell / WorldSpec implementation belongs to v0.2。
- Event contract extension belongs to v0.2。
- Agent memory/self-continuity belongs to later milestones。
