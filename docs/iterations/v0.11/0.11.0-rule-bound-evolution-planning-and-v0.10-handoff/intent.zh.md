# Intent

英文版本：`intent.md`。

v0.11 依赖 v0.10 的 runnable-session 纵向链路。本包在任何 rule-bound world
evolution implementation 开始前，把这个依赖写清楚。

本包的目标很窄：

- 把 v0.10 closeout evidence 记录为 v0.11 输入。
- v0.10 的 caveats 仍是 caveats，不被包装成隐藏 PASS。
- v0.11 route 只推进到 `0.11.1` documentation package creation。
- 本包不打开 implementation scope。

这样可以避免 v0.11 绕过 session/runtime/evidence contract，也避免把 v0.10 的 provider
或 external-validation 缺口误写成已解决。
