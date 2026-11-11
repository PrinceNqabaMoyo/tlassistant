# Fundile Science Diagrams — Playwright Visual Testing & Inspection Playbook

This document is the official execution playbook for interactively inspecting and validating every science diagram across **Milestones 1 through 7**.

Every test runs in **Headed Mode** using the Fundile Autopilot gliding cursor and HUD. You can watch the real UI render, observe pin interactions, review pre-baked hints, and verify MCQ answering.

> [!TIP]
> **Live Human Pause Control (SPACEBAR)**:
> While any headed test is running in the browser, press the **SPACEBAR** or **P** key at any moment to **PAUSE** the autopilot. The HUD will indicate `[PAUSED]`. You can freely inspect the diagram, zoom in, click pins, examine leader lines, and check stipple dot shading. Press **SPACEBAR** again to resume playback.

---

## Quick Reference Table: Individual Diagram Commands

Run any single diagram on demand using the exact command below.

| Milestone | Diagram Master Key | Diagram Title | Subject & Grade | Headed Inspection Command |
| :--- | :--- | :--- | :--- | :--- |
| **M1** | `human_heart` | Mammalian Heart Coronal Section | Gr 9 NS / Gr 10 Life Sci | `npx playwright test e2e/visual/human_heart_textbook.spec.js --project=fundile-autopilot --headed` |
| **M2** | `alveolus_gas_exchange` | Alveolus & Pulmonary Capillary Diffusion | Gr 11 Life Sci (Gaseous Exchange) | `npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "alveolus_gas_exchange"` |
| **M2** | `digestive_system` | Human Alimentary Canal & Digestive System | Gr 9 NS / Gr 11 Life Sci | `npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "digestive_system"` |
| **M2** | `intestinal_villus` | Intestinal Villus Histology & Absorption | Gr 11 Life Sci (Animal Nutrition) | `npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "intestinal_villus"` |
| **M2** | `human_nephron` | Renal Nephron Ultrastructure & Filtration | Gr 11 Life Sci (Excretion in Humans) | `npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "human_nephron"` |
| **M2** | `reference_atlas` | Milestone 2 Reference Atlas Multi-View | Gr 11 Life Sciences | `npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed -g "reference_atlas"` |
| **M3** | `human_eye` | Longitudinal Section of Human Eye | Gr 12 Life Sci (Sensory Organs) | `npx playwright test e2e/visual/milestone3_sensory_endocrine.spec.js --project=fundile-autopilot --headed -g "human_eye"` |
| **M3** | `human_ear` | Coronal Anatomy of Human Ear | Gr 12 Life Sci (Hearing & Balance) | `npx playwright test e2e/visual/milestone3_sensory_endocrine.spec.js --project=fundile-autopilot --headed -g "human_ear"` |
| **M3** | `endocrine_system` | Human Endocrine Glands & Hormones | Gr 12 Life Sci (Endocrine Control) | `npx playwright test e2e/visual/milestone3_sensory_endocrine.spec.js --project=fundile-autopilot --headed -g "endocrine_system"` |
| **M3** | `reference_atlas_m3` | Milestone 3 Reference Atlas Multi-View | Gr 12 Life Sciences | `npx playwright test e2e/visual/milestone3_sensory_endocrine.spec.js --project=fundile-autopilot --headed -g "reference_atlas"` |
| **M4** | `male_reproductive` | Male Reproductive System Anatomy | Gr 9 NS / Gr 12 Life Sci | `npx playwright test e2e/visual/milestone4_reproduction.spec.js --project=fundile-autopilot --headed -g "male_reproductive"` |
| **M4** | `female_reproductive` | Female Reproductive System Anatomy | Gr 9 NS / Gr 12 Life Sci | `npx playwright test e2e/visual/milestone4_reproduction.spec.js --project=fundile-autopilot --headed -g "female_reproductive"` |
| **M4** | `meiosis_crossing_over` | Meiosis Prophase I Crossing-Over | Gr 12 Life Sci (Meiosis) | `npx playwright test e2e/visual/milestone4_reproduction.spec.js --project=fundile-autopilot --headed -g "meiosis_crossing_over"` |
| **M5** | `plant_cell` | Plant Cell Eukaryotic Ultrastructure | Gr 9 NS / Gr 10 Life Sci | `npx playwright test e2e/visual/milestone5_cells_histology.spec.js --project=fundile-autopilot --headed -g "plant_cell"` |
| **M5** | `animal_cell` | Animal Cell Eukaryotic Ultrastructure | Gr 9 NS / Gr 10 Life Sci | `npx playwright test e2e/visual/milestone5_cells_histology.spec.js --project=fundile-autopilot --headed -g "animal_cell"` |
| **M5** | `mitosis_stages` | Stages of Mitotic Cell Division | Gr 10 Life Sci (Cell Division) | `npx playwright test e2e/visual/milestone5_cells_histology.spec.js --project=fundile-autopilot --headed -g "mitosis_stages"` |
| **M5** | `plant_leaf` | Dicotyledonous Leaf Cross-Section | Gr 10 Life Sci (Plant Tissues) | `npx playwright test e2e/visual/milestone5_cells_histology.spec.js --project=fundile-autopilot --headed -g "plant_leaf"` |
| **M6** | `distillation_apparatus`| Simple Distillation Laboratory Apparatus | Gr 7 NS (Separating Mixtures) | `npx playwright test e2e/visual/milestone6_physical_chemistry.spec.js --project=fundile-autopilot --headed -g "distillation_apparatus"` |
| **M6** | `titration_apparatus` | Volumetric Acid-Base Titration Setup | Gr 11 Physical Sciences | `npx playwright test e2e/visual/milestone6_physical_chemistry.spec.js --project=fundile-autopilot --headed -g "titration_apparatus"` |
| **M6** | `galvanic_cell` | Galvanic Daniell Electrochemical Cell | Gr 12 Physical Sciences | `npx playwright test e2e/visual/milestone6_physical_chemistry.spec.js --project=fundile-autopilot --headed -g "galvanic_cell"` |
| **M7** | `solar_system_earth_space` | Solar System & Planetary Orbits | Gr 8 NS (Earth & Space) | `npx playwright test e2e/visual/milestone7_physics_astronomy.spec.js --project=fundile-autopilot --headed -g "solar_system_earth_space"` |
| **M7** | `particle_model` | Particle Model of Matter (Solid/Liq/Gas)| Gr 8 NS (Matter & Materials) | `npx playwright test e2e/visual/milestone7_physics_astronomy.spec.js --project=fundile-autopilot --headed -g "particle_model"` |

