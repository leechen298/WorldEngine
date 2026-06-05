# LLM-backed 生命周期验证结果模板

状态：模板

英文镜像：`llm-backed-lifecycle-validation-result-template.md`。

用于：

```text
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.zh.md
```

## Header

```markdown
# LLM-backed 生命周期验证结果

Status: PASS | FAIL | BLOCKED | PARTIAL
Mode: live LLM-backed lifecycle validation plus checker/scorecard
Date: YYYY-MM-DD
Branch:
Commit:
Result directory:
英文镜像：`YYYY-MM-DD-llm-backed-lifecycle-validation.md`
```

## Scope

In scope：

- provider live smoke。
- LLM-backed world creation。
- world rule parameter evolution。
- rule-compliant event generation。
- Agent persistent autonomy evidence。
- evidence export。
- checker 或 scorecard。
- 第二 Agent 只读复核。

Out of scope：

- 除非完整产品验证套件也通过，否则不声明 final product readiness。
- 不声明 final LLM quality approval。
- 不包含 concrete external validation world seed data。
- Validation Client 不拥有 LLM 或 evaluator logic。

## Scenario

权威 scenario：

- `docs/testing/agent-autonomous/scenarios/llm-backed-full-lifecycle-autonomous.md`

Supporting contracts：

- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`

## Commands And Checkers

| Command or checker | Result | Notes |
| --- | --- | --- |
| ... | ... | ... |

## Covered Evidence

| Score item | Status | Artifact | Notes |
| --- | --- | --- | --- |
| `provider_live_smoke` | pass/fail/blocked/not_run | `provider-live-summary.json` | ... |
| `world_creation_llm_backed` | pass/fail/blocked/not_run | `world-creation-summary.json` | ... |
| `world_rules_generated` | pass/fail/blocked/not_run | `world-rule-summary.json` | ... |
| `parameter_evolution_rule_linked` | pass/fail/blocked/not_run | `rule-parameter-summary.json` | ... |
| `event_legality_enforced` | pass/fail/blocked/not_run | `event-legality-summary.json` | ... |
| `agent_persistent_autonomy` | pass/fail/blocked/not_run | `agent-autonomy-summary.json` | ... |
| `diff_replay_available` | pass/fail/blocked/not_run | `diff-replay-summary.json` | ... |
| `redaction_clean` | pass/fail/blocked/not_run | `redaction-scan.json` | ... |
| `client_evidence_complete` | pass/fail/blocked/not_run | result directory | ... |
| `second_agent_review_clean` | pass/fail/blocked/not_run | `second-agent-review.md` | ... |

## Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `provider-live-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `rule-parameter-summary.json`
- `event-legality-summary.json`
- `agent-autonomy-summary.json`
- `diff-replay-summary.json`
- `world-lifecycle-summary.json`
- `validation-client-evidence-bundle.json`
- `scorecard-summary.json`
- `redaction-scan.json`
- `second-agent-review.md`

## Redaction

```text
API keys included: false
authorization headers included: false
raw prompts included: false
raw provider responses included: false
provider traces included: false
private Agent memory included: false
private Agent goals included: false
raw thought included: false
hidden context included: false
private evaluator/oracle data included: false
```

## Second-Agent Review

```text
Review status:
Blocking P1/P2:
Report path:
```

## Failures

| ID | Severity | Taxonomy | Evidence | Required follow-up |
| --- | --- | --- | --- | --- |
| ... | P1/P2/P3 | provider/world_creation/world_evolution/event_legality/agent_autonomy/redaction/client_evidence/checker_gap | ... | ... |

## Verdict

```text
Verdict:
PASS source:
FAIL taxonomy:
Unresolved blockers:
```

## Boundary

本结果不声明 product readiness、final LLM quality approval、full external consumer
certification 或 real consciousness。
