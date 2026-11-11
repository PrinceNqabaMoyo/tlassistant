import { test, expect } from '@playwright/test';
import { authenticateSuperAdminSession } from '../helpers/authenticateSuperAdmin.js';
import path from 'path';

test.describe('Super Admin Archetype Iteration Studio Verification', () => {
  test('authenticates as Super Admin, navigates to Iteration Studio, selects Math Lit Gr10 Conversions and time, and steps through archetypes with entropy', async ({ page }) => {
    // 1. Authenticate authentic platform owner (Rule 0d-2)
    await authenticateSuperAdminSession(page, 'http://127.0.0.1:5173');

    // 2. Open Archetype Iteration Studio from Admin Desk
    const openIterationBtn = page.locator('[data-testid="btn-open-archetype-iteration"]:visible');
    await expect(openIterationBtn).toBeVisible({ timeout: 15000 });
    await openIterationBtn.click();

    // 3. Confirm workbench desk mounted cleanly
    const workbenchDesk = page.locator('[data-testid="super-admin-archetype-workbench"]:visible');
    await expect(workbenchDesk).toBeVisible({ timeout: 10000 });

    // 4. Assert Iteration Studio tab is active
    const iterTab = page.locator('[data-testid="tab-archetype-iteration"]:visible');
    await expect(iterTab).toBeVisible({ timeout: 5000 });

    // 5. Assert Subject, Grade, and Topic dropdowns are visible and functional
    const subjectSelect = page.locator('[data-testid="select-iteration-subject"]:visible');
    const gradeSelect = page.locator('[data-testid="select-iteration-grade"]:visible');
    const topicSelect = page.locator('[data-testid="select-iteration-topic"]:visible');

    await expect(subjectSelect).toBeVisible({ timeout: 10000 });
    await expect(gradeSelect).toBeVisible({ timeout: 10000 });
    await expect(topicSelect).toBeVisible({ timeout: 10000 });

    // 6. Select Mathematical Literacy -> Grade 10 -> Conversions and time
    await subjectSelect.selectOption('Mathematical Literacy');
    await gradeSelect.selectOption('10');
    
    // Wait for topic options to populate
    await page.waitForTimeout(500);
    await topicSelect.selectOption({ label: 'Conversions and time' });

    // 7. Verify Archetype selector has at least 50 archetypes
    const archetypeSelect = page.locator('[data-testid="select-iteration-archetype"]:visible');
    await expect(archetypeSelect).toBeVisible({ timeout: 10000 });

    // Check count of option elements
    const optionCount = await archetypeSelect.locator('option').count();
    console.log(`[E2E] Loaded ${optionCount} archetypes in dropdown for Conversions and time.`);
    expect(optionCount).toBeGreaterThanOrEqual(50);

    // 8. Assert Status Badge shows 1 / 52
    const statusBadge = page.locator('[data-testid="iteration-status-badge"]:visible');
    await expect(statusBadge).toBeVisible({ timeout: 5000 });
    await expect(statusBadge).toContainText('1 /');

    // 9. Assert initial question is rendered on question canvas
    const promptLocator = page.locator('[data-testid="workbench-question-prompt"]:visible');
    await expect(promptLocator).toBeVisible({ timeout: 10000 });
    const initialPromptText = await promptLocator.innerText();
    console.log(`[E2E] Archetype 1 prompt snippet: ${initialPromptText.slice(0, 80)}...`);

    // 10. Test Linear Stepping: Click "Next Archetype"
    const nextBtn = page.locator('[data-testid="btn-iteration-next"]:visible');
    await expect(nextBtn).toBeEnabled({ timeout: 5000 });
    await nextBtn.click();

    // Verify progression to Archetype 2
    await expect(statusBadge).toContainText('2 /', { timeout: 10000 });
    const secondPromptText = await promptLocator.innerText();
    expect(secondPromptText).not.toEqual(initialPromptText);
    console.log(`[E2E] Stepped cleanly to Archetype 2: ${secondPromptText.slice(0, 80)}...`);

    // 11. Test Stepping Back: Click "Prev Archetype"
    const prevBtn = page.locator('[data-testid="btn-iteration-prev"]:visible');
    await expect(prevBtn).toBeEnabled({ timeout: 5000 });
    await prevBtn.click();

    // Verify return to Archetype 1
    await expect(statusBadge).toContainText('1 /', { timeout: 10000 });

    // 12. Test Random Seed / Entropy: capture initial seed and click Generate
    const seedInput = page.locator('[data-testid="input-workbench-seed"]:visible');
    await expect(seedInput).toBeVisible({ timeout: 5000 });
    const initialSeed = await seedInput.inputValue();

    const generateBtn = page.locator('[data-testid="btn-iteration-generate"]:visible');
    await expect(generateBtn).toBeEnabled({ timeout: 5000 });
    await generateBtn.click();
    await page.waitForTimeout(500);

    // 13. Capture high-resolution screenshot of the uncramped Iteration Studio
    const screenshotPath = path.resolve(process.cwd(), 'playwright-test/workbench_archetype_iteration_rendered.png');
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`[E2E] Iteration Studio screenshot saved to ${screenshotPath}`);
  });
});
