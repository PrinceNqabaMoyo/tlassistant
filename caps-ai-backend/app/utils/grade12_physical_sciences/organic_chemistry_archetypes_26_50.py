"""Grade 12 Physical Sciences — Organic Chemistry Archetypes (Subskills 26–50).
Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/04. Organic molecules.md

Covers:
- Physical properties: Intermolecular forces (London/dispersion, dipole-dipole, hydrogen bonding),
  boiling point comparisons (chain length, branching, functional groups), vapour pressure, melting points,
  viscosity, flammability, water solubility.
- Organic reactions:
  - Combustion (complete oxidation of alkanes).
  - Addition reactions (hydrogenation, halogenation, hydrohalogenation & Markovnikov's rule, hydration).
  - Elimination reactions (dehydrohalogenation & Zaitsev's rule, dehydration of alcohols, cracking).
  - Substitution reactions (halogenation of alkanes with UV light, hydrolysis of haloalkanes, alcohols with HX).
  - Esterification (condensation reaction, mechanism, conditions, fragrance/flavour synthesis).
- Polymers & Plastics:
  - Addition polymerisation (polyethene, PVC, Teflon, polypropene).
  - Condensation polymerisation (polyesters / PET, polyamides / nylon).
- Reaction pathways & comprehensive diagnostic synthesis autopsy.

100% deterministic Python, zero LLM calls, strictly < 2000 lines.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Formats numbers with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _svg_spec(svg: str) -> Dict[str, Any]:
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


# ==============================================================================
# 26. Intermolecular Forces in Organic Molecules
# ==============================================================================
def builder_26(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_26_imf_types", seed, idx)
    pairs = [
        {"cmpA": "propane (CH₃CH₂CH₃)", "typeA": "London (dispersion) forces", "groupA": "alkane", "cmpB": "propan-1-ol (CH₃CH₂CH₂OH)", "typeB": "hydrogen bonding (and London forces)", "groupB": "alcohol"},
        {"cmpA": "butane (CH₃(CH₂)₂CH₃)", "typeA": "London (dispersion) forces", "groupA": "alkane", "cmpB": "butanoic acid (CH₃(CH₂)₂COOH)", "typeB": "strong hydrogen bonding (forms dimers)", "groupB": "carboxylic acid"},
        {"cmpA": "ethane (CH₃CH₃)", "typeA": "London (dispersion) forces", "groupA": "alkane", "cmpB": "chloroethane (CH₃CH₂Cl)", "typeB": "dipole-dipole forces (and London forces)", "groupB": "haloalkane"},
        {"cmpA": "pentane (CH₃(CH₂)₃CH₃)", "typeA": "London (dispersion) forces", "groupA": "alkane", "cmpB": "pentan-2-one (CH₃COCH₂CH₂CH₃)", "typeB": "dipole-dipole forces (and London forces)", "groupB": "ketone"},
    ]
    chosen = rng.choice(pairs)
    temp_seed = rng.randint(20, 25)

    prompt = (
        f"Consider two organic compounds tested under standard atmospheric conditions at {temp_seed} °C:\n"
        f"• Compound A: {chosen['cmpA']} ({chosen['groupA']})\n"
        f"• Compound B: {chosen['cmpB']} ({chosen['groupB']})\n\n"
        f"1. Name the dominant type of intermolecular force acting between molecules of Compound A.\n"
        f"2. Name the dominant type of intermolecular force acting between molecules of Compound B.\n"
        f"3. Explain why the intermolecular forces in Compound B are significantly stronger than those in Compound A."
    )
    ans_str = (
        f"1. {chosen['typeA']}; 2. {chosen['typeB']}; "
        f"3. Compound B contains a polar functional group capable of {chosen['typeB']}, whereas Compound A is non-polar and experiences only weak London forces."
    )
    memo = (
        f"1. Dominant IMF in Compound A: {chosen['typeA']}. [1]\n"
        f"2. Dominant IMF in Compound B: {chosen['typeB']}. [1]\n"
        f"3. Compound A is a non-polar hydrocarbon with only temporary induced dipole (London) forces. "
        f"Compound B possesses a polar functional group resulting in permanent dipoles or hydrogen bonding (O-H / C=O bond), "
        f"which requires significantly more energy to overcome than weak London forces. [3]"
    )
    hints = {
        "tier_1": "Determine the functional group of each compound to identify its polarity.",
        "tier_2": "Alkanes are non-polar (London forces). Alcohols have -OH (hydrogen bonding). Ketones/haloalkanes have dipole-dipole.",
        "tier_3": f"Compound A ({chosen['groupA']}): {chosen['typeA']}. Compound B ({chosen['groupB']}): {chosen['typeB']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="190" height="140" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="115" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">Compound A ({chosen["groupA"]})</text>'
        f'<text x="115" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{chosen["cmpA"]}</text>'
        f'<text x="115" y="110" text-anchor="middle" font-size="11" fill="#475569">IMF: {chosen["typeA"]}</text>'
        f'<text x="115" y="140" text-anchor="middle" font-size="10" fill="#64748b">T = {temp_seed} °C</text>'
        f'<rect x="230" y="20" width="190" height="140" rx="8" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="325" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">Compound B ({chosen["groupB"]})</text>'
        f'<text x="325" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{chosen["cmpB"]}</text>'
        f'<text x="325" y="110" text-anchor="middle" font-size="11" fill="#475569">IMF: {chosen["typeB"]}</text>'
        f'<text x="325" y="140" text-anchor="middle" font-size="10" fill="#64748b">T = {temp_seed} °C</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "26_intermolecular_forces_london_dipole_hydrogen_in_organics",
        "subskill": "26_intermolecular_forces_london_dipole_hydrogen_in_organics",
        "subskill_id": "26_intermolecular_forces_london_dipole_hydrogen_in_organics",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_intermolecular_forces_with_intramolecular_covalent_bonds"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify dominant IMF in Compound A", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Identify dominant IMF in Compound B", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Explanation of non-polar vs polar molecular structure", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Energy requirement comparison to separate molecules", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 27. Boiling Point Comparison: Chain Length / Molecular Mass
# ==============================================================================
def builder_27(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_27_bp_chain_len", seed, idx)
    series_choice = rng.choice([
        {"series": "alkanes", "c1": "ethane (C₂H₆)", "bp1": -89, "c2": "propane (C₃H₈)", "bp2": -42, "c3": "butane (C₄H₁₀)", "bp3": -0.5, "c4": "pentane (C₅H₁₂)", "bp4": 36.1},
        {"series": "primary alcohols", "c1": "methanol (CH₃OH)", "bp1": 64.7, "c2": "ethanol (C₂H₅OH)", "bp2": 78.4, "c3": "propan-1-ol (C₃H₇OH)", "bp3": 97.2, "c4": "butan-1-ol (C₄H₉OH)", "bp4": 117.7},
    ])
    p_offset = rng.randint(0, 5)

    prompt = (
        f"The boiling points of four consecutive members of the homologous series of {series_choice['series']} are given below:\n"
        f"• Compound 1: {series_choice['c1']} → Boiling point: {_fmt_sa(series_choice['bp1'])} °C\n"
        f"• Compound 2: {series_choice['c2']} → Boiling point: {_fmt_sa(series_choice['bp2'])} °C\n"
        f"• Compound 3: {series_choice['c3']} → Boiling point: {_fmt_sa(series_choice['bp3'])} °C\n"
        f"• Compound 4: {series_choice['c4']} → Boiling point: {_fmt_sa(series_choice['bp4'])} °C\n\n"
        f"1. State the relationship between carbon chain length and boiling point for this homologous series.\n"
        f"2. Fully explain this trend in terms of molecular size, surface area, intermolecular forces, and energy required."
    )
    ans_str = (
        f"1. As the carbon chain length (molecular mass) increases, the boiling point increases; "
        f"2. Increasing chain length increases molecular size and surface area, leading to more points of contact and larger electron clouds, "
        f"which strengthens intermolecular (London) forces, requiring more thermal energy to overcome."
    )
    memo = (
        "1. As carbon chain length / molecular mass increases, the boiling point increases. [1]\n"
        "2. Explanation:\n"
        "• Longer carbon chains mean larger molecular size / molecular mass / surface area. [1]\n"
        "• Increased surface area provides more points of contact between adjacent molecules (larger electron cloud). [1]\n"
        "• The strength of the intermolecular London forces increases. [1]\n"
        "• More thermal energy is required to overcome the stronger intermolecular forces to separate molecules into the gas phase. [1]"
    )
    hints = {
        "tier_1": "Observe the temperature values: as chain length increases, does boiling point rise or fall?",
        "tier_2": "Relate longer chains to greater surface area and more electron interactions.",
        "tier_3": "Chain length ↑ → Surface area ↑ → London forces strength ↑ → Energy required to overcome IMF ↑ → Boiling point ↑.",
    }
    svg = (
        f'<svg viewBox="0 0 460 190" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="230" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Boiling Point vs Chain Length ({series_choice["series"]})</text>'
        f'<line x1="60" y1="150" x2="420" y2="150" stroke="#64748b" stroke-width="2"/>'
        f'<line x1="60" y1="150" x2="60" y2="40" stroke="#64748b" stroke-width="2"/>'
        f'<circle cx="110" cy="135" r="5" fill="#2563eb"/><text x="110" y="165" text-anchor="middle" font-size="10" fill="#475569">C1</text>'
        f'<circle cx="200" cy="115" r="5" fill="#2563eb"/><text x="200" y="165" text-anchor="middle" font-size="10" fill="#475569">C2</text>'
        f'<circle cx="290" cy="90" r="5" fill="#2563eb"/><text x="290" y="165" text-anchor="middle" font-size="10" fill="#475569">C3</text>'
        f'<circle cx="380" cy="60" r="5" fill="#2563eb"/><text x="380" y="165" text-anchor="middle" font-size="10" fill="#475569">C4</text>'
        f'<path d="M 110 135 Q 240 100 380 60" fill="none" stroke="#2563eb" stroke-dasharray="4,4" stroke-width="2"/>'
        f'<text x="230" y="180" text-anchor="middle" font-size="11" fill="#334155">Offset parameter: {p_offset}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "27_boiling_point_comparison_homologous_series_chain_length",
        "subskill": "27_boiling_point_comparison_homologous_series_chain_length",
        "subskill_id": "27_boiling_point_comparison_homologous_series_chain_length",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["stating_covalent_bonds_break_during_boiling"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct statement of relationship between chain length and BP", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Reference to larger molecular size / surface area", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification of stronger London forces / more points of contact", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "More thermal energy required to overcome intermolecular forces", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 28. Boiling Point Comparison: Branching and Surface Area (Chain Isomers)
# ==============================================================================
def builder_28(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_28_bp_branching", seed, idx)
    systems = [
        {
            "formula": "C₅H₁₂",
            "cmp1": "pentane (straight chain)", "bp1": 36.1, "shape1": "elongated / straight chain",
            "cmp2": "2-methylbutane", "bp2": 27.8, "shape2": "moderately branched",
            "cmp3": "2,2-dimethylpropane", "bp3": 9.5, "shape3": "highly branched / compact spherical",
        },
        {
            "formula": "C₄H₁₀",
            "cmp1": "butane (straight chain)", "bp1": -0.5, "shape1": "straight chain",
            "cmp2": "2-methylpropane", "bp2": -11.7, "shape2": "branched / compact",
            "cmp3": "synthetic control", "bp3": -20.0, "shape3": "hypothetical model",
        },
    ]
    sys = rng.choice(systems)
    diff = _fmt_sa(round(sys["bp1"] - sys["bp2"], 1))

    prompt = (
        f"Consider the structural isomers with molecular formula {sys['formula']} and their measured boiling points:\n"
        f"• Compound X: {sys['cmp1']} → BP = {_fmt_sa(sys['bp1'])} °C\n"
        f"• Compound Y: {sys['cmp2']} → BP = {_fmt_sa(sys['bp2'])} °C\n\n"
        f"1. Name the type of structural isomerism shown by Compound X and Compound Y.\n"
        f"2. Explain why Compound X has a higher boiling point than Compound Y ({diff} °C difference), "
        f"referring to molecular shape, surface area, intermolecular forces, and energy required."
    )
    ans_str = (
        f"1. Chain isomers; 2. Compound X is a straight-chain molecule with a larger surface area and can pack more closely, "
        f"resulting in stronger intermolecular London forces than branched Compound Y, which requires more energy to overcome."
    )
    memo = (
        "1. Chain isomers. [1]\n"
        "2. Explanation:\n"
        "• Compound X has a straight carbon chain, while Compound Y is branched. [1]\n"
        "• Straight chains have a larger surface area and can pack more closely together. [1]\n"
        "• Branching makes molecules more spherical/compact, reducing surface contact area. [1]\n"
        "• Intermolecular London forces are stronger in Compound X than in Compound Y. [1]\n"
        "• More thermal energy is required to overcome the intermolecular forces in Compound X. [1]"
    )
    hints = {
        "tier_1": "Both molecules have identical molecular formula but different carbon chain branching.",
        "tier_2": "Branching makes molecules more spherical, reducing the surface area of contact.",
        "tier_3": "Straight chain → larger surface area → stronger London forces → more energy needed → higher BP.",
    }
    svg = (
        f'<svg viewBox="0 0 440 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="190" height="140" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="115" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">Compound X (Straight)</text>'
        f'<text x="115" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{sys["cmp1"]}</text>'
        f'<text x="115" y="105" text-anchor="middle" font-size="11" fill="#16a34a">BP = {_fmt_sa(sys["bp1"])} °C</text>'
        f'<text x="115" y="135" text-anchor="middle" font-size="10" fill="#475569">Max surface contact</text>'
        f'<rect x="230" y="20" width="190" height="140" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="325" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">Compound Y (Branched)</text>'
        f'<text x="325" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{sys["cmp2"]}</text>'
        f'<text x="325" y="105" text-anchor="middle" font-size="11" fill="#dc2626">BP = {_fmt_sa(sys["bp2"])} °C</text>'
        f'<text x="325" y="135" text-anchor="middle" font-size="10" fill="#475569">Spherical / reduced area</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "28_boiling_point_comparison_branching_surface_area",
        "subskill": "28_boiling_point_comparison_branching_surface_area",
        "subskill_id": "28_boiling_point_comparison_branching_surface_area",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["attributing_boiling_point_difference_to_covalent_bond_strength"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Identify chain isomerism", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Contrast molecular shapes (elongated vs compact spherical)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Compare surface area of contact", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Compare strength of intermolecular London forces", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": "Compare thermal energy required to separate molecules", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 29. Boiling Point Comparison: Functional Group Type (Comparable Molar Mass)
# ==============================================================================
def builder_29(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_29_bp_functional_groups", seed, idx)
    test_set = [
        {"cmpA": "butane", "formulaA": "C₄H₁₀", "massA": 58, "bpA": -0.5, "imfA": "London forces", "groupA": "alkane"},
        {"cmpB": "propanal", "formulaB": "C₃H₆O", "massB": 58, "bpB": 48.0, "imfB": "dipole-dipole forces", "groupB": "aldehyde"},
        {"cmpC": "propan-1-ol", "formulaC": "C₃H₈O", "massC": 60, "bpC": 97.2, "imfC": "hydrogen bonds (1 per molecule)", "groupC": "alcohol"},
        {"cmpD": "ethanoic acid", "formulaD": "C₂H₄O₂", "massD": 60, "bpD": 118.0, "imfD": "strong hydrogen bonds (dimer formation, 2 per dimer)", "groupD": "carboxylic acid"},
    ]
    pair = rng.choice([("propan-1-ol", "ethanoic acid"), ("butane", "propanal"), ("propanal", "propan-1-ol")])
    c1_name = pair[0]
    c2_name = pair[1]
    d1 = next(x for x in test_set if list(x.values())[0] == c1_name)
    d2 = next(x for x in test_set if list(x.values())[0] == c2_name)
    bp1 = list(d1.values())[3]
    bp2 = list(d2.values())[3]
    imf1 = list(d1.values())[4]
    imf2 = list(d2.values())[4]

    prompt = (
        f"The boiling points of two organic compounds with comparable molar masses are provided:\n"
        f"• Compound 1: {c1_name} → Boiling point = {_fmt_sa(bp1)} °C\n"
        f"• Compound 2: {c2_name} → Boiling point = {_fmt_sa(bp2)} °C\n\n"
        f"1. Explain why compounds with comparable molecular masses are chosen when comparing the effect of functional groups.\n"
        f"2. Identify the type of intermolecular force present in each compound.\n"
        f"3. Fully explain the difference in boiling points between {c1_name} and {c2_name}."
    )
    ans_str = (
        f"1. To ensure that London (dispersion) force strength due to molecular mass/electron count remains constant (fair test); "
        f"2. {c1_name}: {imf1}; {c2_name}: {imf2}; "
        f"3. {c2_name} possesses stronger intermolecular forces ({imf2}) than {c1_name} ({imf1}), requiring more thermal energy to overcome."
    )
    memo = (
        "1. To ensure a fair comparison where London forces resulting from electron count and molecular size are kept roughly constant, "
        "so that the difference in boiling point is solely due to functional group polarity. [1]\n"
        f"2. Intermolecular forces:\n• {c1_name}: {imf1} [1]\n• {c2_name}: {imf2} [1]\n"
        f"3. {imf2} in {c2_name} are stronger than {imf1} in {c1_name}. [1]\n"
        f"Consequently, significantly more thermal energy is needed to overcome the intermolecular forces between molecules of {c2_name}. [1]"
    )
    hints = {
        "tier_1": "Comparable molar mass controls for London force strength.",
        "tier_2": "Look at the functional groups: alcohols have 1 site for H-bonding, carboxylic acids form dimers with 2 H-bonds.",
        "tier_3": f"IMF strength order: {imf2} > {imf1}. Stronger IMF requires more energy to separate molecules.",
    }
    svg = (
        f'<svg viewBox="0 0 450 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<rect x="20" y="20" width="195" height="140" rx="8" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>'
        f'<text x="117" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">{c1_name}</text>'
        f'<text x="117" y="75" text-anchor="middle" font-size="11" fill="#2563eb">BP = {_fmt_sa(bp1)} °C</text>'
        f'<text x="117" y="110" text-anchor="middle" font-size="10" fill="#475569">{imf1}</text>'
        f'<rect x="235" y="20" width="195" height="140" rx="8" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="332" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">{c2_name}</text>'
        f'<text x="332" y="75" text-anchor="middle" font-size="11" fill="#dc2626">BP = {_fmt_sa(bp2)} °C</text>'
        f'<text x="332" y="110" text-anchor="middle" font-size="10" fill="#854d0e">{imf2}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "29_boiling_point_comparison_functional_group_type",
        "subskill": "29_boiling_point_comparison_functional_group_type",
        "subskill_id": "29_boiling_point_comparison_functional_group_type",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["ignoring_molar_mass_control_variable"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Explain importance of controlled molecular mass", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Identify IMF in Compound 1", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identify IMF in Compound 2", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Compare relative IMF strengths", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Relate IMF strength to thermal energy required", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 30. Vapour Pressure and Volatility
# ==============================================================================
def builder_30(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_30_vapour_pressure", seed, idx)
    temp_meas = rng.choice([20, 25, 30])
    compounds = [
        {"name": "propan-1-ol", "vp": 2.8, "imf": "hydrogen bonding", "vol": "moderately volatile"},
        {"name": "propan-2-one (acetone)", "vp": 30.6, "imf": "dipole-dipole forces", "vol": "highly volatile"},
        {"name": "propanoic acid", "vp": 0.4, "imf": "strong hydrogen bonding (dimers)", "vol": "least volatile"},
    ]
    rng.shuffle(compounds)
    high_vp_cmp = max(compounds, key=lambda x: x["vp"])
    low_vp_cmp = min(compounds, key=lambda x: x["vp"])

    prompt = (
        f"Vapour pressure measurements for three organic liquids are recorded in a closed system at {temp_meas} °C:\n"
        f"• Liquid A ({compounds[0]['name']}): {_fmt_sa(compounds[0]['vp'])} kPa\n"
        f"• Liquid B ({compounds[1]['name']}): {_fmt_sa(compounds[1]['vp'])} kPa\n"
        f"• Liquid C ({compounds[2]['name']}): {_fmt_sa(compounds[2]['vp'])} kPa\n\n"
        f"1. Define the term 'vapour pressure'.\n"
        f"2. State the relationship between intermolecular force strength and vapour pressure.\n"
        f"3. Identify which liquid has the highest volatility and explain why in terms of intermolecular forces."
    )
    ans_str = (
        f"1. Vapour pressure is the pressure exerted by a vapour in equilibrium with its liquid in a closed system; "
        f"2. As intermolecular force strength increases, vapour pressure decreases (inversely proportional); "
        f"3. {high_vp_cmp['name']} has the highest volatility because it has the highest vapour pressure, "
        f"indicating weakest intermolecular forces allowing more molecules to escape into the gas phase."
    )
    memo = (
        "1. Vapour pressure: The pressure exerted by a vapour at equilibrium with its liquid (or solid) phase in a closed system at a given temperature. [2]\n"
        "2. Vapour pressure is inversely proportional to intermolecular force strength (stronger IMF → lower vapour pressure). [1]\n"
        f"3. {high_vp_cmp['name']} has the highest vapour pressure ({_fmt_sa(high_vp_cmp['vp'])} kPa). "
        f"It has the weakest intermolecular forces among the liquids, so fewer energy barriers prevent surface molecules "
        f"from evaporating into the vapour phase, giving it the highest volatility. [2]"
    )
    hints = {
        "tier_1": "Recall: weak intermolecular forces mean molecules escape easily into the gas phase.",
        "tier_2": "Higher vapour pressure = more molecules in the vapour phase = higher volatility.",
        "tier_3": f"Highest vapour pressure is {high_vp_cmp['name']} ({_fmt_sa(high_vp_cmp['vp'])} kPa).",
    }
    svg = (
        f'<svg viewBox="0 0 450 180" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="225" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Vapour Pressure at {temp_meas} °C (Closed Container)</text>'
        f'<rect x="30" y="45" width="110" height="110" rx="6" fill="#e0f2fe" stroke="#0284c7"/>'
        f'<text x="85" y="75" text-anchor="middle" font-size="10" font-weight="bold">{compounds[0]["name"]}</text>'
        f'<text x="85" y="105" text-anchor="middle" font-size="12" fill="#0369a1">{_fmt_sa(compounds[0]["vp"])} kPa</text>'
        f'<rect x="170" y="45" width="110" height="110" rx="6" fill="#fef9c3" stroke="#ca8a04"/>'
        f'<text x="225" y="75" text-anchor="middle" font-size="10" font-weight="bold">{compounds[1]["name"]}</text>'
        f'<text x="225" y="105" text-anchor="middle" font-size="12" fill="#a16207">{_fmt_sa(compounds[1]["vp"])} kPa</text>'
        f'<rect x="310" y="45" width="110" height="110" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="365" y="75" text-anchor="middle" font-size="10" font-weight="bold">{compounds[2]["name"]}</text>'
        f'<text x="365" y="105" text-anchor="middle" font-size="12" fill="#b91c1c">{_fmt_sa(compounds[2]["vp"])} kPa</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "30_vapour_pressure_inversely_proportional_to_imf_strength",
        "subskill": "30_vapour_pressure_inversely_proportional_to_imf_strength",
        "subskill_id": "30_vapour_pressure_inversely_proportional_to_imf_strength",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["assuming_high_boiling_point_means_high_vapour_pressure"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of vapour pressure (equilibrium in closed system)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Inverse relationship between IMF and vapour pressure", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification of liquid with highest volatility", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Explanation linked to weakest intermolecular forces", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 31. Melting Point Trends and Crystal Packing
# ==============================================================================
def builder_31(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_31_melting_point_packing", seed, idx)
    odd_even = rng.choice([
        {"odd_alkane": "propane (C₃H₈)", "odd_mp": -188, "even_alkane": "butane (C₄H₁₀)", "even_mp": -138},
        {"odd_alkane": "pentane (C₅H₁₂)", "odd_mp": -130, "even_alkane": "hexane (C₆H₁₄)", "even_mp": -95},
    ])
    temp_val = rng.randint(5, 15)

    prompt = (
        f"Melting points of alkanes depend not only on molecular mass but also on crystal lattice packing efficiency.\n"
        f"• {odd_even['odd_alkane']}: Melting point = {_fmt_sa(odd_even['odd_mp'])} °C\n"
        f"• {odd_even['even_alkane']}: Melting point = {_fmt_sa(odd_even['even_mp'])} °C\n\n"
        f"1. Define 'melting point'.\n"
        f"2. Explain why {odd_even['even_alkane']} has a significantly higher melting point than {odd_even['odd_alkane']}, "
        f"referencing both molecular mass and crystal lattice symmetry/packing."
    )
    ans_str = (
        f"1. The temperature at which the solid and liquid phases of a substance are at equilibrium; "
        f"2. {odd_even['even_alkane']} has higher molecular mass (more electrons / stronger London forces) and an even number of carbons "
        f"which packs more efficiently and symmetrically into the crystal lattice."
    )
    memo = (
        "1. Melting point: The temperature at which the solid and liquid phases of a substance are at equilibrium. [2]\n"
        f"2. Explanation:\n"
        f"• {odd_even['even_alkane']} has a larger molecular mass and larger electron cloud than {odd_even['odd_alkane']}, "
        f"resulting in stronger intermolecular London forces. [1]\n"
        f"• Alkanes with an even number of carbon atoms have end methyl groups on opposite sides of the chain, "
        f"allowing closer and more symmetrical packing in the crystal lattice. [1]\n"
        f"• More thermal energy is required to disrupt both the stronger lattice packing and intermolecular forces. [1]"
    )
    hints = {
        "tier_1": "Melting point is the transition temperature between solid and liquid.",
        "tier_2": "Even-numbered carbon chains pack more symmetrically into solid lattices.",
        "tier_3": "Higher mass = stronger London forces. Better packing = more energy needed to melt.",
    }
    svg = (
        f'<svg viewBox="0 0 440 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Melting Point & Lattice Packing</text>'
        f'<rect x="25" y="45" width="185" height="100" rx="6" fill="#e0e7ff" stroke="#4338ca"/>'
        f'<text x="117" y="75" text-anchor="middle" font-size="11" font-weight="bold">{odd_even["odd_alkane"]}</text>'
        f'<text x="117" y="105" text-anchor="middle" font-size="12" fill="#4338ca">MP = {_fmt_sa(odd_even["odd_mp"])} °C</text>'
        f'<text x="117" y="130" text-anchor="middle" font-size="10" fill="#64748b">Odd-C packing</text>'
        f'<rect x="230" y="45" width="185" height="100" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="322" y="75" text-anchor="middle" font-size="11" font-weight="bold">{odd_even["even_alkane"]}</text>'
        f'<text x="322" y="105" text-anchor="middle" font-size="12" fill="#15803d">MP = {_fmt_sa(odd_even["even_mp"])} °C</text>'
        f'<text x="322" y="130" text-anchor="middle" font-size="10" fill="#64748b">Even-C symmetrical packing (seed offset {temp_val})</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "31_melting_point_trends_and_crystal_packing",
        "subskill": "31_melting_point_trends_and_crystal_packing",
        "subskill_id": "31_melting_point_trends_and_crystal_packing",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["neglecting_crystal_lattice_packing_in_melting_points"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of melting point", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Effect of increased molecular mass on London forces", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Effect of symmetrical crystal packing in even-carbon chains", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Energy requirement conclusion", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 32. Viscosity and Flammability Trends in Hydrocarbons
# ==============================================================================
def builder_32(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_32_viscosity_flammability", seed, idx)
    hydrocarbons = [
        {"name": "hexane (C₆H₁₄)", "visc": "low", "flam": "highly flammable (ignites readily)", "flow_time": 4.2},
        {"name": "decane (C₁₀H₂₂)", "visc": "moderate", "flam": "moderately flammable", "flow_time": 12.8},
        {"name": "hexadecane (C₁₆H₃₄)", "visc": "high", "flam": "difficult to ignite (smoky flame)", "flow_time": 48.5},
    ]
    flow_var = rng.randint(1, 3)

    prompt = (
        f"Three liquid hydrocarbons were tested in a laboratory:\n"
        f"• Liquid 1: hexane (C₆H₁₄) — Flow time through viscometer = {_fmt_sa(hydrocarbons[0]['flow_time'] + flow_var)} s\n"
        f"• Liquid 2: decane (C₁₀H₂₂) — Flow time through viscometer = {_fmt_sa(hydrocarbons[1]['flow_time'] + flow_var)} s\n"
        f"• Liquid 3: hexadecane (C₁₆H₃₄) — Flow time through viscometer = {_fmt_sa(hydrocarbons[2]['flow_time'] + flow_var)} s\n\n"
        f"1. Define 'viscosity'.\n"
        f"2. Explain why hexadecane has a higher viscosity (flows much slower) than hexane.\n"
        f"3. Compare the flammability of hexane and hexadecane, and explain why longer hydrocarbons burn with sootier flames."
    )
    ans_str = (
        f"1. Viscosity is the measure of a fluid's resistance to flow; "
        f"2. Hexadecane has longer carbon chains with larger surface areas, causing chain entanglement and stronger intermolecular London forces; "
        f"3. Hexane is more flammable (lower boiling point / more volatile); hexadecane has a higher carbon-to-hydrogen ratio resulting in incomplete combustion (soot/carbon particles)."
    )
    memo = (
        "1. Viscosity: A fluid's resistance to flow / internal friction between moving fluid layers. [1]\n"
        "2. Hexadecane has much longer carbon chains than hexane. Longer chains experience greater molecular entanglement "
        "and stronger intermolecular London forces, offering greater internal resistance to flow. [2]\n"
        "3. Hexane is much more flammable than hexadecane because it vaporises much more readily (higher vapour pressure / lower BP). "
        "Hexadecane has a higher carbon-to-hydrogen ratio, leading to incomplete combustion in air, which produces free unburned carbon (soot). [2]"
    )
    hints = {
        "tier_1": "Viscosity measures how thick or slow-flowing a liquid is.",
        "tier_2": "Longer chains entangle and have stronger London forces.",
        "tier_3": "Shorter chains vaporise easily (flammable); longer chains burn incompletely (sooty).",
    }
    svg = (
        f'<svg viewBox="0 0 440 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Hydrocarbon Viscosity & Flow Rate</text>'
        f'<rect x="30" y="45" width="110" height="100" rx="6" fill="#ecfdf5" stroke="#059669"/>'
        f'<text x="85" y="75" text-anchor="middle" font-size="11" font-weight="bold">Hexane</text>'
        f'<text x="85" y="105" text-anchor="middle" font-size="11" fill="#059669">Fast flow ({_fmt_sa(hydrocarbons[0]["flow_time"] + flow_var)} s)</text>'
        f'<rect x="165" y="45" width="110" height="100" rx="6" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="220" y="75" text-anchor="middle" font-size="11" font-weight="bold">Decane</text>'
        f'<text x="220" y="105" text-anchor="middle" font-size="11" fill="#d97706">Medium ({_fmt_sa(hydrocarbons[1]["flow_time"] + flow_var)} s)</text>'
        f'<rect x="300" y="45" width="110" height="100" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="355" y="75" text-anchor="middle" font-size="11" font-weight="bold">Hexadecane</text>'
        f'<text x="355" y="105" text-anchor="middle" font-size="11" fill="#dc2626">Slow ({_fmt_sa(hydrocarbons[2]["flow_time"] + flow_var)} s)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "32_viscosity_and_flammability_trends_in_hydrocarbons",
        "subskill": "32_viscosity_and_flammability_trends_in_hydrocarbons",
        "subskill_id": "32_viscosity_and_flammability_trends_in_hydrocarbons",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_combustion_soot_with_impurity"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of viscosity", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Chain length and entanglement explanation for viscosity", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Comparison of flammability and volatility", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Carbon-to-hydrogen ratio and incomplete combustion soot", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 33. Solubility in Water (Polar vs Non-Polar Chains)
# ==============================================================================
def builder_33(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_33_solubility_water", seed, idx)
    alcohols = [
        {"name": "ethanol (CH₃CH₂OH)", "sol": "completely miscible in water", "c_len": 2},
        {"name": "butan-1-ol (CH₃(CH₂)₃OH)", "sol": "moderately soluble (approx. 8 g/100 g H₂O)", "c_len": 4},
        {"name": "hexan-1-ol (CH₃(CH₂)₅OH)", "sol": "immiscible / insoluble (approx. 0,6 g/100 g H₂O)", "c_len": 6},
        {"name": "octan-1-ol (CH₃(CH₂)₇OH)", "sol": "virtually insoluble (immiscible)", "c_len": 8},
    ]
    chosen = rng.sample(alcohols, 2)
    chosen.sort(key=lambda x: x["c_len"])
    alc_short, alc_long = chosen[0], chosen[1]

    prompt = (
        f"Water is a polar solvent that forms strong hydrogen bonds.\n"
        f"Consider the solubility of two primary alcohols in water:\n"
        f"• Alcohol 1: {alc_short['name']} → {alc_short['sol']}\n"
        f"• Alcohol 2: {alc_long['name']} → {alc_long['sol']}\n\n"
        f"1. State the principle of solubility ('like dissolves like') as applied here.\n"
        f"2. Explain why {alc_short['name']} dissolves readily in water while {alc_long['name']} is insoluble or immiscible, "
        f"referencing the hydrophilic -OH group versus the hydrophobic hydrocarbon tail."
    )
    ans_str = (
        f"1. Polar substances dissolve in polar solvents, and non-polar substances dissolve in non-polar solvents; "
        f"2. In {alc_short['name']}, the polar hydrophilic -OH group dominates, forming hydrogen bonds with water molecules. "
        f"In {alc_long['name']}, the non-polar hydrophobic hydrocarbon chain is long and disrupts water's hydrogen bond network without sufficient compensation."
    )
    memo = (
        "1. Polar solutes dissolve in polar solvents via dipole-dipole or hydrogen bonding; non-polar solutes dissolve in non-polar solvents ('like dissolves like'). [1]\n"
        "2. Detailed explanation:\n"
        f"• Both alcohols possess a polar, hydrophilic hydroxyl (-OH) group capable of forming hydrogen bonds with water molecules. [1]\n"
        f"• {alc_short['name']} has a short non-polar hydrocarbon chain (C{alc_short['c_len']}), so hydrogen bonding between the -OH group and water dominates. [1]\n"
        f"• {alc_long['name']} has a much longer non-polar hydrophobic hydrocarbon tail (C{alc_long['c_len']}). [1]\n"
        "• The non-polar chain disrupts the hydrogen-bonded network of water molecules without being able to form strong attractions with water, rendering it insoluble. [1]"
    )
    hints = {
        "tier_1": "Alcohols have two parts: a polar -OH group and a non-polar carbon chain.",
        "tier_2": "As the non-polar chain gets longer, the molecule behaves more like a non-polar alkane.",
        "tier_3": "Hydrophilic -OH vs hydrophobic tail. Long tails prevent dissolving in polar water.",
    }
    svg = (
        f'<svg viewBox="0 0 440 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Solubility of Alcohols in Water</text>'
        f'<rect x="25" y="45" width="185" height="105" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="117" y="70" text-anchor="middle" font-size="11" font-weight="bold">{alc_short["name"]}</text>'
        f'<text x="117" y="95" text-anchor="middle" font-size="10" fill="#1e40af">Short C{alc_short["c_len"]} chain</text>'
        f'<text x="117" y="125" text-anchor="middle" font-size="11" fill="#16a34a">Soluble / Miscible</text>'
        f'<rect x="230" y="45" width="185" height="105" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="322" y="70" text-anchor="middle" font-size="11" font-weight="bold">{alc_long["name"]}</text>'
        f'<text x="322" y="95" text-anchor="middle" font-size="10" fill="#991b1b">Long C{alc_long["c_len"]} hydrophobic tail</text>'
        f'<text x="322" y="125" text-anchor="middle" font-size="11" fill="#dc2626">Insoluble / Immiscible</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "33_solubility_in_water_polar_vs_non_polar_chains",
        "subskill": "33_solubility_in_water_polar_vs_non_polar_chains",
        "subskill_id": "33_solubility_in_water_polar_vs_non_polar_chains",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["assuming_all_alcohols_are_freely_soluble_in_water"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of 'like dissolves like' principle", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Identification of polar hydrophilic -OH and hydrogen bonding with water", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification of non-polar hydrophobic hydrocarbon chain", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Contrast effect of short vs long non-polar chain on water's hydrogen bond network", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 34. Combustion Reactions: Complete Oxidation of Alkanes
# ==============================================================================
def builder_34(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_34_combustion_alkanes", seed, idx)
    alkanes = [
        {"name": "propane", "formula": "C₃H₈", "c": 3, "h": 8, "o2_coeff": 5, "co2_coeff": 3, "h2o_coeff": 4, "eq": "C₃H₈ + 5O₂ → 3CO₂ + 4H₂O"},
        {"name": "butane", "formula": "C₄H₁₀", "c": 4, "h": 10, "o2_coeff": 13, "co2_coeff": 8, "h2o_coeff": 10, "eq": "2C₄H₁₀ + 13O₂ → 8CO₂ + 10H₂O"},
        {"name": "pentane", "formula": "C₅H₁₂", "c": 5, "h": 12, "o2_coeff": 8, "co2_coeff": 5, "h2o_coeff": 6, "eq": "C₅H₁₂ + 8O₂ → 5CO₂ + 6H₂O"},
        {"name": "ethane", "formula": "C₂H₆", "c": 2, "h": 6, "o2_coeff": 7, "co2_coeff": 4, "h2o_coeff": 6, "eq": "2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O"},
    ]
    alk = rng.choice(alkanes)
    moles_fuel = rng.choice([2, 3, 4, 5])
    # stoichiometric ratio
    if alk["name"] in ["butane", "ethane"]:
        # 2 moles fuel -> co2 = co2_coeff, o2 = o2_coeff
        moles_o2 = (moles_fuel * alk["o2_coeff"]) / 2.0
        moles_co2 = (moles_fuel * alk["co2_coeff"]) / 2.0
    else:
        moles_o2 = moles_fuel * alk["o2_coeff"]
        moles_co2 = moles_fuel * alk["co2_coeff"]

    prompt = (
        f"Alkanes are widely used as fuels because their combustion reactions are highly exothermic.\n"
        f"Consider the complete combustion of {alk['name']} ({alk['formula']}) in excess oxygen gas:\n\n"
        f"1. Write down a balanced chemical equation for the complete combustion of {alk['name']} using molecular formulae.\n"
        f"2. State the two main products formed during complete combustion of any hydrocarbon.\n"
        f"3. Calculate the number of moles of oxygen gas (O₂) required to completely burn {moles_fuel} moles of {alk['name']}."
    )
    ans_str = (
        f"1. {alk['eq']}; 2. Carbon dioxide (CO₂) and water (H₂O); "
        f"3. {_fmt_sa(moles_o2)} moles of O₂."
    )
    memo = (
        f"1. Balanced equation: {alk['eq']} [3: 1 for reactants, 1 for products, 1 for balancing]\n"
        f"2. Products: Carbon dioxide (CO₂) and water (H₂O). [2]\n"
        f"3. Stoichiometry: From balanced equation, mole ratio of fuel to O₂ is {2 if alk['name'] in ['butane', 'ethane'] else 1} : {alk['o2_coeff']}.\n"
        f"n(O₂) = {moles_fuel} × ({alk['o2_coeff']} / {2 if alk['name'] in ['butane', 'ethane'] else 1}) = {_fmt_sa(moles_o2)} mol. [2]"
    )
    hints = {
        "tier_1": "Complete combustion always produces carbon dioxide and water vapour.",
        "tier_2": "Balance carbon first, then hydrogen, and finally oxygen.",
        "tier_3": f"Equation: {alk['eq']}. Mole ratio gives {_fmt_sa(moles_o2)} mol O₂.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Combustion of {alk["name"].capitalize()}</text>'
        f'<rect x="30" y="45" width="160" height="90" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="110" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">Fuel: {alk["name"]}</text>'
        f'<text x="110" y="105" text-anchor="middle" font-size="11" fill="#475569">{moles_fuel} mol reacting</text>'
        f'<line x1="195" y1="90" x2="245" y2="90" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow)"/>'
        f'<rect x="250" y="45" width="160" height="90" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="330" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">Products</text>'
        f'<text x="330" y="105" text-anchor="middle" font-size="11" fill="#475569">CO₂ + H₂O + Heat</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "34_combustion_reactions_complete_oxidation_alkanes",
        "subskill": "34_combustion_reactions_complete_oxidation_alkanes",
        "subskill_id": "34_combustion_reactions_complete_oxidation_alkanes",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 7, "hints": hints, "misconception_tags": ["unbalanced_oxygen_atoms_in_hydrocarbon_combustion"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct reactants and products in equation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Correct balancing of combustion equation", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification of CO₂ and H₂O as complete combustion products", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Stoichiometric mole ratio and calculation of O₂", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 35. Addition Reactions: Hydrogenation of Alkenes
# ==============================================================================
def builder_35(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_35_hydrogenation", seed, idx)
    cases = [
        {"alkene": "ethene (CH₂=CH₂)", "alkane": "ethane (CH₃CH₃)", "catalyst": "Pt (platinum), Pd (palladium), or Ni (nickel)", "solv": "dissolved in non-polar solvent"},
        {"alkene": "propene (CH₂=CH-CH₃)", "alkane": "propane (CH₃CH₂CH₃)", "catalyst": "Ni (nickel) / Pt / Pd", "solv": "dissolved in non-polar solvent"},
        {"alkene": "but-2-ene (CH₃-CH=CH-CH₃)", "alkane": "butane (CH₃CH₂CH₂CH₃)", "catalyst": "Pt (platinum) or Ni", "solv": "non-polar solvent"},
    ]
    c = rng.choice(cases)
    temp_seed = rng.choice([150, 180, 200])

    prompt = (
        f"The conversion of an alkene to an alkane is an addition reaction known as hydrogenation.\n"
        f"Consider the reaction of {c['alkene']} with excess hydrogen gas (H₂):\n\n"
        f"1. State the two essential reaction conditions (including catalyst) required for this hydrogenation reaction to occur.\n"
        f"2. Write down the IUPAC name of the organic product formed.\n"
        f"3. Name a major industrial application of the hydrogenation of unsaturated vegetable oils in the food industry."
    )
    ans_str = (
        f"1. Catalyst: Pt, Pd, or Ni; Alkene dissolved in a non-polar solvent (or moderate heat); "
        f"2. {c['alkane'].split()[0]}; 3. Manufacture of margarine (hardening of liquid vegetable oils into solid fats)."
    )
    memo = (
        f"1. Reaction conditions: Metal catalyst such as Pt (platinum), Pd (palladium), or Ni (nickel); "
        f"and alkene dissolved in a non-polar solvent (heat required if using Ni, ~{temp_seed} °C). [2]\n"
        f"2. Organic product: {c['alkane'].split()[0]}. [1]\n"
        f"3. Industrial application: Hardening of plant/vegetable oils to manufacture margarine (converting liquid unsaturated fats to solid/semi-solid saturated fats). [2]"
    )
    hints = {
        "tier_1": "Hydrogenation adds H₂ across the carbon-carbon double bond.",
        "tier_2": "The catalyst is a transition metal like Ni, Pt, or Pd.",
        "tier_3": f"Product is {c['alkane'].split()[0]}. Margarine production from vegetable oils.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Hydrogenation Reaction</text>'
        f'<rect x="25" y="45" width="165" height="95" rx="6" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="107" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["alkene"]}</text>'
        f'<text x="107" y="95" text-anchor="middle" font-size="11" fill="#ca8a04">+ H₂(g)</text>'
        f'<text x="107" y="125" text-anchor="middle" font-size="10" fill="#64748b">Unsaturated</text>'
        f'<line x1="195" y1="92" x2="235" y2="92" stroke="#475569" stroke-width="2"/>'
        f'<text x="215" y="80" text-anchor="middle" font-size="9" fill="#dc2626">Pt / Ni</text>'
        f'<rect x="240" y="45" width="165" height="95" rx="6" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>'
        f'<text x="322" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["alkane"]}</text>'
        f'<text x="322" y="95" text-anchor="middle" font-size="11" fill="#15803d">Alkane</text>'
        f'<text x="322" y="125" text-anchor="middle" font-size="10" fill="#64748b">Saturated (T={temp_seed}°C)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 6,
        "mode": "35_addition_reactions_hydrogenation_of_alkenes",
        "subskill": "35_addition_reactions_hydrogenation_of_alkenes",
        "subskill_id": "35_addition_reactions_hydrogenation_of_alkenes",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["forgetting_metal_catalyst_requirement_in_hydrogenation"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Catalyst requirement (Pt, Pd, or Ni)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Reaction medium (non-polar solvent or heat)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "IUPAC name of saturated alkane product", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Margarine manufacture application explained", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 36. Addition Reactions: Halogenation of Alkenes (Bromine Water Test)
# ==============================================================================
def builder_36(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_36_halogenation_bromine", seed, idx)
    cases = [
        {"alkene": "ethene (CH₂=CH₂)", "halogen": "bromine (Br₂)", "prod": "1,2-dibromoethane", "formula": "CH₂BrCH₂Br"},
        {"alkene": "propene (CH₂=CH-CH₃)", "halogen": "chlorine (Cl₂)", "prod": "1,2-dichloropropane", "formula": "CH₂ClCHClCH₃"},
        {"alkene": "but-2-ene (CH₃-CH=CH-CH₃)", "halogen": "bromine (Br₂)", "prod": "2,3-dibromobutane", "formula": "CH₃CHBrCHBrCH₃"},
    ]
    c = rng.choice(cases)
    tube_lbl = rng.choice(["Test tube A", "Test tube B", "Sample tube 1"])

    prompt = (
        f"In a laboratory test for unsaturation, a student adds a few drops of reddish-brown bromine water (Br₂ in water) "
        f"to {tube_lbl} containing {c['alkene']} at room temperature in the absence of sunlight.\n\n"
        f"1. State the observable colour change in {tube_lbl}.\n"
        f"2. Name the type of organic reaction that takes place.\n"
        f"3. Write down the IUPAC name of the organic product formed.\n"
        f"4. State why an alkane (such as ethane) would not decolourise bromine water rapidly under these same conditions."
    )
    ans_str = (
        f"1. Reddish-brown to colourless (rapid decolourisation); 2. Addition (halogenation); "
        f"3. {c['prod']}; 4. Alkanes are saturated and require ultraviolet (UV) light or heat to undergo substitution."
    )
    memo = (
        f"1. Observation: Reddish-brown colour rapidly decolourises (turns clear/colourless). [1]\n"
        f"2. Reaction type: Addition (or Halogenation / Bromination). [1]\n"
        f"3. IUPAC name of product: {c['prod']}. [2]\n"
        f"4. Alkanes contain only strong, unreactive C-C and C-H single bonds (saturated). "
        f"They cannot undergo addition and require UV light / heat to initiate free-radical substitution. [2]"
    )
    hints = {
        "tier_1": "Alkenes react instantly with bromine water without needing UV light.",
        "tier_2": "The double bond opens up to accept two halogen atoms on adjacent carbons.",
        "tier_3": f"Addition of {c['halogen']} to {c['alkene']} yields {c['prod']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Bromine Water Addition Test ({tube_lbl})</text>'
        f'<rect x="30" y="45" width="160" height="105" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="110" y="70" text-anchor="middle" font-size="11" font-weight="bold">Before Reaction</text>'
        f'<circle cx="110" cy="95" r="16" fill="#b91c1c"/>'
        f'<text x="110" y="130" text-anchor="middle" font-size="10" fill="#7f1d1d">Reddish-brown Br₂</text>'
        f'<rect x="250" y="45" width="160" height="105" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="330" y="70" text-anchor="middle" font-size="11" font-weight="bold">After Reaction</text>'
        f'<circle cx="330" cy="95" r="16" fill="#f0fdf4" stroke="#15803d"/>'
        f'<text x="330" y="130" text-anchor="middle" font-size="10" fill="#14532d">Colourless ({c["prod"]})</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "36_addition_reactions_halogenation_of_alkenes",
        "subskill": "36_addition_reactions_halogenation_of_alkenes",
        "subskill_id": "36_addition_reactions_halogenation_of_alkenes",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_addition_with_substitution_in_bromine_test"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Observable colour change from reddish-brown to colourless", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Identification of addition / halogenation reaction", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "IUPAC name of dihaloalkane product", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Explanation of alkane saturation and UV light requirement", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 37. Addition Reactions: Hydrohalogenation and Markovnikov's Rule
# ==============================================================================
def builder_37(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_37_hydrohalogenation_markovnikov", seed, idx)
    cases = [
        {"alkene": "propene (CH₂=CH-CH₃)", "hx": "hydrogen chloride (HCl)", "major": "2-chloropropane", "minor": "1-chloropropane", "h_atom_c": "C1 (which already has 2 hydrogens)"},
        {"alkene": "propene (CH₂=CH-CH₃)", "hx": "hydrogen bromide (HBr)", "major": "2-bromopropane", "minor": "1-bromopropane", "h_atom_c": "C1 (has 2 hydrogens vs C2 which has 1)"},
        {"alkene": "2-methylpropene (CH₂=C(CH₃)₂)", "hx": "hydrogen bromide (HBr)", "major": "2-bromo-2-methylpropane", "minor": "1-bromo-2-methylpropane", "h_atom_c": "C1 (has 2 hydrogens vs C2 which has 0)"},
        {"alkene": "but-1-ene (CH₂=CH-CH₂-CH₃)", "hx": "hydrogen iodide (HI)", "major": "2-iodobutane", "minor": "1-iodobutane", "h_atom_c": "C1 (has 2 hydrogens)"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"An unsymmetrical alkene undergoes an addition reaction with a hydrogen halide in the absence of water (dry conditions):\n"
        f"• Reactants: {c['alkene']} + {c['hx']}\n\n"
        f"1. State the reaction condition required for this hydrohalogenation reaction.\n"
        f"2. State Markovnikov's rule in your own words.\n"
        f"3. Give the IUPAC name of the MAJOR organic product formed.\n"
        f"4. Give the IUPAC name of the MINOR organic product formed."
    )
    ans_str = (
        f"1. No water present (dry / anhydrous conditions); "
        f"2. When a hydrogen halide adds to an unsymmetrical alkene, the hydrogen atom bonds to the carbon atom with the greater number of hydrogen atoms; "
        f"3. Major product: {c['major']}; 4. Minor product: {c['minor']}."
    )
    memo = (
        "1. Reaction condition: No water / anhydrous / dry hydrogen halide. (Presence of water would yield an alcohol via hydration). [1]\n"
        "2. Markovnikov's rule: In the addition of HX to an unsymmetrical alkene, the hydrogen atom adds to the double-bonded carbon "
        "that already has the greater number of hydrogen atoms directly attached to it (forming the more stable carbocation intermediate). [2]\n"
        f"3. Major product: {c['major']}. [2]\n"
        f"4. Minor product: {c['minor']}. [1]"
    )
    hints = {
        "tier_1": "Recall: 'the rich get richer' — H adds to the carbon with more hydrogens.",
        "tier_2": "In propene, C1 has 2 hydrogens, C2 has 1 hydrogen.",
        "tier_3": f"Major product puts halogen on C2: {c['major']}. Minor is {c['minor']}.",
    }
    svg = (
        f'<svg viewBox="0 0 450 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="225" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Hydrohalogenation (Markovnikov Rule)</text>'
        f'<rect x="25" y="45" width="185" height="105" rx="6" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="117" y="70" text-anchor="middle" font-size="11" font-weight="bold">Reactants</text>'
        f'<text x="117" y="95" text-anchor="middle" font-size="11">{c["alkene"]}</text>'
        f'<text x="117" y="125" text-anchor="middle" font-size="10" fill="#b45309">+ {c["hx"]} (Dry)</text>'
        f'<rect x="235" y="45" width="190" height="105" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="330" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">Major Product (Markovnikov)</text>'
        f'<text x="330" y="95" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{c["major"]}</text>'
        f'<text x="330" y="125" text-anchor="middle" font-size="10" fill="#475569">Minor: {c["minor"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "37_addition_reactions_hydrohalogenation_markovnikov_rule",
        "subskill": "37_addition_reactions_hydrohalogenation_markovnikov_rule",
        "subskill_id": "37_addition_reactions_hydrohalogenation_markovnikov_rule",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["inverting_markovnikov_regiochemistry"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Reaction condition (dry/no water)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Statement of Markovnikov's rule", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "IUPAC name of major haloalkane product", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "IUPAC name of minor haloalkane product", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 38. Addition Reactions: Hydration of Alkenes to Alcohols
# ==============================================================================
def builder_38(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_38_hydration_alkenes", seed, idx)
    cases = [
        {"alkene": "ethene (CH₂=CH₂)", "major_alc": "ethanol", "minor_alc": "none (symmetrical)", "cat": "H₃PO₄ (phosphoric acid) or H₂SO₄"},
        {"alkene": "propene (CH₂=CH-CH₃)", "major_alc": "propan-2-ol", "minor_alc": "propan-1-ol", "cat": "concentrated H₂SO₄ / H₃PO₄ with excess steam (H₂O)"},
        {"alkene": "but-1-ene (CH₂=CH-CH₂-CH₃)", "major_alc": "butan-2-ol", "minor_alc": "butan-1-ol", "cat": "concentrated H₂SO₄ / H₃PO₄ with steam"},
        {"alkene": "2-methylpropene (CH₂=C(CH₃)₂)", "major_alc": "2-methylpropan-2-ol", "minor_alc": "2-methylpropan-1-ol", "cat": "acid catalyst (H₃PO₄ / H₂SO₄)"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"The industrial preparation of alcohols involves the acid-catalysed addition of steam (water) to alkenes (hydration):\n"
        f"• Alkene: {c['alkene']}\n\n"
        f"1. State the two essential reaction conditions required for this hydration reaction.\n"
        f"2. Write down the IUPAC name of the MAJOR alcohol formed.\n"
        f"3. Classify the major alcohol product as primary (1°), secondary (2°), or tertiary (3°)."
    )
    ans_str = (
        f"1. Excess water/steam (H₂O) and strong acid catalyst (H₃PO₄ or H₂SO₄); "
        f"2. Major product: {c['major_alc']}; "
        f"3. {'primary' if 'ethanol' in c['major_alc'] else ('tertiary' if '2-methylpropan-2-ol' in c['major_alc'] else 'secondary')}."
    )
    class_str = 'primary (1°)' if 'ethanol' in c['major_alc'] else ('tertiary (3°)' if '2-methylpropan-2-ol' in c['major_alc'] else 'secondary (2°)')
    memo = (
        f"1. Reaction conditions: Excess water (steam / H₂O) and an acid catalyst (concentrated H₃PO₄ or H₂SO₄) with heat. [2]\n"
        f"2. Major product: {c['major_alc']}. (By Markovnikov's rule, -OH bonds to the more substituted carbon atom). [2]\n"
        f"3. Classification: {class_str}. The carbon atom bonded to the -OH group is bonded to {'1 carbon' if 'primary' in class_str else ('3 carbons' if 'tertiary' in class_str else '2 other carbons')}. [1]"
    )
    hints = {
        "tier_1": "Hydration adds H and OH across the double bond.",
        "tier_2": "Acid catalyst (H₃PO₄ or H₂SO₄) and steam are required.",
        "tier_3": f"Major product: {c['major_alc']} ({class_str}).",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Hydration of Alkenes to Alcohols</text>'
        f'<rect x="25" y="45" width="170" height="95" rx="6" fill="#fef9c3" stroke="#ca8a04"/>'
        f'<text x="110" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["alkene"]}</text>'
        f'<text x="110" y="95" text-anchor="middle" font-size="10" fill="#ca8a04">+ H₂O(g) [steam]</text>'
        f'<line x1="200" y1="92" x2="235" y2="92" stroke="#475569" stroke-width="2"/>'
        f'<text x="217" y="82" text-anchor="middle" font-size="8" fill="#dc2626">H₃PO₄ / H₂SO₄</text>'
        f'<rect x="240" y="45" width="175" height="95" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="327" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["major_alc"]}</text>'
        f'<text x="327" y="95" text-anchor="middle" font-size="10" fill="#1e40af">Major: {class_str}</text>'
        f'<text x="327" y="125" text-anchor="middle" font-size="9" fill="#64748b">Minor: {c["minor_alc"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "38_addition_reactions_hydration_of_alkenes_to_alcohols",
        "subskill": "38_addition_reactions_hydration_of_alkenes_to_alcohols",
        "subskill_id": "38_addition_reactions_hydration_of_alkenes_to_alcohols",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["omitting_acid_catalyst_in_hydration"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Reaction conditions: steam and strong acid catalyst", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name of major alcohol product", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Classification of alcohol (primary/secondary/tertiary)", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 39. Elimination Reactions: Dehydrohalogenation and Zaitsev's Rule
# ==============================================================================
def builder_39(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_39_dehydrohalogenation_zaitsev", seed, idx)
    cases = [
        {"haloalkane": "2-bromobutane (CH₃-CHBr-CH₂-CH₃)", "base": "concentrated KOH in ethanol", "major": "but-2-ene", "minor": "but-1-ene", "byprod": "KBr + H₂O"},
        {"haloalkane": "2-chlorobutane (CH₃-CHCl-CH₂-CH₃)", "base": "concentrated NaOH in ethanol", "major": "but-2-ene", "minor": "but-1-ene", "byprod": "NaCl + H₂O"},
        {"haloalkane": "2-bromo-2-methylbutane (CH₃-CBr(CH₃)-CH₂-CH₃)", "base": "concentrated KOH in ethanol", "major": "2-methylbut-2-ene", "minor": "2-methylbut-1-ene", "byprod": "KBr + H₂O"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"A haloalkane is heated under reflux with a concentrated strong base in ethanol:\n"
        f"• Reactants: {c['haloalkane']} + {c['base']} + strong heat\n\n"
        f"1. Name the type of organic reaction occurring (specific elimination).\n"
        f"2. State the essential reaction conditions required for elimination rather than substitution.\n"
        f"3. State Zaitsev's rule in your own words.\n"
        f"4. Give the IUPAC name of the MAJOR alkene product formed."
    )
    ans_str = (
        f"1. Dehydrohalogenation (elimination); "
        f"2. Concentrated strong base (KOH/NaOH) dissolved in pure ethanol, heated strongly under reflux; "
        f"3. In elimination of HX, hydrogen is removed from the carbon atom with fewer hydrogen atoms (yielding the more substituted alkene); "
        f"4. Major product: {c['major']}."
    )
    memo = (
        "1. Reaction type: Elimination / Dehydrohalogenation. [1]\n"
        "2. Reaction conditions: Concentrated strong base (NaOH or KOH) in ethanol solvent (ethanolic base), strong heat under reflux, absence of water. [2]\n"
        "3. Zaitsev's rule: During elimination, the hydrogen atom is preferentially removed from the β-carbon atom "
        "bonded to fewer hydrogen atoms, producing the more highly substituted (more stable) alkene as the major product. [2]\n"
        f"4. Major product: {c['major']}. [1]"
    )
    hints = {
        "tier_1": "Elimination removes H and halogen to form a double bond.",
        "tier_2": "Concentrated ethanolic base + high heat favours elimination over substitution.",
        "tier_3": f"Zaitsev's rule produces the more substituted alkene: {c['major']}.",
    }
    svg = (
        f'<svg viewBox="0 0 450 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="225" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Dehydrohalogenation (Zaitsev Elimination)</text>'
        f'<rect x="25" y="45" width="185" height="105" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="117" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["haloalkane"]}</text>'
        f'<text x="117" y="95" text-anchor="middle" font-size="10" fill="#dc2626">+ conc. ethanolic base + Δ</text>'
        f'<rect x="235" y="45" width="190" height="105" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="330" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">Major Product: {c["major"]}</text>'
        f'<text x="330" y="95" text-anchor="middle" font-size="10" fill="#475569">Minor Product: {c["minor"]}</text>'
        f'<text x="330" y="125" text-anchor="middle" font-size="9" fill="#15803d">Byproducts: {c["byprod"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "39_elimination_reactions_dehydrohalogenation_zaitsev_rule",
        "subskill": "39_elimination_reactions_dehydrohalogenation_zaitsev_rule",
        "subskill_id": "39_elimination_reactions_dehydrohalogenation_zaitsev_rule",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_conditions_for_elimination_with_dilute_aqueous_substitution"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Reaction type (dehydrohalogenation / elimination)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Reaction conditions (conc. base in ethanol, heat under reflux)", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Statement of Zaitsev's rule", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "IUPAC name of major alkene product", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 40. Elimination Reactions: Dehydration of Alcohols
# ==============================================================================
def builder_40(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_40_dehydration_alcohols", seed, idx)
    cases = [
        {"alcohol": "ethanol (CH₃CH₂OH)", "major": "ethene", "minor": "none", "cat": "concentrated H₂SO₄ at 170 °C (or Al₂O₃ at 350 °C)"},
        {"alcohol": "butan-2-ol (CH₃-CH(OH)-CH₂-CH₃)", "major": "but-2-ene", "minor": "but-1-ene", "cat": "excess concentrated H₂SO₄ or H₃PO₄ with heat"},
        {"alcohol": "propan-1-ol (CH₃CH₂CH₂OH)", "major": "propene", "minor": "none", "cat": "concentrated H₂SO₄ and heat"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"An alcohol undergoes an acid-catalysed elimination reaction known as dehydration:\n"
        f"• Reactant: {c['alcohol']}\n\n"
        f"1. Name the inorganic catalyst and reaction condition required for this dehydration reaction.\n"
        f"2. Write down the IUPAC name of the MAJOR alkene produced.\n"
        f"3. State the inorganic byproduct formed during the reaction."
    )
    ans_str = (
        f"1. Concentrated sulfuric acid (H₂SO₄) or phosphoric acid (H₃PO₄) and excess heat (170 °C); "
        f"2. Major product: {c['major']}; 3. Water (H₂O)."
    )
    memo = (
        f"1. Catalyst & conditions: Concentrated sulfuric acid (H₂SO₄) or concentrated phosphoric acid (H₃PO₄) as dehydrating agent, and high heat (~170 °C). [2]\n"
        f"2. Major product: {c['major']}. (Follows Zaitsev's rule if unsymmetrical). [2]\n"
        f"3. Byproduct: Water (H₂O). [1]"
    )
    hints = {
        "tier_1": "Dehydration removes water (H₂O) from the alcohol molecule.",
        "tier_2": "Concentrated H₂SO₄ acts as a dehydrating agent at elevated temperature.",
        "tier_3": f"Product: {c['major']} + H₂O.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Dehydration of Alcohols</text>'
        f'<rect x="25" y="45" width="165" height="95" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="107" y="75" text-anchor="middle" font-size="11" font-weight="bold">{c["alcohol"]}</text>'
        f'<text x="107" y="105" text-anchor="middle" font-size="10" fill="#1e40af">Alcohol precursor</text>'
        f'<line x1="195" y1="92" x2="240" y2="92" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="217" y="80" text-anchor="middle" font-size="9" fill="#dc2626">conc. H₂SO₄, Δ</text>'
        f'<rect x="245" y="45" width="170" height="95" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="330" y="75" text-anchor="middle" font-size="11" font-weight="bold">{c["major"]}</text>'
        f'<text x="330" y="105" text-anchor="middle" font-size="10" fill="#15803d">+ H₂O byproduct</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 6,
        "mode": "40_elimination_reactions_dehydration_of_alcohols",
        "subskill": "40_elimination_reactions_dehydration_of_alcohols",
        "subskill_id": "40_elimination_reactions_dehydration_of_alcohols",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["forgetting_acid_catalyst_acts_as_dehydrating_agent"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Catalyst (conc. H₂SO₄ or H₃PO₄) and high heat", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name of major alkene product", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Inorganic byproduct identified as water", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 41. Elimination Reactions: Thermal and Catalytic Cracking of Alkanes
# ==============================================================================
def builder_41(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_41_cracking", seed, idx)
    cases = [
        {"feedstock": "decane (C₁₀H₂₂)", "c_feed": 10, "h_feed": 22, "c_alkane": 8, "h_alkane": 18, "alkane_prod": "octane (C₈H₁₈)", "alkene_prod": "ethene (C₂H₄)", "c_alkene": 2, "h_alkene": 4},
        {"feedstock": "dodecane (C₁₂H₂₆)", "c_feed": 12, "h_feed": 26, "c_alkane": 9, "h_alkane": 20, "alkane_prod": "nonane (C₉H₂₀)", "alkene_prod": "propene (C₃H₆)", "c_alkene": 3, "h_alkene": 6},
        {"feedstock": "hexane (C₆H₁₄)", "c_feed": 6, "h_feed": 14, "c_alkane": 4, "h_alkane": 10, "alkane_prod": "butane (C₄H₁₀)", "alkene_prod": "ethene (C₂H₄)", "c_alkene": 2, "h_alkene": 4},
    ]
    c = rng.choice(cases)

    prompt = (
        f"In petroleum refining, cracking is used to break down long-chain alkane molecules into shorter, more useful hydrocarbons:\n"
        f"Reaction: {c['feedstock']} → {c['alkane_prod']} + Compound P\n\n"
        f"1. Define 'cracking'.\n"
        f"2. Distinguish between thermal cracking and catalytic cracking in terms of reaction conditions.\n"
        f"3. Deduce the molecular formula and IUPAC name of Compound P.\n"
        f"4. State the homologous series to which Compound P belongs."
    )
    ans_str = (
        f"1. The chemical process in which longer-chain hydrocarbon molecules are broken down into smaller, more useful molecules; "
        f"2. Thermal cracking uses high temperature and high pressure without catalyst; catalytic cracking uses lower temperature and pressure in the presence of a zeolite/silica-alumina catalyst; "
        f"3. Molecular formula: C{c['c_alkene']}H{c['h_alkene']}, IUPAC name: {c['alkene_prod'].split()[0]}; "
        f"4. Alkenes."
    )
    memo = (
        "1. Cracking: The chemical process of breaking down long-chain hydrocarbon molecules into shorter, more useful alkanes and alkenes. [2]\n"
        "2. Conditions difference: Thermal cracking requires high temperature (~800 °C) and high pressure; "
        "catalytic cracking operates at lower temperatures (~500 °C) and lower pressures in the presence of a catalyst (zeolite / aluminosilicate). [2]\n"
        f"3. By conservation of atoms: C{c['c_feed']}H{c['h_feed']} - C{c['c_alkane']}H{c['h_alkane']} = C{c['c_alkene']}H{c['h_alkene']}. "
        f"IUPAC name: {c['alkene_prod'].split()[0]}. [2]\n"
        "4. Homologous series: Alkenes (contains a C=C double bond). [1]"
    )
    hints = {
        "tier_1": "Cracking breaks long hydrocarbons into a shorter alkane and an alkene.",
        "tier_2": "Subtract the atoms in the alkane product from the feedstock formula.",
        "tier_3": f"Feedstock C{c['c_feed']}H{c['h_feed']} gives {c['alkane_prod']} + {c['alkene_prod']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Catalytic Cracking Process</text>'
        f'<rect x="25" y="45" width="160" height="95" rx="6" fill="#f1f5f9" stroke="#64748b"/>'
        f'<text x="105" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["feedstock"]}</text>'
        f'<text x="105" y="95" text-anchor="middle" font-size="10" fill="#475569">Long-chain alkane</text>'
        f'<line x1="190" y1="92" x2="235" y2="92" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="212" y="80" text-anchor="middle" font-size="8" fill="#2563eb">Zeolite, Δ</text>'
        f'<rect x="240" y="45" width="175" height="95" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="327" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["alkane_prod"]}</text>'
        f'<text x="327" y="95" text-anchor="middle" font-size="10" fill="#15803d">+ Compound P: {c["alkene_prod"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "41_elimination_reactions_thermal_and_catalytic_cracking",
        "subskill": "41_elimination_reactions_thermal_and_catalytic_cracking",
        "subskill_id": "41_elimination_reactions_thermal_and_catalytic_cracking",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 7, "hints": hints, "misconception_tags": ["forgetting_cracking_produces_both_alkanes_and_alkenes"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of cracking", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Distinction between thermal and catalytic cracking conditions", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Molecular formula and IUPAC name of alkene product", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Identification of homologous series as alkenes", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 42. Substitution Reactions: Halogenation of Alkanes (UV Light)
# ==============================================================================
def builder_42(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_42_halogenation_alkanes_uv", seed, idx)
    cases = [
        {"alkane": "methane (CH₄)", "halogen": "chlorine (Cl₂)", "mono": "chloromethane", "byprod": "hydrogen chloride (HCl)", "eq": "CH₄ + Cl₂ → CH₃Cl + HCl"},
        {"alkane": "ethane (CH₃CH₃)", "halogen": "bromine (Br₂)", "mono": "bromoethane", "byprod": "hydrogen bromide (HBr)", "eq": "C₂H₆ + Br₂ → C₂H₅Br + HBr"},
        {"alkane": "propane (CH₃CH₂CH₃)", "halogen": "chlorine (Cl₂)", "mono": "2-chloropropane (and 1-chloropropane)", "byprod": "hydrogen chloride (HCl)", "eq": "C₃H₈ + Cl₂ → C₃H₇Cl + HCl"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"Alkanes are relatively unreactive but undergo substitution reactions with halogens under specific energetic conditions:\n"
        f"• Reactants: {c['alkane']} + {c['halogen']}\n\n"
        f"1. State the essential reaction condition (energy source) required for this substitution reaction to occur.\n"
        f"2. Write down the IUPAC name of the primary mono-substituted haloalkane formed.\n"
        f"3. Name the inorganic byproduct formed.\n"
        f"4. State why this reaction cannot take place in the dark at room temperature."
    )
    ans_str = (
        f"1. Ultraviolet (UV) light or sunlight (or high temperature heat); "
        f"2. {c['mono']}; 3. {c['byprod']}; "
        f"4. Alkanes are unreactive and UV light provides the high activation energy needed to break the halogen-halogen covalent bond (homolytic fission)."
    )
    memo = (
        "1. Reaction condition: Ultraviolet (UV) light / sunlight / heat. [1]\n"
        f"2. Mono-substituted haloalkane: {c['mono']}. [2]\n"
        f"3. Inorganic byproduct: {c['byprod']}. [1]\n"
        "4. Alkanes are saturated and have strong covalent bonds with no high-density electron regions. "
        "UV light is needed to provide the activation energy to homolytically cleave the covalent halogen-halogen bond into free radicals. [2]"
    )
    hints = {
        "tier_1": "Alkanes need UV light or heat to react with halogens.",
        "tier_2": "One halogen atom replaces a hydrogen atom, and the other halogen forms HX.",
        "tier_3": f"Product: {c['mono']} + {c['byprod']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Halogenation of Alkanes (Free Radical Substitution)</text>'
        f'<rect x="25" y="45" width="165" height="95" rx="6" fill="#fef3c7" stroke="#d97706"/>'
        f'<text x="107" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["alkane"]}</text>'
        f'<text x="107" y="95" text-anchor="middle" font-size="11" fill="#d97706">+ {c["halogen"]}</text>'
        f'<line x1="195" y1="92" x2="235" y2="92" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="215" y="80" text-anchor="middle" font-size="9" fill="#dc2626">UV light / hν</text>'
        f'<rect x="240" y="45" width="170" height="95" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="325" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["mono"]}</text>'
        f'<text x="325" y="95" text-anchor="middle" font-size="10" fill="#15803d">+ {c["byprod"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "42_substitution_reactions_halogenation_of_alkanes_uv_light",
        "subskill": "42_substitution_reactions_halogenation_of_alkanes_uv_light",
        "subskill_id": "42_substitution_reactions_halogenation_of_alkanes_uv_light",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["forgetting_uv_light_requirement_for_alkane_halogenation"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "UV light / sunlight / heat condition", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name of mono-haloalkane product", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Inorganic byproduct identified (HX)", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Explanation of activation energy and bond cleavage", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 43. Substitution Reactions: Hydrolysis of Haloalkanes to Alcohols
# ==============================================================================
def builder_43(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_43_hydrolysis_haloalkanes", seed, idx)
    cases = [
        {"haloalkane": "bromoethane (CH₃CH₂Br)", "alcohol": "ethanol", "base": "dilute aqueous NaOH", "byprod": "NaBr"},
        {"haloalkane": "1-chloropropane (CH₃CH₂CH₂Cl)", "alcohol": "propan-1-ol", "base": "dilute aqueous KOH", "byprod": "KCl"},
        {"haloalkane": "2-bromobutane (CH₃CHBrCH₂CH₃)", "alcohol": "butan-2-ol", "base": "dilute aqueous NaOH", "byprod": "NaBr"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"A haloalkane is converted into an alcohol via a nucleophilic substitution reaction known as hydrolysis:\n"
        f"• Reactant: {c['haloalkane']} + {c['base']}\n\n"
        f"1. State the two specific reaction conditions required to favour substitution (hydrolysis) over elimination.\n"
        f"2. Write down the IUPAC name of the alcohol product formed.\n"
        f"3. Name the type of organic reaction occurring (hydrolysis / substitution)."
    )
    ans_str = (
        f"1. Dilute strong base dissolved in water (aqueous solution) and moderate / gentle heating under reflux; "
        f"2. {c['alcohol']}; 3. Substitution (hydrolysis)."
    )
    memo = (
        "1. Reaction conditions: Dilute strong base (aqueous NaOH or KOH / water present) and mild heat / gentle heating under reflux. "
        "(In contrast, concentrated base in ethanol with strong heat causes elimination). [2]\n"
        f"2. IUPAC name of alcohol: {c['alcohol']}. [2]\n"
        "3. Reaction type: Substitution / Hydrolysis. [1]"
    )
    hints = {
        "tier_1": "Hydrolysis replaces the halogen atom with a hydroxyl (-OH) group.",
        "tier_2": "Dilute aqueous base favours substitution; concentrated ethanolic base favours elimination.",
        "tier_3": f"Product: {c['alcohol']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Hydrolysis of Haloalkanes to Alcohols</text>'
        f'<rect x="25" y="45" width="165" height="95" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="107" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["haloalkane"]}</text>'
        f'<text x="107" y="95" text-anchor="middle" font-size="10" fill="#dc2626">+ {c["base"]}</text>'
        f'<line x1="195" y1="92" x2="235" y2="92" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="215" y="80" text-anchor="middle" font-size="9" fill="#2563eb">Warm gently</text>'
        f'<rect x="240" y="45" width="170" height="95" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="325" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["alcohol"]}</text>'
        f'<text x="325" y="95" text-anchor="middle" font-size="10" fill="#1e40af">+ {c["byprod"]} (aq)</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 6,
        "mode": "43_substitution_reactions_hydrolysis_of_haloalkanes_to_alcohols",
        "subskill": "43_substitution_reactions_hydrolysis_of_haloalkanes_to_alcohols",
        "subskill_id": "43_substitution_reactions_hydrolysis_of_haloalkanes_to_alcohols",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["confusing_dilute_aqueous_base_with_concentrated_ethanolic_base"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Reaction conditions: dilute base in water and mild heat", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name of alcohol product", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Classification as substitution / hydrolysis", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 44. Substitution Reactions: Alcohols to Haloalkanes with HX
# ==============================================================================
def builder_44(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_44_alcohol_to_haloalkane", seed, idx)
    cases = [
        {"alcohol": "2-methylpropan-2-ol (tertiary)", "hx": "concentrated HCl", "prod": "2-chloro-2-methylpropane", "cond": "room temperature (rapid reaction without heat)"},
        {"alcohol": "ethanol (primary)", "hx": "concentrated HBr / NaBr with concentrated H₂SO₄", "prod": "bromoethane", "cond": "heating under reflux"},
        {"alcohol": "butan-2-ol (secondary)", "hx": "concentrated HCl with ZnCl₂ catalyst", "prod": "2-chlorobutane", "cond": "gentle heat"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"Alcohols react with hydrogen halides to produce haloalkanes via a substitution reaction:\n"
        f"• Reactants: {c['alcohol']} + {c['hx']}\n\n"
        f"1. State the type of organic reaction occurring.\n"
        f"2. Write down the IUPAC name of the haloalkane formed.\n"
        f"3. Explain why tertiary alcohols react rapidly at room temperature with concentrated HCl, "
        f"whereas primary alcohols require prolonged heating."
    )
    ans_str = (
        f"1. Substitution; 2. {c['prod']}; "
        f"3. Tertiary alcohols react via an SN1 pathway forming a highly stable tertiary carbocation intermediate, which has a very low activation energy."
    )
    memo = (
        "1. Reaction type: Substitution. [1]\n"
        f"2. IUPAC name of product: {c['prod']}. [2]\n"
        "3. Explanation: Tertiary alcohols lose water easily to form a relatively stable tertiary carbocation intermediate (3 alkyl electron-donating groups), "
        "lowering the activation energy so the reaction proceeds readily at room temperature. Primary carbocations are unstable, so primary alcohols require heat. [2]"
    )
    hints = {
        "tier_1": "The -OH group is replaced by the halogen atom.",
        "tier_2": "Tertiary carbocations are much more stable than primary carbocations.",
        "tier_3": f"Product: {c['prod']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Alcohol to Haloalkane Substitution</text>'
        f'<rect x="25" y="45" width="165" height="95" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="107" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["alcohol"]}</text>'
        f'<text x="107" y="95" text-anchor="middle" font-size="10" fill="#2563eb">+ {c["hx"]}</text>'
        f'<line x1="195" y1="92" x2="235" y2="92" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="215" y="80" text-anchor="middle" font-size="9" fill="#dc2626">{c["cond"][:12]}</text>'
        f'<rect x="240" y="45" width="170" height="95" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="325" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["prod"]}</text>'
        f'<text x="325" y="95" text-anchor="middle" font-size="10" fill="#dc2626">+ H₂O</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "44_substitution_reactions_alcohols_to_haloalkanes_with_hx",
        "subskill": "44_substitution_reactions_alcohols_to_haloalkanes_with_hx",
        "subskill_id": "44_substitution_reactions_alcohols_to_haloalkanes_with_hx",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["assuming_primary_alcohols_react_faster_than_tertiary_with_hx"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Reaction type identified as substitution", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name of haloalkane product", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Explanation of carbocation stability in tertiary vs primary alcohols", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 45. Esterification: Condensation Mechanism and Conditions
# ==============================================================================
def builder_45(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_45_esterification_mech", seed, idx)
    cases = [
        {"acid": "ethanoic acid (CH₃COOH)", "alcohol": "ethanol (CH₃CH₂OH)", "ester": "ethyl ethanoate", "formula": "CH₃COOCH₂CH₃", "smell": "sweet pear drops / nail polish remover"},
        {"acid": "propanoic acid (CH₃CH₂COOH)", "alcohol": "methanol (CH₃OH)", "ester": "methyl propanoate", "formula": "CH₃CH₂COOCH₃", "smell": "fruity / rum"},
        {"acid": "butanoic acid (CH₃CH₂CH₂COOH)", "alcohol": "ethanol (CH₃CH₂OH)", "ester": "ethyl butanoate", "formula": "CH₃CH₂CH₂COOCH₂CH₃", "smell": "pineapple"},
        {"acid": "methanoic acid (HCOOH)", "alcohol": "propan-1-ol (CH₃CH₂CH₂OH)", "ester": "propyl methanoate", "formula": "HCOOCH₂CH₂CH₃", "smell": "raspberry"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"An ester is prepared by reacting a carboxylic acid with an alcohol in the presence of an acid catalyst:\n"
        f"• Reactants: {c['acid']} + {c['alcohol']}\n\n"
        f"1. Name the type of organic reaction (esterification / condensation).\n"
        f"2. Name the catalyst used and state its dual function in this reaction.\n"
        f"3. State why the reaction mixture is heated in a water bath rather than directly over an open Bunsen burner flame.\n"
        f"4. Write down the IUPAC name and condensed structural formula of the ester formed."
    )
    ans_str = (
        f"1. Esterification (condensation); "
        f"2. Concentrated sulfuric acid (H₂SO₄): acts as an acid catalyst to increase reaction rate and as a dehydrating agent to absorb water (shifting equilibrium forward); "
        f"3. Alcohols and esters are highly flammable and heat must be distributed safely without risk of fire; "
        f"4. {c['ester']}, {c['formula']}."
    )
    memo = (
        "1. Reaction type: Esterification / Condensation reaction. [1]\n"
        "2. Catalyst and function: Concentrated sulfuric acid (H₂SO₄). "
        "Dual function: (a) Catalyst to lower activation energy/speed up reaction, (b) Dehydrating agent to absorb water byproduct, "
        "shifting the equilibrium position to the right (Le Chatelier's principle) to maximise ester yield. [2]\n"
        "3. Safety: Alcohols and organic esters are highly flammable; a water bath prevents vapour ignition from an open flame. [1]\n"
        f"4. IUPAC name: {c['ester']}; Condensed formula: {c['formula']}. [2]"
    )
    hints = {
        "tier_1": "Alcohol provides the alkyl prefix; carboxylic acid provides the -oate ending.",
        "tier_2": "Concentrated H₂SO₄ catalyzes the reaction and removes water.",
        "tier_3": f"Ester: {c['ester']} ({c['formula']}). Flammable reactants require water bath heating.",
    }
    svg = (
        f'<svg viewBox="0 0 450 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="225" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Esterification Apparatus & Reaction</text>'
        f'<rect x="25" y="45" width="185" height="105" rx="6" fill="#fef08a" stroke="#ca8a04"/>'
        f'<text x="117" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["acid"].split()[0]}</text>'
        f'<text x="117" y="95" text-anchor="middle" font-size="11">+ {c["alcohol"].split()[0]}</text>'
        f'<text x="117" y="125" text-anchor="middle" font-size="10" fill="#854d0e">Water bath heating</text>'
        f'<line x1="215" y1="92" x2="245" y2="92" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="230" y="80" text-anchor="middle" font-size="8" fill="#dc2626">conc. H₂SO₄</text>'
        f'<rect x="250" y="45" width="175" height="105" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="337" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">{c["ester"]}</text>'
        f'<text x="337" y="95" text-anchor="middle" font-size="10" fill="#0f172a">{c["formula"]}</text>'
        f'<text x="337" y="125" text-anchor="middle" font-size="9" fill="#15803d">+ H₂O (Aroma: {c["smell"]})</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "45_esterification_condensation_reaction_mechanism_and_conditions",
        "subskill": "45_esterification_condensation_reaction_mechanism_and_conditions",
        "subskill_id": "45_esterification_condensation_reaction_mechanism_and_conditions",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_acid_part_and_alcohol_part_when_naming_esters"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Reaction type (esterification / condensation)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Catalyst identified with dual function", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Safety explanation of water bath heating (flammability)", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "IUPAC name and condensed formula of ester", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 46. Esterification: Flavouring and Fragrance Synthesis
# ==============================================================================
def builder_46(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_46_ester_flavours", seed, idx)
    cases = [
        {"flavour": "apple", "ester": "methyl butanoate", "acid": "butanoic acid", "alcohol": "methanol", "formula": "CH₃CH₂CH₂COOCH₃"},
        {"flavour": "banana", "ester": "pentyl ethanoate (isopentyl acetate)", "acid": "ethanoic acid", "alcohol": "pentan-1-ol", "formula": "CH₃COO(CH₂)₄CH₃"},
        {"flavour": "orange", "ester": "octyl ethanoate", "acid": "ethanoic acid", "alcohol": "octan-1-ol", "formula": "CH₃COO(CH₂)₇CH₃"},
        {"flavour": "pineapple", "ester": "ethyl butanoate", "acid": "butanoic acid", "alcohol": "ethanol", "formula": "CH₃CH₂CH₂COOCH₂CH₃"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"Esters are responsible for pleasant fruity flavours and aromas.\n"
        f"A food chemist synthesises an artificial {c['flavour']} flavouring which has the IUPAC name {c['ester']}:\n\n"
        f"1. Write down the IUPAC name of the carboxylic acid used to prepare this ester.\n"
        f"2. Write down the IUPAC name of the alcohol used to prepare this ester.\n"
        f"3. Draw the structural formula of the ester functional group.\n"
        f"4. Write down the structural or condensed formula of {c['ester']}."
    )
    ans_str = (
        f"1. Carboxylic acid: {c['acid']}; 2. Alcohol: {c['alcohol']}; "
        f"3. -COO- (carbonyl bonded to oxygen: -C(=O)-O-); 4. {c['formula']}."
    )
    memo = (
        f"1. Carboxylic acid: {c['acid']}. (The '-oate' suffix comes from the acid). [1]\n"
        f"2. Alcohol: {c['alcohol']}. (The first alkyl name comes from the alcohol). [1]\n"
        "3. Ester functional group: -COO- or -C(=O)-O- (a carbonyl carbon atom double-bonded to oxygen and single-bonded to another oxygen atom). [1]\n"
        f"4. Formula of {c['ester']}: {c['formula']}. [2]"
    )
    hints = {
        "tier_1": "In an ester name 'alkyl alkanoate', the alkyl is from the alcohol and alkanoate is from the acid.",
        "tier_2": f"{c['ester']}: {c['alcohol']} + {c['acid']}.",
        "tier_3": f"Acid: {c['acid']}, Alcohol: {c['alcohol']}, Formula: {c['formula']}.",
    }
    svg = (
        f'<svg viewBox="0 0 440 160" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="220" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Ester Synthesis: Artificial {c["flavour"].capitalize()} Flavour</text>'
        f'<rect x="25" y="45" width="180" height="95" rx="6" fill="#fef08a" stroke="#ca8a04"/>'
        f'<text x="115" y="70" text-anchor="middle" font-size="11" font-weight="bold">{c["acid"]}</text>'
        f'<text x="115" y="95" text-anchor="middle" font-size="11">+ {c["alcohol"]}</text>'
        f'<text x="115" y="125" text-anchor="middle" font-size="10" fill="#854d0e">Reactant precursors</text>'
        f'<rect x="235" y="45" width="180" height="95" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="325" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">{c["ester"]}</text>'
        f'<text x="325" y="95" text-anchor="middle" font-size="10" fill="#0f172a">{c["formula"]}</text>'
        f'<text x="325" y="125" text-anchor="middle" font-size="10" fill="#15803d">Flavour: {c["flavour"]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 7,
        "mode": "46_esterification_flavouring_and_fragrance_synthesis",
        "subskill": "46_esterification_flavouring_and_fragrance_synthesis",
        "subskill_id": "46_esterification_flavouring_and_fragrance_synthesis",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 5, "hints": hints, "misconception_tags": ["swapping_acid_and_alcohol_precursors_in_ester_synthesis"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "IUPAC name of carboxylic acid precursor", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name of alcohol precursor", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Structural formula of ester functional group", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Structural / condensed formula of ester", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 47. Addition Polymerisation: Polyethene, PVC and PTFE
# ==============================================================================
def builder_47(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_47_addition_polymers", seed, idx)
    cases = [
        {"monomer": "ethene (CH₂=CH₂)", "polymer": "polyethene (polythene / PE)", "repeat": "[-CH₂-CH₂-]ₙ", "use": "plastic bags, squeeze bottles, packaging film"},
        {"monomer": "chloroethene (vinyl chloride, CH₂=CHCl)", "polymer": "polychloroethene (polyvinyl chloride / PVC)", "repeat": "[-CH₂-CH(Cl)-]ₙ", "use": "water drainage pipes, electrical wire insulation, window frames"},
        {"monomer": "tetrafluoroethene (CF₂=CF₂)", "polymer": "polytetrafluoroethene (PTFE / Teflon)", "repeat": "[-CF₂-CF₂-]ₙ", "use": "non-stick cookware coatings, chemical-resistant gaskets"},
        {"monomer": "propene (CH₂=CH-CH₃)", "polymer": "polypropene (polypropylene / PP)", "repeat": "[-CH₂-CH(CH₃)-]ₙ", "use": "thermal wear, rope, bottle caps, car bumpers"},
    ]
    c = rng.choice(cases)

    prompt = (
        f"Synthetic polymers are large macromolecules produced from repeating sub-units:\n"
        f"• Monomer: {c['monomer']}\n\n"
        f"1. Define 'macromolecule' and 'polymer'.\n"
        f"2. Explain what happens to the carbon-carbon double bond during addition polymerisation.\n"
        f"3. Write down the IUPAC name of the polymer formed.\n"
        f"4. Draw the condensed structural formula of the repeating unit.\n"
        f"5. State one common practical application of this polymer."
    )
    ans_str = (
        f"1. A macromolecule is a molecule that consists of a large number of atoms; a polymer is a large molecule composed of smaller repeating monomer units; "
        f"2. The double bond opens up (breaks), allowing carbon atoms to form new covalent single bonds with adjacent monomer units; "
        f"3. {c['polymer'].split()[0]}; 4. {c['repeat']}; 5. {c['use']}."
    )
    memo = (
        "1. Definitions:\n"
        "• Macromolecule: A molecule consisting of a very large number of atoms. [1]\n"
        "• Polymer: A large molecule formed by joining many small repeating units (monomers) together. [1]\n"
        "2. The carbon-carbon double bond in the monomer breaks/opens up, creating bonding sites to link thousands of monomers "
        "together through strong covalent single bonds without the loss of any small molecules. [1]\n"
        f"3. Polymer name: {c['polymer'].split()[0]}. [1]\n"
        f"4. Repeating unit: {c['repeat']}. [1]\n"
        f"5. Application: {c['use']}. [1]"
    )
    hints = {
        "tier_1": "Addition polymerisation involves opening up carbon-carbon double bonds.",
        "tier_2": "No small molecules (like water) are eliminated during addition polymerisation.",
        "tier_3": f"Polymer: {c['polymer'].split()[0]}. Repeating unit: {c['repeat']}.",
    }
    svg = (
        f'<svg viewBox="0 0 450 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="225" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Addition Polymerisation</text>'
        f'<rect x="25" y="45" width="180" height="105" rx="6" fill="#fef9c3" stroke="#ca8a04"/>'
        f'<text x="115" y="70" text-anchor="middle" font-size="11" font-weight="bold">n Monomers</text>'
        f'<text x="115" y="95" text-anchor="middle" font-size="10">{c["monomer"]}</text>'
        f'<text x="115" y="125" text-anchor="middle" font-size="9" fill="#854d0e">C=C double bonds</text>'
        f'<line x1="210" y1="92" x2="245" y2="92" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="227" y="80" text-anchor="middle" font-size="8" fill="#2563eb">catalyst / P, Δ</text>'
        f'<rect x="250" y="45" width="175" height="105" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="337" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">{c["polymer"].split()[0]}</text>'
        f'<text x="337" y="95" text-anchor="middle" font-size="11" font-weight="bold">{c["repeat"]}</text>'
        f'<text x="337" y="125" text-anchor="middle" font-size="9" fill="#15803d">Use: {c["use"][:25]}</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "47_plastics_and_polymers_addition_polymerisation_polyethene",
        "subskill": "47_plastics_and_polymers_addition_polymerisation_polyethene",
        "subskill_id": "47_plastics_and_polymers_addition_polymerisation_polyethene",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 6, "hints": hints, "misconception_tags": ["confusing_addition_polymerisation_with_condensation_polymerisation"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": "Definitions of macromolecule and polymer", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Opening of double bonds to form single covalent bonds", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "IUPAC name of polymer", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Repeating unit structural formula", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Everyday practical application", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 48. Condensation Polymerisation: Polyesters (PET) and Polyamides (Nylon)
# ==============================================================================
def builder_48(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_48_condensation_polymers", seed, idx)
    cases = [
        {
            "polymer": "polyester (PET / polyethylene terephthalate)",
            "monomer1": "terephthalic acid (benzene-1,4-dicarboxylic acid) [di-acid]",
            "monomer2": "ethane-1,2-diol (ethylene glycol) [diol]",
            "linkage": "ester linkage (-COO-)",
            "small_mol": "water (H₂O)",
            "use": "plastic beverage bottles, fleece textiles, synthetic clothing fibres",
        },
        {
            "polymer": "polyamide (Nylon-6,6)",
            "monomer1": "hexanedioic acid (adipic acid) [di-acid]",
            "monomer2": "hexane-1,6-diamine [diamine]",
            "linkage": "amide / peptide linkage (-CONH-)",
            "small_mol": "water (H₂O)",
            "use": "fishing lines, ropes, parachutes, climbing harnesses",
        },
    ]
    c = rng.choice(cases)

    prompt = (
        f"Condensation polymerisation involves the reaction of bifunctional monomer units with the elimination of a small molecule:\n"
        f"• Polymer: {c['polymer']}\n\n"
        f"1. Define 'condensation polymerisation'.\n"
        f"2. Name the two monomer types required to synthesize {c['polymer']}.\n"
        f"3. Name the chemical bond / linkage that joins the monomer units in the polymer chain.\n"
        f"4. State the small molecule eliminated during each bond formation.\n"
        f"5. Contrast addition polymerisation and condensation polymerisation in terms of small molecule elimination."
    )
    ans_str = (
        f"1. A reaction in which monomers with two functional groups react to form a polymer chain while releasing a small molecule (like water); "
        f"2. {c['monomer1']} and {c['monomer2']}; 3. {c['linkage']}; 4. {c['small_mol']}; "
        f"5. Addition polymerisation produces no small molecule byproduct, whereas condensation polymerisation produces a small molecule (H₂O or HCl) at each link."
    )
    memo = (
        "1. Condensation polymerisation: The chemical reaction in which two different bifunctional monomers combine to form a long macromolecular chain, "
        "accompanied by the release of a small byproduct molecule (such as water or HCl). [2]\n"
        f"2. Monomers required: {c['monomer1']} and {c['monomer2']}. [2]\n"
        f"3. Linkage type: {c['linkage']}. [1]\n"
        f"4. Eliminated small molecule: {c['small_mol']}. [1]\n"
        "5. Key contrast: Addition polymerisation involves opening double bonds with NO byproduct formed; "
        "condensation polymerisation eliminates a small molecule (H₂O or HCl) per linkage formed. [1]"
    )
    hints = {
        "tier_1": "Condensation polymerisation eliminates a small molecule such as H₂O.",
        "tier_2": "Requires bifunctional monomers: di-acids + diols (polyester) or di-acids + diamines (polyamide).",
        "tier_3": f"Monomers: {c['monomer1']} + {c['monomer2']}. Linkage: {c['linkage']}.",
    }
    svg = (
        f'<svg viewBox="0 0 450 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="225" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Condensation Polymerisation ({c["polymer"][:10]})</text>'
        f'<rect x="25" y="45" width="180" height="105" rx="6" fill="#e0e7ff" stroke="#4338ca"/>'
        f'<text x="115" y="70" text-anchor="middle" font-size="10" font-weight="bold">{c["monomer1"][:24]}</text>'
        f'<text x="115" y="95" text-anchor="middle" font-size="10" fill="#4338ca">+ {c["monomer2"][:24]}</text>'
        f'<text x="115" y="125" text-anchor="middle" font-size="9" fill="#64748b">Bifunctional monomers</text>'
        f'<line x1="210" y1="92" x2="245" y2="92" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="227" y="80" text-anchor="middle" font-size="8" fill="#dc2626">- H₂O</text>'
        f'<rect x="250" y="45" width="175" height="105" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="337" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">{c["polymer"][:16]}</text>'
        f'<text x="337" y="95" text-anchor="middle" font-size="10" fill="#0f172a">Link: {c["linkage"][:15]}</text>'
        f'<text x="337" y="125" text-anchor="middle" font-size="9" fill="#15803d">+ (2n-1) H₂O</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 8,
        "mode": "48_plastics_and_polymers_condensation_polymerisation_polyesters",
        "subskill": "48_plastics_and_polymers_condensation_polymerisation_polyesters",
        "subskill_id": "48_plastics_and_polymers_condensation_polymerisation_polyesters",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 7, "hints": hints, "misconception_tags": ["neglecting_water_elimination_in_condensation_polymerisation"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of condensation polymerisation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Identification of both bifunctional monomers", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Name of linkage joining monomers", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Small eliminated molecule identified", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Contrast with addition polymerisation", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 49. Organic Synthesis: Multi-Step Reaction Flowcharts
# ==============================================================================
def builder_49(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_49_synthesis_flowchart", seed, idx)
    pathways = [
        {
            "step1_react": "ethane (C₂H₆)", "rxn1": "substitution (+ Cl₂, UV light)", "prod1": "chloroethane",
            "step2_rxn": "substitution (hydrolysis with dilute aqueous NaOH, warm)", "prod2": "ethanol",
            "step3_rxn": "elimination (dehydration with conc. H₂SO₄, 170 °C)", "prod3": "ethene",
            "step4_rxn": "addition (halogenation with Br₂ in water)", "prod4": "1,2-dibromoethane",
        },
        {
            "step1_react": "propane (C₃H₈)", "rxn1": "substitution (+ Br₂, UV light)", "prod1": "2-bromopropane",
            "step2_rxn": "elimination (dehydrohalogenation with conc. KOH in ethanol, heat)", "prod2": "propene",
            "step3_rxn": "addition (hydration with steam and H₃PO₄ catalyst)", "prod3": "propan-2-ol",
            "step4_rxn": "esterification (reaction with ethanoic acid and conc. H₂SO₄)", "prod4": "propyl ethanoate / 1-methylethyl ethanoate",
        },
    ]
    p = rng.choice(pathways)

    prompt = (
        f"A multi-step organic reaction sequence is shown below starting from {p['step1_react']}:\n"
        f"• Step 1: {p['step1_react']} ──[ Reaction I ]──→ Compound A ({p['prod1']})\n"
        f"• Step 2: Compound A ──[ Reaction II ]──→ Compound B ({p['prod2']})\n"
        f"• Step 3: Compound B ──[ Reaction III ]──→ Compound C ({p['prod3']})\n"
        f"• Step 4: Compound C ──[ Reaction IV ]──→ Compound D ({p['prod4']})\n\n"
        f"1. State the reaction type (addition, substitution, or elimination) for:\n"
        f"   (a) Reaction I\n"
        f"   (b) Reaction II\n"
        f"   (c) Reaction III\n"
        f"   (d) Reaction IV\n"
        f"2. Write down the IUPAC name of Compound C.\n"
        f"3. State the essential reaction conditions for Reaction III."
    )
    ans_str = (
        f"1. (a) Substitution; (b) Substitution; (c) Elimination; (d) Addition; "
        f"2. {p['prod3']}; 3. Concentrated H₂SO₄ (or H₃PO₄) and high heat (approx. 170 °C)."
    )
    memo = (
        "1. Reaction classifications:\n"
        f"• Reaction I: Substitution. [1]\n"
        f"• Reaction II: Substitution (hydrolysis). [1]\n"
        f"• Reaction III: Elimination (dehydration). [1]\n"
        f"• Reaction IV: Addition. [1]\n"
        f"2. IUPAC name of Compound C: {p['prod3']}. [1]\n"
        "3. Reaction conditions for Reaction III: Concentrated sulfuric acid (H₂SO₄) or phosphoric acid (H₃PO₄) and strong heat (~170 °C). [2]"
    )
    hints = {
        "tier_1": "Alkane to haloalkane is substitution; haloalkane to alcohol is substitution; alcohol to alkene is elimination; alkene to dihaloalkane is addition.",
        "tier_2": "Follow the functional group conversions step by step.",
        "tier_3": f"Compound C is {p['prod3']}. Reaction III requires conc. H₂SO₄ and heat.",
    }
    svg = (
        f'<svg viewBox="0 0 460 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="230" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Multi-Step Organic Reaction Pathway</text>'
        f'<rect x="15" y="40" width="95" height="110" rx="6" fill="#f1f5f9" stroke="#64748b"/>'
        f'<text x="62" y="65" text-anchor="middle" font-size="10" font-weight="bold">Start</text>'
        f'<text x="62" y="95" text-anchor="middle" font-size="9">{p["step1_react"][:12]}</text>'
        f'<rect x="125" y="40" width="95" height="110" rx="6" fill="#fee2e2" stroke="#dc2626"/>'
        f'<text x="172" y="65" text-anchor="middle" font-size="10" font-weight="bold">Cmpd A</text>'
        f'<text x="172" y="95" text-anchor="middle" font-size="9">{p["prod1"][:12]}</text>'
        f'<text x="172" y="125" text-anchor="middle" font-size="8" fill="#dc2626">Subst.</text>'
        f'<rect x="235" y="40" width="95" height="110" rx="6" fill="#dbeafe" stroke="#2563eb"/>'
        f'<text x="282" y="65" text-anchor="middle" font-size="10" font-weight="bold">Cmpd B</text>'
        f'<text x="282" y="95" text-anchor="middle" font-size="9">{p["prod2"][:12]}</text>'
        f'<text x="282" y="125" text-anchor="middle" font-size="8" fill="#2563eb">Hydrolysis</text>'
        f'<rect x="345" y="40" width="100" height="110" rx="6" fill="#dcfce7" stroke="#15803d"/>'
        f'<text x="395" y="65" text-anchor="middle" font-size="10" font-weight="bold">Cmpd C</text>'
        f'<text x="395" y="95" text-anchor="middle" font-size="9">{p["prod3"][:12]}</text>'
        f'<text x="395" y="125" text-anchor="middle" font-size="8" fill="#15803d">Elimination</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 9,
        "mode": "49_organic_synthesis_multi_step_reaction_pathways",
        "subskill": "49_organic_synthesis_multi_step_reaction_pathways",
        "subskill_id": "49_organic_synthesis_multi_step_reaction_pathways",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 7, "hints": hints, "misconception_tags": ["confusing_addition_substitution_elimination_reaction_types"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Classification of Reaction I as substitution", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Classification of Reaction II as substitution", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Classification of Reaction III as elimination", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Classification of Reaction IV as addition", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "IUPAC name of Compound C", "marks": 1, "editable": True},
                {"id": "mp_6", "desc": "Essential conditions for Reaction III (conc. acid + heat)", "marks": 2, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


# ==============================================================================
# 50. Organic Chemistry Diagnostic Autopsy and Structural Analysis
# ==============================================================================
def builder_50(rng: random.Random, seed: Optional[int] = None, idx: int = 0) -> Dict[str, Any]:
    qid = _make_id("org12_50_diagnostic_autopsy", seed, idx)
    cases = [
        {
            "unknown": "Compound W", "formula": "C₄H₈O₂", "iupac": "ethyl ethanoate",
            "prop": "pleasant sweet fruity smell; boiling point 77 °C; insoluble in water; non-acidic (pH 7)",
            "isomer_acid": "butanoic acid", "isomer_acid_bp": 163.5,
            "test_desc": "does not effervesce with NaHCO₃",
        },
        {
            "unknown": "Compound W", "formula": "C₄H₈O", "iupac": "butan-2-one",
            "prop": "ketone smell; boiling point 80 °C; moderately soluble in water; does not react with acidified K₂Cr₂O₇",
            "isomer_acid": "butanal", "isomer_acid_bp": 75.0,
            "test_desc": "neutral carbonyl compound",
        },
        {
            "unknown": "Compound W", "formula": "C₄H₁₀O", "iupac": "butan-1-ol",
            "prop": "forms an ester when heated with ethanoic acid; boiling point 117.7 °C; reacts with sodium metal to release H₂ gas",
            "isomer_acid": "ethoxyethane", "isomer_acid_bp": 34.6,
            "test_desc": "reacts with acidified dichromate turning from orange to green",
        },
    ]
    c = rng.choice(cases)
    bp_offset = rng.randint(1, 4)

    prompt = (
        f"An unknown organic liquid, {c['unknown']}, has molecular formula {c['formula']}.\n"
        f"Experimental investigation reveals the following diagnostic results:\n"
        f"• Physical properties: {c['prop']}\n"
        f"• Chemical test: {c['test_desc']}\n"
        f"• Functional isomer: {c['isomer_acid']} (Boiling point: {_fmt_sa(c['isomer_acid_bp'] + bp_offset)} °C)\n\n"
        f"1. Identify the homologous series to which {c['unknown']} belongs.\n"
        f"2. Write down the IUPAC name of {c['unknown']}.\n"
        f"3. Explain the large difference in boiling points between {c['unknown']} and its functional isomer {c['isomer_acid']} "
        f"in terms of intermolecular forces and energy required.\n"
        f"4. State the observation when {c['isomer_acid']} is added to aqueous sodium carbonate (Na₂CO₃)."
    )
    is_ester = "ethyl ethanoate" in c["iupac"]
    ans_str = (
        f"1. {'Esters' if is_ester else ('Ketones' if 'butan-2-one' in c['iupac'] else 'Alcohols')}; "
        f"2. {c['iupac']}; "
        f"3. {c['isomer_acid']} has intermolecular hydrogen bonds (or dimer formation) which are much stronger than the dipole-dipole forces in {c['unknown']}, requiring more thermal energy to separate; "
        f"4. {'Effervescence / bubbling (CO₂ gas released)' if is_ester else 'No visible reaction / no bubbling'}."
    )
    memo = (
        f"1. Homologous series: {'Esters' if is_ester else ('Ketones' if 'butan-2-one' in c['iupac'] else 'Alcohols')}. [1]\n"
        f"2. IUPAC name of {c['unknown']}: {c['iupac']}. [2]\n"
        f"3. IMF comparison:\n"
        f"• {c['isomer_acid']} exhibits intermolecular hydrogen bonding (forming stable cyclic dimers in carboxylic acids). [1]\n"
        f"• {c['unknown']} exhibits weaker dipole-dipole forces and London forces. [1]\n"
        "• Intermolecular hydrogen bonds require significantly more thermal energy to overcome, resulting in the higher boiling point. [1]\n"
        f"4. Chemical test: {'Carboxylic acid reacts with carbonate producing effervescence / bubbles of CO₂ gas.' if is_ester else 'No bubbling (does not react with carbonate).' } [1]"
    )
    hints = {
        "tier_1": "Determine the functional group from the molecular formula and chemical properties.",
        "tier_2": "C₄H₈O₂ with a sweet fruity smell is an ester.",
        "tier_3": f"Unknown: {c['iupac']}. Functional isomer {c['isomer_acid']} forms hydrogen bonds.",
    }
    svg = (
        f'<svg viewBox="0 0 460 170" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:sans-serif;">'
        f'<text x="230" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Diagnostic Autopsy: {c["unknown"]} ({c["formula"]})</text>'
        f'<rect x="25" y="42" width="195" height="112" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="122" y="67" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">{c["unknown"]}: {c["iupac"]}</text>'
        f'<text x="122" y="92" text-anchor="middle" font-size="9" fill="#0f172a">Formula: {c["formula"]}</text>'
        f'<text x="122" y="115" text-anchor="middle" font-size="9" fill="#475569">BP: {c["prop"].split(";")[1][:16]}</text>'
        f'<text x="122" y="138" text-anchor="middle" font-size="8" fill="#16a34a">{c["test_desc"][:25]}</text>'
        f'<rect x="240" y="42" width="195" height="112" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
        f'<text x="337" y="67" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">Functional Isomer</text>'
        f'<text x="337" y="92" text-anchor="middle" font-size="10" font-weight="bold">{c["isomer_acid"]}</text>'
        f'<text x="337" y="115" text-anchor="middle" font-size="9" fill="#dc2626">BP: {_fmt_sa(c["isomer_acid_bp"] + bp_offset)} °C</text>'
        f'<text x="337" y="138" text-anchor="middle" font-size="8" fill="#475569">Stronger H-bonding</text></svg>'
    )
    return {
        "id": qid, "question_id": qid, "term": 1, "caps_weight_percent": 25, "suggested_duration_mins": 9,
        "mode": "50_organic_chemistry_diagnostic_autopsy_and_structural_analysis",
        "subskill": "50_organic_chemistry_diagnostic_autopsy_and_structural_analysis",
        "subskill_id": "50_organic_chemistry_diagnostic_autopsy_and_structural_analysis",
        "topic": "grade12_organic_chemistry", "question_type": "short_answer", "modality": "organic_chemistry",
        "diagram_spec": _svg_spec(svg), "question": prompt, "question_text": prompt,
        "correct_answer": ans_str, "sample_answer": ans_str, "worked_solution": memo, "explanation": memo,
        "marks": 7, "hints": hints, "misconception_tags": ["confusing_ester_and_carboxylic_acid_intermolecular_bonding"],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp_1", "desc": "Identification of homologous series", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "IUPAC name of unknown compound", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Intermolecular forces comparison (hydrogen bonds vs dipole-dipole)", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Thermal energy requirement comparison", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Observation in sodium carbonate chemical test", "marks": 1, "editable": True},
            ],
            "deductions": [], "carry_forward_rule": "consequential_accuracy",
        },
    }


BUILDERS_26_50: Dict[str, Any] = {
    "26_intermolecular_forces_london_dipole_hydrogen_in_organics": builder_26,
    "27_boiling_point_comparison_homologous_series_chain_length": builder_27,
    "28_boiling_point_comparison_branching_surface_area": builder_28,
    "29_boiling_point_comparison_functional_group_type": builder_29,
    "30_vapour_pressure_inversely_proportional_to_imf_strength": builder_30,
    "31_melting_point_trends_and_crystal_packing": builder_31,
    "32_viscosity_and_flammability_trends_in_hydrocarbons": builder_32,
    "33_solubility_in_water_polar_vs_non_polar_chains": builder_33,
    "34_combustion_reactions_complete_oxidation_alkanes": builder_34,
    "35_addition_reactions_hydrogenation_of_alkenes": builder_35,
    "36_addition_reactions_halogenation_of_alkenes": builder_36,
    "37_addition_reactions_hydrohalogenation_markovnikov_rule": builder_37,
    "38_addition_reactions_hydration_of_alkenes_to_alcohols": builder_38,
    "39_elimination_reactions_dehydrohalogenation_zaitsev_rule": builder_39,
    "40_elimination_reactions_dehydration_of_alcohols": builder_40,
    "41_elimination_reactions_thermal_and_catalytic_cracking": builder_41,
    "42_substitution_reactions_halogenation_of_alkanes_uv_light": builder_42,
    "43_substitution_reactions_hydrolysis_of_haloalkanes_to_alcohols": builder_43,
    "44_substitution_reactions_alcohols_to_haloalkanes_with_hx": builder_44,
    "45_esterification_condensation_reaction_mechanism_and_conditions": builder_45,
    "46_esterification_flavouring_and_fragrance_synthesis": builder_46,
    "47_plastics_and_polymers_addition_polymerisation_polyethene": builder_47,
    "48_plastics_and_polymers_condensation_polymerisation_polyesters": builder_48,
    "49_organic_synthesis_multi_step_reaction_pathways": builder_49,
    "50_organic_chemistry_diagnostic_autopsy_and_structural_analysis": builder_50,
}
