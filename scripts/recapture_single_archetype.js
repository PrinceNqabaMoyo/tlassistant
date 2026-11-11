import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { spawnSync } from 'child_process';

async function main() {
  const grade = '10';
  const subject = 'Mathematics';
  const topic = 'Number patterns';
  const archetypeId = 'term_from_n';

  // 1. Fetch live question via generator_registry in python
  const pyCode = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant
res = generate_variant(topic=${JSON.stringify(topic)}, subskill=${JSON.stringify(archetypeId)}, grade=${JSON.stringify(grade)}, subject=${JSON.stringify(subject)}, seed=101, count=1)
print(json.dumps(res[0]))
`;
  const pyRes = spawnSync('caps-ai-backend\\venv\\Scripts\\python.exe', ['-c', pyCode], { encoding: 'utf-8' });
  if (pyRes.status !== 0) {
    console.error('Python error:', pyRes.stderr);
    process.exit(1);
  }
  const q101 = JSON.parse(pyRes.stdout.trim());
  console.log('Fetched question prompt:', q101.prompt);

  // 2. Launch browser and mount into UniversalWorkspaceHarness
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  await page.goto('http://localhost:5173/?harness=universal_workspace', { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForFunction(() => typeof window.__SET_WORKSPACE_QUESTION__ === 'function', { timeout: 15000 });

  await page.evaluate(({ q, grade, subject, topic }) => {
    return window.__SET_WORKSPACE_QUESTION__(q, { grade, subject, topic, mode: 'practice' });
  }, { q: q101, grade, subject, topic });

  await page.waitForSelector('[data-testid="question-surface"]', { state: 'visible', timeout: 10000 });
  await page.waitForTimeout(200);

  const basePrefix = `gr10_mathematics_number_patterns_term_from_n`;
  const prePath = `reports/full_archetype_audit/shots/${basePrefix}_pre_scroll_1.png`;
  await page.screenshot({ path: prePath, fullPage: false });

  const preDomText = await page.locator('[data-testid="question-surface"]').innerText();
  console.log('Rendered student prompt text in DOM:\n', preDomText);

  const defects = [];
  if (/\\(frac|sqrt|text|begin|right|left)\{/.test(preDomText) || /\$\$/.test(preDomText)) {
    defects.push(`[RAW_LATEX_LEAK] Raw LaTeX tokens found in rendered student prompt.`);
  }
  if (/\b(undefined|NaN)\b|\[object Object\]/.test(preDomText)) {
    defects.push(`[JS_TOKEN_LEAK] Page contains undefined/NaN/[object Object].`);
  }
  if (/\bCAPS\b/.test(preDomText)) {
    defects.push(`[BANNED_CAPS_ACRONYM] Prompt displays banned 'CAPS' acronym.`);
  }

  console.log('Defects found:', defects);

  // Trigger Memo
  await page.evaluate(() => {
    if (typeof window.__TRIGGER_WORKSPACE_MEMO__ === 'function') {
      window.__TRIGGER_WORKSPACE_MEMO__();
    }
  });
  await page.waitForTimeout(200);

  const memoPath1 = `reports/full_archetype_audit/shots/${basePrefix}_memo_scroll_1.png`;
  const memoPath2 = `reports/full_archetype_audit/shots/${basePrefix}_memo_scroll_2.png`;
  await page.screenshot({ path: memoPath1, fullPage: false });
  await page.evaluate(() => window.scrollTo(0, 900));
  await page.waitForTimeout(100);
  await page.screenshot({ path: memoPath2, fullPage: false });

  await browser.close();

  // 3. Update ledger_gr10.json
  const ledgerPath = 'reports/full_archetype_audit/ledger_gr10.json';
  const ledger = JSON.parse(fs.readFileSync(ledgerPath, 'utf-8'));
  const target = ledger.archetypes.find(a => a.subject === subject && a.topic === topic && a.archetype_id === archetypeId);
  if (target) {
    target.unresolved_defects = defects;
    target.status = defects.length === 0 ? 'PASS' : 'FAIL';
    target.pre_scroll_screenshots = [prePath];
    target.memo_scroll_screenshots = [memoPath1, memoPath2];
    fs.writeFileSync(ledgerPath, JSON.stringify(ledger, null, 2));
    console.log('Successfully updated ledger_gr10.json! Status:', target.status);
  } else {
    console.error('Target archetype not found in ledger!');
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
