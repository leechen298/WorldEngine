# Test Plan

英文原文：`test-plan.md`。

## 文档门禁

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## 聚焦后端验证

实现授权后运行：

```bash
cd backend
python3 -m pytest app/tests/test_session_narrative_diagnostic_inspection_api.py app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_session_agent_runtime_loop_api.py app/tests/test_session_agent_memory_consolidation_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

预期覆盖：

- session narrative projection 接受 public session/tick-range evidence。
- session narrative projection 可按 branch ID 和 Agent ID 过滤。
- diagnostic inspection 从 public evidence 回答，并记录 out-of-world classification。
- projection/diagnostic call 不 append event、不写 direction queue、不改变 canonical state、不写 Agent memory。
- private markers 和 unsupported mutation flags 被拒绝，且不公开回显 payload。
- rejected request 对 missing evidence、invalid range 或 invalid refs 暴露公开 diagnostic code。
- provenance fields 标识 session、tick range、branch、Agent focus 和 public refs。
- 现有 world-level projection、session Agent runtime、Agent memory 和 manifest tests 继续通过。

## 未授权则不运行

- Provider live calls：未授权。
- 外部 Validation Client automation：未授权。
- Frontend/E2E：不属于本包。
- Full autonomous validation/checker：属于后续包。
