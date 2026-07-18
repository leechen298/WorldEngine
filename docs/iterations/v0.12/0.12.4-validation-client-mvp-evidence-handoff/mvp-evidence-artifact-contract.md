# MVP Evidence Artifact Contract

Chinese mirror: `mvp-evidence-artifact-contract.zh.md`.

## Required Files

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

## Required Semantics

- `manifest.json` is the exported WorldEngine public manifest.
- `operation-log.jsonl` records external validation agent operations as
  public summaries only.
- `api-log.jsonl` records public WorldEngine API request/response summaries.
- `session-summary.json` links session ID, world ID, runtime ticks, snapshots,
  rules, directions, and public artifact refs.
- `agent-evidence.json` links in-world Agent public state, observe/intent/
  action-or-wait/rest, memory, and consolidation refs.
- `inspection-evidence.json` links narrative projection and out-of-world
  diagnostic inspection refs.
- `scorecard-input.json` normalizes public evidence for checker/scorecard.
- `redaction-report.json` records whether forbidden private markers were found.

## Required Status Fields

Every artifact must expose:

- `schema_version`
- `worldengine_version`
- `result_status`
- `redaction_status`
- `artifact_refs`

`result_status` must be one of `pass`, `partial`, `blocked`, `fail`, or
`not_run` at artifact level. Final MVP status is decided later by checker,
scorecard, and review.

## Agent Terminology Rule

Artifacts must use `in_world_agent` for WorldEngine Agents and
`external_validation_agent` for Codex/OpenClaw-style operators. The external
validation agent must not appear in Agent memory, world events, player lists,
or in-world dialogue.
