# Plan

英文镜像：`plan.md`。

## 目标

准备并在 review approval 后执行窄范围 repair，修复 current-product validation 中发现的
`dashboard-archive-summary` E2E regression。

## 已读取的权威输入

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/README.md`
- `docs/testing/e2e-scenarios/dashboard-archive-summary.md`
- `frontend/e2e/dashboard.spec.ts`

## 创建或更新文件

创建：

```text
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/intent.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/intent.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/contract.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/contract.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/technical-design.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/technical-design.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/test-plan.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/test-plan.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/plan.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/plan.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.zh.md
```

更新：

```text
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

## 明确不在范围内

- Documentation stage 不修改 runtime、schema、API、frontend、E2E、fixture、
  migration 或 checker implementation。
- 不修改 Validation Client repository。
- 不执行 LLM-backed lifecycle validation。
- 不实现或测试 DeepSeek/provider。
- 不重写 generated validation results。

## 必需状态值

Documentation drafting 期间：

```text
Status: drafted / ready for user review
implementation_authorized: no
evidence_execution_authorized: no
```

Review approval 后，implementation 可更新为：

```text
implementation_authorized: yes
```

## Phase 1: Documentation Gate

1. 读取 required governance 和 package context。
2. 起草 full package docs 和 Chinese mirrors。
3. 添加 parent v0.8 route/status references。
4. 运行 documentation-stage checks。
5. 停在 implementation 前。

## Phase 2: Review And Authorization

Implementation 只有在以下条件满足后才可开始：

1. documentation/contract evaluator 或 reviewer 记录无 P0/P1 且无 blocking P2。
2. `review.md` 记录 approval。
3. Package 和 parent status 中可见 `implementation_authorized: yes`。

## Phase 3: Reproduce And Diagnose

1. 运行 focused E2E scenario。
2. 如果失败，收集 API/UI/artifact evidence。
3. 如果一次通过，则再重跑一次并收集 state 来判断 intermittency。
4. 记录一个 root-cause bucket。

## Phase 4: Minimal Repair

1. 按 evidence 选择 backend、frontend 或 E2E harness repair。
2. Changes 保持在 allowed files 内。
3. 保留 newer-summary creation 和 render assertions。
4. 只有 touched path 需要时才添加 focused regression coverage。

## Phase 5: Verification

运行 `test-plan.md` 中的 commands：

1. focused E2E。
2. broad E2E。
3. 根据 touched files 运行 adjacent backend/frontend regressions。
4. latest basic full lifecycle saved-result checker。
5. `git diff --check`。

## Phase 6: Required Evaluators

Implementation-bearing closeout 按可用情况使用仓库 evaluator/subagent model：

1. implementation authorization 前的 documentation/contract evaluator。
2. 文件变更后的 implementation-scope evaluator。
3. focused verification 后的 code-review evaluator。
4. PASS claims 前的 validation-evidence evaluator。
5. final assessment 前的 closeout consistency evaluator。

## Stop Conditions

- root cause 需要 Validation Client changes 时停止。
- fix 需要 LLM-backed/provider work 时停止。
- repair 需要 broad archive redesign 时停止。
- 任何 P1 未解决时停止。
- blocking P2 没有 accepted rationale 时停止。
- 唯一通过方式是 skip/weaken failing test 时停止。
- evidence 需要重写 generated result directories 时停止。

## Approval 后交接

Implementation 应使用本 package 和 `worldengine-iteration-dev`。后续 agent 可以在不要求
用户手动调度每个子步骤的情况下完成整个 repair，只要保持在本 contract 内并记录 evidence。
