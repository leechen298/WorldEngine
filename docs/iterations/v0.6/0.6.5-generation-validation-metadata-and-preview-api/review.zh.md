# 评审

状态：review complete

implementation_authorized: yes

## 修改文件

Documentation-stage files：

- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/README.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/README.zh.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/intent.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/intent.zh.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/contract.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/contract.zh.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/technical-design.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/technical-design.zh.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/test-plan.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/test-plan.zh.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/plan.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/plan.zh.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/review.md`
- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/review.zh.md`

为 active child 更新的 parent status files：

- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/GOAL_RUNNER.md`
- `docs/iterations/v0.6/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/CURRENT_STATE.zh.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `docs/iterations/v0.6/v0.6-plan.zh.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/review.zh.md`

本 package documentation-stage review 不授权或修改 implementation files。

本 package implementation files changed：

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_generation_preview_api.py`

## 已运行命令

Documentation checks：

```bash
git diff --check
```

Result：通过，无输出。

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

Result：

```text
missing=0
```

```bash
rg -n "POST /world/generation/preview|GenerationPreviewRequest|GenerationPreviewResponse|preview_generation|implementation_authorized: no|ApiResponse|ApiErrorResponse" docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api
```

Result：通过。Required API/preview contract terms 已在本 package 中找到。

```bash
python3 -c 'from pathlib import Path
import re
bad=[]
for path in Path("docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api").glob("*.zh.md"):
    in_fence=False
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        if line.startswith("```"):
            in_fence=not in_fence
            continue
        if in_fence or not line.startswith("#"):
            continue
        text=line.lstrip("#").strip()
        has_latin=bool(re.search(r"[A-Za-z]", text))
        has_cjk=bool(re.search(r"[\u4e00-\u9fff]", text))
        code_like=text.startswith("`") or text.startswith("0.6.") or "`" in text
        if has_latin and not has_cjk and not code_like:
            bad.append(f"{path}:{lineno}:{line}")
print("generic_english_only_headings=" + str(len(bad)))
for item in bad:
    print(item)
raise SystemExit(1 if bad else 0)'
```

Result：

```text
generic_english_only_headings=0
```

```bash
rg -n 'Campaign status: in progress / 0\.6\.5 ready for review|Current route: `documentation-review-needed`|0\.6\.5-generation-validation-metadata-and-preview-api: ready for review|implementation_authorized: no' docs/iterations/v0.6/CURRENT_STATE.md docs/iterations/v0.6/README.md docs/iterations/v0.6/review.md
```

Result：通过。英文 current status surfaces 包含预期 active child state、route 和 closed
implementation authorization。

```bash
rg -n 'Campaign status：in progress / 0\.6\.5 ready for review|Current route：`documentation-review-needed`|0\.6\.5-generation-validation-metadata-and-preview-api: ready for review|implementation_authorized: no' docs/iterations/v0.6/CURRENT_STATE.zh.md docs/iterations/v0.6/README.zh.md docs/iterations/v0.6/review.zh.md
```

Result：通过。中文 current status surfaces 包含预期 active child state、route 和 closed
implementation authorization。

```bash
python3 -c "import subprocess; allowed=('docs/iterations/v0.6/','backend/app/core/world_generation.py','backend/app/schemas/world_generation.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_plan_import_boundary.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_world_generation_schema.py'); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[]
for line in lines:
    path=line[3:]
    if not path.startswith(allowed):
        bad.append(line)
print('unexpected_status=' + str(len(bad)))
[print(item) for item in bad]
raise SystemExit(1 if bad else 0)"
```

Result：

```text
unexpected_status=0
```

## 测试结果

Documentation-stage checks passed：

- `git diff --check`：通过，无输出。
- Required package docs and mirrors：`missing=0`。
- Required API/preview contract terms：present。
- Chinese mirror heading audit：`generic_english_only_headings=0`。
- English 和 Chinese active status surfaces：expected route 和 implementation
  authorization present。
- Scope guard：`unexpected_status=0`。

Backend implementation tests 在 `implementation_authorized: yes` 前有意不运行。

Implementation-stage TDD 和 verification：

- RED route test：
  `PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py -q`
  失败为 `7 failed`；失败均是缺少 `/world/generation/preview` 的预期 404。
- GREEN route test：
  `PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py -q`
  通过，`7 passed`。
- Evaluator-driven RED for nested payload and imported-plan provenance：
  `PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py -q`
  失败为 `3 failed, 7 passed`；覆盖 nested prompt/extra fields 和 import passed /
  generation failed provenance。
- 修复后同命令通过，`10 passed`。
- Code-review-driven RED for sensitive metadata leakage and bounded summary：
  `PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py -q`
  失败为 `2 failed, 13 passed`；覆盖 `prompt` / `provider_trace` 经
  `worldspec_preview` metadata 泄漏，以及 unbounded `preview_summary.root_label`。
- 修复后同命令通过，`15 passed`。
- Focused suite：
  `PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py -q`
  通过，`62 passed`。
- Adjacent API compatibility：
  `PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py app/tests/test_agent_loop_api.py app/tests/test_event_api_compat.py -q`
  通过，`28 passed`。
- Full backend regression：
  `PYTHONPATH=. .venv/bin/pytest app/tests -q`
  通过，`214 passed`。
- `git diff --check`：通过，无输出。
- Scope guard：`out_of_scope=0`。

## Evaluator 证据

Documentation/contract evaluator verdict：PASS。

- P1 findings：none。
- P2 findings：none。
- P3 findings：none。
- Authorization recommendation：`ready for implementation` /
  `implementation_authorized: yes`。
- Evaluator 确认 package docs 和中文镜像齐全，API envelope 与 error semantics 被保留，
  implementation scope 限于已批准 backend API/schema/core/test paths，forbidden
  frontend、persistence、live AI/provider、prompt、concrete-content、runtime、Agent、
  loader、existing-envelope 和 `backend/worldengine/**` surfaces 均已明确，test coverage
  足够，parent status surfaces 一致。

Implementation-scope evaluator final verdict：PASS。

- P1 findings：none。
- P2 findings：none。
- P3 findings：none。
- 早前 nested prompt/extra-field acceptance 和 imported-plan failed-generation
  provenance 的 P2 findings 已修复并复查。

Code-review evaluator final verdict：PASS。

- P1 findings：sensitive worldspec metadata redaction 后 none。
- P2 findings：import-source 和 bounded-summary 修复后 none。
- P3 findings：none。

Validation-evidence evaluator final verdict：PASS。

- P1 findings：none。
- P2 findings：scope guard allowlist 修正并复查为 `out_of_scope=0` 后 none。
- P3 findings：none。

## 兼容性评审

基于 focused 和 adjacent API tests，existing API envelopes 以及 adjacent event/Agent-loop
API behavior 保持兼容。Existing runtime、loader、Agent/memory、archive、params、frontend 和
`backend/worldengine/` behavior 未被本 package 修改。

## 范围评审

Implementation 停留在本 package approved backend schema/core/route/test scope 内。
Scope guard 报告 `out_of_scope=0`。

## 未解决问题

- P1：none。
- P2：none。
- P3：none。

## 最终评估

Review complete。`0.6.5` 已实现 generation preview API、bounded metadata、sensitive
metadata redaction、request-shape validation、route wiring 和 focused tests。不声明
frontend UI、E2E、Agent smoke、autonomous validation、external validation、projection
readiness、product readiness、release readiness、generation quality、runtime readiness
或 regeneration readiness。
