import { test, expect } from '@playwright/test';

/**
 * Maths Batch 2 Contract Verification (GP-11)
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater end-to-end verification. Live application components only.
 * - Rule 0d-4: Grounded in live JSX components (UniversalWorkspace, QuestionSurface).
 * - Rule 0d-6: Zero silent skips with explicit assertions.
 * - GP-11: Diagrams mount in question card for 2D/3D geometry, Pythagoras, transformations, patterns.
 */

test.describe('Batch 2 Maths Contract (GP-11)', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';

  test('GP-11: Geometric & pattern diagrams mount inside question surface', async ({ page }) => {
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
        window.studentStore.setEnabledSubjects(['mathematics']);
        window.studentStore.completeDiagnostic('mathematics', 75);
      }
    });

    const openSubjectBtn = page.locator('[data-testid="btn-open-subject-session"]').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    await page.waitForFunction(() => typeof window.__FUNDILE_LOAD_QUESTION__ === 'function', { timeout: 15000 });

    const testArchetypes = [
      {
        id: 'gp11_pythagoras',
        subject: 'mathematics',
        grade: 8,
        topic: 'The Theorem of Pythagoras',
        subskill: 'hypotenuse_calculation',
        mode: 'practice',
        question: 'Calculate the length of hypotenuse AC in right-angled triangle ABC.',
        prompt: 'Calculate the length of hypotenuse AC in right-angled triangle ABC.',
        correct_answer: '10 cm',
        diagram_spec: {
          kind: 'triangle',
          points: { A: [0.0, 6.0], B: [0.0, 0.0], C: [8.0, 0.0] },
          vertices: ['A', 'B', 'C'],
          diagram_role: 'context'
        }
      },
      {
        id: 'gp11_transformation',
        subject: 'mathematics',
        grade: 8,
        topic: 'Transformation geometry',
        subskill: 'translation',
        mode: 'practice',
        question: 'Point A(2; 3) is translated 4 units right and 2 units up. Determine coordinates of A\'.',
        prompt: 'Point A(2; 3) is translated 4 units right and 2 units up. Determine coordinates of A\'.',
        correct_answer: '(6; 5)',
        diagram_spec: {
          kind: 'coordinate_transformation',
          diagram_role: 'context',
          points: { P: [2, 3] },
          grid: { x_min: -10, x_max: 10, y_min: -10, y_max: 10 }
        }
      },
      {
        id: 'gp11_patterns',
        subject: 'mathematics',
        grade: 8,
        topic: 'Numeric and geometric patterns',
        subskill: 'dot_pattern',
        mode: 'practice',
        question: 'Study the geometric tile pattern shown in the diagram. How many tiles are in Figure 4?',
        prompt: 'Study the geometric tile pattern shown in the diagram. How many tiles are in Figure 4?',
        correct_answer: '10',
        diagram_spec: {
          kind: 'dot_pattern',
          step_counts: [1, 4, 7, 10],
          arrangement: 'tiles',
          diagram_role: 'context',
          show_difference: false
        }
      }
    ];

    for (const q of testArchetypes) {
      await page.evaluate((item) => {
        window.__FUNDILE_LOAD_QUESTION__(item);
      }, q);

      // Verify diagram is mounted inside the question surface
      const qSurface = page.locator('[data-testid="question-surface"]:visible').first();
      await expect(qSurface).toBeVisible({ timeout: 5000 });

      // Diagram spec rendering or container exists inside question surface
      const diagramContainer = qSurface.locator('svg, canvas').first();
      await expect(diagramContainer).toBeVisible({ timeout: 5000 });

      // Assert diagram is absent from full-memo panel
      const memoPanel = page.locator('[data-testid="panel-full-memo"]');
      await expect(memoPanel.locator('svg, canvas')).toHaveCount(0);
    }
  });
});
