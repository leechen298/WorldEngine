# 测试计划

## 文档检查

- 验证必需迭代包文件存在。
- 验证 `docs/contracts/worldspec-loader-contract.md` 包含必需加载器概念、
  输入形式、输出字段和错误类别。
- 验证英文和中文里程碑索引把 0.3.1 标记为 `ready for review` / `待评审`。
- 验证已触及文档不包含具体演示世界锚点。
- 验证变更文件仍在允许的文档路径内。

## 后续实现测试

`0.3.2-worldspec-loader-implementation` 应新增聚焦测试，覆盖：

- 有效的最小 mapping 输入。
- 有效 JSON 字符串或 bytes 输入。
- 如果实现了文件输入，覆盖可选的文件 JSON 输入。
- 不支持的输入类型。
- 格式错误的 JSON 解析错误。
- 不支持 `schema_version` 的 schema 校验失败。
- 无效 root cell 的 schema 校验失败。
- 成功输出中的中立来源元数据。
- 没有 `RuntimeEngine`、事件、归档、参数、API、持久化或前端副作用。

这些测试不在本仅文档包中实现或运行。

## 命令

```bash
git status --short --branch
git diff --check
test -f docs/contracts/worldspec-loader-contract.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/intent.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/contract.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/technical-design.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/test-plan.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/plan.md
test -f docs/iterations/v0.3/0.3.1-worldspec-loader-contract/review.md
rg -n 'WorldSpecLoader|WorldSpecInput|LoadedWorldSpec|WorldSpecLoaderError|unsupported_input|parse_error|schema_validation_error|io_error|Accepted Inputs|Successful Output|Validation Semantics' docs/contracts/worldspec-loader-contract.md
rg -n 'Status: ready for review|Status: `ready for review`|状态：`待评审`|状态：待评审|0\.3\.1-worldspec-loader-contract' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.md
rg -n 'concrete demo|character|location|story rule|external validation-world data|private oracle' docs/contracts/worldspec-loader-contract.md docs/iterations/v0.3/0.3.1-worldspec-loader-contract docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
git status --porcelain=v1 -uall | rg -v '^( M docs/iterations/v0\.3/0\.3\.0-v0\.3-planning-and-compatibility-baseline/README\.md| M docs/iterations/v0\.3/README\.md| M docs/iterations/v0\.3/README\.zh\.md| M docs/iterations/v0\.3/v0\.3-plan\.md| M docs/iterations/v0\.3/v0\.3-plan\.zh\.md|\?\? docs/contracts/worldspec-loader-contract\.md|\?\? docs/iterations/v0\.3/0\.3\.1-worldspec-loader-contract/)'
```

具体锚点扫描预期只出现禁止性边界文字，而不是新增 fixture 内容。

## 验收标准

- 所有必需文档存在。
- 加载器契约标题和必需错误类别存在。
- package README 和里程碑索引中的状态为 `ready for review` / `待评审`。
- 中文镜像具有等价状态和范围。
- 范围检查显示本包没有修改实现文件。
- 预先存在的已修改 `0.3.0` package README 不属于本包，并且不纳入 0.3.1
  范围。
- `git diff --check` 通过。

## 未运行

本包是仅文档包，且不修改运行时、schema、API、前端、fixture、迁移或测试实现
文件，因此不计划运行后端、前端、API、E2E、Agent smoke 或运行时测试。
