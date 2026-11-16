"""Grade 10 Physical Sciences — Chemical Change: Archetypes 26 to 50.
Ground truth curriculum:
- curriculum_docs_auto/PhysicalSciences_Gr10/Term 3/02. Quantitative aspects of chemical change.md

Covers:
- 26–29: Empirical and molecular formulas from percentage compositions and combustion masses.
- 30–34: Molar gas volume at STP (Vm = 22,4 dm^3/mol), gas volume-mole-mass conversions and unit conversions.
- 35–38: Solution concentration (c = n/V = m/(M*V)), preparing standard solutions, dilution formula (c1V1 = c2V2).
- 39–44: Stoichiometric calculations from balanced equations (mole ratios, mass-mass, gas volume, titrations).
- 45–47: Limiting reactants and mass of unreacted excess reactant.
- 48–50: Percentage yield, percentage purity of samples, and capstone diagnostic autopsy.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Tuple

NA = 6.02e23
VM_STP = 22.4


def _fmt(val: float | int, decimals: int = 2) -> str:
    """Format numeric values with South African comma decimal separator."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    rounded = round(val, decimals)
    if abs(rounded - round(rounded)) < 1e-9:
        return str(int(round(rounded)))
    s = f"{rounded:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _svg_gas_syringe(vol_cm3: float, metal: str, gas: str) -> str:
    """Dynamic SVG of a gas syringe apparatus collecting gas from a conical flask."""
    plunger_x = 240 + min(80, int((vol_cm3 / 120.0) * 80))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 220" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Gas Collection Apparatus ({gas})</text>'
        f'<path d="M 60 180 L 100 180 L 88 120 L 72 120 Z" fill="#e2e8f0" stroke="#334155" stroke-width="2"/>'
        f'<rect x="74" y="112" width="12" height="10" fill="#64748b"/>'
        f'<text x="80" y="165" text-anchor="middle" font-size="9" fill="#0f172a">{metal} + HCl</text>'
        f'<circle cx="75" cy="155" r="2" fill="#38bdf8"/>'
        f'<circle cx="82" cy="148" r="2.5" fill="#38bdf8"/>'
        f'<circle cx="78" cy="138" r="2" fill="#38bdf8"/>'
        f'<path d="M 80 112 L 80 80 L 190 80" fill="none" stroke="#475569" stroke-width="3"/>'
        f'<rect x="190" y="65" width="130" height="30" rx="3" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<line x1="210" y1="65" x2="210" y2="73" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="230" y1="65" x2="230" y2="73" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="250" y1="65" x2="250" y2="73" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="270" y1="65" x2="270" y2="73" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="290" y1="65" x2="290" y2="73" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="210" y="60" text-anchor="middle" font-size="7" fill="#64748b">0</text>'
        f'<text x="250" y="60" text-anchor="middle" font-size="7" fill="#64748b">50</text>'
        f'<text x="290" y="60" text-anchor="middle" font-size="7" fill="#64748b">100</text>'
        f'<rect x="{plunger_x}" y="67" width="10" height="26" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>'
        f'<line x1="{plunger_x + 10}" y1="80" x2="{plunger_x + 45}" y2="80" stroke="#0f172a" stroke-width="3"/>'
        f'<rect x="{plunger_x + 45}" y="70" width="4" height="20" fill="#0f172a"/>'
        f'<text x="255" y="115" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">Volume = {_fmt(vol_cm3)} cm³</text>'
        f'<text x="255" y="130" text-anchor="middle" font-size="8" fill="#64748b">Gas syringe barrel</text>'
        f'</svg>'
    )


def _svg_titration(v_cm3: float, acid: str, base: str) -> str:
    """Dynamic SVG of a titration apparatus showing burette reading and conical flask."""
    meniscus_y = 60 + min(60, int((v_cm3 / 50.0) * 60))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 240" width="100%" style="max-width:380px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        f'<text x="190" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Titration Setup: {acid} vs {base}</text>'
        f'<line x1="80" y1="210" x2="160" y2="210" stroke="#334155" stroke-width="4"/>'
        f'<line x1="100" y1="210" x2="100" y2="35" stroke="#64748b" stroke-width="3"/>'
        f'<line x1="100" y1="70" x2="135" y2="70" stroke="#64748b" stroke-width="2"/>'
        f'<rect x="135" y="35" width="14" height="110" fill="#f8fafc" stroke="#334155" stroke-width="1.5"/>'
        f'<rect x="136" y="{meniscus_y}" width="12" height="{145 - meniscus_y}" fill="#bfdbfe" opacity="0.6"/>'
        f'<line x1="130" y1="50" x2="135" y2="50" stroke="#334155" stroke-width="1"/>'
        f'<line x1="130" y1="75" x2="135" y2="75" stroke="#334155" stroke-width="1"/>'
        f'<line x1="130" y1="100" x2="135" y2="100" stroke="#334155" stroke-width="1"/>'
        f'<line x1="130" y1="125" x2="135" y2="125" stroke="#334155" stroke-width="1"/>'
        f'<text x="126" y="53" text-anchor="end" font-size="7" fill="#475569">0</text>'
        f'<text x="126" y="103" text-anchor="end" font-size="7" fill="#475569">25</text>'
        f'<text x="126" y="128" text-anchor="end" font-size="7" fill="#475569">50</text>'
        f'<polygon points="142,145 138,155 146,155" fill="#334155"/>'
        f'<rect x="139" y="155" width="6" height="6" fill="#0284c7"/>'
        f'<path d="M 125 210 L 160 210 L 150 170 L 135 170 Z" fill="#e0f2fe" stroke="#334155" stroke-width="1.5"/>'
        f'<text x="142" y="198" text-anchor="middle" font-size="8" fill="#0369a1">{base} + Ind.</text>'
        f'<rect x="200" y="60" width="160" height="75" rx="6" fill="#f1f5f9" stroke="#cbd5e1"/>'
        f'<text x="210" y="80" font-size="10" font-weight="bold" fill="#0f172a">Burette Titre Reading:</text>'
        f'<text x="210" y="100" font-size="14" font-weight="bold" fill="#2563eb">V = {_fmt(v_cm3)} cm³</text>'
        f'<text x="210" y="120" font-size="9" fill="#475569">Standard acid ({acid})</text>'
        f'</svg>'
    )


def _make_q(
    r: random.Random,
    subskill: str,
    idx: int,
    prompt: str,
    correct_answer: str,
    solution_text: str,
    marks: int,
    tags: List[str],
    rubric: List[Dict[str, Any]],
    hints: Dict[str, str],
    svg: Optional[str] = None,
) -> Dict[str, Any]:
    q_id = f"g10_chem_{idx:02d}_{r.randint(100000, 999999)}"
    marking_points = [
        {
            "id": f"mp_{i + 1}",
            "desc": item.get("criterion", f"Step {i + 1}"),
            "marks": item.get("marks", 1),
            "editable": True,
        }
        for i, item in enumerate(rubric)
    ]
    out: Dict[str, Any] = {
        "id": q_id,
        "topic": "Quantitative aspects of chemical change",
        "subskill": subskill,
        "archetype_id": subskill,
        "question_type": "numeric_input",
        "modality": "chemical_equation",
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": correct_answer,
        "sample_answer": solution_text,
        "solution": solution_text,
        "explanation": solution_text,
        "marks": marks,
        "term": 3,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "learning_objective_id": f"g10_chem_{subskill}",
        "mode": subskill,
        "misconception_tags": tags,
        "rubric": rubric,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": hints,
    }
    if svg:
        out["diagram_spec"] = {
            "kind": "inline_svg",
            "svg": svg,
            "width": 380,
            "height": 260,
        }
    return out


# 26. Empirical formula from percentage composition
def build_26_empirical_formula_from_percentage_composition(r: random.Random) -> Dict[str, Any]:
    compounds = [
        {"formula": r"\text{CH}_2", "name": "alkene monomer", "c_pct": 85.71, "h_pct": 14.29},
        {"formula": r"\text{NO}_2", "name": "nitrogen dioxide", "n_pct": 30.43, "o_pct": 69.57},
        {"formula": r"\text{SO}_3", "name": "sulfur oxide", "s_pct": 40.05, "o_pct": 59.95},
        {"formula": r"\text{P}_2\text{O}_5", "name": "phosphorus oxide", "p_pct": 43.66, "o_pct": 56.34},
        {"formula": r"\text{Fe}_2\text{O}_3", "name": "iron(III) oxide", "fe_pct": 69.94, "o_pct": 30.06},
    ]
    cp = r.choice(compounds)
    formula = cp["formula"]
    if "c_pct" in cp:
        pct_str = f"**{_fmt(cp['c_pct'])}% carbon** and **{_fmt(cp['h_pct'])}% hydrogen**"
        sol_steps = (
            f"1. Assume a $100\\text{{ g}}$ sample:\n"
            f"   - $m(\\text{{C}}) = {_fmt(cp['c_pct'])}\\text{{ g}}$, $m(\\text{{H}}) = {_fmt(cp['h_pct'])}\\text{{ g}}$\n"
            f"2. Convert mass to moles:\n"
            f"   - $n(\\text{{C}}) = \\frac{{{_fmt(cp['c_pct'])}}}{{12}} = 7{{,}}14\\text{{ mol}}$\n"
            f"   - $n(\\text{{H}}) = \\frac{{{_fmt(cp['h_pct'])}}}{{1}} = 14{{,}}29\\text{{ mol}}$\n"
            f"3. Divide by the smallest mole value ($7{{,}}14$):\n"
            f"   - $\\text{{C}} : \\text{{H}} = \\frac{{7{{,}}14}}{{7{{,}}14}} : \\frac{{14{{,}}29}}{{7{{,}}14}} = 1 : 2$\n"
            f"4. Empirical formula is **${formula}$**."
        )
    elif "n_pct" in cp:
        pct_str = f"**{_fmt(cp['n_pct'])}% nitrogen** and **{_fmt(cp['o_pct'])}% oxygen**"
        sol_steps = (
            f"1. In $100\\text{{ g}}$ of compound:\n"
            f"   - $n(\\text{{N}}) = \\frac{{{_fmt(cp['n_pct'])}}}{{14}} = 2{{,}}17\\text{{ mol}}$\n"
            f"   - $n(\\text{{O}}) = \\frac{{{_fmt(cp['o_pct'])}}}{{16}} = 4{{,}}35\\text{{ mol}}$\n"
            f"2. Divide by $2{{,}}17$:\n"
            f"   - $\\text{{N}} : \\text{{O}} = 1 : 2$\n"
            f"3. Empirical formula is **${formula}$**."
        )
    elif "s_pct" in cp:
        pct_str = f"**{_fmt(cp['s_pct'])}% sulfur** and **{_fmt(cp['o_pct'])}% oxygen**"
        sol_steps = (
            f"1. In $100\\text{{ g}}$ of compound:\n"
            f"   - $n(\\text{{S}}) = \\frac{{{_fmt(cp['s_pct'])}}}{{32{{,}}1}} = 1{{,}}25\\text{{ mol}}$\n"
            f"   - $n(\\text{{O}}) = \\frac{{{_fmt(cp['o_pct'])}}}{{16}} = 3{{,}}75\\text{{ mol}}$\n"
            f"2. Divide by $1{{,}}25$:\n"
            f"   - $\\text{{S}} : \\text{{O}} = 1 : 3$\n"
            f"3. Empirical formula is **${formula}$**."
        )
    elif "p_pct" in cp:
        pct_str = f"**{_fmt(cp['p_pct'])}% phosphorus** and **{_fmt(cp['o_pct'])}% oxygen**"
        sol_steps = (
            f"1. In $100\\text{{ g}}$ of compound:\n"
            f"   - $n(\\text{{P}}) = \\frac{{{_fmt(cp['p_pct'])}}}{{31}} = 1{{,}}41\\text{{ mol}}$\n"
            f"   - $n(\\text{{O}}) = \\frac{{{_fmt(cp['o_pct'])}}}{{16}} = 3{{,}}52\\text{{ mol}}$\n"
            f"2. Divide by $1{{,}}41$:\n"
            f"   - $\\text{{P}} : \\text{{O}} = 1 : 2{{,}}5$\n"
            f"3. Multiply by 2 for whole-number ratio: $2 : 5$.\n"
            f"4. Empirical formula is **${formula}$**."
        )
    else:
        pct_str = f"**{_fmt(cp['fe_pct'])}% iron** and **{_fmt(cp['o_pct'])}% oxygen**"
        sol_steps = (
            f"1. In $100\\text{{ g}}$ of compound:\n"
            f"   - $n(\\text{{Fe}}) = \\frac{{{_fmt(cp['fe_pct'])}}}{{56}} = 1{{,}}25\\text{{ mol}}$\n"
            f"   - $n(\\text{{O}}) = \\frac{{{_fmt(cp['o_pct'])}}}{{16}} = 1{{,}}88\\text{{ mol}}$\n"
            f"2. Divide by $1{{,}}25$: $1 : 1{{,}}5$.\n"
            f"3. Multiply by 2: $2 : 3$. Empirical formula is **${formula}$**."
        )

    prompt = (
        f"A laboratory analysis of a chemical compound determines that it contains {pct_str} by mass.\n\n"
        f"1. Define the term *empirical formula*.\n"
        f"2. Determine the empirical formula of the compound showing all calculation steps."
    )
    ans = f"{formula}"
    sol = f"1. **Empirical formula:** The simplest whole-number ratio of atoms of each element in a compound.\n\n2. **Calculation:**\n{sol_steps}"
    return _make_q(
        r, "26_empirical_formula_from_percentage_composition", 26, prompt, ans, sol, 4,
        ["empirical_formula_ratio_rounding_error"],
        [{"step": 1, "criterion": "Definition of empirical formula", "marks": 1}, {"step": 2, "criterion": "Convert % to moles (n = m/M)", "marks": 1}, {"step": 3, "criterion": "Divide by smallest mole value", "marks": 1}, {"step": 4, "criterion": f"Correct empirical formula: {formula}", "marks": 1}],
        {"tier_1": "Assume a 100 g sample, convert percentages directly to grams, then find moles using n = m/M.", "tier_2": "Divide each mole value by the smallest number of moles to obtain the ratio.", "tier_3": ans},
    )


