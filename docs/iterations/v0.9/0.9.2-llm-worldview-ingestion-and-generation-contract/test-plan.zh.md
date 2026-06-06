# Test Plan

英文镜像：`test-plan.md`。

## Documentation Checks

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract')
docs = ['README', 'intent', 'contract', 'technical-design', 'test-plan', 'plan', 'review']
missing = [str(root / f'{name}{suffix}') for name in docs for suffix in ['.md', '.zh.md'] if not (root / f'{name}{suffix}').exists()]
print('missing_child_docs', len(missing))
if missing:
    print('\n'.join(missing))
    raise SystemExit(1)
PY
```

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract')
required = [
    'WorldviewGenerationRequest',
    'WorldviewGenerationResponse',
    'PublicGeneratedWorldModel',
    'PublicWorldCreationSummary',
    'world_creation_summary',
    'creation_mode',
    'llm_backed',
    'provider_backed',
    'deterministic_generic_fallback_detected',
    'provider_backed',
    'deterministic_fallback',
    'not_configured',
    'blocked',
    'premise_specific',
    'system_digestible',
    'runtime_ready',
    'raw prompts',
    'raw provider responses',
    'validation errors',
    'implementation_authorized: no',
    'provider_live_call_authorized: no',
]
text = '\n'.join(path.read_text() for path in root.glob('*.md'))
missing = [term for term in required if term not in text]
print('missing_required_terms', len(missing))
if missing:
    print('\n'.join(missing))
    raise SystemExit(1)
PY
```

```bash
python3 - <<'PY'
from pathlib import Path
paths = list(Path('docs/iterations/v0.9').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.0-v0.9-planning-and-v0.8-handoff-baseline').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.1-provider-live-smoke-and-redaction-boundary').glob('*.md'))
paths += list(Path('docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract').glob('*.md'))
paths += [Path('docs/roadmap.md')]
errors = []
for path in sorted(paths):
    data = path.read_bytes()
    if data and not data.endswith(b'\n'):
        errors.append(f'{path}: missing final newline')
    for i, line in enumerate(data.splitlines(), 1):
        if line.rstrip(b' \t') != line:
            errors.append(f'{path}:{i}: trailing whitespace')
        if b'\t' in line:
            errors.append(f'{path}:{i}: tab character')
print('markdown_files', len(paths))
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('OK')
PY
```

```bash
git diff --check
```

## Focused Backend Tests After Implementation

Implementation 后预期 focused tests：

- Request schema 接受 bounded public worldview premise，并拒绝 extra 或 private fields。
- Generation response 暴露 structured public generated world model fields。
- Not-configured provider path 返回 public `not_configured` 或 `blocked`，不包含 raw provider details。
- Deterministic fallback path clearly labeled，不能算 LLM-backed PASS。
- Safe mock 或 provider-backed path 返回 public generation evidence，不包含 raw prompt、raw provider
  response、provider trace、secrets、hidden context、private Agent memory、raw thought 或 private goals。
- Serialized response redaction scan 拒绝 forbidden markers。
- Validation error serialization 不 echo raw premise、private field labels 或 secret-like values。
- Negative cases 覆盖 unsupported provider、mock-only path、redaction failure、Validation
  Client-generated content marker、concrete fixture marker 和 deterministic generic fallback detection。
- Existing `POST /worlds` deterministic generic creation 保持 compatible。
- `/manifest` 保持 additive-compatible；新增 generation endpoint 时必须带正确 warnings。

Candidate commands：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_llm_worldview_generation_api.py app/tests/test_public_handoff_contract_api.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
```

## Checker / Artifact Tests After Implementation

仅当本包修改 checker support 时运行：

```bash
python3 tools/testing/validate_agent_autonomous_result.py <result-dir>
```

Expected checker behavior 必须区分：

- provider-backed generated world evidence。
- deterministic fallback evidence。
- not-configured 或 blocked provider evidence。
- mock-only non-live evidence。
- redaction failure。
- checker gap。

## Acceptance Criteria

Documentation-stage acceptance：

- Required package docs and mirrors exist。
- Package status 保持 `ready for documentation/contract review`。
- `implementation_authorized: no`。
- `evidence_execution_authorized: no`。
- `provider_live_call_authorized: no`。
- `external_validation_authorized: no`。
- Contract、design、test plan 和 plan 覆盖 redaction、fallback、blocked provider behavior、
  public generated model shape、compatibility 和 scope guardrails。

Implementation-stage acceptance after review authorization：

- Focused backend tests pass。
- Shared backend surfaces changed 时 backend regression passes。
- Public responses redacted and structured。
- Existing deterministic `POST /worlds` remains compatible。
- 没有 current-session checker/scorecard evidence 时，不声明 live provider PASS、LLM-backed
  lifecycle PASS、external validation PASS、product readiness 或 full v0.9 closeout。

## Not Run

Documentation drafting 阶段不运行 backend tests、E2E tests、Agent smoke、autonomous
validation、live provider calls、checker validation 或 external validation。原因是 implementation
尚未授权。
