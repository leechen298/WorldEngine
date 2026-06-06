# Technical Design

英文镜像：`technical-design.md`。

## Execution Flow

本 package 使用 `docs/testing/agent-autonomous/llm-backed-suite-execution.md` 中的 runbook sequence：

1. preflight and budget check。
2. 启动 required local services。
3. 运行 provider live smoke。
4. 运行 LLM-backed world creation。
5. 运行 rule parameter evolution。
6. 运行 rule-compliant event generation。
7. 运行 Agent persistent autonomy evidence。
8. 运行 full lifecycle。
9. export result directory。
10. 运行 checker/scorecard。
11. 运行 second-Agent review。
12. 写 durable result summary。

## Result Directories

Live artifacts 应写入：

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

Durable summaries 应写入：

```text
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.md
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.zh.md
```

## Result Classification

- `pass`：所有 critical score items pass，checker validates result，且 second-Agent review 无
  blocking P1/P2。
- `fail`：execution 可运行，但 evidence 证明 product、rule、redaction、client-evidence、checker
  或 autonomy violation。
- `blocked`：provider、environment、quota、service 或 missing prerequisite constraints 阻止
  valid evidence。
- `not_run`：execution 被 intentional skip，且 reason 已记录。

## Evidence Integrity

Operating agent 不得在 run 后修 artifacts 来强行 PASS。如果 artifacts malformed 或 missing，
必须 classify result，或在 budget 和 stop rules 允许时从头 rerun 同一 scenario。

## Second-Agent Review

Second-Agent review 必须只读。它应检查 result directory、checker output、scorecard、redaction
scan、operation log、API summary、evidence bundle 和 PASS claims。任何 blocking P1/P2 都会阻断
full lifecycle PASS。
