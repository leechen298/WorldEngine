# 测试计划

## 文档检查

- 确认必需的英文和中文包文件存在。
- 确认 `evidence-index.md`、`evidence-index.zh.md`、
  `compatibility-audit.md` 和 `compatibility-audit.zh.md` 存在。
- 确认包 README、v0.3 milestone index 和 v0.3 plan 都把 0.3.6 标记为 `ready for review`。
- 确认审计文档包含必需兼容性表面术语。
- 确认没有修改实现路径。
- 确认 touched docs 中没有具体演示或外部验证世界哨兵词。

## 命令

```bash
git diff --check
test -f docs/iterations/v0.3/evidence-index.md
test -f docs/iterations/v0.3/evidence-index.zh.md
test -f docs/iterations/v0.3/compatibility-audit.md
test -f docs/iterations/v0.3/compatibility-audit.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/README.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/intent.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/contract.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/technical-design.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/test-plan.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/plan.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/review.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/README.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/intent.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/contract.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/technical-design.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/test-plan.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/plan.zh.md
test -f docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit/review.zh.md
rg -n '0\.3\.6-runtime-bridge-evidence-and-compatibility-audit|Status: ready for review|状态：`待评审`|状态：待评审' docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit
rg -n 'runtime|API|event|archive|params|frontend|schema|fixture|legacy|WorldSpec loader|runtime context bridge|P1|P2|P3|handoff' docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit
! rg -n '[d]emo-world-name|[m]ap-001|[c]haracter-001|[l]ocation-001|[s]tory-rule|[v]alidation-world-data|[p]rivate-oracle' docs/iterations/v0.3/evidence-index.md docs/iterations/v0.3/evidence-index.zh.md docs/iterations/v0.3/compatibility-audit.md docs/iterations/v0.3/compatibility-audit.zh.md docs/iterations/v0.3/0.3.6-runtime-bridge-evidence-and-compatibility-audit docs/iterations/v0.3/README.md docs/iterations/v0.3/README.zh.md docs/iterations/v0.3/v0.3-plan.md docs/iterations/v0.3/v0.3-plan.zh.md
! git status --porcelain=v1 -uall | rg '^( M| A|AM|MM|\?\?) (backend|frontend|schemas|fixtures|migrations|tests)/|^( M| A|AM|MM|\?\?) backend/app/|^( M| A|AM|MM|\?\?) backend/worldengine/'
git status --short --branch
```

## 验收标准

- 所有文档检查成功退出。
- 没有实现文件变更。
- 审计文档列出明确假设、风险和 P1/P2/P3 发现。
- 对运行时、API、事件、归档、参数、前端可见、schema、样例和旧路径表面完成分类。
- 不声称运行时、构建、E2E、UI smoke、Agent smoke 或后端 pytest 通过，除非引用既有包 review 证据或本会话实际运行。

## 未运行

后端、前端、API、E2E、Agent smoke、运行时行为、构建、迁移、样例和 schema 测试不在本包计划内，
因为本包只修改文档。
