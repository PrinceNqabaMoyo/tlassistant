"""Grade 11 Physical Sciences — Atomic Combinations & Intermolecular Forces (Subskills 01–25).
Grounded strictly in:
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/02. Atomic combinations.md
- curriculum_docs_auto/PhysicalSciences_Gr11/Term 1/03. Intermolecular forces.md

Covers:
- Valence electrons, octet stability, and potential energy vs internuclear distance curves
- Bond length, bond strength, bond dissociation energy, and reaction enthalpy estimates
- Lewis diagrams (single, double, triple, and dative coordinate covalent bonds) and octet exceptions
- VSEPR molecular geometry (ideal shapes, lone-pair distortion, multiple bond domains)
- Pauling electronegativity difference (ΔEN), bond polarity spectrum, partial charges, molecular symmetry
- Types of intermolecular forces (London dispersion, dipole-dipole, hydrogen bonding, ion-dipole, induced dipoles)

Zero-LLM: 100% deterministic Python with seed-varied parameters, South African comma decimals, and inline SVG diagrams.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


TOPIC = "grade11_physical_sciences_chemistry"
LO = "phys11_chemical_bonding_imf"


def _fmt_sa(val: float, decimals: int = 1) -> str:
    """Format a float with South African comma decimal separator."""
    rounded = round(val, decimals)
    if decimals == 0 or float(rounded).is_integer():
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _svg_wrap(inner: str, width: int = 380, height: int = 230) -> str:
    """Wrap SVG markup on a clean, high-contrast scientific canvas."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" '
        f'style="background:#ffffff;border:1px solid #cbd5e1;border-radius:6px;">'
        f"{inner}</svg>"
    )


