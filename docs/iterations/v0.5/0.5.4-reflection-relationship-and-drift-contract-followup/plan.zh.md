# 计划

状态：review complete

## 步骤

1. 读取 governing v0.5 docs 和 prior concept contracts。
2. 创建完整 package docs 和中文镜像。
3. 为 relationship state、self-summary、reflection records 和 personality drift
   signals 定义 refined semantics。
4. 明确 deferred implementation，并记录 future authorization criteria。
5. 运行 documentation verification commands。
6. 运行只读 documentation/contract evaluator。
7. 如果 evaluator 通过，将 package 标记为 review complete，并交接给
   `0.5.5-v0.5-evidence-and-compatibility-audit`。

## 停止条件

- 缺少 required docs 或 mirrors 时停止。
- 发现 code/runtime/frontend/migration/file-scope drift 时停止。
- 有 P1 或 unresolved blocking P2 evaluator findings 时停止。
- 如果 proposed change 试图在没有 reviewed contract update 和 implementation
  authorization 的情况下把 package 改成 mixed/code，则停止。

## 交接条件

- Package docs 和 mirrors 存在。
- Documentation checks 通过。
- Documentation/contract evaluator 通过。
- Review 记录 changed files、commands、skipped tests、compatibility review、scope
  review、evaluator evidence 和 unresolved findings。
- Closeout 后 parent v0.5 status surfaces 指向 `0.5.5`。
