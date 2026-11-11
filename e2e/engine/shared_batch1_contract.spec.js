import { test, expect } from '@playwright/test';

/**
 * Shared Batch 1 Contract Verification (GP-3, GP-5, GP-6)
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater end-to-end verification. Live application components only.
 * - Rule 0d-4: Grounded in live JSX components (UniversalWorkspace, BioDiagramModalityRenderer, LedgerModalityRenderer).
 * - Rule 0d-6: Zero silent skips with explicit assertions.
 * - GP-3: Context diagrams render 0 pins; dynamic container title (not generic 'BIOLOGICAL STRUCTURE SCHEMATIC').
 * - GP-5: Stimulus diagram inside [data-testid="question-surface"] and absent from memo panel.
 * - GP-6: Journal tables: no-entry cells stay editable; transactions list rendered when present.
 */

test.describe('Batch 1 Shared Contract (GP-3, GP-5, GP-6)', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';

  test('GP-3 & GP-5: Question-card diagram placement and context diagram pin suppression', async ({ page }) => {
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
      if (window.studentStore) {
        window.studentStore.setEnabledSubjects(['natural_sciences', 'accounting', 'mathematics']);
        ['natural_sciences', 'accounting', 'mathematics'].forEach(s => window.studentStore.completeDiagnostic(s, 75));
      }
    });

    // Mount workspace by clicking Open Subject Session
    const openSubjectBtn = page.locator('[data-testid="btn-open-subject-session"]').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    // Await LearnerAppContainer mounting its test hook
    await page.waitForFunction(() => typeof window.__FUNDILE_LOAD_QUESTION__ === 'function', { timeout: 15000 });

    const contextQuestion = {
      id: 'gp3_context_test',
      question_id: 'gp3_context_test',
      subject: 'natural_sciences',
      grade: 8,
      topic: 'Particle model of matter',
      subskill: 'particle_model',
      mode: 'practice',
      modality: 'bio_diagram',
      diagram_role: 'context',
      question_type: 'short_answer',
      question: 'Study the particle model diagram below. What phase of matter is illustrated?',
      prompt: 'Study the particle model diagram below. What phase of matter is illustrated?',
      correct_answer: 'Gas phase',
      marks: 2,
      diagram_spec: {
        master: 'particle_model',
        image_type: 'particle_model',
        diagram_role: 'context',
        role: 'context',
        view: 'textbook',
        grade_mask: 'g8',
        viewBox: '0 0 600 480',
        pins: [
          { pin: 'A', ref: 'ref_0', anchor: [200, 180], side: 'left', role: 'target' },
          { pin: 'B', ref: 'ref_1', anchor: [380, 180], side: 'right', role: 'distractor' },
        ],
        landmarks: [],
      },
    };

    await page.evaluate(({ q }) => {
      window.__FUNDILE_LOAD_QUESTION__(q, 'Particle model of matter');
    }, { q: contextQuestion });

    // 1. Verify stimulus diagram is mounted on the question surface (GP-5)
    const questionSurface = page.locator('[data-testid="question-surface"]').first();
    await expect(questionSurface).toBeVisible({ timeout: 15000 });
    const diagramCanvas = page.locator('[data-testid="bio-diagram-canvas"]').first();
    await expect(diagramCanvas).toBeVisible({ timeout: 15000 });

    // 2. Verify diagram is absent from full-memo panel (GP-5)
    const memoPanel = page.locator('[data-testid="panel-full-memo"]');
    await expect(memoPanel).toHaveCount(0);

    // 3. Verify GP-3: Context diagram suppresses all pins (0 pins rendered)
    const pins = page.locator('[data-testid^="btn-select-pin-"]');
    await expect(pins).toHaveCount(0);

    // 4. Verify GP-3: Title does NOT say 'BIOLOGICAL STRUCTURE SCHEMATIC' for non-bio master
    const canvasText = await diagramCanvas.textContent();
    expect(canvasText).not.toContain('BIOLOGICAL STRUCTURE SCHEMATIC');
    expect(canvasText).toContain('Particle Model of Matter Master');
  });

  test('GP-6: Journal tables allow typing in blank non-required cells & display transactions', async ({ page }) => {
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
      if (window.studentStore) {
        window.studentStore.setEnabledSubjects(['accounting']);
        window.studentStore.completeDiagnostic('accounting', 75);
      }
    });

    const openSubjectBtn = page.locator('[data-testid="btn-open-subject-session"]').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    await page.waitForFunction(() => typeof window.__FUNDILE_LOAD_QUESTION__ === 'function', { timeout: 15000 });

    const journalQuestion = {
      id: 'gp6_journal_test',
      question_id: 'gp6_journal_test',
      subject: 'economic_and_management_sciences',
      grade: 8,
      topic: 'Cash Receipts Journal',
      subskill: 'crj_recording',
      mode: 'practice',
      modality: 'ledger',
      question_type: 'journal',
      question: 'Record the transactions for Day 5 into the Cash Receipts Journal.',
      prompt: 'Record the transactions for Day 5 into the Cash Receipts Journal.',
      marks: 6,
      transactions: [
        'Day 5: Sold merchandise for cash, Receipt 001, Cost of sales R1 200, Sales R1 800.',
        'Day 5: Owner deposited capital into business bank account, R10 000, Receipt 002.'
      ],
      journal: {
        title_fields: ['DOC', 'DAY', 'DETAILS', 'ANALYSIS', 'BANK', 'SALES', 'COST OF SALES'],
        rows: 4
      }
    };

    await page.evaluate(({ q }) => {
      window.__FUNDILE_LOAD_QUESTION__(q, 'Cash Receipts Journal');
    }, { q: journalQuestion });

    // 1. Verify transactions card is rendered (GP-6)
    const txCard = page.locator('[data-testid="ledger-transactions-card"]').first();
    await expect(txCard).toBeVisible({ timeout: 15000 });
    const txContent = await txCard.textContent();
    expect(txContent).toContain('Day 5: Sold merchandise for cash');

    // 2. Verify non-answer blank cells stay editable (GP-6)
    const ledgerInput = page.locator('table tbody input').first();
    await expect(ledgerInput).toBeVisible({ timeout: 15000 });
    await expect(ledgerInput).toBeEnabled();
    await ledgerInput.click();
    await ledgerInput.fill('1800');
    expect(await ledgerInput.inputValue()).toBe('1800');
  });
});
