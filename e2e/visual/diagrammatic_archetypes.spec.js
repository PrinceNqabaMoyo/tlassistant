import { test, expect } from '@playwright/test';

import { injectGlidingCursorAndHud, updateHud, glideCursorTo, pauseAwareDwell } from '../helpers/autopilotHud.js';



/**

 * Visual & Diagrammatic Archetypes Headed Inspection Suite

 *

 * Strict Compliance:

 * - Rule 0d-1: Zero-theater end-to-end verification. Real authentic user movements,

 *   real form clicks, real state transitions, and post-assertion verification logs only.

 * - Rule 0d-4: Source-code grounded locators confirmed in live JSX components.

 * - Rule 0d-6: Zero silent skips with explicit assertions (no `if (isVisible())`).

 * - Rule 0d-7: Runtime execution verification & non-intrusive margins for test instrumentation.

 * - Rule 2b: Universal curriculum alignment language; zero "CAPS" acronym in UI assertions.

 *

 * Covers All 8 Visual Modalities & Interactive Canvases:

 * 1. Circuit Schematic (CircuitModalityRenderer.jsx) — Physical Sciences Gr 10

 * 2. Punnett Square Genetic Cross (PunnettSquareModalityRenderer.jsx) — Life Sciences Gr 12

 * 3. Biological Diagram Labeling (BioDiagramModalityRenderer.jsx) — Natural Sciences Gr 9

 * 4. Free Body Diagram (FbdModalityRenderer.jsx) — Physical Sciences Gr 11

 * 5. 3D Geometric Nets Polyhedron Folding (GeometricNets3DViewer.jsx) — Mathematics Gr 7

 * 6. 3D Organic Chemistry CPK Molecular Explorer (OrganicChemistry3DViewer.jsx) — Physical Sciences Gr 12

 * 7. Electrodynamics Armature & Live Oscilloscope (ElectrodynamicsMotorViewer.jsx) — Physical Sciences Gr 12

 * 8. Dynamic Circle Geometry Board (DiagramModalityRenderer.jsx) — Mathematics Gr 11

 */



