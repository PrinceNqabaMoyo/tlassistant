import { test, expect, devices } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';
import { injectGlidingCursorAndHud, updateHud, glideAndClick, glideCursorTo } from './helpers/autopilotHud.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

test.describe('Autonomous Mock User Autopilot — Pipeline B: School Batch Enrollment & Parent Sunday Pulse', () => {

  test('Pipeline B: Ayanda Ndlovu MTH701 join, Grade 7 patterns, arithmetic grid long division with error recovery & Mr. Ndlovu Sunday Pulse', async ({ browser }) => {
    test.setTimeout(300000);

    // ══════════════════════════════════════════════════════════════════════
    // WINDOW 1: Ayanda Ndlovu (Grade 7 Senior Phase Learner - Pixel 7)
    // ══════════════════════════════════════════════════════════════════════
    const context1 = await browser.newContext({
      ...devices['Pixel 7'],
    });
    const page1 = await context1.newPage();

    // 1. Visit Landing Page on Mobile WebAPK Viewport
    await page1.goto('/', { waitUntil: 'domcontentloaded' });
    await page1.waitForTimeout(600);
    await injectGlidingCursorAndHud(page1);
    await updateHud(page1, 'AYANDA NDLOVU', 'Launching Grade 7 Mobile WebAPK • Pixel 7 Viewport');
    await page1.waitForTimeout(1000);

    // If on Landing Page, enter Student Workspace via demo login
    const signupBtn1 = page1.locator('[data-testid="btn-landing-signup"]').first();
    const signinBtn1 = page1.locator('[data-testid="btn-landing-signin"]').first();
    if (await signupBtn1.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-landing-signup"]', {
        persona: 'AYANDA NDLOVU',
        message: 'Opening Authentication Portal'
      });
      await page1.waitForTimeout(800);
    } else if (await signinBtn1.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-landing-signin"]', {
        persona: 'AYANDA NDLOVU',
        message: 'Opening Authentication Portal'
      });
      await page1.waitForTimeout(800);
    }

    const demoBtn1 = page1.locator('[data-testid="btn-demo-student-login"]').first();
    await demoBtn1.waitFor({ state: 'visible', timeout: 10000 });
    await glideAndClick(page1, '[data-testid="btn-demo-student-login"]', {
      persona: 'AYANDA NDLOVU',
      message: 'Entering Student Workspace'
    });
    await page1.waitForTimeout(1500);
    await injectGlidingCursorAndHud(page1);

    // 2. Open Join Class Modal and Enter Mrs. Patience Khumalo's Code (MTH701)
    await updateHud(page1, 'AYANDA NDLOVU', 'Enrolling in Grade 7 Mathematics via Mrs. Khumalo Class Code');
    const openJoinBtn = page1.locator('[data-testid="btn-open-join-class-modal"]:visible').first();
    await openJoinBtn.waitFor({ state: 'visible', timeout: 10000 });
    await glideAndClick(page1, '[data-testid="btn-open-join-class-modal"]:visible', {
      persona: 'AYANDA NDLOVU',
      message: 'Opening Teacher Class Link Dialog'
    });
    await page1.waitForTimeout(800);

    // Type MTH701 into class code input
    const codeInput = page1.locator('[data-testid="input-join-class-code"]').first();
    await codeInput.waitFor({ state: 'visible', timeout: 8000 });
    await glideCursorTo(page1, '[data-testid="input-join-class-code"]');
    await codeInput.fill('MTH701');
    await page1.waitForTimeout(500);

    // Submit join request
    await glideAndClick(page1, '[data-testid="btn-join-class-submit"]', {
      persona: 'AYANDA NDLOVU',
      message: 'Submitting Class Join Code (MTH701)'
    });
    await page1.waitForTimeout(800);

    // Click Done to return to Desk
    const doneBtn = page1.locator('[data-testid="btn-join-class-done"]').first();
    await doneBtn.waitFor({ state: 'visible', timeout: 8000 });
    await glideAndClick(page1, '[data-testid="btn-join-class-done"]', {
      persona: 'AYANDA NDLOVU',
      message: 'Enrolled in Mrs. Patience Khumalo Class!'
    });
    await page1.waitForTimeout(1000);
    await injectGlidingCursorAndHud(page1);

    // 3. Inspect Today's Desk with Mrs. Khumalo's Assigned Tasks
    await updateHud(page1, 'AYANDA NDLOVU', 'Reviewing Assigned Homework: Number Patterns & Long Division');
    const upcomingCard = page1.locator('[data-testid="card-task-upcoming"]:visible').first();
    await expect(upcomingCard).toBeVisible({ timeout: 10000 });

    // Click "Open in Mathematics" on the first assigned task (Number Patterns)
    const openTaskBtn = page1.locator('[data-testid="btn-open-task-subject"]:visible').first();
    await glideAndClick(page1, '[data-testid="btn-open-task-subject"]:visible', {
      persona: 'AYANDA NDLOVU',
      message: 'Opening Assigned Task: Grade 7 Number Patterns'
    });
    await page1.waitForTimeout(1500);
    await injectGlidingCursorAndHud(page1);

    // 4. Assert Anti-Fallback Invariant on Question Engine
    await updateHud(page1, 'AYANDA NDLOVU', 'Solving Grade 7 Number Patterns (Anti-Fallback Invariant)');
    const questionSurface = page1.locator('[data-testid="question-surface"]:visible').first();
    await questionSurface.waitFor({ state: 'visible', timeout: 10000 });

    const questionSource = await questionSurface.getAttribute('data-source');
    console.log(`[Autopilot Pipeline B] Question source for Number Patterns: ${questionSource}`);
    expect(questionSource).not.toBe('fallback');
    expect(questionSource).toBe('deterministic_generator');

    // 5. Inspect Pre-baked 3-Tier Hint Engine
    const toggleHintsBtn = page1.locator('[data-testid="btn-toggle-hints"]:visible').first();
    if (await toggleHintsBtn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-toggle-hints"]', {
        persona: 'AYANDA NDLOVU',
        message: 'Reviewing Pre-Calculated 3-Tier Hints'
      });
      await page1.waitForTimeout(500);

      const tier1Btn = page1.locator('[data-testid="btn-hint-tier-1"]').first();
      if (await tier1Btn.isVisible()) {
        await glideAndClick(page1, '[data-testid="btn-hint-tier-1"]', {
          persona: 'AYANDA NDLOVU',
          message: 'Viewing Tier 1 (Nudge): Constant Difference'
        });
        await page1.waitForTimeout(500);
      }

      const tier2Btn = page1.locator('[data-testid="btn-hint-tier-2"]').first();
      if (await tier2Btn.isVisible()) {
        await glideAndClick(page1, '[data-testid="btn-hint-tier-2"]', {
          persona: 'AYANDA NDLOVU',
          message: 'Viewing Tier 2 (Directional Rule): Tn = d*n + c'
        });
        await page1.waitForTimeout(500);
      }
    }

    // Submit Answer for Number Patterns
    const checkBtn1 = page1.locator('[data-testid="btn-check-answer"]:visible').first();
    if (await checkBtn1.isVisible()) {
      await updateHud(page1, 'AYANDA NDLOVU', 'Submitting Number Patterns Solution');
      await glideAndClick(page1, '[data-testid="btn-check-answer"]:visible', {
        persona: 'AYANDA NDLOVU',
        message: 'Checked Number Patterns Solution'
      });
      await page1.waitForTimeout(1200);
    }

    // 6. Navigate to Task 2: Grade 7 Long Division (Columnar Arithmetic Grid)
    await updateHud(page1, 'AYANDA NDLOVU', 'Switching to Long Division on Columnar Arithmetic Grid');
    
    // Switch topic via Topic Scope Modal or return to Desk
    const topicPill = page1.locator('button:has-text("Term 1 •"):visible').first();
    if (await topicPill.isVisible()) {
      await glideAndClick(page1, 'button:has-text("Term 1 •"):visible', {
        persona: 'AYANDA NDLOVU',
        message: 'Opening Topic Scope to Select Whole Numbers'
      });
      await page1.waitForTimeout(800);

      const wholeNumbersTopic = page1.locator('div:has-text("Whole numbers"), div:has-text("Working with whole numbers"), span:has-text("Whole numbers")').first();
      await wholeNumbersTopic.waitFor({ state: 'visible', timeout: 8000 });
      await wholeNumbersTopic.click();
      await page1.waitForTimeout(1500);
    }

    // Verify Arithmetic Grid Workspace is rendered
    const arithmeticGrid = page1.locator('[data-testid="arithmetic-grid-workspace"]:visible').first();
    await arithmeticGrid.waitFor({ state: 'visible', timeout: 10000 });
    if (await arithmeticGrid.isVisible()) {
      await updateHud(page1, 'AYANDA NDLOVU', 'Verifying South African Columnar Long Division Modality');
      await page1.waitForTimeout(800);

      // 7. Simulate Borrowing Error (Enter Incorrect Quotient)
      await updateHud(page1, 'AYANDA NDLOVU', 'Simulating Subtraction Borrowing Slip (Erroneous Quotient 128)');
      const quotientInput = page1.locator('[data-testid="input-quotient"]:visible').first();
      await quotientInput.waitFor({ state: 'visible', timeout: 8000 });
      await glideCursorTo(page1, '[data-testid="input-quotient"]:visible');
      await quotientInput.fill('128');
      await page1.waitForTimeout(500);

      // Click Check Division
      const checkDivBtn = page1.locator('[data-testid="btn-check-answer"]:visible').first();
      await glideAndClick(page1, '[data-testid="btn-check-answer"]:visible', {
        persona: 'AYANDA NDLOVU',
        message: 'Checking Intermediate Steps with Simulated Slip'
      });
      await page1.waitForTimeout(1500);

      // Verify Misconception Tag "subtraction_borrowing_inversion" is diagnosed!
      await updateHud(page1, 'AYANDA NDLOVU', 'Diagnosed Misconception: subtraction_borrowing_inversion');
      const misconceptionTag = page1.locator('text=subtraction_borrowing_inversion').first();
      await expect(misconceptionTag).toBeVisible({ timeout: 10000 });
      await page1.waitForTimeout(1200);

      // 8. Error Recovery: Inspect Tier 2 Rule and Correct Quotient
      await updateHud(page1, 'AYANDA NDLOVU', 'Applying Tier 2 Rule: Place-Value Borrowing Recovery');
      const fillCorrectBtn = page1.locator('button:has-text("Fill Correct")').first();
      if (await fillCorrectBtn.isVisible()) {
        await glideAndClick(page1, 'button:has-text("Fill Correct")', {
          persona: 'AYANDA NDLOVU',
          message: 'Correcting Place-Value Subtraction and Remainder'
        });
      } else {
        await quotientInput.fill('132');
      }
      await page1.waitForTimeout(500);

      // Re-submit corrected solution
      await glideAndClick(page1, '[data-testid="btn-check-answer"]:visible', {
        persona: 'AYANDA NDLOVU',
        message: 'Submitting Corrected Long Division Algorithm'
      });
      await page1.waitForTimeout(1500);

      // Verify Success and XP Award
      const successFeedback = page1.locator('text=Accurate Quotient').first();
      await expect(successFeedback).toBeVisible({ timeout: 10000 });
      await updateHud(page1, 'AYANDA NDLOVU', 'Full Marks Recovered (+35 XP Earned)');
      await page1.waitForTimeout(1500);
    }

    // ══════════════════════════════════════════════════════════════════════
    // WINDOW 2: Mr. Sipho Ndlovu (Parent & Guardian - Mobile Viewport)
    // ══════════════════════════════════════════════════════════════════════
    const context2 = await browser.newContext({
      ...devices['Pixel 7'],
    });
    const page2 = await context2.newPage();

    await page2.goto('/', { waitUntil: 'domcontentloaded' });
    await page2.waitForTimeout(600);
    await injectGlidingCursorAndHud(page2);
    await updateHud(page2, 'MR. SIPHO NDLOVU', 'Logging into Guardian Portal • Mobile Viewport');
    await page2.waitForTimeout(1000);

    // If on landing, sign in as demo user to access switchers
    const signupBtn2 = page2.locator('[data-testid="btn-landing-signup"]:visible').first();
    const signinBtn2 = page2.locator('[data-testid="btn-landing-signin"]:visible').first();
    if (await signupBtn2.isVisible()) {
      await glideAndClick(page2, '[data-testid="btn-landing-signup"]:visible', {
        persona: 'MR. SIPHO NDLOVU',
        message: 'Opening Guardian Access Portal'
      });
      await page2.waitForTimeout(800);
    } else if (await signinBtn2.isVisible()) {
      await glideAndClick(page2, '[data-testid="btn-landing-signin"]:visible', {
        persona: 'MR. SIPHO NDLOVU',
        message: 'Opening Guardian Access Portal'
      });
      await page2.waitForTimeout(800);
    }

    const demoLogin2 = page2.locator('[data-testid="btn-demo-student-login"]:visible').first();
    await demoLogin2.waitFor({ state: 'visible', timeout: 10000 });
    await glideAndClick(page2, '[data-testid="btn-demo-student-login"]:visible', {
      persona: 'MR. SIPHO NDLOVU',
      message: 'Authenticating Guardian Session'
    });
    await page2.waitForTimeout(1500);
    await injectGlidingCursorAndHud(page2);

    // Open User Profile Modal to switch to Parent Role
    const profileBtn2 = page2.locator('[data-testid="btn-open-user-profile"]:visible, button[title*="Profile"]:visible, button[aria-label="Profile Photo"]:visible, button:has-text("Welcome"):visible').first();
    await profileBtn2.waitFor({ state: 'visible', timeout: 10000 });
    await glideAndClick(page2, '[data-testid="btn-open-user-profile"]:visible, button[title*="Profile"]:visible, button[aria-label="Profile Photo"]:visible, button:has-text("Welcome"):visible', {
      persona: 'MR. SIPHO NDLOVU',
      message: 'Opening Profile Settings & Role Switcher'
    });
    await page2.waitForTimeout(800);

    // Switch to Parent role
    const parentRoleBtn = page2.locator('[data-testid="btn-admin-role-parent"]:visible').first();
    await parentRoleBtn.waitFor({ state: 'visible', timeout: 10000 });
    await glideAndClick(page2, '[data-testid="btn-admin-role-parent"]:visible', {
      persona: 'MR. SIPHO NDLOVU',
      message: 'Activating Parent Dashboard'
    });
    await page2.waitForTimeout(1200);
    await injectGlidingCursorAndHud(page2);

    // 9. Enter Ephemeral 15-Minute Handshake Code (PAR-7892)
    await updateHud(page2, 'MR. SIPHO NDLOVU', 'Linking Ayanda Ndlovu via Ephemeral Code (PAR-7892)');
    const addChildBtn = page2.locator('[data-testid="btn-add-child-modal"]:visible').first();
    if (await addChildBtn.isVisible()) {
      await glideAndClick(page2, '[data-testid="btn-add-child-modal"]:visible', {
        persona: 'MR. SIPHO NDLOVU',
        message: 'Opening Add Child Linking Dialog'
      });
      await page2.waitForTimeout(600);

      // Fill PAR-7892
      const linkCodeInput = page2.locator('[data-testid="input-child-link-code"]:visible').first();
      await linkCodeInput.waitFor({ state: 'visible', timeout: 8000 });
      await glideCursorTo(page2, '[data-testid="input-child-link-code"]:visible');
      await linkCodeInput.fill('PAR-7892');
      await page2.waitForTimeout(500);

      // Submit link code
      await glideAndClick(page2, '[data-testid="btn-submit-add-child"]:visible', {
        persona: 'MR. SIPHO NDLOVU',
        message: 'Redeeming Ephemeral 15-Min Linking Passcode'
      });
      await page2.waitForTimeout(1500);
      await injectGlidingCursorAndHud(page2);
    }

    // 10. Switch to Ayanda's Tab in Parent Dashboard
    await updateHud(page2, 'MR. SIPHO NDLOVU', 'Viewing Ayanda Ndlovu Sunday Academic Pulse');
    const ayandaTab = page2.locator('[data-testid="tab-child-ayanda"]:visible').first();
    if (await ayandaTab.isVisible()) {
      await glideAndClick(page2, '[data-testid="tab-child-ayanda"]:visible', {
        persona: 'MR. SIPHO NDLOVU',
        message: 'Selecting Ayanda Ndlovu • Grade 7 Senior Phase'
      });
      await page2.waitForTimeout(1000);
    }

    // 11. Assert Sunday Pulse Telemetry: 1.4 MB Bandwidth & Repaired Misconception
    const dataMeter = page2.locator('[data-testid="data-usage-meter"]:visible').first();
    await expect(dataMeter).toBeVisible({ timeout: 10000 });
    await expect(dataMeter).toContainText('1.4 MB');
    console.log('[Autopilot Pipeline B] Verified: 1.4 MB Cellular Data Consumption displayed.');

    const repairedMisconception = page2.locator('[data-testid="card-repaired-misconception"]:visible').first();
    await expect(repairedMisconception).toBeVisible({ timeout: 10000 });
    await expect(repairedMisconception).toContainText('subtraction_borrowing_inversion');
    console.log('[Autopilot Pipeline B] Verified: subtraction_borrowing_inversion cognitive repair displayed.');

    await updateHud(page2, 'AUTOPILOT COMPLETE', 'Pipeline B Successfully Executed: Batch Enrollment & Sunday Pulse Verified');
    await page2.waitForTimeout(2000);

    // Clean up
    await context1.close();
    await context2.close();
  });

});
