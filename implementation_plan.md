# Science Diagram Elevation & Curriculum Topic Integration Implementation Plan

**Scope:** Natural Sciences (Gr 7–9), Life Sciences (Gr 10–12), and Physical Sciences (Gr 10–12).  
**Architectural Contract:**
1. **3-Layer Architecture:** High-resolution unlabelled visual plate (`/diagrams/*.jpg` / `*.svg`) + server-side anchor table (`caps-ai-backend/app/data/diagram_anchors/*.json`) + anti-leak randomized `ref` tokens (`ref_1`, `ref_2`) with zero DOM answer leakage.
2. **Topic-First Adaptive Sequencing:** Diagrams are never standalone silos; they are subskill builders imported into dedicated per-topic generators (`curriculum_docs_auto/`) and routed across Guided Scaffold (3-tier hints), Practice, and Timed Assessment.
3. **UI Invariants:** Single locked view per question card (`[data-testid="<diagram>-locked-view-badge"]`) + collision-free horizontal elbow leader lines to side-margin badges via `InteractiveCallouts.jsx`. Interactive multi-state exploration belongs exclusively to SimuLearn and `CognitiveSidecarDrawer.jsx`.
4. **Zero-Bundling Invariant (Rule 0d-13):** Ban multi-topic grab bags. Every curriculum topic has its dedicated generator.

---

## Milestone Status Overview

| Milestone | Target Scope | Core Master Components & Generators | Status |
| :--- | :--- | :--- | :---: |
| **Milestone 1** | **Human Heart & Double Circulation** | `HumanHeartSvg.jsx`, `heart.json`, `heart_generator.py`, `ns9_circulatory_respiratory_generator.py`, `ls10_transport_systems_animals_generator.py`, `CardiovascularAtlasAid.jsx` | **COMPLETED** |
| **Milestone 2** | **Human Organ Systems (Respiratory, Digestive, Excretory)** | `AlveolusGasExchangeSvg`, `HumanDigestiveSvg`, `IntestinalVillusSvg`, `HumanNephronSvg`<br>Dedicated generators: `ns9_digestive_system_generator`, `ls11_animal_nutrition_generator`, `ls11_gaseous_exchange_generator`, `ls11_excretion_humans_generator` | **COMPLETED** |
| **Milestone 3** | **Senses (Eye/Ear), Endocrine, Nervous & Reproduction** | `HumanEyeSvg`, `HumanEarSvg`, `EndocrineSystemSvg`, `MaleReproductiveSvg`, `FemaleReproductiveSvg`<br>Dedicated generators: `ls12_responding_environment_humans_generator`, `ls12_endocrine_homeostasis_generator`, `ls12_human_reproduction_generator`, `ns9_human_reproduction_generator` | **COMPLETED** |
| **Milestone 4** | **Cytology, Cell Division (Mitosis/Meiosis), DNA & Genetics** | `PlantCellSvg`, `AnimalCellSvg`, `MitosisStagesSvg`, `MeiosisCrossingOverSvg`<br>Dedicated generators: `ns9_cells_units_of_life_generator`, `ls10_plant_and_animal_cells_generator`, `ls10_cell_division_mitosis_generator`, `ls12_meiosis_generator` | **COMPLETED** |
| **Milestone 5** | **Plant Anatomy, Photosynthesis, Respiration & Ecology** | `PlantLeafSvg`<br>Dedicated generators: `ls10_support_transport_plants_generator`, `ls11_photosynthesis_generator`, `ls11_cellular_respiration_generator`, `ls10_biospheres_to_ecosystems_generator`, `ls11_population_ecology_generator`, `ls12_plant_responses_environment_generator` | **COMPLETED** |
| **Milestone 6** | **Natural Sciences Gr 7–9 Chemistry, Physics, Earth & Space** | `DistillationApparatusSvg`, `ParticleModelSvg`, `ElectricCircuitsNsSvg`, `SolarSystemEarthSpaceSvg`<br>Dedicated generators: `ns7_separating_mixtures_generator`, `ns7_acids_bases_neutrals_generator`, `ns8_particle_model_matter_generator`, `ns8_electric_circuits_generator`, `ns9_forces_electric_cells_generator`, `ns8_solar_system_seasons_generator` | **COMPLETED** |
| **Milestone 7** | **Physical Sciences Gr 10–12 FET Physics & Chemistry Extensions** | `TitrationApparatusSvg`, `GalvanicCellSvg`, `TransverseWaveSvg`, `DopplerEffectSvg`<br>Dedicated generators: `ps10_waves_sound_light_generator`, `ps11_acids_bases_stoichiometry_generator`, `ps12_electrochemistry_galvanic_generator`, `ps12_doppler_effect_generator`, `ps12_vertical_projectile_motion_generator` | **COMPLETED** |

---

## Detailed Completion Summary: Milestone 7 (Physical Sciences Gr 10–12)

### 1. Server-Side Anchor Files (`caps-ai-backend/app/data/diagram_anchors/`)
* `galvanic_cell.json`: Standard Daniell / Voltaic electrochemical cell setup (`viewBox="0 0 600 480"`).
  * 8 anchors: Anode electrode, cathode electrode, anode electrolyte ($1\text{ mol}\cdot\text{dm}^{-3}$ aqueous zinc sulphate), cathode electrolyte ($1\text{ mol}\cdot\text{dm}^{-3}$ aqueous copper sulphate), salt bridge ($KNO_3$ gel), voltmeter, electron flow path ($A \to B$), porous plug.
