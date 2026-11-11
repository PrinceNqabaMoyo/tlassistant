"""Deep Runtime Diagram Integration Auditor (Rule 0d-15)
Executes actual generators in ALL_GENERATORS across real seeds to determine
which diagrams are genuinely emitted in live question payloads vs. which are orphaned.
Zero guessing, zero phantom claims.
"""
import sys
import os

# Add caps-ai-backend to path
BACKEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caps-ai-backend')
sys.path.insert(0, BACKEND_DIR)

from app.services.generator_registry import ALL_GENERATORS, generate_variant

CATEGORY_A_MASTERS = [
    'human_heart',
    'alveolus_gas_exchange',
    'digestive_system',
    'intestinal_villus',
    'human_nephron',
    'human_eye',
    'human_ear',
    'endocrine_system',
    'male_reproductive',
    'female_reproductive',
    'meiosis_crossing_over',
    'plant_cell',
    'animal_cell',
    'mitosis_stages',
    'plant_leaf',
    'distillation_apparatus',
    'titration_apparatus',
    'galvanic_cell',
    'solar_system_earth_space',
    'particle_model',
    'atomic_bohr_structure',
    'chemical_bonding_molecules',
    'electrolytic_cell_apparatus',
    'gas_evolution_rate_apparatus',
    'pulley_incline_masses_system',
    'ac_dc_generator_motor_apparatus',
    'hydraulic_gears_belt_pulley',
    'earth_lithosphere_layers',
    'architectural_floor_packaging_plan',
]

CATEGORY_B_KINDS = [
    'dot_pattern',
    'cartesian_point',
    'radian_sector',
    'cylinder_net',
    'cube_net',
    'solid_3d',
    'argand_diagram',
    'trapezoidal_rule',
    'circle_geometry',
    'cubic',
    'box_and_whisker',
    'statistics_box_and_ogive',
    'ogive',
    'scatter_plot_regression',
    'timeline_finance',
    'venn_3_sets',
    'motion_graph',
    'reaction_energy_profile',
    'supply_demand',
]

MASTER_ALIASES = {
    'heart': 'human_heart',
    'human_digestive_system': 'digestive_system',
    'electric_circuits': 'electric_circuits_ns',
}

KIND_ALIASES = {
    'statistics_box_and_ogive': 'ogive',
}

def run_runtime_diagram_audit():
    print("=" * 80)
    print("   FUNDILE RUNTIME DIAGRAM INTEGRATION AUDIT (RULE 0d-15)")
    print("   Querying actual generator outputs over live seeds (zero theatre)")
    print("=" * 80)

    # Master -> list of (gen_key, seed, topic, subskill) that emitted it
    master_hits = {m: [] for m in CATEGORY_A_MASTERS}
    kind_hits = {k: [] for k in CATEGORY_B_KINDS}

    # Test generators that are visual or relevant
    SEEDS = [1001, 1002, 1003, 1004, 1005]

    total_tested = 0
    total_exceptions = 0

    print(f"Scanning {len(ALL_GENERATORS)} registered generators across 5 test seeds...")

    for gen_key, gen_fn in list(ALL_GENERATORS.items()):
        total_tested += 1
        for seed in SEEDS:
            try:
                # Call generator function
                res = gen_fn(count=1, seed=seed)
                questions = []
                if isinstance(res, list):
                    questions = res
                elif isinstance(res, dict):
                    questions = res.get('questions', [res])
                
                for q in questions:
                    if not isinstance(q, dict):
                        continue
                    spec = q.get('diagram_spec') or q.get('diagram') or q.get('diagram_meta') or {}
                    if not isinstance(spec, dict):
                        continue
                    
                    # Category A check (master or image_type)
                    master = spec.get('master') or spec.get('image_type')
                    master = MASTER_ALIASES.get(master, master)
                    if not master or master not in master_hits:
                        master2 = spec.get('image_type') or spec.get('master')
                        master = MASTER_ALIASES.get(master2, master2)
                    if master and master in master_hits:
                        master_hits[master].append((gen_key, seed, q.get('topic', 'unknown')))

                    # Category B check (kind or type)
                    kind = spec.get('kind') or spec.get('type')
                    if kind and kind in kind_hits:
                        kind_hits[kind].append((gen_key, seed, q.get('topic', 'unknown')))
                    
                    if kind in KIND_ALIASES:
                        aliased_k = KIND_ALIASES[kind]
                        if aliased_k in kind_hits:
                            kind_hits[aliased_k].append((gen_key, seed, q.get('topic', 'unknown')))
                    
                    if spec.get('family') == 'cubic' or spec.get('function_type') == 'cubic':
                        if 'cubic' in kind_hits:
                            kind_hits['cubic'].append((gen_key, seed, q.get('topic', 'unknown')))
            except Exception as e:
                total_exceptions += 1

    print("\n" + "-" * 80)
    print("--- CATEGORY A (HEART STANDARD MASTERS) RUNTIME RESULTS ---")
    print("-" * 80)

    cat_a_active = 0
    cat_a_orphaned = 0

    for m in CATEGORY_A_MASTERS:
        hits = master_hits[m]
        unique_keys = sorted(list(set(h[0] for h in hits)))
        if hits:
            cat_a_active += 1
            print(f"  [PASS] {m:<35} | Hits: {len(hits):2d} | Generators: {', '.join(unique_keys[:2])}")
        else:
            cat_a_orphaned += 1
            print(f"  [PARTIAL: ORPHANED] {m:<25} | Hits:  0 | NO REGISTERED GENERATOR CALLS THIS MASTER")

    print("\n" + "-" * 80)
    print("--- CATEGORY B (GEOGEBRA+ / DESMOS+ VECTOR KINDS) RUNTIME RESULTS ---")
    print("-" * 80)

    cat_b_active = 0
    cat_b_orphaned = 0

    for k in CATEGORY_B_KINDS:
        hits = kind_hits[k]
        unique_keys = sorted(list(set(h[0] for h in hits)))
        if hits:
            cat_b_active += 1
            print(f"  [PASS] {k:<35} | Hits: {len(hits):2d} | Generators: {', '.join(unique_keys[:2])}")
        else:
            cat_b_orphaned += 1
            print(f"  [PARTIAL: ORPHANED] {k:<25} | Hits:  0 | NO REGISTERED GENERATOR CALLS THIS KIND")

    print("\n" + "=" * 80)
    print(f"SUMMARY: {cat_a_active}/{len(CATEGORY_A_MASTERS)} Category A masters active in live generators.")
    print(f"         {cat_a_orphaned} Category A masters orphaned (plates exist, but 0 generator calls).")
    print(f"         {cat_b_active}/{len(CATEGORY_B_KINDS)} Category B kinds active in live generators.")
    print(f"         {cat_b_orphaned} Category B kinds orphaned.")
    print("=" * 80)

    if cat_a_orphaned > 0 or cat_b_orphaned > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    run_runtime_diagram_audit()
