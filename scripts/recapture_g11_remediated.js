import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { spawnSync } from 'child_process';

const TARGETS = [
  { subject: 'Business Studies', topic: 'The marketing function', archetypeId: 'concepts' },
  { subject: 'Business Studies', topic: 'The marketing function', archetypeId: 'the_marketing_function_subskill_4' },
  { subject: 'Business Studies', topic: 'The marketing function', archetypeId: 'the_marketing_function_subskill_5' },
  { subject: 'Mathematics', topic: 'Exponents and surds', archetypeId: 'rational_exponent_to_radical' },
  { subject: 'Mathematics', topic: 'Euclidean geometry', archetypeId: 'cyclic_quad_exterior' },
  { subject: 'Technical Mathematics', topic: 'Exponents and surds', archetypeId: 'rational_exponent_to_radical' },
  { subject: 'Technical Mathematics', topic: 'Logarithms', archetypeId: 'rational_exponent_to_radical' }
];

function sanitizeSlug(str) {
  return String(str || '').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
}

async function main() {
  const grade = '11';
  const browser = await chromium.launch({ headless: true });

  const ledgerPath = 'reports/full_archetype_audit/ledger_gr11.json';
  const ledger = JSON.parse(fs.readFileSync(ledgerPath, 'utf-8'));

  for (const t of TARGETS) {
    const { subject, topic, archetypeId } = t;
    console.log(`\nRecapturing: ${subject} | ${topic} | ${archetypeId}`);

    // Generate question via python generator_registry
    const pyCode = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant
res = generate_variant(topic=${JSON.stringify(topic)}, subskill=${JSON.stringify(archetypeId)}, grade='11', subject=${JSON.stringify(subject)}, seed=101, count=1)
print(json.dumps(res[0]))
`;
    const pyRes = spawnSync('caps-ai-backend\\venv\\Scripts\\python.exe', ['-c', pyCode], { encoding: 'utf-8' });
    if (pyRes.status !== 0) {
      console.error('Python error:', pyRes.stderr);
      continue;
    }
    const q101 = JSON.parse(pyRes.stdout.trim());

    // Fresh page per target
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
    const page = await context.newPage();

    await page.goto('http://localhost:5173/?harness=universal_workspace', { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForFunction(() => typeof window.__SET_WORKSPACE_QUESTION__ === 'function', { timeout: 15000 });

    // Mount in workspace
    await page.evaluate(({ q, grade, subject, topic }) => {
      return window.__SET_WORKSPACE_QUESTION__(q, { grade, subject, topic, mode: 'practice' });
    }, { q: q101, grade, subject, topic });

    await page.waitForSelector('[data-testid="question-surface"]', { state: 'visible', timeout: 10000 });
    await page.waitForTimeout(200);

    const basePrefix = `gr11_${sanitizeSlug(subject)}_${sanitizeSlug(topic)}_${sanitizeSlug(archetypeId)}`;

    // Full multi-scroll pre-capture
    const preScrollHeight = await page.evaluate(() => Math.max(document.body.scrollHeight, document.documentElement.scrollHeight));
    const preCount = Math.max(1, Math.ceil(preScrollHeight / 900));
    const preShots = [];
    for (let s = 0; s < preCount; s++) {
      await page.evaluate((top) => window.scrollTo(0, top), s * 900);
      await page.waitForTimeout(100);
      const shotPath = `reports/full_archetype_audit/shots/${basePrefix}_pre_scroll_${s + 1}.png`;
      await page.screenshot({ path: shotPath, fullPage: false });
      preShots.push(shotPath);
    }

    const preDomText = await page.locator('[data-testid="question-surface"]').innerText();

    const defects = [];
    const ansRaw = String(q101.correct_answer || q101.sample_answer || '').trim();
    if (ansRaw.length >= 3 && !/^(true|false|[a-d]|yes|no)$/i.test(ansRaw)) {
      const promptOnly = String(q101.question || q101.prompt || q101.question_text || '');
      const regex = new RegExp(`\\b${ansRaw.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')}\\b`, 'i');
      if (regex.test(promptOnly)) {
        defects.push(`[ANSWER_LEAK] Final answer '${ansRaw}' appears verbatim in question prompt.`);
      }
    }

    if (/\\(frac|sqrt|text|begin|right|left)\{/.test(preDomText) || /\$\$/.test(preDomText)) {
      defects.push(`[RAW_LATEX_LEAK] Raw LaTeX tokens found in rendered student prompt.`);
    }
    if (/\b(undefined|NaN)\b|\[object Object\]/.test(preDomText)) {
      defects.push(`[JS_TOKEN_LEAK] Page contains undefined/NaN/[object Object].`);
    }
    if (/\bCAPS\b/.test(preDomText)) {
      defects.push(`[BANNED_CAPS_ACRONYM] Prompt displays banned 'CAPS' acronym.`);
    }

    // Trigger memo
    await page.evaluate(() => {
      if (typeof window.__TRIGGER_WORKSPACE_MEMO__ === 'function') {
        window.__TRIGGER_WORKSPACE_MEMO__();
      }
    });
    await page.waitForTimeout(200);

    // Full multi-scroll memo-capture
    const memoScrollHeight = await page.evaluate(() => Math.max(document.body.scrollHeight, document.documentElement.scrollHeight));
    const memoCount = Math.max(1, Math.ceil(memoScrollHeight / 900));
    const memoShots = [];
    for (let s = 0; s < memoCount; s++) {
      await page.evaluate((top) => window.scrollTo(0, top), s * 900);
      await page.waitForTimeout(100);
      const shotPath = `reports/full_archetype_audit/shots/${basePrefix}_memo_scroll_${s + 1}.png`;
      await page.screenshot({ path: shotPath, fullPage: false });
      memoShots.push(shotPath);
    }

    console.log(`Pre: ${preShots.length} shots (${preScrollHeight}px), Memo: ${memoShots.length} shots (${memoScrollHeight}px), Defects:`, defects);

    // Update target in ledger
    const target = ledger.archetypes.find(a => a.subject === subject && a.topic === topic && a.archetype_id === archetypeId);
    if (target) {
      target.unresolved_defects = defects;
      target.status = defects.length === 0 ? 'PASS' : 'FAIL';
      target.pre_scroll_height = preScrollHeight;
      target.pre_scroll_screenshots = preShots;
      target.memo_scroll_height = memoScrollHeight;
      target.memo_scroll_screenshots = memoShots;
    }

    await context.close();
  }

  fs.writeFileSync(ledgerPath, JSON.stringify(ledger, null, 2));
  console.log('\nUpdated ledger_gr11.json successfully!');
  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
