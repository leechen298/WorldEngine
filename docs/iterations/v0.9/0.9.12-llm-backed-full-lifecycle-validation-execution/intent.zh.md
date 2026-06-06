# Intent

英文镜像：`intent.md`。

## Problem

v0.9 已完成到 checker support 和 Validation Client handoff contract，但当前 evidence chain 还没有
端到端执行 LLM-backed lifecycle。在 documented suite 产出 public artifacts、checker/scorecard
output 和 second-Agent review 前，版本不能声明 LLM-backed lifecycle PASS。

## Intent

把 validation 当作 evidence work 运行，而不是 product implementation。本 package 应发现并分类真实状态：

- 所有 critical evidence 通过时为 PASS。
- product、checker、client evidence、redaction 或 scenario behavior 错误时为 FAIL。
- provider quota、missing environment、unavailable service 或 missing precondition 阻止 valid run
  时为 BLOCKED。
- 只有有明确记录的 intentional skip 才可记为 NOT_RUN。

## Non-Intent

本 package 不修 product code、不重写 generated results、不新增 fixtures、不改变 checker semantics、
不实现 Validation Client features，也不声明 product readiness。
