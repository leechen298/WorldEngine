# Plan

英文版本：`plan.md`。

## Objective

准备，并在 review approval 后执行一个窄修复：解决阻塞 full lifecycle autonomous
validation checker 的 public director guidance redaction failure。

## Phase 1: Documentation Gate

1. 读取 root 和 iteration agent rules。
2. 读取 v0.8 current state 和 0.8.9 handoff documents。
3. 读取失败的 full lifecycle validation result 和 scenario contract。
4. 起草本 package 的完整 document set 和 mirrors。
5. 保持 `implementation_authorized: no`。
6. 运行 documentation-stage checks。
7. 派发 read-only documentation/contract evaluator。
8. 在 review approval 记录前停止，不做 runtime 或 test implementation。

## Phase 2: Implementation Authorization

只有满足以下条件后才可开始 implementation：

1. documentation/contract evaluator 无 P0/P1 且无 blocking P2。
2. package review 记录 `implementation_authorized: yes`。
3. 已检查 working tree dirty scope。

## Phase 3: RED Test

1. 更新 focused director guidance test，使其拒绝 forbidden public evidence
   markers。
2. 运行 focused test。
3. 记录当前代码下的 expected failure。

## Phase 4: Runtime Repair

1. 只修改 public director guidance explanation wording。
2. 保持 response schema、operation id、event type 和 event payload safety。
3. 不向 public output 添加 private marker terms。

## Phase 5: Checker Coverage

1. 检查当前 checker 对 direct API operation-log rejection 的 behavior。
2. 只有 current coverage 不足时才补 focused checker regression。
3. 不放松任何 checker rule。

## Phase 6: Verification

按 `test-plan.md` 顺序运行：

1. focused backend test。
2. related 0.8.9.1 regression set。
3. full backend regression。
4. historical saved-result checker，预期仍为 FAIL。
5. optional runtime probe。
6. 只有 review 记录 `evidence_execution_authorized: yes` 时，才重跑 new full
   lifecycle run 和 checker；否则记录 rerun 为 not authorized。
7. `git diff --check`。

## Phase 7: Required Evaluators

使用 `/goal` subagent checkpoints：

1. implementation authorization 前的 documentation/contract evaluator。
2. files changed 后、broad verification 前的 implementation-scope evaluator。
3. focused tests 后、broad regression 或 autonomous validation claims 前的
   code-review evaluator。
4. 记录 checker、API smoke 或 autonomous validation claims 前的
   validation-evidence evaluator。
5. final assessment 前的 closeout consistency evaluator。

## Stop Conditions

- 如果 implementation 需要 Validation Client changes，停止。
- 如果 implementation 需要 concrete validation-world content，停止。
- 如果 public output 仍包含 forbidden private/internal markers，停止。
- 如果仍有 P1，停止。
- 如果仍有未明确接受 rationale 的 P2，停止。
- 如果 full lifecycle PASS 依赖改写旧 failed result，停止。
- 任何 live full lifecycle rerun 前，如果本 package review 未记录
  `evidence_execution_authorized: yes`，停止。

## Review Update Step

implementation 实际运行后，更新 `review.md` 和 `review.zh.md`，记录 changed files、
commands、test results、compatibility review、scope review、subagent findings、
unresolved findings 和 final assessment。
