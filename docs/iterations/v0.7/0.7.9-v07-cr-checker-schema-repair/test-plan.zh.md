# 测试计划

## 文档门禁检查

在实现授权之前运行：

```bash
git status --short --branch --untracked-files=all
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_9_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'import subprocess
allowed_prefixes=("docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair/",)
untracked=subprocess.check_output(["git","ls-files","--others","--exclude-standard"], text=True).splitlines()
bad=[p for p in untracked if p.startswith("docs/iterations/v0.7/") and not p.startswith(allowed_prefixes)]
print("unexpected_untracked_v0_7_docs=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

预期结果：

- 必需的 `0.7.9` 包文档和中文镜像存在。
- 现有未跟踪的 `docs/iterations/v0.8/**` 被排除，不作为 v0.7 修复产物。
- 在评估器批准前，实现授权保持关闭。

## 修复前红灯测试

先添加聚焦回归测试，然后在修改检查器实现前运行相关测试：

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_projection_read_model_contract.py -q
```

修复前预期红灯失败：

- accepted P1/P2 pass reports 被错误接受。
- `data-testid` 和本地 `/Users/...` 报告文本被错误接受。
- 私有清单命令 / 文本被错误接受。
- `private_application_state_summary` 被错误接受。
- “Schema 有效但检查器无效”的权威边界用例缺失或失败。

## 聚焦修复测试

修复后运行：

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_projection_read_model_contract.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py tools/testing/test_validate_agent_autonomous_result.py -q
backend/.venv/bin/python -m pytest tools/testing -q
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
backend/.venv/bin/python -m json.tool docs/testing/external-validation-report-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python -m json.tool docs/contracts/projection-read-model-schema.json
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260531T122230+0800
```

预期结果：

- 所有聚焦检查器测试通过。
- `tools/testing` 通过。
- 有效就绪清单和投影读模型仍通过。
- JSON 文件可解析。
- Agent autonomous saved-result 检查器夹具和现有 saved result 仍通过。

## 最终验证检查

在实现和结果更新之后运行：

```bash
git diff --check
python3 -c 'from pathlib import Path
paths=[
"docs/testing/results/2026-06-02-v0.7-overall-validation.md",
"docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md",
"docs/testing/results/2026-06-02-v0.7-agent-autonomous-saved-result-validation.md",
"docs/testing/results/2026-06-02-v0.7-agent-autonomous-saved-result-validation.zh.md",
]
missing=[p for p in paths if not Path(p).exists()]
print("checked_validation_refs=" + str(len(paths)))
print("missing_validation_refs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'import subprocess
out=subprocess.check_output(["git","status","--porcelain","--untracked-files=all"], text=True)
files=[line[3:] for line in out.splitlines() if line]
scoped_prefixes=("docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair/",)
scoped_exact={
    "docs/contracts/projection-read-model-contract.md",
    "docs/contracts/v0.7-readiness-manifest-schema.json",
    "docs/iterations/v0.7/CAMPAIGN_PLAN.md",
    "docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md",
    "docs/iterations/v0.7/CURRENT_STATE.md",
    "docs/iterations/v0.7/CURRENT_STATE.zh.md",
    "docs/iterations/v0.7/GOAL_RUNNER.md",
    "docs/iterations/v0.7/GOAL_RUNNER.zh.md",
    "docs/iterations/v0.7/README.md",
    "docs/iterations/v0.7/README.zh.md",
    "docs/iterations/v0.7/review.md",
    "docs/iterations/v0.7/review.zh.md",
    "docs/iterations/v0.7/v0.7-plan.md",
    "docs/iterations/v0.7/v0.7-plan.zh.md",
    "docs/testing/external-validation-report-schema.json",
    "docs/testing/results/2026-06-02-v0.7-overall-validation.md",
    "docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md",
    "docs/validation-report-template.md",
    "tools/testing/test_validate_external_validation_report.py",
    "tools/testing/test_validate_projection_read_model_contract.py",
    "tools/testing/test_validate_readiness_manifest.py",
    "tools/testing/validate_external_validation_report.py",
    "tools/testing/validate_projection_read_model_contract.py",
    "tools/testing/validate_readiness_manifest.py",
}
known_unrelated_prefixes=("docs/iterations/v0.8/",)
known_unrelated_exact={"docs/roadmap.md","docs/scope-boundaries.md"}
known_unrelated_license_metadata={
    "LICENSE",
    "NOTICE",
    "README.md",
    "README.zh.md",
    "backend/pyproject.toml",
    "frontend/package.json",
}
scoped=[p for p in files if p in scoped_exact or any(p.startswith(prefix) for prefix in scoped_prefixes)]
known_unrelated_v0_8=[p for p in files if any(p.startswith(prefix) for prefix in known_unrelated_prefixes)]
known_unrelated_boundary_docs=[p for p in files if p in known_unrelated_exact]
known_unrelated_license=[p for p in files if p in known_unrelated_license_metadata]
known_reported=set(scoped + known_unrelated_v0_8 + known_unrelated_boundary_docs + known_unrelated_license)
bad=[p for p in files if p not in known_reported]
print("changed_or_untracked_files=" + str(len(files)))
print("scoped_repair=" + str(len(scoped)))
print("known_unrelated_untracked_v0_8=" + str(len(known_unrelated_v0_8)))
print("known_unrelated_tracked_boundary_docs=" + str(len(known_unrelated_boundary_docs)))
print("known_unrelated_license_metadata=" + str(len(known_unrelated_license)))
print("out_of_scope_changed_or_untracked=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

预期结果：

- 无 whitespace errors。
- 结果文档和 autonomous detail 记录存在。
- 范围守卫证明没有超出 v0.7 修复范围的变更。当前 scoped repair 文件，包括父级状态面和 Campaign
  Plan 同步，会记录为 `scoped_repair`；如果出现无关 v0.8 或 roadmap/scope-boundary 文件，则单独报告。
  如果出现无关 license metadata 文件，也会单独报告，且不得纳入 v0.7 repair commit。

## 未运行的命令

后端运行时测试、API smoke、前端测试 / 构建、E2E、live Agent smoke、
完整自主运行器 / 完整套件、外部验证套件、投影应用验证和 v0.8 检查不要求运行，
除非实现触碰这些表面。

## 阻断项记录规则

任何失败命令、评估器 P1/P2 或剩余 V07-CR 问题，都必须在收尾前记录到
`review.md` 和总体验证结果。

## 禁止未验证声明规则

只有当前会话证据证明所有范围内命令通过、V07-CR P1/P2 阻断项已修复，
并且结果文档保留对外部套件、投影就绪、产品就绪、live Agent smoke、
完整自主运行器、运行时 / API / 前端 / E2E 和 v0.8 就绪状态的明确不声明后，
才能声明 clean pass。
