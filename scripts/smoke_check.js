import { chromium } from 'playwright';

async function runSmokeCheck() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  
  // Abort external CDN requests to prevent network and parser stalls in headless tests
  await context.route(/.*(cdn\.jsdelivr\.net|unpkg\.com|fonts\.googleapis\.com|fonts\.gstatic\.com|cdn\.plot\.ly).*/, route => {
    route.abort();
  });

  const page = await context.newPage();
  page.on('console', msg => console.log('[BROWSER CONSOLE]', msg.type(), msg.text()));
  page.on('pageerror', err => console.error('[BROWSER ERROR]', err.message));
  page.on('response', res => {
    if (res.status() >= 400) console.log('[HTTP ERROR]', res.status(), res.url());
  });

  try {
    console.log('Navigating to http://127.0.0.1:5173...');
    await page.goto('http://127.0.0.1:5173', { waitUntil: 'commit', timeout: 30000 });
    console.log('DOM Content Loaded! Waiting for signup button to mount...');
    const signupBtn = page.locator('[data-testid="btn-landing-signup"]').first();
    await signupBtn.waitFor({ state: 'visible', timeout: 30000 });
    const text = await signupBtn.innerText();
    console.log(`[SMOKE CHECK PASSED] Landing page loaded cleanly. Sign up button text: "${text}"`);
    await browser.close();
    process.exit(0);
  } catch (err) {
    console.error('[SMOKE CHECK FAILED]:', err.message);
    const overlayText = await page.evaluate(() => {
      const el = document.querySelector('vite-error-overlay');
      return el ? (el.shadowRoot ? el.shadowRoot.textContent : el.textContent) : null;
    }).catch(() => null);
    if (overlayText) console.log('[VITE OVERLAY ERROR]:', overlayText);
    const bodyHtml = await page.evaluate(() => document.body ? document.body.innerHTML : 'No body').catch(() => 'Unable to read content');
    console.log('Current Body HTML (first 2000 chars):\n', bodyHtml.slice(0, 2000));
    await page.screenshot({ path: 'smoke_fail.png', fullPage: true }).catch(() => {});
    await browser.close();
    process.exit(1);
  }
}

runSmokeCheck();
