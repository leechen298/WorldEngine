# 0.12.0 Agent 验证规划与 v0.11 交接

英文源文件：`README.md`。

状态：review complete
类型：documentation-only handoff package
implementation_authorized: no
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

从已完成的 v0.11 rule-bound world evolution handoff 打开 v0.12，并准备第一个
Agent implementation package。

本包不实现 Agent runtime、memory、narrative inspection、checker automation 或
Validation Client behavior。它只记录 handoff facts，检查 v0.12 scope 是否从 public
rule-linked world evidence 出发，并在 review 后把 `0.12.1` 准备为下一个
documentation-package-needed route。

## 范围

允许：

- 创建本 `0.12.0` package document set 和中文镜像。
- 记录作为 v0.12 input 的 v0.11 closeout evidence。
- review 后同步 v0.12 parent status 和 route。
- 把 `0.12.1` 准备为下一个 documentation-package-needed route。

禁止：

- 不修改 runtime、API、schema、frontend、checker、fixture、provider、generated
  result、Validation Client、migration、persistence 或 `backend/worldengine/`
  implementation。
- 不执行 provider live call。
- 不执行外部 Validation Client，也不声明 external Validation Client PASS。
- 不实现 Agent runtime、autonomy、memory、rest、sleep、narrative、diagnostic 或
  checker。
- 不声明 complete MVP PASS。

## 来自 v0.11 的交接事实

v0.11 已在 rule-bound world evolution scope 内以 scoped `PASS` 关闭。

v0.12 可用 evidence：

- v0.10 的 public session/manifest/debug handoff surfaces 仍可用。
- provider/worldview preflight 可以标记 configured、safe mock、fallback 和 blocked
  provider states，但不声明 live-provider PASS。
- session-scoped structured rules 和 parameters 可 attach/read。
- natural-language direction 只能作为 world-level pressure；尝试 direct final facts 或
  Agent private-state changes 时会被 rejected。
- rule-compliant session evolution step 可 build/evaluate/apply public event candidates
  和 public diffs，并带 replay evidence。
- worldview fidelity checks 已覆盖 immediate 和 bounded-run public premise coverage；
  bounded-run 缺少 premise indicators 会 fail。
- v0.11 focused closeout regression suite `53 passed`。
- bounded-run coverage 修复后，closeout evaluator re-review PASS。

未转换成 v0.12 PASS 的已知 caveats：

- provider live call 未证明。
- external Validation Client automation 未证明。
- Agent autonomy、memory、rest/sleep、narrative、diagnostics 和 full MVP lifecycle
  未证明。
- frontend E2E、durable persistence 和 product readiness 未证明。

## 状态清单

- [x] Package documents drafted.
- [x] Documentation evaluator complete.
- [x] Parent v0.12 route synchronized.

## 下一 route

Documentation review 通过后，v0.12 应 route 到：

```text
0.12.1-agent-public-state-and-runtime-loop-documentation-package-needed
```
