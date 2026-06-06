# Current State

英文镜像：`CURRENT_STATE.md`。

Campaign status：reviewed / ready for child package development
Active child package：none
Current route：`0.9.0-v0.9-planning-and-v0.8-handoff-baseline-documentation-package-needed`
Implementation authorization：no
Evidence execution authorization：no
Audit execution authorization：no
Provider live-call authorization：no
External validation authorization：no

## Planned Package Roadmap Status

```text
0.9.0-v0.9-planning-and-v0.8-handoff-baseline: planned / documentation package needed
0.9.1-provider-live-smoke-and-redaction-boundary: planned
0.9.2-llm-worldview-ingestion-and-generation-contract: planned
0.9.3-world-model-rule-parameter-schema: planned
0.9.4-worldview-generation-fidelity-evaluation: planned
0.9.5-bounded-runtime-control-and-run-budget: planned
0.9.6-natural-language-world-direction-boundary: planned
0.9.7-rule-linked-evolution-and-event-legality: planned
0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence: planned
0.9.9-external-narrative-and-diagnostic-dialogue-boundary: planned
0.9.10-llm-backed-autonomous-checker-and-fixtures: planned
0.9.11-validation-client-evidence-handoff-contract: planned
0.9.12-llm-backed-full-lifecycle-validation-execution: planned
0.9.13-v0.9-release-candidate-and-closeout: planned
```

Parent v0.9 documentation 已 review，并可进入 concrete child package development。仅凭这个
parent document 不会激活任何 `0.9.x` child package。Validation Client work、generated-result
creation、live provider calls、checker execution、external validation、frontend UI、durable
scheduling 和 `backend/worldengine/` changes 仍未授权。

## Current Route

Current route：

```text
0.9.0-v0.9-planning-and-v0.8-handoff-baseline-documentation-package-needed
```

下一位 agent 只能创建或 review concrete `0.9.0` documentation package。Runtime、schema、API、
frontend、evidence execution、generated-result creation、checker execution 或 fixture changes、
external validation、live provider calls、durable scheduling、Validation Client changes 和
`backend/worldengine/` work 仍未授权，除非 reviewed child package 明确授权 implementation。

## Current Exclusions

Current v0.9 documentation 不声明：

- provider live call passed。
- DeepSeek configured 或 reachable。
- LLM-backed world creation passed。
- world rule generation passed。
- live LLM-backed 或 generated-result worldview fidelity passed。
- provider-backed 或 external-validation bounded runtime control passed。
- rule-compliant event generation passed。
- checker-backed 或 external-validation Agent continuity passed。
- checker-backed 或 external-validation sleep/rest/low-activity memory consolidation passed。
- checker-backed 或 external-validation narrative projection boundary passed。
- checker-backed 或 external-validation out-of-world diagnostic Agent conversation boundary passed。
- LLM-backed checker/schema support passed。
- Validation Client LLM-backed evidence export passed。
- LLM-backed full lifecycle PASS。
- product readiness。
- external validation PASS。

## Approval Target

The active package target is：

```text
0.9.0-v0.9-planning-and-v0.8-handoff-baseline
```

当前任务是 documentation-package creation 或 review。Implementation 必须等 concrete child package
在 documentation/contract/design/test-plan review 后记录 positive implementation authorization。
