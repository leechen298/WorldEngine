# Plan

## Phase 1: Documentation Gate

1. 读取 `0.7.1` projection consumer contract、`0.7.3` readiness manifest evidence，
   以及 current runtime/event/Agent/memory/generation/API docs。
2. Draft package docs and Chinese mirrors。
3. Run documentation-gate checks。
4. 使用 documentation/contract 和 mirror/scope evaluators。
5. 修复 P0/P1/P2 findings，或停止。
6. 只有 evaluator approval 后，才记录 `implementation_authorized: yes`。

## Phase 2: Implementation

1. Add projection read-model contract。
2. Add projection read-model schema。
3. Add projection read-model checker。
4. Add focused checker tests。

## Phase 3: Verification

1. Run focused projection read-model checker tests。
2. Run readiness manifest checker tests as adjacent regression。
3. Run `git diff --check` 和 changed-file scope guard。
4. 使用 implementation-scope、code-review、validation-evidence 和 closeout consistency evaluators。

## Phase 4: Closeout

1. Update review evidence。
2. Update parent v0.7 route/status surfaces，handoff to `0.7.5`。
3. Run closeout consistency review。

## Stop Conditions

- Any read model 需要 product-specific 或 concrete world semantics。
- Projection surface mutates runtime 或暗示 write capability。
- Projection contract readiness 被混同为 v0.8 app readiness。
- Scope guard reports out-of-scope files。

## Review Update Step

每个改变文件的 phase 都必须更新 `review.md`；未运行的 tests 必须明确记录原因。