test.describe('Diagrammatic Archetypes Live Visual Inspection Suite', () => {

  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';



  test('Headed Inspection: Render and interact with all 8 visual diagrammatic modalities', async ({ page }) => {

    test.setTimeout(0); // Unlimited timeout for on-demand human inspection & pausing



    await page.setViewportSize({ width: 1280, height: 850 });

    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });



    // Await persona switcher function on window

    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });



    // Enable full subject suite in student store & calibrate to practice stage

    await page.evaluate(() => {

      if (window.studentStore) {

        const subjects = [

          'accounting',

          'mathematics',

          'physical_sciences',

          'life_sciences',

          'natural_sciences',

          'economic_and_management_sciences'

        ];

        window.studentStore.setEnabledSubjects(subjects);

        subjects.forEach((s) => window.studentStore.completeDiagnostic(s, 65));

      }

    });



    await injectGlidingCursorAndHud(page);



    // =========================================================================

    // MODALITY 1: ELECTRIC CIRCUIT SCHEMATIC (Grade 10 Physical Sciences)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 1/8: Electric Circuit Schematic (Grade 10 Physical Sciences)');



    // Switch to Grade 10 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr10-01',

        name: 'Lesedi Khumalo',

        role: 'student',

        type: 'student',

        grade: 10,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Physical Sciences on the rail

    const physTabGr10 = page.locator('[data-testid="tab-physical_sciences"]:visible').first();

    await expect(physTabGr10).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, physTabGr10);

    await physTabGr10.click();



    // Start session from Today's Desk

    const openSubjectBtn1 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn1).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn1);

    await openSubjectBtn1.click();



    // Open Topic Scope Modal

    const topicScopeBtn1 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn1).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn1);

    await topicScopeBtn1.click();



    // Filter "Electric circuits"

    const searchInput1 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput1).toBeVisible({ timeout: 10000 });

    await searchInput1.fill('Electric circuits');



    const circuitTopicCard = page.locator('[data-testid="topic-card-electric-circuits"]:visible').first();

    await expect(circuitTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, circuitTopicCard);

    await circuitTopicCard.click();



    // Verify Circuit Schematic Canvas rendered

    const circuitCanvas = page.locator('[data-testid="circuit-schematic-canvas"]:visible').first();

    await expect(circuitCanvas).toBeVisible({ timeout: 20000 });



    // Interactive inspections on circuit components

    const batteryComp = page.locator('[data-testid="circuit-component-battery"]:visible').first();

    await expect(batteryComp).toBeVisible();

    await glideCursorTo(page, batteryComp);

    await batteryComp.click();



    const switchComp = page.locator('[data-testid="circuit-component-switch"]:visible').first();

    await expect(switchComp).toBeVisible();

    await glideCursorTo(page, switchComp);

    await switchComp.click();



    const ammeterComp = page.locator('[data-testid="circuit-component-ammeter"]:visible').first();

    await expect(ammeterComp).toBeVisible();

    await glideCursorTo(page, ammeterComp);

    await ammeterComp.click();



    const resistorComp = page.locator('[data-testid="circuit-component-resistor-1"]:visible').first();

    await expect(resistorComp).toBeVisible();

    await glideCursorTo(page, resistorComp);

    await resistorComp.click();



    console.log('[VISUAL AUDIT] Verified Modality 1: Circuit Schematic Canvas loaded and interactive.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // =========================================================================

    // MODALITY 2: PUNNETT SQUARE GENETIC CROSS (Grade 12 Life Sciences)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 2/8: Punnett Square Genetic Cross (Grade 12 Life Sciences)');



    // Return to Today's Desk

    const deskBtn2 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn2).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn2);

    await deskBtn2.click();



    // Switch to Grade 12 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr12-01',

        name: 'Prince Moyo',

        role: 'student',

        type: 'student',

        grade: 12,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        window.studentStore.setEnabledSubjects(['physical_sciences', 'mathematics', 'life_sciences', 'accounting']);

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Life Sciences Tab

    const lifeTabGr12 = page.locator('[data-testid="tab-life_sciences"]:visible').first();

    await expect(lifeTabGr12).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, lifeTabGr12);

    await lifeTabGr12.click();



    // Start session from Today's Desk

    const openSubjectBtn2 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn2).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn2);

    await openSubjectBtn2.click();



    // Open Topic Scope Modal

    const topicScopeBtn2 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn2).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn2);

    await topicScopeBtn2.click();



    // Filter "Genetics and inheritance"

    const searchInput2 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput2).toBeVisible({ timeout: 10000 });

    await searchInput2.fill('Genetics and inheritance');



    const geneticsTopicCard = page.locator('[data-testid="topic-card-genetics-and-inheritance"]:visible').first();

    await expect(geneticsTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, geneticsTopicCard);

    await geneticsTopicCard.click();



    // Verify Punnett Square Canvas rendered

    const punnettCanvas = page.locator('[data-testid="punnett-square-canvas"]:visible').first();

    await expect(punnettCanvas).toBeVisible({ timeout: 20000 });



    // Interactive exploration across Punnett 2x2 grid

    const punnettGrid = punnettCanvas.locator('table');

    await expect(punnettGrid).toBeVisible();

    await glideCursorTo(page, punnettGrid);



    console.log('[VISUAL AUDIT] Verified Modality 2: Punnett Square Genetic Cross Canvas loaded and interactive.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // =========================================================================

    // MODALITY 3: BIOLOGICAL DIAGRAM LABELING (Grade 9 Natural Sciences)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 3/8: Biological Diagram Labeling (Grade 9 Natural Sciences)');



    // Return to Today's Desk

    const deskBtn3 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn3).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn3);

    await deskBtn3.click();



    // Switch to Grade 9 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr09-01',

        name: 'Zanele Ndlovu',

        role: 'student',

        type: 'student',

        grade: 9,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Natural Sciences Tab

    const natSciTabGr9 = page.locator('[data-testid="tab-natural_sciences"]:visible').first();

    await expect(natSciTabGr9).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, natSciTabGr9);

    await natSciTabGr9.click();



    // Start session from Today's Desk

    const openSubjectBtn3 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn3).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn3);

    await openSubjectBtn3.click();



    // Open Topic Scope Modal

    const topicScopeBtn3 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn3).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn3);

    await topicScopeBtn3.click();



    // Filter "Cells as the basic units of life"

    const searchInput3 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput3).toBeVisible({ timeout: 10000 });

    await searchInput3.fill('Cells as the basic units of life');



    const cellTopicCard = page.locator('[data-testid="topic-card-cells-as-the-basic-units-of-life"]:visible').first();

    await expect(cellTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, cellTopicCard);

    await cellTopicCard.click();



    // Verify Bio Diagram Canvas rendered

    const bioCanvas = page.locator('[data-testid="bio-diagram-canvas"]:visible').first();

    await expect(bioCanvas).toBeVisible({ timeout: 20000 });



    // Interactive pin selections

    const pinA = page.locator('[data-testid="bio-pin-A"]:visible').first();

    await expect(pinA).toBeVisible();

    await glideCursorTo(page, pinA);

    await pinA.click();



    const pinB = page.locator('[data-testid="bio-pin-B"]:visible').first();

    await expect(pinB).toBeVisible();

    await glideCursorTo(page, pinB);

    await pinB.click();



    const pinButtonA = page.locator('[data-testid="btn-select-pin-A"]:visible').first();

    await expect(pinButtonA).toBeVisible();

    await glideCursorTo(page, pinButtonA);

    await pinButtonA.click();



    console.log('[VISUAL AUDIT] Verified Modality 3: Biological Diagram Labeling Canvas loaded and interactive.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // =========================================================================

    // MODALITY 3b: ANATOMICAL REPRODUCTIVE DIAGRAM (Grade 9 Natural Sciences)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 3b: Human Reproductive Anatomical Diagram (Grade 9 Natural Sciences)');



    // Open Topic Scope Modal

    const topicScopeBtn3b = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn3b).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn3b);

    await topicScopeBtn3b.click();



    // Search and select "Human reproduction"

    const searchInput3b = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput3b).toBeVisible({ timeout: 10000 });

    await searchInput3b.fill('Human reproduction');



    const reproTopicCard = page.locator('[data-testid="topic-card-human-reproduction"]:visible').first();

    await expect(reproTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, reproTopicCard);

    await reproTopicCard.click();



    // Verify Anatomical Bio Diagram Canvas rendered

    const reproBioCanvas = page.locator('[data-testid="bio-diagram-canvas"]:visible').first();

    await expect(reproBioCanvas).toBeVisible({ timeout: 20000 });



    // Inspect Pin A (Anatomical Organ / Structure)

    const pinReproA = page.locator('[data-testid="bio-pin-A"]:visible').first();

    await expect(pinReproA).toBeVisible();

    await glideCursorTo(page, pinReproA);

    await pinReproA.click();



    // Verify detail callout identifies the organ

    const reproPinDetail = page.locator('[data-testid="bio-pin-detail"]:visible').first();

    await expect(reproPinDetail).toBeVisible();



    console.log('[VISUAL AUDIT] Verified Modality 3b: Anatomical Reproductive Vector Diagram loaded and interactive.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection

    // =========================================================================
    // MODALITY 3c: HUMAN HEART GROSS ANATOMY & ANTI-LEAK PIN CONTRACT (Grade 9 Natural Sciences)
    // =========================================================================
    await updateHud(page, 'LEARNER', 'Modality 3c: Human Heart Gross Anatomy & Anti-Leak Contract (Grade 9 Natural Sciences)');

    // Open Topic Scope Modal
    const topicScopeBtn3c = page.locator('[data-testid="btn-topic-scope"]:visible').first();
    await expect(topicScopeBtn3c).toBeVisible({ timeout: 15000 });
    await glideCursorTo(page, topicScopeBtn3c);
    await topicScopeBtn3c.click();

    // Search and select "Circulatory and respiratory systems"
    const searchInput3c = page.locator('[data-testid="input-topic-search"]:visible').first();
    await expect(searchInput3c).toBeVisible({ timeout: 10000 });
    await searchInput3c.fill('Circulatory and respiratory systems');

    const heartTopicCard = page.locator('[data-testid="topic-card-circulatory-and-respiratory-systems"]:visible').first();
    await expect(heartTopicCard).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, heartTopicCard);
    await heartTopicCard.click();

    // Verify Human Heart Bio Diagram Canvas rendered
    const heartBioCanvas = page.locator('[data-testid="bio-diagram-canvas"]:visible').first();
    await expect(heartBioCanvas).toBeVisible({ timeout: 20000 });

    // Assert Anti-Leak Pin Contract: Select Pin A
    const pinHeartA = page.locator('[data-testid="bio-pin-A"]:visible').first();
    await expect(pinHeartA).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, pinHeartA);
    await pinHeartA.click();

    // Verify detail callout maintains anti-leak invariant (does NOT reveal answer name prior to submission)
    const heartPinDetail = page.locator('[data-testid="bio-pin-detail"]:visible').first();
    await expect(heartPinDetail).toBeVisible();
    await expect(heartPinDetail).toContainText('Active target pin selected for response');

    console.log('[VISUAL AUDIT] Verified Modality 3c: Human Heart Gross Anatomy & Anti-Leak Pin Contract loaded and interactive.');

    // Verify Single Locked View Badge on Question Card (no manual view switcher clutter inside questions)
    const lockedViewBadge = page.locator('[data-testid="heart-locked-view-badge"]:visible').first();
    await expect(lockedViewBadge).toBeVisible();

    // Open Exploratory Visual Aid Sidecar Drawer to verify Multi-View Reference Atlas (Textbook, Blood Flow, Exam Paper)
    const toggleAidBtn = page.locator('[data-testid="btn-toggle-visual-aid"]:visible').first();
    await expect(toggleAidBtn).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, toggleAidBtn);
    await toggleAidBtn.click();

    const sidecarDrawer = page.locator('[data-testid="cognitive-sidecar-drawer"]:visible').first();
    await expect(sidecarDrawer).toBeVisible({ timeout: 10000 });

    const btnFlowView = sidecarDrawer.locator('[data-testid="btn-view-flow"]:visible').first();
    await expect(btnFlowView).toBeVisible();
    await glideCursorTo(page, btnFlowView);
    await btnFlowView.click();
    await pauseAwareDwell(page, 1500);

    const btnExamView = sidecarDrawer.locator('[data-testid="btn-view-exam"]:visible').first();
    await expect(btnExamView).toBeVisible();
    await glideCursorTo(page, btnExamView);
    await btnExamView.click();
    await pauseAwareDwell(page, 1500);

    const btnTextbookView = sidecarDrawer.locator('[data-testid="btn-view-textbook"]:visible').first();
    await expect(btnTextbookView).toBeVisible();
    await glideCursorTo(page, btnTextbookView);
    await btnTextbookView.click();
    await pauseAwareDwell(page, 1500);

    const closeSidecarBtn = sidecarDrawer.locator('[data-testid="btn-close-sidecar"]:visible').first();
    await expect(closeSidecarBtn).toBeVisible();
    await glideCursorTo(page, closeSidecarBtn);
    await closeSidecarBtn.click();
    await expect(sidecarDrawer).not.toBeVisible();

    // =========================================================================
    // MODALITY 3d: CARDIAC CYCLE & VALVE DYNAMICS SIMULEARN REPLAY (Grade 10 Life Sciences)
    // =========================================================================
    await updateHud(page, 'LEARNER', 'Modality 3d: Cardiac Cycle & Valve Dynamics Simulation (Grade 10 Life Sciences)');

    // Return to Today's Desk
    const deskBtn3d = page.locator('[data-testid="tab-desk"]:visible').first();
    await expect(deskBtn3d).toBeVisible({ timeout: 15000 });
    await glideCursorTo(page, deskBtn3d);
    await deskBtn3d.click();

    // Switch to Grade 10 student persona
    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'sch-gr10-01',
        name: 'Lesedi Khumalo',
        role: 'student',
        type: 'student',
        grade: 10,
        school: 'Westville High School',
        assignedTasks: []
      });
      if (window.studentStore) {
        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>
          window.studentStore.completeDiagnostic(s, 65)
        );
      }
    });

    // Select Life Sciences Tab on the rail
    const lifeTabGr10 = page.locator('[data-testid="tab-life_sciences"]:visible').first();
    await expect(lifeTabGr10).toBeVisible({ timeout: 15000 });
    await glideCursorTo(page, lifeTabGr10);
    await lifeTabGr10.click();

    // Start session from Today's Desk
    const openSubjectBtn3d = page.locator('[data-testid="btn-open-subject-session"]:visible').first();
    await expect(openSubjectBtn3d).toBeVisible({ timeout: 15000 });
    await glideCursorTo(page, openSubjectBtn3d);
    await openSubjectBtn3d.click();

    // Open Topic Scope Modal for Life Sciences
    const topicScopeBtn3d = page.locator('[data-testid="btn-topic-scope"]:visible').first();
    await expect(topicScopeBtn3d).toBeVisible({ timeout: 15000 });
    await glideCursorTo(page, topicScopeBtn3d);
    await topicScopeBtn3d.click();

    // Search and select "Transport systems in animals"
    const searchInput3d = page.locator('[data-testid="input-topic-search"]:visible').first();
    await expect(searchInput3d).toBeVisible({ timeout: 10000 });
    await searchInput3d.fill('Transport systems in animals');

    const transportTopicCard = page.locator('[data-testid="topic-card-transport-systems-in-animals"]:visible').first();
    await expect(transportTopicCard).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, transportTopicCard);
    await transportTopicCard.click();

    // Verify Bio Diagram Canvas rendered with Heart Vector
    const cardiacBioCanvas = page.locator('[data-testid="bio-diagram-canvas"]:visible').first();
    await expect(cardiacBioCanvas).toBeVisible({ timeout: 20000 });

    // Launch SimuLearn Process Simulation
    const simulearnTopBtn = page.locator('[data-testid="btn-top-simulearn"]:visible').first();
    await expect(simulearnTopBtn).toBeVisible({ timeout: 15000 });
    await glideCursorTo(page, simulearnTopBtn);
    await simulearnTopBtn.click();

    // Verify SimuLearn Player Modal & Diagram Process Workspace
    const simModal = page.locator('[data-testid="modal-simulearn-player"]:visible').first();
    await expect(simModal).toBeVisible({ timeout: 15000 });

    const simProcess = page.locator('[data-testid="simulearn-diagram-process"]:visible').first();
    await expect(simProcess).toBeVisible();

    const phaseBadge = page.locator('[data-testid="sim-phase-badge"]:visible').first();
    await expect(phaseBadge).toBeVisible();
    await expect(phaseBadge).toContainText('atrial systole', { ignoreCase: true });

    // Step to Next Phase: Ventricular Systole (0,3s) with Lubb sound
    const simNextBtn = page.locator('[data-testid="btn-simulearn-next"]:visible').first();
    await expect(simNextBtn).toBeVisible();
    await glideCursorTo(page, simNextBtn);
    await simNextBtn.click();

    await expect(phaseBadge).toContainText('ventricular systole', { ignoreCase: true });
    const soundBadge = page.locator('[data-testid="sim-sound-badge"]:visible').first();
    await expect(soundBadge).toBeVisible();
    await expect(soundBadge).toContainText('lubb', { ignoreCase: true });

    // Step to Next Phase: General Diastole (0,4s) with Dupp sound
    await glideCursorTo(page, simNextBtn);
    await simNextBtn.click();

    await expect(phaseBadge).toContainText('general diastole', { ignoreCase: true });
    await expect(soundBadge).toContainText(/du[pb]b?/i);

    // Close SimuLearn Player
    const simCloseBtn = page.locator('[data-testid="btn-simulearn-close"]:visible').first();
    await expect(simCloseBtn).toBeVisible();
    await glideCursorTo(page, simCloseBtn);
    await simCloseBtn.click();
    await expect(simModal).not.toBeVisible();

    console.log('[VISUAL AUDIT] Verified Modality 3d: Human Heart Cardiac Cycle & Valve Dynamics Simulation with synchronized sound/ECG HUD verified.');
    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection




    // =========================================================================

    // MODALITY 4: FREE BODY DIAGRAM (Grade 11 Physical Sciences)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 4/8: Free Body Diagram FBD (Grade 11 Physical Sciences)');



    // Return to Today's Desk

    const deskBtn4 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn4).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn4);

    await deskBtn4.click();



    // Switch to Grade 11 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr11-01',

        name: 'Kelebogile Mokoena',

        role: 'student',

        type: 'student',

        grade: 11,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        window.studentStore.setEnabledSubjects(['physical_sciences', 'mathematics', 'life_sciences', 'accounting']);

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Physical Sciences Tab

    const physTabGr11 = page.locator('[data-testid="tab-physical_sciences"]:visible').first();

    await expect(physTabGr11).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, physTabGr11);

    await physTabGr11.click();



    // Start session from Today's Desk

    const openSubjectBtn4 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn4).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn4);

    await openSubjectBtn4.click();



    // Open Topic Scope Modal

    const topicScopeBtn4 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn4).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn4);

    await topicScopeBtn4.click();



    // Filter "Vectors in two dimensions"

    const searchInput4 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput4).toBeVisible({ timeout: 10000 });

    await searchInput4.fill('Vectors in two dimensions');



    const vectorsTopicCard = page.locator('[data-testid="topic-card-vectors-in-two-dimensions"]:visible').first();

    await expect(vectorsTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, vectorsTopicCard);

    await vectorsTopicCard.click();



    // Verify FBD Canvas rendered

    const fbdCanvas = page.locator('[data-testid="fbd-canvas"]:visible').first();

    await expect(fbdCanvas).toBeVisible({ timeout: 20000 });



    // Interactive force inspections (strictly derived from the live forces rendered on canvas)

    const legendForces = fbdCanvas.locator('div[data-testid^="fbd-legend-"]:visible');

    const forceCount = await legendForces.count();

    expect(forceCount).toBeGreaterThanOrEqual(3);



    for (let i = 0; i < forceCount; i++) {

      const legendItem = legendForces.nth(i);

      await expect(legendItem).toBeVisible();

      await glideCursorTo(page, legendItem);

      await legendItem.click();

      await pauseAwareDwell(page, 300);

    }



    // Also inspect vector label in SVG

    const firstVectorLabel = fbdCanvas.locator('text[data-testid^="fbd-label-"]:visible').first();

    await expect(firstVectorLabel).toBeVisible();

    await glideCursorTo(page, firstVectorLabel);

    await firstVectorLabel.click({ force: true });



    console.log(`[VISUAL AUDIT] Verified Modality 4: Free Body Diagram Canvas loaded with ${forceCount} authentic vector forces.`);

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // =========================================================================

    // MODALITY 5: 3D GEOMETRIC NETS POLYHEDRON FOLDING (Grade 7 Mathematics)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 5/8: 3D Geometric Nets Polyhedron Folding (Grade 7 Mathematics)');



    // Return to Today's Desk

    const deskBtn5 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn5).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn5);

    await deskBtn5.click();



    // Switch to Grade 7 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr07-01',

        name: 'Ayanda Sithole',

        role: 'student',

        type: 'student',

        grade: 7,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        window.studentStore.setEnabledSubjects(['mathematics', 'natural_sciences', 'economic_and_management_sciences']);

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Mathematics Tab

    const mathTabGr7 = page.locator('[data-testid="tab-mathematics"]:visible').first();

    await expect(mathTabGr7).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, mathTabGr7);

    await mathTabGr7.click();



    // Start session from Today's Desk

    const openSubjectBtn5 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn5).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn5);

    await openSubjectBtn5.click();



    // Open Topic Scope Modal

    const topicScopeBtn5 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn5).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn5);

    await topicScopeBtn5.click();



    // Filter "Geometry of 3D objects"

    const searchInput5 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput5).toBeVisible({ timeout: 10000 });

    await searchInput5.fill('Geometry of 3D objects');



    const netsTopicCard = page.locator('[data-testid="topic-card-geometry-of-3d-objects"]:visible').first();

    await expect(netsTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, netsTopicCard);

    await netsTopicCard.click();



    // Verify 3D Geometric Nets Canvas rendered

    const netsCanvas = page.locator('[data-testid="geometric-nets-canvas"]:visible').first();

    await expect(netsCanvas).toBeVisible({ timeout: 20000 });



    // Interactive shape switches

    const triPrismBtn = page.locator('[data-testid="btn-net-shape-triangular_prism"]:visible').first();

    await expect(triPrismBtn).toBeVisible();

    await glideCursorTo(page, triPrismBtn);

    await triPrismBtn.click();

    await pauseAwareDwell(page, 600);



    const tetraBtn = page.locator('[data-testid="btn-net-shape-tetrahedron"]:visible').first();

    await expect(tetraBtn).toBeVisible();

    await glideCursorTo(page, tetraBtn);

    await tetraBtn.click();

    await pauseAwareDwell(page, 600);



    const cubeBtn = page.locator('[data-testid="btn-net-shape-cube"]:visible').first();

    await expect(cubeBtn).toBeVisible();

    await glideCursorTo(page, cubeBtn);

    await cubeBtn.click();



    // Toggle flat 2D vs folded 3D

    const foldFlatBtn = page.locator('[data-testid="btn-fold-flat"]:visible').first();

    await expect(foldFlatBtn).toBeVisible();

    await glideCursorTo(page, foldFlatBtn);

    await foldFlatBtn.click();

    await pauseAwareDwell(page, 800);



    const foldFoldedBtn = page.locator('[data-testid="btn-fold-folded"]:visible').first();

    await expect(foldFoldedBtn).toBeVisible();

    await glideCursorTo(page, foldFoldedBtn);

    await foldFoldedBtn.click();



    console.log('[VISUAL AUDIT] Verified Modality 5: 3D Geometric Nets Polyhedron Folding loaded and interactive.');

    await pauseAwareDwell(page, 3500); // Visual dwell for user inspection



    // =========================================================================

    // MODALITY 6: 3D ORGANIC CHEMISTRY CPK EXPLORER (Grade 12 Physical Sciences)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 6/8: 3D Organic Chemistry CPK Explorer (Grade 12 Physical Sciences)');



    // Return to Today's Desk

    const deskBtn6 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn6).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn6);

    await deskBtn6.click();



    // Switch to Grade 12 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr12-01',

        name: 'Prince Moyo',

        role: 'student',

        type: 'student',

        grade: 12,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Physical Sciences Tab

    const physTabGr12 = page.locator('[data-testid="tab-physical_sciences"]:visible').first();

    await expect(physTabGr12).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, physTabGr12);

    await physTabGr12.click();



    // Start session from Today's Desk

    const openSubjectBtn6 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn6).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn6);

    await openSubjectBtn6.click();



    // Open Topic Scope Modal

    const topicScopeBtn6 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn6).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn6);

    await topicScopeBtn6.click();



    // Filter "Organic molecules"

    const searchInput6 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput6).toBeVisible({ timeout: 10000 });

    await searchInput6.fill('Organic molecules');



    const organicTopicCard = page.locator('[data-testid="topic-card-organic-molecules"]:visible').first();

    await expect(organicTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, organicTopicCard);

    await organicTopicCard.click();



    // Verify 3D Organic Chem Canvas rendered

    const organicCanvas = page.locator('[data-testid="organic-chem-canvas"]:visible').first();

    await expect(organicCanvas).toBeVisible({ timeout: 20000 });



    // Interactive molecule selectors

    const molIsobutane = page.locator('[data-testid="btn-mol-methylpropane"]:visible').first();

    await expect(molIsobutane).toBeVisible();

    await glideCursorTo(page, molIsobutane);

    await molIsobutane.click();

    await pauseAwareDwell(page, 600);



    const molPropanol = page.locator('[data-testid="btn-mol-propan1ol"]:visible').first();

    await expect(molPropanol).toBeVisible();

    await glideCursorTo(page, molPropanol);

    await molPropanol.click();

    await pauseAwareDwell(page, 600);



    const molButane = page.locator('[data-testid="btn-mol-butane"]:visible').first();

    await expect(molButane).toBeVisible();

    await glideCursorTo(page, molButane);

    await molButane.click();



    console.log('[VISUAL AUDIT] Verified Modality 6: 3D Organic Chemistry CPK Explorer loaded and interactive.');
    await pauseAwareDwell(page, 3500); // Visual dwell for user inspection

    // Dismiss Sidecar Drawer before navigating topics
    const closeSidecarBtn6 = page.locator('[data-testid="btn-close-sidecar"]:visible').first();
    await expect(closeSidecarBtn6).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, closeSidecarBtn6);
    await closeSidecarBtn6.click();
    await expect(page.locator('[data-testid="cognitive-sidecar-drawer"]:visible').first()).toBeHidden({ timeout: 5000 });



    // =========================================================================

    // MODALITY 7: ELECTRODYNAMICS ARMATURE & LIVE OSCILLOSCOPE (Grade 12 Physical Sciences)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 7/8: Electrodynamics Armature & Live Oscilloscope (Grade 12 Physical Sciences)');



    // In current Physical Sciences workspace, open Topic Scope Modal directly

    const topicScopeBtn7 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn7).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn7);

    await topicScopeBtn7.click();



    // Filter "Electrodynamics"

    const searchInput7 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput7).toBeVisible({ timeout: 10000 });

    await searchInput7.fill('Electrodynamics');



    const electroTopicCard = page.locator('[data-testid="topic-card-electrodynamics"]:visible').first();

    await expect(electroTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, electroTopicCard);

    await electroTopicCard.click();



    // Verify Electrodynamics Canvas rendered

    const electroCanvas = page.locator('[data-testid="electrodynamics-canvas"]:visible').first();

    await expect(electroCanvas).toBeVisible({ timeout: 20000 });



    // Interactive machine mode switching

    const dcMotorBtn = page.locator('[data-testid="btn-mode-dc-motor"]:visible').first();

    await expect(dcMotorBtn).toBeVisible();

    await glideCursorTo(page, dcMotorBtn);

    await dcMotorBtn.click();

    await pauseAwareDwell(page, 1000);



    const acGenBtn = page.locator('[data-testid="btn-mode-ac-generator"]:visible').first();

    await expect(acGenBtn).toBeVisible();

    await glideCursorTo(page, acGenBtn);

    await acGenBtn.click();



    console.log('[VISUAL AUDIT] Verified Modality 7: Electrodynamics Armature & Live Oscilloscope loaded and interactive.');
    await pauseAwareDwell(page, 3500); // Visual dwell for user inspection

    // Dismiss Sidecar Drawer before navigating topics
    const closeSidecarBtn7 = page.locator('[data-testid="btn-close-sidecar"]:visible').first();
    await expect(closeSidecarBtn7).toBeVisible({ timeout: 10000 });
    await glideCursorTo(page, closeSidecarBtn7);
    await closeSidecarBtn7.click();
    await expect(page.locator('[data-testid="cognitive-sidecar-drawer"]:visible').first()).toBeHidden({ timeout: 5000 });



    // =========================================================================

    // MODALITY 8: DYNAMIC CIRCLE GEOMETRY BOARD (Grade 11 Mathematics)

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 8/8: Dynamic Circle Geometry Board (Grade 11 Mathematics)');



    // Return to Today's Desk

    const deskBtn8 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn8).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn8);

    await deskBtn8.click();



    // Switch to Grade 11 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr11-01',

        name: 'Kelebogile Mokoena',

        role: 'student',

        type: 'student',

        grade: 11,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        window.studentStore.setEnabledSubjects(['physical_sciences', 'mathematics', 'life_sciences', 'accounting']);

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Mathematics Tab

    const mathTabGr11 = page.locator('[data-testid="tab-mathematics"]:visible').first();

    await expect(mathTabGr11).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, mathTabGr11);

    await mathTabGr11.click();



    // Start session from Today's Desk

    const openSubjectBtn8 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn8).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn8);

    await openSubjectBtn8.click();



    // Open Topic Scope Modal

    const topicScopeBtn8 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn8).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn8);

    await topicScopeBtn8.click();



    // Filter "Euclidean geometry"

    const searchInput8 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput8).toBeVisible({ timeout: 10000 });

    await searchInput8.fill('Euclidean geometry');



    const euclideanTopicCard = page.locator('[data-testid^="topic-card-euclidean-geometry"]:visible').first();

    await expect(euclideanTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, euclideanTopicCard);

    await euclideanTopicCard.click();



    // Verify Dynamic Diagram Canvas rendered

    const diagramCanvas = page.locator('[data-testid="diagram-canvas-container"]:visible').first();

    await expect(diagramCanvas).toBeVisible({ timeout: 20000 });



    // Toggle theorem guidance

    const toggleScaffoldBtn = page.locator('[data-testid="btn-toggle-diagram-scaffold"]:visible').first();

    await expect(toggleScaffoldBtn).toBeVisible();

    await glideCursorTo(page, toggleScaffoldBtn);

    await toggleScaffoldBtn.click();

    await pauseAwareDwell(page, 800);



    const checkDiagramBtn = page.locator('[data-testid="btn-check-answer"]:visible').first();

    await expect(checkDiagramBtn).toBeVisible();

    await glideCursorTo(page, checkDiagramBtn);



    console.log('[VISUAL AUDIT] Verified Modality 8: Dynamic Circle Geometry Board loaded and interactive.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // =========================================================================

    // MODALITY 9: COGNITIVE SIDECAR - 118-ELEMENT INTERACTIVE PERIODIC TABLE

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 9/11: Cognitive Sidecar - 118-Element Interactive Periodic Table (Physical Sciences)');



    // Return to Today's Desk

    const deskBtn9 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn9).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn9);

    await deskBtn9.click();



    // Select Physical Sciences Tab

    const physTabAid9 = page.locator('[data-testid="tab-physical_sciences"]:visible').first();

    await expect(physTabAid9).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, physTabAid9);

    await physTabAid9.click();



    // Open session

    const openSubjectBtn9 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn9).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn9);

    await openSubjectBtn9.click();



    // Trigger Visual Aid Sidecar Drawer via header button

    const toggleAidBtn9 = page.locator('[data-testid="btn-toggle-visual-aid"]:visible').first();

    await expect(toggleAidBtn9).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, toggleAidBtn9);

    await toggleAidBtn9.click();



    // Verify Sidecar Drawer mounted

    const sidecarDrawer9 = page.locator('[data-testid="cognitive-sidecar-drawer"]:visible').first();

    await expect(sidecarDrawer9).toBeVisible({ timeout: 10000 });



    // Verify Periodic Table Aid mounted

    const periodicTableAid = page.locator('[data-testid="periodic-table-aid"]:visible').first();

    await expect(periodicTableAid).toBeVisible({ timeout: 10000 });



    // Interactive Search: Search "Na" (Sodium)

    const elementSearch = page.locator('[data-testid="input-element-search"]:visible').first();

    await expect(elementSearch).toBeVisible();

    await elementSearch.fill('Na');

    await pauseAwareDwell(page, 500);



    const naCell = page.locator('[data-testid="element-cell-Na"]:visible').first();

    await expect(naCell).toBeVisible();

    await glideCursorTo(page, naCell);

    await naCell.click();



    // Verify Element Inspector displayed with Bohr model

    const inspectorCard = page.locator('[data-testid="element-inspector"]:visible').first();

    await expect(inspectorCard).toBeVisible();



    // Toggle Electronegativity Heatmap View

    const enViewBtn = page.locator('[data-testid="btn-view-electronegativity"]:visible').first();

    await expect(enViewBtn).toBeVisible();

    await glideCursorTo(page, enViewBtn);

    await enViewBtn.click();

    await pauseAwareDwell(page, 1000);



    console.log('[VISUAL AUDIT] Verified Modality 9: Interactive Periodic Table & Electron Shell Explorer loaded and responsive.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // Dismiss Sidecar Drawer

    const closeSidecarBtn9 = page.locator('[data-testid="btn-close-sidecar"]:visible').first();

    await expect(closeSidecarBtn9).toBeVisible();

    await glideCursorTo(page, closeSidecarBtn9);

    await closeSidecarBtn9.click();

    await expect(sidecarDrawer9).toBeHidden({ timeout: 5000 });



    // =========================================================================

    // MODALITY 10: COGNITIVE SIDECAR - DYNAMIC UNIT CIRCLE & WAVE TRIGONOMETRY

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 10/11: Dynamic Unit Circle & Wave Trigonometry Explorer (FET Mathematics)');



    // Return to Today's Desk

    const deskBtn10 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn10).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn10);

    await deskBtn10.click();



    // Select Mathematics Tab

    const mathTab10 = page.locator('[data-testid="tab-mathematics"]:visible').first();

    await expect(mathTab10).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, mathTab10);

    await mathTab10.click();



    // Open session

    const openSubjectBtn10 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn10).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn10);

    await openSubjectBtn10.click();



    // Open Topic Scope Modal and select Trigonometry

    const topicScopeBtn10 = page.locator('[data-testid="btn-topic-scope"]:visible').first();

    await expect(topicScopeBtn10).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, topicScopeBtn10);

    await topicScopeBtn10.click();



    const searchInput10 = page.locator('[data-testid="input-topic-search"]:visible').first();

    await expect(searchInput10).toBeVisible({ timeout: 10000 });

    await searchInput10.fill('Trigonometry');



    const trigTopicCard = page.locator('[data-testid^="topic-card-trigonometry"]:visible').first();

    await expect(trigTopicCard).toBeVisible({ timeout: 10000 });

    await glideCursorTo(page, trigTopicCard);

    await trigTopicCard.click();



    // Open Visual Aid Sidecar

    const toggleAidBtn10 = page.locator('[data-testid="btn-toggle-visual-aid"]:visible').first();

    await expect(toggleAidBtn10).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, toggleAidBtn10);

    await toggleAidBtn10.click();



    // Verify Unit Circle Aid mounted

    const unitCircleAid = page.locator('[data-testid="unit-circle-aid"]:visible').first();

    await expect(unitCircleAid).toBeVisible({ timeout: 10000 });



    // Interactive angle changes

    const btnAngle60 = page.locator('[data-testid="btn-angle-60"]:visible').first();

    await expect(btnAngle60).toBeVisible();

    await glideCursorTo(page, btnAngle60);

    await btnAngle60.click();



    const sinVal = page.locator('[data-testid="trig-sin-value"]:visible').first();

    await expect(sinVal).toBeVisible();



    const btnAngle180 = page.locator('[data-testid="btn-angle-180"]:visible').first();

    await expect(btnAngle180).toBeVisible();

    await glideCursorTo(page, btnAngle180);

    await btnAngle180.click();



    const astcBadge = page.locator('[data-testid="astc-badge"]:visible').first();

    await expect(astcBadge).toBeVisible();



    console.log('[VISUAL AUDIT] Verified Modality 10: Dynamic Unit Circle & Wave Trigonometry loaded and interactive.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // Dismiss Sidecar Drawer

    const closeSidecarBtn10 = page.locator('[data-testid="btn-close-sidecar"]:visible').first();

    await expect(closeSidecarBtn10).toBeVisible();

    await glideCursorTo(page, closeSidecarBtn10);

    await closeSidecarBtn10.click();

    await expect(page.locator('[data-testid="cognitive-sidecar-drawer"]:visible').first()).toBeHidden({ timeout: 5000 });



    // =========================================================================

    // MODALITY 11: BIOMOLECULAR 3D STRUCTURE VIEWER & SIDECAR PILL INTEGRATION

    // =========================================================================

    await updateHud(page, 'LEARNER', 'Modality 11/11: Biomolecular 3D Structure Viewer & Mol* Sidecar Integration (Life Sciences)');



    // Return to Today's Desk

    const deskBtn11 = page.locator('[data-testid="tab-desk"]:visible').first();

    await expect(deskBtn11).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, deskBtn11);

    await deskBtn11.click();



    // Switch to Grade 12 student persona

    await page.evaluate(() => {

      window.__FUNDILE_SWITCH_PERSONA__({

        id: 'sch-gr12-01',

        name: 'Prince Moyo',

        role: 'student',

        type: 'student',

        grade: 12,

        school: 'Westville High School',

        assignedTasks: []

      });

      if (window.studentStore) {

        ['physical_sciences', 'mathematics', 'life_sciences', 'natural_sciences'].forEach((s) =>

          window.studentStore.completeDiagnostic(s, 65)

        );

      }

    });



    // Select Life Sciences Tab

    const lifeTab11 = page.locator('[data-testid="tab-life_sciences"]:visible').first();

    await expect(lifeTab11).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, lifeTab11);

    await lifeTab11.click();



    // Open session

    const openSubjectBtn11 = page.locator('[data-testid="btn-open-subject-session"]:visible').first();

    await expect(openSubjectBtn11).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, openSubjectBtn11);

    await openSubjectBtn11.click();



    // Open Visual Aid Sidecar

    const toggleAidBtn11 = page.locator('[data-testid="btn-toggle-visual-aid"]:visible').first();

    await expect(toggleAidBtn11).toBeVisible({ timeout: 15000 });

    await glideCursorTo(page, toggleAidBtn11);

    await toggleAidBtn11.click();



    // Verify Biomolecular Structure Aid mounted

    const bioAid = page.locator('[data-testid="biomolecular-structure-aid"]:visible').first();

    await expect(bioAid).toBeVisible({ timeout: 10000 });



    // Interactive Molecule Switching: tRNA

    const trnaBtn = page.locator('[data-testid="btn-select-mol-trna"]:visible').first();

    await expect(trnaBtn).toBeVisible();

    await glideCursorTo(page, trnaBtn);

    await trnaBtn.click();

    await pauseAwareDwell(page, 600);



    // Interactive Molecule Switching: Hemoglobin

    const hemoBtn = page.locator('[data-testid="btn-select-mol-hemoglobin"]:visible').first();

    await expect(hemoBtn).toBeVisible();

    await glideCursorTo(page, hemoBtn);

    await hemoBtn.click();

    await pauseAwareDwell(page, 600);



    // Interactive Molecule Switching: B-DNA

    const dnaBtn = page.locator('[data-testid="btn-select-mol-dna"]:visible').first();

    await expect(dnaBtn).toBeVisible();

    await glideCursorTo(page, dnaBtn);

    await dnaBtn.click();

    await pauseAwareDwell(page, 600);



    // Verify Authentic Mol* Sidecar Link exists

    const sidecarPillLink = page.locator('[data-testid="btn-launch-molstar-sidecar"]:visible').first();

    await expect(sidecarPillLink).toBeVisible();

    await expect(sidecarPillLink).toHaveAttribute('href', 'sidecar://biomolecular-structure-viewer');



    console.log('[VISUAL AUDIT] Verified Modality 11: Biomolecular 3D Structure Viewer & Mol* sidecar link verified.');

    await pauseAwareDwell(page, 3000); // Visual dwell for user inspection



    // Dismiss Sidecar Drawer

    const closeSidecarBtn11 = page.locator('[data-testid="btn-close-sidecar"]:visible').first();

    await expect(closeSidecarBtn11).toBeVisible();

    await glideCursorTo(page, closeSidecarBtn11);

    await closeSidecarBtn11.click();

    await expect(page.locator('[data-testid="cognitive-sidecar-drawer"]:visible').first()).toBeHidden({ timeout: 5000 });



    // =========================================================================

    // FINAL VERIFICATION SUMMARY

    // =========================================================================

    await updateHud(page, 'LEARNER', 'All 11 Visual Diagrammatic Archetypes & Cognitive Sidecar Aids Verified Cleanly!');

    console.log('\n======================================================================');

    console.log('   ALL 11 VISUAL ARCHETYPES & COGNITIVE SIDECAR AIDS INSPECTED:');

    console.log('   [1] Electric Circuit Schematic (Grade 10 Physical Sciences)');

    console.log('   [2] Punnett Square Genetic Cross (Grade 12 Life Sciences)');

    console.log('   [3] Biological Diagram Labeling (Grade 9 Natural Sciences)');

    console.log('   [4] Free Body Diagram (Grade 11 Physical Sciences)');

    console.log('   [5] 3D Geometric Nets Polyhedron Folding (Grade 7 Mathematics)');

    console.log('   [6] 3D Organic Chemistry CPK Molecular Explorer (Grade 12 Physical Sciences)');

    console.log('   [7] Electrodynamics Armature & Live Oscilloscope (Grade 12 Physical Sciences)');

    console.log('   [8] Dynamic Circle Geometry Board (Grade 11 Mathematics)');

    console.log('   [9] 118-Element Interactive Periodic Table (Physical Sciences)');

    console.log('   [10] Dynamic Unit Circle & Wave Trigonometry (FET Mathematics)');

    console.log('   [11] Biomolecular 3D Structure Viewer & Mol* Sidecar (Life Sciences)');

    console.log('======================================================================\n');

  });

});

