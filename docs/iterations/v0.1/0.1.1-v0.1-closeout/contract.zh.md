# Contract

Status: complete

英文版本：`contract.md`。

## Public Concepts

- v0.1 scaffold baseline。
- v0.1 release closeout。
- v0.1 test evidence。
- v0.2 next-work boundary。

## Compatibility Constraints

- 不改变 runtime behavior。
- 不改变 API response shape。
- 不改变 frontend behavior。
- 不改变 test expectations。
- v0.1 不能被描述成已经实现 recursive world runtime。

## Allowed Changes

- 更新 `README.md`。
- 新增或更新 `docs/releases/v0.1.md`。
- 新增 test evidence under `docs/testing/results/`。
- 新增 v0.1 iteration package docs。

## Forbidden Changes

- 不修改 backend code。
- 不修改 frontend code。
- 不新增 tests。
- 不实现 v0.2 schemas。
- 不创建 game runtime。

## North Star Check

- Closeout 必须明确 v0.1 只是 scaffold baseline。
- Closeout 必须保护 v0.2 的 recursive world foundation 方向。
- Closeout 不能把 heartbeat/counter scaffold 写成 complete world simulation。

## Out-of-Scope Follow-ups

- WorldCell / WorldSpec schema belongs to v0.2。
- Agent pseudo-self belongs to later milestones。
- Reference village world belongs to later milestones。
