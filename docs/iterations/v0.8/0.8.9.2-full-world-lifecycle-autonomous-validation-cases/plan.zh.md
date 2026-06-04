# Plan

英文版本：`plan.md`。

## Files

新增：

- `docs/iterations/v0.8/0.8.9.2-full-world-lifecycle-autonomous-validation-cases/*`
- `docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md`
- `tools/testing/fixtures/agent-autonomous/valid-worldengine-full-lifecycle/`

修改：

- `docs/testing/agent-autonomous/README.md`
- `docs/testing/agent-autonomous/scorecard.md`
- `docs/testing/agent-autonomous/result-schema.json`
- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `Makefile`

不触碰：

- `backend/app/`
- `backend/worldengine/`
- `frontend/`
- Validation Client repository。

## Steps

1. 起草 package documents 和 scenario contract。
2. 为 full lifecycle scenario 增加 failing checker tests。
3. 只扩展 checker 到能校验 lifecycle artifacts。
4. 为新场景增加 generic positive fixture。
5. 更新 autonomous testing docs and schema。
6. 运行 focused tests and fixture validation。
7. 更新 `review.md`，记录 actual evidence。

## Verification

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q
make validate-agent-autonomous-fixtures
git diff --check
```
