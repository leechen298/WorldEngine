# 契约

Status: review complete

implementation_authorized: no

## 公开概念

`0.6.1` 只定义名称与语义。这些概念是后续 additive schema 和 service 的计划契约
术语；本 package 不创建 runtime class、Pydantic model、route、frontend
component、test 或 generated data file。

### `WorldGenerationRequest`

一个可评审的请求，用于生成候选 `WorldSpec`。

后续实现必须遵守的语义：

- 携带稳定 request id 或 caller-supplied correlation id。
- 只选择一个主要 generation input path：
  - `WorldTemplate` 加显式 constraints，或
  - 已验证的 `GenerationPlan`。
- 可以包含 generic constraints，例如目标 cell count 边界、允许的 entity reference
  kind、metadata tag 和 deterministic seed material。
- 记录 request source 的 provenance，但不存储私有 external validation 细节。
- 不包含具体 demo-world 名称、story content、私有 oracle data 或
  application-specific behavior。

### `WorldTemplate`

一个 generic、可复用的 generation shape，用来约束未来 deterministic generator 如何
创建 `WorldSpec` 数据。

后续实现必须遵守的语义：

- 拥有 template id 和 version。
- 声明 generic cell pattern、entity reference slot、metadata default 和 validation
  constraint。
- 只有在保持 generic 且不编码具体 external world 时，才可以使用 placeholder id 和
  label。
- 不包含具体地图、角色、地点、资源、故事规则、seed data、validation oracle 细节
  或 UI-specific behavior。
- 在相同 request constraints 和 seed material 下必须 deterministic。

### `GenerationPlan`

一个 normalized structured plan，在编译为 `WorldSpec` 前必须可以被验证。

后续实现必须遵守的语义：

- 用数据描述目标 `WorldSpec` 结构，而不是可执行代码。
- 包含 root cell intent、child-cell plan entry、entity reference plan entry、
  metadata entry 和 constraints。
- provider-independent。plan 可以由用户、工具或 AI system 产生，但导入验证必须
  把它视为不可信结构化数据。
- 当无法产生合法 `WorldSpec` 数据时，必须以 diagnostics 失败。
- 后续 package 中不得绕过 `load_worldspec` 或 runtime-readiness check。

### `GeneratedWorldSpec`

由 `WorldSpec` 数据和 generation metadata 组成的候选 generated output。

后续实现必须遵守的语义：

- generated `WorldSpec` 数据必须保留当前 `WorldSpec` invariant：
  `schema_version` 为 `"0.2"`，`id` 非空，`root` 存在，root 和 child cell id 非空，
  `kind` 保持 `"world"`，`entity_refs` 中的 `id` 与 `kind` 非空，metadata 保持
  additive。
- 只有在负责这些检查的 package 中通过已评审的 loader 和 runtime-readiness check
  后，generated output 才能被视为 runnable。
- generated output 必须保留可检查的 diagnostics 和 provenance。
- generation provenance 可以通过 wrapper metadata、generation metadata 或已评审的
  source label 承载，但不得改变 `LoadedWorldSpec` 字段，也不得要求 loader 在本
  package 中接受新的 input type。
- 本 package 不把 generated output 写成 durable fixture 或 seed data。

### `GenerationMetadata`

描述 generation 如何发生的可检查 evidence。

后续实现必须遵守的语义：

- 记录 request id、generation id、template id/version 或 plan id/version、适用时
  的 deterministic seed material 或 seed digest、validation status、diagnostics，
  以及 generation timestamp 或 source clock semantics。
- 为 AI-assisted plan import 记录 provider-independent provenance，但不要求 live
  provider call。
- 当 generation 修订先前 generated output 时，记录来自 `RegenerationRequest` 的
  lineage。
- 不存储私有 prompt、私有 validation oracle internals、secret、credential 或
  external application data。

### `GenerationPreview`

在 runtime use 前展示 generated candidate 的有界、可检查摘要。

后续实现必须遵守的语义：

- 摘要包含 id、schema version、root cell id/kind、child-cell count、entity-ref
  count、metadata key、validation status 和 diagnostics。
- 只有在不编码具体 demo-world 内容时，才可以包含 generic label 或 placeholder
  label 的摘录。
- 它不是 runtime state snapshot，不是 E2E pass claim，也不是 quality verdict。

### `RegenerationRequest`

通过显式 lineage 和 constraints 修订先前 generation 的请求。

后续实现必须遵守的语义：

- 引用 source generation id 或 request id。
- 声明哪些 constraints 已改变，以及哪些兼容性预期必须保持稳定。
- 在 `GenerationMetadata` 中记录 lineage。
- 除非后续已评审 child 明确授权，否则它不意味着 durable persistence、migration 或
  versioned storage。

### 生成诊断

用于解释 parse、schema、constraint、template、plan、validation 和 compatibility
failure 的结构化信息。

后续实现必须遵守的语义：

- diagnostics 必须包含稳定 machine-readable code、human-readable message、可选
  path、severity，以及可用时的 source context。
- diagnostics 必须与现有 loader-style failure reporting 对齐：
  `unsupported_input`、`parse_error` 和 `schema_validation_error` 保持为现有 loader
  code，schema location 使用 JSON Pointer-style path，例如 `/schema_version` 或
  `/root/id`。
