/**
 * Autopilot HUD & Virtual Cursor Overlay
 * Provides visual narration and a smooth gliding cursor for headed Playwright runs.
 * Does NOT hijack the user's host OS mouse pointer; renders an in-browser virtual cursor.
 */

export async function injectGlidingCursorAndHud(page) {
  await page.evaluate(() => {
    if (document.getElementById('autopilot-hud')) return;

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
        background: rgba(15, 23, 42, 0.90);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        color: #f8fafc;
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 9999px;
        padding: 8px 22px;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        font-size: 13px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 12px 30px -4px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0,0,0,0.1);
        pointer-events: none;
        user-select: none;
        transition: all 0.3s ease;
        max-width: 90vw;
        white-space: nowrap;
      }
      #autopilot-hud .badge {
        background: #FF9100;
        color: #0b2545;
        padding: 2.5px 10px;
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
      <span class="pulse"></span>
      <span class="badge" id="autopilot-hud-persona">AUTOPILOT</span>
      <span class="message" id="autopilot-hud-message">Initializing autonomous user session...</span>
    `;
    document.body.appendChild(hud);
  });
}

export async function updateHud(page, persona, message) {
  try {
    await page.evaluate(({ persona, message }) => {
      const pEl = document.getElementById('autopilot-hud-persona');
      const mEl = document.getElementById('autopilot-hud-message');
      if (pEl) pEl.innerText = persona;
      if (mEl) mEl.innerText = message;
    }, { persona, message });
  } catch (e) {
    // Page might have navigated
  }
}

export async function glideCursorTo(page, selector) {
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
  } catch (e) {
    // Selector not visible or error
  }
}

export async function glideAndClick(page, selector, { persona = 'AUTOPILOT', message = '' } = {}) {
  if (message) {
    await updateHud(page, persona, message);
  }
  const loc = page.locator(selector).first();
  await loc.waitFor({ state: 'visible', timeout: 8000 });
  await glideCursorTo(page, selector);
  await page.waitForTimeout(150);

  // Click animation
  await page.evaluate(() => {
    const cursor = document.getElementById('virtual-cursor');
    if (cursor) cursor.classList.add('clicking');
  });
  await loc.click();
  await page.waitForTimeout(100);
  await page.evaluate(() => {
    const cursor = document.getElementById('virtual-cursor');
    if (cursor) cursor.classList.remove('clicking');
  });
}
