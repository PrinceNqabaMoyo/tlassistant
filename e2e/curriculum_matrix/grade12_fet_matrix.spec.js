import { test, expect } from '@playwright/test';
import { evaluateSubjectTrack } from './helpers/matrixRunner.js';
import { exportCognitiveAuditReport } from '../helpers/cognitiveAuditLogger.js';

/**
 * Grade 12 FET Phase Matrix Evaluation (Matric Exit):
 * Subjects: Mathematics, Math Lit, Tech Maths, Physical Sciences, Life Sciences, Accounting, Business Studies
 * Focus:
 * 1. Authentic UI learner journey & workspace navigation
 * 2. Multi-seed question variability, depth, and 3-tier pre-baked hints
 * 3. Adaptive progression (Diagnostic -> Scaffold -> Practice -> Exam)
 * 4. Accommodation of accelerated, steady, and struggling learner personas
 */

test.describe('Curriculum Matrix Evaluation: Grade 12 FET Phase', () => {
  test.setTimeout(180000);
  const baseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test.afterAll(() => {
    const report = exportCognitiveAuditReport();
    console.log(`\n📄 [Grade 12 Matrix Audit] Exported logs to:`);
    console.log(`   - JSON: ${report.jsonPath}`);
    console.log(`   - HTML: ${report.htmlPath} (${report.totalEntries} entries recorded)\n`);
  });

  test('Grade 12 Mathematics: Differential calculus', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 12,
      subject: 'Mathematics',
      topic: 'Differential calculus',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'math',
      testCognitiveRepair: true
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 12 Accounting: Companies', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 12,
      subject: 'Accounting',
      topic: 'Companies',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'ledger',
      testCognitiveRepair: true
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 12 Physical Sciences: Momentum and Impulse', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 12,
      subject: 'Physical Sciences',
      topic: 'Momentum and Impulse',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 12 Business Studies: Impact of recent legislation on businesses', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 12,
      subject: 'Business Studies',
      topic: 'Impact of recent legislation on businesses',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'rubric',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 12 Life Sciences: Genetics and inheritance', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 12,
      subject: 'Life Sciences',
      topic: 'Genetics and inheritance',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 12 Mathematical Literacy: Income tax', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 12,
      subject: 'Mathematical Literacy',
      topic: 'Income tax',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 12 Technical Mathematics: Complex numbers', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 12,
      subject: 'Technical Mathematics',
      topic: 'Complex numbers',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'math',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });
});
