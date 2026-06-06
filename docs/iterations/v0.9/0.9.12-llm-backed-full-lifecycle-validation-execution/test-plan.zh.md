# Test Plan

英文镜像：`test-plan.md`。

## Documentation Checks

```bash
git diff --check
python3 -c "from pathlib import Path; pkg=Path('docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution'); required={'README.md','README.zh.md','intent.md','intent.zh.md','contract.md','contract.zh.md','technical-design.md','technical-design.zh.md','test-plan.md','test-plan.zh.md','plan.md','plan.zh.md','review.md','review.zh.md'}; missing=sorted(name for name in required if not (pkg/name).exists()); print({'files': len(list(pkg.glob('*.md'))), 'missing': missing}); raise SystemExit(1 if missing else 0)"
rg -n 'implementation_authorized[:：] yes|provider_live_call_authorized[:：] yes|evidence_execution_authorized[:：] yes|external_validation_authorized[:：] yes|Status[:：].*execution authorized|Status[:：].*implementation complete' docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution docs/iterations/v0.9/README.md docs/iterations/v0.9/README.zh.md docs/iterations/v0.9/CURRENT_STATE.md docs/iterations/v0.9/CURRENT_STATE.zh.md
```

## Execution Checks After Review

Documentation review 明确授权 evidence execution 后：

- 运行 preflight and budget checks。
- 运行 staged LLM-backed lifecycle suite，或 classify blocker。
- 运行 `make validate-agent-autonomous-fixtures` 确认 fixture regression。
- 对 generated result directory 运行 `make validate-agent-autonomous-result RESULT_DIR=<result-dir>`。
- 运行或请求 second-Agent read-only review。
- 写英文和中文 durable result summaries。

## Not Run During Documentation Draft

Documentation drafting 阶段不运行 provider call、evidence execution、external validation、runtime
smoke、Validation Client execution、generated-result creation 或 code test。

## Acceptance Criteria

- Documentation review 无 P0/P1/blocking P2。
- 如果后续授权 execution，output 必须是 PASS，或 honest classified FAIL/BLOCKED/NOT_RUN，并有
  durable evidence。
- 不写入 secrets 或 private evidence。
