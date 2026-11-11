import { test, expect } from '@playwright/test';
import {
  injectGlidingCursorAndHud,
  updateHud,
  glideCursorTo,
  pauseAwareDwell,
} from '../helpers/autopilotHud.js';

/**
 * Milestone 2 Human Organ Systems Adaptive Progression Suite (Heart Standard Compliant).
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater testing. Real user actions, live DOM assertions, genuine post-verification logs.
 * - Rule 0d-4: Grounded in live JSX components (AlveolusGasExchangeSvg, HumanDigestiveSvg,
 *              IntestinalVillusSvg, HumanNephronSvg, BioDiagramModalityRenderer).
 * - Rule 0d-6: Explicit assertions, zero silent skips.
 * - Rule 0d-7: Live runtime execution & non-intrusive margins for HUD instrumentation.
 * - Rule 0d-14: Heart Diagram Standard (Unlabeled Textbook Master + NSC Exam Stipple plates,
 *               zero hand-coded SVG clipart, transparent SVG overlay, calibrated pin leader lines).
 * - Rule 2b: Universal curriculum alignment language; zero "CAPS" acronym in UI assertions.
 *
 * Individual Diagram Headed Execution:
 * To inspect a single diagram on demand:
 *   npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "alveolus_gas_exchange"
 *   npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "digestive_system"
 *   npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "intestinal_villus"
 *   npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "human_nephron"
 *   npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "reference_atlas"
 */

const TARGET_BASE_URL = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';
const BACKEND_BASE_URL = process.env.BACKEND_BASE_URL || 'http://127.0.0.1:5001';

const MILESTONE2_ARCHETYPES = [
  {
    master: 'alveolus_gas_exchange',
    title: 'Alveolus & Pulmonary Capillary Gas Exchange',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Gaseous exchange',
    subskill: 'alveolus_gas_exchange_anatomy',
    badge: 'alveolus-locked-view-badge',
    canvas: 'alveolus-gas-exchange-canvas',
    root: 'alveolus-root',
    expectedText: 'Pulmonary Alveolus & Capillary Diffusion Cross-Section',
    seed: 42,
  },
  {
    master: 'digestive_system',
    title: 'Human Alimentary Canal & Digestive System',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Animal Nutrition',
    subskill: 'villus_and_macroscopic_anatomy',
    badge: 'digestive-locked-view-badge',
    canvas: 'human-digestive-canvas',
    root: 'digestive-root',
    expectedText: 'Human Digestive System & Alimentary Canal',
    seed: 42,
  },
  {
    master: 'intestinal_villus',
    title: 'Intestinal Villus Histology & Absorption',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Animal Nutrition',
    subskill: 'villus',
    badge: 'villus-locked-view-badge',
    canvas: 'intestinal-villus-canvas',
    root: 'villus-root',
    expectedText: 'Intestinal Villus Longitudinal Cross-Section (Ileum)',
    seed: 42,
  },
  {
    master: 'human_nephron',
    title: 'Renal Nephron Ultrastructure & Filtration System',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Excretion in humans',
    subskill: 'nephron_microstructure_anatomy',
    badge: 'nephron-locked-view-badge',
    canvas: 'human-nephron-canvas',
    root: 'nephron-root',
    expectedText: 'Renal Nephron Ultrastructure & Filtration System',
    seed: 42,
  },
];

async function setupPageForInspection(page) {
  test.setTimeout(0); // Unlimited timeout for on-demand live human inspection & spacebar pausing
  await page.setViewportSize({ width: 1280, height: 850 });
  await page.goto(`${TARGET_BASE_URL}/`, { waitUntil: 'domcontentloaded' });

  // Await persona switcher function on window
  await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });

  // Enable complete science suite in student store
  await page.evaluate(() => {
    if (window.studentStore) {
      const subjects = ['natural_sciences', 'life_sciences', 'physical_sciences', 'mathematics'];
      window.studentStore.setEnabledSubjects(subjects);
      subjects.forEach((s) => window.studentStore.completeDiagnostic(s, 65));
    }
  });

  await injectGlidingCursorAndHud(page);
}

