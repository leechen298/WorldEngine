# Contract

英文镜像：`contract.md`。

## Public Concepts

### `worldview premise`

用户提供的 public 世界观描述。它可以包含 setting、tone、constraints、broad entities、
environmental conditions 或 high-level rules，但必须被视为 untrusted input。

Required semantics：

- 必须被 request validation 限制。
- 不得不经 structured generation 和 validation 就直接复制进 canonical final world state。
- 不得包含 API keys、provider headers、private evaluator data、hidden prompts、private Agent
  memory 或 application-specific oracle data。
- Public evidence 可包含 length、digest、public premise tags 和 redacted summaries，但不包含
  raw private prompt traces。

### `LLM-backed generation request`

由 WorldEngine 发起的 request，用于把 public worldview premise 转成 generated public world
model candidate。

Required semantics：

- 必须由 WorldEngine 发起，不由 Validation Client 发起。
- 必须把 provider state 分类为 `provider_backed`、`deterministic_fallback`、
  `not_configured`、`blocked` 或 `failed`。
- 必须明确标记 deterministic fallback，不得把 fallback 报告为 LLM-backed PASS。
- 必须在没有 live provider access 时仍可通过 blocked 和 safe fallback paths 测试。

### `generated world model`

从 worldview premise 派生的 public、system-digestible world model candidate。

Required public field groups：

```text
schema_version
world_id
generation_id
generation_status
generation_mode
creation_mode
llm_backed
provider_backed
deterministic_generic_fallback_detected
provider_class
model_label
worldengine_owned_generation
premise_digest
public_world_model
world_creation_summary
validation_metadata
redaction
warnings
blockers
```

`public_world_model` 必须是 structured data，不只是 prose。它应只包含 public fields，例如：

```text
title_label
premise_summary
world_parameters_outline
locations_outline
entities_outline
agents_outline
items_outline
environment_outline
rules_outline
boundary_conditions
runtime_readiness_inputs
```

本包可以定义 `0.9.2` 需要的 outlines，但完整 structured rule/parameter schema 属于 `0.9.3`。

Generated model 不得只是 prompt digest 加 fixed observer。它必须在 worldview premise 和 generated
world parameters、entities、agents、environment、boundary conditions、visualization
references、rule outlines 之间提供 public、redacted correspondence。

### `world_creation_summary`

validator 可 inspect 的 public evidence artifact 或 response section。它必须说明 generated output 是否：

- premise-specific。
- system-digestible。
- redacted。
- 不同于 deterministic generic response。
- runtime-ready，或因 public reason 被 blocked。
- `provider_backed`、`deterministic_fallback`、`not_configured`、`blocked` 或 `failed`。

它不得包含 raw prompts、raw responses、provider traces、private evaluator data 或 concrete
external validation seed worlds。

### `generation validation metadata`

在 runtime use 之前用于分类 candidate 的 public validation metadata。

Required groups：

```text
premise_specificity
system_digestibility
deterministic_fallback_label
runtime_readiness
redaction_status
provider_generation_status
diagnostics
```

Diagnostics 必须使用 stable public codes、public messages、optional public paths、severity，
且不包含 private source payloads。

### `generation provenance summary`

说明 generation 如何被分类的 public summary。

Required public fields：

```text
creation_mode
llm_backed
provider_backed
worldengine_owned_generation
provider_class
model_label
call_status
deterministic_generic_fallback_detected
safe_mock_only
provider_live_call_evidence
```

`safe_mock_only` 绝不能算 provider-backed generation PASS。`provider_live_call_evidence` 在
live provider execution 没有被明确授权并在 current session 完成 redaction-check 前，必须为
absent、false 或 blocked。

## Compatibility Constraints

