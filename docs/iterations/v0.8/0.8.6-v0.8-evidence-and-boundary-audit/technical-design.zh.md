# Technical Design

## Audit Shape

Audit report 使用五个 matrix：

1. Package status matrix：`0.8.0` 到 `0.8.5` 的 status、review source、evaluator
   source 和 closeout state。
2. Evidence reference matrix：command result、source file、proof boundary 和 claim
   allowed。
3. Compatibility matrix：v0.3 到 v0.7 compatibility surfaces 以及 current v0.8 evidence
   relationship。
4. Boundary matrix：external validation、product readiness、frontend/E2E、Agent smoke、
   autonomous、generation-quality 和 final readiness non-claims。
5. Findings matrix：P1/P2/P3、source、disposition 和 handoff impact。

## Evidence Source Rules

- Current-session evidence 只能支持其 package review 中记录的 exact proof boundary。
- Historical v0.7 和 v0.6 evidence 只能作为 handoff context。
- `0.8.5` 中 v0.7 checker 和 contract commands 是 handoff compatibility，不是 external
  validation PASS。
- Skipped 或 out-of-scope checks 不是 PASS。

## Audit Report Generation

Audit stage 从以下来源填写 `audit-report.md` 和 `audit-report.zh.md`：

- parent route/status docs。
- child package reviews。
- `docs/testing/results/` 下的 testing result docs。
- reviews 引用的 repository-local contract paths。

Report 必须使用明确 file path citations，并避免 private external app 或 validator details。

## Release-Candidate Recommendation

Recommendation 只有在以下条件都满足时才是 `recommended`：

- all required evidence references resolve。
- no P1 或 blocking P2 remains。
- status surfaces synchronized。
- no forbidden private detail 或 overclaim 被接受。
- skipped/out-of-scope checks visible。

否则为 `blocked` 或 `defer_pending_review`。
