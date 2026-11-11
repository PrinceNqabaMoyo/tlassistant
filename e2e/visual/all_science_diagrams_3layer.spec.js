import { test, expect } from '@playwright/test';
import {
  injectGlidingCursorAndHud,
  updateHud,
  glideCursorTo,
  pauseAwareDwell,
} from '../helpers/autopilotHud.js';

/**
 * All Science Diagram Archetypes 3-Layer Visual Inspection Suite
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater verification. Genuine user actions, live DOM assertions, post-verification logs.
 * - Rule 0d-4: Grounded in live JSX components in diagram_bank/ and BioDiagramModalityRenderer.jsx.
 * - Rule 0d-6: Explicit assertions, zero silent skips.
 * - Rule 0d-7: Runtime execution verification & non-intrusive margins for test instrumentation.
 * - Rule 2b: Universal curriculum alignment language; zero "CAPS" acronym in UI assertions.
 *
 * Covers All 23 Science Diagram Archetypes with the 3-Layer Visual Architecture:
 * 1. Layer 1 (Locked Master Scientific View): Standardized 600x480 coordinate space.
 * 2. Layer 2 (Collision-Free Elbow Callout Pins): Horizontal leader elbows with anti-leak pin contract.
 * 3. Layer 3 (Pedagogical Interactivity & Badges): Dynamic inspection, responsive selection, zero answer leaks.
 */

