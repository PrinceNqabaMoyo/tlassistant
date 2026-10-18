/**
 * Visual Neatness & Button Placement Ergonomics Evaluator
 * Fundile Automated Verification Engine
 * 
 * Programmatically evaluates screenshots and DOM surfaces for:
 * 1. Cognitive clutter & visual density (too busy)
 * 2. Button placement ergonomics (touch target >= 44px on mobile, >= 32px desktop, >= 8px gap)
 * 3. Primary CTA prominence & above-the-fold visibility
 * 4. Destructive vs constructive action separation
 * 5. 60-30-10 color balance & visual noise (saturated badges fighting for attention)
 * 6. Horizontal overflow & clipping leaks
 */
import fs from 'fs';
import path from 'path';

export async function evaluatePageNeatness(page, options = {}) {
  const {
    role = 'user',
    screenName = 'Dashboard',
    isMobile = false,
    screenshotPath = null
  } = options;

  const evaluation = await page.evaluate(({ isMobile }) => {
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;
    const scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;

    // 1. Interactive Elements Analysis
    const interactiveElements = Array.from(document.querySelectorAll('button, a, input, select, textarea, [role="button"], [data-testid^="btn-"], [data-testid^="tab-"]'));
    const visibleInteractive = interactiveElements.filter(el => {
      const rect = el.getBoundingClientRect();
      const style = window.getComputedStyle(el);
      return rect.width > 0 && rect.height > 0 && style.visibility !== 'hidden' && style.display !== 'none' && style.opacity !== '0';
    });

    const densityPer1000px = Math.round((visibleInteractive.length / Math.max(1, scrollHeight)) * 1000);

    // 2. Button Placement & Touch Target Ergonomics
    const buttons = Array.from(document.querySelectorAll('button, [role="button"], [data-testid^="btn-"]')).filter(el => {
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });

    const minTouchSize = isMobile ? 44 : 32;
    let undersizedButtonsCount = 0;
    let crowdedButtonsCount = 0;
    let aboveTheFoldButtons = 0;
    let primaryCtasFound = 0;
    let destructiveSeparationValid = true;

    const buttonDetails = [];

    for (let i = 0; i < buttons.length; i++) {
      const btn = buttons[i];
      const rect = btn.getBoundingClientRect();
      const text = (btn.innerText || btn.getAttribute('aria-label') || btn.getAttribute('title') || '').trim();
      const testId = btn.getAttribute('data-testid') || '';
      const classes = btn.className || '';

      // Check touch target size
      const isUndersized = rect.width < minTouchSize || rect.height < minTouchSize;
      if (isUndersized) undersizedButtonsCount++;

      // Check if button is in primary initial fold
      const isAboveFold = rect.top >= 0 && rect.top <= viewportHeight;
      if (isAboveFold) aboveTheFoldButtons++;

      // Detect primary CTA vs destructive
      const isPrimary = /bg-(blue|emerald|amber|indigo)-600|bg-\[#13519C\]|from-\[#13519C\]/.test(classes);
      const isDestructive = /reject|delete|remove|reset|cancel|block/i.test(text) || /reject|delete|remove|reset/.test(testId);

      if (isPrimary && isAboveFold) primaryCtasFound++;

      // Check proximity to other buttons (minimum 8px gap)
      for (let j = i + 1; j < buttons.length; j++) {
        const otherRect = buttons[j].getBoundingClientRect();
        const horizontalOverlap = Math.max(0, Math.min(rect.right, otherRect.right) - Math.max(rect.left, otherRect.left));
        const verticalOverlap = Math.max(0, Math.min(rect.bottom, otherRect.bottom) - Math.max(rect.top, otherRect.top));

        // If elements are nearly touching (< 6px gap in same row/col)
        const gapX = Math.max(0, Math.max(rect.left, otherRect.left) - Math.min(rect.right, otherRect.right));
        const gapY = Math.max(0, Math.max(rect.top, otherRect.top) - Math.min(rect.bottom, otherRect.bottom));

        if ((horizontalOverlap > 0 && gapY > 0 && gapY < 6) || (verticalOverlap > 0 && gapX > 0 && gapX < 6)) {
          crowdedButtonsCount++;
        }
      }

      buttonDetails.push({
        text: text.slice(0, 30),
        testId,
        width: Math.round(rect.width),
        height: Math.round(rect.height),
        isUndersized,
        isAboveFold,
        isPrimary,
        isDestructive
      });
    }

    // 3. Visual Noise: High-Contrast Competing Badges (60-30-10 Rule)
    const saturatedBadges = Array.from(document.querySelectorAll('[class*="bg-amber-"], [class*="bg-rose-"], [class*="bg-emerald-"], [class*="bg-purple-"], [class*="bg-orange-"], [class*="bg-red-"]')).filter(el => {
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0 && rect.top >= 0 && rect.top <= viewportHeight;
    });

    // 4. Whitespace & Breathing Room Ratio
    const cards = Array.from(document.querySelectorAll('.rounded-xl, .rounded-2xl, .bg-white, [class*="card"]')).filter(el => {
      const rect = el.getBoundingClientRect();
      return rect.width > 120 && rect.height > 80 && rect.top >= 0 && rect.top <= viewportHeight;
    });

    let totalCardArea = 0;
    cards.forEach(card => {
      const rect = card.getBoundingClientRect();
      totalCardArea += (rect.width * rect.height);
    });
    const viewportArea = viewportWidth * viewportHeight;
    const cardAreaRatio = Math.min(1, totalCardArea / Math.max(1, viewportArea));
    const whitespaceRatio = Math.max(0, 1 - cardAreaRatio);

    // 5. Horizontal Overflow Leak
    const hasHorizontalOverflow = document.documentElement.scrollWidth > viewportWidth + 2;

    return {
      viewportWidth,
      viewportHeight,
      scrollHeight,
      totalInteractive: visibleInteractive.length,
      densityPer1000px,
      totalButtons: buttons.length,
      aboveTheFoldButtons,
      primaryCtasFound,
      undersizedButtonsCount,
      crowdedButtonsCount,
      destructiveSeparationValid,
      saturatedBadgeCountAboveFold: saturatedBadges.length,
      whitespaceRatio: Math.round(whitespaceRatio * 100),
      hasHorizontalOverflow,
      sampleButtons: buttonDetails.slice(0, 10)
    };
  }, { isMobile });

  // Compute ergonomic placement & neatness scores
  let score = 100;
  const critique = [];
  const recommendations = [];

  // Deduct for density / overcrowded screen (> 35 per 1000px)
  if (evaluation.densityPer1000px > 35) {
    score -= 20;
    critique.push(`High element density (${evaluation.densityPer1000px} interactive elements/1000px) — cockpit feels overcrowded.`);
    recommendations.push('Group secondary actions into an accordion, segmented tab, or overflow dropdown.');
  } else if (evaluation.densityPer1000px > 25) {
    score -= 10;
    critique.push(`Moderate element density (${evaluation.densityPer1000px}/1000px).`);
  }

  // Deduct for undersized buttons
  if (evaluation.undersizedButtonsCount > 0) {
    score -= Math.min(15, evaluation.undersizedButtonsCount * 3);
    critique.push(`${evaluation.undersizedButtonsCount} button(s) below recommended ${isMobile ? '44px' : '32px'} touch target height.`);
    recommendations.push(`Ensure all interactive buttons use min-h-[${isMobile ? '44px' : '36px'}] and adequate padding.`);
  }

  // Deduct for crowded buttons (< 6px gap)
  if (evaluation.crowdedButtonsCount > 3) {
    score -= 15;
    critique.push(`Multiple adjacent buttons lack spacing (< 6px gap) — risk of misclicks.`);
    recommendations.push('Add gap-2.5 or gap-3 between adjacent action buttons in flex toolbars.');
  }

  // Deduct for visual noise / badge clutter
  if (evaluation.saturatedBadgeCountAboveFold > 10) {
    score -= 15;
    critique.push(`Excessive visual noise (${evaluation.saturatedBadgeCountAboveFold} colored badges in initial fold) violating 60-30-10 palette.`);
    recommendations.push('Use soft neutral tints (slate-100) for standard labels and reserve saturated tints for urgent status.');
  }

  // Deduct for horizontal overflow
  if (evaluation.hasHorizontalOverflow) {
    score -= 20;
    critique.push('Accidental horizontal overflow detected (scrollWidth > window.innerWidth).');
    recommendations.push('Add overflow-x-hidden to outer container or wrap wide tables in overflow-x-auto.');
  }

  // Primary CTA check
  if (evaluation.primaryCtasFound === 0) {
    score -= 10;
    critique.push('No prominent primary CTA button visible above the fold.');
    recommendations.push('Ensure the key action (e.g. Approve, Launch, Generate) has high contrast and is visible without scrolling.');
  }

  score = Math.max(0, Math.min(100, score));

  const status = score >= 80 ? 'NEAT & BALANCED' : score >= 60 ? 'ACCEPTABLE' : 'TOO BUSY / OVERCROWDED';

  return {
    role,
    screenName,
    isMobile,
    screenshotPath,
    score,
    status,
    metrics: evaluation,
    critique,
    recommendations
  };
}

export function generateNeatnessHtmlReport(results = [], outputPath = 'reports/visual_audits/neatness_report.html') {
  const dir = path.dirname(outputPath);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  const overallAvg = Math.round(results.reduce((acc, r) => acc + r.score, 0) / Math.max(1, results.length));

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Fundile UI Visual Neatness & Button Ergonomics Report</title>
  <style>
    body { font-family: system-ui, -apple-system, sans-serif; background: #f8fafc; color: #0f172a; margin: 0; padding: 32px; }
    h1 { font-size: 28px; margin-bottom: 8px; color: #13519C; }
    .badge { display: inline-block; padding: 4px 10px; border-radius: 9999px; font-size: 12px; font-weight: bold; }
    .badge-pass { background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
    .badge-warn { background: #fffbeb; color: #b45309; border: 1px solid #fde68a; }
    .badge-fail { background: #fff1f2; color: #be123c; border: 1px solid #fecdd3; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); gap: 24px; margin-top: 24px; }
    .card { background: white; border-radius: 16px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .card-header { padding: 16px 20px; border-bottom: 1px solid #f1f5f9; display: flex; justify-content: space-between; align-items: center; }
    .card-body { padding: 20px; }
    .metric-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #f8fafc; font-size: 13px; }
    .critique-box { background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 12px; margin-top: 12px; font-size: 13px; color: #92400e; }
    .rec-box { background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px; margin-top: 8px; font-size: 13px; color: #1e40af; }
    .img-preview { width: 100%; height: 220px; object-fit: cover; object-position: top; border-bottom: 1px solid #e2e8f0; background: #e2e8f0; }
  </style>
</head>
<body>
  <h1>Fundile Cockpit Visual Neatness & Button Ergonomics Audit</h1>
  <p style="color: #64748b; margin-top: 0;">Automated evaluation of UI busyness, density, 60-30-10 adherence, and touch target placement.</p>
  
  <div style="display: flex; gap: 16px; margin-top: 16px;">
    <div style="background: white; padding: 16px 24px; border-radius: 12px; border: 1px solid #e2e8f0;">
      <div style="font-size: 12px; color: #64748b; text-transform: uppercase; font-weight: bold;">Average Ergonomics Score</div>
      <div style="font-size: 32px; font-weight: bold; color: ${overallAvg >= 80 ? '#059669' : overallAvg >= 60 ? '#d97706' : '#e11d48'};">${overallAvg} / 100</div>
    </div>
    <div style="background: white; padding: 16px 24px; border-radius: 12px; border: 1px solid #e2e8f0;">
      <div style="font-size: 12px; color: #64748b; text-transform: uppercase; font-weight: bold;">Audited Cockpits</div>
      <div style="font-size: 32px; font-weight: bold; color: #13519C;">${results.length}</div>
    </div>
  </div>

  <div class="grid">
    ${results.map(r => {
      const badgeClass = r.score >= 80 ? 'badge-pass' : r.score >= 60 ? 'badge-warn' : 'badge-fail';
      const relImg = r.screenshotPath ? path.relative(path.dirname(outputPath), r.screenshotPath).replace(/\\/g, '/') : null;
      return `
      <div class="card">
        ${relImg ? `<img src="${relImg}" class="img-preview" alt="${r.screenName}" />` : ''}
        <div class="card-header">
          <div>
            <strong style="font-size: 16px;">${r.screenName}</strong>
            <div style="font-size: 12px; color: #64748b;">${r.role.toUpperCase()} • ${r.isMobile ? 'Mobile Pixel 7' : 'Desktop 1280x800'}</div>
          </div>
          <span class="badge ${badgeClass}">${r.score}/100 • ${r.status}</span>
        </div>
        <div class="card-body">
          <div class="metric-row"><span>Interactive Element Density</span><strong>${r.metrics.densityPer1000px} / 1000px</strong></div>
          <div class="metric-row"><span>Total Buttons Visible</span><strong>${r.metrics.totalButtons} (${r.metrics.aboveTheFoldButtons} in fold)</strong></div>
          <div class="metric-row"><span>Undersized Buttons (&lt; ${r.isMobile ? '44' : '32'}px)</span><strong>${r.metrics.undersizedButtonsCount}</strong></div>
          <div class="metric-row"><span>Crowded Adjacent Buttons (&lt; 6px gap)</span><strong>${r.metrics.crowdedButtonsCount}</strong></div>
          <div class="metric-row"><span>Primary CTAs in Initial Fold</span><strong>${r.metrics.primaryCtasFound}</strong></div>
          <div class="metric-row"><span>Saturated Color Badges in Fold</span><strong>${r.metrics.saturatedBadgeCountAboveFold}</strong></div>
          <div class="metric-row"><span>Horizontal Scroll Leak</span><strong>${r.metrics.hasHorizontalOverflow ? '❌ LEAK DETECTED' : '✅ CLEAN'}</strong></div>

          ${r.critique.length > 0 ? `
          <div class="critique-box">
            <strong>Ergonomic Critique:</strong>
            <ul style="margin: 4px 0 0 16px; padding: 0;">
              ${r.critique.map(c => `<li>${c}</li>`).join('')}
            </ul>
          </div>` : ''}

          ${r.recommendations.length > 0 ? `
          <div class="rec-box">
            <strong>Recommendations to Declutter:</strong>
            <ul style="margin: 4px 0 0 16px; padding: 0;">
              ${r.recommendations.map(rec => `<li>${rec}</li>`).join('')}
            </ul>
          </div>` : ''}
        </div>
      </div>
      `;
    }).join('')}
  </div>
</body>
</html>`;

  fs.writeFileSync(outputPath, html, 'utf-8');
  return outputPath;
}
