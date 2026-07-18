# 意图

英文源文件：`intent.md`。

## 问题

WorldEngine 已经积累了很多看起来像框架的能力和历史 MVP 结论，但项目仍然缺少一场当前、可被
独立验证的运行，来证明世界生成、世界运行、Agent 运行、用户干预、投影和证据属于同一条正典
历史。

如果从当前实现反推设计，很容易保留错误边界。本 package 从已经确认的活世界流程出发，先固定
contract；当前代码只在之后作为可选实现资产清单使用。

## 目标

创建 v0.13 最小完整锚点的 WorldEngine 侧部分：

```text
结构化世界简述 + seed
-> 确定性可运行世界包 + hash
-> 从该准确 hash 启动 Session
-> 精确 lockstep steps
-> Agent 因果循环
-> accepted/rejected intervention judgment
-> event/diff/snapshot/projection/evidence
-> 通过同一组 API 操作的管理控制台
```

## 为什么现在做

在增加世界质量、Agent 深度或游戏引擎表现之前，项目需要稳定验收目标。确定性路径可以消除 live
provider、网络和外部客户端阻断，同时保留后续 Godot 运行必须经过的每个核心节点。

## 与 Roadmap 的关系

v0.13 在历史 v0.10-v0.12 `PARTIAL` 路线之后建立新的锚点 contract。它不会重开这些版本，
也不会把历史证据当作当前证明。它会产出供外部 `0.13.1` Godot/checker package 消费的稳定
公共 surface。

## 非目标

- 不依赖 live LLM 生成或 Agent 决策。
- 本仓库不存放具体外部场景。
- 不创建 Godot project，也不修改外部仓库。
- 不做逐帧同步，不要求 WebSocket。
- 不做生产持久化、恢复执行、分支或部署。
- 不做多 Agent 社会、递归世界、完整记忆巩固、人格漂移、叙事投影或诊断对话。
- 不声明 polished application 或游戏发行完成。

## 预期交接

发布稳定 manifest、schemas、API examples 和 evidence-bundle contract，让外部 Godot
executor 和独立 checker 无需读取 WorldEngine 代码或 storage 就能消费。
