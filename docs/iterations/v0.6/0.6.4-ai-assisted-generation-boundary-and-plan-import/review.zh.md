# 评审

Status: review complete

implementation_authorized: yes

## 变更文件

本 package documentation：

- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/README.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/README.zh.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/intent.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/intent.zh.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/contract.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/contract.zh.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/technical-design.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/technical-design.zh.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/test-plan.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/test-plan.zh.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/plan.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/plan.zh.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/review.md`
- `docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import/review.zh.md`

Implementation files 已在本 package contract 范围内完成：

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/tests/test_plan_import_schema.py`
- `backend/app/tests/test_plan_import_boundary.py`

## 已运行命令

Documentation-stage verification：

```bash
git diff --check
```

结果：通过，无输出。

```bash
python3 -c 'from pathlib import Path
base=Path("docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import")
required=["README.md","README.zh.md","intent.md","intent.zh.md","contract.md","contract.zh.md","technical-design.md","technical-design.zh.md","test-plan.md","test-plan.zh.md","plan.md","plan.zh.md","review.md","review.zh.md"]
missing=[p for p in required if not (base/p).is_file()]
print("missing=", missing)
print("count=", len(list(base.glob("*.md"))))'
```

结果：`missing= []`，`count= 14`。

```bash
rg -n 'PlanImportSource|PlanImportRequest|PlanImportResult|validate_plan_import|import_generation_plan|implementation_authorized: no' docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import
```

结果：通过；required package terms 均存在。

```bash
python3 -c 'from pathlib import Path
base=Path("docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import")
issues=[]
for path in sorted(base.glob("*.zh.md")):
    for idx,line in enumerate(path.read_text().splitlines(),1):
        if line.startswith("#") and any(word in line for word in ["Status", "Scope", "Implementation", "Validation", "Review", "Contract", "Plan", "Technical", "Test", "Current"]):
            issues.append(f"{path}:{idx}:{line}")
print("heading_issues=", len(issues))
print("\n".join(issues))'
```

结果：`heading_issues= 0`。

```bash
python3 -c 'import subprocess, re
status=subprocess.check_output(["git","status","--short"], text=True).splitlines()
allowed=[r"^ M docs/iterations/v0\.6/", r"^\?\? docs/iterations/v0\.6/0\.6\.[1234]-", r"^\?\? backend/app/core/world_generation\.py$", r"^\?\? backend/app/schemas/world_generation\.py$", r"^\?\? backend/app/tests/test_(world_generation_schema|template_catalog|deterministic_world_generation|generation_plan_schema|structured_generation_plan_compiler|plan_import_schema|plan_import_boundary)\.py$"]
violations=[line for line in status if not any(re.match(p,line) for p in allowed)]
print("violations=", violations)'
```

结果：`violations= []`。

```bash
rg -n 'Campaign status: in progress / 0\.6\.4 ready for review|Status: in progress / 0\.6\.4 ready for review|Active child package: `0\.6\.4-ai-assisted-generation-boundary-and-plan-import`|Current route: `documentation-review-needed`|Implementation authorization: no|0\.6\.4-ai-assisted-generation-boundary-and-plan-import: planned / ready for review' docs/iterations/v0.6/README.md docs/iterations/v0.6/CURRENT_STATE.md docs/iterations/v0.6/GOAL_RUNNER.md docs/iterations/v0.6/CAMPAIGN_PLAN.md docs/iterations/v0.6/review.md docs/iterations/v0.6/v0.6-plan.md
```

结果：通过；parent status surfaces 指向 `0.6.4`，当前 route 为
documentation review，implementation authorization 关闭。

Implementation-stage verification：

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py -q
```

Initial RED result before implementation：collection failed，出现 2 个 import
errors，缺少 `PlanImport*` schemas 和 `import_generation_plan` /
`validate_plan_import`。

First GREEN result after implementation：`30 passed`。

新增 nested prompt/free-form rejection 覆盖后的第二个 RED：
`test_plan_import_schema_rejects_prompt_fields_inside_untrusted_plan_payload`
失败，错误为 `DID NOT RAISE <class 'pydantic_core._pydantic_core.ValidationError'>`。

给 `PlanCell` 和 `GenerationPlan` 添加 `ConfigDict(extra="forbid")` 后的最终结果：
`31 passed`。

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py -q
```

最终结果：`47 passed`。

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

最终结果：`199 passed`。

```bash
git diff --check
```

最终结果：通过，无输出。

```bash
python3 -c 'import subprocess, re
status=subprocess.check_output(["git","status","--short"], text=True).splitlines()
allowed=[r"^ M docs/iterations/v0\.6/", r"^\?\? docs/iterations/v0\.6/0\.6\.[1234]-", r"^\?\? backend/app/core/world_generation\.py$", r"^\?\? backend/app/schemas/world_generation\.py$", r"^\?\? backend/app/tests/test_(world_generation_schema|template_catalog|deterministic_world_generation|generation_plan_schema|structured_generation_plan_compiler|plan_import_schema|plan_import_boundary)\.py$"]
violations=[line for line in status if not any(re.match(p,line) for p in allowed)]
print("violations=", violations)'
```

