import { chromium } from 'playwright';

async function testHarnessMount() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  page.on('console', msg => {
    if (msg.type() === 'error') console.log('[CONSOLE ERROR]:', msg.text());
  });
  page.on('pageerror', err => console.error('[PAGE ERROR]:', err.stack || err.message));

  console.log('Navigating to http://localhost:5173/?harness=universal_workspace...');
  await page.goto('http://localhost:5173/?harness=universal_workspace', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForSelector('[data-testid="universal-workspace-harness-ready"]', { state: 'visible', timeout: 15000 });
  console.log('Harness container mounted successfully!');

  // Set a test question
  const mockQ = {
    id: "test_q_1",
    question: "Calculate the value of $2x + 5$ when $x = 4$.",
    correct_answer: "13",
    sample_answer: "Substitute x = 4 into 2x + 5: 2(4) + 5 = 8 + 5 = 13.",
    marks: 2,
    modality: "math",
    marking_schema: {
      total_marks: 2,
      marking_points: [
        { id: "mp1", desc: "Substitution 2(4)", marks: 1 },
        { id: "mp2", desc: "Final calculation 13", marks: 1 }
      ]
    },
    hints: {
      tier_1: "Replace x with 4.",
      tier_2: "Perform multiplication first (BEDMAS).",
      tier_3: "2 * 4 = 8, then 8 + 5 = 13."
    }
  };

  const loaded = await page.evaluate((q) => {
    return window.__SET_WORKSPACE_QUESTION__(q, { grade: "7", subject: "Mathematics", topic: "Algebra" });
  }, mockQ);

  console.log('Question payload loaded into React state:', loaded);
  await page.waitForSelector('[data-testid="question-surface"]', { state: 'visible', timeout: 10000 });
  console.log('question-surface mounted in live DOM!');

  const promptText = await page.locator('[data-testid="question-surface"]').innerText();
  console.log('Mounted prompt text preview:\n', promptText.slice(0, 200));

  await browser.close();
  console.log('Harness verification PASS!');
}

testHarnessMount().catch(e => {
  console.error(e);
  process.exit(1);
});
