# Test Plan

英文版本：`test-plan.md`。

## Documentation Checks

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.1-provider-and-worldview-generation-preflight')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
```

Expected：无 whitespace errors，无 missing 或 empty package docs。

## Focused Backend Tests

实现后运行：

```bash
python3 -m pytest app/tests/test_provider_worldview_preflight_api.py app/tests/test_llm_worldview_generation_api.py app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py
```

Expected：

- provider 未配置时可分类，不崩溃。
- deterministic fallback 继续标记为 non-LLM 和 non-provider-backed。
- provider 已配置但 live-call 未授权时保持 blocked。
- mock provider 继续是 safe mock / non-live。
- private markers 被拒绝或 redacted，不 echo。
- manifest 暴露 preflight surface。

## Recording Rules

- 不声明 live provider PASS。
- 不声明 external Validation Client PASS。
- 未在当前 session 运行的 tests，不得声明 passed。
