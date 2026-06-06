# Test Plan

英文原文：`test-plan.md`。

## Exact Commands To Run

Focused 0.9.6 tests：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Related public surface regression：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
```

Backend regression：

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Documentation and whitespace checks：

```bash
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary')
combined = '\n'.join(path.read_text() for path in root.glob('*.md'))
required = [
    'implementation_authorized: no',
    'provider_live_call_authorized: no',
    'generated_result_creation_authorized: no',
    'external_validation_authorized: no',
    'WorldDirectionRequest',
    'WorldDirectionQueueItem',
    'direct_final_fact',
    'agent_private_state_mutation',
    'rule_bypass',
]
missing = [term for term in required if term not in combined]
if missing:
    raise SystemExit(f'missing required terms: {missing}')
print('OK')
PY
```

## Expected Focused Coverage

- Benign environmental trend guidance 会被 accepted 或 queued，并返回 public direction item。
- External risk、pressure、event-bias、probability-shift、rule-constraint 和
  future-evaluation guidance 会 classified into allowed public categories。
- Death、healing、teleportation、forced relationship 或 forced inventory outcomes 等 direct
  final facts 会被 rejected。
- Direct Agent private memory 或 private goal mutation requests 会被 rejected。
- Rule-bypass language 会被 rejected。
- Private markers 不会 echo 到 public summaries 或 event payloads。
- Extra request fields 会被 rejected。
- `expires_after_tick < apply_after_tick` 会被 rejected。
- Accepted guidance 不会 mutate canonical world state 或 Agent private state。
- 既有 `/worlds/{world_id}/director-guidance` benign guidance behavior 保持 compatible。

## Expected Results

- Focused tests pass。
- Related public surface regression passes。
- Backend regression passes，或记录 unrelated existing failures with evidence。
- `git diff --check` passes。
- Documentation term check passes。

## Commands Not Run And Why

- Live provider smoke：`0.9.6` 不授权。
- Generated result creation：`0.9.6` 不授权。
- Checker execution 或 external validation：`0.9.6` 不授权。
- Validation Client E2E：本包 out of scope。
- Autonomous validation：本包 out of scope。
- Event legality checker：属于 `0.9.7+`，本包不授权。

## Blocker Recording Rule

如果 required command 失败，在 `review.md` 记录 exact command、exit status、relevant output、
suspected scope，以及该 failure 是否 blocks closeout。不得用更窄 command 替代失败命令并声明
package pass。

## No Unverified Claims Rule

只有当前 session 运行过的 commands 才能记录为 passed。Historical v0.8 或更早 v0.9 evidence
只能作为 handoff context 引用。
