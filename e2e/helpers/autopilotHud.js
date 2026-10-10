/**
 * Autopilot HUD & Virtual Cursor Overlay
 * Provides visual narration, realistic gliding cursor, live pause/resume controls,
 * and time-simulation countdowns for headed Playwright test runs.
 * Does NOT hijack the host OS mouse pointer; renders in-browser virtual cursor and controls.
 */

export async function injectGlidingCursorAndHud(page) {
  await page.evaluate(() => {
    if (document.getElementById('autopilot-hud')) return;

    window.__AUTOPILOT_PAUSED = false;

    // Inject styles
    const style = document.createElement('style');
    style.id = 'autopilot-hud-styles';
    style.innerHTML = `
      #virtual-cursor {
        position: fixed;
        pointer-events: none;
        z-index: 2147483647;
        width: 28px;
        height: 28px;
        font-size: 22px;
        top: 0;
        left: 0;
        transform: translate(20px, 20px);
        transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.2s;
        filter: drop-shadow(0 3px 6px rgba(0,0,0,0.35));
        user-select: none;
      }
      #virtual-cursor.clicking {
        transform: scale(0.85);
        filter: drop-shadow(0 1px 2px rgba(0,0,0,0.5));
      }
      #autopilot-hud {
        position: fixed;
        top: 14px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 2147483646;
        background: rgba(15, 23, 42, 0.94);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        color: #f8fafc;
        border: 1px solid rgba(255, 255, 255, 0.22);
        border-radius: 9999px;
        padding: 8px 18px;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        font-size: 13px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 14px 34px -4px rgba(0, 0, 0, 0.5), 0 4px 8px -2px rgba(0,0,0,0.2);
        user-select: none;
        transition: all 0.3s ease;
        max-width: 92vw;
        white-space: nowrap;
      }
      #autopilot-hud .badge {
        background: #FF9100;
        color: #0b2545;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.04em;
        text-transform: uppercase;
      }
      #autopilot-hud .message {
        color: #e2e8f0;
      }
      #autopilot-hud .pulse {
        display: inline-block;
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        box-shadow: 0 0 8px #10B981;
        animation: hudPulse 1.5s infinite;
      }
      #autopilot-hud .pulse.paused {
        background-color: #EF4444;
        box-shadow: 0 0 8px #EF4444;
        animation: none;
      }
      #autopilot-hud-pause-btn {
        pointer-events: auto;
        background: #334155;
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: #f8fafc;
        border-radius: 9999px;
        padding: 3px 12px;
        font-size: 11px;
        font-weight: 700;
        cursor: pointer;
        transition: background 0.2s, transform 0.1s;
        display: inline-flex;
        align-items: center;
        gap: 4px;
      }
      #autopilot-hud-pause-btn:hover {
        background: #475569;
        transform: scale(1.04);
      }
      #autopilot-hud-pause-btn.is-paused {
        background: #DC2626;
        color: #FFFFFF;
        border-color: #EF4444;
      }
      @keyframes hudPulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(0.85); }
      }
    `;
    document.head.appendChild(style);

    // Inject Virtual Cursor
    const cursor = document.createElement('div');
    cursor.id = 'virtual-cursor';
    cursor.innerText = '🖱️';
    document.body.appendChild(cursor);

    // Inject HUD
    const hud = document.createElement('div');
    hud.id = 'autopilot-hud';
    hud.innerHTML = `
      <span class="pulse" id="autopilot-hud-pulse"></span>
      <span class="badge" id="autopilot-hud-persona">AUTOPILOT</span>
      <span class="message" id="autopilot-hud-message">Initializing autonomous user session...</span>
      <button id="autopilot-hud-pause-btn" title="Click or press Spacebar to Pause/Resume">⏸ Pause</button>
    `;
    document.body.appendChild(hud);

    // Toggle pause function
    window.__toggleAutopilotPause = function () {
      window.__AUTOPILOT_PAUSED = !window.__AUTOPILOT_PAUSED;
      const btn = document.getElementById('autopilot-hud-pause-btn');
      const pulse = document.getElementById('autopilot-hud-pulse');
      if (btn) {
        if (window.__AUTOPILOT_PAUSED) {
          btn.innerText = '▶ Resume';
          btn.classList.add('is-paused');
          if (pulse) pulse.classList.add('paused');
        } else {
          btn.innerText = '⏸ Pause';
          btn.classList.remove('is-paused');
          if (pulse) pulse.classList.remove('paused');
        }
      }
    };

    const pauseBtn = document.getElementById('autopilot-hud-pause-btn');
    if (pauseBtn) {
      pauseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        window.__toggleAutopilotPause();
      });
    }

    // Spacebar listener to toggle pause (when not inside input/textarea)
    document.addEventListener('keydown', (e) => {
      if (e.code === 'Space' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
        e.preventDefault();
        window.__toggleAutopilotPause();
      }
    });
  });
}

export async function waitIfPaused(page) {
  try {
    while (true) {
      const isPaused = await page.evaluate(() => window.__AUTOPILOT_PAUSED).catch(() => false);
      if (!isPaused) break;
      await page.waitForTimeout(350);
    }
  } catch (e) {}
}

export async function updateHud(page, persona, message) {
  try {
    await waitIfPaused(page);
    await page.evaluate(({ persona, message }) => {
      const pEl = document.getElementById('autopilot-hud-persona');
      const mEl = document.getElementById('autopilot-hud-message');
      if (pEl) pEl.innerText = persona;
      if (mEl) mEl.innerText = message;
    }, { persona, message });
  } catch (e) {}
}

export async function glideCursorTo(page, selector) {
  await waitIfPaused(page);
  try {
    const loc = page.locator(selector).first();
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
      await page.mouse.move(x, y, { steps: 5 });
    }
  } catch (e) {}
}

export async function glideAndClick(page, selector, { persona = 'AUTOPILOT', message = '' } = {}) {
  await waitIfPaused(page);
  if (message) {
    await updateHud(page, persona, message);
  }
  const loc = page.locator(selector).first();
  await loc.waitFor({ state: 'visible', timeout: 12000 });
  await glideCursorTo(page, selector);
  await waitIfPaused(page);
  await page.waitForTimeout(200);

  // Click animation
  await page.evaluate(() => {
    const cursor = document.getElementById('virtual-cursor');
    if (cursor) cursor.classList.add('clicking');
  });
  await loc.click();
  await page.waitForTimeout(120);
  await page.evaluate(() => {
    const cursor = document.getElementById('virtual-cursor');
    if (cursor) cursor.classList.remove('clicking');
  });
  await waitIfPaused(page);
}

export async function typeRealistic(page, selector, text, { delayMs = 60, persona, message } = {}) {
  await waitIfPaused(page);
  if (message) {
    await updateHud(page, persona || 'AUTOPILOT', message);
  }
  const loc = page.locator(selector).first();
  await loc.waitFor({ state: 'visible', timeout: 10000 });
  await glideCursorTo(page, selector);
  await loc.click();
  await loc.fill('');

  for (const char of text) {
    await waitIfPaused(page);
    await page.keyboard.type(char, { delay: delayMs });
  }
  await page.waitForTimeout(200);
}

export async function simulateStudyBreak(page, countdownSeconds = 60, simulatedMins = 20) {
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
  await page.waitForTimeout(1500);
}
