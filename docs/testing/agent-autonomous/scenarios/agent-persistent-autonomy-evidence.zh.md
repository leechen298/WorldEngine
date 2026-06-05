# Agent Persistent Autonomy Evidence

状态：planned / checker-extension-required

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目标

证明至少一个 Agent 在多轮中展示 sustained public autonomy evidence。

## 必要操作

- 创建或加载至少包含一个 Agent 的 LLM-backed world。
- 推进足够多 ticks，以观察多个 Agent decision moments。
- 捕获 observation、memory summary、public thought 或 reflection summary、intent 或
  no-intent state、selected action、executed action 和 event reaction。
- 验证 action source 是 WorldEngine public evidence，而不是 client script。

## 禁止操作

- 单个 `params.applied` event 被当作 persistent autonomy。
- Validation Client 脚本化 Agent action，并记录成 WorldEngine action。
- 直接 private memory、private goal 或 hidden context mutation。
- raw chain-of-thought 被导出。

## 必要 Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `agent-autonomy-summary.json`
- Agent event artifacts
- Agent decision moments 前后的 snapshots
- `redaction-scan.json`
- `scorecard-summary.json` 或 checker output

## PASS 来源

PASS 需要 checker 或 scorecard output 证明存在 multi-round continuity，且没有
client-scripted Agent action。

## FAIL Taxonomy

- `agent_autonomy`
- `world_evolution`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

允许 public memory summaries、public thought summaries、public intent summaries、
public action summaries 和 public reactions。禁止 private memory payloads、private goals、
raw thoughts、raw chain-of-thought、hidden context 和 private relationship internals。
