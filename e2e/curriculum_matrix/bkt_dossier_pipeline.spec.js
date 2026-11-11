import { test, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';
import { writeTopicDossierFile } from './helpers/bktDossierWriter.js';

/**
 * Comprehensive Grade-to-Grade, Subject-to-Subject, Topic-to-Topic BKT Progression & Dossier Pipeline
 *
 * Tests adaptive progression for:
 *   1. high-performing students (Diagnostic 100% -> 50 Practice Qs -> 3 Exams)
 *   2. medium-performing students (Diagnostic 67% -> 50 Practice Qs -> 3 Exams)
 *   3. low-performing students (Diagnostic 33% -> Scaffold Gap Regression -> Micro-Drills -> 50 Practice Qs -> 3 Exams)
 *
 * Writes every question, student input, expected memorandum answer, and BKT transition in order of BKT to:
 *   `playwright-test/Gr{grade}/{Subject}/{topic}_{performance-level}.md`
 */

const SUBJECT_GRADE_MATRIX = [
  // Grade 7 Senior Phase
  { grade: 7, subject: 'Mathematics' },
  { grade: 7, subject: 'Economic and Management Sciences' },
  { grade: 7, subject: 'Natural Sciences' },
  // Grade 8 Senior Phase
  { grade: 8, subject: 'Mathematics' },
  { grade: 8, subject: 'Economic and Management Sciences' },
  { grade: 8, subject: 'Natural Sciences' },
  // Grade 9 Senior Phase
  { grade: 9, subject: 'Mathematics' },
  { grade: 9, subject: 'Economic and Management Sciences' },
  { grade: 9, subject: 'Natural Sciences' },
  // Grade 10 FET Phase
  { grade: 10, subject: 'Mathematics' },
  { grade: 10, subject: 'Technical Mathematics' },
  { grade: 10, subject: 'Mathematical Literacy' },
  { grade: 10, subject: 'Physical Sciences' },
  { grade: 10, subject: 'Life Sciences' },
  { grade: 10, subject: 'Accounting' },
  { grade: 10, subject: 'Business Studies' },
  // Grade 11 FET Phase
  { grade: 11, subject: 'Mathematics' },
  { grade: 11, subject: 'Technical Mathematics' },
  { grade: 11, subject: 'Mathematical Literacy' },
  { grade: 11, subject: 'Physical Sciences' },
  { grade: 11, subject: 'Life Sciences' },
  { grade: 11, subject: 'Accounting' },
  { grade: 11, subject: 'Business Studies' },
  // Grade 12 FET Phase
  { grade: 12, subject: 'Mathematics' },
  { grade: 12, subject: 'Technical Mathematics' },
  { grade: 12, subject: 'Mathematical Literacy' },
  { grade: 12, subject: 'Physical Sciences' },
  { grade: 12, subject: 'Life Sciences' },
  { grade: 12, subject: 'Accounting' },
  { grade: 12, subject: 'Business Studies' }
];

test.describe('BKT Adaptive Progression & Curriculum Dossier Pipeline (Grades 7–12)', () => {
  test.setTimeout(900000);
  const apiUrl = process.env.VITE_API_BASE_URL || 'http://127.0.0.1:5001';
  const summaryRecords = [];

  test.beforeAll(() => {
    const outDir = path.join(process.cwd(), 'playwright-test');
    if (fs.existsSync(outDir)) {
      for (let g = 7; g <= 12; g++) {
        const grDir = path.join(outDir, `Gr${g}`);
        if (fs.existsSync(grDir)) {
          fs.rmSync(grDir, { recursive: true, force: true });
        }
      }
      const summaryFile = path.join(outDir, 'PIPELINE_SUMMARY.md');
      if (fs.existsSync(summaryFile)) {
        fs.unlinkSync(summaryFile);
      }
      console.log('🧹 [BKT Dossier Pipeline] Cleaned existing playwright-test/ files before fresh run.');
    }
  });

  test.afterAll(() => {
    if (summaryRecords.length === 0) return;
    const outDir = path.join(process.cwd(), 'playwright-test');
    fs.mkdirSync(outDir, { recursive: true });
    const summaryPath = path.join(outDir, 'PIPELINE_SUMMARY.md');

    let totalFiles = 0;
    let totalQuestions = 0;
    let totalIssues = 0;
    const lines = [
      '# Fundile National Curriculum BKT Dossier Pipeline Summary',
      '',
      '| Grade | Subject | Topic | Persona | Practice Qs | Unique Qs | Entropy | Exams | Total Qs | Final BKT | Status | Issues | Dossier File |',
      '| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: | :--- |'
    ];

    for (const rec of summaryRecords) {
      totalFiles += 1;
      totalQuestions += rec.totalQuestions;
      totalIssues += rec.issuesCount;
      lines.push(
        `| Gr${rec.grade} | ${rec.subject} | ${rec.topic} | \`${rec.persona}\` | ${rec.practiceCount} | ${rec.uniquePractice} | ${Math.round(rec.practiceEntropy * 100)}% | ${rec.examsCount} | ${rec.totalQuestions} | **${rec.finalBkt}%** | \`${rec.finalStatus}\` | ${rec.issuesCount === 0 ? '✅ 0' : `⚠️ ${rec.issuesCount}`} | \`${rec.relPath}\` |`
      );
    }

    lines.unshift(
      `- **Total Dossier Files Written:** **${totalFiles}**`,
      `- **Total Questions Generated & Graded:** **${totalQuestions}**`,
      `- **Total Pipeline Issues Detected:** **${totalIssues}**`,
      ''
    );

    fs.writeFileSync(summaryPath, lines.join('\n'), 'utf8');
    console.log(`\n📊 [BKT Dossier Pipeline] Summary written to: ${summaryPath} (${totalFiles} files, ${totalQuestions} questions)\n`);
  });

  for (const track of SUBJECT_GRADE_MATRIX) {
    const { grade, subject } = track;

    test(`Grade ${grade} • ${subject}: All Topics x 3 Personas (50 Practice Qs + 3 Exams)`, async ({ request }) => {
      // 1. Fetch all curriculum topics for this Grade & Subject
      const catalogRes = await request.get(
        `${apiUrl}/api/curriculum/archetypes?subject=${encodeURIComponent(subject)}&grade=${grade}`
      );
      expect(catalogRes.ok(), `Archetype catalog request must succeed for Gr${grade} ${subject}`).toBe(true);
      const catalogData = await catalogRes.json();
      expect(catalogData.success).toBe(true);

      const topics = Array.isArray(catalogData.topics) && catalogData.topics.length > 0
        ? catalogData.topics.map((t) => t.topic)
        : [];
      expect(topics.length, `At least 1 curriculum topic must exist for Gr${grade} ${subject}`).toBeGreaterThan(0);

      for (const topic of topics) {
        const dossierRes = await request.post(`${apiUrl}/api/audit/bkt-dossier`, {
          data: {
            grade,
            subject,
            topic,
            personas: ['high-performing', 'medium-performing', 'low-performing'],
            practice_count: 50,
            exams_count: 3,
            questions_per_exam: 5
          }
        });
        expect(dossierRes.ok(), `POST /api/audit/bkt-dossier failed for Gr${grade} ${subject} - ${topic}`).toBe(true);
        const payload = await dossierRes.json();
        expect(payload.success, `Dossier generation error for ${topic}: ${payload.error || ''}`).toBe(true);
        expect(Array.isArray(payload.dossiers)).toBe(true);
        expect(payload.dossiers.length).toBe(3);

        for (const dossier of payload.dossiers) {
          const writtenPath = writeTopicDossierFile(dossier);
          const relPath = path.relative(process.cwd(), writtenPath).replace(/\\/g, '/');

          summaryRecords.push({
            grade,
            subject,
            topic,
            persona: dossier.persona,
            practiceCount: dossier.practice_questions_count,
            uniquePractice: dossier.unique_practice_questions ?? dossier.practice_questions_count,
            practiceEntropy: dossier.practice_entropy ?? 1.0,
            examsCount: dossier.exams_completed,
            totalQuestions: dossier.total_questions,
            finalBkt: dossier.final_bkt_mastery,
            finalStatus: dossier.final_status,
            issuesCount: (dossier.issues || []).length,
            relPath
          });

          // Enforce pipeline requirements
          expect(
            dossier.practice_questions_count,
            `Practice count must be >= 50 for Gr${grade} ${subject} (${topic}) [${dossier.persona}]`
          ).toBeGreaterThanOrEqual(50);
          expect(
            dossier.exams_completed,
            `Exams completed must be 3 for Gr${grade} ${subject} (${topic}) [${dossier.persona}]`
          ).toBe(3);
          expect(
            dossier.issues,
            `Zero generator/evaluation issues expected for Gr${grade} ${subject} (${topic}) [${dossier.persona}]`
          ).toEqual([]);

          // Verify adaptive BKT progression invariants per persona
          if (dossier.persona === 'high-performing') {
            expect(dossier.final_bkt_mastery).toBeGreaterThanOrEqual(85);
            expect(dossier.final_status).toBe('exam_ready');
          } else if (dossier.persona === 'medium-performing') {
            expect(dossier.final_bkt_mastery).toBeGreaterThanOrEqual(80);
            expect(dossier.final_status).toBe('exam_ready');
          } else if (dossier.persona === 'low-performing') {
            const triggeredGap = dossier.steps.some((s) => s.prerequisite_gap_detected);
            const triggeredMicroDrill = dossier.steps.some((s) => s.stage === 'micro_drill');
            expect(triggeredGap, `Low-performing learner must trigger prerequisite_gap_detected in ${topic}`).toBe(true);
            expect(triggeredMicroDrill, `Low-performing learner must receive micro_drill remediation in ${topic}`).toBe(true);
            expect(dossier.final_bkt_mastery).toBeGreaterThanOrEqual(80);
          }
        }
      }
    });
  }
});
