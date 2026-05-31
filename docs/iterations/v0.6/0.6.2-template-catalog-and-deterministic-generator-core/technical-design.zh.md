# 技术设计

Status: review complete

## 当前状态

当前 backend 已有 `WorldSpec`、`WorldCell`、`EntityRef`、`load_worldspec`、
`build_runtime_context`，以及 schema、loader、runtime-context compatibility 的 backend
tests。当前没有 generation schema、template catalog 或 deterministic generator
implementation。

## 计划实现

授权后新增两个 backend modules：

```text
backend/app/schemas/world_generation.py
backend/app/core/world_generation.py
```

`backend/app/schemas/world_generation.py` 负责 data contracts：

- `TemplateCell`
- `WorldTemplate`
- `TemplateGenerationRequest`
- `GenerationDiagnostic`
- `GenerationMetadata`
- `TemplateGenerationResult`

`backend/app/core/world_generation.py` 负责 deterministic behavior：

- seed normalization 和 seed digest generation。
- template validation 和 diagnostics。
- template cells 与 entity refs 的 stable traversal。
- deterministic `WorldSpec` construction。
- 无 persistence、无 wall-clock output identity、无 external calls。

## 数据流

```text
TemplateGenerationRequest
  -> validate template shape and constraints
  -> diagnostics on failure
  -> deterministic seed digest
  -> WorldSpec(schema_version="0.2")
  -> TemplateGenerationResult(worldspec, metadata, diagnostics)
  -> load_worldspec in tests for compatibility evidence
  -> build_runtime_context in tests for bounded bridge evidence
```

## 计划 schema 语义

- Template ids、versions、cell ids、diagnostic codes、severities 和 messages 必须非空。
- Template cells 是 recursive 且 generic 的。
- Entity refs 复用现有 `EntityRef` 语义。
- Generation metadata 记录 request id、generation id、template id/version、seed
  digest、validation status、diagnostics count 和 lineage fields。
- Generation result 只有在 validation status 为 passed 时才包含 `WorldSpec`。

## 确定性策略

- 通过 sorted keys 的 stable JSON serialization normalize seed material 和 template
  data。
- 使用 deterministic digest 生成 generation id、generated spec id 和 seed metadata。
- 保留来自 template cells 和 entity refs 的 stable ordering。
- 不 mutate template inputs。
- 不使用 random、wall-clock time、process-global counters、filesystem state、
  environment secrets 或 network calls。

## Diagnostics 策略

Diagnostics 是 data，不是 exceptions。计划 codes 包括：

- `duplicate_cell_id`
- `duplicate_entity_ref`
- `invalid_template_bounds`
- `entity_kind_not_allowed`
- `empty_template`
- `schema_validation_error`

Diagnostics 尽可能使用 JSON Pointer-style paths，例如 `/root/child_cells/0/id` 或
`/root/entity_refs/0/kind`。

## 受影响文件

授权后允许：

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/tests/test_world_generation_schema.py`
- `backend/app/tests/test_template_catalog.py`
- `backend/app/tests/test_deterministic_world_generation.py`
- 本 package 的 `review.md` 和 `review.zh.md`
- 仅为当前 child state 更新 parent v0.6 status files

不受影响：

- `backend/app/api/**`
- `backend/app/schemas/api.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/entity.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/agent/**`
- `backend/app/world/**`，本 package 不计划修改这里
- `frontend/**`
- migrations、fixtures、generated outputs、external repositories
- `backend/worldengine/**`

## 兼容性策略

测试必须证明：

- generated output 能作为当前 `WorldSpec` 验证通过。
- loader success 仍是带现有 source semantics 的 `WorldSpecLoaderResult`。
- invalid generated mappings 仍通过现有 loader diagnostics 失败。
- runtime-context summary 保持 bounded，且不暴露 raw `WorldSpec` 或 root payload。
- 现有 schema、loader 和 runtime-context tests 仍通过。

## 风险

- 风险：templates 变成 concrete world fixtures。
  缓解：保持 examples generic，并添加 content guard tests。
- 风险：deterministic output 意外依赖 Python object ordering 或 mutable inputs。
  缓解：stable JSON digest 和 no input mutation tests。
- 风险：implementation 漂移到 API 或 runtime behavior。
  缓解：changed-file scope guard 和显式 forbidden surfaces。
- 风险：generated structural validity 被夸大为 product readiness。
  缓解：review 只记录 schema/loader/runtime-context compatibility，不记录 release、
  runtime、E2E 或 quality readiness。
