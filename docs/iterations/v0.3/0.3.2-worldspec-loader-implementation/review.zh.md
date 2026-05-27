# 评审

状态：`待评审`

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/**` | 新增完整 0.3.2 文档包，包含英文文档和中文镜像。 |
| `docs/iterations/v0.3/README.md`, `docs/iterations/v0.3/README.zh.md` | 在里程碑索引中把 0.3.2 标记为待评审。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `docs/iterations/v0.3/v0.3-plan.zh.md` | 将 0.3.2 状态同步为文档阶段待评审。 |
| `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md`, `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md` | 根据文档评审，把实现阶段禁止术语扫描修订为明确的无匹配检查。 |
| `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.md`, `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.zh.md` | 根据文档评审定义确定性 JSON Pointer 风格加载器错误路径约定。 |
| `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.md`, `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.zh.md` | 新增加载器错误路径约定验收要求。 |

## 已运行命令

本会话文档阶段已运行：

```bash
git status --short --branch
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' docs/iterations/README.md
sed -n '1,260p' docs/project-north-star.md
sed -n '1,260p' docs/product-model.md
sed -n '1,260p' docs/scope-boundaries.md
sed -n '1,260p' docs/roadmap.md
sed -n '1,260p' docs/iterations/v0.3/README.md
sed -n '1,320p' docs/iterations/v0.3/v0.3-plan.md
sed -n '1,260p' docs/iterations/v0.3/00-chatgpt-plan.md
sed -n '300,420p' docs/iterations/v0.3/v0.3-plan.md
sed -n '300,405p' docs/iterations/v0.3/v0.3-plan.zh.md
sed -n '1,220p' docs/contracts/worldspec-loader-contract.md
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
rg -n 'unsupported_input|parse_error|schema_validation_error|io_error|RuntimeEngine|WorldSpec|source_type|source_label' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

文档评审后的修订命令：

```bash
sed -n '1,260p' .agent-runs/20260527-213353-v0.3-0.3.2-worldspec-loader-implementation/docs-review.md
sed -n '1,240p' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md
sed -n '1,240p' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md
git diff --check
rg -n "^! rg -n 'RuntimeEngine\|runtime_engine\|FastAPI\|APIRouter\|archive\|params\|event'" docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md
rg -n "^! rg -n 'concrete demo\|character\|location\|story rule\|external validation-world data\|private oracle'" docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md
git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
```

第二次文档评审对应的修订命令：

```bash
sed -n '1,260p' .agent-runs/20260527-213936-v0.3-0.3.2-worldspec-loader-implementation/docs-review.md
sed -n '1,180p' docs/contracts/worldspec-loader-contract.md
git diff --check
rg -n 'JSON Pointer|/schema_version|/root|path = None' docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.zh.md docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.zh.md
git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\\?\\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\\?\\?) backend/app/|^( M| A|AM|MM|\\?\\?) backend/worldengine/'
git status --short
```

## 测试结果

- `git status --short --branch` 退出码为 `0`；工作区包含新增 0.3.2 package
  文档、v0.3 里程碑 / 计划状态同步，以及预先存在的已修改 0.3.1 README 文件。
- `git diff --check` 退出码为 `0`；未报告空白错误。
- 英文和中文 package 必需文件存在性检查退出码为 `0`。
- 状态同步 grep 退出码为 `0`；0.3.2 在 package README、里程碑索引和 v0.3
  计划中标记为 `ready for review` / `待评审`。
- 加载器要求术语 grep 退出码为 `0`；必需错误类别、来源元数据术语、
  `WorldSpec` 和运行时边界引用都存在。
- 实现范围状态检查退出码为 `0`；文档阶段没有修改后端、前端、schema、fixture、
  迁移、测试实现或旧运行时路径。
- 文档评审 P1 修订已将实现阶段禁止术语扫描改为英文和中文测试计划中的
  `! rg -n ...` 无匹配检查。
- 文档修订阶段的 `git diff --check` 退出码为 `0`；未报告空白错误。
- 文档修订阶段的实现范围状态检查退出码为 `1` 且无匹配；未修改后端、前端、
  schema、fixture、迁移、测试实现或旧运行时路径。
- 第二次文档评审 P1 修订已在 `technical-design.zh.md` 中定义 JSON Pointer
  风格 `WorldSpecLoaderError.path` 语义，在 `contract.zh.md` 中加入对应验收
  覆盖，并在 `test-plan.zh.md` 中要求聚焦 path 断言。
- 第二次文档修订的 `git diff --check` 退出码为 `0`；路径约定 grep 退出码为
  `0`；实现范围状态检查退出码为 `1` 且无匹配，确认未修改实现路径。

文档阶段未运行后端、前端、API、E2E、Agent smoke 或运行时测试，因为本包尚未
修改运行时、schema、API、前端、fixture、迁移或测试实现文件。

## 兼容性评审

文档阶段不改变运行时行为、schema 行为、API 响应形状、事件行为、归档行为、
参数行为、前端行为、后端测试行为、fixture 行为、迁移行为或旧目录
`backend/worldengine/` 行为。

## 范围评审

文档阶段保持在 0.3.2 package 文档和 v0.3 状态同步范围内。它不实现加载器代码，
不修改运行时、schema、API、前端、fixture、迁移或测试实现文件。

## 未解决发现

- P1：文档评审发现的实现阶段禁止术语扫描未取反问题，已在 `test-plan.md` 和
  `test-plan.zh.md` 中解决。
- P1：文档评审发现的加载器错误 `path` 风格未指定问题，已在
  `technical-design.md`、`contract.md` 和 `test-plan.md` 中解决，并同步中文镜像。
- P2：文档阶段未发现。
- P3：实现评审仍需在写代码后验证聚焦加载器测试、schema smoke 测试，以及
  runtime / API 非耦合。

## 最终判断

待评审。
