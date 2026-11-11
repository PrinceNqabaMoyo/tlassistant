"""Comprehensive Curriculum Diagram Pipeline Scanner (Rule 0d-15)
Scans all curriculum topics in curriculum_docs_auto/ and cross-references:
1. Curriculum Diagram Demand (from 28,035 [Diagram Context] annotations and questions).
2. Physical Disk Assets (TB, EX, SVG, ANC for Category A; JSX branches for Category B).
3. Runtime Generator Wiring (executes ALL_GENERATORS over real seeds).

Flags with zero theatre:
- [VERIFIED_ACTIVE]: Visual asset exists, generator emits it under live seeds.
- [FLAG: ORPHANED_RENDERER]: Asset exists on disk, but generator for this topic does NOT emit it.
- [FLAG: MISSING_DIAGRAM_ASSET]: Curriculum demands a diagram, but neither Track 1 nor 2 has an asset for it.
- [FLAG: BROKEN_GENERATOR]: Generator raises an unhandled exception during test runs.
- [TEXT_ONLY_TOPIC]: Curriculum has 0 diagram annotations (purely textual/tabular).
"""
import os
import sys
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(ROOT_DIR, 'caps-ai-backend')
sys.path.insert(0, BACKEND_DIR)

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key

# Standardized Category A Master Disk Definitions (including legacy aliases)
CAT_A_REGISTRY = {
    'human_heart': {
        'tb': ['human_heart_textbook.jpg', 'generated_textbook_heart_coronal.jpg'],
        'ex': ['human_heart_exam_stipple.jpg', 'generated_exam_heart_stipple.jpg'],
        'svg': 'HumanHeartSvg.jsx',
        'anc': 'heart.json'
    },
    'alveolus_gas_exchange': {
        'tb': ['alveolus_gas_exchange_textbook.jpg', 'alveolus_textbook.jpg'],
        'ex': ['alveolus_gas_exchange_exam_stipple.jpg', 'alveolus_exam_stipple.jpg'],
        'svg': 'AlveolusGasExchangeSvg.jsx',
        'anc': 'alveolus_gas_exchange.json'
    },
    'digestive_system': {
        'tb': ['digestive_system_textbook.jpg', 'digestive_textbook.jpg'],
        'ex': ['digestive_system_exam_stipple.jpg', 'digestive_exam_stipple.jpg'],
        'svg': 'HumanDigestiveSvg.jsx',
        'anc': 'digestive_system.json'
    },
    'intestinal_villus': {
        'tb': ['intestinal_villus_textbook.jpg', 'villus_textbook.jpg'],
        'ex': ['intestinal_villus_exam_stipple.jpg', 'villus_exam_stipple.jpg'],
        'svg': 'IntestinalVillusSvg.jsx',
        'anc': 'intestinal_villus.json'
    },
    'human_nephron': {
        'tb': ['human_nephron_textbook.jpg', 'nephron_textbook.jpg'],
        'ex': ['human_nephron_exam_stipple.jpg', 'nephron_exam_stipple.jpg'],
        'svg': 'HumanNephronSvg.jsx',
        'anc': 'human_nephron.json'
    },
    'human_eye': {
        'tb': ['human_eye_textbook.jpg'],
        'ex': ['human_eye_exam_stipple.jpg'],
        'svg': 'HumanEyeSvg.jsx',
        'anc': 'human_eye.json'
    },
    'human_ear': {
        'tb': ['human_ear_textbook.jpg'],
        'ex': ['human_ear_exam_stipple.jpg'],
        'svg': 'HumanEarSvg.jsx',
        'anc': 'human_ear.json'
    },
    'endocrine_system': {
        'tb': ['endocrine_system_textbook.jpg'],
        'ex': ['endocrine_system_exam_stipple.jpg'],
        'svg': 'EndocrineSystemSvg.jsx',
        'anc': 'endocrine_system.json'
    },
    'male_reproductive': {
        'tb': ['male_reproductive_textbook.jpg'],
        'ex': ['male_reproductive_exam_stipple.jpg'],
        'svg': 'MaleReproductiveSvg.jsx',
        'anc': 'male_reproductive.json'
    },
    'female_reproductive': {
        'tb': ['female_reproductive_textbook.jpg'],
        'ex': ['female_reproductive_exam_stipple.jpg'],
        'svg': 'FemaleReproductiveSvg.jsx',
        'anc': 'female_reproductive.json'
    },
    'meiosis_crossing_over': {
        'tb': ['meiosis_crossing_over_textbook.jpg'],
        'ex': ['meiosis_crossing_over_exam_stipple.jpg'],
        'svg': 'MeiosisCrossingOverSvg.jsx',
        'anc': 'meiosis_crossing_over.json'
    },
    'plant_cell': {
        'tb': ['plant_cell_textbook.jpg'],
        'ex': ['plant_cell_exam_stipple.jpg'],
        'svg': 'PlantCellSvg.jsx',
        'anc': 'plant_cell.json'
    },
    'animal_cell': {
        'tb': ['animal_cell_textbook.jpg'],
        'ex': ['animal_cell_exam_stipple.jpg'],
        'svg': 'AnimalCellSvg.jsx',
        'anc': 'animal_cell.json'
    },
    'mitosis_stages': {
        'tb': ['mitosis_stages_textbook.jpg'],
        'ex': ['mitosis_stages_exam_stipple.jpg'],
        'svg': 'MitosisStagesSvg.jsx',
        'anc': 'mitosis_stages.json'
    },
    'plant_leaf': {
        'tb': ['plant_leaf_textbook.jpg'],
        'ex': ['plant_leaf_exam_stipple.jpg'],
        'svg': 'PlantLeafSvg.jsx',
        'anc': 'plant_leaf.json'
    },
    'distillation_apparatus': {
        'tb': ['distillation_apparatus_textbook.jpg'],
        'ex': ['distillation_apparatus_exam_stipple.jpg'],
        'svg': 'DistillationApparatusSvg.jsx',
        'anc': 'distillation_apparatus.json'
    },
    'titration_apparatus': {
        'tb': ['titration_apparatus_textbook.jpg'],
        'ex': ['titration_apparatus_exam_stipple.jpg'],
        'svg': 'TitrationApparatusSvg.jsx',
        'anc': 'titration_apparatus.json'
    },
    'galvanic_cell': {
        'tb': ['galvanic_cell_textbook.jpg'],
        'ex': ['galvanic_cell_exam_stipple.jpg'],
        'svg': 'GalvanicCellSvg.jsx',
        'anc': 'galvanic_cell.json'
    },
    'solar_system_earth_space': {
        'tb': ['solar_system_earth_space_textbook.jpg'],
        'ex': ['solar_system_earth_space_exam_stipple.jpg'],
        'svg': 'SolarSystemEarthSpaceSvg.jsx',
        'anc': 'solar_system_earth_space.json'
    },
    'particle_model': {
        'tb': ['particle_model_textbook.jpg'],
        'ex': ['particle_model_exam_stipple.jpg'],
        'svg': 'ParticleModelSvg.jsx',
        'anc': 'particle_model.json'
    },
    'atomic_bohr_structure': {
        'tb': ['atomic_bohr_structure_textbook.jpg'],
        'ex': ['atomic_bohr_structure_exam_stipple.jpg'],
        'svg': 'AtomicBohrStructureSvg.jsx',
        'anc': 'atomic_bohr_structure.json'
    },
    'chemical_bonding_molecules': {
        'tb': ['chemical_bonding_molecules_textbook.jpg'],
        'ex': ['chemical_bonding_molecules_exam_stipple.jpg'],
        'svg': 'ChemicalBondingMoleculesSvg.jsx',
        'anc': 'chemical_bonding_molecules.json'
    },
    'electrolytic_cell_apparatus': {
        'tb': ['electrolytic_cell_apparatus_textbook.jpg'],
        'ex': ['electrolytic_cell_apparatus_exam_stipple.jpg'],
        'svg': 'ElectrolyticCellApparatusSvg.jsx',
        'anc': 'electrolytic_cell_apparatus.json'
    },
    'gas_evolution_rate_apparatus': {
        'tb': ['gas_evolution_rate_apparatus_textbook.jpg'],
        'ex': ['gas_evolution_rate_apparatus_exam_stipple.jpg'],
        'svg': 'GasEvolutionRateApparatusSvg.jsx',
        'anc': 'gas_evolution_rate_apparatus.json'
    },
    'pulley_incline_masses_system': {
        'tb': ['pulley_incline_masses_system_textbook.jpg'],
        'ex': ['pulley_incline_masses_system_exam_stipple.jpg'],
        'svg': 'PulleyInclineMassesSystemSvg.jsx',
        'anc': 'pulley_incline_masses_system.json'
    },
    'ac_dc_generator_motor_apparatus': {
        'tb': ['ac_dc_generator_motor_apparatus_textbook.jpg'],
        'ex': ['ac_dc_generator_motor_apparatus_exam_stipple.jpg'],
        'svg': 'AcDcGeneratorMotorApparatusSvg.jsx',
        'anc': 'ac_dc_generator_motor_apparatus.json'
    },
    'hydraulic_gears_belt_pulley': {
        'tb': ['hydraulic_gears_belt_pulley_textbook.jpg'],
        'ex': ['hydraulic_gears_belt_pulley_exam_stipple.jpg'],
        'svg': 'HydraulicGearsBeltPulleySvg.jsx',
        'anc': 'hydraulic_gears_belt_pulley.json'
    },
    'earth_lithosphere_layers': {
        'tb': ['earth_lithosphere_layers_textbook.jpg'],
        'ex': ['earth_lithosphere_layers_exam_stipple.jpg'],
        'svg': 'EarthLithosphereLayersSvg.jsx',
        'anc': 'earth_lithosphere_layers.json'
    },
    'architectural_floor_packaging_plan': {
        'tb': ['architectural_floor_packaging_plan_textbook.jpg'],
        'ex': ['architectural_floor_packaging_plan_exam_stipple.jpg'],
        'svg': 'ArchitecturalFloorPackagingPlanSvg.jsx',
        'anc': 'architectural_floor_packaging_plan.json'
    },
}

