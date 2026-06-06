# Plan

英文镜像：`plan.md`。

Status：documentation reviewed / evidence execution authorized

## Objective

为 LLM-backed full lifecycle validation run 准备 reviewed evidence-execution package。

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/llm-backed-suite-execution.md`
- `docs/testing/agent-autonomous/scenarios/` 下所有 LLM-backed scenario docs
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/`

## Files

Create 本 package 的 14 个 documentation files，并把 parent v0.9 route docs 更新到
documentation-review-needed。

Review 后允许：

- `docs/testing/results/**`
- ignored `test-results/agent-autonomous/**`
- 本 package 和 parent route/review docs。

Forbidden：

- code、checker、fixture、frontend、Validation Client、generated-result rewrite、provider credential、
  external repository 或 `backend/worldengine/` changes。

## Steps

1. Draft package docs。
2. 运行 documentation checks。
3. 交给 read-only documentation evaluator。
4. Documentation evaluator 已报告 PASS；status 已更新为 evidence-execution-authorized。
5. 运行 staged validation 或 classify blockers。
6. 运行 checker/scorecard 和 second-Agent review。
7. 写 durable result summaries。
8. 带 PASS 或 classified FAIL/BLOCKED/NOT_RUN route 到 0.9.13 closeout。

## Stop Conditions

- Documentation review 报告 P0/P1/blocking P2。
- Provider credentials 缺失，或必须暴露 secrets 才能使用。
- Validation 需要 code changes。
- Required artifacts 无法产生或 redacted。
- Checker 或 second-Agent review 阻断 PASS。
