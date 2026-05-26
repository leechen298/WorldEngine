# Intent

英文版本：`intent.md`

## 问题

v0.2 已经有 schema、event、boundary、evidence 和 compatibility review
artifacts，但它们分散在 package reviews、audit docs、release drafts 和
findings 中。Human / ChatGPT review 需要一个 release-candidate bundle，把
claims 映射到 evidence，同时不把 planned work 提升成 final release status。

## 目标

创建一个 ready for human / ChatGPT review 的 release-candidate evidence bundle，
并清楚说明：

- v0.2 完成了什么。
- v0.2 明确没有实现什么。
- 每个 release-candidate claim 由什么 evidence 支撑。
- 仍有哪些 findings 或 limitations。
- 为什么 final closeout 延后到 0.2.12。

## 非目标

- 不声明 v0.2 final release。
- 不关闭 0.2.12 work。
- 不实现或修改 runtime、schema、API、frontend、fixture、migration 或 test
  behavior。
- 不把 v0.3 loader、bridge、agent、memory、generation、projection 或 external
  validation work 放入 v0.2。
- 不增加 concrete external-world fixtures、seed data、roles、locations、
  resources、story rules、private validation internals 或 product UI。

## 为什么现在

0.2.9 已创建 evidence index 和 boundary audit。0.2.10 已明确 legacy 和
compatibility boundaries。下一个 milestone step 是在 final closeout 前组装
release-candidate bundle，让 reviewers 判断 v0.2 是否可以 finalize，或是否还需
更多 evidence。

## North Star 对齐

本包通过让 recursive-world foundation 可 review 来支持 north star，同时不把
WorldEngine 收窄成 concrete application backend。它保留 implemented v0.2
foundations 与未来 agent、memory、generation、projection 和 runtime bridge
milestones 之间的边界。
