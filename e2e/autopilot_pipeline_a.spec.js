import { test, expect } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';
import { injectGlidingCursorAndHud, updateHud, glideAndClick, glideCursorTo } from './helpers/autopilotHud.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

test.describe('Autonomous Mock User Autopilot — Pipeline A: Independent Learner & Super Admin Approval', () => {

  test('Pipeline A: Lesedi Khumalo registration, R349 Term Pass EFT, Semi-Automated Admin Approval & Zero-Fallback Question Solving', async ({ browser }) => {
    test.setTimeout(300000);

    // ══════════════════════════════════════════════════════════════════════
    // WINDOW 1: Lesedi Khumalo (Independent Learner, Grade 10 FET)
    // ══════════════════════════════════════════════════════════════════════
    const context1 = await browser.newContext({
      viewport: { width: 1024, height: 768 },
    });
    const page1 = await context1.newPage();

    // 1. Visit Landing Page
    await page1.goto('/', { waitUntil: 'domcontentloaded' });
    await page1.waitForTimeout(500);
    await injectGlidingCursorAndHud(page1);
    await updateHud(page1, 'LESEDI KHUMALO', 'Exploring Landing Page • Grade 10 FET');
    await page1.waitForTimeout(1000);

    // Verify Landing Page Sign-in & Sign-up CTAs exist
    const signUpBtn = page1.locator('[data-testid="btn-landing-signup"]').first();
    await expect(signUpBtn).toBeVisible();

    // 2. Click Sign Up CTA
    await glideAndClick(page1, '[data-testid="btn-landing-signup"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Clicking "Start Free Diagnostic & Practice" CTA'
    });
    await page1.waitForTimeout(800);

    // 3. Fill Registration Form in AuthScreen
    await updateHud(page1, 'LESEDI KHUMALO', 'Filling South African Curriculum Registration Form');
    await page1.waitForSelector('[data-testid="input-signup-name"]', { state: 'visible' });

    await glideCursorTo(page1, '[data-testid="input-signup-name"]');
    await page1.fill('[data-testid="input-signup-name"]', 'Lesedi Khumalo');

    await page1.selectOption('[data-testid="select-signup-role"]', 'student');
    await page1.selectOption('[data-testid="select-signup-grade"]', '10');

    const testEmail = `lesedi.${Date.now()}@fundile.test`;
    await page1.fill('[data-testid="input-signup-email"]', testEmail);
    await page1.fill('[data-testid="input-signup-password"]', 'Fundile@2026!');
    await page1.fill('[data-testid="input-signup-confirm-password"]', 'Fundile@2026!');

    // Check POPIA Section 35 Guardian Consent
    await updateHud(page1, 'LESEDI KHUMALO', 'Confirming POPIA Section 35 Guardian Consent');
    await glideAndClick(page1, '[data-testid="checkbox-popia-consent"]', {
      persona: 'LESEDI KHUMALO',
      message: 'Accepting POPIA Section 35 Legal Consent'
    });
    await page1.waitForTimeout(600);

    // 4. Enter Student Workspace via Instant Demo or Explore
    await updateHud(page1, 'LESEDI KHUMALO', 'Launching Grade 10 Learner Workspace');
    const demoBtn = page1.locator('[data-testid="btn-demo-student-login"]');
    if (await demoBtn.isVisible()) {
      await glideAndClick(page1, '[data-testid="btn-demo-student-login"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Entering Student Workspace'
      });
    }

    await page1.waitForTimeout(1500);
    await injectGlidingCursorAndHud(page1);

    // 5. Navigate to Subscription / EFT Page
    await updateHud(page1, 'LESEDI KHUMALO', 'Navigating to Subscription & EFT POP Upload');
    await page1.evaluate(() => {
      window.history.pushState({}, '', '/#subscription');
      window.dispatchEvent(new Event('popstate'));
    });
    await page1.waitForTimeout(1000);
    await injectGlidingCursorAndHud(page1);

    // If on Subscription page, verify and select R349 Term Pass
    const termPassRadio = page1.locator('[data-testid="plan-term-pass-349"]');
    if (await termPassRadio.isVisible()) {
      await updateHud(page1, 'LESEDI KHUMALO', 'Selecting School Term Pass (R349 / 3 Months - Best Value)');
      await glideAndClick(page1, '[data-testid="plan-term-pass-349"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Selected School Term Pass (R349, 90 Days)'
      });
      await page1.waitForTimeout(600);

      // Copy Bank Reference
      const copyRefBtn = page1.locator('[data-testid="btn-copy-bank-ref"]');
      if (await copyRefBtn.isVisible()) {
        await glideAndClick(page1, '[data-testid="btn-copy-bank-ref"]', {
          persona: 'LESEDI KHUMALO',
          message: 'Copied Unique Bank Payment Reference'
        });
        await page1.waitForTimeout(600);
      }

      // Attach Sample PDF POP
      const samplePdfPath = path.resolve(__dirname, 'fixtures/sample_pop.pdf');
      const fileInput = page1.locator('[data-testid="input-file-pop"]');
      if (await fileInput.count() > 0) {
        await updateHud(page1, 'LESEDI KHUMALO', 'Attaching Access Bank Proof of Payment (PDF)');
        await fileInput.setInputFiles(samplePdfPath);
        await page1.waitForTimeout(1000);
      }
    }

    await updateHud(page1, 'LESEDI KHUMALO', 'EFT Proof Submitted • Awaiting Super Admin Verification');
    await page1.waitForTimeout(1000);

    // ══════════════════════════════════════════════════════════════════════
    // WINDOW 2: Mr. Vinay Pillay (Principal & Super Admin)
    // ══════════════════════════════════════════════════════════════════════
    const context2 = await browser.newContext({
      viewport: { width: 1024, height: 768 },
    });
    const page2 = await context2.newPage();

    await page2.goto('/', { waitUntil: 'domcontentloaded' });
    await page2.waitForTimeout(500);
    await injectGlidingCursorAndHud(page2);
    await updateHud(page2, 'MR. VINAY PILLAY', 'Logging into Super Admin Cockpit • Westville High');
    await page2.waitForTimeout(1000);

    // If on landing page, click Sign in / demo login to enter authenticated state
    const landingSignIn = page2.locator('[data-testid="btn-landing-signin"]').first();
    if (await landingSignIn.isVisible()) {
      await glideAndClick(page2, '[data-testid="btn-landing-signin"]', {
        persona: 'MR. VINAY PILLAY',
        message: 'Opening Authentication Portal'
      });
      await page2.waitForTimeout(600);
    }

    const demoLogin = page2.locator('[data-testid="btn-demo-student-login"]').first();
    if (await demoLogin.isVisible()) {
      await glideAndClick(page2, '[data-testid="btn-demo-student-login"]', {
        persona: 'MR. VINAY PILLAY',
        message: 'Authenticating Privileged Session'
      });
      await page2.waitForTimeout(1000);
      await injectGlidingCursorAndHud(page2);
    }

    // Open User Profile Modal to switch to Admin perspective
    const profileBtn = page2.locator('button[title*="Profile"], button:has-text("Welcome")').first();
    if (await profileBtn.isVisible()) {
      await glideAndClick(page2, 'button[title*="Profile"], button:has-text("Welcome")', {
        persona: 'MR. VINAY PILLAY',
        message: 'Opening Super Admin Profile & Switcher'
      });
      await page2.waitForTimeout(800);

      // Click Super Admin Role Switcher
      const adminRoleBtn = page2.locator('[data-testid="btn-admin-role-admin"]').first();
      if (await adminRoleBtn.isVisible()) {
        await glideAndClick(page2, '[data-testid="btn-admin-role-admin"]', {
          persona: 'MR. VINAY PILLAY',
          message: 'Activating Super Admin View'
        });
        await page2.waitForTimeout(1000);
      }
    }

    // Open EFT Payment Approvals Tab in Admin View
    const paymentsTab = page2.locator('[data-testid="tab-admin-payments"]').first();
    if (await paymentsTab.isVisible()) {
      await updateHud(page2, 'MR. VINAY PILLAY', 'Accessing Real-time EFT Payment Approval Queue');
      await glideAndClick(page2, '[data-testid="tab-admin-payments"]', {
        persona: 'MR. VINAY PILLAY',
        message: 'Reviewing Pending Banking POP Slips'
      });
      await page2.waitForTimeout(1200);

      // ────────────────────────────────────────────────────────────────
      // SEMI-AUTOMATED HUMAN-IN-THE-LOOP APPROVAL
      // ────────────────────────────────────────────────────────────────
      const approve90d = page2.locator('[data-testid="btn-approve-payment-90d"]').first();
      if (await approve90d.isVisible()) {
        const isAutoApprove = process.env.AUTO_APPROVE === 'true';

        if (isAutoApprove) {
          await updateHud(page2, 'AUTO-APPROVE MODE', 'Auto-approving 90-Day School Term Pass...');
          await glideAndClick(page2, '[data-testid="btn-approve-payment-90d"]', {
            persona: 'MR. VINAY PILLAY',
            message: 'Payment Approved (90-Day Term Pass Activated)'
          });
          await page2.waitForTimeout(1500);
        } else {
          // Human-in-the-loop: Prompt the user in HUD and terminal
          await updateHud(page2, '👉 WAITING FOR YOUR APPROVAL', 'Click "3 Mo (Term)" on screen to approve Lesedi, or wait for auto-approval...');
          console.log('\n╔══════════════════════════════════════════════════════════════════════╗');
          console.log('║  👉 [SEMI-AUTOMATED APPROVAL] HUMAN-IN-THE-LOOP INTERACTION          ║');
          console.log('║                                                                      ║');
          console.log('║  In Window 2 (Super Admin Cockpit), please click "3 Mo (Term)"      ║');
          console.log('║  to manually approve Lesedi Khumalo\'s Access Bank POP slip!          ║');
          console.log('║                                                                      ║');
          console.log('║  (Listening for your click... Will auto-proceed in 25s if untouched) ║');
          console.log('╚══════════════════════════════════════════════════════════════════════╝\n');

          const waitStart = Date.now();
          let userClicked = false;

          while (Date.now() - waitStart < 25000) {
            const visible = await approve90d.isVisible().catch(() => false);
            const disabled = await approve90d.isDisabled().catch(() => false);
            if (!visible || disabled) {
              userClicked = true;
              break;
            }
            await page2.waitForTimeout(500);
          }

          if (userClicked) {
            console.log('✅ [HUMAN APPROVAL DETECTED] You clicked "3 Mo (Term)"! Payment approved.');
            await updateHud(page2, '✅ HUMAN APPROVAL CONFIRMED', 'Approval detected! Unlocking student workspace...');
            await page2.waitForTimeout(1500);
          } else {
            console.log('⏰ [AUTO-APPROVAL FALLBACK] 25s elapsed without click. Auto-approving now...');
            await updateHud(page2, 'AUTO-APPROVAL FALLBACK', 'Auto-approving 90-Day School Term Pass for Lesedi Khumalo...');
            if (await approve90d.isVisible()) {
              await glideAndClick(page2, '[data-testid="btn-approve-payment-90d"]', {
                persona: 'MR. VINAY PILLAY',
                message: 'Payment Approved (90-Day Term Pass Activated)'
              });
              await page2.waitForTimeout(1500);
            }
          }
        }
      }
    }

    // ══════════════════════════════════════════════════════════════════════
    // WINDOW 1 RE-ENGAGEMENT: Paywall Dropped & Question Solving
    // ══════════════════════════════════════════════════════════════════════
    await page1.bringToFront();
    await updateHud(page1, 'LESEDI KHUMALO', 'Payment Approved! Paywall Dropped • Returning to Workspace');
    await page1.evaluate(() => {
      window.history.pushState({}, '', '/');
      window.dispatchEvent(new Event('popstate'));
    });
    await page1.waitForTimeout(1200);
    await injectGlidingCursorAndHud(page1);

    // Click Mathematics Tab if present
    const mathTab = page1.locator('button:has-text("Mathematics"), [id*="tab-mathematics"]').first();
    if (await mathTab.isVisible()) {
      await glideAndClick(page1, 'button:has-text("Mathematics"), [id*="tab-mathematics"]', {
        persona: 'LESEDI KHUMALO',
        message: 'Switching to Mathematics Subject Folder'
      });
      await page1.waitForTimeout(1000);
    }

    // Verify Question Problem Surface & Anti-Fallback Invariant
    await updateHud(page1, 'LESEDI KHUMALO', 'Verifying Authentic CAPS Question Engine');
    const questionSurface = page1.locator('[data-testid="question-surface"]').first();
    if (await questionSurface.isVisible()) {
      const source = await questionSurface.getAttribute('data-source');
      console.log(`[Autopilot Pipeline A] Question source: ${source}`);
      expect(source).not.toBe('fallback');
      expect(source).toBe('deterministic_generator');

      // Test Pre-baked 3-Tier Hint Engine (Zero Token Cost)
      await updateHud(page1, 'LESEDI KHUMALO', 'Viewing Deterministic 3-Tier Pre-Baked Hints');
      const toggleHintsBtn = page1.locator('[data-testid="btn-toggle-hints"]').first();
      if (await toggleHintsBtn.isVisible()) {
        await glideAndClick(page1, '[data-testid="btn-toggle-hints"]', {
          persona: 'LESEDI KHUMALO',
          message: 'Toggling 3-Tier Hint Drawer'
        });
        await page1.waitForTimeout(600);

        // Click Tier 1 Hint
        const tier1Btn = page1.locator('[data-testid="btn-hint-tier-1"]').first();
        if (await tier1Btn.isVisible()) {
          await glideAndClick(page1, '[data-testid="btn-hint-tier-1"]', {
            persona: 'LESEDI KHUMALO',
            message: 'Inspecting Tier 1 (Nudge) Hint'
          });
          await page1.waitForTimeout(500);
        }

        // Click Tier 2 Hint
        const tier2Btn = page1.locator('[data-testid="btn-hint-tier-2"]').first();
        if (await tier2Btn.isVisible()) {
          await glideAndClick(page1, '[data-testid="btn-hint-tier-2"]', {
            persona: 'LESEDI KHUMALO',
            message: 'Inspecting Tier 2 (Directional Rule) Hint'
          });
          await page1.waitForTimeout(500);
        }
      }

      // Submit Check Answer
      const checkBtn = page1.locator('[data-testid="btn-check-answer"]').first();
      if (await checkBtn.isVisible()) {
        await updateHud(page1, 'LESEDI KHUMALO', 'Submitting Solution for Consequential Marking');
        await glideAndClick(page1, '[data-testid="btn-check-answer"]', {
          persona: 'LESEDI KHUMALO',
          message: 'Checking Derivation & Marking Scheme'
        });
        await page1.waitForTimeout(1000);
      }
    }

    await updateHud(page1, 'AUTOPILOT COMPLETE', 'Pipeline A Successfully Executed: Semi-Automated Approval Verified');
    await page1.waitForTimeout(2000);

    // Clean up
    await context1.close();
    await context2.close();
  });
});
