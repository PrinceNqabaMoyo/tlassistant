import { test, expect } from '@playwright/test';
import { authenticateSuperAdminSession } from '../helpers/authenticateSuperAdmin.js';

/**
 * Super Admin Cockpit Surface & Button Audit
 * Strict Invariant Compliance:
 * - Rule 0d-2: Platform Owner identity strictly used (princenqaba@gmail.com)
 * - Rule 0d-4: Zero phantom selectors (all test-ids verified in AdminForms.jsx and SuperAdminPanels.jsx)
 * - Rule 0d-6: Zero silent skips (explicit expect assertions)
 */
test.describe('Super Admin Cockpit: Navigation & Button Surface Integrity', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test('Super Admin Cockpit: Card Navigation & EFT Clearance Desk Audits', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await authenticateSuperAdminSession(page, targetBaseUrl);

    // Verify Admin Header / Dashboard Title
    const adminHeading = page.locator('text=Administrator Dashboard');
    await expect(adminHeading).toBeVisible({ timeout: 15000 });

    // 1. Audit Primary Cockpit Cards
    const manageUsersBtn = page.locator('button:has-text("Manage Users")').first();
    await expect(manageUsersBtn).toBeVisible();
    await expect(manageUsersBtn).toBeEnabled();

    const manageSubscribersBtn = page.locator('button:has-text("Manage Subscribers")').first();
    await expect(manageSubscribersBtn).toBeVisible();
    await expect(manageSubscribersBtn).toBeEnabled();

    const viewAnalyticsBtn = page.locator('button:has-text("View Analytics")').first();
    await expect(viewAnalyticsBtn).toBeVisible();
    await expect(viewAnalyticsBtn).toBeEnabled();

    // 2. Open EFT Payment Approvals Desk
    const reviewPaymentsBtn = page.locator('[data-testid="tab-admin-payments"]');
    await expect(reviewPaymentsBtn).toBeVisible();
    await expect(reviewPaymentsBtn).toBeEnabled();
    await reviewPaymentsBtn.click();

    // Verify EFT Approvals surface loaded
    const approvalsHeading = page.locator('h1:has-text("EFT Payment Approvals")');
    await expect(approvalsHeading).toBeVisible({ timeout: 10000 });

    // 3. Audit Filter Tabs
    const filterPending = page.locator('button:has-text("pending")').first();
    await expect(filterPending).toBeVisible();

    const filterApproved = page.locator('button:has-text("approved")').first();
    await expect(filterApproved).toBeVisible();
    await filterApproved.click();
    await page.locator('.animate-spin').waitFor({ state: 'detached', timeout: 10000 }).catch(() => {});

    const filterAll = page.locator('button:has-text("all")').first();
    await expect(filterAll).toBeVisible();
    await filterAll.click();
    await page.locator('.animate-spin').waitFor({ state: 'detached', timeout: 10000 }).catch(() => {});

    // 4. Return to Dashboard via Back button
    const backBtn = page.locator('button:has-text("Back to Dashboard")');
    await expect(backBtn).toBeVisible();
    await backBtn.click();

    // Confirm return to Admin Dashboard
    await expect(adminHeading).toBeVisible({ timeout: 10000 });
  });
});