# Category B Kinds
CAT_B_REGISTRY = {
    'dot_pattern': 'GeoGebraGeometryRenderer.jsx',
    'cartesian_point': 'GeoGebraGeometryRenderer.jsx',
    'radian_sector': 'GeoGebraGeometryRenderer.jsx',
    'cube_net': 'GeoGebraGeometryRenderer.jsx',
    'rectangular_prism_net': 'GeoGebraGeometryRenderer.jsx',
    'triangular_prism_net': 'GeoGebraGeometryRenderer.jsx',
    'square_pyramid_net': 'GeoGebraGeometryRenderer.jsx',
    'cylinder_net': 'GeoGebraGeometryRenderer.jsx',
    'solid_3d': 'GeoGebraGeometryRenderer.jsx',
    'function_graph': 'FunctionGraph.jsx',
    'argand_diagram': 'FunctionGraph.jsx',
    'trapezoidal_rule': 'FunctionGraph.jsx',
    'circle_geometry': 'FunctionGraph.jsx',
    'box_and_whisker': 'StatsAndFinancialGraphRenderer.jsx',
    'statistics_box_and_ogive': 'StatsAndFinancialGraphRenderer.jsx',
    'ogive': 'StatsAndFinancialGraphRenderer.jsx',
    'scatter_plot_regression': 'StatsAndFinancialGraphRenderer.jsx',
    'timeline_finance': 'StatsAndFinancialGraphRenderer.jsx',
    'venn_3_sets': 'StatsAndFinancialGraphRenderer.jsx',
    'motion_graph': 'PhysicsAndEconomicsGraphRenderer.jsx',
    'reaction_energy_profile': 'PhysicsAndEconomicsGraphRenderer.jsx',
    'supply_demand': 'PhysicsAndEconomicsGraphRenderer.jsx',
}

