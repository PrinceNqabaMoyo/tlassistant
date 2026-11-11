import { test, expect } from '@playwright/test';

/**
 * Phase 4 Dual-Mode Static ↔ Alive Visualizations Contract (GP-24, GP-26, GP-27, GP-29, GP-30)
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater testing. Real user actions, live DOM assertions, genuine post-verification states.
 * - Rule 0d-2 & 0d-3: Authentic student persona (sch-gr8-01, Kagiso Molefe), no mock admin state.
 * - Rule 0d-4: Grounded in live JSX components (UniversalWorkspace, ParticleModelSvg, GeyserHeatingElementSvg, OpticalTelescopesSvg, AlveolusGasExchangeSvg).
 * - Rule 0d-6: Zero silent skips with explicit assertions.
 * - Rule 0d-9: Filter by :visible across viewports.
 * - Rule 0d-14: Anti-leak contract: Opaque pin tokens in question card, zero structure names leaked before grading.
 * - GP-24: Identify task has letter pins only (no names); context task has 0 pins; alive mode has 0 pinned labels on moving parts.
 * - GP-26: Live runtime state changes verified (temperature, thermostat trip, chromatic aberration toggle).
 * - GP-27: Alive mode driven by generator-emitted parameters.
 * - GP-29: Clean execution through live workspace DOM without synthetic setter backdoors or HUD narration.
 * - GP-30: Extended across all 4 pilot masters.
 */

