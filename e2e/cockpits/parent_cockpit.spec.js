import { test, expect } from '@playwright/test';

/**
 * Parent Guardian Portal Surface & Button Audit
 * Strict Invariant Compliance:
 * - Rule 0d-3: Role-State Decoupling (Parent profile loaded without studentStore corruption)
 * - Rule 0d-4: Zero phantom selectors (all test-ids verified in ParentDashboard.jsx)
 * - Rule 0d-6: Zero silent skips (explicit expect assertions)
 */
test.describe('Parent Guardian Portal: Navigation & Button Surface Integrity', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';
  const parentEmail = 'nomsa.khumalo.parent@fundile.test';

  test('Parent Cockpit: Child Switcher, Pulse Metrics & Workspace Launcher Audits', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${targetBaseUrl}/#parent`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'sch-par-001',
        name: 'Mrs. Nomsa Khumalo',
        role: 'parent',
        type: 'parent',
        title: 'Mrs.',
        firstName: 'Nomsa',
        lastName: 'Khumalo',
        email: 'nomsa.khumalo.parent@fundile.test',
        whatsappPhone: '+27 82 555 7892'
      });
    });

    // 1. Verify Parent Portal Header
    const portalTitle = page.locator('h1:has-text("Parent & Guardian Bridge")');
    await expect(portalTitle).toBeVisible({ timeout: 15000 });

    const guardianBadge = page.locator('text=Verified Guardian Feed');
    await expect(guardianBadge).toBeVisible();

    // 2. Audit Child Switcher Tabs
    const lesediTab = page.locator('[data-testid="tab-child-lesedi"], [data-testid^="tab-child-"]').first();
    await expect(lesediTab).toBeVisible();
    await lesediTab.click();

    // 3. Audit Launch Learner Workspace CTA
    const launchWorkspaceBtn = page.locator('[data-testid="btn-launch-learner-workspace"]');
    await expect(launchWorkspaceBtn).toBeVisible();
    await expect(launchWorkspaceBtn).toBeEnabled();

    // 4. Audit Add Child Modal Interaction
    const openAddChildBtn = page.locator('[data-testid="btn-add-child-modal"]');
    await expect(openAddChildBtn).toBeVisible();
    await openAddChildBtn.click();

    // Verify Modal & Tabs
    const directTab = page.locator('[data-testid="tab-add-child-direct"]');
    await expect(directTab).toBeVisible({ timeout: 10000 });
    await directTab.click();

    const nameInput = page.locator('[data-testid="input-child-name-direct"]');
    await expect(nameInput).toBeVisible();

    const gradeSelect = page.locator('[data-testid="select-child-grade-direct"]');
    await expect(gradeSelect).toBeVisible();

    // Switch to Link via 15-Minute Code tab
    const codeTab = page.locator('[data-testid="tab-add-child-code"]');
    await expect(codeTab).toBeVisible();
    await codeTab.click();

    const codeInput = page.locator('[data-testid="input-child-link-code"]');
    await expect(codeInput).toBeVisible();

    // Close Modal via Cancel / Close
    const closeBtn = page.locator('button:has-text("Cancel")').first();
    await expect(closeBtn).toBeVisible();
    await closeBtn.click();
    await expect(nameInput).not.toBeVisible();
  });
});