# 27. Empirical formula from combustion or synthesis masses
def build_27_empirical_formula_from_combustion_or_synthesis_masses(r: random.Random) -> Dict[str, Any]:
    # Metal heating in crucible: Mg + O2 -> MgO or Cu + S -> CuS / Cu2S
    pairs = [
        {"metal": "magnesium", "symbol": "Mg", "M_m": 24.3, "M_nm": 16.0, "ratio": (1, 1), "formula": r"\text{MgO}", "m_metal": r.choice([2.43, 4.86, 1.22])},
        {"metal": "copper", "symbol": "Cu", "M_m": 63.5, "M_nm": 32.1, "ratio": (1, 1), "formula": r"\text{CuS}", "m_metal": r.choice([6.35, 12.70, 3.18])},
        {"metal": "zinc", "symbol": "Zn", "M_m": 65.4, "M_nm": 16.0, "ratio": (1, 1), "formula": r"\text{ZnO}", "m_metal": r.choice([6.54, 13.08, 3.27])},
    ]
    p = r.choice(pairs)
    n_metal = round(p["m_metal"] / p["M_m"], 2)
    m_nm = round(n_metal * p["M_nm"], 2)
    m_product = round(p["m_metal"] + m_nm, 2)

    prompt = (
        f"In an experiment, a clean ribbon of {p['metal']} with mass **${_fmt(p['m_metal'])}\\text{{ g}}$** "
        f"is heated strongly in a crucible until it completely reacts with oxygen to form a white powder.\n"
        f"The mass of the product after cooling is **${_fmt(m_product)}\\text{{ g}}$**.\n\n"
        f"1. Calculate the mass of oxygen that reacted with the {p['metal']}.\n"
        f"2. Determine the empirical formula of the oxide formed."
    )
    ans = f"{p['formula']}"
    sol = (
        f"1. Mass of oxygen reacted:\n"
        f"   $$m(\\text{{O}}) = m(\\text{{product}}) - m(\\text{{{p['symbol']}}}) = {_fmt(m_product)} - {_fmt(p['m_metal'])} = {_fmt(m_nm)}\\text{{ g}}$$\n\n"
        f"2. Mole calculation:\n"
        f"   - $n(\\text{{{p['symbol']}}}) = \\frac{{{_fmt(p['m_metal'])}}}{{{_fmt(p['M_m'])}}} = {_fmt(n_metal)}\\text{{ mol}}$\n"
        f"   - $n(\\text{{O}}) = \\frac{{{_fmt(m_nm)}}}{{{_fmt(p['M_nm'])}}} = {_fmt(n_metal)}\\text{{ mol}}$\n"
        f"   Mole ratio: $\\frac{{{_fmt(n_metal)}}}{{{_fmt(n_metal)}}} : \\frac{{{_fmt(n_metal)}}}{{{_fmt(n_metal)}}} = 1 : 1$\n"
        f"   Empirical formula: **${p['formula']}$**."
    )
    return _make_q(
        r, "27_empirical_formula_from_combustion_or_synthesis_masses", 27, prompt, ans, sol, 4,
        ["subtraction_error_in_synthesis_masses", "ratio_miscalculation"],
        [{"step": 1, "criterion": f"Mass of nonmetal = {_fmt(m_nm)} g", "marks": 1}, {"step": 2, "criterion": "Moles of both elements calculated", "marks": 1}, {"step": 3, "criterion": "Simplest mole ratio 1:1", "marks": 1}, {"step": 4, "criterion": f"Empirical formula ${p['formula']}$", "marks": 1}],
        {"tier_1": "Subtract the metal mass from the product mass to find the mass of oxygen reacted.", "tier_2": "Calculate moles for both metal and oxygen using n = m/M.", "tier_3": ans},
    )


# 28. Molecular formula from empirical formula and molar mass
def build_28_molecular_formula_from_empirical_formula_and_molar_mass(r: random.Random) -> Dict[str, Any]:
    choices = [
        {"emp": r"\text{CH}_2", "emp_name": "CH2", "M_emp": 14.0, "k": 2, "mol": r"\text{C}_2\text{H}_4", "M_mol": 28.0, "name": "ethene"},
        {"emp": r"\text{CH}_2", "emp_name": "CH2", "M_emp": 14.0, "k": 3, "mol": r"\text{C}_3\text{H}_6", "M_mol": 42.0, "name": "propene"},
        {"emp": r"\text{CH}_2", "emp_name": "CH2", "M_emp": 14.0, "k": 4, "mol": r"\text{C}_4\text{H}_8", "M_mol": 56.0, "name": "butene"},
        {"emp": r"\text{CH}_2\text{O}", "emp_name": "CH2O", "M_emp": 30.0, "k": 6, "mol": r"\text{C}_6\text{H}_{12}\text{O}_6", "M_mol": 180.0, "name": "glucose"},
        {"emp": r"\text{CH}_2\text{O}", "emp_name": "CH2O", "M_emp": 30.0, "k": 2, "mol": r"\text{C}_2\text{H}_4\text{O}_2", "M_mol": 60.0, "name": "ethanoic acid"},
        {"emp": r"\text{NO}_2", "emp_name": "NO2", "M_emp": 46.0, "k": 2, "mol": r"\text{N}_2\text{O}_4", "M_mol": 92.0, "name": "dinitrogen tetroxide"},
    ]
    c = r.choice(choices)
    prompt = (
        f"A compound with the empirical formula **${c['emp']}$** has an experimentally determined "
        f"molar mass of **${_fmt(c['M_mol'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$**.\n\n"
        f"1. Calculate the empirical formula mass ($M_{{\\text{{emp}}}}$).\n"
        f"2. Determine the scaling multiplier $k = \\frac{{M}}{{M_{{\\text{{emp}}}}}}$.\n"
        f"3. State the molecular formula of the compound."
    )
    ans = f"{c['mol']}"
    sol = (
        f"1. Empirical formula mass:\n"
        f"   $$M_{{\\text{{emp}}}} = {_fmt(c['M_emp'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$$\n\n"
        f"2. Multiplier $k$:\n"
        f"   $$k = \\frac{{M}}{{M_{{\\text{{emp}}}}}} = \\frac{{{_fmt(c['M_mol'])}}}{{{_fmt(c['M_emp'])}}} = {c['k']}$$\n\n"
        f"3. Molecular formula:\n"
        f"   $$({c['emp_name']})_{{{c['k']}}} = **{c['mol']}**$$"
    )
    return _make_q(
        r, "28_molecular_formula_from_empirical_formula_and_molar_mass", 28, prompt, ans, sol, 3,
        ["inverting_molar_mass_ratio", "confusing_empirical_and_molecular_formula"],
        [{"step": 1, "criterion": f"Empirical formula mass = {_fmt(c['M_emp'])} g/mol", "marks": 1}, {"step": 2, "criterion": f"Ratio k = {c['k']}", "marks": 1}, {"step": 3, "criterion": f"Molecular formula ${c['mol']}$", "marks": 1}],
        {"tier_1": "Find the molar mass of the empirical formula unit first.", "tier_2": "Divide given compound molar mass by the empirical formula mass to find k.", "tier_3": ans},
    )


