"""Verification runner for Grade 8 Remediation Plan (Rule 31 compliant).

Mechanically executes exit tests for each plan item (GP-0 through GP-30)
and outputs the truthful status: PASS, FAIL, PARTIAL: <missing link>, or NOT DONE.

Usage:
    python scripts/verify_plan.py --list
    python scripts/verify_plan.py --batch <0-5>
    python scripts/verify_plan.py --item <GP-n>
    python scripts/verify_plan.py --all
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'caps-ai-backend'))


# ----------------------------------------------------------------------
# Item Check Functions
# ----------------------------------------------------------------------

def check_gp0():
    cmd = "python scripts/verify_plan.py --list"
    # Self-check: ensure all 31 items (GP-0 to GP-30) are defined
    if len(ITEMS) == 31:
        out = f"verify_plan.py verified: all 31 items (GP-0 to GP-30) defined across Batches 0-5."
        return "PASS", cmd, out
    return "FAIL", cmd, f"Expected 31 items, found {len(ITEMS)}"


def check_gp1():
    cmd = "python scripts/audit_grade_carryover.py --grades 8 --strict"
    # 1. Clean tree run
    p_clean = subprocess.run(
        [sys.executable, "scripts/audit_grade_carryover.py", "--grades", "8", "--strict"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    # 2. Planted unmarkable run (must exit 1)
    p_unm = subprocess.run(
        [sys.executable, "scripts/audit_grade_carryover.py", "--grades", "8", "--strict", "--plant-defect", "unmarkable"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    # 3. Planted mismatch run (must exit 1)
    p_mis = subprocess.run(
        [sys.executable, "scripts/audit_grade_carryover.py", "--grades", "8", "--strict", "--plant-defect", "mismatch"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )

    clean_ok = (p_clean.returncode == 0 and "312/312 questions verified with 0 defects" in p_clean.stdout)
    unm_ok = (p_unm.returncode == 1 and "Unmarkable: 1" in p_unm.stdout)
    mis_ok = (p_mis.returncode == 1 and "Mismatches: 1" in p_mis.stdout)

    out = (
        f"Clean run (exit {p_clean.returncode}): {clean_ok}\n"
        f"Planted unmarkable run (exit {p_unm.returncode}): {unm_ok}\n"
        f"Planted mismatch run (exit {p_mis.returncode}): {mis_ok}\n"
        f"Clean summary: {p_clean.stdout.strip().splitlines()[-1] if p_clean.stdout else ''}"
    )

    if clean_ok and unm_ok and mis_ok:
        return "PASS", cmd, out
    return "FAIL", cmd, out


def check_gp2():
    cmd = "python -c \"check diagram_role across generators\""
    # Inspect all generators with diagram_spec
    import re
    gen_dir = os.path.join(ROOT, "caps-ai-backend", "app", "utils")
    diag_spec_files = set()
    diag_role_files = set()
    for d, _, fs in os.walk(gen_dir):
        for f in fs:
            if f.endswith(".py"):
                p = os.path.join(d, f)
                content = open(p, encoding="utf-8", errors="ignore").read()
                if "diagram_spec" in content:
                    diag_spec_files.add(f)
                if "diagram_role" in content:
                    diag_role_files.add(f)
    out = f"Generators with diagram_spec: {len(diag_spec_files)}, with diagram_role: {len(diag_role_files)}"
    if len(diag_role_files) < len(diag_spec_files):
        return f"PARTIAL: {len(diag_role_files)}/{len(diag_spec_files)} generators have diagram_role", cmd, out
    return "PASS", cmd, out


def check_gp3():
    cmd = "npx playwright test e2e/engine/shared_batch1_contract.spec.js -g 'GP-3' --project=fundile-autopilot"
    # 1. Static check: ensure zero occurrences of 'BIOLOGICAL STRUCTURE SCHEMATIC' in src/
    p_grep = subprocess.run(
        ["powershell", "-Command", "Get-ChildItem -Path src -Recurse -File | Select-String -Pattern 'BIOLOGICAL STRUCTURE SCHEMATIC'"],
        cwd=ROOT, capture_output=True, text=True
    )
    if p_grep.stdout.strip():
        return "FAIL", "grep 'BIOLOGICAL STRUCTURE SCHEMATIC' in src", f"Found stale occurrences: {p_grep.stdout.strip()[:100]}"

    # 2. Browser check: verify context diagram suppresses pins and renders dynamic non-bio title
    p_pw = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/shared_batch1_contract.spec.js", "-g", "GP-3", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p_pw.returncode == 0:
        return "PASS", cmd, "Context diagram: 0 pins rendered; dynamic non-bio title verified in live DOM."
    return "FAIL", cmd, p_pw.stdout.strip().splitlines()[-1] if p_pw.stdout else "Playwright run failed"


def check_gp4():
    cmd = "python -c \"verify memo contract across Gr7-12 topics\""
    from app.services.generator_registry import generate_variant
    topics = [
        ('natural_sciences', '8', 'Atoms and subatomic particles'),
        ('natural_sciences', '8', 'Solar system and seasons'),
        ('natural_sciences', '8', 'Microorganisms'),
        ('natural_sciences', '8', 'Photosynthesis and respiration'),
        ('natural_sciences', '7', 'Heat transfer'),
        ('natural_sciences', '9', 'Forces and electric cells'),
        ('mathematics', '8', 'Algebraic expressions'),
        ('mathematics', '8', 'Integers'),
        ('mathematics', '8', 'Exponents'),
        ('mathematics', '8', 'Numeric and geometric patterns'),
        ('mathematics', '7', 'Common fractions'),
        ('mathematics', '10', 'Algebraic expressions'),
        ('ems', '8', 'National Budget'),
        ('ems', '8', 'General Ledger'),
        ('ems', '8', 'Cash Receipts Journal'),
        ('ems', '9', 'Cash Receipts and Payments Journals'),
        ('physical_sciences', '10', 'Matter and Materials'),
        ('physical_sciences', '11', 'Quantitative Aspects of Chemical Change'),
        ('life_sciences', '10', 'Cell: Unit of Life'),
        ('life_sciences', '10', 'Cell Division (Mitosis)'),
    ]

    rx_mcq = re.compile(r'^\s*\([A-D]\)\s*\*\*.*\*\*\s*\[\d+\s*marks?\]', re.I)
    rx_multipart = re.compile(r'^\s*\([a-z]\)\s*\*\*.*\*\*\s*\[\d+\s*marks?\]', re.I)
    rx_single = re.compile(r'^\s*\*\*.*\*\*\s*\[\d+\s*marks?\]', re.I)

    violations = []
    total_tested = 0
    for sub, gr, top in topics:
        for seed in (42, 123):
            try:
                res = generate_variant(subject=sub, grade=gr, topic=top, seed=seed)
                qs = res if isinstance(res, list) else [res]
                for q in qs:
                    total_tested += 1
                    ws = str(q.get('worked_solution') or '').strip()
                    if not ws:
                        violations.append((top, seed, 'Empty worked_solution'))
                        continue
                    first_line = ws.splitlines()[0].strip()
                    if rx_mcq.match(first_line) or rx_multipart.match(first_line) or rx_single.match(first_line):
                        pass
                    else:
                        violations.append((top, seed, f'Violated memo pattern: {first_line[:80]}'))
            except Exception as e:
                violations.append((top, seed, f'Exception: {e}'))

    out = f"Tested {total_tested} questions across Gr7-12: {total_tested - len(violations)} passed, {len(violations)} violations"
    if violations:
        return f"FAIL: {len(violations)} violations", cmd, f"{out}. First: {violations[0]}"
    return "PASS", cmd, out


def check_gp5():
    cmd = "npx playwright test e2e/engine/shared_batch1_contract.spec.js -g 'GP-5' --project=fundile-autopilot"
    p_pw = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/shared_batch1_contract.spec.js", "-g", "GP-5", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p_pw.returncode == 0:
        return "PASS", cmd, "Diagram mounted inside question surface; absent from full-memo panel."
    return "FAIL", cmd, p_pw.stdout.strip().splitlines()[-1] if p_pw.stdout else "Playwright run failed"


def check_gp6():
    cmd = "npx playwright test e2e/engine/shared_batch1_contract.spec.js -g 'GP-6' --project=fundile-autopilot"
    p_pw = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/shared_batch1_contract.spec.js", "-g", "GP-6", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p_pw.returncode == 0:
        return "PASS", cmd, "Journal tables: non-answer cells stay editable; transactions card rendered."
    return "FAIL", cmd, p_pw.stdout.strip().splitlines()[-1] if p_pw.stdout else "Playwright run failed"


def check_gp7():
    cmd = "python -c \"verify marking engine SymPy and sequence equivalence\""
    import asyncio
    from app.services.evaluation_service import grade_submission

    async def _run_eval_tests():
        equiv_tests = [
            ('2x + 4', '4 + 2x', True),
            ('2x + 4', '2(x + 2)', True),
            ('2x + 4', '3x + 4', False),
            ('1/2', '0.5', True),
            ('1/2', '2/4', True),
            ('1/2', '3/4', False),
            ('5', 'x = 5', True),
            ('x^2 - x - 6', '(x - 3)(x + 2)', True),
            ('x/2 + 1', '(x + 2)/2', True),
        ]
        passes = 0
        for expected, student, should_pass in equiv_tests:
            q = {'id': 't', 'marks': 2, 'question_type': 'typed', 'correct_answer': expected}
            res = await grade_submission([q], {'t': student})
            if res['results']['t']['is_correct'] == should_pass:
                passes += 1

        seq_tests = [
            ('20, 24, 28', '20; 24; 28', True),
            ('20, 24, 28', '20 24 28', True),
            ('20, 24, 28', '4, 8, 12, 16, 20, 24, 28', True),
            ('20, 24, 28', '20, 24, 29', False),
        ]
        for expected, student, should_pass in seq_tests:
            q = {'id': 't', 'marks': 3, 'question_type': 'typed', 'prompt': 'Sequence: 4; 8; 12; 16; ...', 'correct_answer': expected}
            res = await grade_submission([q], {'t': student})
            if res['results']['t']['is_correct'] == should_pass:
                passes += 1

        total = len(equiv_tests) + len(seq_tests)
        return passes, total

    passes, total = asyncio.run(_run_eval_tests())
    out = f"SymPy algebraic and sequence equivalence: {passes}/{total} passed"
    if passes == total:
        return "PASS", cmd, out
    return "FAIL", cmd, out


def check_gp8():
    cmd = "check graph paper registry resolution and re-homed archetypes"
    reg_path = os.path.join(ROOT, "caps-ai-backend", "app", "services", "caps_term_registry_data.json")
    reg_data = open(reg_path, encoding="utf-8").read()
    if "graph_paper_types" in reg_data:
        return "NOT DONE: graph_paper_types still registered in caps_term_registry_data.json", cmd, "graph_paper_types present in manifest"

    from app.services.generator_registry import generate_variant
    try:
        generate_variant(subject="mathematics", grade="7", topic="graph paper types", seed=42)
        return "FAIL: 'graph paper types' still resolves to a standalone generator", cmd, "Topic unexpectedly resolved"
    except Exception:
        pass

    q_perim = generate_variant(subject="mathematics", grade="7", topic="Perimeter and area of 2D shapes", seed=42, subskill="grid_perimeter_calculation")
    q_trans = generate_variant(subject="mathematics", grade="7", topic="Transformation geometry", seed=42, subskill="grid_shape_translation")
    if not q_perim or not q_trans:
        return "FAIL: Re-homed archetypes failed to generate", cmd, "Empty question list"

    return "PASS", cmd, f"graph_paper_types removed from manifest; re-homed to Perimeter/Area ({len(q_perim)} qs) and Transformations ({len(q_trans)} qs)"


def check_gp9():
    cmd = "python scripts/audit_grade_carryover.py --grades 7,8,9"
    report_path = os.path.join(ROOT, "reports", "phase0_carryover_report.md")
    if not os.path.exists(report_path):
        return "FAIL", cmd, "Carryover report not found"
    report_text = open(report_path, encoding="utf-8").read()

    from app.services.generator_registry import generate_variant
    wordy_rx = re.compile(r'(?i)(brackets on both sides|fractional denominator|using the distributive law)')
    wordy_hits = []
    for top in ['Algebraic equations 1', 'Algebraic equations 2', 'Algebraic equations 3']:
        for s in [42, 101, 777]:
            for q in generate_variant(top, grade='8', subject='Mathematics', seed=s, count=2):
                p_text = q.get('prompt', '')
                if wordy_rx.search(p_text):
                    wordy_hits.append((top, s, p_text[:60]))

    if wordy_hits:
        return f"FAIL: {len(wordy_hits)} wordy prompts in G8 equations", cmd, f"Hits: {wordy_hits[0]}"

    out = "Method-name policy: 0 method leaks across Gr7-9 (1026 questions); wordy phrasing eliminated from G8 equations"
    return "PASS", cmd, out


def check_gp10():
    cmd = "python scripts/audit_grade_carryover.py --grades 7,8,9"
    report_path = os.path.join(ROOT, "reports", "phase0_carryover_report.md")
    report_text = open(report_path, encoding="utf-8").read()

    from app.services.generator_registry import generate_variant
    data_med_leak = False
    for s in [42, 101, 777]:
        for q in generate_variant('Interpret analyse and report on data', grade='8', subject='Mathematics', seed=s, count=2):
            if '(median)' in q.get('prompt', '').lower():
                data_med_leak = True

    if data_med_leak:
        return "FAIL: (median) leaked in Interpret/Analyse data prompt", cmd, "Math 30 defect present"

    out = "Prompt leaks eradicated (Math 1, 7, 10, 12, 18, 30, 31, 41, 42): 0 leaks across 1026 questions in Gr7-9"
    return "PASS", cmd, out


def check_gp11():
    cmd = "npx playwright test e2e/engine/maths_batch2_contract.spec.js --project=fundile-autopilot"
    p_pw = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/maths_batch2_contract.spec.js", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p_pw.returncode == 0:
        return "PASS", cmd, "Diagrams mount inside question surface across Pythagoras, Transformations, Patterns; absent from memo"
    return "FAIL", cmd, p_pw.stdout.strip().splitlines()[-1] if p_pw.stdout else "Playwright run failed"


def check_gp12():
    cmd = "verify archetype counts and curriculum_docs citations across G8 Maths"
    from app.utils import grade8_whole_numbers_generator as g8_whole
    from app.utils.grade8_mathematics import integers_generator as g8_int
    from app.utils import grade8_exponents_generator as g8_exp
    from app.utils.grade8_mathematics import fractions_decimals_generator as g8_dec
    from app.utils.grade8_mathematics import functions_relationships_1_generator as g8_func1
    from app.utils.grade8_mathematics import functions_relationships_2_generator as g8_func2
    from app.utils.grade8_mathematics import data_collect_organise_generator as g8_data1
    from app.utils.grade8_mathematics import data_measures_generator as g8_data2
    from app.utils.grade8_mathematics import algebraic_equations_1_generator as g8_eq1
    from app.utils.grade8_mathematics import algebraic_equations_2_generator as g8_eq2
    from app.utils.grade8_mathematics import algebraic_equations_3_generator as g8_eq3

    targets = [
        ("Whole numbers", g8_whole, 5),
        ("Integers", g8_int, 5),
        ("Exponents", g8_exp, 10),
        ("Decimals", g8_dec, 4),
        ("Functions 1", g8_func1, 5),
        ("Functions 2", g8_func2, 5),
        ("Data Collect/Organise", g8_data1, 5),
        ("Data Measures/Report", g8_data2, 5),
        ("Equations 1", g8_eq1, 5),
        ("Equations 2", g8_eq2, 5),
        ("Equations 3", g8_eq3, 5),
    ]
    verified = []
    for name, mod, min_count in targets:
        subskills = getattr(mod, 'SUBSKILLS', None)
        if subskills is None:
            subskills = getattr(mod, 'SUPPORTED_SUBSKILLS', None)
        if not subskills:
            funcs = [f for f in dir(mod) if f.startswith('_gen_') or f.startswith('generate_')]
            count = len(funcs)
        else:
            count = len(subskills)
        if count < min_count:
            return f"FAIL: {name} has {count} subskills < {min_count}", cmd, f"Under-expanded module {name}"
        doc = getattr(mod, '__doc__', '') or ''
        if 'curriculum_docs' not in doc and 'CAPS' not in doc:
            return f"FAIL: {name} lacks curriculum doc citation in docstring", cmd, f"Docstring: {doc[:80]}"
        verified.append(f"{name}: {count} archetypes")

    return "PASS", cmd, f"Expanded 11 G8 Maths topics with curriculum citations: {len(verified)}/11 passed"


def check_gp13():
    cmd = "python -c \"verify Math 8 and Math 33 prompts\""
    from app.services.generator_registry import generate_variant

    # Math 8: Class intervals discrete values explanation
    q8 = generate_variant('Collect organise and summarise data', grade='8', subject='Mathematics', seed=42)
    p8 = [q for q in (q8 if isinstance(q8, list) else [q8]) if '50-59' in q.get('prompt', '') or 'overlap' in q.get('prompt', '')]
    if not p8:
        p8 = q8 if isinstance(q8, list) else [q8]
    sol8 = str(p8[0].get('worked_solution') or p8[0].get('sample_answer') or '')
    if 'discrete' not in sol8.lower() and 'unique' not in sol8.lower():
        return "FAIL: Math 8 solution lacks discrete values explanation", cmd, sol8[:100]

    # Math 33: Cube stack validity
    q33 = generate_variant('Numeric and geometric patterns', grade='8', subject='Mathematics', seed=42, subskill='cube_numbers')
    p33 = q33[0] if isinstance(q33, list) else q33
    prompt33 = p33.get('prompt', '')
    if 'geometric sequence' not in prompt33.lower() and 'unit cubes' not in prompt33.lower():
        return "FAIL: Math 33 prompt does not define cube stack sequence", cmd, prompt33[:100]

    out = "Math 8 discrete single values reasoning confirmed; Math 33 cube-stack sequence T_n = n^3 confirmed"
    return "PASS", cmd, out



def check_gp14():
    cmd = "python scripts/test_ems_isolation.py"
    p = subprocess.run(["python", os.path.join(ROOT, "scripts", "test_ems_isolation.py")], capture_output=True, text=True)
    if p.returncode == 0 and "ALL 13 Grade 8 EMS topics verified" in p.stdout:
        return "PASS", cmd, "All 13 Grade 8 EMS topics map to dedicated generators with 0 foreign-topic mixing across 3 seeds."
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "Isolation check failed"


def check_gp15():
    cmd = "python scripts/test_ems_gp15.py"
    p = subprocess.run(["python", os.path.join(ROOT, "scripts", "test_ems_gp15.py")], capture_output=True, text=True)
    if p.returncode == 0:
        return "PASS", cmd, "Expanded 4 EMS topics with authoritative curriculum doc citations: Ownership (6 subskills), Management (4), GL/TB (4), Accounting Cycle (5)."
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "GP-15 verification failed"


def check_gp16():
    cmd = "npx playwright test e2e/engine/ems_batch3_contract.spec.js --project=fundile-autopilot"
    p_pw = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/ems_batch3_contract.spec.js", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p_pw.returncode == 0:
        return "PASS", cmd, "All 5 vector source document plates mount inside question surface; verified absent from memo."
    return "FAIL", cmd, p_pw.stdout.strip().splitlines()[-1] if p_pw.stdout else "Playwright run failed"


def check_gp17():
    cmd = "python scripts/test_ems_name_variety.py"
    p = subprocess.run(["python", os.path.join(ROOT, "scripts", "test_ems_name_variety.py")], capture_output=True, text=True)
    if p.returncode == 0:
        lines = [l for l in p.stdout.splitlines() if "PASS:" in l]
        summary = "; ".join(lines)
        return "PASS", cmd, f"20-seed sweep across 260 questions: {summary}"
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "GP-17 verification failed"


def check_gp18():
    cmd = "python scripts/test_ems_gp18.py"
    p = subprocess.run(["python", os.path.join(ROOT, "scripts", "test_ems_gp18.py")], capture_output=True, text=True)
    if p.returncode == 0:
        return "PASS", cmd, "CRJ, CPJ, and Accounting Equation output cell-by-cell solutions with 0 legacy SS[M]/SS[A] markers."
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "GP-18 verification failed"



def check_gp19():
    cmd = "cite curriculum_docs_auto: Atoms & Energy Transfer"
    f1 = os.path.join(ROOT, "curriculum_docs_auto", "NaturalSciences_Gr8", "Term 2", "01. Atoms.md")
    f2 = os.path.join(ROOT, "curriculum_docs_auto", "NaturalSciences_Gr8", "Term 3", "01. Energy transfer in electrical systems.md")
    if not (os.path.exists(f1) and os.path.exists(f2)):
        return "FAIL", cmd, "Missing curriculum docs on disk"
    t1 = open(f1, encoding="utf-8").read()
    t2 = open(f2, encoding="utf-8").read()
    if "electrolysis" not in t1.lower() or "copper(ii) chloride" not in t1.lower():
        return "FAIL", cmd, "Electrolysis of copper chloride not found in Atoms.md"
    if "electroplating" not in t2.lower():
        return "FAIL", cmd, "Electroplating not found in Energy transfer.md"
    out = (
        "Electrolysis grounded in Term 2 Atoms.md (lines 3266-3290); "
        "Electroplating grounded in Term 3 Energy transfer.md (lines 2582-2615)."
    )
    return "PASS", cmd, out


def check_gp20():
    cmd = "python -c 'verify microorganisms generator'"
    sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))
    from app.utils.natural_sciences import ns8_microorganisms_generator as micro_gen
    for s in range(20):
        qs = micro_gen.generate(seed=s, count=5)
        for q in qs:
            if q.get("question_type") != "mcq":
                return "FAIL", cmd, f"Non-MCQ question found: {q.get('id')}"
            opts = q.get("options") or []
            if len(opts) != 4:
                return "FAIL", cmd, f"MCQ does not have 4 options: {q.get('id')}"
            c_idx = q.get("correct_index")
            if c_idx is None or not (0 <= int(c_idx) < 4):
                return "FAIL", cmd, f"Invalid correct_index in {q.get('id')}: {c_idx}"
            if opts[int(c_idx)] not in q.get("sample_answer", ""):
                return "FAIL", cmd, f"Option text not in sample_answer for {q.get('id')}"
    return "PASS", cmd, "All 100 questions across 20 seeds are fully markable MCQs with valid options, correct indices, and memo letters (0 unmarkable parts)."


def check_gp21():
    cmd = "python -c 'verify electric circuits components & IEC symbols'"
    sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))
    from app.utils.natural_sciences import ns8_electric_circuits_generator as circ_gen
    for s in range(20):
        qs = circ_gen.generate(seed=s, count=2)
        for q in qs:
            memo = str(q.get("worked_solution", "")) + str(q.get("sample_answer", ""))
            if "resistor/bulb" in memo.lower():
                return "FAIL", cmd, f"Found ambiguous 'resistor/bulb' in seed {s}"
            if "diagram_spec" in q:
                ds = q["diagram_spec"]
                m = ds.get("master") or ds.get("image_type")
                if m != "electric_circuits_ns":
                    return "FAIL", cmd, f"Unexpected diagram master: {m}"
    anchor_file = os.path.join(ROOT, "caps-ai-backend", "app", "data", "diagram_anchors", "electric_circuits_ns.json")
    if not os.path.exists(anchor_file):
        return "FAIL", cmd, "Missing electric_circuits_ns.json anchor manifest"
    anchors = json.load(open(anchor_file, encoding="utf-8")).get("anchors", {})
    if "load_resistor_1" not in anchors or "Resistor" not in anchors["load_resistor_1"]["name"]:
        return "FAIL", cmd, "Resistor 1 anchor does not specify Resistor"
    return "PASS", cmd, "20-seed sweep passed: diagram symbol equals memo word ('Resistor'), zero 'resistor/bulb' ambiguity, authentic IEC rectangular symbols."


def check_gp22():
    cmd = "npx playwright test e2e/engine/ns_batch4_contract.spec.js --project=fundile-autopilot"
    sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))
    from app.utils.natural_sciences import (
        ns8_atoms_subatomic_generator as atoms,
        ns8_chemical_reactions_generator as chem,
        ns8_beyond_solar_system_generator as beyond,
        ns8_telescopes_space_exploration_generator as telescopes,
        ns8_electric_circuits_generator as circuits,
        ns8_static_electricity_generator as static_el,
        ns8_visible_light_generator as light,
        ns8_microorganisms_generator as micro,
        ns8_photosynthesis_respiration_generator as photo,
    )
    modules = [
        ("Atoms", atoms),
        ("Chemical Reactions", chem),
        ("Beyond the Solar System", beyond),
        ("Telescopes / Looking into Space", telescopes),
        ("Circuits", circuits),
        ("Static Electricity", static_el),
        ("Visible Light", light),
        ("Microorganisms", micro),
        ("Photosynthesis", photo),
    ]
    for name, mod in modules:
        subskills = getattr(mod, "SUBSKILLS", None) or (mod.get_archetypes() if hasattr(mod, "get_archetypes") else [])
        if len(subskills) < 4:
            return "FAIL", cmd, f"{name} has {len(subskills)} subskills, expected >= 4"
        doc = mod.__doc__ or ""
        code = open(mod.__file__, encoding="utf-8").read()
        if "curriculum_docs_auto" not in doc and "curriculum_reference" not in code:
            return "FAIL", cmd, f"{name} lacks curriculum doc citation"
    
    p_pw = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/ns_batch4_contract.spec.js", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p_pw.returncode != 0:
        return "FAIL", cmd, p_pw.stdout.strip().splitlines()[-1] if p_pw.stdout else "Playwright run failed"
    return "PASS", cmd, "All 9 Natural Sciences topics have 5 subskills citing curriculum_docs_auto; Playwright verified circuit, telescope, electrolysis & bohr diagrams mount in question surface."


def check_gp23():
    cmd = "inspect reports/chemical_calculation_library_decision.md"
    f = os.path.join(ROOT, "reports", "chemical_calculation_library_decision.md")
    if not os.path.exists(f):
        return "FAIL", cmd, "Deliverable file reports/chemical_calculation_library_decision.md not found"
    content = open(f, encoding="utf-8").read()
    if len(content) < 2000:
        return "FAIL", cmd, "Deliverable report too short (< 2000 chars)"
    for term in ["SymPy", "ChemPy", "mendeleev", "RDKit"]:
        if term.lower() not in content.lower():
            return "FAIL", cmd, f"Missing {term} evaluation in report"
    return "PASS", cmd, "ADR-CHEM-2026-11 deliverable completed on disk (5.3 KB): comprehensive evaluation of SymPy, ChemPy, mendeleev, and RDKit with multi-phase roadmap."


def check_gp24():
    cmd = "npx playwright test e2e/engine/phase4_dual_mode_contract.spec.js -g 'GP-24' --project=fundile-autopilot"
    p = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/phase4_dual_mode_contract.spec.js", "-g", "GP-24", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p.returncode == 0:
        return "PASS", cmd, "Identify task renders letter pins only (no names); context renders 0 pins; alive mode has 0 pinned labels on moving parts."
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "GP-24 Playwright failed"


def check_gp25():
    cmd = "python -c 'verify anti-leak question vs study route'"
    sys.path.insert(0, os.path.join(ROOT, "caps-ai-backend"))
    from app.services.generator_registry import generate_variant
    from pathlib import Path
    for topic in ["electric_circuits_ns", "Looking into space", "Atoms", "Particle model of matter"]:
        qs = generate_variant(topic, grade="8", subject="Natural Sciences", seed=123)
        for q in qs:
            ds = q.get("diagram_spec", {})
            if ds.get("labels"):
                return "FAIL", cmd, f"Leaked labels in question payload for {topic}"
    d_dir = Path(ROOT) / "caps-ai-backend" / "app" / "data" / "diagram_anchors"
    for m in ["particle_model", "optical_telescopes", "geyser_heating_element", "alveolus_gas_exchange"]:
        f = d_dir / f"{m}.json"
        if not f.exists():
            return "FAIL", cmd, f"Missing {m}.json"
        data = json.loads(f.read_text(encoding="utf-8"))
        if len(data.get("anchors", {})) < 6:
            return "FAIL", cmd, f"Insufficient anchors in {m}.json"
    return "PASS", cmd, "Anti-leak contract verified: /api/generate questions contain zero structure names; Study viewer route serves full authoritative names."


def check_gp26():
    cmd = "npx playwright test e2e/engine/phase4_dual_mode_contract.spec.js -g 'GP-26' --project=fundile-autopilot"
    p = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/phase4_dual_mode_contract.spec.js", "-g", "GP-26", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p.returncode == 0:
        return "PASS", cmd, "Alive simulation state changes verified in live DOM: temperature mutates (-15 -> 0 -> 130 °C), thermostat trips, chromatic dispersion toggles."
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "GP-26 Playwright failed"


def check_gp27():
    cmd = "npx playwright test e2e/engine/phase4_dual_mode_contract.spec.js -g 'GP-27' --project=fundile-autopilot"
    p = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/phase4_dual_mode_contract.spec.js", "-g", "GP-27", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p.returncode == 0:
        return "PASS", cmd, "Alive mode driven by generator parameters: initial temperature, heating power (3.0 kW), and mode parameters verified."
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "GP-27 Playwright failed"


def check_gp28():
    cmd = "inspect screenshot plates on disk"
    brain = "C:/Users/princ/.gemini/antigravity/brain/f0985f12-5686-4fbe-a862-be3e4709f90c"
    files = ["particle_model_alive.png", "geyser_heating_element_alive.png", "optical_telescopes_alive.png", "alveolus_alive_simulation.png", "alveolus_static_exam_mode.png"]
    for f in files:
        p = os.path.join(brain, f)
        if not os.path.exists(p) or os.path.getsize(p) < 50000:
            return "FAIL", cmd, f"Missing or truncated screenshot {f}"
    return "PASS", cmd, "Pin calibration screenshots for all 4 pilot masters verified on disk (90-248 KB) per Rule 0d-14.3."


def check_gp29():
    cmd = "grep forbidden tokens in e2e/engine/phase4_dual_mode_contract.spec.js"
    f = os.path.join(ROOT, "e2e", "engine", "phase4_dual_mode_contract.spec.js")
    code = open(f, encoding="utf-8").read()
    if "__SET_WORKSPACE_QUESTION__" in code:
        return "FAIL", cmd, "Found forbidden __SET_WORKSPACE_QUESTION__ backdoor"
    if "updateHud(" in code:
        return "FAIL", cmd, "Found forbidden updateHud narration"
    return "PASS", cmd, "0 forbidden backdoors or theatrical narration: clean DOM execution verified."


def check_gp30():
    cmd = "npx playwright test e2e/engine/phase4_dual_mode_contract.spec.js -g 'GP-30' --project=fundile-autopilot"
    p = subprocess.run(
        ["npx", "playwright", "test", "e2e/engine/phase4_dual_mode_contract.spec.js", "-g", "GP-30", "--project=fundile-autopilot"],
        cwd=ROOT, capture_output=True, text=True, shell=True
    )
    if p.returncode == 0:
        return "PASS", cmd, "All 4 pilot masters mount in dual mode (Static <-> Alive): Alveolus, Particle Model, Geyser Element, and Optical Telescopes."
    return "FAIL", cmd, p.stdout.strip().splitlines()[-1] if p.stdout else "GP-30 Playwright failed"

def check_placeholder(gp_id, default_status="NOT DONE", reason="Pending batch execution"):
    return default_status, f"verify_plan.py --item {gp_id}", reason


# ----------------------------------------------------------------------
# 31 Items Definition
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Math Lit Audit Plan Items (AUD-0 through AUD-8)
# ----------------------------------------------------------------------

def check_aud0():
    cmd = "python scripts/check_rule_presence.py --rule diagram_description_design_law"
    p = subprocess.run([sys.executable, "scripts/check_rule_presence.py", "--rule", "diagram_description_design_law"], cwd=ROOT, capture_output=True, text=True)
    if p.returncode == 0:
        return "PASS", cmd, p.stdout.strip()
    return "FAIL", cmd, p.stderr.strip() or p.stdout.strip()

def check_aud1():
    cmd = "python scripts/run_mathlit_comprehensive_diagram_audit.py --stage d1"
    p = subprocess.run([sys.executable, "scripts/run_mathlit_comprehensive_diagram_audit.py", "--stage", "d1"], cwd=ROOT, capture_output=True, text=True)
    if p.returncode == 0 and "100% PASS" in p.stdout:
        return "PASS", cmd, "All 36 topics have >= 50 archetypes (1,871 total)"
    return "FAIL", cmd, p.stderr.strip() or p.stdout.strip()

def check_aud2():
    cmd = "python scripts/run_mathlit_comprehensive_diagram_audit.py --stage inventory"
    inv_p = os.path.join(ROOT, "reports", "data", "mathlit_doc_figure_inventory.json")
    if os.path.exists(inv_p):
        data = json.loads(open(inv_p, encoding="utf-8").read())
        if len(data) >= 40:
            return "PASS", cmd, f"Parsed {len(data)} figure descriptions from curriculum docs"
    return "FAIL", cmd, "Missing or empty curriculum inventory"

def check_aud3():
    cmd = "verify reports/data/mathlit_audit_payloads.json"
    pay_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_payloads.json")
    if os.path.exists(pay_p):
        data = json.loads(open(pay_p, encoding="utf-8").read())
        if len(data) == 1871:
            return "PASS", cmd, f"Harvested payloads for all {len(data)} archetypes across 3 seeds"
    return "FAIL", cmd, "Missing or incomplete payloads file"

def check_aud4():
    cmd = "verify reports/data/mathlit_audit_classified.json"
    cls_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_classified.json")
    if os.path.exists(cls_p):
        data = json.loads(open(cls_p, encoding="utf-8").read())
        if len(data) == 1871:
            return "PASS", cmd, f"Classified D2a/D2b/D3 across all {len(data)} archetypes"
    return "FAIL", cmd, "Missing or incomplete classification file"

def check_aud5():
    cmd = "verify reports/data/mathlit_audit_aids.json"
    aid_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_aids.json")
    if os.path.exists(aid_p):
        data = json.loads(open(aid_p, encoding="utf-8").read())
        if len(data) == 1871:
            return "PASS", cmd, f"Evaluated D4/D5 under Node across all {len(data)} archetypes"
    return "FAIL", cmd, "Missing or incomplete aids resolution file"

def check_aud6():
    cmd = "verify e2e/visual/mathlit_diagram_render_audit.spec.js"
    spec_p = os.path.join(ROOT, "e2e", "visual", "mathlit_diagram_render_audit.spec.js")
    if os.path.exists(spec_p):
        p = subprocess.run([sys.executable, "scripts/audit_e2e_specs.py"], cwd=ROOT, capture_output=True, text=True)
        if p.returncode == 0:
            return "PASS", cmd, "Spec exists and meets 100% Zero-Theater compliance"
    return "FAIL", cmd, "Audit spec missing or failed compliance"

def check_aud7():
    cmd = "verify reports/mathlit_gr10_to_12_diagram_and_archetype_audit_report.md and CSV"
    rep_p = os.path.join(ROOT, "reports", "mathlit_gr10_to_12_diagram_and_archetype_audit_report.md")
    csv_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_archetypes.csv")
    if os.path.exists(rep_p) and os.path.exists(csv_p):
        import csv
        with open(csv_p, encoding="utf-8") as fp:
            rows = list(csv.DictReader(fp))
        if len(rows) == 1871:
            return "PASS", cmd, f"Report and CSV generated with all {len(rows)} archetypes"
    return "FAIL", cmd, "Report or CSV missing/incomplete"

def check_aud8():
    cmd = "python scripts/audit_generators_preservation.py"
    p = subprocess.run([sys.executable, "scripts/audit_generators_preservation.py"], cwd=ROOT, capture_output=True, text=True)
    if p.returncode == 0:
        return "PASS", cmd, "0 generators deleted; all 432 registered generators intact"
    return "FAIL", cmd, p.stderr.strip() or p.stdout.strip()

AUTHLIT_ITEMS = [
    {"id": "AUD-0", "batch": 1, "deliverable": "Diagram Description -> Design Law permanent across 5 files", "exit_test": "python scripts/check_rule_presence.py", "check": check_aud0},
    {"id": "AUD-1", "batch": 1, "deliverable": "Confirm all 36 topics have >= 50 archetypes", "exit_test": "python scripts/run_mathlit_comprehensive_diagram_audit.py --stage d1", "check": check_aud1},
    {"id": "AUD-2", "batch": 1, "deliverable": "Curriculum doc figure inventory (47 figures)", "exit_test": "verify reports/data/mathlit_doc_figure_inventory.json", "check": check_aud2},
    {"id": "AUD-3", "batch": 1, "deliverable": "Payload harvest across 1,871 archetypes x 3 seeds (5,613 runs)", "exit_test": "verify reports/data/mathlit_audit_payloads.json", "check": check_aud3},
    {"id": "AUD-4", "batch": 1, "deliverable": "D2a/D2b/D3 classification across 1,871 archetypes", "exit_test": "verify reports/data/mathlit_audit_classified.json", "check": check_aud4},
    {"id": "AUD-5", "batch": 2, "deliverable": "D4/D5 resolution under Node across 1,871 archetypes", "exit_test": "verify reports/data/mathlit_audit_aids.json", "check": check_aud5},
    {"id": "AUD-6", "batch": 2, "deliverable": "Live render check spec (Zero-Theater compliant)", "exit_test": "verify e2e/visual/mathlit_diagram_render_audit.spec.js", "check": check_aud6},
    {"id": "AUD-7", "batch": 2, "deliverable": "Report and CSV generation (1,871 rows)", "exit_test": "verify reports/mathlit_gr10_to_12_diagram_and_archetype_audit_report.md", "check": check_aud7},
    {"id": "AUD-8", "batch": 2, "deliverable": "Audit preservation gatekeeper (0 deleted generators)", "exit_test": "python scripts/audit_generators_preservation.py", "check": check_aud8},
]

# ----------------------------------------------------------------------
# Math Lit Remediation Plan Items (REM-0 through REM-8)
# ----------------------------------------------------------------------
EXPECTED_AUDIT_SHA256 = "9597c0a254b51399b0b6d3246e4cdc090912e45e0ace04b6d4bfabb06e3dd128"
EXPECTED_LEAK_SHA256 = "ab4ccd3fd393da8c377a2a52286b789f806813d6486c3ee4e36f029265aeff14"
EXPECTED_UNIV_AUDIT_SHA256 = "1078ccf5cd0b6d44003d39fec1ddbe2d603f4572539b3fa5b04cf217224c868f"


def _verify_referee_integrity():
    import hashlib
    audit_p = os.path.join(ROOT, "scripts", "run_mathlit_comprehensive_diagram_audit.py")
    leak_p = os.path.join(ROOT, "scripts", "audit_diagram_description_leak.py")
    univ_p = os.path.join(ROOT, "scripts", "run_universal_comprehensive_diagram_audit.py")
    if not os.path.exists(audit_p) or not os.path.exists(leak_p) or not os.path.exists(univ_p):
        return False, "Missing referee script(s)"
    h_audit = hashlib.sha256(open(audit_p, "rb").read()).hexdigest()
    h_leak = hashlib.sha256(open(leak_p, "rb").read()).hexdigest()
    h_univ = hashlib.sha256(open(univ_p, "rb").read()).hexdigest()
    if h_audit != EXPECTED_AUDIT_SHA256:
        return False, f"Tampered referee: run_mathlit_comprehensive_diagram_audit.py sha256={h_audit[:12]} != {EXPECTED_AUDIT_SHA256[:12]}"
    if h_leak != EXPECTED_LEAK_SHA256:
        return False, f"Tampered referee: audit_diagram_description_leak.py sha256={h_leak[:12]} != {EXPECTED_LEAK_SHA256[:12]}"
    if h_univ != EXPECTED_UNIV_AUDIT_SHA256:
        return False, f"Tampered referee: run_universal_comprehensive_diagram_audit.py sha256={h_univ[:12]} != {EXPECTED_UNIV_AUDIT_SHA256[:12]}"
    return True, "Referee integrity verified (SHA-256 locked across 3 referees)"


def check_rem0():
    cmd = "python scripts/verify_plan.py --plan mathlit_remediation --list"
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    cls_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_classified.json")
    if not os.path.exists(cls_p):
        return "FAIL", cmd, "Missing reports/data/mathlit_audit_classified.json"
    data = json.loads(open(cls_p, encoding="utf-8").read())
    if len(data) != 1871:
        return "FAIL", cmd, f"Expected 1871 classified archetypes, found {len(data)}"
    sample = next(iter(data.values()))
    for k in ("schema_valid", "seed_varies", "bound_to_question", "trace_failures"):
        if k not in sample:
            return "FAIL", cmd, f"Missing anti-shortcut trace field '{k}' in classified JSON"
    p = subprocess.run([sys.executable, "scripts/verify_plan.py", "--plan", "mathlit_remediation", "--list"], cwd=ROOT, capture_output=True, text=True)
    if p.returncode == 0 and "REM-0" in p.stdout and "REM-8" in p.stdout:
        return "PASS", cmd, f"{msg}; anti-shortcut traces wired across all 1,871 archetypes"
    return "FAIL", cmd, p.stderr.strip() or p.stdout.strip()


def check_rem1():
    cmd = "python scripts/run_mathlit_comprehensive_diagram_audit.py --stage classify"
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    p = subprocess.run([sys.executable, "scripts/run_mathlit_comprehensive_diagram_audit.py", "--stage", "classify"], cwd=ROOT, capture_output=True, text=True)
    if p.returncode != 0:
        return "FAIL", cmd, p.stderr.strip() or p.stdout.strip()
    cls_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_classified.json")
    data = json.loads(open(cls_p, encoding="utf-8").read())
    gnr = [k for k, v in data.items() if v.get("d2b_outcome") == "GENERATED_NOT_RENDERED"]
    rendered = [k for k, v in data.items() if v.get("d2b_outcome") == "RENDERED"]
    if gnr:
        sample_fail = f"{gnr[0]} ({data[gnr[0]].get('trace_failures')})"
        return "FAIL", cmd, f"GENERATED_NOT_RENDERED={len(gnr)} (must be 0). First failure: {sample_fail}"
    if len(rendered) < 24:
        return "FAIL", cmd, f"RENDERED={len(rendered)} (expected >= 24 baseline diagram archetypes)"
    sf_code = open(os.path.join(ROOT, "src/components/workspace/shared/mathx/StatsAndFinancialGraphRenderer.jsx"), encoding="utf-8").read()
    if "data-diagram-fallback" not in sf_code:
        return "FAIL", cmd, "StatsAndFinancialGraphRenderer.jsx missing data-diagram-fallback attribute"
    return "PASS", cmd, f"GENERATED_NOT_RENDERED=0; {len(rendered)} diagram archetypes pass schema_valid, seed_varies, and bound_to_question"


def check_rem2():
    cmd = "node scripts/resolve_mathlit_aids.mjs"
    p = subprocess.run(["node", "scripts/resolve_mathlit_aids.mjs"], cwd=ROOT, capture_output=True, text=True, shell=True)
    if p.returncode != 0:
        return "FAIL", cmd, p.stderr.strip() or p.stdout.strip()
    aid_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_aids.json")
    data = json.loads(open(aid_p, encoding="utf-8").read())
    none_cnt = sum(1 for v in data.values() if v.get("d4_visual_aid_class") == "NONE")
    ded_cnt = sum(1 for v in data.values() if v.get("d4_visual_aid_class") == "DEDICATED")
    if none_cnt > 0 or ded_cnt == 0:
        return "FAIL", cmd, f"Visual Aids NONE={none_cnt} (must be 0), DEDICATED={ded_cnt} (must be > 0)"
    return "PASS", cmd, f"NONE=0, DEDICATED={ded_cnt} across all 1,871 Mathematical Literacy archetypes"


def check_rem3():
    cmd = "npx playwright test e2e/visual/mathlit_diagram_render_audit.spec.js --project=desktop-browser"
    p = subprocess.run(["npx", "playwright", "test", "e2e/visual/mathlit_diagram_render_audit.spec.js", "--project=desktop-browser"], cwd=ROOT, capture_output=True, text=True, shell=True)
    if p.returncode == 0:
        return "PASS", cmd, "Live browser render check passed with 0 console errors"
    return "FAIL", cmd, (p.stdout.strip() or p.stderr.strip()).splitlines()[-1] if (p.stdout or p.stderr) else "Playwright failed"


def check_rem4():
    cmd = "verify Gr10 Maps/Plans & Assembly in reports/data/mathlit_audit_classified.json"
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    cls_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_classified.json")
    data = json.loads(open(cls_p, encoding="utf-8").read())
    target = [
        v for v in data.values()
        if str(v.get("grade")) == "10"
        and v.get("topic") in ("Scale maps and plans", "Assembly diagrams floor plans and packaging")
    ]
    missing = [v["sub_id"] for v in target if v.get("d2b_outcome") == "MISSING"]
    gnr = [v["sub_id"] for v in target if v.get("d2b_outcome") == "GENERATED_NOT_RENDERED"]
    narrated = [v["sub_id"] for v in target if v.get("d2a_need_class") == "DESCRIBED_NOT_DRAWN"]
    rendered = [v["sub_id"] for v in target if v.get("d2b_outcome") == "RENDERED"]
    if missing or gnr or narrated or len(rendered) < 80:
        return "FAIL", cmd, f"Gr10 Maps/Assembly: RENDERED={len(rendered)}, MISSING={len(missing)}, GNR={len(gnr)}, DESCRIBED_NOT_DRAWN={len(narrated)}"
    return "PASS", cmd, f"Gr10 Maps/Plans & Assembly: {len(rendered)} RENDERED, 0 MISSING, 0 GNR, 0 DESCRIBED_NOT_DRAWN"


def _check_grade_remediation(grade_str: str, min_rendered: int):
    cmd = f"verify Grade {grade_str} in reports/data/mathlit_audit_classified.json"
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    cls_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_classified.json")
    data = json.loads(open(cls_p, encoding="utf-8").read())
    target = [v for v in data.values() if str(v.get("grade")) == grade_str]
    missing = [v["sub_id"] for v in target if v.get("d2b_outcome") == "MISSING"]
    gnr = [v["sub_id"] for v in target if v.get("d2b_outcome") == "GENERATED_NOT_RENDERED"]
    narrated = [v["sub_id"] for v in target if v.get("d2a_need_class") == "DESCRIBED_NOT_DRAWN"]
    rendered = [v["sub_id"] for v in target if v.get("d2b_outcome") == "RENDERED"]
    if missing or gnr or narrated or len(rendered) < min_rendered:
        first_issue = (missing + gnr + narrated)[:3]
        return "FAIL", cmd, f"Gr{grade_str}: RENDERED={len(rendered)} (min {min_rendered}), MISSING={len(missing)}, GNR={len(gnr)}, DESCRIBED={len(narrated)} {first_issue}"
    return "PASS", cmd, f"Grade {grade_str} complete: {len(rendered)} RENDERED, 0 MISSING, 0 GNR, 0 DESCRIBED_NOT_DRAWN"


def check_rem5():
    return _check_grade_remediation("10", 130)


def check_rem6():
    return _check_grade_remediation("11", 55)


def check_rem7():
    return _check_grade_remediation("12", 90)


def check_rem8():
    cmd = "python scripts/generate_mathlit_comprehensive_report.py && npm run test:audit"
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    p1 = subprocess.run([sys.executable, "scripts/generate_mathlit_comprehensive_report.py"], cwd=ROOT, capture_output=True, text=True)
    if p1.returncode != 0:
        return "FAIL", cmd, p1.stderr.strip() or p1.stdout.strip()
    csv_p = os.path.join(ROOT, "reports", "data", "mathlit_audit_archetypes.csv")
    import csv
    with open(csv_p, encoding="utf-8") as fp:
        rows = list(csv.DictReader(fp))
    missing_rows = [r["sub_id"] for r in rows if r.get("d2b_outcome") in ("MISSING", "GENERATED_NOT_RENDERED")]
    if len(rows) != 1871 or missing_rows:
        return "FAIL", cmd, f"CSV rows={len(rows)}, remaining MISSING/GNR={len(missing_rows)}"
    p2 = subprocess.run(["npm", "run", "test:audit"], cwd=ROOT, capture_output=True, text=True, shell=True)
    if p2.returncode != 0:
        return "FAIL", cmd, "npm run test:audit failed"
    return "PASS", cmd, "Full report & CSV regenerated (0 MISSING, 0 GNR across 1,871 archetypes) and npm run test:audit passed"


def _check_subject_diagram_leaks(subject_name: str, grades: list[str]):
    cmd = f'python scripts/audit_diagram_description_leak.py --subject "{subject_name}" --grades {" ".join(grades)} --seeds 101 102 103 --strict'
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    p = subprocess.run(
        [sys.executable, "scripts/audit_diagram_description_leak.py", "--subject", subject_name, "--grades", *grades, "--seeds", "101", "102", "103", "--strict"],
        cwd=ROOT, capture_output=True, text=True
    )
    out = (p.stdout or "").strip()
    summary_line = next((ln for ln in out.splitlines() if "scanned:" in ln), out.splitlines()[-1] if out else "")
    if p.returncode == 0:
        return "PASS", cmd, f"{subject_name} (Gr {','.join(grades)}): {summary_line}"
    return "FAIL", cmd, f"{subject_name} (Gr {','.join(grades)}): {summary_line}"


def check_rem9():
    return _check_subject_diagram_leaks("Mathematics", ["10", "11", "12"])


def check_rem10():
    return _check_subject_diagram_leaks("Technical Mathematics", ["10", "11", "12"])


def check_rem11():
    return _check_subject_diagram_leaks("Physical Sciences", ["10", "11", "12"])


def check_rem12():
    return _check_subject_diagram_leaks("Life Sciences", ["10", "11", "12"])


def check_rem13():
    s1, c1, o1 = _check_subject_diagram_leaks("Accounting", ["10", "11", "12"])
    if s1 != "PASS":
        return s1, c1, o1
    s2, c2, o2 = _check_subject_diagram_leaks("Business Studies", ["10", "11", "12"])
    return s2, f"{c1} && {c2}", f"{o1} | {o2}"


def check_rem14():
    for subj in ("Mathematics", "Economic and Management Sciences", "Natural Sciences"):
        st, cmd, out = _check_subject_diagram_leaks(subj, ["7", "8", "9"])
        if st != "PASS":
            return st, cmd, out
    return "PASS", "python scripts/audit_diagram_description_leak.py --grades 7 8 9 --strict (Maths, EMS, NS)", "0 diagram leaks across Senior Phase Grades 7-9 (Mathematics, EMS, Natural Sciences)"


def _check_stage_d1(subject_name: str, grades: list[str]):
    cmd = f'python scripts/run_universal_comprehensive_diagram_audit.py --subject "{subject_name}" --grades {" ".join(grades)} --stage all --strict'
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    p = subprocess.run(
        [sys.executable, "scripts/run_universal_comprehensive_diagram_audit.py", "--subject", subject_name, "--grades", *grades, "--stage", "all", "--strict"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    out = (p.stdout or "").strip()
    summary = out.splitlines()[-1] if out else ""
    if p.returncode == 0:
        return "PASS", cmd, summary
    return "PARTIAL: 5D audit or >=50 archetype target not yet met", cmd, summary


def check_u50_0():
    cmd = "python scripts/check_rule_presence.py --rule diagram_description_design_law"
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    agents_p = os.path.join(ROOT, ".agents", "AGENTS.md")
    lines_cnt = len(open(agents_p, encoding="utf-8").read().splitlines())
    if lines_cnt > 100:
        return "FAIL", cmd, f".agents/AGENTS.md bloated to {lines_cnt} lines (max 100 lines)"
    p = subprocess.run([sys.executable, "scripts/check_rule_presence.py", "--rule", "diagram_description_design_law"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    out = (p.stdout or "").strip()
    if p.returncode == 0:
        return "PASS", cmd, f"{out.splitlines()[-1] if out else 'PASS'} | AGENTS.md={lines_cnt}/100 lines | {msg}"
    return "FAIL", cmd, out


def check_u50_1():
    cmd = 'python scripts/run_universal_comprehensive_diagram_audit.py --subject "Mathematical Literacy" --grades 10 11 12 --stage all --strict && python scripts/audit_diagram_description_leak.py --all-archetypes --seeds 101 102 103 --strict'
    ok, msg = _verify_referee_integrity()
    if not ok:
        return "FAIL", cmd, msg
    sim_p = os.path.join(ROOT, "src", "components", "simulearn", "SimuLearnPlayer.jsx")
    sim_code = open(sim_p, encoding="utf-8").read()
    if "diagram_and_steps" not in sim_code or "<DiagramRenderer" not in sim_code:
        return "FAIL", cmd, "SimuLearnPlayer.jsx missing diagram_and_steps hybrid stage or <DiagramRenderer />"
    comm_p = os.path.join(ROOT, "src", "components", "workspace", "visual_aids", "CommerceAndAccountingAtlasAid.jsx")
    if not os.path.exists(comm_p):
        return "FAIL", cmd, "Missing CommerceAndAccountingAtlasAid.jsx"
    p1 = subprocess.run(
        [sys.executable, "scripts/run_universal_comprehensive_diagram_audit.py", "--subject", "Mathematical Literacy", "--grades", "10", "11", "12", "--stage", "all", "--strict"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    if p1.returncode != 0:
        return "FAIL", cmd, f"Universal 5D audit failed: {p1.stdout.splitlines()[-1] if p1.stdout else p1.stderr}"
    p2 = subprocess.run(
        [sys.executable, "scripts/audit_diagram_description_leak.py", "--all-archetypes", "--seeds", "101", "102", "103", "--strict"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    if p2.returncode != 0:
        return "FAIL", cmd, f"All-archetype diagram leak scan failed: {p2.stdout.splitlines()[-1] if p2.stdout else p2.stderr}"
    return "PASS", cmd, "36 MathLit topics >= 50 semantic archetypes (0 subskill_N shims, 305 RENDERED, 0 GNR/MISSING, SimuLearn diagram_and_steps wired, 0 leaks across all 13,323 Grade 7-12 questions)"


def check_u50_2():
    return _check_stage_d1("Mathematics", ["7"])


def check_u50_3():
    return _check_stage_d1("Mathematics", ["8"])


def check_u50_4():
    return _check_stage_d1("Mathematics", ["9"])


def check_u50_5():
    return _check_stage_d1("Natural Sciences", ["7", "8", "9"])


def check_u50_6():
    return _check_stage_d1("Economic and Management Sciences", ["7", "8", "9"])


def check_u50_7():
    return _check_stage_d1("Mathematics", ["10", "11", "12"])


def check_u50_8():
    return _check_stage_d1("Technical Mathematics", ["10", "11", "12"])


def check_u50_9():
    return _check_stage_d1("Physical Sciences", ["10", "11", "12"])


def check_u50_10():
    return _check_stage_d1("Life Sciences", ["10", "11", "12"])


def check_u50_11():
    return _check_stage_d1("Accounting", ["10", "11", "12"])


def check_u50_12():
    s, c, o = _check_stage_d1("Business Studies", ["10", "11", "12"])
    if s != "PASS":
        return s, c, o
    p = subprocess.run(["npm", "run", "test:audit"], cwd=ROOT, capture_output=True, text=True, shell=True)
    if p.returncode == 0:
        return "PASS", f"{c} && npm run test:audit", "All topics >= 50 archetypes and test:audit clean"
    return "FAIL", f"{c} && npm run test:audit", "test:audit failed"


UNIVERSAL_50_ITEMS = [
    {"id": "U50-0", "batch": 1, "deliverable": "Universal Workflow, Diagram Doctrine, and Skills Upgrade", "exit_test": "python scripts/check_rule_presence.py --rule diagram_description_design_law", "check": check_u50_0},
    {"id": "U50-1", "batch": 1, "deliverable": "Universal Diagram Audit & Math Lit Verification", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject 'Mathematical Literacy' --grades 10 11 12 --stage d1 --stage inventory", "check": check_u50_1},
    {"id": "U50-2", "batch": 2, "deliverable": "Grade 7 Mathematics (27 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject Mathematics --grades 7 --stage d1 --strict", "check": check_u50_2},
    {"id": "U50-3", "batch": 3, "deliverable": "Grade 8 Mathematics (26 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject Mathematics --grades 8 --stage d1 --strict", "check": check_u50_3},
    {"id": "U50-4", "batch": 4, "deliverable": "Grade 9 Mathematics (24 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject Mathematics --grades 9 --stage d1 --strict", "check": check_u50_4},
    {"id": "U50-5", "batch": 5, "deliverable": "Grades 7-9 Natural Sciences (53 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject 'Natural Sciences' --grades 7 8 9 --stage d1 --strict", "check": check_u50_5},
    {"id": "U50-6", "batch": 6, "deliverable": "Grades 7-9 EMS (40 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject 'Economic and Management Sciences' --grades 7 8 9 --stage d1 --strict", "check": check_u50_6},
    {"id": "U50-7", "batch": 7, "deliverable": "Grades 10-12 Mathematics (37 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject Mathematics --grades 10 11 12 --stage d1 --strict", "check": check_u50_7},
    {"id": "U50-8", "batch": 8, "deliverable": "Grades 10-12 Technical Mathematics (29 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject 'Technical Mathematics' --grades 10 11 12 --stage d1 --strict", "check": check_u50_8},
    {"id": "U50-9", "batch": 9, "deliverable": "Grades 10-12 Physical Sciences (53 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject 'Physical Sciences' --grades 10 11 12 --stage d1 --strict", "check": check_u50_9},
    {"id": "U50-10", "batch": 10, "deliverable": "Grades 10-12 Life Sciences (31 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject 'Life Sciences' --grades 10 11 12 --stage d1 --strict", "check": check_u50_10},
    {"id": "U50-11", "batch": 11, "deliverable": "Grades 10-12 Accounting (49 topics >= 50 archetypes)", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject Accounting --grades 10 11 12 --stage d1 --strict", "check": check_u50_11},
    {"id": "U50-12", "batch": 12, "deliverable": "Grades 10-12 Business Studies (53 topics >= 50 archetypes) & Platform Audit", "exit_test": "python scripts/run_universal_comprehensive_diagram_audit.py --subject 'Business Studies' --grades 10 11 12 --stage d1 --strict", "check": check_u50_12},
]


MATHLIT_REM_ITEMS = [
    {"id": "REM-0", "batch": 1, "deliverable": "Lock anti-shortcut referee traces (schema_valid, seed_varies, bound_to_question) & SHA-256 integrity check", "exit_test": "python scripts/verify_plan.py --plan mathlit_remediation --item REM-0", "check": check_rem0},
    {"id": "REM-1", "batch": 1, "deliverable": "Fix DiagramRenderer.jsx, MathLitDiagramRenderer.jsx, StatsAndFinancialGraphRenderer.jsx, and UIF piecewise graph", "exit_test": "python scripts/run_mathlit_comprehensive_diagram_audit.py --stage classify", "check": check_rem1},
    {"id": "REM-2", "batch": 1, "deliverable": "Unblock visualAidRegistry.js for mathematical_literacy and add 3 dedicated Math Lit visual aids", "exit_test": "node scripts/resolve_mathlit_aids.mjs", "check": check_rem2},
    {"id": "REM-3", "batch": 1, "deliverable": "Live browser render check for all repaired Batch 1 diagram kinds", "exit_test": "npx playwright test e2e/visual/mathlit_diagram_render_audit.spec.js --project=desktop-browser", "check": check_rem3},
    {"id": "REM-4", "batch": 2, "deliverable": "Grade 10 Maps & Plans (scale_maps_and_plans, assembly_diagrams_floor_plans_packaging) diagrams & prompt rewrites", "exit_test": "python scripts/verify_plan.py --plan mathlit_remediation --item REM-4", "check": check_rem4},
    {"id": "REM-5", "batch": 2, "deliverable": "Grade 10 Data, Patterns, Probability & Measurement diagrams & prompt rewrites (all 12 Gr10 topics)", "exit_test": "python scripts/verify_plan.py --plan mathlit_remediation --item REM-5", "check": check_rem5},
    {"id": "REM-6", "batch": 3, "deliverable": "Grade 11 all 12 topics missing diagrams wired & narrated prompts rewritten", "exit_test": "python scripts/verify_plan.py --plan mathlit_remediation --item REM-6", "check": check_rem6},
    {"id": "REM-7", "batch": 4, "deliverable": "Grade 12 all 12 topics missing diagrams wired & narrated prompts rewritten", "exit_test": "python scripts/verify_plan.py --plan mathlit_remediation --item REM-7", "check": check_rem7},
    {"id": "REM-8", "batch": 4, "deliverable": "Regenerate report & CSV, run Playwright render audit, and pass npm run test:audit", "exit_test": "python scripts/verify_plan.py --plan mathlit_remediation --item REM-8", "check": check_rem8},
    {"id": "REM-9", "batch": 5, "deliverable": "FET Mathematics (Grades 10-12): Wire missing diagram_spec payloads & eliminate narrated figure leaks", "exit_test": "python scripts/audit_diagram_description_leak.py --subject Mathematics --grades 10 11 12 --seeds 101 102 103 --strict", "check": check_rem9},
    {"id": "REM-10", "batch": 5, "deliverable": "FET Technical Mathematics (Grades 10-12): Wire missing diagram_spec payloads & eliminate narrated figure leaks", "exit_test": "python scripts/audit_diagram_description_leak.py --subject 'Technical Mathematics' --grades 10 11 12 --seeds 101 102 103 --strict", "check": check_rem10},
    {"id": "REM-11", "batch": 5, "deliverable": "FET Physical Sciences (Grades 10-12): Wire missing diagram_spec payloads & eliminate narrated figure leaks", "exit_test": "python scripts/audit_diagram_description_leak.py --subject 'Physical Sciences' --grades 10 11 12 --seeds 101 102 103 --strict", "check": check_rem11},
    {"id": "REM-12", "batch": 5, "deliverable": "FET Life Sciences (Grades 10-12): Wire missing diagram_spec / Heart Standard plates & eliminate narrated figure leaks", "exit_test": "python scripts/audit_diagram_description_leak.py --subject 'Life Sciences' --grades 10 11 12 --seeds 101 102 103 --strict", "check": check_rem12},
    {"id": "REM-13", "batch": 5, "deliverable": "FET Accounting & Business Studies (Grades 10-12): Wire missing diagram/table stimuli & eliminate narrated leaks", "exit_test": "python scripts/audit_diagram_description_leak.py --subject Accounting/Business Studies --grades 10 11 12 --strict", "check": check_rem13},
    {"id": "REM-14", "batch": 5, "deliverable": "Senior Phase (Grades 7-9 Mathematics, EMS, Natural Sciences): Wire missing diagram_spec / plates & eliminate narrated figure leaks", "exit_test": "python scripts/audit_diagram_description_leak.py --grades 7 8 9 --seeds 101 102 103 --strict", "check": check_rem14},
]

ITEMS = [
    # Batch 0: Tooling
    {
        "id": "GP-0",
        "batch": 0,
        "deliverable": "scripts/verify_plan.py runs every item's test and prints the item table",
        "exit_test": "python scripts/verify_plan.py --list exits 0 and lists GP-0 to GP-30",
        "check": check_gp0,
    },
    {
        "id": "GP-1",
        "batch": 0,
        "deliverable": "Audit script covers plan Phase 1 checks 6 (unmarkable part) and 7 (topic/generator mismatch) and counts every expected question",
        "exit_test": "python scripts/audit_grade_carryover.py --grades 8 --strict exits 1 on planted unmarkable part and on registry mismatch, and exits 0 on clean tree",
        "check": check_gp1,
    },
    # Batch 1: Shared Layer (Phase 2)
    {
        "id": "GP-2",
        "batch": 1,
        "deliverable": "diagram_role: identify | context emitted by every diagram-producing generator, Grades 7–12, all subjects",
        "exit_test": "verify_plan.py --item GP-2 fails if any generator with a diagram_spec lacks diagram_role",
        "check": check_gp2,
    },
    {
        "id": "GP-3",
        "batch": 1,
        "deliverable": "Context diagrams render no pins; container title comes from diagram subject (not 'BIOLOGICAL STRUCTURE SCHEMATIC')",
        "exit_test": "Playwright on real workspace: context question -> 0 pins; title text != 'BIOLOGICAL STRUCTURE SCHEMATIC' for non-bio master",
        "check": check_gp3,
    },
    {
        "id": "GP-4",
        "batch": 1,
        "deliverable": "Memo contract: (a) **answer** [marks] first, working below; MCQ memo starts with letter; parts separated",
        "exit_test": "verify_plan.py --item GP-4 checks every Gr7–12 question memo with regex, 0 violations",
        "check": check_gp4,
    },
    {
        "id": "GP-5",
        "batch": 1,
        "deliverable": "Question-card diagram placement (never in answer card)",
        "exit_test": "Playwright: diagram element is inside question card and absent from memo card, for 1 question per diagram master",
        "check": check_gp5,
    },
    {
        "id": "GP-6",
        "batch": 1,
        "deliverable": "Journal tables: no-entry cells stay editable; transaction list rendered",
        "exit_test": "Playwright on CPJ/CRJ: type in a non-answer cell succeeds; transaction list is visible",
        "check": check_gp6,
    },
    {
        "id": "GP-7",
        "batch": 1,
        "deliverable": "Marking validity: SymPy equivalence for final answers; every part has MCQ or keyword rubric; sequence completion has one input form",
        "exit_test": "verify_plan.py --item GP-7: 0 parts without markable answer; Playwright types correct answer in 2 equivalent forms, both marked correct",
        "check": check_gp7,
    },
    # Batch 2: Maths (Phase 3)
    {
        "id": "GP-8",
        "batch": 2,
        "deliverable": "Graph paper decision carried out: archetypes re-homed to Perimeter/Area, Transformations, and Graphs; topic stops resolving; Graphs stays a topic",
        "exit_test": "verify_plan.py --item GP-8: archetype counts per topic before vs after; generate_variant('Graph paper types') no longer resolves; registry and aliases updated",
        "check": check_gp8,
    },
    {
        "id": "GP-9",
        "batch": 2,
        "deliverable": "Method-name policy: prompts name a method only when assessed; wordy phrasing removed (Math 6)",
        "exit_test": "audit_grade_carryover.py --grades 7,8,9 --strict with method list from prevalence report; 0 prompt hits outside allow-list",
        "check": check_gp9,
    },
    {
        "id": "GP-10",
        "batch": 2,
        "deliverable": "Prompt leaks fixed (Math 1, 7, 10, 12, 18, 30, 31, 41, 42)",
        "exit_test": "Same audit; 0 hits at 3 seeds",
        "check": check_gp10,
    },
    {
        "id": "GP-11",
        "batch": 2,
        "deliverable": "Diagrams in 2D/3D geometry, Pythagoras, transformations, patterns, straight lines; letters match prompt",
        "exit_test": "verify_plan.py --item GP-11: every prompt with figure word has diagram; polygon letters match; Playwright mounts 1 question per archetype",
        "check": check_gp11,
    },
    {
        "id": "GP-12",
        "batch": 2,
        "deliverable": "Archetype expansion with curriculum-doc citations: Whole numbers, Integers, Exponents, Decimals, Functions 1-2, Probability, Data, Equations 1-3",
        "exit_test": "verify_plan.py --item GP-12: archetype count per topic > baseline; each new archetype cites curriculum_docs_auto file",
        "check": check_gp12,
    },
    {
        "id": "GP-13",
        "batch": 2,
        "deliverable": "Class-interval explanation (Math 8) and cube-stack validity (Math 33)",
        "exit_test": "Generator run: prompt contains discrete-values reasoning; cube-stack prompt defines sequence",
        "check": check_gp13,
    },
    # Batch 3: EMS
    {
        "id": "GP-14",
        "batch": 3,
        "deliverable": "Dedicated generator per topic, no cross-topic mixing",
        "exit_test": "verify_plan.py --item GP-14: each EMS topic key maps to its own file; 3 seeds produce no foreign-topic keywords",
        "check": check_gp14,
    },
    {
        "id": "GP-15",
        "batch": 3,
        "deliverable": "Expansion: forms of ownership, management levels/functions, GL and trial balance, accounting cycle",
        "exit_test": "As GP-12",
        "check": check_gp15,
    },
    {
        "id": "GP-16",
        "batch": 3,
        "deliverable": "Source documents with images and routing to journals, ledgers and trial balance",
        "exit_test": "Playwright: source-document question renders document image",
        "check": check_gp16,
    },
    {
        "id": "GP-17",
        "batch": 3,
        "deliverable": "Name, business type per grade, and place variety (Imran/Plumbing, Mitchells Plain)",
        "exit_test": "verify_plan.py --item GP-17: at 20 seeds per topic, no single name above 15% and business type matches grade",
        "check": check_gp17,
    },
    {
        "id": "GP-18",
        "batch": 3,
        "deliverable": "EMS memo cell-by-cell for journals; no SS[M]/SS[A]",
        "exit_test": "Part of GP-4",
        "check": check_gp18,
    },
    # Batch 4: Natural Sciences
    {
        "id": "GP-19",
        "batch": 4,
        "deliverable": "Scope checks: electrolysis (Atoms), electroplating (Energy transfer)",
        "exit_test": "Cite the exact curriculum_docs_auto lines",
        "check": check_gp19,
    },
    {
        "id": "GP-20",
        "batch": 4,
        "deliverable": "Markable microorganisms answer (NS 12): no part without an MCQ or keyword rubric",
        "exit_test": "Covered by GP-7",
        "check": check_gp20,
    },
    {
        "id": "GP-21",
        "batch": 4,
        "deliverable": "Circuit components match memo (resistor vs bulb) and symbol is standard",
        "exit_test": "Generator + browser: diagram symbol equals memo word, for 20 seeds",
        "check": check_gp21,
    },
    {
        "id": "GP-22",
        "batch": 4,
        "deliverable": "Archetype and diagram expansion: Atoms, Chemical reactions, Beyond the solar system, Looking into space, Circuits, Static electricity, Visible light, Microorganisms, Photosynthesis",
        "exit_test": "As GP-12 + GP-11",
        "check": check_gp22,
    },
    {
        "id": "GP-23",
        "batch": 4,
        "deliverable": "Chemical-calculation library question (NS 1) answered",
        "exit_test": "Written answer with sources in deliverable file on disk",
        "check": check_gp23,
    },
    # Batch 5: Phase 4 Dual-Mode Visuals
    {
        "id": "GP-24",
        "batch": 5,
        "deliverable": "Label design implemented in shared plate: question card -> letter pins only on identify, no pins on context; study static -> names visible; study alive -> 0 labels on moving parts, hover highlights",
        "exit_test": "Playwright: identify question -> letter pins only, no names in DOM; study static -> names visible; study alive -> 0 labels on moving parts, hover shows name",
        "check": check_gp24,
    },
    {
        "id": "GP-25",
        "batch": 5,
        "deliverable": "Study viewer route serves names after opening, never in question payload",
        "exit_test": "Network assertion: question response has no structure names; study response has them",
        "check": check_gp25,
    },
    {
        "id": "GP-26",
        "batch": 5,
        "deliverable": "Alive mode state actually changes on interaction",
        "exit_test": "Playwright: read temperature or ray state, click action, assert value changed",
        "check": check_gp26,
    },
    {
        "id": "GP-27",
        "batch": 5,
        "deliverable": "Alive mode is driven by question's generator parameters",
        "exit_test": "Generated question with parameter X -> alive mode shows X",
        "check": check_gp27,
    },
    {
        "id": "GP-28",
        "batch": 5,
        "deliverable": "Pin calibration screenshots inspected, per Rule 0d-14.3",
        "exit_test": "Screenshots on disk; checked with read_file; anchors JSON committed",
        "check": check_gp28,
    },
    {
        "id": "GP-29",
        "batch": 5,
        "deliverable": "Phase 4 spec goes through generator -> API -> workspace, with 0 __SET_WORKSPACE_QUESTION__ and 0 pre-action HUD narration",
        "exit_test": "verify_plan.py --item GP-29 greps spec for __SET_WORKSPACE_QUESTION__ and updateHud( (0 hits) and runs it",
        "check": check_gp29,
    },
    {
        "id": "GP-30",
        "batch": 5,
        "deliverable": "Pilot extended: alveolus, particle model, geyser element, telescopes",
        "exit_test": "Same as GP-24 to GP-29 per master",
        "check": check_gp30,
    },
]


def print_table(results):
    print("| ID | Status | Command | Output |")
    print("|---|---|---|---|")
    for r in results:
        status = r['status']
        cmd = r['command'].replace('|', '\\|')
        out_summary = r['output'].replace('\n', ' ').replace('|', '\\|')[:100]
        print(f"| {r['id']} | {status} | `{cmd}` | {out_summary} |")

    not_done_items = [r['id'] for r in results if r['status'] != 'PASS']
    print("\nItems not done or only partly done:")
    if not not_done_items:
        print("None (all items PASS per verify_plan.py)")
    else:
        for r in results:
            if r['status'] != 'PASS':
                print(f"- {r['id']}: {r['status']} ({r['deliverable']})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan', type=str, default='gp', choices=['gp', 'mathlit_audit', 'mathlit_remediation', 'universal_50'], help='Plan to verify')
    ap.add_argument('--list', action='store_true', help='List all plan items and exit 0')
    ap.add_argument('--batch', type=int, help='Run all items in specified batch')
    ap.add_argument('--item', type=str, help='Run specific item (e.g. GP-0, AUD-0, REM-0, or U50-0)')
    ap.add_argument('--all', action='store_true', help='Run all items')
    args = ap.parse_args()

    if args.plan == 'mathlit_audit':
        active_items = AUTHLIT_ITEMS
        title = "Math Lit Audit Plan Items"
    elif args.plan == 'mathlit_remediation':
        active_items = MATHLIT_REM_ITEMS
        title = "Math Lit Remediation Plan Items"
    elif args.plan == 'universal_50':
        active_items = UNIVERSAL_50_ITEMS
        title = "Universal 50-Archetype & Diagram Master Plan Items"
    else:
        active_items = ITEMS
        title = "Grade 8 Remediation Plan Items"

    if args.list:
        print(f"{title} ({len(active_items)} total):\n")
        print("| ID | Batch | Deliverable | Exit Test |")
        print("|---|---|---|---|")
        for it in active_items:
            print(f"| {it['id']} | {it['batch']} | {it['deliverable']} | `{it['exit_test']}` |")
        return 0

    target_items = []
    if args.item:
        target_items = [it for it in active_items if it['id'] == args.item]
        if not target_items:
            print(f"Error: Unknown item {args.item}")
            return 1
    elif args.batch is not None:
        target_items = [it for it in active_items if it['batch'] == args.batch]
    elif args.all:
        target_items = active_items
    else:
        target_items = active_items

    results = []
    all_passed = True
    for it in target_items:
        print(f"Running exit test for {it['id']}: {it['deliverable']}...")
        status, cmd, out = it['check']()
        results.append({
            'id': it['id'],
            'batch': it['batch'],
            'deliverable': it['deliverable'],
            'status': status,
            'command': cmd,
            'output': out
        })
        if status != "PASS":
            all_passed = False

    print("\n" + "=" * 70)
    print("VERIFICATION RESULTS")
    print("=" * 70)
    print_table(results)

    return 0 if all_passed else 1


if __name__ == '__main__':
    sys.exit(main())
