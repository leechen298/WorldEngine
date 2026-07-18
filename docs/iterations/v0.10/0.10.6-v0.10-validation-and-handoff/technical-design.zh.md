# Technical Design

英文版本：`technical-design.md`。

## Affected Files

- `docs/iterations/v0.10/0.10.6-v0.10-validation-and-handoff/*`
- `README.md` 中列出的 v0.10 parent status/review/plan/handoff docs。
- 仅在 handoff route synchronization 需要时更新 v0.11 parent status docs。

## Design

本包 validation-first，不应需要 runtime 或 frontend implementation changes。主要输出是 documented
validation result 和 status synchronization。

Validation evidence 来自现有 commands 和 direct manifest inspection。如果发现 P1/P2 defect，
必须停止 implementation，直到 defect repair scope 被记录在本 package review 中，并且仍位于
already-approved v0.10 contract 内。

## Manifest Inspection

通过 FastAPI TestClient 或等价 local API path 检查 `/manifest`，并记录：

- `worldengine_version`。
- MVP contract/version fields。
- session surfaces implemented/pass。
- dashboard remaining status。
- checker handoff unsupported items。
- provider readiness caveat。

## Non-Goals

不执行 external Validation Client，不发起 provider live call，不做 dashboard feature work，不实现
v0.11/v0.12，不改 `backend/worldengine/`。
