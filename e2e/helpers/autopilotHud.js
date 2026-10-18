import fs from 'fs';
import path from 'path';

const projectRoot = process.cwd();
const pauseBridgeFile = path.resolve(projectRoot, '.pause_signal.json');

/**
 * Visual Cursor & On-Demand Inspection Helpers for Playwright E2E Tests
 * - Renders a sleek in-browser cursor pointer to visually follow actions.
 * - Injects a non-intrusive [ ⏸️ Pause ] pill in the bottom-left corner.
 * - Allows pausing on-demand via browser click OR PowerShell terminal ('p' + Enter).
 * - Default execution: 100% continuous auto-run without mandatory gating.
 */

export async function injectGlidingCursorAndHud(page) {
  try {
    await page.evaluate(() => {
      if (document.getElementById('virtual-cursor')) return;

      // Inject cursor & HUD styles
      const style = document.createElement('style');
      style.id = 'autopilot-hud-styles';
      style.innerHTML = `
        #virtual-cursor {
          position: fixed;
          pointer-events: none;
          z-index: 2147483647;
          width: 26px;
          height: 26px;
          font-size: 20px;
          top: 0;
          left: 0;
          transform: translate(20px, 20px);
          transition: transform 0.25s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.15s;
          filter: drop-shadow(0 2px 4px rgba(0,0,0,0.35));
          user-select: none;
        }
        #virtual-cursor.clicking {
          transform: scale(0.85);
          filter: drop-shadow(0 1px 2px rgba(0,0,0,0.5));
        }
        #fundile-pause-pill {
          position: fixed;
          bottom: 16px;
          left: 16px;
          z-index: 2147483640;
          padding: 6px 14px;
          border-radius: 9999px;
          font-family: system-ui, -apple-system, sans-serif;
          font-size: 11px;
          font-weight: 700;
          cursor: pointer;
          border: 1px solid rgba(0,0,0,0.15);
          background: rgba(15, 23, 42, 0.85);
          color: #ffffff;
          backdrop-filter: blur(8px);
          box-shadow: 0 4px 12px rgba(0,0,0,0.18);
          transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
          user-select: none;
          display: flex;
          align-items: center;
          gap: 6px;
        }
        #fundile-pause-pill:hover {
          transform: translateY(-1px);
          background: rgba(15, 23, 42, 0.95);
        }
        #fundile-pause-pill.is-paused {
          background: #d97706 !important;
          border-color: #f59e0b !important;
          box-shadow: 0 0 16px rgba(245, 158, 11, 0.6) !important;
          animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
          0%, 100% { opacity: 1; transform: scale(1); }
          50% { opacity: 0.88; transform: scale(1.02); }
        }
      `;
      document.head.appendChild(style);

      // Inject Virtual Cursor element
      const cursor = document.createElement('div');
      cursor.id = 'virtual-cursor';
      cursor.innerText = '🖱️';
      document.body.appendChild(cursor);

      // Inject On-Demand Pause/Resume Pill (Rule 0d-7: non-interactive margins bottom: 16px; left: 16px)
      if (!document.getElementById('fundile-pause-pill')) {
        const pill = document.createElement('button');
        pill.id = 'fundile-pause-pill';
        pill.type = 'button';
        pill.innerText = '⏸️ Pause Autopilot';
        pill.title = 'Click to pause autopilot and inspect this view. Click again to resume.';
        pill.addEventListener('click', (e) => {
          e.stopPropagation();
          window.__FUNDILE_PAUSED__ = !window.__FUNDILE_PAUSED__;
          if (window.__FUNDILE_PAUSED__) {
            pill.innerText = '▶️ Resume Autopilot';
            pill.classList.add('is-paused');
          } else {
            pill.innerText = '⏸️ Pause Autopilot';
            pill.classList.remove('is-paused');
          }
        });
        document.body.appendChild(pill);
      }
    });
  } catch (e) {}
}