# 29. Empirical and molecular formula combined organic
def build_29_empirical_and_molecular_formula_combined_organic(r: random.Random) -> Dict[str, Any]:
    variants = [
        {"c": 40.0, "h": 6.67, "o": 53.33, "emp": r"\text{CH}_2\text{O}", "M_emp": 30.0, "M": 180.0, "k": 6, "mol": r"\text{C}_6\text{H}_{12}\text{O}_6", "name": "glucose"},
        {"c": 54.55, "h": 9.09, "o": 36.36, "emp": r"\text{C}_2\text{H}_4\text{O}", "M_emp": 44.0, "M": 88.0, "k": 2, "mol": r"\text{C}_4\text{H}_8\text{O}_2", "name": "ethyl ethanoate isomer"},
        {"c": 52.17, "h": 13.04, "o": 34.78, "emp": r"\text{C}_2\text{H}_6\text{O}", "M_emp": 46.0, "M": 46.0, "k": 1, "mol": r"\text{C}_2\text{H}_6\text{O}", "name": "ethanol"},
    ]
    v = r.choice(variants)
    prompt = (
        f"An organic compound contains **{_fmt(v['c'])}% C**, **{_fmt(v['h'])}% H**, and **{_fmt(v['o'])}% O** by mass.\n"
        f"The molar mass of the compound is determined to be **${_fmt(v['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$**.\n\n"
        f"1. Determine the empirical formula of the compound.\n"
        f"2. Determine the molecular formula of the compound."
    )
    ans = f"Empirical: {v['emp']}, Molecular: {v['mol']}"
    sol = (
        f"1. In a $100\\text{{ g}}$ sample:\n"
        f"   - $n(\\text{{C}}) = \\frac{{{_fmt(v['c'])}}}{{12}} = {_fmt(v['c']/12.0, 2)}\\text{{ mol}}$\n"
        f"   - $n(\\text{{H}}) = \\frac{{{_fmt(v['h'])}}}{{1}} = {_fmt(v['h'], 2)}\\text{{ mol}}$\n"
        f"   - $n(\\text{{O}}) = \\frac{{{_fmt(v['o'])}}}{{16}} = {_fmt(v['o']/16.0, 2)}\\text{{ mol}}$\n"
        f"   Dividing by smallest mole value gives empirical formula: **${v['emp']}$**.\n\n"
        f"2. Empirical formula mass: $M_{{\\text{{emp}}}} = {_fmt(v['M_emp'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$.\n"
        f"   Ratio: $k = \\frac{{{_fmt(v['M'])}}}{{{_fmt(v['M_emp'])}}} = {v['k']}$.\n"
        f"   Therefore, molecular formula is **${v['mol']}$**."
    )
    return _make_q(
        r, "29_empirical_and_molecular_formula_combined_organic", 29, prompt, ans, sol, 5,
        ["empirical_formula_ratio_rounding_error", "confusing_empirical_and_molecular_formula"],
        [{"step": 1, "criterion": "Moles of C, H, O calculated", "marks": 2}, {"step": 2, "criterion": f"Empirical formula ${v['emp']}$", "marks": 1}, {"step": 3, "criterion": f"Ratio k = {v['k']}", "marks": 1}, {"step": 4, "criterion": f"Molecular formula ${v['mol']}$", "marks": 1}],
        {"tier_1": "Find moles of each element first to get empirical formula.", "tier_2": "Calculate empirical formula mass and divide molar mass by it to get k.", "tier_3": ans},
    )


# 30. Molar gas volume at STP volume to moles
def build_30_molar_gas_volume_at_stp_volume_to_moles(r: random.Random) -> Dict[str, Any]:
    gases = ["oxygen (O₂)", "carbon dioxide (CO₂)", "nitrogen (N₂)", "hydrogen (H₂)", "methane (CH₄)"]
    gas = r.choice(gases)
    v_dm3 = r.choice([2.24, 4.48, 5.60, 11.20, 22.40, 33.60, 44.80, 56.00])
    n = round(v_dm3 / VM_STP, 3)

    prompt = (
        f"A sample of {gas} occupies a volume of **${_fmt(v_dm3)}\\text{{ dm}}^3$** "
        f"at standard temperature and pressure (STP).\n\n"
        f"1. State the value of the molar gas volume ($V_m$) at STP.\n"
        f"2. Calculate the number of moles of gas present in the sample."
    )
    ans = f"{_fmt(n)} mol"
    sol = (
        f"1. At STP, the molar gas volume is $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$.\n\n"
        f"2. Number of moles:\n"
        f"   $$n = \\frac{{V}}{{V_m}} = \\frac{{{_fmt(v_dm3)}}}{{22{{,}}4}} = {_fmt(n)}\\text{{ mol}}$$"
    )
    return _make_q(
        r, "30_molar_gas_volume_at_stp_volume_to_moles", 30, prompt, ans, sol, 3,
        ["forgot_stp_molar_volume_22_4"],
        [{"step": 1, "criterion": "State Vm = 22,4 dm^3/mol", "marks": 1}, {"step": 2, "criterion": "Formula: n = V / Vm", "marks": 1}, {"step": 3, "criterion": f"Answer n = {_fmt(n)} mol", "marks": 1}],
        {"tier_1": "Recall that 1 mole of any gas occupies 22,4 dm^3 at STP.", "tier_2": "Use formula n = V / Vm where Vm = 22,4 dm^3/mol.", "tier_3": ans},
    )


# 31. Molar gas volume at STP moles to volume
def build_31_molar_gas_volume_at_stp_moles_to_volume(r: random.Random) -> Dict[str, Any]:
    gases = ["chlorine (Cl₂)", "ammonia (NH₃)", "sulfur dioxide (SO₂)", "argon (Ar)"]
    gas = r.choice(gases)
    n = r.choice([0.15, 0.25, 0.50, 1.25, 2.50, 3.00, 0.05])
    v_dm3 = round(n * VM_STP, 3)

    prompt = (
        f"Calculate the volume (in $\\text{{dm}}^3$) occupied by **${_fmt(n)}\\text{{ mol}}$** of {gas} "
        f"at standard temperature and pressure (STP)."
    )
    ans = f"{_fmt(v_dm3)} dm3"
    sol = (
        f"At STP:\n"
        f"$$V = n \\times V_m = {_fmt(n)} \\times 22{{,}}4 = {_fmt(v_dm3)}\\text{{ dm}}^3$$"
    )
    return _make_q(
        r, "31_molar_gas_volume_at_stp_moles_to_volume", 31, prompt, ans, sol, 2,
        ["inverted_gas_volume_formula"],
        [{"step": 1, "criterion": "Formula V = n * Vm", "marks": 1}, {"step": 2, "criterion": f"Answer V = {_fmt(v_dm3)} dm^3", "marks": 1}],
        {"tier_1": "Multiply moles by the molar gas volume at STP.", "tier_2": "V = n * 22,4 dm^3.", "tier_3": ans},
    )


# 32. Gas volume at STP from mass
def build_32_gas_volume_at_stp_from_mass(r: random.Random) -> Dict[str, Any]:
    gases = [
        {"name": "carbon dioxide (CO₂)", "formula": r"\text{CO}_2", "M": 44.0, "mass": r.choice([22.0, 44.0, 88.0, 11.0, 5.5])},
        {"name": "oxygen (O₂)", "formula": r"\text{O}_2", "M": 32.0, "mass": r.choice([16.0, 32.0, 64.0, 8.0, 4.0])},
        {"name": "methane (CH₄)", "formula": r"\text{CH}_4", "M": 16.0, "mass": r.choice([8.0, 16.0, 32.0, 4.0, 2.0])},
        {"name": "sulfur dioxide (SO₂)", "formula": r"\text{SO}_2", "M": 64.1, "mass": r.choice([32.05, 64.1, 128.2])},
    ]
    g = r.choice(gases)
    n = round(g["mass"] / g["M"], 3)
    v_dm3 = round(n * VM_STP, 2)

    prompt = (
        f"Calculate the volume occupied by **${_fmt(g['mass'])}\\text{{ g}}$** of {g['name']} "
        f"at standard temperature and pressure (STP).\n"
        f"($M({g['formula']}) = {_fmt(g['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$)"
    )
    ans = f"{_fmt(v_dm3)} dm3"
    sol = (
        f"1. Calculate moles of gas:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{_fmt(g['mass'])}}}{{{_fmt(g['M'])}}} = {_fmt(n)}\\text{{ mol}}$$\n\n"
        f"2. Calculate volume at STP:\n"
        f"   $$V = n \\times V_m = {_fmt(n)} \\times 22{{,}}4 = {_fmt(v_dm3)}\\text{{ dm}}^3$$"
    )
    return _make_q(
        r, "32_gas_volume_at_stp_from_mass", 32, prompt, ans, sol, 3,
        ["skipped_mole_conversion_in_gas_calc"],
        [{"step": 1, "criterion": f"Calculate n = m/M = {_fmt(n)} mol", "marks": 1}, {"step": 2, "criterion": "Formula V = n * Vm", "marks": 1}, {"step": 3, "criterion": f"Answer V = {_fmt(v_dm3)} dm^3", "marks": 1}],
        {"tier_1": "Convert mass to moles using n = m/M first.", "tier_2": "Multiply moles by 22,4 dm^3/mol to find volume at STP.", "tier_3": ans},
    )


# 33. Mass of gas at STP from volume
def build_33_mass_of_gas_at_stp_from_volume(r: random.Random) -> Dict[str, Any]:
    gases = [
        {"name": "oxygen gas (O₂)", "formula": r"\text{O}_2", "M": 32.0, "v": r.choice([5.6, 11.2, 2.24, 44.8])},
        {"name": "carbon dioxide gas (CO₂)", "formula": r"\text{CO}_2", "M": 44.0, "v": r.choice([4.48, 11.2, 5.6, 22.4])},
        {"name": "nitrogen gas (N₂)", "formula": r"\text{N}_2", "M": 28.0, "v": r.choice([5.6, 11.2, 2.24, 33.6])},
    ]
    g = r.choice(gases)
    n = round(g["v"] / VM_STP, 3)
    m = round(n * g["M"], 2)

    prompt = (
        f"A weather balloon contains **${_fmt(g['v'])}\\text{{ dm}}^3$** of {g['name']} at STP.\n"
        f"Calculate the mass of the gas in the balloon.\n"
        f"($M({g['formula']}) = {_fmt(g['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$)"
    )
    ans = f"{_fmt(m)} g"
    sol = (
        f"1. Calculate moles of gas:\n"
        f"   $$n = \\frac{{V}}{{V_m}} = \\frac{{{_fmt(g['v'])}}}{{22{{,}}4}} = {_fmt(n)}\\text{{ mol}}$$\n\n"
        f"2. Calculate mass of gas:\n"
        f"   $$m = n \\times M = {_fmt(n)} \\times {_fmt(g['M'])} = {_fmt(m)}\\text{{ g}}$$"
    )
    return _make_q(
        r, "33_mass_of_gas_at_stp_from_volume", 33, prompt, ans, sol, 3,
        ["forgot_to_multiply_moles_by_molar_mass"],
        [{"step": 1, "criterion": f"Calculate n = V/Vm = {_fmt(n)} mol", "marks": 1}, {"step": 2, "criterion": "Formula m = n * M", "marks": 1}, {"step": 3, "criterion": f"Answer m = {_fmt(m)} g", "marks": 1}],
        {"tier_1": "Divide volume by 22,4 dm^3/mol to obtain moles.", "tier_2": "Multiply moles by molar mass M to obtain mass in grams.", "tier_3": ans},
    )


# 34. Unit conversions for gas volume cm3 to dm3
def build_34_unit_conversions_for_gas_volume_cm3_to_dm3(r: random.Random) -> Dict[str, Any]:
    v_cm3 = r.choice([250.0, 500.0, 750.0, 1200.0, 2500.0, 350.0])
    v_dm3 = round(v_cm3 / 1000.0, 4)
    n = round(v_dm3 / VM_STP, 4)

    prompt = (
        f"A laboratory syringe collects **${_fmt(v_cm3)}\\text{{ cm}}^3$** of hydrogen gas, $\\text{{H}}_2(\\text{{g}})$, at STP.\n\n"
        f"1. Convert the volume from $\\text{{cm}}^3$ to $\\text{{dm}}^3$.\n"
        f"2. Calculate the number of moles of hydrogen gas collected."
    )
    ans = f"{_fmt(n, 4)} mol"
    sol = (
        f"1. Unit conversion:\n"
        f"   $$V = \\frac{{{_fmt(v_cm3)}}}{{1000}} = {_fmt(v_dm3, 3)}\\text{{ dm}}^3$$\n\n"
        f"2. Number of moles:\n"
        f"   $$n = \\frac{{V}}{{V_m}} = \\frac{{{_fmt(v_dm3, 3)}}}{{22{{,}}4}} = {_fmt(n, 4)}\\text{{ mol}}$$"
    )
    return _make_q(
        r, "34_unit_conversions_for_gas_volume_cm3_to_dm3", 34, prompt, ans, sol, 3,
        ["failed_cm3_to_dm3_conversion"],
        [{"step": 1, "criterion": f"Convert to {_fmt(v_dm3, 3)} dm^3 (divide by 1000)", "marks": 1}, {"step": 2, "criterion": "Formula n = V / Vm", "marks": 1}, {"step": 3, "criterion": f"Answer n = {_fmt(n, 4)} mol", "marks": 1}],
        {"tier_1": "1 dm^3 = 1000 cm^3, so divide cm^3 by 1000 to convert to dm^3.", "tier_2": "Then use n = V / 22,4 dm^3/mol.", "tier_3": ans},
    )


