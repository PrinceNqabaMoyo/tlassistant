import fs from 'fs';
import path from 'path';

const projectRoot = process.cwd();
const pauseBridgeFile = path.resolve(projectRoot, '.pause_signal.json');

/**
 * Authoritative Node.js state for Autopilot Pause / Resume
 * - Decoupled, idempotent state machine (doPause / doResume).
 * - Refractory cooldown prevents bounce / double-click re-pausing.
 */
let isAutopilotPaused = false;
let pauseWaiters = [];
let lastResumeTime = 0;

export function doPause() {
  const now = Date.now();
  // Don't allow re-pausing within 1200ms of resuming
  if (now - lastResumeTime < 1200) {
    console.log('[AUTOPILOT] Pause request ignored: Cooldown active after recent resume.');
    return;
  }
  if (isAutopilotPaused) return; // Already paused (idempotent)
  isAutopilotPaused = true;
  console.log('\n================================================================================');
  console.log('⏸️  [AUTOPILOT CONTROLLER] State: PAUSED FOR INSPECTION');
  console.log('   👉 To resume: Click [▶️ RESUME AUTOPILOT] in browser, or press Spacebar / R');
  console.log('================================================================================\n');
}

export function doResume() {
  if (!isAutopilotPaused) return; // Already running (idempotent)
  lastResumeTime = Date.now();
  isAutopilotPaused = false;
  console.log('\n▶️  [AUTOPILOT CONTROLLER] State: RESUMED! Advancing test...\n');
  const waiters = pauseWaiters;
  pauseWaiters = [];
  waiters.forEach((resolve) => resolve());
}

/**
 * Register Node-to-Browser bridge functions once per page
 */
export async function setupAutopilotBridge(page) {
  if (!page || page.isClosed()) return;

  if (!page.__autopilotBridgeInstalled) {
    page.__autopilotBridgeInstalled = true;

    try {
      // Idempotent Explicit Pause
      await page.exposeFunction('__FUNDILE_NODE_PAUSE__', () => {
        doPause();
        return isAutopilotPaused;
      });

      // Idempotent Explicit Resume
      await page.exposeFunction('__FUNDILE_NODE_RESUME__', () => {
        doResume();
        return isAutopilotPaused;
      });

      // Toggle
      await page.exposeFunction('__FUNDILE_NODE_TOGGLE_PAUSE__', () => {
        if (isAutopilotPaused) {
          doResume();
        } else {
          doPause();
        }
        return isAutopilotPaused;
      });

      await page.exposeFunction('__FUNDILE_NODE_IS_PAUSED__', () => {
        return isAutopilotPaused;
      });
    } catch (e) {
      // Already registered in multi-call context
    }
  }
}

/**
 * Visual Cursor & On-Demand Inspection Helpers for Playwright E2E Tests
 * - Renders virtual cursor pointer to follow actions.
 * - Injects floating [ ⏸️ PAUSE AUTOPILOT ] pill strictly at bottom: 16px; left: 16px (Rule 0d-7).
 * - Cooldown protection: Clicking resume locks out re-pause for 1.5 seconds.
 */
