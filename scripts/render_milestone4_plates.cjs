const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const TARGETS = [
  {
    svg: 'male_reproductive_cleaned.svg',
    out: 'male_reproductive_textbook.jpg',
    width: 1000,
    height: 800,
    maxW: '900px',
    maxH: '740px',
  },
  {
    svg: 'female_reproductive_cleaned.svg',
    out: 'female_reproductive_textbook.jpg',
    width: 1000,
    height: 800,
    maxW: '900px',
    maxH: '740px',
  },
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 800 } });

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
              padding: 0;
              background: #FFFFFF;
              display: flex;
              justify-content: center;
              align-items: center;
              width: ${t.width}px;
              height: ${t.height}px;
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

    await page.setContent(htmlContent, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    const outPath = path.resolve('public/diagrams', t.out);
    await page.screenshot({
      path: outPath,
      type: 'jpeg',
      quality: 98,
      clip: { x: 0, y: 0, width: t.width, height: t.height },
    });
    console.log(`Rendered ${outPath} (${fs.statSync(outPath).size} bytes)`);
  }

  await browser.close();
})();
