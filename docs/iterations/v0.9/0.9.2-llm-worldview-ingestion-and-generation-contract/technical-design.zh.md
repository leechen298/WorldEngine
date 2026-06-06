# Technical Design

英文镜像：`technical-design.md`。

## Current State

当前相关 surfaces：

- `backend/app/schemas/world_generation.py` 已包含 v0.6 deterministic generation concepts：
  `WorldTemplate`、`GenerationPlan`、`GenerationMetadata`、diagnostics、preview、lineage 和
  runtime-readiness request/result shapes。
- `backend/app/api/routes/world.py` 暴露 v0.8 public `POST /worlds`，operation id 为
  `create_world`。当前它根据 prompt digest 返回 deterministic generic public initial state
  和 visualization data。
- `backend/app/schemas/world.py` 包含 public handoff、world creation、provider readiness、
  director guidance、public state 和 redaction schemas。
- `backend/app/agent/provider_config.py`、`backend/app/api/routes/provider.py` 和
  `backend/app/schemas/provider.py` 定义 `0.9.1` provider smoke 和 redacted summary boundary。
- `GET /manifest` 现在列出 `/provider/live-smoke`，并警告 provider readiness 不是 live
  provider call proof。
- LLM-backed world creation test scenario 要求 public generated state、
  `world_creation_summary`、redaction scan、scorecard/checker evidence，以及明确区分
  deterministic generic output。

`0.9.2` 必须基于这些 surfaces 构建，不触碰 `backend/worldengine/`，也不让 validation
clients 成为 generation owners。

## Contract Alignment and Invariants

review 之后 implementation 必须保持这些 invariants：

- Deterministic `POST /worlds` 继续 available 且 clearly labeled。
- LLM-backed generation 与 deterministic fallback 有独立 public classification。
- WorldEngine 拥有 provider/generation behavior。
- LLM output 是 untrusted structured data。必须先解析为 public structured model 或 plan，
  再 validation、diagnostics、classification，之后才能 summarize 为 runtime-ready。
- Public generated output 足够 structured，可供 runtime/checker use。
- Public evidence 不包含 raw prompts、raw provider payloads、provider traces、private Agent
  state、private evaluator data、hidden context 或 secrets。
- Full rule/parameter schema 延后到 `0.9.3`；`0.9.2` 只暴露 generated world creation 所需的
  outlines 和 readiness inputs。

## Proposed Implementation

review authorization 后，添加一个 small active-backend generation layer：

```text
Public worldview request
  -> request validation and redaction guard
  -> provider readiness / provider smoke boundary classification
  -> LLM-backed generation adapter, safe mock classifier, or blocked/fallback classifier
  -> untrusted structured output normalization
  -> validation, diagnostics, and runtime-readiness classification
  -> public generated world model candidate
  -> validation metadata and diagnostics
  -> public world_creation_summary response or artifact
```

Preferred API shape：

```text
POST /worlds/generate-from-worldview
operation_id: generate_world_from_worldview
```

该 endpoint 应 additive，不替换 existing `POST /worlds`。如果 implementation 选择其他 path，
route 仍必须 public、OpenAPI-discoverable，并明确分离 LLM-backed generation 和 deterministic
generic creation。

## Candidate Backend Shape

Expected implementation surfaces：

```text
backend/app/agent/provider_config.py
backend/app/agent/worldview_generation.py
backend/app/api/routes/world_generation.py
backend/app/api/routes/__init__.py
backend/app/api/app_factory.py
backend/app/schemas/world_generation.py
backend/app/schemas/world.py
backend/app/tests/test_llm_worldview_generation_api.py
backend/app/tests/test_world_generation_contracts.py
backend/app/tests/test_public_handoff_contract_api.py
```

Alternative file names 可接受，只要符合 local conventions，并停留在 allowed active backend paths。

## Data Model / Schema Changes

Additive schema concepts 应包括：

```text
WorldviewGenerationRequest
WorldviewGenerationResponse
PublicGeneratedWorldModel
PublicWorldCreationSummary
WorldviewGenerationValidationMetadata
WorldviewGenerationRedaction
WorldviewGenerationDiagnostic
WorldviewGenerationMode
WorldviewGenerationStatus
```

Required public enum semantics：

```text
generation_mode:
  provider_backed
  deterministic_fallback
  safe_mock
  not_configured
  blocked

generation_status:
  generated
  fallback
  not_configured
  blocked
  failed
  redaction_failure

creation_mode:
  llm_backed_generation
  deterministic_generic_fallback
  safe_mock_non_live
  provider_not_configured
  blocked
```

Required public validation flags or summaries：

```text
llm_backed: true | false
provider_backed: true | false
premise_specific: true | false | unknown
system_digestible: true | false
runtime_ready: true | false | blocked
deterministic_generic_response: true | false
deterministic_generic_fallback_detected: true | false
raw_prompt_included: false
raw_provider_response_included: false
provider_trace_included: false
private_data_included: false
```

provider 未配置时，response 应返回 public blocked 或 not-configured classification，而不是抛出
private provider details。

## Runtime / Service Design

generation helper 应暴露 narrow functions：

- validate public worldview request。
- build private provider intent，但不在 public evidence 中暴露。
- create generated model candidate，或 classify generation as blocked。
- summarize public generated model fields。
- validate redaction before returning public evidence。
- classify deterministic fallback separately from provider-backed generation。
- sanitize request validation errors，避免 echo rejected raw premise/private field values。

helper 不得：

- persist generated worlds。
- mutate active runtime state。
- append canonical world events。
- execute bounded runtime ticks。
- install rules or parameters into runtime。
- store provider traces or raw prompt data。

本包中的 runtime readiness 是 public classification，不是 actual runtime execution。后续 package
拥有 rule schema、fidelity evaluation 和 bounded runtime execution。

## Compatibility

- `POST /worlds` 保持 deterministic and compatible。
- `GET /manifest` 可以 additive 增加新 generation endpoint 和 warnings。
- Existing provider readiness labels 与 `0.9.1` 保持 compatible。
- Existing v0.6 generation schemas 保持 compatible；new schemas additive，可以复用
  diagnostics、metadata 和 runtime-readiness terms。
- Existing tests for public handoff、world creation、provider redaction 和 validation error
  sanitization 必须继续通过。

## Redaction Scan Points

Redaction 和 private-value echo checks 必须覆盖：

- request validation errors。
- provider result classification。
- generation metadata。
- public generated model。
- `world_creation_summary`。
- serialized API responses。
- 本包创建的任何 result artifacts 或 operation logs。

Forbidden markers 包括 raw prompt、raw request、raw response、provider_trace、
hidden_context、private memory、private goal、self_state、authorization、bearer、api_key、
secret、token、credential 和 concrete validation-world fixture markers。

## Risks

- Risk：deterministic fallback 被夸大成 LLM-backed success。
  Mitigation：要求明确 `generation_mode` 和 fallback tests。
- Risk：public evidence 泄露 raw prompt 或 provider response text。
  Mitigation：redaction schema 加 serialized-response scans，并注入 forbidden markers。
- Risk：generated model 只有 prose，不是 system-digestible。
  Mitigation：schema tests 要求 structured public model sections。
- Risk：implementation drift 到 `0.9.3+` rules 和 runtime execution。
  Mitigation：本包只限 outlines、summaries 和 readiness classification。
- Risk：safe mock provider behavior 被算作 provider-backed world generation。
  Mitigation：明确 `safe_mock_non_live` / `safe_mock_only` classification 和 negative tests。
- Risk：Validation Client 成为 generation owner。
  Mitigation：无 external repository changes，并要求 WorldEngine-owned generation evidence。