export async function injectGlidingCursorAndHud(page) {
  if (!page || page.isClosed()) return;

  await setupAutopilotBridge(page);

  try {
    await page.evaluate(() => {
      // 1. Inject Styles
      if (!document.getElementById('autopilot-hud-styles')) {
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
            position: fixed !important;
            bottom: 16px !important;
            left: 16px !important;
            z-index: 2147483647 !important;
            padding: 10px 20px !important;
            border-radius: 9999px !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
            font-size: 13px !important;
            font-weight: 700 !important;
            cursor: pointer !important;
            border: 2px solid #ef4444 !important;
            background: #0f172a !important;
            color: #ffffff !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4) !important;
            user-select: none !important;
            display: flex !important;
            align-items: center !important;
            gap: 8px !important;
            transition: transform 0.15s ease, background 0.2s ease, box-shadow 0.2s ease !important;
            outline: none !important;
          }
          #fundile-pause-pill:hover {
            transform: translateY(-2px) scale(1.02) !important;
          }
          #fundile-pause-pill:active {
            transform: translateY(0) scale(0.98) !important;
          }
          #fundile-pause-pill.is-paused {
            background: #16a34a !important;
            border-color: #ffffff !important;
            box-shadow: 0 0 25px rgba(22, 163, 74, 0.9) !important;
            animation: fundile-pulse 1.5s infinite !important;
          }
          #fundile-pause-pill.is-resuming {
            background: #0284c7 !important;
            border-color: #38bdf8 !important;
            box-shadow: 0 0 20px rgba(2, 132, 199, 0.7) !important;
            pointer-events: none !important;
            cursor: wait !important;
          }
          @keyframes fundile-pulse {
            0% { transform: scale(1); box-shadow: 0 0 15px rgba(22, 163, 74, 0.7); }
            50% { transform: scale(1.04); box-shadow: 0 0 30px rgba(22, 163, 74, 1); }
            100% { transform: scale(1); box-shadow: 0 0 15px rgba(22, 163, 74, 0.7); }
          }
        `;
        document.head.appendChild(style);
      }

      // 2. Inject Virtual Cursor
      if (!document.getElementById('virtual-cursor')) {
        const cursor = document.createElement('div');
        cursor.id = 'virtual-cursor';
        cursor.innerText = '🖱️';
        document.body.appendChild(cursor);
      }

      // 3. Inject Floating Pause Pill with Cooldown Protection
      let pill = document.getElementById('fundile-pause-pill');
      if (!pill) {
        pill = document.createElement('button');
        pill.id = 'fundile-pause-pill';
        pill.type = 'button';
        pill.innerHTML = '⏸️ PAUSE AUTOPILOT <span style="font-size:11px;opacity:0.75;margin-left:4px;">(Space/P)</span>';
        pill.title = 'Click or press Spacebar / P to pause autopilot. Click again or press Spacebar / R to resume.';

        let isLocallyPaused = false;
        let isResumingCooldown = false;

        const updatePillUI = (paused) => {
          isLocallyPaused = paused;
          if (paused) {
            isResumingCooldown = false;
            pill.innerHTML = '▶️ RESUME AUTOPILOT <span style="font-size:11px;opacity:0.85;margin-left:4px;">(Space/R)</span>';
            pill.classList.remove('is-resuming');
            pill.classList.add('is-paused');
            pill.style.background = '#16a34a';
            pill.style.borderColor = '#ffffff';
            pill.style.boxShadow = '0 0 25px rgba(22, 163, 74, 0.9)';
          } else {
            pill.classList.remove('is-paused');
            pill.classList.remove('is-resuming');
            pill.innerHTML = '⏸️ PAUSE AUTOPILOT <span style="font-size:11px;opacity:0.75;margin-left:4px;">(Space/P)</span>';
            pill.style.background = '#0f172a';
            pill.style.borderColor = '#ef4444';
            pill.style.boxShadow = '0 4px 16px rgba(0, 0, 0, 0.4)';
          }
        };

        window.__FUNDILE_SET_UI__ = updatePillUI;

        // Exposed global helpers
        window.__FUNDILE_RESUME__ = async () => {
          if (isResumingCooldown) return;
          isResumingCooldown = true;
          isLocallyPaused = false;

          // Transition pill to "RESUMING..." with pointer-events locked
          pill.innerHTML = '▶️ RESUMING... <span style="font-size:11px;opacity:0.85;margin-left:4px;">(Advancing)</span>';
          pill.classList.remove('is-paused');
          pill.classList.add('is-resuming');

          if (typeof window.__FUNDILE_NODE_RESUME__ === 'function') {
            await window.__FUNDILE_NODE_RESUME__();
          }

          // Lock out re-pausing for 1500ms so bounce/double-clicks NEVER re-pause
          setTimeout(() => {
            isResumingCooldown = false;
            updatePillUI(false);
          }, 1500);
        };

        window.__FUNDILE_PAUSE__ = async () => {
          if (isResumingCooldown) return; // Cannot pause during resume cooldown
          updatePillUI(true);
          if (typeof window.__FUNDILE_NODE_PAUSE__ === 'function') {
            await window.__FUNDILE_NODE_PAUSE__();
          }
        };

        // Explicit Idempotent Click Handler
        pill.addEventListener('click', async (e) => {
          e.preventDefault();
          e.stopPropagation();

          if (isResumingCooldown) return;

          if (isLocallyPaused) {
            await window.__FUNDILE_RESUME__();
          } else {
            await window.__FUNDILE_PAUSE__();
          }
        });

        // Dedicated Keyboard Listeners
        window.addEventListener('keydown', async (e) => {
          const activeTag = (document.activeElement && document.activeElement.tagName) || '';
          if (activeTag === 'INPUT' || activeTag === 'TEXTAREA' || (document.activeElement && document.activeElement.isContentEditable)) {
            return;
          }

          if (isResumingCooldown) return;

          const key = (e.key || '').toLowerCase();
          if (key === 'r' && isLocallyPaused) {
            e.preventDefault();
            await window.__FUNDILE_RESUME__();
          } else if (key === 'p' && !isLocallyPaused) {
            e.preventDefault();
            await window.__FUNDILE_PAUSE__();
          } else if (e.code === 'Space') {
            e.preventDefault();
            // Blur active element so Space doesn't re-trigger native button click
            if (document.activeElement && typeof document.activeElement.blur === 'function') {
              document.activeElement.blur();
            }

            if (isLocallyPaused) {
              await window.__FUNDILE_RESUME__();
            } else {
              await window.__FUNDILE_PAUSE__();
            }
          }
        });

        document.body.appendChild(pill);
      }
    });
  } catch (e) {}
}

/**
 * Await paused state without busy polling or race conditions
 */
export async function waitIfPaused(page) {
  if (!page || page.isClosed()) return;

  // Check file bridge for CLI backwards-compatibility
  let filePaused = false;
  if (fs.existsSync(pauseBridgeFile)) {
    try {
      const data = JSON.parse(fs.readFileSync(pauseBridgeFile, 'utf8') || '{}');
      filePaused = data.status === 'pause';
    } catch {}
  }

  if (filePaused) {
    doPause();
  }

  if (!isAutopilotPaused) return;

  // Ensure browser pill visually shows paused state
  await page.evaluate(() => {
    if (typeof window.__FUNDILE_SET_UI__ === 'function') {
      window.__FUNDILE_SET_UI__(true);
    }
  }).catch(() => {});

  // Wait asynchronously until isAutopilotPaused is set to false
  while (isAutopilotPaused) {
    if (page.isClosed()) break;
    await Promise.race([
      new Promise((resolve) => pauseWaiters.push(resolve)),
      new Promise((resolve) => setTimeout(resolve, 150))
    ]);
  }

  // Ensure browser pill visually shows running state
  await page.evaluate(() => {
    if (typeof window.__FUNDILE_SET_UI__ === 'function') {
      window.__FUNDILE_SET_UI__(false);
    }
  }).catch(() => {});

  try {
    if (fs.existsSync(pauseBridgeFile)) fs.unlinkSync(pauseBridgeFile);
  } catch {}
}

/**
 * Pause-aware visual dwell helper
 * - Slices dwell duration into 100ms segments.
 * - While paused in waitIfPaused, remaining duration DOES NOT DECREMENT.
 * - Once resumed, finishes the remaining time of the dwell.
 */
export async function pauseAwareDwell(page, totalMs = 3000) {
  let remainingMs = totalMs;
  while (remainingMs > 0) {
    if (page.isClosed()) break;
    await waitIfPaused(page);
    const slice = Math.min(100, remainingMs);
    await page.waitForTimeout(slice);
    remainingMs -= slice;
  }
}

export async function updateHud(page, persona, message) {
  if (persona && message) {
    console.log(`   [${persona}] ${message}`);
  }
  await waitIfPaused(page);
}

export async function glideCursorTo(page, selector) {
  await waitIfPaused(page);
  try {
    const loc = typeof selector === 'string' ? page.locator(selector).first() : selector;
    await loc.scrollIntoViewIfNeeded({ timeout: 2000 }).catch(() => {});
    const box = await loc.boundingBox();
    if (box) {
      const vp = page.viewportSize() || { width: 1280, height: 850 };
      const rawX = Math.round(box.x + box.width / 2);
      const rawY = Math.round(box.y + box.height / 2);
      const x = Math.min(Math.max(10, rawX), vp.width - 10);
      const y = Math.min(Math.max(10, rawY), vp.height - 10);
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
