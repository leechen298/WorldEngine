# 技术设计

Status: review complete

## 设计边界

`0.6.4` 添加本地、provider-independent import boundary。它接收 structured
`GenerationPlan` data 和 redacted provenance，validate import envelope，然后把 plan
validation 委托给 `validate_generation_plan`。

本设计不调用 providers，不解析 prompts，不开放 API routes，不持久化 data，也不自行 compile/run
imported plan。

## 计划 Schema Additions

`backend/app/schemas/world_generation.py` 可以添加：

- `PlanImportSource`，包含 source kind、optional source id、provider label、model label、
  redaction flag 和 generic metadata。
- `PlanImportRequest`，包含 import id、`GenerationPlan`、provenance 和 optional import
  metadata。
- `PlanImportResult`，包含 optional accepted plan、provenance、diagnostics 和 validation
  status。

Import schemas 应拒绝 unexpected fields，避免 prompt text 被静默接受。

## 计划 Core Additions

`backend/app/core/world_generation.py` 可以添加：

- `validate_plan_import(request)`。
- `import_generation_plan(request)`。

Import validation 应检查 provenance JSON compatibility、import metadata JSON
compatibility、prompt-field rejection，以及来自 `validate_generation_plan` 的所有
diagnostics。

## 确定性与安全

Import results 不得包含 wall-clock time、random identity、external network、environment
secret 或 provider SDK。Diagnostics 必须 stable 且带 path。

## 兼容性

Existing template generation 和 structured-plan compilation 必须保持兼容。Runtime、API、
frontend、loader、persistence 和 `backend/worldengine/` behavior 保持不变。

## 范围外

- Live AI generation。
- Prompt execution 或 storage。
- API exposure。
- Preview、regeneration、persistence、external validation、projection 和 UI。
