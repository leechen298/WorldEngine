# 契约

Status: review complete

implementation_authorized: yes

## 公开概念

本 package 只实现 `0.6.1` generation contract 的 deterministic subset。

- `WorldTemplate`：backend schema，描述 generic template id、version、root
  template cell、entity reference slots、metadata defaults 和 constraints。
- `TemplateCell`：backend schema，描述 generic cell ids、可选 generic labels、
  entity refs、child cells 和 metadata。
- `GenerationDiagnostic`：用于 template validation 和 generation failures 的稳定
  diagnostic code、severity、message、可选 path 和 source context。
- `GenerationMetadata`：generation id、request id、template id/version、
  deterministic seed digest、validation status、diagnostics count，以及后续 package
  所需 lineage fields。
- `TemplateGenerationRequest`：template、seed material 和 constraints 的 request
  wrapper。
- `TemplateGenerationResult`：成功时包含 generated `WorldSpec`、metadata 和
  diagnostics，失败时只包含 diagnostics。

## 允许修改

文档阶段：

- 在 `docs/iterations/v0.6/` 下创建和更新本 package。
- 记录 documentation/contract evaluator evidence。

实现阶段，仅在 `implementation_authorized: yes` 后：

- 创建 `backend/app/schemas/world_generation.py`。
- 创建 `backend/app/core/world_generation.py`。
- 创建 focused tests：
  - `backend/app/tests/test_world_generation_schema.py`
  - `backend/app/tests/test_template_catalog.py`
  - `backend/app/tests/test_deterministic_world_generation.py`
- 更新本 package 的 `review.md` / `review.zh.md`。
- 仅为当前 child state 和 evidence 更新 parent v0.6 status surfaces。

## 禁止修改

- 不修改 `backend/app/schemas/world_cell.py`、`backend/app/schemas/entity.py`、
  `backend/app/core/worldspec_loader.py`、`backend/app/core/runtime_context.py` 或
  `backend/app/core/runtime_engine.py`，除非发现 design gap，并先把 package 退回文档
  review。
- 不修改 `backend/app/api/**`、`backend/app/schemas/api.py`、`frontend/**`、
  `backend/app/agent/**`、persistence/repository modules、archive、params、
  migrations、fixtures、generated result files、external repositories 或
  `backend/worldengine/**`。
- 不添加 public generation API routes、structured-plan compiler behavior、
  AI-assisted plan import、metadata/preview API、regeneration behavior、dashboard UI、
  E2E behavior、external validation readiness、projection readiness、live external
  AI-provider calls、durable persistence 或 migrations。
- 不添加 concrete demo-world names、maps、characters、locations、resources、story
  rules、private validation oracle details、generated seed data 或
  application-specific backend behavior。
- 不声明 generated worlds 的 runnable 能力超过本 package 中的 loader/runtime-context
  compatibility evidence。

## 实现要求

- Generated output 必须通过当前 `WorldSpec` schema 验证，且 `schema_version ==
  "0.2"`。
- 对同一 template、request id、constraints 和 seed material，generation 必须是
  deterministic。
- 不同 seed material 可以改变已评审 deterministic ids/metadata，但必须保持 schema
  validity。
- Diagnostics 必须 deterministic，并包含 stable code、severity、message、可选 JSON
  Pointer-style path 和可选 source context。
- Invalid templates 必须返回 diagnostics，而不是 mutation input 或依赖 hidden state。
- Template inputs 和 generated outputs 必须保持 generic、inspectable。
- Generator 不得调用 external services、读取 environment secrets、用 wall-clock time
  生成 output identity，或持久化 generated data。

## 兼容性要求

- 现有 `WorldSpec`、`WorldCell` 和 `EntityRef` invariant 保持不变。
- 现有 loader error codes 和 JSON Pointer path behavior 保持不变。
- Runtime-context summaries 保持 bounded，不得暴露 raw `WorldSpec` 或 root payload。
- Runtime tick/event behavior 保持不变。
- 现有 API routes 和 envelopes 保持不变。
- 现有 v0.4 Agent Loop 和 v0.5 memory surfaces 保持不变。
- 历史 v0.5 evidence 只作为 handoff context。

## 授权条件

只有满足以下条件后，本 package 才能记录 `implementation_authorized: yes`：

- 所有 package docs 和中文镜像存在。
- `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md` 已完成 review。
- documentation/contract evaluator 报告 PASS，且无 P0/P1、无 blocking unresolved
  P2。
- review evidence 确认本 package 已读取并遵守 `0.6.1`。
- 未来 implementation 的 changed-file scope 限定在本 contract 允许的文件内。
- planned tests 覆盖 deterministic output、invalid template diagnostics、generated
  `WorldSpec` loader compatibility 和相邻 runtime-context compatibility。

## North Star 检查

本 package 将 world generation 推进为 generic engine capability。它不把 repository
变成 demo backend，不存储 concrete world content，并保持 generated worlds 与现有
engine spine 兼容。

## 范围外后续工作

- `0.6.3`：structured generation plan compiler。
- `0.6.4`：AI-assisted plan import。
- `0.6.5`：backend API、validation、metadata 和 preview API。
- `0.6.6`：regeneration and runtime-readiness integration。
- `0.6.7`：dashboard preview and E2E smoke。
- v0.7 external validation readiness。
- v0.8 projection application readiness。
