# Validation Client Handoff Prompt

英文原文：`validation-client-handoff-prompt.md`。

在独立 WorldEngine-Validation-Client iteration 中使用此 prompt，不要在 WorldEngine 仓库中使用：

```text
Implement MVP evidence export for WorldEngine v0.12 using only public
WorldEngine APIs and public artifacts.

Required reading:
- WorldEngine docs/iterations/v0.12/0.12.4-validation-client-mvp-evidence-handoff/
- WorldEngine /manifest response
- WorldEngine public OpenAPI metadata

Required outputs:
- manifest.json
- operation-log.jsonl
- api-log.jsonl
- session-summary.json
- agent-evidence.json
- inspection-evidence.json
- scorecard-input.json
- redaction-report.json

Rules:
- Do not implement Validation Client code inside WorldEngine.
- Do not represent Codex, OpenClaw, or any external validation agent as an
  in-world Agent, player, memory, dialogue participant, or world event actor.
- Do not own provider configuration or provider-call authorization. The client
  may only operate public WorldEngine APIs after the appropriate
  WorldEngine/environment authorization and configuration already exist.
- Do not include raw prompts, raw provider responses, raw thought, private
  memory, private goals, hidden context, secrets, or private evaluator data.
- Treat narrative and diagnostic inspection as read-only evidence.
- Treat PASS/PARTIAL/BLOCKED/FAIL as checker/scorecard/review classifications,
  not as a Validation Client self-claim.
```

预期结果：Validation Client package 可以为 `0.12.5` checker/scorecard review 导出 public evidence，而不需要猜 WorldEngine artifact semantics。
