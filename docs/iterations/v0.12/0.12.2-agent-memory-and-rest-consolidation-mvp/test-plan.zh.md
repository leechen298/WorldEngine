# Test Plan

英文源文件：`test-plan.md`。

## Documentation Gate

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.2-agent-memory-and-rest-consolidation-mvp')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.2-agent-memory-and-rest-consolidation-mvp docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Focused Backend Verification

Implementation authorization 后运行：

```bash
python3 -m pytest app/tests/test_session_agent_memory_consolidation_api.py app/tests/test_session_agent_runtime_loop_api.py app/tests/test_agent_memory_substrate.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

Expected coverage：

- memory summary read 返回 public working/episodic summaries。
- non-rest Agent step 或 consolidation 记录 bounded public working memory。
- rest consolidation 记录 public episodic summary 和 consolidation event。
- private marker payloads 被 reject，或不出现在 public evidence 中。
- repeated ordinary ticks 不修改 personality 或 skills。
- ordinary non-rest ticks 不自动创建 episodic、long-term 或 consolidation records。
- evidence refs 标识 memory/event/runtime sources。
- existing session Agent runtime loop 和 memory substrate tests 继续通过。
- manifest/public handoff 以 additive 方式暴露 memory surfaces。

## Commands Not Run Unless Later Authorized

- Provider live calls：未授权。
- External Validation Client automation：未授权。
- Frontend/E2E：不属于本 package。
- Full autonomous validation/checker：属于后续 packages。
