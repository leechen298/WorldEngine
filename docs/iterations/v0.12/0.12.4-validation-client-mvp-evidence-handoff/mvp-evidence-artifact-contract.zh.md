# MVP Evidence Artifact Contract

英文原文：`mvp-evidence-artifact-contract.md`。

## 必需文件

```text
manifest.json
operation-log.jsonl
api-log.jsonl
session-summary.json
agent-evidence.json
inspection-evidence.json
scorecard-input.json
redaction-report.json
```

## 必需语义

- `manifest.json` 是导出的 WorldEngine public manifest。
- `operation-log.jsonl` 只以 public summaries 记录 external validation agent operations。
- `api-log.jsonl` 记录 public WorldEngine API request/response summaries。
- `session-summary.json` 关联 session ID、world ID、runtime ticks、snapshots、rules、directions 和 public artifact refs。
- `agent-evidence.json` 关联 in-world Agent public state、observe/intent/action-or-wait/rest、memory 和 consolidation refs。
- `inspection-evidence.json` 关联 narrative projection 和 out-of-world diagnostic inspection refs。
- `scorecard-input.json` 为 checker/scorecard normalize public evidence。
- `redaction-report.json` 记录是否发现 forbidden private markers。

## 必需状态字段

每个 artifact 必须暴露：

- `schema_version`
- `worldengine_version`
- `result_status`
- `redaction_status`
- `artifact_refs`

Artifact 级 `result_status` 必须是 `pass`、`partial`、`blocked`、`fail` 或 `not_run`。最终 MVP status 由后续 checker、scorecard 和 review 决定。

## Agent Terminology Rule

Artifacts 必须用 `in_world_agent` 表示 WorldEngine Agents，用 `external_validation_agent` 表示 Codex/OpenClaw-style operators。External validation agent 不得出现在 Agent memory、world events、player lists 或 in-world dialogue 中。
