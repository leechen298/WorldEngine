# Test Plan

Chinese mirror: `test-plan.zh.md`.

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

Expected focused tests after implementation:

- Request schema accepts bounded public worldview premise and rejects extra or
  private fields.
- Generation response exposes structured public generated world model fields.
- Not-configured provider path returns public `not_configured` or `blocked`
  without raw provider details.
- Deterministic fallback path is clearly labeled and cannot be counted as
  LLM-backed PASS.
- Safe mock or provider-backed path returns public generation evidence without
  raw prompt, raw provider response, provider trace, secrets, hidden context,
  private Agent memory, raw thought, or private goals.
- Serialized response redaction scan rejects forbidden markers.
- Validation error serialization does not echo raw premise, private field
  labels, or secret-like values.
- Negative cases cover unsupported provider, mock-only path, redaction
  failure, Validation Client-generated content markers, concrete fixture
  markers, and deterministic generic fallback detection.
- Existing `POST /worlds` deterministic generic creation remains compatible.
- `/manifest` remains additive-compatible and lists any new generation
  endpoint only with correct warnings.

Candidate commands:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_llm_worldview_generation_api.py app/tests/test_public_handoff_contract_api.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
```

## Checker / Artifact Tests After Implementation

Run only if this package changes checker support:

```bash
python3 tools/testing/validate_agent_autonomous_result.py <result-dir>
```

Expected checker behavior must distinguish:

- provider-backed generated world evidence.
- deterministic fallback evidence.
- not-configured or blocked provider evidence.
- mock-only non-live evidence.
- redaction failure.
- checker gap.

## Acceptance Criteria

Documentation-stage acceptance:

- Required package docs and mirrors exist.
- Package status remains `ready for documentation/contract review`.
- `implementation_authorized: no`.
- `evidence_execution_authorized: no`.
- `provider_live_call_authorized: no`.
- `external_validation_authorized: no`.
- Contract, design, test plan, and plan cover redaction, fallback, blocked
  provider behavior, public generated model shape, compatibility, and scope
  guardrails.

Implementation-stage acceptance after review authorization:

- Focused backend tests pass.
- Backend regression passes if shared backend surfaces change.
- Public responses are redacted and structured.
- Existing deterministic `POST /worlds` remains compatible.
- No live provider PASS, LLM-backed lifecycle PASS, external validation PASS,
  product readiness, or full v0.9 closeout is claimed without current-session
  checker/scorecard evidence.

## Not Run

During documentation drafting, do not run backend tests, E2E tests, Agent
smoke, autonomous validation, live provider calls, checker validation, or
external validation. Record them as not run because implementation is not yet
authorized.
