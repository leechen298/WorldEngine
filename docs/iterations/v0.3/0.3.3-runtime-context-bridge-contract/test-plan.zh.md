# Test Plan

## 文档检查

- 验证必需迭代包文件和中文镜像存在。
- 验证 `docs/contracts/runtime-context-bridge-contract.md` 包含必需桥接概念、
  可接受输入、上下文字段、错误类别、兼容性表面和禁止推断。
- 验证英文和中文里程碑索引把 0.3.3 标记为 `ready for review` / `待评审`。
- 验证已触及文档没有引入具体演示世界锚点。
- 验证变更文件保持在允许的文档路径内。

## 后续实现测试

`0.3.4-runtime-context-bridge-implementation` 应添加聚焦测试覆盖：

- 从成功加载的 `WorldSpec` 派生上下文。
- 对不支持的桥接输入返回 `unsupported_input`。
- 对不完整加载器输出返回 `invalid_loaded_worldspec`。
- 对 schema 校验之外的派生失败返回 `context_derivation_error`。
- 未提供上下文时，默认 `RuntimeEngine` 构造和 `step()` 行为不变。
- 可选上下文存储不改变 `RuntimeEngine.step()` 输出。
- 不产生原始 `WorldSpec` 事件 payload。
- 如果实现触及这些表面，则 `/runtime/state`、`/runtime/step`、
  `/world/events` 和 `/world/event-steps` 响应形状不变。
- 如果实现触及运行时构造，则参数和归档行为不变。
- 除非经评审包明确允许，否则不改变前端、fixture、migration、持久化或旧
  路径。

这些测试不会在本仅文档包中实现或运行。

## 命令

```bash
git status --short --branch
git diff --check
test -f docs/contracts/runtime-context-bridge-contract.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.zh.md
test -f docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.zh.md
rg -n 'RuntimeContextBridge|RuntimeContextInput|RuntimeContext|RuntimeContextSummary|RuntimeContextBridgeError|unsupported_input|invalid_loaded_worldspec|context_derivation_error|Accepted Input|Runtime Context Shape|Compatibility Evidence Required Before Implementation' docs/contracts/runtime-context-bridge-contract.md
rg -n 'tick|world_time_seconds|/runtime/state|/runtime/step|/world/events|/world/event-steps|params|archive|frontend|backend/worldengine|raw `WorldSpec`|WorldCell.*runtime module' docs/contracts/runtime-context-bridge-contract.md docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract
rg -n 'Status: ready for review|状态：`待评审`|状态：待评审|0\.3\.3-runtime-context-bridge-contract' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/contracts/runtime-context-bridge-contract.md docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

具体锚点 grep 是无匹配检查。如果未来文档评审要求某个词只出现在禁止变更
句子中，需要在 `review.md` 记录匹配和理由。

## 验收标准

- 必需文档和中文镜像存在。
- 桥接契约标题和必需术语存在。
- 迭代包 README 和里程碑索引中的状态为 `ready for review`。
- 中文镜像具有等价状态和范围。
- 范围检查显示本包未修改实现文件。
- `git diff --check` 通过。
- 文档记录假设、未决风险、兼容性证据要求，以及仅文档不运行测试的理由。

## 未运行

本包是仅文档包，不修改运行时、schema、API、前端、fixture、migration 或测试
实现文件，因此不计划运行后端、前端、API、E2E、Agent smoke 或运行时行为
测试。
