# Mathematical Literacy (Grades 10–12): Diagram & Cognitive Sidecar Remediation Plan (Rev 2)

## 1. Goal Description

Remediate the diagram, renderer-dispatch, schema-mismatch, prompt-narration, and visual-aid defects across Mathematical Literacy Grades 10–12 (36 topics, 1,871 archetypes) discovered by the audit and the follow-up code review:

1. **Preserve working banked diagrams & fix real `DiagramRenderer.jsx` drops**:
   - Keep `architectural_floor_packaging_plan` routed to [`ArchitecturalFloorPackagingPlanSvg.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/modalities/diagram_bank/ArchitecturalFloorPackagingPlanSvg.jsx) via `getBankedDiagramComponent` (do **not** alias it to `floor_plan`, which lacks the BIC `X`, door-swing arc, and Room C fixtures).
   - Fix [`DiagramRenderer.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/shared/mathx/DiagramRenderer.jsx) lines 987–1060 to dispatch on `effectiveKind` and pass `normalizedSpec` instead of raw `spec.kind` / `spec`, and remove the `Boolean(spec.type && !spec.kind)` hijack on line 1009 that sent `type: 'step_tariff'` to `FunctionGraph`.
   - Add a dedicated first-quadrant `cartesian_system` multi-line & piecewise plotter in [`MathLitDiagramRenderer.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/shared/mathx/MathLitDiagramRenderer.jsx) (handling `{ x_range, y_range, lines, points_of_interest, x_label, y_label }`) instead of aliasing `cartesian_system -> function_graph` (which drew a default parabola).
2. **Eliminate silent dummy-data fallbacks in [`StatsAndFinancialGraphRenderer.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/shared/mathx/StatsAndFinancialGraphRenderer.jsx) & [`GeoGebraGeometryRenderer.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/shared/mathx/GeoGebraGeometryRenderer.jsx)**:
   - Normalize generator schemas (`slices` → `sectors` on `pie_chart`, `steps` → `blocks` on `step_tariff`, `bars` / `series` → `categories` / `values` / `values2` on `bar_graph` / `double_bar_graph`, `summary` → `min, q1, median, q3, max` on `box_and_whisker`, and `boxplot` → `box_and_whisker`) so the SVG always renders the question's seeded numbers—never hardcoded `Cat A / Cat B` fallback values.
   - Replace the wrong `kind: 'function_flow'` on `gr11_fin_uif_piecewise_graph_interpretation` with a `cartesian_system` piecewise capped line graph showing the $(\text{R }12\,478;\text{ R }124{,}78)$ UIF ceiling.
3. **Unblock Cognitive Sidecar Visual Aids (`visualAidRegistry.js`)**:
   - Match `normSubject.includes('mathematical_literacy')` in [`visualAidRegistry.js`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/visual_aids/visualAidRegistry.js#L478) and register 3 dedicated Math Lit visual aids (`aid_mathlit_maps_and_plans`, `aid_mathlit_tariffs_and_taxation`, `aid_mathlit_measurement_and_packaging`).
4. **Remediate Missing Diagrams & Narrated Prompts (Diagram Description → Design Law, [`diagram_doctrine.md` §9](file:///c:/Users/princ/fundile-tlassistant-vite/diagram_doctrine.md#L183))**:
   - Across Grades 10, 11, and 12, wire seeded Approach B `diagram_spec` payloads for every `PROMPT_REFERENCES_FIGURE`, `DESCRIBED_NOT_DRAWN`, and `TEXT_SUBSTITUTED` archetype, **and rewrite the prompt prose** to refer to the figure (`"Use the map/plan/graph below…"`) without narrating the answer or layout dimensions in text.
5. **Fix the Audit Classifier (`scripts/run_mathlit_comprehensive_diagram_audit.py`)**:
   - Update Stage Classify to check the real `DiagramRenderer.jsx` dispatch + `diagram_bank` + required schema keys per kind, so `RENDERED` is only reported when both the renderer branch and the data fields are valid.

---

## 2. Autonomous Overnight Execution Mode (Owner-Authorized Continuous Run)

> [!IMPORTANT]
> **Continuous Overnight Execution Across All Subjects (`REM-0` $\rightarrow$ `REM-14` & `GP-0` $\rightarrow$ `GP-30`)**:
> Per owner authorization, the agent will execute batches **continuously without stopping for manual intervention** between batches, verifying each item with `python scripts/verify_plan.py` as it goes:
> - **Batch 1 (`REM-0` to `REM-3`) — COMPLETED (`PASS`)**: Audit referee lock + `DiagramRenderer.jsx` / `StatsAndFinancialGraphRenderer.jsx` / `MathLitDiagramRenderer.jsx` dispatch & schema normalization + `gr11_fin_uif_piecewise_graph_interpretation` fix + `visualAidRegistry.js` unblock & 3 Math Lit aids + live Playwright render audit.
> - **Batch 2 (`REM-4` to `REM-5`)**: Mathematical Literacy Grade 10 — Draw seeded `diagram_spec` payloads and rewrite narrated prompts across Maps/Plans/Scale (52), Assembly/Floor Plans/Packaging (25), Data Handling (11), Patterns/Tariffs (12), Probability (17), and Measurement/Numbers/Finance (10).
> - **Batch 3 (`REM-6`)**: Mathematical Literacy Grade 11 — Draw seeded `diagram_spec` payloads and rewrite narrated prompts across Plans & Representations (14), Maps (11), Finance/Tax/UIF (5), Data Handling & Patterns (7), and Exchange Rates/Interest/Weight/Probability (8).
> - **Batch 4 (`REM-7` to `REM-8`)**: Mathematical Literacy Grade 12 — Draw seeded `diagram_spec` payloads and rewrite narrated prompts across Plans & Scale (30), Maps & Models (21), Scale & Map Work (12), Data/Probability/Finance/Measurement (29) + regenerate full report/CSV + pass `npm run test:audit`.
> - **Batch 5 (`REM-9` to `REM-14` + `--plan gp`)**: Cross-Subject FET (Grades 10–12: Mathematics, Technical Mathematics, Physical Sciences, Life Sciences, Accounting, Business Studies) & Senior Phase (Grades 7–9: Mathematics, EMS, Natural Sciences) — Run `audit_diagram_description_leak.py --strict`, wire missing seeded `diagram_spec` / Heart Standard plates, rewrite narrated figure prompts, and complete remaining `GP-1` to `GP-30` items.

---

## 3. Proposed Changes

### Component 1: Frontend Dispatch, Schema Normalization & Sidecar Aids (Batch 1)

#### [MODIFY] [`src/components/workspace/shared/mathx/DiagramRenderer.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/shared/mathx/DiagramRenderer.jsx)
- Add `'boxplot': 'box_and_whisker'` to `kindAliases`; remove `'cartesian_system': 'function_graph'` so `cartesian_system` routes to `MathLitDiagramRenderer`.
- Add `'cartesian_system'` to `mathLitKinds`.
- Keep `getBankedDiagramComponent(bankedKey)` intact for `architectural_floor_packaging_plan`.
- On lines 987, 1003, 1015, and 1040, check `effectiveKind` instead of `spec.kind`, pass `normalizedSpec` instead of `spec`, and change line 1009 `Boolean(spec.type && !spec.kind)` to `Boolean(spec.params && spec.type && !effectiveKind)` so `type: 'step_tariff'` is not hijacked by `FunctionGraph`.

