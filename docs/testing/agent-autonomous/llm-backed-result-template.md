# LLM-backed Lifecycle Result Directory Template

Status: template / checker-extension-required

Use this template for:

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

The `raw/` directory may contain raw public artifacts from WorldEngine and the
Validation Client. It must still obey redaction. It must not contain:

- API keys.
- authorization headers.
- raw prompts.
- raw provider requests.
- raw provider responses.
- provider traces.
- private Agent memory.
- private Agent goals.
- raw thought.
- raw chain-of-thought.
- hidden context.
- private evaluator or oracle data.

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

PASS requires `status=pass`, accepted `verdict_source`, no critical failures,
and a clean second-Agent review.
