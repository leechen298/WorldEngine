# Test Plan

英文原文：`test-plan.md`。

## 文档门禁

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.4-validation-client-mvp-evidence-handoff')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
    'mvp-evidence-artifact-contract.md', 'mvp-evidence-artifact-contract.zh.md',
    'validation-client-handoff-prompt.md', 'validation-client-handoff-prompt.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "^implementation_authorized: yes|^provider_live_call_authorized: yes|^external_validation_authorized: yes" docs/iterations/v0.12/0.12.4-validation-client-mvp-evidence-handoff docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## 文档验证

预期覆盖：

- artifact contract 命名 required MVP files。
- result directory shape 明确。
- operation-log 和 API-log fields 明确。
- status taxonomy 包含 PASS、PARTIAL、BLOCKED 和 FAIL。
- redaction markers 包含 private memory、raw thought、provider trace、raw provider response、secrets 和 token-style markers。
- terminology 区分 in-world Agents 与 external validation agents。
- handoff prompt 告诉 Validation Client 不要在 WorldEngine 中实现代码。
- 不声明 provider live-call、external validation execution、checker PASS 或 MVP closeout。

Expected command results：

- `git diff --check` exit `0` 且无输出。
- required-file completeness 返回 `{'missing': [], 'empty': []}`。
- active yes-authorization `rg` scan exit `1`，因为没有 active yes authorization fields。
- package whitespace check 返回空 `problems` list。

## Blocker Recording Rule

如果 documentation review 发现 required evidence export 依赖缺失的 external client capability、checker assets、provider/environment credentials、permissions 或 external repository access，必须在 review evidence 中记录为 `BLOCKED`/`PARTIAL`，不能声明 PASS 或伪造 validation evidence。

## No-Unverified-Claims Rule

除非当前 work session 已运行并记录证据，否则不得声明 provider live calls、external validation automation、checker classification、code tests、frontend/E2E 或 MVP PASS。

## 未授权则不运行

- Provider live calls：未授权。
- External Validation Client automation：未授权。
- Full lifecycle checker/autonomous validation：属于 `0.12.5`。
- Frontend/E2E：不属于本包。
- Code tests：除非本包后续授权 schema/checker support changes，否则不需要。
