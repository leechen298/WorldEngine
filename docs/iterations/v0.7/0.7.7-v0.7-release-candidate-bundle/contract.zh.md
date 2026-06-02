# Contract

## Release-Candidate Inputs

Bundle 必须追踪：

- parent v0.7 docs and review。
- `0.7.0` 到 `0.7.6` 的所有 child package reviews。
- `0.7.5` evidence matrix。
- `0.7.6` audit report。
- current changed-file scope。

## 允许变更

- 创建或更新
  `docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle/` 下的文件。
- Release-candidate closeout 后更新 parent v0.7 status 和 route surfaces。

## 禁止变更

- 不标记 final release 或 final closeout。
- 不修改 implementation files。
- 不添加 tests、checkers、schemas、runtime behavior、API behavior、frontend behavior、
  migrations、fixtures、generated results 或 external repositories。
- 不改变已记录 evidence 之外的 readiness claims。

## Required Release-Candidate Contents

- completed child package table。
- current evidence map。
- explicit exclusions。
- unresolved findings。
- final-closeout recommendation。

## Closeout Gate

Closeout 只能在以下条件满足后发生：

- release-candidate summary 存在。
- evidence link checks 通过。
- `git diff --check` 通过。
- changed-file scope guard 通过。
- evaluators 未报告 blocking findings。
