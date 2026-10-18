import { test, expect } from '@playwright/test';

/**
 * Student Today's Desk & Workspace Cockpit Button Audit
 * Strict Invariant Compliance:
 * - Rule 0d-3: Role-State Decoupling
 * - Rule 0d-4: Zero phantom selectors (all test-ids verified in StudentDashboard.jsx)
 * - Rule 0d-6: Zero silent skips (explicit expect assertions)
 */
test.describe('Student Cockpit: Today\'s Desk, Modals & Navigation Audits', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';
  const studentEmail = 'lesedi.khumalo@fundile.test';

  test('Student Cockpit: Today\'s Desk, Join Class & Link Guardian Modal Audits', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'sch-gr10-01',
        name: 'Lesedi Khumalo',
        role: 'student',
        type: 'student',
        grade: 10,
        school: 'Westville High School',
        assignedTasks: []
      });
    });

    // 1. Verify Today's Desk tab is present & active
    const deskTab = page.locator('[data-testid="tab-desk"]').first();
    await expect(deskTab).toBeVisible({ timeout: 15000 });
    await deskTab.click();

    // 2. Audit Quick Action Modals: Join Class Modal
    const joinClassBtn = page.locator('[data-testid="btn-open-join-class-modal"]').first();
    await expect(joinClassBtn).toBeVisible();
    await joinClassBtn.click();

    const joinCodeInput = page.locator('[data-testid="input-join-class-code"]');
    await expect(joinCodeInput).toBeVisible({ timeout: 10000 });

    const cancelJoinBtn = page.locator('[data-testid="btn-close-join-class"]').first();
    await expect(cancelJoinBtn).toBeVisible();
    await cancelJoinBtn.click();
    await expect(joinCodeInput).not.toBeVisible();

    // 3. Audit Link Guardian Modal
    const linkGuardianBtn = page.locator('[data-testid="btn-open-link-guardian-modal"]').first();
    await expect(linkGuardianBtn).toBeVisible();
    await linkGuardianBtn.click();

    // Close modal
    const closeGuardianBtn = page.locator('button:has-text("Done"), button:has-text("Close")').first();
    await expect(closeGuardianBtn).toBeVisible({ timeout: 10000 });
    await closeGuardianBtn.click();

    // 4. Audit Open Subject Session CTA
    const openSubjectBtn = page.locator('[data-testid="btn-open-subject-session"]').first();
    await expect(openSubjectBtn).toBeVisible();
    await expect(openSubjectBtn).toBeEnabled();
  });
});
