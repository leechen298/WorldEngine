# Contract

英文镜像：`contract.md`。

## Public Concepts

- `v0.9_closeout_status`：`pass`、`blocked` 或 `deferred`。
- `release_candidate_summary`：v0.9 的 parent evidence assessment。
- `classified_blocker`：带 taxonomy、evidence 和 next route 的 unresolved gap。

## Allowed Changes

- 本 package docs。
- parent v0.9 route/status/review docs。
- 现有 documentation paths 下的 durable closeout summary references。

## Forbidden Changes

- 不改 backend、frontend、API、schema、checker、fixture、migration 或 Validation Client
  implementation。
- 不运行 live provider calls。
- 不执行 new evidence execution。
- 不重写 generated result 以强行 PASS。
- 除非 current evidence 证明，否则不声明 product readiness、external validation PASS 或
  LLM-backed lifecycle PASS。

## Required Evidence

- 0.9.12 result summary：
  `docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md`
- 0.9.12 result directory：
  `test-results/agent-autonomous/20260606T142210+0800-llm-backed-full-lifecycle`
- `0.9.1` 到 `0.9.12` parent 和 child review docs。
- closeout edits 后的 status consistency checks。

## Exit Criteria

当 closeout docs 满足以下条件时，v0.9 可按 BLOCKED close：

- 识别 blocking taxonomy。
- 引用 checker-valid evidence。
- 保持 implementation 和 provider authorization closed。
- 不声明 product readiness 或 external validation PASS。
- 将 future work 路由到更窄 repair 或 future-version plan。