* `titration_apparatus.json`: Volumetric acid-base titration assembly (`viewBox="0 0 600 480"`).
  * 8 anchors: Graduated burette tube, liquid concave meniscus, retort stand & base, burette clamp, stopcock tap, delivery jet tip, conical flask with analyte, white contrast tile.
* `transverse_wave.json`: Sinusoidal transverse wave profile & displacement anatomy (`viewBox="0 0 600 480"`).
  * 8 anchors: Wave crest, wave trough, wave amplitude ($A$), wavelength ($\lambda$), equilibrium rest line, wave propagation vector, particle oscillation axis ($90^\circ$ perpendicular), consecutive in-phase crest.
* `doppler_effect.json`: Moving sound source wavefront compression and dilation (`viewBox="0 0 600 480"`).
  * 7 anchors: Moving sound source ($v_s$), compressed wavefronts ahead ($\lambda_L < \lambda_s, f_L > f_s$), stretched wavefronts behind ($\lambda_L > \lambda_s, f_L < f_s$), stationary observer ahead, stationary observer behind, source velocity vector, medium sound speed ($v$).

### 2. Subskill Builders & Dedicated Generators
* `physical_sciences_builders.py`: Modular subskill builders for Galvanic Cell, Titration Apparatus, Transverse Wave, and Doppler Effect. Emits anti-leak randomized `ref` tokens, collision-free margin callouts, and 3-tier hints.
* `ps10_waves_sound_light_generator.py`: PS Gr 10 Term 1 (Waves, sound and light: Transverse wave anatomy, wave equation $v = f \times \lambda$, sound echo timing $v = \frac{2d}{\Delta t}$, electromagnetic photon energy $E = h \times f = \frac{hc}{\lambda}$).
* `ps11_acids_bases_stoichiometry_generator.py`: PS Gr 11 Term 3 & Gr 12 Term 2 (Acids, bases and volumetric titrations: Titration apparatus visual scaffold, stoichiometry $\frac{c_a V_a}{c_b V_b} = \frac{n_a}{n_b}$, standard solutions, indicator selection).
* `ps12_electrochemistry_galvanic_generator.py`: PS Gr 12 Term 3 (Electrochemical reactions: Galvanic cell visual scaffold, standard cell potential $E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$, oxidation/reduction half-reactions, net cell equations, standard cell notation, salt bridge functions).
* `ps12_doppler_effect_generator.py`: PS Gr 12 Term 2 (The Doppler effect: Wavefront compression visual scaffold, approaching/receding formulas $f_L = \frac{v \pm v_L}{v \pm v_s} f_s$, astronomical redshift, medical ultrasound diagnostics).
* `ps12_vertical_projectile_motion_generator.py`: PS Gr 12 Term 1 (Vertical projectile motion in 1D: Ground-launch upward projectiles, cliff launch trajectories, apex time/height, kinematic graphs).

### 3. Frontend Component Elevation (`src/components/workspace/modalities/diagram_bank/`)
* `GalvanicCellSvg.jsx`: Standardized to `viewBox="0 0 600 480"`, stripped all baked text leaks ("Anode (-)", "Cathode (+)", "Zn", "Cu"), wired `InteractiveCallouts`, added locked view badge `[data-testid="galvanic-cell-locked-view-badge"]`.
* `TitrationApparatusSvg.jsx`: Standardized to `viewBox="0 0 600 480"`, stripped all baked text leaks, wired `InteractiveCallouts`, added locked view badge `[data-testid="titration-apparatus-locked-view-badge"]`.
* `TransverseWaveSvg.jsx`: Standardized to `viewBox="0 0 600 480"`, stripped all baked text leaks ("Crest 1", "Wavelength (λ)", "Amplitude (A)", "Rest Position"), wired `InteractiveCallouts`, added locked view badge `[data-testid="transverse-wave-locked-view-badge"]`.
* `DopplerEffectSvg.jsx`: Authored new component with standardized `viewBox="0 0 600 480"`, non-concentric spherical sound wavefronts, moving sound source, approaching and receding observers, wired `InteractiveCallouts`, locked view badge `[data-testid="doppler-effect-locked-view-badge"]`.
* `index.js`: Exported and registered all 4 components in `DIAGRAM_BANK`.

### 4. Verification Gate Results
* `scratch/run_physical_sciences_tests.py`: 4/4 test suites passed (anchor schema, anti-leak checks, dedicated generator execution, topic registry resolution).
* Holistic pre-flight gate (`npm run test:audit`):
  * Step 0: 288/288 generators intact (0 baseline deletions).
  * Step 1: 0 selector or privilege violations across all 38 Playwright specs.
  * Step 1b: 58 archetypes and 7 visual aids audited with 0 contract violations.
  * Step 1c: `diagrams.md` 386/386 items mapped with 0 gaps.
  * Step 2: 515 tests across 35 files discovered in 4.6s.
  * Step 3: DOM smoke check passed in 14.3s on `127.0.0.1:5173`.
* Manifest Synchronization: `fundile-architecture.json` updated with 5 new entries; `fundile-architecture.html` regenerated (348 KB).
