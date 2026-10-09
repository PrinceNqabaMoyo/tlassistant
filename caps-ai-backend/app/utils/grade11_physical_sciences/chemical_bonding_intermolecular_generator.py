"""Grade 11 Physical Sciences — Chemical Bonding & Intermolecular Forces (Deterministic 6-Pillar Generator).
100% aligned with South African CAPS Curriculum (Physical Sciences Grade 11 Chemistry Paper 2: Matter and Materials).
Covers:
- Molecular shapes and VSEPR theory (linear, trigonal planar, tetrahedral, trigonal pyramidal, angular/bent)
- Electronegativity difference and bond polarity (polar covalent vs non-polar covalent vs ionic)
- Intermolecular forces (IMF): London dispersion forces, dipole-dipole forces, hydrogen bonding
- Relationships between IMF and physical properties: boiling points, melting points, and vapor pressure

Zero-LLM: 100% deterministic Python logic with pre-baked 3-tier hints.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

TOPIC = "grade11_physical_sciences_chemistry"
LO = "phys11_chemical_bonding_imf"

MOLECULES_VSEPR = [
    {"formula": "CH_4", "name": "methane", "shape": "tetrahedral", "bond_angle": "109.5°", "lone_pairs": 0, "bonded_pairs": 4, "polar": False},
    {"formula": "NH_3", "name": "ammonia", "shape": "trigonal pyramidal", "bond_angle": "107°", "lone_pairs": 1, "bonded_pairs": 3, "polar": True},
    {"formula": "H_2O", "name": "water", "shape": "angular (bent)", "bond_angle": "104.5°", "lone_pairs": 2, "bonded_pairs": 2, "polar": True},
    {"formula": "CO_2", "name": "carbon dioxide", "shape": "linear", "bond_angle": "180°", "lone_pairs": 0, "bonded_pairs": 2, "polar": False},
    {"formula": "BF_3", "name": "boron trifluoride", "shape": "trigonal planar", "bond_angle": "120°", "lone_pairs": 0, "bonded_pairs": 3, "polar": False},
]

IMF_COMPARISONS = [
    {
        "subst_a": "H_2O (water)",
        "imf_a": "hydrogen bonds",
        "subst_b": "H_2S (hydrogen sulfide)",
        "imf_b": "dipole-dipole forces",
        "bp_a": 100,
        "bp_b": -60,
        "reason": "Water molecules have strong hydrogen bonding between hydrogen and oxygen, requiring significantly more energy to separate than the weaker dipole-dipole forces between H_2S molecules.",
    },
    {
        "subst_a": "HF (hydrogen fluoride)",
        "imf_a": "hydrogen bonds",
        "subst_b": "HCl (hydrogen chloride)",
        "imf_b": "dipole-dipole forces",
        "bp_a": 20,
        "bp_b": -85,
        "reason": "HF forms hydrogen bonds due to the small, highly electronegative fluorine atom, which are stronger than the dipole-dipole forces in HCl.",
    },
    {
        "subst_a": "CH_3CH_2OH (ethanol)",
        "imf_a": "hydrogen bonds",
        "subst_b": "CH_3OCH_3 (dimethyl ether)",
        "imf_b": "dipole-dipole forces",
        "bp_a": 78,
        "bp_b": -24,
        "reason": "Ethanol possesses a polar -OH group capable of intermolecular hydrogen bonding, whereas dimethyl ether only has dipole-dipole forces.",
    },
]


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed)


def _build_vsepr_drill(r: random.Random) -> Dict[str, Any]:
    mol = r.choice(MOLECULES_VSEPR)

    prompt = (
        rf"Consider the molecule $\text{{{mol['formula']}}}$ ({mol['name']}):\n\n"
        rf"1. State the number of electron pairs (bonded and lone pairs) surrounding the central atom.\n"
        rf"2. Name the molecular shape of $\text{{{mol['formula']}}}$ according to the VSEPR model.\n"
        rf"3. State whether the molecule is polar or non-polar. Provide a reason referring to molecular symmetry."
    )

    polarity_desc = "polar" if mol["polar"] else "non-polar"
    symmetry_desc = "asymmetrical charge distribution" if mol["polar"] else "symmetrical shape such that bond dipoles cancel out"

    answer = rf"Shape: {mol['shape']}, Polarity: {polarity_desc} ({symmetry_desc})"

    return {
        "id": f"phys11_vsepr_{r.randint(1000, 9999)}",
        "question_type": "typed",
        "topic": "Atomic combinations",
        "learning_objective_id": LO,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "marks": 5,
        "correct_answer": answer,
        "sample_answer": (
            rf"1. {mol['bonded_pairs']} bonded pairs and {mol['lone_pairs']} lone pairs.\n"
            rf"2. Molecular shape: {mol['shape']}.\n"
            rf"3. Polarity: {polarity_desc} because the molecule has {symmetry_desc}."
        ),
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Bonded pairs ({mol['bonded_pairs']}) and lone pairs ({mol['lone_pairs']})", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"VSEPR molecular shape ({mol['shape']})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Polarity ({polarity_desc}) with symmetry explanation", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": f"Count the valence electrons of the central atom and determine how many are involved in bonding vs lone pairs.",
            "2_concept": "VSEPR theory states that electron pairs around a central atom repel each other to take maximum separation.",
            "3_breakdown": f"Shape is {mol['shape']}. It is {polarity_desc} because it has {symmetry_desc}."
        },
        "misconception_tags": ["vsepr_shape_confusion", "bond_vs_molecular_polarity_confusion"],
    }


def _build_imf_drill(r: random.Random) -> Dict[str, Any]:
    comp = r.choice(IMF_COMPARISONS)

    prompt = (
        rf"The boiling point of $\text{{{comp['subst_a']}}}$ is {comp['bp_a']}^\circ\text{{C}}$, whereas "
        rf"the boiling point of $\text{{{comp['subst_b']}}}$ is {comp['bp_b']}^\circ\text{{C}}$.\n\n"
        rf"1. Identify the predominant type of intermolecular force present in $\text{{{comp['subst_a']}}}$.\n"
        rf"2. Identify the predominant type of intermolecular force present in $\text{{{comp['subst_b']}}}$.\n"
        rf"3. Fully explain the difference in boiling points between the two substances."
    )

    return {
        "id": f"phys11_imf_{r.randint(1000, 9999)}",
        "question_type": "typed",
        "topic": "Intermolecular forces",
        "learning_objective_id": LO,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 6,
        "prompt": prompt,
        "marks": 5,
        "correct_answer": f"IMF in {comp['subst_a']}: {comp['imf_a']}; IMF in {comp['subst_b']}: {comp['imf_b']}. {comp['reason']}",
        "sample_answer": (
            rf"1. {comp['subst_a']}: {comp['imf_a']}.\n"
            rf"2. {comp['subst_b']}: {comp['imf_b']}.\n"
            rf"3. {comp['reason']}"
        ),
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of {comp['imf_a']} in {comp['subst_a']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Identification of {comp['imf_b']} in {comp['subst_b']}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Comparison of IMF strength and energy required to overcome forces", "marks": 3, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Hydrogen bonds occur when hydrogen is bonded to small, highly electronegative atoms: N, O, or F.",
            "2_concept": "Substances with stronger intermolecular forces require more thermal energy to overcome, resulting in higher boiling points.",
            "3_breakdown": comp["reason"],
        },
        "misconception_tags": ["imf_classification_error", "intramolecular_vs_intermolecular_confusion"],
    }


def generate(subskill: Optional[str] = None, difficulty: str = "medium", count: int = 1, seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    generators = [_build_vsepr_drill, _build_imf_drill]
    if subskill == "vsepr":
        generators = [_build_vsepr_drill]
    elif subskill == "imf":
        generators = [_build_imf_drill]

    questions = []
    for _ in range(count):
        gen_fn = r.choice(generators)
        questions.append(gen_fn(r))
    return questions
