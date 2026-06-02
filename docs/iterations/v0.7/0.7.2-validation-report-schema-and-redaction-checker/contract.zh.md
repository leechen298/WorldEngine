# Contract

## Public Concepts

- `ExternalValidationReport`：machine-readable、redacted report，用来描述针对
  reviewed WorldEngine contract surface 的 public behavior。
- `ReportStatus`：`pass`、`fail`、`blocked`、`skipped` 或 `out_of_scope`。
- `RedactionConfirmation`：required boolean confirmation，确认 forbidden external
  consumer details 已移除。
- `ForbiddenDetailReview`：required object，其中列出的 forbidden detail flags 必须
  为 false，report 才能被接受。
- `RedactionRiskScan`：generic checker logic，在不需要 private fixture data 的情况下，
  拒绝明显的 private paths、UI-selector markers、hidden reset markers、
  oracle-internal markers、seed-data markers、transcript markers 和 non-redacted
  external event payload markers。

## Report Semantics

Schema/checker 必须保留这些 fields：

- report id。
- engine commit or version reference。
- public contract surface exercised。
- external suite id。
- redacted target id。
- capability area。
- abstract scenario id。
- high-level public goal。
- status：`pass`、`fail`、`blocked`、`skipped` 或 `out_of_scope`。
- observed public behavior。
- redacted evidence summary。
- compatibility notes。
- unresolved P1/P2/P3 findings。
- redaction confirmation。
- forbidden detail review。
- scope review。

`pass` 只有在 redaction confirmation 为 true、forbidden detail flags 全部为 false、
required public-behavior evidence 存在、且没有 unresolved P1/P2 finding 时才有效。
`blocked`、`skipped`、`out_of_scope` 不是 pass equivalents，并且必须包含 explicit reasons。

## Allowed Changes

- 创建或更新
  `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/`。
- 创建或更新本 child package 的中文镜像。
- 创建 `docs/testing/external-validation-report-schema.json`。
- 创建 `tools/testing/validate_external_validation_report.py`。
- 创建 `tools/testing/test_validate_external_validation_report.py`。
- Additively update `docs/validation-report-template.md`。
- Review 和 closeout 后更新 parent v0.7 status and route surfaces：
  - `docs/iterations/v0.7/README.md`
  - `docs/iterations/v0.7/README.zh.md`
  - `docs/iterations/v0.7/v0.7-plan.md`
  - `docs/iterations/v0.7/v0.7-plan.zh.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.7/CURRENT_STATE.md`
  - `docs/iterations/v0.7/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.7/review.md`
  - `docs/iterations/v0.7/review.zh.md`

## Forbidden Changes

- 不修改 runtime、core schemas、API routes、frontend、persistence、migrations、
  fixture runners、generated result artifacts、external repositories 或
  `backend/worldengine/`。
- 不添加 concrete external validation world data、concrete world names、
  character names、location names、story rules、seed data、private transcripts、
  UI selectors、hidden reset API details、private fixture paths、oracle internals
  或 non-redacted external event payloads。
- 不创建 consumer-specific example reports。Tests 只能使用 abstract identifiers，
  例如 `external-suite-001`、`target-redacted-001` 和 `scenario-001`。
- 不削弱 `docs/contracts/external-validation-readiness-contract.md` 或
  `docs/contracts/external-fixture-runner-contract.md`。
- 不声明 external suite PASS、projection application readiness、product readiness、
  release readiness、runtime PASS、API PASS、frontend PASS、E2E PASS、
  Agent smoke PASS 或 autonomous PASS。

## Compatibility Requirements

- Existing Agent smoke 和 Agent autonomous saved-result schemas/checkers 必须保持不变，
  除非明确触及 shared-tooling dependency。本 package 应避免 shared-tooling changes。
- `docs/validation-report-template.md` 的变化必须 additive，并与 `0.7.1`
  readiness semantics 对齐。
- Checker 必须只使用 Python standard library，除非 package review 明确扩展 dependencies。
- Runtime/API/frontend behavior 必须保持不变。
- Schema/checker 不得要求 private consumer details 才能 validate report。

## Review Gates

Implementation 只有在以下条件满足后才能开始：

- package docs 与中文镜像存在。
- documentation/contract evaluator 报告无 P0/P1 且无 blocking P2。
- package `review.md` 记录 `implementation_authorized: yes`。

Closeout 只有在以下条件满足后才能进行：

- focused checker tests 通过。
- `git diff --check` 通过。
- changed-file scope guard 通过。
- implementation-scope evaluator 无 blocking findings。
- code-review evaluator 无 blocking findings。
- validation-evidence evaluator 确认 command evidence 已记录且没有 overclaiming。
- closeout consistency review 确认 parent 与 child status surfaces 对齐。

## Out-of-Scope Follow-ups

- `0.7.3`：contract bundle and readiness manifest。
- `0.7.4`：projection read-model contracts and any approved implementation。
- `0.7.5`：current-core compatibility evidence package。
- `0.7.6`：release-candidate bundle。
- `v0.8`：projection application readiness。
