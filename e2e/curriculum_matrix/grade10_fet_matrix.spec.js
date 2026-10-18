import { test, expect } from '@playwright/test';
import { evaluateSubjectTrack } from './helpers/matrixRunner.js';
import { exportCognitiveAuditReport } from '../helpers/cognitiveAuditLogger.js';

/**
 * Grade 10 FET Phase Matrix Evaluation:
 * Subjects: Mathematics, Math Lit, Tech Maths, Physical Sciences, Life Sciences, Accounting, Business Studies
 * Focus:
 * 1. Authentic UI learner journey & workspace navigation
 * 2. Multi-seed question variability, depth, and 3-tier pre-baked hints
 * 3. Adaptive progression (Diagnostic -> Scaffold -> Practice -> Exam)
 * 4. Accommodation of accelerated, steady, and struggling learner personas
 */

test.describe('Curriculum Matrix Evaluation: Grade 10 FET Phase', () => {
  test.setTimeout(180000);
  const baseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test.afterAll(() => {
    const report = exportCognitiveAuditReport();
    console.log(`\n📄 [Grade 10 Matrix Audit] Exported logs to:`);
    console.log(`   - JSON: ${report.jsonPath}`);
    console.log(`   - HTML: ${report.htmlPath} (${report.totalEntries} entries recorded)\n`);
  });

  test('Grade 10 Mathematics: Algebraic expressions', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 10,
      subject: 'Mathematics',
      topic: 'Algebraic expressions',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'math',
      testCognitiveRepair: true
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 10 Accounting: Financial accounting of a sole trader', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 10,
      subject: 'Accounting',
      topic: 'Financial accounting of a sole trader',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'ledger',
      testCognitiveRepair: true
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 10 Physical Sciences: Classification of matter', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 10,
      subject: 'Physical Sciences',
      topic: 'Classification of matter',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 10 Business Studies: The macro environment', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 10,
      subject: 'Business Studies',
      topic: 'The macro environment',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'rubric',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 10 Life Sciences: The chemistry of life', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 10,
      subject: 'Life Sciences',
      topic: 'The chemistry of life',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 10 Mathematical Literacy: Personal income expenditure and budgets', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 10,
      subject: 'Mathematical Literacy',
      topic: 'Personal income expenditure and budgets',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 10 Technical Mathematics: Number Systems', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 10,
      subject: 'Technical Mathematics',
      topic: 'Number Systems',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'math',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });
});