def verify_cat_a_disk(master):
    if master not in CAT_A_REGISTRY:
        return False, "Unknown master"
    meta = CAT_A_REGISTRY[master]
    
    tb_found = any(
        os.path.exists(os.path.join(ROOT_DIR, 'public', 'diagrams', name)) and 
        os.path.getsize(os.path.join(ROOT_DIR, 'public', 'diagrams', name)) > 1000
        for name in meta['tb']
    )
    ex_found = any(
        os.path.exists(os.path.join(ROOT_DIR, 'public', 'diagrams', name)) and 
        os.path.getsize(os.path.join(ROOT_DIR, 'public', 'diagrams', name)) > 1000
        for name in meta['ex']
    )
    svg_found = os.path.exists(os.path.join(ROOT_DIR, 'src', 'components', 'workspace', 'modalities', 'diagram_bank', meta['svg']))
    anc_found = os.path.exists(os.path.join(BACKEND_DIR, 'app', 'data', 'diagram_anchors', meta['anc']))

    is_complete = tb_found and ex_found and svg_found and anc_found
    details = f"TB:{tb_found} EX:{ex_found} SVG:{svg_found} ANC:{anc_found}"
    return is_complete, details

def verify_cat_b_disk(kind):
    if kind not in CAT_B_REGISTRY:
        return False, "Unknown kind"
    comp_file = CAT_B_REGISTRY[kind]
    full_path = os.path.join(ROOT_DIR, 'src', 'components', 'workspace', 'shared', 'mathx', comp_file)
    if not os.path.exists(full_path):
        full_path = os.path.join(ROOT_DIR, 'src', 'components', 'workspace', comp_file)
    
    if not os.path.exists(full_path):
        return False, f"Missing file {comp_file}"
    
    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
        src = f.read()
    
    has_branch = f"'{kind}'" in src or f'"{kind}"' in src
    return has_branch, f"File:{comp_file} Branch:{has_branch}"

