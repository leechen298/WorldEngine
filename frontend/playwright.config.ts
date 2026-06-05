import { defineConfig, devices } from "@playwright/test";

const apiBaseUrl = process.env.E2E_API_BASE_URL ?? "http://127.0.0.1:18000";
const appBaseUrl = process.env.E2E_APP_BASE_URL ?? "http://127.0.0.1:15173";
const apiUrl = new URL(apiBaseUrl);
const appUrl = new URL(appBaseUrl);
const apiHost = apiUrl.hostname;
const apiPort = apiUrl.port || (apiUrl.protocol === "https:" ? "443" : "80");
const appHost = appUrl.hostname;
const appPort = appUrl.port || (appUrl.protocol === "https:" ? "443" : "80");

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
        `CORS_ORIGINS=${appUrl.origin} WORLD_SUMMARY_INTERVAL_TICKS=2 WORLD_SNAPSHOT_INTERVAL_TICKS=2 .venv/bin/python -m uvicorn app.main:app --host ${apiHost} --port ${apiPort}`,
      cwd: "../backend",
      url: `${apiBaseUrl}/health`,
      reuseExistingServer: false,
      timeout: 120_000,
    },
    {
      command: `VITE_API_BASE_URL=${apiBaseUrl} pnpm dev --host ${appHost} --port ${appPort}`,
      cwd: ".",
      url: appBaseUrl,
      reuseExistingServer: false,
      timeout: 120_000,
    },
  ],
});
