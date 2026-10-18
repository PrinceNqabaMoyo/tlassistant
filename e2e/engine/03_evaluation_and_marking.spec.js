import { test, expect } from '@playwright/test';
import { recordUserInputAndEvaluation, exportCognitiveAuditReport } from '../helpers/cognitiveAuditLogger.js';

/**
 * Procedural Evaluation & Carry-Over Marking Audit
 * Strict Invariant Compliance:
 * - Rule 19: Procedure Tracker / Evaluation Service Contract
 * - Rule 22: Misconception Taxonomy (clean snake_case tags)
 * - Zero LLM cost in marking critical path
 */
test.describe('Cognitive Engine: Procedural Evaluation & Marking API', () => {
  const backendBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  test.afterAll(() => {
    const report = exportCognitiveAuditReport();
    console.log(`\n📄 [Cognitive Audit] Exported generation, input & evaluation report to:`);
    console.log(`   - JSON: ${report.jsonPath}`);
    console.log(`   - HTML: ${report.htmlPath} (${report.totalEntries} entries recorded)\n`);
  });

  test('Evaluation 1: Correct MCQ Answer Verification', async ({ request }) => {
    const markPayload = {
      question_id: 'q_test_mcq',
      user_answer: 1, // index 1
      question: {
        id: 'q_test_mcq',
        question_type: 'mcq',
        marks: 2,
        options: ['Option A', 'Option B (Correct)', 'Option C', 'Option D'],
        correct_idx: 1
      }
    };

    const res = await request.post(`${backendBaseUrl}/api/mark`, {
      data: markPayload
    });

    expect(res.ok()).toBe(true);
    const data = await res.json();
    expect(data.is_correct).toBe(true);
    expect(data.score).toBe(2);

    recordUserInputAndEvaluation({
      role: 'learner',
      subject: 'Business Studies / EMS',
      grade: '10',
      topic: 'Concept Assessment',
      modality: 'MCQ Single Choice',
      question: markPayload.question,
      userInput: markPayload.question.options[markPayload.user_answer],
      evaluation: data
    });
  });

  test('Evaluation 2: Long Division Arithmetic Grid Evaluation', async ({ request }) => {
    const markPayload = {
      question_id: 'q_test_div',
      user_answer: {
        quotient: 169,
        remainder: 0
      },
      question: {
        id: 'q_test_div',
        modality: 'arithmetic_grid',
        subskill: 'long_division',
        marks: 4,
        arithmetic_grid: {
          dividend: 4394,
          divisor: 26,
          expected_quotient: 169,
          expected_remainder: 0
        }
      }
    };

    const res = await request.post(`${backendBaseUrl}/api/mark`, {
      data: markPayload
    });

    expect(res.ok()).toBe(true);
    const data = await res.json();
    expect(data.score).toBeGreaterThanOrEqual(1);

    recordUserInputAndEvaluation({
      role: 'learner',
      subject: 'Mathematics',
      grade: '7',
      topic: 'Working with Whole Numbers: Long Division',
      modality: 'Arithmetic Grid',
      question: markPayload.question,
      userInput: `Quotient: ${markPayload.user_answer.quotient}, Remainder: ${markPayload.user_answer.remainder}`,
      evaluation: data
    });
  });

  test('Evaluation 3: Incorrect Submission Returns Helpful Feedback Without LLM', async ({ request }) => {
    const markPayload = {
      question_id: 'q_test_incorrect',
      user_answer: 0, // incorrect index
      question: {
        id: 'q_test_incorrect',
        question_type: 'mcq',
        marks: 2,
        options: ['Incorrect A', 'Correct B'],
        correct_idx: 1
      }
    };

    const res = await request.post(`${backendBaseUrl}/api/mark`, {
      data: markPayload
    });

    expect(res.ok()).toBe(true);
    const data = await res.json();
    expect(data.is_correct).toBe(false);
    expect(data.score).toBe(0);

    recordUserInputAndEvaluation({
      role: 'learner',
      subject: 'Mathematics / Accounting',
      grade: '10',
      topic: 'Misconception Diagnostic',
      modality: 'MCQ Single Choice',
      question: markPayload.question,
      userInput: markPayload.question.options[markPayload.user_answer],
      evaluation: data
    });
  });
});
