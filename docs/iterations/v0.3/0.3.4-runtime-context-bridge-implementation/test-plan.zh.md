# 测试计划

## 单元测试

在 `backend/app/tests/test_runtime_context_bridge.py` 添加聚焦测试：

- 从成功的 `LoadedWorldSpec` 派生上下文。
- 上下文字段匹配已评审形状。
- 不支持输入返回 `unsupported_input`。
- 未成功的加载器结果根据实现的输入 wrapper 返回 `unsupported_input` 或
  `invalid_loaded_worldspec`。
- 不完整加载输出返回 `invalid_loaded_worldspec`。
- 派生失败返回 `context_derivation_error`。
- 上下文 summary 只包含有界诊断字段。
- 上下文 summary 不包含原始 `WorldSpec` 对象或原始 `WorldSpec` 字典。
- 无上下文时默认 `RuntimeEngine()` 构造和 `step()`。
- 如果添加可选上下文存储，`RuntimeEngine.step()` 输出保持不变。
- 带上下文推进运行时时，不出现原始 `WorldSpec` 事件 payload。

## 回归测试

运行被触及兼容表面的既有聚焦测试：

- `backend/app/tests/test_runtime_step.py`
- `backend/app/tests/test_event_api_compat.py`
- `backend/app/tests/test_event_schema_compat.py`
- `backend/app/tests/test_world_params.py`
- `backend/app/tests/test_params_agent.py`
- `backend/app/tests/test_archive_snapshot_summary.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_worldspec_schema_smoke.py`

如果实现触及 `runtime_context.py`、`runtime_engine.py` 或聚焦测试之外的共享运行时
helper，则运行更广的后端测试。

## 命令

文档阶段检查：

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/README.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/intent.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/contract.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/plan.zh.md
test -f docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/review.zh.md
rg -n 'Status: ready for review|状态：`待评审`|状态：待评审|0\.3\.4-runtime-context-bridge-implementation' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation
rg -n 'RuntimeContextBridge|RuntimeContextInput|RuntimeContext|RuntimeContextSummary|RuntimeContextBridgeError|unsupported_input|invalid_loaded_worldspec|context_derivation_error|RuntimeEngine|world_time_seconds|/runtime/state|/runtime/step|/world/events|/world/event-steps|params|archive|frontend|backend/worldengine' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

实现阶段检查：

```bash
git status --short --branch
git diff --check
pytest backend/app/tests/test_runtime_context_bridge.py
pytest backend/app/tests/test_runtime_step.py
pytest backend/app/tests/test_event_api_compat.py
pytest backend/app/tests/test_event_schema_compat.py
pytest backend/app/tests/test_world_params.py backend/app/tests/test_params_agent.py
pytest backend/app/tests/test_archive_snapshot_summary.py
pytest backend/app/tests/test_worldspec_loader.py backend/app/tests/test_worldspec_schema_smoke.py
! rg -n 'APIRouter|FastAPI|archive|params_apply|migration|frontend|backend/worldengine' backend/app/core/runtime_context.py
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' backend/app/core/runtime_context.py backend/app/tests/test_runtime_context_bridge.py
```

带 `!` 前缀的 `rg` 命令是无匹配检查。如果已评审实现只是在负向测试或说明性注释
中需要匹配词，应去掉 `!` 运行匹配命令，检查每个匹配，并在 `review.md` 中记录理由。

## 验收标准

- 必需包文档和中文镜像存在。
- 包 README 和里程碑索引把 0.3.4 标记为 `ready for review` / `待评审`。
- 文档记录假设、开放风险、允许变更、禁止变更、验收要求和实现阶段验证。
- 实现只添加已批准的桥接代码、可选惰性运行时存储和聚焦测试。
- 聚焦运行时上下文桥接测试在实现会话中通过。
- 必需兼容测试在实现会话中通过。
- 范围检查显示没有超出已评审契约的 schema、API、前端、fixture、migration、
  持久化、参数、归档、事件或遗留实现变更。
- 具体锚点扫描显示未引入具体演示世界或外部验证世界内容。

## 未运行

文档阶段不计划运行后端、前端、API、E2E、Agent smoke 和运行时行为测试，因为未修改
实现文件。

实现阶段跳过的任何验证都必须在 `review.md` 中记录原因和残余风险。
