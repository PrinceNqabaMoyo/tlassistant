// Render-level leak check (Rule 0d-7: executes the real UI, reads real DOM text).
// Mounts live generator output in UniversalWorkspaceHarness, then scans the rendered
// question card and memo for leaked markup. Requires a server on 127.0.0.1:5173.
// Usage: node scripts/render_leak_check.js
import { chromium } from 'playwright';
import fs from 'fs';
import { spawnSync } from 'child_process';

const CASES = [
  ['Mathematics', '7', 'Algebraic expressions 1'],
  ['Mathematics', '7', 'The decimal notation for fractions'],
  ['Mathematics', '8', 'Algebraic equations 1'],
  ['Mathematics', '8', 'Common fractions'],
  ['Mathematics', '8', 'Fractions in decimal notation'],
  ['Mathematics', '8', 'Surface area and volume of 3D objects'],
  ['Mathematics', '8', 'Geometry of 2D shapes'],
  ['Mathematics', '8', 'Geometry of straight lines'],
  ['Mathematics', '9', 'Equations 1'],
  ['Mathematical Literacy', '10', 'Conversions and time'],
  ['Natural Sciences', '8', 'Photosynthesis and respiration'],
  ['Natural Sciences', '8', 'Chemical reactions'],
  ['EMS', '8', '@journal'], // '@' prefix = every Gr8 EMS manifest topic containing the word
];
const SEEDS = [42, 101];

const PY = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant
cases = json.loads(sys.argv[1]); seeds = json.loads(sys.argv[2])
manifest = json.load(open('caps-ai-backend/app/services/caps_term_registry_data.json', encoding='utf-8'))
rows = manifest if isinstance(manifest, list) else manifest.get('topics') or manifest.get('entries') or []
out = []
for subject, grade, topic in cases:
    names = [topic]
    if topic.startswith('@'):
        w = topic[1:].lower()
        names = sorted({r['name'] for r in rows if isinstance(r, dict) and str(r.get('grade')) == grade
                        and r.get('subject') == subject and w in str(r.get('name', '')).lower()})
    for name in names:
        for seed in seeds:
            try:
                for q in generate_variant(name, seed=seed, count=1, grade=grade, subject=subject):
                    out.append({'subject': subject, 'grade': grade, 'topic': name, 'seed': seed, 'q': q})
            except Exception as e:
                out.append({'subject': subject, 'grade': grade, 'topic': name, 'seed': seed, 'error': str(e)[:200]})
print(json.dumps(out, ensure_ascii=True))
`;

const PATTERNS = {
  literal_asterisks: /\*\*/,
  literal_double_backslash: /\\\\/,
  literal_backslash_n: /\\n/,
  ss_marker: /SS\s*\[/,
  raw_dollar_math: /\$\$|\\\(|\\\)/,
  raw_latex_command: /\\(frac|text|begin|end|hline|times|dfrac|sqrt)\b/,
  js_token: /\b(undefined|NaN)\b|\[object Object\]/,
};

function snippet(text, rx) {
  const m = rx.exec(text);
  if (!m) return null;
  return text.slice(Math.max(0, m.index - 40), m.index + 60).replace(/\n/g, ' / ');
}

async function main() {
  const py = spawnSync('python', ['-c', PY, JSON.stringify(CASES), JSON.stringify(SEEDS)], {
    encoding: 'utf-8', maxBuffer: 64 * 1024 * 1024,
  });
  if (py.status !== 0) { console.error(py.stderr); process.exit(1); }
  const items = JSON.parse(py.stdout.trim());
  console.log(`Generated ${items.length} items`);

  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  const consoleErrors = [];
  page.on('console', (m) => {
    if (m.type() === 'error') console.log('[BROWSER CONSOLE ERROR]:', m.text());
  });
  page.on('pageerror', (e) => console.error('[BROWSER PAGE ERROR]:', e));

  await page.goto('http://127.0.0.1:5173/?harness=universal_workspace', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForFunction(() => typeof window.__SET_WORKSPACE_QUESTION__ === 'function', null, { timeout: 30000 });

  const results = [];
  for (const it of items) {
    if (it.error) { results.push({ ...it, hits: { generator_error: it.error } }); continue; }
    console.log(`Mounting: Gr${it.grade} ${it.subject} / ${it.topic} (seed ${it.seed})...`);
    const setRes = await page.evaluate(({ q, meta }) => {
      try {
        return window.__SET_WORKSPACE_QUESTION__(q, meta);
      } catch (err) {
        return { error: String(err) };
      }
    }, { q: it.q, meta: { grade: it.grade, subject: it.subject, topic: it.topic, mode: 'practice' } });
    if (setRes && setRes.error) {
      console.error('SET_WORKSPACE_QUESTION error:', setRes.error);
    }
    const surface = page.locator('[data-testid="question-surface"]');
    try {
      await surface.waitFor({ state: 'visible', timeout: 10000 });
    } catch (err) {
      const harnessText = await page.locator('[data-testid="universal-workspace-harness-ready"]').innerText().catch(() => 'no harness');
      console.error(`Surface wait failed for Gr${it.grade} ${it.topic}. Harness text:\n`, harnessText.slice(0, 300));
      throw err;
    }
    const questionText = await surface.innerText();
    const bodyBefore = await page.locator('body').innerText();
    await page.evaluate(() => window.__TRIGGER_WORKSPACE_MEMO__());
    await page.waitForTimeout(400);
    const bodyAfter = await page.locator('body').innerText();
    const memoText = bodyAfter.startsWith(bodyBefore.slice(0, 200)) ? bodyAfter.replace(bodyBefore, '') : bodyAfter;
    const hits = {};
    for (const [name, rx] of Object.entries(PATTERNS)) {
      const q = snippet(questionText, rx);
      const m = snippet(memoText, rx);
      if (q) hits[`question:${name}`] = q;
      if (m) hits[`memo:${name}`] = m;
    }
    results.push({ subject: it.subject, grade: it.grade, topic: it.topic, seed: it.seed, hits });
  }
  await browser.close();

  fs.mkdirSync('reports', { recursive: true });
  fs.writeFileSync('reports/render_leak_check.json', JSON.stringify({ consoleErrors, results }, null, 1));
  const failing = results.filter((r) => Object.keys(r.hits).length);
  console.log(`Rendered ${results.length} items; ${failing.length} with leaks; console errors: ${consoleErrors.length}`);
  const byKey = {};
  for (const r of failing) for (const k of Object.keys(r.hits)) {
    const id = `Gr${r.grade} ${r.topic} :: ${k}`;
    byKey[id] = byKey[id] || r.hits[k];
  }
  for (const [k, v] of Object.entries(byKey)) console.log(`- ${k} | ${v}`);
  process.exit(failing.length ? 1 : 0);
}

main().catch((e) => { console.error(e); process.exit(1); });
