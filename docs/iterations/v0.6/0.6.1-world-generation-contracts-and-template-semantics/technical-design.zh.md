# 技术设计

Status: review complete

## 当前状态

WorldEngine 当前已有 generic `WorldSpec` schema 和 loader/runtime bridge，但还没有
world-generation implementation。相关当前 surface 包括：

- `backend/app/schemas/world_cell.py`：`WorldSpec` 包含 `schema_version`、`id`、可
  选 `label`、`root` 和 metadata；`WorldCell` 包含 `id`、可选 `label`、`kind`、
  `entity_refs`、`child_cells` 和 metadata。
- `backend/app/schemas/entity.py`：`EntityRef` 包含非空 `id` 和 `kind`、可选
  `label` 以及 metadata。
- `backend/app/core/worldspec_loader.py`：`load_worldspec` 接受 mapping 或 JSON
  string/bytes，通过 `WorldSpec` 验证，并返回 success 或 loader errors。当前正常
  failure code 包括 `unsupported_input`、`parse_error` 和
  `schema_validation_error`，schema path 使用 JSON Pointer-style location。
- `backend/app/core/runtime_context.py`：`build_runtime_context` 从 loaded
  `WorldSpec` 派生 bounded runtime context；summary 不得暴露 raw `WorldSpec` 或
  root payload。
- `backend/app/core/runtime_engine.py`：runtime state、tick behavior、event
  emission、params、callbacks 和可选 runtime context 都是 compatibility-sensitive。
- `backend/app/schemas/api.py` 和 `backend/app/api/app_factory.py`：API envelope
  和 exception handling 对成功响应使用 `code`、`data`、`msg`，对错误响应使用
  `code`、`msg` 和可选 `data`。现有 HTTP-to-application error mapping 包括
  400 到 10、401 到 20、403 到 21、404 到 24、409 到 29、422 到 30、500 到 50。

`0.6.1` 不修改这些文件。

## 文档结构

本 package 新增一个完整的 documentation-only child package：

```text
docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/
├── README.md
├── README.zh.md
├── intent.md
├── intent.zh.md
├── contract.md
├── contract.zh.md
├── technical-design.md
├── technical-design.zh.md
├── test-plan.md
├── test-plan.zh.md
├── plan.md
├── plan.zh.md
├── review.md
└── review.zh.md
```

## 概念流程

计划中的 generation contract 使用以下流程：

```text
WorldGenerationRequest
  -> WorldTemplate and constraints, or validated GenerationPlan
  -> GeneratedWorldSpec with GenerationMetadata and diagnostics
  -> GenerationPreview for bounded inspection
  -> later loader/runtime-readiness checks before runtime use
```

对 AI-assisted generation，流程被刻意拆开：

```text
external/user/tool/AI output
  -> untrusted structured GenerationPlan import
  -> validation and diagnostics
  -> later compilation into WorldSpec only after a reviewed package authorizes it
```

Live provider invocation、provider credential、prompt storage 和 hidden model
side effect 都不属于本 package。

## 计划字段语义

后续 additive schema 应保留以下语义：

| Concept | 必需语义分组 |
| --- | --- |
| `WorldGenerationRequest` | request identity、单一主要 input path、constraints、provenance、适用时的 deterministic seed material |
| `WorldTemplate` | template identity/version、generic cell patterns、entity-ref slots、metadata defaults、validation constraints |
| `GenerationPlan` | root intent、child-cell entries、entity-ref entries、metadata entries、constraints、provenance |
| `GeneratedWorldSpec` | candidate `WorldSpec`、metadata、diagnostics、validation state |
| `GenerationMetadata` | request/generation identity、template or plan lineage、seed lineage、validation status、diagnostics、timestamps/source clock |
| `GenerationPreview` | ids、counts、metadata keys、validation status、diagnostics 的 bounded summary |
| `RegenerationRequest` | source generation/request lineage、changed constraints、compatibility expectations |
| diagnostics | stable code、message、optional path、severity、source context |

这些是语义要求，不是本 package 中的实现 schema。

## 兼容性策略

generated output contract 以现有 loader behavior 为锚点：

- 后续 generated `WorldSpec` value 必须通过 `load_worldspec` 验证。
- loader parse 和 schema validation error 仍是 invalid generated spec 的权威错误，
  包括现有 error code 和 JSON Pointer-style path。
- runtime context 仍通过 `build_runtime_context` 派生；除非后续已评审 child 明确定义
  additive summary，否则 generation metadata 不得泄露到 runtime context。
- Runtime tick、event emission、params、archive、Agent Loop 和 memory behavior 在
  后续 package 授权任何 additive integration 前保持不变。Tick event 和 runtime
  state 不得暴露 raw generated spec 或 root payload。
- 未来 generation API response 必须使用现有 API envelope 和 error shape。

## 受影响范围

受影响文件仅限本 package 目录。本 package 不影响 runtime、schema、service、API、
frontend、backend test、fixture、migration、generated output、external
repository 或 legacy code。

## 防漂移规则

- 将 generation contract 视为 engine contract，而不是 demo-world authoring。
- 模板必须保持 generic；只有不会被误认为具体 world content 时，才允许使用
  placeholder id。
- 将 AI-assisted generation 视为 structured plan import and validation，而不是 live
  provider behavior。
- 不从 structural validity 推导 generated-world quality claim。
- 不把历史 v0.5 evidence 提升为当前 v0.6 pass evidence。
- 在 implementation-bearing child 记录自己的 reviewed authorization 前，保持
  implementation authorization closed。

## 风险

- 风险：后续把 contract term 实现成具体 fixture data。
  缓解：禁止具体内容，并要求 focused scope guard。
- 风险：generated output 通过 shape check 后被夸大为 runnable 或 high quality。
  缓解：区分 structural validity、runtime readiness、preview 和 quality claim。
- 风险：AI-assisted generation 被当成 live provider integration。
  缓解：先要求 provider-independent structured plan import。
- 风险：后续 API work 偏离现有 envelope。
  缓解：明确 `ApiResponse` / `ApiErrorResponse` 兼容性。
