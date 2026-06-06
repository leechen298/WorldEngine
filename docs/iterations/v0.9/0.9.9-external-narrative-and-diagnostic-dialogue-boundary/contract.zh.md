# Contract

英文原文：`contract.md`。

## Public Concepts

`NarrativeProjectionArtifact`

- 描述当前 world evidence 的 external narrative projection public artifact。
- 包含 projection id、world id、source event refs、snapshot refs、Agent continuity refs、
  public narrative summary 或 redacted narrative text、provenance、redaction status 和
  mutation flags。
- 它是 external projection evidence，不是 canonical world state。

`DiagnosticDialogueArtifact`

- 描述面向 Agent 的 out-of-world diagnostic question 和 public answer summary 的 public artifact。
- 包含 dialogue id、world id、可选 Agent id、question summary、response summary、evidence refs、
  provenance、redaction status 和 mutation flags。
- 默认它是 diagnostic inspection evidence，不是 in-world dialogue。

`ProjectionBoundaryDecision`

- 说明 projection 或 diagnostic artifact 是 allowed、rejected 还是 redacted 的 public decision record。
- 它必须记录 artifact 为什么在 canonical state 之外或之内。本包默认只允许 outside-canonical-state behavior。

## Boundary Table

| Surface | Default classification | May mutate canonical events | May write Agent memory | May become in-world dialogue |
| --- | --- | --- | --- | --- |
| Narrative projection | external projection | no | no | no |
| Diagnostic Agent question | out-of-world diagnostic | no | no | no |
| Canonical world event | in-world event | yes, through event API only | only through reviewed future bridge | maybe, if event type says so |
| Agent continuity artifact | public Agent evidence | no direct state mutation | no private memory write | no |

## Required Checks

Projection 和 diagnostic evidence 必须 reject 或 diagnose：

- raw thought 或 chain-of-thought。
- private memory payloads、private goals、hidden context、private evaluator data、raw prompts、
  raw provider traces、API keys、authorization headers 和 secrets。
- 声称直接修改 canonical state 的 narrative text。
- 默认追加 canonical events 的 projection artifacts。
- 默认把 diagnostic conversation 表示为 in-world dialogue。
- 默认把 diagnostic conversation 表示为 Agent memory。
- 缺少 public provenance 或 redaction status 的 artifacts。

Accepted artifacts 必须记录：

- `canonical_state_mutation_applied: false`。
- `canonical_event_appended: false`，除非后续 reviewed bridge 明确授权 event writing。
- `agent_memory_write_applied: false`。
- `in_world_dialogue_recorded: false`。
- public evidence refs 和 redaction status。

## Allowed Changes

Documentation review authorization 后，本包可以修改：

- `backend/app/schemas/` 中面向 public narrative projection、diagnostic dialogue、
  boundary decisions、provenance 和 redaction status 的 additive schemas。
- `backend/app/core/` 中用于 projection 和 diagnostic artifact construction 的 narrow
  deterministic helpers。
- 如 public inspection 需要，可添加 additive active-backend route behavior 或 manifest/OpenAPI exposure。
- `backend/app/tests/` 下的 focused backend tests。
- package `review.md` 和 `review.zh.md`。
- 只在 review 或 implementation closeout 后更新 v0.9 parent status/review docs 的 route/status handoff。

## Forbidden Changes

本包不得：

- 修改 `backend/worldengine/`。
- 修改 frontend code。
- 修改 Validation Client 或 external repositories。
- 执行 live provider calls 或 LLM interpretation。
- 创建 generated worlds 或 generated-result artifacts。
- 执行 checkers 或修改 checker fixtures。
- 运行 external validation 或 autonomous validation。
- 实现 durable scheduling、background workers、cron、queue services 或 deployment infrastructure。
- 实现 player-in-world chat、product chat UI 或 narrative game content。
- 默认把 diagnostic conversations 写入 canonical world timeline 或 Agent memory。
- 存储或导出 raw thought、chain-of-thought、private memory payloads、private goals、hidden
  context、raw prompts、raw provider requests、raw provider responses、provider traces、API
  keys、authorization headers、secrets 或 private evaluator data。

## Compatibility Requirements

- Existing event、runtime、snapshot/archive、world direction、rule-linked event legality 和
  Agent continuity surfaces 必须保持兼容。
- Existing Agent memory stores 不得收到 diagnostic writes。
- Existing public handoff manifest behavior 必须保持兼容。
- New schemas 必须 reject extra fields 和 private markers。
- Projection 和 diagnostic artifacts 应能被后续 `0.9.10` checker/schema/fixture work 消费，
  但本包不实现 checker fixtures，也不执行 checkers。

## North Star Check

本包支持 inspectable external projection，同时保持 WorldEngine 的 canonical event/state spine。

## Out-of-Scope Follow-ups

- `0.9.10`：LLM-backed checker fixtures、schema、scorecard support 和 checker execution。
- 未来 bridge 可以明确授权 diagnostic-to-memory behavior，但本包默认禁止。

## Exit Criteria

本包只有在以下条件满足时才可 close：

- required package docs 和 mirrors 存在。
- documentation/contract evaluator 报告无 P0/P1 且无 blocking P2。
- code changes 前已记录 implementation authorization。
- focused tests 证明 projection/diagnostic artifacts 保持在 canonical state 之外，默认不追加
  canonical events，默认不写入 Agent memory，reject private markers，并保持 compatibility。
- relevant backend regressions 在当前 session 通过。
- `review.md` 记录 exact commands、changed files、subagent findings、compatibility review、
  scope review、unresolved findings 和 final route。
