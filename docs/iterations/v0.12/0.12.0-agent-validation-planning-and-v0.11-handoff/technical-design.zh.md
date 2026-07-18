# Technical Design

英文源文件：`technical-design.md`。

这是 documentation-only package，不包含 runtime architecture changes。

## Documentation Architecture

- `README.md` 记录 scope、v0.11 handoff facts、caveats 和 next route。
- `intent.md` 说明 Agent continuity work 为什么必须从 rule-bound world evidence 开始。
- `contract.md` 定义 allowed/forbidden changes 和 compatibility constraints。
- `test-plan.md` 定义 documentation checks 和未运行命令。
- `plan.md` 定义本 handoff package 的执行顺序。
- `review.md` 记录 documentation-stage evidence、evaluator review 和 parent route
  synchronization。

## Handoff Model

本包只把 v0.11 evidence 当作 input：

```text
v0.11 rule-bound world PASS
-> 0.12.0 handoff docs
-> 0.12.1 Agent public state/runtime loop docs
```

本包不得从 v0.11 event/diff evidence 推断 Agent autonomy。Agent behavior 只能在后续
reviewed package 中开始。

## Parent Route Update

Documentation evaluator review 通过后，parent v0.12 docs 可以更新：

- active child package：本 docs-only package 关闭后为 none。
- current route：
  `0.12.1-agent-public-state-and-runtime-loop-documentation-package-needed`。
- implementation authorization：no。
- evidence execution authorization：no。