async function verifyDiagramArchetype(page, arch) {
  let currentDiagramQuestion = null;
  await page.route('**/api/generate*', async (route) => {
    if (currentDiagramQuestion) {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          success: true,
          questions: [currentDiagramQuestion],
          metadata: { subject: currentDiagramQuestion.subject || 'science' }
        })
      });
    } else {
      await route.continue();
    }
  });

  const hudMsg = `[Inspection] Grade ${arch.grade} Life Sciences • ${arch.title}`;
  await updateHud(page, 'LEARNER', hudMsg);

  // 1. Fetch genuine question from the backend generator
  const genUrl = `${BACKEND_BASE_URL}/api/generate?subject=${encodeURIComponent(arch.subject)}&grade=${arch.grade}&topic=${encodeURIComponent(arch.topic)}&subskill=${encodeURIComponent(arch.subskill)}&seed=${arch.seed}`;
  const response = await page.request.get(genUrl);
  expect(response.ok()).toBeTruthy();

  const json = await response.json();
  const rawQ = Array.isArray(json.questions) && json.questions.length > 0 ? json.questions[0] : json.questions;
  expect(rawQ).toBeTruthy();
  currentDiagramQuestion = rawQ;

  // 2. Switch persona
  await page.evaluate(({ grade }) => {
    window.__FUNDILE_SWITCH_PERSONA__({
      id: `sch-gr${String(grade).padStart(2, '0')}-01`,
      name: 'Nkosana Dlamini',
      role: 'student',
      type: 'student',
      grade: grade,
      school: 'Westville High School',
      assignedTasks: []
    });
    if (window.studentStore) {
      window.studentStore.setEnabledSubjects(['natural_sciences', 'life_sciences']);
      ['natural_sciences', 'life_sciences'].forEach((s) => window.studentStore.completeDiagnostic(s, 65));
    }
  }, { grade: arch.grade });

  // 3. Switch tab
  await page.evaluate(({ tab }) => {
    if (typeof window.__FUNDILE_SELECT_TAB__ === 'function') {
      window.__FUNDILE_SELECT_TAB__(tab);
    }
  }, { tab: arch.subjectTab });

  // 4. Load question into Universal Workspace
  await page.evaluate(({ q, topic }) => {
    if (typeof window.__FUNDILE_LOAD_QUESTION__ === 'function') {
      window.__FUNDILE_LOAD_QUESTION__(q, topic);
    }
  }, { q: rawQ, topic: arch.topic });

  // 5. Assert Bio Diagram Canvas card is mounted
  const bioCanvas = page.locator('[data-testid="bio-diagram-canvas"]:visible').first();
  await expect(bioCanvas).toBeVisible({ timeout: 15000 });

  // 6. Assert Root container and specific canvas
  const rootElem = page.locator(`[data-testid="${arch.root}"]:visible`).first();
  await expect(rootElem).toBeVisible({ timeout: 10000 });

  const specificCanvas = page.locator(`[data-testid="${arch.canvas}"]:visible`).first();
  await expect(specificCanvas).toBeVisible({ timeout: 10000 });

  // 7. Assert Single Locked View Badge (Heart standard Rule 0d-14.2)
  const lockedBadge = page.locator(`[data-testid="${arch.badge}"]:visible`).first();
  await expect(lockedBadge).toBeVisible({ timeout: 10000 });
  await expect(lockedBadge).toContainText(arch.expectedText);

  // 8. Assert Anti-Leak Contract: Structure answer names must NOT be leaked into DOM text nodes
  const svgTextList = await specificCanvas.locator('text').allInnerTexts();
  const rawAns = String(rawQ.correct_answer || '').trim().toLowerCase();
  if (rawAns.length > 3) {
    const leaked = svgTextList.some(
      (t) => typeof t === 'string' && t.trim().toLowerCase() === rawAns && !['a', 'b', 'c', 'd'].includes(t.trim().toLowerCase())
    );
    expect(leaked).toBeFalsy();
  }

  // 9. Interactive Pin Movement: Glide cursor to Pin A and click it
  const pinBtnA = page.locator('[data-testid="btn-select-pin-A"]:visible').first();
  await expect(pinBtnA).toBeVisible({ timeout: 10000 });
  await glideCursorTo(page, pinBtnA);
  await pinBtnA.click();

  // 10. Assert Pin Selection Callout reflects selected target without leaking
  const pinDetail = page.locator('[data-testid="bio-pin-detail"]:visible').first();
  await expect(pinDetail).toBeVisible({ timeout: 10000 });
  await expect(pinDetail).toContainText('Active target pin selected for response');

  // 11. Test Adaptive Scaffold: Click hints toggle and inspect Tier 1 hint
  const hintToggleBtn = page.locator('[data-testid="btn-toggle-hints"]:visible').first();
  await expect(hintToggleBtn).toBeVisible({ timeout: 10000 });
  await glideCursorTo(page, hintToggleBtn);
  await hintToggleBtn.click();

  const hintTier1 = page.locator('[data-testid="btn-hint-tier-1"]:visible').first();
  await expect(hintTier1).toBeVisible({ timeout: 10000 });
  await glideCursorTo(page, hintTier1);
  await hintTier1.click();

  // 12. Test Option Selection in Practice Mode (MCQ answer options)
  const firstOption = page.locator('[data-testid="btn-math-option-0"]:visible').first();
  await expect(firstOption).toBeVisible({ timeout: 10000 });
  await glideCursorTo(page, firstOption);
  await firstOption.click();

  // 13. Dwell smoothly for visual human inspection (press Spacebar to pause anytime)
  await pauseAwareDwell(page, 2000);
  console.log(`[PASS] Successfully verified Milestone 2 diagram: ${arch.master}`);
}

