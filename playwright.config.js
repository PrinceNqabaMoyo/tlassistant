import { defineConfig, devices } from '@playwright/test';

/**
 * Playwright Configuration for Fundile TLAssistant Autonomous Autopilot Engine
 */
export default defineConfig({
  testDir: './e2e',
  timeout: 300000,
  expect: {
    timeout: 10000,
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
    baseURL: 'http://127.0.0.1:5173',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    launchOptions: {
      slowMo: process.env.SLOWMO ? parseInt(process.env.SLOWMO, 10) : 350,
    },
  },
  projects: [
    {
      name: 'desktop-chrome',
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1366, height: 768 },
      },
    },
    {
      name: 'mobile-pixel',
      use: {
        ...devices['Pixel 7'],
      },
    },
  ],
});
