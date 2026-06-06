# Test Plan

英文镜像：`test-plan.md`。

## Unit Tests

在 `tools/testing/test_validate_agent_autonomous_result.py` 中新增或更新 focused tests，覆盖：

- supported LLM-backed scenario enum acceptance。
- LLM-backed `pass`、`fail`、`blocked` 和 `not_run` status classification。
- provider live smoke PASS-critical artifact validation。
- world creation 对 deterministic generic fallback 的 PASS 拒绝。
- rule parameter evolution 对 unexplained changes 或 fixed-counter-only PASS 的拒绝。
- event legality 对 direct final-state mutation PASS 的拒绝。
- Agent persistent autonomy 对 single-event-only 或 client-scripted action PASS 的拒绝。
- full lifecycle 要求每个 critical scorecard item 都 pass。
- full lifecycle 要求 `second-agent-review.md` 且无 blocking P1/P2。
- redaction leak fixtures 失败：raw prompt、raw provider response、provider trace、private
  memory、raw thought、hidden context 和 private evaluator markers。
- missing required artifact fixtures 失败。
- existing dashboard 和 basic lifecycle fixtures 仍按原规则 pass/fail。

## Regression Tests

- `make validate-agent-autonomous-fixtures`
- `backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q`
- `git diff --check`
- 本 package 和 parent v0.9 docs 的 package completeness/status scans。

## Commands

```bash
make validate-agent-autonomous-fixtures
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
git diff --check
python - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures')
required = {
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
}
missing = sorted(name for name in required if not (pkg / name).exists())
print({'files': len(list(pkg.glob('*.md'))), 'missing': missing})
raise SystemExit(1 if missing else 0)
PY
```

## Acceptance Criteria

- LLM-backed scenarios 在 schema、validator、fixtures 和 docs 中获得 checker support。
- Critical artifacts、scorecard items、redaction scan 或 second-Agent review evidence 缺失时，
  PASS 会被拒绝。
- BLOCKED 和 NOT_RUN 可以诚实表达，但不会变成 PASS。
- Existing autonomous saved-result checker behavior 被保留。
- 不运行 provider calls，不修改 runtime behavior、frontend、Validation Client、generated-result
  rewrites 或 `backend/worldengine/`。

## Not Run During Documentation Stage

Documentation drafting 阶段不运行 implementation tests。上述 commands 在 implementation 后成为必跑项。
