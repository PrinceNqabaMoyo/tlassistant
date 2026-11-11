const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const brainDir = 'C:\\Users\\princ\\.gemini\\antigravity\\brain\\f0985f12-5686-4fbe-a862-be3e4709f90c';
const pubDir = path.resolve('public/diagrams');

// 1. Copy generated textbook plates
fs.copyFileSync(
  path.join(brainDir, 'plant_cell_textbook_master_1792861976569.jpg'),
  path.join(pubDir, 'plant_cell_textbook.jpg')
);
console.log(`Copied plant_cell_textbook.jpg: ${fs.statSync(path.join(pubDir, 'plant_cell_textbook.jpg')).size} bytes`);

fs.copyFileSync(
  path.join(brainDir, 'mitosis_textbook_master_1792862000376.jpg'),
  path.join(pubDir, 'mitosis_stages_textbook.jpg')
);
console.log(`Copied mitosis_stages_textbook.jpg: ${fs.statSync(path.join(pubDir, 'mitosis_stages_textbook.jpg')).size} bytes`);

fs.copyFileSync(
  path.join(brainDir, 'dicot_leaf_textbook_master_1792862014160.jpg'),
  path.join(pubDir, 'plant_leaf_textbook.jpg')
);
console.log(`Copied plant_leaf_textbook.jpg: ${fs.statSync(path.join(pubDir, 'plant_leaf_textbook.jpg')).size} bytes`);

// 2. Render animal_cell_textbook.jpg from animal_cell_clean.svg
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 800 } });

  const svgPath = path.join(pubDir, 'animal_cell_clean.svg');
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
            width: 1000px;
            height: 800px;
          }
          svg {
            max-height: 740px;
            max-width: 900px;
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

  const outPath = path.join(pubDir, 'animal_cell_textbook.jpg');
  await page.screenshot({
    path: outPath,
    type: 'jpeg',
    quality: 98,
    clip: { x: 0, y: 0, width: 1000, height: 800 },
  });
  console.log(`Rendered animal_cell_textbook.jpg (${fs.statSync(outPath).size} bytes)`);

  await browser.close();
})();
