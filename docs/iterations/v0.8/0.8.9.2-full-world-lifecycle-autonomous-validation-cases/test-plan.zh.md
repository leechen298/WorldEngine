# Test Plan

英文版本：`test-plan.md`。

## Focused Tests

运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
make validate-agent-autonomous-fixtures
```

Expected coverage：

- existing valid dashboard fixture 继续通过。
- existing invalid autonomous fixtures 继续失败。
- new full lifecycle scenario 在完整 lifecycle evidence 下通过。
- unsupported or incomplete lifecycle evidence 失败。
- 缺少 Agent action evidence 失败。
- client-scripted Agent action evidence 失败。
- non-advancing runtime evidence 失败。
- redaction evidence failed 失败。

## Regression Tests

运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

如果 checker change 范围变大或出现意外失败，也运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py tools/testing/test_validate_agent_autonomous_result.py -q
```

## Scenario Verification

本 package 之外的 live validation run，后续必须创建 result directory 并运行：

```bash
make validate-agent-autonomous-result RESULT_DIR=<worldengine-full-lifecycle-result-dir>
```

本 package 只让该 validation case 变成可执行。

## Acceptance Criteria

- 新场景已文档化。
- checker 支持 `worldengine-full-lifecycle-autonomous`。
- schema 允许新场景。
- positive and negative checker tests 证明 lifecycle evidence 被强制校验。
- fixture validation 通过。
- 不引入 runtime、provider、frontend、API route 或 Validation Client code changes。

## Not Run

Live WorldEngine autonomous validation 不属于本 package。它必须稍后用真实
WorldEngine 和 Validation Client services 执行。
