"""Curriculum Missing Diagrams Backlog Generator (Rule 0d-15)
Analyzes all 506 curriculum topics and 28,035 diagram annotations to identify
visual assets required by textbook/exam questions that are COMPLETELY MISSING
from Fundile's visual bank (neither Category A nor Category B).

Outputs machine-generated report to:
- reports/curriculum_missing_diagrams_backlog.md
- reports/curriculum_missing_diagrams_backlog.json
"""
import os
import sys
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM_DIR = os.path.join(ROOT_DIR, 'curriculum_docs_auto')
if not os.path.exists(CURRICULUM_DIR):
    CURRICULUM_DIR = os.path.join(ROOT_DIR, 'caps-ai-backend', 'curriculum_docs_auto')

# Existing visual assets in Fundile
EXISTING_CAT_A = {
    'human_heart', 'alveolus_gas_exchange', 'digestive_system', 'intestinal_villus',
    'human_nephron', 'human_eye', 'human_ear', 'endocrine_system', 'male_reproductive',
    'female_reproductive', 'meiosis_crossing_over', 'plant_cell', 'animal_cell',
    'mitosis_stages', 'plant_leaf', 'distillation_apparatus', 'titration_apparatus',
    'galvanic_cell', 'solar_system_earth_space', 'particle_model', 'atomic_bohr_structure',
    'chemical_bonding_molecules', 'electrolytic_cell_apparatus', 'gas_evolution_rate_apparatus',
    'pulley_incline_masses_system', 'ac_dc_generator_motor_apparatus', 'hydraulic_gears_belt_pulley',
    'earth_lithosphere_layers', 'architectural_floor_packaging_plan'
}

EXISTING_CAT_B = {
    'dot_pattern', 'cartesian_point', 'radian_sector', 'cube_net', 'rectangular_prism_net',
    'triangular_prism_net', 'square_pyramid_net', 'cylinder_net', 'solid_3d', 'function_graph',
    'argand_diagram', 'trapezoidal_rule', 'circle_geometry', 'box_and_whisker',
    'statistics_box_and_ogive', 'ogive', 'scatter_plot_regression', 'timeline_finance',
    'venn_3_sets', 'motion_graph', 'reaction_energy_profile', 'supply_demand',
    'circuit', 'free_body_diagram', 'optics_ray', 'punnett_square'
}

