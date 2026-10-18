import { test, expect } from '@playwright/test';

/**
 * School Admin Cockpit Surface & Button Audit
 * Strict Invariant Compliance:
 * - Rule 0d-3: Role-State Decoupling (School Admin profile loaded cleanly)
 * - Rule 0d-4: Zero phantom selectors (all test-ids verified in SchoolAdminView.jsx)
 * - Rule 0d-6: Zero silent skips (explicit expect assertions)
 */
test.describe('School Admin Cockpit: Pacing, Faculty & SASAMS Ledger Audits', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';
  const schoolAdminEmail = 'dr.naidoo@westvillehigh.test';

  test('School Admin Cockpit: Tabs, ATP Pacing & SASAMS CSV Export Audit', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${targetBaseUrl}/#schoolAdmin`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'fac-01',
        name: 'Dr. V. Naidoo',
        title: 'Headmaster & Executive Principal',
        role: 'school',
        type: 'school',
        school: 'Westville High School',
        emis: '500124892'
      });
    });

    // 1. Verify School Admin Header
    const schoolHeading = page.locator('text=Westville High School').first();
    await expect(schoolHeading).toBeVisible({ timeout: 15000 });

    // 2. Audit Tab Switching: ATP Curriculum Pacing
    const pacingTab = page.locator('button:has-text("Curriculum Pacing")').first();
    await expect(pacingTab).toBeVisible();
    await pacingTab.click();

    // 3. Audit SASAMS Mark Ledger Tab
    const sasamsTab = page.locator('[data-testid="tab-school-sasams"]');
    await expect(sasamsTab).toBeVisible();
    await sasamsTab.click();

    // 4. Audit SASAMS Export Button
    const exportCsvBtn = page.locator('[data-testid="btn-export-sasams-csv"]');
    await expect(exportCsvBtn).toBeVisible();
    await expect(exportCsvBtn).toBeEnabled();

    // Trigger CSV export and verify download response
    const [download] = await Promise.all([
      page.waitForEvent('download'),
      exportCsvBtn.click()
    ]);
    const filename = download.suggestedFilename();
    expect(filename.toLowerCase()).toContain('sasams');
  });
});
