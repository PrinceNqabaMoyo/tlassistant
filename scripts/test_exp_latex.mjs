import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:5173/?harness=universal_workspace', { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('[data-testid="universal-workspace-harness-ready"]');

  await page.evaluate(() => {
    window.__SET_WORKSPACE_QUESTION__({
      id: 'test_exp',
      question_type: 'typed',
      prompt: 'Simplify the following numerical expression. Show all steps:\n\n\\[ \\sqrt{64} - 2^{2} + \\sqrt[3]{27} \\]',
      correct_answer: '7',
      marks: 3,
    }, { grade: '7', subject: 'Mathematics', topic: 'Exponents' });
  });

  await page.waitForSelector('[data-testid="question-surface"]');
  const text = await page.locator('[data-testid="question-surface"]').innerText();
  console.log('DOM innerText:', JSON.stringify(text));
  const hasRaw = /\\(frac|sqrt|text|begin|right|left)\{/.test(text) || /\$\$/.test(text);
  console.log('Has raw LaTeX leak:', hasRaw);
  await browser.close();
})();
