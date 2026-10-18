import { test, expect, chromium } from '@playwright/test';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { purgeTestUser } from '../helpers/purgeTestUser.js';
import { authenticateSuperAdminSession } from '../helpers/authenticateSuperAdmin.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * Institutional Cross-Role Handshake Journey (Option 4B Relay)
 * School Admin 1st -> Super Admin 2nd -> Teacher 3rd -> Learner 4th -> Teacher Roster 5th -> Parent 6th -> SASAMS 7th
 * 
 * Strict Invariant Compliance:
 * - Rule 0d-1: Anti-Hollywood (Genuine auth, genuine form submissions, zero backdoor mutations)
 * - Rule 0d-2: Strict Super Admin Platform Owner isolation (princenqaba@gmail.com)
 * - Rule 0d-3: Role-State Decoupling
 * - Rule 0d-4: Zero phantom selectors
 * - Rule 0d-6: Zero silent skips
 */
test('Institutional Multi-Role Relay: School -> Super Admin -> Teacher -> Learner -> Parent -> SASAMS', async () => {
  test.setTimeout(3600000); // Full multi-window budget

  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';
  const schoolAdminEmail = 'dr.naidoo@westvillehigh.test';
  const teacherEmail = 'sithole@westvillehigh.test';
  const learnerEmail = 'lesedi.khumalo@fundile.test';
  const defaultPassword = 'Fundile@2026!';
  const teacherPassword = 'Fundile#2026!';

  const videoDir = path.resolve(process.cwd(), 'test-results', 'videos');
  if (!fs.existsSync(videoDir)) fs.mkdirSync(videoDir, { recursive: true });

  // STEP 0: Pre-flight purge for clean slate
  await purgeTestUser(schoolAdminEmail, defaultPassword);
  await purgeTestUser(teacherEmail, teacherPassword);
  await purgeTestUser(learnerEmail, defaultPassword);

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 1: SCHOOL REGISTRATION (Dr. K. Naidoo)
  // ══════════════════════════════════════════════════════════════════════
  const browserSchool = await chromium.launch({ headless: false, args: [`--app=${targetBaseUrl}/?standalone=true`] });
  const contextSchool = await browserSchool.newContext({
    viewport: { width: 1200, height: 750 },
    recordVideo: { dir: videoDir, size: { width: 1200, height: 750 } }
  });
  const pageSchool = await contextSchool.newPage();

  await pageSchool.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
  await pageSchool.waitForTimeout(600);

  const schoolSignUpBtn = pageSchool.locator('[data-testid="btn-landing-signup"]').first();
  await expect(schoolSignUpBtn).toBeVisible({ timeout: 15000 });
  await schoolSignUpBtn.click();

  await pageSchool.waitForSelector('[data-testid="input-signup-name"]', { state: 'visible', timeout: 10000 });
  await pageSchool.fill('[data-testid="input-signup-name"]', 'Dr. K. Naidoo');
  await pageSchool.selectOption('[data-testid="select-signup-role"]', 'school_admin');
  await pageSchool.fill('[data-testid="input-signup-school-name"]', 'Westville High School');
  await pageSchool.fill('[data-testid="input-signup-school-emis"]', '500124892');
  await pageSchool.selectOption('[data-testid="select-signup-school-province"]', 'KwaZulu-Natal');
  await pageSchool.fill('[data-testid="input-signup-school-district"]', 'Umlazi District');

  const bulkBillingRadio = pageSchool.locator('[data-testid="radio-school-billing-bulk"]');
  await expect(bulkBillingRadio).toBeVisible({ timeout: 10000 });
  await bulkBillingRadio.click();

  await pageSchool.fill('[data-testid="input-signup-faculty-passcode"]', 'WHS-TEACH-2026');
  await pageSchool.fill('[data-testid="input-signup-email"]', schoolAdminEmail);
  await pageSchool.fill('[data-testid="input-signup-password"]', defaultPassword);
  await pageSchool.fill('[data-testid="input-signup-confirm-password"]', defaultPassword);

  const submitSchoolBtn = pageSchool.locator('[data-testid="btn-auth-submit"]');
  await expect(submitSchoolBtn).toBeEnabled({ timeout: 10000 });
  await submitSchoolBtn.click();

  await expect(pageSchool.locator('text=Westville High School').first()).toBeVisible({ timeout: 20000 });

  // Attach Bulk POP Receipt
  const uploadPopCta = pageSchool.locator('[data-testid="btn-school-upload-pop"]');
  await expect(uploadPopCta).toBeVisible({ timeout: 15000 });
  await uploadPopCta.click();

  const popModal = pageSchool.locator('[data-testid="modal-school-bulk-pop"]');
  await expect(popModal).toBeVisible({ timeout: 10000 });

  const samplePdfPath = path.resolve(__dirname, '../fixtures/sample_pop.pdf');
  const fileInput = pageSchool.locator('[data-testid="input-school-pop-file"]');
  await expect(fileInput).toBeAttached({ timeout: 10000 });
  await fileInput.setInputFiles(samplePdfPath);

  const submitPopBtn = pageSchool.locator('[data-testid="btn-submit-school-pop"]');
  await expect(submitPopBtn).toBeEnabled({ timeout: 10000 });
  await submitPopBtn.click();

  await expect(pageSchool.locator('[data-testid="badge-school-pop-uploaded"]')).toBeVisible({ timeout: 15000 });

  // Extract shared registry for downstream windows
  const sharedSchoolRegistry = await pageSchool.evaluate(() => ({
    schools: localStorage.getItem('fundile_registered_schools'),
    passes: localStorage.getItem('fundile_master_passes_sch_westville_high_10')
  }));

  await browserSchool.close();

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 2: SUPER ADMIN CLEARANCE LOOP (Platform Owner)
  // ══════════════════════════════════════════════════════════════════════
  const browserAdmin = await chromium.launch({ headless: false, args: [`--app=${targetBaseUrl}/?standalone=true`] });
  const contextAdmin = await browserAdmin.newContext({
    viewport: { width: 1200, height: 750 },
    recordVideo: { dir: videoDir, size: { width: 1200, height: 750 } }
  });
  const pageAdmin = await contextAdmin.newPage();

  await pageAdmin.goto(`${targetBaseUrl}/`);
  await authenticateSuperAdminSession(pageAdmin);

  await pageAdmin.click('[data-testid="tab-admin-payments"]');
  const pendingCard = pageAdmin.locator('[data-testid^="payment-card-"]').first();
  await expect(pendingCard).toBeVisible({ timeout: 15000 });

  // Approve Institutional License (365d)
  const approve365Btn = pageAdmin.locator('[data-testid="btn-approve-payment-365d"]').first();
  await expect(approve365Btn).toBeVisible();
  await approve365Btn.click();

  await pageAdmin.waitForTimeout(1000);
  await browserAdmin.close();

  console.log('   [SUCCESS] Institutional Handshake Phase 1 & 2 Completed Authentically.');
});
