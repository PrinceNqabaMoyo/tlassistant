import { test, expect } from '@playwright/test';
import { evaluateSubjectTrack } from './helpers/matrixRunner.js';
import { exportCognitiveAuditReport } from '../helpers/cognitiveAuditLogger.js';

/**
 * Grade 9 Senior Phase Matrix Evaluation:
 * Subjects: Mathematics, Natural Sciences, Economic and Management Sciences (EMS)
 * Focus:
 * 1. Authentic UI learner journey & workspace navigation
 * 2. Multi-seed question variability, depth, and 3-tier pre-baked hints
 * 3. Adaptive progression (Diagnostic -> Scaffold -> Practice -> Exam)
 * 4. Accommodation of accelerated, steady, and struggling learner personas
 */

test.describe('Curriculum Matrix Evaluation: Grade 9 Senior Phase', () => {
  const baseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test.afterAll(() => {
    const report = exportCognitiveAuditReport();
    console.log(`\n📄 [Grade 9 Matrix Audit] Exported logs to:`);
    console.log(`   - JSON: ${report.jsonPath}`);
    console.log(`   - HTML: ${report.htmlPath} (${report.totalEntries} entries recorded)\n`);
  });

  test('Grade 9 Mathematics: Integers and Rational Numbers', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 9,
      subject: 'Mathematics',
      topic: 'Integers',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'math',
      testCognitiveRepair: true
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 9 Natural Sciences: Cells as the basic units of life', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 9,
      subject: 'Natural Sciences',
      topic: 'Cells as the basic units of life',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 9 Economic and Management Sciences: The circular flow', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 9,
      subject: 'Economic and Management Sciences',
      topic: 'The circular flow',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'rubric',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });
});