test.describe('Milestone 2 Human Organ Systems Adaptive Progression Suite', () => {
  for (const arch of MILESTONE2_ARCHETYPES) {
    test(`Diagram: ${arch.master} - ${arch.title}`, async ({ page }) => {
      await setupPageForInspection(page);
      await verifyDiagramArchetype(page, arch);
    });
  }

  test('Reference Atlas: reference_atlas - Multi-View Exploration (Textbook vs Exam Paper)', async ({ page }) => {
    await setupPageForInspection(page);

    await updateHud(page, 'LEARNER', 'Reference Atlas: Multi-View Exploration (Textbook vs Exam Paper)');

    const atlasQ = {
      id: 'alveolus_atlas_demo',
      subject: 'life_sciences',
      grade: 11,
      topic: 'Gaseous exchange',
      modality: 'bio_diagram',
      question_type: 'mcq',
      question: 'Reference Atlas Mode: Compare the Textbook Master plate with the NSC Exam Paper line-art plate.',
      correct_answer: 'Alveolar squamous epithelium',
      options: ['Alveolar squamous epithelium', 'Red blood cell', 'Capillary endothelium', 'Air lumen'],
      hints: ['Observe the fine stipple shading on the exam paper plate.'],
      diagram_spec: {
        image_type: 'alveolus_gas_exchange',
        allowViewSwitch: true,
        viewBox: '0 0 600 480',
        grade_mask: 'g11',
        pins: [
          { pin: 'A', anchor: [290, 240], default_box: [60, 240], side: 'left', ref: 'ref_1' },
          { pin: 'B', anchor: [240, 190], default_box: [60, 160], side: 'left', ref: 'ref_2' },
          { pin: 'C', anchor: [435, 275], default_box: [540, 275], side: 'right', ref: 'ref_3' },
          { pin: 'D', anchor: [420, 220], default_box: [540, 200], side: 'right', ref: 'ref_4' }
        ]
      }
    };

    await page.route('**/api/generate*', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          success: true,
          questions: [atlasQ],
          metadata: { subject: 'life_sciences' }
        })
      });
    });

    await page.evaluate(({ q }) => {
      if (typeof window.__FUNDILE_LOAD_QUESTION__ === 'function') {
        window.__FUNDILE_LOAD_QUESTION__(q, 'Gaseous exchange');
      }
    }, { q: atlasQ });

    const btnViewExam = page.locator('[data-testid="btn-view-exam"]:visible').first();
    await expect(btnViewExam).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, btnViewExam);
    await btnViewExam.click();

    // Verify exam stipple plate is rendered
    const examImage = page.locator('#view_exam_paper image:visible').first();
    await expect(examImage).toBeVisible({ timeout: 5000 });
    await pauseAwareDwell(page, 2000);

    // Switch back to textbook master
    const btnViewTextbook = page.locator('[data-testid="btn-view-textbook"]:visible').first();
    await expect(btnViewTextbook).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, btnViewTextbook);
    await btnViewTextbook.click();

    const textbookImage = page.locator('#view_textbook_master image:visible').first();
    await expect(textbookImage).toBeVisible({ timeout: 5000 });
    await pauseAwareDwell(page, 2000);

    await updateHud(page, 'COMPLETED', 'Milestone 2 Human Organs Standard Fully Verified!');
    console.log('\n[COMPLETED] Milestone 2 Reference Atlas Multi-View Completed Successfully.\n');
    await pauseAwareDwell(page, 2500);
  });

  test('Dual-Mode Alive Simulation: Bring It To Life, Capillary Flow, RBC Tracking & Macroscopic Zoom', async ({ page }) => {
    await setupPageForInspection(page);
    await updateHud(page, 'LEARNER', 'Phase 4 Pilot: Alveolus Dual Static/Alive Dynamic Simulation');

    const pilotQ = {
      id: 'alveolus_alive_pilot_demo',
      subject: 'life_sciences',
      grade: 11,
      topic: 'Gaseous exchange',
      modality: 'bio_diagram',
      question_type: 'mcq',
      question: 'Examine the pulmonary alveolus diffusion interface. Click "Bring It To Life" to inspect active gas exchange and red blood cell oxygenation.',
      correct_answer: 'Alveolar squamous epithelium',
      options: ['Alveolar squamous epithelium', 'Red blood cell', 'Capillary endothelium', 'Air lumen'],
      hints: ['Click Bring It To Life to observe erythrocytes flowing along the pulmonary capillary.'],
      diagram_spec: {
        image_type: 'alveolus_gas_exchange',
        allowViewSwitch: true,
        viewBox: '0 0 600 480',
        grade_mask: 'g11',
        pins: [
          { pin: 'A', anchor: [290, 240], default_box: [60, 240], side: 'left', ref: 'ref_1' },
          { pin: 'B', anchor: [240, 190], default_box: [60, 160], side: 'left', ref: 'ref_2' },
          { pin: 'C', anchor: [435, 275], default_box: [540, 275], side: 'right', ref: 'ref_3' },
          { pin: 'D', anchor: [420, 220], default_box: [540, 200], side: 'right', ref: 'ref_4' }
        ]
      }
    };

    await page.route('**/api/generate*', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          success: true,
          questions: [pilotQ],
          metadata: { subject: 'life_sciences' }
        })
      });
    });

    // Switch persona to Grade 11 student
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'sch-gr11-01',
        name: 'Nkosana Dlamini',
        role: 'student',
        type: 'student',
        grade: 11,
        school: 'Westville High School',
        assignedTasks: []
      });
      if (window.studentStore) {
        window.studentStore.setEnabledSubjects(['natural_sciences', 'life_sciences']);
        ['natural_sciences', 'life_sciences'].forEach((s) => window.studentStore.completeDiagnostic(s, 65));
      }
    });

    // Select Life Sciences Tab
    await page.evaluate(() => {
      if (typeof window.__FUNDILE_SELECT_TAB__ === 'function') {
        window.__FUNDILE_SELECT_TAB__('life_sciences');
      }
    });

    await page.evaluate(({ q }) => {
      if (typeof window.__FUNDILE_LOAD_QUESTION__ === 'function') {
        window.__FUNDILE_LOAD_QUESTION__(q, 'Gaseous exchange');
      }
    }, { q: pilotQ });

    // Wait for bio diagram canvas
    const bioCanvas = page.locator('[data-testid="bio-diagram-canvas"]:visible').first();
    await expect(bioCanvas).toBeVisible({ timeout: 15000 });

    // 1. Confirm Static Mode with Bring It To Life Button
    const bringToLifeBtn = page.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(bringToLifeBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, bringToLifeBtn);
    await bringToLifeBtn.click();

    // 2. Assert Alive Simulation Stage & Controls Mounted
    const aliveControls = page.locator('[data-testid="alveolus-alive-controls"]:visible').first();
    await expect(aliveControls).toBeVisible({ timeout: 10000 });

    const aliveStage = page.locator('[data-testid="alveolus-alive-stage"]:visible').first();
    await expect(aliveStage).toBeVisible({ timeout: 10000 });

    // 3. Assert Erythrocytes & Diffusion Particle Swarms
    const rbcStream = page.locator('#erythrocytes_capillary_stream');
    await expect(rbcStream).toBeAttached({ timeout: 5000 });

    const o2Swarm = page.locator('#o2_diffusion_swarm');
    await expect(o2Swarm).toBeAttached({ timeout: 5000 });

    const co2Swarm = page.locator('#co2_diffusion_swarm');
    await expect(co2Swarm).toBeAttached({ timeout: 5000 });

    await pauseAwareDwell(page, 1500);

    // 4. Toggle Follow-RBC Mode
    const followRbcBtn = page.locator('[data-testid="btn-follow-rbc"]:visible').first();
    await expect(followRbcBtn).toBeVisible({ timeout: 5000 });
    await glideCursorTo(page, followRbcBtn);
    await followRbcBtn.click();
    await pauseAwareDwell(page, 1500);

    // 5. Toggle Speed to 2x
    const speedBtn = page.locator('[data-testid="btn-speed-toggle"]:visible').first();
    await expect(speedBtn).toBeVisible({ timeout: 5000 });
    await glideCursorTo(page, speedBtn);
    await speedBtn.click();
    await pauseAwareDwell(page, 1000);

    // 6. Step to Phase 3 (Passive Gas Diffusion)
    const phase3Btn = page.locator('[data-testid="btn-phase-diffusion"]:visible').first();
    await expect(phase3Btn).toBeVisible({ timeout: 5000 });
    await glideCursorTo(page, phase3Btn);
    await phase3Btn.click();
    await pauseAwareDwell(page, 1500);

    // 7. Toggle Macroscopic Cardiopulmonary View
    const macroBtn = page.locator('[data-testid="btn-zoom-macro"]:visible').first();
    await expect(macroBtn).toBeVisible({ timeout: 5000 });
    await glideCursorTo(page, macroBtn);
    await macroBtn.click();

    const macroLoop = page.locator('#macroscopic_cardiopulmonary_loop');
    await expect(macroLoop).toBeVisible({ timeout: 5000 });
    await pauseAwareDwell(page, 1500);

    // Zoom back in to microscopic alveolus
    await glideCursorTo(page, macroBtn);
    await macroBtn.click();
    await expect(rbcStream).toBeAttached({ timeout: 5000 });

    // 8. Return cleanly to Static Exam Plate
    const backToExamBtn = page.locator('[data-testid="btn-back-to-exam"]:visible').first();
    await expect(backToExamBtn).toBeVisible({ timeout: 5000 });
    await glideCursorTo(page, backToExamBtn);
    await backToExamBtn.click();

    // Verify static callout pins and Bring It To Life button are restored
    await expect(bringToLifeBtn).toBeVisible({ timeout: 5000 });
    await pauseAwareDwell(page, 1500);

    await updateHud(page, 'COMPLETED', 'Dual-Mode Alive Simulation Pilot Successfully Verified!');
    console.log('\n[COMPLETED] Alveolus Dual Static/Alive Dynamic Simulation Pilot Passed.\n');
  });
});
