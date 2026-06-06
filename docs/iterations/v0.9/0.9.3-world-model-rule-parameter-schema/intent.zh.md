# Intent

英文镜像：`intent.md`。

## 问题

如果 generated worlds 的 parameters 和 rules 只是 prose 或 loose outline dictionaries，就无法
被验证为会演化的系统。`0.9.2` 刻意停在 public generated model candidate，并把完整
rule/parameter schema 延后到本包。

当前 runtime parameter path 也仍然很窄：`/world/params` 接受针对少量 registered parameters
的 patches，例如 `counter.increment`、`heartbeat.enabled` 和 `scene.weather`。v0.9 增加
generated-world rule/parameter contract 时，必须保持这条 path compatible。

## 目标

创建 reviewed contract、design 和 test plan，授权后可以 additive 实现：

- 用 ids、value types、bounds、visibility、provenance 和 public descriptions 表达 generated
  world parameters。
- 用 stable rule ids、trigger conditions、target parameter refs、allowed operations、effects、
  constraints 和 public evidence fields 表达 world evolution rules。
- 表达 validators 可检查、且不包含 hidden provider traces 的 constraints 和 boundaries。
- deterministic validate 和 summarize rule/parameter sets。
- 保持现有 `/world/params` behavior。

## 非目标

- 不跨 ticks 运行或评估 rules。
- 不证明 worldview fidelity。
- 不实现 event legality 或 rule-linked event generation。
- 不执行 live provider calls。
- 不持久化 generated worlds，也不把 generated rules 安装进 active runtime state。
- 不加入具体 game worlds、maps、characters、resources、locations 或 story rules。
- 不修改 Validation Client 或任何 external repository。
- 不修改 `backend/worldengine/`。
- 不实现 bounded runtime controls、Agent continuity、narrative projection、diagnostic dialogue、
  checker fixtures 或 full lifecycle validation。

## 为什么现在做

`0.9.4` 需要 fidelity checks，后续 packages 还需要 bounded runs、world direction、event
legality 和 rule-linked evolution evidence。它们都需要 deterministic public rule/parameter
schema，才能验证 generated behavior。

## North Star Alignment

本包强化 WorldEngine 作为 generic world generation and runtime engine 的方向。它为 generated
world parameters 和 rules 创建 public contracts，而不是把仓库收窄成具体 game、story、
validation world 或 product client。