# 35. Concentration of solution moles and volume
def build_35_concentration_of_solution_moles_and_volume(r: random.Random) -> Dict[str, Any]:
    n = r.choice([0.1, 0.25, 0.5, 0.75, 1.5, 2.0])
    v_cm3 = r.choice([250.0, 500.0, 1000.0, 2000.0, 100.0])
    v_dm3 = v_cm3 / 1000.0
    c = round(n / v_dm3, 2)

    prompt = (
        f"A learner dissolves **${_fmt(n)}\\text{{ mol}}$** of sodium hydroxide ($\\text{{NaOH}}$) "
        f"in water to make a solution of total volume **${_fmt(v_cm3)}\\text{{ cm}}^3$**.\n\n"
        f"1. Convert the volume into $\\text{{dm}}^3$.\n"
        f"2. Calculate the concentration of the sodium hydroxide solution in $\\text{{mol}}\\cdot\\text{{dm}}^{{-3}}$."
    )
    ans = f"{_fmt(c)} mol/dm3"
    sol = (
        f"1. $V = \\frac{{{_fmt(v_cm3)}}}{{1000}} = {_fmt(v_dm3)}\\text{{ dm}}^3$\n\n"
        f"2. Concentration:\n"
        f"   $$c = \\frac{{n}}{{V}} = \\frac{{{_fmt(n)}}}{{{_fmt(v_dm3)}}} = {_fmt(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$"
    )
    return _make_q(
        r, "35_concentration_of_solution_moles_and_volume", 35, prompt, ans, sol, 3,
        ["forgot_to_convert_cm3_to_dm3_in_concentration"],
        [{"step": 1, "criterion": f"Convert V = {_fmt(v_dm3)} dm^3", "marks": 1}, {"step": 2, "criterion": "Formula c = n / V", "marks": 1}, {"step": 3, "criterion": f"Concentration c = {_fmt(c)} mol/dm^3", "marks": 1}],
        {"tier_1": "Volume must always be in dm^3 when calculating molar concentration.", "tier_2": "Divide cm^3 by 1000 to get dm^3, then apply c = n / V.", "tier_3": ans},
    )


# 36. Concentration of solution mass molar mass volume
def build_36_concentration_of_solution_mass_molar_mass_volume(r: random.Random) -> Dict[str, Any]:
    salts = [
        {"name": "sodium chloride", "formula": r"\text{NaCl}", "M": 58.5, "mass": r.choice([5.85, 11.70, 2.93])},
        {"name": "sodium carbonate", "formula": r"\text{Na}_2\text{CO}_3", "M": 106.0, "mass": r.choice([10.60, 5.30, 21.20])},
        {"name": "potassium hydroxide", "formula": r"\text{KOH}", "M": 56.1, "mass": r.choice([5.61, 11.22, 2.81])},
    ]
    s = r.choice(salts)
    v_cm3 = r.choice([250.0, 500.0, 1000.0])
    v_dm3 = v_cm3 / 1000.0
    n = round(s["mass"] / s["M"], 3)
    c = round(n / v_dm3, 2)

    prompt = (
        f"A solution is prepared by dissolving **${_fmt(s['mass'])}\\text{{ g}}$** of {s['name']} (${s['formula']}$) "
        f"in distilled water to make exactly **${_fmt(v_cm3)}\\text{{ cm}}^3$** of solution.\n"
        f"($M({s['formula']}) = {_fmt(s['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)\n\n"
        f"1. Calculate the number of moles of {s['name']} dissolved.\n"
        f"2. Calculate the concentration of the solution in $\\text{{mol}}\\cdot\\text{{dm}}^{{-3}}$."
    )
    ans = f"{_fmt(c)} mol/dm3"
    sol = (
        f"1. Moles of solute:\n"
        f"   $$n = \\frac{{m}}{{M}} = \\frac{{{_fmt(s['mass'])}}}{{{_fmt(s['M'])}}} = {_fmt(n)}\\text{{ mol}}$$\n\n"
        f"2. Volume in $\\text{{dm}}^3$: $V = \\frac{{{_fmt(v_cm3)}}}{{1000}} = {_fmt(v_dm3)}\\text{{ dm}}^3$\n\n"
        f"3. Concentration:\n"
        f"   $$c = \\frac{{n}}{{V}} = \\frac{{{_fmt(n)}}}{{{_fmt(v_dm3)}}} = {_fmt(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"   (or directly: $c = \\frac{{m}}{{M \\cdot V}}$)"
    )
    return _make_q(
        r, "36_concentration_of_solution_mass_molar_mass_volume", 36, prompt, ans, sol, 3,
        ["forgot_to_convert_cm3_to_dm3_in_concentration", "confused_moles_and_mass"],
        [{"step": 1, "criterion": f"Calculate n = m/M = {_fmt(n)} mol", "marks": 1}, {"step": 2, "criterion": f"Convert V = {_fmt(v_dm3)} dm^3", "marks": 1}, {"step": 3, "criterion": f"Answer c = {_fmt(c)} mol/dm^3", "marks": 1}],
        {"tier_1": "Calculate moles using n = m/M, then convert volume to dm^3.", "tier_2": "Use c = n / V or c = m / (M * V).", "tier_3": ans},
    )


# 37. Mass of solute required for standard solution
def build_37_mass_of_solute_required_for_standard_solution(r: random.Random) -> Dict[str, Any]:
    compounds = [
        {"name": "anhydrous sodium carbonate", "formula": r"\text{Na}_2\text{CO}_3", "M": 106.0},
        {"name": "sodium hydroxide", "formula": r"\text{NaOH}", "M": 40.0},
        {"name": "potassium hydrogen phthalate", "formula": r"\text{KHC}_8\text{H}_4\text{O}_4", "M": 204.2},
        {"name": "copper(II) sulfate", "formula": r"\text{CuSO}_4", "M": 159.6},
    ]
    cp = r.choice(compounds)
    v_cm3 = r.choice([250.0, 500.0, 1000.0])
    c = r.choice([0.10, 0.20, 0.25, 0.50])
    v_dm3 = v_cm3 / 1000.0
    n = c * v_dm3
    m = round(n * cp["M"], 2)

    prompt = (
        f"A chemistry educator instructs a learner to prepare **${_fmt(v_cm3)}\\text{{ cm}}^3$** "
        f"of a **${_fmt(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** standard solution of {cp['name']} (${cp['formula']}$).\n"
        f"($M({cp['formula']}) = {_fmt(cp['M'])}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)\n\n"
        f"1. Define the term *standard solution*.\n"
        f"2. Calculate the exact mass of {cp['name']} that must be weighed on an analytical balance."
    )
    ans = f"{_fmt(m)} g"
    sol = (
        f"1. **Standard solution:** A solution of known concentration.\n\n"
        f"2. Required mass calculation:\n"
        f"   - $V = \\frac{{{_fmt(v_cm3)}}}{{1000}} = {_fmt(v_dm3)}\\text{{ dm}}^3$\n"
        f"   - Moles required: $n = c \\times V = {_fmt(c)} \\times {_fmt(v_dm3)} = {_fmt(n)}\\text{{ mol}}$\n"
        f"   - Mass required: $m = n \\times M = {_fmt(n)} \\times {_fmt(cp['M'])} = {_fmt(m)}\\text{{ g}}$\n"
        f"   (or $m = c \\cdot M \\cdot V = {_fmt(c)} \\times {_fmt(cp['M'])} \\times {_fmt(v_dm3)} = {_fmt(m)}\\text{{ g}}$)"
    )
    return _make_q(
        r, "37_mass_of_solute_required_for_standard_solution", 37, prompt, ans, sol, 4,
        ["standard_solution_mass_formula_inversion"],
        [{"step": 1, "criterion": "Definition: solution of known concentration", "marks": 1}, {"step": 2, "criterion": f"Convert V = {_fmt(v_dm3)} dm^3", "marks": 1}, {"step": 3, "criterion": "Formula m = c * M * V", "marks": 1}, {"step": 4, "criterion": f"Answer m = {_fmt(m)} g", "marks": 1}],
        {"tier_1": "Rearrange c = m / (M * V) to solve for mass: m = c * M * V.", "tier_2": "Ensure volume is in dm^3 by dividing cm^3 by 1000.", "tier_3": ans},
    )


# 38. Dilution of standard solutions c1v1 c2v2
def build_38_dilution_of_standard_solutions_c1v1_c2v2(r: random.Random) -> Dict[str, Any]:
    c1 = r.choice([1.0, 2.0, 3.0, 5.0])
    c2 = r.choice([0.1, 0.2, 0.25, 0.5])
    v2_cm3 = r.choice([250.0, 500.0, 1000.0])
    v1_cm3 = round((c2 * v2_cm3) / c1, 2)

    prompt = (
        f"A concentrated stock solution of hydrochloric acid has a concentration of **${_fmt(c1)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**.\n"
        f"A learner needs to prepare **${_fmt(v2_cm3)}\\text{{ cm}}^3$** of a diluted solution with concentration **${_fmt(c2)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**.\n\n"
        f"1. State the principle/formula used for diluting solutions without changing solute moles.\n"
        f"2. Calculate the volume of concentrated stock solution ($V_1$) in $\\text{{cm}}^3$ that must be measured."
    )
    ans = f"{_fmt(v1_cm3)} cm3"
    sol = (
        f"1. During dilution, the amount of solute in moles remains constant: $n_1 = n_2$.\n"
        f"   Therefore: $c_1 V_1 = c_2 V_2$.\n\n"
        f"2. Rearranging for $V_1$:\n"
        f"   $$V_1 = \\frac{{c_2 V_2}}{{c_1}} = \\frac{{{_fmt(c2)} \\times {_fmt(v2_cm3)}}}{{{_fmt(c1)}}} = {_fmt(v1_cm3)}\\text{{ cm}}^3$$"
    )
    return _make_q(
        r, "38_dilution_of_standard_solutions_c1v1_c2v2", 38, prompt, ans, sol, 3,
        ["inversion_of_dilution_formula"],
        [{"step": 1, "criterion": "Dilution principle c1V1 = c2V2", "marks": 1}, {"step": 2, "criterion": "Substitution of values", "marks": 1}, {"step": 3, "criterion": f"Answer V1 = {_fmt(v1_cm3)} cm^3", "marks": 1}],
        {"tier_1": "Use the dilution equation c1 * V1 = c2 * V2.", "tier_2": "Solve for V1 = (c2 * V2) / c1.", "tier_3": ans},
    )


