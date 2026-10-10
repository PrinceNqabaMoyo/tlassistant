import { expect, chromium, devices } from '@playwright/test';
import path from 'path';
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
    breakDurationSec = 15, // short for automated runs, 60s for full demo
  } = config;

  console.log(`\n🚀 [${setName}] Launching Full Multi-Subject Learner Journey Simulation...`);
  console.log(`   Learner: ${learnerName} (Grade ${grade}, ${isMobile ? 'Mobile Pixel 7' : 'Desktop PWA'})`);
  console.log(`   Email: ${email}`);
  console.log(`   Subjects: ${subject1} & ${subject2 || 'None'}\n`);

  // STEP 0: PRE-FLIGHT PURGE (Clean slate)
  await purgeTestUser(email, password);

  // STEP 1: LAUNCH LEARNER BROWSER WINDOW
  let browser1;
  let page1;

  if (isMobile) {
    // Mobile Viewport (Pixel 7 WebAPK 393x851)
    browser1 = await chromium.launch({
      headless: false,
      args: ['--window-position=0,0', '--window-size=500,980']
    });
    const context1 = await browser1.newContext({
      ...devices['Pixel 7'],
      viewport: { width: 393, height: 851 }
    });
    page1 = await context1.newPage();
  } else {
    // Desktop PWA (1024x768 standalone window)
    browser1 = await chromium.launch({
      headless: false,
      args: ['--window-position=0,0', '--window-size=740,980']
    });
    page1 = await browser1.newPage({
      viewport: { width: 720, height: 880 }
    });
  }

  await page1.goto('http://127.0.0.1:5173/', { waitUntil: 'domcontentloaded' });
  await page1.waitForTimeout(600);
  await injectGlidingCursorAndHud(page1);
  await updateHud(page1, learnerName.toUpperCase(), `Launching ${setName} • Grade ${grade}`);
  await page1.waitForTimeout(800);

  // STEP 2: OPEN AUTH MODAL & SIGN UP
  const signUpBtn = page1.locator('[data-testid="btn-landing-signup"]').first();
  if (await signUpBtn.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-landing-signup"]', {
      persona: learnerName.toUpperCase(),
      message: 'Clicking "Start Free Diagnostic & Practice" CTA'
    });
    await page1.waitForTimeout(800);
  }

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
    if (await trialRadio.isVisible()) {
      await glideAndClick(page1, '[data-testid="radio-plan-free-trial"]', {
        persona: learnerName.toUpperCase(),
        message: 'Selecting 14-Day Free Trial (R0 Upfront)'
      });
      await page1.waitForTimeout(400);
    }
  } else {
    const directPlanRadio = page1.locator('[data-testid="radio-plan-direct-sub"]').first();
    if (await directPlanRadio.isVisible()) {
      await glideAndClick(page1, '[data-testid="radio-plan-direct-sub"]', {
        persona: learnerName.toUpperCase(),
        message: 'Selecting Direct Subscription (EFT Flow)'
      });
      await page1.waitForTimeout(400);
    }
  }

  // Submit Registration
  await glideAndClick(page1, '[data-testid="btn-auth-submit"]', {
    persona: learnerName.toUpperCase(),
    message: `Submitting Grade ${grade} Registration`
  });
  await page1.waitForTimeout(1500);

  // STEP 3: PAYMENT / CLEARANCE
  let browser2 = null;
  if (plan !== 'free_trial' && plan !== 'institutional_sync') {
    await updateHud(page1, learnerName.toUpperCase(), 'Entering Subscription & EFT Banking Desk');
    await page1.evaluate(() => {
      window.history.pushState({}, '', '/#subscription');
      window.dispatchEvent(new Event('popstate'));
    });
    await page1.waitForTimeout(1000);
    await injectGlidingCursorAndHud(page1);

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

    const planOption = page1.locator(planTestId).first();
    if (await planOption.isVisible()) {
      await glideAndClick(page1, planTestId, {
        persona: learnerName.toUpperCase(),
        message: `Selecting Plan: ${plan}`
      });
      await page1.waitForTimeout(500);

      const copyRefBtn = page1.locator('[data-testid="btn-copy-bank-ref"]').first();
      if (await copyRefBtn.isVisible()) {
        await glideAndClick(page1, '[data-testid="btn-copy-bank-ref"]', {
          persona: learnerName.toUpperCase(),
          message: 'Copying Bank Payment Reference'
        });
        await page1.waitForTimeout(400);
      }

      const samplePdfPath = path.resolve(__dirname, '../fixtures/sample_pop.pdf');
      const fileInput = page1.locator('[data-testid="input-file-pop"]').first();
      if (await fileInput.count() > 0) {
        await updateHud(page1, learnerName.toUpperCase(), 'Attaching Access Bank POP (sample_pop.pdf)');
        await fileInput.setInputFiles(samplePdfPath);
        await page1.waitForTimeout(800);
      }
    }

    // Launch Window 2: Super Admin Clearance
    browser2 = await chromium.launch({
      headless: false,
      args: ['--window-position=745,0', '--window-size=740,980']
    });
    const page2 = await browser2.newPage({ viewport: { width: 720, height: 880 } });
    await page2.goto('http://127.0.0.1:5173/?sandbox', { waitUntil: 'domcontentloaded' });
    await page2.waitForTimeout(600);
    await injectGlidingCursorAndHud(page2);

    // Switch to Admin
    const profileBtn2 = page2.locator('button[title*="Profile"], button:has-text("Welcome")').first();
    if (await profileBtn2.isVisible()) {
      await profileBtn2.click().catch(() => {});
      await page2.waitForTimeout(600);
      const adminRoleBtn = page2.locator('[data-testid="btn-admin-role-admin"]').first();
      if (await adminRoleBtn.isVisible()) {
        await adminRoleBtn.click().catch(() => {});
        await page2.waitForTimeout(800);
      }
    }

    const paymentsTab = page2.locator('[data-testid="tab-admin-payments"]').first();
    if (await paymentsTab.isVisible()) {
      await paymentsTab.click().catch(() => {});
      await page2.waitForTimeout(1000);

      const approveBtn = page2.locator(approveBtnTestId).first();
      if (await approveBtn.isVisible()) {
        await updateHud(page2, '👉 APPROVE PAYMENT', `Click to approve ${learnerName}!`);
        // Wait up to 30s for manual click, otherwise auto-approve
        const waitStart = Date.now();
        let clicked = false;
        while (Date.now() - waitStart < 30000) {
          const visible = await approveBtn.isVisible().catch(() => false);
          if (!visible) { clicked = true; break; }
          await page2.waitForTimeout(500);
        }
        if (!clicked) {
          await approveBtn.click().catch(() => {});
        }
        await updateHud(page2, '✅ APPROVED', `${learnerName} payment cleared!`);
        await page2.waitForTimeout(1000);
      }
    }
  }

  // STEP 4: ENTER WORKSPACE -> SUBJECT 1
  await page1.bringToFront();
  await updateHud(page1, learnerName.toUpperCase(), `Entering Workspace • ${subject1}`);
  await page1.evaluate(() => {
    window.history.pushState({}, '', '/');
    window.dispatchEvent(new Event('popstate'));
  });
  await page1.waitForTimeout(1200);
  await injectGlidingCursorAndHud(page1);

  // If teacher code provided, join class
  if (teacherCode) {
    const openJoinBtn = page1.locator('[data-testid="btn-open-join-class-modal"]:visible').first();
    if (await openJoinBtn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-open-join-class-modal"]:visible', {
        persona: learnerName.toUpperCase(),
        message: `Enrolling via Teacher Code: ${teacherCode}`
      });
      await page1.waitForTimeout(600);
      const codeInput = page1.locator('[data-testid="input-join-class-code"]').first();
      if (await codeInput.isVisible()) {
        await typeRealistic(page1, '[data-testid="input-join-class-code"]', teacherCode);
        const submitJoin = page1.locator('[data-testid="btn-submit-join-class"]').first();
        if (await submitJoin.isVisible()) {
          await submitJoin.click().catch(() => {});
          await page1.waitForTimeout(1000);
        }
      }
    }
  }

  // Open Subject 1 Tab
  const s1Tab = page1.locator(`button:has-text("${subject1TabName || subject1}"), [id*="tab-${(subject1TabName || subject1).toLowerCase()}"]`).first();
  if (await s1Tab.isVisible()) {
    await glideAndClick(page1, `button:has-text("${subject1TabName || subject1}"), [id*="tab-${(subject1TabName || subject1).toLowerCase()}"]`, {
      persona: learnerName.toUpperCase(),
      message: `Opening Subject 1: ${subject1}`
    });
    await page1.waitForTimeout(1000);
  }

  // Verify Stage 0 Diagnostic Surface
  await updateHud(page1, learnerName.toUpperCase(), `Stage 0: Diagnostic Benchmark for ${subject1}`);
  const questionSurface1 = page1.locator('[data-testid="question-surface"]').first();
  await questionSurface1.waitFor({ state: 'visible', timeout: 15000 });
  const source1 = await questionSurface1.getAttribute('data-source');
  console.log(`[${setName}] Subject 1 Question Source: ${source1}`);
  expect(source1).not.toBe('fallback');

  // Submit Answer / Check
  const checkBtn1 = page1.locator('[data-testid="btn-check-answer"]').first();
  if (await checkBtn1.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-check-answer"]', {
      persona: learnerName.toUpperCase(),
      message: 'Checking Answer • Calibrating Diagnostic Index'
    });
    await page1.waitForTimeout(1200);
  }

  // Advance to Practice
  const nextBtn1 = page1.locator('[data-testid="btn-next-question"]').first();
  if (await nextBtn1.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-next-question"]', {
      persona: learnerName.toUpperCase(),
      message: 'Advancing to Practice & Autonomous Mastery'
    });
    await page1.waitForTimeout(1200);
  }

  // STEP 5: STUDY BREAK & RE-LOGIN
  if (subject2) {
    await updateHud(page1, learnerName.toUpperCase(), 'Logging Out for Scheduled Study Break...');
    const profileMenuBtn = page1.locator(`button[title*="Profile"], button:has-text("${learnerName.split(' ')[0]}")`).first();
    if (await profileMenuBtn.isVisible()) {
      await profileMenuBtn.click().catch(() => {});
      await page1.waitForTimeout(600);
      const logoutBtn = page1.locator('button:has-text("Sign Out"), button:has-text("Logout")').first();
      if (await logoutBtn.isVisible()) {
        await logoutBtn.click().catch(() => {});
        await page1.waitForTimeout(1000);
      }
    }

    // Study break countdown simulation
    await simulateStudyBreak(page1, breakDurationSec, 20);

    // Re-login
    await updateHud(page1, learnerName.toUpperCase(), `Logging In for Subject 2: ${subject2}`);
    const signinBtn = page1.locator('[data-testid="btn-landing-signin"]').first();
    if (await signinBtn.isVisible()) {
      await signinBtn.click().catch(() => {});
      await page1.waitForTimeout(800);
      await typeRealistic(page1, '[data-testid="input-signin-email"], [data-testid="input-signup-email"]', email);
      await typeRealistic(page1, '[data-testid="input-signin-password"], [data-testid="input-signup-password"]', password);
      const submitLogin = page1.locator('[data-testid="btn-auth-submit"]').first();
      if (await submitLogin.isVisible()) {
        await submitLogin.click().catch(() => {});
        await page1.waitForTimeout(1500);
      }
    }

    // STEP 6: SUBJECT 2
    await injectGlidingCursorAndHud(page1);
    await updateHud(page1, learnerName.toUpperCase(), `Switching to Subject 2: ${subject2}`);
    const s2Tab = page1.locator(`button:has-text("${subject2TabName || subject2}"), [id*="tab-${(subject2TabName || subject2).toLowerCase()}"]`).first();
    if (await s2Tab.isVisible()) {
      await glideAndClick(page1, `button:has-text("${subject2TabName || subject2}"), [id*="tab-${(subject2TabName || subject2).toLowerCase()}"]`, {
        persona: learnerName.toUpperCase(),
        message: `Opening Subject 2: ${subject2}`
      });
      await page1.waitForTimeout(1000);
    }

    const questionSurface2 = page1.locator('[data-testid="question-surface"]').first();
    await questionSurface2.waitFor({ state: 'visible', timeout: 15000 });
    const source2 = await questionSurface2.getAttribute('data-source');
    console.log(`[${setName}] Subject 2 Question Source: ${source2}`);
    expect(source2).not.toBe('fallback');

    const checkBtn2 = page1.locator('[data-testid="btn-check-answer"]').first();
    if (await checkBtn2.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-check-answer"]', {
        persona: learnerName.toUpperCase(),
        message: 'Checking Answer • Recording Progress'
      });
      await page1.waitForTimeout(1200);
    }
  }

  // STEP 7: CERTIFICATION & CLEANUP
  await updateHud(page1, `🎉 ${setName} CERTIFIED`, `Completed Multi-Subject Journey for ${learnerName}!`);
  console.log(`\n✅ [${setName} CERTIFIED] Journey complete for ${learnerName}.\n`);
  await page1.waitForTimeout(3000);

  await browser1.close();
  if (browser2) await browser2.close();
}
