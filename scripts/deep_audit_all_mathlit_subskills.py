import sys
import json
from collections import defaultdict

sys.path.insert(0, 'caps-ai-backend')

from app.services.generator_registry import ALL_GENERATORS, get_topic_archetypes, generate_variant

with open('caps-ai-backend/app/services/caps_term_registry_data.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

mathlit_entries = [
    x for x in manifest
    if 'literacy' in (x.get('subject') or '').lower() and str(x.get('grade')) in ('10', '11')
]

SUPPORTED_DIAGRAM_KINDS = {
    'right_triangle', 'number_line', 'circle_subtended_angle', 'circle_cyclic_quad',
    'circle_tangent_secant', 'triangle', 'quadrilateral', 'angle_diagram', 'parallel_transversal',
    'dot_pattern', 'cartesian_point', 'radian_sector', 'cube_net', 'rectangular_prism_net',
    'triangular_prism_net', 'square_pyramid_net', 'cylinder_net', 'solid_3d',
    'function_graph', 'argand_diagram', 'trapezoidal_rule', 'circle_geometry', 'linear_programming',
    'box_and_whisker', 'statistics_box_and_ogive', 'ogive', 'scatter_plot_regression',
    'timeline_finance', 'venn_3_sets', 'contingency_table', 'contingency_table_and_tree',
    'step_tariff', 'break_even', 'probability_spinner', 'function_flow', 'flow_diagram',
    'bar_graph', 'double_bar_graph', 'histogram', 'frequency_polygon', 'pie_chart',
    'motion_graph', 'reaction_energy_profile', 'kc_equilibrium_graph', 'maxwell_boltzmann',
    'supply_demand', 'circular_flow', 'production_chain', 'promissory_note', 'source_document',
    'sankey_energy', 'grid_paper', 'organogram', 'porters_five_forces', 'process_flow',
    'food_chain', 'concept_map', 'ph_scale'
}

print(f"Total Gr10 & Gr11 MathLit manifest entries: {len(mathlit_entries)}")

for entry in mathlit_entries:
    grade = str(entry.get('grade'))
    topic_name = entry.get('name') or entry.get('topic_name')
    gen_key = entry.get('generator_key')
    info = get_topic_archetypes(gen_key or topic_name, grade=grade, subject='Mathematical Literacy')
    archs = info.get('archetypes', [])
    resolved_key = info.get('generator_key')
    
    issues = defaultdict(int)
    sample_issues = {}
    emitted_subskills = set()
    diagram_kinds_seen = defaultdict(int)
    unrendered_diagrams = defaultdict(int)
    diagrams_count = 0
    
    for sub in archs:
        try:
            res = generate_variant(
                topic=resolved_key,
                grade=grade,
                subject='Mathematical Literacy',
                subskill=sub,
                seed=101,
                count=1
            )
            qs = res if isinstance(res, list) else res.get('questions', [res])
            q = qs[0]
            emitted_sub = q.get('subskill') or q.get('archetype') or q.get('subtopic')
            emitted_subskills.add(emitted_sub)
            if emitted_sub != sub:
                issues['subskill_mismatch'] += 1
                sample_issues.setdefault('subskill_mismatch', f"requested={sub}, got={emitted_sub}")
                
            prompt = str(q.get('prompt') or q.get('question') or '')
            ans = str(q.get('correct_answer') or q.get('expected_answer') or '')
            opts = q.get('options') or []
            sol = str(q.get('worked_solution') or q.get('explanation') or q.get('sample_answer') or '')
            
            # Check synthetic options
            for o in opts:
                if '(Alt ' in str(o) or '(Option ' in str(o):
                    issues['synthetic_alt_options'] += 1
                    sample_issues.setdefault('synthetic_alt_options', f"{sub}: {opts}")
                    break
            
            # Check worked solution
            if len(sol.strip()) < 20:
                issues['short_or_missing_solution'] += 1
                sample_issues.setdefault('short_or_missing_solution', f"{sub}: '{sol}'")
                
            # Check formatting corruptions
            if '{ }' in prompt or '{ }' in ans or '{ }' in sol:
                issues['brace_space_corruption'] += 1
                sample_issues.setdefault('brace_space_corruption', f"{sub}")
                
            # Check diagrams
            diag = q.get('diagram_spec') or q.get('diagram')
            if diag:
                diagrams_count += 1
                kind = diag.get('kind') or diag.get('diagram_type') or diag.get('type') or 'MISSING_KIND'
                diagram_kinds_seen[kind] += 1
                if not diag.get('kind') or diag.get('kind') not in SUPPORTED_DIAGRAM_KINDS:
                    unrendered_diagrams[kind] += 1
                    sample_issues.setdefault('unrendered_diagram', f"{sub}: diag keys={list(diag.keys())}, kind={diag.get('kind')}, diagram_type={diag.get('diagram_type')}")
            else:
                low_p = prompt.lower()
                if any(w in low_p for w in ['refer to the', 'shown below', 'diagram below', 'plan below', 'map below', 'accompanying', 'figure below']):
                    if '|' not in prompt and '```' not in prompt:
                        issues['prompt_mentions_missing_diagram'] += 1
                        sample_issues.setdefault('prompt_mentions_missing_diagram', f"{sub}: {prompt[:90]}...")
        except Exception as e:
            issues['exception'] += 1
            sample_issues.setdefault('exception', f"{sub}: {e}")
            
    print(f"\n[Gr{grade}] {topic_name} -> {resolved_key}")
    print(f"  Discovered archetypes: {len(archs)} | Distinct emitted when stepped: {len(emitted_subskills)} | With diagram object: {diagrams_count}/{len(archs)}")
    if diagram_kinds_seen:
        print(f"  Diagram kinds emitted: {dict(diagram_kinds_seen)}")
    if unrendered_diagrams:
        print(f"  [DEFECT] UNRENDERED diagram kinds (ignored by DiagramRenderer.jsx!): {dict(unrendered_diagrams)}")
    if issues:
        print(f"  [DEFECTS FOUND]: {dict(issues)}")
        for k, v in sample_issues.items():
            print(f"    Sample {k}: {v}")
