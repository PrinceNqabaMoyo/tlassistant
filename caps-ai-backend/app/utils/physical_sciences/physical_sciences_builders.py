"""Physical Sciences Grade 10-12 & Technical/Mathematical Literacy Diagram Subskill Builders.

Provides deterministic, 3-layer subskill builders for:
Role L (Identification & Functional Callout Labelling):
- Periodic Transverse Wave Profile (transverse_wave) - Grade 10 Term 1 Waves, Sound & Light
- Doppler Effect Wavefronts (doppler_effect) - Grade 12 Term 2 Waves, Sound & Light

Role C (Quantitative Calculation & Step-by-Step Derivation, ZERO A-D Pins):
- Bohr-Rutherford Atomic Structure (atomic_bohr_structure) - Grade 10 Term 1 Matter & Materials
- Mechanical & Hydraulic Systems (hydraulic_gears_belt_pulley) - Grade 10 Technical Mathematics
- Architectural Floor Plan & Scale (architectural_floor_packaging_plan) - Grade 10/11 Mathematical Literacy
- Chemical Bonding & Molecular Geometry (chemical_bonding_molecules) - Grade 11 Term 1 Matter & Materials
- Two-Body Inclined Plane & Pulley System (pulley_incline_masses_system) - Grade 11 Term 1 Mechanics
- Acid-Base Titration Stoichiometry (titration_apparatus) - Grade 11/12 Chemical Change
- Galvanic Electrochemical Cell EMF (galvanic_cell) - Grade 12 Term 3 Electrochemistry
- Electrolytic Cell Decomposition (electrolytic_cell_apparatus) - Grade 12 Term 3 Electrochemistry
- Gas Evolution & Reaction Rate Kinetics (gas_evolution_rate_apparatus) - Grade 12 Term 2 Chemical Change
- Electrodynamics AC Generator RMS (ac_dc_generator_motor_apparatus) - Grade 12 Term 3 Electrodynamics

Strictly complies with the 6-Pillar Generator Contract, Rule R9 (Role C vs Role L), and Rule R2 (Zero LaTeX/Markdown Leaks).
"""

from __future__ import annotations

import json
import math
import os
import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

ANCHORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "diagram_anchors",
)