export async function waitIfPaused(page) {
  if (!page || page.isClosed()) return;

  let isPaused = false;
  try {
    isPaused = await page.evaluate(() => Boolean(window.__FUNDILE_PAUSED__)).catch(() => false);
  } catch {}

  if (!isPaused && fs.existsSync(pauseBridgeFile)) {
    try {
      const data = JSON.parse(fs.readFileSync(pauseBridgeFile, 'utf8') || '{}');
      isPaused = data.status === 'pause';
    } catch {}
  }

  if (!isPaused) return;

  console.log('\n================================================================================');
  console.log('⏸️  [PAUSED BY USER]');
  console.log('   The test is paused for inspection.');
  console.log('   👉 Click [▶️ Resume Autopilot] in the browser (or press Enter in PowerShell) to resume...');
  console.log('================================================================================\n');

  // Update browser pill to show active pause state
  await page.evaluate(() => {
    window.__FUNDILE_PAUSED__ = true;
    const pill = document.getElementById('fundile-pause-pill');
    if (pill) {
      pill.innerText = '▶️ Resume Autopilot';
      pill.classList.add('is-paused');
    }
  }).catch(() => {});

  while (isPaused) {
    await page.waitForTimeout(200);
    if (page.isClosed()) break;
    try {
      const browserPaused = await page.evaluate(() => Boolean(window.__FUNDILE_PAUSED__)).catch(() => false);
      let filePaused = false;
      if (fs.existsSync(pauseBridgeFile)) {
        const data = JSON.parse(fs.readFileSync(pauseBridgeFile, 'utf8') || '{}');
        filePaused = data.status === 'pause';
      }
      isPaused = browserPaused || filePaused;
    } catch {
      break;
    }
  }

  // Restore browser pill
  await page.evaluate(() => {
    window.__FUNDILE_PAUSED__ = false;
    const pill = document.getElementById('fundile-pause-pill');
    if (pill) {
      pill.innerText = '⏸️ Pause Autopilot';
      pill.classList.remove('is-paused');
    }
  }).catch(() => {});

  try {
    if (fs.existsSync(pauseBridgeFile)) fs.unlinkSync(pauseBridgeFile);
  } catch {}

  console.log('▶️ [RESUMED] Advancing to next action...\n');
}

export async function updateHud(page, persona, message) {
  if (persona && message) {
    console.log(`   [${persona}] ${message}`);
  }
}

export async function glideCursorTo(page, selector) {
  try {
    const loc = typeof selector === 'string' ? page.locator(selector).first() : selector;
    const box = await loc.boundingBox();
    if (box) {
      const x = Math.round(box.x + box.width / 2);
      const y = Math.round(box.y + box.height / 2);
      await page.evaluate(({ x, y }) => {
        const cursor = document.getElementById('virtual-cursor');
        if (cursor) {
          cursor.style.transform = `translate(${x}px, ${y}px)`;
        }
      }, { x, y });
      await page.mouse.move(x, y, { steps: 3 });
    }
  } catch (e) {}
}

export async function glideAndClick(page, selector, { persona = 'AUTOPILOT', message = '' } = {}) {
  await waitIfPaused(page);

  if (message) {
    await updateHud(page, persona, message);
  }
  const loc = typeof selector === 'string' ? page.locator(selector).first() : selector;
  await loc.waitFor({ state: 'visible', timeout: 15000 });
  await glideCursorTo(page, loc);
  await page.waitForTimeout(100);

  // Click visual animation
  await page.evaluate(() => {
    const cursor = document.getElementById('virtual-cursor');
    if (cursor) cursor.classList.add('clicking');
  }).catch(() => {});

  await loc.click();
  await page.waitForTimeout(100);

  await page.evaluate(() => {
    const cursor = document.getElementById('virtual-cursor');
    if (cursor) cursor.classList.remove('clicking');
  }).catch(() => {});
}

export async function typeRealistic(page, selector, text, { delayMs = 30, persona, message } = {}) {
  await waitIfPaused(page);

  if (message) {
    await updateHud(page, persona || 'AUTOPILOT', message);
  }
  const loc = typeof selector === 'string' ? page.locator(selector).first() : selector;
  await loc.waitFor({ state: 'visible', timeout: 15000 });
  await glideCursorTo(page, loc);
  await loc.click();
  await loc.fill('');

  for (const char of text) {
    await waitIfPaused(page);
    await page.keyboard.type(char, { delay: delayMs });
  }
  await page.waitForTimeout(100);
}

export async function simulateStudyBreak(page, countdownSeconds = 10, simulatedMins = 20) {
  console.log(`\n☕ [STUDY BREAK] Simulating ${simulatedMins}-minute study break (${countdownSeconds}s on-screen timer)...`);
  for (let rem = countdownSeconds; rem > 0; rem--) {
    await waitIfPaused(page);
    await updateHud(
      page,
      '☕ STUDY BREAK',
      `Resting cognitive load (${simulatedMins}m simulated) • ${rem}s remaining...`
    );
    await page.waitForTimeout(1000);
  }
  await updateHud(page, '⚡ BREAK COMPLETE', 'Refreshed and ready for Subject 2!');
  await page.waitForTimeout(1000);
}
