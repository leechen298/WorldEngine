# Review

状态：`待评审`

## 变更文件

| 文件 | 变更 |
|---|---|
| `docs/contracts/external-fixture-runner-contract.md` | 新增公开外部验证样例运行器契约、允许的公开消费表面、脱敏报告要求、脱敏规则、兼容性约束和禁止推断。 |
| `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/**` | 新增完整 0.3.5 迭代包文档和中英文镜像。 |
| `docs/iterations/v0.3/README.md`, `docs/iterations/v0.3/README.zh.md` | 在里程碑索引中将 0.3.5 标为待评审。 |
| `docs/iterations/v0.3/v0.3-plan.md`, `docs/iterations/v0.3/v0.3-plan.zh.md` | 将 0.3.5 状态同步为文档阶段待评审。 |

## 已运行命令

```bash
git status --short --branch
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' docs/iterations/README.md
sed -n '1,220p' docs/project-north-star.md
sed -n '1,220p' docs/product-model.md
sed -n '1,180p' docs/scope-boundaries.md
sed -n '1,140p' docs/roadmap.md
sed -n '1,220p' docs/external-fixture-boundary.md
sed -n '1,220p' docs/validation-report-template.md
sed -n '1,240p' docs/contracts/worldspec-loader-contract.md
sed -n '1,260p' docs/contracts/runtime-context-bridge-contract.md
sed -n '1,260p' docs/iterations/v0.3/README.md
sed -n '1,170p' docs/iterations/v0.3/README.zh.md
sed -n '600,690p' docs/iterations/v0.3/v0.3-plan.md
sed -n '600,690p' docs/iterations/v0.3/v0.3-plan.zh.md
mkdir -p docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness
```

```bash
git diff --check
test -f docs/contracts/external-fixture-runner-contract.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/README.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/intent.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/contract.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/technical-design.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/test-plan.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/plan.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/review.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/README.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/intent.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/contract.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/plan.zh.md
test -f docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/review.zh.md
rg -n 'ExternalFixtureRunner|ExternalSuiteId|RedactedTargetId|PublicContractSurface|RedactedValidationReport|Allowed Consumption Surfaces|Redacted Validation Report Shape|Required Redaction Rules|Forbidden Inferences|Acceptance Requirements' docs/contracts/external-fixture-runner-contract.md
rg -ni 'report id|engine commit|public API / CLI version|external suite id|redacted target id|capability area|scenario id|status: `pass`, `fail`, or `blocked`|observed public behavior|redacted evidence summary|compatibility notes|unresolved issues' docs/contracts/external-fixture-runner-contract.md docs/validation-report-template.md
rg -n '0\.3\.5-external-fixture-contract-readiness|Status: ready for review|状态：`待评审`|状态：待评审' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/contracts/external-fixture-runner-contract.md docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\?\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\?\?) backend/app/|^( M| A|AM|MM|\?\?) backend/worldengine/'
git diff --stat
git status --short --branch
```

## 测试结果

- `git diff --check` 退出码为 `0`，未报告空白错误。
- 必需的英文和中文迭代包文件存在检查退出码为 `0`。
- 外部验证样例运行器契约标题 / 必需术语 grep 退出码为 `0`。
- 脱敏报告字段 grep 退出码为 `0`；新契约和既有验证报告模板中存在必需报告字段。
- 状态同步 grep 退出码为 `0`；0.3.5 在迭代包 README、里程碑索引和 v0.3 计划中
  标记为 `ready for review` / `待评审`。
- 具体锚点 sentinel no-match 检查退出码为 `0`；未发现具体样例或外部验证世界
  sentinel 内容。
- 实现范围状态检查退出码为 `0`；未修改后端、前端、schema、样例、迁移、测试实现或
  旧运行时路径。
- 最终 `git status --short --branch` 退出码为 `0`；变更路径限于 v0.3 文档和新增外部
  验证样例运行器契约 / 迭代包文档。
- 后端、前端、API、E2E、Agent smoke、运行时、构建、迁移、样例和 schema 测试不计划运行，
  因为本包只修改文档。

## 兼容性评审

本仅文档包不改变运行时行为、schema 行为、API 返回形状、事件行为、归档行为、参数行为、
前端行为、样例行为、迁移行为、后端测试行为和旧路径 `backend/worldengine/` 行为。

## 范围评审

本包保持在 0.3.5 文档范围内。它只定义公开外部验证样例运行器契约和迭代包文档。
它不实现外部运行器，也不添加外部样例内部细节。

## 假设

- 已完成的 0.3 加载器和桥接层包提供足够的公开契约上下文。
- 未来外部运行器可以使用抽象 suite、target 和 scenario 标识符。
- 脱敏报告证据在不暴露私有验证细节的情况下仍然有用。

## 未解决发现

- P1：未发现。
- P2：未发现。
- P3：未来外部运行器可能需要更多公开 CLI 或 API 文档，才能端到端运行。
- P3：如果自由文本报告不适合自动化，脱敏报告可能需要后续包提供更严格的机器可读 schema。

## 最终评估

待评审
