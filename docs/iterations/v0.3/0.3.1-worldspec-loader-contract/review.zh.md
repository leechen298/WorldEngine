# 评审

状态：`评审完成`

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/contracts/worldspec-loader-contract.md` | 新增加载器契约，覆盖输入、输出、错误、校验、示例、兼容性和禁止推断。 |
| `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/**` | 新增完整 0.3.1 迭代包文档和中文镜像。 |
| `docs/iterations/v0.3/README.md`, `docs/iterations/v0.3/README.zh.md` | 在里程碑索引中把 0.3.1 标记为待评审。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `docs/iterations/v0.3/v0.3-plan.zh.md` | 同步 0.3.1 状态为待评审。 |
| `docs/iterations/v0.3/0.3.0-v0.3-planning-and-compatibility-baseline/README.md` | 回滚检查点 `40db35453f915623ff2938e660abf71ec332b017` 中包含的越界 0.3.0 状态编辑。 |

评审后状态修正：

- `docs/contracts/worldspec-loader-contract.md` 已标记为 `review complete`。
- `docs/iterations/v0.3/README.zh.md` 对已完成迭代包使用中文评审完成
  状态。
- `docs/iterations/v0.3/v0.3-plan.md` 和
  `docs/iterations/v0.3/v0.3-plan.zh.md` 将 0.3.1 标记为
  `review complete` / `评审完成`。
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.zh.md`
  使用中文评审完成状态，并让评审清单与英文镜像同步。

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
git diff --name-only origin/v0.3 -- docs/iterations/v0.3/0.3.0-v0.3-planning-and-compatibility-baseline/README.md
! git diff --name-only origin/v0.3 | rg -v '^(docs/contracts/worldspec-loader-contract\.md|docs/iterations/v0\.3/README\.md|docs/iterations/v0\.3/README\.zh\.md|docs/iterations/v0\.3/v0\.3-plan\.md|docs/iterations/v0\.3/v0\.3-plan\.zh\.md|docs/iterations/v0\.3/0\.3\.1-worldspec-loader-contract/)'
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
- 变更文件范围检查退出码为 `0`；没有报告实现路径。
- 最后的 `git status --short --branch` 退出码为 `0`。
- 文档修订已纠正
  `.agent-runs/20260527-205813-v0.3-0.3.1-worldspec-loader-contract/docs-review.md`
  中的 P1 范围证据问题：检查点
  `40db35453f915623ff2938e660abf71ec332b017` 中越界的 `0.3.0` README
  变更已回滚，并且
  `git diff --name-only origin/v0.3 -- docs/iterations/v0.3/0.3.0-v0.3-planning-and-compatibility-baseline/README.md`
  在修正后没有输出路径。
- 基于 `git diff --name-only origin/v0.3` 的累计分支范围检查在取反
  `rg` 下退出码为 `0`；分支 diff 中没有保留 0.3.1 加载器契约、0.3.1
  迭代包文档或 v0.3 状态同步文档之外的路径。
- 后续文档评审
  `.agent-runs/20260527-210415-v0.3-0.3.1-worldspec-loader-contract/docs-review.md`
  对检查点 `f0f7b54` 报告无阻塞问题，并确认该仅文档包可交接给下一
  mixed/code 包实现。

本包是仅文档包，且不修改运行时、schema、API、前端、fixture、迁移或测试实现
文件，因此不计划运行后端、前端、API、E2E、Agent smoke 或运行时测试。

## 兼容性评审

本仅文档包不改变运行时行为、schema 行为、API 响应形状、事件行为、归档行为、
参数行为、前端行为、后端测试行为、fixture 行为、迁移行为或旧目录
`backend/worldengine/` 行为。

## 范围评审

本包保持在 0.3.1 文档范围内。它只定义加载器契约和迭代包文档，不实现加载器
或桥接行为。较早提交的检查点包含了越界的 `0.3.0` README 状态编辑；本次文档
修订已把该路径从分支累计 diff 中移除，并将 0.3.1 证据限定为加载器契约、0.3.1
迭代包文档，以及 v0.3 里程碑 / 计划状态同步。

## 未解决发现

- P1：未发现。
- P2：未发现。
- P3：未发现。

## 最终判断

评审完成。