---

## Batch Milestone Commands

To run all diagrams in a milestone sequentially:

### Milestone 1: Mammalian Heart
```powershell
npx playwright test e2e/visual/human_heart_textbook.spec.js --project=fundile-autopilot --headed
```

### Milestone 2: Human Organ Systems (Alveolus, Digestive, Villus, Nephron)
```powershell
npx playwright test e2e/visual/milestone2_human_organs.spec.js --project=fundile-autopilot --headed
```

### Milestone 3: Sensory Organs & Endocrine System (Eye, Ear, Endocrine)
```powershell
npx playwright test e2e/visual/milestone3_sensory_endocrine.spec.js --project=fundile-autopilot --headed
```

### Milestone 4: Reproductive Systems & Meiosis (Male Repro, Female Repro, Meiosis Crossing Over)
```powershell
npx playwright test e2e/visual/milestone4_reproduction.spec.js --project=fundile-autopilot --headed
```

### Milestone 5: Cell Biology & Histology (Plant Cell, Animal Cell, Mitosis Stages, Dicot Leaf)
```powershell
npx playwright test e2e/visual/milestone5_cells_histology.spec.js --project=fundile-autopilot --headed
```

---

## Diagram Architecture Standards & Verification Criteria

When viewing each diagram in the browser, verify the following 5 criteria:

1. **Unlabeled High-Res Visual Plates (Rule 0d-14.1)**:
   - Base illustration must sit on pure white `#FFFFFF` background.
   - Zero baked text, numbers, pointer arrows, or letters inside the image itself.
   - Smooth Campbell/OpenStax 3D shading in Textbook view; crisp pen-and-ink stipple dot shading in Exam view.
2. **Single Locked View Badge in Question Mode (Rule 0d-14.2)**:
   - Question cards must show a clean locked badge (e.g., `[data-testid="nephron-locked-view-badge"]`) indicating the view and grade.
   - Zero student-facing view switcher buttons in question mode.
3. **Collision-Free Horizontal Elbow Callouts (Rule 0d-14.3)**:
   - Dynamic pins (`A`, `B`, `C`, `D`) must use horizontal elbow lines with side margin badges at `x=60` (left) or `x=540` (right).
   - The red anchor circle must terminate dead-center on the target anatomical structure.
4. **Anti-Leak Security Contract (Rule 0d-14.4)**:
   - No structure answer names may appear in DOM text nodes prior to student submission.
   - Selecting a pin displays: `"Pin X: Active target pin selected for response"`.
5. **Adaptive Progression Lifecycle**:
   - **Diagnostic**: Initial mastery benchmark.
   - **Scaffold**: Pre-baked 3-tier hints appear when requested (`[data-testid="btn-toggle-hints"]`).
   - **Practice**: Interactive MCQ option selection (`[data-testid="btn-math-option-0"]`).
   - **Reference Atlas**: Multi-view toggle (`Textbook Master` vs `Exam Paper`) accessible in visual aid drawer.

---

## File Locations on Disk

### Milestone 1 (Mammalian Heart)
- **Component**: `src/components/workspace/modalities/diagram_bank/HumanHeartSvg.jsx`
- **Textbook Plate**: `public/diagrams/generated_textbook_heart_coronal.jpg`
- **Exam Plate**: `public/diagrams/generated_exam_heart_stipple.jpg`
- **Flow Plate**: `public/diagrams/wapcaplet_clean.svg`
- **Anchor Manifest**: `caps-ai-backend/app/data/diagram_anchors/heart.json`

