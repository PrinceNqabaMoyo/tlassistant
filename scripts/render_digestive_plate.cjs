const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 600, height: 600 } });
  const svgPath = path.resolve('public/diagrams/digestive_system_wikimedia.svg');
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
            width: 600px;
            height: 600px;
          }
          svg {
            max-height: 560px;
            max-width: 440px;
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
  await page.screenshot({ path: 'public/diagrams/digestive_textbook.jpg', type: 'jpeg', quality: 95 });
  await browser.close();
  console.log('Successfully generated public/diagrams/digestive_textbook.jpg with inline SVG');
})();
