# Fundile Unified Visual Architecture & Workspace Direction (v2.0)
**Architectural Blueprint: Static Exam Precision, Merged Enhancement Companions, Multi-Scale Systems & Paper Folio Workspace**

---

## 1. Executive Directive: Eliminating Disjointedness Across All 30 Tracks

Fundile is an end-to-end curriculum learning engine across Senior Phase (Grades 7–9) and FET Phase (Grades 10–12), not a loose collection of disconnected widgets. To prevent visual, pedagogical, and cognitive fragmentation, the visual and workspace architecture is governed by four strict operational boundaries:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                FUNDILE UNIFIED VISUAL PIPELINE                              │
├──────────────────────────────────────────┬──────────────────────────────────────────────────┤
│           SURFACE 1: ASSESSMENT          │               SURFACE 2: REMEDIATION             │
│      (The Question Folio in Workspace)   │         (The Merged Enhancement Companion)       │
├──────────────────────────────────────────┼──────────────────────────────────────────────────┤
│ • 100% Static 2D Examination Diagrams.   │ • Single dedicated drawer per question archetype.│
│ • Locked to authentic South African exam │ • Tab 1: Static Fully Annotated Master Atlas.    │
│   presentation (clean textbook/stipple). │ • Tab 2: Live Process Simulation + SimuLearn 3D. │
│ • Strictly isolated question-specific    │ • Multi-scale zoom: Micro (Organelle/Alveolus)   │
│   callouts (only A, B if question tests  │   ↔ Macro (Organ System / Whole Circuit).        │
│   A, B; zero pins if role == 'context'). │ • Interactive parameter sliders, live micro-     │
│ • Never hijacks question modality into   │   physics, and formula calculation popovers.     │
│   edge-selection unless explicitly asked.│ • Stage-gated: Open in Scaffold/Practice;        │
│ • Paper-like workbook aesthetic (#FAF8F3)│   Locked to Official Data Sheet in Diagnostic/   │
│   with Charcoal (#1E2022) typography.    │   Exam Mode.                                     │
└──────────────────────────────────────────┴──────────────────────────────────────────────────┘
                                           ▲
                                           │ Powered by single production pipeline
                                           │
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                 SURFACE 3: THE OFFLINE STUDIO (Blender 5.2.3 MCP + SVG Engine)              │
│  • Modeled once in Blender 5.2.3 / Precision GeoGebra-Grade SVG.                            │
│  • Output A: Unlabeled 2D static plate for Question Folio (public/diagrams/*_exam.jpg/svg). │
│  • Output B: Fully annotated high-res reference plate for Companion Tab 1.                  │
│  • Output C: Lightweight .glb mesh / animated vector stream for Companion Tab 2.            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Pillar 1: Question Cards in Adaptive Progression (Static Exam Authentic Diagrams & Non-Hijacking Modality Contract)

### 2.1 The Two Problems Being Eradicated
1. **Annotation Leakage**: A Grade 7, 8, or 9 question asking only about the *Left Ventricle* (or using a distillation apparatus purely for context) displays a generic diagram with 4–8 permanent labels ($A$ through $H$) pointing to untested structures.
2. **Modality Hijacking**: Attaching a `diagram_spec` to a mathematical calculation, data-handling graph, or economics supply/demand question must **never** override the question's native input modality (`math_short`, `math_steps`, `semantic`, `mcq`, or `ledger`) into `diagram_select` edge-clicking mode. Similarly, multi-part answer dictionaries (`{"part_a": "...", "part_b": "..."}`) must render as lettered sub-part inputs `(a), (b)`, never as accounting ledger tables.

### 2.2 The Question-Dedicated Pin Isolation & Modality Preservation Standard
1. **100% Static & Exam-Authentic**: Question cards (Diagnostic, Scaffold, Practice, Exam) **never** run 3D simulations. South African examinations are administered on 2D paper; question cards reflect this with crisp, static 2D figures rendered **inside the Question Folio** immediately below the question text.
2. **Dynamic Pin Isolation (`tested_pins` & `diagram_role`)**:
   - The underlying plate in `public/diagrams/` is **100% unlabeled**.
   - When `diagram_role === "context"` (or `pins` is empty), **zero callout pins or letters** are rendered.
   - When `diagram_role === "identify"`, `InteractiveCallouts.jsx` dynamically renders **only the exact pin letters referenced by the active question seed** (e.g., if Seed 1 asks *"Identify part A and part B"*, only Pin A and Pin B appear).
3. **Cross-Grade Scope Isolation (`grade_mask`)**: Grade 7–9 Natural Sciences questions never expose FET-level histological pins (`g7`, `g8`, `g9` masks strictly filter `diagram_anchors/*.json`).
4. **Native Input Modality Preservation**:
   - A question is only routed to `question_type = "diagram_select"` when `question.correct_edge` is explicitly defined.
   - All other questions with `diagram_spec` retain their native `math`, `semantic`, `mcq`, or `ledger` input area in the Answer section while displaying their static 2D diagram in the Question Folio.

---

## 3. Pillar 2: Merging Visual Aids & SimuLearn into the "Archetype Enhancement Companion"

### 3.1 Unifying Fragmented Learning Aids
Previously, Fundile maintained two separate supplementary surfaces:
1. `CognitiveSidecarDrawer.jsx` (exploratory visual aid sandbox).
2. `SimuLearnPlayer.jsx` (step-by-step animated worked solution replay).

These two components are merged into a single, cohesive **Archetype Enhancement Companion** (a unified slide-out drawer accessible via an *"Explore Enhancement Companion"* button on the question card).

### 3.2 The Two-View Companion Architecture + Multi-Scale System Zoom

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  ENHANCEMENT COMPANION: Gaseous Exchange at the Alveolus (Gr 9 NS / Gr 11 Life Sciences)    │
│  [ 📖 Tab 1: Annotated Master Atlas ]     [ ⚡ Tab 2: Live Process & SimuLearn Replay ]     │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  TAB 1: ANNOTATED MASTER ATLAS (Static Full Reference + Micro-to-Macro System Zoom)         │
│  • High-resolution, comprehensive publication-grade anatomical, apparatus, or commercial    │
│    diagram with every constituent part permanently labeled.                                 │
│  • Multi-Scale System Zoom Toggle:                                                          │
│    [ 🔬 Micro View: Single Alveolus & Capillary ] ↔ [ 🫀 Macro View: Lungs & Heart Loop ]   │
│  • Expandable glossary defining curriculum functions and common exam traps for every part.  │
│                                                                                             │
│  TAB 2: LIVE PROCESS SIMULATION & CHOREOGRAPHED DERIVATION (How It Actually Works)          │
│  • Sub-mode A (Interactive Process Sandbox): Real-time 3D WebGL / SVG physics & biology     │
│    simulation (e.g. O₂/CO₂ partial-pressure diffusion across squamous epithelium, or        │
│    algebraic balance-scale / transposition slider).                                         │
│  • Sub-mode B (SimuLearn Worked Solution Replay): Pausable, reversible step-by-step         │
│    choreographed derivation of the exact active question seed with synchronized callouts.   │
│                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 Stage-Based Access Governance
- **Scaffold & Practice Modes**: Full access to both Tab 1 (Master Atlas) and Tab 2 (Live Process Simulation & SimuLearn Replay).
- **Diagnostic & Timed Exam Modes**: Exploratory simulations and worked replays are **locked**; learners may only open permitted **Official Exam Reference Sheets** (Periodic Table, Formula Sheet, Accounting Formats).

---

## 4. Pillar 3: Complete Modality Taxonomy Across All Subjects (Grades 7–12)

Visual assets are strictly partitioned by cognitive modality so every subject (Sciences, Mathematics, EMS, Accounting, Business Studies) renders in its authentic representation:

| Subject & Domain | Question Folio Static Diagram (Surface 1) | Companion Tab 1 (Master Atlas) | Companion Tab 2 (Live Process & SimuLearn) |
| :--- | :--- | :--- | :--- |
| **Physics: Kinematics, Forces & Waves** | Static $v\text{–}t$, $x\text{–}t$ graphs; Free Body Diagrams (FBD); ray diagrams; wave profiles. | Full vector resolution & ray landmark reference chart. | Interactive incline/vector scrubber ($mg\sin\theta, mg\cos\theta$), lens/mirror ray bench, and step-by-step formula derivation. |
| **Physics & NS: Electric Circuits & Grid** | Clean static IEC circuit schematic (cells, switches, bulbs, resistors, ammeters, voltmeters) or Sankey energy arrow diagram. | IEC Symbol Reference & National Grid step-up/step-down schematic (`Boiler → Turbine → Generator → Transformer`). | Interactive circuit elevation loop ($V = IR$, series vs parallel current split, geyser heating element / fuse trip simulation). |
| **Chemistry & NS: Matter, Atoms & Reactions** | Static Bohr atom model, particle state boxes, periodic table excerpt, distillation/filtration/electrolysis apparatus. | Annotated Lab Apparatus Atlas & Grade-Scoped Periodic Table (Metals / Metalloids / Non-metals). | Interactive KMT particle chamber (heating curve & phase transitions), acid-base litmus/pH indicator bench, and equation balancer. |
| **Biology & NS: Anatomy, Cells & Ecology** | Unlabeled textbook/stipple plate (`PlantCellSvg`, `HumanHeartSvg`, `DigestiveSystemSvg`, `FlowerAnatomySvg`, `FoodWebSvg`) with isolated pins. | Fully labeled medical/botanical master plate with **Micro ↔ Macro System Zoom** (e.g., Villus ↔ Digestive Tract; Alveolus ↔ Cardiopulmonary System). | Dynamic physiological process simulation (peristalsis, cardiac cycle, inhalation/exhalation pressure-volume mechanics) + SimuLearn. |
| **Earth & Astronomy (NS Gr 7–9)** | Static 2D diagram of Earth's 4 spheres, rock cycle, 23,5° axial tilt seasons, lunar phases/eclipses, SALT/MeerKAT telescopes, stellar lifecycle. | Annotated Earth & Space Reference Atlas (Troposphere–Thermosphere profile, Lithosphere strata, HR/Star lifecycle chart). | Interactive 3D/2D Orbital Seasons & Tides simulator, Rock Cycle pressure/cooling simulator, and Telescope light-path explorer. |
| **Mathematics: Number, Algebra & Patterns** | Visual matchstick/dot geometric sequences, flow diagrams (`Input → Rule → Output`), number lines, and vertical arithmetic grids. | Exponent laws, algebraic factorisation identities, and number system hierarchy ($\mathbb{N} \subset \mathbb{N}_0 \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$). | Interactive Number Line Hopper, Algebraic Balance & Transposition animator (`LHS = RHS`), and Pattern term-builder. |
| **Mathematics: Geometry, Measurement & Trig** | Crisp 2D Euclidean figures (parallel lines & transversals, congruent/similar triangles, circles, Cartesian transformations) & 3D wireframe/net solids with dimensions outside the shape. | Euclidean Theorem & Reason Reference Sheet (unabbreviated exam reasons) + 3D Polyhedra Net Atlas ($V - E + F = 2$). | Interactive transversal angle glider, 2D Circle/Triangle explorer, and 3D Hinged Net folding/unfolding simulator. |
| **Mathematics: Functions, Graphs & Data** | Plotted Cartesian linear/nonlinear graphs, bar graphs, double bar graphs, histograms, pie charts, scatter plots, 5-stroke SVG tally tables, probability spinners & tree diagrams. | Statistical Measures & Graph Type Reference Guide ($m = \frac{y_2-y_1}{x_2-x_1}$, dual-intercepts, $\theta = \frac{f}{N}\times 360^\circ$). | Interactive $y = mx + c$ gradient/intercept scrubber, Stem-and-Leaf / Frequency builder, and Probability Spinner/Tree simulator. |
| **EMS, Accounting & Business Studies** | Authentic Source Documents (Receipts, Till Slips, Invoices, Cheque Counterfoils, Bank Statements), Circular Flow diagrams, Supply & Demand Equilibrium graphs, Production Chains, and Transaction Stimulus Cards. | Accounting Cycle Blueprint (`Source Doc → Subsidiary Journal → General Ledger → Trial Balance → Financial Statements`) & Markup Formula Guide. | Cell-by-cell SimuLearn Journal/Ledger posting replay (`DEAD CLIC` / `A = OE + L` impact) and interactive Supply & Demand shift explorer. |

---

## 5. Pillar 4: The Atlas Paper-Like Question Workspace UI

### 5.1 Restrained Scope: Question Solving Surface Only
The archival paper aesthetic is applied **strictly to the problem-solving folio** inside `UniversalWorkspace.jsx`, leaving the global shell (Desktop Command Rail, Header, Teacher LMS, School Admin pacing desks) unchanged.

### 5.2 Key Design Principles of the Paper Folio
1. **Tactile Archival Quality**: The central solving surface uses an archival warm paper canvas (`#FAF8F3` / `#FDFBF7`) with warm stone borders (`#EAE5DC`) instead of sterile cool gray.
2. **Charcoal Typography**: Question prose and mathematical expressions are rendered in rich charcoal (`#1E2022`) for high contrast without harsh glare.
3. **Seamless Embedded Figures**: Question diagrams sit flush on the paper folio canvas on a clean `#FFFFFF` plate with subtle `#EAE5DC` framing, free of noisy headers or redundant badges.
4. **Color-Coded Semantic Term Binding**: In worked solutions, hints, and Companion replays, variables share the exact ink color of their diagram vectors/series (e.g., Demand / Primary vector in `#13519C`, Supply / Secondary vector in `#D97706`, Equilibrium / Resultant in `#059669`).

---

## 6. Pillar 5: Blender 5.2.3 MCP + Precision SVG Production Pipeline

1. **Category A (Organic Anatomy, 3D Lab Apparatus, Astronomical/Mechanical Cutaways)**: Modeled in Blender 5.2.3 (connected via MCP) or rendered as publication-grade medical/scientific plates:
   - Output A: Unlabeled static 2D plate (`public/diagrams/*_exam.jpg` or `.svg`) for the Question Folio.
   - Output B: Fully labeled Master Atlas plate for Companion Tab 1.
   - Output C: Interactive 3D `.glb` or multi-state vector simulation for Companion Tab 2.
2. **Category B (Analytical Graphs, Euclidean Geometry, Circuits, Economics Curves, Data Charts, Source Documents)**: Rendered via deterministic, high-precision parametric SVG components (`DiagramRenderer.jsx`, `StatsAndFinancialGraphRenderer.jsx`, `GeometryDiagramRenderer.jsx`, `CircuitModalityRenderer.jsx`) with zero pixelation at any zoom level.
