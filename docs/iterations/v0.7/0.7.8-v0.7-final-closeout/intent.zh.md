# Intent

## 问题

v0.7 campaign 已有 release-candidate bundle，但 parent version 尚未正式 closed。Final closeout
必须基于 current-session evidence 和 visible exclusions 做一个 bounded status decision。

## 期望结果

- 确认所有 v0.7 child packages 均 review complete。
- 重新运行 final in-scope checker 和 scope commands。
- 为未运行 product/runtime/external surfaces 记录 explicit exclusions。
- 如果没有 P1/P2 blocker，标记 v0.7 final。

## 非目标

- 不修复 implementation。
- 不运行 external suites。
- 不启动 v0.8。
- 不扩大 evidence claims。
