# Plan

## Phase 1: Draft Closeout

1. 创建 package docs 和中文镜像。
2. 创建 `final-closeout.md` 和中文镜像。

## Phase 2: Final Verification

1. 运行 checker regression 和 CLI validation。
2. 运行 JSON parse checks。
3. 运行 docs/evidence link checks。
4. 运行 `git diff --check` 和 scope guard。

## Phase 3: Final Review

1. 更新 final closeout evidence。
2. Use final evaluator and mirror/scope evaluator。
3. 修复 blockers 或停止。

## Phase 4: Parent Final Status

1. 如果 evaluators pass，更新 parent v0.7 status surfaces 为 `final / closeout complete`。
2. 在 parent review 记录 final status。

## Stop Conditions

- 任一 final command fails。
- 任一 P1/P2 remains unresolved。
- Scope guard reports out-of-scope files。
- Final closeout would imply unrun product/runtime/external claims。
