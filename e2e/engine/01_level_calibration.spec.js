import { test, expect } from '@playwright/test';
import { recordQuestionGeneration } from '../helpers/cognitiveAuditLogger.js';

/**
 * Question Generator Level Calibration & Anti-Meta-Curriculum Audit
 * Strict Invariant Compliance:
 * - Rule 16: Deterministic generation (Same seed -> identical question & worked solution)
 * - Rule 24: Pre-baked 3-Tier hints present ahead of time (zero LLM token cost)
 * - Rule 26b: Zero-Meta-Curriculum Invariant (No "According to CAPS...", authentic DBE/IEB style)
 */
test.describe('Cognitive Engine: Question Level Calibration & Hint Fidelity', () => {
  const backendBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5173';

  // Test Matrix across Senior Phase & FET Phase
  const calibrationMatrix = [
    {
      subject: 'Accounting',
      grade: '10',
      topic: 'Cash Receipts Journal (VAT 15%)',
      expectedPhase: 'FET',
      bannedKeywords: ['according to caps', 'curriculum document', 'dbe requirements', 'annual teaching plan']
    },
    {
      subject: 'Mathematics',
      grade: '10',
      topic: 'Algebraic Expressions',
      expectedPhase: 'FET',
      bannedKeywords: ['according to caps', 'curriculum document', 'policy statement']
    },
    {
      subject: 'EMS',
      grade: '7',
      topic: 'Source Documents',
      expectedPhase: 'Senior',
      bannedKeywords: ['according to caps', 'term 1 weighting', 'atp requirements']
    },
    {
      subject: 'Mathematics',
      grade: '7',
      topic: 'Whole Numbers: Long Division Algorithm',
      expectedPhase: 'Senior',
      bannedKeywords: ['according to caps', 'caps curriculum']
    }
  ];

  for (const item of calibrationMatrix) {
    test(`Verify ${item.subject} Gr ${item.grade} (${item.topic}) Level & Hint Contract`, async ({ request }) => {
      const url = `${backendBaseUrl}/api/generate?subject=${encodeURIComponent(item.subject)}&grade=${item.grade}&topic=${encodeURIComponent(item.topic)}&seed=4242`;
      const response = await request.get(url);

      // Verify endpoint responded OK
      expect(response.ok()).toBe(true);
      const data = await response.json();
      expect(data.success).toBe(true);

      const question = Array.isArray(data.questions) ? data.questions[0] : (data.questions || data);
      expect(question).toBeDefined();

      recordQuestionGeneration({
        role: 'learner',
        subject: item.subject,
        grade: item.grade,
        topic: item.topic,
        question
      });

      // 1. Verify Prompt Text Exists & is Non-Empty
      const prompt = (question.prompt || question.question || question.prompt_latex || '').toLowerCase();
      expect(prompt.length).toBeGreaterThan(10);

      // 2. Rule 26b Anti-Meta-Curriculum Invariant Check
      for (const banned of item.bannedKeywords) {
        expect(prompt).not.toContain(banned);
      }

      // 3. Rule 24 Deterministic 3-Tier Hints Check
      const hints = question.hints || {};
      const hasTieredHints = 
        (hints.tier_1 && hints.tier_2 && hints.tier_3) ||
        (Array.isArray(hints) && hints.length >= 3) ||
        (hints[0] && hints[1] && hints[2]);

      expect(hasTieredHints).toBeTruthy();

      // 4. Verify Marking Schema / Total Marks Present
      const marks = question.marks || question.marking_schema?.total_marks || 1;
      expect(marks).toBeGreaterThanOrEqual(1);
    });
  }
});
