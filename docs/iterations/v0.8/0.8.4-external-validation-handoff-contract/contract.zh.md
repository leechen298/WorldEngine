# Contract

## Public Concepts

- `ExternalValidationHandoff`：public、core-side contract，描述 WorldEngine 可以为未来
  external validation function 暴露或记录什么。
- `HandoffSurface`：core-side surface 的 stable public identifier，例如
  `generation_core_readiness`、`runtime_context_summary`、`agent_loop_probe`、
  `readiness_manifest` 或 `projection_read_model`。
- `HandoffEvidenceReference`：repository-relative、redacted 的 current-session evidence
  reference。除非同时有生成它的 command 或 review result，否则它本身不是证据。
- `HandoffStatus`：`contract_ready`、`core_evidence_ready`、`blocked`、`skipped` 或
  `out_of_scope`。
- `HandoffEvidenceClass`：`documentation`、`schema_checker`、`api_backend`、
  `frontend_e2e`、`agent_smoke`、`autonomous`、`external_validation` 或
  `manual_review`。
- `RedactionConfirmation`：必须声明 public evidence 已排除 forbidden private details。
- `ForbiddenDetailReview`：必须分类是否存在 forbidden detail classes。
- `BlockerSemantics`：防止 `blocked`、`skipped` 和 `out_of_scope` 被当作 PASS 的规则。

## Handoff Semantics

`contract_ready` 表示 public contract surface 已 review。它不表示 runtime behavior、
external validation、product readiness 或 v0.8 readiness passed。

`core_evidence_ready` 只能由后续 reviewed evidence package 使用，且必须有 current-session
commands 证明 named core-side surface，并在 review 中记录 exact evidence。本 package 只定义
该术语，不把它用作 PASS claim。

`blocked`、`skipped` 和 `out_of_scope` 不是 pass equivalents。每个都必须包含 reason、
affected surface id、evidence class，以及 next-action 或 handoff note。

`external_validation` 作为 evidence class 只能作为 future class 被命名。本 package 不授权运行
external validator，也不接受 external validation PASS evidence。

## Allowed Handoff Fields

未来 handoff records 只能包含这些 public field classes：

- handoff id 和 version。
- engine version、commit 或 package reference。
- public handoff surface id。
- public contract surface path。
- evidence class。
- handoff status。
- repository-relative redacted evidence reference。
- 可用时的 command 或 review evidence reference。
- redaction confirmation。
- forbidden-detail review。
- unresolved P1/P2/P3 findings。
- blocker、skipped 或 out-of-scope rationale。
- compatibility notes。
- scope review notes。

## Forbidden Detail Classes

Public handoff records 不得包含：

- private external repository paths。
- external validator connection details 或 commands。
- private runner state。
- private scenarios、oracle internals 或 acceptance targets。
- product UI selectors、screenshots、transcripts 或 product routes。
- concrete external validation worlds、maps、characters、locations、resources、
  story rules、seed data 或 product content。
- hidden reset APIs、write hooks、persistence hooks 或 private fixture hooks。
- provider traces、raw prompts、secrets、credentials 或 non-redacted external event payloads。
- raw memory records 或 private application state。

## Allowed Changes

- 创建或更新 `docs/iterations/v0.8/0.8.4-external-validation-handoff-contract/` 下的文件。
- 创建或更新本 package 的 Chinese mirrors。
- Documentation review 后更新 parent v0.8 route/status/review surfaces。

## Forbidden Changes

- 不修改 runtime、schema、API、frontend、backend test、checker implementation、fixture、
  migration、generated result、external repository、external validator code、external
  application code 或 `backend/worldengine/` implementation files。
- 本 package 不创建 `docs/contracts/` schemas、`tools/testing` checkers、report templates、
  generated evidence artifacts 或 public API surfaces。
- 不实现 external validator connection workflow、automation commands、private scenario
  contracts、oracle behavior、product UI、app repository layout 或 product-specific
  acceptance criteria。
- 不声明 external validation PASS、external consumer PASS、product readiness、projection
  application readiness、runtime/API/frontend/E2E PASS、Agent smoke PASS、autonomous PASS、
  generation-quality PASS、minimum working-state PASS 或 final v0.8 readiness。

## Compatibility Requirements

- v0.7 external validation report semantics 仍是 redacted report baseline。
- v0.7 readiness manifest semantics 仍是 public evidence-reference baseline。
- v0.7 projection read-model semantics 仍是 read-only/no-write baseline。
- v0.7 `0.7.9` checker/docs clean pass 仍只能作为 handoff context。
- v0.8 `0.8.1` claim taxonomy、`0.8.2` observable surface boundary 和 `0.8.3`
  core-readiness evidence 保持兼容，不由本 package 扩大范围。

## Review Gates

本 package 只有在以下条件满足后才可标记 review complete：

- 所有 required English docs 和 Chinese mirrors 均存在。
- documentation checks 通过。
- parent/child status surfaces 一致。
- changed-file scope guard 确认 documentation-only scope 加 already reviewed prior v0.8
  changes。
- read-only documentation/contract evaluator 报告无 P1、无 blocking P2。

本 documentation-only package 之后 implementation 仍未授权；除非未来 package 创建 reviewed
mixed/code contract。

## Handoff

如果 reviewed，本 package 将 handoff contract 交给
`0.8.5-core-working-state-smoke-evidence`。`0.8.5` 仍必须创建或确认自己的 package
documents 和 review gate，之后才可运行 evidence 或修改 implementation files。
