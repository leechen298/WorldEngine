# 合同

Status: review complete

implementation_authorized: yes

## 公共概念

本 package 定义 `0.6.1` generation contract 中的 structured-plan subset，并以 additive
方式扩展 `0.6.2` deterministic generator surface。

- `GenerationPlan`：normalized、provider-independent data，用于描述 candidate
  `WorldSpec` structure 和 constraints。
- `PlanCell`：一个 world cell 的 plan entry，包含 generic id、optional label、entity
  references、child cells 和 metadata。
- `PlanGenerationRequest`：request wrapper，携带 request id、`GenerationPlan`、optional
  deterministic seed material 和 optional request-level constraints。
- Plan compiler diagnostics：用于 unsupported plan versions、duplicate ids、duplicate
  entity references、invalid bounds、disallowed entity kinds、non-JSON seed/material
  values 和 malformed plan metadata 的 deterministic `GenerationDiagnostic` records。
- Plan generation metadata：additively 扩展现有 generation metadata，使 plan-generated
  output 记录 plan id/version 和 source kind，同时保留 template-generation metadata
  behavior。

## 允许修改

文档阶段：

- 创建和更新 `docs/iterations/v0.6/` 下的本 package。
- 仅为当前 child state 和 evidence 更新 parent v0.6 status surfaces。
- 记录 subagent/evaluator evidence。

实现阶段，仅在 `implementation_authorized: yes` 后：

- 更新 `backend/app/schemas/world_generation.py`。
- 更新 `backend/app/core/world_generation.py`。
- 添加 focused tests：
  - `backend/app/tests/test_generation_plan_schema.py`
  - `backend/app/tests/test_structured_generation_plan_compiler.py`
- 只在验证兼容性需要时更新现有 focused generation tests：
  - `backend/app/tests/test_world_generation_schema.py`
  - `backend/app/tests/test_deterministic_world_generation.py`
- 更新本 package `review.md` / `review.zh.md`。
- 仅为当前 child state 和 evidence 更新 parent v0.6 status surfaces。

如果 implementation 需要新增 core module，而不是扩展
`backend/app/core/world_generation.py`，必须停止并回到 documentation review 后再添加该路径。

## 禁止修改

- 不修改 `backend/app/api/**`、`backend/app/schemas/api.py`、`frontend/**`、
  persistence/repository modules、migrations、fixtures、generated output files、
  external repositories 或 `backend/worldengine/**`。
- 不修改 `backend/app/core/runtime_context.py`、`backend/app/core/runtime_engine.py`、
  `backend/app/core/worldspec_loader.py`、`backend/app/schemas/world_cell.py` 或
  `backend/app/schemas/entity.py`，除非发现 design gap 并先让本 package 回到
  documentation review。
- 不添加 public generation API routes、AI-assisted plan import、live provider calls、
  preview API、regeneration behavior、dashboard UI、E2E behavior、external validation
  readiness、projection readiness、durable persistence 或 migrations。
- 不把 free-form prompt text 当成可执行 generation behavior。
- 不读取 environment secrets，不用 wall-clock/random identity 生成 output，也不持久化
  generated data。
- 不添加 concrete demo-world names、maps、characters、locations、resources、story rules、
  private validation oracle details、generated seed data 或 application-specific backend
  behavior。

## 实现要求

- 对相同 plan、request id、constraints 和 seed material，plan compilation 必须
  deterministic。
- Generated output 必须按当前 `WorldSpec` schema 校验，且 `schema_version == "0.2"`。
- Compiler 必须返回 diagnostics，不得 mutate input 或依赖 hidden state。
- Diagnostics 必须包含 stable code、severity、message、optional JSON Pointer-style
  path 和 source context。
- `0.6.2` 的 strict JSON seed/material canonicalization 必须继续适用于 plan
  compilation。
- Plan-generated output 必须保持 generic 和 inspectable。
- `0.6.2` 的 template-generation behavior 必须保持兼容。

## 兼容性要求

- 现有 `WorldSpec`、`WorldCell` 和 `EntityRef` invariants 保持不变。
- 现有 loader error codes 和 JSON Pointer path behavior 保持不变。
- 现有 runtime-context summaries 保持 bounded 且不变。
- Runtime tick/event behavior 保持不变。
- 现有 API routes 和 envelopes 保持不变。
- 现有 v0.4 Agent Loop 与 v0.5 memory surfaces 保持不变。
- Historical v0.5 evidence 只作为 handoff context。

## 授权标准

只有满足以下条件后，本 package 才能记录 `implementation_authorized: yes`：

- 所有 package docs 和中文镜像存在。
- `contract.md`、`technical-design.md`、`test-plan.md` 和 `plan.md` 已 review。
- documentation/contract evaluator 报告 PASS，无 P0/P1 和 blocking unresolved P2。
- review evidence 确认本 package 已阅读并遵循 `0.6.1` 与 `0.6.2`。
- future implementation changed-file scope 限于本 contract 的 allowed files。
- planned tests 覆盖 valid plan compilation、invalid diagnostics、duplicate ids/refs、
  constraint violations、unsupported plan version、non-JSON seed/material、no input
  mutation、loader compatibility 和 template generator compatibility。

## 北极星检查

本 package 推进 generic world generation 作为 structured engine capability。它不把
WorldEngine 变成 demo backend，也不添加 application-specific generation behavior。

## 范围外后续

- `0.6.4`：AI-assisted plan import。
- `0.6.5`：backend API、validation、metadata 和 preview API。
- `0.6.6`：regeneration 和 runtime-readiness integration。
- `0.6.7`：dashboard preview 和 E2E smoke。
- v0.7 external validation readiness。
- v0.8 projection application readiness。
