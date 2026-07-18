# Intent

英文版本：`intent.md`。

如果 rules 和 parameters 只是 prose 或 hidden model output，MVP world 就无法合法演化。
本包让 rule/parameter structure 对 session 可见，也能被 validator 读取。

目标不是应用 events。目标是让 session 能携带 validated public rule set，供后续 packages
在 accept、reject 和 apply events 时引用。
