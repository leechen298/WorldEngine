# Contract

## Public Concepts

- `ReadinessManifest`：public、machine-readable index，记录 WorldEngine readiness
  surfaces 和 evidence classifications。
- `ContractSurface`：external consumer 可读取的 public document、schema 或 template path。
- `CapabilityArea`：generic public capability label，例如 external validation readiness、
  redacted report validation 或 projection consumer boundary。
- `ReadinessClaim`：reviewed v0.7 contracts 中的 scoped taxonomy value。
- `EvidenceReference`：public、redacted evidence path 或 checker command reference。
  除非有 current-session evidence 并被明确分类，否则它不是 external suite PASS。

## Manifest Semantics

Manifest 必须包含：

- manifest id。
- manifest version。
- engine version or reference。
- generated source classification。
- public contract surfaces。
- public schema surfaces。
- public template surfaces。
- supported readiness claim values。
- capability areas。
- redacted evidence references。
- compatibility notes。
- redaction rules。

必须包含的 public surface paths：

- `docs/contracts/external-fixture-runner-contract.md`
- `docs/contracts/external-validation-readiness-contract.md`
- `docs/contracts/projection-consumer-contract.md`
- `docs/testing/external-validation-report-schema.json`
- `docs/validation-report-template.md`
- `tools/testing/validate_external_validation_report.py`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md`

Manifest 可以在 `readiness_claim_values` taxonomy section 中列出 reviewed taxonomy
values，包括 PASS-like values；这个列表本身不是证据。`evidence_references[*].status`
更严格：本 package 只能使用 `contract ready`、`report format ready`、`blocked`、
`skipped` 或 `out of scope`。Checker 必须拒绝 evidence references 中的
`external suite pass`、`external consumer pass` 和 `core-side compatibility ready`，
除非后续 reviewed package 为这些状态增加 current-session accepted evidence rules。

Manifest 不得包含 private runner state、private paths、concrete world details、UI
selectors、hidden reset details、oracle internals、seed data、transcripts 或
non-redacted event payloads。

## Allowed Changes

- 创建或更新
  `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/`。
- 创建或更新本 child package 中文镜像。
- 创建 `docs/contracts/v0.7-readiness-manifest-schema.json`。
- 创建 `docs/contracts/v0.7-readiness-manifest.json`。
- 创建 `tools/testing/validate_readiness_manifest.py`。
- 创建 `tools/testing/test_validate_readiness_manifest.py`。
- Review 和 closeout 后更新 parent v0.7 status and route surfaces。

## Forbidden Changes

- 不修改 runtime、API routes、frontend、persistence、migrations、generated results、
  external repositories、fixture runners 或 `backend/worldengine/`。
- 不添加 private external suite configuration、private repository paths、
  concrete external world data、concrete world names、character names、location
  names、story rules、seed data、UI selectors、hidden reset API details、
  validation oracle internals、transcripts 或 non-redacted event payloads。
- 不创建 product app behavior、projection read models、write APIs、persistence、
  migrations、release packaging 或 external suite automation。
- 不声明 external suite PASS、projection application readiness、product readiness、
  release readiness、runtime PASS、API PASS、frontend PASS、E2E PASS、live Agent
  smoke PASS 或 full autonomous PASS。

## Compatibility Requirements

- Existing contract docs 保持有效。
- Existing external validation report schema/checker behavior 保持兼容。
- Manifest fields 必须 additive and versioned。
- Manifest paths 必须是 public repository-relative paths。
- Historical v0.6 evidence 只能作为 handoff context 引用，不能作为 v0.7 PASS evidence。

## Review Gates

Implementation 只有在以下条件满足后才能开始：

- package docs 与中文镜像存在。
- documentation/contract evaluator 报告无 P0/P1 且无 blocking P2。
- package `review.md` 记录 `implementation_authorized: yes`。

Closeout 只有在以下条件满足后才能进行：

- focused manifest checker tests 通过。
- 如果 manifest 引用 external validation report schema/checker，则 existing external
  validation report checker tests 通过。
- `git diff --check` 通过。
- changed-file scope guard 通过。
- implementation-scope、code-review、validation-evidence 和 closeout consistency
  evaluators 无 blocking findings。

## Out-of-Scope Follow-ups

- `0.7.4`：projection consumer read-model contracts。
- `0.7.5`：quality regression and compatibility evidence。
- `0.7.6`：evidence and compatibility audit。
- `0.7.7`：release-candidate bundle。
- `0.7.8`：final closeout。
