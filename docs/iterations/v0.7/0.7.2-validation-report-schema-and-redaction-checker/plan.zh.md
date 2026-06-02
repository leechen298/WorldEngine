# Plan

## Phase 1: Documentation Gate

1. 读取 parent v0.7 state、`0.7.1` reviewed contracts、validation report template、
   external fixture runner contract，以及 existing saved-result checker patterns。
2. Draft this package document set and Chinese mirrors。
3. 运行 `test-plan.md` 中的 documentation-gate checks。
4. 使用 read-only subagent/evaluator review 检查 documentation、contract、mirror
   和 scope consistency。
5. 修复 P0/P1/P2 findings，或停止。
6. 只有 documentation/contract gate 通过后，才记录 evaluator findings 并设置
   `implementation_authorized: yes`。

## Phase 2: Implementation

1. Add `docs/testing/external-validation-report-schema.json`。
2. Add `tools/testing/validate_external_validation_report.py`。
3. Add `tools/testing/test_validate_external_validation_report.py`。
4. Additively update `docs/validation-report-template.md`。
5. 保持 implementation 只在 approved files 内。

## Phase 3: Verification

1. Run focused checker tests。
2. 如果触及 shared assumptions，运行 existing Agent smoke/autonomous checker tests；
   或运行它们证明 saved-result checker 没有 regression。
3. Run `git diff --check`。
4. Run changed-file scope guard。
5. 使用 implementation-scope evaluator、code-review evaluator、validation-evidence evaluator。
6. 修复或明确处理每个 P0/P1/P2 finding。

## Phase 4: Closeout

1. Update `review.md` and `review.zh.md`，记录 exact command evidence、
   compatibility review、scope review、evaluator evidence、unresolved findings
   和 final assessment。
2. Update parent v0.7 route/status surfaces，handoff 到
   `0.7.3-contract-bundle-and-readiness-manifest`。
3. Run closeout consistency review。
4. Parent and child status surfaces 不一致时停止。

## Stop Conditions

- Checker 需要 private fixture data、concrete external world details、UI
  selectors、oracle internals、private paths、transcripts 或 non-redacted event
  payloads 才能 validate report。
- `blocked`、`skipped` 或 `out_of_scope` 无法与 `pass` 区分。
- Redaction rules 弱于 `0.7.1` 或 report template。
- Required evaluator 返回 unresolved P0/P1 或 blocking P2。
- Scope guard 报告 out-of-scope changed files。

## Review Update Step

每个改变文件的 phase 都必须在 claim completion 前更新 package review evidence。
未运行的 tests 必须明确记录原因。
