import { defineConfig, devices } from "@playwright/test";

const apiBaseUrl = process.env.E2E_API_BASE_URL ?? "http://127.0.0.1:8000";
const appBaseUrl = process.env.E2E_APP_BASE_URL ?? "http://127.0.0.1:5173";

export default defineConfig({
  testDir: "./e2e",
  outputDir: "../test-results/e2e/artifacts",
  fullyParallel: false,
  workers: 1,
  reporter: [
    ["list"],
    ["html", { outputFolder: "../test-results/e2e/html-report", open: "never" }],
  ],
  use: {
    ...devices["Desktop Chrome"],
    baseURL: appBaseUrl,
    testIdAttribute: "data-test",
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
  },
  webServer: [
    {
      command:
        "WORLD_SUMMARY_INTERVAL_TICKS=2 WORLD_SNAPSHOT_INTERVAL_TICKS=2 .venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000",
      cwd: "../backend",
      url: `${apiBaseUrl}/health`,
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
    },
    {
      command: `VITE_API_BASE_URL=${apiBaseUrl} pnpm dev --host 127.0.0.1`,
      cwd: ".",
      url: appBaseUrl,
      reuseExistingServer: !process.env.CI,
      timeout: 120_000,
    },
  ],
});
