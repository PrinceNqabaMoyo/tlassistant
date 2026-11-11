import { chromium } from 'playwright';

async function testLocalhost() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  console.log('Navigating to http://localhost:5173...');
  const t0 = Date.now();
  await page.goto('http://localhost:5173', { waitUntil: 'commit', timeout: 15000 });
  console.log('Commit reached in', Date.now() - t0, 'ms');
  await page.waitForLoadState('domcontentloaded', { timeout: 15000 });
  console.log('DOMContentLoaded reached in', Date.now() - t0, 'ms');
  const title = await page.title();
  console.log('Page title:', title);
  await browser.close();
}

testLocalhost().catch(console.error);
