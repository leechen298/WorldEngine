# Intent

## 问题

v0.7 已完成 implementation、evidence 与 audit packages。Final closeout 不应从分散 evidence
开始，需要一个 reviewable release-candidate bundle，说明什么已完成、什么被排除、final closeout
可以声明什么。

## 期望结果

- 从 reviewed evidence 产出 release-candidate summary。
- 保留未运行 runtime/API/frontend/live/external surfaces 的明确 exclusions。
- 确认没有 unresolved P1/P2 阻塞 final closeout。
- 将 bounded candidate handoff 给 `0.7.8`。

## 非目标

- 不标记 v0.7 final。
- 不运行新的 validation suites。
- 不修改 implementation files。
- 不隐藏 exclusions 或 unresolved findings。
