import { expect, test } from "@playwright/test";

test("dashboard-generation-preview submits a generic preview and readiness check", async ({ page }) => {
  await page.goto("/");

  await expect(page.getByTestId("generation-panel")).toBeVisible();
  await page.getByTestId("generation-request-id-input").fill("e2e-generation-preview");
  await page.getByTestId("generation-root-id-input").fill("e2e-root");
  await page.getByTestId("generation-root-label-input").fill("E2E Root");
  await page.getByTestId("generation-child-id-input").fill("e2e-child");
  await page.getByTestId("generation-child-label-input").fill("E2E Child");
  await page.getByTestId("generation-seed-input").fill("e2e-seed");

  await page.getByTestId("generation-preview-submit").click();

  await expect(page.getByTestId("generation-validation-status")).toHaveText("passed");
  await expect(page.getByTestId("generation-id")).toContainText("generation-");
  await expect(page.getByTestId("generation-summary")).toContainText("total_cell_count");
  await expect(page.getByTestId("generation-readiness-status")).toHaveText("passed");
});
