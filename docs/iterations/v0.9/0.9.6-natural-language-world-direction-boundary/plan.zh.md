# Plan

英文原文：`plan.md`。

## Objective

创建并 review 具体 `0.9.6` package；只有授权后，才实现 reviewed active-backend
natural-language world direction boundary。

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/GOAL_RUNNER.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `backend/app/api/routes/world.py`
- `backend/app/schemas/world.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.md`

## Documentation Stage

1. 创建 required package docs 和 Chinese mirrors。
2. 校验 package file count 和 required terms。
3. 请求 read-only documentation/contract evaluator review。
4. Implementation authorization 前修复 P0/P1/blocking P2 findings。
5. 如果 clean，仅为本包在 `review.md` 中记录 implementation authorization。

## Implementation Stage

Implementation 只能在 documentation gate 通过后开始。

1. 添加 direction schema 和 API behavior focused tests。
2. 运行 focused tests，确认预期 RED failure。
3. 添加 additive public direction schemas 和 deterministic classifier。
4. 添加 in-memory queued guidance behavior 和 public summaries。
5. 保持 existing director-guidance compatibility。
6. 运行 focused 和 related tests。
7. 请求 implementation-scope subagent review。
8. 先用 tests 修复 findings。
9. 运行 backend regression。
10. 在 `review.md` 更新 changed files、commands、compatibility、scope、subagent
    findings、unresolved findings 和 final route。

## Files To Create Or Update

Documentation stage：

```text
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.zh.md
```

Implementation stage candidate files：

```text
backend/app/schemas/world_direction.py
backend/app/schemas/world.py
backend/app/api/routes/world.py
backend/app/tests/test_world_direction_boundary.py
backend/app/tests/test_public_handoff_contract_api.py
```

## Files Explicitly Out Of Scope

- `backend/worldengine/`
- frontend files
- checker implementation 和 fixtures
- generated result directories
- Validation Client repository
- provider configuration 或 live provider call paths
- durable scheduler 或 deployment infrastructure

## Review Gates

- Implementation authorization 前进行 documentation/contract evaluator。
- Code changes 后、broad verification 前进行 implementation-scope evaluator。
- Parent route 推进到 `0.9.7` 前进行 closeout consistency review。

## Verification Commands

使用 `test-plan.md` 中的 commands。不得用更窄 checks 声明 package pass。

## Stop Conditions

出现以下情况停止：

- direction handling 开始 mutate final facts。
- user text 可以改变 direct Agent private state、goals、memory、relationship、inventory 或
  life state。
- implementation 需要 live provider interpretation。
- 需要 event legality 或 rule adjudication 才能完成本包。
- 需要 frontend、Validation Client、checker、generated-result、durable scheduler 或
  `backend/worldengine/` changes。
- required subagent checkpoint 报告 unresolved P0/P1 或 blocking P2。

## Handoff After Closeout

如果 implementation clean close，更新 parent v0.9 route 到
`0.9.7-rule-linked-evolution-and-event-legality-documentation-package-needed`。