# 39. Mole ratio interpretation from balanced equations
def build_39_mole_ratio_interpretation_from_balanced_equations(r: random.Random) -> Dict[str, Any]:
    reactions = [
        {"eq": r"\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \to 2\text{NH}_3(\text{g})", "r1": "N₂", "r2": "H₂", "p": "NH₃", "coef1": 1, "coef2": 3, "coef_p": 2, "n1": r.choice([2.0, 3.0, 5.0])},
        {"eq": r"2\text{H}_2(\text{g}) + \text{O}_2(\text{g}) \to 2\text{H}_2\text{O}(\text{g})", "r1": "O₂", "r2": "H₂", "p": "H₂O", "coef1": 1, "coef2": 2, "coef_p": 2, "n1": r.choice([1.5, 2.5, 4.0])},
        {"eq": r"2\text{SO}_2(\text{g}) + \text{O}_2(\text{g}) \to 2\text{SO}_3(\text{g})", "r1": "O₂", "r2": "SO₂", "p": "SO₃", "coef1": 1, "coef2": 2, "coef_p": 2, "n1": r.choice([0.8, 1.2, 2.0])},
    ]
    rx = r.choice(reactions)
    n_r2 = round(rx["n1"] * (rx["coef2"] / rx["coef1"]), 2)
    n_p = round(rx["n1"] * (rx["coef_p"] / rx["coef1"]), 2)

    prompt = (
        f"Consider the industrial synthesis reaction represented by the balanced chemical equation:\n\n"
        f"$${rx['eq']}$$\n\n"
        f"1. State the mole ratio between the reactants ${rx['r1']}$ and ${rx['r2']}$.\n"
        f"2. If **${_fmt(rx['n1'])}\\text{{ mol}}$** of ${rx['r1']}$ reacts completely, calculate the moles of ${rx['r2']}$ required.\n"
        f"3. Calculate the moles of ${rx['p']}$ produced."
    )
    ans = f"n({rx['r2']}) = {_fmt(n_r2)} mol, n({rx['p']}) = {_fmt(n_p)} mol"
    sol = (
        f"1. Stoichiometric mole ratio from balanced equation:\n"
        f"   $$n({rx['r1']}) : n({rx['r2']}) = {rx['coef1']} : {rx['coef2']}$$\n\n"
        f"2. Moles of ${rx['r2']}$ required:\n"
        f"   $$n({rx['r2']}) = {_fmt(rx['n1'])} \\times \\frac{{{rx['coef2']}}}{{{rx['coef1']}}} = {_fmt(n_r2)}\\text{{ mol}}$$\n\n"
        f"3. Moles of ${rx['p']}$ produced:\n"
        f"   $$n({rx['p']}) = {_fmt(rx['n1'])} \\times \\frac{{{rx['coef_p']}}}{{{rx['coef1']}}} = {_fmt(n_p)}\\text{{ mol}}$$"
    )
    return _make_q(
        r, "39_mole_ratio_interpretation_from_balanced_equations", 39, prompt, ans, sol, 3,
        ["stoichiometric_ratio_inversion"],
        [{"step": 1, "criterion": f"Mole ratio {rx['coef1']}:{rx['coef2']}", "marks": 1}, {"step": 2, "criterion": f"Moles of {rx['r2']} = {_fmt(n_r2)} mol", "marks": 1}, {"step": 3, "criterion": f"Moles of {rx['p']} = {_fmt(n_p)} mol", "marks": 1}],
        {"tier_1": "Look at the big stoichiometric coefficients in front of each formula.", "tier_2": "Multiply given moles by the ratio of required coefficient to given coefficient.", "tier_3": ans},
    )


# 40. Stoichiometric mass mass calculations basic
def build_40_stoichiometric_mass_mass_calculations_basic(r: random.Random) -> Dict[str, Any]:
    # 2Mg + O2 -> 2MgO
    m_mg = r.choice([2.4, 4.8, 7.2, 12.0, 24.0])
    M_mg = 24.3
    M_mgo = 40.3
    n_mg = round(m_mg / M_mg, 3)
    n_mgo = n_mg  # 2:2 = 1:1
    m_mgo = round(n_mgo * M_mgo, 2)

    prompt = (
        f"Magnesium burns in excess oxygen to produce magnesium oxide according to the equation:\n\n"
        f"$$2\\text{{Mg}}(\\text{{s}}) + \\text{{O}}_2(\\text{{g}}) \\to 2\\text{{MgO}}(\\text{{s}})$$\n\n"
        f"($M(\\text{{Mg}}) = 24{{,}}3\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $M(\\text{{MgO}}) = 40{{,}}3\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)\n\n"
        f"A sample of **${_fmt(m_mg)}\\text{{ g}}$** of magnesium is burned completely.\n"
        f"1. Calculate the number of moles of $\\text{{Mg}}$ that reacted.\n"
        f"2. Use the mole ratio to determine the moles of $\\text{{MgO}}$ formed.\n"
        f"3. Calculate the mass of $\\text{{MgO}}$ produced."
    )
    ans = f"{_fmt(m_mgo)} g"
    sol = (
        f"1. Moles of $\\text{{Mg}}$:\n"
        f"   $$n(\\text{{Mg}}) = \\frac{{m}}{{M}} = \\frac{{{_fmt(m_mg)}}}{{24{{,}}3}} = {_fmt(n_mg)}\\text{{ mol}}$$\n\n"
        f"2. Mole ratio from balanced equation:\n"
        f"   $$n(\\text{{Mg}}) : n(\\text{{MgO}}) = 2 : 2 = 1 : 1$$\n"
        f"   Therefore, $n(\\text{{MgO}}) = {_fmt(n_mgo)}\\text{{ mol}}$.\n\n"
        f"3. Mass of $\\text{{MgO}}$:\n"
        f"   $$m(\\text{{MgO}}) = n \\times M = {_fmt(n_mgo)} \\times 40{{,}}3 = {_fmt(m_mgo)}\\text{{ g}}$$"
    )
    return _make_q(
        r, "40_stoichiometric_mass_mass_calculations_basic", 40, prompt, ans, sol, 3,
        ["direct_mass_ratio_misconception"],
        [{"step": 1, "criterion": f"Calculate n(Mg) = {_fmt(n_mg)} mol", "marks": 1}, {"step": 2, "criterion": "Mole ratio 1:1 applied", "marks": 1}, {"step": 3, "criterion": f"Mass of MgO = {_fmt(m_mgo)} g", "marks": 1}],
        {"tier_1": "Never use masses directly in chemical equations; convert mass to moles first.", "tier_2": "Apply mole ratio, then multiply moles of product by product molar mass.", "tier_3": ans},
    )


# 41. Stoichiometric mass mass calculations two products
def build_41_stoichiometric_mass_mass_calculations_two_products(r: random.Random) -> Dict[str, Any]:
    # CaCO3(s) -> CaO(s) + CO2(g)
    m_caco3 = r.choice([25.0, 50.0, 100.0, 150.0, 200.0])
    M_caco3 = 100.1
    M_cao = 56.1
    M_co2 = 44.0

    n = round(m_caco3 / M_caco3, 3)
    m_cao = round(n * M_cao, 2)
    m_co2 = round(n * M_co2, 2)

    prompt = (
        f"Calcium carbonate decomposes on heating according to the balanced equation:\n\n"
        f"$$\\text{{CaCO}}_3(\\text{{s}}) \\xrightarrow{{\\Delta}} \\text{{CaO}}(\\text{{s}}) + \\text{{CO}}_2(\\text{{g}})$$\n\n"
        f"($M(\\text{{CaCO}}_3) = 100{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$M(\\text{{CaO}}) = 56{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$M(\\text{{CO}}_2) = 44{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)\n\n"
        f"A mass of **${_fmt(m_caco3)}\\text{{ g}}$** of $\\text{{CaCO}}_3$ decomposes completely.\n"
        f"1. Calculate the mass of calcium oxide ($\\text{{CaO}}$) formed.\n"
        f"2. Calculate the mass of carbon dioxide ($\\text{{CO}}_2$) formed.\n"
        f"3. Verify that the law of conservation of mass holds for these products."
    )
    ans = f"m(CaO) = {_fmt(m_cao)} g, m(CO2) = {_fmt(m_co2)} g"
    sol = (
        f"1. Moles of $\\text{{CaCO}}_3$:\n"
        f"   $$n = \\frac{{{_fmt(m_caco3)}}}{{100{{,}}1}} = {_fmt(n)}\\text{{ mol}}$$\n"
        f"   From $1:1$ mole ratio, $n(\\text{{CaO}}) = {_fmt(n)}\\text{{ mol}}$.\n"
        f"   $$m(\\text{{CaO}}) = {_fmt(n)} \\times 56{{,}}1 = {_fmt(m_cao)}\\text{{ g}}$$\n\n"
        f"2. From $1:1$ mole ratio, $n(\\text{{CO}}_2) = {_fmt(n)}\\text{{ mol}}$.\n"
        f"   $$m(\\text{{CO}}_2) = {_fmt(n)} \\times 44{{,}}0 = {_fmt(m_co2)}\\text{{ g}}$$\n\n"
        f"3. Verification:\n"
        f"   $$m(\\text{{products}}) = {_fmt(m_cao)} + {_fmt(m_co2)} = {_fmt(round(m_cao + m_co2, 1))}\\text{{ g}} \\approx {_fmt(m_caco3)}\\text{{ g}}$$\n"
        f"   Mass of reactants equals total mass of products."
    )
    return _make_q(
        r, "41_stoichiometric_mass_mass_calculations_two_products", 41, prompt, ans, sol, 4,
        ["conservation_of_mass_neglect"],
        [{"step": 1, "criterion": f"Calculate n = {_fmt(n)} mol", "marks": 1}, {"step": 2, "criterion": f"Mass of CaO = {_fmt(m_cao)} g", "marks": 1}, {"step": 3, "criterion": f"Mass of CO2 = {_fmt(m_co2)} g", "marks": 1}, {"step": 4, "criterion": "Verification of conservation of mass", "marks": 1}],
        {"tier_1": "Calculate moles of CaCO3 first, then use 1:1 mole ratio for each product.", "tier_2": "Sum of masses of CaO and CO2 must equal the initial mass of CaCO3.", "tier_3": ans},
    )


