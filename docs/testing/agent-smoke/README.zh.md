# Agent Smoke Protocol

Status: current protocol

英文版本：`README.md`。

Agent smoke 是 agent-assisted exploratory check。Codex 可以通过 UI 或 CLI 操作应用、
观察 UI 状态、记录原始 operation log，并写 transcript notes，但 Codex 不能给出最终
PASS verdict。

## Scenario Index

| Scenario | Status | Instructions |
|---|---|---|
| `dashboard-basic-runtime` | `executable` | `docs/testing/agent-smoke/scenarios/dashboard-basic-runtime.md` |
| `dashboard-params-flow` | `live-smoke-recorded` | `docs/testing/agent-smoke/scenarios/dashboard-params-flow.md` |
| `dashboard-invalid-param` | `validator-supported-no-live-run-recorded` | `docs/testing/agent-smoke/scenarios/dashboard-invalid-param.md` |

`dashboard-params-flow` 已有 deterministic validator 支持，并且已有
`test-results/agent-smoke/latest/` live smoke result。`dashboard-invalid-param`
已有 deterministic validator 支持，但仓库中还没有对应 live smoke result。没有新的
validated result directory 时，不要报告 `dashboard-invalid-param` 已经通过。

## Required Evidence

每次运行都把 local artifacts 写到：

```text
test-results/agent-smoke/<timestamp>/
```

需要提交和 push 的最新原始证据，镜像保留在：

```text
test-results/agent-smoke/latest/
```

不要把每个 timestamp run 都提交进仓库。只有需要审计的 latest 原始记录入仓，
长期摘要仍然写到 `docs/testing/results/`。

Required files：

- `result.json`
- `transcript.md`
- `console.log`
- `api-summary.json`
- `operation-log.jsonl`
- `screenshots/` 下至少一个文件

第一版 protocol 中，`trace.zip` 是 optional。

## Operation Log Rule

`operation-log.jsonl` 是 Agent 实际做了什么的原始记录。每个非空行都必须是一个
JSON object。

允许的 operation types：

- `ui`：必须包含 `seq`、`target`、`action`。
- `cli`：必须包含 `seq`、`command`、`exit_code`。

直接 API 调用不能作为 Agent operation。需要 API 状态作为确定性证据时，应由
checker/CLI 产出到 `api-summary.json`，而不是写成 Codex 自己直接调用 API。

## Verdict Rule

`result.json` 必须包含：

```json
{
  "status": "pass",
  "verdict_source": "deterministic_checker"
}
```

如果 `verdict_source` 是 `agent`，即使 Codex 成功观察到了 UI，本次运行也无效。

使用下面命令验证一次 run：

```bash
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/<timestamp>
```

Codex 的最终总结只能引用 validation command result、evidence path 和原始 operation log
path，不能替代 evidence。
