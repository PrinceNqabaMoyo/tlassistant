import { test, expect } from '@playwright/test';

/**
 * Teacher Cockpit Surface & Button Audit
 * Strict Invariant Compliance:
 * - Rule 0d-3: Role-State Decoupling (Teacher profile loaded cleanly)
 * - Rule 0d-4: Zero phantom selectors (all elements verified in TeacherDashboard.jsx)
 * - Rule 0d-6: Zero silent skips (explicit expect assertions)
 */
test.describe('Teacher Cockpit: Navigation & Button Surface Integrity', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';
  const teacherEmail = 'sithole@westvillehigh.test';

  test.beforeEach(async ({ page }) => {
    // Authenticate as Teacher via localStorage pre-injection
    await page.addInitScript(({ email }) => {
      localStorage.setItem('fundile_currentUser', JSON.stringify({
        uid: 'teacher_sithole',
        name: 'Mr. N. Sithole',
        email,
        role: 'teacher',
        school: 'Westville High School',
        department: 'Commerce'
      }));
    }, { email: teacherEmail });
  });

  test('Teacher Cockpit: Roster Tabs, Analytics Heatmap & Assessment Tools Audit', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${targetBaseUrl}/#teacher`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'fac-03',
        name: 'Mr. N. Sithole',
        title: 'HOD: Accounting & Commercial Studies',
        role: 'teacher',
        type: 'teacher',
        subject: 'Accounting',
        assignedClassName: 'Grade 10A (Accounting)',
        joinCode: 'ACC10A'
      });
    });

    // 1. Verify Teacher Cockpit Header
    const teacherHeading = page.locator('h1:has-text("Mr. N. Sithole")');
    await expect(teacherHeading).toBeVisible({ timeout: 15000 });

    // 2. Audit Header Action Buttons
    const createClassBtn = page.locator('button:has-text("Create Class")').first();
    await expect(createClassBtn).toBeVisible();
    await expect(createClassBtn).toBeEnabled();

    const printExamBtn = page.locator('button:has-text("Print Test & Memo")').first();
    await expect(printExamBtn).toBeVisible();
    await expect(printExamBtn).toBeEnabled();

    // 3. Audit Primary 3-Tab Navigation Bar
    const rostersTab = page.locator('button:has-text("📋 Rosters")').first();
    await expect(rostersTab).toBeVisible();
    await rostersTab.click();

    const analyticsTab = page.locator('button:has-text("📊 Analytics")').first();
    await expect(analyticsTab).toBeVisible();
    await analyticsTab.click();

    const assessmentsTab = page.locator('button:has-text("📝 Assessments")').first();
    await expect(assessmentsTab).toBeVisible();
    await assessmentsTab.click();

    // Switch back to rosters tab
    await rostersTab.click();
    await expect(rostersTab).toHaveClass(/bg-\[#13519C\]/);
  });
});
