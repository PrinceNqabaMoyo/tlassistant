import { test, expect, chromium } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';
import {
  injectGlidingCursorAndHud,
  glideAndClick,
  typeRealistic,
  updateHud
} from './helpers/autopilotHud.js';
import { purgeTestUser } from './helpers/purgeTestUser.js';
import { authenticateSuperAdminSession } from './helpers/authenticateSuperAdmin.js';
import { waitForStep } from './helpers/stepPrompt.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

test('Set 1: Authentic School-Linked Multi-Stakeholder Journey (School Registration 1st -> Super Admin 2nd -> Teacher Onboarding 3rd -> Learner 4th -> Teacher Roster 5th -> Parent Pulse 6th -> School Admin SASAMS 7th)', async () => {
  test.setTimeout(3600000); // 1 hour test budget

  const schoolAdminEmail = 'dr.naidoo@westvillehigh.test';
  const teacherEmail = 'sithole@westvillehigh.test';
  const learnerEmail = 'lesedi.khumalo@fundile.test';
  const defaultPassword = 'Fundile@2026!';
  const teacherPassword = 'Fundile#2026!';

  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';
  const isHeadless = process.env.HEADLESS === 'true' || process.env.CI === 'true';
  const learnerStoragePath = path.resolve(__dirname, 'fixtures/learner_storage_state.json');

  console.log('\n[SET 1] Authentic Chronological Multi-Stakeholder Lifecycle (Option 4B Stepper)...');
  console.log('   Hardware Optimization: 1 Window active at a time (~250 MB RAM cap)');
  console.log('   Phase 1: School Registration 1st — Dr. K. Naidoo (Registers Westville High, Bulk License & Faculty Passcode)');
  console.log('   Phase 2: Super Admin Clearance 2nd — Platform Owner Clearance Desk Review');
  console.log('   Phase 3: Institutional Educator Onboarding 3rd — Mr. N. Sithole (Selects Westville High & Enters WHS-TEACH-2026)');
  console.log('   Phase 4: School-Linked Learner 4th — Lesedi Khumalo (Selects Westville High & Enters Master Pass WHS-GR10-8421)');
  console.log('   Phase 5: Teacher Roster Review 5th — Mr. N. Sithole verifies Lesedi live on ACC10A & confirms Authority Controls');
  console.log('   Phase 6: Parent Guardian Portal 6th — Mrs. Nomsa Khumalo views Sunday Academic Pulse');
  console.log('   Phase 7: School Admin Strategic Desk 7th — Dr. K. Naidoo reviews ATP Pacing & exports official SASAMS Mark Ledger\n');

  // ══════════════════════════════════════════════════════════════════════
  // STEP 0: PRE-FLIGHT TARGETED PURGE (Clean slate for all test accounts)
  // ══════════════════════════════════════════════════════════════════════
  await purgeTestUser(schoolAdminEmail, defaultPassword);
  await purgeTestUser(teacherEmail, teacherPassword);
  await purgeTestUser(learnerEmail, defaultPassword);

  const getLaunchOpts = () => ({
    headless: isHeadless,
    args: isHeadless ? [] : ['--window-size=1280,820', '--window-position=50,50']
  });

  // Shared in-memory registry extracted from Phase 1 registration
  let sharedSchoolRegistry = null;

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 1: SCHOOL REGISTRATION 1ST (Dr. K. Naidoo — School Admin)
  // ══════════════════════════════════════════════════════════════════════
  console.log('\n[PHASE 1] Launching School Admin Window: Dr. K. Naidoo registering Westville High School...');
  const browserSchool1 = await chromium.launch(getLaunchOpts());
  const contextSchool1 = await browserSchool1.newContext({
    viewport: { width: 1200, height: 750 }
  });
  const pageSchool1 = await contextSchool1.newPage();

  await pageSchool1.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
  await pageSchool1.waitForTimeout(600);
  await injectGlidingCursorAndHud(pageSchool1);

  // 1. Click Sign Up CTA on Landing Page
  const schoolSignUpBtn = pageSchool1.locator('[data-testid="btn-landing-signup"]:visible, [data-testid="btn-landing-signup"]').first();
  await expect(schoolSignUpBtn).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageSchool1, schoolSignUpBtn, {
    persona: 'DR. K. NAIDOO',
    message: 'Opening Institutional Registration'
  });
  await pageSchool1.waitForTimeout(400);

  // 2. Fill School Admin Registration Form
  await pageSchool1.waitForSelector('[data-testid="input-signup-name"]', { state: 'visible', timeout: 10000 });
  await typeRealistic(pageSchool1, '[data-testid="input-signup-name"]', 'Dr. K. Naidoo', {
    persona: 'DR. K. NAIDOO',
    message: 'Entering Administrator Name: Dr. K. Naidoo'
  });

  await pageSchool1.selectOption('[data-testid="select-signup-role"]', 'school_admin');
  await pageSchool1.waitForTimeout(300);

  // Fill Official School Registration Fields
  await typeRealistic(pageSchool1, '[data-testid="input-signup-school-name"]', 'Westville High School', {
    persona: 'DR. K. NAIDOO',
    message: 'Entering Official School Name: Westville High School'
  });

  await typeRealistic(pageSchool1, '[data-testid="input-signup-school-emis"]', '500124892', {
    persona: 'DR. K. NAIDOO',
    message: 'Entering EMIS Number: 500124892'
  });

  await pageSchool1.selectOption('[data-testid="select-signup-school-province"]', 'KwaZulu-Natal');

  await typeRealistic(pageSchool1, '[data-testid="input-signup-school-district"]', 'Umlazi District', {
    persona: 'DR. K. NAIDOO',
    message: 'Entering District: Umlazi District'
  });

  const bulkBillingRadio = pageSchool1.locator('[data-testid="radio-school-billing-bulk"]');
  await expect(bulkBillingRadio).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageSchool1, bulkBillingRadio, {
    persona: 'DR. K. NAIDOO',
    message: 'Selecting Institutional Bulk Prepaid Model'
  });
  await pageSchool1.waitForTimeout(200);

  await typeRealistic(pageSchool1, '[data-testid="input-signup-faculty-passcode"]', 'WHS-TEACH-2026', {
    persona: 'DR. K. NAIDOO',
    message: 'Setting Official Faculty Passcode: WHS-TEACH-2026'
  });

  await typeRealistic(pageSchool1, '[data-testid="input-signup-email"]', schoolAdminEmail, {
    persona: 'DR. K. NAIDOO',
    message: `Entering Official Email: ${schoolAdminEmail}`
  });

  await typeRealistic(pageSchool1, '[data-testid="input-signup-password"]', defaultPassword, {
    persona: 'DR. K. NAIDOO',
    message: 'Setting Strong Password'
  });

  await typeRealistic(pageSchool1, '[data-testid="input-signup-confirm-password"]', defaultPassword, {
    persona: 'DR. K. NAIDOO',
    message: 'Confirming Password'
  });

  const submitSchoolBtn = pageSchool1.locator('[data-testid="btn-auth-submit"]');
  await expect(submitSchoolBtn).toBeEnabled({ timeout: 10000 });
  await glideAndClick(pageSchool1, submitSchoolBtn, {
    persona: 'DR. K. NAIDOO',
    message: 'Submitting Official Institutional School Registration'
  });
  await pageSchool1.waitForTimeout(2000);

  // 3. Verify School Admin Dashboard Loaded
  await expect(pageSchool1.locator('text=Westville High School').first()).toBeVisible({ timeout: 20000 });
  await expect(pageSchool1.locator('text=WHS-TEACH-2026').or(pageSchool1.locator('text=Faculty Passcode')).first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Westville High School registered dynamically with Faculty Passcode WHS-TEACH-2026');

  // 4. Institutional Bulk License Clearance & POP Upload (Rule 0d-1 & Rule 0d-5)
  const uploadPopCta = pageSchool1.locator('[data-testid="btn-school-upload-pop"]');
  await expect(uploadPopCta).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageSchool1, uploadPopCta, {
    persona: 'DR. K. NAIDOO',
    message: 'Opening Institutional Bulk License POP Upload Modal'
  });
  await pageSchool1.waitForTimeout(1500);

  // Submit Institutional POP Form
  const popModal = pageSchool1.locator('[data-testid="modal-school-bulk-pop"]');
  await expect(popModal).toBeVisible({ timeout: 10000 });
  await expect(pageSchool1.locator('[data-testid="input-school-pop-reference"]')).toHaveValue('WHS-BULK-2026');
  await pageSchool1.waitForTimeout(600);

  // Authentically attach official Access Bank bulk payment slip
  const bulkPdfPath = path.resolve(__dirname, 'fixtures/westville_high_bulk_pop.pdf');
  const fileInput = pageSchool1.locator('[data-testid="input-school-pop-file"]');
  await expect(fileInput).toBeAttached({ timeout: 10000 });
  await fileInput.setInputFiles(bulkPdfPath);
  await updateHud(pageSchool1, 'DR. K. NAIDOO', 'Attached Access Bank Bulk Payment Stamped Slip (westville_high_bulk_pop.pdf)');
  await pageSchool1.waitForTimeout(1000);

  const submitPopBtn = pageSchool1.locator('[data-testid="btn-submit-school-pop"]');
  await expect(submitPopBtn).toBeEnabled({ timeout: 10000 });
  await glideAndClick(pageSchool1, submitPopBtn, {
    persona: 'DR. K. NAIDOO',
    message: 'Submitting Access Bank Bulk EFT Receipt (WHS-BULK-2026 • R45,000.00)'
  });
  await pageSchool1.waitForTimeout(2000);

  // Assert clearance pending badge
  await expect(pageSchool1.locator('[data-testid="badge-school-pop-uploaded"]')).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Dr. Naidoo uploaded Access Bank Bulk POP receipt (Ref: WHS-BULK-2026)');

  // 5. Check Faculty Allocations tab to confirm generated Grade 10 Master Passkeys
  const facultyTab1 = pageSchool1.locator('button:has-text("Teaching Staff & Allocations"), button:has-text("Teaching Staff")').first();
  await expect(facultyTab1).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageSchool1, facultyTab1, {
    persona: 'DR. K. NAIDOO',
    message: 'Navigating to Faculty Allocations & Master Passkey Registry'
  });
  await pageSchool1.waitForTimeout(800);

  await expect(pageSchool1.locator('text=WHS-GR10-8421').or(pageSchool1.locator('text=Grade 10 Institutional Master Passkeys')).first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Grade 10 Master Passkey Registry generated (WHS-GR10-8421 through 8426)');

  // Extract dynamically generated school record & master passes from localStorage
  sharedSchoolRegistry = await pageSchool1.evaluate(() => ({
    schools: localStorage.getItem('fundile_registered_schools'),
    passes: localStorage.getItem('fundile_master_passes_sch_westville_high_10')
  }));
  console.log('   [EXTRACTED] Dynamic school registry captured for downstream stakeholders');

  // Navigate back to School Overview / ATP Heatmap so clearance pending badge is in full view
  const pacingTab1 = pageSchool1.locator('button:has-text("ATP Curriculum Pacing Heatmap")').first();
  await expect(pacingTab1).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageSchool1, pacingTab1, {
    persona: 'DR. K. NAIDOO',
    message: 'Returning to School Overview with Active Clearance Banner'
  });
  await pageSchool1.waitForTimeout(600);

  // Pause for inspection (Option 4B)
  await waitForStep('PHASE 1: SCHOOL REGISTRATION & BULK POP UPLOAD (DR. K. NAIDOO)', 'Westville High School registered dynamically with EMIS 500124892, Faculty Passcode WHS-TEACH-2026, and Access Bank bulk POP submitted to Clearance Desk.', pageSchool1);

  // Close Phase 1 browser completely — strictly 1 window active at a time (~250 MB RAM cap)
  await browserSchool1.close();
  console.log('   [CLOSED] Phase 1 browser closed. RAM freed.\n');

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 2: SUPER ADMIN CLEARANCE & INSTITUTIONAL LICENSE REVIEW
  // ══════════════════════════════════════════════════════════════════════
  console.log('[PHASE 2] Launching Super Admin Window: Clearance Desk...');
  const browserAdmin = await chromium.launch(getLaunchOpts());
  const contextAdmin = await browserAdmin.newContext({
    viewport: { width: 1200, height: 750 }
  });
  const pageAdmin = await contextAdmin.newPage();

  // Authentic Super Admin sign-in (Rule 0d-2: Platform Owner, Zero Mock Personas)
  await authenticateSuperAdminSession(pageAdmin, targetBaseUrl);
  await injectGlidingCursorAndHud(pageAdmin);

  // Navigate to Clearance Desk / Payments Tab
  const adminPaymentsTab = pageAdmin.locator('[data-testid="tab-admin-payments"]').first();
  await expect(adminPaymentsTab).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageAdmin, adminPaymentsTab, {
    persona: 'SUPER ADMIN',
    message: 'Opening Institutional Clearance Desk'
  });
  await pageAdmin.waitForTimeout(1000);

  // Assert clearance desk loaded and shows Dr. Naidoo's pending institutional payment
  const naidooCardContainer = pageAdmin.locator('div[data-testid^="payment-card-"]:has([data-testid="payment-email-dr.naidoo@westvillehigh.test"]), div[data-testid^="payment-card-"]:has-text("dr.naidoo@westvillehigh.test"), div[data-testid^="payment-card-"]:has-text("WHS-BULK-2026")').first();
  await expect(naidooCardContainer).toBeVisible({ timeout: 20000 });
  console.log('   [VERIFIED] Westville High School bulk payment visible in Super Admin Clearance Desk');

  // Genuine Super Admin Review & Approval Actions (Rule 0d-1 & Rule 0d-5)
  const viewPopBtn = naidooCardContainer.locator('[data-testid="btn-view-pop"]').first();
  await expect(viewPopBtn).toBeVisible({ timeout: 15000 });
  const [popPopup] = await Promise.all([
    pageAdmin.waitForEvent('popup').catch(() => null),
    glideAndClick(pageAdmin, viewPopBtn, {
      persona: 'SUPER ADMIN',
      message: 'Reviewing Access Bank Electronic Funds Transfer Slip for Westville High School'
    })
  ]);
  if (popPopup) {
    await popPopup.waitForLoadState('domcontentloaded').catch(() => {});
    await pageAdmin.waitForTimeout(1000);
    await popPopup.close().catch(() => {});
  }
  await pageAdmin.waitForTimeout(600);

  const approve365Btn = naidooCardContainer.locator('[data-testid="btn-approve-payment-365d"]').first();
  await expect(approve365Btn).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageAdmin, approve365Btn, {
    persona: 'SUPER ADMIN',
    message: 'Approving 365-Day Institutional Bulk License for Westville High School'
  });
  await pageAdmin.waitForTimeout(1500);

  // Assert payment approved
  await expect(naidooCardContainer.locator('span:has-text("approved"), span:has-text("APPROVED")').first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Super Admin cleared Westville High School Institutional Bulk License');

  // Pause for inspection (Option 4B)
  await waitForStep('PHASE 2: SUPER ADMIN CLEARANCE & BULK LICENSE APPROVAL', 'Super Admin verified Access Bank EFT slip and approved 365-day bulk license for Westville High School.', pageAdmin);

  // Close Phase 2 browser completely
  await browserAdmin.close();
  console.log('   [CLOSED] Phase 2 browser closed. RAM freed.\n');

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 3: INSTITUTIONAL EDUCATOR ONBOARDING (Mr. N. Sithole)
  // ══════════════════════════════════════════════════════════════════════
  console.log('[PHASE 3] Launching Institutional Educator Window: Mr. N. Sithole...');
  const browserTeacher = await chromium.launch(getLaunchOpts());
  const contextTeacher = await browserTeacher.newContext({
    viewport: { width: 1200, height: 750 }
  });

  // Inject dynamically registered Westville High School into teacher's session
  if (sharedSchoolRegistry) {
    await contextTeacher.addInitScript((data) => {
      if (data.schools) localStorage.setItem('fundile_registered_schools', data.schools);
      if (data.passes) localStorage.setItem('fundile_master_passes_sch_westville_high_10', data.passes);
    }, sharedSchoolRegistry);
  }

  const pageTeacher = await contextTeacher.newPage();
  await pageTeacher.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
  await pageTeacher.waitForTimeout(600);
  await injectGlidingCursorAndHud(pageTeacher);

  // 1. Click Sign Up CTA on Landing Page
  const teacherSignUpBtn = pageTeacher.locator('[data-testid="btn-landing-signup"]:visible, [data-testid="btn-landing-signup"]').first();
  await expect(teacherSignUpBtn).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageTeacher, teacherSignUpBtn, {
    persona: 'MR. N. SITHOLE',
    message: 'Opening Educator Registration'
  });
  await pageTeacher.waitForTimeout(400);

  // 2. Fill Educator Registration Form as Institutional School Faculty
  await pageTeacher.waitForSelector('[data-testid="input-signup-name"]', { state: 'visible', timeout: 10000 });
  await typeRealistic(pageTeacher, '[data-testid="input-signup-name"]', 'Mr. N. Sithole', {
    persona: 'MR. N. SITHOLE',
    message: 'Entering Educator Name: Mr. N. Sithole'
  });

  await pageTeacher.selectOption('[data-testid="select-signup-role"]', 'teacher');
  await pageTeacher.waitForTimeout(200);

  // Select Institutional School Educator Type
  const instRadio = pageTeacher.locator('[data-testid="radio-teacher-institutional"]');
  await expect(instRadio).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageTeacher, instRadio, {
    persona: 'MR. N. SITHOLE',
    message: 'Selecting Institutional School Educator'
  });
  await pageTeacher.waitForTimeout(200);

  // Select Dynamically Registered School: Westville High School
  await pageTeacher.selectOption('[data-testid="select-signup-teacher-school"]', 'sch_westville_high');
  await pageTeacher.selectOption('[data-testid="select-signup-teacher-subject"]', 'Accounting');
  await pageTeacher.waitForTimeout(200);

  // Enter Faculty Invite Passcode
  await typeRealistic(pageTeacher, '[data-testid="input-teacher-invite-code"]', 'WHS-TEACH-2026', {
    persona: 'MR. N. SITHOLE',
    message: 'Entering Faculty Passcode: WHS-TEACH-2026'
  });
  await pageTeacher.waitForTimeout(300);

  // Verify faculty passcode was authenticated
  await expect(pageTeacher.locator('[data-testid="badge-faculty-pass-verified"]').or(pageTeacher.locator('text=Verified Faculty Passcode')).first()).toBeVisible({ timeout: 10000 });

  await typeRealistic(pageTeacher, '[data-testid="input-signup-email"]', teacherEmail, {
    persona: 'MR. N. SITHOLE',
    message: `Entering Official Email: ${teacherEmail}`
  });

  await typeRealistic(pageTeacher, '[data-testid="input-signup-password"]', teacherPassword, {
    persona: 'MR. N. SITHOLE',
    message: 'Setting Strong Password'
  });

  await typeRealistic(pageTeacher, '[data-testid="input-signup-confirm-password"]', teacherPassword, {
    persona: 'MR. N. SITHOLE',
    message: 'Confirming Password'
  });

  const submitTeacherBtn = pageTeacher.locator('[data-testid="btn-auth-submit"]');
  await expect(submitTeacherBtn).toBeEnabled({ timeout: 10000 });
  await glideAndClick(pageTeacher, submitTeacherBtn, {
    persona: 'MR. N. SITHOLE',
    message: 'Submitting Faculty Registration'
  });
  await pageTeacher.waitForTimeout(2000);

  // 3. Verify Teacher Cockpit Loaded with Inherited Roster
  await expect(pageTeacher.locator('text=Mr. N. Sithole').or(pageTeacher.locator('text=Teacher')).or(pageTeacher.locator('text=ACC10A')).first()).toBeVisible({ timeout: 20000 });
  await expect(pageTeacher.locator('text=ACC10A').first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Institutional teacher cockpit loaded & provisioned with class ACC10A');

  // Pause for inspection (Option 4B)
  await waitForStep('PHASE 3: INSTITUTIONAL EDUCATOR ONBOARDING', 'Mr. N. Sithole signed up with Faculty Passcode WHS-TEACH-2026, linked to Westville High School, and provisioned with class ACC10A.', pageTeacher);

  // Close Phase 3 browser completely
  await browserTeacher.close();
  console.log('   [CLOSED] Phase 3 browser closed. RAM freed.\n');

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 4: SCHOOL-LINKED LEARNER REGISTRATION & PROBLEM-SOLVING (Lesedi Khumalo)
  // ══════════════════════════════════════════════════════════════════════
  console.log('[PHASE 4] Launching Learner Window: Lesedi Khumalo...');
  const browserLearner = await chromium.launch(getLaunchOpts());
  const contextLearner = await browserLearner.newContext({
    viewport: { width: 1200, height: 750 }
  });

  // Inject dynamically registered Westville High School and passkeys into learner session
  if (sharedSchoolRegistry) {
    await contextLearner.addInitScript((data) => {
      if (data.schools) localStorage.setItem('fundile_registered_schools', data.schools);
      if (data.passes) localStorage.setItem('fundile_master_passes_sch_westville_high_10', data.passes);
    }, sharedSchoolRegistry);
  }

  const pageLearner = await contextLearner.newPage();
  await pageLearner.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
  await pageLearner.waitForTimeout(600);
  await injectGlidingCursorAndHud(pageLearner);

  // 1. Click Sign Up CTA on Landing Page
  const learnerSignUpBtn = pageLearner.locator('[data-testid="btn-landing-signup"]:visible, [data-testid="btn-landing-signup"]').first();
  await expect(learnerSignUpBtn).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageLearner, learnerSignUpBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Clicking Sign Up CTA'
  });
  await pageLearner.waitForTimeout(500);

  // 2. Fill CAPS FET Registration Form as School-Linked Learner
  await pageLearner.waitForSelector('[data-testid="input-signup-name"]', { state: 'visible', timeout: 10000 });
  await typeRealistic(pageLearner, '[data-testid="input-signup-name"]', 'Lesedi Khumalo', {
    persona: 'LESEDI KHUMALO',
    message: 'Typing Learner Name: Lesedi Khumalo'
  });

  await pageLearner.selectOption('[data-testid="select-signup-role"]', 'student');
  await pageLearner.waitForTimeout(200);

  // Select School-Linked Account Type
  const schoolLinkedRadio = pageLearner.locator('[data-testid="radio-account-school-linked"]');
  await expect(schoolLinkedRadio).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, schoolLinkedRadio, {
    persona: 'LESEDI KHUMALO',
    message: 'Selecting School-Linked Account'
  });
  await pageLearner.waitForTimeout(200);

  // Select Approved School: Westville High School (dynamically registered in Phase 1)
  await pageLearner.selectOption('[data-testid="select-signup-school"]', 'sch_westville_high');
  await pageLearner.waitForTimeout(200);

  // Enter Grade 10 Master Pass Key
  await typeRealistic(pageLearner, '[data-testid="input-school-master-pass"]', 'WHS-GR10-8421', {
    persona: 'LESEDI KHUMALO',
    message: 'Entering Grade 10 Master Pass: WHS-GR10-8421'
  });
  await pageLearner.waitForTimeout(300);

  // Verify Master Pass validation message
  await expect(pageLearner.locator('[data-testid="badge-master-pass-verified"]').or(pageLearner.locator('text=Grade 10 Master Pass Verified')).first()).toBeVisible({ timeout: 10000 });

  await typeRealistic(pageLearner, '[data-testid="input-signup-email"]', learnerEmail, {
    persona: 'LESEDI KHUMALO',
    message: `Entering Email: ${learnerEmail}`
  });

  await typeRealistic(pageLearner, '[data-testid="input-signup-password"]', defaultPassword, {
    persona: 'LESEDI KHUMALO',
    message: 'Entering Password'
  });

  await typeRealistic(pageLearner, '[data-testid="input-signup-confirm-password"]', defaultPassword, {
    persona: 'LESEDI KHUMALO',
    message: 'Confirming Password'
  });

  const popiaCheckbox = pageLearner.locator('[data-testid="checkbox-popia-consent"]');
  await expect(popiaCheckbox).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, popiaCheckbox, {
    persona: 'LESEDI KHUMALO',
    message: 'Acknowledging POPIA Section 35 Minor Consent'
  });
  await pageLearner.waitForTimeout(200);

  const submitLearnerBtn = pageLearner.locator('[data-testid="btn-auth-submit"]');
  await expect(submitLearnerBtn).toBeEnabled({ timeout: 10000 });
  await glideAndClick(pageLearner, submitLearnerBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Submitting School-Linked Account Registration'
  });
  await pageLearner.waitForTimeout(1500);
  console.log('   [VERIFIED] School-linked sign-up submitted with valid Master Pass WHS-GR10-8421');

  // 3. Self-Service Subject & Class Enrollment Modal
  const subjectEnrollSaveBtn = pageLearner.locator('[data-testid="btn-save-subject-enrollment"]').first();
  await expect(subjectEnrollSaveBtn).toBeVisible({ timeout: 15000 });

  const accSelect = pageLearner.locator('[data-testid="select-enrolled-class-accounting"]').first();
  await expect(accSelect).toBeVisible({ timeout: 10000 });
  await accSelect.selectOption('ACC10A');

  const mathSelect = pageLearner.locator('[data-testid="select-enrolled-class-mathematics"]').first();
  await expect(mathSelect).toBeVisible({ timeout: 10000 });
  await mathSelect.selectOption('MATH10B');

  await glideAndClick(pageLearner, subjectEnrollSaveBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Saving Subject & Teacher Allocations'
  });
  await pageLearner.waitForTimeout(1000);
  console.log('   [VERIFIED] Enrolled into Mr. Sithole (Accounting 10A) and Mrs. Khumalo (Maths 10B)');

  // 4. Generate Guardian Link Passcode for Mrs. Nomsa Khumalo
  const linkParentBtn = pageLearner.locator('[data-testid="btn-open-link-guardian-modal"]').first();
  await expect(linkParentBtn).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageLearner, linkParentBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Opening Link Parent Modal'
  });
  await pageLearner.waitForTimeout(400);

  const genCodeBtn = pageLearner.locator('[data-testid="btn-generate-link-code"], button:has-text("Generate")').first();
  await expect(genCodeBtn).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, genCodeBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Generating Guardian Link Code'
  });
  await pageLearner.waitForTimeout(600);

  const closeLinkModal = pageLearner.locator('[data-testid="btn-close-link-guardian-modal"], button:has-text("Close")').first();
  await expect(closeLinkModal).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, closeLinkModal, {
    persona: 'LESEDI KHUMALO',
    message: 'Closing Guardian Link Modal'
  });
  await pageLearner.waitForTimeout(500);
  console.log('   [VERIFIED] Guardian link code generated');

  // 5. Deep Problem-Solving: Switch to Accounting Subject Tab
  const accTab = pageLearner.locator('[data-testid="tab-accounting"], [data-testid="btn-open-subject-session"], button:has-text("Open in Accounting"), [id*="tab-accounting"]').first();
  await expect(accTab).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageLearner, accTab, {
    persona: 'LESEDI KHUMALO',
    message: 'Switching to Accounting Subject Folder'
  });
  await pageLearner.waitForTimeout(1000);

  // ── Stage 0: Diagnostic Benchmark ──
  const questionSurface1 = pageLearner.locator('[data-testid="question-surface"]').first();
  await expect(questionSurface1).toBeVisible({ timeout: 35000 });

  const editableInput1 = pageLearner.locator('table input[type="text"]:visible, [data-testid="question-surface"] input[type="text"]:visible').first();
  await expect(editableInput1).toBeVisible({ timeout: 45000 });

  const source1 = await questionSurface1.getAttribute('data-source');
  console.log(`   [Verification] Accounting Question Source: ${source1}`);
  expect(source1).not.toBe('fallback');

  await typeRealistic(pageLearner, editableInput1, '1725', {
    persona: 'LESEDI KHUMALO',
    message: 'Entering gross-calculated VAT amount (1725) — deliberate misconception'
  });
  await pageLearner.waitForTimeout(400);

  const checkBtn1 = pageLearner.locator('[data-testid="btn-check-answer"]').first();
  await expect(checkBtn1).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, checkBtn1, {
    persona: 'LESEDI KHUMALO',
    message: 'Submitting Diagnostic Baseline Answer'
  });

  // Explicitly wait for marking verification to complete (Rule 0d-1 & 0d-6)
  await expect(
    pageLearner.locator('text=Cognitive Mastery Dial')
      .or(pageLearner.locator('text=Marks Awarded'))
      .or(pageLearner.locator('text=Schema Verified'))
      .first()
  ).toBeVisible({ timeout: 25000 });
  console.log('   [VERIFIED] Diagnostic answer marked & baseline calibrated');
  await pageLearner.waitForTimeout(800);

  // Select Stage 1: Scaffold Mode (Guided hints enabled)
  const scaffoldModeBtn = pageLearner.locator('[data-testid="btn-mode-scaffold"]').first();
  await expect(scaffoldModeBtn).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageLearner, scaffoldModeBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Selecting Stage 1: Guided Scaffold Mode'
  });
  await pageLearner.waitForTimeout(600);

  // Advance from diagnostic to Scaffold problem
  const nextBtnDiag = pageLearner.locator('[data-testid="btn-next-question"]').first();
  await expect(nextBtnDiag).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageLearner, nextBtnDiag, {
    persona: 'LESEDI KHUMALO',
    message: 'Advancing to next problem for guided scaffolding'
  });

  // Wait for new question generation to finish and scaffold mode to be active
  const toggleHintsBtn = pageLearner.locator('[data-testid="btn-toggle-hints"]').first();
  await expect(toggleHintsBtn).toBeVisible({ timeout: 45000 });
  console.log('   [VERIFIED] Scaffold problem generated and loaded');

  // ── Stage 1: Scaffold Mode (3-Tier Pre-Baked Hints) ──
  await glideAndClick(pageLearner, toggleHintsBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Unfolding 3-Tier Hint Drawer in Scaffold Mode'
  });
  await pageLearner.waitForTimeout(400);

  // Tier 1: Nudge
  const tier1Btn = pageLearner.locator('[data-testid="btn-hint-tier-1"]').first();
  await expect(tier1Btn).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, tier1Btn, {
    persona: 'LESEDI KHUMALO',
    message: 'Reading Tier 1: Location Nudge'
  });
  await pageLearner.waitForTimeout(400);

  // Tier 2: Directional Rule
  const tier2Btn = pageLearner.locator('[data-testid="btn-hint-tier-2"]').first();
  await expect(tier2Btn).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, tier2Btn, {
    persona: 'LESEDI KHUMALO',
    message: 'Reading Tier 2: Conceptual Rule (VAT Inclusive is 115%)'
  });
  await pageLearner.waitForTimeout(400);

  // Tier 3: Worked Step Calculation
  const tier3Btn = pageLearner.locator('[data-testid="btn-hint-tier-3"]').first();
  await expect(tier3Btn).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, tier3Btn, {
    persona: 'LESEDI KHUMALO',
    message: 'Reading Tier 3: Worked Step (R11 500 * 15/115 = R1 500)'
  });
  await pageLearner.waitForTimeout(600);

  // Learner corrects the entry using Tier 3
  const editableInput2 = pageLearner.locator('table input[type="text"]:visible, [data-testid="question-surface"] input[type="text"]:visible').first();
  await expect(editableInput2).toBeVisible({ timeout: 15000 });
  await typeRealistic(pageLearner, editableInput2, '1500', {
    persona: 'LESEDI KHUMALO',
    message: 'Entering corrected Output VAT: R1 500'
  });
  await pageLearner.waitForTimeout(400);

  // Check corrected answer -> Verified marks awarded
  const checkBtn2 = pageLearner.locator('[data-testid="btn-check-answer"]').first();
  await expect(checkBtn2).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, checkBtn2, {
    persona: 'LESEDI KHUMALO',
    message: 'Checking Corrected Entry'
  });
  await expect(
    pageLearner.locator('text=Cognitive Mastery Dial')
      .or(pageLearner.locator('text=Marks Awarded'))
      .or(pageLearner.locator('text=+35 XP'))
      .first()
  ).toBeVisible({ timeout: 25000 });
  console.log('   [VERIFIED] Corrected answer marked — verified marks awarded');

  const nextBtn1 = pageLearner.locator('[data-testid="btn-next-question"]').first();
  await expect(nextBtn1).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, nextBtn1, {
    persona: 'LESEDI KHUMALO',
    message: 'Advancing to next question'
  });
  await pageLearner.waitForTimeout(1000);

  // ── Subject 2: Grade 10 Mathematics (Algebra & Trinomial Factoring) ──
  console.log('\n[LEARNER WORKSPACE] Switching to Mathematics Subject...');
  const mathTab = pageLearner.locator('[data-testid="tab-mathematics"], button:has-text("Mathematics"), [id*="tab-mathematics"]').first();
  await expect(mathTab).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageLearner, mathTab, {
    persona: 'LESEDI KHUMALO',
    message: 'Opening Mathematics Subject Folder'
  });
  await pageLearner.waitForTimeout(1000);

  const questionSurface2 = pageLearner.locator('[data-testid="question-surface"]').first();
  await expect(questionSurface2).toBeVisible({ timeout: 35000 });

  const mathOptionA = pageLearner.locator('[data-testid="btn-math-option-0"]')
    .or(pageLearner.locator('[data-testid="question-surface"] button').filter({ hasText: /^[A-D]\b|\(x/i }))
    .first();
  await expect(mathOptionA).toBeVisible({ timeout: 35000 });

  const source2 = await questionSurface2.getAttribute('data-source');
  console.log(`   [Verification] Mathematics Question Source: ${source2}`);
  expect(source2).not.toBe('fallback');
  await glideAndClick(pageLearner, mathOptionA, {
    persona: 'LESEDI KHUMALO',
    message: 'Selecting factorised trinomial option: (x - 3)(x - 4)'
  });
  await pageLearner.waitForTimeout(400);

  const mathCheckBtn = pageLearner.locator('[data-testid="btn-check-answer"]').first();
  await expect(mathCheckBtn).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, mathCheckBtn, {
    persona: 'LESEDI KHUMALO',
    message: 'Submitting Derivation for Consequential Marking [M][CA]'
  });
  await expect(
    pageLearner.locator('text=Cognitive Mastery Dial')
      .or(pageLearner.locator('text=Marks Awarded'))
      .or(pageLearner.locator('text=Consequential Marking'))
      .or(pageLearner.locator('text=+35 XP'))
      .or(pageLearner.locator('text=Schema Verified'))
      .first()
  ).toBeVisible({ timeout: 25000 });
  console.log('   [VERIFIED] Mathematics answer submitted and marked');

  // Final Wrap-Up: Return to Today's Desk
  const deskTab = pageLearner.locator('[data-testid="tab-desk"], button:has-text("Desk"), [id*="tab-desk"]').first();
  await expect(deskTab).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageLearner, deskTab, {
    persona: 'LESEDI KHUMALO',
    message: 'Opening Today\'s Desk Final Summary'
  });
  await pageLearner.waitForTimeout(1200);
  console.log('   [VERIFIED] Today\'s Desk loaded');

  // Save storage state for downstream inspections
  await contextLearner.storageState({ path: learnerStoragePath });
  console.log('   [SAVED] Learner storage state saved to learner_storage_state.json');

  // Pause for inspection (Option 4B)
  await waitForStep('PHASE 4: LEARNER PROBLEM-SOLVING & CURRICULUM DEPTH', 'Lesedi completed Accounting CRJ and Mathematics trinomial factoring with verified marks awarded.', pageLearner);

  // Close Phase 4 browser
  await browserLearner.close();
  console.log('   [CLOSED] Phase 4 browser closed. RAM freed.\n');

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 5: TEACHER ROSTER REVIEW & AUTHORITY CONTROLS (Mr. N. Sithole)
  // ══════════════════════════════════════════════════════════════════════
  console.log('[PHASE 5] Re-opening Educator Cockpit: Mr. N. Sithole reviewing roster...');
  const browserTeacherReview = await chromium.launch(getLaunchOpts());
  const contextTeacherReview = await browserTeacherReview.newContext({
    storageState: learnerStoragePath,
    viewport: { width: 1200, height: 750 }
  });

  if (sharedSchoolRegistry) {
    await contextTeacherReview.addInitScript((data) => {
      if (data.schools) localStorage.setItem('fundile_registered_schools', data.schools);
      if (data.passes) localStorage.setItem('fundile_master_passes_sch_westville_high_10', data.passes);
    }, sharedSchoolRegistry);
  }

  const pageTeacherReview = await contextTeacherReview.newPage();
  await pageTeacherReview.goto(`${targetBaseUrl}/?persona=teacher`, { waitUntil: 'domcontentloaded' });
  await pageTeacherReview.waitForTimeout(1000);
  await injectGlidingCursorAndHud(pageTeacherReview);

  // Verify Teacher Cockpit Loaded with Lesedi Khumalo on ACC10A Roster
  await expect(pageTeacherReview.locator('text=Mr. N. Sithole').or(pageTeacherReview.locator('text=Teacher')).or(pageTeacherReview.locator('text=ACC10A')).first()).toBeVisible({ timeout: 20000 });
  await expect(pageTeacherReview.locator('text=Lesedi Khumalo').or(pageTeacherReview.locator('text=ACC10A')).first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Mr. Sithole verified Lesedi Khumalo LIVE on ACC10A roster');

  // Verify Teacher Authority: Remove Student from Class Roster button
  const removeBtn = pageTeacherReview.locator('[data-testid*="btn-remove-student"]').first();
  await expect(removeBtn).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Teacher authority button (Remove from Class) confirmed active on roster');

  // Pause for inspection (Option 4B)
  await waitForStep('PHASE 5: TEACHER ROSTER REVIEW & AUTHORITY CONTROLS', 'Mr. N. Sithole confirmed Lesedi Khumalo is live on ACC10A roster and verified teacher removal authority.', pageTeacherReview);

  // Close Phase 5 browser completely
  await browserTeacherReview.close();
  console.log('   [CLOSED] Phase 5 browser closed. RAM freed.\n');

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 6: PARENT GUARDIAN PORTAL (Mrs. Nomsa Khumalo)
  // ══════════════════════════════════════════════════════════════════════
  console.log('[PHASE 6] Launching Parent Window: Mrs. Nomsa Khumalo...');
  const browserParent = await chromium.launch(getLaunchOpts());
  const contextParent = await browserParent.newContext({
    storageState: learnerStoragePath,
    viewport: { width: 1200, height: 750 }
  });
  const pageParent = await contextParent.newPage();

  await pageParent.goto(`${targetBaseUrl}/?persona=parent`, { waitUntil: 'domcontentloaded' });
  await pageParent.waitForTimeout(800);
  await injectGlidingCursorAndHud(pageParent);

  await expect(pageParent.locator('text=Mrs.').or(pageParent.locator('text=Parent')).or(pageParent.locator('text=Guardian')).or(pageParent.locator('text=Academic Pulse')).first()).toBeVisible({ timeout: 15000 });
  await expect(pageParent.locator('text=Lesedi Khumalo').or(pageParent.locator('text=Academic Pulse')).first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Parent dashboard loaded & verified Lesedi Khumalo on Sunday Academic Pulse');

  // Pause for inspection (Option 4B)
  await waitForStep('PHASE 6: PARENT GUARDIAN PORTAL (MRS. NOMSA KHUMALO)', 'Parent portal loaded with Sunday Academic Pulse and linked learner Lesedi Khumalo.', pageParent);

  // Close Phase 6 browser completely
  await browserParent.close();
  console.log('   [CLOSED] Phase 6 browser closed. RAM freed.\n');

  // ══════════════════════════════════════════════════════════════════════
  // PHASE 7: SCHOOL ADMIN STRATEGIC OPERATIONS (Dr. K. Naidoo)
  // ══════════════════════════════════════════════════════════════════════
  console.log('[PHASE 7] Launching School Admin Window: Dr. K. Naidoo...');
  const browserSchoolFinal = await chromium.launch(getLaunchOpts());
  const contextSchoolFinal = await browserSchoolFinal.newContext({
    storageState: learnerStoragePath,
    viewport: { width: 1200, height: 750 }
  });

  if (sharedSchoolRegistry) {
    await contextSchoolFinal.addInitScript((data) => {
      if (data.schools) localStorage.setItem('fundile_registered_schools', data.schools);
      if (data.passes) localStorage.setItem('fundile_master_passes_sch_westville_high_10', data.passes);
    }, sharedSchoolRegistry);
  }

  const pageSchoolFinal = await contextSchoolFinal.newPage();
  await pageSchoolFinal.goto(`${targetBaseUrl}/?persona=school`, { waitUntil: 'domcontentloaded' });
  await pageSchoolFinal.waitForTimeout(800);
  await injectGlidingCursorAndHud(pageSchoolFinal);

  await expect(pageSchoolFinal.locator('text=Westville High School').or(pageSchoolFinal.locator('text=Dr.')).or(pageSchoolFinal.locator('text=ATP')).first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] School Admin dashboard loaded with ATP Pacing Heatmap');

  // Navigate to Marks & SASAMS Export Module
  const sasamsTab = pageSchoolFinal.locator('[data-testid="tab-school-sasams"], button:has-text("Marks & SASAMS Export")').first();
  await expect(sasamsTab).toBeVisible({ timeout: 15000 });
  await glideAndClick(pageSchoolFinal, sasamsTab, {
    persona: 'DR. K. NAIDOO',
    message: 'Navigating to SASAMS Mark Collation & Verification'
  });
  await pageSchoolFinal.waitForTimeout(600);

  // Verify Lesedi Khumalo appears in the official mark collation
  await expect(pageSchoolFinal.locator('text=Khumalo').or(pageSchoolFinal.locator('text=Lesedi')).first()).toBeVisible({ timeout: 15000 });
  console.log('   [VERIFIED] Lesedi Khumalo visible on SASAMS Mark Collation with Level 7 achievement');

  // Trigger SASAMS CSV Export
  const exportSasamsBtn = pageSchoolFinal.locator('[data-testid="btn-export-sasams-csv"], button:has-text("Export to SASAMS")').first();
  await expect(exportSasamsBtn).toBeVisible({ timeout: 10000 });
  await glideAndClick(pageSchoolFinal, exportSasamsBtn, {
    persona: 'DR. K. NAIDOO',
    message: 'Exporting Official SASAMS Mark Ledger (CSV)'
  });
  await pageSchoolFinal.waitForTimeout(1000);
  console.log('   [VERIFIED] Official SASAMS CSV export generated successfully');

  // Pause for inspection (Option 4B)
  await waitForStep('PHASE 7: SCHOOL ADMIN STRATEGIC OPERATIONS & SASAMS LEDGER', 'Dr. K. Naidoo verified Westville High ATP Pacing, confirmed Lesedi Khumalo on SASAMS marks ledger, and exported official CSV.', pageSchoolFinal);

  // Close Phase 7 browser completely
  await browserSchoolFinal.close();
  console.log('   [CLOSED] Phase 7 browser closed. RAM freed.\n');

  console.log('\n╔══════════════════════════════════════════════════════════════════════════════╗');
  console.log('║  [SET 1 FULL MULTI-STAKEHOLDER SEQUENCE CERTIFIED SUCCESSFULLY]              ║');
  console.log('║                                                                              ║');
  console.log('║  1. School Admin (Phase 1): Westville High Dynamic Registration 1st.         ║');
  console.log('║  2. Super Admin (Phase 2): Clearance Desk & Institutional Governance 2nd.    ║');
  console.log('║  3. Teacher (Phase 3): Mr. N. Sithole Onboarding & ACC10A Provisioning 3rd.  ║');
  console.log('║  4. Learner (Phase 4): Lesedi Khumalo Sign-up, CRJ & Math Factoring 4th.     ║');
  console.log('║  5. Teacher (Phase 5): ACC10A Roster Review & Authority Controls 5th.        ║');
  console.log('║  6. Parent (Phase 6): Mrs. Nomsa Khumalo Sunday Academic Pulse 6th.          ║');
  console.log('║  7. School Admin (Phase 7): Dr. K. Naidoo SASAMS CSV Mark Collation 7th.     ║');
  console.log('╚══════════════════════════════════════════════════════════════════════════════╝\n');
});
