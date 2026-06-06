# Contract

英文镜像：`contract.md`。

## Public Concepts

- `llm_backed_validation_run`：documented suite 的 bounded execution。
- `live_provider_smoke`：WorldEngine-owned provider call，带 redacted public evidence。
- `validation_result_status`：`pass`、`fail`、`blocked` 或 `not_run`。
- `durable_result_summary`：`docs/testing/results/` 下的 Markdown record。
- `second_agent_review`：read-only evidence review，可阻断 PASS。

## Allowed Changes After Review

- `docs/testing/results/` 下的 result summaries。
- `test-results/agent-autonomous/**` 下 ignored raw result artifacts。
- 本 package docs 和 parent v0.9 route/review docs。

## Execution Authorization After Review

Documentation/contract review 通过后，本 package 可授权：

- 启动已配置的 required local services。
- 运行 documented basic 和 LLM-backed validation flows。
- 只通过 documented validation commands 发起 WorldEngine-owned live provider calls，且 credentials
  必须已由 environment 拥有。
- 运行 saved-result checker 和 scorecard commands。
- 请求 second-Agent read-only review。
- 写 durable result summaries。

## Forbidden Changes

- 不改代码来让 failing run pass。
- 不重写 generated result 来强行 PASS。
- 不修改 checker、fixture 或 schema。
- 不实现 Validation Client。
- 不实现 frontend。
- 不创建、展示或存储 provider credentials。
- 没有 checker/scorecard/second-Agent evidence 时，不声明 external validation PASS。
- 不记录 raw prompt、raw provider request/response、provider trace、API key、authorization header、
  private Agent memory、private Agent goal、raw thought、hidden context、private evaluator data 或
  seed/oracle evidence。
- 不在 `backend/worldengine/` 下新增 runtime features。

## Required Evidence

PASS result 需要：

- `result.json`
- `operation-log.jsonl`
- `provider-live-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `rule-parameter-summary.json`
- `event-legality-summary.json`
- `agent-autonomy-summary.json`
- `diff-replay-summary.json`
- `world-lifecycle-summary.json`
- `validation-client-evidence-bundle.json`，或明确映射的 `manifest.json`/`evidence_bundle_manifest`
- `redaction-scan.json`
- `scorecard-summary.json`
- `second-agent-review.md`
- 证明 saved-result valid 的 checker output。

## Stop Rules

遇到以下情况必须停止并分类：

- provider cost、quota、rate limit 或 network constraints 阻止 reliable validation。
- 不存在 WorldEngine-owned live provider call path。
- required artifacts 缺失且无法从同一次 run 重新生成。
- redaction scan 发现 blocking leak。
- claimed PASS 缺少 checker support。
- Agent action 是 client-scripted，或 direct user direction 直接修改 final world facts。

## Handoff

无论 PASS 还是 classified FAIL/BLOCKED/NOT_RUN，均 hand off 到
`0.9.13-v0.9-release-candidate-and-closeout`。
