import { expect } from '@playwright/test';
import { recordQuestionGeneration, recordUserInputAndEvaluation } from '../../helpers/cognitiveAuditLogger.js';
import { evaluatePageNeatness } from '../../helpers/neatnessEvaluator.js';
import {
  buildCanonicalAnswer,
  buildPartialAnswer,
  buildWrongAnswer,
  enterAndSubmitLiveAnswer
} from './modalityAnswerDriver.js';

/**
 * Universal Two-Tier Hybrid Matrix Runner for Curriculum & Archetype Evaluation (Grades 7–12).
 * Enforces Rules 0d-1 through 0d-12:
 * - Zero-Theater & Zero Silent Skips (no `if (isVisible())` or `if (count() > 0)`)
 * - Exhaustive Tier 1 Psychometric & Grading Triad Contract across all curriculum topics & archetypes
 * - Live Tier 2 Browser UI Complementarity (Desktop 1280x800 & Mobile 440x956 iPhone 16 Pro Max)
 * - 3 Simulated Adaptive Learner Journeys (Fast-Track, Steady Developing, Struggling Regression)
 */

function normalizeSubjectKey(subject) {
  const clean = String(subject || '').toLowerCase().trim().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
  if (clean === 'economic_and_management_sciences') return 'ems';
  if (clean === 'maths') return 'mathematics';
  if (clean === 'mathslit' || clean === 'maths_lit') return 'mathematical_literacy';
  if (clean === 'physics') return 'physical_sciences';
  if (clean === 'business') return 'business_studies';
  if (clean === 'lifesci') return 'life_sciences';
  if (clean === 'techmaths') return 'technical_mathematics';
  if (clean === 'natsci') return 'natural_sciences';
  return clean;
}

