import { chromium } from 'playwright';
import { spawnSync } from 'child_process';

async function main() {
  const pyCode = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant
res = generate_variant(topic='Euclidean geometry', subskill='cyclic_quad_exterior', grade='11', subject='Mathematics', seed=101, count=1)
print(json.dumps(res[0]))
`;
  const pyRes = spawnSync('caps-ai-backend\\venv\\Scripts\\python.exe', ['-c', pyCode], { encoding: 'utf-8' });
  const q101 = JSON.parse(pyRes.stdout.trim());

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));

  await page.goto('http://localhost:5173/?harness=universal_workspace', { waitUntil: 'networkidle' });
  await page.waitForFunction(() => typeof window.__SET_WORKSPACE_QUESTION__ === 'function');

  console.log('Mounting question...');
  await page.evaluate(({ q }) => {
    return window.__SET_WORKSPACE_QUESTION__(q, { grade: '11', subject: 'Mathematics', topic: 'Euclidean geometry', mode: 'practice' });
  }, { q: q101 });

  try {
    await page.waitForSelector('[data-testid="question-surface"]', { state: 'visible', timeout: 5000 });
    console.log('SUCCESS: Mounted question-surface!');
  } catch (e) {
    console.error('FAILED TO MOUNT:', e.message);
  }

  await browser.close();
}

main();