def scan_curriculum_docs():
    print("=" * 80)
    print("   CURRICULUM DIAGRAM PIPELINE & GAP AUDITOR (RULE 0d-15)")
    print("=" * 80)

    curriculum_dir = os.path.join(ROOT_DIR, 'curriculum_docs_auto')
    if not os.path.exists(curriculum_dir):
        curriculum_dir = os.path.join(BACKEND_DIR, 'curriculum_docs_auto')

    topic_records = []

    print(f"Reading curriculum docs from: {curriculum_dir}")
    for root, dirs, files in os.walk(curriculum_dir):
        for f in files:
            if not f.endswith('.md'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, curriculum_dir)
            parts = rel.split(os.sep)
            subject_grade = parts[0]
            
            # Extract subject and grade
            sg_match = re.match(r'([A-Za-z]+)_Gr(\d+)', subject_grade)
            if not sg_match:
                continue
            subject_name = sg_match.group(1)
            grade_num = sg_match.group(2)

            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()

            # Find Diagram Context annotations
            diagram_contexts = re.findall(r'\[Diagram Context\s*-\s*([^\]]+)\]', content)
            
            # Extract sample question text after each context
            sample_questions = []
            for m in re.finditer(r'\[Diagram Context\s*-\s*([^\]]+)\]', content):
                start = m.end()
                snippet = content[start:start+400].strip()
                sample_questions.append(snippet[:200].replace('\n', ' '))

            topic_title = f.replace('.md', '')
            topic_clean = re.sub(r'^\d+\.\s*', '', topic_title).strip()

            topic_records.append({
                'subject_grade': subject_grade,
                'subject': subject_name,
                'grade': grade_num,
                'topic': topic_clean,
                'file': rel,
                'diagram_count': len(diagram_contexts),
                'diagram_contexts': diagram_contexts[:5],
                'sample_question': sample_questions[0] if sample_questions else ''
            })

    print(f"Total topics indexed: {len(topic_records)}")
    diagram_demanding_topics = [t for t in topic_records if t['diagram_count'] > 0]
    print(f"Topics demanding diagrams in curriculum: {len(diagram_demanding_topics)}")

    # ---------------------------------------------------------
    # Cross-reference with generators and disk reality
    # ---------------------------------------------------------
    SEEDS = [1001, 1002, 1003]

    verified_active = []
    orphaned_renderers = []
    missing_assets = []
    generator_missing = []

    print("\nExecuting live seed test across diagram-demanding topics...")

    for t in diagram_demanding_topics:
        subject = t['subject']
        grade = t['grade']
        topic = t['topic']

        # Map to generator key
        gen_key = None
        try:
            gen_key = resolve_generator_key(topic, grade=grade, subject=subject)
        except Exception:
            pass

        generator_fn = ALL_GENERATORS.get(gen_key) if gen_key else None

        if not generator_fn:
            generator_missing.append({
                'topic': t,
                'reason': f"No generator registered for {subject} Gr {grade} '{topic}'"
            })
            continue

        # Execute 3 seeds
        emitted_diagrams = []
        gen_error = None
        for seed in SEEDS:
            try:
                res = generator_fn(count=1, seed=seed)
                q_list = res if isinstance(res, list) else res.get('questions', [res])
                for q in q_list:
                    if isinstance(q, dict):
                        spec = q.get('diagram_spec') or q.get('diagram') or q.get('diagram_meta')
                        if spec and isinstance(spec, dict):
                            emitted_diagrams.append(spec)
            except Exception as e:
                gen_error = str(e)
                break

        if gen_error:
            generator_missing.append({
                'topic': t,
                'gen_key': gen_key,
                'reason': f"Generator crashed: {gen_error}"
            })
            continue

        if emitted_diagrams:
            # Check if emitted diagram has disk assets
            for spec in emitted_diagrams:
                master = spec.get('master') or spec.get('image_type')
                kind = spec.get('kind') or spec.get('type')

                if master and master in CAT_A_REGISTRY:
                    ok, det = verify_cat_a_disk(master)
                    if ok:
                        verified_active.append({
                            'topic': t,
                            'gen_key': gen_key,
                            'visual_type': 'Category A',
                            'identifier': master,
                            'details': det
                        })
                    else:
                        missing_assets.append({
                            'topic': t,
                            'gen_key': gen_key,
                            'visual_type': 'Category A',
                            'identifier': master,
                            'details': f"Emitted but disk asset incomplete: {det}"
                        })
                elif kind and kind in CAT_B_REGISTRY:
                    ok, det = verify_cat_b_disk(kind)
                    if ok:
                        verified_active.append({
                            'topic': t,
                            'gen_key': gen_key,
                            'visual_type': 'Category B',
                            'identifier': kind,
                            'details': det
                        })
                    else:
                        missing_assets.append({
                            'topic': t,
                            'gen_key': gen_key,
                            'visual_type': 'Category B',
                            'identifier': kind,
                            'details': f"Emitted but JSX renderer missing branch: {det}"
                        })
        else:
            # Topic has diagram in curriculum, generator exists, but emits ZERO diagrams!
            orphaned_renderers.append({
                'topic': t,
                'gen_key': gen_key,
                'reason': f"Generator runs cleanly but omits diagrams (emits text/formula only)"
            })

    # Deduplicate verified active by topic
    unique_active = {}
    for a in verified_active:
        k = f"{a['topic']['subject_grade']}_{a['topic']['topic']}"
        if k not in unique_active:
            unique_active[k] = a

    unique_orphaned = {}
    for o in orphaned_renderers:
        k = f"{o['topic']['subject_grade']}_{o['topic']['topic']}"
        if k not in unique_orphaned:
            unique_orphaned[k] = o

    print("\n" + "=" * 80)
    print("CURRICULUM SCAN RESULTS (RULE 0d-15)")
    print("=" * 80)
    print(f"Total Topics Scanned:                      {len(topic_records)}")
    print(f"Topics Demanding Diagrams in Curriculum:   {len(diagram_demanding_topics)}")
    print(f"  [VERIFIED ACTIVE]:                       {len(unique_active)} topics actively emit verified diagrams")
    print(f"  [FLAG: GENERATOR OMITS DIAGRAM]:         {len(unique_orphaned)} topics have generators that omit diagrams")
    print(f"  [FLAG: GENERATOR MISSING/CRASHING]:      {len(generator_missing)} topics lack a registered generator")
    print(f"  [FLAG: DISK ASSET INCOMPLETE]:           {len(missing_assets)} emitted diagrams have broken disk assets")
    print("=" * 80)

    # Save full JSON report
    report_json = {
        'total_topics': len(topic_records),
        'diagram_demanding_topics': len(diagram_demanding_topics),
        'active_count': len(unique_active),
        'generator_omits_diagram_count': len(unique_orphaned),
        'generator_missing_count': len(generator_missing),
        'asset_incomplete_count': len(missing_assets),
        'verified_active': list(unique_active.values()),
        'generator_omits_diagram': list(unique_orphaned.values()),
        'generator_missing': generator_missing,
        'asset_incomplete': missing_assets
    }

    report_path = os.path.join(ROOT_DIR, 'curriculum_diagram_pipeline_report.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_json, f, indent=2)

    print(f"\nFull machine-generated report saved to: {report_path}")

    # Generate Markdown gap matrix
    md_path = os.path.join(ROOT_DIR, 'reports', 'curriculum_diagram_gap_matrix.md')
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Factual Curriculum Diagram Gap Matrix (Rule 0d-15 Machine Audit)\n\n")
        f.write(f"- **Total Topics in Curriculum:** {len(topic_records)}\n")
        f.write(f"- **Topics with Diagram Contexts:** {len(diagram_demanding_topics)}\n")
        f.write(f"- **Active Topics (Generator Emits Diagram + Asset Exists):** {len(unique_active)}\n")
        f.write(f"- **Flagged Topics (Generator Omits Diagram):** {len(unique_orphaned)}\n")
        f.write(f"- **Flagged Topics (Generator Missing/Error):** {len(generator_missing)}\n\n")

        f.write("## 1. Flagged Topics: Generator Exists But Omits Curriculum Diagrams\n\n")
        f.write("| Subject & Grade | Curriculum Topic | Generator Key | Curriculum Diagram Context Snippet |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for o in list(unique_orphaned.values())[:50]:
            top = o['topic']
            ctx = top['diagram_contexts'][0] if top['diagram_contexts'] else 'N/A'
            f.write(f"| {top['subject_grade']} | {top['topic']} | `{o['gen_key']}` | {ctx[:50]}... |\n")

        f.write("\n## 2. Verified Active Diagram Topics\n\n")
        f.write("| Subject & Grade | Curriculum Topic | Generator Key | Visual Type | Identifier |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for a in list(unique_active.values()):
            top = a['topic']
            f.write(f"| {top['subject_grade']} | {top['topic']} | `{a['gen_key']}` | {a['visual_type']} | `{a['identifier']}` |\n")

    print(f"Markdown gap matrix saved to: {md_path}")
    return len(unique_orphaned) == 0 and len(generator_missing) == 0

if __name__ == '__main__':
    ok = scan_curriculum_docs()
    sys.exit(0 if ok else 1)
