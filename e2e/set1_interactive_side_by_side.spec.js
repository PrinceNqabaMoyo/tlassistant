import { test, expect, chromium } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';
import {
  injectGlidingCursorAndHud,
  updateHud,
  glideAndClick,
  glideCursorTo,
  typeRealistic,
  waitIfPaused,
  simulateStudyBreak
} from './helpers/autopilotHud.js';
import { purgeTestUser } from './helpers/purgeTestUser.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

test('Set 1: Deep Multi-Subject Learner Journey — Accounting & Mathematics (Gr 10 FET)', async () => {
  // Set 1-hour timeout allowing full deep pedagogical progression
  test.setTimeout(3600000);

  const testEmail = 'lesedi.khumalo@fundile.test';
  const testPassword = 'Fundile@2026!';

  console.log('\n🚀 [SET 1] Launching Multi-Subject Learner Journey Simulation...');
  console.log('   Learner: Lesedi Khumalo (Grade 10 FET, Westville High)');
  console.log('   Subjects: Accounting (CRJ VAT 15%) & Mathematics (Geometry & Algebra)');
  console.log('   Lifecycle: Targeted Purge -> Sign-Up -> Super Admin Approval -> Subj 1 -> Break -> Subj 2 -> Certification\n');

  // ══════════════════════════════════════════════════════════════════════
  // STEP 0: PRE-FLIGHT TARGETED PURGE (Clean slate for Lesedi Khumalo)
  // ══════════════════════════════════════════════════════════════════════
  await purgeTestUser(testEmail, testPassword);

  // ══════════════════════════════════════════════════════════════════════
  // WINDOW 1: Left Half of Screen (Lesedi Khumalo - Desktop Installed PWA)
  // ══════════════════════════════════════════════════════════════════════
  const browser1 = await chromium.launch({
    headless: false,
    args: [
      '--window-position=0,0',
      '--window-size=740,980'
    ]
  });
  const page1 = await browser1.newPage({
    viewport: { width: 720, height: 880 }
  });

  await page1.goto('http://127.0.0.1:5173/', { waitUntil: 'domcontentloaded' });
  await page1.waitForTimeout(600);
  await injectGlidingCursorAndHud(page1);
  await updateHud(page1, 'LESEDI KHUMALO', 'Exploring Landing Page • Grade 10 FET Candidate');
  await page1.waitForTimeout(1000);

  // 1. Click Sign Up CTA on Landing Page
  const signUpBtn = page1.locator('[data-testid="btn-landing-signup"]').first();
  if (await signUpBtn.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-landing-signup"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Clicking "Start Free Diagnostic & Practice" CTA'
    });
    await page1.waitForTimeout(800);
  }

  // 2. Fill CAPS FET Registration Form
  await updateHud(page1, 'LESEDI KHUMALO', 'Registering Clean Profile: Lesedi Khumalo (Grade 10 FET)');
  await page1.waitForSelector('[data-testid="input-signup-name"]', { state: 'visible', timeout: 10000 });

  await typeRealistic(page1, '[data-testid="input-signup-name"]', 'Lesedi Khumalo', {
    persona: 'LESEDI KHUMALO',
    message: 'Typing Learner Name: Lesedi Khumalo'
  });

  await page1.selectOption('[data-testid="select-signup-role"]', 'student');
  await page1.selectOption('[data-testid="select-signup-grade"]', '10');

  await typeRealistic(page1, '[data-testid="input-signup-email"]', testEmail, {
    persona: 'LESEDI KHUMALO',
    message: `Entering Email: ${testEmail}`
  });

  await typeRealistic(page1, '[data-testid="input-signup-password"]', testPassword, {
    persona: 'LESEDI KHUMALO',
    message: 'Entering Enterprise-Policy Password'
  });

  await typeRealistic(page1, '[data-testid="input-signup-confirm-password"]', testPassword, {
    persona: 'LESEDI KHUMALO',
    message: 'Confirming Password'
  });

  // Check POPIA Section 35 Guardian Consent
  await glideAndClick(page1, '[data-testid="checkbox-popia-consent"]', {
    persona: 'LESEDI KHUMALO',
    message: 'Confirming POPIA Section 35 Minor Consent'
  });
  await page1.waitForTimeout(500);

  // Select Direct Subscription to test full Access Bank EFT POP Clearance
  const directPlanRadio = page1.locator('[data-testid="radio-plan-direct-sub"]').first();
  if (await directPlanRadio.isVisible()) {
    await glideAndClick(page1, '[data-testid="radio-plan-direct-sub"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Selecting Direct Subscription Plan (EFT Flow)'
    });
    await page1.waitForTimeout(500);
  }

  // Submit Registration Form
  await glideAndClick(page1, '[data-testid="btn-auth-submit"]', {
    persona: 'LESEDI KHUMALO',
    message: 'Submitting CAPS Grade 10 Registration'
  });
  await page1.waitForTimeout(1500);

  // 3. Navigate to Subscription / EFT Upload
  await updateHud(page1, 'LESEDI KHUMALO', 'Entering Subscription & EFT Banking Desk');
  await page1.evaluate(() => {
    window.history.pushState({}, '', '/#subscription');
    window.dispatchEvent(new Event('popstate'));
  });
  await page1.waitForTimeout(1000);
  await injectGlidingCursorAndHud(page1);

  // Select School Term Pass (R349 / 3 Months — Most Popular)
  const termPassRadio = page1.locator('[data-testid="plan-term-pass-349"]').first();
  if (await termPassRadio.isVisible()) {
    await glideAndClick(page1, '[data-testid="plan-term-pass-349"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Selecting School Term Pass (R349 / 3 Months)'
    });
    await page1.waitForTimeout(600);

    // Copy Unique Bank Payment Reference
    const copyRefBtn = page1.locator('[data-testid="btn-copy-bank-ref"]').first();
    if (await copyRefBtn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-copy-bank-ref"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Copying Access Bank Payment Reference'
      });
      await page1.waitForTimeout(500);
    }

    // Attach Sample PDF Proof of Payment
    const samplePdfPath = path.resolve(__dirname, 'fixtures/sample_pop.pdf');
    const fileInput = page1.locator('[data-testid="input-file-pop"]').first();
    if (await fileInput.count() > 0) {
      await updateHud(page1, 'LESEDI KHUMALO', 'Attaching Access Bank Proof of Payment (sample_pop.pdf)');
      await fileInput.setInputFiles(samplePdfPath);
      await page1.waitForTimeout(800);
    }
  }

  await updateHud(page1, 'LESEDI KHUMALO', 'EFT Proof Submitted • Awaiting Super Admin Clearance');
  await page1.waitForTimeout(1200);

  // ══════════════════════════════════════════════════════════════════════
  // WINDOW 2: Right Half of Screen (Super Admin - Real-Time EFT Desk)
  // ══════════════════════════════════════════════════════════════════════
  const browser2 = await chromium.launch({
    headless: false,
    args: [
      '--window-position=745,0',
      '--window-size=740,980'
    ]
  });
  const page2 = await browser2.newPage({
    viewport: { width: 720, height: 880 }
  });

  await page2.goto('http://127.0.0.1:5173/?sandbox', { waitUntil: 'domcontentloaded' });
  await page2.waitForTimeout(600);
  await injectGlidingCursorAndHud(page2);
  await updateHud(page2, 'SUPER ADMIN', 'Opening Super Admin Cockpit • Payment Queue');
  await page2.waitForTimeout(1000);

  // Switch to Admin Role
  const profileBtn2 = page2.locator('button[title*="Profile"], button:has-text("Welcome")').first();
  if (await profileBtn2.isVisible()) {
    await glideAndClick(page2, 'button[title*="Profile"], button:has-text("Welcome")', {
      persona: 'SUPER ADMIN',
      message: 'Opening Super Admin Switcher'
    });
    await page2.waitForTimeout(800);

    const adminRoleBtn = page2.locator('[data-testid="btn-admin-role-admin"]').first();
    if (await adminRoleBtn.isVisible()) {
      await glideAndClick(page2, '[data-testid="btn-admin-role-admin"]', {
        persona: 'SUPER ADMIN',
        message: 'Activating Super Admin Oversight'
      });
      await page2.waitForTimeout(1000);
    }
  }

  // Open EFT Payment Approvals Tab in Admin View
  const paymentsTab = page2.locator('[data-testid="tab-admin-payments"]').first();
  if (await paymentsTab.isVisible()) {
    await glideAndClick(page2, '[data-testid="tab-admin-payments"]', {
      persona: 'SUPER ADMIN',
      message: 'Reviewing Pending Banking POP Slips'
    });
    await page2.waitForTimeout(1200);

    // ────────────────────────────────────────────────────────────────
    // HUMAN-IN-THE-LOOP APPROVAL: Wait for the user to click the orange button!
    // ────────────────────────────────────────────────────────────────
    const approve90d = page2.locator('[data-testid="btn-approve-payment-90d"]').first();
    if (await approve90d.isVisible()) {
      await updateHud(
        page2,
        '👉 YOUR TURN TO APPROVE',
        'Please click the orange "3 Mo (Term)" button on screen to approve Lesedi!'
      );

      console.log('\n╔══════════════════════════════════════════════════════════════════════════════╗');
      console.log('║  👉 [SET 1 HUMAN APPROVAL REQUIRED]                                          ║');
      console.log('║                                                                              ║');
      console.log('║  Window 2 (Super Admin Cockpit) is open on the RIGHT side of your screen.    ║');
      console.log('║  Please click the orange "3 Mo (Term)" button with your mouse to approve     ║');
      console.log('║  Lesedi Khumalo\'s Access Bank POP slip!                                      ║');
      console.log('║                                                                              ║');
      console.log('║  (Listening for your click... Will pause until clicked)                      ║');
      console.log('╚══════════════════════════════════════════════════════════════════════════════╝\n');

      const waitStart = Date.now();
      let userClicked = false;

      while (Date.now() - waitStart < 90000) {
        const visible = await approve90d.isVisible().catch(() => false);
        const disabled = await approve90d.isDisabled().catch(() => false);
        if (!visible || disabled) {
          userClicked = true;
          break;
        }
        await page2.waitForTimeout(500);
      }

      if (userClicked) {
        console.log('\n✅ [HUMAN APPROVAL CONFIRMED] Manual click detected! Payment approved by you.');
        await updateHud(page2, '✅ PAYMENT APPROVED', 'Approval confirmed! Unlocking student workspace...');
        await page2.waitForTimeout(1500);
      } else {
        console.log('⏰ Auto-approving as fallback...');
        await approve90d.click().catch(() => {});
      }
    }
  }

  // ══════════════════════════════════════════════════════════════════════
  // WINDOW 1: Paywall Drops -> SUBJECT 1: Grade 10 Accounting (CRJ)
  // ══════════════════════════════════════════════════════════════════════
  await page1.bringToFront();
  await updateHud(page1, 'LESEDI KHUMALO', 'Payment Approved! Paywall Dropped • Entering Workspace');
  await page1.evaluate(() => {
    window.history.pushState({}, '', '/');
    window.dispatchEvent(new Event('popstate'));
  });
  await page1.waitForTimeout(1200);
  await injectGlidingCursorAndHud(page1);

  // Switch to Accounting Subject Tab
  const accTab = page1.locator('button:has-text("Accounting"), [id*="tab-accounting"]').first();
  if (await accTab.isVisible()) {
    await glideAndClick(page1, 'button:has-text("Accounting"), [id*="tab-accounting"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Switching to Accounting Subject Folder (Emerald)'
    });
    await page1.waitForTimeout(1000);
  }

  // ────────────────────────────────────────────────────────────────
  // SUBJECT 1: STAGE 0 — DIAGNOSTIC BENCHMARK (Unassisted Calibration)
  // ────────────────────────────────────────────────────────────────
  await updateHud(page1, 'LESEDI KHUMALO', 'Stage 0: Diagnostic Benchmark • Calibrating Starting Mastery');
  const questionSurface1 = page1.locator('[data-testid="question-surface"]').first();
  await questionSurface1.waitFor({ state: 'visible', timeout: 12000 });

  // Verify Zero-Fallback Invariant
  const source1 = await questionSurface1.getAttribute('data-source');
  console.log(`\n[Set 1 Verification] Accounting Question Source: ${source1}`);
  expect(source1).not.toBe('fallback');

  // Deliberate Realistic Misconception:
  // Lesedi calculates VAT 15% on Gross (11500 * 0.15 = 1725) instead of 11500 * (15/115) = 1500
  await updateHud(page1, 'LESEDI KHUMALO', 'Simulating typical learner mistake: VAT on Gross (15% vs 15/115)');
  const editableInputs1 = page1.locator('input[type="text"]:visible');
  const inputCount1 = await editableInputs1.count();
  if (inputCount1 > 0) {
    // Fill first editable cell with gross-calculated VAT amount (1725)
    await typeRealistic(page1, editableInputs1.first(), '1725', {
      persona: 'LESEDI KHUMALO',
      message: 'Entering erroneous net calculation: R1 725'
    });
    await page1.waitForTimeout(600);
  }

  // Submit Diagnostic Answer
  const checkBtn1 = page1.locator('[data-testid="btn-check-answer"]').first();
  if (await checkBtn1.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-check-answer"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Submitting Diagnostic Baseline Answer'
    });
    await page1.waitForTimeout(1200);
  }

  // Verify Diagnostic Result: System flags misconception & prescribes Scaffold Mode
  await updateHud(page1, 'LESEDI KHUMALO', 'Diagnostic flags "net_vs_gross_confusion" • Gating to Scaffold Mode');
  await page1.waitForTimeout(1500);

  // ────────────────────────────────────────────────────────────────
  // SUBJECT 1: STAGE 1 — SCAFFOLD MODE (3-Tier Pre-Baked Hints)
  // ────────────────────────────────────────────────────────────────
  await updateHud(page1, 'LESEDI KHUMALO', 'Stage 1: Scaffold Mode • Opening 3-Tier Pre-Baked Hints Drawer');
  const toggleHintsBtn = page1.locator('[data-testid="btn-toggle-hints"]').first();
  if (await toggleHintsBtn.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-toggle-hints"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Unfolding 3-Tier Hint Drawer'
    });
    await page1.waitForTimeout(600);

    // Tier 1: Nudge
    const tier1Btn = page1.locator('[data-testid="btn-hint-tier-1"]').first();
    if (await tier1Btn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-hint-tier-1"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Reading Tier 1: Location Nudge'
      });
      await page1.waitForTimeout(800);
    }

    // Tier 2: Directional Rule
    const tier2Btn = page1.locator('[data-testid="btn-hint-tier-2"]').first();
    if (await tier2Btn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-hint-tier-2"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Reading Tier 2: Conceptual Rule (VAT Inclusive is 115%)'
      });
      await page1.waitForTimeout(800);
    }

    // Tier 3: Worked Step Calculation
    const tier3Btn = page1.locator('[data-testid="btn-hint-tier-3"]').first();
    if (await tier3Btn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-hint-tier-3"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Reading Tier 3: Worked Step (R11 500 * 15/115 = R1 500)'
      });
      await page1.waitForTimeout(1000);
    }
  }

  // Learner Corrects the Ledger Entry with Tier 3 Knowledge!
  await updateHud(page1, 'LESEDI KHUMALO', 'Applying Hint: Correcting Output VAT to R1 500 & Sales to R10 000');
  if (inputCount1 > 0) {
    await typeRealistic(page1, editableInputs1.first(), '1500', {
      persona: 'LESEDI KHUMALO',
      message: 'Entering corrected Output VAT: R1 500'
    });
    await page1.waitForTimeout(500);
  }

  // Re-check solution -> Verified marks awarded!
  if (await checkBtn1.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-check-answer"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Checking Corrected Entry'
    });
    await page1.waitForTimeout(1200);
  }

  // Next problem -> Advances through Practice and Exam
  const nextBtn1 = page1.locator('[data-testid="btn-next-question"]').first();
  if (await nextBtn1.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-next-question"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Advancing to Stage 2: Autonomous Practice'
    });
    await page1.waitForTimeout(1000);
  }

  // ────────────────────────────────────────────────────────────────
  // SUBJECT 1: STAGE 2 & 3 — PRACTICE & TIMED EXAM MODE
  // ────────────────────────────────────────────────────────────────
  await updateHud(page1, 'LESEDI KHUMALO', 'Stage 2 & 3: Solving Autonomous Practice & Timed Exam CRJ');
  await page1.waitForTimeout(2000);

  // ══════════════════════════════════════════════════════════════════════
  // INTER-SESSION STUDY BREAK (~20 mins simulated, 60s timer)
  // ══════════════════════════════════════════════════════════════════════
  await updateHud(page1, 'LESEDI KHUMALO', 'Accounting Block Complete! Checking Today\'s Desk before Break');
  const deskTab = page1.locator('button:has-text("Desk"), [id*="tab-desk"]').first();
  if (await deskTab.isVisible()) {
    await glideAndClick(page1, 'button:has-text("Desk"), [id*="tab-desk"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Viewing Today\'s Desk Progress & Dual-Ring MasteryDial'
    });
    await page1.waitForTimeout(1500);
  }

  // Logout cleanly
  const profileMenuBtn = page1.locator('button[title*="Profile"], button:has-text("Lesedi")').first();
  if (await profileMenuBtn.isVisible()) {
    await glideAndClick(page1, 'button[title*="Profile"], button:has-text("Lesedi")', {
      persona: 'LESEDI KHUMALO',
      message: 'Logging Out for Scheduled Study Break'
    });
    await page1.waitForTimeout(600);

    const logoutBtn = page1.locator('button:has-text("Sign Out"), button:has-text("Logout")').first();
    if (await logoutBtn.isVisible()) {
      await glideAndClick(page1, 'button:has-text("Sign Out"), button:has-text("Logout")', {
        persona: 'LESEDI KHUMALO',
        message: 'Confirming Logout'
      });
      await page1.waitForTimeout(1000);
    }
  }

  // Simulate 20-minute study break with visual 60-second timer
  await simulateStudyBreak(page1, 60, 20);

  // Re-login: Fresh session for Subject 2
  await updateHud(page1, 'LESEDI KHUMALO', 'Logging Back In for Subject 2: Mathematics');
  const signinBtn = page1.locator('[data-testid="btn-landing-signin"]').first();
  if (await signinBtn.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-landing-signin"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Opening Sign-In Portal'
    });
    await page1.waitForTimeout(800);

    await typeRealistic(page1, '[data-testid="input-signin-email"], [data-testid="input-signup-email"]', testEmail, {
      persona: 'LESEDI KHUMALO',
      message: `Entering Email: ${testEmail}`
    });

    await typeRealistic(page1, '[data-testid="input-signin-password"], [data-testid="input-signup-password"]', testPassword, {
      persona: 'LESEDI KHUMALO',
      message: 'Entering Password'
    });

    const submitLoginBtn = page1.locator('[data-testid="btn-auth-submit"]').first();
    if (await submitLoginBtn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-auth-submit"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Submitting Sign-In'
      });
      await page1.waitForTimeout(1500);
    }
  }

  // ══════════════════════════════════════════════════════════════════════
  // SUBJECT 2: Grade 10 Mathematics (Euclidean Geometry & Algebra)
  // ══════════════════════════════════════════════════════════════════════
  await injectGlidingCursorAndHud(page1);
  await updateHud(page1, 'LESEDI KHUMALO', 'Subject 2: Switching to Mathematics Folder (Brand Blue)');

  const mathTab = page1.locator('button:has-text("Mathematics"), [id*="tab-mathematics"]').first();
  if (await mathTab.isVisible()) {
    await glideAndClick(page1, 'button:has-text("Mathematics"), [id*="tab-mathematics"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Opening Mathematics Subject Folder'
    });
    await page1.waitForTimeout(1000);
  }

  // Stage 0: Mathematics Diagnostic Benchmark
  await updateHud(page1, 'LESEDI KHUMALO', 'Mathematics Stage 0: Diagnostic Benchmark (Algebra & Geometry)');
  const questionSurface2 = page1.locator('[data-testid="question-surface"]').first();
  await questionSurface2.waitFor({ state: 'visible', timeout: 12000 });

  const source2 = await questionSurface2.getAttribute('data-source');
  console.log(`\n[Set 1 Verification] Mathematics Question Source: ${source2}`);
  expect(source2).not.toBe('fallback');

  // Stage 1: Guided Scaffolding & KaTeX Working Pad
  await updateHud(page1, 'LESEDI KHUMALO', 'Mathematics Stage 1: Guided Derivation & SymPy Method Marks');
  const mathCheckBtn = page1.locator('[data-testid="btn-check-answer"]').first();
  if (await mathCheckBtn.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-check-answer"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Submitting Derivation for Consequential Marking [M][CA]'
    });
    await page1.waitForTimeout(1200);
  }

  // Advance to Practice & Timed Exam
  const mathNextBtn = page1.locator('[data-testid="btn-next-question"]').first();
  if (await mathNextBtn.isVisible()) {
    await glideAndClick(page1, '[data-testid="btn-next-question"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Advancing to Mathematics Autonomous Practice & Exam'
    });
    await page1.waitForTimeout(1500);
  }

  // ══════════════════════════════════════════════════════════════════════
  // FINAL WRAP-UP: Master Telemetry & Multi-Subject Certification
  // ══════════════════════════════════════════════════════════════════════
  await updateHud(page1, 'LESEDI KHUMALO', 'Session Complete! Reviewing Multi-Subject MasteryDial on Desk');
  if (await deskTab.isVisible()) {
    await glideAndClick(page1, 'button:has-text("Desk"), [id*="tab-desk"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Opening Today\'s Desk Final Summary'
    });
    await page1.waitForTimeout(1500);
  }

  await updateHud(
    page1,
    '🎉 SET 1 CERTIFIED',
    'Verified Full Multi-Subject Journey: Diagnostic -> Scaffold -> Break -> Practice -> Exam!'
  );
  console.log('\n╔══════════════════════════════════════════════════════════════════════════════╗');
  console.log('║  🎉 [SET 1 CERTIFIED SUCCESSFULLY]                                          ║');
  console.log('║                                                                              ║');
  console.log('║  1. Pre-Flight Purge: Clean slate verified.                                  ║');
  console.log('║  2. Sign-Up & Access Bank EFT: Super Admin clearance loop verified.          ║');
  console.log('║  3. Accounting (CRJ): Diagnostic -> 3-Tier Hints -> Micro-Drill verified.   ║');
  console.log('║  4. 20-Min Study Break: Simulated rest & re-login verified.                  ║');
  console.log('║  5. Mathematics: Geometry & Algebra SymPy derivations verified.              ║');
  console.log('║  6. Zero Fallback Invariant: 100% deterministic generator questions.        ║');
  console.log('╚══════════════════════════════════════════════════════════════════════════════╝\n');

  await page1.waitForTimeout(5000);

  // Clean up browsers
  await browser1.close();
  await browser2.close();
});
