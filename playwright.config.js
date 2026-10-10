import { defineConfig, devices } from '@playwright/test';

/**
 * Playwright Configuration for Fundile TLAssistant Autonomous Autopilot Engine
 */
export default defineConfig({
  testDir: './e2e',
  timeout: 3600000, // 1 hour per test set to allow full multi-subject journey
  expect: {
    timeout: 15000,
  },
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: 0,
  workers: 1, // Sequential execution for side-by-side multi-window coordination
  reporter: [
    ['list'],
    ['html', { outputFolder: 'playwright-report', open: 'never' }]
  ],
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL || 'https://caps-ai-math-assistant-app.web.app',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    launchOptions: {
      slowMo: process.env.SLOWMO ? parseInt(process.env.SLOWMO, 10) : 350,
    },
  },
  // Spin up local Vite dev server ONLY if explicitly targeting localhost
  ...(process.env.PLAYWRIGHT_BASE_URL && (process.env.PLAYWRIGHT_BASE_URL.includes('localhost') || process.env.PLAYWRIGHT_BASE_URL.includes('127.0.0.1'))
    ? {
        webServer: {
          command: 'npm run dev',
          url: 'http://127.0.0.1:5173',
          reuseExistingServer: true,
          timeout: 120000,
        },
      }
    : {}),
  projects: [
    {
      name: 'fundile-autopilot',
      use: {
        ...devices['Desktop Chrome'],
      },
    },
  ],
});
