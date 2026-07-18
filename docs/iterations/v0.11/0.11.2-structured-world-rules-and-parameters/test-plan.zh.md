# Test Plan

英文版本：`test-plan.md`。

## Documentation Checks

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.2-structured-world-rules-and-parameters')
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

## Focused Backend Tests

实现后运行：

```bash
python3 -m pytest app/tests/test_session_rule_parameters_api.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_params.py app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py
```

Expected：

- valid rule set attach 到 session，并可读回 public summary。
- invalid refs/types 被拒绝，且不替换 last accepted summary。
- private markers 被拒绝且不 echo。
- 现有 `/world/params` behavior 继续通过。
- session create/run/status behavior 继续通过。
- manifest 暴露 session rule endpoints。

## Recording Rules

- 不声明 event generation、direction queue、fidelity、provider live 或 external
  Validation Client PASS。
- 未在当前 session 运行的 tests，不得声明 passed。
