const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 700, height: 600 } });

  const svgPath = path.resolve('public/diagrams/source_plates/female_organs_frontal_unlabeled.svg');
  const svgContent = fs.readFileSync(svgPath, 'utf8');

  const htmlContent = `
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          * { box-sizing: border-box; }
          body {
            margin: 0;
            padding: 10px;
            background: #FFFFFF;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 700px;
            height: 600px;
          }
          svg {
            max-height: 520px;
            max-width: 650px;
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

  const outPath = path.resolve('public/diagrams/source_plates/female_organs_preview.jpg');
  await page.screenshot({
    path: outPath,
    type: 'jpeg',
    quality: 95,
  });
  console.log(`Rendered ${outPath}`);
  await browser.close();
})();
