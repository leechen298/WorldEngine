import { expect, test } from "@playwright/test";

test("minimum runnable anchor drives the real Engine V1 full flow", async ({ page }) => {
  await page.goto("/admin/runnable-anchor");

  await expect(page.getByRole("heading", { name: "可运行锚点工作台" })).toBeVisible();
  await expect(page.getByTestId("capabilities-ready")).toContainText("engine-v1-mvp");
  await expect(page.getByTestId("operation-count")).toHaveText("14");

  await page.getByTestId("generate-package").click();
  await expect(page.getByTestId("package-readiness")).toHaveText("ready");
  await expect(page.getByTestId("package-hash")).toHaveText(/^[a-f0-9]{64}$/);
  await expect(page.getByTestId("determinism-status")).toContainText("2/2 hash 一致");

  await page.getByTestId("boot-session").click();
  await expect(page.getByTestId("session-id")).toHaveText(/^session-/);
  await expect(page.getByTestId("projection-tick")).toHaveText("0");
  await expect(page.getByTestId("projection-revision")).toHaveText("0");
  await expect(page.getByTestId("projection-state-hash")).toHaveText(/^[a-f0-9]{64}$/);

  const windowId = await page.getByTestId("active-window-id").innerText();
  await page.getByTestId("submit-direction-pair").click();
  await expect(page.getByTestId("accepted-direction-result")).toContainText("accepted");
  await expect(page.getByTestId("accepted-direction-result")).toContainText(windowId);
  await expect(page.getByTestId("rejected-direction-result")).toContainText("rejected");
  await expect(page.getByTestId("rejected-direction-result")).toContainText(
    "direct_final_fact_forbidden",
  );
  await expect(page.getByTestId("rejected-direction-result")).toContainText(windowId);

  await page.getByTestId("step-count").fill("2");
  await page.getByTestId("step-session").click();
  await expect(page.getByTestId("step-range")).toHaveText("0 → 2");
  await expect(page.getByTestId("projection-tick")).toHaveText("2");
  await expect(page.getByTestId("agent-cycle-count")).toHaveText("2");
  await expect(page.getByTestId("agent-decision-mode")).toHaveText(
    "experience_guided_policy",
  );
  await expect(page.getByTestId("agent-experience-count")).toHaveText("2");
  await expect(page.getByTestId("evidence-status")).toHaveText("complete");

  const revisionAfterStep = Number(await page.getByTestId("projection-revision").innerText());
  await page.getByTestId("submit-action").click();
  await expect(page.getByTestId("action-result")).toContainText("accepted");
  await expect(page.getByTestId("action-result")).toContainText("action_rule_accepted");
  await expect
    .poll(async () => Number(await page.getByTestId("projection-revision").innerText()))
    .toBeGreaterThan(revisionAfterStep);

  await page.getByTestId("submit-feedback").click();
  await expect(page.getByTestId("feedback-result")).toContainText("accepted");
  await expect(page.getByTestId("feedback-result")).toContainText("feedback_accepted");
  await expect(page.getByTestId("projection-feedback-count")).toHaveText("1");
  await expect(page.getByTestId("evidence-status")).toHaveText("complete");

  await expect(page.getByTestId("event-count")).not.toHaveText("0");
  await expect(page.getByTestId("diff-count")).not.toHaveText("0");
  await expect(page.getByTestId("snapshot-count")).not.toHaveText("0");
  await expect(page.getByTestId("direction-count")).toHaveText("2");

  await page.getByRole("tab", { name: /^Agent/ }).click();
  await expect(page.getByTestId("agent-causal-chain")).toContainText(
    "experience_guided_policy",
  );
  await expect(page.getByTestId("agent-causal-chain")).toContainText("ActionRequest");
  await expect(page.getByTestId("agent-causal-chain")).toContainText("action_id");

  await page.getByRole("tab", { name: /^方向/ }).click();
  await expect(page.getByTestId("direction-table")).toContainText(
    "direct_final_fact_forbidden",
  );

  await page.getByRole("tab", { name: /^Diff/ }).click();
  await expect(page.getByTestId("diff-list")).toContainText("/revision");
  await page.getByRole("tab", { name: /^Snapshot/ }).click();
  await expect(page.getByTestId("snapshot-list")).toContainText("snapshot-");

  const downloadPromise = page.waitForEvent("download");
  await page.getByTestId("download-evidence").click();
  const download = await downloadPromise;
  await expect(download.suggestedFilename()).toMatch(/^session-.*-evidence\.json$/);
});
