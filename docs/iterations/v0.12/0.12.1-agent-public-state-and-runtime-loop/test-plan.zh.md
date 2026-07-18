# Test Plan

英文源文件：`test-plan.md`。

## Documentation Gate

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.1-agent-public-state-and-runtime-loop docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Focused Backend Verification

Implementation authorization 后运行：

```bash
python3 -m pytest app/tests/test_session_agent_runtime_loop_api.py app/tests/test_agent_loop_service.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

Expected coverage：

- session Agent list/read 返回 public default Agent state。
- session Agent step 记录 public observation 和 intent evidence。
- 不把 client-submitted action payload 接受为 autonomy。
- event log 包含 public Agent evidence，且 `client_scripted_action: false`。
- redaction-sensitive strings 被 reject 或不出现在 public evidence 中。
- manifest/public handoff 以 additive 方式暴露 session Agent endpoints。
- existing request-driven Agent loop tests 继续通过。

## Commands Not Run Unless Later Authorized

- Provider live calls：未授权。
- External Validation Client automation：未授权。
- Frontend/E2E：不属于本 package，除非后续 review 扩大范围。
- Full Agent smoke/autonomous validation：属于后续 packages。
- Full MVP checker/scorecard：属于 `0.12.5` 和 `0.12.6`。
