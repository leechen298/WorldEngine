# Contract

英文原文：`contract.md`。

## 公开概念

- `inspection surface`：只读 API/artifact，用公开 evidence 汇总行为，不改变 canonical state。
- `session narrative projection`：面向 session、tick range、可选 branch、可选 Agent focus 的可读公开摘要。
- `diagnostic inspection summary`：由 public evidence 派生的 out-of-world Q&A 风格公开摘要。
- `inspection provenance`：用于标识 projection 输入的公开 refs 和 filters，包括 events、snapshots、Agent state、memory summaries、tick range、branch 或 session。

## 允许变更

- 在 `backend/app/schemas/` 中增加 public inspection request/response schema。
- 以 additive 方式扩展现有 external projection boundary helper。
- 在现有 session 或 world 路由边界下增加只读 session inspection endpoint。
- 为新 endpoint 增加 manifest/public-surface discovery。
- 增加聚焦后端测试。
- 更新 package 和 parent review evidence。

## 禁止变更

- narrative/diagnostic inspection 不得造成 canonical state mutation、event append、direction queue write、Agent memory write 或 in-world dialogue record。
- public inspection artifact 不得包含 raw thought、chain-of-thought、private memory、private goals、hidden context、provider traces、raw prompts、raw provider responses、secrets、tokens 或 private evaluator data。
- 不允许 client-owned Agent autonomy，也不把 external validation agent 记录为 in-world Agent。
- 不做 gameplay dialogue、具体 demo content、frontend、persistence/migration、provider live call、外部 Validation Client implementation、checker automation 或完整 MVP closeout。
- 不在 `backend/worldengine/` 下实现。

## 必须行为

- Narrative inspection 可按 session ID、tick range、branch ID 和 Agent ID 对已有数据做 scope。
- Diagnostic inspection 只能从 public evidence summary 回答，并记录它是 out-of-world。
- Accepted inspection artifact 包含 provenance/filter fields 和 redaction status。
- Rejected inspection request 返回公开 diagnostic code，不回显 private payload。
- Inspection call 不改变 event count、canonical state、direction queue 或 Agent memory。
- Manifest additions 必须是 additive，并标识 endpoint 是 read-only inspection surface。

## 兼容性要求

- 现有 world-level projection 和 diagnostic endpoint 继续通过。
- 现有 session Agent runtime 和 memory tests 继续通过。
- 现有 public handoff manifest tests 继续通过。
- Schema additions 必须 additive。

## 退出条件

- Documentation evaluator 不记录 P1/P2 findings。
- 代码变更前记录 `implementation_authorized: yes`。
- 聚焦测试证明 session/tick-range/branch/Agent-focused projection、diagnostic public-evidence behavior、read-only behavior、redaction、provenance、mutation rejection 和 compatibility。
- Implementation-scope evaluator 在 closeout 前没有 blocking P1/P2。
