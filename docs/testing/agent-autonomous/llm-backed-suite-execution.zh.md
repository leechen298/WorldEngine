# LLM-backed Lifecycle Suite Execution

状态：planned runbook / checker-extension-required

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目的

本文是后续 LLM-backed autonomous lifecycle validation run 的执行入口。只有 required
WorldEngine behavior、Validation Client evidence fields 和 checker support 存在后，
它才可执行。

## Required Reading

- `docs/testing/llm-backed-lifecycle-validation-plan.zh.md`
- `docs/testing/agent-autonomous/scenarios/provider-live-smoke-deepseek.zh.md`
- `docs/testing/agent-autonomous/scenarios/llm-backed-world-creation.zh.md`
- `docs/testing/agent-autonomous/scenarios/world-rule-parameter-evolution.zh.md`
- `docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.zh.md`
- `docs/testing/agent-autonomous/scenarios/agent-persistent-autonomy-evidence.zh.md`
- `docs/testing/agent-autonomous/scenarios/llm-backed-full-lifecycle-autonomous.zh.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.zh.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.zh.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.zh.md`

## Preconditions

- WorldEngine 拥有 provider configuration 和 provider calls。
- DeepSeek key 通过 WorldEngine environment variables 提供。
- Validation Client 不保存、不展示、不转发 provider keys。
- 存在 WorldEngine-owned live provider smoke call path。
- WorldEngine 可以生成 public LLM-backed world state 和 rules。
- WorldEngine 可以根据 rules 演化 parameters 和 events。
- WorldEngine 可以暴露 public Agent continuity evidence。
- Validation Client 可以导出 required evidence artifacts。
- scenario 已有 checker 或 scorecard support。

## Execution Sequence

1. Preflight and budget check。
2. Start WorldEngine and Validation Client。
3. Run `provider-live-smoke-deepseek`。
4. Run `llm-backed-world-creation`。
5. Run `world-rule-parameter-evolution`。
6. Run `rule-compliant-event-generation`。
7. Run `agent-persistent-autonomy-evidence`。
8. 使用 `llm-backed-result-template.md` 导出 result directory。
9. Run checker or scorecard。
10. Run second-Agent read-only review。
11. 在 `docs/testing/results/` 下写 durable result summary。

## Stop Rules

出现以下情况时停止并分类 FAIL：

- provider live call 不能通过 WorldEngine attempted。
- deterministic generic world output 是唯一 creation path。
- user direction 直接修改 final world state。
- Agent action 是 client-scripted。
- required artifacts 缺失。
- redaction scan 发现 blocking leak。
- claimed PASS 缺少 checker support。
- budget、quota、rate limit 或 network constraints 阻止可靠 provider validation。

## FAIL Taxonomy

使用一个或多个：

- `provider`
- `world_creation`
- `world_evolution`
- `event_legality`
- `agent_autonomy`
- `redaction`
- `client_evidence`
- `checker_gap`
