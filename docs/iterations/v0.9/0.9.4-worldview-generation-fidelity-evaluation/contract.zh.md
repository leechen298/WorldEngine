# Contract

英文原文：`contract.md`。

## 公开概念

`WorldviewFidelityScorecard`

- 单个 generated world 的 public summary。
- 用 `pass`、`fail`、`blocked` 或 `not_run` 报告 `final_status`。
- 包含 immediate generation fidelity 和 bounded-run fidelity sections。
- 必须包含 redaction flags 和 public failure categories。

`ImmediateWorldviewFidelityArtifact`

- 将 generated public world model 与 public premise 对照评估。
- 通过 public tokens、public digest tags、generated public model summaries、
  world creation metadata 和 rule summary references 检查 premise coverage。
- 对 deterministic generic fallback 和 non-digestible output 给出 fail 或 blocked。

`BoundedRunWorldviewFidelityArtifact`

- 在后续 bounded run 提供 public runtime summaries 时进行评估。
- 当 bounded runtime evidence 缺失或尚不支持时报告 `blocked`。
- 不得运行 ticks、调用 providers 或 mutate canonical state。

`WorldviewContradiction`

- 用于记录与 premise 或 generated boundaries 矛盾的 public taxonomy item。
- categories 包括 `missing_premise`、`generic_fallback`、
  `runtime_contradiction`、`rule_contradiction`、`redaction`、`evidence_gap`
  和 `checker_gap`。

## 允许修改

- 在 `backend/app/schemas/world_generation.py` 中添加 additive schema models。
- 在 `backend/app/core/worldview_fidelity.py` 中添加 deterministic helper。
- 在 `backend/app/tests/test_worldview_fidelity_evaluation.py` 中添加 focused backend tests。
- 更新本包目录下的 package-local documentation 和 review。
- 仅在本包 implementation complete 后更新父级 v0.9 status。

## 禁止修改

- 不进行 provider live calls。
- 不记录 raw prompt、raw provider request、raw provider response、provider trace、
  authorization header、API key、private evaluator oracle、private Agent memory、
  raw thought、chain-of-thought、hidden context 或 private goal evidence。
- 不在 core repository files 中加入 concrete validation-world fixture data。
- 不修改 `backend/worldengine/`。
- 不修改 frontend dashboard、Validation Client、external repository、migration 或 deployment。
- 不实现 bounded runtime control。
- 不实现 rule-linked parameter evolution 或 event legality。
- 不基于 human 或 Agent impression 做 subjective PASS。
- 不声称 deterministic fallback 是 LLM-backed 或 provider-backed。

## 兼容性要求

- 既有 `/world/generation/worldview`、`/worlds`、`/world/params`、provider
  readiness 和 rule-parameter validation behavior 必须保持 compatible。
- Schema changes 必须是 additive；新模型接受 public evidence 时必须拒绝 unexpected
  private fields。
- Fidelity helpers 必须是基于 supplied public evidence 的 pure functions。它们不得
  mutate world state、runtime stores、environment variables、provider config 或既有
  response objects。
- 0.9.1、0.9.2 和 0.9.3 的既有 tests 必须继续通过。

## 后续范围

- `0.9.5`：bounded runtime control and run budgets。
- `0.9.6`：natural-language world direction semantics。
- `0.9.7`：rule-linked evolution and event legality。
- `0.9.8`：Agent continuity and consolidation evidence。
- `0.9.10`：full LLM-backed autonomous scenario 的 checker fixtures 和 scorecard support。
- `0.9.12`：live 或 explicitly blocked full lifecycle validation evidence。

## 退出条件

本包只有在以下条件满足后才能 close：

- required package docs 和 mirrors 存在。
- documentation/contract evaluator 报告无 P0/P1 且无 blocking P2。
- code changes 之前已记录 implementation authorization。
- focused tests 证明 faithful output、missing premise output、generic fallback、
  contradictory runtime output、missing bounded-run evidence 和 redaction failure handling。
- 当前会话 relevant backend regressions 通过。
- `review.md` 记录 exact commands、changed files、subagent findings、
  compatibility review、scope review、unresolved findings 和 final route。

