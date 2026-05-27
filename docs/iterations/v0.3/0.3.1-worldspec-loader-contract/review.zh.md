# 评审

状态：`待评审`

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/contracts/worldspec-loader-contract.md` | 新增加载器契约，覆盖输入、输出、错误、校验、示例、兼容性和禁止推断。 |
| `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/**` | 新增完整 0.3.1 迭代包文档和中文镜像。 |
| `docs/iterations/v0.3/README.md`, `docs/iterations/v0.3/README.zh.md` | 在里程碑索引中把 0.3.1 标记为待评审。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `docs/iterations/v0.3/v0.3-plan.zh.md` | 同步 0.3.1 状态为待评审。 |

## 已运行命令

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
git status --short --branch
```

## 测试结果

- `git status --short --branch` 退出码为 `0`；工作区包含 v0.3 文档变更、
  新增加载器契约，以及预先存在的已修改 `0.3.0` README。
- `git diff --check` 退出码为 `0`；未报告空白错误。
- 英文和中文必需迭代包文件存在性检查退出码为 `0`。
- 加载器契约标题和术语 grep 退出码为 `0`；必需概念、输入 / 输出标题和错误
  类别都存在。
- 状态同步 grep 退出码为 `0`；英文文档中 0.3.1 为 `ready for review`，中文
  文档中为 `待评审`。
- 具体锚点扫描退出码为 `0`，结果只包含边界、禁止变更和验证文字；没有新增
  具体 fixture 内容。
- 变更文件范围检查退出码为 `0`；没有报告实现路径。预先存在的已修改
  `0.3.0` README 仍在本包范围之外。
- 最后的 `git status --short --branch` 退出码为 `0`。

本包是仅文档包，且不修改运行时、schema、API、前端、fixture、迁移或测试实现
文件，因此不计划运行后端、前端、API、E2E、Agent smoke 或运行时测试。

## 兼容性评审

本仅文档包不改变运行时行为、schema 行为、API 响应形状、事件行为、归档行为、
参数行为、前端行为、后端测试行为、fixture 行为、迁移行为或旧目录
`backend/worldengine/` 行为。

## 范围评审

本包保持在 0.3.1 文档范围内。它只定义加载器契约和迭代包文档，不实现加载器
或桥接行为。

已知预先存在的工作区变更：

- `docs/iterations/v0.3/0.3.0-v0.3-planning-and-compatibility-baseline/README.md`
  在本包开始前已经被修改，本次 0.3.1 工作未编辑该文件。

## 未解决发现

- P1：未发现。
- P2：未发现。
- P3：未发现。

## 最终判断

待评审。
