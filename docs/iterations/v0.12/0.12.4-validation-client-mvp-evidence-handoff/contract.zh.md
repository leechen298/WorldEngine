# Contract

英文原文：`contract.md`。

## 公开概念

- `WorldEngine MVP evidence bundle`：从 WorldEngine 和 client operation logs 导出的 public artifacts 目录。
- `operation-log.jsonl`：external client action log，只记录 public client operations，不包含 private prompts、secrets、raw provider payloads 或 hidden evaluator data。
- `api-log.jsonl`：WorldEngine public APIs 的 request/response summary log，必须 redacted 到 public fields。
- `scorecard-input.json`：供 checker/scorecard classification 使用的 public normalized input。
- `in-world Agent`：由 WorldEngine public runtime state 表示的 Agent。
- `external validation agent`：Codex/OpenClaw-style 世界外执行者；绝不是 in-world Agent 或 player。

## 必需 Artifact Contract

MVP evidence bundle 至少包含：

- `manifest.json`：导出的 WorldEngine `/manifest` response。
- `operation-log.jsonl`：external client public operation log。
- `api-log.jsonl`：public API summary log。
- `session-summary.json`：public session、runtime、snapshot、rule、Agent、memory 和 inspection refs。
- `agent-evidence.json`：public Agent observe/intent/action-or-wait/rest/memory evidence。
- `inspection-evidence.json`：narrative/diagnostic read-only inspection evidence。
- `scorecard-input.json`：checker/scorecard 使用的 normalized public evidence。
- `redaction-report.json`：public redaction scan result。

Optional artifacts 可以包含 screenshots、OpenAPI metadata 或 reviewer notes，但必须只含 public evidence。

## 允许变更

- 新增或更新 package documentation 和 handoff prompt docs。
- 只有本包记录对应 implementation authorization 后，才可增加 public schema/checker support。
- 增加 redaction marker lists、artifact field definitions 和 status taxonomy。
- closeout 后更新 parent review/route evidence。

## 禁止变更

- 不在本仓库实现 Validation Client。
- 不做 provider live calls 或 external validation execution。
- 不把 external validation agent 表示为 in-world Agent 或 player。
- 不让 Validation Client 对 WorldEngine provider calls、generation、world mutation、Agent autonomy 或 PASS decisions 拥有权威。
- 不包含 raw/private evidence、private prompts、secrets、raw provider responses、raw thought、private Agent memory、hidden context 或 private evaluator data。
- 不做 frontend、autonomous validation、complete MVP closeout 或 `backend/worldengine/` implementation。

## 必须行为

- Handoff artifacts 必须 public-only 且可 redaction-scan。
- PASS/PARTIAL/BLOCKED/FAIL 必须是 checker/scorecard/review classifications，不是 Validation Client 自行声明。
- Provider credentials 缺失、external client capability 缺失或 checker capability 缺失，后续 validation 中必须归类为 BLOCKED/PARTIAL，不能在这里掩盖。
- Artifact additions 必须相对早期 manifest/result concepts 保持 additive。

## 退出条件

- Documentation evaluator 不记录 P1/P2 findings。
- Handoff artifact contract 和 prompt 足够让独立 Validation Client iteration 使用。
- 不声明 provider live-call 或 external validation execution。
- Parent route 推进到 `0.12.5-full-lifecycle-checker-and-autonomous-validation`。
