# 0.9.5 Bounded Runtime Control And Run Budget

英文原文：`README.md`。

Status：implementation complete / focused verification passed
Type：mixed implementation package

## 目标

为当前 in-memory WorldEngine execution 增加 bounded runtime control，使 caller 可以运行有限
tick 数或有限 world-time duration、pause、resume，并获得带明确 guard limits 的 public run
summary。

## 范围

本包可在 `backend/app/` active backend runtime path 中扩展：

- bounded run request and response schemas。
- deterministic in-memory runtime helper behavior。
- bounded run、pause 和 resume API endpoints。
- maximum tick 和 world-time duration guards。
- public provider-call 和 cost guard counters；由于本包不授权 provider calls，这些 counters
  必须保持为零。
- focused backend and API tests。

它必须保持既有 `/runtime/step` behavior compatible，并且不得引入 durable scheduling、
background workers、deployment infrastructure、frontend UI、checker execution、external
validation 或 Validation Client changes。

## 交付物

- Public runtime-control schemas。
- Active runtime code path 中的 bounded run helper。
- Bounded run、pause 和 resume runtime API surface。
- Public run summary evidence。
- Focused tests，覆盖 tick limits、duration limits、pause/resume、max guards、
  provider/cost counters，以及与 single-step runtime behavior 的兼容性。

## 当前授权

Documentation/contract review 已通过。Implementation 仅授权本包记录的 scoped active-backend
in-memory runtime-control work。

Provider live calls、generated-result creation、checker execution、external validation、
Validation Client changes、durable scheduling 或 frontend UI work 仍未授权。

## 最终评估状态

已在 scoped active-backend in-memory runtime-control work 范围内完成 implementation。
Focused、related runtime 和 backend regression verification 已通过。只读 implementation
复审报告没有未解决 P1/P2/P3 findings。

Provider live calls、generated-result creation、checker execution、external validation、
Validation Client changes、durable scheduling、frontend UI、event legality、Agent
continuity 和 `backend/worldengine/` changes 仍未授权，也未声明通过。
