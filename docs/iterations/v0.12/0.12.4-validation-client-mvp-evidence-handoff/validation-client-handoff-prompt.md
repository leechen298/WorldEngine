# Validation Client Handoff Prompt

Chinese mirror: `validation-client-handoff-prompt.zh.md`.

Use this prompt in a separate WorldEngine-Validation-Client iteration, not in
the WorldEngine repository:

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

Expected result: a Validation Client package can export public evidence for
`0.12.5` checker/scorecard review without guessing WorldEngine artifact
semantics.
