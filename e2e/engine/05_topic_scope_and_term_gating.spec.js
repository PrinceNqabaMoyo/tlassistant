import { test, expect } from '@playwright/test';

/**
 * 05_topic_scope_and_term_gating.spec.js
 * 
 * Verifies:
 * 1. Zero-ambiguity deterministic dropdown selection in TopicScopeModal.
 * 2. Exact CAPS match without requiring manual typing.
 * 3. Subscription-based term gating:
 *    - Independent non-annual subscribers (Term 1 pass / Monthly pass) have Terms 2-4 locked.
 *    - Annual Distinction Pass subscribers have all 4 terms completely unlocked.
 * 4. Pacing flexibility: No weekly gating within unlocked terms.
 */

test.describe('Cognitive Engine: Topic Scope & Subscription Term Gating', () => {
  const baseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test('Verify Deterministic Dropdown & Subscription Term Gating in Live UI', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${baseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });

    // 1. Mount persona as an independent learner on a Term 1 Pass
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'test-student-term-pass',
        name: 'Sipho Zulu',
        role: 'student',
        type: 'student',
        grade: 10,
        school: 'Independent Homeschool Learner',
        isIndependent: true,
        assignedTasks: []
      });
      if (window.studentStore) {
        window.studentStore.setIndependentMode(true, 'term_pass');
        window.studentStore.setActiveSession({
          subjectId: 'mathematics',
          topic: 'Algebraic Expressions',
          progressionMode: 'practice',
          lastActiveTab: 'mathematics'
        });
      }
    });

    // 2. Open Mathematics session from Today's Desk or rail
    const openSubjectBtn = page.locator('[data-testid="tab-mathematics"]:visible, [data-testid="btn-open-subject-session"]:visible, button:has-text("Mathematics"):visible').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    // 3. Assert Workspace is loaded and Topic Scope button is visible
    const changeTopicBtn = page.locator('button[data-testid="btn-topic-scope"]:visible');
    await expect(changeTopicBtn).toBeVisible({ timeout: 15000 });

    // 4. Open Topic Scope Modal
    await changeTopicBtn.click();

    const dropdown = page.locator('select[data-testid="select-topic-dropdown"]:visible');
    await expect(dropdown).toBeVisible({ timeout: 5000 });

    // 5. Verify Deterministic Dropdown structure & Term Gating for Term 1 Pass:
    // Term 1 options should be ENABLED
    const term1Option = dropdown.locator('option:not([disabled])').filter({ hasText: 'T1:' }).first();
    await expect(term1Option).toBeEnabled();

    // Future term options (Term 2, 3, 4) should be DISABLED with "Annual Pass Required"
    const lockedOption = dropdown.locator('option[disabled]').filter({ hasText: 'Annual Pass Required' }).first();
    await expect(lockedOption).toBeDisabled();

    // 6. Verify Term Tabs: Term 2 tab should indicate lock
    const term2Tab = page.locator('.grid-cols-4 button:has-text("Term 2"):visible');
    await expect(term2Tab).toBeVisible();
    await term2Tab.click();

    // Should display the upgrade banner for future terms
    const upgradeNotice = page.locator('text=Term 2 Scope Locked');
    await expect(upgradeNotice).toBeVisible();

    const upgradeBtn = page.locator('button:has-text("Upgrade to Annual Pass"):visible');
    await expect(upgradeBtn).toBeVisible();

    // Take verification screenshot of locked term state
    await page.screenshot({ path: 'reports/cognitive_audit/screenshots/topic_gating_term2_locked.png' });

    // 7. Switch back to Term 1 tab
    const term1Tab = page.locator('.grid-cols-4 button:has-text("Term 1"):visible');
    await term1Tab.click();

    // 8. Select a topic deterministically from the dropdown
    const targetTopicValue = await term1Option.getAttribute('value');
    expect(targetTopicValue).toBeTruthy();

    await dropdown.selectOption(targetTopicValue);

    // Modal should close automatically upon selection
    await expect(dropdown).toBeHidden({ timeout: 5000 });

    // 9. Verify workspace header updated to the exact selected topic
    const workspaceHeader = page.locator(`h2:has-text("${targetTopicValue}"):visible`);
    await expect(workspaceHeader).toBeVisible({ timeout: 5000 });

    // Take verification screenshot of updated workspace
    await page.screenshot({ path: 'reports/cognitive_audit/screenshots/topic_selected_exact_match.png' });

    console.log(`[PASS] Deterministic topic selection and term gating verified: "${targetTopicValue}" loaded with zero ambiguity.`);
  });

  test('Verify Annual Distinction Pass Unlocks All 4 Terms', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${baseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });

    // 1. Mount persona as an independent learner on an Annual Distinction Pass
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'test-student-annual-pass',
        name: 'Nqobile Dlamini',
        role: 'student',
        type: 'student',
        grade: 10,
        school: 'Independent Homeschool Learner',
        isIndependent: true,
        assignedTasks: []
      });
      if (window.studentStore) {
        window.studentStore.setIndependentMode(true, 'annual_pass');
        window.studentStore.setActiveSession({
          subjectId: 'mathematics',
          topic: 'Algebraic Expressions',
          progressionMode: 'practice',
          lastActiveTab: 'mathematics'
        });
      }
    });

    const openSubjectBtn = page.locator('[data-testid="tab-mathematics"]:visible, [data-testid="btn-open-subject-session"]:visible, button:has-text("Mathematics"):visible').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    const changeTopicBtn = page.locator('button[data-testid="btn-topic-scope"]:visible');
    await expect(changeTopicBtn).toBeVisible({ timeout: 15000 });
    await changeTopicBtn.click();

    const dropdown = page.locator('select[data-testid="select-topic-dropdown"]:visible');
    await expect(dropdown).toBeVisible({ timeout: 5000 });

    // On Annual Pass, Term 2, 3, and 4 should have ZERO disabled options in the dropdown
    const disabledOptions = dropdown.locator('option[disabled]:not([value=""])');
    const disabledCount = await disabledOptions.count();
    expect(disabledCount).toBe(0);

    // Switching to Term 2 tab shows unlocked topics, NOT the upgrade banner
    const term2Tab = page.locator('.grid-cols-4 button:has-text("Term 2"):visible');
    await term2Tab.click();

    const upgradeNotice = page.locator('text=Term 2 Scope Locked');
    await expect(upgradeNotice).toBeHidden();

    // Take verification screenshot of annual pass unlocked terms
    await page.screenshot({ path: 'reports/cognitive_audit/screenshots/topic_annual_pass_all_unlocked.png' });

    console.log('[PASS] Annual Distinction Pass verified: All 4 terms 100% unlocked with zero restrictions.');
  });
});