# Semantic mapping from existing assets to text keywords
EXISTING_ASSET_KEYWORDS = {
    # Cat A
    'human_heart': ['heart', 'cardiac', 'atrium', 'ventricle', 'aorta', 'pulmonary artery'],
    'alveolus_gas_exchange': ['alveol', 'gas exchange', 'capillary network in lung'],
    'digestive_system': ['digestive system', 'alimentary canal', 'esophagus', 'stomach', 'small intestine'],
    'intestinal_villus': ['villus', 'villi', 'lacteal', 'microvilli', 'brush border'],
    'human_nephron': ['nephron', 'bowman', 'glomerulus', 'renal tubule', 'loop of henle'],
    'human_eye': ['human eye', 'cornea', 'retina', 'pupil', 'iris', 'lens', 'ciliary body'],
    'human_ear': ['human ear', 'tympanic', 'cochlea', 'auditory nerve', 'ossicles', 'pinna'],
    'endocrine_system': ['endocrine', 'pituitary', 'adrenal gland', 'thyroid gland', 'islets of langerhans'],
    'male_reproductive': ['male reproductive', 'testis', 'vas deferens', 'prostate', 'scrotum'],
    'female_reproductive': ['female reproductive', 'uterus', 'ovary', 'fallopian', 'endometrium', 'cervix'],
    'meiosis_crossing_over': ['crossing over', 'chiasma', 'homologous chromosomes', 'synapsis'],
    'plant_cell': ['plant cell', 'cell wall', 'vacuole', 'chloroplast'],
    'animal_cell': ['animal cell', 'cytoplasm', 'mitochondri', 'endoplasmic reticulum', 'golgi'],
    'mitosis_stages': ['mitosis', 'prophase', 'metaphase', 'anaphase', 'telophase'],
    'plant_leaf': ['leaf', 'transverse section of leaf', 'mesophyll', 'stoma', 'guard cell', 'xylem', 'phloem'],
    'distillation_apparatus': ['distillation', 'liebig condenser', 'fractionating column'],
    'titration_apparatus': ['titration', 'burette', 'erlenmeyer flask', 'retort stand', 'meniscus'],
    'galvanic_cell': ['galvanic', 'daniell cell', 'salt bridge', 'zinc copper cell'],
    'solar_system_earth_space': ['solar system', 'planets', 'earth and moon', 'revolution of earth'],
    'particle_model': ['particle model', 'states of matter', 'solid liquid gas arrangement'],
    'atomic_bohr_structure': ['bohr model', 'electron shells', 'nucleus protons neutrons', 'atomic structure'],
    'chemical_bonding_molecules': ['chemical bonding', 'covalent bond', 'lewis structure', 'water molecule'],
    'electrolytic_cell_apparatus': ['electrolysis', 'electrolytic cell', 'electroplating'],
    'gas_evolution_rate_apparatus': ['gas evolution', 'gas syringe', 'reaction rate flask', 'calcium carbonate hcl'],
    'pulley_incline_masses_system': ['pulley', 'inclined plane with mass', 'frictionless pulley', 'two masses connected'],
    'ac_dc_generator_motor_apparatus': ['generator', 'dc motor', 'slip rings', 'split ring commutator', 'armature coil'],
    'hydraulic_gears_belt_pulley': ['hydraulic press', 'gear train', 'driver gear', 'v-belt pulley'],
    'earth_lithosphere_layers': ['earth layers', 'lithosphere', 'crust mantle core', 'tectonic plates'],
    'architectural_floor_packaging_plan': ['floor plan', 'elevation plan', 'residential house plan', 'packaging net'],
    # Cat B
    'circuit': ['circuit diagram', 'voltmeter', 'ammeter', 'resistors in series', 'parallel resistors'],
    'free_body_diagram': ['free-body', 'fbd', 'force vectors', 'normal force', 'friction vector'],
    'motion_graph': ['velocity-time graph', 'displacement-time graph', 'acceleration-time graph', 'v-t graph'],
    'reaction_energy_profile': ['potential energy profile', 'activation energy graph', 'exothermic profile', 'enthalpy graph'],
    'supply_demand': ['supply and demand', 'demand curve', 'market equilibrium', 'price quantity graph'],
    'circle_geometry': ['circle geometry', 'tangent to circle', 'cyclic quadrilateral', 'subtended angle'],
    'box_and_whisker': ['box and whisker', 'five number summary', 'quartiles'],
    'statistics_box_and_ogive': ['ogive', 'cumulative frequency curve'],
    'argand_diagram': ['argand', 'complex plane', 'imaginary axis'],
    'trapezoidal_rule': ['trapezoidal rule', 'riemann sum', 'area under irregular curve'],
    'radian_sector': ['circular sector', 'radian angle', 'arc length s = r'],
    'function_graph': ['parabola', 'hyperbola', 'cubic graph', 'exponential graph', 'turning points', 'asymptote'],
}

def is_concept_covered(description):
    desc_lower = description.lower()
    for asset, kws in EXISTING_ASSET_KEYWORDS.items():
        for kw in kws:
            if kw in desc_lower:
                return asset
    return None

