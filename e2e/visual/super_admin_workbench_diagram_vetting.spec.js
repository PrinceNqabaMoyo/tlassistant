import { test, expect } from '@playwright/test';
import { authenticateSuperAdminSession } from '../helpers/authenticateSuperAdmin.js';
import path from 'path';

test.describe('Super Admin Archetype & Diagram Vetting Workbench Live Verification', () => {
  test('authenticates as Super Admin, generates NS9_HEART_CHAMBERS, and renders authentic heart diagram with calibrated pins', async ({ page }) => {
    // 1. Authenticate authentic platform owner (Rule 0d-2)
    await authenticateSuperAdminSession(page, 'http://127.0.0.1:5173');

    // 2. Open Archetype & Diagram Vetting Workbench from Admin Desk
    const openWorkbenchBtn = page.locator('[data-testid="btn-open-vetting-workbench"]:visible');
    await expect(openWorkbenchBtn).toBeVisible({ timeout: 15000 });
    await openWorkbenchBtn.click();

    // 3. Confirm workbench desk mounted cleanly
    const workbenchDesk = page.locator('[data-testid="super-admin-archetype-workbench"]:visible');
    await expect(workbenchDesk).toBeVisible({ timeout: 10000 });

    // 4. Select NS9_HEART_CHAMBERS from archetype catalogue
    const heartArchetypeBtn = page.locator('[data-testid="archetype-item-NS9_HEART_CHAMBERS"]:visible');
    await expect(heartArchetypeBtn).toBeVisible({ timeout: 10000 });
    await heartArchetypeBtn.click();

    // 5. Generate question on Seed 1
    const generateBtn = page.locator('[data-testid="btn-vet-generate"]:visible');
    await expect(generateBtn).toBeEnabled({ timeout: 5000 });
    await generateBtn.click();

    // 6. Assert Diagram Container is NOT empty
    const diagramContainer = page.locator('[data-testid="workbench-diagram-container"]:visible');
    await expect(diagramContainer).toBeVisible({ timeout: 15000 });

    // 7. Assert Banked Diagram Container is mounted
    const bankedContainer = page.locator('[data-testid="banked-diagram-container"]:visible');
    await expect(bankedContainer).toBeVisible({ timeout: 10000 });

    // 8. Assert Heart Locked View Badge is visible
    const lockedBadge = page.locator('[data-testid="heart-locked-view-badge"]:visible');
    await expect(lockedBadge).toBeVisible({ timeout: 5000 });
    await expect(lockedBadge).toContainText('Textbook Coronal Cross-Section');

    // 9. Assert SVG with textbook master image is rendered
    const textbookImage = diagramContainer.locator('image[href*="generated_textbook_heart_coronal.jpg"]');
    await expect(textbookImage).toBeVisible({ timeout: 5000 });

    // 10. Assert interactive callout pins and landmarks
    const pinA = diagramContainer.locator('text:has-text("A")');
    const pinB = diagramContainer.locator('text:has-text("B")');
    await expect(pinA.first()).toBeVisible({ timeout: 5000 });
    await expect(pinB.first()).toBeVisible({ timeout: 5000 });

    const landmarkIVC = diagramContainer.locator('text:has-text("Inferior Vena Cava")');
    await expect(landmarkIVC.first()).toBeVisible({ timeout: 5000 });

    // 11. Capture high-resolution screenshot for visual inspection
    const screenshotPath = path.resolve(process.cwd(), 'playwright-test/workbench_heart_diagram_rendered.png');
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`[E2E] Screenshot saved to ${screenshotPath}`);

    // 12. Test Multi-View Mode toggle
    const toggleViewModeBtn = page.locator('[data-testid="btn-toggle-workbench-view-mode"]:visible');
    await expect(toggleViewModeBtn).toBeVisible({ timeout: 5000 });
    await toggleViewModeBtn.click();

    // Switch to Exam Line-Art View
    const examViewBtn = page.locator('[data-testid="btn-view-exam"]:visible');
    await expect(examViewBtn).toBeVisible({ timeout: 5000 });
    await examViewBtn.click();

    // Assert Exam stipple image rendered
    const examStippleImage = diagramContainer.locator('image[href*="generated_exam_heart_stipple.jpg"]');
    await expect(examStippleImage).toBeVisible({ timeout: 5000 });
    console.log('[E2E] Verified multi-view toggle to exam stipple view!');
  });

  test('filters by Grade 7, verifies 7 archetypes in catalogue, and renders NS7_SOLAR_SYSTEM_ORBITS and MATH7_TRIANGLE_INTERIOR_ANGLES', async ({ page }) => {
    // 1. Authenticate authentic platform owner (Rule 0d-2)
    await authenticateSuperAdminSession(page, 'http://127.0.0.1:5173');

    // 2. Open Archetype & Diagram Vetting Workbench from Admin Desk
    const openWorkbenchBtn = page.locator('[data-testid="btn-open-vetting-workbench"]:visible');
    await expect(openWorkbenchBtn).toBeVisible({ timeout: 15000 });
    await openWorkbenchBtn.click();

    // 3. Confirm workbench desk mounted cleanly
    const workbenchDesk = page.locator('[data-testid="super-admin-archetype-workbench"]:visible');
    await expect(workbenchDesk).toBeVisible({ timeout: 10000 });

    // 4. Click Grade 7 Filter button
    const grade7Btn = page.locator('[data-testid="btn-workbench-grade-7"]:visible');
    await expect(grade7Btn).toBeVisible({ timeout: 5000 });
    await grade7Btn.click();

    // 5. Assert all 7 Grade 7 archetypes are visible in the catalogue
    const gr7Archetypes = [
      'NS7_DISTILLATION_GLASSWARE',
      'NS7_SOLAR_SYSTEM_ORBITS',
      'MATH7_CYLINDER_NET',
      'MATH7_CUBE_NET',
      'MATH7_TRIANGULAR_PRISM_NET',
      'MATH7_TRIANGLE_INTERIOR_ANGLES',
      'MATH7_QUADRILATERAL_INTERIOR_ANGLES'
    ];

    for (const aId of gr7Archetypes) {
      const archItem = page.locator(`[data-testid="archetype-item-${aId}"]:visible`);
      await expect(archItem).toBeVisible({ timeout: 5000 });
    }
    console.log('[E2E] All 7 Grade 7 archetypes verified visible in catalogue!');

    // 6. Test NS7_SOLAR_SYSTEM_ORBITS generation & diagram render
    const solarArchBtn = page.locator('[data-testid="archetype-item-NS7_SOLAR_SYSTEM_ORBITS"]:visible');
    await solarArchBtn.scrollIntoViewIfNeeded();
    await solarArchBtn.click();

    const generateBtn = page.locator('[data-testid="btn-vet-generate"]:visible');
    await expect(generateBtn).toContainText('NS7_SOLAR_SYSTEM_ORBITS', { timeout: 10000 });

    const diagramContainer = page.locator('[data-testid="workbench-diagram-container"]:visible');
    await expect(diagramContainer).toBeVisible({ timeout: 15000 });

    const solarCanvas = diagramContainer.locator('[data-testid="solar-system-earth-space-canvas"]:visible');
    await expect(solarCanvas).toBeVisible({ timeout: 15000 });

    const solarImage = diagramContainer.locator('image[href*="solar_system_earth_space_textbook.jpg"]');
    await expect(solarImage).toBeVisible({ timeout: 5000 });
    console.log('[E2E] NS7_SOLAR_SYSTEM_ORBITS diagram rendered successfully!');

    // 7. Test MATH7_TRIANGLE_INTERIOR_ANGLES generation & JSXGraph precision board render
    const triangleArchBtn = page.locator('[data-testid="archetype-item-MATH7_TRIANGLE_INTERIOR_ANGLES"]:visible');
    await triangleArchBtn.scrollIntoViewIfNeeded();
    await triangleArchBtn.click();

    await expect(generateBtn).toContainText('MATH7_TRIANGLE_INTERIOR_ANGLES', { timeout: 10000 });

    const jxgBoard = diagramContainer.locator('[data-testid="geogebra-diagram-board"]:visible');
    await expect(jxgBoard).toBeVisible({ timeout: 15000 });
    console.log('[E2E] MATH7_TRIANGLE_INTERIOR_ANGLES precision vector board rendered successfully!');
  });
});
