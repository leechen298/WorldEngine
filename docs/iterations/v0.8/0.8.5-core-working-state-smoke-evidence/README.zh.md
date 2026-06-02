# 0.8.5 Core Working State Smoke Evidence

状态：review complete
类型：mixed validation package
implementation_authorized: no
evidence_execution_authorized: yes, limited to exact commands in `test-plan.md`

## 目的

本 package 定义 v0.8 在后续讨论 minimum working-state readiness 前必须运行的 core-side
smoke evidence。它不运行或实现 external validator，也不声明 product-readiness 或
external-validation PASS。

本 package 准备这些 public core surfaces 的 evidence：

```text
WorldSpec schema and loader
  -> generation preview/regeneration/runtime-readiness
  -> core-readiness probe
  -> runtime step and event evidence
  -> Agent loop perception/action evidence
  -> memory-context and archive compatibility
  -> handoff status classification
```

## 当前状态

当前 reviewed inputs 包括：

- `0.8.1` minimum working-state taxonomy。
- `0.8.2` observable surface boundaries。
- `0.8.3` core-readiness route 和 focused backend/API evidence。
- `0.8.4` external-validation handoff contract。
- v0.7 `0.7.9` checker/docs repair evidence 只作为 handoff context。

`0.8.5` 必须把这些 inputs 转换为 core-side evidence 的 current-session command matrix。
任何 skipped、blocked 或 out-of-scope surface 都必须明确分类。

## Evidence Scope

Review 后 in-scope：

- 针对 generation、runtime context、runtime step、Agent loop、memory context、archive 和
  core-readiness surfaces 的 focused backend/API/schema tests。
- 如果需要确认 v0.7 handoff compatibility，可运行 repository-local 的 focused public
  contract/checker commands。
- changed-file 和 artifact scope guards。
- redaction 和 overclaim scans。
- 只有 reviewed test plan 授权时，才可在 `docs/testing/results/` 下生成 documentation result
  artifacts。

除非后续 reviewed package 授权，否则 out of scope：

- external validator execution。
- external app 或 projection app execution。
- product-specific scenarios 或 acceptance targets。
- frontend feature changes。
- runtime/API behavior changes。
- checker/schema/template implementation changes。
- fixture 或 migration changes。
- `backend/worldengine/` work。

## Review Gate

Read-only documentation/contract review 已通过且无 P1/P2/P3 findings。`review.md` 记录
bounded `evidence_execution_authorized: yes`，且只限 `test-plan.md` 中的 exact commands；
这些 commands 已在 bounded proof surfaces 内通过。Validation-evidence review 已通过且无 blocking
findings。Implementation 仍未授权。
