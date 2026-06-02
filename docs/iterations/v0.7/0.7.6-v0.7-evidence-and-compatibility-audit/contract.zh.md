# Contract

## Audit Inputs

Audit 必须检查或追踪：

- parent v0.7 docs and review。
- `0.7.0` review。
- `0.7.1` review。
- `0.7.2` review and checker evidence。
- `0.7.3` review and manifest evidence。
- `0.7.4` review and projection read-model evidence。
- `0.7.5` review and evidence matrix。
- current changed-file set。

## 允许变更

- 创建或更新
  `docs/iterations/v0.7/0.7.6-v0.7-evidence-and-compatibility-audit/` 下的文件。
- Audit closeout 后更新 parent v0.7 status 和 route surfaces。

## 禁止变更

- 不修改 runtime、schema、API、frontend、tests、checkers、fixtures、migrations、
  external repositories、generated results 或 `backend/worldengine/`。
- 不添加新的 validation behavior。
- 不标记 v0.7 final。
- 不在没有 explicit blocker status 的情况下接受 unresolved P1/P2。

## Required Audit Questions

- 所有 child package reviews 是否存在且 internally consistent？
- `0.7.5` command evidence 是否只支持 checker/schema/manifest compatibility claims？
- 未运行的 runtime/API/frontend/E2E/live Agent/full autonomous/external suite/projection app/product/generation/release checks 是否仍被排除？
- 是否有 approved v0.7 scope 外的 implementation file changed？
- Unresolved findings 是否完成 P1/P2/P3 classification？

## Closeout Gate

Closeout 只能在以下条件满足后发生：

- audit report 存在。
- traceability checks 通过。
- `git diff --check` 通过。
- changed-file scope guard 通过。
- documentation/audit 和 closeout consistency evaluators 未报告 blocking findings。
