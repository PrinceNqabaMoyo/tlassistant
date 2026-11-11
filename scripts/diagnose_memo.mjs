import { chromium } from 'playwright';
import { spawnSync } from 'child_process';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:5173/?harness=universal_workspace');
  await page.waitForSelector('[data-testid="universal-workspace-harness-ready"]');

  const pyCode = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant
res = generate_variant('Integers', subskill='integers_ordering_number_line', grade='7', subject='Mathematics', seed=101, count=1)
print(json.dumps(res[0]))
`;
  const res = spawnSync('.\\caps-ai-backend\\venv\\Scripts\\python.exe', ['-c', pyCode], { encoding: 'utf-8' });
  const q = JSON.parse(res.stdout);

  await page.evaluate(({ q }) => window.__SET_WORKSPACE_QUESTION__(q, { grade: '7', subject: 'Mathematics', topic: 'Integers' }), { q });
  await page.waitForTimeout(300);

  const preH = await page.evaluate(() => document.documentElement.scrollHeight);
  console.log('Pre scrollHeight:', preH);

  await page.evaluate(() => window.__TRIGGER_WORKSPACE_MEMO__());
  await page.waitForTimeout(300);

  const memoBtn = await page.$('[data-testid="btn-view-full-memo"]');
  console.log('Memo button found:', !!memoBtn);
  if (memoBtn) {
    await memoBtn.click();
    await page.waitForTimeout(300);
  }

  const memoH = await page.evaluate(() => document.documentElement.scrollHeight);
  console.log('Memo scrollHeight:', memoH);

  const memoPanel = await page.$('[data-testid="panel-full-memo"]');
  console.log('Memo panel found:', !!memoPanel);

  if (memoPanel) {
    const box = await memoPanel.boundingBox();
    console.log('Memo panel boundingBox:', box);
  }

  await browser.close();
})().catch(e => {
  console.error('Diagnostic error:', e);
  process.exit(1);
});
