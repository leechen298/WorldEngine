# Test Plan

## 文档检查

运行：

```bash
git diff --check
```

验证必需文件存在：

```bash
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
```

验证契约标题和必需术语：

```bash
rg -n 'ExternalFixtureRunner|ExternalSuiteId|RedactedTargetId|PublicContractSurface|RedactedValidationReport|Allowed Consumption Surfaces|Redacted Validation Report Shape|Required Redaction Rules|Forbidden Inferences|Acceptance Requirements' docs/contracts/external-fixture-runner-contract.md
```

验证脱敏和报告字段：

```bash
rg -ni 'report id|engine commit|public API / CLI version|external suite id|redacted target id|capability area|scenario id|status: `pass`, `fail`, or `blocked`|observed public behavior|redacted evidence summary|compatibility notes|unresolved issues' docs/contracts/external-fixture-runner-contract.md docs/validation-report-template.md
```

验证状态同步：

```bash
rg -n '0\.3\.5-external-fixture-contract-readiness|Status: ready for review|状态：`待评审`|状态：待评审' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness
```

验证没有新增具体样例 sentinel 锚点：

```bash
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/contracts/external-fixture-runner-contract.md docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
```

验证没有修改实现文件：

```bash
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\?\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\?\?) backend/app/|^( M| A|AM|MM|\?\?) backend/worldengine/'
```

## 不计划运行的测试

后端、前端、API、E2E、Agent smoke、运行时、构建、迁移、样例和 schema 测试不计划运行，
因为本包只修改文档。