# 42. Stoichiometric mass to gas volume at stp (with SVG)
def build_42_stoichiometric_mass_to_gas_volume_at_stp(r: random.Random) -> Dict[str, Any]:
    # Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)
    m_mg = r.choice([0.12, 0.24, 0.48, 0.72, 0.06])
    M_mg = 24.3
    n_mg = round(m_mg / M_mg, 4)
    n_h2 = n_mg
    v_h2_dm3 = round(n_h2 * VM_STP, 3)
    v_h2_cm3 = round(v_h2_dm3 * 1000.0, 1)

    svg = _svg_gas_syringe(v_h2_cm3, "Mg", "H₂")
    prompt = (
        f"Refer to the gas collection apparatus showing a reaction between magnesium ribbon and dilute hydrochloric acid:\n\n"
        f"$$\\text{{Mg}}(\\text{{s}}) + 2\\text{{HCl}}(\\text{{aq}}) \\to \\text{{MgCl}}_2(\\text{{aq}}) + \\text{{H}}_2(\\text{{g}})$$\n\n"
        f"($M(\\text{{Mg}}) = 24{{,}}3\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$ at STP)\n\n"
        f"A piece of magnesium of mass **${_fmt(m_mg)}\\text{{ g}}$** reacts completely with excess $\\text{{HCl}}$.\n"
        f"1. Calculate the number of moles of $\\text{{Mg}}$ reacted.\n"
        f"2. Calculate the volume of hydrogen gas, $\\text{{H}}_2(\\text{{g}})$, collected in the syringe at STP in $\\text{{cm}}^3$."
    )
    ans = f"{_fmt(v_h2_cm3)} cm3"
    sol = (
        f"1. Moles of $\\text{{Mg}}$:\n"
        f"   $$n(\\text{{Mg}}) = \\frac{{{_fmt(m_mg)}}}{{24{{,}}3}} = {_fmt(n_mg, 4)}\\text{{ mol}}$$\n\n"
        f"2. From the equation, $n(\\text{{H}}_2) : n(\\text{{Mg}}) = 1 : 1$.\n"
        f"   Therefore, $n(\\text{{H}}_2) = {_fmt(n_h2, 4)}\\text{{ mol}}$.\n\n"
        f"3. Volume of $\\text{{H}}_2$ at STP:\n"
        f"   $$V = n \\times V_m = {_fmt(n_h2, 4)} \\times 22{{,}}4 = {_fmt(v_h2_dm3, 3)}\\text{{ dm}}^3$$\n"
        f"   Convert to $\\text{{cm}}^3$:\n"
        f"   $$V = {_fmt(v_h2_dm3, 3)} \\times 1000 = {_fmt(v_h2_cm3)}\\text{{ cm}}^3$$"
    )
    return _make_q(
        r, "42_stoichiometric_mass_to_gas_volume_at_stp", 42, prompt, ans, sol, 4,
        ["gas_volume_unit_conversion_error", "forgot_stp_molar_volume_22_4"],
        [{"step": 1, "criterion": f"Calculate n(Mg) = {_fmt(n_mg, 4)} mol", "marks": 1}, {"step": 2, "criterion": "Mole ratio 1:1 applied", "marks": 1}, {"step": 3, "criterion": f"Calculate V in dm^3 = {_fmt(v_h2_dm3, 3)} dm^3", "marks": 1}, {"step": 4, "criterion": f"Convert to cm^3 = {_fmt(v_h2_cm3)} cm^3", "marks": 1}],
        {"tier_1": "Calculate moles of Mg, use 1:1 mole ratio for H2, then multiply by 22,4 dm^3/mol.", "tier_2": "Remember to multiply by 1000 to convert dm^3 to cm^3.", "tier_3": ans},
        svg=svg,
    )


# 43. Stoichiometric solution volume to mass
def build_43_stoichiometric_solution_volume_to_mass(r: random.Random) -> Dict[str, Any]:
    # Zn(s) + 2HCl(aq) -> ZnCl2(aq) + H2(g)
    v_cm3 = r.choice([25.0, 50.0, 75.0, 100.0])
    c_hcl = r.choice([0.5, 1.0, 1.5, 2.0])
    v_dm3 = v_cm3 / 1000.0
    n_hcl = round(c_hcl * v_dm3, 4)
    n_zn = round(n_hcl / 2.0, 4)
    M_zn = 65.4
    m_zn = round(n_zn * M_zn, 2)

    prompt = (
        f"Zinc reacts with dilute hydrochloric acid according to:\n\n"
        f"$$\\text{{Zn}}(\\text{{s}}) + 2\\text{{HCl}}(\\text{{aq}}) \\to \\text{{ZnCl}}_2(\\text{{aq}}) + \\text{{H}}_2(\\text{{g}})$$\n\n"
        f"($M(\\text{{Zn}}) = 65{{,}}4\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)\n\n"
        f"Exactly **${_fmt(v_cm3)}\\text{{ cm}}^3$** of a **${_fmt(c_hcl)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** $\\text{{HCl}}$ solution reacts completely.\n"
        f"1. Calculate the number of moles of $\\text{{HCl}}$ reacted.\n"
        f"2. Use the mole ratio to find the moles of $\\text{{Zn}}$ consumed.\n"
        f"3. Calculate the mass of zinc consumed in the reaction."
    )
    ans = f"{_fmt(m_zn)} g"
    sol = (
        f"1. Moles of $\\text{{HCl}}$:\n"
        f"   $$n(\\text{{HCl}}) = c \\times V = {_fmt(c_hcl)} \\times \\frac{{{_fmt(v_cm3)}}}{{1000}} = {_fmt(n_hcl, 4)}\\text{{ mol}}$$\n\n"
        f"2. Stoichiometric mole ratio:\n"
        f"   $$n(\\text{{Zn}}) : n(\\text{{HCl}}) = 1 : 2$$\n"
        f"   $$n(\\text{{Zn}}) = \\frac{{{_fmt(n_hcl, 4)}}}{{2}} = {_fmt(n_zn, 4)}\\text{{ mol}}$$\n\n"
        f"3. Mass of zinc:\n"
        f"   $$m(\\text{{Zn}}) = n \\times M = {_fmt(n_zn, 4)} \\times 65{{,}}4 = {_fmt(m_zn)}\\text{{ g}}$$"
    )
    return _make_q(
        r, "43_stoichiometric_solution_volume_to_mass", 43, prompt, ans, sol, 3,
        ["stoichiometric_ratio_inversion"],
        [{"step": 1, "criterion": f"Calculate n(HCl) = {_fmt(n_hcl, 4)} mol", "marks": 1}, {"step": 2, "criterion": f"Mole ratio 1:2 -> n(Zn) = {_fmt(n_zn, 4)} mol", "marks": 1}, {"step": 3, "criterion": f"Mass of Zn = {_fmt(m_zn)} g", "marks": 1}],
        {"tier_1": "Calculate moles of acid using n = c * V.", "tier_2": "Note the 1:2 ratio: moles of Zn is half the moles of HCl.", "tier_3": ans},
    )


# 44. Stoichiometric solution neutralisation titration (with SVG)
def build_44_stoichiometric_solution_neutralisation_titration(r: random.Random) -> Dict[str, Any]:
    # HCl + NaOH -> NaCl + H2O
    v_base = 25.0
    c_base = r.choice([0.10, 0.15, 0.20, 0.25])
    v_acid = r.choice([18.5, 20.0, 22.4, 25.0, 28.0])
    # c_a * V_a / (c_b * V_b) = 1/1 => c_a = c_b * V_b / V_a
    c_acid = round((c_base * v_base) / v_acid, 3)

    svg = _svg_titration(v_acid, "HCl", "NaOH")
    prompt = (
        f"Refer to the titration apparatus showing the neutralisation of **${_fmt(v_base)}\\text{{ cm}}^3$** "
        f"of a standard sodium hydroxide solution ($\\text{{NaOH}}$) of concentration **${_fmt(c_base)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**:\n\n"
        f"$$\\text{{HCl}}(\\text{{aq}}) + \\text{{NaOH}}(\\text{{aq}}) \\to \\text{{NaCl}}(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}})$$\n\n"
        f"The end-point is reached when **${_fmt(v_acid)}\\text{{ cm}}^3$** of hydrochloric acid ($\\text{{HCl}}$) has been added from the burette.\n\n"
        f"1. State the formula for titration calculations relating acid and base: $\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{n_a}}{{n_b}}$.\n"
        f"2. Calculate the concentration of the hydrochloric acid solution ($c_a$) in $\\text{{mol}}\\cdot\\text{{dm}}^{{-3}}$."
    )
    ans = f"{_fmt(c_acid)} mol/dm3"
    sol = (
        f"1. Balanced equation mole ratio: $n_a : n_b = 1 : 1$.\n\n"
        f"2. Titration formula calculation:\n"
        f"   $$\\frac{{c_a \\times V_a}}{{c_b \\times V_b}} = \\frac{{1}}{{1}}$$\n"
        f"   $$c_a = \\frac{{c_b \\times V_b}}{{V_a}} = \\frac{{{_fmt(c_base)} \\times {_fmt(v_base)}}}{{{_fmt(v_acid)}}} = {_fmt(c_acid)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$"
    )
    return _make_q(
        r, "44_stoichiometric_solution_neutralisation_titration", 44, prompt, ans, sol, 3,
        ["titration_formula_acid_base_inversion"],
        [{"step": 1, "criterion": "Formula caVa/cbVb = na/nb", "marks": 1}, {"step": 2, "criterion": "Correct substitution of known values", "marks": 1}, {"step": 3, "criterion": f"Answer ca = {_fmt(c_acid)} mol/dm^3", "marks": 1}],
        {"tier_1": "Use the formula (ca * Va) / (cb * Vb) = na / nb.", "tier_2": "Because the mole ratio is 1:1, ca = (cb * Vb) / Va.", "tier_3": ans},
        svg=svg,
    )


# 45. Limiting reactant determination from initial moles
def build_45_limiting_reactant_determination_from_initial_moles(r: random.Random) -> Dict[str, Any]:
    # 2H2 + O2 -> 2H2O
    pairs = [
        {"n_h2": 4.0, "n_o2": 1.5, "limiting": "O₂", "excess": "H₂", "req_h2": 3.0},
        {"n_h2": 3.0, "n_o2": 2.0, "limiting": "H₂", "excess": "O₂", "req_o2": 1.5},
        {"n_h2": 5.0, "n_o2": 3.0, "limiting": "H₂", "excess": "O₂", "req_o2": 2.5},
        {"n_h2": 6.0, "n_o2": 2.0, "limiting": "O₂", "excess": "H₂", "req_h2": 4.0},
    ]
    p = r.choice(pairs)
    prompt = (
        f"Hydrogen gas reacts with oxygen gas according to the balanced equation:\n\n"
        f"$$2\\text{{H}}_2(\\text{{g}}) + \\text{{O}}_2(\\text{{g}}) \\to 2\\text{{H}}_2\\text{{O}}(\\text{{g}})$$\n\n"
        f"A reaction vessel initially contains **${_fmt(p['n_h2'])}\\text{{ mol}}$** of $\\text{{H}}_2$ "
        f"and **${_fmt(p['n_o2'])}\\text{{ mol}}$** of $\\text{{O}}_2$.\n\n"
        f"1. Define the term *limiting reactant*.\n"
        f"2. Determine which reactant is the limiting reactant through clear mole comparison."
    )
    ans = f"{p['limiting']}"
    if p["limiting"] == "O₂":
        expl = (
            f"From the equation, $1\\text{{ mol of }}\\text{{O}}_2$ requires $2\\text{{ mol of }}\\text{{H}}_2$.\n"
            f"For ${_fmt(p['n_o2'])}\\text{{ mol of }}\\text{{O}}_2$, we need: "
            f"${_fmt(p['n_o2'])} \\times 2 = {_fmt(p['req_h2'])}\\text{{ mol of }}\\text{{H}}_2$.\n"
            f"We have ${_fmt(p['n_h2'])}\\text{{ mol of }}\\text{{H}}_2$ (which is more than required).\n"
            f"Therefore, $\\text{{O}}_2$ will be completely consumed first: **limiting reactant is {p['limiting']}**."
        )
    else:
        expl = (
            f"From the equation, $2\\text{{ mol of }}\\text{{H}}_2$ requires $1\\text{{ mol of }}\\text{{O}}_2$.\n"
            f"For ${_fmt(p['n_h2'])}\\text{{ mol of }}\\text{{H}}_2$, we need: "
            f"$\\frac{{{_fmt(p['n_h2'])}}}{{2}} = {_fmt(p['req_o2'])}\\text{{ mol of }}\\text{{O}}_2$.\n"
            f"We have ${_fmt(p['n_o2'])}\\text{{ mol of }}\\text{{O}}_2$ (which is more than required).\n"
            f"Therefore, $\\text{{H}}_2$ is completely consumed first: **limiting reactant is {p['limiting']}**."
        )
    sol = f"1. **Limiting reactant:** The reactant that is completely consumed during a reaction and determines the amount of product formed.\n\n2. **Mole comparison:**\n{expl}"
    return _make_q(
        r, "45_limiting_reactant_determination_from_initial_moles", 45, prompt, ans, sol, 3,
        ["limiting_reactant_determined_by_smaller_mass_or_moles_alone"],
        [{"step": 1, "criterion": "Definition of limiting reactant", "marks": 1}, {"step": 2, "criterion": "Mole ratio comparison shown", "marks": 1}, {"step": 3, "criterion": f"Identified limiting reactant: {p['limiting']}", "marks": 1}],
        {"tier_1": "The limiting reactant is NOT simply the one with fewer moles; compare required moles using the balanced equation.", "tier_2": "Divide each reactant's moles by its stoichiometric coefficient; the smaller value is limiting.", "tier_3": ans},
    )


