# Test Plan

英文镜像：`test-plan.md`。

## Documentation Checks

运行：

```bash
git diff --check
python3 -c "from pathlib import Path; pkg=Path('docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract'); required={'README.md','README.zh.md','intent.md','intent.zh.md','contract.md','contract.zh.md','technical-design.md','technical-design.zh.md','test-plan.md','test-plan.zh.md','plan.md','plan.zh.md','review.md','review.zh.md'}; missing=sorted(name for name in required if not (pkg/name).exists()); print({'files': len(list(pkg.glob('*.md'))), 'missing': missing}); raise SystemExit(1 if missing else 0)"
rg -n 'implementation_authorized[:：] yes|provider_live_call_authorized[:：] yes|evidence_execution_authorized[:：] yes|external_validation_authorized[:：] yes|Validation Client repository implementation|provider key handling in client|client-side evaluator authority' docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract docs/iterations/v0.9/README.md docs/iterations/v0.9/README.zh.md docs/iterations/v0.9/CURRENT_STATE.md docs/iterations/v0.9/CURRENT_STATE.zh.md
```

Authorization scan 预期只报告 forbidden-scope prose，不报告 positive authorization。

## Review Checks

只读 documentation evaluator 必须验证：

- package 有所有 required files 和 mirrors。
- contract 将 client role 限定为 display/export only。
- provider ownership 仍属于 WorldEngine。
- PASS authority 仍属于 checker/second-Agent review。
- artifact names 与 0.9.10 checker 和 LLM-backed artifact contract 对齐。
- redaction 和 relative-path rules 明确。
- parent route 指向 documentation review，而不是 implementation。

## Not Run

本 documentation-only package 不运行 code tests、provider calls、checker fixture execution、
frontend smoke、Validation Client execution、generated-result creation 或 external validation。

## Acceptance Criteria

- Validation Client handoff contract 足够 stable，可供后续 client package 实现 display/export
  behavior。
- 不授予 implementation authorization。
- 不引入 client-owned LLM behavior、provider key handling 或 evaluator authority。