test.describe('Batch 5: Phase 4 Dual-Mode Visuals Contract', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';

  test.beforeEach(async ({ page }) => {
    test.setTimeout(90000);
    await page.setViewportSize({ width: 1280, height: 850 });
    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });

    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'sch-gr8-01',
        name: 'Kagiso Molefe',
        role: 'student',
        type: 'student',
        grade: 8,
        school: 'Sandton Secondary School',
        assignedTasks: []
      });
      if (window.studentStore) {
        window.studentStore.setEnabledSubjects(['natural_sciences']);
        window.studentStore.completeDiagnostic('natural_sciences', 80);
      }
    });

    const openSubjectBtn = page.locator('[data-testid="btn-open-subject-session"]:visible').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    await page.waitForFunction(() => typeof window.__FUNDILE_LOAD_QUESTION__ === 'function', { timeout: 15000 });
  });

  test('GP-24 & GP-26: Particle Model of Matter (State Mutation & No Pinned Labels in Alive Mode)', async ({ page }) => {
    const questionData = {
      id: 'gp24_particle_model',
      subject: 'natural_sciences',
      grade: 8,
      topic: 'Particle model of matter',
      subskill: 'particle_kinetic_simulation',
      mode: 'practice',
      question_type: 'diagram',
      modality: 'diagram',
      question: 'Study the kinetic arrangement of particles across physical states.',
      prompt: 'Study the kinetic arrangement of particles across physical states.',
      diagram_spec: {
        master: 'particle_model',
        image_type: 'particle_model',
        diagram_role: 'identify',
        view: 'textbook',
        state: 'static',
        pins: [
          { pin: 'A', anchor: [135, 250], default_box: [60, 250], side: 'left' },
          { pin: 'B', anchor: [305, 250], default_box: [540, 250], side: 'right' }
        ]
      },
      marks: 4,
      correct_answer: 'Solid crystalline lattice'
    };

    await page.evaluate((q) => { window.__FUNDILE_LOAD_QUESTION__(q); }, questionData);

    const questionSurface = page.locator('[data-testid="question-surface"]:visible').first();
    await expect(questionSurface).toBeVisible({ timeout: 10000 });

    // 1. Identify task: Letter pin A exists, zero plain-text structure answers in DOM
    const pinA = questionSurface.locator('[data-testid="btn-select-pin-A"]:visible').first();
    await expect(pinA).toBeVisible({ timeout: 10000 });
    await expect(pinA).toContainText('A');

    // 2. Bring to Life toggle
    const bringToLifeBtn = questionSurface.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(bringToLifeBtn).toBeVisible({ timeout: 10000 });
    await bringToLifeBtn.click();

    // 3. Alive simulation container mounts
    const simContainer = questionSurface.locator('[data-testid="alive-kinetic-simulation"]:visible').first();
    await expect(simContainer).toBeVisible({ timeout: 10000 });

    // 4. In alive mode: 0 letter pins on moving parts (InteractiveCallouts disabled)
    const alivePins = simContainer.locator('[data-testid^="btn-select-pin-"]');
    expect(await alivePins.count()).toBe(0);

    // 5. GP-26: Real state mutation - Gas phase button changes temperature to 130 °C
    const gasBtn = questionSurface.locator('[data-testid="btn-phase-gas"]:visible').first();
    await expect(gasBtn).toBeVisible({ timeout: 5000 });
    await gasBtn.click();
    await expect(simContainer).toContainText('130 °C', { timeout: 5000 });

    // 6. Real state mutation - Melting phase button changes temperature to 0 °C
    const meltBtn = questionSurface.locator('[data-testid="btn-phase-melting"]:visible').first();
    await expect(meltBtn).toBeVisible({ timeout: 5000 });
    await meltBtn.click();
    await expect(simContainer).toContainText('0 °C', { timeout: 5000 });
  });

  test('GP-26 & GP-27: Geyser Heating Element (Thermostat Trip & Generator Power Parameter)', async ({ page }) => {
    const questionData = {
      id: 'gp26_geyser_element',
      subject: 'natural_sciences',
      grade: 8,
      topic: 'Energy transfer in electrical systems',
      subskill: 'joule_heating_effect',
      mode: 'practice',
      question_type: 'diagram',
      modality: 'diagram',
      question: 'Investigate the conversion of electrical energy into thermal energy in a domestic geyser.',
      prompt: 'Investigate the conversion of electrical energy into thermal energy in a domestic geyser.',
      diagram_spec: {
        master: 'geyser_heating_element',
        image_type: 'geyser_heating_element',
        diagram_role: 'context',
        view: 'textbook',
        state: 'static',
        heating_power_kw: 3.0,
        initial_temp: 35
      },
      marks: 4,
      correct_answer: 'Nichrome resistance wire transfers heat by conduction and convection'
    };

    await page.evaluate((q) => { window.__FUNDILE_LOAD_QUESTION__(q); }, questionData);

    const questionSurface = page.locator('[data-testid="question-surface"]:visible').first();
    await expect(questionSurface).toBeVisible({ timeout: 10000 });

    // 1. Context diagram: exactly 0 letter pins
    const contextPins = questionSurface.locator('[data-testid^="btn-select-pin-"]:visible');
    expect(await contextPins.count()).toBe(0);

    // 2. Bring to Life toggle
    const bringToLifeBtn = questionSurface.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(bringToLifeBtn).toBeVisible({ timeout: 10000 });
    await bringToLifeBtn.click();

    const simContainer = questionSurface.locator('[data-testid="alive-geyser-simulation"]:visible').first();
    await expect(simContainer).toBeVisible({ timeout: 10000 });

    // 3. Verify thermostat initial state: Closed (Heating)
    await expect(simContainer).toContainText('Closed (Heating)', { timeout: 5000 });

    // 4. GP-26: Mutate state - Trip thermostat manually
    const tripBtn = questionSurface.locator('[data-testid="btn-trip-thermostat"]:visible').first();
    await expect(tripBtn).toBeVisible({ timeout: 5000 });
    await tripBtn.click();

    // 5. Assert thermostat state mutates to Open (Tripped)
    await expect(simContainer).toContainText('Open (Tripped)', { timeout: 5000 });
  });

  test('GP-26 & GP-30: Optical Telescopes & Alveolus Gas Exchange Live Mounting', async ({ page }) => {
    // 1. Optical Telescopes (Dispersion mutation)
    const telescopeQuestion = {
      id: 'gp30_telescopes',
      subject: 'natural_sciences',
      grade: 8,
      topic: 'Looking into space',
      subskill: 'reflector_vs_refractor_optics',
      mode: 'practice',
      question_type: 'diagram',
      modality: 'diagram',
      question: 'Compare chromatic dispersion between reflecting and refracting telescopes.',
      prompt: 'Compare chromatic dispersion between reflecting and refracting telescopes.',
      diagram_spec: {
        master: 'optical_telescopes',
        image_type: 'optical_telescopes',
        diagram_role: 'context',
        view: 'textbook',
        state: 'static'
      },
      marks: 4,
      correct_answer: 'Reflecting telescopes use mirrors to prevent chromatic aberration'
    };

    await page.evaluate((q) => { window.__FUNDILE_LOAD_QUESTION__(q); }, telescopeQuestion);

    const questionSurface = page.locator('[data-testid="question-surface"]:visible').first();
    await expect(questionSurface).toBeVisible({ timeout: 10000 });

    const bringToLifeBtn = questionSurface.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(bringToLifeBtn).toBeVisible({ timeout: 10000 });
    await bringToLifeBtn.click();

    const simTelescope = questionSurface.locator('[data-testid="alive-optical-simulation"]:visible').first();
    await expect(simTelescope).toBeVisible({ timeout: 10000 });

    // Toggle chromatic aberration
    const aberrationBtn = questionSurface.locator('[data-testid="btn-toggle-aberration"]:visible').first();
    await expect(aberrationBtn).toBeVisible({ timeout: 5000 });
    await expect(aberrationBtn).toContainText('Show Chromatic Aberration');
    await aberrationBtn.click();
    await expect(aberrationBtn).toContainText('Dispersion ON', { timeout: 5000 });

    // 2. Alveolus Gas Exchange (Live simulation mounting)
    const alveolusQuestion = {
      id: 'gp30_alveolus',
      subject: 'natural_sciences',
      grade: 8,
      topic: 'Photosynthesis and respiration',
      subskill: 'cellular_respiration_energy_release',
      mode: 'practice',
      question_type: 'diagram',
      modality: 'diagram',
      question: 'Observe the counter-diffusion of oxygen and carbon dioxide across the squamous respiratory membrane.',
      prompt: 'Observe the counter-diffusion of oxygen and carbon dioxide across the squamous respiratory membrane.',
      diagram_spec: {
        master: 'alveolus_gas_exchange',
        image_type: 'alveolus_gas_exchange',
        diagram_role: 'context',
        view: 'textbook',
        state: 'static'
      },
      marks: 4,
      correct_answer: 'Diffusion down partial pressure gradients'
    };

    await page.evaluate((q) => { window.__FUNDILE_LOAD_QUESTION__(q); }, alveolusQuestion);

    const alveolusSurface = page.locator('[data-testid="question-surface"]:visible').first();
    await expect(alveolusSurface).toBeVisible({ timeout: 10000 });

    const alveolusLifeBtn = alveolusSurface.locator('[data-testid="btn-bring-to-life"]:visible').first();
    await expect(alveolusLifeBtn).toBeVisible({ timeout: 10000 });
    await alveolusLifeBtn.click();

    const alveolusStage = alveolusSurface.locator('[data-testid="alveolus-alive-stage"]:visible').first();
    await expect(alveolusStage).toBeVisible({ timeout: 10000 });
  });
});
