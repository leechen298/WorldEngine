# Intent

英文镜像：`intent.md`。

## Why This Package Exists

v0.9 已实现并文档化多个 LLM-backed foundation slices，但不能诚实声明 full LLM-backed
lifecycle PASS。0.9.12 在任何 live provider call 之前把最终 validation run 分类为
BLOCKED。

本 package 用来防止状态漂移：记录 release-candidate boundary，明确 unresolved blockers，
并给后续工作一个精确 post-closeout route。

## Intended Outcome

- v0.9 parent docs 反映最终 BLOCKED closeout state。
- 0.9.12 durable result summary 作为权威 evidence 被引用。
- 不扩大 implementation、provider、Validation Client 或 external validation claim。
- 后续工作可以选择更窄的 provider/runner repair package 或 v1.0 planning，而不会误读
  v0.9 为 product-ready。