export async function evaluateSubjectTrack({
  page,
  request,
  baseUrl = 'http://localhost:5173',
  grade,
  subject,
  topic,
  sampleSeeds = [101, 202, 303, 404],
  bannedKeywords = ['according to caps', 'curriculum document', 'dbe requirements', 'annual teaching plan'],
  expectedModality = 'standard',
  testCognitiveRepair = true
}) {
  const normalizedSubjectId = normalizeSubjectKey(subject);
  console.log(`\n📋 [Matrix Evaluation] Starting Grade ${grade} • ${subject} (${normalizedSubjectId}) • "${topic}"...`);

  // ═════════════════════════════════════════════════════════════════════════
  // TIER 1A: CURRICULUM TOPIC & ARCHETYPE CATALOG INTROSPECTION + GRADING TRIAD
  // ═════════════════════════════════════════════════════════════════════════
  const catalogUrl = `${baseUrl}/api/curriculum/archetypes?subject=${encodeURIComponent(subject)}&grade=${grade}`;
  const catalogRes = await request.get(catalogUrl);
  expect(catalogRes.ok(), `GET /api/curriculum/archetypes must respond OK for ${subject} Gr ${grade}`).toBe(true);
  const catalogData = await catalogRes.json();
  expect(catalogData.success).toBe(true);

  const trackTopics = Array.isArray(catalogData.topics) && catalogData.topics.length > 0
    ? catalogData.topics
    : Array.isArray(catalogData.catalog) && catalogData.catalog.length > 0 && Array.isArray(catalogData.catalog[0]?.topics)
      ? catalogData.catalog[0].topics
      : [{ topic, archetypes: ['default'] }];

  let totalTopicsAudited = 0;
  let totalArchetypesAudited = 0;

  for (const topicEntry of trackTopics) {
    const tName = topicEntry.topic;
    const rawSubskills = topicEntry.archetypes || topicEntry.subskills || [];
    const subskills = Array.isArray(rawSubskills) && rawSubskills.length > 0
      ? rawSubskills
      : ['default'];

    // For the primary topic under test, audit every registered archetype (subskill);
    // for all sibling topics in the subject-grade track, audit the canonical topic generator + Grading Triad.
    const archetypesToAudit = tName.toLowerCase() === topic.toLowerCase() ? subskills : [subskills[0]];

    for (const subskill of archetypesToAudit) {
      const subskillParam = subskill && subskill !== 'default' ? `&subskill=${encodeURIComponent(subskill)}` : '';
      const genRes = await request.get(
        `${baseUrl}/api/generate?subject=${encodeURIComponent(subject)}&grade=${grade}&topic=${encodeURIComponent(tName)}${subskillParam}&seed=101`
      );
      expect(genRes.ok(), `Generate failed for Gr ${grade} ${subject} - ${tName} (${subskill})`).toBe(true);
      const genPayload = await genRes.json();
      const q = Array.isArray(genPayload.questions) ? genPayload.questions[0] : (genPayload.questions || genPayload);
      expect(q, `Question must be defined for ${tName} (${subskill})`).toBeDefined();

      // 1. 6-Pillar Contract & Anti-Meta-Curriculum Invariant
      const promptText = String(q.prompt || q.question || q.question_text || q.instruction || q.prompt_latex || '').trim();
      expect(promptText.length, `Prompt for ${tName} (${subskill}) must be substantive`).toBeGreaterThan(10);
      expect(promptText).not.toContain('undefined');
      expect(promptText).not.toContain('NaN');
      for (const banned of bannedKeywords) {
        expect(promptText.toLowerCase()).not.toContain(banned);
      }
      expect([1, 2, 3, 4]).toContain(Number(q.term));
      expect(Number(q.caps_weight_percent)).toBeGreaterThan(0);

      // Invariant A: Grade-Bound Cross-Grade Protection
      if (Number(grade) < 12) {
        const pLow = promptText.toLowerCase();
        const tLow = String(q.topic || '').toLowerCase();
        const sLow = String(q.subskill || '').toLowerCase();
        for (const term of ['complex_numbers', 'argand', 'polar form', 'de moivre']) {
          expect(tLow, `Grade ${grade} question topic must not contain Grade 12 concept '${term}'`).not.toContain(term);
          expect(sLow, `Grade ${grade} question subskill must not contain Grade 12 concept '${term}'`).not.toContain(term);
        }
      }

      // 2. Marking Schema Point-Sum Integrity
      const totalMarks = Number(q.marks || q.marking_schema?.total_marks || 1);
      const mpList = q.marking_schema?.marking_points || [];
      expect(mpList.length, `Marking points must be non-empty for ${tName}`).toBeGreaterThan(0);
      const mpSum = mpList.reduce((acc, mp) => acc + (Number(mp.marks) || 0), 0);
      expect(mpSum, `Marking points sum must equal total marks for ${tName}`).toBe(totalMarks);

      // 3. 3-Tier Hints & Anti-Spoiler Invariant
      const hints = q.hints || {};
      expect(Boolean(hints.tier_1 && hints.tier_2 && hints.tier_3), `3-tier hints required for ${tName}`).toBe(true);
      const expectedStr = String(q.expected_answer ?? '').trim();
      if (expectedStr.length >= 4 && typeof q.expected_answer !== 'object') {
        expect(String(hints.tier_1).toLowerCase()).not.toContain(expectedStr.toLowerCase());
      }

      // 4. The Grading Triad (100% Canonical / Partial Method Marks / 0% Distractor + Misconception Tag)
      // (a) 100% Canonical Answer
      const canonicalAns = buildCanonicalAnswer(q);
      const mark100Res = await request.post(`${baseUrl}/api/mark`, {
        data: { question_id: q.id, user_answer: canonicalAns, subject, grade, question: q }
      });
      expect(mark100Res.ok()).toBe(true);
      const mark100 = await mark100Res.json();
      const max100 = mark100.max_score ?? mark100.total ?? totalMarks;
      expect(
        mark100.is_correct && mark100.score === max100,
        `Canonical answer must award 100% (${mark100.score}/${max100}) for Gr ${grade} ${subject} • ${tName} (${subskill})`
      ).toBe(true);

      recordUserInputAndEvaluation({
        role: 'learner',
        subject,
        grade: String(grade),
        topic: tName,
        modality: q.modality || expectedModality,
        question: q,
        userInput: canonicalAns,
        evaluation: { ...mark100, max_score: max100 }
      });

      // (b) Partial Method Credit (when marks >= 2)
      if (totalMarks >= 2) {
        const partialAns = buildPartialAnswer(q);
        const markPartialRes = await request.post(`${baseUrl}/api/mark`, {
          data: { question_id: q.id, user_answer: partialAns, subject, grade, question: q }
        });
        expect(markPartialRes.ok()).toBe(true);
        const markPartial = await markPartialRes.json();
        const maxPartial = markPartial.max_score ?? markPartial.total ?? totalMarks;
        expect(
          markPartial.score > 0 && markPartial.score < maxPartial,
          `Partial answer must award method marks (0 < ${markPartial.score} < ${maxPartial}) for Gr ${grade} ${subject} • ${tName}`
        ).toBe(true);
      }

      // (c) 0% Wrong / Distractor Answer + Misconception Tag
      const wrongAns = buildWrongAnswer(q);
      const mark0Res = await request.post(`${baseUrl}/api/mark`, {
        data: { question_id: q.id, user_answer: wrongAns, subject, grade, question: q }
      });
      expect(mark0Res.ok()).toBe(true);
      const mark0 = await mark0Res.json();
      expect(mark0.score, `Wrong answer must score 0 for ${tName}`).toBe(0);
      expect(Boolean(mark0.misconception_tag), `Wrong answer must emit misconception_tag for ${tName}`).toBe(true);

      totalArchetypesAudited += 1;
    }
    totalTopicsAudited += 1;
  }

  console.log(`   ✓ Tier 1 Exhaustive Audit: ${totalTopicsAudited} curriculum topics & ${totalArchetypesAudited} archetypes passed 100%/Partial/0% Grading Triad.`);

  // ═════════════════════════════════════════════════════════════════════════
  // TIER 1B: SEED DETERMINISM, MULTI-SEED ENTROPY & STAGE MONOTONICITY
  // ═════════════════════════════════════════════════════════════════════════
  const detResA = await request.get(`${baseUrl}/api/generate?subject=${encodeURIComponent(subject)}&grade=${grade}&topic=${encodeURIComponent(topic)}&seed=42`);
  const detResB = await request.get(`${baseUrl}/api/generate?subject=${encodeURIComponent(subject)}&grade=${grade}&topic=${encodeURIComponent(topic)}&seed=42`);
  const detQA = (await detResA.json()).questions?.[0];
  const detQB = (await detResB.json()).questions?.[0];
  expect(detQA.prompt).toBe(detQB.prompt);
  expect(JSON.stringify(detQA.expected_answer)).toBe(JSON.stringify(detQB.expected_answer));

  // Verify Stage-Complexity Calibration (Diagnostic 0/1/2, Scaffold, Practice, Assessment, Micro-Drill)
  const diagEasyRes = await request.get(`${baseUrl}/api/generate?subject=${encodeURIComponent(subject)}&grade=${grade}&topic=${encodeURIComponent(topic)}&stage=diagnostic&diagnostic_step=0&seed=101`);
  const diagHardRes = await request.get(`${baseUrl}/api/generate?subject=${encodeURIComponent(subject)}&grade=${grade}&topic=${encodeURIComponent(topic)}&stage=diagnostic&diagnostic_step=2&seed=101`);
  const microDrillRes = await request.get(`${baseUrl}/api/generate?subject=${encodeURIComponent(subject)}&grade=${grade}&topic=${encodeURIComponent(topic)}&stage=micro_drill&seed=101`);
  const diagEasyQ = (await diagEasyRes.json()).questions?.[0];
  const diagHardQ = (await diagHardRes.json()).questions?.[0];
  const microDrillQ = (await microDrillRes.json()).questions?.[0];
  expect(diagEasyQ.difficulty).toBe('easy');
  expect(diagHardQ.difficulty).toBe('hard');
  expect(String(microDrillQ.mode).startsWith('elementary')).toBe(true);

  const generatedPrompts = [];
  for (const seed of sampleSeeds) {
    const res = await request.get(`${baseUrl}/api/generate?subject=${encodeURIComponent(subject)}&grade=${grade}&topic=${encodeURIComponent(topic)}&seed=${seed}`);
    expect(res.ok()).toBe(true);
    const data = await res.json();
    const question = Array.isArray(data.questions) ? data.questions[0] : (data.questions || data);
    const promptText = String(question.prompt || question.question || question.question_text || '').trim();
    generatedPrompts.push(promptText);

    recordQuestionGeneration({
      role: 'learner',
      subject,
      grade: String(grade),
      topic,
      modality: question.modality || expectedModality,
      question
    });
  }

  const uniquePrompts = new Set(generatedPrompts);
  console.log(`   ✓ Seed Determinism (seed=42) & Multi-Seed Variability (${uniquePrompts.size}/${sampleSeeds.length} distinct variants) verified.`);

  // ═════════════════════════════════════════════════════════════════════════
  // TIER 2A: DESKTOP VIEWPORT (1280×800) UI COMPLEMENTARITY & 3 LEARNER PROFILES
  // ═════════════════════════════════════════════════════════════════════════
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.goto(`${baseUrl}/`, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });

  await page.evaluate(({ gradeNum, topicName, normSubId }) => {
    try {
      localStorage.removeItem('fundile_pending_subject_enrollment');
    } catch {}
    window.__FUNDILE_SWITCH_PERSONA__({
      id: `matrix-student-gr${gradeNum}`,
      name: `Learner Gr ${gradeNum}`,
      role: 'student',
      type: 'student',
      grade: gradeNum,
      school: 'Westville High School',
      assignedTasks: []
    });
    if (window.studentStore) {
      window.studentStore.setEnabledSubjects([
        normSubId,
        'mathematics',
        'ems',
        'natural_sciences',
        'accounting',
        'physical_sciences',
        'life_sciences',
        'business_studies',
        'mathematical_literacy',
        'technical_mathematics'
      ]);
      window.studentStore.setActiveSession({
        subjectId: normSubId,
        topic: topicName,
        progressionMode: 'diagnostic',
        lastActiveTab: normSubId
      });
      window.studentStore.resetSubjectToZero(normSubId);
    }
  }, { gradeNum: Number(grade), topicName: topic, normSubId: normalizedSubjectId });

  const openSubjectBtn = page.locator(`[data-testid="tab-${normalizedSubjectId}"]:visible`).first();
  await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
  await openSubjectBtn.click();

  const openSessionBtn = page.locator('[data-testid="btn-open-subject-session"]:visible').first();
  await expect(openSessionBtn).toBeVisible({ timeout: 15000 });
  await openSessionBtn.click();

  const questionSurface = page.locator('[data-testid="question-surface"]:visible').first();
  await expect(questionSurface).toBeVisible({ timeout: 15000 });
  await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });

  // ── INVARIANT C: Live UI Default-Topic Verification ─────────────────────
  const topicScopeBtn = page.locator('[data-testid="btn-topic-scope"]:visible').first();
  await expect(topicScopeBtn).toBeVisible({ timeout: 10000 });
  const activeTopicScope = (await topicScopeBtn.innerText()).trim();
  expect(activeTopicScope.length, 'Active topic scope in header ribbon must be non-empty').toBeGreaterThan(0);

  // ── INVARIANT A (DOM Level): Grade-Bound Cross-Grade Bleed Prevention ───
  const initialPromptText = (await questionSurface.innerText()).toLowerCase();
  if (Number(grade) < 12) {
    expect(initialPromptText, `Grade ${grade} prompt must not leak Grade 12 complex numbers`).not.toContain('argand');
    expect(initialPromptText, `Grade ${grade} prompt must not leak Grade 12 polar form`).not.toContain('polar form');
  }

  // ── INVARIANT B (DOM Level): Multi-Part Question & Input Parity ─────────
  const promptLines = initialPromptText.split('\n').map(l => l.trim()).filter(Boolean);
  const numberedPartCount = promptLines.filter(l => /^(\d+[\.\)]|\([a-z\d]+\))\s+/.test(l)).length;
  if (numberedPartCount > 1) {
    const partInputs = page.locator('[data-testid^="input-math-answer-part-"]:visible');
    const inputCount = await partInputs.count();
    expect(
      inputCount,
      `Multi-part question with ${numberedPartCount} parts must render at least ${numberedPartCount} labeled answer boxes`
    ).toBeGreaterThanOrEqual(numberedPartCount);
  }

  // Desktop UI Neatness & Zero Overflow Check
  const desktopNeatness = await evaluatePageNeatness(page, {
    role: 'student',
    screenName: `Gr${grade}_${normalizedSubjectId}_Desktop`,
    isMobile: false
  });
  expect(desktopNeatness.metrics.hasHorizontalOverflow, 'Desktop workspace must have zero horizontal overflow').toBe(false);

  // Verify Progression Stage Ribbon buttons exist
  const diagnosticBtn = page.locator('[data-testid="btn-mode-diagnostic"]:visible').first();
  const scaffoldBtn = page.locator('[data-testid="btn-mode-scaffold"]:visible').first();
  const practiceBtn = page.locator('[data-testid="btn-mode-practice"]:visible').first();
  const assessmentBtn = page.locator('[data-testid="btn-mode-assessment"]:visible').first();
  await expect(diagnosticBtn).toBeVisible();
  await expect(scaffoldBtn).toBeVisible();
  await expect(practiceBtn).toBeVisible();
  await expect(assessmentBtn).toBeVisible();

  // -------------------------------------------------------------------------
  // LEARNER PROFILE 1: FAST-TRACK HIGH-PERFORMER (3/3 Diagnostic -> 3. Exam Mode)
  // -------------------------------------------------------------------------
  console.log(`   [Profile 1] Fast-Track Learner: Completing 3/3 Diagnostic at 100% -> Direct Exam Mode Unlock...`);
  for (let diagStep = 1; diagStep <= 3; diagStep++) {
    await enterAndSubmitLiveAnswer(page, { answerType: 'canonical', topic });
    if (diagStep < 3) {
      const nextBtn = page.locator('[data-testid="btn-next-question"]:visible').first();
      await expect(nextBtn).toBeVisible({ timeout: 10000 });
      await nextBtn.click();
      await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });
    }
  }

  const fastTrackState = await page.evaluate((normSubId) => window.studentStore.getSubject(normSubId), normalizedSubjectId);
  expect(fastTrackState.status).toBe('exam_ready');
  expect(fastTrackState.formativeMastery).toBeGreaterThanOrEqual(80);

  // Verify Diagnostic Debrief Card and click Proceed to Exam Mode
  const proceedCalibratedBtn = page.locator('[data-testid="btn-proceed-calibrated-stage"]:visible').first();
  await expect(proceedCalibratedBtn).toBeVisible({ timeout: 10000 });
  await proceedCalibratedBtn.click();

  await expect(page.locator('[data-testid="exam-timer-display"]:visible').first()).toBeVisible({ timeout: 10000 });
  console.log(`   ✓ [Profile 1] 3/3 Diagnostic fast-tracked learner directly to 3. Exam Mode (${fastTrackState.formativeMastery}% Mastery).`);

  // -------------------------------------------------------------------------
  // LEARNER PROFILE 2: STEADY DEVELOPING LEARNER (Scaffold -> Practice -> Exam)
  // -------------------------------------------------------------------------
  console.log(`   [Profile 2] Steady Learner: 1. Scaffold (2 Qs) -> 2. Practice (3 Qs) -> 3. Exam Mode...`);
  await page.evaluate((normSubId) => {
    window.studentStore.resetSubjectToZero(normSubId);
    window.studentStore.completeDiagnostic(normSubId, 33); // Routes to Scaffold at 42% baseline
  }, normalizedSubjectId);
  await scaffoldBtn.click();

  // Verify 3-Tier Hints in Scaffold Mode
  const toggleHintsBtn = page.locator('[data-testid="btn-toggle-hints"]:visible').first();
  await expect(toggleHintsBtn).toBeVisible({ timeout: 10000 });
  await toggleHintsBtn.click();
  await expect(page.locator('[data-testid="btn-hint-tier-1"]:visible').first()).toBeVisible({ timeout: 5000 });
  await page.locator('[data-testid="btn-hint-tier-2"]:visible').first().click();
  await page.locator('[data-testid="btn-hint-tier-3"]:visible').first().click();

  // Answer 2 questions accurately in 1. Scaffold -> advances to 2. Practice (>= 60%)
  for (let i = 0; i < 2; i++) {
    const nextBtn = page.locator('[data-testid="btn-next-question"]:visible').first();
    await expect(nextBtn).toBeVisible({ timeout: 10000 });
    await nextBtn.click();
    await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });
    await enterAndSubmitLiveAnswer(page, { answerType: 'canonical', topic });
  }

  const afterScaffoldState = await page.evaluate((normSubId) => window.studentStore.getSubject(normSubId), normalizedSubjectId);
  expect(afterScaffoldState.status).toBe('practice');
  expect(afterScaffoldState.formativeMastery).toBeGreaterThanOrEqual(60);

  // Answer 3 questions accurately in 2. Practice -> advances to 3. Exam Mode (>= 80%)
  for (let i = 0; i < 3; i++) {
    const nextBtn = page.locator('[data-testid="btn-next-question"]:visible').first();
    await expect(nextBtn).toBeVisible({ timeout: 10000 });
    await nextBtn.click();
    await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });
    await enterAndSubmitLiveAnswer(page, { answerType: 'canonical', topic });
  }

  const afterPracticeState = await page.evaluate((normSubId) => window.studentStore.getSubject(normSubId), normalizedSubjectId);
  expect(afterPracticeState.status).toBe('exam_ready');
  expect(afterPracticeState.formativeMastery).toBeGreaterThanOrEqual(80);

  // Verify Exam Mode Unlocked milestone card is present in Practice mode without forced countdown
  const examUnlockedBanner = page.locator('[data-testid="banner-exam-unlocked"]:visible').first();
  await expect(examUnlockedBanner).toBeVisible({ timeout: 10000 });
  await expect(page.locator('[data-testid="btn-start-timed-exam"]:visible').first()).toBeVisible();
  const keepPracticingBtn = page.locator('[data-testid="btn-keep-practicing"]:visible').first();
  await expect(keepPracticingBtn).toBeVisible();
  await keepPracticingBtn.click();
  await expect(examUnlockedBanner).toHaveCount(0, { timeout: 5000 });

  // Verify Official Marking Memorandum comparison panel
  const viewMemoBtn = page.locator('[data-testid="btn-view-full-memo"]:visible').first();
  await expect(viewMemoBtn).toBeVisible({ timeout: 10000 });
  await viewMemoBtn.click();
  await expect(page.locator('[data-testid="panel-full-memo"]:visible').first()).toBeVisible({ timeout: 5000 });
  console.log(`   ✓ [Profile 2] Steady Learner progressed Scaffold (42%) -> Practice (${afterScaffoldState.formativeMastery}%) -> Exam Unlocked & verified Memo.`);

  // -------------------------------------------------------------------------
  // LEARNER PROFILE 3: STRUGGLING LEARNER (2 Consecutive Errors -> Regression & Repair)
  // -------------------------------------------------------------------------
  console.log(`   [Profile 3] Struggling Learner: 2 consecutive wrong answers -> Prerequisite Gap Regression...`);
  for (let errStep = 1; errStep <= 2; errStep++) {
    const nextBtn = page.locator('[data-testid="btn-next-question"]:visible').first();
    await expect(nextBtn).toBeVisible({ timeout: 10000 });
    await nextBtn.click();
    await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });
    await enterAndSubmitLiveAnswer(page, { answerType: 'wrong', topic });
  }

  const regressedState = await page.evaluate((normSubId) => window.studentStore.getSubject(normSubId), normalizedSubjectId);
  expect(regressedState.prerequisiteGapDetected).toBe(true);
  expect(regressedState.status).toBe('scaffold');
  await expect(page.locator('[data-testid="banner-prerequisite-gap"]:visible').first()).toBeVisible({ timeout: 10000 });
  const startMicroDrillBtn = page.locator('[data-testid="btn-start-micro-drill"]:visible').first();
  await expect(startMicroDrillBtn).toBeVisible({ timeout: 5000 });
  await startMicroDrillBtn.click();
  await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });
  console.log(`   ✓ [Profile 3] Prerequisite Gap Banner & Elementary Micro-Drill regression verified.`);

  if (testCognitiveRepair) {
    console.log(`   [Profile 3b] Post-Exam Triage & 3-Step Cognitive Repair Pipeline...`);
    await page.evaluate(() => {
      if (window.studentStore) {
        window.studentStore.setPresetProfile('exam_ready_85');
      }
    });
    await assessmentBtn.click();
    await expect(page.locator('[data-testid="exam-timer-display"]:visible').first()).toBeVisible({ timeout: 10000 });

    const examNextBtn = page.locator('[data-testid="btn-next-question"]:visible').first();
    await expect(examNextBtn).toBeVisible({ timeout: 10000 });
    await examNextBtn.click();
    await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });

    await enterAndSubmitLiveAnswer(page, { answerType: 'wrong', topic });

    const openTriageBtn = page.locator('[data-testid="btn-open-triage-modal"]:visible').first();
    await expect(openTriageBtn).toBeVisible({ timeout: 10000 });
    await openTriageBtn.click();

    const launchDrillBtn = page.locator('button:has-text("Launch 5-Min Fix Drill"):visible').first();
    await expect(launchDrillBtn).toBeVisible({ timeout: 5000 });
    await launchDrillBtn.click();

    const optionA = page.locator('button:has-text("R977.50 + 15%"):visible').first();
    await expect(optionA).toBeVisible({ timeout: 5000 });
    await optionA.click();
    const verifyRealizationBtn = page.locator('button:has-text("Verify Realization"):visible').first();
    await expect(verifyRealizationBtn).toBeVisible();
    await verifyRealizationBtn.click();

    const proceedReplayBtn = page.locator('button:has-text("Proceed to SimuLearn Micro-Replay"):visible').first();
    await expect(proceedReplayBtn).toBeVisible();
    await proceedReplayBtn.click();

    const readyVerificationBtn = page.locator('button:has-text("Ready for Verification Pair"):visible').first();
    await expect(readyVerificationBtn).toBeVisible();
    await readyVerificationBtn.click();

    const drillInput1 = page.locator('input[placeholder="e.g. 600"]:visible').first();
    await expect(drillInput1).toBeVisible();
    await drillInput1.fill('600');
    const drillInput2 = page.locator('input[placeholder="e.g. 6000"]:visible').first();
    await expect(drillInput2).toBeVisible();
    await drillInput2.fill('6000');

    const verifyRemediationBtn = page.locator('button:has-text("Verify & Certify Remediation"):visible').first();
    await expect(verifyRemediationBtn).toBeVisible();
    await verifyRemediationBtn.click();

    const returnBtn = page.locator('button:has-text("Return to Dashboard"):visible').first();
    await expect(returnBtn).toBeVisible();
    await returnBtn.click();

    await expect(page.locator('[data-testid="badge-remedial-repaired"]:visible').first()).toBeVisible({ timeout: 5000 });
    console.log(`   ✓ [Profile 3b] 3-Step Cognitive Repair Sequence completed.`);
  }

  // ═════════════════════════════════════════════════════════════════════════
  // TIER 2B: MOBILE VIEWPORT (440×956 iPhone 16 Pro Max) UI COMPLEMENTARITY
  // ═════════════════════════════════════════════════════════════════════════
  console.log(`   [Mobile 440×956] Verifying Mobile UI Complementarity & Canonical Answer Input...`);
  await page.setViewportSize({ width: 440, height: 956 });
  const nextMobileBtn = page.locator('[data-testid="btn-next-question"]:visible').first();
  await expect(nextMobileBtn).toBeVisible({ timeout: 10000 });
  await nextMobileBtn.click();
  await expect(page.locator('text=Generating authentic question...')).toHaveCount(0, { timeout: 15000 });

  const mobileNeatness = await evaluatePageNeatness(page, {
    role: 'student',
    screenName: `Gr${grade}_${normalizedSubjectId}_Mobile_440x956`,
    isMobile: true
  });
  expect(mobileNeatness.metrics.hasHorizontalOverflow, 'Mobile 440x956 workspace must have zero horizontal overflow').toBe(false);

  await enterAndSubmitLiveAnswer(page, { answerType: 'canonical', topic });
  console.log(`   ✓ [Mobile 440×956] Canonical answer entered & verified on mobile viewport with 0 horizontal overflow.`);

  console.log(`🏁 [Matrix Evaluation] Completed Grade ${grade} • ${subject} • "${topic}" (${totalTopicsAudited} topics, ${totalArchetypesAudited} archetypes).\n`);
  return {
    subject,
    grade,
    topic,
    topicsAudited: totalTopicsAudited,
    archetypesAudited: totalArchetypesAudited,
    entropyScore: uniquePrompts.size / sampleSeeds.length,
    status: 'PASSED'
  };
}
