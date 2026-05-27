# 测试计划

## 单元测试

新增 `backend/app/tests/test_worldspec_loader.py`，聚焦覆盖：

- 有效最小 mapping 输入。
- 有效 JSON 字符串输入。
- 有效 JSON bytes 输入。
- 如果实现文件加载，覆盖有效文件 JSON 输入。
- 不支持的输入类型返回 `unsupported_input`。
- 格式错误的 JSON 返回 `parse_error`。
- 不支持的 `schema_version` 返回 `schema_validation_error`。
- 无效 root cell 数据返回 `schema_validation_error`。
- 错误 `path` 规范化使用 JSON Pointer 风格路径，包括不支持 schema 版本时的
  `/schema_version`，以及无效 root cell 数据时的 `/root/...` 路径。
- 无法定位的加载器错误，例如不支持输入或无法定位的解析失败，返回
  `path = None`。
- 成功结果元数据：`source_type`、可选 `source_label` 和已校验
  `schema_version`。
- 没有 `RuntimeEngine`、API、事件、归档、参数、持久化、前端、fixture、迁移或
  旧路径副作用。

## 回归测试

运行现有覆盖 `WorldSpec` 校验的 schema smoke 测试。只有当实现触及加载器模块
或测试文件之外的共享 helper 时，才按影响范围运行更广的后端测试。

## 命令

文档阶段检查：

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.zh.md
test -f docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.zh.md
rg -n 'Status: ready for review|状态：`待评审`|状态：待评审|0\.3\.2-worldspec-loader-implementation' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.2-worldspec-loader-implementation
rg -n 'unsupported_input|parse_error|schema_validation_error|io_error|RuntimeEngine|WorldSpec|source_type|source_label|JSON Pointer|/schema_version|/root' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

实现阶段检查：

```bash
git status --short --branch
git diff --check
pytest backend/app/tests/test_worldspec_loader.py
pytest backend/app/tests/test_worldspec_schema_smoke.py
! rg -n 'RuntimeEngine|runtime_engine|FastAPI|APIRouter|archive|params|event' backend/app/core/worldspec_loader.py
! rg -n 'concrete demo|character|location|story rule|external validation-world data|private oracle' backend/app/core/worldspec_loader.py backend/app/tests/test_worldspec_loader.py
```

runtime / API 耦合扫描和具体锚点扫描都是无匹配检查。如果实现只需要在否定测试
或说明性注释中使用某个术语，应去掉 `!` 运行对应的 `rg -n ...` 命令，逐项评审
匹配，并在实现收尾前把理由记录到 `review.md` / `review.zh.md`。

## 验收标准

- 必需 package 文档和中文镜像存在。
- package README 和里程碑索引将 0.3.2 标记为 `ready for review` /
  `待评审`。
- 文档说明假设、未解决风险、允许变更、禁止变更、确定性加载器错误路径风格和
  可测试验收要求。
- 实现只新增已批准的加载器模块和聚焦测试，除非评审批准更窄的本地 helper。
- 当前实现会话中的聚焦加载器测试通过。
- 当前实现会话中的现有 `WorldSpec` schema smoke 测试通过。
- 范围检查显示没有运行时、schema、API、前端、fixture、迁移、持久化、归档、
  参数、事件或旧路径实现变更，除非本包契约明确批准。
- 具体锚点扫描没有引入具体演示世界或外部验证世界内容。

## 未运行

文档阶段不计划运行后端、前端、API、E2E、Agent smoke 或运行时行为测试，因为
没有修改实现文件。

实现阶段如跳过任何验证，必须在 `review.md` / `review.zh.md` 中记录原因和
剩余风险。