def _load_anchors(master_name: str) -> Dict[str, Any]:
    path = os.path.join(ANCHORS_DIR, f"{master_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


GALVANIC_DATA = _load_anchors("galvanic_cell")
TITRATION_DATA = _load_anchors("titration_apparatus")
TRANSVERSE_DATA = _load_anchors("transverse_wave")
DOPPLER_DATA = _load_anchors("doppler_effect")
ATOMIC_BOHR_DATA = _load_anchors("atomic_bohr_structure")
CHEMICAL_BONDING_DATA = _load_anchors("chemical_bonding_molecules")
ELECTROLYTIC_CELL_DATA = _load_anchors("electrolytic_cell_apparatus")
GAS_EVOLUTION_DATA = _load_anchors("gas_evolution_rate_apparatus")
PULLEY_INCLINE_DATA = _load_anchors("pulley_incline_masses_system")
AC_DC_GENERATOR_DATA = _load_anchors("ac_dc_generator_motor_apparatus")
HYDRAULIC_GEARS_DATA = _load_anchors("hydraulic_gears_belt_pulley")
ARCHITECTURAL_PLAN_DATA = _load_anchors("architectural_floor_packaging_plan")


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ps_salt"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _landmarks_from_data(data: Dict[str, Any], keys: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    anchors = data.get("anchors", {})
    chosen = keys if keys else list(anchors.keys())[:4]
    out: List[Dict[str, Any]] = []
    for k in chosen:
        if k in anchors:
            cfg = anchors[k]
            name = cfg.get("name") or cfg.get("acceptable", [k])[0]
            out.append({
                "name": name,
                "text": name,
                "anchor": cfg["anchor"],
                "default_box": cfg["default_box"],
                "side": cfg["side"],
                "role": "landmark",
            })
    return out


def _make_role_c_payload(
    *,
    qid: str,
    master_name: str,
    grade: int,
    term: int,
    mode: str,
    prompt: str,
    worked_solution: str,
    marking_points: List[Dict[str, Any]],
    hints: Dict[str, str],
    misconception_tags: List[str],
    landmarks: List[Dict[str, Any]],
) -> Dict[str, Any]:
    grade_str = f"g{grade}"
    total_marks = sum(int(mp.get("marks", 1)) for mp in marking_points)
    diagram_spec = {
        "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
        "master": master_name,
        "image_type": master_name,
        "view": "textbook",
        "grade_mask": grade_str,
        "viewBox": "0 0 600 480",
        "state": "static",
        "pins": [],
        "landmarks": landmarks,
    }
    return {
        "id": qid,
        "question_id": qid,
        "term": term,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "mode": mode,
        "question_type": "short_answer",
        "modality": "bio_diagram",
        "diagram_spec": diagram_spec,
        "diagram_meta": {
            "master": master_name,
            "view": "textbook",
            "grade_mask": grade_str,
        },
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": worked_solution,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "marks": total_marks,
        "hints": hints,
        "misconception_tags": misconception_tags,
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _build_generic_ps_question(
    data: Dict[str, Any],
    master_name: str,
    component_name: str,
    seed: int,
    grade: int,
    term: int,
    qid_prefix: str,
    subskill_choices: List[str],
    subskill: Optional[str] = None,
    mode: str = "practice",
) -> Dict[str, Any]:
    """Role L builder for Transverse Wave and Doppler Effect Wavefronts."""
    r = random.Random(seed)
    anchors = data["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [
        k for k, v in anchors.items()
        if grade_str in v.get("grades", [grade_str])
    ]
    if len(allowed_keys) < 4:
        allowed_keys = list(anchors.keys())

    if subskill is None or subskill not in subskill_choices:
        subskill = subskill_choices[seed % len(subskill_choices)]

    target_key = allowed_keys[seed % len(allowed_keys)]
    target = anchors[target_key]
    target_name = target.get("name") or target.get("acceptable", [target_key])[0]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    active_keys = [target_key] + other_keys[:3]
    r.shuffle(active_keys)

    pin_letters = ["A", "B", "C", "D"]
    client_pins: List[Dict[str, Any]] = []
    server_solution_map: Dict[str, str] = {}
    target_pin_letter = ""

    for idx, key in enumerate(active_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, key, idx)
        if key == target_key:
            target_pin_letter = letter

        akey_name = anchors[key].get("name") or anchors[key].get("acceptable", [key])[0]
        server_solution_map[letter] = akey_name
        client_pins.append({
            "pin": letter,
            "ref": ref,
            "anchor": anchors[key]["anchor"],
            "default_box": anchors[key]["default_box"],
            "side": anchors[key]["side"],
            "role": "target" if key == target_key else "distractor",
        })

    if subskill == "identification":
        prompt = (
            f"Refer to the diagram of the {component_name}.\n\n"
            f"1. Identify the wave feature or region indicated by callout ({target_pin_letter}). (1)\n"
            f"2. Define or state the physical significance of this feature. (2)"
        )
        worked_solution = (
            f"1. Callout ({target_pin_letter}): {target_name}.\n"
            f"2. Physical significance: {target['description']}"
        )
        marks = 3
        misconception_tag = f"{master_name}_identification_error"
        marking_schema = {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"1. Correct identification of callout ({target_pin_letter}): {target_name}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"2. Physical definition / significance: {target['description']}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "none",
        }
    else:
        prompt = (
            f"Refer to the diagram of the {component_name}.\n\n"
            f"1. Which callout letter (A, B, C, or D) represents the feature described below? (1)\n"
            f"   \"{target['description']}\"\n"
            f"2. State the full scientific name of this feature. (1)"
        )
        worked_solution = (
            f"1. Callout letter: {target_pin_letter}\n"
            f"2. Feature name: {target_name} ({target['description']})"
        )
        marks = 2
        misconception_tag = f"{master_name}_functional_role_confusion"
        marking_schema = {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"1. Selection of callout ({target_pin_letter})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"2. Scientific name: {target_name}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "none",
        }

    hints = {
        "tier_1": f"Observe where callout ({target_pin_letter}) points on the {component_name} diagram.",
        "tier_2": f"Consider the physical definition: {target['description'][:80]}...",
        "tier_3": worked_solution,
    }

    qid = f"{qid_prefix}_{seed}_{subskill}_{target_key}"

    diagram_spec = {
        "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
        "master": master_name,
        "image_type": master_name,
        "view": "textbook",
        "grade_mask": grade_str,
        "viewBox": "0 0 600 480",
        "state": "static",
        "pins": client_pins,
        "landmarks": [],
        "target_pin": target_pin_letter,
        "target_key": target_key,
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": term,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4 if mode == "scaffold" else 3,
        "mode": mode,
        "question_type": "short_answer",
        "modality": "bio_diagram",
        "diagram_spec": diagram_spec,
        "diagram_meta": {
            "master": master_name,
            "view": "textbook",
            "grade_mask": grade_str,
            "target_pin": target_pin_letter,
            "target_key": target_key,
        },
        "question": prompt,
        "question_text": prompt,
        "correct_answer": worked_solution,
        "sample_answer": worked_solution,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [misconception_tag],
        "marking_schema": marking_schema,
        "_solution_map": server_solution_map,
    }


# ============================================================================
# ROLE L BUILDERS (Transverse Wave & Doppler Wavefronts)
# ============================================================================

def build_transverse_wave_question(
    seed: int,
    grade: int = 10,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    return _build_generic_ps_question(
        data=TRANSVERSE_DATA,
        master_name="transverse_wave",
        component_name="Periodic Transverse Wave Profile",
        seed=seed,
        grade=grade,
        term=1,
        qid_prefix="ps10_transverse",
        subskill_choices=["identification", "function"],
        subskill=subskill,
        mode=mode,
    )


def build_doppler_effect_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    return _build_generic_ps_question(
        data=DOPPLER_DATA,
        master_name="doppler_effect",
        component_name="Doppler Effect Wavefront Propagation",
        seed=seed,
        grade=grade,
        term=2,
        qid_prefix="ps12_doppler",
        subskill_choices=["identification", "function"],
        subskill=subskill,
        mode=mode,
    )


# ============================================================================
# ROLE C BUILDERS (Quantitative / Derivation, ZERO A-D Pins)
# ============================================================================

def build_atomic_bohr_structure_question(
    seed: int,
    grade: int = 10,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 10 Atomic Structure, Isotopes, sp-Notation & Relative Atomic Mass."""
    r = random.Random(seed)
    isotopes = [
        {"elem": "Chlorine", "sym": "Cl", "z": 17, "a1": 35, "p1": 75, "a2": 37, "p2": 25, "sp": "1s² 2s² 2p⁶ 3s² 3p⁵", "val": 7, "ion": "Cl⁻"},
        {"elem": "Magnesium", "sym": "Mg", "z": 12, "a1": 24, "p1": 79, "a2": 25, "p2": 21, "sp": "1s² 2s² 2p⁶ 3s²", "val": 2, "ion": "Mg²⁺"},
        {"elem": "Boron", "sym": "B", "z": 5, "a1": 10, "p1": 20, "a2": 11, "p2": 80, "sp": "1s² 2s² 2p¹", "val": 3, "ion": "B³⁺"},
        {"elem": "Neon", "sym": "Ne", "z": 10, "a1": 20, "p1": 90, "a2": 22, "p2": 10, "sp": "1s² 2s² 2p⁶", "val": 8, "ion": "Ne (noble gas)"},
    ]
    iso = isotopes[seed % len(isotopes)]
    n1 = iso["a1"] - iso["z"]
    ram = round((iso["a1"] * iso["p1"] + iso["a2"] * iso["p2"]) / 100.0, 2)

    prompt = (
        f"Refer to the Bohr-Rutherford atomic structure diagram showing concentric quantized electron energy shells around the central nucleus.\n"
        f"An element {iso['elem']} (\\(\\text{{{iso['sym']}}}, Z = {iso['z']}\\)) occurs naturally as two isotopes: "
        f"\\({iso['elem']}-{iso['a1']}\\) ({iso['p1']}% abundance) and \\({iso['elem']}-{iso['a2']}\\) ({iso['p2']}% abundance).\n\n"
        f"1. Determine the number of protons, neutrons, and electrons in a neutral atom of \\({iso['elem']}-{iso['a1']}\\). (2)\n"
        f"2. Write down the ground-state spectroscopic electron configuration (\\(sp\\)-notation) for a neutral \\(\\text{{{iso['sym']}}}\\) atom and state its number of valence electrons. (2)\n"
        f"3. Calculate the relative atomic mass (\\(A_r\\)) of {iso['elem']} in \\(\\text{{g}}\\cdot\\text{{mol}}^{{-1}}\\). (2)"
    )

    sol = (
        f"Step 1: Subatomic particle counts for neutral {iso['elem']}-{iso['a1']} (Z = {iso['z']}, A = {iso['a1']}):\n"
        f"- Protons = Z = {iso['z']}\n"
        f"- Electrons = {iso['z']} (neutral atom)\n"
        f"- Neutrons = A - Z = {iso['a1']} - {iso['z']} = {n1}\n\n"
        f"Step 2: Ground-state sp-notation and valence electrons:\n"
        f"- Electron configuration: {iso['sp']}\n"
        f"- Valence electrons in outer shell: {iso['val']}\n\n"
        f"Step 3: Relative atomic mass (A_r) calculation:\n"
        f"A_r = [({iso['a1']} × {iso['p1']}) + ({iso['a2']} × {iso['p2']}) ] ÷ 100\n"
        f"A_r = ({iso['a1'] * iso['p1']} + {iso['a2'] * iso['p2']}) ÷ 100 = {_fmt_sa(ram)} g·mol⁻¹"
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Protons = {iso['z']}, Electrons = {iso['z']}, Neutrons = {iso['a1']} - {iso['z']} = {n1}", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. sp-notation: {iso['sp']} and valence electrons = {iso['val']}", "marks": 2, "editable": True},
        {"id": "mp_3", "desc": f"3. Relative atomic mass A_r = [({iso['a1']}×{iso['p1']}) + ({iso['a2']}×{iso['p2']})]/100 = {_fmt_sa(ram)} g·mol⁻¹", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "In a neutral atom, protons = electrons = atomic number Z, and neutrons = mass number A - Z.",
        "tier_2": f"Fill orbitals in order 1s, 2s, 2p, 3s, 3p for {iso['z']} electrons, then weight each isotope mass by its percentage abundance.",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_bohr_{seed}",
        master_name="atomic_bohr_structure",
        grade=grade,
        term=1,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["confused_mass_number_and_neutrons", "incorrect_orbital_filling_order"],
        landmarks=_landmarks_from_data(ATOMIC_BOHR_DATA),
    )


def build_chemical_bonding_molecules_question(
    seed: int,
    grade: int = 11,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 11 Chemical Bonding, Electronegativity ΔEN, VSEPR Geometry & Polarity."""
    molecules = [
        {
            "formula": "H₂O",
            "name": "water",
            "central": "O",
            "ligand": "H",
            "en_c": 3.5,
            "en_l": 2.1,
            "bp": 2,
            "lp": 2,
            "shape": "Angular (Bent)",
            "angle": "104,5°",
            "polarity": "Polar molecule (asymmetrical bent geometry with net dipole moment toward oxygen)",
            "imf": "Hydrogen bonding (strong dipole-dipole attraction)",
        },
        {
            "formula": "NH₃",
            "name": "ammonia",
            "central": "N",
            "ligand": "H",
            "en_c": 3.0,
            "en_l": 2.1,
            "bp": 3,
            "lp": 1,
            "shape": "Trigonal pyramidal",
            "angle": "107°",
            "polarity": "Polar molecule (asymmetrical trigonal pyramidal shape with lone pair on nitrogen; net dipole does not cancel)",
            "imf": "Hydrogen bonding",
        },
        {
            "formula": "CO₂",
            "name": "carbon dioxide",
            "central": "C",
            "ligand": "O",
            "en_c": 2.5,
            "en_l": 3.5,
            "bp": 2,
            "lp": 0,
            "shape": "Linear",
            "angle": "180°",
            "polarity": "Non-polar molecule (symmetrical linear geometry causes the two equal C=O bond dipoles to cancel out)",
            "imf": "London dispersion (induced dipole) forces",
        },
    ]
    mol = molecules[seed % len(molecules)]
    delta_en = round(abs(mol["en_c"] - mol["en_l"]), 1)

    prompt = (
        f"Refer to the molecular geometry and chemical bonding diagram.\n"
        f"Consider a molecule of {mol['name']} (\\(\\text{{{mol['formula']}}}\\)), given the Pauling electronegativities "
        f"\\(\\text{{EN}}({mol['central']}) = {_fmt_sa(mol['en_c'], 1)}\\) and \\(\\text{{EN}}({mol['ligand']}) = {_fmt_sa(mol['en_l'], 1)}\\).\n\n"
        f"1. Calculate the electronegativity difference (\\(\\Delta\\text{{EN}}\\)) for a single \\(\\text{{{mol['central']}}}—\\text{{{mol['ligand']}}}\\) bond and classify the bond polarity. (2)\n"
        f"2. State the number of bonding electron domains and lone pairs around the central \\(\\text{{{mol['central']}}}\\) atom, and use VSEPR theory to state the molecular shape and bond angle. (2)\n"
        f"3. Deduce whether the overall \\(\\text{{{mol['formula']}}}\\) molecule is polar or non-polar, and name the dominant intermolecular force between \\(\\text{{{mol['formula']}}}\\) molecules. (2)"
    )

    sol = (
        f"Step 1: Electronegativity difference (ΔEN):\n"
        f"ΔEN = |{_fmt_sa(mol['en_c'], 1)} - {_fmt_sa(mol['en_l'], 1)}| = {_fmt_sa(delta_en, 1)} -> Polar covalent bond.\n\n"
        f"Step 2: VSEPR electron domains and molecular geometry around {mol['central']}:\n"
        f"- {mol['bp']} bonding domains and {mol['lp']} lone pair(s) around central {mol['central']} atom.\n"
        f"- Molecular shape: {mol['shape']} (bond angle ≈ {mol['angle']}).\n\n"
        f"Step 3: Overall molecular polarity and intermolecular forces:\n"
        f"- {mol['polarity']}.\n"
        f"- Dominant intermolecular force: {mol['imf']}."
    )

    mps = [
        {"id": "mp_1", "desc": f"1. ΔEN = |{_fmt_sa(mol['en_c'], 1)} - {_fmt_sa(mol['en_l'], 1)}| = {_fmt_sa(delta_en, 1)} (Polar covalent bond)", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. {mol['bp']} bonding domains, {mol['lp']} lone pair(s); VSEPR shape: {mol['shape']} ({mol['angle']})", "marks": 2, "editable": True},
        {"id": "mp_3", "desc": f"3. Molecular polarity ({mol['polarity']}) and IMF ({mol['imf']})", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "Subtract the two electronegativities to find ΔEN (0 < ΔEN < 2,1 indicates a polar covalent bond).",
        "tier_2": f"Count lone pairs on the central {mol['central']} atom to determine whether bond dipoles cancel out symmetrically.",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_bonding_{seed}",
        master_name="chemical_bonding_molecules",
        grade=grade,
        term=1,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["polar_bond_equals_polar_molecule", "omitted_lone_pair_repulsion"],
        landmarks=_landmarks_from_data(CHEMICAL_BONDING_DATA),
    )


def build_pulley_incline_masses_system_question(
    seed: int,
    grade: int = 11,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 11 Newton's Second Law Two-Body Inclined Plane & Pulley System."""
    configs = [
        {"m1": 4.0, "m2": 6.0, "theta": 30, "mu": 0.15},
        {"m1": 5.0, "m2": 8.0, "theta": 30, "mu": 0.20},
        {"m1": 3.0, "m2": 5.0, "theta": 25, "mu": 0.12},
    ]
    cfg = configs[seed % len(configs)]
    m1 = cfg["m1"]
    m2 = cfg["m2"]
    theta = cfg["theta"]
    mu = cfg["mu"]
    g = 9.8
    rad = math.radians(theta)
    fg_par = round(m1 * g * math.sin(rad), 2)
    fn = round(m1 * g * math.cos(rad), 2)
    fk = round(mu * fn, 2)
    fg2 = round(m2 * g, 2)
    a_sys = round((fg2 - fg_par - fk) / (m1 + m2), 2)
    tension = round(fg2 - m2 * a_sys, 2)

    prompt = (
        f"Refer to the two-body inclined plane and pulley system diagram.\n"
        f"Block 1 of mass \\(m_1 = {_fmt_sa(m1)}\\text{{ kg}}\\) rests on a rough incline angled at \\(\\theta = {theta}^\\circ\\) to the horizontal, "
        f"and is connected by a light inextensible string over a frictionless pulley to a hanging Block 2 of mass \\(m_2 = {_fmt_sa(m2)}\\text{{ kg}}\\). "
        f"When released, Block 1 accelerates up the incline. The coefficient of kinetic friction between Block 1 and the incline is \\(\\mu_k = {_fmt_sa(mu)}\\). (Take \\(g = 9,8\\text{{ m}}\\cdot\\text{{s}}^{{-2}}\\).)\n\n"
        f"1. Calculate the magnitude of the kinetic frictional force (\\(f_k\\)) acting on Block 1. (2)\n"
        f"2. Apply Newton's Second Law to both blocks to calculate the magnitude of the acceleration (\\(a\\)) of the system. (3)\n"
        f"3. Calculate the magnitude of the tension (\\(T\\)) in the connecting string. (2)"
    )

    sol = (
        f"Step 1: Calculate normal force N and kinetic friction f_k on Block 1:\n"
        f"N = m₁ g cos({theta}°) = {_fmt_sa(m1)} × 9,8 × cos({theta}°) = {_fmt_sa(fn)} N\n"
        f"f_k = μ_k N = {_fmt_sa(mu)} × {_fmt_sa(fn)} = {_fmt_sa(fk)} N down the incline.\n\n"
        f"Step 2: Apply Newton's Second Law (F_net = m a) to each block:\n"
        f"- Parallel weight component of Block 1: F_g∥ = m₁ g sin({theta}°) = {_fmt_sa(m1)} × 9,8 × sin({theta}°) = {_fmt_sa(fg_par)} N\n"
        f"- For Block 1 (up incline positive): T - F_g∥ - f_k = m₁ a => T - {_fmt_sa(fg_par)} - {_fmt_sa(fk)} = {_fmt_sa(m1)}a  ...(1)\n"
        f"- For Block 2 (downward positive): m₂ g - T = m₂ a => {_fmt_sa(fg2)} - T = {_fmt_sa(m2)}a  ...(2)\n"
        f"Adding (1) and (2): {_fmt_sa(fg2)} - {_fmt_sa(fg_par)} - {_fmt_sa(fk)} = ({_fmt_sa(m1)} + {_fmt_sa(m2)})a\n"
        f"a = {_fmt_sa(round(fg2 - fg_par - fk, 2))} ÷ {_fmt_sa(m1 + m2)} = {_fmt_sa(a_sys)} m·s⁻²\n\n"
        f"Step 3: Substitute a = {_fmt_sa(a_sys)} m·s⁻² into equation (2) to find tension T:\n"
        f"T = {_fmt_sa(fg2)} - ({_fmt_sa(m2)} × {_fmt_sa(a_sys)}) = {_fmt_sa(tension)} N"
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Normal force N = {_fmt_sa(fn)} N and kinetic friction f_k = μ_k N = {_fmt_sa(fk)} N", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. Simultaneous Newton II equations and system acceleration a = {_fmt_sa(a_sys)} m·s⁻²", "marks": 3, "editable": True},
        {"id": "mp_3", "desc": f"3. String tension T = {_fmt_sa(tension)} N", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "Resolve the weight of Block 1 into F_g⊥ = m₁ g cos(θ) and F_g∥ = m₁ g sin(θ).",
        "tier_2": "Write F_net = m a for Block 1 (T - F_g∥ - f_k = m₁ a) and Block 2 (m₂ g - T = m₂ a), then add the equations to eliminate T.",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_pulley_incline_{seed}",
        master_name="pulley_incline_masses_system",
        grade=grade,
        term=1,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["swapped_sin_and_cos_on_incline", "omitted_parallel_weight_component"],
        landmarks=_landmarks_from_data(PULLEY_INCLINE_DATA),
    )


def build_titration_apparatus_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 11/12 Acid-Base Titration Stoichiometry & pH Calculation."""
    scenarios = [
        {"ca": 0.12, "va_cm3": 25.0, "vb_cm3": 20.0},
        {"ca": 0.15, "va_cm3": 25.0, "vb_cm3": 25.0},
        {"ca": 0.10, "va_cm3": 20.0, "vb_cm3": 16.0},
    ]
    sc = scenarios[seed % len(scenarios)]
    ca = sc["ca"]
    va_cm3 = sc["va_cm3"]
    vb_cm3 = sc["vb_cm3"]
    va_dm3 = round(va_cm3 / 1000.0, 4)
    vb_dm3 = round(vb_cm3 / 1000.0, 4)
    na_mol = round(ca * va_dm3, 5)
    nb_mol = round(2 * na_mol, 5)
    cb = round(nb_mol / vb_dm3, 3)

    prompt = (
        f"Refer to the acid-base titration apparatus diagram showing a burette containing sodium hydroxide (\\(\\text{{NaOH}}\\)) "
        f"titrated into an Erlenmeyer flask containing standard sulfuric acid (\\(\\text{{H}}_2\\text{{SO}}_4\\)).\n"
        f"The balanced neutralisation equation is:\n"
        f"\\(\\text{{H}}_2\\text{{SO}}_4(\\text{{aq}}) + 2\\text{{NaOH}}(\\text{{aq}}) \\rightarrow \\text{{Na}}_2\\text{{SO}}_4(\\text{{aq}}) + 2\\text{{H}}_2\\text{{O}}(\\ell)\\)\n\n"
        f"In the titration, \\({_fmt_sa(va_cm3)}\\text{{ cm}}^3\\) of \\({_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\) \\(\\text{{H}}_2\\text{{SO}}_4\\) is exactly neutralised by \\({_fmt_sa(vb_cm3)}\\text{{ cm}}^3\\) of \\(\\text{{NaOH}}\\).\n\n"
        f"1. Calculate the number of moles (\\(n_a\\)) of \\(\\text{{H}}_2\\text{{SO}}_4\\) pipetted into the conical flask. (2)\n"
        f"2. Calculate the concentration (\\(c_b\\)) of the \\(\\text{{NaOH}}\\) solution in \\(\\text{{mol}}\\cdot\\text{{dm}}^{{-3}}\\). (3)\n"
        f"3. Name a suitable acid-base indicator for this strong acid–strong base titration and state why its endpoint matches the equivalence point. (2)"
    )

    sol = (
        f"Step 1: Calculate moles of H₂SO₄ (n_a = c_a × V_a):\n"
        f"V_a = {_fmt_sa(va_cm3)} ÷ 1000 = {_fmt_sa(va_dm3, 4)} dm³\n"
        f"n(H₂SO₄) = {_fmt_sa(ca)} × {_fmt_sa(va_dm3, 4)} = {_fmt_sa(na_mol, 4)} mol\n\n"
        f"Step 2: Use the stoichiometric mole ratio n_a : n_b = 1 : 2 (or c_a V_a / c_b V_b = n_a / n_b):\n"
        f"n(NaOH) = 2 × n(H₂SO₄) = 2 × {_fmt_sa(na_mol, 4)} = {_fmt_sa(nb_mol, 4)} mol\n"
        f"c_b = n(NaOH) ÷ V_b = {_fmt_sa(nb_mol, 4)} ÷ ({_fmt_sa(vb_cm3)} ÷ 1000) = {_fmt_sa(cb, 3)} mol·dm⁻³\n\n"
        f"Step 3: Indicator selection:\n"
        f"Bromothymol blue (pH range 6,0 – 7,6); both H₂SO₄ (strong acid) and NaOH (strong base) ionise/dissociate completely, so the salt Na₂SO₄ does not hydrolyse and the equivalence point occurs at pH = 7."
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Moles of H₂SO₄: n_a = {_fmt_sa(ca)} × {_fmt_sa(va_dm3, 4)} = {_fmt_sa(na_mol, 4)} mol", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. Mole ratio 1:2 applied and concentration c_b(NaOH) = {_fmt_sa(cb, 3)} mol·dm⁻³", "marks": 3, "editable": True},
        {"id": "mp_3", "desc": "3. Bromothymol blue indicator; strong acid + strong base equivalence point at pH = 7", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "Convert cm³ to dm³ by dividing by 1000 before using n = cV.",
        "tier_2": "Notice the 1 : 2 mole ratio in H₂SO₄ + 2NaOH -> Na₂SO₄ + 2H₂O: n(NaOH) = 2 × n(H₂SO₄).",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_titration_{seed}",
        master_name="titration_apparatus",
        grade=grade,
        term=2 if grade == 12 else 3,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["omitted_diprotic_mole_ratio", "volume_unit_conversion_error"],
        landmarks=_landmarks_from_data(TITRATION_DATA),
    )


def build_galvanic_cell_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 12 Galvanic (Voltaic) Cell Standard EMF, Half-Reactions & Cell Notation."""
    cells = [
        {
            "anode": "Zn", "anode_ion": "Zn²⁺", "e_an": -0.76, "ox_half": "Zn(s) → Zn²⁺(aq) + 2e⁻",
            "cathode": "Cu", "cathode_ion": "Cu²⁺", "e_cat": 0.34, "red_half": "Cu²⁺(aq) + 2e⁻ → Cu(s)",
            "notation": "Zn(s) | Zn²⁺(aq) (1 mol·dm⁻³) || Cu²⁺(aq) (1 mol·dm⁻³) | Cu(s)",
        },
        {
            "anode": "Mg", "anode_ion": "Mg²⁺", "e_an": -2.36, "ox_half": "Mg(s) → Mg²⁺(aq) + 2e⁻",
            "cathode": "Ag", "cathode_ion": "Ag⁺", "e_cat": 0.80, "red_half": "Ag⁺(aq) + e⁻ → Ag(s)",
            "notation": "Mg(s) | Mg²⁺(aq) (1 mol·dm⁻³) || Ag⁺(aq) (1 mol·dm⁻³) | Ag(s)",
        },
        {
            "anode": "Ni", "anode_ion": "Ni²⁺", "e_an": -0.25, "ox_half": "Ni(s) → Ni²⁺(aq) + 2e⁻",
            "cathode": "Cu", "cathode_ion": "Cu²⁺", "e_cat": 0.34, "red_half": "Cu²⁺(aq) + 2e⁻ → Cu(s)",
            "notation": "Ni(s) | Ni²⁺(aq) (1 mol·dm⁻³) || Cu²⁺(aq) (1 mol·dm⁻³) | Cu(s)",
        },
    ]
    c = cells[seed % len(cells)]
    emf = round(c["e_cat"] - c["e_an"], 2)
    e_an_str = f"{_fmt_sa(c['e_an'])} V"
    e_cat_str = f"+{_fmt_sa(c['e_cat'])} V"

    prompt = (
        f"Refer to the standard Galvanic (Voltaic) electrochemical cell diagram operating at \\(298\\text{{ K}}\\) with \\(1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}\\) electrolytes.\n"
        f"The cell consists of a \\(\\text{{{c['anode']}}}|\\text{{{c['anode_ion']}}}\\) half-cell (\\(E^\\circ = {e_an_str}\\)) connected via a salt bridge and external voltmeter to a "
        f"\\(\\text{{{c['cathode']}}}|\\text{{{c['cathode_ion']}}}\\) half-cell (\\(E^\\circ = {e_cat_str}\\)).\n\n"
        f"1. Write down the oxidation half-reaction occurring at the anode and the reduction half-reaction occurring at the cathode. (2)\n"
        f"2. Write down the standard cell notation for this galvanic cell. (2)\n"
        f"3. Calculate the initial standard EMF (\\(E^\\circ_{{\\text{{cell}}}}\\)) of this galvanic cell, and state the direction of cation migration through the salt bridge. (3)"
    )

    sol = (
        f"Step 1: Half-reactions at the electrodes:\n"
        f"- Anode (oxidation, lower E° = {e_an_str}): {c['ox_half']}\n"
        f"- Cathode (reduction, higher E° = {e_cat_str}): {c['red_half']}\n\n"
        f"Step 2: Standard cell notation (Anode | Anode electrolyte || Cathode electrolyte | Cathode):\n"
        f"{c['notation']}\n\n"
        f"Step 3: Standard cell EMF calculation and salt bridge ion migration:\n"
        f"E°_cell = E°_cathode - E°_anode\n"
        f"E°_cell = ({_fmt_sa(c['e_cat'])}) - ({_fmt_sa(c['e_an'])}) = +{_fmt_sa(emf)} V\n"
        f"Cations in the salt bridge migrate toward the {c['cathode']} cathode half-cell to maintain electrical neutrality."
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Oxidation half-reaction ({c['ox_half']}) and reduction half-reaction ({c['red_half']})", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. Standard cell notation: {c['notation']}", "marks": 2, "editable": True},
        {"id": "mp_3", "desc": f"3. E°_cell = E°_cathode - E°_anode = ({_fmt_sa(c['e_cat'])}) - ({_fmt_sa(c['e_an'])}) = +{_fmt_sa(emf)} V; cations migrate to cathode", "marks": 3, "editable": True},
    ]

    hints = {
        "tier_1": "The species with the more negative standard reduction potential E° undergoes oxidation at the anode.",
        "tier_2": "Use E°_cell = E°_cathode - E°_anode without changing the sign of either standard reduction potential.",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_galvanic_{seed}",
        master_name="galvanic_cell",
        grade=grade,
        term=3,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["anode_cathode_sign_inversion", "reversed_cell_notation"],
        landmarks=_landmarks_from_data(GALVANIC_DATA),
    )


def build_electrolytic_cell_apparatus_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 12 Electrolytic Cell Decomposition of CuCl₂ & Electroplating Stoichiometry."""
    masses = [3.175, 6.35, 1.27]
    m_cu = masses[seed % len(masses)]
    mol_cu = round(m_cu / 63.5, 3)
    mol_cl2 = mol_cu
    vol_cl2 = round(mol_cl2 * 22.4, 3)
    mol_e = round(2 * mol_cu, 3)

    prompt = (
        f"In an Electrolytic Cell experiment depositing \\({_fmt_sa(m_cu, 3)}\\text{{ g}}\\) of copper metal, refer to the apparatus diagram showing the electrolysis of concentrated aqueous copper(II) chloride (\\(\\text{{CuCl}}_2\\)) using inert graphite electrodes connected to a DC power source.\n\n"
        f"1. State the energy conversion that takes place in an electrolytic cell, and write down the half-reaction occurring at the positive anode and the half-reaction occurring at the negative cathode. (3)\n"
        f"2. Given that a mass of \\({_fmt_sa(m_cu, 3)}\\text{{ g}}\\) of pure copper metal (\\(M(\\text{{Cu}}) = 63,5\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}\\)) is deposited onto the cathode, calculate the number of moles of electrons (\\(n(e^-)\\)) transferred through the circuit. (2)\n"
        f"3. Calculate the volume of chlorine gas (\\(\\text{{Cl}}_2\\)) evolved at the anode at STP (\\(V_m = 22,4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}\\)). (2)"
    )

    sol = (
        f"Step 1 (for m(Cu) = {_fmt_sa(m_cu, 3)} g): Energy conversion and electrode half-reactions:\n"
        f"- Energy conversion: Electrical energy is converted into chemical energy.\n"
        f"- Positive Anode (oxidation): 2Cl⁻(aq) → Cl₂(g) + 2e⁻\n"
        f"- Negative Cathode (reduction): Cu²⁺(aq) + 2e⁻ → Cu(s)\n\n"
        f"Step 2: Moles of Cu deposited and moles of electrons transferred:\n"
        f"n(Cu) = m ÷ M = {_fmt_sa(m_cu, 3)} ÷ 63,5 = {_fmt_sa(mol_cu, 3)} mol\n"
        f"From Cu²⁺ + 2e⁻ → Cu, mole ratio n(e⁻) : n(Cu) = 2 : 1:\n"
        f"n(e⁻) = 2 × {_fmt_sa(mol_cu, 3)} = {_fmt_sa(mol_e, 3)} mol of electrons.\n\n"
        f"Step 3: Volume of Cl₂(g) produced at STP:\n"
        f"n(Cl₂) = n(Cu) = {_fmt_sa(mol_cl2, 3)} mol\n"
        f"V(Cl₂) = n × V_m = {_fmt_sa(mol_cl2, 3)} × 22,4 = {_fmt_sa(vol_cl2, 3)} dm³"
    )

    mps = [
        {"id": "mp_1", "desc": "1. Electrical to chemical energy; Anode: 2Cl⁻ → Cl₂ + 2e⁻; Cathode: Cu²⁺ + 2e⁻ → Cu", "marks": 3, "editable": True},
        {"id": "mp_2", "desc": f"2. n(Cu) = {_fmt_sa(mol_cu, 3)} mol and n(e⁻) = 2 × {_fmt_sa(mol_cu, 3)} = {_fmt_sa(mol_e, 3)} mol", "marks": 2, "editable": True},
        {"id": "mp_3", "desc": f"3. Volume of Cl₂ at STP: V = {_fmt_sa(mol_cl2, 3)} × 22,4 = {_fmt_sa(vol_cl2, 3)} dm³", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "In an electrolytic cell, the anode is positive (attracts Cl⁻ anions for oxidation) and the cathode is negative (attracts Cu²⁺ cations for reduction).",
        "tier_2": "Calculate n(Cu) = m / 63,5. Since 2 moles of electrons reduce 1 mole of Cu²⁺, n(e⁻) = 2 × n(Cu) and n(Cl₂) = n(Cu).",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_electrolytic_{seed}",
        master_name="electrolytic_cell_apparatus",
        grade=grade,
        term=3,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["electrolytic_electrode_polarity_inversion", "omitted_electron_mole_ratio"],
        landmarks=_landmarks_from_data(ELECTROLYTIC_CELL_DATA),
    )


def build_gas_evolution_rate_apparatus_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 12 Reaction Rate & Gas Evolution Stoichiometry."""
    runs = [
        {"vol_cm3": 48.0, "time_s": 20, "vm": 24.0},
        {"vol_cm3": 60.0, "time_s": 25, "vm": 24.0},
        {"vol_cm3": 72.0, "time_s": 30, "vm": 24.0},
    ]
    run = runs[seed % len(runs)]
    v_cm3 = run["vol_cm3"]
    t_s = run["time_s"]
    vm = run["vm"]
    rate = round(v_cm3 / t_s, 2)
    n_gas = round((v_cm3 / 1000.0) / vm, 4)
    m_caco3 = round(n_gas * 100.0, 2)

    prompt = (
        f"Refer to the Gas Evolution and Reaction Rate apparatus diagram in which excess hydrochloric acid (\\(\\text{{HCl}}\\)) reacts with calcium carbonate (\\(\\text{{CaCO}}_3\\)) granules in a conical flask connected to a graduated gas syringe:\n"
        f"\\(\\text{{CaCO}}_3(\\text{{s}}) + 2\\text{{HCl}}(\\text{{aq}}) \\rightarrow \\text{{CaCl}}_2(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\ell) + \\text{{CO}}_2(\\text{{g}})\\)\n\n"
        f"During the first \\({t_s}\\text{{ s}}\\) of the reaction, \\({_fmt_sa(v_cm3)}\\text{{ cm}}^3\\) of \\(\\text{{CO}}_2\\) gas is collected in the gas syringe at room temperature and pressure (where molar gas volume \\(V_m = {_fmt_sa(vm)}\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}\\)).\n\n"
        f"1. Calculate the average rate of production of \\(\\text{{CO}}_2\\) gas over the first \\({t_s}\\text{{ s}}\\) in \\(\\text{{cm}}^3\\cdot\\text{{s}}^{{-1}}\\). (2)\n"
        f"2. Calculate the mass of \\(\\text{{CaCO}}_3\\) (\\(M = 100\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}\\)) consumed during the first \\({t_s}\\text{{ s}}\\). (3)\n"
        f"3. Use collision theory to explain how grinding the \\(\\text{{CaCO}}_3\\) granules into a fine powder affects the initial gradient of the gas volume versus time graph. (2)"
    )

    sol = (
        f"Step 1: Average reaction rate in cm³·s⁻¹:\n"
        f"Average Rate = ΔV ÷ Δt = {_fmt_sa(v_cm3)} cm³ ÷ {t_s} s = {_fmt_sa(rate)} cm³·s⁻¹\n\n"
        f"Step 2: Moles of CO₂ gas and mass of CaCO₃ consumed:\n"
        f"V(CO₂) = {_fmt_sa(v_cm3)} ÷ 1000 = {_fmt_sa(v_cm3 / 1000.0, 3)} dm³\n"
        f"n(CO₂) = V ÷ V_m = {_fmt_sa(v_cm3 / 1000.0, 3)} ÷ {_fmt_sa(vm)} = {_fmt_sa(n_gas, 4)} mol\n"
        f"Since mole ratio n(CaCO₃) : n(CO₂) = 1 : 1:\n"
        f"m(CaCO₃) = n × M = {_fmt_sa(n_gas, 4)} × 100 = {_fmt_sa(m_caco3)} g\n\n"
        f"Step 3: Collision theory explanation:\n"
        f"Grinding CaCO₃ into a powder increases the exposed total surface area of the solid reactant, resulting in more frequent effective collisions per unit time and a steeper initial gradient on the volume-versus-time graph."
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Average rate = ΔV / Δt = {_fmt_sa(v_cm3)} / {t_s} = {_fmt_sa(rate)} cm³·s⁻¹", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. n(CO₂) = {_fmt_sa(n_gas, 4)} mol and mass m(CaCO₃) = {_fmt_sa(n_gas, 4)} × 100 = {_fmt_sa(m_caco3)} g", "marks": 3, "editable": True},
        {"id": "mp_3", "desc": "3. Powder increases surface area -> more effective collisions per unit time -> steeper initial gradient", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "Average rate = ΔV / Δt. Convert cm³ to dm³ (divide by 1000) before dividing by V_m = 24 dm³·mol⁻¹.",
        "tier_2": "From the balanced equation, 1 mol of CaCO₃ produces 1 mol of CO₂, and M(CaCO₃) = 40 + 12 + 3(16) = 100 g·mol⁻¹.",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_gas_rate_{seed}",
        master_name="gas_evolution_rate_apparatus",
        grade=grade,
        term=2,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["cm3_to_dm3_conversion_omitted", "collision_theory_omitted_per_unit_time"],
        landmarks=_landmarks_from_data(GAS_EVOLUTION_DATA),
    )


def build_ac_dc_generator_motor_apparatus_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 12 Electrodynamics AC Generator RMS Voltage, Current & Average Power."""
    specs = [
        {"vmax": 311.13, "r_load": 44.0, "freq": 50},
        {"vmax": 340.0, "r_load": 50.0, "freq": 50},
        {"vmax": 240.0, "r_load": 30.0, "freq": 60},
    ]
    sp = specs[seed % len(specs)]
    vmax = sp["vmax"]
    r_load = sp["r_load"]
    freq = sp["freq"]
    vrms = round(vmax / math.sqrt(2), 2)
    irms = round(vrms / r_load, 2)
    p_avg = round(vrms * irms, 2)
    period = round(1.0 / freq, 3)

    prompt = (
        f"Refer to the Electrodynamics AC Generator apparatus diagram showing a rectangular armature coil rotating at a constant frequency of \\(f = {freq}\\text{{ Hz}}\\) inside a uniform magnetic field, connected via slip rings and carbon brushes to an external resistor of resistance \\(R = {_fmt_sa(r_load)}\\text{{ }}\\Omega\\).\n"
        f"The generator produces a peak (maximum) induced EMF of \\(V_{{\\max}} = {_fmt_sa(vmax)}\\text{{ V}}\\).\n\n"
        f"1. State the physical law of electromagnetic induction that governs the magnitude of the induced EMF, and calculate the period (\\(T\\)) of rotation of the coil. (2)\n"
        f"2. Calculate the root-mean-square voltage (\\(V_{{\\text{{rms}}}}\\)) and root-mean-square current (\\(I_{{\\text{{rms}}}}\\)) delivered to the \\({_fmt_sa(r_load)}\\text{{ }}\\Omega\\) load. (3)\n"
        f"3. Calculate the average electrical power (\\(P_{{\\text{{ave}}}}\\)) dissipated in the load resistor. (2)"
    )

    sol = (
        f"Step 1: Faraday's Law and rotational period T:\n"
        f"- Faraday's Law: The magnitude of the induced EMF across a conductor is directly proportional to the rate of change of magnetic flux linkage (ε = -N ΔΦ / Δt).\n"
        f"- Period T = 1 ÷ f = 1 ÷ {freq} = {_fmt_sa(period, 3)} s\n\n"
        f"Step 2: RMS voltage (V_rms) and RMS current (I_rms):\n"
        f"V_rms = V_max ÷ √2 = {_fmt_sa(vmax)} ÷ 1,4142 = {_fmt_sa(vrms)} V\n"
        f"I_rms = V_rms ÷ R = {_fmt_sa(vrms)} ÷ {_fmt_sa(r_load)} = {_fmt_sa(irms)} A\n\n"
        f"Step 3: Average power (P_ave) dissipated:\n"
        f"P_ave = V_rms × I_rms = {_fmt_sa(vrms)} × {_fmt_sa(irms)} = {_fmt_sa(p_avg)} W"
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Faraday's Law stated and period T = 1/{freq} = {_fmt_sa(period, 3)} s", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. V_rms = V_max / √2 = {_fmt_sa(vrms)} V and I_rms = V_rms / R = {_fmt_sa(irms)} A", "marks": 3, "editable": True},
        {"id": "mp_3", "desc": f"3. Average power P_ave = V_rms × I_rms = {_fmt_sa(p_avg)} W", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "Period T = 1 / f. For sinusoidal alternating current, V_rms = V_max / √2.",
        "tier_2": "Calculate I_rms = V_rms / R, then use P_ave = V_rms × I_rms (or V_rms² / R).",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ps{grade}_electrodynamics_{seed}",
        master_name="ac_dc_generator_motor_apparatus",
        grade=grade,
        term=3,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["used_peak_voltage_in_average_power", "slip_rings_vs_split_ring_commutator"],
        landmarks=_landmarks_from_data(AC_DC_GENERATOR_DATA),
    )


def build_hydraulic_gears_belt_pulley_question(
    seed: int,
    grade: int = 10,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 10 Technical Mathematics / Physical Sciences Gear Ratio, Belt Drive & Pascal Hydraulic Press."""
    configs = [
        {"n_driver": 20, "n_driven": 60, "rpm_in": 900, "a1": 0.02, "a2": 0.24, "f1": 150},
        {"n_driver": 18, "n_driven": 54, "rpm_in": 1200, "a1": 0.015, "a2": 0.18, "f1": 200},
        {"n_driver": 24, "n_driven": 48, "rpm_in": 600, "a1": 0.025, "a2": 0.25, "f1": 180},
    ]
    cfg = configs[seed % len(configs)]
    nd1 = cfg["n_driver"]
    nd2 = cfg["n_driven"]
    rpm_in = cfg["rpm_in"]
    vr = round(nd2 / nd1, 2)
    rpm_out = round(rpm_in / vr, 2)
    a1 = cfg["a1"]
    a2 = cfg["a2"]
    f1 = cfg["f1"]
    p_hyd = round(f1 / a1, 2)
    f2 = round(p_hyd * a2, 2)

    prompt = (
        f"Refer to the Mechanical Gear Train and Hydraulic Press diagram.\n"
        f"In the mechanical gear drive, a driver gear with \\(N_1 = {nd1}\\) teeth rotates at \\(n_1 = {rpm_in}\\text{{ r/min}}\\) and meshes with a driven gear having \\(N_2 = {nd2}\\) teeth. "
        f"In the adjacent hydraulic press, an input force of \\(F_1 = {f1}\\text{{ N}}\\) is applied to a master piston of cross-sectional area \\(A_1 = {_fmt_sa(a1, 3)}\\text{{ m}}^2\\) connected to a slave lift piston of area \\(A_2 = {_fmt_sa(a2, 2)}\\text{{ m}}^2\\).\n\n"
        f"1. Calculate the gear ratio (velocity ratio \\(\\text{{VR}} = \\frac{{N_2}}{{N_1}}\\)) and the rotational frequency (\\(n_2\\)) of the driven gear in \\(\\text{{r/min}}\\). (2)\n"
        f"2. Calculate the fluid pressure (\\(P\\)) transmitted through the incompressible hydraulic oil in pascals (\\(\\text{{Pa}}\\)). (2)\n"
        f"3. Use Pascal's principle (\\(\\frac{{F_1}}{{A_1}} = \\frac{{F_2}}{{A_2}}\\)) to calculate the maximum upward output force (\\(F_2\\)) exerted by the slave piston. (2)"
    )

    sol = (
        f"Step 1: Gear ratio and driven gear rotational speed:\n"
        f"Gear ratio VR = N₂ ÷ N₁ = {nd2} ÷ {nd1} = {_fmt_sa(vr)}\n"
        f"Since N₁ × n₁ = N₂ × n₂:\n"
        f"n₂ = ({nd1} × {rpm_in}) ÷ {nd2} = {_fmt_sa(rpm_out)} r/min\n\n"
        f"Step 2: Hydraulic fluid pressure P:\n"
        f"P = F₁ ÷ A₁ = {f1} N ÷ {_fmt_sa(a1, 3)} m² = {_fmt_sa(p_hyd)} Pa\n\n"
        f"Step 3: Output force F₂ from Pascal's principle (F₂ = P × A₂):\n"
        f"F₂ = {_fmt_sa(p_hyd)} × {_fmt_sa(a2, 2)} = {_fmt_sa(f2)} N"
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Gear ratio VR = {_fmt_sa(vr)} and driven speed n₂ = {_fmt_sa(rpm_out)} r/min", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. Hydraulic pressure P = F₁ / A₁ = {_fmt_sa(p_hyd)} Pa", "marks": 2, "editable": True},
        {"id": "mp_3", "desc": f"3. Output force F₂ = P × A₂ = {_fmt_sa(f2)} N", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": "For meshing gears, N₁ n₁ = N₂ n₂ (a larger driven gear rotates more slowly with higher torque).",
        "tier_2": "By Pascal's principle, pressure P = F₁ / A₁ is transmitted equally throughout the fluid, so F₂ = (A₂ / A₁) × F₁.",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"tm{grade}_mech_hydraulics_{seed}",
        master_name="hydraulic_gears_belt_pulley",
        grade=grade,
        term=3,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["inverted_gear_speed_ratio", "hydraulic_area_force_inversion"],
        landmarks=_landmarks_from_data(HYDRAULIC_GEARS_DATA),
    )


def build_architectural_floor_packaging_plan_question(
    seed: int,
    grade: int = 11,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    """Role C: Grade 10/11 Mathematical Literacy Architectural Floor Plan Scale, Area & Tiling Cost."""
    plans = [
        {"scale": 50, "plan_l_cm": 12.0, "plan_w_cm": 9.0, "tile_area": 1.5, "waste_pct": 10},
        {"scale": 100, "plan_l_cm": 6.5, "plan_w_cm": 4.0, "tile_area": 2.0, "waste_pct": 10},
        {"scale": 50, "plan_l_cm": 10.0, "plan_w_cm": 8.0, "tile_area": 1.6, "waste_pct": 10},
    ]
    pl = plans[seed % len(plans)]
    scale = pl["scale"]
    l_cm = pl["plan_l_cm"]
    w_cm = pl["plan_w_cm"]
    real_l_m = round((l_cm * scale) / 100.0, 2)
    real_w_m = round((w_cm * scale) / 100.0, 2)
    area_m2 = round(real_l_m * real_w_m, 2)
    total_area_with_waste = round(area_m2 * (1.0 + pl["waste_pct"] / 100.0), 2)
    boxes = math.ceil(total_area_with_waste / pl["tile_area"])

    prompt = (
        f"Refer to the Architectural Floor Plan diagram drawn to a number scale of \\(1 : {scale}\\).\n"
        f"On the printed floor plan, the rectangular lounge measures \\({_fmt_sa(l_cm)}\\text{{ cm}}\\) in length by \\({_fmt_sa(w_cm)}\\text{{ cm}}\\) in width.\n\n"
        f"1. Convert the plan measurements using the scale \\(1 : {scale}\\) to calculate the actual length and actual width of the lounge in metres (\\(\\text{{m}}\\)). (2)\n"
        f"2. Calculate the actual floor area of the lounge in square metres (\\(\\text{{m}}^2\\)). (2)\n"
        f"3. Ceramic floor tiles are sold in boxes covering \\({_fmt_sa(pl['tile_area'])}\\text{{ m}}^2\\) per box. Allowing an additional \\({pl['waste_pct']}\\%\\) for cutting and breakage, calculate the minimum number of full boxes of tiles that must be purchased. (2)"
    )

    sol = (
        f"Step 1: Convert plan dimensions to actual dimensions in metres (Scale 1 : {scale}, 100 cm = 1 m):\n"
        f"- Actual length = ({_fmt_sa(l_cm)} cm × {scale}) ÷ 100 = {_fmt_sa(real_l_m)} m\n"
        f"- Actual width = ({_fmt_sa(w_cm)} cm × {scale}) ÷ 100 = {_fmt_sa(real_w_m)} m\n\n"
        f"Step 2: Actual floor area of the lounge:\n"
        f"Area = Length × Width = {_fmt_sa(real_l_m)} m × {_fmt_sa(real_w_m)} m = {_fmt_sa(area_m2)} m²\n\n"
        f"Step 3: Tiling area with {pl['waste_pct']}% wastage and number of boxes required:\n"
        f"Total area needed = {_fmt_sa(area_m2)} × 1,{pl['waste_pct']} = {_fmt_sa(total_area_with_waste)} m²\n"
        f"Exact boxes = {_fmt_sa(total_area_with_waste)} ÷ {_fmt_sa(pl['tile_area'])} = {_fmt_sa(round(total_area_with_waste / pl['tile_area'], 2))}\n"
        f"Rounding UP to full boxes: {boxes} boxes of tiles."
    )

    mps = [
        {"id": "mp_1", "desc": f"1. Actual dimensions: Length = {_fmt_sa(real_l_m)} m and Width = {_fmt_sa(real_w_m)} m", "marks": 2, "editable": True},
        {"id": "mp_2", "desc": f"2. Actual floor area = {_fmt_sa(real_l_m)} × {_fmt_sa(real_w_m)} = {_fmt_sa(area_m2)} m²", "marks": 2, "editable": True},
        {"id": "mp_3", "desc": f"3. Area with {pl['waste_pct']}% waste = {_fmt_sa(total_area_with_waste)} m² and rounded up to {boxes} boxes", "marks": 2, "editable": True},
    ]

    hints = {
        "tier_1": f"Multiply the plan measurement in cm by {scale}, then divide by 100 to convert centimetres into metres.",
        "tier_2": f"Multiply the floor area by 1,{pl['waste_pct']} for cutting wastage, divide by {_fmt_sa(pl['tile_area'])} m² per box, and always round UP to the next whole box.",
        "tier_3": sol,
    }

    return _make_role_c_payload(
        qid=f"ml{grade}_floor_plan_{seed}",
        master_name="architectural_floor_packaging_plan",
        grade=grade,
        term=2,
        mode=mode,
        prompt=prompt,
        worked_solution=sol,
        marking_points=mps,
        hints=hints,
        misconception_tags=["cm_to_m_conversion_error", "rounded_down_partial_tile_box"],
        landmarks=_landmarks_from_data(ARCHITECTURAL_PLAN_DATA),
    )
