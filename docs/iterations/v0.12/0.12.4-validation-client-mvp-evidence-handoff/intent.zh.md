# Intent

英文原文：`intent.md`。

## 问题

WorldEngine 现在可以暴露 public session runtime、rule-bound evolution、Agent state、Agent memory/consolidation 和 read-only inspection surfaces。外部 Validation Client 仍需要一个精确 public contract，说明要导出什么以及 checker 如何读取 evidence。

如果没有这个 contract，client 就必须从实现细节推断 artifact names、operation-log semantics、redaction requirements 和 Agent terminology。

## 用户价值

后续 Validation Client 任务可以不用猜 WorldEngine 行为，就实现 MVP evidence export，也不会把 external validation agents 和 in-world Agents 混在一起。

## 工程价值

本包建立 WorldEngine public evidence 和 external validation automation 之间的稳定边界。WorldEngine 仍是 public artifact semantics 的来源；external client 只是 consumer/exporter。

## 非目标

- 不写 Validation Client code。
- 不执行 provider。
- 不跑 autonomous validation。
- 不做 checker PASS/PARTIAL/BLOCKED/FAIL closeout。
- 除非后续 reviewed repair 明确授权 focused schema/checker support，否则不改 product code。
