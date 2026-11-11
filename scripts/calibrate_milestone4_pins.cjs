const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.resolve(__dirname, '..');
const ANCHORS_DIR = path.join(PROJECT_ROOT, 'caps-ai-backend', 'app', 'data', 'diagram_anchors');
const OUT_DIR = path.join(PROJECT_ROOT, 'calibration_shots');

if (!fs.existsSync(OUT_DIR)) {
  fs.mkdirSync(OUT_DIR, { recursive: true });
}

const DIAGRAMS = [
  { master: 'male_reproductive', json: 'male_reproductive.json', img: '/diagrams/male_reproductive_textbook.jpg', x: 40, w: 520 },
  { master: 'female_reproductive', json: 'female_reproductive.json', img: '/diagrams/female_reproductive_textbook.jpg', x: 40, w: 520 },
  { master: 'meiosis_crossing_over', json: 'meiosis_crossing_over.json', img: '/diagrams/meiosis_crossing_over_textbook.jpg', x: 20, w: 560 },
];

function buildHtml(diag) {
  const anchorData = JSON.parse(fs.readFileSync(path.join(ANCHORS_DIR, diag.json), 'utf8'));
  const anchors = anchorData.anchors;
  const pinKeys = Object.keys(anchors);
  
  const pinElements = pinKeys.map((key, idx) => {
    const a = anchors[key];
    const letter = String.fromCharCode(65 + idx);
    const [tx, ty] = a.anchor;
    const isLeft = (a.side === 'left') || (tx < 300);
    const boxX = isLeft ? 50 : 550;
    const boxY = a.default_box ? a.default_box[1] : ty;
    const elbowX = isLeft ? 90 : 510;
    
    return `
      <!-- Pin ${letter}: ${a.name} -->
      <g id="callout_${letter}">
        <path d="M ${tx},${ty} L ${elbowX},${ty} L ${elbowX},${boxY} L ${boxX},${boxY}" 
              fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 2" />
        <circle cx="${tx}" cy="${ty}" r="4.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.5" />
        <rect x="${boxX - 16}" y="${boxY - 14}" width="32" height="28" rx="6" fill="#1e293b" />
        <text x="${boxX}" y="${boxY + 5}" fill="#ffffff" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">${letter}</text>
        <text x="${isLeft ? boxX + 22 : boxX - 22}" y="${boxY + 4}" fill="#0f172a" font-size="10" font-family="sans-serif" font-weight="600" text-anchor="${isLeft ? 'start' : 'end'}">${a.name}</text>
      </g>
    `;
  }).join('\n');

  return `
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          body { margin: 0; padding: 20px; background: #f8fafc; font-family: sans-serif; display: flex; justify-content: center; }
          .card { background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; width: 620px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
          h2 { margin: 0 0 8px 0; font-size: 14px; color: #334155; }
        </style>
      </head>
      <body>
        <div class="card">
          <h2>${diag.master} — Visual Calibration (600x480)</h2>
          <svg viewBox="0 0 600 480" width="600" height="480" style="background: white; border: 1px solid #cbd5e1; border-radius: 8px;">
            <image href="${diag.img}" x="${diag.x}" y="0" width="${diag.w}" height="480" preserveAspectRatio="xMidYMid meet" />
            ${pinElements}
          </svg>
        </div>
      </body>
    </html>
  `;
}

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 800, height: 700 } });

  for (const diag of DIAGRAMS) {
    const html = buildHtml(diag);
    await page.goto('http://127.0.0.1:5173');
    await page.setContent(html);
    await page.waitForTimeout(500);
    const shotPath = path.join(OUT_DIR, `${diag.master}_calibration.png`);
    await page.locator('.card').screenshot({ path: shotPath });
    console.log(`Saved calibration screenshot: ${shotPath}`);
  }

  await browser.close();
}

main().catch(console.error);
