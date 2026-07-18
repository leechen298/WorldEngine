# Contract

英文版本：`contract.md`。

## Public Concepts

- `provider_preflight_status`：provider/worldview generation path 的 public readiness
  classification。
- `generation_mode`：现有 public worldview generation mode，例如
  `deterministic_fallback`、`safe_mock`、`blocked` 或 `not_configured`。
- `live_call_authorization`：package-level 明确声明 live provider calls 未授权。
- `redaction_safe_summary`：不包含 secrets、raw prompts、raw responses、traces、
  hidden context 或 private evaluator data 的 public evidence。

## Allowed Changes

- 新增 `backend/app/schemas/provider_preflight.py` 或等价 additive schemas。
- 新增 additive API route，例如 `POST /provider/worldview-preflight`。
- 复用已有 provider readiness 和 worldview generation helpers，但不运行 live provider calls。
- 更新 manifest public surfaces，暴露新的 preflight endpoint。
- 增加 focused backend tests。
- 更新本 package 和 parent v0.11 review/route docs。

## Forbidden Changes

- 不运行 live provider call。
- 不声明 provider-backed quality PASS。
- Public payloads 不得包含 secret、raw prompt、raw response、provider trace、
  private Agent memory、hidden context、raw thought 或 private evaluator data。
- 不实现 Validation Client。
- 不实现 world rules、direction queue、event generation、diff application 或 fidelity scoring。
- 不做 durable persistence/migrations。
- 不修改 `backend/worldengine/`。

## Compatibility Requirements

- 现有 `/provider/live-smoke`、`/world/generation/worldview`、`/sessions` 和
  `/sessions/from-worldview` behavior 保持 additive-compatible。
- Provider 未配置时，必须仍可分类为 `not_configured`，或在 request fallback 时分类为
  deterministic fallback。
- Provider 已配置但 live-call 未授权时，必须保持 blocked，不得静默降级成 provider-backed PASS。
- Mock provider 必须继续标记为 non-live 和 non-provider-backed。

## Out-of-Scope Follow-Ups

- 真实 provider-backed generation 只有在后续 package 明确授权 live provider 和 evidence 时才可做。
- Structured rules and parameters 属于 `0.11.2`。
- Direction queue/boundary 属于 `0.11.3`。
- Rule-compliant events/diffs 属于 `0.11.4`。
- Fidelity validation 属于 `0.11.5`。
