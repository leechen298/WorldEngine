# Contract

英文镜像：`contract.md`。

## Public Concepts

### `generated rule parameter set`

由 generated world model 派生出的 public structured bundle，包含 generated world parameters、
rules、constraints、boundaries 和 validation metadata。

Required semantics：

- 它是 public 且 redacted。
- 它不是 active runtime state。
- runtime 使用前可以 deterministic validate。
- 可用时，它引用 `0.9.2` 的 `world_id`、`generation_id` 和 `premise_digest`。
- 不得包含 raw prompts、raw provider responses、provider traces、hidden context、private
  Agent memory、private evaluator data 或 secrets。

### `world parameter definition`

public generated parameter definition。

Required field groups：

```text
parameter_id
path
value_type
initial_value
visibility
description
constraints
source
rule_refs
```

Required semantics：

- `parameter_id` 在 generated rule parameter set 内 stable。
- `path` 是 dot-separated public parameter path。
- `value_type` 是 `int`、`float`、`bool`、`string` 或 `json`。
- `initial_value` 必须匹配 `value_type`。
- `visibility` 必须保持 public 或 internal-public；不允许 private Agent state。
- `constraints` 可包含 public bounds、enum values、required keys 或 shape hints，但不能包含
  hidden rule logic。
- `rule_refs` 必须指向同一 set 内的 public rule ids。

### `world evolution rule`

描述 parameters 可以如何变化的 public rule definition。

Required field groups：

```text
rule_id
rule_kind
trigger
conditions
effects
target_parameter_refs
allowed_ops
priority
cooldown
evidence
```

Required semantics：

- `rule_id` stable 且 public。
- `rule_kind` 用于分类，例如 `environment_trend`、`resource_drift`、
  `agent_public_pressure`、`boundary` 或 `constraint`。
- `trigger` 描述 rule 何时 eligible。本包只定义 schema，不执行 triggers。
- `conditions` 是 public deterministic checks 或 structured public expressions。
- `effects` 描述 allowed parameter operations 和 expected value changes。
- `target_parameter_refs` 必须解析到同一 set 内的 parameter ids。
- `allowed_ops` 必须使用现有 patch vocabulary：`add`、`set`、`remove`，或未来需要时的
  public no-op classification。
- `evidence` 必须包含 public explanation fields，且不得包含 raw LLM reasoning 或 provider
  traces。

### `world constraint`

作用于 parameters、rules 或整个 generated set 的 public constraint。

Required semantics：

- Constraints 必须足够 deterministic，能被 validation 检查。
- Constraints 可表达 value ranges、enum membership、required parameter refs、forbidden
  operation refs 或 public dependency checks。
- Constraints 不得只用 untestable prose 作为唯一 rule。

### `world boundary`

限制 generated-world behavior 的 public boundary。

Required semantics：

- Boundaries 是 inspectable public constraints，不是 hidden runtime behavior。
- Boundaries 可限制 private-state mutation、direct user-imposed final facts、provider trace
  exposure、concrete fixture content 或 unbounded runtime changes。
- 本包不执行 boundaries。它们为后续 packages 提供 schema 和 validation evidence。

### `rule parameter validation result`

针对 generated rule parameter set 的 deterministic public validation result。

Required field groups：

```text
validation_status
diagnostics
accepted_parameter_count
accepted_rule_count
rejected_parameter_count
rejected_rule_count
redaction_status
compatibility_summary
```

Validation 必须 reject 或 diagnose：

- duplicate parameter ids。
- duplicate rule ids。
- unresolved rule refs。
- unresolved parameter refs。
- declared `value_type` 与 initial values 不匹配。
- 需要 targets 时，rules 没有 target parameter refs。
- 只有 prose、没有 structured trigger/effect 的 rules。
- private、secret-like、provider-trace、raw prompt 或 concrete fixture markers。

### `world rule summary`

validators 可检查的 public summary artifact 或 response section。

Required semantics：

- 汇总 accepted/rejected counts、parameter paths、rule ids、boundary ids 和 diagnostics。
- 可包含 public explanations。
- 不得包含 raw provider content 或 private source payloads。

## Compatibility Constraints

- Existing `/world/params` behavior 必须保持 compatible。
- Existing `ParamPatchItem`、`ApplyParamsRequest`、`ParamRegistry` 和 `ParamValidator`
  semantics 必须保持 compatible，除非本 contract 更新并重新 review。
- Existing deterministic `POST /worlds` behavior 必须保持 compatible。
- Existing `/world/generation/worldview` response 必须保持 compatible。
- Existing `WorldSpec` schemas 如被触及，只能 additive。
- Existing event schemas 保持 additive-compatible；event legality execution 不在本包范围。
- New schemas 必须是 generic WorldEngine concepts，不得包含 concrete world content。
- Validation errors 和 diagnostics 不得 echo private field values、secret-like values、raw
  prompts、raw provider details、hidden context 或 private field labels。

## Allowed Changes

documentation review 授权后，本包可以修改：

- `backend/app/schemas/world_generation.py`，用于 additive rule/parameter schemas；或按本地
  style 新增 narrow active-backend schema module。
- `backend/app/core/world_generation.py`，或新增 narrow active-backend helper，用于
  deterministic validation 和 public summaries。
- `backend/app/api/routes/world_generation.py`，仅当需要 additive endpoint 或 existing
  worldview-generation response field 以支持 rule/parameter validation。
- `backend/app/api/routes/world.py` 和 manifest data，仅用于 additive public surface
  discovery。
- `backend/app/world/validation/registry.py`、`backend/app/world/validation/validator.py` 及
  related validation tests，仅用于 additive compatibility support。Existing registered path
  behavior 不得破坏。
- `backend/app/tests/` 下 focused backend tests。
- package `review.md` 和 `review.zh.md`。
- v0.9 parent status/review docs，仅用于 review 或 implementation closeout 后的 route/status
  handoff。

## Forbidden Changes

本包不得：

- 修改 `backend/worldengine/`。
- 修改 frontend code。
- 修改 Validation Client 或 external repositories。
- 执行 live provider calls。
- 把 generated rules 或 generated worlds 持久化到 durable storage。
- 把 generated rules 安装进 active runtime state。
- 运行 bounded runtime ticks 作为 rule evolution 证明。
- 实现 worldview fidelity evaluation。
- 实现 natural-language direction、event legality、Agent continuity、narrative projection、
  diagnostic dialogue、checker fixtures、Validation Client evidence export 或 full lifecycle
  validation。
- 加入 concrete demo-world names、maps、characters、locations、resources、story rules、
  validation oracle data 或 application-specific backend behavior。
- 存储或导出 API keys、authorization headers、raw prompts、raw provider requests、raw provider
  responses、provider traces、hidden context、private Agent memory、raw thought、
  chain-of-thought 或 private evaluator data。
- 声明 rule-linked evolution PASS、LLM-backed lifecycle PASS、external validation PASS 或
  product readiness。

## North Star Check

本包通过为 generated worlds 定义 public rule and parameter contracts 来保持 WorldEngine
generic。它为未来 world evolution 准备 runtime/checker spine，但不创建具体 game world 或
product backend。

## Out-of-Scope Follow-ups

- `0.9.4`：worldview generation fidelity evaluation。
- `0.9.5`：bounded runtime control and run budgets。
- `0.9.6`：natural-language world direction boundary。
- `0.9.7`：rule-linked evolution and event legality execution。
- `0.9.10`：checker fixtures and scorecard support。
