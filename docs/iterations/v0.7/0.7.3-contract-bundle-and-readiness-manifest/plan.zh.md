# Plan

## Phase 1: Documentation Gate

1. 读取 `0.7.1` contracts、`0.7.2` schema/checker evidence、current API references、
   contract docs、release docs 和 parent v0.7 state。
2. Draft package docs and Chinese mirrors。
3. 运行 `test-plan.md` 中的 documentation-gate checks。
4. 使用 documentation/contract evaluator 和 mirror/scope evaluator。
5. 修复 P0/P1/P2 findings，或停止。
6. 只有 evaluator approval 后，才记录 `implementation_authorized: yes`。

## Phase 2: Implementation

1. Add readiness manifest schema。
2. Add v0.7 readiness manifest。
3. Add readiness manifest checker。
4. Add focused checker tests。
5. 保持 implementation isolated to approved files。

## Phase 3: Verification

1. Run focused manifest checker tests。
2. Run external validation report checker tests as adjacent regression。
3. Run `git diff --check`。
4. Run changed-file scope guard。
5. 使用 implementation-scope、code-review、validation-evidence 和 closeout consistency evaluators。
6. 修复或明确处理每个 P0/P1/P2 finding。

## Phase 4: Closeout

1. Update package review evidence。
2. Update parent v0.7 route/status surfaces，handoff to `0.7.4`。
3. Run closeout consistency review。
4. Parent and child status surfaces 不一致时停止。

## Stop Conditions

- Manifest 需要 private runner state 或 private repository paths。
- Manifest 在没有 accepted evidence 的情况下暗示 external suite PASS。
- Public contract identifiers 与 actual docs drift。
- Scope guard 报告 out-of-scope files。
- Required evaluator 返回 unresolved P0/P1 或 blocking P2。

## Review Update Step

每个改变文件的 phase 都必须在 claim completion 前更新 `review.md`。未运行的 tests
必须明确记录原因。
