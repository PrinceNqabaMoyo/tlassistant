const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const TARGETS = [
  {
    svg: 'male_sagittal_vector.svg',
    out: 'male_sagittal_preview.jpg',
    width: 600,
    height: 480,
    maxW: '540px',
    maxH: '440px',
  },
  {
    svg: 'female_front_1_vector.svg',
    out: 'female_front_1_preview.jpg',
    width: 600,
    height: 480,
    maxW: '540px',
    maxH: '440px',
  },
  {
    svg: 'female_no_description.svg',
    out: 'female_no_desc_preview.jpg',
    width: 600,
    height: 480,
    maxW: '540px',
    maxH: '440px',
  },
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 600, height: 480 } });

  for (const t of TARGETS) {
    const svgPath = path.resolve('public/diagrams/source_plates', t.svg);
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

    const outPath = path.resolve('public/diagrams/source_plates', t.out);
    await page.screenshot({
      path: outPath,
      type: 'jpeg',
      quality: 95,
      clip: { x: 0, y: 0, width: t.width, height: t.height },
    });
    console.log(`Rendered ${outPath}`);
  }

  await browser.close();
})();
