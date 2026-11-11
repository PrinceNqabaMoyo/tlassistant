import { chromium } from 'playwright';
import { spawnSync } from 'child_process';

function getQuestion(topic, subskill) {
  const py = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant
qs = generate_variant(topic=${JSON.stringify(topic)}, subskill=${JSON.stringify(subskill)}, grade='7', subject='Mathematics', seed=101, count=1)
print(json.dumps(qs[0]))
`;
  const res = spawnSync('.\\caps-ai-backend\\venv\\Scripts\\python.exe', ['-c', py], { encoding: 'utf-8' });
  return JSON.parse(res.stdout);
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('http://localhost:5173/?harness=universal_workspace');
  await page.waitForSelector('[data-testid="universal-workspace-harness-ready"]');
  
  for (const [topic, subskill] of [
    ['Integers', 'integers_in_context'],
    ['Exponents', 'solve_power_equation'],
    ['Surface area and volume of 3D objects', 'cylinder_net_surface_area']
  ]) {
    const q = getQuestion(topic, subskill);
    await page.evaluate(({ q, topic }) => {
      window.__SET_WORKSPACE_QUESTION__(q, { grade: '7', subject: 'Mathematics', topic });
    }, { q, topic });
    await page.waitForTimeout(300);
    const text = await page.locator('[data-testid="question-surface"]').innerText();
    const regex = /\\(frac|sqrt|text|begin|right|left)\{|\$\$/;
    const match = text.match(regex);
    console.log(`\n=== ${topic} / ${subskill} ===`);
    console.log('Match:', match ? match[0] : null);
    if (match) {
      const idx = text.indexOf(match[0]);
      console.log('Snippet around match:', JSON.stringify(text.slice(Math.max(0, idx - 40), idx + 60)));
    }
  }
  
  await browser.close();
})();
