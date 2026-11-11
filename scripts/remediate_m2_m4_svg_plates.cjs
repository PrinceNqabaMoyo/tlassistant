const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 600, height: 480 }, deviceScaleFactor: 2 });

  // Helper to inject SVG, clean it in DOM, fit viewBox via getBBox(), and render both textbook and exam stipple
  async function renderSvgPair({
    name,
    svgPath,
    cleanFnStr,
    enhanceTextbookFnStr,
    padRatio = 0.08,
  }) {
    const rawSvg = fs.readFileSync(path.resolve(svgPath), 'utf8');
    // Strip XML declaration and DOCTYPE if any
    const cleanXml = rawSvg
      .replace(/<\?xml[^>]*\?>/gi, '')
      .replace(/<!DOCTYPE[^>]*>/gi, '');

    const html = `
      <!DOCTYPE html>
      <html>
        <head>
          <style>
            * { box-sizing: border-box; }
            html, body {
              margin: 0;
              padding: 0;
              width: 600px;
              height: 480px;
              background: #FFFFFF;
              overflow: hidden;
              display: flex;
              align-items: center;
              justify-content: center;
            }
            svg {
              width: 600px;
              height: 480px;
              display: block;
            }
          </style>
        </head>
        <body>
          ${cleanXml}
        </body>
      </html>
    `;

    await page.setContent(html);
    await page.waitForTimeout(200);

    // Run cleaning and viewBox fitting in browser context
    const bboxInfo = await page.evaluate(
      ({ cleanFnStr, enhanceTextbookFnStr, padRatio }) => {
        const svg = document.querySelector('svg');
        if (!svg) return null;

        // Remove all text and switch elements globally
        svg.querySelectorAll('text, tspan, switch').forEach((el) => el.remove());

        if (cleanFnStr) {
          const fn = new Function('svg', cleanFnStr);
          fn(svg);
        }

        // Ensure SVG is visible and measure exact bounding box of remaining artwork
        svg.removeAttribute('width');
        svg.removeAttribute('height');
        svg.style.width = '600px';
        svg.style.height = '480px';

        const bbox = svg.getBBox();
        const padX = bbox.width * padRatio;
        const padY = bbox.height * padRatio;
        const vx = bbox.x - padX;
        const vy = bbox.y - padY;
        const vw = bbox.width + padX * 2;
        const vh = bbox.height + padY * 2;
        svg.setAttribute('viewBox', `${vx} ${vy} ${vw} ${vh}`);
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');

        if (enhanceTextbookFnStr) {
          const fn = new Function('svg', enhanceTextbookFnStr);
          fn(svg);
        }

        return { x: bbox.x, y: bbox.y, width: bbox.width, height: bbox.height, viewBox: `${vx} ${vy} ${vw} ${vh}` };
      },
      { cleanFnStr, enhanceTextbookFnStr, padRatio }
    );

    console.log(`[${name}] fitted viewBox:`, bboxInfo);

    const textbookOut = path.resolve('public/diagrams', `${name}_textbook.jpg`);
    await page.screenshot({ path: textbookOut, type: 'jpeg', quality: 96 });
    console.log(`Saved ${textbookOut}`);

    // Now transform the live SVG DOM into authentic NSC black-and-white pen-and-ink line-art + stipple
    await page.evaluate(() => {
      const svg = document.querySelector('svg');
      svg.style.filter = 'none';

      // Create SVG defs with stipple patterns of varying density
      let defs = svg.querySelector('defs');
      if (!defs) {
        defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
        svg.prepend(defs);
      }

      const vb = svg.viewBox.baseVal;
      const scaleUnit = Math.max(vb.width, vb.height) / 500;
      const pDense = 6 * scaleUnit;
      const pMed = 9 * scaleUnit;
      const pLight = 13 * scaleUnit;
      const rDot = 0.85 * scaleUnit;

      defs.innerHTML += `
        <pattern id="nsc_stipple_dense" width="${pDense}" height="${pDense}" patternUnits="userSpaceOnUse">
          <rect width="${pDense}" height="${pDense}" fill="#FFFFFF"/>
          <circle cx="${pDense * 0.25}" cy="${pDense * 0.25}" r="${rDot * 1.1}" fill="#1a1a1a"/>
          <circle cx="${pDense * 0.75}" cy="${pDense * 0.70}" r="${rDot}" fill="#1a1a1a"/>
          <circle cx="${pDense * 0.65}" cy="${pDense * 0.20}" r="${rDot * 0.8}" fill="#333333"/>
        </pattern>
        <pattern id="nsc_stipple_med" width="${pMed}" height="${pMed}" patternUnits="userSpaceOnUse">
          <rect width="${pMed}" height="${pMed}" fill="#FFFFFF"/>
          <circle cx="${pMed * 0.3}" cy="${pMed * 0.3}" r="${rDot}" fill="#222222"/>
          <circle cx="${pMed * 0.75}" cy="${pMed * 0.75}" r="${rDot * 0.9}" fill="#222222"/>
        </pattern>
        <pattern id="nsc_stipple_light" width="${pLight}" height="${pLight}" patternUnits="userSpaceOnUse">
          <rect width="${pLight}" height="${pLight}" fill="#FFFFFF"/>
          <circle cx="${pLight * 0.45}" cy="${pLight * 0.45}" r="${rDot * 0.85}" fill="#333333"/>
        </pattern>
      `;

      // Convert all shape elements to crisp black line-art + open white / stippled interiors
      const shapes = svg.querySelectorAll('path, rect, circle, ellipse, polygon, polyline');
      shapes.forEach((el) => {
        if (el.closest('defs') || el.closest('clipPath') || el.closest('mask')) return;
        const cs = window.getComputedStyle(el);
        const fill = cs.fill;
        const fillOpacity = parseFloat(cs.fillOpacity || '1');
        const opacity = parseFloat(cs.opacity || '1');

        // Parse RGB luminance if solid color
        let lum = 255;
        const rgbMatch = fill && fill.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
        if (rgbMatch) {
          const r = parseInt(rgbMatch[1], 10);
          const g = parseInt(rgbMatch[2], 10);
          const b = parseInt(rgbMatch[3], 10);
          lum = 0.299 * r + 0.587 * g + 0.114 * b;
        } else if (fill && fill.startsWith('url(')) {
          lum = 175; // Gradient fill -> medium-light stipple
        }

        if (fill === 'none' || fillOpacity < 0.08 || opacity < 0.08) {
          el.style.fill = 'none';
        } else if (lum > 235) {
          el.style.fill = '#FFFFFF';
          el.style.fillOpacity = '1';
        } else if (lum > 185) {
          el.style.fill = 'url(#nsc_stipple_light)';
          el.style.fillOpacity = '1';
        } else if (lum > 110) {
          el.style.fill = 'url(#nsc_stipple_med)';
          el.style.fillOpacity = '1';
        } else {
          el.style.fill = 'url(#nsc_stipple_dense)';
          el.style.fillOpacity = '1';
        }

        // Ensure crisp black anatomical outline
        el.style.stroke = '#111111';
        const curSw = parseFloat(cs.strokeWidth || '0');
        el.style.strokeWidth = curSw > 0.2 ? `${Math.min(Math.max(curSw, 1.1 * scaleUnit), 3.0 * scaleUnit)}px` : `${1.1 * scaleUnit}px`;
        el.style.strokeOpacity = '1';
      });
    });

    await page.waitForTimeout(200);
    const examOut = path.resolve('public/diagrams', `${name}_exam_stipple.jpg`);
    await page.screenshot({ path: examOut, type: 'jpeg', quality: 96 });
    console.log(`Saved ${examOut}`);
  }

  // 1. Human Eye (from eye_no_circles_border.svg)
  await renderSvgPair({
    name: 'human_eye',
    svgPath: 'public/diagrams/source_plates/eye_no_circles_border.svg',
    padRatio: 0.06,
    cleanFnStr: `
      const layer1 = svg.querySelector('#layer1');
      if (layer1) {
        Array.from(layer1.children).forEach(c => {
          const id = c.id || '';
          if (
            id === 'g6398' ||
            id === 'path12577' ||
            id.startsWith('path10') ||
            id.startsWith('path148') ||
            id === 'g14824' ||
            id.startsWith('text1')
          ) {
            c.remove();
          }
        });
      }
    `,
    enhanceTextbookFnStr: `
      svg.style.filter = 'drop-shadow(0px 4px 10px rgba(15, 23, 42, 0.08))';
    `,
  });

  // 2. Human Ear (from ear_3d_blank.svg — 100% free of leader lines)
  await renderSvgPair({
    name: 'human_ear',
    svgPath: 'public/diagrams/source_plates/ear_3d_blank.svg',
    padRatio: 0.06,
    cleanFnStr: `
      // Remove grey background slabs (#dee3db) and any leader lines
      svg.querySelectorAll('path, rect, g').forEach((c) => {
        const fill = (c.getAttribute('fill') || '').toLowerCase();
        const style = (c.getAttribute('style') || '').toLowerCase();
        if (fill === '#dee3db' || style.includes('#dee3db')) {
          c.remove();
        }
      });
    `,
    enhanceTextbookFnStr: `
      svg.style.filter = 'drop-shadow(0px 3px 8px rgba(15, 23, 42, 0.08))';
    `,
  });

  // 3. Digestive System (from digestive_system_wikimedia.svg)
  await renderSvgPair({
    name: 'digestive',
    svgPath: 'public/diagrams/digestive_system_wikimedia.svg',
    padRatio: 0.05,
    cleanFnStr: `
      // Remove only the single invisible stray stomach outline floating to the right of the body
      svg.querySelectorAll('path').forEach(el => {
        const cs = window.getComputedStyle(el);
        if (cs.fill === 'none' && (cs.stroke === 'none' || cs.strokeOpacity === '0')) {
          el.remove();
        }
      });
    `,
    enhanceTextbookFnStr: `
      svg.style.filter = 'drop-shadow(0px 3px 6px rgba(15, 23, 42, 0.07))';
    `,
  });

  // 4. Endocrine System (from endocrine_system_wikimedia.svg)
  await renderSvgPair({
    name: 'endocrine_system',
    svgPath: 'public/diagrams/endocrine_system_wikimedia.svg',
    padRatio: 0.06,
    cleanFnStr: `
      // Remove stray circle on top-right and stray lines at bottom
      svg.querySelectorAll('path, circle, ellipse, line, polyline').forEach(el => {
        try {
          const b = el.getBBox();
          const r = el.getBoundingClientRect();
          if (b.y > 250 || r.left > 430) {
            el.remove();
          }
        } catch (e) {}
      });
    `,
    enhanceTextbookFnStr: `
      svg.style.filter = 'drop-shadow(0px 3px 6px rgba(15, 23, 42, 0.07))';
    `,
  });

  // 5. Female Reproductive System (from female_reproductive_cleaned.svg)
  await renderSvgPair({
    name: 'female_reproductive',
    svgPath: 'public/diagrams/female_reproductive_cleaned.svg',
    padRatio: 0.10,
    cleanFnStr: ``,
    enhanceTextbookFnStr: `
      svg.style.filter = 'drop-shadow(0px 4px 10px rgba(15, 23, 42, 0.08))';
    `,
  });

  await browser.close();
})();
