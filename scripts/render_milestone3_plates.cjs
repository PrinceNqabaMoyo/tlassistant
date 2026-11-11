const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const TARGETS = [
  {
    svg: 'human_eye_wikimedia.svg',
    out: 'human_eye_textbook.jpg',
    maxW: '520px',
    maxH: '480px',
  },
  {
    svg: 'human_ear_wikimedia.svg',
    out: 'human_ear_textbook.jpg',
    maxW: '520px',
    maxH: '480px',
  },
  {
    svg: 'endocrine_system_wikimedia.svg',
    out: 'endocrine_system_textbook.jpg',
    maxW: '480px',
    maxH: '520px',
  },
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 640, height: 600 } });

  for (const t of TARGETS) {
    const svgPath = path.resolve('public/diagrams', t.svg);
    const svgContent = fs.readFileSync(svgPath, 'utf8');

    const htmlContent = `
      <!DOCTYPE html>
      <html>
        <head>
          <style>
            * { box-sizing: border-box; }
            body {
              margin: 0;
              padding: 20px;
              background: #FFFFFF;
              display: flex;
              justify-content: center;
              align-items: center;
              width: 640px;
              height: 600px;
            }
            svg {
              max-height: ${t.maxH};
              max-width: ${t.maxW};
              height: auto;
              width: auto;
            }
          </style>
        </head>
        <body>
          ${svgContent}
        </body>
      </html>
    `;

    await page.setContent(htmlContent);
    await page.waitForTimeout(500);
    const outPath = path.resolve('public/diagrams', t.out);
    await page.screenshot({ path: outPath, type: 'jpeg', quality: 95 });
    console.log(`Rendered ${t.out} (${fs.statSync(outPath).size} bytes)`);
  }

  await browser.close();
  console.log('Successfully rendered all Milestone 3 textbook plates.');
})();