def _pillars(
    qid: str,
    subskill: str,
    prompt: str,
    answer: str,
    sample: str,
    marking_points: List[Dict[str, Any]],
    hints: Dict[str, str],
    misconception_tags: List[str],
    marks: int = 3,
    duration: int = 4,
    topic_label: str = "Atomic combinations",
    term: int = 1,
    diagram_spec: Optional[Dict[str, Any]] = None,
    question_type: str = "typed",
    options: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Assemble standardized 6-pillar Grade 11 Physical Sciences Chemistry payload."""
    total_marks = sum(int(mp.get("marks", 1)) for mp in marking_points) if marking_points else marks
    payload: Dict[str, Any] = {
        "id": qid,
        "question_id": qid,
        "topic": topic_label,
        "subskill": subskill,
        "learning_objective_id": LO,
        "subject": "Physical Sciences",
        "grade": 11,
        "term": term,
        "caps_weight_percent": 15,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill}",
        "question_type": question_type,
        "prompt": prompt,
        "question_text": prompt,
        "correct_answer": answer,
        "expected_answer": answer,
        "answer_latex": answer,
        "sample_answer": sample,
        "worked_solution": sample,
        "marks": total_marks,
        "marking_schema": {
            "total_marks": total_marks,
            "marking_points": marking_points,
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
        "hint_sections": hints,
        "misconception_tags": misconception_tags,
    }
    if options:
        payload["options"] = options
    if diagram_spec is not None:
        payload["diagram_spec"] = diagram_spec
    return payload


# =========================================================================== #
# 01: Valence Electrons and Octet Rule
# =========================================================================== #
def build_01_valence_electrons_and_octet_rule(rng: random.Random) -> Dict[str, Any]:
    atoms = [
        {"sym": "C", "name": "carbon", "z": 6, "config": "1s² 2s² 2p²", "val": 4, "bonds": 4, "group": 14},
        {"sym": "N", "name": "nitrogen", "z": 7, "config": "1s² 2s² 2p³", "val": 5, "bonds": 3, "group": 15},
        {"sym": "O", "name": "oxygen", "z": 8, "config": "1s² 2s² 2p⁴", "val": 6, "bonds": 2, "group": 16},
        {"sym": "F", "name": "fluorine", "z": 9, "config": "1s² 2s² 2p⁵", "val": 7, "bonds": 1, "group": 17},
        {"sym": "Si", "name": "silicon", "z": 14, "config": "[Ne] 3s² 3p²", "val": 4, "bonds": 4, "group": 14},
        {"sym": "P", "name": "phosphorus", "z": 15, "config": "[Ne] 3s² 3p³", "val": 5, "bonds": 3, "group": 15},
        {"sym": "S", "name": "sulfur", "z": 16, "config": "[Ne] 3s² 3p⁴", "val": 6, "bonds": 2, "group": 16},
        {"sym": "Cl", "name": "chlorine", "z": 17, "config": "[Ne] 3s² 3p⁵", "val": 7, "bonds": 1, "group": 17},
    ]
    el = rng.choice(atoms)
    prompt = (
        f"An isolated atom of {el['name']} ($\\text{{{el['sym']}}}$, atomic number $Z = {el['z']}$) "
        f"has the ground-state electron configuration ${el['config']}$.\n\n"
        f"1. State the number of valence electrons in a neutral {el['name']} atom.\n"
        f"2. How many covalent bonds does {el['name']} typically form to attain a full noble-gas octet in its valence energy level?"
    )
    ans = f"{el['val']} valence electrons; {el['bonds']} covalent bond(s)"
    sample = (
        f"1. Electrons in the outermost shell (Group {el['group']}): {el['val']} valence electrons.\n"
        f"2. Number of additional electrons required for an octet = 8 - {el['val']} = {el['bonds']}. "
        f"Therefore, {el['name']} typically forms {el['bonds']} covalent bond(s)."
    )
    return _pillars(
        qid=f"ps11_01_{rng.randint(10000, 99999)}",
        subskill="01_valence_electrons_and_octet_rule",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct valence electrons: {el['val']}", "marks": 1},
            {"id": "mp2", "desc": f"Octet deficit 8 - {el['val']} = {el['bonds']} covalent bonds", "marks": 2},
        ],
        hints={
            "1_nudge": "Valence electrons are the electrons in the highest principal energy level (outermost shell).",
            "2_concept": f"Subtract the valence electron count from 8 to determine the bonding capacity (valency).",
            "3_breakdown": sample,
        },
        misconception_tags=["counting_core_electrons_as_valence", "confusing_group_number_with_valency"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 02: Potential Energy Curve of Bond Formation (Inline SVG)
# =========================================================================== #
def build_02_potential_energy_curve_bond_formation(rng: random.Random) -> Dict[str, Any]:
    systems = [
        {"pair": "H–H (hydrogen molecule)", "r0": 74, "eb": -432, "eb_pos": 432, "note": "attractive and repulsive forces balance at minimum potential energy"},
        {"pair": "Cl–Cl (chlorine molecule)", "r0": 199, "eb": -243, "eb_pos": 243, "note": "attractive electrostatic forces balance nuclear and electronic repulsion"},
        {"pair": "F–F (fluorine molecule)", "r0": 142, "eb": -159, "eb_pos": 159, "note": "the net electrostatic force is zero at the minimum energy well"},
        {"pair": "Br–Br (bromine molecule)", "r0": 228, "eb": -193, "eb_pos": 193, "note": "optimal internuclear overlap gives the most stable covalent bond"},
    ]
    sys_c = rng.choice(systems)
    svg = _svg_wrap(
        f'<line x1="55" y1="20" x2="55" y2="200" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="45" y1="100" x2="350" y2="100" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,3"/>'
        f'<text x="20" y="30" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a">E (kJ/mol)</text>'
        f'<text x="35" y="104" font-family="sans-serif" font-size="11" fill="#475569">0</text>'
        f'<text x="230" y="116" font-family="sans-serif" font-size="11" fill="#0f172a">Internuclear distance r (pm)</text>'
        f'<path d="M 80 25 Q 105 190, 145 175 Q 190 155, 250 108 L 330 102" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
        f'<circle cx="145" cy="175" r="4.5" fill="#dc2626"/>'
        f'<line x1="145" y1="100" x2="145" y2="175" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="3,2"/>'
        f'<line x1="55" y1="175" x2="145" y2="175" stroke="#dc2626" stroke-width="1.2" stroke-dasharray="3,2"/>'
        f'<text x="135" y="92" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">{sys_c["r0"]} pm</text>'
        f'<text x="152" y="182" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Point X</text>'
        f'<text x="8" y="178" font-family="sans-serif" font-size="10" font-weight="bold" fill="#dc2626">{sys_c["eb"]}</text>'
        f'<text x="200" y="40" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e293b">{sys_c["pair"]}</text>',
        width=380,
        height=220,
    )
    prompt = (
        f"Refer to the potential energy curve for the formation of a {sys_c['pair']} bond.\n\n"
        f"1. State the bond length (in pm) and bond energy (in kJ/mol) represented at Point X.\n"
        f"2. Compare the magnitudes of the attractive and repulsive forces acting on the two atoms at Point X.\n"
        f"3. Explain why the potential energy rises sharply to the left of Point X (smaller $r$)."
    )
    ans = f"Bond length = {sys_c['r0']} pm; Bond energy = {sys_c['eb_pos']} kJ/mol; Attractive force equals repulsive force at X"
    sample = (
        f"1. Bond length = {sys_c['r0']} pm; Bond energy = {sys_c['eb_pos']} kJ·mol⁻¹ (energy minimum at {sys_c['eb']} kJ·mol⁻¹).\n"
        f"2. At Point X, {sys_c['note']} (attractive forces equal repulsive forces in magnitude).\n"
        f"3. For distances shorter than {sys_c['r0']} pm, strong electrostatic repulsion between the two positively charged nuclei "
        f"and between inner electron shells dominates, sharply increasing potential energy."
    )
    return _pillars(
        qid=f"ps11_02_{rng.randint(10000, 99999)}",
        subskill="02_potential_energy_curve_bond_formation",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Read bond length = {sys_c['r0']} pm and bond energy = {sys_c['eb_pos']} kJ/mol", "marks": 2},
            {"id": "mp2", "desc": "Attractive and repulsive forces are balanced (equal) at minimum X", "marks": 1},
            {"id": "mp3", "desc": "Nuclear-nuclear and electron-electron repulsion dominates at r < r0", "marks": 1},
        ],
        hints={
            "1_nudge": "Point X marks the lowest potential energy state where the covalent bond is most stable.",
            "2_concept": "Bond energy is the energy required to break the bond (positive magnitude of the well depth).",
            "3_breakdown": sample,
        },
        misconception_tags=["reporting_negative_bond_energy_magnitude", "ignoring_nuclear_repulsion_short_distance"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Potential energy curve ({sys_c['pair']}, r={sys_c['r0']} pm)"},
    )


# =========================================================================== #
# 03: Bond Length vs Bond Strength and Multiplicity
# =========================================================================== #
def build_03_bond_length_vs_bond_strength_energy(rng: random.Random) -> Dict[str, Any]:
    series_list = [
        {
            "title": "Carbon–Carbon Bond Order",
            "items": [("C–C (single)", 154, 348), ("C=C (double)", 134, 614), ("C≡C (triple)", 120, 839)],
            "factor": "number of shared electron pairs (bond order)",
            "strongest": "C≡C (triple)",
        },
        {
            "title": "Hydrogen Halide Size Trend",
            "items": [("H–F", 92, 565), ("H–Cl", 127, 431), ("H–Br", 141, 366), ("H–I", 161, 299)],
            "factor": "atomic radius of the halogen atom",
            "strongest": "H–F",
        },
        {
            "title": "Carbon–Oxygen Bond Order",
            "items": [("C–O (single)", 143, 358), ("C=O (double)", 121, 799), ("C≡O (triple)", 113, 1072)],
            "factor": "bond multiplicity between carbon and oxygen",
            "strongest": "C≡O (triple)",
        },
    ]
    sel = rng.choice(series_list)
    rows = "\n".join(f"| {b} | {l} pm | {e} kJ·mol⁻¹ |" for b, l, e in sel["items"])
    prompt = (
        f"Study the experimental bond data below for **{sel['title']}**:\n\n"
        f"| Bond | Bond Length | Bond Energy |\n|---|---|---|\n{rows}\n\n"
        f"1. Identify which bond is the strongest and state the relationship between bond length and bond strength.\n"
        f"2. Identify the structural factor responsible for this trend."
    )
    ans = f"Strongest: {sel['strongest']}; Shorter bond length corresponds to higher bond energy (stronger bond)"
    sample = (
        f"1. The strongest bond is **{sel['strongest']}** because it requires the most energy to break. "
        f"As bond length decreases, bond strength (bond energy) increases.\n"
        f"2. This trend is governed by the {sel['factor']}."
    )
    return _pillars(
        qid=f"ps11_03_{rng.randint(10000, 99999)}",
        subskill="03_bond_length_vs_bond_strength_energy",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identify {sel['strongest']} as strongest bond", "marks": 1},
            {"id": "mp2", "desc": "Inverse relationship: shorter bond length means stronger bond", "marks": 1},
            {"id": "mp3", "desc": f"Explain via {sel['factor']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Stronger bonds pull nuclei closer together and require more energy to dissociate.",
            "2_concept": "Shorter bond length and higher bond order result in higher bond dissociation energy.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_longer_bonds_are_stronger", "confusing_bond_length_with_molecular_size"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 04: Lewis Dot Diagrams — Single Covalent Bonds (Inline SVG)
# =========================================================================== #
def build_04_lewis_dot_diagrams_single_covalent_bonds(rng: random.Random) -> Dict[str, Any]:
    molecules = [
        {"formula": "H₂O", "name": "water", "central": "O", "outer": "H", "bp": 2, "lp_central": 2, "lp_total": 2},
        {"formula": "NH₃", "name": "ammonia", "central": "N", "outer": "H", "bp": 3, "lp_central": 1, "lp_total": 1},
        {"formula": "CH₄", "name": "methane", "central": "C", "outer": "H", "bp": 4, "lp_central": 0, "lp_total": 0},
        {"formula": "HCl", "name": "hydrogen chloride", "central": "Cl", "outer": "H", "bp": 1, "lp_central": 3, "lp_total": 3},
        {"formula": "PCl₃", "name": "phosphorus trichloride", "central": "P", "outer": "Cl", "bp": 3, "lp_central": 1, "lp_total": 10},
    ]
    m = rng.choice(molecules)
    svg = _svg_wrap(
        f'<rect x="20" y="20" width="320" height="170" rx="10" fill="#f8fafc" stroke="#94a3b8"/>'
        f'<text x="180" y="50" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">Lewis Analysis: {m["formula"]}</text>'
        f'<circle cx="180" cy="115" r="24" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="180" y="121" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a">{m["central"]}</text>'
        f'<circle cx="110" cy="115" r="16" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="110" y="120" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="bold" fill="#991b1b">{m["outer"]}</text>'
        f'<line x1="126" y1="115" x2="156" y2="115" stroke="#0f172a" stroke-width="2.5"/>'
        f'<text x="180" y="170" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#334155">Central atom: {m["central"]} | Bonding pairs: ? | Lone pairs: ?</text>',
        width=360,
        height=210,
    )
    prompt = (
        f"Refer to the Lewis representation schematic for a molecule of {m['name']} ($\\text{{{m['formula']}}}$).\n\n"
        f"1. State the total number of shared bonding electron pairs in the molecule.\n"
        f"2. State the number of lone (non-bonding) electron pairs on the {m['central']} atom.\n"
        f"3. State the total number of lone electron pairs across the entire molecule."
    )
    ans = f"Bonding pairs: {m['bp']}; Lone pairs on {m['central']}: {m['lp_central']}; Total lone pairs: {m['lp_total']}"
    sample = (
        f"1. Number of single covalent bonds (bonding pairs) = {m['bp']}.\n"
        f"2. Lone pairs on central/key atom {m['central']} = {m['lp_central']}.\n"
        f"3. Total lone pairs in {m['formula']} = {m['lp_total']}."
    )
    return _pillars(
        qid=f"ps11_04_{rng.randint(10000, 99999)}",
        subskill="04_lewis_dot_diagrams_single_covalent_bonds",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct bonding pairs: {m['bp']}", "marks": 1},
            {"id": "mp2", "desc": f"Lone pairs on {m['central']}: {m['lp_central']}", "marks": 1},
            {"id": "mp3", "desc": f"Total lone pairs: {m['lp_total']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Each single covalent bond counts as 1 shared bonding electron pair (2 electrons).",
            "2_concept": "Count remaining valence electrons on each atom that are not shared and divide by 2 for lone pairs.",
            "3_breakdown": sample,
        },
        misconception_tags=["counting_electrons_instead_of_pairs", "forgetting_terminal_atom_lone_pairs"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Lewis bonding pairs schematic ({m['formula']})"},
    )


# =========================================================================== #
# 05: Lewis Dot Diagrams — Multiple Bonds (Inline SVG)
# =========================================================================== #
def build_05_lewis_dot_diagrams_multiple_bonds(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"formula": "CO₂", "desc": "O=C=O", "shared_e": 8, "mult": "two double bonds", "lp_total": 4},
        {"formula": "N₂", "desc": "N≡N", "shared_e": 6, "mult": "one triple bond", "lp_total": 2},
        {"formula": "O₂", "desc": "O=O", "shared_e": 4, "mult": "one double bond", "lp_total": 4},
        {"formula": "HCN", "desc": "H–C≡N", "shared_e": 8, "mult": "one single bond and one triple bond", "lp_total": 1},
        {"formula": "C₂H₂", "desc": "H–C≡C–H", "shared_e": 10, "mult": "two single bonds and one triple bond", "lp_total": 0},
    ]
    c = rng.choice(cases)
    svg = _svg_wrap(
        f'<rect x="20" y="20" width="320" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1"/>'
        f'<text x="180" y="55" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">Multiple Covalent Bonding: {c["formula"]}</text>'
        f'<text x="180" y="100" text-anchor="middle" font-family="monospace" font-size="22" font-weight="bold" fill="#2563eb">{c["desc"]}</text>'
        f'<text x="180" y="142" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#475569">Count shared electrons and lone pairs</text>',
        width=360,
        height=190,
    )
    prompt = (
        f"Refer to the structural representation of $\\text{{{c['formula']}}}$ (${c['desc']}$).\n\n"
        f"1. State the bond multiplicity present in $\\text{{{c['formula']}}}$.\n"
        f"2. Calculate the total number of **shared valence electrons** across all covalent bonds in one molecule.\n"
        f"3. State the total number of **lone electron pairs** in the molecule."
    )
    ans = f"{c['mult']}; {c['shared_e']} shared electrons; {c['lp_total']} lone pair(s)"
    sample = (
        f"1. {c['formula']} contains {c['mult']}.\n"
        f"2. Each covalent bond line represents 2 shared electrons, giving {c['shared_e']} shared electrons in total.\n"
        f"3. Completing octets (and duplets on H) gives {c['lp_total']} lone pair(s)."
    )
    return _pillars(
        qid=f"ps11_05_{rng.randint(10000, 99999)}",
        subskill="05_lewis_dot_diagrams_multiple_bonds",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct bond types: {c['mult']}", "marks": 1},
            {"id": "mp2", "desc": f"Total shared electrons = {c['shared_e']}", "marks": 1},
            {"id": "mp3", "desc": f"Total lone pairs = {c['lp_total']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Double bonds share 4 electrons (2 pairs); triple bonds share 6 electrons (3 pairs).",
            "2_concept": "Total shared electrons = 2 × (total number of bond lines).",
            "3_breakdown": sample,
        },
        misconception_tags=["counting_pairs_instead_of_electrons", "wrong_double_triple_electron_count"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Multiple bond Couper notation ({c['formula']})"},
    )


# =========================================================================== #
# 06: Dative (Coordinate) Covalent Bonding (Inline SVG)
# =========================================================================== #
def build_06_dative_coordinate_covalent_bonding(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "donor": "NH₃ (ammonia)",
            "acceptor": "H⁺ (hydrogen ion)",
            "product": "NH₄⁺ (ammonium ion)",
            "donor_atom": "nitrogen (N)",
            "normal_bonds": 3,
        },
        {
            "donor": "H₂O (water)",
            "acceptor": "H⁺ (hydrogen ion)",
            "product": "H₃O⁺ (hydronium ion)",
            "donor_atom": "oxygen (O)",
            "normal_bonds": 2,
        },
    ]
    rxn = rng.choice(reactions)
    svg = _svg_wrap(
        f'<rect x="15" y="15" width="350" height="170" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="45" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Formation of {rxn["product"]}</text>'
        f'<text x="85" y="105" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" fill="#2563eb">{rxn["donor"].split()[0]}</text>'
        f'<text x="145" y="105" text-anchor="middle" font-family="sans-serif" font-size="15" fill="#0f172a">+</text>'
        f'<text x="190" y="105" text-anchor="middle" font-family="sans-serif" font-size="15" font-weight="bold" fill="#dc2626">{rxn["acceptor"].split()[0]}</text>'
        f'<text x="235" y="105" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#0f172a">→</text>'
        f'<text x="295" y="105" text-anchor="middle" font-family="sans-serif" font-size="16" font-weight="bold" fill="#059669">[{rxn["product"].split()[0]}]</text>'
        f'<text x="190" y="152" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#475569">Arrow indicates donation of lone pair from {rxn["donor_atom"]}</text>',
        width=380,
        height=200,
    )
    prompt = (
        f"Refer to the reaction diagram showing the formation of the {rxn['product']} when {rxn['donor']} reacts with an {rxn['acceptor']}.\n\n"
        f"1. Define a **dative covalent (coordinate covalent) bond**.\n"
        f"2. Explain how the dative covalent bond forms between {rxn['donor']} and {rxn['acceptor']}.\n"
        f"3. State how many normal covalent bonds and how many dative covalent bonds exist in the final {rxn['product']}."
    )
    ans = f"Both shared electrons originate from {rxn['donor_atom']}; {rxn['normal_bonds']} normal covalent bonds and 1 dative covalent bond"
    sample = (
        f"1. A dative covalent bond is a covalent bond in which both shared electrons are donated by the same atom.\n"
        f"2. The {rxn['donor_atom']} atom in {rxn['donor']} donates a lone pair of electrons into the empty 1s orbital of the {rxn['acceptor']}.\n"
        f"3. There are {rxn['normal_bonds']} normal covalent bonds and 1 dative covalent bond (once formed, all {rxn['normal_bonds'] + 1} bonds are equivalent in length and strength)."
    )
    return _pillars(
        qid=f"ps11_06_{rng.randint(10000, 99999)}",
        subskill="06_dative_coordinate_covalent_bonding",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Definition: both electrons in shared pair come from one atom", "marks": 2},
            {"id": "mp2", "desc": f"Lone pair donation from {rxn['donor_atom']} to empty orbital on H+", "marks": 1},
            {"id": "mp3", "desc": f"{rxn['normal_bonds']} normal bonds + 1 dative bond", "marks": 1},
        ],
        hints={
            "1_nudge": "An H⁺ ion has zero electrons and therefore needs an entire pair from another atom.",
            "2_concept": "In a dative covalent bond, one atom supplies both electrons (its lone pair).",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_dative_with_ionic_transfer", "claiming_H_plus_shares_one_electron"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Dative covalent bond ({rxn['product']})"},
    )


# =========================================================================== #
# 07: Octet Rule Exceptions (Incomplete & Expanded Octets)
# =========================================================================== #
def build_07_octet_rule_exceptions_incomplete_and_expanded(rng: random.Random) -> Dict[str, Any]:
    exceptions = [
        {"formula": "BeCl₂", "central": "Be", "e_count": 4, "kind": "incomplete octet (electron-deficient)", "shape": "linear"},
        {"formula": "BF₃", "central": "B", "e_count": 6, "kind": "incomplete octet (electron-deficient)", "shape": "trigonal planar"},
        {"formula": "PCl₅", "central": "P", "e_count": 10, "kind": "expanded octet (hypervalent)", "shape": "trigonal bipyramidal"},
        {"formula": "SF₆", "central": "S", "e_count": 12, "kind": "expanded octet (hypervalent)", "shape": "octahedral"},
    ]
    ex = rng.choice(exceptions)
    prompt = (
        f"The molecule $\\text{{{ex['formula']}}}$ does not obey the standard octet rule around its central atom.\n\n"
        f"1. Calculate the total number of valence electrons surrounding the central {ex['central']} atom in $\\text{{{ex['formula']}}}$.\n"
        f"2. Classify $\\text{{{ex['formula']}}}$ as having an **incomplete octet** or an **expanded octet**."
    )
    ans = f"{ex['e_count']} valence electrons around {ex['central']}; {ex['kind']}"
    sample = (
        f"1. Central atom {ex['central']} forms {ex['e_count'] // 2} single covalent bonds with no lone pairs, "
        f"giving 2 × {ex['e_count'] // 2} = {ex['e_count']} valence electrons around {ex['central']}.\n"
        f"2. Because {ex['e_count']} {'<' if ex['e_count'] < 8 else '>'} 8, it is an **{ex['kind']}**."
    )
    return _pillars(
        qid=f"ps11_07_{rng.randint(10000, 99999)}",
        subskill="07_octet_rule_exceptions_incomplete_and_expanded",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct electron count: {ex['e_count']} valence electrons", "marks": 2},
            {"id": "mp2", "desc": f"Classification: {ex['kind']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Count each single covalent bond to the central atom as 2 valence electrons.",
            "2_concept": "Fewer than 8 electrons = incomplete octet; more than 8 electrons (Period 3+) = expanded octet.",
            "3_breakdown": sample,
        },
        misconception_tags=["forcing_8_electrons_on_boron_or_phosphorus"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 08: VSEPR Ideal Shapes (Zero Lone Pairs) (Inline SVG)
# =========================================================================== #
def build_08_vsepr_ideal_shapes_no_lone_pairs(rng: random.Random) -> Dict[str, Any]:
    shapes = [
        {"formula": "BeCl₂", "notation": "AX₂", "bp": 2, "shape": "Linear", "angle": "180°", "x_pos": [(90, 110), (270, 110)]},
        {"formula": "BF₃", "notation": "AX₃", "bp": 3, "shape": "Trigonal planar", "angle": "120°", "x_pos": [(180, 45), (115, 155), (245, 155)]},
        {"formula": "CH₄", "notation": "AX₄", "bp": 4, "shape": "Tetrahedral", "angle": "109,5°", "x_pos": [(180, 40), (110, 140), (250, 140), (195, 175)]},
        {"formula": "PCl₅", "notation": "AX₅", "bp": 5, "shape": "Trigonal bipyramidal", "angle": "90° and 120°", "x_pos": [(180, 35), (180, 185), (105, 110), (255, 110), (215, 145)]},
        {"formula": "SF₆", "notation": "AX₆", "bp": 6, "shape": "Octahedral", "angle": "90°", "x_pos": [(180, 35), (180, 185), (105, 85), (255, 85), (105, 135), (255, 135)]},
    ]
    sh = rng.choice(shapes)
    bonds_svg = "".join(
        f'<line x1="180" y1="110" x2="{px}" y2="{py}" stroke="#334155" stroke-width="2.5"/>'
        f'<circle cx="{px}" cy="{py}" r="13" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>'
        f'<text x="{px}" y="{py + 4}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0369a1">X</text>'
        for px, py in sh["x_pos"]
    )
    svg = _svg_wrap(
        bonds_svg
        + f'<circle cx="180" cy="110" r="18" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="180" y="115" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#92400e">A</text>'
        f'<text x="180" y="208" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#475569">VSEPR Template: {sh["notation"]} ({sh["formula"]})</text>',
        width=360,
        height=220,
    )
    prompt = (
        f"Refer to the VSEPR molecular geometry diagram for $\\text{{{sh['formula']}}}$ (general formula ${sh['notation']}$).\n\n"
        f"1. State the number of bonding electron pairs and lone pairs around the central atom A.\n"
        f"2. Name the ideal VSEPR molecular shape.\n"
        f"3. State the characteristic bond angle(s)."
    )
    ans = f"Bonding pairs: {sh['bp']}, Lone pairs: 0; Shape: {sh['shape']}; Bond angle: {sh['angle']}"
    sample = (
        f"1. Central atom A has {sh['bp']} bonding electron pairs and 0 lone pairs ({sh['notation']}).\n"
        f"2. To minimise electrostatic repulsion, the electron pairs arrange in an ideal **{sh['shape']}** shape.\n"
        f"3. Characteristic bond angle(s): {sh['angle']}."
    )
    return _pillars(
        qid=f"ps11_08_{rng.randint(10000, 99999)}",
        subskill="08_vsepr_ideal_shapes_no_lone_pairs",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"{sh['bp']} bonding pairs, 0 lone pairs", "marks": 1},
            {"id": "mp2", "desc": f"Shape: {sh['shape']}", "marks": 1},
            {"id": "mp3", "desc": f"Bond angle: {sh['angle']}", "marks": 1},
        ],
        hints={
            "1_nudge": "Ideal VSEPR shapes have 0 lone pairs on the central atom (AXₙ).",
            "2_concept": f"Count the X atoms attached to central atom A ({sh['bp']} domains).",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_trigonal_planar_with_pyramidal", "incorrect_bond_angle_for_ideal_geometry"],
        marks=3,
        duration=4,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Ideal VSEPR geometry ({sh['notation']}, {sh['formula']})"},
    )


# =========================================================================== #
# 09: VSEPR Shapes with Lone Pair Distortion (Inline SVG)
# =========================================================================== #
def build_09_vsepr_shapes_with_lone_pairs_distortion(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"formula": "H₂O", "notation": "AX₂E₂", "bp": 2, "lp": 2, "shape": "Bent / Angular", "angle": "104,5°"},
        {"formula": "NH₃", "notation": "AX₃E", "bp": 3, "lp": 1, "shape": "Trigonal pyramidal", "angle": "107°"},
        {"formula": "H₂S", "notation": "AX₂E₂", "bp": 2, "lp": 2, "shape": "Bent / Angular", "angle": "92°"},
        {"formula": "PH₃", "notation": "AX₃E", "bp": 3, "lp": 1, "shape": "Trigonal pyramidal", "angle": "93,5°"},
    ]
    c = rng.choice(cases)
    svg = _svg_wrap(
        f'<circle cx="180" cy="105" r="18" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        f'<text x="180" y="110" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#92400e">{c["formula"]}</text>'
        f'<ellipse cx="180" cy="55" rx="22" ry="12" fill="#dcfce7" stroke="#16a34a" stroke-dasharray="3,2"/>'
        f'<text x="180" y="59" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#15803d">Lone pair(s): {c["lp"]}</text>'
        f'<line x1="166" y1="118" x2="115" y2="165" stroke="#334155" stroke-width="2.5"/>'
        f'<line x1="194" y1="118" x2="245" y2="165" stroke="#334155" stroke-width="2.5"/>'
        f'<text x="180" y="195" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#475569">General VSEPR: {c["notation"]} | Angle ≈ {c["angle"]}</text>',
        width=360,
        height=215,
    )
    prompt = (
        f"Refer to the VSEPR electron-pair diagram for $\\text{{{c['formula']}}}$ (${c['notation']}$).\n\n"
        f"1. State the number of bonding pairs and lone pairs around the central atom.\n"
        f"2. Name the molecular shape of $\\text{{{c['formula']}}}$.\n"
        f"3. Explain why its bond angle ({c['angle']}) is compressed below the ideal tetrahedral angle of $109{{,}}5^\\circ$."
    )
    ans = f"{c['bp']} bonding pairs, {c['lp']} lone pair(s); {c['shape']}; lone pair–bonding pair repulsion is stronger than bonding–bonding repulsion"
    sample = (
        f"1. {c['bp']} bonding pairs and {c['lp']} lone pair(s) (4 electron domains total, tetrahedral electron-domain arrangement).\n"
        f"2. Molecular shape: **{c['shape']}**.\n"
        f"3. Lone pairs occupy more angular space closer to the central nucleus, so lone-pair–bonding-pair repulsion is stronger than "
        f"bonding-pair–bonding-pair repulsion, compressing the bond angle to {c['angle']}."
    )
    return _pillars(
        qid=f"ps11_09_{rng.randint(10000, 99999)}",
        subskill="09_vsepr_shapes_with_lone_pairs_distortion",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"{c['bp']} bonding pairs and {c['lp']} lone pair(s)", "marks": 1},
            {"id": "mp2", "desc": f"Molecular shape: {c['shape']}", "marks": 1},
            {"id": "mp3", "desc": "Stronger lone-pair repulsion compresses bonding angles", "marks": 2},
        ],
        hints={
            "1_nudge": "Molecular shape describes only the positions of the atomic nuclei, not the lone pairs.",
            "2_concept": "Repulsion order: lone–lone > lone–bonding > bonding–bonding.",
            "3_breakdown": sample,
        },
        misconception_tags=["calling_NH3_tetrahedral_shape", "ignoring_lone_pair_compression"],
        marks=4,
        duration=5,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"VSEPR lone-pair distortion ({c['formula']})"},
    )


# =========================================================================== #
# 10: VSEPR with Multiple Bonds as Single Domains
# =========================================================================== #
def build_10_vsepr_multiple_bonds_as_single_domain(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"formula": "CO₂", "struct": "O=C=O", "domains": 2, "lp": 0, "shape": "Linear", "angle": "180°"},
        {"formula": "HCN", "struct": "H–C≡N", "domains": 2, "lp": 0, "shape": "Linear", "angle": "180°"},
        {"formula": "CH₂O", "struct": "H₂C=O", "domains": 3, "lp": 0, "shape": "Trigonal planar", "angle": "120°"},
        {"formula": "SO₂", "struct": "O=S=O (with 1 lone pair on S)", "domains": 3, "lp": 1, "shape": "Bent / Angular", "angle": "119°"},
    ]
    c = rng.choice(cases)
    prompt = (
        f"In VSEPR theory, a double or triple covalent bond is counted as **one** region of electron density (one domain) "
        f"when determining molecular geometry.\n\n"
        f"Consider $\\text{{{c['formula']}}}$ (${c['struct']}$):\n"
        f"1. How many electron domains surround the central atom?\n"
        f"2. Predict the molecular shape and approximate bond angle of $\\text{{{c['formula']}}}$."
    )
    ans = f"{c['domains']} electron domains ({c['lp']} lone pair); {c['shape']} ({c['angle']})"
    sample = (
        f"1. Counting each single/double/triple bond and any lone pair on the central atom as one domain gives {c['domains']} electron domains "
        f"(with {c['lp']} lone pair(s) on the central atom).\n"
        f"2. Shape: **{c['shape']}** with bond angle ≈ {c['angle']}."
    )
    return _pillars(
        qid=f"ps11_10_{rng.randint(10000, 99999)}",
        subskill="10_vsepr_multiple_bonds_as_single_domain",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Count {c['domains']} electron domains around central atom", "marks": 1},
            {"id": "mp2", "desc": f"Shape: {c['shape']} ({c['angle']})", "marks": 2},
        ],
        hints={
            "1_nudge": "Treat double and triple bonds as a single electron domain pointing in one direction.",
            "2_concept": "2 domains with 0 lone pairs -> linear; 3 domains with 0 lone pairs -> trigonal planar; 3 domains with 1 lone pair -> bent.",
            "3_breakdown": sample,
        },
        misconception_tags=["counting_double_bond_as_two_VSEPR_directions"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 11: Pauling Electronegativity Difference Calculation
# =========================================================================== #
def build_11_pauling_electronegativity_difference_calculation(rng: random.Random) -> Dict[str, Any]:
    bonds = [
        ("H", 2.1, "O", 3.5),
        ("H", 2.1, "Cl", 3.0),
        ("C", 2.5, "O", 3.5),
        ("Be", 1.5, "Cl", 3.0),
        ("Li", 1.0, "F", 4.0),
        ("Na", 0.9, "Cl", 3.0),
        ("H", 2.1, "C", 2.5),
        ("N", 3.0, "H", 2.1),
    ]
    a1, en1, a2, en2 = rng.choice(bonds)
    diff = round(abs(en2 - en1), 1)
    neg_atom = a2 if en2 > en1 else a1
    pos_atom = a1 if en2 > en1 else a2
    prompt = (
        f"Given the Pauling electronegativities $\\text{{EN}}({a1}) = {_fmt_sa(en1, 1)}$ and "
        f"$\\text{{EN}}({a2}) = {_fmt_sa(en2, 1)}$:\n\n"
        f"1. Calculate the electronegativity difference ($\\Delta\\text{{EN}}$) for the ${a1}\\text{{—}}{a2}$ bond.\n"
        f"2. Identify which atom pulls the shared bonding electrons more strongly."
    )
    ans = f"ΔEN = {_fmt_sa(diff, 1)}; {neg_atom} pulls shared electrons more strongly"
    sample = (
        f"1. $\\Delta\\text{{EN}} = |{_fmt_sa(en2, 1)} - {_fmt_sa(en1, 1)}| = {_fmt_sa(diff, 1)}$.\n"
        f"2. Because {neg_atom} has the higher electronegativity, {neg_atom} attracts the shared electron pair more strongly than {pos_atom}."
    )
    return _pillars(
        qid=f"ps11_11_{rng.randint(10000, 99999)}",
        subskill="11_pauling_electronegativity_difference_calculation",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Subtraction |{_fmt_sa(en2,1)} - {_fmt_sa(en1,1)}| = {_fmt_sa(diff,1)}", "marks": 2},
            {"id": "mp2", "desc": f"Identify {neg_atom} as stronger electron attractor", "marks": 1},
        ],
        hints={
            "1_nudge": "Electronegativity difference is always taken as a positive magnitude: |EN₁ - EN₂|.",
            "2_concept": "The element with the larger electronegativity attracts shared bonding electrons closer to itself.",
            "3_breakdown": sample,
        },
        misconception_tags=["negative_electronegativity_difference", "adding_instead_of_subtracting_EN"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 12: Bond Polarity Spectrum Classification
# =========================================================================== #
def build_12_bond_polarity_spectrum_classification(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"pair": "Cl–Cl in Cl₂", "en_a": 3.0, "en_b": 3.0, "btype": "Non-polar (pure) covalent"},
        {"pair": "C–H in CH₄", "en_a": 2.5, "en_b": 2.1, "btype": "Weakly polar covalent"},
        {"pair": "O–H in H₂O", "en_a": 3.5, "en_b": 2.1, "btype": "Strongly polar covalent"},
        {"pair": "Be–Cl in BeCl₂", "en_a": 1.5, "en_b": 3.0, "btype": "Strongly polar covalent"},
        {"pair": "Na–F in NaF", "en_a": 0.9, "en_b": 4.0, "btype": "Predominantly ionic"},
        {"pair": "K–Cl in KCl", "en_a": 0.8, "en_b": 3.0, "btype": "Predominantly ionic"},
    ]
    c = rng.choice(cases)
    den = round(abs(c["en_a"] - c["en_b"]), 1)
    prompt = (
        f"Using the standard electronegativity difference guidelines ($\\Delta\\text{{EN}} = 0$: non-polar covalent; "
        f"$0 < \\Delta\\text{{EN}} \\le 1{{,}}0$: weakly polar covalent; $1{{,}}0 < \\Delta\\text{{EN}} \\le 2{{,}}1$: strongly polar covalent; "
        f"$\\Delta\\text{{EN}} > 2{{,}}1$: ionic):\n\n"
        f"Calculate $\\Delta\\text{{EN}}$ and classify the **{c['pair']}** bond given individual electronegativities of "
        f"${_fmt_sa(c['en_a'], 1)}$ and ${_fmt_sa(c['en_b'], 1)}$."
    )
    ans = f"ΔEN = {_fmt_sa(den, 1)} -> {c['btype']}"
    sample = (
        f"$\\Delta\\text{{EN}} = |{_fmt_sa(c['en_a'], 1)} - {_fmt_sa(c['en_b'], 1)}| = {_fmt_sa(den, 1)}$.\n"
        f"Bond classification: **{c['btype']}**."
    )
    return _pillars(
        qid=f"ps11_12_{rng.randint(10000, 99999)}",
        subskill="12_bond_polarity_spectrum_classification",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Calculate ΔEN = {_fmt_sa(den, 1)}", "marks": 1},
            {"id": "mp2", "desc": f"Classify as {c['btype']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Find ΔEN = |EN₁ - EN₂| first.",
            "2_concept": "Compare ΔEN against the thresholds 0, 1,0, and 2,1.",
            "3_breakdown": sample,
        },
        misconception_tags=["classifying_ΔEN_0.4_as_nonpolar_or_ionic", "wrong_2.1_ionic_boundary"],
        marks=3,
        duration=3,
    )


# =========================================================================== #
# 13: Partial Charges & Dipole Representation (Inline SVG)
# =========================================================================== #
def build_13_partial_charges_dipole_arrow_representation(rng: random.Random) -> Dict[str, Any]:
    dipoles = [
        {"a": "H", "b": "Cl", "ena": 2.1, "enb": 3.0, "pos": "H", "neg": "Cl"},
        {"a": "H", "b": "Br", "ena": 2.1, "enb": 2.8, "pos": "H", "neg": "Br"},
        {"a": "C", "b": "O", "ena": 2.5, "enb": 3.5, "pos": "C", "neg": "O"},
        {"a": "H", "b": "F", "ena": 2.1, "enb": 4.0, "pos": "H", "neg": "F"},
        {"a": "S", "b": "O", "ena": 2.5, "enb": 3.5, "pos": "S", "neg": "O"},
    ]
    d = rng.choice(dipoles)
    svg = _svg_wrap(
        f'<rect x="30" y="35" width="300" height="110" rx="25" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>'
        f'<circle cx="110" cy="90" r="22" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<circle cx="250" cy="90" r="22" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<line x1="132" y1="90" x2="228" y2="90" stroke="#0f172a" stroke-width="2.5"/>'
        f'<text x="110" y="95" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a">{d["a"]}</text>'
        f'<text x="250" y="95" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#991b1b">{d["b"]}</text>'
        f'<text x="110" y="55" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563eb">δ⁺ ?</text>'
        f'<text x="250" y="55" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">δ⁻ ?</text>'
        f'<text x="180" y="172" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#475569">Polar covalent bond {d["a"]}—{d["b"]} (EN: {_fmt_sa(d["ena"],1)} vs {_fmt_sa(d["enb"],1)})</text>',
        width=360,
        height=195,
    )
    prompt = (
        f"Refer to the polar covalent bond schematic for ${d['a']}\\text{{—}}{d['b']}$ "
        f"($\\text{{EN}}({d['a']}) = {_fmt_sa(d['ena'], 1)}$; $\\text{{EN}}({d['b']}) = {_fmt_sa(d['enb'], 1)}$).\n\n"
        f"1. State which atom carries the partial positive charge ($\\delta^+$) and which carries the partial negative charge ($\\delta^-$).\n"
        f"2. State the direction in which the bond dipole points."
    )
    ans = f"{d['pos']} is δ⁺; {d['neg']} is δ⁻; dipole points from {d['pos']} towards {d['neg']}"
    sample = (
        f"1. {d['neg']} has higher electronegativity ({_fmt_sa(d['enb'], 1)} > {_fmt_sa(d['ena'], 1)}), so {d['neg']} carries $\\delta^-$ "
        f"and {d['pos']} carries $\\delta^+$.\n"
        f"2. Electron density shifts towards {d['neg']}, so the dipole points from {d['pos']} towards {d['neg']}."
    )
    return _pillars(
        qid=f"ps11_13_{rng.randint(10000, 99999)}",
        subskill="13_partial_charges_dipole_arrow_representation",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Assign δ⁺ to {d['pos']} and δ⁻ to {d['neg']}", "marks": 2},
            {"id": "mp2", "desc": f"Dipole arrow from {d['pos']} to {d['neg']}", "marks": 1},
        ],
        hints={
            "1_nudge": "The more electronegative atom pulls electron density closer and becomes slightly negative (δ⁻).",
            "2_concept": "Partial charges show unequal sharing without full electron transfer.",
            "3_breakdown": sample,
        },
        misconception_tags=["reversing_delta_plus_and_delta_minus", "writing_full_ionic_charges_on_covalent_bond"],
        marks=3,
        duration=3,
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Partial charge dipole ({d['a']}-{d['b']})"},
    )


# =========================================================================== #
# 14: Non-Polar Molecules with Polar Bonds (Symmetrical Cancellation)
# =========================================================================== #
def build_14_molecular_polarity_via_symmetry_and_shape(rng: random.Random) -> Dict[str, Any]:
    sym_mols = [
        {"formula": "CO₂", "shape": "linear", "bond": "C=O", "den": "1,0"},
        {"formula": "CH₄", "shape": "tetrahedral", "bond": "C–H", "den": "0,4"},
        {"formula": "CF₄", "shape": "tetrahedral", "bond": "C–F", "den": "1,5"},
        {"formula": "BF₃", "shape": "trigonal planar", "bond": "B–F", "den": "2,0"},
        {"formula": "CCl₄", "shape": "tetrahedral", "bond": "C–Cl", "den": "0,5"},
        {"formula": "BeCl₂", "shape": "linear", "bond": "Be–Cl", "den": "1,5"},
    ]
    m = rng.choice(sym_mols)
    prompt = (
        f"In a molecule of $\\text{{{m['formula']}}}$, each individual ${m['bond']}$ bond has an electronegativity difference "
        f"of $\\Delta\\text{{EN}} = {m['den']}$ and is therefore polar covalent.\n\n"
        f"Yet $\\text{{{m['formula']}}}$ is classified overall as a **non-polar molecule**. Explain why, referring to molecular shape and symmetry."
    )
    ans = f"Symmetrical {m['shape']} shape causes the polar bond dipoles to cancel out, giving zero net dipole moment"
    sample = (
        f"1. $\\text{{{m['formula']}}}$ has a symmetrical **{m['shape']}** geometry with identical terminal atoms and no lone pairs on the central atom.\n"
        f"2. The equal bond dipoles point symmetrically away from the centre and cancel each other out vectorially, "
        f"resulting in a symmetrical charge distribution (non-polar molecule)."
    )
    return _pillars(
        qid=f"ps11_14_{rng.randint(10000, 99999)}",
        subskill="14_molecular_polarity_via_symmetry_and_shape",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Identify symmetrical {m['shape']} molecular shape", "marks": 1},
            {"id": "mp2", "desc": "Equal bond dipoles cancel out / symmetrical charge distribution", "marks": 2},
        ],
        hints={
            "1_nudge": "Polar bonds do not automatically mean the entire molecule is polar.",
            "2_concept": "Symmetry determines whether vector bond dipoles cancel to zero.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_polar_bonds_always_mean_polar_molecule"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 15: Asymmetrical Polar Molecules Analysis
# =========================================================================== #
def build_15_asymmetrical_polar_molecules_analysis(rng: random.Random) -> Dict[str, Any]:
    asym = [
        {"formula": "CHF₃", "shape": "tetrahedral", "reason": "different terminal atoms (three F and one H) create an asymmetrical charge distribution"},
        {"formula": "BF₂Cl", "shape": "trigonal planar", "reason": "different terminal halogen atoms (F and Cl) prevent the bond dipoles from cancelling"},
        {"formula": "HCN", "shape": "linear", "reason": "asymmetrical linear molecule (H—C≡N) with unequal ends and net dipole towards nitrogen"},
        {"formula": "CHCl₃", "shape": "tetrahedral", "reason": "three polar C–Cl bonds and one C–H bond produce an unbalanced tetrahedral charge distribution"},
        {"formula": "NH₃", "shape": "trigonal pyramidal", "reason": "one lone pair on nitrogen makes the shape asymmetrical so the three N–H dipoles do not cancel"},
    ]
    a = rng.choice(asym)
    prompt = (
        f"Consider the molecule $\\text{{{a['formula']}}}$, which has a {a['shape']} molecular geometry.\n\n"
        f"1. State whether $\\text{{{a['formula']}}}$ is polar or non-polar.\n"
        f"2. Provide a full structural explanation for your answer."
    )
    ans = f"Polar molecule because {a['reason']}"
    sample = (
        f"1. $\\text{{{a['formula']}}}$ is a **polar molecule** (possesses a permanent dipole).\n"
        f"2. Even though the {a['shape']} arrangement looks balanced geometrically, {a['reason']}, resulting in a net dipole moment."
    )
    return _pillars(
        qid=f"ps11_15_{rng.randint(10000, 99999)}",
        subskill="15_asymmetrical_polar_molecules_analysis",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Correctly state: polar molecule", "marks": 1},
            {"id": "mp2", "desc": f"Reason: {a['reason']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Check both the molecular shape (lone pairs) AND whether all terminal atoms are identical.",
            "2_concept": "If terminal atoms differ or a lone pair causes asymmetry, bond dipoles cannot cancel.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_all_tetrahedral_molecules_are_nonpolar"],
        marks=3,
        duration=4,
    )


# =========================================================================== #
# 16: Bond Energy Enthalpy Estimate Calculation
# =========================================================================== #
def build_16_bond_energy_enthalpy_estimate_calculations(rng: random.Random) -> Dict[str, Any]:
    rxns = [
        {
            "eq": "H₂(g) + Cl₂(g) → 2HCl(g)",
            "broken_desc": "1(H–H) + 1(Cl–Cl)",
            "broken_val": 436 + 243,
            "formed_desc": "2(H–Cl)",
            "formed_val": 2 * 432,
            "given": "E(H–H) = 436 kJ/mol, E(Cl–Cl) = 243 kJ/mol, E(H–Cl) = 432 kJ/mol",
        },
        {
            "eq": "2H₂(g) + O₂(g) → 2H₂O(g)",
            "broken_desc": "2(H–H) + 1(O=O)",
            "broken_val": 2 * 436 + 498,
            "formed_desc": "4(O–H)",
            "formed_val": 4 * 464,
            "given": "E(H–H) = 436 kJ/mol, E(O=O) = 498 kJ/mol, E(O–H) = 464 kJ/mol",
        },
        {
            "eq": "N₂(g) + 3H₂(g) → 2NH₃(g)",
            "broken_desc": "1(N≡N) + 3(H–H)",
            "broken_val": 945 + 3 * 436,
            "formed_desc": "6(N–H)",
            "formed_val": 6 * 391,
            "given": "E(N≡N) = 945 kJ/mol, E(H–H) = 436 kJ/mol, E(N–H) = 391 kJ/mol",
        },
    ]
    r = rng.choice(rxns)
    dh = r["broken_val"] - r["formed_val"]
    exo = "exothermic" if dh < 0 else "endothermic"
    prompt = (
        f"Consider the gas-phase reaction:\n"
        f"$${r['eq']}$$\n\n"
        f"Using the average bond energies ({r['given']}):\n"
        f"1. Calculate the total energy absorbed to break the reactant bonds.\n"
        f"2. Calculate the total energy released when product bonds form.\n"
        f"3. Determine $\\Delta H$ and state whether the reaction is exothermic or endothermic."
    )
    ans = f"ΔH = {dh} kJ/mol ({exo})"
    sample = (
        f"1. Energy absorbed (bonds broken) = {r['broken_desc']} = {r['broken_val']} kJ·mol⁻¹.\n"
        f"2. Energy released (bonds formed) = {r['formed_desc']} = {r['formed_val']} kJ·mol⁻¹.\n"
        f"3. $\\Delta H = \\sum E_{{\\text{{broken}}}} - \\sum E_{{\\text{{formed}}}} = {r['broken_val']} - {r['formed_val']} = {dh}\\text{{ kJ·mol}}^{{-1}}$.\n"
        f"Since $\\Delta H {'<' if dh < 0 else '>'} 0$, the reaction is **{exo}**."
    )
    return _pillars(
        qid=f"ps11_16_{rng.randint(10000, 99999)}",
        subskill="16_bond_energy_enthalpy_estimate_calculations",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Bonds broken = {r['broken_val']} kJ/mol", "marks": 1},
            {"id": "mp2", "desc": f"Bonds formed = {r['formed_val']} kJ/mol", "marks": 1},
            {"id": "mp3", "desc": f"ΔH = {dh} kJ/mol", "marks": 1},
            {"id": "mp4", "desc": f"Classify as {exo}", "marks": 1},
        ],
        hints={
            "1_nudge": "Bond breaking is endothermic (+); bond formation is exothermic (-).",
            "2_concept": "ΔH = Σ(Energy of bonds broken) - Σ(Energy of bonds formed).",
            "3_breakdown": sample,
        },
        misconception_tags=["reversing_formed_minus_broken", "forgetting_stoichiometric_bond_multipliers"],
        marks=4,
        duration=5,
    )


# =========================================================================== #
# 17: Intramolecular vs Intermolecular Forces Distinction (Inline SVG)
# =========================================================================== #
def build_17_intramolecular_vs_intermolecular_forces_distinction(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        {"formula": "HCl", "bond": "H—Cl covalent bond", "imf": "dipole-dipole forces"},
        {"formula": "H₂O", "bond": "O—H covalent bond", "imf": "hydrogen bonding"},
        {"formula": "Br₂", "bond": "Br—Br covalent bond", "imf": "induced dipole (London) forces"},
    ]
    p = rng.choice(pairs)
    svg = _svg_wrap(
        f'<circle cx="80" cy="100" r="18" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<circle cx="150" cy="100" r="18" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="98" y1="100" x2="132" y2="100" stroke="#1e40af" stroke-width="4"/>'
        f'<text x="115" y="75" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1e40af">Force A</text>'
        f'<line x1="168" y1="100" x2="212" y2="100" stroke="#9333ea" stroke-width="2.5" stroke-dasharray="5,4"/>'
        f'<text x="190" y="75" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#7e22ce">Force B</text>'
        f'<circle cx="230" cy="100" r="18" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<circle cx="300" cy="100" r="18" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<line x1="248" y1="100" x2="282" y2="100" stroke="#1e40af" stroke-width="4"/>'
        f'<text x="190" y="155" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#0f172a">System: Adjacent {p["formula"]} molecules</text>',
        width=380,
        height=185,
    )
    prompt = (
        f"Refer to the molecular schematic illustrating two adjacent $\\text{{{p['formula']}}}$ molecules.\n\n"
        f"1. Identify whether **Force A** (solid line within a molecule) and **Force B** (dashed line between molecules) "
        f"are intramolecular or intermolecular forces, and name the specific type of each for $\\text{{{p['formula']}}}$.\n"
        f"2. State which force (A or B) is overcome when liquid $\\text{{{p['formula']}}}$ boils."
    )
    ans = f"Force A: intramolecular ({p['bond']}); Force B: intermolecular ({p['imf']}); boiling overcomes Force B"
    sample = (
        f"1. **Force A** is an intramolecular (interatomic) force — specifically the **{p['bond']}**.\n"
        f"   **Force B** is an intermolecular force — specifically **{p['imf']}**.\n"
        f"2. Boiling is a physical phase change that overcomes **Force B** (intermolecular forces) without breaking Force A (covalent bonds)."
    )
    return _pillars(
        qid=f"ps11_17_{rng.randint(10000, 99999)}",
        subskill="17_intramolecular_vs_intermolecular_forces_distinction",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Force A = intramolecular {p['bond']}", "marks": 1},
            {"id": "mp2", "desc": f"Force B = intermolecular {p['imf']}", "marks": 1},
            {"id": "mp3", "desc": "Physical boiling overcomes Force B (intermolecular forces)", "marks": 1},
        ],
        hints={
            "1_nudge": "Intra- means within a single molecule; inter- means between separate molecules.",
            "2_concept": "Phase changes (melting/boiling) only overcome intermolecular forces, leaving covalent molecules intact.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_boiling_breaks_covalent_bonds"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Intramolecular vs Intermolecular forces ({p['formula']})"},
    )


# =========================================================================== #
# 18: London Dispersion (Induced Dipole) Forces
# =========================================================================== #
def build_18_london_induced_dipole_dispersion_forces(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("I₂(s) (solid iodine)", "non-polar diatomic molecule"),
        ("CO₂(s) (dry ice)", "non-polar linear molecule"),
        ("CH₄(l) (liquid methane)", "non-polar tetrahedral molecule"),
        ("CCl₄(l) (tetrachloromethane)", "non-polar tetrahedral molecule"),
        ("Ar(l) (liquid argon)", "monatomic noble gas atom"),
    ]
    sub, desc = rng.choice(substances)
    prompt = (
        f"Even though **{sub}** is a {desc} with no permanent dipole, it can be condensed into a liquid and frozen into a solid at low temperatures.\n\n"
        f"1. Name the intermolecular force acting between particles of {sub}.\n"
        f"2. Explain briefly how this attractive force originates between non-polar particles."
    )
    ans = "Induced dipole (London dispersion) forces formed by temporary fluctuations in electron distribution inducing dipoles in neighbouring molecules"
    sample = (
        f"1. **Induced dipole (London dispersion) forces**.\n"
        f"2. Random motion of electrons causes an instantaneous uneven distribution of charge, creating a temporary dipole in one particle. "
        f"This temporary dipole distorts the electron cloud of an adjacent particle, inducing an opposite temporary dipole that produces weak electrostatic attraction."
    )
    return _pillars(
        qid=f"ps11_18_{rng.randint(10000, 99999)}",
        subskill="18_london_induced_dipole_dispersion_forces",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Name: induced dipole / London / dispersion forces", "marks": 1},
            {"id": "mp2", "desc": "Momentary uneven electron density creates temporary dipole", "marks": 1},
            {"id": "mp3", "desc": "Induces complementary dipole in neighbouring particle", "marks": 1},
        ],
        hints={
            "1_nudge": "Electrons move constantly and are not always distributed symmetrically at any single instant.",
            "2_concept": "Temporary instantaneous dipoles induce dipoles in nearby non-polar molecules.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_nonpolar_molecules_have_no_IMF"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 19: Dipole-Dipole Forces in Polar Molecules
# =========================================================================== #
def build_19_dipole_dipole_interactions_polar_molecules(rng: random.Random) -> Dict[str, Any]:
    mols = [
        ("HCl", "hydrogen chloride", "linear"),
        ("H₂S", "hydrogen sulfide", "bent (angular)"),
        ("SO₂", "sulfur dioxide", "bent (angular)"),
        ("CH₃Cl", "chloromethane", "tetrahedral"),
        ("HBr", "hydrogen bromide", "linear"),
    ]
    f, name, shape = rng.choice(mols)
    prompt = (
        f"Consider pure liquid **{name}** ($\\text{{{f}}}$), which consists of {shape} polar molecules.\n\n"
        f"1. Identify the strongest intermolecular force acting between $\\text{{{f}}}$ molecules.\n"
        f"2. Explain why hydrogen bonding does **not** occur between $\\text{{{f}}}$ molecules."
    )
    ans = f"Dipole-dipole forces; {f} lacks H bonded directly to N, O, or F"
    sample = (
        f"1. **Dipole-dipole forces** (alongside weaker induced dipole forces) act between the $\\delta^+$ and $\\delta^-$ poles of adjacent {f} molecules.\n"
        f"2. Hydrogen bonding only occurs when hydrogen is covalently bonded to a small, highly electronegative atom of **N, O, or F**; {f} does not satisfy this requirement."
    )
    return _pillars(
        qid=f"ps11_19_{rng.randint(10000, 99999)}",
        subskill="19_dipole_dipole_interactions_polar_molecules",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Identify dipole-dipole forces", "marks": 1},
            {"id": "mp2", "desc": "State that hydrogen bonding requires H bonded to N, O, or F", "marks": 2},
        ],
        hints={
            "1_nudge": "Polar molecules with permanent dipoles attract each other via opposite partial charges.",
            "2_concept": "Hydrogen bonding is restricted to H covalently bonded to N, O, or F.",
            "3_breakdown": sample,
        },
        misconception_tags=["assuming_any_molecule_with_H_has_hydrogen_bonding"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 20: Hydrogen Bonding Criteria & Examples (Inline SVG)
# =========================================================================== #
def build_20_hydrogen_bonding_criteria_and_examples(rng: random.Random) -> Dict[str, Any]:
    hb_mols = [
        {"formula": "HF", "atom": "F (fluorine)", "en": "4,0"},
        {"formula": "H₂O", "atom": "O (oxygen)", "en": "3,5"},
        {"formula": "NH₃", "atom": "N (nitrogen)", "en": "3,0"},
        {"formula": "CH₃OH", "atom": "O (oxygen)", "en": "3,5"},
    ]
    m = rng.choice(hb_mols)
    svg = _svg_wrap(
        f'<text x="90" y="95" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">{m["formula"]}</text>'
        f'<text x="90" y="115" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#2563eb">(H δ⁺)</text>'
        f'<line x1="125" y1="100" x2="225" y2="100" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="5,4"/>'
        f'<text x="175" y="85" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">Hydrogen bond</text>'
        f'<text x="265" y="95" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">{m["formula"]}</text>'
        f'<text x="265" y="115" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#dc2626">({m["atom"].split()[0]} δ⁻)</text>'
        f'<text x="180" y="160" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#475569">EN of {m["atom"].split()[0]} = {m["en"]}</text>',
        width=360,
        height=185,
    )
    prompt = (
        f"Refer to the diagram illustrating the strong intermolecular attraction between adjacent $\\text{{{m['formula']}}}$ molecules.\n\n"
        f"1. State the two structural requirements necessary for **hydrogen bonding** to form between molecules.\n"
        f"2. Explain why hydrogen bonds between $\\text{{{m['formula']}}}$ molecules are significantly stronger than ordinary dipole-dipole forces."
    )
    ans = f"H covalently bonded to small highly electronegative {m['atom']} (EN={m['en']}) + lone pair on adjacent {m['atom'].split()[0]}"
    sample = (
        f"1. (i) A hydrogen atom must be covalently bonded directly to a small, highly electronegative atom (N, O, or F — here {m['atom']}). "
        f"(ii) An adjacent molecule must possess a lone pair on N, O, or F.\n"
        f"2. Because {m['atom']} has very high electronegativity ({m['en']}) and a small atomic radius, the H atom becomes strongly $\\delta^+$ "
        f"and attracts the concentrated lone pair on the neighbouring {m['atom'].split()[0]} atom strongly."
    )
    return _pillars(
        qid=f"ps11_20_{rng.randint(10000, 99999)}",
        subskill="20_hydrogen_bonding_criteria_and_examples",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "H covalently bonded to small highly electronegative atom (N, O, or F)", "marks": 1},
            {"id": "mp2", "desc": "Lone pair on N, O, or F of neighbouring molecule", "marks": 1},
            {"id": "mp3", "desc": "Large δ⁺ on H and small atomic size produce intense dipole attraction", "marks": 1},
        ],
        hints={
            "1_nudge": "Remember the three small, highly electronegative elements: N, O, and F.",
            "2_concept": "Hydrogen bonding is a special, very strong case of dipole-dipole attraction.",
            "3_breakdown": sample,
        },
        misconception_tags=["calling_hydrogen_bond_an_intramolecular_covalent_bond"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Hydrogen bonding interaction ({m['formula']})"},
    )


# =========================================================================== #
# 21: Ion-Dipole Hydration & Dissolution (Inline SVG)
# =========================================================================== #
def build_21_ion_dipole_hydration_and_dissolution(rng: random.Random) -> Dict[str, Any]:
    salts = [
        ("NaCl", "Na⁺", "Cl⁻"),
        ("KCl", "K⁺", "Cl⁻"),
        ("KI", "K⁺", "I⁻"),
        ("NaBr", "Na⁺", "Br⁻"),
    ]
    salt, cat, ani = rng.choice(salts)
    svg = _svg_wrap(
        f'<circle cx="110" cy="100" r="22" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="110" y="105" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a">{cat}</text>'
        f'<text x="110" y="55" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#dc2626">O(δ⁻)—H₂</text>'
        f'<line x1="110" y1="62" x2="110" y2="78" stroke="#475569" stroke-dasharray="3,2"/>'
        f'<circle cx="260" cy="100" r="22" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
        f'<text x="260" y="105" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#14532d">{ani}</text>'
        f'<text x="260" y="55" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#2563eb">H(δ⁺)—OH</text>'
        f'<line x1="260" y1="62" x2="260" y2="78" stroke="#475569" stroke-dasharray="3,2"/>'
        f'<text x="185" y="170" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#0f172a">Hydration of {salt}(aq) in H₂O</text>',
        width=370,
        height=190,
    )
    prompt = (
        f"Refer to the hydration diagram showing solid **{salt}** dissolving in water ($\\text{{{salt}(aq)}}$).\n\n"
        f"1. Name the intermolecular force formed between the dissolved ions and water molecules.\n"
        f"2. Describe how water molecules orient themselves around the **{cat}** cation versus the **{ani}** anion."
    )
    ans = f"Ion-dipole forces; δ⁻ oxygen end faces {cat}, while δ⁺ hydrogen ends face {ani}"
    sample = (
        f"1. **Ion-dipole forces** form between the charged ions and polar water dipoles.\n"
        f"2. The partially negative oxygen end ($\\delta^-$) of water is attracted to and faces the positive {cat} ion, "
        f"whereas the partially positive hydrogen ends ($\\delta^+$) orient towards the negative {ani} ion, weakening the ionic crystal lattice."
    )
    return _pillars(
        qid=f"ps11_21_{rng.randint(10000, 99999)}",
        subskill="21_ion_dipole_hydration_and_dissolution",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Identify ion-dipole forces", "marks": 1},
            {"id": "mp2", "desc": f"Water O(δ⁻) attracts {cat}; H(δ⁺) attracts {ani}", "marks": 2},
        ],
        hints={
            "1_nudge": "Opposite charges attract: ions attract the oppositely charged poles of polar water molecules.",
            "2_concept": "In water, oxygen carries δ⁻ and hydrogens carry δ⁺.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_ion_dipole_with_dipole_dipole"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context", "title": f"Ion-dipole hydration ({salt} in water)"},
    )


# =========================================================================== #
# 22: Ion-Induced Dipole and Dipole-Induced Dipole Forces
# =========================================================================== #
def build_22_ion_induced_and_dipole_induced_dipole_forces(rng: random.Random) -> Dict[str, Any]:
    mixtures = [
        ("O₂ gas dissolved in water (H₂O)", "dipole-induced dipole forces", "polar H₂O molecule induces a temporary dipole in non-polar O₂"),
        ("CHCl₃ (polar) mixed with CCl₄ (non-polar)", "dipole-induced dipole forces", "polar CHCl₃ induces a temporary dipole in non-polar CCl₄"),
        ("Fe²⁺ ion interacting with O₂ in haemoglobin", "ion-induced dipole forces", "positively charged Fe²⁺ ion distorts the electron cloud of non-polar O₂"),
        ("MgCl₂(s) interacting with non-polar CCl₄", "ion-induced dipole forces", "ions induce weak temporary dipoles in non-polar CCl₄ molecules"),
    ]
    mix, force_type, mech = rng.choice(mixtures)
    prompt = (
        f"Identify the specific type of intermolecular force operating in the system: **{mix}**.\n\n"
        f"Explain briefly how this attraction arises between the two species."
    )
    ans = f"{force_type} ({mech})"
    sample = f"Force type: **{force_type}**.\nMechanism: The {mech}."
    return _pillars(
        qid=f"ps11_22_{rng.randint(10000, 99999)}",
        subskill="22_ion_induced_and_dipole_induced_dipole_forces",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Correct identification: {force_type}", "marks": 1},
            {"id": "mp2", "desc": f"Mechanism: {mech}", "marks": 2},
        ],
        hints={
            "1_nudge": "Classify each partner as an ion, a permanent polar dipole, or a non-polar molecule.",
            "2_concept": "Ion + non-polar = ion-induced dipole; polar dipole + non-polar = dipole-induced dipole.",
            "3_breakdown": sample,
        },
        misconception_tags=["confusing_ion_induced_with_dipole_induced"],
        marks=3,
        duration=3,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 23: Van der Waals Forces Classification
# =========================================================================== #
def build_23_van_der_waals_forces_classification(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("Dipole-dipole, dipole-induced dipole, and induced dipole (London) forces", "Ion-dipole forces and covalent bonds are NOT van der Waals forces", "ion-dipole forces"),
        ("HCl(l), CHCl₃ in CCl₄, and I₂(s)", "All three exhibit van der Waals intermolecular forces (dipole-dipole, dipole-induced dipole, induced dipole)", "covalent network bonds"),
        ("Dipole-dipole, induced dipole, and dipole-induced dipole forces", "Hydrogen bonding is a strong sub-type of dipole-dipole attraction, whereas ionic and covalent bonds are intramolecular/lattice forces", "ionic bonds"),
    ]
    pair_a, note, excluded = rng.choice(scenarios)
    options = [
        "Dipole-dipole, dipole-induced dipole, and induced dipole forces",
        "Ion-dipole, ion-induced dipole, and covalent bonds",
        "Ionic bonds, metallic bonds, and hydrogen bonds",
        "Ion-dipole, dipole-dipole, and covalent network bonds",
    ]
    correct = options[0]
    rng.shuffle(options)
    opts_text = "\n".join(f"- {opt}" for opt in options)
    prompt = (
        f"Which ONE of the following groups lists ONLY intermolecular forces collectively classified as **van der Waals forces**?\n\n"
        f"{opts_text}\n\n"
        f"State your choice and explain why **{excluded}** are excluded from van der Waals forces."
    )
    sample = (
        f"Correct choice: **{correct}**.\n"
        f"Reason: {note} because van der Waals forces operate exclusively between neutral molecules (or atoms), whereas ion-dipole involves a charged ion."
    )
    return _pillars(
        qid=f"ps11_23_{rng.randint(10000, 99999)}",
        subskill="23_van_der_waals_forces_classification",
        prompt=prompt,
        answer=correct,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"Select {correct}", "marks": 1},
            {"id": "mp2", "desc": "Explain exclusion of ion-dipole (involves ions, not neutral molecules)", "marks": 2},
        ],
        hints={
            "1_nudge": "Van der Waals forces act between electrically neutral molecules/atoms.",
            "2_concept": "The three van der Waals forces are dipole-dipole, dipole-induced dipole, and induced dipole.",
            "3_breakdown": sample,
        },
        misconception_tags=["including_ion_dipole_in_van_der_waals"],
        marks=3,
        duration=3,
        topic_label="Intermolecular forces",
        question_type="mcq",
        options=options,
    )


# =========================================================================== #
# 24: Molecular Mass and Surface Area Effect on London Forces
# =========================================================================== #
def build_24_molecular_mass_and_surface_area_on_london_forces(rng: random.Random) -> Dict[str, Any]:
    series = [
        {
            "group": "Halogens",
            "a": "F₂ (gas, -188 °C)",
            "b": "Cl₂ (gas, -34 °C)",
            "c": "Br₂ (liquid, 59 °C)",
            "d": "I₂ (solid, 184 °C)",
            "why": "molecular mass and electron cloud size increase from F₂ to I₂",
        },
        {
            "group": "Alkanes",
            "a": "CH₄ (methane, M = 16 g/mol, -164 °C)",
            "b": "C₂H₆ (ethane, M = 30 g/mol, -89 °C)",
            "c": "C₅H₁₂ (pentane, M = 72 g/mol, 36 °C)",
            "d": "C₂₀H₄₂ (icosane, M = 282 g/mol, 343 °C)",
            "why": "carbon chain length, molar mass, and surface contact area increase from CH₄ to C₂₀H₄₂",
        },
    ]
    s = rng.choice(series)
    prompt = (
        f"Consider the series of non-polar **{s['group']}** with their boiling points at standard pressure:\n"
        f"- {s['a']}\n- {s['b']}\n- {s['c']}\n- {s['d']}\n\n"
        f"1. Name the intermolecular force present in all four non-polar substances.\n"
        f"2. Explain why the boiling point and phase change from gas to liquid to solid across this series."
    )
    ans = f"Induced dipole (London) forces; {s['why']}, increasing induced dipole strength and energy needed to boil"
    sample = (
        f"1. **Induced dipole (London dispersion) forces**.\n"
        f"2. As {s['why']}, the electron cloud is more easily polarised (more temporary dipoles form). "
        f"This strengthens the induced dipole intermolecular forces, requiring more thermal energy to separate molecules and raising the boiling point."
    )
    return _pillars(
        qid=f"ps11_24_{rng.randint(10000, 99999)}",
        subskill="24_molecular_mass_and_surface_area_on_london_forces",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": "Identify induced dipole (London) forces", "marks": 1},
            {"id": "mp2", "desc": f"Note increase in molecular mass / size / surface area: {s['why']}", "marks": 1},
            {"id": "mp3", "desc": "Link to stronger IMF and more energy required to separate molecules", "marks": 1},
        ],
        hints={
            "1_nudge": "Non-polar molecules only experience induced dipole (London) forces.",
            "2_concept": "Larger molar mass and surface area produce stronger temporary dipoles.",
            "3_breakdown": sample,
        },
        misconception_tags=["claiming_stronger_covalent_bonds_increase_boiling_point"],
        marks=3,
        duration=4,
        topic_label="Intermolecular forces",
    )


# =========================================================================== #
# 25: Atomic Combinations VSEPR + Polarity + IMF Synthesis
# =========================================================================== #
def build_25_atomic_combinations_vsepr_polarity_synthesis(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {"f": "NH₃", "en_c": 3.0, "en_l": 2.1, "bp": 3, "lp": 1, "shape": "Trigonal pyramidal", "polar": "Polar", "imf": "Hydrogen bonding"},
        {"f": "CH₄", "en_c": 2.5, "en_l": 2.1, "bp": 4, "lp": 0, "shape": "Tetrahedral", "polar": "Non-polar", "imf": "Induced dipole (London) forces"},
        {"f": "H₂O", "en_c": 3.5, "en_l": 2.1, "bp": 2, "lp": 2, "shape": "Bent / Angular", "polar": "Polar", "imf": "Hydrogen bonding"},
        {"f": "CO₂", "en_c": 2.5, "en_l": 3.5, "bp": 2, "lp": 0, "shape": "Linear", "polar": "Non-polar", "imf": "Induced dipole (London) forces"},
    ]
    c = rng.choice(cases)
    den = round(abs(c["en_c"] - c["en_l"]), 1)
    prompt = (
        f"Analyse the molecule $\\text{{{c['f']}}}$ completely (electronegativities: central = ${_fmt_sa(c['en_c'], 1)}$, terminal = ${_fmt_sa(c['en_l'], 1)}$):\n\n"
        f"1. Calculate $\\Delta\\text{{EN}}$ for each bond and classify the bond polarity.\n"
        f"2. State the number of bonding pairs and lone pairs around the central atom and name the VSEPR shape.\n"
        f"3. Deduce overall molecular polarity and state the strongest intermolecular force present in pure $\\text{{{c['f']}}}$."
    )
    ans = f"ΔEN = {_fmt_sa(den,1)} (polar bond); {c['shape']}; {c['polar']} molecule; {c['imf']}"
    sample = (
        f"1. $\\Delta\\text{{EN}} = {_fmt_sa(den, 1)}$ -> polar covalent bond.\n"
        f"2. {c['bp']} bonding domain(s), {c['lp']} lone pair(s) -> VSEPR shape: **{c['shape']}**.\n"
        f"3. Overall molecular polarity: **{c['polar']}**. Dominant IMF: **{c['imf']}**."
    )
    return _pillars(
        qid=f"ps11_25_{rng.randint(10000, 99999)}",
        subskill="25_atomic_combinations_vsepr_polarity_synthesis",
        prompt=prompt,
        answer=ans,
        sample=sample,
        marking_points=[
            {"id": "mp1", "desc": f"ΔEN = {_fmt_sa(den, 1)} (polar covalent bond)", "marks": 1},
            {"id": "mp2", "desc": f"{c['bp']} bonding, {c['lp']} lone pairs -> {c['shape']}", "marks": 2},
            {"id": "mp3", "desc": f"{c['polar']} molecule with {c['imf']}", "marks": 2},
        ],
        hints={
            "1_nudge": "Follow the 3-step chain: ΔEN -> VSEPR shape & symmetry -> molecular polarity -> IMF.",
            "2_concept": "Symmetrical shapes without lone pairs cancel bond dipoles; asymmetrical shapes remain polar.",
            "3_breakdown": sample,
        },
        misconception_tags=["polar_bond_equals_polar_molecule", "omitted_lone_pair_repulsion"],
        marks=5,
        duration=6,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_valence_electrons_and_octet_rule": build_01_valence_electrons_and_octet_rule,
    "02_potential_energy_curve_bond_formation": build_02_potential_energy_curve_bond_formation,
    "03_bond_length_vs_bond_strength_energy": build_03_bond_length_vs_bond_strength_energy,
    "04_lewis_dot_diagrams_single_covalent_bonds": build_04_lewis_dot_diagrams_single_covalent_bonds,
    "05_lewis_dot_diagrams_multiple_bonds": build_05_lewis_dot_diagrams_multiple_bonds,
    "06_dative_coordinate_covalent_bonding": build_06_dative_coordinate_covalent_bonding,
    "07_octet_rule_exceptions_incomplete_and_expanded": build_07_octet_rule_exceptions_incomplete_and_expanded,
    "08_vsepr_ideal_shapes_no_lone_pairs": build_08_vsepr_ideal_shapes_no_lone_pairs,
    "09_vsepr_shapes_with_lone_pairs_distortion": build_09_vsepr_shapes_with_lone_pairs_distortion,
    "10_vsepr_multiple_bonds_as_single_domain": build_10_vsepr_multiple_bonds_as_single_domain,
    "11_pauling_electronegativity_difference_calculation": build_11_pauling_electronegativity_difference_calculation,
    "12_bond_polarity_spectrum_classification": build_12_bond_polarity_spectrum_classification,
    "13_partial_charges_dipole_arrow_representation": build_13_partial_charges_dipole_arrow_representation,
    "14_molecular_polarity_via_symmetry_and_shape": build_14_molecular_polarity_via_symmetry_and_shape,
    "15_asymmetrical_polar_molecules_analysis": build_15_asymmetrical_polar_molecules_analysis,
    "16_bond_energy_enthalpy_estimate_calculations": build_16_bond_energy_enthalpy_estimate_calculations,
    "17_intramolecular_vs_intermolecular_forces_distinction": build_17_intramolecular_vs_intermolecular_forces_distinction,
    "18_london_induced_dipole_dispersion_forces": build_18_london_induced_dipole_dispersion_forces,
    "19_dipole_dipole_interactions_polar_molecules": build_19_dipole_dipole_interactions_polar_molecules,
    "20_hydrogen_bonding_criteria_and_examples": build_20_hydrogen_bonding_criteria_and_examples,
    "21_ion_dipole_hydration_and_dissolution": build_21_ion_dipole_hydration_and_dissolution,
    "22_ion_induced_and_dipole_induced_dipole_forces": build_22_ion_induced_and_dipole_induced_dipole_forces,
    "23_van_der_waals_forces_classification": build_23_van_der_waals_forces_classification,
    "24_molecular_mass_and_surface_area_on_london_forces": build_24_molecular_mass_and_surface_area_on_london_forces,
    "25_atomic_combinations_vsepr_polarity_synthesis": build_25_atomic_combinations_vsepr_polarity_synthesis,
}
