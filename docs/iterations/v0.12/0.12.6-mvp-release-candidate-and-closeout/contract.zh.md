# Contract

英文原文：`contract.md`。

## Final Classification Rule

Final closeout 必须是：

- `PASS`：complete current external evidence 存在，并通过 checker、scorecard 和 read-only evaluator review。
- `PARTIAL`：WorldEngine-side capabilities 和 deterministic checker evidence 存在，但 fresh external validation evidence 缺失或不完整。
- `BLOCKED`：required provider/client/checker/environment capability 阻止 meaningful current validation。
- `FAIL`：current evidence 证明 blocking product 或 contract failure。

基于 `0.12.5`，除非 closeout 前出现并检查新的 current external result evidence，本包必须以 `PARTIAL` 关闭。

## 允许变更

- Closeout docs。
- Roadmap status update。
- Parent v0.12 status/review update。
- Documentation verification commands。

## 禁止变更

- 不修改 runtime、API、schema、frontend、checker、fixture、provider 或 Validation Client implementation。
- 不做 provider live-call。
- 不执行 external validation。
- 没有 current external result evidence 时，不声明 MVP PASS。

## 必需证据

- v0.10、v0.11 和 v0.12 package status summary。
- `0.12.5` PARTIAL/BLOCKED evidence。
- closeout verification 运行的 commands。
- 未运行 commands 及原因。
- known gaps 和 next owner。
