# Technical Design

英文镜像：`technical-design.md`。

## Current State

相关 current surfaces：

- `backend/app/schemas/world_generation.py` 包含 `0.9.2`
  `WorldviewGenerationRequest`、`WorldviewGenerationResponse`、`PublicGeneratedWorldModel`、
  `PublicWorldCreationSummary` 和 validation metadata。`PublicGeneratedWorldModel` 当前暴露
  `world_parameters_outline`、`rules_outline`、`boundary_conditions` 和
  `runtime_readiness_inputs`。
- `backend/app/agent/worldview_generation.py` 创建 non-live public generated world
  candidates。它产出 rule 和 parameter outlines，但不验证完整 rule/parameter set。
- `backend/app/schemas/params.py` 定义 patch request shape：`ParamPatchItem` 和
  `ApplyParamsRequest`。
- `backend/app/world/validation/registry.py` 注册 writable runtime paths：
  `counter.increment`、`heartbeat.enabled` 和 `scene.weather`。
- `backend/app/world/validation/validator.py` 校验 existing patch ops、reserved prefixes、
  known paths、value types 和 bounds。
- `backend/app/api/routes/world_params.py` 暴露 existing `/world/params` read/apply routes，
  并发出 `params.applied` events。
- `backend/app/schemas/event.py` 提供 additive event refs，但 event legality execution 不属于
  本包。
- `backend/app/schemas/world_cell.py` 提供 generic `WorldSpec`；本包不应要求 breaking schema
  change。

## Contract Alignment and Invariants

review 授权后的 implementation 必须保持：

- existing `/world/params` apply/read behavior。
- existing deterministic `POST /worlds`。
- existing `/world/generation/worldview` response compatibility。
- 不修改 `backend/worldengine/`。
- validate generated rule parameter sets 时不 mutate active runtime。
- 不执行 live provider calls。
- public redaction raw prompt/provider/private markers。

generated rule parameter set 是 public candidate contract，不是 installed runtime state。

## Proposed Implementation

review 授权后的 preferred implementation shape：

```text
Public generated model or explicit rule parameter payload
  -> schema validation
  -> deterministic rule/parameter validation helper
  -> redaction/private-marker scan
  -> public validation result
  -> public world_rule_summary
```

Implementation 应添加 narrow schema and validation layer，而不是把 rule semantics 嵌入 runtime
engine。

## Affected Surfaces

Expected surfaces：

```text
backend/app/schemas/world_generation.py
backend/app/core/world_generation.py or backend/app/core/world_rule_parameters.py
backend/app/api/routes/world_generation.py
backend/app/api/routes/world.py
backend/app/tests/test_world_generation_schema.py
backend/app/tests/test_world_rule_parameter_schema.py
backend/app/tests/test_llm_worldview_generation_api.py
backend/app/tests/test_world_params.py or test_param_validator.py
```

只要留在 contract 内，允许使用其他 active-backend 文件名。

## Data Model / Schema Changes

Additive schema concepts 应包括：

```text
WorldParameterValueType
WorldParameterVisibility
WorldParameterDefinition
WorldParameterRef
WorldRuleTrigger
WorldRuleCondition
WorldRuleEffect
WorldEvolutionRule
WorldConstraint
WorldBoundary
GeneratedRuleParameterSet
RuleParameterDiagnostic
RuleParameterValidationResult
PublicWorldRuleSummary
```

Candidate field semantics：

- `WorldParameterDefinition.parameter_id`：set 内 stable id。
- `WorldParameterDefinition.path`：public parameter references 使用的 dot path。
- `WorldParameterDefinition.initial_value`：JSON-compatible value，按 `value_type` 检查。
- `WorldEvolutionRule.rule_id`：stable public id。
- `WorldEvolutionRule.target_parameter_refs`：必须能 resolve 的 parameter ids。
- `WorldEvolutionRule.effects`：structured public operations，以及 public value expressions 或
  value deltas。
- `WorldConstraint`：针对 parameters、rules 或 generated set 的 deterministic public
  constraints。
- `WorldBoundary`：inspectable public boundary category and explanation。
- `RuleParameterValidationResult`：包含 public diagnostics 和 redaction status 的
  deterministic accept/reject result。

## Runtime / Service Design

Validation helper responsibilities：

- 确保 parameter ids 和 paths 唯一。
- 确保 rule ids 唯一。
- resolve parameter refs 和 rule refs。
- 按 `value_type` 校验 `initial_value`。
- 校验 structured trigger/effect presence。
- 在 ids、paths、descriptions、evidence、diagnostics 和 summary fields 中 reject private
  markers。
- 产出 stable codes 和 public paths 的 public diagnostics。
- 产出未来可成为 `world-rule-summary.json` 的 public summary。

Helper 不得：

- 随时间评估 rules。
- 对 `WorldState` 应用 parameter patches。
- append events。
- persist generated data。
- call providers。
- inspect private Agent memory 或 hidden evaluator data。

## Compatibility

Existing patch validation 继续使用 current registry and validator。Generated rule/parameter
schema 可以引用 future 或 generated parameter paths，但不得 silent 地让这些 paths 变成
`/world/params` writable。把 generated definitions bridge 到 runtime writable params 是 future
work，需要重新 review。

Existing schema/API additions 应保持 optional and additive。

## Risks

- Risk：generated rules 仍是 untestable prose。
  Mitigation：tests reject 没有 structured triggers/effects 或 target refs 的 rules。
- Risk：generated parameter paths 破坏 `/world/params`。
  Mitigation：compatibility tests 保持 current registered-path behavior。
- Risk：private prompt/provider data 通过 descriptions 或 evidence 泄露。
  Mitigation：serialized schema/summary redaction tests。
- Risk：package drift into runtime evolution。
  Mitigation：contract 禁止 applying patches、appending events 或 running tick-based proof。
