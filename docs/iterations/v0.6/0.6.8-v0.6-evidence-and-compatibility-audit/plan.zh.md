# 计划

状态：review complete

## 执行计划

1. 读取 parent v0.6 status 和 child reviews through `0.6.7`。
2. 创建 0.6.8 audit package 和中文镜像。
3. 记录 evidence matrix、compatibility matrix、exclusions 和 finding classification。
4. 运行 documentation checks 和 scope guard。
5. 请求 documentation/evidence evaluator review。
6. 如果 evaluator PASS 且无 P1/P2，则标记 review complete。
7. 更新 parent status surfaces，交接给
   `0.6.9-v0.6-release-candidate-bundle`。

## Stop Conditions 停止条件

- 如果需要 implementation changes，则停止。
- 如果任何 evidence claim 无法追溯到当前 package review 或 current-session command
  result，则停止。
- 如果仍有 unresolved P1/P2 findings，则停止。
- 如果 audit wording 暗示 final release、product readiness、external validation readiness、
  projection readiness 或 generation quality，则停止。

## Handoff 交接

`0.6.9-v0.6-release-candidate-bundle` 接收 evidence matrix、compatibility matrix 和
unresolved finding classification。
