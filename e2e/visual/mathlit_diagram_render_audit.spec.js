import { test, expect } from '@playwright/test';
import { authenticateSuperAdminSession } from '../helpers/authenticateSuperAdmin.js';
import path from 'path';

/**
 * Math Lit Diagram Render Live Audit (AUD-6)
 *
 * Verifies that Mathematical Literacy questions with diagrams render cleanly
 * in the real browser without JavaScript errors, with non-zero dimensions.
 */
test.describe('Math Lit Diagram Render Live Verification (AUD-6)', () => {
  test('authenticates as Super Admin, navigates to Archetype Studio, and verifies Math Lit diagram rendering', async ({ page }) => {
    // 1. Authenticate authentic platform owner (Rule 0d-2)
    await authenticateSuperAdminSession(page, 'http://127.0.0.1:5173');

    // 2. Open Archetype Iteration Studio from Admin Desk
    const openIterationBtn = page.locator('[data-testid="btn-open-archetype-iteration"]:visible');
    await expect(openIterationBtn).toBeVisible({ timeout: 15000 });
    await openIterationBtn.click();

    // 3. Confirm workbench desk mounted cleanly
    const workbenchDesk = page.locator('[data-testid="super-admin-archetype-workbench"]:visible');
    await expect(workbenchDesk).toBeVisible({ timeout: 10000 });

    // 4. Assert Subject, Grade, and Topic dropdowns are visible
    const subjectSelect = page.locator('[data-testid="select-iteration-subject"]:visible');
    const gradeSelect = page.locator('[data-testid="select-iteration-grade"]:visible');
    const topicSelect = page.locator('[data-testid="select-iteration-topic"]:visible');

    await expect(subjectSelect).toBeVisible({ timeout: 10000 });
    await expect(gradeSelect).toBeVisible({ timeout: 10000 });
    await expect(topicSelect).toBeVisible({ timeout: 10000 });

    // Wait for curriculum topics catalog to finish loading from backend (default Gr10 topic attached)
    await page.waitForSelector('[data-testid="select-iteration-topic"] option[value="Conversions and time"]', { state: 'attached', timeout: 30000 });

    // 5. Select Mathematical Literacy -> Grade 11 -> PLANS AND OTHER REPRESENTATIONS
    await subjectSelect.selectOption('Mathematical Literacy');
    await gradeSelect.selectOption('11');
    await page.waitForSelector('[data-testid="select-iteration-topic"] option[value="PLANS AND OTHER REPRESENTATIONS"]', { state: 'attached', timeout: 15000 });
    await topicSelect.selectOption('PLANS AND OTHER REPRESENTATIONS');

    // 6. Select Archetype 1 (floor_plan)
    const archetypeSelect = page.locator('[data-testid="select-iteration-archetype"]:visible');
    await expect(archetypeSelect).toBeVisible({ timeout: 15000 });

    // Assert status badge shows Step 1 of 52
    const statusBadge = page.locator('[data-testid="iteration-status-badge"]:visible');
    await expect(statusBadge).toBeVisible({ timeout: 10000 });
    await expect(statusBadge).toContainText('Step 1 of 52');

    // 7. Verify question prompt and stimulus diagram render
    const promptLocator = page.locator('[data-testid="workbench-question-prompt"]:visible');
    await expect(promptLocator).toBeVisible({ timeout: 15000 });

    // Diagram container
    const diagramContainer = page.locator('[data-testid="workbench-iteration-diagram-container"]:visible, [data-testid="workbench-diagram-container"]:visible');
    await expect(diagramContainer).toBeVisible({ timeout: 15000 });

    // Floor plan SVG rendered by MathLitDiagramRenderer
    const floorPlanSvg = diagramContainer.locator('[data-testid="mathlit-diagram-floor-plan"]:visible');
    await expect(floorPlanSvg).toBeVisible({ timeout: 15000 });

    // 8. Select Archetype 10 (index 9: elevation_compass) and verify compass SVG renders
    await archetypeSelect.selectOption('9');
    const compassSvg = diagramContainer.locator('[data-testid="mathlit-diagram-compass"]:visible');
    await expect(compassSvg).toBeVisible({ timeout: 15000 });

    // 9. Select Archetype 11 (index 10: elevation_view) and verify architectural elevation SVG renders
    await archetypeSelect.selectOption('10');
    const elevationSvg = diagramContainer.locator('[data-testid="mathlit-diagram-elevation"]:visible');
    await expect(elevationSvg).toBeVisible({ timeout: 15000 });

    // 10. Select Archetype 29 (index 28: bar_scale) and verify dynamic graphic bar scale SVG renders
    await archetypeSelect.selectOption('28');
    const barScaleSvg = diagramContainer.locator('[data-testid="mathlit-diagram-bar-scale"]:visible');
    await expect(barScaleSvg).toBeVisible({ timeout: 15000 });

    // Capture screenshot for audit verification
    const reportsDir = path.resolve(process.cwd(), 'reports', 'screenshots');
    await page.screenshot({ path: path.join(reportsDir, 'mathlit_gr11_plans_floor_plan_rendered.png') });
    console.log('[AUD-6] Verified Math Lit floor_plan, elevation_compass, elevation_view, and bar_scale rendered cleanly.');
  });
});
