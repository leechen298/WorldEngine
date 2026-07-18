# WorldEngine 可运行 MVP

状态：`开发中`

本文件是当前唯一执行契约。旧版本规划保留为历史资料，但不决定当前工作顺序或完成状态。

## 一句话目标

用一个外部 Godot 客户端证明：WorldEngine 可以生成一个世界、持续推进权威历史、让 Agent
根据公开状态作出决定、接受有边界的用户干预，并把结果通过通用接口反馈给任意客户端。

## 产品分工

### WorldEngine

- 定义世界初始设定、规则、Agent 和公开状态。
- 维护 tick、世界时间、事件、diff、snapshot 和状态哈希。
- 运行 Agent 的感知、决策、规则判断、行动和公开经验引用。
- 判断用户方向、客户端动作和反馈是否合法。
- 通过公开 HTTP/OpenAPI 发布投影与证据。

### 游戏引擎或其他客户端

- 负责画面、动画、输入、碰撞和精细物理。
- 大部分时间在本地流畅运行。
- 发生重要事件时立即同步，其他时候按固定频率拉取投影和事件。
- 把需要进入权威历史的动作或结果反馈给 WorldEngine。

### 独立 checker

- 读取客户端保存的原始 HTTP 证据和 WorldEngine evidence bundle。
- 独立检查哈希、tick、revision、事件因果和场景断言。
- 独占最终 PASS/FAIL 判定；Godot 执行器不能写 verdict。

## MVP 固定场景

具体地图、美术和角色只存在于外部验证仓库。场景包含一个位置、一个 Agent 和一个整数状态
变量 `world_signal`。Godot 用像素风画面显示位置、Agent、信号装置、tick 和最近事件。

完整流程：

1. Godot 调用 `/api/v1/capabilities`，按 `operation_id` 发现接口。
2. Godot 提交世界 brief，WorldEngine 生成 deterministic runnable package。
3. Godot 用 package id/hash 创建 Session，显示初始公开投影。
4. Godot 推进至少两个 tick；Agent 每个 tick 产生可观察的决策与行动证据。
5. 用户在开放窗口提交 `bounded_pressure`，它先排队，在后续 tick 按规则生效。
6. 用户尝试 `direct_final_fact`，WorldEngine 必须拒绝且不能产生状态 diff。
7. Godot 提交一个合法客户端 action 和一条 typed feedback。
8. Godot 轮询增量事件、刷新权威投影并保存画面与原始响应。
9. 独立 checker 重新读取 evidence bundle，检查所有断言并生成最终 verdict。

## 完成条件

- [x] WorldEngine 发布稳定的 Engine V1 capability manifest。
- [x] 世界 brief 可以生成 ready package，并具有稳定 package hash。
- [x] Session 可以启动并精确推进 tick。
- [x] Agent 决策、行动、经验引用、事件和 diff 可以形成公开因果链。
- [x] 有边界方向可排队并在后续 tick 生效；直接指定最终事实会被拒绝。
- [x] 客户端 action、typed feedback、event polling 和 evidence export 可用。
- [x] 项目后台可以手工操作并观察上述 WorldEngine 能力。
- [ ] 外部 Godot 客户端真实连接公开 API，并显示可运行像素世界。
- [ ] Godot 保存完整原始执行证据，但不能写最终 verdict。
- [ ] 独立 checker 对正常场景给出 PASS。
- [ ] 篡改哈希、缺失证据、重复 run id、跨 Session 证据或预写 verdict 均被 checker 拒绝。
- [ ] 完整后端、前端、HTTP、Godot headless、视觉和 checker 验证全部通过。

## 当前允许的简化

- 后端可以使用进程内存储；重启后不保留 Session。
- 世界可以只有一个位置、一个 Agent 和少量整数状态变量。
- Agent 可以先使用 deterministic policy，但必须真实读取状态、生成决定、经过规则判断并留下
  因果证据，不能由客户端伪造结果。
- Godot 使用简单像素素材即可，不要求完整游戏内容。
- 当前不要求 live LLM provider、复杂物理、多人联网或大型世界。

## 不可妥协的边界

- WorldEngine 不依赖 Godot，也不包含 Godot 项目代码或具体场景数据。
- Godot 不读取 WorldEngine 私有代码、数据库或内存。
- 每个被接受的权威状态变化都必须关联 event 和 diff。
- 公开证据不得包含密钥、provider 原始内容、私有记忆或思维链。
- executor 和 checker 必须是独立实现边界，不能共享 verdict 逻辑。

## 当前事实基线

- Engine V1 聚焦后端测试：`24 passed`。
- 前端单元测试：`50 passed`。
- 前端生产构建：通过，有一个现存 large-chunk warning。
- 完整后端回归：`485 passed`。
- WorldEngine-side HTTP smoke：`WORLDENGINE_MVP_ANCHOR_PASS`，11 项检查全部通过；它仍不能
  替代外部 Godot/checker 证明。

## 工作方式

直接围绕未完成条件实现。设计变化写回本文件；代码、测试和证据可以在同一开发周期内演进。
只有边界变化、数据破坏风险或完成声明才需要单独审查，不再为每个小步骤建立版本包。
