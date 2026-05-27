# 评审

状态：`待评审`

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/**` | 添加完整 0.3.4 包文档及英文/中文镜像。 |
| `docs/iterations/v0.3/README.md`, `docs/iterations/v0.3/README.zh.md` | 在里程碑索引中将 0.3.4 标记为待评审。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `docs/iterations/v0.3/v0.3-plan.zh.md` | 将 0.3.4 状态同步为文档阶段待评审。 |
| `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md`, `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.zh.md` | 文档评审修订：将已知不可用的根目录 pytest 命令替换为后端 venv `python -m pytest` 命令。 |

## 已运行命令

```bash
git status --short --branch
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,220p' docs/iterations/README.md
sed -n '1,220p' docs/project-north-star.md
sed -n '1,220p' docs/product-model.md
sed -n '1,240p' docs/scope-boundaries.md
sed -n '1,260p' docs/roadmap.md
find docs/iterations/v0.3 -maxdepth 3 -type f | sort
sed -n '1,260p' docs/iterations/v0.3/README.md
sed -n '1,320p' docs/iterations/v0.3/v0.3-plan.md
sed -n '1,320p' docs/iterations/v0.3/00-chatgpt-plan.md
sed -n '1,260p' docs/iterations/v0.3/development-workflow.md
sed -n '509,609p' docs/iterations/v0.3/v0.3-plan.md
sed -n '1,240p' docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.md
sed -n '1,240p' docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.md
sed -n '1,220p' docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.md
sed -n '1,220p' docs/contracts/runtime-context-bridge-contract.md
sed -n '1,260p' backend/app/core/worldspec_loader.py
sed -n '1,260p' backend/app/core/runtime_engine.py
sed -n '1,240p' backend/app/core/event_bus.py
find backend/app/world/modules -maxdepth 2 -type f -print | sort
find backend/app/tests -maxdepth 1 -type f -print | sort
mkdir -p docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation
```

```bash
git diff --check
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.zh.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.zh.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.zh.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.zh.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.zh.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.zh.md && test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.zh.md
rg -n 'Status: ready for review|状态：`待评审`|状态：待评审|0\.3\.4-runtime-context-bridge-implementation' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation
rg -n 'RuntimeContextBridge|RuntimeContextInput|RuntimeContext|RuntimeContextSummary|RuntimeContextBridgeError|unsupported_input|invalid_loaded_worldspec|context_derivation_error|RuntimeEngine|world_time_seconds|/runtime/state|/runtime/step|/world/events|/world/event-steps|params|archive|frontend|backend/worldengine' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
git status --short --branch
```

文档评审修订：

```bash
git status --short --branch
sed -n '1,240p' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md
sed -n '1,240p' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.zh.md
sed -n '120,190p' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.md
rg -n "pytest backend/app/tests|backend/.*python -m pytest|\\.venv/bin/python -m pytest app/tests" docs/iterations/v0.3
git diff --check
rg -n "\\.venv/bin/python -m pytest app/tests/test_runtime_context_bridge\\.py|Run backend pytest commands from `backend/`" docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md
rg -n "\\.venv/bin/python -m pytest app/tests/test_runtime_context_bridge\\.py|后端 pytest 命令必须在 `backend/`" docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.zh.md
! rg -n "pytest backend/app/tests" docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

## 测试结果

- `git diff --check` 退出码为 `0`；未报告空白错误。
- 必需英文和中文包文件存在性检查退出码为 `0`。
- 状态同步 grep 退出码为 `0`；0.3.4 已在包和里程碑文档中标记为
  `ready for review` / `待评审`。
- 必需概念和兼容术语 grep 退出码为 `0`；桥接概念、错误类别、运行时端点、
  事件端点、参数、归档、前端和遗留边界术语均存在。
- 哨兵具体锚点无匹配检查退出码为 `0`；未发现具体 fixture 或外部验证世界哨兵内容。
- 实现范围状态检查退出码为 `0`；本次文档阶段包未修改 backend、frontend、
  schema、fixture、migration、测试实现或遗留运行时路径。
- 最终 `git status --short --branch` 退出码为 `0`；变更路径仅限 v0.3 文档和新的
  0.3.4 包文档。
- 文档评审修订 `git diff --check` 退出码为 `0`；英文和中文测试计划中的后端
  venv `python -m pytest` 实现阶段命令 grep 退出码为 `0`；0.3.4 测试计划中
  不再出现已知不可用的 `pytest backend/app/tests` 命令；实现范围状态检查退出码为
  `0` 且无匹配，确认未修改实现路径。

文档阶段不计划运行后端、前端、API、E2E、Agent smoke 和运行时行为测试，因为未修改
实现文件。

## 兼容评审

本次文档阶段包未改变运行时行为、schema 行为、API 响应形状、事件行为、归档行为、
参数行为、前端行为、后端测试行为、fixture 行为、migration 行为和遗留
`backend/worldengine/` 行为。

## 范围评审

本包保持在 0.3.4 文档范围内。它只创建包文档并更新状态，不实现桥接行为。

## 已解决文档评审发现

- P1：文档评审发现实现阶段 pytest 命令使用了根目录调用形式，而 0.3.2 证据已显示
  该形式会在本仓库环境中失败。本次文档修订已通过要求从 `backend/` 运行后端
  venv `python -m pytest` 命令修复。

## 未解决发现

- P1：文档评审修订后无。
- P2：起草期间未发现。
- P3：开始实现前仍需要文档评审。

## 最终评估

待评审

## 实现收尾证据

状态：实现完成

### 实现变更文件

| 文件 | 变更 |
|---|---|
| `backend/app/core/runtime_context.py` | 添加纯运行时上下文桥接 dataclass、结构化结果/错误模型、上下文派生和有界摘要 helper。 |
| `backend/app/core/runtime_engine.py` | 添加可选惰性 `runtime_context` 构造/from-env 透传存储和只读 accessor；运行时状态与 step 行为保持不变。 |
| `backend/app/tests/test_runtime_context_bridge.py` | 添加聚焦桥接、错误、摘要、运行时默认行为、惰性存储和无原始 WorldSpec 事件测试。 |
| `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.md`, `review.zh.md` | 添加实现收尾证据。 |

### 已运行实现命令

```bash
git status --short --branch
git diff --check
cd backend
.venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py
.venv/bin/python -m pytest app/tests/test_runtime_step.py
.venv/bin/python -m pytest app/tests/test_event_api_compat.py
.venv/bin/python -m pytest app/tests/test_event_schema_compat.py
.venv/bin/python -m pytest app/tests/test_world_params.py app/tests/test_params_agent.py
.venv/bin/python -m pytest app/tests/test_archive_snapshot_summary.py
.venv/bin/python -m pytest app/tests/test_worldspec_loader.py app/tests/test_worldspec_schema_smoke.py
cd ..
rg -n 'APIRouter|FastAPI|archive|params_apply|migration|frontend|backend/worldengine' backend/app/core/runtime_context.py; test $? -eq 1
rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' backend/app/core/runtime_context.py backend/app/tests/test_runtime_context_bridge.py; test $? -eq 1
git status --short --branch
```

### 实现测试结果

- `git diff --check` 退出码为 `0`；未报告空白错误。
- `.venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py` 退出码为 `0`；11 passed。
- `.venv/bin/python -m pytest app/tests/test_runtime_step.py` 退出码为 `0`；16 passed。
- `.venv/bin/python -m pytest app/tests/test_event_api_compat.py` 退出码为 `0`；2 passed。
- `.venv/bin/python -m pytest app/tests/test_event_schema_compat.py` 退出码为 `0`；10 passed。
- `.venv/bin/python -m pytest app/tests/test_world_params.py app/tests/test_params_agent.py` 退出码为 `0`；9 passed。
- `.venv/bin/python -m pytest app/tests/test_archive_snapshot_summary.py` 退出码为 `0`；14 passed。
- `.venv/bin/python -m pytest app/tests/test_worldspec_loader.py app/tests/test_worldspec_schema_smoke.py` 退出码为 `0`；11 passed。
- 运行时上下文禁止表面 grep 通过无匹配断言，整体退出码为 `0`。
- 具体锚点 grep 通过无匹配断言，整体退出码为 `0`。

### 实现兼容评审

桥接实现是纯函数边界，只从 `LoadedWorldSpec` 派生有界上下文。
`RuntimeEngine` 可接受可选上下文，但不会把它序列化进 `RuntimeState`，
不会在 `step()` 中使用它，也不会在事件 payload 中包含原始 `WorldSpec`
数据。当前实现会话中，运行时、事件 API、参数、归档、loader、schema smoke
和可选 `Event.refs` 兼容测试均已通过。

未修改 schemas、migrations、API routes、frontend 文件、fixtures、persistence
models、params 实现、archive 实现、event bus 行为或遗留 `backend/worldengine/`
文件。

### 实现范围评审

实现保持在已评审的 0.3.4 包范围内：一个新的桥接模块、一个聚焦惰性运行时
holder 变更、一个聚焦测试文件，以及允许的收尾证据更新。未实现场景生成、
Agent loop、记忆、投影、故事行为、具体 demo-world 内容、外部验证世界内容、
API 暴露或前端行为。

### 实现未解决发现

- P1：无。
- P2：无。
- P3：无。

### 实现最终评估

实现完成，可进入 runner checkpoint / 后续评审。
