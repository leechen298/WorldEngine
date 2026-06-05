# LLM-backed Lifecycle Result Directory Template

状态：template / checker-extension-required

用于：

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

## Directory Layout

```text
result.json
operation-log.jsonl
api-log.jsonl
api-summary.json
provider-live-summary.json
world-creation-summary.json
world-rule-summary.json
rule-parameter-summary.json
event-legality-summary.json
agent-autonomy-summary.json
diff-replay-summary.json
world-lifecycle-summary.json
validation-client-evidence-bundle.json
scorecard-summary.json
redaction-scan.json
second-agent-review.md
transcript.md
console.log
screenshots/
raw/
```

## Boundary

`raw/` directory 可以包含来自 WorldEngine 和 Validation Client 的 raw public artifacts。
但它仍必须遵守 redaction，不得包含：

- API keys。
- authorization headers。
- raw prompts。
- raw provider requests。
- raw provider responses。
- provider traces。
- private Agent memory。
- private Agent goals。
- raw thought。
- raw chain-of-thought。
- hidden context。
- private evaluator 或 oracle data。

## `result.json` Minimum Fields

- `scenario`: `llm-backed-full-lifecycle-autonomous`
- `goal`
- `mode`
- `status`
- `verdict_source`
- `score_items`
- `required_artifacts`
- `artifacts`
- `operation_log`
- `api_summary`
- `redaction`
- `second_agent_review`
- `unverified_items`
- `failures`

PASS 需要 `status=pass`、accepted `verdict_source`、无 critical failures，并且第二 Agent
复核 clean。
