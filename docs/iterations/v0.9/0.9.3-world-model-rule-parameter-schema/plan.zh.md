# Plan

英文镜像：`plan.md`。

## Files

Documentation stage 创建：

```text
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/README.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/README.zh.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/intent.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/intent.zh.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/contract.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/contract.zh.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/technical-design.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/technical-design.zh.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/test-plan.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/test-plan.zh.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/plan.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/plan.zh.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/review.md
docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/review.zh.md
```

只在 documentation review 或 implementation closeout 后修改：

```text
docs/iterations/v0.9/README.md
docs/iterations/v0.9/README.zh.md
docs/iterations/v0.9/CURRENT_STATE.md
docs/iterations/v0.9/CURRENT_STATE.zh.md
docs/iterations/v0.9/CAMPAIGN_PLAN.md
docs/iterations/v0.9/CAMPAIGN_PLAN.zh.md
docs/iterations/v0.9/GOAL_RUNNER.md
docs/iterations/v0.9/GOAL_RUNNER.zh.md
docs/iterations/v0.9/v0.9-plan.md
docs/iterations/v0.9/v0.9-plan.zh.md
docs/iterations/v0.9/review.md
docs/iterations/v0.9/review.zh.md
```

review authorization 后的 implementation candidate files：

```text
backend/app/schemas/world_generation.py
backend/app/core/world_rule_parameters.py
backend/app/api/routes/world_generation.py
backend/app/api/routes/world.py
backend/app/tests/test_world_rule_parameter_schema.py
backend/app/tests/test_world_generation_schema.py
backend/app/tests/test_llm_worldview_generation_api.py
backend/app/tests/test_param_validator.py
backend/app/tests/test_world_params.py
```

Do not touch：

```text
backend/worldengine/
frontend/
Validation Client or external repositories
generated result directories
migrations
concrete fixture worlds
```

## Steps

1. Draft package documents and mirrors。
2. Run documentation existence、required-term 和 Markdown cleanliness checks。
3. Request read-only subagent review for contract/design/test-plan coverage。
4. 修复任何 P0/P1/P2 findings 后才能 authorization。
5. 如果 review passes，更新 package 和 parent docs，只授权 reviewed non-live implementation
   scope。
6. 授权后使用 `worldengine-iteration-dev` 进入 implementation。
7. 运行 focused tests 和 backend regression。
8. 用 exact commands、changed files、compatibility review、scope review、unresolved findings
   和 next route 更新 package/parent review evidence。

## Verification

Documentation-stage verification：

```bash
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema')
docs = ['README', 'intent', 'contract', 'technical-design', 'test-plan', 'plan', 'review']
missing = [str(root / f'{name}{suffix}') for name in docs for suffix in ['.md', '.zh.md'] if not (root / f'{name}{suffix}').exists()]
print('missing_child_docs', len(missing))
if missing:
    print('\n'.join(missing))
    raise SystemExit(1)
PY
```

Implementation-stage verification after authorization：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_rule_parameter_schema.py app/tests/test_world_generation_schema.py app/tests/test_llm_worldview_generation_api.py app/tests/test_param_validator.py app/tests/test_world_params.py -q
```

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```
