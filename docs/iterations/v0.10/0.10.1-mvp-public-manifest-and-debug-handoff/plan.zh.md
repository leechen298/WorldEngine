# Plan

## Ordered Execution Steps

1. 读取治理文档和当前 v0.10 route。
2. 读取现有 `/manifest` schema、route 和 focused tests。
3. 起草本 package document set 和 mirrors。
4. 运行 read-only documentation / contract evaluator。
5. 如果无 P1/blocking P2，更新 `review.md` 记录 `implementation_authorized: yes`。
6. 在 `backend/app/schemas/world.py` 实现 additive schema changes。
7. 更新 `backend/app/api/routes/world.py` 的 `/manifest` construction。
8. 更新 `backend/app/tests/test_public_handoff_contract_api.py` focused manifest tests。
9. 运行 `test-plan.md` 中的 exact commands。
10. 运行 implementation-scope 和 code/evidence evaluator checkpoints。
11. 修复 in-scope findings 或记录 blockers。
12. 更新 package 和 parent reviews，记录 changed files、commands、results、compatibility
    review、scope review、unresolved findings 和 handoff。
13. 如果 closeout 通过，将 parent route 推进到
    `0.10.2-world-session-contract-and-state-store-documentation-package-needed`。

## Phase Boundaries

Documentation phase：

- 创建并 review package documents。
- 在 `review.md` 记录 `implementation_authorized: yes` 前，不编辑 implementation files。

Implementation phase：

- 只编辑 allowed schema、route 和 focused test files。
- 保持 changes additive and redacted。

Verification phase：

- 运行 focused tests 和 documentation checks。
- final route closeout 前使用 evaluator checkpoints。

## Stop Conditions

遇到以下情况停止：

- required package docs 或 mirrors 缺失。
- documentation / contract evaluator 报告 unresolved P1 或 blocking P2。
- implementation 需要 approved scope 外文件。
- manifest work 需要 session state、runtime execution、provider live calls、checker fixtures、
  frontend、Validation Client、generated results、migrations 或 external repository changes。
- secret/raw/private data 会出现在 public manifest output。
- planned/future session surfaces 会在 implementation 前被报告为 `pass` 或 `available`。

## Review Update Step

implementation 前，记录 documentation review gate 和 authorization decision。closeout 前，
更新 `review.md` 和 parent v0.10 review，记录：

- changed files。
- commands run。
- test results。
- subagent/evaluator evidence。
- compatibility review。
- scope review。
- unresolved findings。
- final assessment and handoff route。
