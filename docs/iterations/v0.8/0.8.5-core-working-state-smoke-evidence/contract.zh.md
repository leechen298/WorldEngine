# Contract

## Public Concepts

- `CoreWorkingStateSmokeEvidence`：针对 public core-side WorldEngine surfaces 的
  current-session command evidence。
- `CoreSurface`：无需 external validator data，即可通过 repository-local code、tests、checkers
  或 API behavior 证明的 bounded surface。
- `SmokeEvidenceClass`：`backend_schema`、`backend_api`、`runtime_event`、
  `agent_loop`、`memory_context`、`archive`、`generation`、`handoff_contract`、
  `frontend`、`e2e`、`agent_smoke`、`autonomous`、`external_validation` 或
  `manual_review`。
- `SmokeEvidenceStatus`：`pass`、`fail`、`blocked`、`skipped` 或 `out_of_scope`。
- `ProofBoundary`：command result 支持的 exact claim。
- `EvidenceArtifact`：本 package 创建或引用的 repository-local、redacted result file 或
  command log reference。

## Required Core Surfaces

本 package 必须分类这些 surfaces：

- WorldSpec schema 和 loader compatibility。
- generation schema、plan compiler、preview、regeneration、runtime-readiness 和
  core-readiness surfaces。
- runtime context bridge 和 runtime step evidence。
- event schema/API compatibility。
- Agent loop service/API/perception/action evidence。
- memory-context substrate 和 perception compatibility。
- archive snapshot/summary compatibility。
- v0.7 public contract/checker compatibility，作为 handoff context。
- frontend、E2E、Agent smoke、autonomous 和 external validation surfaces 只有在 reviewed
  test plan 授权 commands 时才 in-scope；否则必须明确分类为 skipped 或 out of scope。

## Allowed Changes

Documentation stage：

- 创建或更新 `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/` 下的文件。
- 创建或更新本 package 的 Chinese mirrors。
- 更新 parent v0.8 route/status/review surfaces。

Evidence stage after review：

- 运行 `test-plan.md` 授权的 exact commands。
- 在本 package `review.md` 中记录 redacted command evidence。
- 只有在 `review.md` 创建前记录 artifact path 时，才可在 `docs/testing/results/` 下创建 result
  summary。

## Forbidden Changes

- Documentation stage 不修改 runtime、schema、API、frontend、backend test、checker
  implementation、fixture、migration、generated result、external repository、external
  validator code、external application code 或 `backend/worldengine/` files。
- 不实现新 product behavior，也不为了 validation pass 修改 product functionality。
- 不导入、clone、运行或实现 external validator 或 external app repository。
- 不添加 concrete validation worlds、product scenarios、UI selectors、private screenshots、
  private transcripts、private paths、oracle internals、provider traces、raw prompts、
  secrets 或 non-redacted external event payloads。
- 不把 skipped、blocked、out-of-scope、historical 或 documentation evidence 当成 PASS。
- 不声明 external validation PASS、product readiness、projection app readiness、generation
  quality PASS、full autonomous PASS 或 final v0.8 readiness。

## Command Authorization Boundary

Documentation review 完成前：

- `implementation_authorized: no`
- `evidence_execution_authorized: no`

Documentation/contract review 后，`review.md` 可记录：

- `implementation_authorized: no`，除非 evaluator 明确发现需要 test/checker/artifact
  implementation change，并且 contract 先更新。
- `evidence_execution_authorized: yes`，仅限 `test-plan.md` 中 exact commands，且前提是没有
  P1 或 blocking P2。

## Compatibility Requirements

- v0.3 loader/runtime-context bridge 保持 compatible。
- v0.4 Agent loop action/perception boundary 保持 compatible。
- v0.5 memory context 保持 read-only 和 process-local。
- v0.6 generation、preview、regeneration 和 runtime-readiness surfaces 保持 compatible。
- v0.7 public validation report、readiness manifest、projection read-model 和 `0.7.9`
  checker/docs repair evidence 只作为 handoff context。
- v0.8 `0.8.3` core-readiness evidence 仍只限 focused route。
- v0.8 `0.8.4` handoff statuses 只用于 classification，不作为 PASS substitutes。

## Review Gates

Documentation review 必须确认：

- 所有 required English docs 和 Chinese mirrors 均存在。
- command matrix 覆盖 required core surfaces 或明确分类 gaps。
- proof boundaries 具体且不过度声明。
- skipped、blocked 和 out-of-scope surfaces 有明确 rationale。
- artifact paths redacted 且 repository-local。
- documentation drafting 不修改 runtime/test/checker implementation files。
- read-only documentation/contract evaluator 报告无 P1、无 blocking P2。

Evidence execution 后的 closeout 属于后续 implementation/evidence stage，不能在 documentation
drafting 阶段完成。
