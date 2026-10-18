import { test, expect } from '@playwright/test';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { evaluatePageNeatness, generateNeatnessHtmlReport } from '../helpers/neatnessEvaluator.js';
import { authenticateSuperAdminSession } from '../helpers/authenticateSuperAdmin.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * Visual Neatness & Button Placement Ergonomics Audit Suite
 * Strict Invariant Compliance:
 * - Captures high-res screenshots for each user type (Super Admin, Parent, School Admin, Teacher, Student)
 * - Programmatically judges visual busyness, element density, 60-30-10 adherence, and button placement ergonomics
 * - Outputs actionable HTML report at reports/visual_audits/neatness_report.html
 */
test.describe('Visual Neatness & Cockpit Clutter Audit', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';
  const screenshotDir = path.resolve(__dirname, '../../reports/visual_audits/screenshots');
  const reportPath = path.resolve(__dirname, '../../reports/visual_audits/neatness_report.html');
  const auditResults = [];

  test.beforeAll(() => {
    if (!fs.existsSync(screenshotDir)) {
      fs.mkdirSync(screenshotDir, { recursive: true });
    }
  });

  test.afterAll(() => {
    if (auditResults.length > 0) {
      const generatedPath = generateNeatnessHtmlReport(auditResults, reportPath);
      console.log(`\n📊 [Visual Audit] Generated comprehensive visual neatness report at: ${generatedPath}\n`);
    }
  });

  // 1. Super Admin Cockpit (Desktop)
  test('Evaluate Super Admin Cockpit: Clearance Desk & System Density', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await authenticateSuperAdminSession(page, targetBaseUrl);

    // Verify Admin Header / Dashboard Title renders
    const adminHeading = page.locator('text=Administrator Dashboard');
    await expect(adminHeading).toBeVisible({ timeout: 15000 });

    const shotPath = path.join(screenshotDir, 'super_admin_cockpit_desktop.png');
    await page.screenshot({ path: shotPath, fullPage: true });

    const audit = await evaluatePageNeatness(page, {
      role: 'super_admin',
      screenName: 'Super Admin Governance Cockpit',
      isMobile: false,
      screenshotPath: shotPath
    });

    auditResults.push(audit);
    console.log(`[Visual Audit] Super Admin Score: ${audit.score}/100 (${audit.status})`);
    expect(audit.metrics.hasHorizontalOverflow).toBe(false);
  });

  // 2. Parent Dashboard (Desktop)
  test('Evaluate Parent Dashboard Desktop: Sunday Pulse & Child Cards', async ({ page }) => {
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

    // Verify Parent Portal Header
    const portalTitle = page.locator('h1:has-text("Parent & Guardian Bridge")');
    await expect(portalTitle).toBeVisible({ timeout: 15000 });

    const shotPath = path.join(screenshotDir, 'parent_dashboard_desktop.png');
    await page.screenshot({ path: shotPath, fullPage: true });

    const audit = await evaluatePageNeatness(page, {
      role: 'parent',
      screenName: 'Parent Guardian Portal (Sunday Pulse)',
      isMobile: false,
      screenshotPath: shotPath
    });

    auditResults.push(audit);
    console.log(`[Visual Audit] Parent Desktop Score: ${audit.score}/100 (${audit.status})`);
    expect(audit.metrics.hasHorizontalOverflow).toBe(false);
  });

  // 3. Parent Dashboard (Mobile Pixel 7)
  test('Evaluate Parent Dashboard Mobile: Touch Targets & Thumb Zone', async ({ page }) => {
    await page.setViewportSize({ width: 393, height: 851 }); // Pixel 7
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

    // Verify Parent Portal Header
    const portalTitle = page.locator('h1:has-text("Parent & Guardian Bridge")');
    await expect(portalTitle).toBeVisible({ timeout: 15000 });

    const shotPath = path.join(screenshotDir, 'parent_dashboard_mobile.png');
    await page.screenshot({ path: shotPath, fullPage: true });

    const audit = await evaluatePageNeatness(page, {
      role: 'parent',
      screenName: 'Parent Guardian Portal (Mobile WebAPK)',
      isMobile: true,
      screenshotPath: shotPath
    });

    auditResults.push(audit);
    console.log(`[Visual Audit] Parent Mobile Score: ${audit.score}/100 (${audit.status})`);
    expect(audit.metrics.hasHorizontalOverflow).toBe(false);
  });

  // 4. School Admin Strategic Desk (Desktop)
  test('Evaluate School Admin Strategic Desk: Pacing Matrix Density', async ({ page }) => {
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

    // Verify School Admin Header
    const schoolHeading = page.locator('text=Westville High School').first();
    await expect(schoolHeading).toBeVisible({ timeout: 15000 });

    const shotPath = path.join(screenshotDir, 'school_admin_desk_desktop.png');
    await page.screenshot({ path: shotPath, fullPage: true });

    const audit = await evaluatePageNeatness(page, {
      role: 'school_admin',
      screenName: 'School Admin Strategic Desk (ATP Pacing)',
      isMobile: false,
      screenshotPath: shotPath
    });

    auditResults.push(audit);
    console.log(`[Visual Audit] School Admin Score: ${audit.score}/100 (${audit.status})`);
    expect(audit.metrics.hasHorizontalOverflow).toBe(false);
  });

  // 5. Teacher LMS Cockpit (Desktop)
  test('Evaluate Teacher LMS Cockpit: Class Rosters & Heatmap', async ({ page }) => {
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

    // Verify Teacher Cockpit Header
    const teacherHeading = page.locator('h1:has-text("Mr. N. Sithole")');
    await expect(teacherHeading).toBeVisible({ timeout: 15000 });

    const shotPath = path.join(screenshotDir, 'teacher_cockpit_desktop.png');
    await page.screenshot({ path: shotPath, fullPage: true });

    const audit = await evaluatePageNeatness(page, {
      role: 'teacher',
      screenName: 'Educator LMS Cockpit (Rosters & Heatmap)',
      isMobile: false,
      screenshotPath: shotPath
    });

    auditResults.push(audit);
    console.log(`[Visual Audit] Teacher Cockpit Score: ${audit.score}/100 (${audit.status})`);
    expect(audit.metrics.hasHorizontalOverflow).toBe(false);
  });

  // 6. Student Today\'s Desk (Desktop)
  test('Evaluate Student Today\'s Desk & Workspace: Problem Surface Cleanliness', async ({ page }) => {
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

    // Verify Today's Desk tab is present & active
    const deskTab = page.locator('[data-testid="tab-desk"]').first();
    await expect(deskTab).toBeVisible({ timeout: 15000 });

    const shotPath = path.join(screenshotDir, 'student_today_desk_desktop.png');
    await page.screenshot({ path: shotPath, fullPage: true });

    const audit = await evaluatePageNeatness(page, {
      role: 'student',
      screenName: 'Learner Today\'s Desk (Desktop PWA)',
      isMobile: false,
      screenshotPath: shotPath
    });

    auditResults.push(audit);
    console.log(`[Visual Audit] Student Today's Desk Score: ${audit.score}/100 (${audit.status})`);
    expect(audit.metrics.hasHorizontalOverflow).toBe(false);
  });
});
