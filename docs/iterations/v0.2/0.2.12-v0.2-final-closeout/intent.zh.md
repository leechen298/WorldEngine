# Intent

英文版本：`intent.md`

## 问题

v0.2 已有 reviewed release-candidate bundle，但 final milestone status 不能随意声明。
Closeout step 需要一个小范围 package，确保 final decision 由 evidence 支撑，记录
reviewer acceptance，并保留 v0.2 foundation work 与未来 v0.3 implementation 之间的边界。

## 结果

Review approval 之后，本包应让 final v0.2 status 在 release 和 iteration documentation
中保持清晰，并记录：

- final review decision。
- 是否存在 P1/P2 blockers。
- open P3 findings 如何被 accepted 或 handoff。
- closeout session 中运行了哪些 commands。
- 未修改 runtime、schema、API、frontend、fixture、migration 或 test implementation files。

## 非目标

- 不实现 WorldSpec loader。
- 不把 RuntimeEngine 迁移到 WorldCell。
- 不实现 runtime bridge。
- 不实现 world generation、projection、agent loop、memory 或 pseudo-self continuity。
- 不增加 external fixture 或 validation repositories。
- 不增加 concrete external-world details。
- 不增加 tests，也不声明 implementation behavior，除非相关 command 明确作为 final
  documentation verification 在当前 session 中运行。

## 成功标准

- Package docs complete and ready for review。
- Final closeout acceptance requirements 可测试。
- Assumptions 和 open risks 明确。
- English 和 Chinese mirrors 同步。
- v0.2 milestone index 和 package README 将本包标记为 `ready for review`。