# 46. Limiting reactant from initial masses of both reactants
def build_46_limiting_reactant_from_initial_masses_of_both_reactants(r: random.Random) -> Dict[str, Any]:
    # 2Al + 3Cl2 -> 2AlCl3
    # M(Al) = 27.0 g/mol, M(Cl2) = 71.0 g/mol, M(AlCl3) = 133.5 g/mol
    m_al = r.choice([5.4, 10.8, 27.0])
    m_cl2 = r.choice([14.2, 21.3, 71.0, 35.5])
    M_al = 27.0
    M_cl2 = 71.0
    M_alcl3 = 133.5

    n_al = round(m_al / M_al, 3)
    n_cl2 = round(m_cl2 / M_cl2, 3)

    # 2 mol Al needs 3 mol Cl2 -> ratio n_al / 2 vs n_cl2 / 3
    val_al = n_al / 2.0
    val_cl2 = n_cl2 / 3.0

    if val_al < val_cl2:
        limiting = "Al"
        n_prod = n_al  # 2:2
        m_prod = round(n_prod * M_alcl3, 2)
    else:
        limiting = "Cl₂"
        n_prod = round(n_cl2 * (2.0 / 3.0), 3)
        m_prod = round(n_prod * M_alcl3, 2)

    prompt = (
        f"Aluminum reacts vigorously with chlorine gas according to:\n\n"
        f"$$2\\text{{Al}}(\\text{{s}}) + 3\\text{{Cl}}_2(\\text{{g}}) \\to 2\\text{{AlCl}}_3(\\text{{s}})$$\n\n"
        f"($M(\\text{{Al}}) = 27{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$M(\\text{{Cl}}_2) = 71{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, "
        f"$M(\\text{{AlCl}}_3) = 133{{,}}5\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)\n\n"
        f"A chemist mixes **${_fmt(m_al)}\\text{{ g}}$** of $\\text{{Al}}$ with **${_fmt(m_cl2)}\\text{{ g}}$** of $\\text{{Cl}}_2$.\n"
        f"1. Calculate the initial moles of $\\text{{Al}}$ and $\\text{{Cl}}_2$.\n"
        f"2. Determine the limiting reactant.\n"
        f"3. Calculate the theoretical mass of aluminum chloride ($\\text{{AlCl}}_3$) produced."
    )
    ans = f"Limiting: {limiting}, Mass: {_fmt(m_prod)} g"
    sol = (
        f"1. Initial moles:\n"
        f"   - $n(\\text{{Al}}) = \\frac{{{_fmt(m_al)}}}{{27{{,}}0}} = {_fmt(n_al)}\\text{{ mol}}$\n"
        f"   - $n(\\text{{Cl}}_2) = \\frac{{{_fmt(m_cl2)}}}{{71{{,}}0}} = {_fmt(n_cl2)}\\text{{ mol}}$\n\n"
        f"2. Limiting reactant test (moles / coefficient):\n"
        f"   - $\\text{{Al}}: \\frac{{{_fmt(n_al)}}}{{2}} = {_fmt(val_al, 3)}$\n"
        f"   - $\\text{{Cl}}_2: \\frac{{{_fmt(n_cl2)}}}{{3}} = {_fmt(val_cl2, 3)}$\n"
        f"   Since the smaller ratio belongs to **{limiting}**, **{limiting} is the limiting reactant**.\n\n"
        f"3. Maximum mass of $\\text{{AlCl}}_3$ produced:\n"
        f"   $$n(\\text{{AlCl}}_3) = {_fmt(n_prod)}\\text{{ mol}}$$\n"
        f"   $$m(\\text{{AlCl}}_3) = {_fmt(n_prod)} \\times 133{{,}}5 = {_fmt(m_prod)}\\text{{ g}}$$"
    )
    return _make_q(
        r, "46_limiting_reactant_from_initial_masses_of_both_reactants", 46, prompt, ans, sol, 5,
        ["choosing_limiting_reactant_from_raw_mass"],
        [{"step": 1, "criterion": "Moles of both reactants calculated", "marks": 2}, {"step": 2, "criterion": f"Limiting reactant identified as {limiting}", "marks": 1}, {"step": 3, "criterion": "Moles of product based on limiting reactant", "marks": 1}, {"step": 4, "criterion": f"Theoretical mass = {_fmt(m_prod)} g", "marks": 1}],
        {"tier_1": "Convert both masses into moles before doing any comparison.", "tier_2": "Divide each mole value by its stoichiometric coefficient to identify the limiting reactant.", "tier_3": ans},
    )


# 47. Mass of excess reactant remaining unreacted
def build_47_mass_of_excess_reactant_remaining_unreacted(r: random.Random) -> Dict[str, Any]:
    # 2H2 + O2 -> 2H2O
    # H2 is limiting: e.g. 4.0 g H2 and 40.0 g O2
    # M(H2) = 2.0 g/mol, M(O2) = 32.0 g/mol
    m_h2 = r.choice([2.0, 4.0, 6.0, 8.0])
    m_o2 = r.choice([48.0, 64.0, 80.0, 96.0])
    n_h2 = m_h2 / 2.0
    n_o2_initial = m_o2 / 32.0

    # 2 mol H2 consumes 1 mol O2
    n_o2_used = n_h2 / 2.0
    n_o2_excess = round(n_o2_initial - n_o2_used, 3)
    m_o2_excess = round(n_o2_excess * 32.0, 2)

    prompt = (
        f"A mixture of **${_fmt(m_h2)}\\text{{ g}}$** of hydrogen gas ($\\text{{H}}_2$) "
        f"and **${_fmt(m_o2)}\\text{{ g}}$** of oxygen gas ($\\text{{O}}_2$) is ignited in a sealed container:\n\n"
        f"$$2\\text{{H}}_2(\\text{{g}}) + \\text{{O}}_2(\\text{{g}}) \\to 2\\text{{H}}_2\\text{{O}}(\\text{{l}})$$\n\n"
        f"($M(\\text{{H}}_2) = 2{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $M(\\text{{O}}_2) = 32{{,}}0\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)\n\n"
        f"1. Identify the excess reactant.\n"
        f"2. Calculate the number of moles of the excess reactant that reacted.\n"
        f"3. Calculate the mass of the excess reactant remaining unreacted after the reaction is complete."
    )
    ans = f"{_fmt(m_o2_excess)} g of O2"
    sol = (
        f"1. Initial moles:\n"
        f"   - $n(\\text{{H}}_2) = \\frac{{{_fmt(m_h2)}}}{{2{{,}}0}} = {_fmt(n_h2)}\\text{{ mol}}$\n"
        f"   - $n(\\text{{O}}_2) = \\frac{{{_fmt(m_o2)}}}{{32{{,}}0}} = {_fmt(n_o2_initial)}\\text{{ mol}}$\n"
        f"   Since $2\\text{{ mol of }}\\text{{H}}_2$ needs $1\\text{{ mol of }}\\text{{O}}_2$, "
        f"${_fmt(n_h2)}\\text{{ mol of }}\\text{{H}}_2$ needs $\\frac{{{_fmt(n_h2)}}}{{2}} = {_fmt(n_o2_used)}\\text{{ mol of }}\\text{{O}}_2$.\n"
        f"   We have ${_fmt(n_o2_initial)}\\text{{ mol of }}\\text{{O}}_2$, so **$\\text{{O}}_2$ is in excess**.\n\n"
        f"2. Moles of $\\text{{O}}_2$ consumed: **${_fmt(n_o2_used)}\\text{{ mol}}$**.\n\n"
        f"3. Moles of $\\text{{O}}_2$ remaining:\n"
        f"   $$n_{{\\text{{excess}}}} = {_fmt(n_o2_initial)} - {_fmt(n_o2_used)} = {_fmt(n_o2_excess)}\\text{{ mol}}$$\n"
        f"   Mass remaining unreacted:\n"
        f"   $$m = {_fmt(n_o2_excess)} \\times 32{{,}}0 = {_fmt(m_o2_excess)}\\text{{ g}}$$"
    )
    return _make_q(
        r, "47_mass_of_excess_reactant_remaining_unreacted", 47, prompt, ans, sol, 4,
        ["excess_reactant_mass_subtraction_before_moles"],
        [{"step": 1, "criterion": "Identified excess reactant as O2", "marks": 1}, {"step": 2, "criterion": f"Moles reacted = {_fmt(n_o2_used)} mol", "marks": 1}, {"step": 3, "criterion": f"Moles remaining = {_fmt(n_o2_excess)} mol", "marks": 1}, {"step": 4, "criterion": f"Mass remaining = {_fmt(m_o2_excess)} g", "marks": 1}],
        {"tier_1": "Determine how many moles of the excess reactant are actually used up by the limiting reactant.", "tier_2": "Subtract used moles from initial moles, then multiply by molar mass.", "tier_3": ans},
    )


# 48. Theoretical yield and actual yield percentage
def build_48_theoretical_yield_and_actual_yield_percentage(r: random.Random) -> Dict[str, Any]:
    # Theoretical yield calculated, actual yield given
    theo = r.choice([15.0, 20.0, 25.0, 40.0, 50.0])
    pct_yield = r.choice([75.0, 80.0, 85.0, 90.0, 68.0])
    actual = round((pct_yield / 100.0) * theo, 2)

    prompt = (
        f"In a chemical synthesis of aspirin, the stoichiometric calculation predicts a theoretical yield "
        f"of **${_fmt(theo)}\\text{{ g}}$**.\n"
        f"After completing the synthesis, purification, and drying, the learner isolates **${_fmt(actual)}\\text{{ g}}$** of pure product.\n\n"
        f"1. Define the term *percentage yield*.\n"
        f"2. Calculate the percentage yield of the reaction.\n"
        f"3. State two realistic practical reasons why the actual yield in a laboratory experiment is often less than 100%."
    )
    ans = f"{_fmt(pct_yield)}%"
    sol = (
        f"1. **Percentage yield:** The ratio of the actual yield to the theoretical yield, expressed as a percentage:\n"
        f"   $$\\%\\text{{ yield}} = \\frac{{\\text{{actual yield}}}}{{\\text{{theoretical yield}}}} \\times 100\\%$$\n\n"
        f"2. Calculation:\n"
        f"   $$\\%\\text{{ yield}} = \\frac{{{_fmt(actual)}}}{{{_fmt(theo)}}} \\times 100\\% = {_fmt(pct_yield)}\\%$$\n\n"
        f"3. Practical reasons for loss of yield:\n"
        f"   - Incomplete reaction (reaction reaches equilibrium or does not go to 100% completion).\n"
        f"   - Mechanical loss during filtration, transfer between beakers, or recrystallisation.\n"
        f"   - Formation of unwanted side products through competing side reactions."
    )
    return _make_q(
        r, "48_theoretical_yield_and_actual_yield_percentage", 48, prompt, ans, sol, 4,
        ["inverting_percentage_yield_formula"],
        [{"step": 1, "criterion": "Definition of percentage yield", "marks": 1}, {"step": 2, "criterion": f"Calculation giving {_fmt(pct_yield)}%", "marks": 2}, {"step": 3, "criterion": "Two valid practical reasons for yield loss", "marks": 1}],
        {"tier_1": "Percentage yield = (actual yield / theoretical yield) * 100%.", "tier_2": "Actual yield is what was weighed in the lab; theoretical is what stoichiometry predicted.", "tier_3": ans},
    )