#### [MODIFY] [`src/components/workspace/shared/mathx/MathLitDiagramRenderer.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/shared/mathx/MathLitDiagramRenderer.jsx)
- Add a `kind === 'cartesian_system'` branch (`data-testid="mathlit-diagram-cartesian"`) that plots first-quadrant linear/piecewise series from `spec.lines` (`[{ label, points: [[x,y], ...] }]`), axis ranges `spec.x_range` / `spec.y_range`, axis titles `spec.x_label` / `spec.y_label`, and labeled `spec.points_of_interest` (`[{ x, y, label }]`).
- In `packaging_packing` / `packaging_cartons` and `2d_net` / `cube_net` helpers, accept `{ layout, highlight_face, solid }` from Gr 11 `plans_representations` in addition to `{ container, box }`.

#### [MODIFY] [`src/components/workspace/shared/mathx/StatsAndFinancialGraphRenderer.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/shared/mathx/StatsAndFinancialGraphRenderer.jsx)
- `BoxAndWhiskerSvg`: read `const bw = spec.box_and_whisker || spec.summary || spec;` and map `q2` → `median`.
- `StepTariffGraph`: accept `spec.steps` (`[{ label, rate / cost_per_unit, min, max }]`) in addition to `spec.blocks`.
- `BarAndHistogramSvg`: accept `spec.bars` (`[{ label, value }]`) and `spec.series` (`[{ name, data: [{ label, value }] }]`) in addition to `spec.categories` / `spec.values` / `spec.values2`.
- `PieChartSvg`: accept `spec.slices` (`[{ label, pct / percentage / value }]`) in addition to `spec.sectors`.

