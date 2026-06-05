# 完整产品验证执行手册

状态：计划中的执行手册，未执行

英文镜像：`runbook.md`。

## 目的

本文描述后续验证聊天如何执行完整 WorldEngine 产品验证。它不声明验证已经运行。

## Preflight

1. 阅读：
   - `AGENTS.md`。
   - `docs/project-north-star.md`。
   - `docs/product-model.md`。
   - `docs/scope-boundaries.md`。
   - `docs/roadmap.md`。
   - `docs/testing/complete-product-validation/README.md`。
   - `docs/testing/complete-product-validation/validation-spec.md`。
   - `docs/testing/complete-product-validation/scenario-matrix.md`。
   - `docs/testing/product-capability-validation-playbook.md`。
2. 记录当前 branch、commit、dirty files，以及 ignored generated artifact directories。
3. 明确验证范围：
   - 只验证当前产品基线。
   - 是否包含 LLM-backed lifecycle。
   - 是否包含外部 Validation Client。
4. 创建 result directory：

```text
test-results/product-validation/<timestamp>-complete-product-validation/
```

如果运行 LLM-backed autonomous validation，也创建：

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

## 执行顺序

### Stage 0: Documentation and scope audit

- 确认没有 claim 与 `docs/iterations/**/CURRENT_STATE.md` 冲突。
- 确认没有从 historical closeout 推断 product PASS。
- 确认 core docs 或 fixtures 中没有 external validation world content。
- 记录 scope exclusions。

### Stage 1: Schema、contract 和 checker fixtures

运行版本对应的 schema 和 checker commands。完整运行应包含当前已有 checker fixtures：

```bash
make validate-agent-smoke-fixtures
make validate-agent-autonomous-fixtures
```

再加入 active version 或 result plan 中的 contract-specific commands。

### Stage 2: Backend focused tests

先运行与能力矩阵绑定的 focused backend tests，再跑 broad regression。具体文件随版本变化，
但应覆盖：

- recursive schemas 和 loader bridge。
- runtime、events、params、snapshots 和 archive behavior。
- Agent loop 和 memory substrate。
- generation 和 import boundaries。
- in-scope projection/readiness/report checkers。

### Stage 3: Backend broad regression

运行 active code path 的 backend broad suite。

### Stage 4: Frontend unit and build

dashboard 行为在范围内时，运行 frontend unit tests 和 build。

### Stage 5: Browser E2E

运行当前 E2E scenarios。E2E PASS 必须来自 assertions，不是只有页面加载成功。
状态变更 flow 应尽量 cross-check API/event evidence。

### Stage 6: Agent smoke

Agent smoke result directories 只能通过 deterministic checker output 验证：

```bash
make validate-agent-smoke-result RESULT_DIR=<smoke-result-dir>
```

### Stage 7: Autonomous saved-result validation

autonomous result directories 只能通过 documented checker 验证：

```bash
make validate-agent-autonomous-result RESULT_DIR=<autonomous-result-dir>
```

不要把 saved-result validation 说成 full autonomous runner。

### Stage 8: LLM-backed lifecycle

只有明确 in scope 且实现支持存在时运行。遵循：

- `docs/testing/llm-backed-lifecycle-validation-plan.md`。
- 存在时遵循 `docs/testing/agent-autonomous/llm-backed-suite-execution.md`。

必要顺序：

1. provider live smoke。
2. LLM-backed world creation。
3. rule parameter evolution。
4. rule-compliant event generation。
5. persistent Agent autonomy evidence。
6. evidence export。
7. checker 或 scorecard。
8. 第二 Agent 只读复核。

### Stage 9: External client evidence review

如果 Validation Client 在范围内：

- 只通过 public WorldEngine APIs/contracts 操作。
- 确认客户端没有拥有 LLM、generation、Agent action 或 evaluator logic。
- 确认 operation logs 区分 UI/CLI actions 和 API evidence。
- 确认导出的 evidence bundle 已脱敏。

### Stage 10: Final verdict audit

填写 coverage matrix 和 result template。每个 capability 必须是：

- `pass`。
- `fail`。
- `blocked`。
- `skipped`。
- `out_of_scope`。

## Stop Rules

出现以下情况时停止并分类：

- evidence 中出现 secrets 或 private provider/Agent/evaluator data。
- direct API call 被记录为 Agent UI/CLI operation。
- deterministic mock behavior 被用作 live behavior 证明。
- LLM-backed validation 缺少 WorldEngine-owned live provider call path。
- required artifacts 缺失。
- claimed PASS source 缺 checker support。
- user direction 没有 rule adjudication 就直接成为 final world fact。

## Durable Result

结果写入：

```text
docs/testing/results/YYYY-MM-DD-complete-product-validation.md
docs/testing/results/YYYY-MM-DD-complete-product-validation.zh.md
```

使用 `result-template.md` 和 `result-template.zh.md`。
