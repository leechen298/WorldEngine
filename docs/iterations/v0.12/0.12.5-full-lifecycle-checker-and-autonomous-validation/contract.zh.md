# Contract

英文原文：`contract.md`。

## Classification Boundary

本包可以基于 current-session evidence 分类 full lifecycle：

- `PASS`：当前导出的 v0.12 evidence directory 通过 checker/scorecard 和 read-only evaluator review，且没有 blocking P1/P2。
- `PARTIAL`：deterministic checker/fixture evidence 通过，但 required fresh external export 或 review evidence 不完整。
- `BLOCKED`：external client capability、result directory、provider/environment、permissions 或 checker assets 缺失。
- `FAIL`：当前 evidence 存在，且 checker/scorecard/review 发现 blocking product 或 contract issue。

历史 saved results 可以证明 checker behavior，但不得作为当前 v0.12 PASS evidence。

## 允许变更

- Package docs 和 result evidence docs。
- 运行现有 checker commands：
  - `make validate-agent-autonomous-fixtures`
  - `make validate-agent-autonomous-result RESULT_DIR=<current-or-fixture-dir>`
- 读取现有 `test-results/agent-autonomous/**` 作为历史上下文。
- 记录 checker outputs、scorecard summary、read-only evaluator review 和 blocker classification。

## 禁止变更

- 不为强行 PASS 修改 product code。
- 不在本仓库实现 Validation Client。
- 未明确授权不做 provider live-call。
- 不把 external validation agent 表述为 in-world Agent。
- 不把 UI smoke 当 full lifecycle PASS。
- 不把 historical result 复用为 current v0.12 PASS。
- 不使用 hidden evaluator data 或 raw/private evidence。
- 不做 final MVP closeout；`0.12.6` 负责 closeout。

## 必需证据

- exact checker command and exit status。
- result directory or fixture directory。
- scorecard/verdict source。
- skipped or unverified items。
- redaction status。
- read-only evaluator review status。
- final package classification with rationale。

## 退出条件

- Documentation evaluator 不记录 P1/P2 findings。
- 运行 checker commands 前记录 evidence execution authorization。
- Checker commands 已运行，或 blockers 被明确记录。
- Read-only evaluator review 无 blocking P1/P2，或者 package 记录 PARTIAL/BLOCKED/FAIL。
- Parent route 推进到 `0.12.6-mvp-release-candidate-and-closeout`。