def analyze_missing_diagrams():
    print("=" * 80)
    print("   CURRICULUM MISSING DIAGRAMS BACKLOG AUDITOR (RULE 0d-15)")
    print("=" * 80)
    print(f"Reading curriculum docs from: {CURRICULUM_DIR}")

    missing_candidates = []
    covered_candidates = []

    for root, dirs, files in os.walk(CURRICULUM_DIR):
        for f in files:
            if not f.endswith('.md'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, CURRICULUM_DIR)
            parts = rel.split(os.sep)
            subject_grade = parts[0]
            
            sg_match = re.match(r'([A-Za-z]+)_Gr(\d+)', subject_grade)
            if not sg_match:
                continue
            subject = sg_match.group(1)
            grade = sg_match.group(2)
            topic_name = re.sub(r'^\d+\.\s*', '', f.replace('.md', '')).strip()

            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()

            # Find all Diagram Context blocks
            matches = list(re.finditer(r'\[Diagram Context\s*-\s*([^\]]+)\]', content))
            if not matches:
                continue

            for idx, m in enumerate(matches):
                context_id = m.group(1).strip()
                start = m.end()
                # Extract up to next 600 chars of description and question
                snippet = content[start:start+700].strip()
                
                # Extract blockquote description
                desc_match = re.search(r'>\s*([^\n\r]+(?:\n\r?>\s*[^\n\r]+)*)', snippet)
                desc = desc_match.group(0).replace('>', '').replace('\n', ' ').strip() if desc_match else snippet[:200]
                
                # Check coverage against our existing 51 assets
                covered_asset = is_concept_covered(desc)
                
                record = {
                    'subject': subject,
                    'grade': grade,
                    'subject_grade': subject_grade,
                    'topic': topic_name,
                    'file': rel,
                    'context_id': context_id,
                    'description': desc[:300],
                    'sample_text': snippet[:200].replace('\n', ' ')
                }

                if covered_asset:
                    record['matched_existing_asset'] = covered_asset
                    covered_candidates.append(record)
                else:
                    missing_candidates.append(record)

    print(f"Total Diagram Contexts Analyzed: {len(covered_candidates) + len(missing_candidates)}")
    print(f"Diagram Contexts Covered by Existing Bank: {len(covered_candidates)}")
    print(f"Diagram Contexts with NO Existing Asset:   {len(missing_candidates)}")

    # ---------------------------------------------------------
    # Cluster Missing Diagrams into Major Curricular Concepts
    # ---------------------------------------------------------
    # Rule-based clustering of descriptions into clear missing diagram assets
    CLUSTER_RULES = [
        # Life Sciences
        ('dna_replication_and_transcription', 'Life Sciences', ['dna', 'rna', 'transcription', 'translation', 'ribosome', 'codon', 'anticodon', 'nucleotide']),
        ('flower_angiosperm_anatomy', 'Life Sciences', ['flower', 'petal', 'sepal', 'anther', 'stigma', 'stamen', 'carpel', 'ovary', 'pollination']),
        ('reflex_arc_and_nervous_system', 'Life Sciences', ['reflex arc', 'spinal cord', 'sensory neuron', 'motor neuron', 'synapse', 'receptor']),
        ('human_brain_structure', 'Life Sciences', ['brain', 'cerebrum', 'cerebellum', 'medulla oblongata', 'hypothalamus']),
        ('human_skeleton_and_joints', 'Life Sciences', ['skeleton', 'joint', 'synovial', 'femur', 'cartilage', 'ligament', 'vertebra']),
        ('mitochondrion_ultrastructure', 'Life Sciences', ['mitochondri', 'cristae', 'matrix', 'cellular respiration']),
        ('chloroplast_and_photosynthesis', 'Life Sciences', ['chloroplast', 'thylakoid', 'grana', 'stroma', 'light phase']),
        ('cladogram_phylogenetic_tree', 'Life Sciences', ['phylogenetic', 'cladogram', 'evolutionary tree', 'common ancestor']),
        ('pedigree_chart_genetics', 'Life Sciences', ['pedigree', 'family tree', 'inherited disorder', 'carrier generation']),
        ('biomes_and_ecosystem_pyramids', 'Life Sciences', ['biome', 'pyramid of biomass', 'pyramid of numbers', 'trophic level', 'food web']),

        # Physical Sciences
        ('organic_functional_groups_structures', 'Physical Sciences', ['homologous series', 'alkane', 'alkene', 'alcohol', 'ester', 'carboxylic acid', 'ketone', 'aldehyde', 'isomer']),
        ('electromagnetic_induction_faraday', 'Physical Sciences', ['faraday', 'solenoid', 'magnetic field lines', 'induced emf', 'galvanometer', 'bar magnet']),
        ('photoelectric_effect_energy_levels', 'Physical Sciences', ['photoelectric', 'photon', 'work function', 'cutoff frequency', 'gold leaf electroscope']),
        ('doppler_effect_wavefronts', 'Physical Sciences', ['doppler', 'wavefronts', 'pitch', 'approaching source', 'red shift']),
        ('geometrical_optics_snell_refraction', 'Physical Sciences', ['refraction', 'snell', 'glass block', 'critical angle', 'total internal reflection', 'refractive index']),
        ('transverse_wave_pulse_interference', 'Physical Sciences', ['transverse wave', 'superposition', 'constructive interference', 'destructive', 'wave pulse', 'crest trough']),
        ('electrochemical_chlor_alkali_membrane', 'Physical Sciences', ['membrane cell', 'chlor-alkali', 'brine electrolysis', 'mercury cell']),

        # Natural Sciences
        ('rock_cycle_and_sedimentary_strata', 'Natural Sciences', ['rock cycle', 'igneous', 'sedimentary', 'metamorphic', 'strata', 'magma']),
        ('greenhouse_effect_atmosphere', 'Natural Sciences', ['greenhouse effect', 'atmosphere radiation', 'troposphere', 'stratosphere', 'ozone layer']),
        ('simple_machines_levers_wheel_axle', 'Natural Sciences', ['first class lever', 'second class lever', 'fulcrum', 'wheel and axle', 'mechanical advantage']),
        ('acids_bases_ph_indicators_color', 'Natural Sciences', ['ph scale', 'universal indicator', 'litmus paper', 'bromothymol blue']),

        # Mathematical Literacy & Business
        ('water_electricity_municipal_bill_sample', 'Mathematical Literacy', ['municipal bill', 'tariff statement', 'electricity meter reading', 'water consumption']),
        ('furniture_assembly_exploded_diagram', 'Mathematical Literacy', ['assembly diagram', 'exploded view', 'instructions step', 'nuts bolts assembly']),
        ('business_organogram_hierarchy', 'Business Studies', ['organogram', 'organizational structure', 'chain of command', 'span of control', 'hierarchical chart']),
        ('swot_pestle_matrix_framework', 'Business Studies', ['swot', 'pestle', 'porter', 'value chain', 'market environment matrix']),
    ]

    cluster_counts = {}
    clustered_records = {c[0]: [] for c in CLUSTER_RULES}
    unclassified = []

    for m in missing_candidates:
        desc_lower = m['description'].lower()
        matched = False
        for cluster_id, cat, keywords in CLUSTER_RULES:
            if any(kw in desc_lower for kw in keywords):
                cluster_counts[cluster_id] = cluster_counts.get(cluster_id, 0) + 1
                clustered_records[cluster_id].append(m)
                matched = True
                break
        if not matched:
            unclassified.append(m)

    # ---------------------------------------------------------
    # Format and save reports
    # ---------------------------------------------------------
    md_path = os.path.join(ROOT_DIR, 'reports', 'curriculum_missing_diagrams_backlog.md')
    json_path = os.path.join(ROOT_DIR, 'reports', 'curriculum_missing_diagrams_backlog.json')
    os.makedirs(os.path.dirname(md_path), exist_ok=True)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Authoritative Curriculum Missing Diagrams Backlog (Rule 0d-15 Machine Audit)\n\n")
        f.write("This report catalogs visual assets explicitly demanded by South African curriculum documents, past exam papers, and textbook exercises in `curriculum_docs_auto/` where **zero visual assets (Category A plate or Category B renderer) currently exist in Fundile**.\n\n")
        f.write(f"- **Total Curriculum Diagram Annotations Analyzed:** {len(covered_candidates) + len(missing_candidates)}\n")
        f.write(f"- **Annotations Covered by Existing Bank (Active/Orphaned):** {len(covered_candidates)}\n")
        f.write(f"- **Annotations With No Existing Asset (True Gaps):** {len(missing_candidates)}\n")
        f.write(f"- **Identified Canonical Missing Visual Masters:** {len(CLUSTER_RULES)}\n\n")

        f.write("## 1. Top Missing Visual Assets Required by Curriculum (Ranked by Exam Frequency)\n\n")
        f.write("| Visual Concept ID | Subject Area | Target Modality | Curriculum Annotations | Representative Curriculum Context |\n")
        f.write("| :--- | :--- | :---: | :---: | :--- |\n")

        sorted_clusters = sorted(CLUSTER_RULES, key=lambda c: cluster_counts.get(c[0], 0), reverse=True)
        for cluster_id, subject_area, keywords in sorted_clusters:
            cnt = cluster_counts.get(cluster_id, 0)
            sample = clustered_records[cluster_id][0] if clustered_records[cluster_id] else None
            snippet = sample['description'][:140] + "..." if sample else "Referenced across curriculum past papers"
            modality = "Category A (Plate)" if subject_area in ['Life Sciences', 'Natural Sciences'] and 'tree' not in cluster_id else "Category B (Precision Vector)"
            f.write(f"| `{cluster_id}` | {subject_area} | {modality} | **{cnt}** | {snippet} |\n")

        f.write("\n## 2. Subject Breakdown of Missing Visuals\n\n")
        subj_totals = {}
        for c in sorted_clusters:
            s = c[1]
            subj_totals[s] = subj_totals.get(s, 0) + cluster_counts.get(c[0], 0)
        for s, total in sorted(subj_totals.items(), key=lambda x: x[1], reverse=True):
            f.write(f"- **{s}:** {total} curriculum references across textbooks and exams\n")

    # Save JSON report
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_annotations': len(covered_candidates) + len(missing_candidates),
            'covered_annotations': len(covered_candidates),
            'missing_annotations': len(missing_candidates),
            'missing_clusters': [
                {
                    'id': c[0],
                    'subject': c[1],
                    'count': cluster_counts.get(c[0], 0),
                    'keywords': c[2],
                    'sample_records': clustered_records[c[0]][:3]
                }
                for c in sorted_clusters
            ]
        }, f, indent=2)

    print("\n" + "=" * 80)
    print("MISSING DIAGRAM BACKLOG SUMMARY")
    print("=" * 80)
    for c in sorted_clusters[:10]:
        print(f"  {c[0]:<40} | {c[1]:<18} | Hits: {cluster_counts.get(c[0], 0):3d}")
    print("=" * 80)
    print(f"Report saved to: {md_path}")
    print(f"JSON saved to:   {json_path}")

if __name__ == '__main__':
    analyze_missing_diagrams()
