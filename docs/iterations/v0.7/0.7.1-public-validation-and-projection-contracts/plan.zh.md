# Plan

## Files

Create:

- `docs/contracts/external-validation-readiness-contract.md`
- `docs/contracts/projection-consumer-contract.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/README.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/intent.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/contract.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/technical-design.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/test-plan.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/plan.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md`
- Chinese mirrors for package docs。

Modify after review:

- `docs/iterations/v0.7/` 下的 v0.7 parent status and route surfaces。

Do not touch:

- runtime、schema、API、frontend、backend test、checker implementation、fixture、migration、
  external repository、generated result 和 `backend/worldengine/` implementation files。

## Steps

1. Read v0.7 parent docs、`0.7.0` review、boundary docs、existing fixture runner contract、
   validation report template、testing playbooks 和 current implementation map。
2. Draft the `0.7.1` child package and Chinese mirrors。
3. Draft documentation-only public contract docs。
4. Run the documentation checks in `test-plan.md`。
5. Dispatch read-only documentation and mirror/scope evaluator review。
6. Fix P1/P2 findings or stop。
7. Update review evidence。
8. If review passes, mark `0.7.1` review complete and hand off to `0.7.2`。

## Stop Conditions

- Any implementation file changes appear。
- Contract docs require concrete external world details or private runner details。
- Readiness language implies product readiness、projection application readiness 或 external suite PASS
  without evidence。
- `0.7.2` authorization criteria are ambiguous。
- Required evaluator review reports P1 or unresolved P2。
