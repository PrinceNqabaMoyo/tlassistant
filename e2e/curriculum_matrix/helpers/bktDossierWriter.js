import fs from 'fs';
import path from 'path';

/**
 * Formats and writes a complete BKT Adaptive Progression & Question Audit Dossier
 * to `playwright-test/Gr{grade}/{Subject}/{topic}_{performance-level}.md`.
 */

export function sanitizePathSegment(str) {
  return String(str || 'unknown')
    .trim()
    .replace(/[<>:"/\\|?*]+/g, '')
    .replace(/\s+/g, '_')
    .replace(/_+/g, '_')
    .replace(/^_|_$/g, '');
}

export function renderDossierMarkdown(dossier) {
  const {
    grade,
    subject,
    topic,
    persona,
    resolved_generator_key,
    archetypes_discovered = [],
    total_questions,
    practice_questions_count,
    exams_completed,
    exam_questions_count,
    exam_summaries = {},
    final_bkt_mastery,
    final_evaluative_score,
    final_status,
    issues = [],
    passed_pipeline,
    steps = []
  } = dossier;

  const lines = [];
  lines.push(`# BKT Adaptive Progression & Question Audit Dossier`);
  lines.push(``);
  lines.push(`| Attribute | Value |`);
  lines.push(`| :--- | :--- |`);
  lines.push(`| **Grade** | Grade ${grade} (\`Gr${grade}\`) |`);
  lines.push(`| **Subject** | ${subject} |`);
  lines.push(`| **Topic** | ${topic} |`);
  lines.push(`| **Student Performance Level** | \`${persona}\` |`);
  lines.push(`| **Resolved Generator Key** | \`${resolved_generator_key}\` |`);
  lines.push(`| **Archetypes / Subskills** | \`${archetypes_discovered.join(', ')}\` |`);
  lines.push(`| **Total Questions (BKT Order)** | **${total_questions}** |`);
  lines.push(`| **Practice Level Questions** | **${practice_questions_count}** *(Minimum Required: 50)* |`);
  lines.push(`| **Exams Written** | **${exams_completed} Exams** (${exam_questions_count} Exam Questions) |`);
  lines.push(`| **Final Formative BKT Mastery** | **${final_bkt_mastery}%** |`);
  lines.push(`| **Final Evaluative Exam Score** | **${final_evaluative_score}%** |`);
  lines.push(`| **Final Adaptive Status** | \`${final_status}\` |`);
  lines.push(`| **Pipeline Verification Status** | ${passed_pipeline ? '✅ **PASSED (0 Issues)**' : `⚠️ **FLAGGED (${issues.length} Issues)**`} |`);
  lines.push(``);

  if (issues.length > 0) {
    lines.push(`## 🚨 Pipeline Diagnostic & Issue Flags`);
    for (const iss of issues) {
      lines.push(`- ❌ ${iss}`);
    }
    lines.push(``);
  }

  lines.push(`## 📊 Exam-Level Performance Summary (3 Exams)`);
  lines.push(``);
  lines.push(`| Exam | Questions | Score Awarded | Max Marks | Percentage |`);
  lines.push(`| :--- | :---: | :---: | :---: | :---: |`);
  for (const [exNum, exData] of Object.entries(exam_summaries)) {
    const pct = exData.max_score > 0 ? Math.round((exData.score / exData.max_score) * 100) : 0;
    lines.push(`| **Exam ${exNum}** | ${exData.questions} | ${exData.score} | ${exData.max_score} | **${pct}%** |`);
  }
  lines.push(``);

  lines.push(`## 📈 Chronological BKT Progression Matrix`);
  lines.push(``);
  lines.push(`| Step | Progression Stage / Phase | Seed | Question ID | Subskill | Diff | Intent | Score | BKT Mastery (Before -> After) | Status | Misconception / Note |`);
  lines.push(`| :---: | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |`);

  for (const s of steps) {
    const note = s.prerequisite_gap_detected
      ? `⚠️ GAP REGRESSION (${s.misconception_tag || 'error'})`
      : s.misconception_tag
        ? `\`${s.misconception_tag}\``
        : `—`;
    lines.push(
      `| ${s.step} | ${s.phase_label} | ${s.seed} | \`${s.question_id}\` | \`${s.subskill}\` | ${s.difficulty} | ${s.intent} | **${s.score}/${s.max_score}** | ${s.bkt_before}% &rarr; **${s.bkt_after}%** | \`${s.status_after}\` | ${note} |`
    );
  }
  lines.push(``);

  lines.push(`---`);
  lines.push(``);
  lines.push(`## 📝 Complete Question, Student Input & Memorandum Ledger (In Order of BKT)`);
  lines.push(``);

  for (const s of steps) {
    lines.push(`### Step ${s.step}: ${s.phase_label} — \`${s.question_id}\` (Seed: \`${s.seed}\`)`);
    lines.push(
      `- **Stage:** \`${s.stage}\` | **Mode:** \`${s.mode}\` | **Difficulty:** \`${s.difficulty}\` | **Subskill:** \`${s.subskill}\``
    );
    lines.push(
      `- **BKT Mastery:** \`${s.bkt_before}%\` &rarr; \`${s.bkt_after}%\` | **Evaluative Score:** \`${s.evaluative_score}%\` | **Adaptive Status:** \`${s.status_before}\` &rarr; \`${s.status_after}\``
    );
    lines.push(``);
    lines.push(`**Question Prompt:**`);
    lines.push(`> ${String(s.prompt || '').replace(/\n/g, '\n> ')}`);
    lines.push(``);

    if (Array.isArray(s.options) && s.options.length > 0) {
      lines.push(`**Multiple Choice Options:**`);
      s.options.forEach((opt, optIdx) => {
        const letter = String.fromCharCode(65 + optIdx);
        lines.push(`- **[${letter}]** ${String(opt).replace(/\n/g, ' ')}`);
      });
      lines.push(``);
    }

    if (Array.isArray(s.sub_parts) && s.sub_parts.length > 0) {
      lines.push(`**Question Sub-Parts (${s.sub_parts.length} Labeled Answer Boxes):**`);
      for (const sp of s.sub_parts) {
        lines.push(`- **[${sp.part || ''}] ${sp.label || sp.prompt || ''}** *(${sp.marks || 1} mark)* — Expected: \`${sp.expected_answer ?? ''}\``);
      }
      lines.push(``);
    }

    lines.push(`- **Student Inputted Answer (${s.intent}):** ${s.user_input_formatted}`);
    lines.push(`- **Expected / Memo Answer:** ${s.expected_memo_formatted}`);
    if (s.worked_solution) {
      const cleanSol = String(s.worked_solution).trim();
      lines.push(`- **Official Worked Solution:** ${cleanSol}`);
    }
    lines.push(
      `- **Marking Evaluation:** **${s.score} / ${s.max_score}** (${s.is_correct ? '✅ Correct' : '❌ Incorrect / Partial'})${s.misconception_tag ? ` | **Misconception Tag:** \`${s.misconception_tag}\`` : ''}`
    );
    lines.push(``);
  }

  return lines.join('\n').replace(/\{\{,\}\}/g, '{,}');
}

export function writeTopicDossierFile(dossier, rootDir = process.cwd()) {
  const gradeFolder = `Gr${dossier.grade}`;
  const subjectFolder = sanitizePathSegment(dossier.subject);
  const topicSlug = sanitizePathSegment(dossier.topic);
  const personaSlug = sanitizePathSegment(dossier.persona);

  const dirPath = path.join(rootDir, 'playwright-test', gradeFolder, subjectFolder);
  fs.mkdirSync(dirPath, { recursive: true });

  const fileName = `${topicSlug}_${personaSlug}.md`;
  const filePath = path.join(dirPath, fileName);
  const mdContent = renderDossierMarkdown(dossier);
  fs.writeFileSync(filePath, mdContent, 'utf8');
  return filePath;
}