# 49. Percentage purity of impure reactant sample
def build_49_percentage_purity_of_impure_reactant_sample(r: random.Random) -> Dict[str, Any]:
    # Impure CaCO3 sample decomposing or reacting with acid
    # CaCO3 -> CaO + CO2
    # CO2 collected at STP
    v_co2_dm3 = r.choice([2.24, 4.48, 1.12, 3.36])
    n_co2 = round(v_co2_dm3 / VM_STP, 3)
    # n_caco3 = n_co2
    m_pure_caco3 = round(n_co2 * 100.1, 2)
    # Sample mass must be greater than m_pure
    purity_pct = r.choice([80.0, 85.0, 90.0, 75.0])
    m_sample = round(m_pure_caco3 / (purity_pct / 100.0), 2)
    actual_purity = round((m_pure_caco3 / m_sample) * 100.0, 1)

    prompt = (
        f"A sample of impure limestone ($\text{{CaCO}}_3$) with a mass of **${_fmt(m_sample)}\\text{{ g}}$** "
        f"reacts completely with excess dilute hydrochloric acid:\n\n"
        f"$$\\text{{CaCO}}_3(\\text{{s}}) + 2\\text{{HCl}}(\\text{{aq}}) \\to \\text{{CaCl}}_2(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}}) + \\text{{CO}}_2(\\text{{g}})$$\n\n"
        f"($M(\\text{{CaCO}}_3) = 100{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$, $V_m = 22{{,}}4\\text{{ dm}}^3\\cdot\\text{{mol}}^{{-1}}$ at STP)\n\n"
        f"The volume of $\\text{{CO}}_2(\\text{{g}})$ collected at STP is **${_fmt(v_co2_dm3)}\\text{{ dm}}^3$**.\n"
        f"1. Calculate the number of moles of $\\text{{CO}}_2(\\text{{g}})$ produced.\n"
        f"2. Determine the mass of pure $\\text{{CaCO}}_3$ present in the limestone sample.\n"
        f"3. Calculate the percentage purity of the limestone sample."
    )
    ans = f"{_fmt(actual_purity)}%"
    sol = (
        f"1. Moles of $\\text{{CO}}_2$:\n"
        f"   $$n(\\text{{CO}}_2) = \\frac{{V}}{{V_m}} = \\frac{{{_fmt(v_co2_dm3)}}}{{22{{,}}4}} = {_fmt(n_co2)}\\text{{ mol}}$$\n\n"
        f"2. Mass of pure $\\text{{CaCO}}_3$:\n"
        f"   Mole ratio: $n(\\text{{CaCO}}_3) : n(\\text{{CO}}_2) = 1 : 1$.\n"
        f"   $$n(\\text{{CaCO}}_3) = {_fmt(n_co2)}\\text{{ mol}}$$\n"
        f"   $$m(\\text{{pure }}\\text{{CaCO}}_3) = {_fmt(n_co2)} \\times 100{{,}}1 = {_fmt(m_pure_caco3)}\\text{{ g}}$$\n\n"
        f"3. Percentage purity:\n"
        f"   $$\\%\\text{{ purity}} = \\frac{{m_{{\\text{{pure}}}}}}{{m_{{\\text{{sample}}}}}} \\times 100\\% = \\frac{{{_fmt(m_pure_caco3)}}}{{{_fmt(m_sample)}}} \\times 100\\% = {_fmt(actual_purity)}\\%$$"
    )
    return _make_q(
        r, "49_percentage_purity_of_impure_reactant_sample", 49, prompt, ans, sol, 4,
        ["percentage_purity_inverted_ratio", "used_impure_sample_mass_in_mole_formula"],
        [{"step": 1, "criterion": f"Calculate n(CO2) = {_fmt(n_co2)} mol", "marks": 1}, {"step": 2, "criterion": f"Pure mass = {_fmt(m_pure_caco3)} g", "marks": 1}, {"step": 3, "criterion": "Formula % purity = (m_pure / m_sample) * 100%", "marks": 1}, {"step": 4, "criterion": f"Answer % purity = {_fmt(actual_purity)}%", "marks": 1}],
        {"tier_1": "Never calculate moles using the impure sample mass; find moles of pure reactant from the gas product.", "tier_2": "% purity = (mass of pure substance / total mass of impure sample) * 100%.", "tier_3": ans},
    )


# 50. Stoichiometry and quantitative chemistry diagnostic autopsy
def build_50_stoichiometry_and_quantitative_chemistry_diagnostic_autopsy(r: random.Random) -> Dict[str, Any]:
    errors = [
        (
            "Direct mass ratio misconception instead of mole ratio",
            "A learner is asked how much magnesium oxide is produced from 24 g of Mg in 2Mg + O2 -> 2MgO. The learner writes: 'Because the ratio is 2 : 2, 24 g of Mg must form 24 g of MgO.'",
            "Chemical equations state ratios of *moles* (particles), NOT ratios of *masses*. Different substances have different molar masses. 24 g of Mg is 1 mol of Mg, which produces 1 mol of MgO. Since M(MgO) = 40,3 g/mol, the mass formed is 40,3 g."
        ),
        (
            "Using gas molar volume formula for aqueous solution",
            "A learner calculates the moles of HCl in 250 cm^3 of 0,5 mol/dm^3 solution by writing: n = V / Vm = 0,25 / 22,4 = 0,011 mol.",
            "The formula n = V / Vm (Vm = 22,4 dm^3/mol) applies exclusively to gases at standard temperature and pressure (STP). For aqueous solutions, the correct formula is n = c * V = 0,5 * 0,25 = 0,125 mol."
        ),
        (
            "Determining limiting reactant from raw masses without moles",
            "In the reaction 2Al + 3Cl2 -> 2AlCl3, a learner mixes 54 g of Al and 71 g of Cl2. The learner concludes: '54 g is less than 71 g, so Al is the limiting reactant.'",
            "Limiting reactant cannot be judged from masses alone because substances have different molar masses and stoichiometric coefficients. 54 g of Al = 2 mol; 71 g of Cl2 = 1 mol. The equation requires 3 mol of Cl2 for 2 mol of Al. Therefore, Cl2 runs out first and is the limiting reactant."
        ),
    ]
    err_title, err_desc, correction = r.choice(errors)
    prompt = (
        f"**Diagnostic Autopsy:** Review the following learner error in quantitative chemistry:\n\n"
        f"**Error Description:** {err_desc}\n\n"
        f"1. State the fundamental chemistry misconception demonstrated by the learner.\n"
        f"2. Provide the scientifically correct calculation and state the underlying quantitative principle violated."
    )
    ans = f"{correction}"
    sol = f"**Misconception Analysis:** {err_title}.\n\n**Scientific Correction:** {correction}"
    return _make_q(
        r, "50_stoichiometry_and_quantitative_chemistry_diagnostic_autopsy", 50, prompt, ans, sol, 3,
        ["misconception_in_advanced_stoichiometry_application"],
        [{"step": 1, "criterion": f"Identified error: {err_title}", "marks": 1}, {"step": 2, "criterion": "Underlying scientific principle explained", "marks": 1}, {"step": 3, "criterion": "Corrected calculation provided", "marks": 1}],
        {"tier_1": "Carefully examine whether the learner treated mass as moles, confused gas laws with solutions, or compared masses instead of molar coefficients.", "tier_2": "State the correct formula and show the step-by-step resolution.", "tier_3": ans},
    )


ARCHETYPES_26_50 = {
    "26_empirical_formula_from_percentage_composition": build_26_empirical_formula_from_percentage_composition,
    "27_empirical_formula_from_combustion_or_synthesis_masses": build_27_empirical_formula_from_combustion_or_synthesis_masses,
    "28_molecular_formula_from_empirical_formula_and_molar_mass": build_28_molecular_formula_from_empirical_formula_and_molar_mass,
    "29_empirical_and_molecular_formula_combined_organic": build_29_empirical_and_molecular_formula_combined_organic,
    "30_molar_gas_volume_at_stp_volume_to_moles": build_30_molar_gas_volume_at_stp_volume_to_moles,
    "31_molar_gas_volume_at_stp_moles_to_volume": build_31_molar_gas_volume_at_stp_moles_to_volume,
    "32_gas_volume_at_stp_from_mass": build_32_gas_volume_at_stp_from_mass,
    "33_mass_of_gas_at_stp_from_volume": build_33_mass_of_gas_at_stp_from_volume,
    "34_unit_conversions_for_gas_volume_cm3_to_dm3": build_34_unit_conversions_for_gas_volume_cm3_to_dm3,
    "35_concentration_of_solution_moles_and_volume": build_35_concentration_of_solution_moles_and_volume,
    "36_concentration_of_solution_mass_molar_mass_volume": build_36_concentration_of_solution_mass_molar_mass_volume,
    "37_mass_of_solute_required_for_standard_solution": build_37_mass_of_solute_required_for_standard_solution,
    "38_dilution_of_standard_solutions_c1v1_c2v2": build_38_dilution_of_standard_solutions_c1v1_c2v2,
    "39_mole_ratio_interpretation_from_balanced_equations": build_39_mole_ratio_interpretation_from_balanced_equations,
    "40_stoichiometric_mass_mass_calculations_basic": build_40_stoichiometric_mass_mass_calculations_basic,
    "41_stoichiometric_mass_mass_calculations_two_products": build_41_stoichiometric_mass_mass_calculations_two_products,
    "42_stoichiometric_mass_to_gas_volume_at_stp": build_42_stoichiometric_mass_to_gas_volume_at_stp,
    "43_stoichiometric_solution_volume_to_mass": build_43_stoichiometric_solution_volume_to_mass,
    "44_stoichiometric_solution_neutralisation_titration": build_44_stoichiometric_solution_neutralisation_titration,
    "45_limiting_reactant_determination_from_initial_moles": build_45_limiting_reactant_determination_from_initial_moles,
    "46_limiting_reactant_from_initial_masses_of_both_reactants": build_46_limiting_reactant_from_initial_masses_of_both_reactants,
    "47_mass_of_excess_reactant_remaining_unreacted": build_47_mass_of_excess_reactant_remaining_unreacted,
    "48_theoretical_yield_and_actual_yield_percentage": build_48_theoretical_yield_and_actual_yield_percentage,
    "49_percentage_purity_of_impure_reactant_sample": build_49_percentage_purity_of_impure_reactant_sample,
    "50_stoichiometry_and_quantitative_chemistry_diagnostic_autopsy": build_50_stoichiometry_and_quantitative_chemistry_diagnostic_autopsy,
}

BUILDERS_26_50 = ARCHETYPES_26_50
