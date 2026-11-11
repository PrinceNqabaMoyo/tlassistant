"""Grade 12 Physical Sciences — Acids and Bases Generator.
Deterministic 6-pillar CAPS question generator covering Paper 2 (Chemistry Term 2):
- Arrhenius and Brønsted-Lowry theories: Proton donors and proton acceptors.
- Conjugate acid-base pairs & ampholytes (amphiprotic substances).
- Strong vs weak acids and bases, concentrated vs dilute.
- Auto-ionisation of water and pH calculations: Kw = [H3O+][OH-] = 1.0 x 10^-14, pH = -log[H3O+].
- Acid-base titrations: (ca * Va) / (cb * Vb) = na / nb, indicator selection.
- Salt hydrolysis: acidic, basic, and neutral salts.

Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


CONJUGATE_SYSTEMS = [
    {
        "equation": r"\text{NH}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_4^+(\text{aq}) + \text{OH}^-(\text{aq})",
        "acid_1": r"\text{H}_2\text{O}",
        "base_1": r"\text{OH}^-",
        "base_2": r"\text{NH}_3",
        "acid_2": r"\text{NH}_4^+",
        "ampholyte": r"\text{H}_2\text{O}",
    },
    {
        "equation": r"\text{CH}_3\text{COOH}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{CH}_3\text{COO}^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
        "acid_1": r"\text{CH}_3\text{COOH}",
        "base_1": r"\text{CH}_3\text{COO}^-",
        "base_2": r"\text{H}_2\text{O}",
        "acid_2": r"\text{H}_3\text{O}^+",
        "ampholyte": r"\text{H}_2\text{O}",
    },
    {
        "equation": r"\text{HCO}_3^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{CO}_3^{2-}(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
        "acid_1": r"\text{HCO}_3^-",
        "base_1": r"\text{CO}_3^{2-}",
        "base_2": r"\text{H}_2\text{O}",
        "acid_2": r"\text{H}_3\text{O}^+",
        "ampholyte": r"\text{HCO}_3^-",
    },
]

TITRATION_PAIRS = [
    {
        "acid": "Hydrochloric acid (HCl)",
        "acid_formula": r"\text{HCl}",
        "acid_protic": 1,
        "base": "Sodium hydroxide (NaOH)",
        "base_formula": r"\text{NaOH}",
        "base_protic": 1,
        "na": 1,
        "nb": 1,
        "type": "Strong acid - strong base",
        "indicator": "Bromothymol blue",
        "indicator_range": "pH 6,0 - 7,6 (green at equivalence)",
        "salt": "Sodium chloride (NaCl)",
        "salt_nature": "Neutral (pH = 7) because neither Na+ nor Cl- hydrolyses",
    },
    {
        "acid": "Sulphuric acid (H2SO4)",
        "acid_formula": r"\text{H}_2\text{SO}_4",
        "acid_protic": 2,
        "base": "Sodium hydroxide (NaOH)",
        "base_formula": r"\text{NaOH}",
        "base_protic": 1,
        "na": 1,
        "nb": 2,
        "type": "Strong diprotic acid - strong base",
        "indicator": "Bromothymol blue",
        "indicator_range": "pH 6,0 - 7,6",
        "salt": "Sodium sulphate (Na2SO4)",
        "salt_nature": "Neutral (pH = 7)",
    },
    {
        "acid": "Ethanoic acid (CH3COOH)",
        "acid_formula": r"\text{CH}_3\text{COOH}",
        "acid_protic": 1,
        "base": "Sodium hydroxide (NaOH)",
        "base_formula": r"\text{NaOH}",
        "base_protic": 1,
        "na": 1,
        "nb": 1,
        "type": "Weak acid - strong base",
        "indicator": "Phenolphthalein",
        "indicator_range": "pH 8,2 - 10,0 (faint pink at equivalence)",
        "salt": "Sodium ethanoate (CH3COONa)",
        "salt_nature": "Basic (pH > 7) due to anion hydrolysis: CH3COO- + H2O <-> CH3COOH + OH-",
    },
    {
        "acid": "Hydrochloric acid (HCl)",
        "acid_formula": r"\text{HCl}",
        "acid_protic": 1,
        "base": "Ammonia solution (NH3)",
        "base_formula": r"\text{NH}_3",
        "base_protic": 1,
        "na": 1,
        "nb": 1,
        "type": "Strong acid - weak base",
        "indicator": "Methyl orange",
        "indicator_range": "pH 3,1 - 4,4 (orange-yellow at equivalence)",
        "salt": "Ammonium chloride (NH4Cl)",
        "salt_nature": "Acidic (pH < 7) due to cation hydrolysis: NH4+ + H2O <-> NH3 + H3O+",
    },
]


def _build_definitions_conjugate_drill(r: random.Random) -> Dict[str, Any]:
    sys = r.choice(CONJUGATE_SYSTEMS)

    prompt = (
        f"Consider the acid-base equilibrium reaction below:\n\n"
        f"$${sys['equation']}$$\n\n"
        f"1. Define an **acid** according to the Brønsted-Lowry theory.\n"
        f"2. Identify the **two conjugate acid-base pairs** in this reaction.\n"
        f"3. Explain why ${sys['ampholyte']}$ can act as an **ampholyte** (amphiprotic substance)."
    )

    sol = (
        f"1. **Brønsted-Lowry acid:** A proton ($H^+$ ion) donor.\n"
        f"2. Conjugate acid-base pairs:\n"
        f"   - Pair 1: Acid: ${sys['acid_1']}$, Conjugate base: ${sys['base_1']}$\n"
        f"   - Pair 2: Base: ${sys['base_2']}$, Conjugate acid: ${sys['acid_2']}$\n"
        f"3. An ampholyte can act as either an acid (donating a proton) or a base (accepting a proton) depending on the reaction environment."
    )

    return {
        "id": f"g12_ps_ab_def_{r.randint(10000, 99999)}",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Pairs: ({sys['acid_1']}/{sys['base_1']}) and ({sys['acid_2']}/{sys['base_2']})",
        "worked_solution": sol,
        "sub_parts": [
            {
                "part": "1",
                "label": "1. Brønsted-Lowry acid definition",
                "prompt": "Define an acid according to the Brønsted-Lowry theory.",
                "expected_answer": "Proton donor",
                "marks": 1,
            },
            {
                "part": "2",
                "label": "2. Conjugate acid-base pairs",
                "prompt": "Identify the two conjugate acid-base pairs in this reaction.",
                "expected_answer": f"({sys['acid_1']}, {sys['base_1']}) and ({sys['acid_2']}, {sys['base_2']})",
                "marks": 2,
            },
            {
                "part": "3",
                "label": "3. Ampholyte property",
                "prompt": f"Explain why {sys['ampholyte']} can act as an ampholyte.",
                "expected_answer": "Acts as either an acid or a base",
                "marks": 2,
            },
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Proton (H+) donor", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Pair 1: {sys['acid_1']} and {sys['base_1']}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Pair 2: {sys['base_2']} and {sys['acid_2']}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Definition of ampholyte: acts as both acid and base", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Brønsted-Lowry: Acids DONATE protons; Bases ACCEPT protons.",
            "tier_2": "A conjugate pair differs by exactly one proton ($H^+$).",
            "tier_3": f"Pair 1: ${sys['acid_1']}$ / ${sys['base_1']}$. Pair 2: ${sys['acid_2']}$ / ${sys['base_2']}$.",
        },
        "misconception_tags": ["confused_conjugate_acid_and_base", "arrhenius_bronsted_confusion"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


def _build_ph_calc_drill(r: random.Random) -> Dict[str, Any]:
    acid_choice = r.choice(["HCl", "HNO3", "NaOH", "KOH", "H2SO4"])
    c = r.choice([0.01, 0.02, 0.05, 0.1, 0.15, 0.25, 0.5])

    if acid_choice in ["HCl", "HNO3"]:
        h3o = c
        ph = round(-math.log10(h3o), 2)
        prompt = (
            f"A standard aqueous solution of **{acid_choice}** has a concentration of **{_fmt_sa(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}** at $25^\\circ\\text{{C}}$.\n\n"
            f"1. Is {acid_choice} a strong or weak acid?\n"
            f"2. Write down the hydronium ion concentration $[\\text{{H}}_3\\text{{O}}^+]$.\n"
            f"3. Calculate the pH of the solution."
        )
        sol = (
            f"1. {acid_choice} is a **strong monoprotic acid** that ionises completely in water.\n"
            f"2. $[\\text{{H}}_3\\text{{O}}^+] = {_fmt_sa(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$\n"
            f"3. $\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = -\\log({_fmt_sa(h3o)}) = {_fmt_sa(ph)}$"
        )
    elif acid_choice == "H2SO4":
        h3o = 2 * c
        ph = round(-math.log10(h3o), 2)
        prompt = (
            f"A solution of sulphuric acid, $\\text{{H}}_2\\text{{SO}}_4$, has a concentration of **{_fmt_sa(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}** at $25^\\circ\\text{{C}}$.\n\n"
            f"Assuming complete ionisation of both protons, calculate the pH of the solution."
        )
        sol = (
            f"$\\text{{H}}_2\\text{{SO}}_4$ is a diprotic acid: each mole produces $2\\text{{ moles}}$ of $\\text{{H}}_3\\text{{O}}^+$.\n"
            f"$[\\text{{H}}_3\\text{{O}}^+] = 2 \\times c = 2 \\times {_fmt_sa(c)} = {_fmt_sa(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$\n"
            f"$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = -\\log({_fmt_sa(h3o)}) = {_fmt_sa(ph)}$"
        )
    else:
        oh = c
        h3o = 1.0e-14 / oh
        ph = round(-math.log10(h3o), 2)
        prompt = (
            f"A solution of potassium/sodium hydroxide, **{acid_choice}**, has a concentration of **{_fmt_sa(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}** at $25^\\circ\\text{{C}}$.\n\n"
            f"Given $K_w = [\\text{{H}}_3\\text{{O}}^+][\\text{{OH}}^-] = 1{{,}}0 \\times 10^{{-14}}$, calculate the pH of the basic solution."
        )
        sol = (
            f"{acid_choice} is a strong base that dissociates completely: $[\\text{{OH}}^-] = {_fmt_sa(oh)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.\n"
            f"$[\\text{{H}}_3\\text{{O}}^+] = \\frac{{K_w}}{{[\\text{{OH}}^-]}} = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sa(oh)}}} = {h3o:.2e}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$\n"
            f"$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = {_fmt_sa(ph)}$"
        )

    if acid_choice in ["HCl", "HNO3"]:
        sub_parts = [
            {"part": "1", "label": f"1. Strength of {acid_choice}", "prompt": f"Is {acid_choice} a strong or weak acid?", "expected_answer": "Strong", "marks": 1},
            {"part": "2", "label": "2. Hydronium [H3O+] conc.", "prompt": "Write down [H3O+] in mol/dm3.", "expected_answer": _fmt_sa(h3o), "marks": 1},
            {"part": "3", "label": "3. pH of solution", "prompt": "Calculate the pH of the solution.", "expected_answer": _fmt_sa(ph), "marks": 1},
        ]
    else:
        sub_parts = [
            {"part": "1", "label": "1. pH calculation", "prompt": "Calculate the pH of the solution.", "expected_answer": _fmt_sa(ph), "marks": 3}
        ]

    return {
        "id": f"g12_ps_ab_ph_{r.randint(10000, 99999)}",
        "type": "numeric" if len(sub_parts) == 1 else "compound",
        "prompt": prompt,
        "correct_answer": _fmt_sa(ph),
        "worked_solution": sol,
        "sub_parts": sub_parts,
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Determine [H3O+] from concentration", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: pH = -log[H3O+]", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Final pH = {_fmt_sa(ph)}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_diprotic_factor_h2so4", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Recall: $\\text{pH} = -\\log[\\text{H}_3\\text{O}^+]$.",
            "tier_2": "For bases, use $K_w = [\\text{H}_3\\text{O}^+][\\text{OH}^-] = 1{{,}}0 \\times 10^{-14}$ to find $[\\text{H}_3\\text{O}^+]$ first.",
            "tier_3": f"Calculation: pH = {_fmt_sa(ph)}.",
        },
        "misconception_tags": ["negative_log_sign_error", "forgot_diprotic_factor_h2so4"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


def _build_titration_drill(r: random.Random) -> Dict[str, Any]:
    pair = r.choice(TITRATION_PAIRS)
    ca = round(r.uniform(0.08, 0.25), 2)
    va = round(r.uniform(18.0, 30.0), 1)
    vb = round(r.choice([20.0, 25.0]), 1)

    # (ca * va) / (cb * vb) = na / nb  => cb = (ca * va * nb) / (vb * na)
    cb = round((ca * va * pair["nb"]) / (vb * pair["na"]), 3)

    prompt = (
        f"During a laboratory titration, **${_fmt_sa(va)}\\text{{ cm}}^3$** of **{pair['acid']}** of concentration "
        f"**${_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** is required to completely neutralise "
        f"**${_fmt_sa(vb)}\\text{{ cm}}^3$** of an aqueous solution of **{pair['base']}**.\n\n"
        f"1. Choose the most suitable indicator for this titration: **{pair['indicator']}** or **Phenolphthalein** / **Methyl orange**.\n"
        f"2. Explain your indicator choice based on the nature of the salt formed at equivalence.\n"
        f"3. Calculate the concentration of the {pair['base']} solution ($c_b$)."
    )

    sol = (
        f"1. Suitable indicator: **{pair['indicator']}**\n"
        f"2. Reason: This is a {pair['type']} titration. The salt formed, {pair['salt']}, is {pair['salt_nature']}. "
        f"The pH at equivalence falls within the range of {pair['indicator']} ({pair['indicator_range']}).\n"
        f"3. Concentration calculation:\n"
        f"   $\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{n_a}}{{n_b}}$\n"
        f"   $\\frac{{{_fmt_sa(ca)} \\times {_fmt_sa(va)}}}{{c_b \\times {_fmt_sa(vb)}}} = \\frac{{{pair['na']}}}{{{pair['nb']}}}$\n"
        f"   $c_b = \\frac{{{_fmt_sa(ca)} \\times {_fmt_sa(va)} \\times {pair['nb']}}}{{{_fmt_sa(vb)} \\times {pair['na']}}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$"
    )

    return {
        "id": f"g12_ps_ab_titr_{r.randint(10000, 99999)}",
        "type": "compound",
        "modality": "bio_diagram",
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin_letter") or locals().get("target_pin") else "context",
            "image_type": "titration_apparatus",
            "burette_sol": f"{pair['acid']} ({_fmt_sa(ca)} mol/dm3)",
            "flask_sol": f"{pair['base']}",
            "burette_vol": f"{_fmt_sa(va)} cm3",
            "flask_vol": f"{_fmt_sa(vb)} cm3",
            "indicator": pair["indicator"],
            "labels": [
                {"id": "A", "name": f"Burette with standard {pair['acid']} ({_fmt_sa(ca)} mol/dm3)", "x": 62, "y": 32},
                {"id": "B", "name": "Retort stand and clamping bosshead", "x": 26, "y": 22},
                {"id": "C", "name": "Stopcock tap for fine fluid delivery", "x": 62, "y": 64},
                {"id": "D", "name": f"Conical flask with {pair['base']} + {pair['indicator']}", "x": 62, "y": 84},
                {"id": "E", "name": "White tile to highlight color change at equivalence point", "x": 78, "y": 92},
                {"id": "F", "name": f"Meniscus reading level ({_fmt_sa(va)} cm3 delivered)", "x": 42, "y": 44},
            ],
        },
        "prompt": prompt,
        "correct_answer": f"cb = {_fmt_sa(cb)} mol/dm3",
        "worked_solution": sol,
        "sub_parts": [
            {
                "part": "1",
                "label": "1. Suitable indicator",
                "prompt": f"Choose the most suitable indicator for this titration ({pair['type']}).",
                "expected_answer": pair["indicator"],
                "marks": 1,
            },
            {
                "part": "2",
                "label": "2. Reason for indicator choice",
                "prompt": "Explain your indicator choice based on the nature of the salt formed at equivalence.",
                "expected_answer": pair["salt_nature"],
                "marks": 2,
            },
            {
                "part": "3",
                "label": "3. Base concentration (cb)",
                "prompt": f"Calculate the concentration of the {pair['base']} solution ($c_b$).",
                "expected_answer": _fmt_sa(cb),
                "marks": 2,
            },
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct indicator choice: {pair['indicator']}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Justification linking equivalence pH to {pair['salt_nature']}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Formula: (ca*Va)/(cb*Vb) = na/nb", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Correct mole ratio substitution", "marks": 1, "editable": True},
                {"id": "mp5", "desc": f"Calculated cb = {_fmt_sa(cb)} mol/dm3", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "inverted_mole_ratio", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Use the titration formula: $\\frac{c_a V_a}{c_b V_b} = \\frac{n_a}{n_b}$.",
            "tier_2": f"Mole ratio $n_a : n_b = {pair['na']} : {pair['nb']}$. Volumes can remain in $\\text{{cm}}^3$ because the unit cancels out.",
            "tier_3": f"$c_b = \\frac{{{_fmt_sa(ca)} \\times {_fmt_sa(va)} \\times {pair['nb']}}}{{{_fmt_sa(vb)} \\times {pair['na']}}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.",
        },
        "misconception_tags": ["wrong_indicator_selection", "salt_hydrolysis_misconception", "inverted_mole_ratio"],
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 5,
    }


def generate(seed: Optional[int] = None, mode: str = "compound", **kwargs) -> Dict[str, Any]:
    """Main generator entrypoint adhering to 6-pillar contract."""
    if mode == "scaffold" or kwargs.get("subskill") in ("titration_apparatus", "titration_apparatus_diagram", "titration"):
        from app.utils.physical_sciences.physical_sciences_builders import build_titration_apparatus_question
        s = seed if seed is not None else 1001
        return [build_titration_apparatus_question(seed=s, grade=12, mode="scaffold")] if kwargs.get("as_list") else build_titration_apparatus_question(seed=s, grade=12, mode="scaffold")

    r = _rng(seed)

    if mode == "elementary_definitions_conjugate":
        return _build_definitions_conjugate_drill(r)
    elif mode == "elementary_ph_calc":
        return _build_ph_calc_drill(r)
    elif mode == "elementary_titration":
        return _build_titration_drill(r)
    else:
        choice = r.choice(["conjugate", "ph", "titration"])
        if choice == "conjugate":
            return _build_definitions_conjugate_drill(r)
        elif choice == "ph":
            return _build_ph_calc_drill(r)
        else:
            return _build_titration_drill(r)