最终结果：`violations= []`。

```bash
rg -n 'openai|anthropic|provider SDK|api_key|secret|requests|httpx|aiohttp|urllib|backend/worldengine|frontend|migrations|prompt|WorldSpec\(|WorldCell\(|EntityRef\(' backend/app/core/world_generation.py backend/app/schemas/world_generation.py backend/app/tests/test_plan_import_schema.py backend/app/tests/test_plan_import_boundary.py
```

最终结果：只命中 prompt rejection tests 和既有 `WorldSpec` / `WorldCell`
construction。未新增 provider SDK、network、API、frontend、persistence、runtime、
external validation、projection 或 `backend/worldengine/` surface。

## 测试结果

Final focused package tests：`31 passed`。
Final adjacent compatibility tests：`47 passed`。
Final full backend regression：`199 passed`。

## 兼容性 review

Implementation 对 generation schema/core 做 additive 扩展。Focused、adjacent 和
full backend regression 继续覆盖既有 template generation 和 structured-plan compiler
行为。`GenerationPlan` 与 `PlanCell` 现在拒绝 unknown fields，避免 untrusted import 中的
nested prompt/free-form payload 被静默忽略。

## 范围 review

Scope guard 通过。Implementation 停留在 generation schema/core、focused plan-import
tests、package review docs 和 parent v0.6 status surfaces 内。未修改 API、frontend、
persistence、runtime、external validation、projection、concrete content 或
`backend/worldengine/` files。

## Subagent / Evaluator 证据

Read-only planning/code-surface subagent 已确认：

- `0.6.4` 必须是 mixed/code seven-file package，并带中文镜像。
- 最小 implementation 应保持在 generation schema/core 和 focused plan-import tests。
- live providers、prompts、API、frontend、persistence、runtime、external validation、
  projection、concrete content 和 `backend/worldengine/**` 都属于禁止范围。

Documentation/contract evaluator PASS：

- Subagent verdict：PASS；无 blocking P1/P2 findings。
- Subagent 引用的证据：
  - `contract.md:29-40` 限定 implementation files 与 tests。
  - `contract.md:45-72` 禁止 provider/network/prompts/API/frontend/
    persistence/runtime/concrete content，并要求通过
    `validate_generation_plan` validation。
  - `technical-design.md:7-12` 定义 provider-independent import boundary，
    不包含 provider calls、API routes、persistence 或 compile/run side effects。
  - `CURRENT_STATE.md:3-6` 在本次授权更新前显示 active `0.6.4`、
    `documentation-review-needed`，且 authorization 关闭。

Code-review evaluator PASS：

- Subagent verdict：PASS；P1/P2/P3 none。
- 它独立运行 focused `31 passed`、adjacent `47 passed`、full backend
  `199 passed`、`git diff --check` 和 scope guard `violations= []`。
- 它确认 `PlanCell` 和 `GenerationPlan` 使用 `ConfigDict(extra="forbid")`，
  `validate_plan_import()` 检查 redaction、JSON-compatible provenance/import
  metadata，并复用 `validate_generation_plan()`；失败路径不包含 accepted plan/source；
  tests 覆盖 nested prompt/free-form rejection。

Validation-evidence evaluator PASS：

- Subagent verdict：PASS for validation-evidence closeout；P1/P2/P3 none。
- 它独立运行 focused `31 passed`、adjacent `47 passed`、full backend
  `199 passed`、`git diff --check`、scope guard `violations= []` 和 forbidden-surface
  search。
- 它允许将本 package 和 parent status surfaces 更新为 `0.6.4 review complete` 并交接给
  `0.6.5`。

Closeout consistency evaluator PASS：

- 初始 evaluator pass 发现 `README.md/.zh.md` 中 active-child value 仍指向 0.6.4
  的 P2；随后已修复为指向
  `0.6.5-generation-validation-metadata-and-preview-api`。
- Final subagent verdict：PASS；P1/P2/P3 none。
- 它独立验证了 `git diff --check`、scope guard `violations= []`、expected status
  search、stale status search 和 full backend `199 passed`。
- 它确认 parent/child status surfaces 一致，`0.6.4` 可以算 review complete，handoff
  to `0.6.5` 正确，并且 active `0.6.5` child 的 implementation authorization 已关闭。

## 未解决 findings

- P1：未发现。
- P2：未发现。
- P3：未发现。

## 最终评估

Review complete。`0.6.4` 已在 package contract 范围内实现 provider-independent plan
import schemas、validation helpers、deterministic diagnostics 和 focused tests。它将
reviewed import/provenance semantics 交接给
`0.6.5-generation-validation-metadata-and-preview-api`。
