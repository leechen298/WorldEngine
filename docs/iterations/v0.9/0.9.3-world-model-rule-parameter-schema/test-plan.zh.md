# Test Plan

英文镜像：`test-plan.md`。

## Unit Tests

implementation authorization 后新增或更新 focused tests：

- `backend/app/tests/test_world_rule_parameter_schema.py`
  - accepts a valid generated rule parameter set。
  - rejects duplicate parameter ids。
  - rejects duplicate rule ids。
  - rejects unresolved target parameter refs。
  - rejects unresolved rule refs。
  - rejects `initial_value` that does not match `value_type`。
  - rejects prose-only rules without structured triggers/effects。
  - rejects private/raw/provider/secret markers in ids、paths、descriptions、evidence、
    diagnostics 和 summary fields。
  - returns a public `RuleParameterValidationResult` and `PublicWorldRuleSummary`。
- `backend/app/tests/test_world_generation_schema.py`
  - verifies new schema models serialize and round-trip without private fields。
  - verifies `PublicGeneratedWorldModel` remains backward-compatible。
- `backend/app/tests/test_llm_worldview_generation_api.py`
  - verifies `/world/generation/worldview` remains compatible。
  - 如果 implementation 添加 rule summary field，验证它是 additive 且 redacted。
- `backend/app/tests/test_param_validator.py` 或 `test_world_params.py`
  - verifies existing `/world/params` registered paths still pass/reject as before。
  - verifies generated-only parameter definitions 不会 silent 地变成 writable runtime paths，除非后续
    package 明确 bridge。

## Regression Tests

运行 focused compatibility tests：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_rule_parameter_schema.py app/tests/test_world_generation_schema.py app/tests/test_llm_worldview_generation_api.py app/tests/test_param_validator.py app/tests/test_world_params.py -q
```

运行 backend regression：

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

运行 diff/format checks：

```bash
git diff --check
```

运行 package documentation checks：

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

## Acceptance Criteria

- Full package docs and mirrors exist。
- Implementation 前 documentation review 记录 no P0/P1/P2 findings。
- Implementation 只添加 additive schema/API/helper behavior。
- Valid generated rule parameter set 被 accepted and summarized。
- Invalid ids、refs、value types、unstructured rules 和 private markers 被 public diagnostics
  rejected。
- Existing `/world/params` behavior 保持 compatible。
- Existing `0.9.2` worldview generation behavior 保持 compatible。
- 不发生 live provider calls、external validation、generated-result directories、Validation
  Client changes、frontend changes、migrations 或 `backend/worldengine/` changes。

## Not Run

implementation 授权前，本包不运行 backend tests，除非是 optional baseline checks。Live provider
calls、checker execution、external validation、generated-result creation 和 Validation Client tests
在本包内仍未授权。
