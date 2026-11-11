import { chromium } from 'playwright';
import { spawn } from 'child_process';
import http from 'http';

function checkPort(port) {
  return new Promise((resolve) => {
    const req = http.get(`http://127.0.0.1:${port}/`, (res) => {
      resolve(res.statusCode === 200);
    });
    req.on('error', () => resolve(false));
    req.setTimeout(4000, () => { req.destroy(); resolve(false); });
  });
}

async function runSmokeCheck() {
  let serverProcess = null;
  const isRunning = await checkPort(5173);

  if (!isRunning) {
    console.log('[SMOKE CHECK] Starting vite preview on 127.0.0.1:5173...');
    serverProcess = spawn('npx.cmd', ['vite', 'preview', '--port', '5173', '--host', '127.0.0.1'], {
      shell: true,
      stdio: 'ignore'
    });
    // Wait for server to bind
    for (let i = 0; i < 20; i++) {
      await new Promise(r => setTimeout(r, 1000));
      if (await checkPort(5173)) break;
    }
  }

  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'] });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });

  const page = await context.newPage();
  page.on('console', msg => {
    if (msg.type() === 'error') console.log(`[CONSOLE ERROR]:`, msg.text());
  });
  page.on('pageerror', err => console.error('[PAGE ERROR]:', err.stack || err.message));

  try {
    console.log('Navigating to http://127.0.0.1:5173...');
    await page.goto('http://127.0.0.1:5173', { waitUntil: 'domcontentloaded', timeout: 30000 });
    console.log('Page loaded! Waiting for body to mount...');
    await page.waitForSelector('#root', { state: 'attached', timeout: 15000 });
    const title = await page.title();
    console.log(`[SMOKE CHECK PASSED] Landing page loaded cleanly. Title: "${title}"`);
    await browser.close();
    if (serverProcess) {
      serverProcess.kill('SIGTERM');
    }
    process.exit(0);
  } catch (err) {
    console.error('[SMOKE CHECK FAILED]:', err.message);
    const bodyHtml = await page.evaluate(() => document.body ? document.body.innerHTML : 'No body').catch(() => 'Unable to read content');
    console.log('Current Body HTML (first 1000 chars):\n', bodyHtml.slice(0, 1000));
    await browser.close();
    if (serverProcess) {
      serverProcess.kill('SIGTERM');
    }
    process.exit(1);
  }
}

runSmokeCheck();