const ALL_23_DIAGRAMS = [
  // =========================================================================
  // GROUP 1: NATURAL SCIENCES (Grades 7–9 Senior Phase) - 4 Archetypes
  // =========================================================================
  {
    id: 'distillation_apparatus',
    title: 'Simple Distillation Apparatus',
    subject: 'natural_sciences',
    subjectTab: 'natural_sciences',
    grade: 7,
    topic: 'Separating mixtures',
    subskill: 'distillation_apparatus',
    badge: 'distillation-apparatus-locked-view-badge',
    canvas: 'distillation-apparatus-canvas',
    description: 'Separation of mixtures via boiling and Liebig condenser condensation'
  },
  {
    id: 'particle_model',
    title: 'Particle Model of Matter',
    subject: 'natural_sciences',
    subjectTab: 'natural_sciences',
    grade: 8,
    topic: 'Particle model of matter',
    subskill: 'particle_model',
    badge: 'particle-model-locked-view-badge',
    canvas: 'particle-model-canvas',
    description: 'Kinetic microscopic arrangement across solid, liquid, and gas phases'
  },
  {
    id: 'electric_circuits_ns',
    title: 'Electric Circuits (Series & Parallel)',
    subject: 'natural_sciences',
    subjectTab: 'natural_sciences',
    grade: 8,
    topic: 'Series and parallel circuits',
    subskill: 'electric_circuits_ns',
    badge: 'electric-circuits-ns-locked-view-badge',
    canvas: 'electric-circuits-ns-canvas',
    description: 'Closed circuit schematics with series/parallel resistors and meters'
  },
  {
    id: 'solar_system_earth_space',
    title: 'The Solar System & Planetary Orbits',
    subject: 'natural_sciences',
    subjectTab: 'natural_sciences',
    grade: 8,
    topic: 'The Solar System',
    subskill: 'solar_system_earth_space',
    badge: 'solar-system-earth-space-locked-view-badge',
    canvas: 'solar-system-earth-space-canvas',
    description: 'Heliocentric celestial mechanics, terrestrial vs gas giant planets'
  },

  // =========================================================================
  // GROUP 2: LIFE SCIENCES (Grades 10–12 FET Phase) - 15 Archetypes
  // =========================================================================
  {
    id: 'human_heart',
    title: 'Mammalian Heart Gross Anatomy',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 10,
    topic: 'Transport systems in animals',
    subskill: 'heart_diagram',
    badge: 'heart-locked-view-badge',
    canvas: 'bio-diagram-canvas',
    description: 'Four chambers, atrioventricular valves, aorta & pulmonary circulation'
  },
  {
    id: 'plant_cell',
    title: 'Plant Cell Eukaryotic Ultrastructure',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 10,
    topic: 'Cells the basic units of life',
    subskill: 'plant_cell',
    badge: 'plant-cell-locked-view-badge',
    canvas: 'plant-cell-canvas',
    description: 'Cellulose cell wall, large central vacuole with tonoplast, and chloroplasts'
  },
  {
    id: 'animal_cell',
    title: 'Animal Cell Eukaryotic Ultrastructure',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 10,
    topic: 'Cells the basic units of life',
    subskill: 'animal_cell',
    badge: 'animal-cell-locked-view-badge',
    canvas: 'animal-cell-canvas',
    description: 'Plasma membrane, centrosome centrioles, mitochondria cristae, and lysosomes'
  },
  {
    id: 'plant_leaf',
    title: 'Dicotyledonous Leaf Cross-Section',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 10,
    topic: 'Support and transport systems in plants',
    subskill: 'leaf_structure_diagram',
    badge: 'plant-leaf-locked-view-badge',
    canvas: 'plant-leaf-canvas',
    description: 'Cuticle, epidermis, palisade & spongy mesophyll, stomatal guard cells'
  },
  {
    id: 'mitosis_stages',
    title: 'Stages of Mitotic Cell Division',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 10,
    topic: 'Cell division',
    subskill: 'mitosis_stages',
    badge: 'mitosis-stages-locked-view-badge',
    canvas: 'mitosis-stages-canvas',
    description: 'Prophase, Metaphase plate, Anaphase sister chromatids, Telophase'
  },
  {
    id: 'alveolus_gas_exchange',
    title: 'Alveolar-Capillary Gas Exchange Interface',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Gaseous exchange',
    subskill: 'alveolus_gas_exchange_anatomy',
    badge: 'alveolus-locked-view-badge',
    canvas: 'alveolus-gas-exchange-canvas',
    description: 'Alveolar pneumocytes, surfactant, capillary endothelium, erythrocyte diffusion'
  },
  {
    id: 'digestive_system',
    title: 'Human Alimentary Canal & Digestive System',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Animal Nutrition',
    subskill: 'digestive',
    badge: 'digestive-locked-view-badge',
    canvas: 'human-digestive-canvas',
    description: 'Esophagus, stomach, liver, pancreas, duodenum, ileum, colon'
  },
  {
    id: 'intestinal_villus',
    title: 'Intestinal Villus Microscopic Anatomy',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Animal Nutrition',
    subskill: 'villus',
    badge: 'villus-locked-view-badge',
    canvas: 'intestinal-villus-canvas',
    description: 'Columnar epithelium, microvilli brush border, lacteal, capillary plexus'
  },
  {
    id: 'human_nephron',
    title: 'Human Nephron & Renal Corpuscle',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 11,
    topic: 'Excretion in humans',
    subskill: 'nephron',
    badge: 'nephron-locked-view-badge',
    canvas: 'human-nephron-canvas',
    description: 'Glomerulus podocytes, Bowman capsule, PCT, loop of Henle, DCT, collecting duct'
  },
  {
    id: 'human_eye',
    title: 'Longitudinal Section of the Human Eye',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 12,
    topic: 'Human responses to the environment',
    subskill: 'eye',
    badge: 'eye-locked-view-badge',
    canvas: 'human-eye-canvas',
    description: 'Cornea, pupil, iris, lens, ciliary body, suspensory ligaments, retina, fovea'
  },
  {
    id: 'human_ear',
    title: 'Longitudinal Section of the Human Ear',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 12,
    topic: 'Human responses to the environment',
    subskill: 'ear',
    badge: 'ear-locked-view-badge',
    canvas: 'human-ear-canvas',
    description: 'Pinna, tympanic membrane, malleus, incus, stapes, cochlea, semicircular canals'
  },
  {
    id: 'endocrine_system',
    title: 'Human Endocrine System & Glandular Map',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 12,
    topic: 'The human endocrine system and homeostasis',
    subskill: 'endocrine_system_map',
    badge: 'endocrine-locked-view-badge',
    canvas: 'endocrine-system-canvas',
    description: 'Hypothalamus, pituitary, thyroid, adrenal glands, pancreas islets, gonads'
  },
  {
    id: 'male_reproductive',
    title: 'Male Reproductive System Sagittal Section',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 12,
    topic: 'Human Reproduction',
    subskill: 'male_reproductive',
    badge: 'male-repro-locked-view-badge',
    canvas: 'male-reproductive-canvas',
    description: 'Testis, epididymis, vas deferens, seminal vesicle, prostate, urethra'
  },
  {
    id: 'female_reproductive',
    title: 'Female Reproductive System Coronal Section',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 12,
    topic: 'Human Reproduction',
    subskill: 'female_reproductive',
    badge: 'female-repro-locked-view-badge',
    canvas: 'female-reproductive-canvas',
    description: 'Ovaries, Fallopian tubes with fimbriae, uterine fundus, endometrium, cervix'
  },
  {
    id: 'meiosis_crossing_over',
    title: 'Meiosis Prophase I Crossing-Over & Chiasmata',
    subject: 'life_sciences',
    subjectTab: 'life_sciences',
    grade: 12,
    topic: 'Meiosis',
    subskill: 'meiosis_crossing_over',
    badge: 'meiosis-crossing-over-locked-view-badge',
    canvas: 'meiosis-crossing-over-canvas',
    description: 'Synapsis of homologous bivalent tetrads, chiasma formation, genetic recombination'
  },

  // =========================================================================
  // GROUP 3: PHYSICAL SCIENCES (Grades 10–12 FET Phase) - 4 Archetypes
  // =========================================================================
  {
    id: 'transverse_wave',
    title: 'Transverse Wave Anatomy & Periodic Motion',
    subject: 'physical_sciences',
    subjectTab: 'physical_sciences',
    grade: 10,
    topic: 'Transverse waves',
    subskill: 'transverse_wave_anatomy',
    badge: 'transverse-wave-locked-view-badge',
    canvas: 'transverse-wave-canvas',
    description: 'Crest, trough, amplitude, equilibrium position, wavelength, points in phase'
  },
  {
    id: 'titration_apparatus',
    title: 'Volumetric Acid-Base Titration Apparatus',
    subject: 'physical_sciences',
    subjectTab: 'physical_sciences',
    grade: 11,
    topic: 'Quantitative aspects of chemical change',
    subskill: 'titration_apparatus',
    badge: 'titration-apparatus-locked-view-badge',
    canvas: 'titration-apparatus-canvas',
    description: 'Burette, stopcock valve, conical flask, retort stand, clamp, meniscus read'
  },
  {
    id: 'galvanic_cell',
    title: 'Galvanic Electrochemical Cell (Daniell Cell)',
    subject: 'physical_sciences',
    subjectTab: 'physical_sciences',
    grade: 12,
    topic: 'Electrochemical reactions',
    subskill: 'galvanic_cell_apparatus',
    badge: 'galvanic-cell-locked-view-badge',
    canvas: 'galvanic-cell-canvas',
    description: 'Zinc anode (-), copper cathode (+), KNO3 salt bridge, voltmeter, electron flow'
  },
  {
    id: 'doppler_effect',
    title: 'Doppler Effect Wavefront Geometry',
    subject: 'physical_sciences',
    subjectTab: 'physical_sciences',
    grade: 12,
    topic: 'The Doppler effect',
    subskill: 'doppler_effect_wavefronts',
    badge: 'doppler-effect-locked-view-badge',
    canvas: 'doppler-effect-canvas',
    description: 'Moving acoustic source, compressed wavefronts ahead, red-shift expansion behind'
  }
];

