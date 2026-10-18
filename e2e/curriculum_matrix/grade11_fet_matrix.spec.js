import { test, expect } from '@playwright/test';
import { evaluateSubjectTrack } from './helpers/matrixRunner.js';
import { exportCognitiveAuditReport } from '../helpers/cognitiveAuditLogger.js';

/**
 * Grade 11 FET Phase Matrix Evaluation:
 * Subjects: Mathematics, Math Lit, Tech Maths, Physical Sciences, Life Sciences, Accounting, Business Studies
 * Focus:
 * 1. Authentic UI learner journey & workspace navigation
 * 2. Multi-seed question variability, depth, and 3-tier pre-baked hints
 * 3. Adaptive progression (Diagnostic -> Scaffold -> Practice -> Exam)
 * 4. Accommodation of accelerated, steady, and struggling learner personas
 */

test.describe('Curriculum Matrix Evaluation: Grade 11 FET Phase', () => {
  test.setTimeout(180000);
  const baseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test.afterAll(() => {
    const report = exportCognitiveAuditReport();
    console.log(`\n📄 [Grade 11 Matrix Audit] Exported logs to:`);
    console.log(`   - JSON: ${report.jsonPath}`);
    console.log(`   - HTML: ${report.htmlPath} (${report.totalEntries} entries recorded)\n`);
  });

  test('Grade 11 Mathematics: Exponents and surds', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 11,
      subject: 'Mathematics',
      topic: 'Exponents and surds',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'math',
      testCognitiveRepair: true
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 11 Accounting: Bank reconciliation', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 11,
      subject: 'Accounting',
      topic: 'Bank reconciliation',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'ledger',
      testCognitiveRepair: true
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 11 Physical Sciences: Vectors in two dimensions', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 11,
      subject: 'Physical Sciences',
      topic: 'Vectors in two dimensions',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 11 Business Studies: The challenges of the business environments', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 11,
      subject: 'Business Studies',
      topic: 'The challenges of the business environments',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'rubric',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 11 Life Sciences: Photosynthesis', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 11,
      subject: 'Life Sciences',
      topic: 'Photosynthesis',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 11 Mathematical Literacy: Interest banking and inflation', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 11,
      subject: 'Mathematical Literacy',
      topic: 'Interest banking and inflation',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'standard',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });

  test('Grade 11 Technical Mathematics: Exponents and surds', async ({ page, request }) => {
    const result = await evaluateSubjectTrack({
      page,
      request,
      baseUrl,
      grade: 11,
      subject: 'Technical Mathematics',
      topic: 'Exponents and surds',
      sampleSeeds: [101, 202, 303, 404],
      expectedModality: 'math',
      testCognitiveRepair: false
    });
    expect(result.status).toBe('PASSED');
    expect(result.entropyScore).toBeGreaterThan(0.2);
  });
});
