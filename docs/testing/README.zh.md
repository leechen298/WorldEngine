# Testing and Evidence

Status: testing evidence guide

英文版本：`README.md`。

本目录记录 WorldEngine iterations 的 testing standards 和 evidence。

## Evidence Rules

- 没有在当前 work session 运行命令时，不要声称 tests passed。
- Code packages 必须在 package `review.md` 中列出 exact commands 和 results。
- Runtime、UI、E2E 或 live smoke claims 必须包含可 review 的 evidence。
- Docs-only packages 可以跳过 code tests，但必须在 `review.md` 说明 no-test rationale。

## Result Files

使用 `docs/testing/results/` 存放 durable evidence summaries，适用于 package 运行 broader
verification 或 manual/runtime checks 的场景。

建议命名格式：

```text
YYYY-MM-DD-<version-package>-<slug>.md
```

每个 result file 应包含：

- command 或 workflow。
- environment assumptions。
- output summary。
- failures 或 skipped checks。
- 回链到 iteration package。

## Agent Smoke

Agent-assisted smoke tests 必须遵循 `docs/testing/agent-smoke/`。Codex 或其他 agent
可以执行和观察，但 PASS/FAIL 必须来自 deterministic Playwright assertions 或
`tools/testing/validate_agent_smoke_result.py`。

历史 raw Agent smoke artifacts 应放在 ignored `test-results/agent-smoke/<timestamp>/`
下。最新一次已 review 的原始记录可以提交到 `test-results/agent-smoke/latest/`，用于审计。
Durable summaries 应放在 `docs/testing/results/` 下。
