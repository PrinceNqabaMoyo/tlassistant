import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:5173/?harness=universal_workspace');
  await page.waitForSelector('[data-testid="universal-workspace-harness-ready"]');

  // Set sample question
  await page.evaluate(() => {
    window.__SET_WORKSPACE_QUESTION__({
      id: "q_test_1",
      question_type: "short_answer",
      prompt: "Calculate: $125 \\times 4$",
      correct_answer: "500",
      worked_solution: "Step 1: Multiply 100 by 4 = 400. Step 2: Multiply 25 by 4 = 100. Step 3: 400 + 100 = 500.",
      marks: 2,
    }, { grade: '7', subject: 'Mathematics', topic: 'Whole Numbers' });
  });

  await page.waitForSelector('[data-testid="question-surface"]');
  console.log("Question surface visible!");

  // Click check button
  const checkBtn = await page.waitForSelector('[data-testid="btn-check-answer"]', { timeout: 5000 });
  await checkBtn.click();
  console.log("Check button clicked!");

  // Wait for memo button
  const memoBtn = await page.waitForSelector('[data-testid="btn-view-full-memo"]', { timeout: 5000 });
  console.log("Memo button visible, clicking it...");
  await memoBtn.click();

  // Wait for panel-full-memo
  const memoPanel = await page.waitForSelector('[data-testid="panel-full-memo"]', { timeout: 5000 });
  console.log("Memo panel visible:", !!memoPanel);

  // Check bounding box
  const box = await memoPanel.boundingBox();
  console.log("Memo panel bounding box:", box);

  await browser.close();
})().catch(err => {
  console.error("Test error:", err.message);
  process.exit(1);
});
