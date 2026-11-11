import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  console.log('Navigating to harness URL...');
  await page.goto('http://localhost:5173/?harness=universal_workspace', { waitUntil: 'domcontentloaded' });
  const el = await page.waitForSelector('[data-testid="universal-workspace-harness-ready"]', { timeout: 10000 });
  console.log('Harness mounted successfully! Found:', !!el);
  await browser.close();
})().catch(err => {
  console.error('Test error:', err.message);
  process.exit(1);
});