- 未来 API 暴露 generation diagnostics 时，必须符合当前 error envelope：HTTP status
  映射到 numeric `code`，`msg` 保持 string，可选 `data` 可以承载 `errors`，并在
  已评审时承载 `metrics`。
- diagnostics 是 evidence，不是隐藏控制流。

## 兼容性要求

- 本 package 不改变 `WorldSpec`、`WorldCell` 和 `EntityRef`。
- 除非后续已评审 child 授权 additive schema extension，未来 generated
  `WorldSpec` 数据必须验证通过当前 `WorldSpec` schema。
- 本 package 不改变 `load_worldspec`、`LoadedWorldSpec`、
  `WorldSpecLoaderResult` 和 `WorldSpecLoaderError` 语义。正常 parse 与 schema
  failure 返回 loader result errors，而不是抛出异常。
- 本 package 不改变 `RuntimeContext`、`RuntimeContextSummary`、
  `build_runtime_context` 和 `summarize_runtime_context`。runtime context 保持有界，
  只包含 ids、schema version、root type、source fields 和 metadata summary；不得
  泄露 raw `WorldSpec` 或 root payload。
- 本 package 不改变 `RuntimeEngine.get_runtime_context`、`RuntimeEngine.step`、
  tick/time behavior、event emission 和 params behavior。除非后续已评审 child 明确
  授权 additive evidence surface，否则 runtime step event 不得包含 raw generated
  spec 或 root payload。
- v0.4 Agent Loop schema 和 `POST /world/agent/loop/step` 保持不变。
- v0.5 working-memory 与 episodic-memory context surface 保持不变。
- 现有 API envelope 和 error shape 保持不变：成功响应使用 `code`、`data` 和
  `msg`；错误响应使用 `code`、`msg` 和可选 `data`。
- 现有 route、archive behavior、event route、params route、frontend behavior、
  fixture boundary、migration 和 legacy `backend/worldengine/` behavior 保持不变。
- 历史 v0.5 evidence 只作为 handoff context，不算作当前 v0.6 pass evidence。

## 允许修改

- 创建或更新本 package 目录下的文档。
- 用 prose 定义 planned public concept semantics 和字段级含义。
- 定义 documentation-only 的 compatibility、scope、evidence 和 authorization
  criteria。
- 记录 documentation check、subagent/evaluator evidence、finding 和 review status。

## 禁止修改

- 不修改 runtime、schema、service、API、frontend、backend test、fixture、
  migration、generated result、external repository 或 `backend/worldengine/`
  implementation file。
- 不创建计划中的未来实现路径，例如
  `backend/app/schemas/world_generation.py`、
  `backend/app/world/generation.py`、
  `backend/app/api/routes/world_generation.py`、
  `backend/app/tests/test_world_generation_*.py` 或
  `frontend/src/components/GenerationPanel.vue`。
- 不定义具体 generated world example，generic placeholder id 除外。
- 不要求 live external AI-provider call 或 provider-specific secret。
- 不引入 external validation readiness、projection readiness、durable
  persistence、migration、release status 或 product-readiness claim。
- 不为本 package 标记 `implementation_authorized: yes`。

## `0.6.2` 的授权条件

`0.6.2-template-catalog-and-deterministic-generator-core` 只有在自己的 package 文
档存在，且 review evidence 确认以下条件后，才可以记录
`implementation_authorized: yes`：

- 已读取本已评审 `0.6.1` contract，并保持 generated content generic。
- 明确指出允许创建或修改哪些 backend schema/service/test 文件。
- 将实现范围限制在 deterministic template catalog 与 template-to-`WorldSpec`
  generator core。
- 不加入 structured plan compilation、AI-assisted plan import、backend API route、
  frontend preview UI、regeneration、durable persistence、migration、external
  validation readiness 或 projection readiness。
- 定义 focused tests，证明 deterministic output、invalid template diagnostics 和
  generated `WorldSpec` loader compatibility。
- 为 implementation 触及的 loader 和 runtime-context surface 定义相邻兼容性回归
  evidence，包括保留 loader error codes、JSON Pointer paths、bounded runtime
  context summaries 和 existing API envelopes。
- 包含 documentation/contract evaluator report，且无未解决 P1/P2 finding。

## North Star 检查

本 contract 通过把 world generation 定义为 generic、inspectable 的 engine
capability 来支持 north star。它让 external application 继续作为 consumer，把具
体 world content 留在 core repository 之外，并保留后续 generated world 必须接入的
event/runtime/memory spine。

## 范围外后续工作

- `0.6.2`：deterministic template catalog and generator core。
- `0.6.3`：structured generation plan compiler。
- `0.6.4`：provider-independent AI-assisted plan import。
- `0.6.5`：generation validation, metadata, and preview API。
- `0.6.6`：regeneration and runtime-readiness integration。
- `0.6.7`：dashboard generation preview and E2E smoke。
- `0.6.8`：evidence and compatibility audit。
- `0.6.9`：release-candidate bundle。
- `0.6.10`：final closeout。
- v0.7 external validation readiness。
- v0.8 projection application readiness。
