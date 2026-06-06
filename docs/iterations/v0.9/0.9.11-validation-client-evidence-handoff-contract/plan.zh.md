# Plan

英文镜像：`plan.md`。

Status：documentation reviewed / no implementation authorized

## Objective

在 0.9.10 checker/schema/fixture support 之后，创建 reviewable 0.9.11 documentation package，
定义 Validation Client evidence handoff contract。

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/contract.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`
- `docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence/technical-design.md`
- `docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/technical-design.md`

## Files

Create：

- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/README.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/README.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/intent.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/intent.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/test-plan.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/test-plan.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/plan.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/plan.zh.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/review.md`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/review.zh.md`

Update：

- parent v0.9 route/status/review docs 从 documentation-package-needed 推进到
  documentation-review-needed。

Do not touch：

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- `tools/testing/**`
- generated result directories
- external repositories 或 Validation Client code

## Steps

1. Draft 完整 0.9.11 package document set。
2. 更新 parent route/status docs 到 documentation-review-needed。
3. 运行 `test-plan.md` 中的 documentation checks。
4. 交给 read-only documentation evaluator。
5. 如果 evaluator 报告无 P0/P1/blocking P2，更新 review evidence 并 route 到下一包；如果仍有
   findings，先修 documentation，再推进 route。

## Stop Conditions

- Handoff 需要 client-owned provider calls 或 provider keys。
- Handoff 允许 client 决定 PASS。
- Required artifacts 不能保持 redacted 和 public。
- 任何 implementation 或 runtime change 变成必要。
- Documentation evaluator 报告 P0/P1/blocking P2。
