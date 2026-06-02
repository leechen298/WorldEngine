# Technical Design

## Primary Artifact

`release-candidate-summary.md` 是 release-candidate bundle。它不得被命名或视作 final release notes。

## Sections

- status and claim boundary。
- completed child packages。
- evidence map。
- exclusions。
- unresolved findings。
- recommendation to final closeout。

## Consistency Checks

用 file-existence checks 验证所有 child reviews、`0.7.5` evidence matrix 和 `0.7.6`
audit report。

用 scope guard 确认没有 reviewed v0.7 surface 之外的 implementation files changed。

用 status searches 确认本 package 没有标记 v0.7 final。

## Compatibility Rule

Release-candidate approval 表示 final closeout package 可以在自己的 checks 通过后 review and mark
final。它本身不是 final approval。
