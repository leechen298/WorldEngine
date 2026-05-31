# 技术设计

Status: review complete

## 设计边界

`0.6.3` 扩展现有 generation module，不引入 public API 或 runtime pathway。Compiler
接收 structured plan data，validate 后返回与 `0.6.2` 相同模式的 generation result。

本设计不包含 route、frontend、persistence、runtime tick、Agent/memory、fixture 或 legacy
`backend/worldengine/` surface。

## 计划 Schema Additions

`backend/app/schemas/world_generation.py` 可以添加：

- `PlanCell`：recursive structured cell plan，包含 generic `id`、optional
  `label`、`entity_refs`、`child_cells` 和 `metadata`。
- `GenerationPlan`：plan `id`、`version`、root `PlanCell`、optional metadata 和
  constraints。
- `PlanGenerationRequest`：request id、plan、optional seed material 和 request-level
  constraints。
- additive metadata fields，例如 `source_kind`、`plan_id` 和 `plan_version`，同时保留当前
  template-generation behavior。

Implementation 不得改变 `WorldSpec`、`WorldCell` 或 `EntityRef`。

## 计划 Core Additions

`backend/app/core/world_generation.py` 可以添加：

- `validate_generation_plan(plan, request_constraints=None)`。
- `generate_worldspec_from_plan(request)`。
- 与 template generation 共享或并行使用 deterministic digest 与 JSON canonicalization
  behavior 的 private helpers。

Compiler 把 `PlanCell` 映射为 `WorldCell`，不执行 hidden rules。它应复用或平行实现
`0.6.2` diagnostics，覆盖 duplicate cell ids、duplicate entity refs、child-count
bounds、entity-kind allowlists、unsupported versions 和 unsupported seed/material values。

## 确定性

Seed digest 必须包含 request id、normalized plan data、request constraints 和 seed
material。Unsupported non-JSON values、non-finite floats、tuples、sets、objects 或
non-string dict keys 必须以 stable diagnostics 失败，不能被 coercion 成 output。

## 兼容性

Valid compiler output 必须通过当前 `WorldSpec` schema、loader 和 runtime-context bridge
tests。现有 template generation 必须保持 deterministic 和 compatible。

## 失败模型

Invalid plans 返回 failed generation result，包含 diagnostics 且不含 `WorldSpec`。
Diagnostics 使用 stable machine-readable codes 和指向 plan input 的 JSON Pointer-style
paths。

## 范围外

- AI-assisted import 或 provider behavior。
- Prompt execution 或 free-form prose parsing。
- API、frontend、E2E、persistence、migrations、external validation、projection、
  runtime tick/event、Agent/memory 和 regeneration behavior。