### Milestone 2 (Human Organs)
- **Alveolus Gas Exchange**:
  - Component: `src/components/workspace/modalities/diagram_bank/AlveolusGasExchangeSvg.jsx`
  - Textbook Plate: `public/diagrams/alveolus_textbook.jpg`
  - Exam Plate: `public/diagrams/alveolus_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/alveolus_gas_exchange.json`
- **Human Digestive System**:
  - Component: `src/components/workspace/modalities/diagram_bank/HumanDigestiveSvg.jsx`
  - Textbook Plate: `public/diagrams/digestive_textbook.jpg`
  - Exam Plate: `public/diagrams/digestive_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/digestive_system.json`
- **Intestinal Villus Histology**:
  - Component: `src/components/workspace/modalities/diagram_bank/IntestinalVillusSvg.jsx`
  - Textbook Plate: `public/diagrams/villus_textbook.jpg`
  - Exam Plate: `public/diagrams/villus_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/intestinal_villus.json`
- **Human Nephron Ultrastructure**:
  - Component: `src/components/workspace/modalities/diagram_bank/HumanNephronSvg.jsx`
  - Textbook Plate: `public/diagrams/nephron_textbook.jpg`
  - Exam Plate: `public/diagrams/nephron_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/human_nephron.json`

### Milestone 3 (Sensory Organs & Endocrine System)
- **Human Eye Longitudinal Section**:
  - Component: `src/components/workspace/modalities/diagram_bank/HumanEyeSvg.jsx`
  - Textbook Plate: `public/diagrams/human_eye_textbook.jpg`
  - Exam Plate: `public/diagrams/human_eye_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/human_eye.json`
- **Human Ear Coronal Anatomy**:
  - Component: `src/components/workspace/modalities/diagram_bank/HumanEarSvg.jsx`
  - Textbook Plate: `public/diagrams/human_ear_textbook.jpg`
  - Exam Plate: `public/diagrams/human_ear_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/human_ear.json`
- **Human Endocrine System**:
  - Component: `src/components/workspace/modalities/diagram_bank/EndocrineSystemSvg.jsx`
  - Textbook Plate: `public/diagrams/endocrine_system_textbook.jpg`
  - Exam Plate: `public/diagrams/endocrine_system_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/endocrine_system.json`

### Milestone 4 (Reproductive Systems & Meiosis)
- **Male Reproductive System (Sagittal Section)**:
  - Component: `src/components/workspace/modalities/diagram_bank/MaleReproductiveSvg.jsx`
  - Textbook Plate: `public/diagrams/male_reproductive_textbook.jpg`
  - Exam Plate: `public/diagrams/male_reproductive_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/male_reproductive.json`
- **Female Reproductive System (Coronal Section)**:
  - Component: `src/components/workspace/modalities/diagram_bank/FemaleReproductiveSvg.jsx`
  - Textbook Plate: `public/diagrams/female_reproductive_textbook.jpg`
  - Exam Plate: `public/diagrams/female_reproductive_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/female_reproductive.json`
- **Meiosis Prophase I Crossing-Over & Chiasma**:
  - Component: `src/components/workspace/modalities/diagram_bank/MeiosisCrossingOverSvg.jsx`
  - Textbook Plate: `public/diagrams/meiosis_crossing_over_textbook.jpg`
  - Exam Plate: `public/diagrams/meiosis_crossing_over_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/meiosis_crossing_over.json`

### Milestone 5 (Cell Biology & Histology)
- **Plant Cell Eukaryotic Ultrastructure**:
  - Component: `src/components/workspace/modalities/diagram_bank/PlantCellSvg.jsx`
  - Textbook Plate: `public/diagrams/plant_cell_textbook.jpg`
  - Exam Plate: `public/diagrams/plant_cell_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/plant_cell.json`
- **Animal Cell Eukaryotic Ultrastructure**:
  - Component: `src/components/workspace/modalities/diagram_bank/AnimalCellSvg.jsx`
  - Textbook Plate: `public/diagrams/animal_cell_textbook.jpg`
  - Exam Plate: `public/diagrams/animal_cell_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/animal_cell.json`
- **Mitosis Stages (Somatic Cell Division 2n = 4)**:
  - Component: `src/components/workspace/modalities/diagram_bank/MitosisStagesSvg.jsx`
  - Textbook Plate: `public/diagrams/mitosis_stages_textbook.jpg`
  - Exam Plate: `public/diagrams/mitosis_stages_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/mitosis_stages.json`
- **Dicotyledonous Leaf Transverse Cross-Section**:
  - Component: `src/components/workspace/modalities/diagram_bank/PlantLeafSvg.jsx`
  - Textbook Plate: `public/diagrams/plant_leaf_textbook.jpg`
  - Exam Plate: `public/diagrams/plant_leaf_exam_stipple.jpg`
  - Anchor Manifest: `caps-ai-backend/app/data/diagram_anchors/plant_leaf.json`
