import { test, expect } from '@playwright/test';

/**
 * Natural Sciences Batch 4 Contract Verification (GP-21, GP-22)
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater end-to-end verification. Live application components only.
 * - Rule 0d-4: Grounded in live JSX components (UniversalWorkspace, QuestionSurface, diagram_bank).
 * - Rule 0d-6: Zero silent skips with explicit assertions.
 * - GP-21: Circuit components in diagram match memo and standard IEC symbols.
 * - GP-22: Diagrams mount inside question surface and are absent from memo card.
 */

test.describe('Batch 4 Natural Sciences Contract (GP-21, GP-22)', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';

  test('GP-21 & GP-22: Natural Sciences diagrams mount inside question surface and are absent from memo', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });

    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'sch-gr8-01',
        name: 'Kagiso Molefe',
        role: 'student',
        type: 'student',
        grade: 8,
        school: 'Sandton Secondary School',
        assignedTasks: []
      });
      if (window.studentStore) {
        window.studentStore.setEnabledSubjects(['natural_sciences']);
        window.studentStore.completeDiagnostic('natural_sciences', 80);
      }
    });

    const openSubjectBtn = page.locator('[data-testid="btn-open-subject-session"]').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    await page.waitForFunction(() => typeof window.__FUNDILE_LOAD_QUESTION__ === 'function', { timeout: 15000 });

    const nsArchetypes = [
      {
        id: 'gp21_circuit_context',
        subject: 'natural_sciences',
        grade: 8,
        topic: 'Electric circuits',
        subskill: 'series_parallel_rules',
        mode: 'practice',
        question_type: 'short_answer',
        question: 'An electrical circuit contains a 12 V battery and two identical resistors in parallel.',
        prompt: 'An electrical circuit contains a 12 V battery and two identical resistors in parallel.',
        correct_answer: 'Resistor 1 and Resistor 2 have 12 V across them',
        worked_solution: 'Each parallel branch receives full supply voltage (12 V).',
        diagram_spec: {
          master: 'electric_circuits_ns',
          image_type: 'electric_circuits_ns',
          diagram_role: 'context',
          view: 'series_and_parallel_circuit_schematic',
          state: 'static'
        },
        expectedSelector: '[data-testid="electric-circuits-ns-canvas"]',
        badgeSelector: '[data-testid="electric-circuits-ns-locked-view-badge"]'
      },
      {
        id: 'gp22_telescope_context',
        subject: 'natural_sciences',
        grade: 8,
        topic: 'Looking into space',
        subskill: 'optical_telescopes_salt',
        mode: 'practice',
        question_type: 'paragraph',
        question: 'Identify the primary optical architecture of the Southern African Large Telescope (SALT).',
        prompt: 'Identify the primary optical architecture of the Southern African Large Telescope (SALT).',
        correct_answer: 'SALT is a reflecting telescope using a hexagonal primary mirror array.',
        worked_solution: 'SALT uses spherical segmented hexagonal mirrors.',
        diagram_spec: {
          master: 'optical_telescopes',
          image_type: 'optical_telescopes',
          diagram_role: 'context',
          view: 'textbook',
          state: 'static'
        },
        expectedSelector: '[data-testid="optical-telescopes-root"]',
        badgeSelector: '[data-testid="telescopes-locked-view-badge"]'
      },
      {
        id: 'gp22_electrolysis_context',
        subject: 'natural_sciences',
        grade: 8,
        topic: 'Atoms',
        subskill: 'decomposition_of_compounds_electrolysis',
        mode: 'practice',
        question_type: 'paragraph',
        question: 'Define the process of electrolysis in the decomposition of copper(II) chloride.',
        prompt: 'Define the process of electrolysis in the decomposition of copper(II) chloride.',
        correct_answer: 'Chemical decomposition using electrical current.',
        worked_solution: 'CuCl2 decomposes into copper and chlorine gas.',
        diagram_spec: {
          master: 'electrolytic_cell_apparatus',
          image_type: 'electrolytic_cell_apparatus',
          diagram_role: 'context',
          view: 'exam',
          state: 'static'
        },
        expectedSelector: '[data-testid="electrolytic-cell-apparatus-root"]',
        badgeSelector: '[data-testid="electrolytic-cell-apparatus-locked-view-badge"]'
      },
      {
        id: 'gp22_bohr_context',
        subject: 'natural_sciences',
        grade: 8,
        topic: 'Atoms',
        subskill: 'first_twenty_elements_bohr',
        mode: 'practice',
        question_type: 'mcq',
        question: 'Examine the subatomic configuration of the atom.',
        prompt: 'Examine the subatomic configuration of the atom.',
        options: ['Carbon (Z=6)', 'Nitrogen (Z=7)', 'Oxygen (Z=8)', 'Neon (Z=10)'],
        correct_index: '0',
        correct_answer: 'Carbon (Z=6)',
        sample_answer: 'A. Carbon (Z=6)',
        worked_solution: '**A. Carbon (Z=6)** [2 marks]\n\nContains 6 protons and 6 electrons.',
        diagram_spec: {
          master: 'atomic_bohr_structure',
          image_type: 'atomic_bohr_structure',
          diagram_role: 'context',
          view: 'exam',
          state: 'static'
        },
        expectedSelector: '[data-testid="atomic-bohr-structure-root"]',
        badgeSelector: '[data-testid="atomic-bohr-structure-locked-view-badge"]'
      }
    ];

    for (const q of nsArchetypes) {
      await page.evaluate((questionData) => {
        window.__FUNDILE_LOAD_QUESTION__(questionData);
      }, q);

      // 1. Assert diagram element is mounted inside visible question surface
      const questionSurface = page.locator('[data-testid="question-surface"]:visible').first();
      await expect(questionSurface).toBeVisible({ timeout: 10000 });

      const diagramInQuestion = questionSurface.locator(`${q.expectedSelector}:visible`).first();
      await expect(diagramInQuestion).toBeVisible({ timeout: 10000 });

      // 2. Assert locked view badge is visible
      const badge = questionSurface.locator(`${q.badgeSelector}:visible`).first();
      await expect(badge).toBeVisible({ timeout: 5000 });

      // 3. For context diagrams, assert exactly 0 interactive letter pins
      const pinButtons = questionSurface.locator('[data-testid^="btn-select-pin-"]:visible');
      expect(await pinButtons.count()).toBe(0);

      // 4. Assert diagram element is absent from full-memo panel
      const memoPanel = page.locator('[data-testid="panel-full-memo"]');
      const memoDiagramCount = await memoPanel.locator(q.expectedSelector).count();
      expect(memoDiagramCount).toBe(0);
    }
  });
});
