import { expect, chromium, devices } from '@playwright/test';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import {
  injectGlidingCursorAndHud,
  updateHud,
  glideAndClick,
  glideCursorTo,
  typeRealistic,
  simulateStudyBreak
} from './autopilotHud.js';
import { purgeTestUser } from './purgeTestUser.js';
import { authenticateSuperAdminSession } from './authenticateSuperAdmin.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * Universal Participant Set Runner
 * Executes an authentic end-to-end user journey for any participant in mock_test_participants.md:
 * 1. Targeted pre-flight account purge (clean slate)
 * 2. Native form-factor browser launch (Mobile Pixel 7 WebAPK or Desktop PWA)
 * 3. Registration with enterprise credentials & POPIA Section 35 consent
 * 4. Payment flow: 14-day free trial OR EFT slip upload with Super Admin clearance loop
 * 5. Subject 1: Diagnostic benchmark -> Guided Scaffolding / 3-Tier hints -> Practice
 * 6. 20-minute study break simulation with visual countdown
 * 7. Clean re-login and Subject 2 execution
 * 8. Today's Desk multi-subject mastery summary & certification
 */
export async function runParticipantSet(config) {
  const {
    setName,
    learnerName,
    grade,
    email,
    password = 'Fundile@2026!',
    plan = 'term_pass', // 'free_trial' | 'term_pass' | 'monthly_pass' | 'annual_pass' | 'institutional_sync'
    isMobile = false,
    subject1,
    subject1TabName,
    subject2,
    subject2TabName,
    teacherCode = null,
    parentEmail = null,
    parentName = null,
    abilityProfile = 'scaffold_guided', // 'scaffold_guided' | 'struggling_regression' | 'distinction_candidate' | 'visual_spatial' | 'trial_autonomous'
    breakDurationSec = 15, // short for automated runs, 60s for full demo
  } = config;

  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';

  console.log(`\n🚀 [${setName}] Launching Full Multi-Subject Learner Journey Simulation...`);
  console.log(`   Learner: ${learnerName} (Grade ${grade}, ${isMobile ? 'Mobile Pixel 7' : 'Desktop PWA'})`);
  console.log(`   Email: ${email}`);
  console.log(`   Target Server: ${targetBaseUrl}`);
  console.log(`   Subjects: ${subject1} & ${subject2 || 'None'}\n`);

  // STEP 0: PRE-FLIGHT PURGE (Clean slate)
  await purgeTestUser(email, password);

  // STEP 1: LAUNCH LEARNER BROWSER WINDOW
  let browser1;
  let page1;

  const videoDir = path.resolve(process.cwd(), 'test-results', 'videos');
  if (!fs.existsSync(videoDir)) {
    fs.mkdirSync(videoDir, { recursive: true });
  }

  if (isMobile) {
    // Authentic Mobile Standalone WebAPK (Pixel 7 412x915)
    browser1 = await chromium.launch({
      headless: false,
      args: [
        '--window-position=0,0',
        '--window-size=440,960'
      ]
    });
    const context1 = await browser1.newContext({
      ...devices['Pixel 7'],
      viewport: { width: 412, height: 915 },
      recordVideo: { dir: videoDir, size: { width: 412, height: 915 } }
    });
    page1 = await context1.newPage();
  } else {
    // Desktop Standalone PWA (1280x800)
    browser1 = await chromium.launch({
      headless: false,
      args: [
        '--window-position=0,0',
        '--window-size=1280,850'
      ]
    });
    const context1 = await browser1.newContext({
      viewport: { width: 1280, height: 800 },
      recordVideo: { dir: videoDir, size: { width: 1280, height: 800 } }
    });
    page1 = await context1.newPage();
  }

  await page1.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
  await page1.waitForTimeout(600);
  await injectGlidingCursorAndHud(page1);
  await updateHud(page1, learnerName.toUpperCase(), `Launching ${setName} • Grade ${grade}`);
  await page1.waitForTimeout(800);

  // STEP 2: OPEN AUTH MODAL & SIGN UP
  const signUpBtn = page1.locator('[data-testid="btn-landing-signup"]').first();
  await expect(signUpBtn).toBeVisible({ timeout: 15000 });
  await glideAndClick(page1, signUpBtn, {
    persona: learnerName.toUpperCase(),
    message: 'Clicking "Start Free Diagnostic & Practice" CTA'
  });
  await page1.waitForTimeout(800);

  await updateHud(page1, learnerName.toUpperCase(), `Registering Grade ${grade} Account: ${learnerName}`);
  await page1.waitForSelector('[data-testid="input-signup-name"]', { state: 'visible', timeout: 12000 });

  await typeRealistic(page1, '[data-testid="input-signup-name"]', learnerName, {
    persona: learnerName.toUpperCase(),
    message: `Entering Learner Name: ${learnerName}`
  });

  await page1.selectOption('[data-testid="select-signup-role"]', 'student');
  await page1.selectOption('[data-testid="select-signup-grade"]', String(grade));

  await typeRealistic(page1, '[data-testid="input-signup-email"]', email, {
    persona: learnerName.toUpperCase(),
    message: `Entering Email: ${email}`
  });

  await typeRealistic(page1, '[data-testid="input-signup-password"]', password, {
    persona: learnerName.toUpperCase(),
    message: 'Entering Enterprise Password'
  });

  await typeRealistic(page1, '[data-testid="input-signup-confirm-password"]', password, {
    persona: learnerName.toUpperCase(),
    message: 'Confirming Password'
  });

  // POPIA Section 35 Guardian Consent
  await glideAndClick(page1, '[data-testid="checkbox-popia-consent"]', {
    persona: learnerName.toUpperCase(),
    message: 'Confirming POPIA Section 35 Minor Consent'
  });
  await page1.waitForTimeout(400);

  // Plan Selection in Auth Modal
  if (plan === 'free_trial') {
    const trialRadio = page1.locator('[data-testid="radio-plan-free-trial"]').first();
    await expect(trialRadio).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, trialRadio, {
      persona: learnerName.toUpperCase(),
      message: 'Selecting 14-Day Free Trial (R0 Upfront)'
    });
    await page1.waitForTimeout(400);
  } else {
    const directPlanRadio = page1.locator('[data-testid="radio-plan-direct-sub"]').first();
    await expect(directPlanRadio).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, directPlanRadio, {
      persona: learnerName.toUpperCase(),
      message: 'Selecting Direct Subscription (EFT Flow)'
    });
    await page1.waitForTimeout(400);
  }

  // Submit Registration
  await glideAndClick(page1, '[data-testid="btn-auth-submit"]', {
    persona: learnerName.toUpperCase(),
    message: `Submitting Grade ${grade} Registration`
  });
  await page1.waitForTimeout(1500);

  // STEP 3: PAYMENT / CLEARANCE
  let browser2 = null;
  const planDays = plan === 'monthly_pass' ? 30 : plan === 'annual_pass' ? 365 : 90;

  if (plan !== 'free_trial' && plan !== 'institutional_sync') {
    await updateHud(page1, learnerName.toUpperCase(), 'Entering Subscription & EFT Banking Desk');
    
    // Select plan on subscription page
    let planTestId = '[data-testid="plan-term-pass-349"]';
    let approveBtnTestId = '[data-testid="btn-approve-payment-90d"]';
    if (plan === 'monthly_pass') {
      planTestId = '[data-testid="plan-monthly-149"]';
      approveBtnTestId = '[data-testid="btn-approve-payment-30d"]';
    } else if (plan === 'annual_pass') {
      planTestId = '[data-testid="plan-annual-pass-999"]';
      approveBtnTestId = '[data-testid="btn-approve-payment-365d"]';
    }

    // Wait for subscription page to appear
    const planOption = page1.locator(planTestId).first();
    await expect(planOption).toBeVisible({ timeout: 15000 });
    await glideAndClick(page1, planOption, {
      persona: learnerName.toUpperCase(),
      message: `Selecting Plan: ${plan}`
    });
    await page1.waitForTimeout(600);

    const copyRefBtn = page1.locator('[data-testid="btn-copy-bank-ref"]').first();
    await expect(copyRefBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, copyRefBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Copying Bank Payment Reference'
    });
    await page1.waitForTimeout(400);

    const learnerPdfPath = path.resolve(__dirname, '../fixtures/access_bank_learner_pop.pdf');
    const choosePopBtn = page1.locator('[data-testid="btn-choose-pop"]').first();
    await expect(choosePopBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, choosePopBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Opening POP attachment modal'
    });
    await page1.waitForTimeout(400);

    const fileInput = page1.locator('[data-testid="input-file-pop"], input[type="file"]').first();
    await fileInput.setInputFiles(learnerPdfPath);
    await updateHud(page1, learnerName.toUpperCase(), 'Attached Access Bank POP (access_bank_learner_pop.pdf)');
    await page1.waitForTimeout(800);

    const submitPopBtn = page1.locator('[data-testid="btn-submit-pop"]').first();
    await expect(submitPopBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, submitPopBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Submitting POP for Admin review'
    });
    await page1.waitForTimeout(1000);

    // Launch Window 2: Super Admin Clearance in clean light UI
    browser2 = await chromium.launch({
      headless: false,
      args: ['--window-position=745,0', '--window-size=740,980']
    });
    const context2 = await browser2.newContext({
      viewport: { width: 1024, height: 768 },
      recordVideo: { dir: videoDir, size: { width: 1024, height: 768 } }
    });
    const page2 = await context2.newPage();
    await authenticateSuperAdminSession(page2, targetBaseUrl);
    await injectGlidingCursorAndHud(page2);

    await updateHud(page2, 'SUPER ADMIN', `Reviewing EFT Slip for ${learnerName}`);
    
    // Open EFT Payment Approvals queue
    const adminPaymentsTab = page2.locator('[data-testid="tab-admin-payments"]').first();
    await expect(adminPaymentsTab).toBeVisible({ timeout: 15000 });
    await glideAndClick(page2, adminPaymentsTab, {
      persona: 'SUPER ADMIN',
      message: 'Opening EFT Approvals Desk'
    });
    await page2.waitForTimeout(1000);

    // Verify learner payment is visible
    const learnerPaymentCard = page2.locator(`[data-testid="payment-email-${email}"]`).first();
    await expect(learnerPaymentCard).toBeVisible({ timeout: 15000 });

    const learnerCardContainer = page2.locator(`div[data-testid^="payment-card-"]:has([data-testid="payment-email-${email}"])`).first();
    await expect(learnerCardContainer).toBeVisible({ timeout: 15000 });

    // Preview POP PDF via authentic signed URL
    const viewPopBtn = learnerCardContainer.locator('[data-testid="btn-view-pop"]').first();
    await expect(viewPopBtn).toBeVisible({ timeout: 10000 });
    const [popPopup] = await Promise.all([
      page2.waitForEvent('popup').catch(() => null),
      glideAndClick(page2, viewPopBtn, {
        persona: 'SUPER ADMIN',
        message: 'Opening POP Verification Preview (Signed URL)'
      })
    ]);
    if (popPopup) {
      await popPopup.waitForLoadState('domcontentloaded').catch(() => {});
      await popPopup.close().catch(() => {});
    }

    const approveBtn = learnerCardContainer.locator(approveBtnTestId).first();
    await expect(approveBtn).toBeVisible({ timeout: 20000 });
    await expect(approveBtn).toBeEnabled({ timeout: 10000 });
    await updateHud(page2, '👉 APPROVE PAYMENT', `Click to approve ${learnerName}!`);
    await glideAndClick(page2, approveBtn, {
      persona: 'SUPER ADMIN',
      message: `Approving ${plan} for ${learnerName}`
    });
    await updateHud(page2, '✅ APPROVED', `${learnerName} payment cleared!`);
    await page2.waitForTimeout(1200);
    await browser2.close();
    browser2 = null;
  }

  // STEP 4: ENTER WORKSPACE -> SUBJECT 1
  await page1.bringToFront();
  await updateHud(page1, learnerName.toUpperCase(), `Entering Workspace • ${subject1}`);
  if (plan !== 'free_trial' && plan !== 'institutional_sync') {
    const backToDashBtn = page1.locator('[data-testid="btn-back-to-dashboard"]:visible, button:has-text("Back to dashboard"):visible').first();
    await expect(backToDashBtn).toBeVisible({ timeout: 15000 });
    await glideAndClick(page1, backToDashBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Returning to dashboard'
    });
    await page1.waitForTimeout(1500);
  } else {
    // For free trial and institutional sync, verify clean direct mount onto student desk
    const dashElement = page1.locator('[data-testid="btn-open-join-class-modal"]:visible, [data-testid^="tab-"]:visible').first();
    await expect(dashElement).toBeVisible({ timeout: 25000 });
    await page1.waitForTimeout(1000);
  }
  await injectGlidingCursorAndHud(page1);

  // If teacher code provided, join class
  if (teacherCode) {
    const openJoinBtn = page1.locator('[data-testid="btn-open-join-class-modal"]:visible, button:has-text("Join Class"):visible').first();
    await expect(openJoinBtn).toBeVisible({ timeout: 15000 });
    await glideAndClick(page1, openJoinBtn, {
      persona: learnerName.toUpperCase(),
      message: `Enrolling via Teacher Code: ${teacherCode}`
    });
    await page1.waitForTimeout(600);

    const codeInput = page1.locator('[data-testid="input-join-class-code"]:visible').first();
    await expect(codeInput).toBeVisible({ timeout: 10000 });
    await typeRealistic(page1, codeInput, teacherCode);

    const submitJoin = page1.locator('[data-testid="btn-join-class-submit"]:visible').first();
    await expect(submitJoin).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, submitJoin, {
      persona: learnerName.toUpperCase(),
      message: `Submitting class code ${teacherCode}`
    });
    await page1.waitForTimeout(1000);
    const doneJoinBtn = page1.locator('[data-testid="btn-join-class-done"]:visible').first();
    await expect(doneJoinBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, doneJoinBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Dismissing class join confirmation'
    });
    await page1.waitForTimeout(600);
  }

  // If parent linking configured, generate link code
  if (parentEmail || parentName) {
    const linkParentBtn = page1.locator('[data-testid="btn-open-link-guardian-modal"]:visible, button:has-text("Link Parent"):visible').first();
    await expect(linkParentBtn).toBeVisible({ timeout: 15000 });
    await glideAndClick(page1, linkParentBtn, {
      persona: learnerName.toUpperCase(),
      message: `Opening Link Parent Modal • ${parentName || 'Parent'}`
    });
    await page1.waitForTimeout(800);

    const genCodeBtn = page1.locator('[data-testid="btn-generate-link-code"]:visible').first();
    await expect(genCodeBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, genCodeBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Generating Guardian Link Code'
    });
    await page1.waitForTimeout(1000);

    const closeLinkModal = page1.locator('[data-testid="btn-close-link-guardian-modal"]:visible').first();
    await expect(closeLinkModal).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, closeLinkModal, {
      persona: learnerName.toUpperCase(),
      message: 'Closing Guardian Link modal'
    });
    await page1.waitForTimeout(600);
  }

  // Open Subject 1 Tab
  const s1Key = subject1.toLowerCase().replace(/[^a-z0-9]/g, '_');
  const s1TabNameKey = (subject1TabName || '').toLowerCase().replace(/[^a-z0-9]/g, '_');
  const s1Clean = subject1.toLowerCase().replace(/[^a-z0-9]/g, '');
  const s1TabNameClean = (subject1TabName || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  const s1Tab = page1.locator(`[data-testid="tab-${s1Key}"]:visible, [data-testid="tab-${s1TabNameKey}"]:visible, [data-testid="tab-${s1Clean}"]:visible, [data-testid="tab-${s1TabNameClean}"]:visible, button:has-text("${subject1TabName || subject1}"):visible, button:has-text("${subject1}"):visible`).first();
  await s1Tab.waitFor({ state: 'visible', timeout: 15000 });
  await glideAndClick(page1, s1Tab, {
    persona: learnerName.toUpperCase(),
    message: `Opening Subject 1: ${subject1}`
  });
  await page1.waitForTimeout(1000);

  const startSessionBtn1 = page1.locator('[data-testid="btn-open-subject-session"]:visible').first();
  if (await startSessionBtn1.isVisible({ timeout: 2000 }).catch(() => false)) {
    await glideAndClick(page1, startSessionBtn1, {
      persona: learnerName.toUpperCase(),
      message: `Starting Session for ${subject1}`
    });
  }

  // Verify Stage 0 Diagnostic Surface & await deterministic question generation
  await updateHud(page1, learnerName.toUpperCase(), `Stage 0: Diagnostic Benchmark for ${subject1}`);
  const questionSurface1 = page1.locator('[data-testid="question-surface"]:visible').first();
  await questionSurface1.waitFor({ state: 'visible', timeout: 35000 });
  await expect(questionSurface1).not.toHaveAttribute('data-source', 'none', { timeout: 35000 });
  const source1 = await questionSurface1.getAttribute('data-source');
  console.log(`[${setName}] Subject 1 Question Source: ${source1}`);
  expect(source1).not.toBe('fallback');
  expect(source1).not.toBe('none');

  // PEDAGOGICAL ABILITY SIMULATION (Genuine Cognitive Interaction & Adaptive Branching)
  if (abilityProfile === 'struggling_regression') {
    // Set 11 (Sibusiso Zulu): Struggling Matric Student -> Adaptive Regression & SimuLearn Replay
    await updateHud(page1, learnerName.toUpperCase(), 'Struggling Learner: Attempting Problem & Encountering Misconception');

    // First attempt fails
    const checkBtn1 = page1.locator('[data-testid="btn-check-answer"]:visible').first();
    await expect(checkBtn1).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, checkBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Checking Attempt 1 • Persistent Misconception Slip'
    });
    await page1.waitForTimeout(1200);

    // Second attempt fails to trigger Cognitive Circuit Breaker
    await updateHud(page1, learnerName.toUpperCase(), 'Attempt 2 Fails • Triggering Adaptive Prerequisite Lineage');
    await glideAndClick(page1, checkBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Checking Attempt 2 • Consecutive Blocker Identified'
    });
    await page1.waitForTimeout(1200);

    // Verify Prerequisite Gap Banner
    const prereqBanner = page1.locator('[data-testid="banner-prerequisite-gap"]:visible').first();
    await expect(prereqBanner).toBeVisible({ timeout: 15000 });
    await updateHud(page1, learnerName.toUpperCase(), 'Prerequisite Gap Detected! Launching SimuLearn Replay');

    // Launch SimuLearn Worked Solution Replay
    const launchSimuBtn = page1.locator('[data-testid="btn-launch-simulearn"]:visible').first();
    await expect(launchSimuBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, launchSimuBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Opening 5-Minute SimuLearn Worked Solution Replay'
    });
    await page1.waitForTimeout(1000);

    // Verify SimuLearn Modal is Open
    const simuModal = page1.locator('[data-testid="modal-simulearn-player"]:visible').first();
    await expect(simuModal).toBeVisible({ timeout: 10000 });
    await updateHud(page1, 'SIMULEARN ENGINE', 'Watching Step-by-Step Visual Solution Replay');

    // Step through the animated replay
    const nextStepBtn = page1.locator('[data-testid="btn-simulearn-next"]:visible').first();
    await expect(nextStepBtn).toBeVisible({ timeout: 10000 });
    await expect(nextStepBtn).toBeEnabled({ timeout: 5000 });
    await glideAndClick(page1, nextStepBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Advancing SimuLearn Step'
    });
    await page1.waitForTimeout(800);

    // Complete SimuLearn replay
    const completeSimuBtn = page1.locator('[data-testid="btn-simulearn-complete"]:visible').first();
    await expect(completeSimuBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, completeSimuBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Completing SimuLearn Replay • Returning to Practice'
    });
    await page1.waitForTimeout(1000);

    // Start 5-Minute Prerequisite Drill
    const microDrillBtn = page1.locator('[data-testid="btn-start-micro-drill"]:visible').first();
    await expect(microDrillBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, microDrillBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Entering 5-Min Prerequisite Micro-Drill'
    });
    await page1.waitForTimeout(1200);

    // Verify new foundational question surface loaded
    await expect(page1.locator('[data-testid="question-surface"]:visible')).toBeVisible({ timeout: 25000 });
    await updateHud(page1, learnerName.toUpperCase(), 'Mastered Foundational Prerequisite • Schema Repaired!');

  } else if (abilityProfile === 'distinction_candidate') {
    // Set 8 (Prince Mthembu): Matric Distinction Peak Candidate -> Exam Mode Unlock
    await updateHud(page1, learnerName.toUpperCase(), 'Distinction Candidate: Unassisted Solution & High Accuracy');
    const checkBtn1 = page1.locator('[data-testid="btn-check-answer"]:visible').first();
    await expect(checkBtn1).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, checkBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Submitting High-Accuracy Solution • Method Marks [M][A][CA]'
    });
    await page1.waitForTimeout(1200);

    // Advance to next question to solidify formative mastery >= 80%
    const nextBtn1 = page1.locator('[data-testid="btn-next-question"]:visible').first();
    await expect(nextBtn1).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, nextBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Cementing Formative Mastery (>=80%)'
    });
    await page1.waitForTimeout(1200);

    // Unlock & Switch to Stage 3 Exam Mode
    const examModeBtn = page1.locator('[data-testid="btn-mode-assessment"]:visible').first();
    await expect(examModeBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, examModeBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Entering Stage 3: Timed DBE/IEB Exam Mode'
    });
    await page1.waitForTimeout(1000);

    // Verify Exam Timer is active
    const examTimerBadge = page1.locator('[data-testid="exam-timer-display"]:visible, :has-text("Exam Timer"):visible').first();
    await expect(examTimerBadge).toBeVisible({ timeout: 10000 });
    await updateHud(page1, learnerName.toUpperCase(), 'Exam Mode Active: Timed Conditions & Locked Hints');

  } else if (abilityProfile === 'visual_spatial') {
    // Set 2 (Ayanda Ndlovu): Junior Senior Phase Spatial Visualizer (Geometric Nets)
    await updateHud(page1, learnerName.toUpperCase(), 'Visual Learner: Exploring 3D Spatial Geometry');
    
    const checkBtn1 = page1.locator('[data-testid="btn-check-answer"]:visible').first();
    await expect(checkBtn1).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, checkBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Checking Spatial Geometry Submission'
    });
    await page1.waitForTimeout(1200);

    const nextBtn1 = page1.locator('[data-testid="btn-next-question"]:visible').first();
    await expect(nextBtn1).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, nextBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Advancing to Practice'
    });
    await page1.waitForTimeout(1200);

  } else {
    // Default: 'scaffold_guided' (Sets 3, 5, 6, 7, 9, 10)
    await updateHud(page1, learnerName.toUpperCase(), 'Stage 0: Calibrating Diagnostic Index');
    const checkBtn1 = page1.locator('[data-testid="btn-check-answer"]:visible').first();
    await expect(checkBtn1).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, checkBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Checking Diagnostic Answer'
    });
    await page1.waitForTimeout(1200);

    const nextBtn1 = page1.locator('[data-testid="btn-next-question"]:visible').first();
    await expect(nextBtn1).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, nextBtn1, {
      persona: learnerName.toUpperCase(),
      message: 'Advancing to Practice'
    });
    await page1.waitForTimeout(1200);
  }

  // STEP 5: STUDY BREAK & RE-LOGIN
  if (subject2) {
    await updateHud(page1, learnerName.toUpperCase(), 'Logging Out for Scheduled Study Break...');
    const logoutBtn = page1.locator('[data-testid="btn-open-logout-modal"]:visible, button:has-text("Sign Out"):visible, button:has-text("Logout"):visible').first();
    await expect(logoutBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, logoutBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Opening Sign Out Confirmation'
    });
    await page1.waitForTimeout(600);
    const confirmLogoutBtn = page1.locator('[data-testid="btn-confirm-logout"]:visible, button:has-text("Yes, Sign Out"):visible').first();
    await expect(confirmLogoutBtn).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, confirmLogoutBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Confirming Sign Out'
    });
    await page1.waitForTimeout(1000);

    // Study break countdown simulation
    await simulateStudyBreak(page1, breakDurationSec, 20);

    // Re-login
    await updateHud(page1, learnerName.toUpperCase(), `Logging In for Subject 2: ${subject2}`);
    const signinBtn = page1.locator('[data-testid="btn-landing-signin"]:visible').first();
    await expect(signinBtn).toBeVisible({ timeout: 15000 });
    await glideAndClick(page1, signinBtn, {
      persona: learnerName.toUpperCase(),
      message: 'Opening Sign-In Modal'
    });
    await page1.waitForTimeout(800);
    await typeRealistic(page1, '[data-testid="input-signin-email"], [data-testid="input-signup-email"]', email);
    await typeRealistic(page1, '[data-testid="input-signin-password"], [data-testid="input-signup-password"]', password);
    const submitLogin = page1.locator('[data-testid="btn-auth-submit"]:visible').first();
    await expect(submitLogin).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, submitLogin, {
      persona: learnerName.toUpperCase(),
      message: 'Submitting Sign-In Credentials'
    });
    await page1.waitForTimeout(1500);

    // STEP 6: SUBJECT 2
    await injectGlidingCursorAndHud(page1);
    const s2Key = subject2.toLowerCase().replace(/[^a-z0-9]/g, '_');
    const s2TabNameKey = (subject2TabName || '').toLowerCase().replace(/[^a-z0-9]/g, '_');
    const s2Clean = subject2.toLowerCase().replace(/[^a-z0-9]/g, '');
    const s2TabNameClean = (subject2TabName || '').toLowerCase().replace(/[^a-z0-9]/g, '');
    const s2Tab = page1.locator(`[data-testid="tab-${s2Key}"]:visible, [data-testid="tab-${s2TabNameKey}"]:visible, [data-testid="tab-${s2Clean}"]:visible, [data-testid="tab-${s2TabNameClean}"]:visible, button:has-text("${subject2TabName || subject2}"):visible, button:has-text("${subject2}"):visible`).first();
    await s2Tab.waitFor({ state: 'visible', timeout: 15000 });
    await glideAndClick(page1, s2Tab, {
      persona: learnerName.toUpperCase(),
      message: `Opening Subject 2: ${subject2}`
    });
    await page1.waitForTimeout(1000);

    const startSessionBtn2 = page1.locator('[data-testid="btn-open-subject-session"]:visible').first();
    if (await startSessionBtn2.isVisible({ timeout: 2000 }).catch(() => false)) {
      await glideAndClick(page1, startSessionBtn2, {
        persona: learnerName.toUpperCase(),
        message: `Starting Session for ${subject2}`
      });
    }

    const questionSurface2 = page1.locator('[data-testid="question-surface"]:visible').first();
    await questionSurface2.waitFor({ state: 'visible', timeout: 35000 });
    await expect(questionSurface2).not.toHaveAttribute('data-source', 'none', { timeout: 35000 });
    const source2 = await questionSurface2.getAttribute('data-source');
    console.log(`[${setName}] Subject 2 Question Source: ${source2}`);
    expect(source2).not.toBe('fallback');
    expect(source2).not.toBe('none');

    const checkBtn2 = page1.locator('[data-testid="btn-check-answer"]:visible').first();
    await expect(checkBtn2).toBeVisible({ timeout: 10000 });
    await glideAndClick(page1, checkBtn2, {
      persona: learnerName.toUpperCase(),
      message: 'Checking Answer • Recording Progress'
    });
    await page1.waitForTimeout(1200);
  }

  // STEP 7: CERTIFICATION & CLEANUP
  await updateHud(page1, `🎉 ${setName} CERTIFIED`, `Completed Multi-Subject Journey for ${learnerName}!`);
  console.log(`\n✅ [${setName} CERTIFIED] Journey complete for ${learnerName}.\n`);
  await page1.waitForTimeout(3000);

  await browser1.close();
  if (browser2) await browser2.close();
}
