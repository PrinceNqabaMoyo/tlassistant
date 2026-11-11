import { test, expect } from '@playwright/test';
import {
  injectGlidingCursorAndHud,
  updateHud,
  glideCursorTo,
  pauseAwareDwell,
} from '../helpers/autopilotHud.js';

/**
 * Phase 4 Dual-Mode Static ↔ Alive Visualizations & SimuLearn Integration Suite
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater testing. Real user actions, live DOM assertions, genuine post-verification logs.
 * - Rule 0d-4: Grounded in live JSX components (ParticleModelSvg.jsx, GeyserHeatingElementSvg.jsx,
 *              OpticalTelescopesSvg.jsx, BioDiagramModalityRenderer.jsx).
 * - Rule 0d-6: Explicit assertions, zero silent skips.
 * - Rule 0d-7: Live runtime execution & non-intrusive margins for HUD instrumentation.
 * - Rule 0d-9: Responsive visibility & CSS union invariant (:visible).
 * - Rule 0d-14: Heart Diagram Standard (Unlabeled Textbook Master + NSC Exam Stipple plates,
 *               zero hand-coded SVG clipart, transparent SVG overlay, calibrated pin leader lines).
 * - Rule 2b: Universal curriculum alignment language; zero "CAPS" acronym in UI assertions.
 */

const TARGET_BASE_URL = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';

const DUAL_MODE_QUESTIONS = [
  {
    master: 'particle_model',
    title: 'Particle Model of Matter (Solid, Liquid, Gas)',
    subject: 'natural_sciences',
    grade: 8,
    topic: 'Particle model of matter',
    badge: 'particle-model-locked-view-badge',
    canvas: 'particle-model-canvas',
    root: 'particle-model-root',
    expectedText: 'Particle Model of Matter Master',
    simContainer: 'alive-kinetic-simulation',
    question: {
      id: 'q_ns8_particle_model_dual',
      question_type: 'diagram',
      modality: 'diagram',
      prompt: 'Study the particle model diagram below representing matter across different physical states.',
      marks: 5,
      diagram_spec: {
        type: 'particle_model',
        master: 'particle_model',
        image_type: 'particle_model',
        view: 'textbook',
        state: 'static',
        labels: [
          { id: 'A', name: 'Solid Phase' },
          { id: 'B', name: 'Liquid Phase' },
          { id: 'C', name: 'Gas Phase' }
        ],
        pins: [
          { pin: 'A', target_x: 100, target_y: 200 },
          { pin: 'B', target_x: 300, target_y: 200 },
          { pin: 'C', target_x: 500, target_y: 200 }
        ]
      },
      options: ['Solid crystalline lattice', 'Liquid sliding particles', 'Rapid gas particles', 'Ionised plasma'],
      correct_index: 0,
      correct_answer: 'Solid crystalline lattice'
    }
  },
  {
    master: 'geyser_heating_element',
    title: 'Domestic Geyser Electrical Heating Element',
    subject: 'natural_sciences',
    grade: 8,
    topic: 'Energy transfer in electrical systems',
    badge: 'geyser-locked-view-badge',
    canvas: 'geyser-canvas',
    root: 'geyser-root',
    expectedText: 'Domestic Water Heater Tank & Heating Element Master',
    simContainer: 'alive-geyser-simulation',
    question: {
      id: 'q_ns8_geyser_dual',
      question_type: 'diagram',
      modality: 'diagram',
      prompt: 'Examine the domestic geyser electrical heating element and thermostat assembly.',
      marks: 5,
      diagram_spec: {
        type: 'geyser_heating_element',
        master: 'geyser_heating_element',
        image_type: 'geyser_heating_element',
        view: 'textbook',
        state: 'static',
        labels: [
          { id: 'A', name: 'Coiled Heating Element' },
          { id: 'B', name: 'Thermostat Sensor Probe' },
          { id: 'C', name: 'Cold Water Inlet' }
        ],
        pins: [
          { pin: 'A', target_x: 300, target_y: 250 },
          { pin: 'B', target_x: 300, target_y: 150 },
          { pin: 'C', target_x: 100, target_y: 400 }
        ]
      },
      options: ['Coiled resistance heating element', 'Thermostat bimetallic probe', 'Cold water inlet pipe', 'Sacrificial anode rod'],
      correct_index: 0,
      correct_answer: 'Coiled resistance heating element'
    }
  },
  {
    master: 'optical_telescopes',
    title: 'Astronomical Optical Telescopes (SALT Reflector vs Refractor)',
    subject: 'natural_sciences',
    grade: 8,
    topic: 'Looking into space',
    badge: 'telescopes-locked-view-badge',
    canvas: 'telescopes-canvas',
    root: 'telescopes-root',
    expectedText: 'Astronomical Optical Telescopes Master',
    simContainer: 'alive-optical-simulation',
    question: {
      id: 'q_ns8_telescopes_dual',
      question_type: 'diagram',
      modality: 'diagram',
      prompt: 'Compare the optical ray paths in astronomical reflecting and refracting telescopes.',
      marks: 5,
      diagram_spec: {
        type: 'optical_telescopes',
        master: 'optical_telescopes',
        image_type: 'optical_telescopes',
        view: 'textbook',
        state: 'static',
        labels: [
          { id: 'A', name: 'Primary Mirror' },
          { id: 'B', name: 'Secondary Mirror' },
          { id: 'C', name: 'Objective Lens' }
        ],
        pins: [
          { pin: 'A', target_x: 120, target_y: 200 },
          { pin: 'B', target_x: 450, target_y: 200 },
          { pin: 'C', target_x: 150, target_y: 400 }
        ]
      },
      options: ['Concave primary mirror', 'Flat secondary mirror', 'Convex objective lens', 'Eyepiece lens'],
      correct_index: 0,
      correct_answer: 'Concave primary mirror'
    }
  },
];

