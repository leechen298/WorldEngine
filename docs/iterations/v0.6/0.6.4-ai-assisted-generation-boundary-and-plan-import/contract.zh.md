# 合同

Status: review complete

implementation_authorized: yes

## 公共概念

- `PlanImportSource`：provider-independent provenance，描述 imported structured plan 的来源。
  可记录 source kind、source id、provider label、model label、redaction flag 和 generic
  metadata。
- `PlanImportRequest`：untrusted import envelope，携带 import id、`GenerationPlan`、
  `PlanImportSource` 和 optional metadata。
- `PlanImportResult`：import validation result，包含 accepted `GenerationPlan` 和 redacted
  provenance，或只包含 diagnostics 而不含 accepted plan。
- Import diagnostics：针对 malformed provenance、non-JSON import metadata、rejected
  prompt fields，以及 `0.6.3` invalid plan diagnostics 的 stable `GenerationDiagnostic`
  records。

## 允许修改

文档阶段：

- 创建和更新 `docs/iterations/v0.6/` 下的本 package。
- 仅为当前 child state 和 evidence 更新 parent v0.6 status surfaces。
- 记录 subagent/evaluator evidence。

实现阶段，仅在 `implementation_authorized: yes` 后：

- 更新 `backend/app/schemas/world_generation.py`。
- 更新 `backend/app/core/world_generation.py`。
- 添加 focused tests：
  - `backend/app/tests/test_plan_import_schema.py`
  - `backend/app/tests/test_plan_import_boundary.py`
- 只在需要时更新 existing focused plan/compiler tests：
  - `backend/app/tests/test_generation_plan_schema.py`
  - `backend/app/tests/test_structured_generation_plan_compiler.py`
- 更新本 package `review.md` / `review.zh.md`。
- 仅为当前 child state 和 evidence 更新 parent v0.6 status surfaces。

如果 implementation 需要新增 module 或 API route，必须停止并回到 documentation review 后再添加。

## 禁止修改

- 不修改 `backend/app/api/**`、`backend/app/schemas/api.py`、`frontend/**`、
  persistence/repository modules、migrations、fixtures、generated output files、
  external repositories 或 `backend/worldengine/**`。
- 不修改 runtime、Agent/memory、archive/params、loader、runtime-context、`WorldSpec`、
  `WorldCell` 或 `EntityRef` behavior。
- 不添加 live provider credentials、network calls、model orchestration、background
  jobs、hidden retry loops、prompt libraries、prompt storage 或 prompt execution。
- 不持久化 private prompts、secrets、external application data、private validation oracle
  details、generated seed data 或 concrete world/story content。
- 不声明 generation quality、external validation readiness、projection readiness、
  product readiness、release readiness、API behavior 或 frontend behavior。

## 实现要求

- Import validation 必须把每个 imported plan 都当作 untrusted structured data。
- Import 不得绕过 `validate_generation_plan()`。
- Accepted imports 必须携带 redacted provenance，且 JSON-compatible、provider-independent。
- Rejected imports 必须返回 deterministic diagnostics，且不包含 accepted plan。
- Extra free-form prompt fields 必须被拒绝，不能静默忽略。
- Static/mock tests 不得要求 network、credentials、environment secrets 或 provider SDKs。

## 兼容性要求

- Existing template generation 和 structured-plan compiler behavior 保持兼容。
- 现有 `WorldSpec`、loader、runtime-context、API envelope、runtime、Agent/memory 和
  frontend behavior 保持不变。
- Historical v0.5 evidence 只作为 handoff context。

## 授权标准

只有满足以下条件后，本 package 才能记录 `implementation_authorized: yes`：

- 所有 package docs 和中文镜像存在。
- documentation/contract evaluator 报告 PASS，无 P0/P1 和 blocking unresolved P2。
- contract/design/test-plan/plan 明确禁止 live providers、prompts、API、frontend、
  persistence 和 concrete content。
- planned tests 覆盖 accepted import、invalid imported plan、malformed provenance、
  non-JSON import metadata、prompt field rejection 和 compiler compatibility。

## 北极星检查

本 package 通过让 AI output 保持为 reviewable structured data，安全推进 AI-assisted world
generation。它不让 WorldEngine 变成 provider-specific 或 application-specific。

## 范围外后续

- `0.6.5`：generation validation、metadata 和 preview API。
- `0.6.6`：regeneration 和 runtime-readiness integration。
- `0.6.7`：dashboard preview 和 E2E smoke。
- v0.7 external validation readiness。
- v0.8 projection application readiness。
