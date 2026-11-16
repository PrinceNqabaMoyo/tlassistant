"""Grade 12 Physical Sciences - Acids and Bases Archetypes (26 to 50).

Subskills 26-50 covering Term 2 Chemistry:
- Salt Hydrolysis: concepts, neutral salts, basic salts, acidic salts, predicting solution pH.
- Indicators: selection rationale, color transitions, Le Chatelier's equilibrium.
- Titration Curves: strong-strong, weak acid-strong base, strong acid-weak base.
- Practical Titration: apparatus, procedure, standard solution preparation.
- Titration Stoichiometry: 1:1, diprotic acid, dibasic base/carbonate.
- Real-World Applications: vinegar % purity, oxalic acid standardization, antacid capacity.
- Advanced Stoichiometry: excess reagent mixture pH, back-titration of impure carbonate & fertiliser.
- Environmental & Industrial: acid rain neutralization, chloralkali process, cosmetic chemistry (perms & hair relaxers).
- Capstone NSC Exam Multi-Part Autopsy.

Zero-Meta-Curriculum Invariant strictly enforced. 100% Procedural & Deterministic.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int | random.Random] = None) -> random.Random:
    if isinstance(seed, random.Random):
        return seed
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def _fmt_sa(val: float | int, places: int = 2) -> str:
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _fmt_sci(val: float, places: int = 2) -> str:
    s = f"{val:.{places}e}"
    base, exp = s.split("e")
    exp_int = int(exp)
    base_fmt = base.replace(".", "{,}")
    return f"{base_fmt} \\times 10^{{{exp_int}}}"


# ==============================================================================
# Subskill 26: Salt Hydrolysis Concept and Definition
# ==============================================================================
def build_26_salt_hydrolysis_concept_definition(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    salts = [
        {"name": "sodium ethanoate", "formula": r"\text{CH}_3\text{COONa}", "ion": r"\text{CH}_3\text{COO}^-", "type": "basic", "ph_str": "greater than 7"},
        {"name": "ammonium chloride", "formula": r"\text{NH}_4\text{Cl}", "ion": r"\text{NH}_4^+", "type": "acidic", "ph_str": "less than 7"},
        {"name": "potassium nitrate", "formula": r"\text{KNO}_3", "ion": "neither ion", "type": "neutral", "ph_str": "equal to 7"},
    ]
    s = r.choice(salts)

    prompt = (
        f"A salt is formed in an acid-base neutralisation reaction.\n"
        f"When crystals of **{s['name']}** (${s['formula']}$) are dissolved in pure water at $25^\\circ\\text{{C}}$, "
        f"the resulting solution is found to be **{s['type']}** (pH is {s['ph_str']}).\n\n"
        f"1. Define the term **hydrolysis of a salt**.\n"
        f"2. Explain why a neutralisation reaction does not necessarily produce a neutral solution ($\\text{{pH}} = 7$).\n"
        f"3. Identify which ion from ${s['formula']}$, if any, reacts with water during hydrolysis."
    )

    sol = (
        f"1. **Hydrolysis of a salt:** The reaction of an anion or a cation (or both) of a salt with water molecules to produce excess hydronium ions ($\\text{{H}}_3\\text{{O}}^+$) or hydroxide ions ($\\text{{OH}}^-$).\n"
        f"2. **Neutralisation vs Neutral pH:** Neutralisation refers to the point where stoichiometrically equivalent amounts of acid and base have reacted. "
        f"However, if the salt formed contains a conjugate ion derived from a weak acid or weak base, that ion will hydrolyse in water, generating either excess $\\text{{H}}_3\\text{{O}}^+$ or $\\text{{OH}}^-$ and shifting the pH away from 7.\n"
        f"3. **Hydrolysing ion:** **{s['ion']}**."
    )

    return {
        "id": f"g12_ps_ab_26_{r.randint(10000, 99999)}",
        "subskill": "26_salt_hydrolysis_concept_definition",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Hydrolysis: reaction of salt ion with water; Active ion: {s['ion']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Definition of salt hydrolysis", "prompt": "Define salt hydrolysis.", "expected_answer": "Reaction of salt ion with water producing H3O+ or OH-", "marks": 2},
            {"part": "2", "label": "2. Neutralisation vs neutral pH", "prompt": "Why is neutralisation not always pH 7?", "expected_answer": "Salt ions can hydrolyse forming excess H3O+ or OH-", "marks": 2},
            {"part": "3", "label": "3. Identify hydrolysing ion", "prompt": "Identify hydrolysing ion.", "expected_answer": s['ion'], "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: reaction of an ion from a salt with water", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Explanation linking salt ion hydrolysis to pH deviation from 7", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Correct ion identified: {s['ion']}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Hydrolysis means 'splitting with water': an ion from the salt reacts with water.",
            "tier_2": "Cations of weak bases hydrolyse to give acidic solutions; anions of weak acids hydrolyse to give basic solutions.",
            "tier_3": f"Active ion in {s['name']}: {s['ion']}.",
        },
        "misconception_tags": ["neutralisation_equals_ph_7_fallacy", "salt_hydrolysis_misconception"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 27: Hydrolysis of Neutral Salts (Strong Acid + Strong Base)
# ==============================================================================
def build_27_hydrolysis_neutral_salts(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    salts = [
        {"name": "sodium chloride", "formula": r"\text{NaCl}", "cat": r"\text{Na}^+", "an": r"\text{Cl}^-", "acid": "HCl", "base": "NaOH"},
        {"name": "potassium nitrate", "formula": r"\text{KNO}_3", "cat": r"\text{K}^+", "an": r"\text{NO}_3^-", "acid": "HNO3", "base": "KOH"},
        {"name": "sodium sulfate", "formula": r"\text{Na}_2\text{SO}_4", "cat": r"\text{Na}^+", "an": r"\text{SO}_4^{2-}", "acid": "H2SO4", "base": "NaOH"},
    ]
    s = r.choice(salts)

    prompt = (
        f"A salt solution is prepared by completely dissolving **{s['name']}** (${s['formula']}$) in pure water at $25^\\circ\\text{{C}}$.\n\n"
        f"1. Identify the parent acid and parent base that react to form ${s['formula']}$.\n"
        f"2. Explain why neither the ${s['cat']}$ cation nor the ${s['an']}$ anion undergoes hydrolysis in water.\n"
        f"3. State the pH of the resulting solution at $25^\\circ\\text{{C}}$ and classify it as acidic, basic, or neutral."
    )

    sol = (
        f"1. **Parent acid and base:**\n"
        f"   - Parent acid: **{s['acid']}** (strong acid)\n"
        f"   - Parent base: **{s['base']}** (strong base)\n"
        f"2. **Lack of hydrolysis:**\n"
        f"   - ${s['cat']}$ is the cation of a strong base; it has no affinity for $\\text{{OH}}^-$ ions and does not accept protons or react with water.\n"
        f"   - ${s['an']}$ is the conjugate base of a strong acid; because the parent acid is strong, its conjugate base is extremely weak and cannot accept protons from water molecules.\n"
        f"3. **Solution pH:** $\\text{{pH}} = 7{{,}}00$ (**neutral**), because the $[\\text{{H}}_3\\text{{O}}^+]$ and $[\\text{{OH}}^-]$ balance established by water auto-ionisation remains completely undisturbed."
    )

    return {
        "id": f"g12_ps_ab_27_{r.randint(10000, 99999)}",
        "subskill": "27_hydrolysis_neutral_salts",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Parents: {s['acid']} + {s['base']}; pH = 7 (neutral)",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Parent acid and base", "prompt": "Identify parent acid and base.", "expected_answer": f"{s['acid']} and {s['base']}", "marks": 2},
            {"part": "2", "label": "2. Reason for no hydrolysis", "prompt": "Why no hydrolysis?", "expected_answer": "Conjugates of strong acids/bases are too weak to react with water", "marks": 2},
            {"part": "3", "label": "3. pH value and nature", "prompt": "State pH and nature.", "expected_answer": "pH = 7 (neutral)", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct parent acid ({s['acid']}) and base ({s['base']})", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Explanation: conjugate ions of strong acids/bases do not hydrolyse", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "pH = 7 and neutral", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Strong acid + strong base = neutral salt.",
            "tier_2": "Because the parents are strong, their conjugate ions are extremely weak and do not react with water.",
            "tier_3": f"${s['formula']}$ comes from {s['acid']} and {s['base']}, so pH = 7.",
        },
        "misconception_tags": ["strong_conjugate_misconception", "salt_hydrolysis_omission"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 28: Hydrolysis of Basic Salts (Weak Acid + Strong Base)
# ==============================================================================
def build_28_hydrolysis_basic_salts(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    salts = [
        {"name": "sodium ethanoate", "formula": r"\text{CH}_3\text{COONa}", "anion": r"\text{CH}_3\text{COO}^-", "acid": "CH3COOH", "base": "NaOH", "eq": r"\text{CH}_3\text{COO}^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{CH}_3\text{COOH}(\text{aq}) + \text{OH}^-(\text{aq})"},
        {"name": "potassium fluoride", "formula": r"\text{KF}", "anion": r"\text{F}^-", "acid": "HF", "base": "KOH", "eq": r"\text{F}^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{HF}(\text{aq}) + \text{OH}^-(\text{aq})"},
        {"name": "sodium cyanide", "formula": r"\text{NaCN}", "anion": r"\text{CN}^-", "acid": "HCN", "base": "NaOH", "eq": r"\text{CN}^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{HCN}(\text{aq}) + \text{OH}^-(\text{aq})"},
        {"name": "sodium methanoate", "formula": r"\text{HCOONa}", "anion": r"\text{HCOO}^-", "acid": "HCOOH", "base": "NaOH", "eq": r"\text{HCOO}^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{HCOOH}(\text{aq}) + \text{OH}^-(\text{aq})"},
    ]
    s = r.choice(salts)

    prompt = (
        f"An aqueous solution of **{s['name']}** (${s['formula']}$) turns red litmus paper blue and has a $\\text{{pH}} > 7$.\n\n"
        f"1. Identify the parent acid and parent base of ${s['formula']}$, and state their relative strengths.\n"
        f"2. Write down a balanced chemical equation for the **hydrolysis reaction** of the anion (${s['anion']}$) in water.\n"
        f"3. Using your equation, explain why the aqueous solution is **basic (alkaline)**."
    )

    sol = (
        f"1. **Parents:**\n"
        f"   - Parent acid: **{s['acid']}** (weak acid)\n"
        f"   - Parent base: **{s['base']}** (strong base)\n"
        f"2. **Hydrolysis equation:**\n"
        f"   $${s['eq']}$$\n"
        f"3. **Explanation:** Because {s['acid']} is a weak acid, its conjugate base (${s['anion']}$) has sufficient basic strength to act as a proton acceptor. "
        f"It accepts a proton from water, producing hydroxide ions ($\\text{{OH}}^-$). "
        f"This causes $[\\text{{OH}}^-] > [\\text{{H}}_3\\text{{O}}^+]$, resulting in $\\text{{pH}} > 7$ (basic solution)."
    )

    return {
        "id": f"g12_ps_ab_28_{r.randint(10000, 99999)}",
        "subskill": "28_hydrolysis_basic_salts",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Parents: {s['acid']} (weak) + {s['base']} (strong); Eq: {s['eq']}; pH > 7",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Parent acid and base", "prompt": "Identify parent acid and base.", "expected_answer": f"{s['acid']} (weak) and {s['base']} (strong)", "marks": 2},
            {"part": "2", "label": "2. Anion hydrolysis equation", "prompt": "Write hydrolysis equation.", "expected_answer": s['eq'], "marks": 2},
            {"part": "3", "label": "3. Explanation of basic pH", "prompt": "Explain why solution is basic.", "expected_answer": "Produces excess OH- ions", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct parent acid ({s['acid']} weak) and parent base ({s['base']} strong)", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Balanced hydrolysis equation producing OH-", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Explanation linking excess [OH-] to pH > 7", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "The conjugate base of a weak acid acts as a proton acceptor in water.",
            "tier_2": "The anion accepts $H^+$ from water, creating $OH^-$ and shifting pH above 7.",
            "tier_3": f"Equation: ${s['eq']}$. Produces excess $OH^-$.",
        },
        "misconception_tags": ["anion_hydrolysis_direction_error", "basic_salt_formula_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 29: Hydrolysis of Acidic Salts (Strong Acid + Weak Base)
# ==============================================================================
def build_29_hydrolysis_acidic_salts(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    salts = [
        {"name": "ammonium chloride", "formula": r"\text{NH}_4\text{Cl}", "cat": r"\text{NH}_4^+", "acid": "HCl", "base": "NH3", "eq": r"\text{NH}_4^+(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_3(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})"},
        {"name": "ammonium nitrate", "formula": r"\text{NH}_4\text{NO}_3", "cat": r"\text{NH}_4^+", "acid": "HNO3", "base": "NH3", "eq": r"\text{NH}_4^+(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_3(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})"},
        {"name": "ammonium sulfate", "formula": r"(\text{NH}_4)_2\text{SO}_4", "cat": r"\text{NH}_4^+", "acid": "H2SO4", "base": "NH3", "eq": r"\text{NH}_4^+(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_3(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})"},
    ]
    s = r.choice(salts)

    prompt = (
        f"An aqueous solution of **{s['name']}** (${s['formula']}$) has a measured pH of approximately $5{{,}}2$ at $25^\\circ\\text{{C}}$.\n\n"
        f"1. Name the parent acid and parent base of ${s['formula']}$, and state their relative strengths.\n"
        f"2. Write down a balanced chemical equation for the **hydrolysis reaction** of the cation (${s['cat']}$) in water.\n"
        f"3. Explain why this hydrolysis reaction causes the solution to be **acidic**."
    )

    sol = (
        f"1. **Parents:**\n"
        f"   - Parent acid: **{s['acid']}** (strong acid)\n"
        f"   - Parent base: **{s['base']}** (weak base)\n"
        f"2. **Hydrolysis equation:**\n"
        f"   $${s['eq']}$$\n"
        f"3. **Explanation:** Because {s['base']} is a weak base, its conjugate acid (${s['cat']}$) is relatively strong and acts as a proton donor. "
        f"It donates a proton to a water molecule, generating hydronium ions ($\\text{{H}}_3\\text{{O}}^+$). "
        f"This causes $[\\text{{H}}_3\\text{{O}}^+] > [\\text{{OH}}^-]$, resulting in $\\text{{pH}} < 7$ (acidic solution)."
    )

    return {
        "id": f"g12_ps_ab_29_{r.randint(10000, 99999)}",
        "subskill": "29_hydrolysis_acidic_salts",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Parents: {s['acid']} (strong) + {s['base']} (weak); Eq: {s['eq']}; pH < 7",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Parent acid and base", "prompt": "Identify parent acid and base.", "expected_answer": f"{s['acid']} (strong) and {s['base']} (weak)", "marks": 2},
            {"part": "2", "label": "2. Cation hydrolysis equation", "prompt": "Write hydrolysis equation.", "expected_answer": s['eq'], "marks": 2},
            {"part": "3", "label": "3. Explanation of acidic pH", "prompt": "Explain why solution is acidic.", "expected_answer": "Produces excess H3O+ ions", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct parent acid ({s['acid']} strong) and parent base ({s['base']} weak)", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Balanced cation hydrolysis equation generating H3O+", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Explanation linking excess [H3O+] to pH < 7", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Strong acid + weak base = acidic salt.",
            "tier_2": "The ammonium ion ($NH_4^+$) donates a proton to water, producing $H_3O^+$.",
            "tier_3": f"Equation: ${s['eq']}$. Increases $[H_3O^+]$, so pH < 7.",
        },
        "misconception_tags": ["cation_hydrolysis_direction_error", "acidic_salt_identification_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 30: Predicting Salt Solution pH
# ==============================================================================
def build_30_predicting_salt_solution_ph(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    salt_pool = [
        {"formula": r"\text{K}_2\text{CO}_3", "name": "Potassium carbonate", "acid": "H2CO3 (weak)", "base": "KOH (strong)", "nature": "Basic (pH > 7)"},
        {"formula": r"\text{NH}_4\text{Br}", "name": "Ammonium bromide", "acid": "HBr (strong)", "base": "NH3 (weak)", "nature": "Acidic (pH < 7)"},
        {"formula": r"\text{LiNO}_3", "name": "Lithium nitrate", "acid": "HNO3 (strong)", "base": "LiOH (strong)", "nature": "Neutral (pH = 7)"},
        {"formula": r"\text{CH}_3\text{COOK}", "name": "Potassium ethanoate", "acid": "CH3COOH (weak)", "base": "KOH (strong)", "nature": "Basic (pH > 7)"},
        {"formula": r"(\text{NH}_4)_2\text{SO}_4", "name": "Ammonium sulfate", "acid": "H2SO4 (strong)", "base": "NH3 (weak)", "nature": "Acidic (pH < 7)"},
        {"formula": r"\text{NaCl}", "name": "Sodium chloride", "acid": "HCl (strong)", "base": "NaOH (strong)", "nature": "Neutral (pH = 7)"},
    ]
    r.shuffle(salt_pool)
    chosen = salt_pool[:3]

    prompt = (
        f"Three unlabeled beakers contain equimolar aqueous solutions of the following salts:\n"
        f"- Salt 1: **{chosen[0]['name']}** (${chosen[0]['formula']}$)\n"
        f"- Salt 2: **{chosen[1]['name']}** (${chosen[1]['formula']}$)\n"
        f"- Salt 3: **{chosen[2]['name']}** (${chosen[2]['formula']}$)\n\n"
        f"For EACH salt:\n"
        f"1. Identify the parent acid and parent base from which it was formed.\n"
        f"2. Predict whether its aqueous solution is **acidic**, **basic**, or **neutral**.\n"
        f"3. Give a concise reason for your prediction based on salt hydrolysis."
    )

    sol_lines = []
    for i, item in enumerate(chosen, 1):
        sol_lines.append(f"Salt {i} (${item['formula']}$): Parent acid: {item['acid']}; Parent base: {item['base']}. Prediction: **{item['nature']}**.")
    sol = "\n".join(sol_lines)

    return {
        "id": f"g12_ps_ab_30_{r.randint(10000, 99999)}",
        "subskill": "30_predicting_salt_solution_ph",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": "; ".join([f"{x['formula']}: {x['nature']}" for x in chosen]),
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": f"1. Salt 1 ({chosen[0]['formula']})", "prompt": f"Predict nature of {chosen[0]['formula']}.", "expected_answer": chosen[0]['nature'], "marks": 2},
            {"part": "2", "label": f"2. Salt 2 ({chosen[1]['formula']})", "prompt": f"Predict nature of {chosen[1]['formula']}.", "expected_answer": chosen[1]['nature'], "marks": 2},
            {"part": "3", "label": f"3. Salt 3 ({chosen[2]['formula']})", "prompt": f"Predict nature of {chosen[2]['formula']}.", "expected_answer": chosen[2]['nature'], "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Salt 1: parent acid/base and correct nature ({chosen[0]['nature']})", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Salt 2: parent acid/base and correct nature ({chosen[1]['nature']})", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Salt 3: parent acid/base and correct nature ({chosen[2]['nature']})", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Strong acid + strong base = neutral. Strong acid + weak base = acidic. Weak acid + strong base = basic.",
            "tier_2": "Look at the cation and anion: which one comes from a weak parent? That is the ion that hydrolyses.",
            "tier_3": f"{chosen[0]['formula']} is {chosen[0]['nature']}; {chosen[1]['formula']} is {chosen[1]['nature']}; {chosen[2]['formula']} is {chosen[2]['nature']}.",
        },
        "misconception_tags": ["salt_ph_prediction_error", "parent_strength_misidentification"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 31: Indicator Selection Rationale
# ==============================================================================
def build_31_indicator_selection_rationale(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    titrations = [
        {
            "acid": "Hydrochloric acid (HCl)",
            "base": "Sodium hydroxide (NaOH)",
            "type": "Strong acid - strong base",
            "equiv_ph": r"7{,}0",
            "indicator": "Bromothymol blue",
            "ind_range": r"6{,}0 - 7{,}6",
            "color_change": "Yellow (acid) to green (end-point) to blue (base)",
        },
        {
            "acid": "Ethanoic acid (CH3COOH)",
            "base": "Sodium hydroxide (NaOH)",
            "type": "Weak acid - strong base",
            "equiv_ph": r"8{,}5 - 9{,}0",
            "indicator": "Phenolphthalein",
            "ind_range": r"8{,}3 - 10{,}0",
            "color_change": "Colourless (acid) to faint pink (end-point) to dark pink (base)",
        },
        {
            "acid": "Nitric acid (HNO3)",
            "base": "Ammonia solution (NH3)",
            "type": "Strong acid - weak base",
            "equiv_ph": r"5{,}0 - 5{,}5",
            "indicator": "Methyl orange",
            "ind_range": r"3{,}1 - 4{,}4",
            "color_change": "Red (acid) to orange-yellow (end-point) to yellow (base)",
        },
    ]
    t = r.choice(titrations)

    prompt = (
        f"A learner titrates **{t['acid']}** against **{t['base']}** in a matric laboratory practical.\n\n"
        f"1. State the general rule for selecting a suitable acid-base indicator for a titration.\n"
        f"2. Predict the approximate pH at the **equivalence point** of this titration, referencing the nature of the salt formed.\n"
        f"3. Select the most suitable indicator from the following options and state the observed colour change at the end-point:\n"
        f"   - **Methyl orange** (pH range: $3{{,}}1 - 4{{,}}4$)\n"
        f"   - **Bromothymol blue** (pH range: $6{{,}}0 - 7{{,}}6$)\n"
        f"   - **Phenolphthalein** (pH range: $8{{,}}3 - 10{{,}}0$)"
    )

    sol = (
        f"1. **Selection rule:** The indicator's pH transition range must encompass or closely match the pH at the equivalence point of the titration.\n"
        f"2. **Equivalence pH:** This is a {t['type']} titration. The salt formed hydrolyses to give an equivalence pH of approximately **{t['equiv_ph']}**.\n"
        f"3. **Indicator choice:** **{t['indicator']}** (pH range: {t['ind_range']}).\n"
        f"   Colour change: {t['color_change']}."
    )

    return {
        "id": f"g12_ps_ab_31_{r.randint(10000, 99999)}",
        "subskill": "31_indicator_selection_rationale",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Indicator: {t['indicator']}; Equivalence pH: {t['equiv_ph']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. General indicator selection rule", "prompt": "State indicator selection rule.", "expected_answer": "Indicator pH range must match equivalence point pH", "marks": 2},
            {"part": "2", "label": "2. Equivalence point pH", "prompt": "Predict equivalence point pH.", "expected_answer": t['equiv_ph'], "marks": 2},
            {"part": "3", "label": "3. Indicator choice and colour change", "prompt": "Choose indicator and colour change.", "expected_answer": f"{t['indicator']}; {t['color_change']}", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Rule: indicator pH range must overlap equivalence point pH", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Equivalence pH predicted correctly ({t['equiv_ph']}) with salt hydrolysis justification", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Correct indicator chosen: {t['indicator']} with correct end-point colour", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Match the indicator's operating pH range to the expected equivalence pH.",
            "tier_2": f"{t['type']} produces a salt with equivalence pH around {t['equiv_ph']}.",
            "tier_3": f"Best indicator: {t['indicator']}.",
        },
        "misconception_tags": ["universal_indicator_misuse_in_titration", "indicator_range_mismatch"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 32: Indicator Color Transition and Le Chatelier Equilibrium
# ==============================================================================
def build_32_indicator_color_transition_equilibrium(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    ind_data = [
        {"name": "Bromothymol blue", "hin_color": "yellow", "in_color": "blue", "mid_color": "green", "mid_ph": r"6{,}8"},
        {"name": "Phenolphthalein", "hin_color": "colourless", "in_color": "pink", "mid_color": "faint pink", "mid_ph": r"9{,}0"},
        {"name": "Methyl orange", "hin_color": "red", "in_color": "yellow", "mid_color": "orange", "mid_ph": r"3{,}8"},
    ]
    ind = r.choice(ind_data)

    prompt = (
        f"An acid-base indicator ($\\text{{HIn}}$) is a weak organic acid that establishes the following equilibrium in aqueous solution:\n\n"
        f"$$\\underset{{\\text{{({ind['hin_color']})}}}}{{\\text{{HIn}}(\\text{{aq}})}} + \\text{{H}}_2\\text{{O}}(\\text{{l}}) \\rightleftharpoons \\underset{{\\text{{({ind['in_color']})}}}}{{\\text{{In}}^-(\\text{{aq}})}} + \\text{{H}}_3\\text{{O}}^+(\\text{{aq}})$$\n\n"
        f"1. Use **Le Chatelier's principle** to explain the color change when a few drops of this indicator are added to a strongly **acidic** solution.\n"
        f"2. Use Le Chatelier's principle to explain the color change when a few drops of this indicator are added to a strongly **basic** solution.\n"
        f"3. What color is observed when $[\\text{{HIn}}] = [\\text{{In}}^-]$ at the **end-point**?"
    )

    sol = (
        f"1. **Addition of acid:** Adding acid introduces a high concentration of $\\text{{H}}_3\\text{{O}}^+$ ions. "
        f"According to Le Chatelier's principle, the equilibrium shifts to the **left** to consume added $\\text{{H}}_3\\text{{O}}^+$. "
        f"This increases $[\\text{{HIn}}]$, and the solution turns **{ind['hin_color']}**.\n"
        f"2. **Addition of base:** Adding base introduces $\\text{{OH}}^-$ ions, which react with and remove $\\text{{H}}_3\\text{{O}}^+$ ions (forming water). "
        f"According to Le Chatelier's principle, the equilibrium shifts to the **right** to replace $\\text{{H}}_3\\text{{O}}^+$. "
        f"This increases $[\\text{{In}}^-]$, and the solution turns **{ind['in_color']}**.\n"
        f"3. **End-point color:** When $[\\text{{HIn}}] = [\\text{{In}}^-]$, equal amounts of both colored species are present, producing the intermediate transition color: **{ind['mid_color']}**."
    )

    return {
        "id": f"g12_ps_ab_32_{r.randint(10000, 99999)}",
        "subskill": "32_indicator_color_transition_equilibrium",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Acid: {ind['hin_color']}; Base: {ind['in_color']}; End-point: {ind['mid_color']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Le Chatelier shift in acid", "prompt": "Explain color in acid.", "expected_answer": f"Shifts left, turns {ind['hin_color']}", "marks": 2},
            {"part": "2", "label": "2. Le Chatelier shift in base", "prompt": "Explain color in base.", "expected_answer": f"Shifts right, turns {ind['in_color']}", "marks": 2},
            {"part": "3", "label": "3. Colour when [HIn]=[In-]", "prompt": "What color at end-point?", "expected_answer": ind['mid_color'], "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Acid: shift left justified by Le Chatelier, color {ind['hin_color']}", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Base: shift right justified by OH- removing H3O+, color {ind['in_color']}", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Intermediate transition color: {ind['mid_color']}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Adding $H^+$ pushes equilibrium backwards to reactants.",
            "tier_2": "Adding $OH^-$ removes $H^+$, pulling equilibrium forward to products.",
            "tier_3": f"Acid gives {ind['hin_color']}; base gives {ind['in_color']}; end-point gives {ind['mid_color']}.",
        },
        "misconception_tags": ["le_chatelier_indicator_shift_error", "endpoint_vs_equivalence_confusion"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 33: Titration Curve for Strong Acid - Strong Base
# ==============================================================================
def build_33_titration_curve_strong_acid_strong_base(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    va = r.choice([20.0, 25.0])
    ca = r.choice([0.1, 0.2])
    cb = ca
    veq = va  # since ca = cb and 1:1 ratio
    start_ph = round(-math.log10(ca), 1)

    # Inline SVG of strong acid - strong base titration curve
    svg_curve = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 280" width="100%" height="100%">'
        f'<rect width="450" height="280" fill="#ffffff" rx="6"/>'
        f'<text x="225" y="22" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">TITRATION CURVE: STRONG ACID vs STRONG BASE</text>'
        f'<line x1="60" y1="240" x2="410" y2="240" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="240" x2="60" y2="40" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="235" y="270" font-family="Arial" font-size="11" text-anchor="middle" fill="#0f172a">Volume of standard NaOH added (cm³)</text>'
        f'<text x="20" y="140" font-family="Arial" font-size="11" text-anchor="middle" fill="#0f172a" transform="rotate(-90 20 140)">pH</text>'
        f'<text x="50" y="244" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">0</text>'
        f'<text x="50" y="144" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">7</text>'
        f'<text x="50" y="50" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">14</text>'
        f'<line x1="56" y1="140" x2="410" y2="140" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4"/>'
        f'<path d="M 60 225 L 200 215 Q 220 210 225 140 Q 230 65 250 60 L 400 55" stroke="#2563eb" stroke-width="2.5" fill="none"/>'
        f'<circle cx="225" cy="140" r="5" fill="#dc2626"/>'
        f'<line x1="225" y1="140" x2="225" y2="240" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3"/>'
        f'<text x="225" y="254" font-family="Arial" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">{_fmt_sa(veq)}</text>'
        f'<text x="235" y="135" font-family="Arial" font-size="10" font-weight="bold" fill="#dc2626">Equivalence (pH = 7,0)</text>'
        f'</svg>'
    )

    prompt = (
        f"A titration curve shows the titration of **${_fmt_sa(va)}\\text{{ cm}}^3$** of **HCl** "
        f"against **NaOH** of concentration **${_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**.\n\n"
        f"1. Read the initial pH of the acid from the curve and verify that $[\\text{{H}}_3\\text{{O}}^+] = {_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.\n"
        f"2. State the volume of NaOH required to reach the equivalence point ($V_{{\\text{{eq}}}}$).\n"
        f"3. State the pH at the equivalence point and explain why the pH curve exhibits a steep vertical jump at this point.\n"
        f"4. Name the most suitable indicator for this titration."
    )

    sol = (
        f"1. **Initial pH:** $\\text{{pH}} = {_fmt_sa(start_ph)}$. Since $\\text{{HCl}}$ is a strong monoprotic acid, "
        f"$[\\text{{H}}_3\\text{{O}}^+] = c = {_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$, giving $\\text{{pH}} = -\\log({_fmt_sa(ca)}) = {_fmt_sa(start_ph)}$.\n"
        f"2. **Equivalence volume:** $V_{{\\text{{eq}}}} = {_fmt_sa(veq)}\\text{{ cm}}^3$.\n"
        f"3. **Equivalence pH and steep jump:** $\\text{{pH}} = 7{{,}}00$. The curve jumps steeply across several pH units because near the equivalence point, "
        f"the unneutralised $[\\text{{H}}_3\\text{{O}}^+]$ is extremely low, so adding a single drop of base neutralises the remaining traces of acid and creates excess $\\text{{OH}}^-$.\n"
        f"4. **Suitable indicator:** **Bromothymol blue** (or phenolphthalein/methyl orange, since the steep vertical inflection spans pH 4 to 10)."
    )

    return {
        "id": f"g12_ps_ab_33_{r.randint(10000, 99999)}",
        "subskill": "33_titration_curve_strong_acid_strong_base",
        "type": "compound",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_curve,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "correct_answer": f"Equivalence volume = {_fmt_sa(veq)} cm3; Equivalence pH = 7,0; Indicator: Bromothymol blue",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Initial pH verification", "prompt": "Read initial pH.", "expected_answer": _fmt_sa(start_ph), "marks": 1},
            {"part": "2", "label": "2. Equivalence volume", "prompt": "State equivalence volume.", "expected_answer": f"{_fmt_sa(veq)} cm3", "marks": 1},
            {"part": "3", "label": "3. Equivalence pH and steep jump", "prompt": "State equivalence pH and explain steepness.", "expected_answer": "pH = 7.0; tiny amount of acid neutralised by one drop", "marks": 2},
            {"part": "4", "label": "4. Suitable indicator", "prompt": "Name suitable indicator.", "expected_answer": "Bromothymol blue", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Initial pH verified as {_fmt_sa(start_ph)}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Equivalence volume read as {_fmt_sa(veq)} cm3", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Equivalence pH = 7.0 with explanation of logarithmic steepness", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Bromothymol blue identified", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Strong acid + strong base always has its equivalence point at exactly pH 7,0 at 25°C.",
            "tier_2": "The steep portion covers pH 4 to 10.",
            "tier_3": f"Equivalence volume: {_fmt_sa(veq)} cm3; pH = 7,0; Indicator: Bromothymol blue.",
        },
        "misconception_tags": ["equivalence_point_reading_error", "indicator_range_mismatch"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 34: Titration Curve for Weak Acid - Strong Base
# ==============================================================================
def build_34_titration_curve_weak_acid_strong_base(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    va = r.choice([20.0, 25.0])
    veq = va
    equiv_ph = round(r.uniform(8.6, 9.1), 1)

    svg_curve = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 280" width="100%" height="100%">'
        f'<rect width="450" height="280" fill="#ffffff" rx="6"/>'
        f'<text x="225" y="22" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">TITRATION CURVE: WEAK ACID vs STRONG BASE</text>'
        f'<line x1="60" y1="240" x2="410" y2="240" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="240" x2="60" y2="40" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="235" y="270" font-family="Arial" font-size="11" text-anchor="middle" fill="#0f172a">Volume of standard NaOH added (cm³)</text>'
        f'<text x="20" y="140" font-family="Arial" font-size="11" text-anchor="middle" fill="#0f172a" transform="rotate(-90 20 140)">pH</text>'
        f'<text x="50" y="244" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">0</text>'
        f'<text x="50" y="144" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">7</text>'
        f'<text x="50" y="50" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">14</text>'
        f'<line x1="56" y1="140" x2="410" y2="140" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4"/>'
        f'<path d="M 60 195 Q 100 180 180 165 Q 215 155 225 115 Q 235 65 260 60 L 400 55" stroke="#059669" stroke-width="2.5" fill="none"/>'
        f'<circle cx="225" cy="115" r="5" fill="#dc2626"/>'
        f'<line x1="225" y1="115" x2="225" y2="240" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3"/>'
        f'<text x="225" y="254" font-family="Arial" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">{_fmt_sa(veq)}</text>'
        f'<text x="235" y="112" font-family="Arial" font-size="10" font-weight="bold" fill="#dc2626">Equivalence (pH = {_fmt_sa(equiv_ph)})</text>'
        f'</svg>'
    )

    prompt = (
        f"A titration curve shows the titration of **${_fmt_sa(va)}\\text{{ cm}}^3$** of ethanoic acid ($\\text{{CH}}_3\\text{{COOH}}$) "
        f"with standard sodium hydroxide ($\\text{{NaOH}}$).\n\n"
        f"1. State why the initial pH is higher than that of a strong acid of equal concentration.\n"
        f"2. Why is the pH at the equivalence point **greater than 7** (${_fmt_sa(equiv_ph)}$)?\n"
        f"3. Explain why **phenolphthalein** (pH range: $8{{,}}3 - 10{{,}}0$) is the preferred indicator for this titration, "
        f"while methyl orange is unsuitable."
    )

    sol = (
        f"1. **Initial pH:** Ethanoic acid is a weak acid that ionises only partially in water, producing a lower $[\\text{{H}}_3\\text{{O}}^+]$ and thus a higher initial pH (~3 instead of 1).\n"
        f"2. **Equivalence pH > 7:** At the equivalence point, all ethanoic acid has been converted to sodium ethanoate ($\\text{{CH}}_3\\text{{COONa}}$). "
        f"The ethanoate anion hydrolyses in water ($\\text{{CH}}_3\\text{{COO}}^- + \\text{{H}}_2\\text{{O}} \\rightleftharpoons \\text{{CH}}_3\\text{{COOH}} + \\text{{OH}}^-$), "
        f"producing excess $\\text{{OH}}^-$ ions and shifting the equivalence pH into the basic region (~${_fmt_sa(equiv_ph)}$).\n"
        f"3. **Indicator choice:** Phenolphthalein has a pH transition range of $8{{,}}3 - 10{{,}}0$, which perfectly encompasses the equivalence pH (${_fmt_sa(equiv_ph)}$). "
        f"Methyl orange changes color between pH $3{{,}}1 - 4{{,}}4$, which occurs well before the equivalence point is reached."
    )

    return {
        "id": f"g12_ps_ab_34_{r.randint(10000, 99999)}",
        "subskill": "34_titration_curve_weak_acid_strong_base",
        "type": "compound",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_curve,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "correct_answer": f"Equivalence pH = {_fmt_sa(equiv_ph)} > 7 due to ethanoate hydrolysis; Indicator: Phenolphthalein",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Higher initial pH", "prompt": "Why is initial pH higher?", "expected_answer": "Weak acid ionises partially, lower [H3O+]", "marks": 1},
            {"part": "2", "label": "2. Reason equivalence pH > 7", "prompt": "Why is equivalence pH > 7?", "expected_answer": "Anion hydrolysis of CH3COO- produces OH-", "marks": 2},
            {"part": "3", "label": "3. Phenolphthalein justification", "prompt": "Why phenolphthalein and not methyl orange?", "expected_answer": "Range 8.3-10.0 matches equivalence pH", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Initial pH higher due to incomplete ionisation of weak acid", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Equivalence pH > 7 explained via ethanoate anion hydrolysis forming OH-", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Phenolphthalein range matching equivalence point justified", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Weak acid + strong base = basic salt at equivalence.",
            "tier_2": "Because the equivalence pH is ~9, choose an indicator that changes color around pH 9.",
            "tier_3": f"Equivalence pH = {_fmt_sa(equiv_ph)}; Indicator: Phenolphthalein.",
        },
        "misconception_tags": ["weak_acid_curve_inflection_error", "wrong_indicator_for_weak_acid"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 35: Titration Curve for Strong Acid - Weak Base
# ==============================================================================
def build_35_titration_curve_strong_acid_weak_base(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    vb = r.choice([20.0, 25.0])
    veq = vb
    equiv_ph = round(r.uniform(5.1, 5.5), 1)

    svg_curve = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 280" width="100%" height="100%">'
        f'<rect width="450" height="280" fill="#ffffff" rx="6"/>'
        f'<text x="225" y="22" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">TITRATION CURVE: STRONG ACID vs WEAK BASE</text>'
        f'<line x1="60" y1="240" x2="410" y2="240" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="240" x2="60" y2="40" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="235" y="270" font-family="Arial" font-size="11" text-anchor="middle" fill="#0f172a">Volume of standard HCl added (cm³)</text>'
        f'<text x="20" y="140" font-family="Arial" font-size="11" text-anchor="middle" fill="#0f172a" transform="rotate(-90 20 140)">pH</text>'
        f'<text x="50" y="244" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">0</text>'
        f'<text x="50" y="144" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">7</text>'
        f'<text x="50" y="50" font-family="Arial" font-size="10" text-anchor="end" fill="#475569">14</text>'
        f'<line x1="56" y1="140" x2="410" y2="140" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4"/>'
        f'<path d="M 60 75 Q 120 85 180 100 Q 215 115 225 170 Q 235 220 260 225 L 400 230" stroke="#7c3aed" stroke-width="2.5" fill="none"/>'
        f'<circle cx="225" cy="170" r="5" fill="#dc2626"/>'
        f'<line x1="225" y1="170" x2="225" y2="240" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3"/>'
        f'<text x="225" y="254" font-family="Arial" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">{_fmt_sa(veq)}</text>'
        f'<text x="235" y="167" font-family="Arial" font-size="10" font-weight="bold" fill="#dc2626">Equivalence (pH = {_fmt_sa(equiv_ph)})</text>'
        f'</svg>'
    )

    prompt = (
        f"A learner titrates **${_fmt_sa(vb)}\\text{{ cm}}^3$** of aqueous ammonia ($\\text{{NH}}_3$) "
        f"by adding standard hydrochloric acid ($\\text{{HCl}}$).\n\n"
        f"1. Why is the initial pH of the ammonia solution around $11{{,}}0$ rather than $13{{,}}0$?\n"
        f"2. Explain why the equivalence point pH is **less than 7** (${_fmt_sa(equiv_ph)}$), identifying the chemical species responsible.\n"
        f"3. Select the best indicator for this titration from methyl orange, bromothymol blue, and phenolphthalein. Justify your choice."
    )

    sol = (
        f"1. **Initial pH:** Ammonia is a weak base that ionises only partially in water, producing a lower $[\\text{{OH}}^-]$ than a strong base of equal concentration.\n"
        f"2. **Equivalence pH < 7:** At equivalence, $\\text{{NH}}_4\\text{{Cl}}$ is formed. "
        f"The ammonium ion ($\\text{{NH}}_4^+$) hydrolyses in water ($\\text{{NH}}_4^+ + \\text{{H}}_2\\text{{O}} \\rightleftharpoons \\text{{NH}}_3 + \\text{{H}}_3\\text{{O}}^+$), "
        f"generating excess $\\text{{H}}_3\\text{{O}}^+$ and making the equivalence point acidic (~${_fmt_sa(equiv_ph)}$).\n"
        f"3. **Indicator:** **Methyl orange** (pH range: $3{{,}}1 - 4{{,}}4$). Its transition range encompasses the acidic equivalence point."
    )

    return {
        "id": f"g12_ps_ab_35_{r.randint(10000, 99999)}",
        "subskill": "35_titration_curve_strong_acid_weak_base",
        "type": "compound",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_curve,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "correct_answer": f"Equivalence pH = {_fmt_sa(equiv_ph)} < 7 due to NH4+ hydrolysis; Indicator: Methyl orange",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Lower initial base pH", "prompt": "Why is initial pH ~11?", "expected_answer": "Weak base ionises partially", "marks": 1},
            {"part": "2", "label": "2. Reason equivalence pH < 7", "prompt": "Why is equivalence pH < 7?", "expected_answer": "Cation hydrolysis of NH4+ produces H3O+", "marks": 2},
            {"part": "3", "label": "3. Indicator selection", "prompt": "Choose indicator and justify.", "expected_answer": "Methyl orange; range 3.1-4.4 matches acidic equivalence", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Weak base partial ionisation explanation", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Equivalence pH < 7 explained via NH4+ cation hydrolysis", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Methyl orange selected and justified by pH range", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Strong acid + weak base = acidic salt at equivalence.",
            "tier_2": "Because the equivalence pH is ~5, choose an indicator that transitions in the acidic region (pH 3–5).",
            "tier_3": f"Equivalence pH = {_fmt_sa(equiv_ph)}; Indicator: Methyl orange.",
        },
        "misconception_tags": ["strong_acid_weak_base_indicator_error", "salt_cation_hydrolysis_omission"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 36: Titration Apparatus and Experimental Procedure
# ==============================================================================
def build_36_titration_apparatus_and_procedure(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    actions = [
        {"item": "Burette", "rinse": "Rinsed with the standard acid/base solution it will deliver", "wrong_rinse": "Rinsing with water dilutes the titrant and causes a false high titre volume"},
        {"item": "Pipette", "rinse": "Rinsed with the exact solution it will transfer", "wrong_rinse": "Rinsing with water dilutes the aliquot delivered to the flask"},
        {"item": "Conical flask", "rinse": "Rinsed with distilled water only", "wrong_rinse": "Rinsing with acid/base would introduce extra unmeasured moles of reactant"},
    ]
    target = r.choice(actions)

    # Inline SVG representing titration apparatus with seed-varied readings
    initial_reading = f"{r.uniform(1.10, 4.90):.2f}".replace('.', ',')
    aliquot_vol = r.choice(["20,0", "25,0"])
    flask_fill = r.choice(["#fef2f2", "#fdf4ff", "#e0f2fe", "#f0fdf4"])
    indicator_label = r.choice(["Phenolphthalein", "Bromothymol blue", "Methyl orange"])

    svg_app = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 330" width="100%" height="100%">'
        f'<rect width="420" height="330" fill="#f8fafc" rx="6"/>'
        f'<text x="210" y="24" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f172a">TITRATION EXPERIMENTAL APPARATUS</text>'
        f'<rect x="70" y="290" width="190" height="15" fill="#334155" rx="2"/>'
        f'<rect x="100" y="40" width="10" height="250" fill="#64748b"/>'
        f'<rect x="108" y="70" width="45" height="12" fill="#475569"/>'
        f'<rect x="150" y="50" width="16" height="170" fill="#f1f5f9" stroke="#0284c7" stroke-width="1.5"/>'
        f'<line x1="158" y1="50" x2="158" y2="210" stroke="#0284c7" stroke-width="0.5" stroke-dasharray="2"/>'
        f'<polygon points="150,220 166,220 160,235 156,235" fill="#94a3b8"/>'
        f'<rect x="153" y="222" width="10" height="6" fill="#dc2626"/>'
        f'<path d="M 145 242 L 171 242 L 195 295 L 121 295 Z" fill="{flask_fill}" stroke="#0284c7" stroke-width="1.5"/>'
        f'<rect x="110" y="296" width="96" height="6" fill="#ffffff" stroke="#94a3b8"/>'
        f'<text x="180" y="90" font-family="Arial" font-size="11" fill="#0369a1">A: Burette (Reading: {initial_reading} cm³)</text>'
        f'<text x="180" y="230" font-family="Arial" font-size="11" fill="#dc2626">B: Stopcock tap</text>'
        f'<text x="205" y="265" font-family="Arial" font-size="11" fill="#0369a1">C: Conical flask ({aliquot_vol} cm³ + {indicator_label})</text>'
        f'<text x="205" y="300" font-family="Arial" font-size="11" fill="#475569">D: White tile</text>'
        f'</svg>'
    )

    prompt = (
        f"A laboratory learner sets up the titration apparatus.\n\n"
        f"1. State the precise rinsing procedure for the **{target['item']}** before performing the titration.\n"
        f"2. Explain why rinsing the {target['item']} with {target['wrong_rinse']}.\n"
        f"3. State the purpose of placing a **white tile** beneath the conical flask.\n"
        f"4. Why is the conical flask continuously swirled during the addition of the titrant?"
    )

    sol = (
        f"1. **Rinsing procedure:** {target['rinse']}.\n"
        f"2. **Consequence of incorrect rinsing:** {target['wrong_rinse']}.\n"
        f"3. **White tile purpose:** To provide a clear, neutral white background that makes subtle indicator color changes at the end-point easily visible.\n"
        f"4. **Swirling purpose:** To ensure thorough, instantaneous mixing of reactants so that local excess does not trigger premature color change."
    )

    return {
        "id": f"g12_ps_ab_36_{r.randint(10000, 99999)}",
        "subskill": "36_titration_apparatus_and_procedure",
        "type": "compound",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_app,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "correct_answer": f"Rinse: {target['rinse']}; White tile: see color change clearly",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": f"1. Rinsing of {target['item']}", "prompt": f"Rinsing procedure for {target['item']}.", "expected_answer": target['rinse'], "marks": 1},
            {"part": "2", "label": "2. Reason for rinsing rule", "prompt": "Why this rinsing rule?", "expected_answer": target['wrong_rinse'], "marks": 2},
            {"part": "3", "label": "3. Purpose of white tile", "prompt": "Purpose of white tile.", "expected_answer": "To clearly observe indicator colour change", "marks": 1},
            {"part": "4", "label": "4. Purpose of swirling", "prompt": "Why swirl conical flask?", "expected_answer": "Ensure complete mixing", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct rinsing rule for {target['item']}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Scientific justification of error introduced by incorrect rinsing", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "White tile purpose: detect color change against white background", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Swirling purpose: ensure homogeneous mixing", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Burette & pipette are rinsed with the solution they hold; conical flask is rinsed ONLY with distilled water.",
            "tier_2": "Water droplets inside a burette dilute the solution, changing its concentration.",
            "tier_3": f"{target['rinse']}; white tile enhances color visibility.",
        },
        "misconception_tags": ["conical_flask_rinsing_error", "burette_dilution_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 37: Standard Solution Preparation Calculations
# ==============================================================================
def build_37_standard_solution_preparation(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    standards = [
        {"name": "anhydrous sodium carbonate (Na2CO3)", "formula": r"\text{Na}_2\text{CO}_3", "molar_mass": 105.99, "m_str": r"106{,}0"},
        {"name": "oxalic acid dihydrate (H2C2O4.2H2O)", "formula": r"\text{H}_2\text{C}_2\text{O}_4\cdot 2\text{H}_2\text{O}", "molar_mass": 126.07, "m_str": r"126{,}1"},
        {"name": "sodium hydroxide (NaOH)", "formula": r"\text{NaOH}", "molar_mass": 40.0, "m_str": r"40{,}0"},
    ]
    st = r.choice(standards)
    vol_cm3 = r.choice([250.0, 500.0, 1000.0])
    vol_dm3 = vol_cm3 / 1000.0
    conc = r.choice([0.05, 0.1, 0.15, 0.2, 0.25])
    # m = c * M * V
    mass = round(conc * st["molar_mass"] * vol_dm3, 3)

    prompt = (
        f"A learner prepares a **standard solution** of **{st['name']}**.\n"
        f"The solution must have a volume of **${_fmt_sa(vol_cm3)}\\text{{ cm}}^3$** and a concentration of "
        f"**${_fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** at $25^\\circ\\text{{C}}$.\n\n"
        f"1. Define a **standard solution**.\n"
        f"2. Calculate the mass of ${st['formula']}$ that must be weighed out to prepare this solution.\n"
        f"   (Molar mass of ${st['formula']} = ${st['m_str']}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"3. Name the specific laboratory volumetric glassware required to make up this exact volume."
    )

    sol = (
        f"1. **Standard solution:** A solution of known concentration.\n"
        f"2. **Mass calculation:**\n"
        f"   $$V = \\frac{{{_fmt_sa(vol_cm3)}}}{{1000}} = {_fmt_sa(vol_dm3)}\\text{{ dm}}^3$$\n"
        f"   $$n = c \\times V = {_fmt_sa(conc)} \\times {_fmt_sa(vol_dm3)} = {_fmt_sa(conc * vol_dm3, 4)}\\text{{ mol}}$$\n"
        f"   $$m = n \\times M = {_fmt_sa(conc * vol_dm3, 4)} \\times {st['m_str']} = {_fmt_sa(mass)}\\text{{ g}}$$\n"
        f"3. **Volumetric glassware:** A **${_fmt_sa(vol_cm3)}\\text{{ cm}}^3$ volumetric flask**."
    )

    return {
        "id": f"g12_ps_ab_37_{r.randint(10000, 99999)}",
        "subskill": "37_standard_solution_preparation",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"m = {_fmt_sa(mass)} g in a {_fmt_sa(vol_cm3)} cm3 volumetric flask",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Standard solution definition", "prompt": "Define standard solution.", "expected_answer": "Solution of known concentration", "marks": 2},
            {"part": "2", "label": "2. Calculate mass", "prompt": "Calculate required mass.", "expected_answer": f"{_fmt_sa(mass)} g", "marks": 3},
            {"part": "3", "label": "3. Name volumetric flask", "prompt": "Name required glassware.", "expected_answer": f"{_fmt_sa(vol_cm3)} cm3 volumetric flask", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: solution of precisely known concentration", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Formula n = cV or m = cMV with cm3 to dm3 conversion", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct mass calculation = {_fmt_sa(mass)} g", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Volumetric flask identified", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "volume_unit_conversion_omission", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Standard solution = solution of known concentration.",
            "tier_2": "Convert $\\text{cm}^3$ to $\\text{dm}^3$ by dividing by 1000, then use $m = c \\times M \\times V$.",
            "tier_3": f"$m = {_fmt_sa(conc)} \\times {st['m_str']} \\times {_fmt_sa(vol_dm3)} = {_fmt_sa(mass)}\\text{{ g}}$.",
        },
        "misconception_tags": ["volume_unit_conversion_omission", "standard_solution_definition_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 38: Titration Stoichiometry 1 to 1 (HCl + NaOH)
# ==============================================================================
def build_38_titration_stoichiometry_1_to_1(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    ca = round(r.uniform(0.08, 0.25), 2)
    va = round(r.uniform(18.0, 28.0), 1)
    vb = round(r.choice([20.0, 25.0]), 1)
    # ca * va / na = cb * vb / nb with na=1, nb=1 => cb = ca * va / vb
    cb = round((ca * va) / vb, 3)

    prompt = (
        f"During a matric titration experiment, **${_fmt_sa(va)}\\text{{ cm}}^3$** of a standard "
        f"**${_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** hydrochloric acid ($\\text{{HCl}}$) solution "
        f"completely neutralises **${_fmt_sa(vb)}\\text{{ cm}}^3$** of an aqueous sodium hydroxide ($\\text{{NaOH}}$) solution.\n\n"
        f"$$\\text{{HCl}}(\\text{{aq}}) + \\text{{NaOH}}(\\text{{aq}}) \\rightarrow \\text{{NaCl}}(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}})$$\n\n"
        f"1. State the mole ratio in which $\\text{{HCl}}$ and $\\text{{NaOH}}$ react.\n"
        f"2. Calculate the number of moles of $\\text{{HCl}}$ used in the titration.\n"
        f"3. Calculate the concentration ($c_b$) of the sodium hydroxide solution."
    )

    na_moles = round(ca * (va / 1000.0), 5)

    sol = (
        f"1. **Mole ratio:** $n_a : n_b = 1 : 1$.\n"
        f"2. **Moles of HCl:**\n"
        f"   $$n_a = c_a \\times V_a = {_fmt_sa(ca)} \\times \\frac{{{_fmt_sa(va)}}}{{1000}} = {_fmt_sci(na_moles)}\\text{{ mol}}$$\n"
        f"3. **Base concentration:**\n"
        f"   $$\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{n_a}}{{n_b}} \\implies c_b = \\frac{{c_a V_a n_b}}{{V_b n_a}}$$\n"
        f"   $$c_b = \\frac{{{_fmt_sa(ca)} \\times {_fmt_sa(va)} \\times 1}}{{{_fmt_sa(vb)} \\times 1}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$"
    )

    return {
        "id": f"g12_ps_ab_38_{r.randint(10000, 99999)}",
        "subskill": "38_titration_stoichiometry_1_to_1",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"cb = {_fmt_sa(cb)} mol/dm3",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Stoichiometric mole ratio", "prompt": "State mole ratio.", "expected_answer": "1:1", "marks": 1},
            {"part": "2", "label": "2. Moles of acid used", "prompt": "Calculate moles of HCl.", "expected_answer": _fmt_sci(na_moles), "marks": 2},
            {"part": "3", "label": "3. Base concentration (cb)", "prompt": "Calculate cb.", "expected_answer": f"{_fmt_sa(cb)} mol/dm3", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Mole ratio 1:1 stated", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculation of moles na = caVa", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Correct final cb = {_fmt_sa(cb)} mol/dm3", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Use the standard titration formula: $\\frac{c_a V_a}{c_b V_b} = \\frac{n_a}{n_b}$.",
            "tier_2": "Because $n_a:n_b = 1:1$, volumes can stay in $\\text{cm}^3$ because units cancel.",
            "tier_3": f"$c_b = \\frac{{{_fmt_sa(ca)} \\times {_fmt_sa(va)}}}{{{_fmt_sa(vb)}}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.",
        },
        "misconception_tags": ["titration_formula_substitution_error", "rounding_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 39: Titration Stoichiometry Diprotic Acid (H2SO4 + 2NaOH)
# ==============================================================================
def build_39_titration_stoichiometry_diprotic_acid(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    ca = round(r.uniform(0.05, 0.15), 2)
    va = round(r.uniform(15.0, 25.0), 1)
    vb = round(r.choice([20.0, 25.0]), 1)
    # H2SO4 + 2NaOH -> Na2SO4 + 2H2O => na = 1, nb = 2
    # cb = (ca * va * nb) / (vb * na) = (ca * va * 2) / vb
    cb = round((ca * va * 2.0) / vb, 3)

    prompt = (
        f"A volume of **${_fmt_sa(va)}\\text{{ cm}}^3$** of standard sulphuric acid ($\\text{{H}}_2\\text{{SO}}_4$) "
        f"of concentration **${_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** is required to completely neutralise "
        f"**${_fmt_sa(vb)}\\text{{ cm}}^3$** of a sodium hydroxide ($\\text{{NaOH}}$) solution.\n\n"
        f"$$\\text{{H}}_2\\text{{SO}}_4(\\text{{aq}}) + 2\\text{{NaOH}}(\\text{{aq}}) \\rightarrow \\text{{Na}}_2\\text{{SO}}_4(\\text{{aq}}) + 2\\text{{H}}_2\\text{{O}}(\\text{{l}})$$\n\n"
        f"1. State the stoichiometric mole ratio of acid to base ($n_a : n_b$).\n"
        f"2. Calculate the concentration of the sodium hydroxide solution ($c_b$).\n"
        f"3. Explain what error in $c_b$ would result if a learner failed to account for the diprotic nature of sulphuric acid."
    )

    cb_half = round(cb / 2.0, 3)

    sol = (
        f"1. **Mole ratio:** $n_a : n_b = 1 : 2$ ($1\\text{{ mole of }}\\text{{H}}_2\\text{{SO}}_4$ reacts with $2\\text{{ moles of }}\\text{{NaOH}}$).\n"
        f"2. **Concentration calculation:**\n"
        f"   $$\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{n_a}}{{n_b}} = \\frac{{1}}{{2}}$$\n"
        f"   $$c_b = \\frac{{c_a V_a \\times 2}}{{V_b \\times 1}} = \\frac{{{_fmt_sa(ca)} \\times {_fmt_sa(va)} \\times 2}}{{{_fmt_sa(vb)}}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **Error explanation:** If the diprotic factor of 2 is omitted, $c_b$ would be incorrectly calculated as half of its true value (${_fmt_sa(cb_half)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$)."
    )

    return {
        "id": f"g12_ps_ab_39_{r.randint(10000, 99999)}",
        "subskill": "39_titration_stoichiometry_diprotic_acid",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"cb = {_fmt_sa(cb)} mol/dm3; mole ratio = 1:2",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Stoichiometric mole ratio", "prompt": "State mole ratio na : nb.", "expected_answer": "1:2", "marks": 1},
            {"part": "2", "label": "2. Calculate base concentration (cb)", "prompt": "Calculate cb.", "expected_answer": f"{_fmt_sa(cb)} mol/dm3", "marks": 3},
            {"part": "3", "label": "3. Consequence of omitting diprotic factor", "prompt": "Explain error if factor omitted.", "expected_answer": "cb calculated as half the true value", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Mole ratio 1:2 identified", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula: (caVa)/(cbVb) = na/nb with na=1, nb=2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct cb = {_fmt_sa(cb)} mol/dm3", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Error explanation: cb would be halved", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "inverted_mole_ratio", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Watch the mole ratio: $n_a = 1$, $n_b = 2$.",
            "tier_2": "$\\frac{c_a V_a}{c_b V_b} = \\frac{1}{2} \\implies c_b = \\frac{2 c_a V_a}{V_b}$.",
            "tier_3": f"$c_b = \\frac{{2 \\times {_fmt_sa(ca)} \\times {_fmt_sa(va)}}}{{{_fmt_sa(vb)}}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.",
        },
        "misconception_tags": ["inverted_mole_ratio", "forgot_diprotic_factor_h2so4"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 40: Titration Stoichiometry Dibasic Base / Carbonate (2HCl + Na2CO3)
# ==============================================================================
def build_40_titration_stoichiometry_dibasic_base(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    cb = round(r.uniform(0.08, 0.20), 2)
    vb = round(r.choice([20.0, 25.0]), 1)
    va = round(r.uniform(18.0, 32.0), 1)
    # 2HCl + Na2CO3 -> 2NaCl + H2O + CO2 => na = 2, nb = 1
    # ca = (cb * vb * na) / (va * nb) = (cb * vb * 2) / va
    ca = round((cb * vb * 2.0) / va, 3)

    prompt = (
        f"A standard solution of sodium carbonate ($\\text{{Na}}_2\\text{{CO}}_3$) of concentration "
        f"**${_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** is titrated against an unstandardised "
        f"hydrochloric acid ($\\text{{HCl}}$) solution.\n\n"
        f"$$\\text{{Na}}_2\\text{{CO}}_3(\\text{{aq}}) + 2\\text{{HCl}}(\\text{{aq}}) \\rightarrow 2\\text{{NaCl}}(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}}) + \\text{{CO}}_2(\\text{{g}})$$\n\n"
        f"It is found that **${_fmt_sa(va)}\\text{{ cm}}^3$** of hydrochloric acid is required to completely neutralise "
        f"**${_fmt_sa(vb)}\\text{{ cm}}^3$** of the sodium carbonate solution.\n\n"
        f"1. What visual observation indicates the evolution of gas during this reaction?\n"
        f"2. Calculate the concentration of the hydrochloric acid solution ($c_a$).\n"
        f"3. Name a suitable indicator for this titration."
    )

    sol = (
        f"1. **Visual observation:** Effervescence (bubbling) due to the release of carbon dioxide gas ($\\text{{CO}}_2$).\n"
        f"2. **Concentration calculation:**\n"
        f"   $$\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{n_a}}{{n_b}} = \\frac{{2}}{{1}}$$\n"
        f"   $$c_a = \\frac{{2 \\times c_b V_b}}{{V_a}} = \\frac{{2 \\times {_fmt_sa(cb)} \\times {_fmt_sa(vb)}}}{{{_fmt_sa(va)}}} = {_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **Suitable indicator:** **Methyl orange** (equivalence pH is acidic, ~4–5, due to carbonic acid formed)."
    )

    return {
        "id": f"g12_ps_ab_40_{r.randint(10000, 99999)}",
        "subskill": "40_titration_stoichiometry_dibasic_base",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"ca = {_fmt_sa(ca)} mol/dm3; Indicator: Methyl orange",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Gas observation", "prompt": "State visual observation.", "expected_answer": "Effervescence / bubbling", "marks": 1},
            {"part": "2", "label": "2. Calculate acid concentration (ca)", "prompt": "Calculate ca.", "expected_answer": f"{_fmt_sa(ca)} mol/dm3", "marks": 3},
            {"part": "3", "label": "3. Suitable indicator", "prompt": "Name suitable indicator.", "expected_answer": "Methyl orange", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Effervescence / bubbling identified", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Formula (caVa)/(cbVb) = 2/1", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct ca = {_fmt_sa(ca)} mol/dm3", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Methyl orange identified", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Mole ratio: $n_a = 2$, $n_b = 1$.",
            "tier_2": "$\\frac{c_a V_a}{c_b V_b} = \\frac{2}{1} \\implies c_a = \\frac{2 c_b V_b}{V_a}$.",
            "tier_3": f"$c_a = \\frac{{2 \\times {_fmt_sa(cb)} \\times {_fmt_sa(vb)}}}{{{_fmt_sa(va)}}} = {_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.",
        },
        "misconception_tags": ["carbonate_mole_ratio_error", "indicator_carbonate_titration_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 41: Percentage of Ethanoic Acid in Vinegar
# ==============================================================================
def build_41_vinegar_ethanoic_acid_percentage(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    cb = round(r.uniform(0.1, 0.25), 2)
    vb = round(r.uniform(18.0, 26.0), 1)
    v_vinegar = 20.0
    # CH3COOH + NaOH -> CH3COONa + H2O
    # ca = cb * vb / v_vinegar
    ca = round((cb * vb) / v_vinegar, 3)
    # Molar mass of CH3COOH = 60.05 g/mol
    m_per_dm3 = ca * 60.05
    # % (m/v) = mass in 100 cm3 = (m_per_dm3 / 10)
    percent_mv = round(m_per_dm3 / 10.0, 2)

    prompt = (
        f"A chemist titrates commercial white vinegar to determine its ethanoic acid ($\\text{{CH}}_3\\text{{COOH}}$) content.\n"
        f"A sample of **${_fmt_sa(v_vinegar)}\\text{{ cm}}^3$** of vinegar is placed in a conical flask and titrated with standard "
        f"**${_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** sodium hydroxide ($\\text{{NaOH}}$) using phenolphthalein.\n"
        f"The end-point is reached when **${_fmt_sa(vb)}\\text{{ cm}}^3$** of $\\text{{NaOH}}$ has been added.\n\n"
        f"$$\\text{{CH}}_3\\text{{COOH}}(\\text{{aq}}) + \\text{{NaOH}}(\\text{{aq}}) \\rightarrow \\text{{CH}}_3\\text{{COONa}}(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}})$$\n\n"
        f"1. Calculate the concentration of ethanoic acid in the vinegar ($c_a$) in $\\text{{mol}}\\cdot\\text{{dm}}^{{-3}}$.\n"
        f"2. Calculate the mass of ethanoic acid present in $100\\text{{ cm}}^3$ of vinegar (molar mass of $\\text{{CH}}_3\\text{{COOH}} = 60{{,}}05\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$).\n"
        f"3. Hence, determine the percentage $(\\text{{m/v}})$ of ethanoic acid in the vinegar."
    )

    sol = (
        f"1. **Ethanoic acid concentration:**\n"
        f"   $$c_a = \\frac{{c_b V_b}}{{V_a}} = \\frac{{{_fmt_sa(cb)} \\times {_fmt_sa(vb)}}}{{{_fmt_sa(v_vinegar)}}} = {_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"2. **Mass in $100\\text{{ cm}}^3$ ($0{{,}}1\\text{{ dm}}^3$):**\n"
        f"   $$n = c_a \\times V = {_fmt_sa(ca)} \\times 0{{,}}1 = {_fmt_sa(ca * 0.1, 4)}\\text{{ mol}}$$\n"
        f"   $$m = n \\times M = {_fmt_sa(ca * 0.1, 4)} \\times 60{{,}}05 = {_fmt_sa(percent_mv)}\\text{{ g}}$$\n"
        f"3. **Percentage $(\\text{{m/v}})$:**\n"
        f"   $$\\%(\\text{{m/v}}) = \\frac{{\\text{{mass (g)}}}}{{100\\text{{ cm}}^3}} \\times 100 = {_fmt_sa(percent_mv)}\\%$$"
    )

    return {
        "id": f"g12_ps_ab_41_{r.randint(10000, 99999)}",
        "subskill": "41_vinegar_ethanoic_acid_percentage",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"ca = {_fmt_sa(ca)} mol/dm3; % (m/v) = {_fmt_sa(percent_mv)}%",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Concentration of ethanoic acid", "prompt": "Calculate ca.", "expected_answer": f"{_fmt_sa(ca)} mol/dm3", "marks": 2},
            {"part": "2", "label": "2. Mass in 100 cm3", "prompt": "Calculate mass in 100 cm3.", "expected_answer": f"{_fmt_sa(percent_mv)} g", "marks": 2},
            {"part": "3", "label": "3. Percentage (m/v)", "prompt": "Determine % (m/v).", "expected_answer": f"{_fmt_sa(percent_mv)}%", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Concentration ca = {_fmt_sa(ca)} mol/dm3", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Moles and mass in 100 cm3 = {_fmt_sa(percent_mv)} g", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Final % (m/v) = {_fmt_sa(percent_mv)}%", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Titration gives $c_a$. Then find mass of solute in 100 cm3 of solution.",
            "tier_2": "$m = c \\times V \\times M$, with $V = 0{{,}}1\\text{ dm}^3$.",
            "tier_3": f"$c_a = {_fmt_sa(ca)}$; mass in 100 cm3 = {_fmt_sa(percent_mv)} g = {_fmt_sa(percent_mv)}%.",
        },
        "misconception_tags": ["percent_mv_definition_error", "vinegar_molar_mass_omission"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 42: Oxalic Acid Standardization of NaOH
# ==============================================================================
def build_42_oxalic_acid_standard_titration(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    mass_oxalic = round(r.uniform(1.4, 2.8), 2)
    flask_vol_cm3 = 250.0
    # Molar mass H2C2O4.2H2O = 126.07 g/mol
    n_oxalic_total = mass_oxalic / 126.07
    ca = round(n_oxalic_total / (flask_vol_cm3 / 1000.0), 4)

    va = 25.0
    vb = round(r.uniform(20.0, 28.0), 1)
    # H2C2O4 + 2NaOH -> Na2C2O4 + 2H2O
    # cb = (2 * ca * va) / vb
    cb = round((2.0 * ca * va) / vb, 3)

    prompt = (
        f"A primary standard solution of oxalic acid dihydrate ($\\text{{H}}_2\\text{{C}}_2\\text{{O}}_4\\cdot 2\\text{{H}}_2\\text{{O}}$, "
        f"$M = 126{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) is prepared by dissolving **${_fmt_sa(mass_oxalic)}\\text{{ g}}$** "
        f"of pure solid in distilled water in a **$250\\text{{ cm}}^3$** volumetric flask.\n\n"
        f"An aliquot of **$25{{,}}0\\text{{ cm}}^3$** of this standard oxalic acid solution is pipetted into a conical flask and titrated against "
        f"an unstandardised $\\text{{NaOH}}$ solution. An average titre of **${_fmt_sa(vb)}\\text{{ cm}}^3$** of $\\text{{NaOH}}$ is required to reach the end-point.\n\n"
        f"$$\\text{{H}}_2\\text{{C}}_2\\text{{O}}_4(\\text{{aq}}) + 2\\text{{NaOH}}(\\text{{aq}}) \\rightarrow \\text{{Na}}_2\\text{{C}}_2\\text{{O}}_4(\\text{{aq}}) + 2\\text{{H}}_2\\text{{O}}(\\text{{l}})$$\n\n"
        f"1. Calculate the exact concentration ($c_a$) of the oxalic acid standard solution.\n"
        f"2. Calculate the exact concentration ($c_b$) of the standardised sodium hydroxide solution."
    )

    sol = (
        f"1. **Standard oxalic acid concentration:**\n"
        f"   $$n_a = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(mass_oxalic)}}}{{126{{,}}1}} = {_fmt_sa(n_oxalic_total, 5)}\\text{{ mol}}$$\n"
        f"   $$c_a = \\frac{{n_a}}{{V}} = \\frac{{{_fmt_sa(n_oxalic_total, 5)}}}{{0{{,}}25}} = {_fmt_sa(ca, 4)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"2. **NaOH concentration:**\n"
        f"   $$\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{1}}{{2}} \\implies c_b = \\frac{{2 c_a V_a}}{{V_b}}$$\n"
        f"   $$c_b = \\frac{{2 \\times {_fmt_sa(ca, 4)} \\times 25{{,}}0}}{{{_fmt_sa(vb)}}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$"
    )

    return {
        "id": f"g12_ps_ab_42_{r.randint(10000, 99999)}",
        "subskill": "42_oxalic_acid_standard_titration",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"ca = {_fmt_sa(ca, 4)} mol/dm3; cb = {_fmt_sa(cb)} mol/dm3",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Standard oxalic acid concentration", "prompt": "Calculate ca.", "expected_answer": f"{_fmt_sa(ca, 4)} mol/dm3", "marks": 3},
            {"part": "2", "label": "2. Standardised NaOH concentration", "prompt": "Calculate cb.", "expected_answer": f"{_fmt_sa(cb)} mol/dm3", "marks": 3},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Calculation of moles na = m/M", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Concentration ca = {_fmt_sa(ca, 4)} mol/dm3", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Titration stoichiometry with 1:2 mole ratio", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final cb = {_fmt_sa(cb)} mol/dm3", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_dihydrate_water_mass", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Step 1: Calculate $c_a = m / (M \\times V)$. Step 2: Use $\\frac{c_a V_a}{c_b V_b} = \\frac{1}{2}$.",
            "tier_2": "Remember that oxalic acid is diprotic ($n_a = 1, n_b = 2$).",
            "tier_3": f"$c_a = {_fmt_sa(ca, 4)}$; $c_b = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$.",
        },
        "misconception_tags": ["omitted_dihydrate_water_mass", "inverted_mole_ratio"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 43: Antacid Neutralisation Capacity
# ==============================================================================
def build_43_antacid_neutralisation_capacity(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    antacids = [
        {"name": "sodium bicarbonate (baking soda, NaHCO3)", "formula": r"\text{NaHCO}_3", "molar_mass": 84.01, "eq": r"\text{NaHCO}_3(\text{s}) + \text{HCl}(\text{aq}) \rightarrow \text{NaCl}(\text{aq}) + \text{H}_2\text{O}(\text{l}) + \text{CO}_2(\text{g})", "ratio": 1},
        {"name": "milk of magnesia (Mg(OH)2)", "formula": r"\text{Mg(OH)}_2", "molar_mass": 58.32, "eq": r"\text{Mg(OH)}_2(\text{s}) + 2\text{HCl}(\text{aq}) \rightarrow \text{MgCl}_2(\text{aq}) + 2\text{H}_2\text{O}(\text{l})", "ratio": 2},
        {"name": "calcium carbonate (CaCO3)", "formula": r"\text{CaCO}_3", "molar_mass": 100.09, "eq": r"\text{CaCO}_3(\text{s}) + 2\text{HCl}(\text{aq}) \rightarrow \text{CaCl}_2(\text{aq}) + \text{H}_2\text{O}(\text{l}) + \text{CO}_2(\text{g})", "ratio": 2},
    ]
    ant = r.choice(antacids)
    tablet_mass_g = round(r.uniform(0.5, 1.2), 2)
    c_stomach = 0.1  # mol/dm3 stomach acid
    # n_base = mass / molar_mass
    n_base = tablet_mass_g / ant["molar_mass"]
    n_acid = n_base * ant["ratio"]
    v_acid_dm3 = n_acid / c_stomach
    v_acid_cm3 = round(v_acid_dm3 * 1000.0, 1)

    prompt = (
        f"A learner suffering from heartburn takes an antacid tablet containing **${_fmt_sa(tablet_mass_g)}\\text{{ g}}$** "
        f"of active **{ant['name']}**.\n\n"
        f"$${ant['eq']}$$\n\n"
        f"Hydrochloric acid in the stomach has an average concentration of **$0{{,}}1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**.\n\n"
        f"1. Calculate the number of moles of ${ant['formula']}$ in one tablet.\n"
        f"2. Calculate the volume of stomach acid (in $\\text{{cm}}^3$) that one tablet can neutralise.\n"
        f"3. Explain why taking an excessive overdose of antacids is undesirable for digestive health."
    )

    sol = (
        f"1. **Moles of base:**\n"
        f"   $$n_{{\\text{{base}}}} = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(tablet_mass_g)}}}{{{_fmt_sa(ant['molar_mass'])}}} = {_fmt_sci(n_base)}\\text{{ mol}}$$\n"
        f"2. **Volume of stomach acid neutralised:**\n"
        f"   Mole ratio: $n_{{\\text{{acid}}}} = {ant['ratio']} \\times n_{{\\text{{base}}}} = {_fmt_sci(n_acid)}\\text{{ mol}}$\n"
        f"   $$V_{{\\text{{acid}}}} = \\frac{{n_{{\\text{{acid}}}}}}{{c}} = \\frac{{{_fmt_sci(n_acid)}}}{{0{{,}}1}} = {_fmt_sa(v_acid_dm3, 4)}\\text{{ dm}}^3 = {_fmt_sa(v_acid_cm3)}\\text{{ cm}}^3$$\n"
        f"3. **Overdose effect:** Stomach acid ($\text{{HCl}}$) is biologically required to activate digestive enzymes (pepsin) "
        f"and destroy harmful ingested bacteria. Neutralising all stomach acid impairs digestion and increases vulnerability to gastric infections."
    )

    return {
        "id": f"g12_ps_ab_43_{r.randint(10000, 99999)}",
        "subskill": "43_antacid_neutralisation_capacity",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Volume neutralised = {_fmt_sa(v_acid_cm3)} cm3",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Moles of active ingredient", "prompt": "Calculate moles of base.", "expected_answer": _fmt_sci(n_base), "marks": 2},
            {"part": "2", "label": "2. Volume of stomach acid", "prompt": "Calculate volume of HCl neutralised.", "expected_answer": f"{_fmt_sa(v_acid_cm3)} cm3", "marks": 3},
            {"part": "3", "label": "3. Overdose consequence", "prompt": "Why is antacid overdose harmful?", "expected_answer": "Inactivates digestive enzymes and removes antibacterial barrier", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Calculation of moles n = m/M", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Mole ratio applied correctly to find moles of HCl", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Volume calculation V = n/c = {_fmt_sa(v_acid_cm3)} cm3", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Overdose consequence on enzyme activation / digestion", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Find moles of antacid active ingredient first: $n = m / M$.",
            "tier_2": f"Use the balanced equation: $1\\text{{ mol base}}$ neutralises ${ant['ratio']}\\text{{ mol HCl}}$.",
            "tier_3": f"Volume = {_fmt_sa(v_acid_cm3)} cm3.",
        },
        "misconception_tags": ["antacid_mole_ratio_error", "unit_conversion_dm3_to_cm3_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 44: Excess Reagent Mixture pH Calculation
# ==============================================================================
def build_44_excess_acid_base_mixture_ph(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    # Mixture of strong acid (HCl) and strong base (NaOH)
    va = round(r.uniform(20.0, 40.0), 1)
    vb = round(r.uniform(20.0, 40.0), 1)
    ca = round(r.uniform(0.1, 0.3), 2)
    cb = round(r.uniform(0.1, 0.3), 2)

    na = ca * (va / 1000.0)
    nb = cb * (vb / 1000.0)
    v_total = (va + vb) / 1000.0

    if na > nb:
        excess_moles = na - nb
        c_excess = excess_moles / v_total
        ph = round(-math.log10(c_excess), 2)
        excess_species = "hydrochloric acid (HCl)"
        prompt = (
            f"A learner mixes **${_fmt_sa(va)}\\text{{ cm}}^3$** of **${_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** $\\text{{HCl}}$ "
            f"with **${_fmt_sa(vb)}\\text{{ cm}}^3$** of **${_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** $\\text{{NaOH}}$ at $25^\\circ\\text{{C}}$.\n\n"
            f"1. Determine which reactant is in **excess**.\n"
            f"2. Calculate the number of moles of excess reactant remaining unreacted.\n"
            f"3. Calculate the pH of the resulting mixture."
        )
        sol = (
            f"1. **Moles of reactants:**\n"
            f"   $$n_a = c_a V_a = {_fmt_sa(ca)} \\times {_fmt_sa(va / 1000.0, 4)} = {_fmt_sci(na)}\\text{{ mol}}$$\n"
            f"   $$n_b = c_b V_b = {_fmt_sa(cb)} \\times {_fmt_sa(vb / 1000.0, 4)} = {_fmt_sci(nb)}\\text{{ mol}}$$\n"
            f"   Since $n_a > n_b$, **{excess_species}** is in excess.\n"
            f"2. **Excess moles:**\n"
            f"   $$n_{{\\text{{excess}}}} = n_a - n_b = {_fmt_sci(excess_moles)}\\text{{ mol}}$$\n"
            f"3. **Final pH:**\n"
            f"   $$V_{{\\text{{total}}}} = {_fmt_sa(va)} + {_fmt_sa(vb)} = {_fmt_sa(va + vb)}\\text{{ cm}}^3 = {_fmt_sa(v_total, 4)}\\text{{ dm}}^3$$\n"
            f"   $$[\\text{{H}}_3\\text{{O}}^+] = \\frac{{n_{{\\text{{excess}}}}}}{{V_{{\\text{{total}}}}}} = {_fmt_sa(c_excess, 4)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
            f"   $$\\text{{pH}} = -\\log({_fmt_sa(c_excess, 4)}) = {_fmt_sa(ph)}$$"
        )
    else:
        excess_moles = nb - na
        c_excess = excess_moles / v_total
        h3o = 1.0e-14 / c_excess
        ph = round(-math.log10(h3o), 2)
        excess_species = "sodium hydroxide (NaOH)"
        prompt = (
            f"A learner mixes **${_fmt_sa(va)}\\text{{ cm}}^3$** of **${_fmt_sa(ca)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** $\\text{{HCl}}$ "
            f"with **${_fmt_sa(vb)}\\text{{ cm}}^3$** of **${_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** $\\text{{NaOH}}$ at $25^\\circ\\text{{C}}$.\n\n"
            f"1. Determine which reactant is in **excess**.\n"
            f"2. Calculate the number of moles of excess reactant remaining unreacted.\n"
            f"3. Calculate the pH of the resulting mixture."
        )
        sol = (
            f"1. **Moles of reactants:**\n"
            f"   $$n_a = c_a V_a = {_fmt_sa(ca)} \\times {_fmt_sa(va / 1000.0, 4)} = {_fmt_sci(na)}\\text{{ mol}}$$\n"
            f"   $$n_b = c_b V_b = {_fmt_sa(cb)} \\times {_fmt_sa(vb / 1000.0, 4)} = {_fmt_sci(nb)}\\text{{ mol}}$$\n"
            f"   Since $n_b > n_a$, **{excess_species}** is in excess.\n"
            f"2. **Excess moles:**\n"
            f"   $$n_{{\\text{{excess}}}} = n_b - n_a = {_fmt_sci(excess_moles)}\\text{{ mol}}$$\n"
            f"3. **Final pH:**\n"
            f"   $$V_{{\\text{{total}}}} = {_fmt_sa(va)} + {_fmt_sa(vb)} = {_fmt_sa(va + vb)}\\text{{ cm}}^3 = {_fmt_sa(v_total, 4)}\\text{{ dm}}^3$$\n"
            f"   $$[\\text{{OH}}^-] = \\frac{{n_{{\\text{{excess}}}}}}{{V_{{\\text{{total}}}}}} = {_fmt_sa(c_excess, 4)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
            f"   $$[\\text{{H}}_3\\text{{O}}^+] = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sa(c_excess, 4)}}} = {_fmt_sci(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
            f"   $$\\text{{pH}} = {_fmt_sa(ph)}$$"
        )

    return {
        "id": f"g12_ps_ab_44_{r.randint(10000, 99999)}",
        "subskill": "44_excess_acid_base_mixture_ph",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Excess: {excess_species}; pH = {_fmt_sa(ph)}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Identify excess reactant", "prompt": "Which reactant is in excess?", "expected_answer": excess_species, "marks": 2},
            {"part": "2", "label": "2. Moles of excess", "prompt": "Calculate moles in excess.", "expected_answer": _fmt_sci(excess_moles), "marks": 2},
            {"part": "3", "label": "3. Final pH", "prompt": "Calculate pH of mixture.", "expected_answer": _fmt_sa(ph), "marks": 3},
        ],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculation of initial moles na and nb and excess identified as {excess_species}", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Calculation of excess moles = {_fmt_sci(excess_moles)}", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Calculation of total volume V_total = Va + Vb", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final pH calculated correctly = {_fmt_sa(ph)}", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "forgot_to_use_total_volume", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Calculate moles of $H^+$ and moles of $OH^-$. Subtract to find excess moles.",
            "tier_2": "Divide excess moles by the TOTAL volume ($V_a + V_b$) in $\\text{dm}^3$.",
            "tier_3": f"Excess: {excess_species}; final $pH = {_fmt_sa(ph)}$.",
        },
        "misconception_tags": ["forgot_to_use_total_volume", "excess_subtraction_order_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 45: Back-Titration of Impure Carbonate
# ==============================================================================
def build_45_back_titration_impure_carbonate(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    mass_sample = round(r.uniform(1.2, 2.5), 2)
    # Impure CaCO3 sample treated with excess HCl
    # Total HCl added: V_acid = 50 cm3, c_acid = 1.0 mol/dm3 => n_acid_init = 0.050 mol
    v_acid_cm3 = 50.0
    c_acid = 1.0
    n_acid_init = c_acid * (v_acid_cm3 / 1000.0)

    # Let purity be between 70% and 92%
    purity = round(r.uniform(70.0, 92.0), 1)
    mass_caco3 = round((purity / 100.0) * mass_sample, 3)
    n_caco3 = mass_caco3 / 100.09
    # CaCO3 + 2HCl -> CaCl2 + H2O + CO2 => n_acid_reacted = 2 * n_caco3
    n_acid_reacted = 2.0 * n_caco3
    n_acid_excess = n_acid_init - n_acid_reacted

    # Excess acid back-titrated with NaOH of c_base = 0.5 mol/dm3
    c_base = 0.5
    v_base_cm3 = round((n_acid_excess / c_base) * 1000.0, 1)

    prompt = (
        f"An impure sample of calcium carbonate ($\\text{{CaCO}}_3$) of mass **${_fmt_sa(mass_sample)}\\text{{ g}}$** "
        f"is treated with **${_fmt_sa(v_acid_cm3)}\\text{{ cm}}^3$** of excess **${_fmt_sa(c_acid)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** "
        f"hydrochloric acid ($\\text{{HCl}}$).\n\n"
        f"$$\\text{{CaCO}}_3(\\text{{s}}) + 2\\text{{HCl}}(\\text{{aq}}) \\rightarrow \\text{{CaCl}}_2(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}}) + \\text{{CO}}_2(\\text{{g}})$$\n\n"
        f"After the reaction ceases, the unreacted excess hydrochloric acid is back-titrated with standard "
        f"**${_fmt_sa(c_base)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** sodium hydroxide ($\\text{{NaOH}}$) solution.\n"
        f"Exactly **${_fmt_sa(v_base_cm3)}\\text{{ cm}}^3$** of $\\text{{NaOH}}$ is required to reach the end-point.\n\n"
        f"1. Calculate the initial number of moles of $\\text{{HCl}}$ added to the sample.\n"
        f"2. Calculate the number of moles of excess $\\text{{HCl}}$ that reacted with $\\text{{NaOH}}$.\n"
        f"3. Calculate the number of moles of $\\text{{HCl}}$ that reacted with $\\text{{CaCO}}_3$.\n"
        f"4. Calculate the percentage purity of the calcium carbonate sample (molar mass of $\\text{{CaCO}}_3 = 100{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$)."
    )

    sol = (
        f"1. **Initial moles of HCl:**\n"
        f"   $$n_{{\\text{{init}}}} = c_a V_a = {_fmt_sa(c_acid)} \\times 0{{,}}050 = {_fmt_sa(n_acid_init, 4)}\\text{{ mol}}$$\n"
        f"2. **Excess moles of HCl:**\n"
        f"   $$n_{{\\text{{excess}}}} = c_b V_b = {_fmt_sa(c_base)} \\times \\frac{{{_fmt_sa(v_base_cm3)}}}{{1000}} = {_fmt_sci(n_acid_excess)}\\text{{ mol}}$$\n"
        f"3. **Moles of HCl reacted with $\\text{{CaCO}}_3$:**\n"
        f"   $$n_{{\\text{{reacted}}}} = n_{{\\text{{init}}}} - n_{{\\text{{excess}}}} = {_fmt_sci(n_acid_reacted)}\\text{{ mol}}$$\n"
        f"4. **Percentage purity:**\n"
        f"   $$n_{{\\text{{CaCO}}_3}} = \\frac{{n_{{\\text{{reacted}}}}}}{{2}} = {_fmt_sci(n_caco3)}\\text{{ mol}}$$\n"
        f"   $$m_{{\\text{{CaCO}}_3}} = n \\times M = {_fmt_sci(n_caco3)} \\times 100{{,}}1 = {_fmt_sa(mass_caco3)}\\text{{ g}}$$\n"
        f"   $$\\% \\text{{ purity}} = \\frac{{{_fmt_sa(mass_caco3)}}}{{{_fmt_sa(mass_sample)}}} \\times 100 = {_fmt_sa(purity)}\\%$$"
    )

    return {
        "id": f"g12_ps_ab_45_{r.randint(10000, 99999)}",
        "subskill": "45_back_titration_impure_carbonate",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Purity = {_fmt_sa(purity)}%",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Initial moles of HCl", "prompt": "Calculate initial moles of HCl.", "expected_answer": _fmt_sa(n_acid_init, 4), "marks": 1},
            {"part": "2", "label": "2. Excess moles of HCl", "prompt": "Calculate excess moles of HCl.", "expected_answer": _fmt_sci(n_acid_excess), "marks": 2},
            {"part": "3", "label": "3. Moles reacted with CaCO3", "prompt": "Calculate moles reacted with sample.", "expected_answer": _fmt_sci(n_acid_reacted), "marks": 1},
            {"part": "4", "label": "4. Percentage purity", "prompt": "Calculate % purity.", "expected_answer": f"{_fmt_sa(purity)}%", "marks": 3},
        ],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": "Initial moles of HCl calculated", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Excess moles from NaOH titration", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Moles reacted = initial - excess", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Factor of 2 applied for CaCO3 and final purity = {_fmt_sa(purity)}%", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Back-titration: $n_{\\text{reacted}} = n_{\\text{initial}} - n_{\\text{excess}}$.",
            "tier_2": "Remember: $1\\text{ mol CaCO}_3$ reacts with $2\\text{ mol HCl}$, so divide $n_{\\text{reacted}}$ by 2.",
            "tier_3": f"Pure mass = {_fmt_sa(mass_caco3)} g; Purity = {_fmt_sa(purity)}%.",
        },
        "misconception_tags": ["back_titration_subtraction_error", "carbonate_factor_of_two_omission"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 46: Back-Titration of Nitrogen in Fertiliser (Kjeldahl Method)
# ==============================================================================
def build_46_back_titration_nitrogen_kjeldahl(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    mass_fert = round(r.uniform(1.0, 2.0), 2)
    percent_n = round(r.uniform(18.0, 32.0), 1)
    mass_n = (percent_n / 100.0) * mass_fert
    # Molar mass of N = 14.01 g/mol
    n_ammonia = mass_n / 14.01

    # Absorbed in 50 cm3 of 0.5 mol/dm3 H2SO4 (diprotic!)
    # Total moles H2SO4 = 0.5 * 0.05 = 0.025 mol
    # 2NH3 + H2SO4 -> (NH4)2SO4 => n_h2so4_reacted = n_ammonia / 2
    n_h2so4_init = 0.025
    n_h2so4_reacted = n_ammonia / 2.0
    n_h2so4_excess = n_h2so4_init - n_h2so4_reacted

    # Titrated with 0.2 mol/dm3 NaOH: H2SO4 + 2NaOH -> Na2SO4 + 2H2O => n_naoh = 2 * n_h2so4_excess
    c_naoh = 0.2
    v_naoh_cm3 = round(((2.0 * n_h2so4_excess) / c_naoh) * 1000.0, 1)

    prompt = (
        f"A chemist analyses the nitrogen content in a fertiliser sample of mass **${_fmt_sa(mass_fert)}\\text{{ g}}$**.\n"
        f"The nitrogen is converted completely into ammonia ($\\text{{NH}}_3$) and distilled into "
        f"**$50{{,}}0\\text{{ cm}}^3$** of **$0{{,}}50\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** sulphuric acid ($\\text{{H}}_2\\text{{SO}}_4$).\n\n"
        f"$$2\\text{{NH}}_3(\\text{{g}}) + \\text{{H}}_2\\text{{SO}}_4(\\text{{aq}}) \\rightarrow (\\text{{NH}}_4)_2\\text{{SO}}_4(\\text{{aq}})$$\n\n"
        f"The unreacted excess sulphuric acid is back-titrated with **$0{{,}}20\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** sodium hydroxide ($\\text{{NaOH}}$).\n"
        f"Exactly **${_fmt_sa(v_naoh_cm3)}\\text{{ cm}}^3$** of $\\text{{NaOH}}$ is required to reach the end-point.\n\n"
        f"1. Calculate the initial number of moles of sulphuric acid.\n"
        f"2. Calculate the number of moles of excess sulphuric acid that reacted with $\\text{{NaOH}}$.\n"
        f"3. Calculate the percentage of nitrogen ($\\%\\text{{N}}$) in the fertiliser sample."
    )

    sol = (
        f"1. **Initial moles of $\\text{{H}}_2\\text{{SO}}_4$:**\n"
        f"   $$n_{{\\text{{init}}}} = c \\times V = 0{{,}}50 \\times 0{{,}}050 = {_fmt_sa(n_h2so4_init, 4)}\\text{{ mol}}$$\n"
        f"2. **Excess moles of $\\text{{H}}_2\\text{{SO}}_4$:**\n"
        f"   $$n_{{\\text{{NaOH}}}} = c_b V_b = 0{{,}}20 \\times \\frac{{{_fmt_sa(v_naoh_cm3)}}}{{1000}} = {_fmt_sci(2.0 * n_h2so4_excess)}\\text{{ mol}}$$\n"
        f"   $$n_{{\\text{{excess}}}} = \\frac{{n_{{\\text{{NaOH}}}}}}{{2}} = {_fmt_sci(n_h2so4_excess)}\\text{{ mol}}$$\n"
        f"3. **Nitrogen content:**\n"
        f"   $$n_{{\\text{{H}}_2\\text{{SO}}_4\\text{{ (reacted)}}}} = n_{{\\text{{init}}}} - n_{{\\text{{excess}}}} = {_fmt_sci(n_h2so4_reacted)}\\text{{ mol}}$$\n"
        f"   $$n_{{\\text{{NH}}_3}} = 2 \\times n_{{\\text{{reacted}}}} = {_fmt_sci(n_ammonia)}\\text{{ mol}}$$\n"
        f"   $$m_{{\\text{{N}}}} = n_{{\\text{{NH}}_3}} \\times 14{{,}}01 = {_fmt_sa(mass_n, 3)}\\text{{ g}}$$\n"
        f"   $$\\%\\text{{N}} = \\frac{{{_fmt_sa(mass_n, 3)}}}{{{_fmt_sa(mass_fert)}}} \\times 100 = {_fmt_sa(percent_n)}\\%$$"
    )

    return {
        "id": f"g12_ps_ab_46_{r.randint(10000, 99999)}",
        "subskill": "46_back_titration_nitrogen_kjeldahl",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"%N = {_fmt_sa(percent_n)}%",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Initial moles of H2SO4", "prompt": "Calculate initial moles of H2SO4.", "expected_answer": _fmt_sa(n_h2so4_init, 4), "marks": 1},
            {"part": "2", "label": "2. Excess moles of H2SO4", "prompt": "Calculate excess moles of H2SO4.", "expected_answer": _fmt_sci(n_h2so4_excess), "marks": 2},
            {"part": "3", "label": "3. Percentage nitrogen", "prompt": "Calculate % N.", "expected_answer": f"{_fmt_sa(percent_n)}%", "marks": 3},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Initial moles of H2SO4 calculated", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Excess moles of H2SO4 calculated accounting for 1:2 ratio with NaOH", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Conversion to moles of N and final %N = {_fmt_sa(percent_n)}%", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Carefully track two 1:2 ratios: $2\\text{NH}_3 : 1\\text{H}_2\\text{SO}_4$ and $1\\text{H}_2\\text{SO}_4 : 2\\text{NaOH}$.",
            "tier_2": "Each mole of $\\text{NH}_3$ contains $14{{,}}01\\text{ g}$ of nitrogen.",
            "tier_3": f"$\\%\\text{{N}} = {_fmt_sa(percent_n)}\\%$.",
        },
        "misconception_tags": ["nitrogen_molar_mass_diatomic_confusion", "diprotic_ratio_confusion"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 47: Acid Rain Environmental Chemistry & Neutralization
# ==============================================================================
def build_47_acid_rain_environmental_impact(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    scenarios = [
        {"pollutant": "sulfur dioxide (SO2)", "eq1": r"\text{SO}_2(\text{g}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{H}_2\text{SO}_3(\text{aq})", "source": "burning of coal in coal-fired power stations"},
        {"pollutant": "nitrogen dioxide (NO2)", "eq1": r"4\text{NO}_2(\text{g}) + 2\text{H}_2\text{O}(\text{l}) + \text{O}_2(\text{g}) \rightarrow 4\text{HNO}_3(\text{aq})", "source": "internal combustion engines in motor vehicles"},
    ]
    sc = r.choice(scenarios)

    prompt = (
        f"Unpolluted rainwater has a natural pH of approximately $5{{,}}6$ due to dissolved atmospheric $\\text{{CO}}_2$.\n"
        f"However, industrial emissions of **{sc['pollutant']}** cause severe **acid rain** with pH levels dropping below $4{{,}}0$.\n\n"
        f"1. Name the primary human activity responsible for atmospheric emissions of {sc['pollutant']}.\n"
        f"2. Write a balanced chemical equation showing how {sc['pollutant']} reacts with atmospheric water/oxygen to form acidic rain.\n"
        f"3. Write a balanced chemical equation showing how acid rain damages marble and limestone buildings ($\\text{{CaCO}}_3$).\n"
        f"4. Name a basic compound commonly added by farmers to neutralise acidic soils (agricultural liming)."
    )

    sol = (
        f"1. **Primary source:** {sc['source']}.\n"
        f"2. **Acid formation equation:**\n"
        f"   $${sc['eq1']}$$\n"
        f"3. **Limestone damage equation:**\n"
        f"   $$\\text{{CaCO}}_3(\\text{{s}}) + 2\\text{{H}}^+(\\text{{aq}}) \\rightarrow \\text{{Ca}}^{{2+}}(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}}) + \\text{{CO}}_2(\\text{{g}})$$\n"
        f"   (The insoluble calcium carbonate is converted into soluble calcium salts, eroding historical stonework).\n"
        f"4. **Agricultural liming agent:** **Calcium oxide (quicklime, $\\text{{CaO}}$)** or **calcium carbonate (limestone, $\\text{{CaCO}}_3$)** or **calcium hydroxide (slaked lime, $\\text{{Ca(OH)}}_2$)**."
    )

    return {
        "id": f"g12_ps_ab_47_{r.randint(10000, 99999)}",
        "subskill": "47_acid_rain_environmental_impact",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Source: {sc['source']}; Eq: {sc['eq1']}; Liming: CaO / CaCO3",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Industrial emission source", "prompt": "Identify emission source.", "expected_answer": sc['source'], "marks": 1},
            {"part": "2", "label": "2. Acid formation equation", "prompt": "Write acid rain equation.", "expected_answer": sc['eq1'], "marks": 2},
            {"part": "3", "label": "3. Limestone corrosion equation", "prompt": "Write limestone corrosion equation.", "expected_answer": "CaCO3 + 2H+ -> Ca2+ + H2O + CO2", "marks": 2},
            {"part": "4", "label": "4. Agricultural liming agent", "prompt": "Name soil liming agent.", "expected_answer": "Calcium oxide (CaO) or calcium carbonate (CaCO3)", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Emission source correctly identified", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Balanced equation for acid rain formation", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Balanced equation for acid-carbonate reaction eroding limestone", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Agricultural liming compound named", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Acid rain dissolves limestone (calcium carbonate) by forming carbon dioxide gas and water.",
            "tier_2": "Farmers neutralise acidic soils by spreading lime (CaO or $\\text{CaCO}_3$).",
            "tier_3": f"{sc['eq1']}; Liming agent: $\\text{{CaO}}$ or $\\text{{CaCO}}_3$.",
        },
        "misconception_tags": ["acid_rain_limestone_reaction_error", "natural_rain_ph_misconception"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 48: Chloralkali Industry Applications
# ==============================================================================
def build_48_chloralkali_industry_applications(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    temps = [
        {"cond": "cold (below 60°C)", "product": "sodium hypochlorite (NaClO)", "eq": r"\text{Cl}_2(\text{g}) + 2\text{NaOH}(\text{aq}) \rightarrow \text{NaCl}(\text{aq}) + \text{NaClO}(\text{aq}) + \text{H}_2\text{O}(\text{l})", "use": "household bleach and municipal water disinfection"},
        {"cond": "hot (above 60°C)", "product": "sodium chlorate (NaClO3)", "eq": r"3\text{Cl}_2(\text{g}) + 6\text{NaOH}(\text{aq}) \rightarrow 5\text{NaCl}(\text{aq}) + \text{NaClO}_3(\text{aq}) + 3\text{H}_2\text{O}(\text{l})", "use": "herbicide and chemical oxygen generation"},
    ]
    t = r.choice(temps)

    prompt = (
        f"The **chloralkali industry** produces chlorine ($\\text{{Cl}}_2$), hydrogen ($\\text{{H}}_2$), and sodium hydroxide ($\\text{{NaOH}}$) "
        f"via the electrolysis of concentrated aqueous brine ($\\text{{NaCl}}$):\n\n"
        f"$$2\\text{{NaCl}}(\\text{{aq}}) + 2\\text{{H}}_2\\text{{O}}(\\text{{l}}) \\rightarrow \\text{{Cl}}_2(\\text{{g}}) + \\text{{H}}_2(\\text{{g}}) + 2\\text{{NaOH}}(\\text{{aq}})$$\n\n"
        f"When chlorine gas is reacted with aqueous sodium hydroxide under **{t['cond']}** conditions, a disproportionation reaction occurs.\n\n"
        f"1. Write down the balanced chemical equation for the reaction of $\\text{{Cl}}_2$ with $\\text{{NaOH}}$ under these conditions.\n"
        f"2. Name the major commercial chlorine-containing product (**{t['product']}**).\n"
        f"3. State one major industrial or domestic application of this product."
    )

    sol = (
        f"1. **Balanced equation:**\n"
        f"   $${t['eq']}$$\n"
        f"2. **Product name:** **{t['product']}**.\n"
        f"3. **Application:** {t['use']}."
    )

    return {
        "id": f"g12_ps_ab_48_{r.randint(10000, 99999)}",
        "subskill": "48_chloralkali_industry_applications",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Product: {t['product']}; Eq: {t['eq']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Disproportionation reaction equation", "prompt": "Write balanced equation.", "expected_answer": t['eq'], "marks": 2},
            {"part": "2", "label": "2. Name product", "prompt": "Name product.", "expected_answer": t['product'], "marks": 1},
            {"part": "3", "label": "3. State commercial application", "prompt": "State application.", "expected_answer": t['use'], "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Balanced equation with correct coefficients and states", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Correct commercial product identified: {t['product']}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Valid application: {t['use']}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Under 60°C produces bleach ($\text{NaClO}$); above 60°C produces chlorate ($\text{NaClO}_3$).",
            "tier_2": "Chlorine is both oxidised and reduced in this reaction (disproportionation).",
            "tier_3": f"${t['eq']}$; application: {t['use']}.",
        },
        "misconception_tags": ["chloralkali_reaction_conditions_confusion", "bleach_formula_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 49: Hair Cosmetics Acid-Base Chemistry (Perms and Relaxers)
# ==============================================================================
def build_49_hair_cosmetics_acid_base_chemistry(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    categories = [
        {"type": "lye hair relaxer", "base": "Sodium hydroxide (NaOH)", "ph_range": "12 - 14", "mechanism": "high pH causes rapid swelling and alkaline hydrolysis of keratin peptide bonds and cystine bridges"},
        {"type": "no-lye hair relaxer", "base": "Guanidine hydroxide (from Ca(OH)2 + guanidine carbonate)", "ph_range": "9 - 11", "mechanism": "milder alkaline environment that reduces cystine while reducing scalp burning, but causes calcium buildup"},
    ]
    cat = r.choice(categories)

    prompt = (
        f"Human hair is primarily composed of the protein **keratin**, which has a natural acidic pH mantle between $4$ and $5$.\n"
        f"Commercial hair relaxers alter this structure using strong alkalis.\n\n"
        f"1. Consider a **{cat['type']}**:\n"
        f"   - Name the active basic ingredient.\n"
        f"   - State the typical pH range of this product.\n"
        f"2. Explain chemically how the basic pH alters the sulfur-sulfur disulphide bonds in **cystine**.\n"
        f"3. In permanent waving (perming), why is a neutralising treatment of hydrogen peroxide ($\\text{{H}}_2\\text{{O}}_2$) applied after ammonium thioglycolate?"
    )

    sol = (
        f"1. **{cat['type']}:**\n"
        f"   - Active basic ingredient: **{cat['base']}**\n"
        f"   - Operating pH range: **pH {cat['ph_range']}**\n"
        f"2. **Mechanism on disulphide bonds:** {cat['mechanism']}. "
        f"The high hydroxide concentration breaks disulphide cross-links (reducing cystine to cysteine), allowing the protein strands to slide and flatten.\n"
        f"3. **Hydrogen peroxide neutraliser role:** $\\text{{H}}_2\\text{{O}}_2$ acts as an oxidising agent. "
        f"It re-oxidises the cysteine amino acid residues back to cystine, re-forming the disulphide ($-S-S-$) covalent cross-links in their new reshaped positions."
    )

    return {
        "id": f"g12_ps_ab_49_{r.randint(10000, 99999)}",
        "subskill": "49_hair_cosmetics_acid_base_chemistry",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Base: {cat['base']}; pH: {cat['ph_range']}; H2O2 re-oxidises disulphide bonds",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Active base and pH range", "prompt": "Name active base and pH range.", "expected_answer": f"{cat['base']}; pH {cat['ph_range']}", "marks": 2},
            {"part": "2", "label": "2. Mechanism on disulphide bonds", "prompt": "How does alkali alter hair?", "expected_answer": "Breaks disulphide bonds / reduces cystine to cysteine", "marks": 2},
            {"part": "3", "label": "3. Role of H2O2 neutraliser", "prompt": "Role of H2O2 in perming?", "expected_answer": "Oxidises cysteine back to cystine to fix new shape", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Active base ({cat['base']}) and pH range ({cat['ph_range']})", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Disulphide bond reduction / cystine to cysteine explained", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "H2O2 identified as oxidising agent reforming disulphide bonds", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Lye relaxers contain NaOH (pH 12–14); no-lye relaxers use guanidine hydroxide (pH 9–11).",
            "tier_2": "Disulphide bonds ($-S-S-$) hold keratin in shape. Perms reduce them; $\\text{H}_2\\text{O}_2$ re-oxidises them.",
            "tier_3": f"{cat['base']}; pH {cat['ph_range']}; $\\text{{H}}_2\\text{{O}}_2$ re-forms disulphide bonds.",
        },
        "misconception_tags": ["hair_keratin_ph_misconception", "h2o2_acid_base_role_confusion"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 50: Capstone NSC Paper 2 Multi-Part Exam Autopsy
# ==============================================================================
def build_50_capstone_exam_titration_autopsy(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    # A full NSC Question 7 exemplar
    m_oxalic = round(r.uniform(3.1, 4.5), 2)
    vol_standard_flask = 500.0  # cm3
    c_oxalic = round(m_oxalic / (126.07 * (vol_standard_flask / 1000.0)), 4)

    v_pipette = 25.0
    v_titre = round(r.uniform(21.0, 29.0), 1)
    # H2C2O4 + 2NaOH -> Na2C2O4 + 2H2O => cb = (2 * ca * va) / vb
    cb = round((2.0 * c_oxalic * v_pipette) / v_titre, 3)

    prompt = (
        f"**QUESTION 7 (NSC Chemistry Examination Simulation)**\n\n"
        f"7.1 A matric learner prepares a primary standard solution of oxalic acid dihydrate ($\\text{{H}}_2\\text{{C}}_2\\text{{O}}_4\\cdot 2\\text{{H}}_2\\text{{O}}$, "
        f"$M = 126{{,}}1\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}$) by dissolving **${_fmt_sa(m_oxalic)}\\text{{ g}}$** of pure crystals in distilled water "
        f"to make exactly **$500\\text{{ cm}}^3$** of solution in a volumetric flask.\n"
        f"   7.1.1 Define a *standard solution*.\n"
        f"   7.1.2 Calculate the concentration ($c_a$) of this oxalic acid standard solution.\n\n"
        f"7.2 The learner pipettes **$25{{,}}0\\text{{ cm}}^3$** of this standard oxalic acid solution into a conical flask and titrates it against "
        f"an unstandardised sodium hydroxide ($\\text{{NaOH}}$) solution. An average volume of **${_fmt_sa(v_titre)}\\text{{ cm}}^3$** of $\\text{{NaOH}}$ is required to reach the end-point.\n\n"
        f"$$\\text{{H}}_2\\text{{C}}_2\\text{{O}}_4(\\text{{aq}}) + 2\\text{{NaOH}}(\\text{{aq}}) \\rightarrow \\text{{Na}}_2\\text{{C}}_2\\text{{O}}_4(\\text{{aq}}) + 2\\text{{H}}_2\\text{{O}}(\\text{{l}})$$\n\n"
        f"   7.2.1 Calculate the concentration of the sodium hydroxide solution ($c_b$).\n"
        f"   7.2.2 Choose the most suitable indicator for this titration: *bromothymol blue* or *phenolphthalein*.\n"
        f"   7.2.3 Explain your choice in 7.2.2 with reference to the hydrolysis of the salt formed at the equivalence point."
    )

    sol = (
        f"7.1.1 **Standard solution:** A solution of known concentration.\n"
        f"7.1.2 **Concentration of oxalic acid:**\n"
        f"      $$n = \\frac{{m}}{{M}} = \\frac{{{_fmt_sa(m_oxalic)}}}{{126{{,}}1}} = {_fmt_sa(m_oxalic / 126.07, 4)}\\text{{ mol}}$$\n"
        f"      $$c_a = \\frac{{n}}{{V}} = \\frac{{{_fmt_sa(m_oxalic / 126.07, 4)}}}{{0{{,}}500}} = {_fmt_sa(c_oxalic, 4)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n\n"
        f"7.2.1 **Concentration of NaOH ($c_b$):**\n"
        f"      $$\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{n_a}}{{n_b}} = \\frac{{1}}{{2}}$$\n"
        f"      $$c_b = \\frac{{2 \\times c_a V_a}}{{V_b}} = \\frac{{2 \\times {_fmt_sa(c_oxalic, 4)} \\times 25{{,}}0}}{{{_fmt_sa(v_titre)}}} = {_fmt_sa(cb)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"7.2.2 **Indicator:** **Phenolphthalein**.\n"
        f"7.2.3 **Justification:** This is a weak diprotic acid titrated against a strong base. "
        f"The salt formed, sodium oxalate ($\\text{{Na}}_2\\text{{C}}_2\\text{{O}}_4$), undergoes anion hydrolysis in water "
        f"($\\text{{C}}_2\\text{{O}}_4^{{2-}} + \\text{{H}}_2\\text{{O}} \\rightleftharpoons \\text{{HC}}_2\\text{{O}}_4^- + \\text{{OH}}^-$), "
        f"producing excess $\\text{{OH}}^-$ ions and creating an equivalence point pH in the basic range (pH 8–9). "
        f"Phenolphthalein is suitable because its pH range ($8{{,}}3 - 10{{,}}0$) encompasses this basic equivalence point."
    )

    return {
        "id": f"g12_ps_ab_50_{r.randint(10000, 99999)}",
        "subskill": "50_capstone_exam_titration_autopsy",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"ca = {_fmt_sa(c_oxalic, 4)} mol/dm3; cb = {_fmt_sa(cb)} mol/dm3; Indicator: Phenolphthalein",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "7.1.1", "label": "7.1.1 Standard solution definition", "prompt": "Define standard solution.", "expected_answer": "Solution of known concentration", "marks": 2},
            {"part": "7.1.2", "label": "7.1.2 Oxalic acid concentration", "prompt": "Calculate ca.", "expected_answer": f"{_fmt_sa(c_oxalic, 4)} mol/dm3", "marks": 3},
            {"part": "7.2.1", "label": "7.2.1 NaOH concentration", "prompt": "Calculate cb.", "expected_answer": f"{_fmt_sa(cb)} mol/dm3", "marks": 3},
            {"part": "7.2.2", "label": "7.2.2 Suitable indicator", "prompt": "Choose indicator.", "expected_answer": "Phenolphthalein", "marks": 1},
            {"part": "7.2.3", "label": "7.2.3 Salt hydrolysis justification", "prompt": "Justify indicator choice via salt hydrolysis.", "expected_answer": "Anion hydrolysis produces basic pH 8-9 matching phenolphthalein range", "marks": 3},
        ],
        "marking_schema": {
            "total_marks": 12,
            "marking_points": [
                {"id": "mp1", "desc": "Standard solution definition", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Calculation of moles of oxalic acid and ca", "marks": 3, "editable": True},
                {"id": "mp3", "desc": f"Titration formula with 1:2 mole ratio and cb = {_fmt_sa(cb)} mol/dm3", "marks": 3, "editable": True},
                {"id": "mp4", "desc": "Phenolphthalein chosen", "marks": 1, "editable": True},
                {"id": "mp5", "desc": "Anion hydrolysis equation/explanation producing basic pH matching phenolphthalein range", "marks": 3, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "This is a full NSC exam question combining standard preparation, titration calculation, and salt hydrolysis.",
            "tier_2": "Mole ratio $n_a:n_b = 1:2$. Anion hydrolysis shifts equivalence pH > 7.",
            "tier_3": f"$c_a = {_fmt_sa(c_oxalic, 4)}$; $c_b = {_fmt_sa(cb)}$; Indicator: Phenolphthalein.",
        },
        "misconception_tags": ["capstone_titration_error", "anion_hydrolysis_omission"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 8,
    }


# ==============================================================================
# Mapping dictionary of builders 26 to 50
# ==============================================================================
BUILDERS_26_50 = {
    "26_salt_hydrolysis_concept_definition": build_26_salt_hydrolysis_concept_definition,
    "27_hydrolysis_neutral_salts": build_27_hydrolysis_neutral_salts,
    "28_hydrolysis_basic_salts": build_28_hydrolysis_basic_salts,
    "29_hydrolysis_acidic_salts": build_29_hydrolysis_acidic_salts,
    "30_predicting_salt_solution_ph": build_30_predicting_salt_solution_ph,
    "31_indicator_selection_rationale": build_31_indicator_selection_rationale,
    "32_indicator_color_transition_equilibrium": build_32_indicator_color_transition_equilibrium,
    "33_titration_curve_strong_acid_strong_base": build_33_titration_curve_strong_acid_strong_base,
    "34_titration_curve_weak_acid_strong_base": build_34_titration_curve_weak_acid_strong_base,
    "35_titration_curve_strong_acid_weak_base": build_35_titration_curve_strong_acid_weak_base,
    "36_titration_apparatus_and_procedure": build_36_titration_apparatus_and_procedure,
    "37_standard_solution_preparation": build_37_standard_solution_preparation,
    "38_titration_stoichiometry_1_to_1": build_38_titration_stoichiometry_1_to_1,
    "39_titration_stoichiometry_diprotic_acid": build_39_titration_stoichiometry_diprotic_acid,
    "40_titration_stoichiometry_dibasic_base": build_40_titration_stoichiometry_dibasic_base,
    "41_vinegar_ethanoic_acid_percentage": build_41_vinegar_ethanoic_acid_percentage,
    "42_oxalic_acid_standard_titration": build_42_oxalic_acid_standard_titration,
    "43_antacid_neutralisation_capacity": build_43_antacid_neutralisation_capacity,
    "44_excess_acid_base_mixture_ph": build_44_excess_acid_base_mixture_ph,
    "45_back_titration_impure_carbonate": build_45_back_titration_impure_carbonate,
    "46_back_titration_nitrogen_kjeldahl": build_46_back_titration_nitrogen_kjeldahl,
    "47_acid_rain_environmental_impact": build_47_acid_rain_environmental_impact,
    "48_chloralkali_industry_applications": build_48_chloralkali_industry_applications,
    "49_hair_cosmetics_acid_base_chemistry": build_49_hair_cosmetics_acid_base_chemistry,
    "50_capstone_exam_titration_autopsy": build_50_capstone_exam_titration_autopsy,
}