async function setupHarnessPage(page) {
  test.setTimeout(90000);
  await page.setViewportSize({ width: 1280, height: 850 });
  await page.goto(`${TARGET_BASE_URL}/?harness=universal_workspace`, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof window.__SET_WORKSPACE_QUESTION__ === 'function', { timeout: 15000 });
  await injectGlidingCursorAndHud(page);
}

test.describe('Milestone Phase 4 Dual-Mode Visuals & SimuLearn Suite', () => {

  test('1. Verify Particle Model of Matter Dual-Mode Static ↔ Alive & Heating Curve Zoom', async ({ page }) => {
    await setupHarnessPage(page);
    const item = DUAL_MODE_QUESTIONS[0];

    const hudMsg = `[Dual-Mode] Grade ${item.grade} Natural Sciences • ${item.title}`;
    await updateHud(page, 'LEARNER', hudMsg);

    // Set question into harness
    await page.evaluate(({ q, meta }) => {
      window.__SET_WORKSPACE_QUESTION__(q, meta);
    }, { q: item.question, meta: { grade: item.grade, subject: item.subject, topic: item.topic } });

    // Step A: Assert Static Exam Mode Canvas & Locked View Badge
    const canvas = page.locator(`[data-testid="${item.canvas}"]:visible`).first();
    await expect(canvas).toBeVisible({ timeout: 15000 });

    const lockedBadge = page.locator(`[data-testid="${item.badge}"]:visible`).first();
    await expect(lockedBadge).toBeVisible({ timeout: 10000 });
    await expect(lockedBadge).toContainText(item.expectedText);

    // Step B: Switch to Alive Mode
    const bringToLifeBtn = page.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(bringToLifeBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, bringToLifeBtn);
    await bringToLifeBtn.click();

    // Step C: Verify Alive Simulation Container & Scientific HUD
    const simElem = page.locator(`[data-testid="${item.simContainer}"]:visible`).first();
    await expect(simElem).toBeVisible({ timeout: 10000 });
    await page.screenshot({ path: `C:/Users/princ/.gemini/antigravity/brain/f0985f12-5686-4fbe-a862-be3e4709f90c/${item.master}_alive.png` });

    await expect(simElem).toContainText('AVG KINETIC ENERGY');
    await expect(simElem).toContainText('TEMPERATURE (T)');

    // Step D: Test Phase Steppers
    const meltBtn = page.locator('[data-testid="btn-phase-melting"]:visible').first();
    await expect(meltBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, meltBtn);
    await meltBtn.click();
    await pauseAwareDwell(page, 500);

    const gasBtn = page.locator('[data-testid="btn-phase-gas"]:visible').first();
    await expect(gasBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, gasBtn);
    await gasBtn.click();
    await pauseAwareDwell(page, 500);

    // Step E: Test Particle Tracking Toggle
    const followBtn = page.locator('[data-testid="btn-follow-particle"]:visible').first();
    await expect(followBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, followBtn);
    await followBtn.click();
    await pauseAwareDwell(page, 500);

    // Step F: Test Macroscopic Heating Curve Zoom Modal
    const zoomBtn = page.locator('[data-testid="btn-zoom-heating-curve"]:visible').first();
    await expect(zoomBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, zoomBtn);
    await zoomBtn.click();

    const modal = page.locator('[data-testid="modal-heating-curve"]:visible').first();
    await expect(modal).toBeVisible({ timeout: 10000 });
    await expect(modal).toContainText('Heating Curve of Water');

    const closeModalBtn = page.locator('[data-testid="btn-close-heating-curve"]:visible').first();
    await expect(closeModalBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, closeModalBtn);
    await closeModalBtn.click();
    await expect(modal).not.toBeVisible();

    // Step G: Return to Exam Mode
    const backToExamBtn = page.locator('[data-testid="btn-back-to-exam"]:visible').first();
    await expect(backToExamBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, backToExamBtn);
    await backToExamBtn.click();

    await expect(canvas).toBeVisible({ timeout: 10000 });
    console.log('[✓] Particle Model of Matter Dual-Mode Verified');
  });

  test('2. Verify Domestic Geyser Heating Element Dual-Mode Static ↔ Alive & Thermostat Trip', async ({ page }) => {
    await setupHarnessPage(page);
    const item = DUAL_MODE_QUESTIONS[1];

    const hudMsg = `[Dual-Mode] Grade ${item.grade} Natural Sciences • ${item.title}`;
    await updateHud(page, 'LEARNER', hudMsg);

    // Set question into harness
    await page.evaluate(({ q, meta }) => {
      window.__SET_WORKSPACE_QUESTION__(q, meta);
    }, { q: item.question, meta: { grade: item.grade, subject: item.subject, topic: item.topic } });

    // Step A: Assert Static Exam Mode Canvas & Locked View Badge
    const canvas = page.locator(`[data-testid="${item.canvas}"]:visible`).first();
    await expect(canvas).toBeVisible({ timeout: 15000 });

    const lockedBadge = page.locator(`[data-testid="${item.badge}"]:visible`).first();
    await expect(lockedBadge).toBeVisible({ timeout: 10000 });
    await expect(lockedBadge).toContainText(item.expectedText);

    // Step B: Switch to Alive Mode
    const bringToLifeBtn = page.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(bringToLifeBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, bringToLifeBtn);
    await bringToLifeBtn.click();

    // Step C: Verify Alive Simulation Container & Scientific HUD
    const simElem = page.locator(`[data-testid="${item.simContainer}"]:visible`).first();
    await expect(simElem).toBeVisible({ timeout: 10000 });
    await page.screenshot({ path: `C:/Users/princ/.gemini/antigravity/brain/f0985f12-5686-4fbe-a862-be3e4709f90c/${item.master}_alive.png` });

    await expect(simElem).toContainText('JOULE POWER');
    await expect(simElem).toContainText('WATER TEMP (T)');

    // Step D: Test Thermostat Trip
    const tripBtn = page.locator('[data-testid="btn-trip-thermostat"]:visible').first();
    await expect(tripBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, tripBtn);
    await tripBtn.click();
    await pauseAwareDwell(page, 500);

    await expect(simElem).toContainText('CUT-OFF TRIP');

    // Reset trip
    await tripBtn.click();
    await pauseAwareDwell(page, 500);

    // Step E: Return to Exam Mode
    const backToExamBtn = page.locator('[data-testid="btn-back-to-exam"]:visible').first();
    await expect(backToExamBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, backToExamBtn);
    await backToExamBtn.click();

    await expect(canvas).toBeVisible({ timeout: 10000 });
    console.log('[✓] Domestic Geyser Heating Element Dual-Mode Verified');
  });

  test('3. Verify Astronomical Optical Telescopes Dual-Mode Static ↔ Alive & Dispersion Toggle', async ({ page }) => {
    await setupHarnessPage(page);
    const item = DUAL_MODE_QUESTIONS[2];

    const hudMsg = `[Dual-Mode] Grade ${item.grade} Natural Sciences • ${item.title}`;
    await updateHud(page, 'LEARNER', hudMsg);

    // Set question into harness
    await page.evaluate(({ q, meta }) => {
      window.__SET_WORKSPACE_QUESTION__(q, meta);
    }, { q: item.question, meta: { grade: item.grade, subject: item.subject, topic: item.topic } });

    // Step A: Assert Static Exam Mode Canvas & Locked View Badge
    const canvas = page.locator(`[data-testid="${item.canvas}"]:visible`).first();
    await expect(canvas).toBeVisible({ timeout: 15000 });

    const lockedBadge = page.locator(`[data-testid="${item.badge}"]:visible`).first();
    await expect(lockedBadge).toBeVisible({ timeout: 10000 });
    await expect(lockedBadge).toContainText(item.expectedText);

    // Step B: Switch to Alive Mode
    const bringToLifeBtn = page.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(bringToLifeBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, bringToLifeBtn);
    await bringToLifeBtn.click();

    // Step C: Verify Alive Simulation Container & Scientific HUD
    const simElem = page.locator(`[data-testid="${item.simContainer}"]:visible`).first();
    await expect(simElem).toBeVisible({ timeout: 10000 });
    await page.screenshot({ path: `C:/Users/princ/.gemini/antigravity/brain/f0985f12-5686-4fbe-a862-be3e4709f90c/${item.master}_alive.png` });

    await expect(simElem).toContainText('SALT Standard');
    await expect(simElem).toContainText('REFRACTOR MAGNIFICATION');

    // Step D: Filter Tabs (Reflecting Only -> Refracting Only -> All)
    const refractorTab = page.locator('[data-testid="btn-filter-refractor"]:visible').first();
    await expect(refractorTab).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, refractorTab);
    await refractorTab.click();
    await pauseAwareDwell(page, 500);

    const reflectorTab = page.locator('[data-testid="btn-filter-reflector"]:visible').first();
    await expect(reflectorTab).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, reflectorTab);
    await reflectorTab.click();
    await pauseAwareDwell(page, 500);

    const allTab = page.locator('[data-testid="btn-filter-all"]:visible').first();
    await expect(allTab).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, allTab);
    await allTab.click();
    await pauseAwareDwell(page, 500);

    // Step E: Toggle Chromatic Aberration
    const abToggleBtn = page.locator('[data-testid="btn-toggle-aberration"]:visible').first();
    await expect(abToggleBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, abToggleBtn);
    await abToggleBtn.click();
    await pauseAwareDwell(page, 500);

    // Step F: Return to Exam Mode
    const backToExamBtn = page.locator('[data-testid="btn-back-to-exam"]:visible').first();
    await expect(backToExamBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, backToExamBtn);
    await backToExamBtn.click();

    await expect(canvas).toBeVisible({ timeout: 10000 });
    console.log('[✓] Astronomical Optical Telescopes Dual-Mode Verified');
  });

});
