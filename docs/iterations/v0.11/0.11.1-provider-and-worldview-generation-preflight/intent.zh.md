# Intent

英文版本：`intent.md`。

v0.11 的 rule-bound evolution 需要先知道 world 是如何生成的，或者将如何生成。Rules
和 events 依赖 worldview data 之前，clients 需要一个公开的 preflight answer：

- Provider 是否已配置？
- 由于本包不授权 live call，live provider execution 是否会被 blocked？
- 当前是否使用 safe mock？
- 当前是否使用 deterministic fallback？
- 能否在不泄漏 private input 或 provider details 的情况下分类 worldview request？

本包把这些答案做成 public API 和 manifest surface，但不声明 provider-backed quality，
也不运行 live provider calls。