test.describe('All Science Diagram Archetypes 3-Layer Visual Inspection Suite', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';
  const backendBaseUrl = process.env.BACKEND_BASE_URL || 'http://127.0.0.1:5001';

  test('Headed Inspection: Sequentially verify and observe all 23 science diagram archetypes', async ({ page }) => {
    test.setTimeout(0); // Unlimited timeout for on-demand live human inspection & spacebar pausing

    await page.setViewportSize({ width: 1280, height: 850 });
    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });

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

    console.log('\n======================================================================');
    console.log(`[*] STARTING VISUAL REEL FOR ALL ${ALL_23_DIAGRAMS.length} SCIENCE DIAGRAM ARCHETYPES`);
    console.log('    Press SPACEBAR in browser anytime to PAUSE and inspect details');
    console.log('======================================================================\n');

    for (let i = 0; i < ALL_23_DIAGRAMS.length; i++) {
      const diag = ALL_23_DIAGRAMS[i];
      const stepNum = i + 1;
      const subjectLabel =
        diag.subject === 'natural_sciences' ? 'Natural Sciences' :
        diag.subject === 'life_sciences' ? 'Life Sciences' : 'Physical Sciences';

      const hudMsg = `[${stepNum}/${ALL_23_DIAGRAMS.length}] Grade ${diag.grade} ${subjectLabel} • ${diag.title}`;
      await updateHud(page, 'LEARNER', hudMsg);

      // 1. Fetch the genuine 3-layer diagram question payload from the live backend FIRST
      const genUrl = `${backendBaseUrl}/api/generate?subject=${encodeURIComponent(diag.subject)}&grade=${diag.grade}&topic=${encodeURIComponent(diag.topic)}&subskill=${encodeURIComponent(diag.subskill)}&seed=12345`;
      const response = await page.request.get(genUrl);
      expect(response.ok()).toBeTruthy();

      const json = await response.json();
      const question = Array.isArray(json.questions) && json.questions.length > 0 ? json.questions[0] : json.questions;
      currentDiagramQuestion = question;

      // 2. Switch persona to the authentic grade for this diagram
      await page.evaluate(({ grade }) => {
        window.__FUNDILE_SWITCH_PERSONA__({
          id: `sch-gr${String(grade).padStart(2, '0')}-01`,
          name: 'Science Visual Inspector',
          role: 'student',
          type: 'student',
          grade: grade,
          school: 'Westville High School',
          assignedTasks: []
        });
        if (window.studentStore) {
          window.studentStore.setEnabledSubjects(['natural_sciences', 'life_sciences', 'physical_sciences', 'mathematics']);
          ['natural_sciences', 'life_sciences', 'physical_sciences'].forEach((s) => window.studentStore.completeDiagnostic(s, 65));
        }
      }, { grade: diag.grade });

      // 3. Switch to the relevant subject tab on the desktop rail
      await page.evaluate(({ tab }) => {
        if (typeof window.__FUNDILE_SELECT_TAB__ === 'function') {
          window.__FUNDILE_SELECT_TAB__(tab);
        }
      }, { tab: diag.subjectTab });

      // 4. Load the question into the Universal Workspace
      await page.evaluate(({ q, topic }) => {
        if (typeof window.__FUNDILE_LOAD_QUESTION__ === 'function') {
          window.__FUNDILE_LOAD_QUESTION__(q, topic);
        }
      }, { q: question, topic: diag.topic });

      // 5. Assert that the Bio Diagram Canvas card mounts cleanly
      const bioCanvas = page.locator('[data-testid="bio-diagram-canvas"]:visible').first();
      await expect(bioCanvas).toBeVisible({ timeout: 15000 });

      // 6. Assert that the specific diagram canvas is visible
      const specificCanvas = page.locator(`[data-testid="${diag.canvas}"]:visible`).first();
      await expect(specificCanvas).toBeVisible({ timeout: 10000 });

      // 7. Assert that the locked view badge is visible
      const lockedBadge = page.locator(`[data-testid="${diag.badge}"]:visible`).first();
      await expect(lockedBadge).toBeVisible({ timeout: 10000 });

      // 8. Assert Anti-Leak Contract (No raw correct answer leaked in SVG text nodes)
      const svgTextContent = await specificCanvas.locator('text').allInnerTexts();
      const rawAnswer = String(question.correct_answer || '').trim().toLowerCase();
      if (rawAnswer.length > 3) {
        const hasLeak = svgTextContent.some(
          (t) => typeof t === 'string' && t.trim().toLowerCase() === rawAnswer && !['a', 'b', 'c', 'd'].includes(t.trim().toLowerCase())
        );
        expect(hasLeak).toBeFalsy();
      }

      // 9. Interactive movement: Glide cursor to pin button A and click it
      const pinSelectA = page.locator('[data-testid="btn-select-pin-A"]:visible').first();
      await expect(pinSelectA).toBeVisible({ timeout: 10000 });
      await glideCursorTo(page, pinSelectA);
      await pinSelectA.click();

      // 10. Assert active pin detail appears with anti-leak message
      const pinDetail = page.locator('[data-testid="bio-pin-detail"]:visible').first();
      await expect(pinDetail).toBeVisible({ timeout: 5000 });
      await expect(pinDetail).toContainText('Active target pin selected for response');

      // 11. Interactive movement: Glide cursor to locked view badge
      await glideCursorTo(page, lockedBadge);

      console.log(`[HEADED AUDIT ${stepNum}/23] Verified ${diag.title} (Grade ${diag.grade} ${subjectLabel}) - Locked View & Anti-Leak Active.`);

      // 11. Visual dwell for human inspection (Spacebar-pause aware)
      await pauseAwareDwell(page, 1500);
    }

    console.log('\n======================================================================');
    console.log('✅ ALL 23 SCIENCE DIAGRAM ARCHETYPES SUCCESSFULLY INSPECTED & VERIFIED');
    console.log('======================================================================\n');
  });
});
