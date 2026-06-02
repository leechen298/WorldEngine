# Contract

## Public Concepts

- `EvidenceMatrix`：package-local table，记录 command coverage、result 和 claim boundary。
- `SupportedClaim`：由 current-session command 支撑的 claim。
- `SkippedCheck`：未运行的 command 或 surface，包含 reason 和 impact。
- `OutOfScopeCheck`：超出本 package contract 的 surface。

## 允许的 Evidence Surfaces

本 package 只允许运行并记录现有文件的证据：

- external validation report checker tests。
- readiness manifest checker tests。
- projection read-model checker tests。
- Agent smoke saved-result checker tests。
- Agent autonomous saved-result checker tests。
- v0.7 schema/manifest JSON parsing。
- existing v0.7 checker entrypoints 的 CLI validation。
- `git diff --check`。
- changed-file scope guard。

## Required Classification

Evidence matrix 必须把这些 surfaces 标记为 passed、failed、blocked、skipped 或 out of scope：

- external validation report schema/checker。
- readiness manifest schema/checker。
- projection read-model schema/checker。
- Agent smoke saved-result checker。
- Agent autonomous saved-result checker。
- backend runtime/API behavior。
- frontend behavior。
- browser E2E。
- live Agent smoke。
- full autonomous runner/full suite。
- external validation suite。
- projection application readiness。
- product readiness。
- generation-quality readiness。
- release readiness。

## 允许变更

- 创建或更新
  `docs/iterations/v0.7/0.7.5-quality-regression-and-compatibility-evidence/` 下的文件。
- 创建或更新 package-local `evidence-matrix.md` 和中文镜像。
- Review 和 closeout 后更新 parent v0.7 status 与 route surfaces。

## 禁止变更

- 不修改 runtime、API、frontend、backend product code、migrations、persistence、fixtures、
  external repositories、generated result fixtures 或 `backend/worldengine/`。
- 本 package 不添加或改变 checker behavior、tests、schemas 或 contracts。
- 不声明任何没有 current-session command 支撑的 PASS。
- 不把 v0.6 handoff evidence 作为 current v0.7 PASS evidence。

## 兼容性要求

- Existing v0.7 checker behavior 保持不变。
- Evidence claims 必须匹配 exact command surface。
- Historical evidence 只能作为 handoff context。
- Unrun checks 必须被分类，不能暗示 hidden PASS。

## Review Gates

Evidence execution 只能在以下条件满足后开始：

- package docs 和中文镜像存在。
- documentation/contract evaluator 未报告 P0/P1 或 blocking P2。
- package `review.md` 记录 `evidence_execution_authorized: yes`。

Closeout 只能在以下条件满足后发生：

- in-scope commands 已运行或被诚实分类。
- `evidence-matrix.md` 记录 exact results 与 exclusions。
- `git diff --check` 通过。
- changed-file scope guard 通过。
- validation-evidence 和 closeout consistency evaluators 未报告 blocking findings。
