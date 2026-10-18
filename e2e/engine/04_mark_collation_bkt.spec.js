import { test, expect } from '@playwright/test';

/**
 * Mark Collation, BKT Progression & Adaptive Prerequisite Audit
 * Strict Invariant Compliance:
 * - Rule 5: Standard Package Rule-Based 100% Deterministic & Zero-LLM BKT
 * - Rule 12: Shared Student Model (studentStore is single source of truth)
 * - Rule 0d-4: Zero phantom selectors (all test-ids grounded in UniversalWorkspace)
 * - Rule 0d-6: Zero silent skips (explicit expect assertions)
 */
test.describe('Cognitive Engine: Mark Collation & Bayesian Knowledge Tracing', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test('Collation 1: Diagnostic Calibration & EMA BKT State Transition', async ({ page }) => {
    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.studentStore !== 'undefined', { timeout: 15000 });

    // Reset studentStore to clean 0% baseline state
    await page.evaluate(() => {
      window.studentStore.resetAllSubjectsToZero();
    });

    // 1. Verify Baseline is 0% Diagnostic Required
    const initialStatus = await page.evaluate(() => {
      const sub = window.studentStore.getSubject('accounting');
      return {
        mastery: sub.formativeMastery,
        status: sub.status,
        attempts: sub.questionsAttempted
      };
    });

    expect(initialStatus.mastery).toBe(0);
    expect(initialStatus.status).toBe('diagnostic_required');

    // 2. Calibrate Baseline via completeDiagnostic(score = 60)
    await page.evaluate(() => {
      window.studentStore.completeDiagnostic('accounting', 60);
    });

    const calibrated = await page.evaluate(() => {
      const sub = window.studentStore.getSubject('accounting');
      return {
        mastery: sub.formativeMastery,
        evaluative: sub.evaluativeScore,
        status: sub.status
      };
    });

    expect(calibrated.mastery).toBe(60);
    expect(calibrated.evaluative).toBe(48); // 60 * 0.8
    expect(calibrated.status).toBe('practice'); // unlocked >= 60%

    // 3. Test EMA BKT Collation Formula:
    // M_new = round(60 * 0.75 + 100 * 0.25) = round(45 + 25) = 70%
    await page.evaluate(() => {
      window.studentStore.recordAttempt('accounting', {
        isCorrect: true,
        score: 5,
        totalMarks: 5,
        xp: 35,
        mode: 'practice'
      });
    });

    const postAttempt = await page.evaluate(() => {
      const sub = window.studentStore.getSubject('accounting');
      return {
        mastery: sub.formativeMastery,
        attempts: sub.questionsAttempted,
        passed: sub.questionsPassed
      };
    });

    expect(postAttempt.mastery).toBe(70);
    expect(postAttempt.attempts).toBe(2);
    expect(postAttempt.passed).toBe(1);
  });

  test('Collation 2: Progression Gating, Exam Mode Unlock & Evaluative Weighting', async ({ page }) => {
    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.studentStore !== 'undefined', { timeout: 15000 });

    // 1. Test Scaffold Stage (< 60%)
    await page.evaluate(() => {
      window.studentStore.completeDiagnostic('mathematics', 45);
    });
    const scaffoldState = await page.evaluate(() => window.studentStore.getSubject('mathematics').status);
    expect(scaffoldState).toBe('scaffold');

    // 2. Test Practice Stage (>= 60% and < 80%)
    await page.evaluate(() => {
      window.studentStore.completeDiagnostic('mathematics', 65);
    });
    const practiceState = await page.evaluate(() => window.studentStore.getSubject('mathematics').status);
    expect(practiceState).toBe('practice');

    // 3. Test Practice -> Exam Ready Unlock via recordAttempt:
    // Starting with diagnostic baseline 75%, recording a 100% pass pushes formative to 81%, unlocking 'exam_ready'!
    await page.evaluate(() => {
      window.studentStore.completeDiagnostic('mathematics', 75);
      window.studentStore.recordAttempt('mathematics', {
        isCorrect: true,
        score: 10,
        totalMarks: 10,
        xp: 40,
        mode: 'practice'
      });
    });
    const examReadyState = await page.evaluate(() => window.studentStore.getSubject('mathematics').status);
    expect(examReadyState).toBe('exam_ready');

    // 4. Test Evaluative Score Weighting in Exam Mode:
    // Diagnostic baseline 75% -> Initial evaluative: 75 * 0.8 = 60.
    // Score 100% in exam/assessment mode: round(60 * 0.7 + 100 * 0.3) = round(42 + 30) = 72.
    await page.evaluate(() => {
      window.studentStore.recordAttempt('mathematics', {
        isCorrect: true,
        score: 10,
        totalMarks: 10,
        xp: 50,
        mode: 'assessment'
      });
    });

    const postExamState = await page.evaluate(() => {
      const sub = window.studentStore.getSubject('mathematics');
      return {
        evaluative: sub.evaluativeScore,
        status: sub.status,
        xp: sub.xpEarned
      };
    });

    expect(postExamState.evaluative).toBe(72);
    expect(postExamState.status).toBe('exam_ready');
    expect(postExamState.xp).toBeGreaterThanOrEqual(50);
  });
});
