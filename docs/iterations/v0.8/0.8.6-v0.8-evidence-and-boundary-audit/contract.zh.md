# Contract

## Public Concepts

- `EvidenceReference`：作为 bounded v0.8 claim 证据的 path、command result 或 package
  review entry。
- `AuditFinding`：检查 evidence、boundaries、compatibility、status 或 redaction 时发现的
  P1/P2/P3 issue。
- `AuditDisposition`：`clear`、`blocked`、`carry_forward_p3`、`out_of_scope` 或
  `not_claimed`。
- `ReleaseCandidateRecommendation`：`recommended`、`blocked` 或
  `defer_pending_review`。

## Allowed Changes

Documentation stage：

- 创建或更新本 package docs 和 Chinese mirrors。
- 在本 package 下创建 audit report template。
- 将 parent v0.8 status surfaces 更新为 ready-for-review。

Audit stage after review：

- 填写 `audit-report.md` 和 `audit-report.zh.md`。
- 在本 package `review.md` 及 mirror 中记录 command results、findings 和 release-candidate
  recommendation。
- 只有 package review 授权 closeout 时，才更新 parent route。

## Forbidden Changes

- 不得修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository、external validator、external application、
  deployment 或 `backend/worldengine/` files。
- 不得在本 package 内 repair code。
- 不得添加不是 documentation/audit checks 的新 evidence commands。
- 不得隐藏 unresolved P1/P2 findings。
- 不得把 skipped、blocked、out-of-scope、stale 或 historical evidence 转换为 PASS。
- 不得声明 external validation PASS、external consumer PASS、product readiness、
  frontend/E2E PASS、Agent smoke PASS、autonomous PASS、generation-quality PASS 或 final v0.8
  readiness。

## Required Audit Surfaces

Audit 必须覆盖：

- `0.8.0` 到 `0.8.5` package status 和 review evidence。
- v0.7 blocker 与 `0.7.9` checker/docs repair handoff boundaries。
- v0.3 loader/runtime bridge、v0.4 Agent loop、v0.5 memory、v0.6 generation 和 v0.7
  public contract compatibility references。
- `0.8.5` skipped/out-of-scope classifications。
- redaction 和 private-detail exclusions。
- parent route/status synchronization。

## Closeout Rule

只有在没有 unresolved P1 或 blocking P2 时，本 package 才可推荐
`0.8.7-v0.8-release-candidate-bundle`。P3 只有在 audit report 明确命名 issue 并说明其为何不阻塞
release-candidate packaging 时，才可 carry forward。
