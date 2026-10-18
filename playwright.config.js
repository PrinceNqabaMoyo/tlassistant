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
    baseURL: process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173',
    trace: 'on',
    screenshot: 'on',
    video: 'on',
    launchOptions: {
      slowMo: process.env.SLOWMO ? parseInt(process.env.SLOWMO, 10) : 350,
    },
  },
  // Spin up or reuse local Vite dev server on port 5173
  webServer: {
    command: process.platform === 'win32' ? 'npm.cmd run dev' : 'npm run dev',
    url: 'http://127.0.0.1:5173',
    reuseExistingServer: true,
    timeout: 120000,
  },
  projects: [
    {
      name: 'fundile-autopilot',
      use: {
        ...devices['Desktop Chrome'],
      },
    },
    {
      name: 'desktop-browser',
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1280, height: 800 },
      },
    },
    {
      name: 'desktop-pwa',
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1280, height: 800 },
        launchOptions: {
          args: ['--app=http://127.0.0.1:5173/?standalone=true', '--window-size=1280,850'],
        },
      },
    },
    {
      name: 'mobile-browser',
      use: {
        ...devices['Pixel 7'],
      },
    },
    {
      name: 'mobile-pwa',
      use: {
        ...devices['Pixel 7'],
        launchOptions: {
          args: ['--app=http://127.0.0.1:5173/?standalone=true', '--window-size=430,950'],
        },
      },
    },
  ],
});