#### [MODIFY] [`src/components/workspace/visual_aids/visualAidRegistry.js`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/visual_aids/visualAidRegistry.js)
- Include `normSubject.includes('mathematical_literacy')` in the mathematics fallback branch.
- Register `aid_mathlit_maps_and_plans`, `aid_mathlit_tariffs_and_taxation`, and `aid_mathlit_measurement_and_packaging` backed by a new dual-tab companion component [`src/components/workspace/visual_aids/MathLitAtlasAid.jsx`](file:///c:/Users/princ/fundile-tlassistant-vite/src/components/workspace/visual_aids/MathLitAtlasAid.jsx) (Tab 1: Static Annotated Master Atlas; Tab 2: Interactive Tariff/Scale/Packaging Scrubber).

---

### Component 2: Grade 10, 11 & 12 Generator Diagram & Prompt Upgrades (Batches 2–4)

#### [MODIFY] Grade 10 Generators (`caps-ai-backend/app/utils/mathematical_literacy/`)
- `scale_maps/` (52 subskills): attach seeded `bar_scale`, `compass_rose`, `strip_map`, `grid_map`, `floor_plan`, or `seating_plan` `diagram_spec` and rewrite prompts to reference the figure without narrating answers.
- `assembly_packaging/` (25 missing subskills): attach seeded `floor_plan`, `elevation_view`, `packaging_packing`, `packaging_cartons`, or `cube_net` `diagram_spec`.
- `data_handling/` (11 missing) & `patterns_relationships/` (12 missing) & `probability/` (17 missing) & `measuring` / `perimeter_area` / `numbers`: attach seeded `histogram`, `bar_graph`, `double_bar_graph`, `pie_chart`, `box_and_whisker`, `step_tariff`, `break_even`, `cartesian_system`, `venn_3_sets`, `contingency_table_and_tree`, `probability_spinner`, `mensuration_2d`, or `mensuration_3d` `diagram_spec`.

#### [MODIFY] Grade 11 Generators (`caps-ai-backend/app/utils/mathematical_literacy/gr11_*`)
- `gr11_finance_tax/uif_calculations.py`: change `gr11_fin_uif_piecewise_graph_interpretation` from `kind: 'function_flow'` to `kind: 'cartesian_system'` with the two-segment UIF line `[(0, 0), (12478, 124.78), (25000, 124.78)]` and cap point `(12478, 124.78)`.
- `gr11_plans_representations/` (14 missing), `gr11_maps/` (11 missing, including rewriting `subskill_10` so the compass direction is read from the diagram rather than stated in prose), `gr11_data_handling/`, `gr11_patterns_relationships/`, `gr11_finance_tax/`, `gr11_weight_and_temperature_generator.py`, `gr11_probability_generator.py`.

#### [MODIFY] Grade 12 Generators (`caps-ai-backend/app/utils/mathematical_literacy/gr12_*`)
- `gr12_plans_and_scale/` (30 missing), `gr12_maps_and_plans_models/` (21 missing), `gr12_scale_and_map_work/` (12 missing), `gr12_interest_banking_inflation/` (8 missing), `gr12_probability/` (6 missing), `gr12_data_handling/` (5 missing), `gr12_measurement_lengths_perimeter_area_volume/` (5 missing), `gr12_measuring_weight_bmi_medicine_dosages/` (4 missing), and remaining prompt-reference items.

---

## 4. Plan Items & Exit Tests (`verify_plan.py --plan mathlit_remediation`)

| ID | Batch | Deliverable | Exit Test (must exit 0) |
|---|:---:|---|---|
| **REM-0** | 1 | Update `scripts/run_mathlit_comprehensive_diagram_audit.py` & `scripts/verify_plan.py` (`--plan mathlit_remediation`) so `RENDERED` requires both a real renderer branch and non-empty schema data keys | `python scripts/verify_plan.py --plan mathlit_remediation --list` exits 0 and lists `REM-0` to `REM-8` |
| **REM-1** | 1 | Fix `DiagramRenderer.jsx`, `MathLitDiagramRenderer.jsx` (`cartesian_system`, net layouts), `StatsAndFinancialGraphRenderer.jsx` (`slices`/`steps`/`bars`/`series`/`summary`), and `gr11_fin_uif_piecewise_graph_interpretation` | `python scripts/run_mathlit_comprehensive_diagram_audit.py --stage classify` reports `GENERATED_NOT_RENDERED == 0` and all 24 existing diagram archetypes pass schema validation with 0 dummy fallbacks |
| **REM-2** | 1 | Unblock `visualAidRegistry.js` for `mathematical_literacy` and add 3 dedicated Math Lit visual aids (`MathLitAtlasAid.jsx`) | `node scripts/resolve_mathlit_aids.mjs` reports `NONE == 0` and `DEDICATED > 0` across 1,871 archetypes |
| **REM-3** | 1 | Live browser render check for all repaired Batch 1 diagram kinds (`architectural_floor_packaging_plan`, `cartesian_system`, `step_tariff`, `box_and_whisker`, `bar_chart`, `double_bar_chart`, `pie_chart`, `2d_net`, `cube_net`) | `npx playwright test e2e/visual/mathlit_diagram_render_audit.spec.js --project=desktop-browser` exits 0 with 0 console errors |
| **REM-4** | 2 | Grade 10 Maps & Plans (`scale_maps_and_plans`, `assembly_diagrams_floor_plans_packaging`) — 77 missing diagrams wired + narrated prompts rewritten | `python scripts/run_mathlit_comprehensive_diagram_audit.py --stage harvest --stage classify` shows 0 `MISSING` and 0 `DESCRIBED_NOT_DRAWN` in Gr 10 Maps/Plans/Assembly across seeds 101–103 |
| **REM-5** | 2 | Grade 10 Data, Patterns, Probability & Measurement — remaining 50 Gr 10 missing diagrams wired + narrated prompts rewritten | Audit shows 0 `MISSING` and 0 `PROMPT_REFERENCES_FIGURE` leaks across all 12 Grade 10 topics (623 archetypes) |
| **REM-6** | 3 | Grade 11 all 12 topics — 45 missing diagrams wired + narrated prompts (including `gr11_maps` `subskill_10`) rewritten | Audit shows 0 `MISSING` and 0 `PROMPT_REFERENCES_FIGURE` leaks across all 12 Grade 11 topics (624 archetypes) |
| **REM-7** | 4 | Grade 12 all 12 topics — 92 missing diagrams wired + narrated prompts rewritten | Audit shows 0 `MISSING` and 0 `PROMPT_REFERENCES_FIGURE` leaks across all 12 Grade 12 topics (624 archetypes) |
| **REM-8** | 4 | Regenerate `reports/mathlit_gr10_to_12_diagram_and_archetype_audit_report.md` & CSV, run Playwright render audit across Gr 10–12, and pass full pre-flight gate | `python scripts/generate_mathlit_comprehensive_report.py`, `npx playwright test e2e/visual/mathlit_diagram_render_audit.spec.js --project=desktop-browser`, and `npm run test:audit` all exit 0 |
| **REM-9** | 5 | FET Mathematics (Grades 10–12) — wire missing `diagram_spec` payloads & rewrite narrated figure prompts | `python scripts/audit_diagram_description_leak.py --subject Mathematics --grades 10 11 12 --seeds 101 102 103 --strict` exits 0 |
| **REM-10** | 5 | FET Technical Mathematics (Grades 10–12) — wire missing `diagram_spec` payloads & rewrite narrated figure prompts | `python scripts/audit_diagram_description_leak.py --subject "Technical Mathematics" --grades 10 11 12 --seeds 101 102 103 --strict` exits 0 |
| **REM-11** | 5 | FET Physical Sciences (Grades 10–12) — wire missing `diagram_spec` payloads & rewrite narrated figure prompts | `python scripts/audit_diagram_description_leak.py --subject "Physical Sciences" --grades 10 11 12 --seeds 101 102 103 --strict` exits 0 |
| **REM-12** | 5 | FET Life Sciences (Grades 10–12) — wire missing `diagram_spec` / Heart Standard plates & rewrite narrated figure prompts | `python scripts/audit_diagram_description_leak.py --subject "Life Sciences" --grades 10 11 12 --seeds 101 102 103 --strict` exits 0 |
| **REM-13** | 5 | FET Accounting & Business Studies (Grades 10–12) — wire missing diagram/table stimuli & eliminate narrated figure leaks | `python scripts/audit_diagram_description_leak.py --subject Accounting --grades 10 11 12 --strict` and `--subject "Business Studies"` both exit 0 |
| **REM-14** | 5 | Senior Phase (Grades 7–9 Mathematics, EMS, Natural Sciences) — wire missing `diagram_spec` / plates & eliminate narrated figure leaks (+ `--plan gp`) | `python scripts/audit_diagram_description_leak.py --grades 7 8 9 --seeds 101 102 103 --strict` exits 0 across Maths, EMS, and Natural Sciences |