- Existing `POST /worlds` deterministic generic behavior 必须继续 available 且 clearly labeled。
- Existing public handoff manifest behavior 保持 additive-compatible。
- Existing v0.6 generation schemas 和 loader/runtime-readiness semantics 保持 compatible。
- Existing `WorldSpec` schema changes 必须 additive，除非本 contract 被更新并重新 review。
- Existing API response envelope behavior 保持 compatible，除非 implementation 明确使用 v0.8
  handoff 已要求的 public top-level response shape。
- Existing unconfigured provider behavior 保持 safe and testable。
- New public outputs 使用 generic WorldEngine concepts，不使用 external application details。
- Validation errors 和 rejected request diagnostics 不得 echo raw worldview input、secret-like
  values、raw provider details、hidden context 或 private field labels。

## Allowed Changes

review authorization 后，本包可修改：

- `backend/app/api/routes/`
- `backend/app/api/app_factory.py`
- `backend/app/agent/provider_config.py`
- `backend/app/agent/worldview_generation.py`
- `backend/app/schemas/`
- `backend/app/core/world_generation.py` 或同等范围 active-backend generation helper。
- `backend/app/tests/` 下 focused backend tests。
- 仅在需要 public `world_creation_summary` checker support 时，修改
  `tools/testing/validate_agent_autonomous_result.py` 和 focused tests。
- package `review.md` 和 `review.zh.md`。
- 仅为 route/status handoff，在 review 或 implementation closeout 后更新 v0.9 parent
  status/review docs。

## Forbidden Changes

本包不得：

- 修改 `backend/worldengine/`。
- 修改 Validation Client repository。
- 让 Validation Client 拥有 provider calls、prompt assembly、generation、evaluation 或 provider credentials。
- 添加 concrete demo-world names、maps、characters、locations、resources、story rules、
  seed data、oracle internals 或 application-specific backend logic。
- 持久化 provider keys、authorization headers、raw prompts、raw provider requests、raw
  provider responses、provider traces、hidden context、private evaluator data、private
  Agent memory、raw thought 或 chain-of-thought。
- 从 deterministic fallback、safe mock 或 provider readiness 声明 LLM-backed generation PASS。
- 把 `/provider/live-smoke` safe mock success 当成 provider-backed world generation evidence。
- 声明 provider live PASS，除非 live call 被明确授权、运行，并在 current session 通过 redaction check。
- 实现 `0.9.3+` rule schema、bounded runtime controls、event legality、Agent continuity、
  narrative projection、diagnostic dialogue、Validation Client evidence export 或 full lifecycle validation。
- 引入 migrations、durable generated-world persistence、product UI、game packaging 或 external
  repository changes。
- 修改 `backend/app/agent/` 中的 Agent loop、private memory、private goals 或 Agent continuity
  behavior。

## North Star Check

本包保持 WorldEngine 是 generic recursive world generation engine。它定义 public engine
contracts 和 generated model summaries，而不是具体 game world 或 application backend。
External clients 继续只是 public generation/evidence contract 的消费者。

## Out-of-Scope Follow-ups

- `0.9.3`：full world model rule and parameter schema。
- `0.9.4`：worldview generation fidelity evaluation。
- `0.9.5`：bounded runtime control and run budget。
- `0.9.7`：rule-linked event legality and evolution。
- `0.9.10`：LLM-backed checker、fixtures、schema 和 scorecard。
- `0.9.11`：Validation Client evidence handoff contract。
- `0.9.12`：LLM-backed full lifecycle validation execution。

## Stop Rules

如果出现以下情况，停止 implementation：

- generated output 无法表示为 structured public data。
- premise specificity 无法在不暴露 raw prompt 或 raw provider response 的情况下证明。
- provider configuration 需要 environment-owned runtime configuration 之外的 secrets。
- 需要 Validation Client changes。
- deterministic fallback 必须被报告为 LLM-backed PASS。
- implementation 需要 concrete demo-world content。
- tests 无法证明 redaction 和 fallback/blocker classification。
- validation errors 会 echo raw/private request values。
- implementation 发现本包需要后续 package 拥有的 broader rule schema 或 checker architecture。
