# 测试计划

英文源文件：`test-plan.md`。

状态：文档已起草 / 等待评审

## 要运行的精确命令

文档门禁：

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.11/0.11.5-worldview-fidelity-and-v0.11-validation')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" \
  docs/iterations/v0.11/0.11.5-worldview-fidelity-and-v0.11-validation \
  docs/iterations/v0.11/CURRENT_STATE.md \
  docs/iterations/v0.11/README.md \
  docs/iterations/v0.11/review.md
```

授权后的 evidence / implementation 验证：

```bash
python3 -m pytest app/tests/test_worldview_fidelity_evaluation.py app/tests/test_session_rule_bound_evolution_api.py app/tests/test_rule_linked_evolution_legality.py app/tests/test_provider_worldview_preflight_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
```

## 预期结果

- 文档完整性检查不返回 missing 或 empty package files。
- 授权扫描在 review gate 前不发现提前的 implementation/live/external yes。
- 聚焦后端测试通过。
- Immediate fidelity 只有在 public premise indicators 被覆盖且不存在 generic fallback/redaction failure 时才 pass。
- Public run evidence 缺失时，bounded-run fidelity 为 blocked。
- Scorecard final status 反映 immediate 和 bounded-run evidence。
- Redaction tests 证明 raw/private evidence 不会回显。
- v0.11 closeout 记录未运行内容：provider live、外部 Validation Client、Agent autonomy 和 complete MVP automation。

## 不运行的命令及原因

- 本包未授权 provider live smoke。
- 本包未授权外部 Validation Client 自动化。
- 本包不改 frontend，因此不计划 frontend E2E。
- Autonomous Agent validation 不属于 v0.11.5 范围。

## 阻塞记录规则

若命令失败，先在本包 contract 范围内修复。只有外部环境、provider 授权、Validation Client/checker 能力或属于其他 package 的范围问题，才记录为 `BLOCKED`。

## 禁止未验证声明

`review.md` 只能记录当前 session 实际运行过的命令。不得从本包声明 provider live、外部验证、frontend E2E、自主 Agent、v0.12 readiness 或完整 MVP PASS。
