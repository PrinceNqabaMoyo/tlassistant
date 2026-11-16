"""Grade 12 Physical Sciences - Acids and Bases Archetypes (01 to 25).

Subskills 01-25 covering Term 2 Chemistry:
- Theories: Arrhenius and Brønsted-Lowry models of acids and bases.
- Conjugate acid-base pairs in simple, organic, and polyprotic systems.
- Ampholytes (amphiprotic substances) and their dual behavior.
- Auto-protolysis of water and Kw temperature dependence.
- Strong vs weak acids and bases (extent of ionisation/dissociation).
- Concentrated vs dilute solutions and electrical conductivity.
- Equilibrium constants Ka and Kb, expressions, calculations, and ranking.
- Successive ionisation constants for diprotic/polyprotic acids.
- pH and pOH calculations: strong monoprotic, strong diprotic, strong monobasic, strong dibasic.
- Hydronium and hydroxide concentration from pH, water dilution calculations.
- Weak acid and weak base equilibrium pH calculations.

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
    """Format scientific notation with SA comma decimal separator."""
    s = f"{val:.{places}e}"
    base, exp = s.split("e")
    exp_int = int(exp)
    base_fmt = base.replace(".", "{,}")
    return f"{base_fmt} \\times 10^{{{exp_int}}}"


# ==============================================================================
# Subskill 01: Arrhenius Acid & Base Definitions
# ==============================================================================
def build_01_arrhenius_acid_base_definitions(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    substances = [
        {"name": "hydrochloric acid", "formula": r"\text{HCl}", "type": "acid", "ion": r"\text{H}_3\text{O}^+", "eq": r"\text{HCl}(\text{g}) + \text{H}_2\text{O}(\text{l}) \rightarrow \text{H}_3\text{O}^+(\text{aq}) + \text{Cl}^-(\text{aq})"},
        {"name": "nitric acid", "formula": r"\text{HNO}_3", "type": "acid", "ion": r"\text{H}_3\text{O}^+", "eq": r"\text{HNO}_3(\text{l}) + \text{H}_2\text{O}(\text{l}) \rightarrow \text{H}_3\text{O}^+(\text{aq}) + \text{NO}_3^-(\text{aq})"},
        {"name": "sodium hydroxide", "formula": r"\text{NaOH}", "type": "base", "ion": r"\text{OH}^-", "eq": r"\text{NaOH}(\text{s}) \xrightarrow{\text{H}_2\text{O}} \text{Na}^+(\text{aq}) + \text{OH}^-(\text{aq})"},
        {"name": "potassium hydroxide", "formula": r"\text{KOH}", "type": "base", "ion": r"\text{OH}^-", "eq": r"\text{KOH}(\text{s}) \xrightarrow{\text{H}_2\text{O}} \text{K}^+(\text{aq}) + \text{OH}^-(\text{aq})"},
        {"name": "calcium hydroxide", "formula": r"\text{Ca(OH)}_2", "type": "base", "ion": r"\text{OH}^-", "eq": r"\text{Ca(OH)}_2(\text{s}) \xrightarrow{\text{H}_2\text{O}} \text{Ca}^{2+}(\text{aq}) + 2\text{OH}^-(\text{aq})"},
    ]
    sub = r.choice(substances)
    vol = r.choice([250, 500, 750, 1000])

    prompt = (
        f"A chemistry learner dissolves a sample of pure **{sub['name']}** (${sub['formula']}$) in "
        f"${vol}\\text{{ cm}}^3$ of distilled water.\n\n"
        f"1. Define an **Arrhenius {sub['type']}**.\n"
        f"2. Write down a balanced chemical equation showing how ${sub['formula']}$ behaves in aqueous solution.\n"
        f"3. Explain why the Arrhenius model cannot explain acid-base behavior in non-aqueous solvents (e.g. gaseous reactions)."
    )

    if sub['type'] == 'acid':
        def_text = "An Arrhenius acid is a substance that forms hydronium ions (H3O+) when dissolved in water (increases [H3O+])."
    else:
        def_text = "An Arrhenius base is a substance that forms hydroxide ions (OH-) when dissolved in water (increases [OH-])."

    sol = (
        f"1. **Arrhenius {sub['type']} definition:** {def_text}\n"
        f"2. **Dissociation / ionisation equation:**\n"
        f"   $${sub['eq']}$$\n"
        f"3. **Limitation:** The Arrhenius definition is restricted strictly to aqueous solutions where water is the solvent. "
        f"It cannot account for acid-base neutralisation in the gas phase (e.g. $\\text{{NH}}_3(\\text{{g}}) + \\text{{HCl}}(\\text{{g}}) \\rightarrow \\text{{NH}}_4\\text{{Cl}}(\\text{{s}})$) "
        f"or in non-aqueous solvents where no free $\\text{{OH}}^-$ or $\\text{{H}}_3\\text{{O}}^+$ ions are produced."
    )

    return {
        "id": f"g12_ps_ab_01_{r.randint(10000, 99999)}",
        "subskill": "01_arrhenius_acid_base_definitions",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Arrhenius {sub['type']}: increases [{sub['ion']}] in water; Eq: {sub['eq']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": f"1. Arrhenius {sub['type']} definition", "prompt": f"Define an Arrhenius {sub['type']}.", "expected_answer": def_text, "marks": 2},
            {"part": "2", "label": f"2. Dissociation equation for {sub['formula']}", "prompt": "Write a balanced equation for the dissolution.", "expected_answer": sub['eq'], "marks": 2},
            {"part": "3", "label": "3. Limitation of Arrhenius model", "prompt": "State the limitation of the Arrhenius model.", "expected_answer": "Restricted to aqueous solutions only", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Definition: increases [{sub['ion']}] in aqueous solution", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Balanced equation with correct states and formulas", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Limitation: only applies in aqueous medium / water", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"Arrhenius linked acidity directly to hydronium ions and alkalinity to hydroxide ions in aqueous solution.",
            "tier_2": f"For an Arrhenius {sub['type']}, focus on whether dissolving in water increases $[\\text{{H}}_3\\text{{O}}^+]$ or $[\\text{{OH}}^-]$.",
            "tier_3": f"{def_text} Equation: ${sub['eq']}$.",
        },
        "misconception_tags": ["arrhenius_bronsted_confusion", "solvent_limitation_omitted"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 02: Brønsted-Lowry Proton Donor & Acceptor
# ==============================================================================
def build_02_bronsted_lowry_proton_donor_acceptor(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    reactions = [
        {
            "eq": r"\text{HCl}(\text{g}) + \text{NH}_3(\text{g}) \rightarrow \text{NH}_4^+(\text{s}) + \text{Cl}^-(\text{s})",
            "donor": r"\text{HCl}",
            "donor_name": "hydrogen chloride",
            "acceptor": r"\text{NH}_3",
            "acceptor_name": "ammonia",
        },
        {
            "eq": r"\text{HNO}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightarrow \text{H}_3\text{O}^+(\text{aq}) + \text{NO}_3^-(\text{aq})",
            "donor": r"\text{HNO}_3",
            "donor_name": "nitric acid",
            "acceptor": r"\text{H}_2\text{O}",
            "acceptor_name": "water",
        },
        {
            "eq": r"\text{H}_2\text{O}(\text{l}) + \text{S}^{2-}(\text{aq}) \rightleftharpoons \text{HS}^-(\text{aq}) + \text{OH}^-(\text{aq})",
            "donor": r"\text{H}_2\text{O}",
            "donor_name": "water",
            "acceptor": r"\text{S}^{2-}",
            "acceptor_name": "sulfide ion",
        },
        {
            "eq": r"\text{HF}(\text{aq}) + \text{NH}_3(\text{aq}) \rightleftharpoons \text{NH}_4^+(\text{aq}) + \text{F}^-(\text{aq})",
            "donor": r"\text{HF}",
            "donor_name": "hydrofluoric acid",
            "acceptor": r"\text{NH}_3",
            "acceptor_name": "ammonia",
        },
    ]
    rxn = r.choice(reactions)

    prompt = (
        f"Consider the chemical reaction represented below:\n\n"
        f"$${rxn['eq']}$$\n\n"
        f"1. Define an **acid** in terms of the Brønsted-Lowry theory.\n"
        f"2. Identify the **proton donor** in the forward reaction and justify your choice.\n"
        f"3. Identify the **proton acceptor** in the forward reaction and state its role."
    )

    sol = (
        f"1. **Brønsted-Lowry acid:** A proton ($H^+$ ion) donor.\n"
        f"2. **Proton donor:** ${rxn['donor']}$ ({rxn['donor_name']}). It loses/transfers a proton ($H^+$) during the reaction.\n"
        f"3. **Proton acceptor:** ${rxn['acceptor']}$ ({rxn['acceptor_name']}). It gains/accepts a proton ($H^+$), acting as the Brønsted-Lowry base."
    )

    return {
        "id": f"g12_ps_ab_02_{r.randint(10000, 99999)}",
        "subskill": "02_bronsted_lowry_proton_donor_acceptor",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Acid = Proton donor; Donor: {rxn['donor']}, Acceptor: {rxn['acceptor']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Brønsted-Lowry acid definition", "prompt": "Define a Brønsted-Lowry acid.", "expected_answer": "A proton (H+) donor", "marks": 2},
            {"part": "2", "label": "2. Identify proton donor", "prompt": "Identify the proton donor and justify.", "expected_answer": f"{rxn['donor']} donates H+", "marks": 2},
            {"part": "3", "label": "3. Identify proton acceptor", "prompt": "Identify the proton acceptor and state its role.", "expected_answer": f"{rxn['acceptor']} accepts H+ (base)", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: Proton (H+) donor", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Donor identified as {rxn['donor']} with justification of losing H+", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Acceptor identified as {rxn['acceptor']} acting as base", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "In the Brønsted-Lowry model: Acids donate protons ($H^+$); Bases accept protons ($H^+$).",
            "tier_2": f"Follow the hydrogen atom: which species on the left loses an $H^+$ to form a product? That is the acid (${rxn['donor']}$).",
            "tier_3": f"Proton donor is ${rxn['donor']}$; proton acceptor is ${rxn['acceptor']}$.",
        },
        "misconception_tags": ["confused_proton_donor_and_acceptor", "electron_vs_proton_confusion"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 03: Conjugate Acid-Base Pairs
# ==============================================================================
def build_03_conjugate_acid_base_pairs(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    pairs_pool = [
        {
            "eq": r"\text{HNO}_2(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NO}_2^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
            "acid_1": r"\text{HNO}_2",
            "base_1": r"\text{NO}_2^-",
            "base_2": r"\text{H}_2\text{O}",
            "acid_2": r"\text{H}_3\text{O}^+",
        },
        {
            "eq": r"\text{NH}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_4^+(\text{aq}) + \text{OH}^-(\text{aq})",
            "acid_1": r"\text{H}_2\text{O}",
            "base_1": r"\text{OH}^-",
            "base_2": r"\text{NH}_3",
            "acid_2": r"\text{NH}_4^+",
        },
        {
            "eq": r"\text{HCN}(\text{aq}) + \text{SO}_4^{2-}(\text{aq}) \rightleftharpoons \text{CN}^-(\text{aq}) + \text{HSO}_4^-(\text{aq})",
            "acid_1": r"\text{HCN}",
            "base_1": r"\text{CN}^-",
            "base_2": r"\text{SO}_4^{2-}",
            "acid_2": r"\text{HSO}_4^-",
        },
        {
            "eq": r"\text{HF}(\text{aq}) + \text{CH}_3\text{COO}^-(\text{aq}) \rightleftharpoons \text{F}^-(\text{aq}) + \text{CH}_3\text{COOH}(\text{aq})",
            "acid_1": r"\text{HF}",
            "base_1": r"\text{F}^-",
            "base_2": r"\text{CH}_3\text{COO}^-",
            "acid_2": r"\text{CH}_3\text{COOH}",
        },
    ]
    item = r.choice(pairs_pool)

    prompt = (
        f"Consider the reversible acid-base reaction:\n\n"
        f"$${item['eq']}$$\n\n"
        f"1. Define a **conjugate acid-base pair**.\n"
        f"2. Write down the formulae of the **TWO conjugate acid-base pairs** in this equilibrium reaction.\n"
        f"3. For the pair containing ${item['acid_1']}$, clearly state which formula is the acid and which is the conjugate base."
    )

    sol = (
        f"1. **Conjugate acid-base pair:** Two compounds or ions that differ only by a single proton ($H^+$) and a charge of $+1$.\n"
        f"2. **Conjugate acid-base pairs:**\n"
        f"   - Pair 1: (${item['acid_1']}$, ${item['base_1']}$)\n"
        f"   - Pair 2: (${item['acid_2']}$, ${item['base_2']}$)\n"
        f"3. In Pair 1, ${item['acid_1']}$ is the acid (proton donor) and ${item['base_1']}$ is its conjugate base (proton acceptor)."
    )

    return {
        "id": f"g12_ps_ab_03_{r.randint(10000, 99999)}",
        "subskill": "03_conjugate_acid_base_pairs",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Pair 1: ({item['acid_1']}, {item['base_1']}); Pair 2: ({item['acid_2']}, {item['base_2']})",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Definition of conjugate pair", "prompt": "Define a conjugate acid-base pair.", "expected_answer": "Differ by one proton (H+)", "marks": 2},
            {"part": "2", "label": "2. Two conjugate pairs", "prompt": "Write down the two conjugate acid-base pairs.", "expected_answer": f"({item['acid_1']}, {item['base_1']}) and ({item['acid_2']}, {item['base_2']})", "marks": 2},
            {"part": "3", "label": "3. Identify acid and conjugate base", "prompt": f"Identify acid and conjugate base in pair containing {item['acid_1']}.", "expected_answer": f"Acid: {item['acid_1']}, Conjugate base: {item['base_1']}", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: two species differing by exactly one proton (H+)", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Pair 1: {item['acid_1']} and {item['base_1']}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Pair 2: {item['acid_2']} and {item['base_2']}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Identification of {item['acid_1']} as acid and {item['base_1']} as conjugate base", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Conjugate pairs always differ by exactly one hydrogen ion ($H^+$).",
            "tier_2": "The species with more hydrogens is the acid; remove one $H^+$ to get its conjugate base.",
            "tier_3": f"Pair 1: ${item['acid_1']} / {item['base_1']}$; Pair 2: ${item['acid_2']} / {item['base_2']}$.",
        },
        "misconception_tags": ["mismatched_conjugate_pairs", "charge_bookkeeping_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 04: Conjugate Pairs in Organic Acids
# ==============================================================================
def build_04_conjugate_pairs_organic_acids(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    acids = [
        {"name": "methanoic acid (formic acid)", "formula": r"\text{HCOOH}", "base": r"\text{HCOO}^-", "base_name": "methanoate ion"},
        {"name": "ethanoic acid (acetic acid)", "formula": r"\text{CH}_3\text{COOH}", "base": r"\text{CH}_3\text{COO}^-", "base_name": "ethanoate ion"},
        {"name": "propanoic acid", "formula": r"\text{CH}_3\text{CH}_2\text{COOH}", "base": r"\text{CH}_3\text{CH}_2\text{COO}^-", "base_name": "propanoate ion"},
        {"name": "benzoic acid", "formula": r"\text{C}_6\text{H}_5\text{COOH}", "base": r"\text{C}_6\text{H}_5\text{COO}^-", "base_name": "benzoate ion"},
    ]
    ac = r.choice(acids)

    prompt = (
        f"**{ac['name']}** (${ac['formula']}$) is an organic carboxylic acid that partially ionises in water according to the equilibrium:\n\n"
        f"$${ac['formula']}(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}}) \\rightleftharpoons {ac['base']}(\\text{{aq}}) + \\text{{H}}_3\\text{{O}}^+(\\text{{aq}})$$\n\n"
        f"1. Name the functional group present in ${ac['formula']}$.\n"
        f"2. Write down the chemical formula of the **conjugate base** of ${ac['formula']}$.\n"
        f"3. Which hydrogen atom in ${ac['formula']}$ is donated during protolysis? (Specify the acidic proton)."
    )

    sol = (
        f"1. **Functional group:** Carboxyl group ($-\\text{{COOH}}$).\n"
        f"2. **Conjugate base:** ${ac['base']}$ ({ac['base_name']}).\n"
        f"3. **Acidic proton:** The hydrogen atom directly attached to the oxygen atom in the carboxyl (hydroxyl) group ($-O-H$). "
        f"The carbon-bonded hydrogen atoms (in alkyl groups) are not acidic and do not ionise."
    )

    return {
        "id": f"g12_ps_ab_04_{r.randint(10000, 99999)}",
        "subskill": "04_conjugate_pairs_organic_acids",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Functional group: Carboxyl; Conjugate base: {ac['base']}; Proton: -COOH hydrogen",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Carboxyl functional group", "prompt": "Name the functional group.", "expected_answer": "Carboxyl group", "marks": 1},
            {"part": "2", "label": "2. Conjugate base formula", "prompt": "Write formula of conjugate base.", "expected_answer": ac['base'], "marks": 1},
            {"part": "3", "label": "3. Location of acidic proton", "prompt": "Which hydrogen atom is donated?", "expected_answer": "Hydrogen bonded to oxygen (-OH)", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Carboxyl group identified", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct conjugate base formula: {ac['base']}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Identification of hydroxyl/carboxyl H as the ionising proton", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Carboxylic acids ionise by releasing the proton from the $-COOH$ group.",
            "tier_2": f"When ${ac['formula']}$ loses an $H^+$, the negative charge resides on the oxygen: ${ac['base']}$.",
            "tier_3": f"Conjugate base: ${ac['base']}$. Proton comes from the oxygen atom of the carboxyl group.",
        },
        "misconception_tags": ["organic_proton_confusion", "alkyl_hydrogen_ionisation_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 05: Conjugate Pairs in Polyprotic Systems
# ==============================================================================
def build_05_conjugate_pairs_polyprotic(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    systems = [
        {
            "acid": "phosphoric acid",
            "h3a": r"\text{H}_3\text{PO}_4",
            "step1_base": r"\text{H}_2\text{PO}_4^-",
            "step2_base": r"\text{HPO}_4^{2-}",
            "step3_base": r"\text{PO}_4^{3-}",
            "target": r"\text{H}_2\text{PO}_4^-",
        },
        {
            "acid": "carbonic acid",
            "h3a": r"\text{H}_2\text{CO}_3",
            "step1_base": r"\text{HCO}_3^-",
            "step2_base": r"\text{CO}_3^{2-}",
            "step3_base": r"\text{CO}_3^{2-}",
            "target": r"\text{HCO}_3^-",
        },
        {
            "acid": "sulfurous acid",
            "h3a": r"\text{H}_2\text{SO}_3",
            "step1_base": r"\text{HSO}_3^-",
            "step2_base": r"\text{SO}_3^{2-}",
            "step3_base": r"\text{SO}_3^{2-}",
            "target": r"\text{HSO}_3^-",
        },
    ]
    sys = r.choice(systems)

    prompt = (
        f"Consider the polyprotic acid **{sys['acid']}** (${sys['h3a']}$).\n\n"
        f"1. Define a **polyprotic acid**.\n"
        f"2. Write down the chemical formula of the **conjugate acid** of ${sys['target']}$.\n"
        f"3. Write down the chemical formula of the **conjugate base** of ${sys['target']}."
    )

    conj_acid = sys['h3a']
    conj_base = sys['step2_base']

    sol = (
        f"1. **Polyprotic acid:** An acid capable of donating more than one proton ($H^+$ ion) per molecule during successive ionisation steps.\n"
        f"2. **Conjugate acid of ${sys['target']}$:** Add an $H^+$ to get ${conj_acid}$.\n"
        f"3. **Conjugate base of ${sys['target']}$:** Remove an $H^+$ to get ${conj_base}$."
    )

    return {
        "id": f"g12_ps_ab_05_{r.randint(10000, 99999)}",
        "subskill": "05_conjugate_pairs_polyprotic",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Conjugate acid: {conj_acid}; Conjugate base: {conj_base}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Polyprotic acid definition", "prompt": "Define a polyprotic acid.", "expected_answer": "Donates more than one proton per molecule", "marks": 2},
            {"part": "2", "label": f"2. Conjugate acid of {sys['target']}", "prompt": "Write conjugate acid formula.", "expected_answer": conj_acid, "marks": 1},
            {"part": "3", "label": f"3. Conjugate base of {sys['target']}", "prompt": "Write conjugate base formula.", "expected_answer": conj_base, "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: donates more than one proton per molecule", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Correct conjugate acid: {conj_acid}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Correct conjugate base: {conj_base}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "To find a conjugate acid, ADD an $H^+$ and increase charge by $+1$.",
            "tier_2": "To find a conjugate base, REMOVE an $H^+$ and decrease charge by $-1$.",
            "tier_3": f"${sys['target']} + H^+ \\rightarrow {conj_acid}$; ${sys['target']} - H^+ \\rightarrow {conj_base}$.",
        },
        "misconception_tags": ["polyprotic_charge_miscalculation", "inverted_conjugate_logic"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 06: Amphiprotic Water Behavior
# ==============================================================================
def build_06_amphiprotic_water_behavior(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    pairs = [
        {
            "partner_base": r"\text{NH}_3",
            "partner_base_name": "ammonia",
            "water_as_acid_eq": r"\text{NH}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_4^+(\text{aq}) + \text{OH}^-(\text{aq})",
            "partner_acid": r"\text{HCl}",
            "partner_acid_name": "hydrochloric acid",
            "water_as_base_eq": r"\text{HCl}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightarrow \text{Cl}^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
        },
        {
            "partner_base": r"\text{CO}_3^{2-}",
            "partner_base_name": "carbonate ion",
            "water_as_acid_eq": r"\text{CO}_3^{2-}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{HCO}_3^-(\text{aq}) + \text{OH}^-(\text{aq})",
            "partner_acid": r"\text{HNO}_3",
            "partner_acid_name": "nitric acid",
            "water_as_base_eq": r"\text{HNO}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightarrow \text{NO}_3^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
        },
    ]
    p = r.choice(pairs)

    prompt = (
        f"Water ($\\text{{H}}_2\\text{{O}}$) is a well-known **amphiprotic** (amphoteric) substance.\n\n"
        f"1. Define the term **amphiprotic**.\n"
        f"2. Write down a balanced chemical equation showing water acting as a **Brønsted-Lowry acid** in the presence of ${p['partner_base']}$.\n"
        f"3. Write down a balanced chemical equation showing water acting as a **Brønsted-Lowry base** in the presence of ${p['partner_acid']}."
    )

    sol = (
        f"1. **Amphiprotic definition:** A substance that can act as either a Brønsted-Lowry acid (donate a proton) or a Brønsted-Lowry base (accept a proton).\n"
        f"2. **Water as acid (proton donor):**\n"
        f"   $${p['water_as_acid_eq']}$$\n"
        f"   Here, $\\text{{H}}_2\\text{{O}}$ donates $H^+$ to ${p['partner_base']}$ forming $\\text{{OH}}^-$.\n"
        f"3. **Water as base (proton acceptor):**\n"
        f"   $${p['water_as_base_eq']}$$\n"
        f"   Here, $\\text{{H}}_2\\text{{O}}$ accepts $H^+$ from ${p['partner_acid']}$ forming $\\text{{H}}_3\\text{{O}}^+.$"
    )

    return {
        "id": f"g12_ps_ab_06_{r.randint(10000, 99999)}",
        "subskill": "06_amphiprotic_water_behavior",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Amphiprotic: acts as acid or base; Acid eq: {p['water_as_acid_eq']}; Base eq: {p['water_as_base_eq']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Definition of amphiprotic", "prompt": "Define amphiprotic.", "expected_answer": "Acts as both proton donor and proton acceptor", "marks": 2},
            {"part": "2", "label": "2. Water as acid equation", "prompt": "Write equation where water acts as acid.", "expected_answer": p['water_as_acid_eq'], "marks": 2},
            {"part": "3", "label": "3. Water as base equation", "prompt": "Write equation where water acts as base.", "expected_answer": p['water_as_base_eq'], "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Definition: substance that can donate or accept a proton", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Correct balanced equation showing water donating H+", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Correct balanced equation showing water accepting H+", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Amphiprotic = amphoteric in proton terms: donor in one reaction, acceptor in another.",
            "tier_2": "When water acts as an acid, it forms $OH^-$. When it acts as a base, it forms $H_3O^+$.",
            "tier_3": f"Acid: ${p['water_as_acid_eq']}$; Base: ${p['water_as_base_eq']}$.",
        },
        "misconception_tags": ["amphoteric_vs_amphiprotic_confusion", "water_ion_confusion"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 07: Amphiprotic Ions (Hydrogen Carbonate, Hydrogen Sulfate)
# ==============================================================================
def build_07_amphiprotic_ions(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    ions = [
        {
            "name": "hydrogen carbonate ion",
            "formula": r"\text{HCO}_3^-",
            "acid_eq": r"\text{HCO}_3^-(\text{aq}) + \text{OH}^-(\text{aq}) \rightleftharpoons \text{CO}_3^{2-}(\text{aq}) + \text{H}_2\text{O}(\text{l})",
            "base_eq": r"\text{HCO}_3^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq}) \rightleftharpoons \text{H}_2\text{CO}_3(\text{aq}) + \text{H}_2\text{O}(\text{l})",
        },
        {
            "name": "hydrogen sulfate ion",
            "formula": r"\text{HSO}_4^-",
            "acid_eq": r"\text{HSO}_4^-(\text{aq}) + \text{OH}^-(\text{aq}) \rightleftharpoons \text{SO}_4^{2-}(\text{aq}) + \text{H}_2\text{O}(\text{l})",
            "base_eq": r"\text{HSO}_4^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq}) \rightleftharpoons \text{H}_2\text{SO}_4(\text{aq}) + \text{H}_2\text{O}(\text{l})",
        },
        {
            "name": "dihydrogen phosphate ion",
            "formula": r"\text{H}_2\text{PO}_4^-",
            "acid_eq": r"\text{H}_2\text{PO}_4^-(\text{aq}) + \text{OH}^-(\text{aq}) \rightleftharpoons \text{HPO}_4^{2-}(\text{aq}) + \text{H}_2\text{O}(\text{l})",
            "base_eq": r"\text{H}_2\text{PO}_4^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq}) \rightleftharpoons \text{H}_3\text{PO}_4(\text{aq}) + \text{H}_2\text{O}(\text{l})",
        },
    ]
    ion = r.choice(ions)

    prompt = (
        f"The **{ion['name']}** (${ion['formula']}$) is an ampholyte (amphiprotic ion).\n\n"
        f"1. Explain why ${ion['formula']}$ can act as an amphiprotic substance.\n"
        f"2. Write a balanced ionic equation showing ${ion['formula']}$ acting as an acid in the presence of hydroxide ions ($\\text{{OH}}^-$).\n"
        f"3. Write a balanced ionic equation showing ${ion['formula']}$ acting as a base in the presence of hydronium ions ($\\text{{H}}_3\\text{{O}}^+$)."
    )

    sol = (
        f"1. **Explanation:** ${ion['formula']}$ contains an ionisable hydrogen atom (allowing it to donate a proton, $H^+$) "
        f"and has a negative charge / lone pair (allowing it to accept a proton, $H^+$).\n"
        f"2. **Acting as acid (proton donor):**\n"
        f"   $${ion['acid_eq']}$$\n"
        f"3. **Acting as base (proton acceptor):**\n"
        f"   $${ion['base_eq']}$$"
    )

    return {
        "id": f"g12_ps_ab_07_{r.randint(10000, 99999)}",
        "subskill": "07_amphiprotic_ions",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Acid eq: {ion['acid_eq']}; Base eq: {ion['base_eq']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Explanation of amphiprotic nature", "prompt": "Explain why it is amphiprotic.", "expected_answer": "Can both donate and accept H+", "marks": 2},
            {"part": "2", "label": "2. Equation as acid with OH-", "prompt": "Write equation acting as acid.", "expected_answer": ion['acid_eq'], "marks": 2},
            {"part": "3", "label": "3. Equation as base with H3O+", "prompt": "Write equation acting as base.", "expected_answer": ion['base_eq'], "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Explanation: has donor H and acceptor capacity", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Balanced equation as acid with OH-", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Balanced equation as base with H3O+", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Acting as an acid means donating $H^+$; acting as a base means accepting $H^+$.",
            "tier_2": f"When ${ion['formula']}$ loses $H^+$ to $OH^-$, it forms water and its conjugate base. When it accepts $H^+$ from $H_3O^+$, it forms its conjugate acid.",
            "tier_3": f"Acid eq: ${ion['acid_eq']}$; Base eq: ${ion['base_eq']}$.",
        },
        "misconception_tags": ["ion_charge_balance_error", "ampholyte_equation_omission"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 08: Auto-protolysis of Water and Kw
# ==============================================================================
def build_08_autoprotolysis_water_kw(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    vol_cm3 = r.choice([250.0, 500.0, 750.0, 1000.0, 1500.0, 2000.0])
    vol_dm3 = vol_cm3 / 1000.0
    kw = 1.0e-14
    h3o = 1.0e-7
    moles_h3o = h3o * vol_dm3

    prompt = (
        f"A chemist studies a pure distilled water sample of volume **${_fmt_sa(vol_cm3)}\\text{{ cm}}^3$** at $25^\\circ\\text{{C}}$.\n"
        f"Water undergoes self-ionisation (auto-protolysis) with an equilibrium constant of $K_w = 1{{,}}0 \\times 10^{{-14}}$.\n\n"
        f"1. Write down the balanced chemical equation representing the auto-ionisation of water.\n"
        f"2. Write down the equilibrium constant expression for $K_w$.\n"
        f"3. Calculate the concentration of hydronium ions ($[\\text{{H}}_3\\text{{O}}^+]$) in this pure water sample at $25^\\circ\\text{{C}}$, and hence show that pure water is neutral.\n"
        f"4. Calculate the total number of moles of hydronium ions present in the ${_fmt_sa(vol_cm3)}\\text{{ cm}}^3$ sample."
    )

    sol = (
        f"1. **Equation:**\n"
        f"   $$2\\text{{H}}_2\\text{{O}}(\\text{{l}}) \\rightleftharpoons \\text{{H}}_3\\text{{O}}^+(\\text{{aq}}) + \\text{{OH}}^-(\\text{{aq}})$$\n"
        f"2. **Expression:**\n"
        f"   $$K_w = [\\text{{H}}_3\\text{{O}}^+][\\text{{OH}}^-] = 1{{,}}0 \\times 10^{{-14}} \\text{{ at }} 25^\\circ\\text{{C}}$$\n"
        f"3. **Calculations:**\n"
        f"   In pure water, $[\\text{{H}}_3\\text{{O}}^+] = [\\text{{OH}}^-] = x$.\n"
        f"   $$x^2 = 1{{,}}0 \\times 10^{{-14}} \\implies x = 1{{,}}0 \\times 10^{{-7}}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"   Since $[\\text{{H}}_3\\text{{O}}^+] = [\\text{{OH}}^-] = 1{{,}}0 \\times 10^{{-7}}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$, the solution is strictly neutral ($\\text{{pH}} = 7{{,}}00$).\n"
        f"4. **Moles in sample:**\n"
        f"   $$n = c \\times V = 1{{,}}0 \\times 10^{{-7}} \\times {_fmt_sa(vol_dm3)} = {_fmt_sci(moles_h3o)}\\text{{ mol}}$$"
    )

    return {
        "id": f"g12_ps_ab_08_{r.randint(10000, 99999)}",
        "subskill": "08_autoprotolysis_water_kw",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"[H3O+] = 1,0 x 10^-7 mol/dm3; Moles in {_fmt_sa(vol_cm3)} cm3 = {_fmt_sci(moles_h3o)} mol",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Auto-ionisation equation", "prompt": "Write auto-ionisation equation of water.", "expected_answer": "2H2O <-> H3O+ + OH-", "marks": 2},
            {"part": "2", "label": "2. Kw expression", "prompt": "Write Kw expression.", "expected_answer": "Kw = [H3O+][OH-]", "marks": 1},
            {"part": "3", "label": "3. Concentrations in pure water", "prompt": "Calculate [H3O+] and show neutral.", "expected_answer": "1.0 x 10^-7 mol/dm3", "marks": 2},
            {"part": "4", "label": "4. Total moles in sample", "prompt": "Calculate total moles of H3O+ in sample.", "expected_answer": _fmt_sci(moles_h3o), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": "Balanced auto-protolysis equation", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Kw expression: Kw = [H3O+][OH-]", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Calculated [H3O+] = 1.0 x 10^-7 and neutrality justified", "marks": 2, "editable": True},
                {"id": "mp4", "desc": f"Total moles n = cV = {_fmt_sci(moles_h3o)} mol", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Auto-protolysis of water: two water molecules react to produce one hydronium and one hydroxide ion.",
            "tier_2": "Because the mole ratio is 1:1, $[H_3O^+] = [OH^-] = 1{{,}}0 \\times 10^{-7}\\text{ mol}\\cdot\\text{dm}^{-3}$.",
            "tier_3": f"$n = c \\times V = 1{{,}}0 \\times 10^{-7} \\times {_fmt_sa(vol_dm3)} = {_fmt_sci(moles_h3o)}\\text{{ mol}}$.",
        },
        "misconception_tags": ["kw_definition_error", "neutral_definition_misconception"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 09: Temperature Dependence of Kw
# ==============================================================================
def build_09_temperature_dependence_kw(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    temp_data = [
        {"temp": 10, "kw": 0.29e-14, "kw_str": r"2{,}9 \times 10^{-15}", "h3o": math.sqrt(0.29e-14), "ph": 7.27},
        {"temp": 40, "kw": 2.92e-14, "kw_str": r"2{,}92 \times 10^{-14}", "h3o": math.sqrt(2.92e-14), "ph": 6.77},
        {"temp": 60, "kw": 9.61e-14, "kw_str": r"9{,}61 \times 10^{-14}", "h3o": math.sqrt(9.61e-14), "ph": 6.51},
        {"temp": 100, "kw": 5.13e-13, "kw_str": r"5{,}13 \times 10^{-13}", "h3o": math.sqrt(5.13e-13), "ph": 6.14},
    ]
    data = r.choice(temp_data)

    prompt = (
        f"The auto-ionisation of water is an **endothermic** process:\n\n"
        f"$$2\\text{{H}}_2\\text{{O}}(\\text{{l}}) + \\text{{heat}} \\rightleftharpoons \\text{{H}}_3\\text{{O}}^+(\\text{{aq}}) + \\text{{OH}}^-(\\text{{aq}}) \\quad (\\Delta H > 0)$$\n\n"
        f"At ${data['temp']}^\\circ\\text{{C}}$, the value of the ion-product constant of water is **$K_w = {data['kw_str']}$**.\n\n"
        f"1. Apply **Le Chatelier's principle** to explain why the value of $K_w$ at ${data['temp']}^\\circ\\text{{C}}$ differs from its value at $25^\\circ\\text{{C}}$ ($1{{,}}0 \\times 10^{{-14}}$).\n"
        f"2. Calculate the hydronium ion concentration ($[\\text{{H}}_3\\text{{O}}^+]$) in pure water at ${data['temp']}^\\circ\\text{{C}}$.\n"
        f"3. Calculate the pH of pure water at ${data['temp']}^\\circ\\text{{C}}$ and explain why the water is still **neutral** despite having a $\\text{{pH}} \\neq 7$."
    )

    if data['temp'] > 25:
        le_chat = f"As temperature increases from 25°C to {data['temp']}°C, the system favors the endothermic forward reaction to absorb added heat. This increases both [H3O+] and [OH-], increasing the equilibrium constant Kw."
    else:
        le_chat = f"As temperature decreases from 25°C to {data['temp']}°C, the system favors the exothermic reverse reaction to release heat. This decreases [H3O+] and [OH-], decreasing the equilibrium constant Kw."

    sol = (
        f"1. **Le Chatelier explanation:** {le_chat}\n"
        f"2. **Hydronium concentration:**\n"
        f"   In pure water, $[\\text{{H}}_3\\text{{O}}^+] = [\\text{{OH}}^-] = \\sqrt{{K_w}}$\n"
        f"   $$[\\text{{H}}_3\\text{{O}}^+] = \\sqrt{{{data['kw_str']}}} = {_fmt_sci(data['h3o'])}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **pH and neutrality:**\n"
        f"   $$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = -\\log({_fmt_sci(data['h3o'])}) = {_fmt_sa(data['ph'])}$$\n"
        f"   Water is **neutral** because neutrality requires $[\\text{{H}}_3\\text{{O}}^+] = [\\text{{OH}}^-]$, NOT that $\\text{{pH}} = 7{{,}}00$. "
        f"At ${data['temp']}^\\circ\\text{{C}}$, $[\\text{{H}}_3\\text{{O}}^+]$ equals $[\\text{{OH}}^-]$ exactly, so it is strictly neutral."
    )

    return {
        "id": f"g12_ps_ab_09_{r.randint(10000, 99999)}",
        "subskill": "09_temperature_dependence_kw",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"pH = {_fmt_sa(data['ph'])}; Neutral because [H3O+] = [OH-]",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Le Chatelier explanation for Kw change", "prompt": "Explain Kw change with temperature.", "expected_answer": le_chat, "marks": 2},
            {"part": "2", "label": f"2. [H3O+] at {data['temp']}°C", "prompt": f"Calculate [H3O+] at {data['temp']}°C.", "expected_answer": _fmt_sci(data['h3o']), "marks": 2},
            {"part": "3", "label": "3. pH and neutrality justification", "prompt": "Calculate pH and justify neutrality.", "expected_answer": f"pH = {_fmt_sa(data['ph'])}, neutral because [H3O+] = [OH-]", "marks": 3},
        ],
        "marking_schema": {
            "total_marks": 7,
            "marking_points": [
                {"id": "mp1", "desc": "Le Chatelier: endothermic shift explanation", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Calculation: [H3O+] = sqrt(Kw) = {_fmt_sci(data['h3o'])}", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"pH calculation = {_fmt_sa(data['ph'])}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Justification that neutral means [H3O+] = [OH-], regardless of pH number", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Neutrality is defined as $[H_3O^+] = [OH^-]$, which only equals $pH = 7$ at 25°C.",
            "tier_2": "Because auto-ionisation is endothermic, higher temperatures shift equilibrium to the right ($K_w$ increases).",
            "tier_3": f"$[H_3O^+] = \\sqrt{{{data['kw_str']}}}$, so $pH = {_fmt_sa(data['ph'])}$.",
        },
        "misconception_tags": ["ph_7_dogma", "le_chatelier_temperature_shift_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 10: Strong vs Weak Acids Ionisation
# ==============================================================================
def build_10_strong_vs_weak_acids_ionisation(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    pairs = [
        {
            "strong": "Hydrochloric acid (HCl)",
            "strong_eq": r"\text{HCl}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightarrow \text{H}_3\text{O}^+(\text{aq}) + \text{Cl}^-(\text{aq})",
            "weak": "Ethanoic acid (CH3COOH)",
            "weak_eq": r"\text{CH}_3\text{COOH}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{CH}_3\text{COO}^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
            "conc": r"0{,}1",
        },
        {
            "strong": "Nitric acid (HNO3)",
            "strong_eq": r"\text{HNO}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightarrow \text{H}_3\text{O}^+(\text{aq}) + \text{NO}_3^-(\text{aq})",
            "weak": "Hydrofluoric acid (HF)",
            "weak_eq": r"\text{HF}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{F}^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
            "conc": r"0{,}2",
        },
    ]
    p = r.choice(pairs)

    prompt = (
        f"Two beakers each contain a **${p['conc']}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** solution of an acid at $25^\\circ\\text{{C}}$:\n"
        f"- Beaker A: **{p['strong']}**\n"
        f"- Beaker B: **{p['weak']}**\n\n"
        f"1. Define a **strong acid**.\n"
        f"2. Define a **weak acid**.\n"
        f"3. Explain the significance of using a single forward arrow ($\\rightarrow$) for Beaker A versus a reversible double arrow ($\\rightleftharpoons$) for Beaker B in their ionisation equations.\n"
        f"4. State which beaker will have a lower pH and give a concise reason."
    )

    sol = (
        f"1. **Strong acid:** An acid that ionises completely (almost 100%) in water to form a high concentration of $\\text{{H}}_3\\text{{O}}^+$ ions.\n"
        f"2. **Weak acid:** An acid that ionises only partially (small percentage) in water to form a low concentration of $\\text{{H}}_3\\text{{O}}^+$ ions.\n"
        f"3. **Arrow significance:**\n"
        f"   - Single arrow ($\\rightarrow$): Represents complete forward ionisation; virtually no intact reactant molecules remain at equilibrium.\n"
        f"   - Reversible arrows ($\\rightleftharpoons$): Represents incomplete partial ionisation reaching a dynamic equilibrium where intact molecules predominate.\n"
        f"4. **Lower pH:** **Beaker A** ({p['strong']}). Complete ionisation yields a significantly higher $[\\text{{H}}_3\\text{{O}}^+]$, and since $\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+]$, higher hydronium concentration corresponds to a lower pH."
    )

    return {
        "id": f"g12_ps_ab_10_{r.randint(10000, 99999)}",
        "subskill": "10_strong_vs_weak_acids_ionisation",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": "Strong: complete ionisation; Weak: partial ionisation; Beaker A has lower pH",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Definition of strong acid", "prompt": "Define a strong acid.", "expected_answer": "Ionises completely in water", "marks": 2},
            {"part": "2", "label": "2. Definition of weak acid", "prompt": "Define a weak acid.", "expected_answer": "Ionises only partially in water", "marks": 2},
            {"part": "3", "label": "3. Significance of reaction arrows", "prompt": "Explain significance of single vs double arrows.", "expected_answer": "Complete vs dynamic equilibrium ionisation", "marks": 2},
            {"part": "4", "label": "4. Beaker with lower pH", "prompt": "Which beaker has lower pH and why?", "expected_answer": "Beaker A due to higher [H3O+]", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp1", "desc": "Strong acid definition: complete ionisation in water", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Weak acid definition: partial ionisation in water", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Arrow distinction: irreversible completion vs dynamic equilibrium", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Beaker A lower pH linked to higher [H3O+]", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Strength refers to the percentage of molecules that form ions in solution.",
            "tier_2": "Complete ionisation = strong acid = higher $[H_3O^+]$ = lower pH.",
            "tier_3": "Beaker A is completely ionised (single arrow), so $[H_3O^+]$ is highest, giving the lowest pH.",
        },
        "misconception_tags": ["strength_vs_concentration_confusion", "equilibrium_arrow_omission"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 11: Strong vs Weak Bases Dissociation
# ==============================================================================
def build_11_strong_vs_weak_bases_dissociation(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    bases = [
        {"strong": "Sodium hydroxide (NaOH)", "strong_eq": r"\text{NaOH}(\text{s}) \rightarrow \text{Na}^+(\text{aq}) + \text{OH}^-(\text{aq})", "weak": "Ammonia (NH3)", "weak_eq": r"\text{NH}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_4^+(\text{aq}) + \text{OH}^-(\text{aq})"},
        {"strong": "Potassium hydroxide (KOH)", "strong_eq": r"\text{KOH}(\text{s}) \rightarrow \text{K}^+(\text{aq}) + \text{OH}^-(\text{aq})", "weak": "Magnesium hydroxide (Mg(OH)2)", "weak_eq": r"\text{Mg(OH)}_2(\text{s}) \rightleftharpoons \text{Mg}^{2+}(\text{aq}) + 2\text{OH}^-(\text{aq})"},
    ]
    b = r.choice(bases)

    prompt = (
        f"A laboratory technician compares two base solutions:\n"
        f"- Base X: **{b['strong']}**\n"
        f"- Base Y: **{b['weak']}**\n\n"
        f"1. Define a **strong base**.\n"
        f"2. Define a **weak base**.\n"
        f"3. Explain the mechanical difference between **dissociation** (for ionic bases like NaOH) and **ionisation** (for molecular bases like NH3).\n"
        f"4. If both solutions have the same initial concentration ($0{{,}}1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$), which one will have the higher electrical conductivity?"
    )

    sol = (
        f"1. **Strong base:** A base that dissociates almost completely in aqueous solution to yield a high concentration of $\\text{{OH}}^-$ ions.\n"
        f"2. **Weak base:** A base that dissociates or ionises only partially in aqueous solution to produce a low concentration of $\\text{{OH}}^-$ ions.\n"
        f"3. **Dissociation vs Ionisation:**\n"
        f"   - **Dissociation:** The splitting apart of pre-existing ions from an ionic solid lattice when dissolved in water (${b['strong_eq']}$).\n"
        f"   - **Ionisation:** A reaction between neutral covalent molecules and water to create new ions that were not present previously (${b['weak_eq']}$).\n"
        f"4. **Electrical conductivity:** **Base X** ({b['strong']}). Complete dissociation releases a far greater concentration of mobile ions ($\\text{{Na}}^+$ and $\\text{{OH}}^-$) to carry electric current."
    )

    return {
        "id": f"g12_ps_ab_11_{r.randint(10000, 99999)}",
        "subskill": "11_strong_vs_weak_bases_dissociation",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": "Strong base dissociates completely; Base X has higher conductivity",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Definition of strong base", "prompt": "Define a strong base.", "expected_answer": "Dissociates completely in water", "marks": 2},
            {"part": "2", "label": "2. Definition of weak base", "prompt": "Define a weak base.", "expected_answer": "Dissociates/ionises only partially", "marks": 2},
            {"part": "3", "label": "3. Dissociation vs ionisation", "prompt": "Distinguish dissociation from ionisation.", "expected_answer": "Pre-existing ions separating vs molecules forming new ions", "marks": 2},
            {"part": "4", "label": "4. Higher electrical conductivity", "prompt": "Which solution conducts better?", "expected_answer": "Base X due to higher mobile ion concentration", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp1", "desc": "Strong base: complete dissociation", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Weak base: partial dissociation/ionisation", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Dissociation (ionic lattice splitting) vs ionisation (molecular reaction forming ions)", "marks": 2, "editable": True},
                {"id": "mp4", "desc": "Base X higher conductivity due to greater mobile ion concentration", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Ionic compounds dissociate (ions already exist); covalent molecules ionise (ions are formed by proton transfer).",
            "tier_2": "Electrical conductivity depends directly on the concentration of mobile ions.",
            "tier_3": "Base X dissociates completely, providing more mobile ions and higher conductivity.",
        },
        "misconception_tags": ["dissociation_vs_ionisation_confusion", "conductivity_ion_density_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 12: Concentrated vs Dilute Solutions
# ==============================================================================
def build_12_concentrated_vs_dilute_solutions(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    scenarios = [
        {
            "id_label": "Solution 1",
            "substance": "Hydrochloric acid (HCl)",
            "solute_mol": 5.0,
            "vol_dm3": 1.0,
            "class_str": "Concentrated solution of a strong acid",
        },
        {
            "id_label": "Solution 2",
            "substance": "Hydrochloric acid (HCl)",
            "solute_mol": 0.005,
            "vol_dm3": 1.0,
            "class_str": "Dilute solution of a strong acid",
        },
        {
            "id_label": "Solution 3",
            "substance": "Ethanoic acid (CH3COOH)",
            "solute_mol": 6.0,
            "vol_dm3": 1.0,
            "class_str": "Concentrated solution of a weak acid",
        },
        {
            "id_label": "Solution 4",
            "substance": "Ethanoic acid (CH3COOH)",
            "solute_mol": 0.01,
            "vol_dm3": 1.0,
            "class_str": "Dilute solution of a weak acid",
        },
    ]
    r.shuffle(scenarios)
    s1, s2 = scenarios[0], scenarios[1]

    c1 = s1["solute_mol"] / s1["vol_dm3"]
    c2 = s2["solute_mol"] / s2["vol_dm3"]

    prompt = (
        f"A learner is given two aqueous acid solutions:\n"
        f"- **Beaker P:** Contains ${_fmt_sa(s1['solute_mol'])}\\text{{ mol}}$ of **{s1['substance']}** dissolved in ${_fmt_sa(s1['vol_dm3'])}\\text{{ dm}}^3$ of water.\n"
        f"- **Beaker Q:** Contains ${_fmt_sa(s2['solute_mol'])}\\text{{ mol}}$ of **{s2['substance']}** dissolved in ${_fmt_sa(s2['vol_dm3'])}\\text{{ dm}}^3$ of water.\n\n"
        f"1. Clearly distinguish between the terms **strong** and **concentrated** as applied to acids.\n"
        f"2. Calculate the concentration of the acid in Beaker P and Beaker Q.\n"
        f"3. Classify each solution as one of:\n"
        f"   - *Concentrated strong acid*\n"
        f"   - *Dilute strong acid*\n"
        f"   - *Concentrated weak acid*\n"
        f"   - *Dilute weak acid*"
    )

    sol = (
        f"1. **Distinction:**\n"
        f"   - **Strong/Weak:** Refers to the intrinsic chemical property of the substance—specifically the degree or extent to which molecules ionise in water.\n"
        f"   - **Concentrated/Dilute:** Refers to the proportion of solute present in a given volume of solution ($c = n/V$, ratio of solute to solvent).\n"
        f"2. **Concentration calculations:**\n"
        f"   - Beaker P: $c = \\frac{{n}}{{V}} = \\frac{{{_fmt_sa(s1['solute_mol'])}}}{{{_fmt_sa(s1['vol_dm3'])}}} = {_fmt_sa(c1)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$\n"
        f"   - Beaker Q: $c = \\frac{{n}}{{V}} = \\frac{{{_fmt_sa(s2['solute_mol'])}}}{{{_fmt_sa(s2['vol_dm3'])}}} = {_fmt_sa(c2)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$\n"
        f"3. **Classification:**\n"
        f"   - Beaker P: **{s1['class_str']}**\n"
        f"   - Beaker Q: **{s2['class_str']}**"
    )

    return {
        "id": f"g12_ps_ab_12_{r.randint(10000, 99999)}",
        "subskill": "12_concentrated_vs_dilute_solutions",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Beaker P: {s1['class_str']}; Beaker Q: {s2['class_str']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Strong vs Concentrated distinction", "prompt": "Distinguish strong from concentrated.", "expected_answer": "Extent of ionisation vs ratio of solute to solvent", "marks": 2},
            {"part": "2", "label": "2. Calculate concentrations", "prompt": "Calculate concentrations in P and Q.", "expected_answer": f"cP = {_fmt_sa(c1)} mol/dm3, cQ = {_fmt_sa(c2)} mol/dm3", "marks": 2},
            {"part": "3", "label": "3. Classify solutions", "prompt": "Classify solutions P and Q.", "expected_answer": f"P: {s1['class_str']}, Q: {s2['class_str']}", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Distinction: strong is degree of ionisation; concentrated is ratio of solute to solvent", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Calculated c = n/V for both beakers", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Correct classification of both solutions", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Strength = ionisation extent. Concentration = moles per cubic decimetre.",
            "tier_2": "A strong acid can be dilute if very little is added to water. A weak acid can be concentrated if a large amount is added.",
            "tier_3": f"P is {_fmt_sa(c1)} mol/dm3 ({s1['class_str']}); Q is {_fmt_sa(c2)} mol/dm3 ({s2['class_str']}).",
        },
        "misconception_tags": ["strength_conflated_with_concentration", "solute_solvent_ratio_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 13: Electrical Conductivity of Acid-Base Solutions
# ==============================================================================
def build_13_electrical_conductivity_electrolytes(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    cases = [
        {"acid_a": "1,0 mol/dm3 HCl", "type_a": "strong acid", "acid_b": "1,0 mol/dm3 CH3COOH", "type_b": "weak acid", "winner": "HCl", "reason": "higher concentration of mobile ions due to complete ionisation"},
        {"acid_a": "0,01 mol/dm3 HCl", "type_a": "dilute strong acid", "acid_b": "1,0 mol/dm3 HCl", "type_b": "concentrated strong acid", "winner": "1,0 mol/dm3 HCl", "reason": "greater ion density per unit volume"},
        {"acid_a": "0,1 mol/dm3 H2SO4", "type_a": "diprotic strong acid", "acid_b": "0,1 mol/dm3 HCl", "type_b": "monoprotic strong acid", "winner": "0,1 mol/dm3 H2SO4", "reason": "diprotic ionisation produces twice the hydronium ion concentration"},
    ]
    c = r.choice(cases)

    # Inline SVG representing an electrical conductivity circuit with seed-varied telemetry
    current_val = f"{r.uniform(0.12, 1.85):.2f}".replace('.', ',')
    bulb_fill = r.choice(["#fef08a", "#fde047", "#facc15", "#f59e0b"])
    bulb_r = r.choice([13, 14, 15, 16])
    sol_color = r.choice(["#e0f2fe", "#bae6fd", "#7dd3fc", "#dbeafe"])

    svg_circuit = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 250" width="100%" height="100%">'
        f'<rect width="450" height="250" fill="#f8fafc" rx="8"/>'
        f'<text x="225" y="24" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">ELECTROLYTIC CONDUCTIVITY APPARATUS</text>'
        f'<rect x="150" y="100" width="150" height="120" fill="{sol_color}" stroke="#0284c7" stroke-width="2" rx="4"/>'
        f'<path d="M 150 130 Q 225 140 300 130" stroke="#0284c7" stroke-width="1.5" fill="none"/>'
        f'<text x="225" y="175" font-family="Arial" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Electrolyte Solution</text>'
        f'<text x="225" y="195" font-family="Arial" font-size="11" fill="#475569" text-anchor="middle">Active Test: {c["acid_a"]}</text>'
        f'<rect x="180" y="70" width="12" height="100" fill="#475569" stroke="#1e293b"/>'
        f'<rect x="258" y="70" width="12" height="100" fill="#475569" stroke="#1e293b"/>'
        f'<line x1="186" y1="70" x2="186" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="186" y1="45" x2="100" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="100" y1="45" x2="100" y2="150" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="100" y1="150" x2="140" y2="150" stroke="#1e293b" stroke-width="2"/>'
        f'<circle cx="80" cy="95" r="{bulb_r}" fill="{bulb_fill}" stroke="#ca8a04" stroke-width="2"/>'
        f'<text x="80" y="99" font-family="Arial" font-size="10" font-weight="bold" fill="#854d0e" text-anchor="middle">BULB</text>'
        f'<line x1="264" y1="70" x2="264" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="264" y1="45" x2="350" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="350" y1="45" x2="350" y2="150" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="350" y1="150" x2="310" y2="150" stroke="#1e293b" stroke-width="2"/>'
        f'<circle cx="370" cy="95" r="16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="370" y="94" font-family="Arial" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>'
        f'<text x="370" y="106" font-family="Arial" font-size="9" fill="#2563eb" text-anchor="middle">{current_val} A</text>'
        f'<line x1="215" y1="45" x2="235" y2="45" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="225" y1="35" x2="225" y2="55" stroke="#1e293b" stroke-width="3"/>'
        f'<line x1="230" y1="40" x2="230" y2="50" stroke="#1e293b" stroke-width="1.5"/>'
        f'</svg>'
    )

    prompt = (
        f"A learner sets up an electrical conductivity circuit with carbon electrodes immersed in an acid solution.\n"
        f"The circuit is tested with two different solutions:\n"
        f"- Solution A: **{c['acid_a']}** ({c['type_a']})\n"
        f"- Solution B: **{c['acid_b']}** ({c['type_b']})\n\n"
        f"1. What constitutes an electric current in an electrolyte solution?\n"
        f"2. In which solution will the bulb glow more brightly (and the ammeter record a higher current)?\n"
        f"3. Fully explain your answer with reference to the concentration of **mobile ions**."
    )

    sol = (
        f"1. **Electric current in an electrolyte:** The directed movement (flow) of **mobile ions** (cations toward the cathode, anions toward the anode).\n"
        f"2. **Brighter bulb:** **{c['winner']}**.\n"
        f"3. **Explanation:** Electrical conductivity is directly proportional to the concentration of free mobile ions in solution. "
        f"{c['winner']} provides a {c['reason']}, resulting in lower electrical resistance, greater current flow, and a brighter bulb."
    )

    return {
        "id": f"g12_ps_ab_13_{r.randint(10000, 99999)}",
        "subskill": "13_electrical_conductivity_electrolytes",
        "type": "compound",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg_circuit,
            "diagram_role": "context",
        },
        "prompt": prompt,
        "correct_answer": f"Brighter: {c['winner']}; Reason: {c['reason']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Nature of electrolytic current", "prompt": "What carries current in solution?", "expected_answer": "Mobile ions", "marks": 1},
            {"part": "2", "label": "2. Solution with brighter bulb", "prompt": "Which solution gives brighter bulb?", "expected_answer": c['winner'], "marks": 1},
            {"part": "3", "label": "3. Explanation linking to mobile ions", "prompt": "Explain based on mobile ions.", "expected_answer": c['reason'], "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Identification of mobile ions as charge carriers", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Correct winner: {c['winner']}", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Explanation linking higher ion concentration to greater conductivity", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "In solution, electrons do NOT flow freely; current is carried by dissolved mobile ions.",
            "tier_2": "Higher concentration of ions = lower resistance = higher current = brighter bulb.",
            "tier_3": f"{c['winner']} has a {c['reason']}.",
        },
        "misconception_tags": ["electrons_in_solution_myth", "conductivity_ion_density_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 14: Acid Ionisation Constant Ka Expression
# ==============================================================================
def build_14_acid_ionisation_constant_ka_expression(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    acids = [
        {
            "name": "methanoic acid (HCOOH)",
            "eq": r"\text{HCOOH}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{H}_3\text{O}^+(\text{aq}) + \text{HCOO}^-(\text{aq})",
            "ka_expr": r"K_a = \frac{[\text{H}_3\text{O}^+][\text{HCOO}^-]}{[\text{HCOOH}]}",
            "ka_val": r"1{,}8 \times 10^{-4}",
        },
        {
            "name": "ethanoic acid (CH3COOH)",
            "eq": r"\text{CH}_3\text{COOH}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{H}_3\text{O}^+(\text{aq}) + \text{CH}_3\text{COO}^-(\text{aq})",
            "ka_expr": r"K_a = \frac{[\text{H}_3\text{O}^+][\text{CH}_3\text{COO}^-]}{[\text{CH}_3\text{COOH}]}",
            "ka_val": r"1{,}8 \times 10^{-5}",
        },
        {
            "name": "hydrofluoric acid (HF)",
            "eq": r"\text{HF}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{H}_3\text{O}^+(\text{aq}) + \text{F}^-(\text{aq})",
            "ka_expr": r"K_a = \frac{[\text{H}_3\text{O}^+][\text{F}^-]}{[\text{HF}]}",
            "ka_val": r"6{,}8 \times 10^{-4}",
        },
        {
            "name": "hypochlorous acid (HOCl)",
            "eq": r"\text{HOCl}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{H}_3\text{O}^+(\text{aq}) + \text{OCl}^-(\text{aq})",
            "ka_expr": r"K_a = \frac{[\text{H}_3\text{O}^+][\text{OCl}^-]}{[\text{HOCl}]}",
            "ka_val": r"3{,}0 \times 10^{-8}",
        },
    ]
    ac = r.choice(acids)

    prompt = (
        f"A weak acid, **{ac['name']}**, ionises partially in water according to the equilibrium:\n\n"
        f"$${ac['eq']}$$\n\n"
        f"1. Write down the equilibrium constant expression for $K_a$ for this acid.\n"
        f"2. Explain why the concentration of water ($[\\text{{H}}_2\\text{{O}}(\\text{{l}})]$) is omitted from the $K_a$ expression.\n"
        f"3. Given that $K_a = {ac['ka_val']}$ at $25^\\circ\\text{{C}}$, state whether the equilibrium position favors the products or the reactants. Give a reason."
    )

    sol = (
        f"1. **$K_a$ Expression:**\n"
        f"   $${ac['ka_expr']}$$\n"
        f"2. **Omission of water:** Water is the pure liquid solvent present in vast excess; its concentration remains virtually constant during the ionisation and is incorporated into the constant $K_a$.\n"
        f"3. **Equilibrium position:** The equilibrium lies far to the **left (favors reactants)**. "
        f"Because $K_a \\ll 1$ ($K_a = {ac['ka_val']}$), the numerator ($[\\text{{products}}]$) is far smaller than the denominator ($[\\text{{reactants}}]$), meaning only a tiny fraction of molecules ionise."
    )

    return {
        "id": f"g12_ps_ab_14_{r.randint(10000, 99999)}",
        "subskill": "14_acid_ionisation_constant_ka_expression",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Ka expression: {ac['ka_expr']}; Favors reactants because Ka << 1",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Ka expression", "prompt": "Write Ka expression.", "expected_answer": ac['ka_expr'], "marks": 2},
            {"part": "2", "label": "2. Reason water is omitted", "prompt": "Why is water omitted from Ka?", "expected_answer": "Concentration of pure liquid water is constant", "marks": 1},
            {"part": "3", "label": "3. Position of equilibrium", "prompt": "Which side is favored and why?", "expected_answer": "Reactants favored because Ka << 1", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct Ka expression: {ac['ka_expr']}", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Reason: [H2O(l)] is constant / incorporated into Ka", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Equilibrium favors reactants justified by Ka << 1", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Recall: $K_a = \\frac{[\\text{products}]}{[\\text{reactants}]}$. Pure liquids are omitted.",
            "tier_2": "A small $K_a$ ($< 10^{-3}$) means reactants are favored; very little product is formed.",
            "tier_3": f"${ac['ka_expr']}$; favors reactants because ${ac['ka_val']} < 1$.",
        },
        "misconception_tags": ["water_included_in_ka_error", "ka_magnitude_misinterpretation"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 15: Base Dissociation Constant Kb Expression
# ==============================================================================
def build_15_base_dissociation_constant_kb_expression(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    bases = [
        {
            "name": "ammonia (NH3)",
            "eq": r"\text{NH}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{NH}_4^+(\text{aq}) + \text{OH}^-(\text{aq})",
            "kb_expr": r"K_b = \frac{[\text{NH}_4^+][\text{OH}^-]}{[\text{NH}_3]}",
            "kb_val": r"1{,}8 \times 10^{-5}",
        },
        {
            "name": "methylamine (CH3NH2)",
            "eq": r"\text{CH}_3\text{NH}_2(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{CH}_3\text{NH}_3^+(\text{aq}) + \text{OH}^-(\text{aq})",
            "kb_expr": r"K_b = \frac{[\text{CH}_3\text{NH}_3^+][\text{OH}^-]}{[\text{CH}_3\text{NH}_2]}",
            "kb_val": r"4{,}4 \times 10^{-4}",
        },
        {
            "name": "pyridine (C5H5N)",
            "eq": r"\text{C}_5\text{H}_5\text{N}(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{C}_5\text{H}_5\text{NH}^+(\text{aq}) + \text{OH}^-(\text{aq})",
            "kb_expr": r"K_b = \frac{[\text{C}_5\text{H}_5\text{NH}^+][\text{OH}^-]}{[\text{C}_5\text{H}_5\text{N}]}",
            "kb_val": r"1{,}7 \times 10^{-9}",
        },
    ]
    b = r.choice(bases)

    prompt = (
        f"A weak base, **{b['name']}**, dissolves in water to establish the dynamic equilibrium:\n\n"
        f"$${b['eq']}$$\n\n"
        f"1. Write down the equilibrium constant expression for $K_b$ for this base.\n"
        f"2. How does the magnitude of $K_b$ correlate with base strength?\n"
        f"3. In a $0{{,}}1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ solution of {b['name']} with $K_b = {b['kb_val']}$, "
        f"is $[\\text{{OH}}^-]$ greater than, less than, or equal to $0{{,}}1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$? Explain."
    )

    sol = (
        f"1. **$K_b$ Expression:**\n"
        f"   $${b['kb_expr']}$$\n"
        f"2. **Correlation:** A larger $K_b$ indicates a stronger base that dissociates/ionises to a greater extent, producing a higher $[\\text{{OH}}^-]$ at equilibrium.\n"
        f"3. **Comparison:** $[\\text{{OH}}^-]$ is **less than $0{{,}}1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$**. "
        f"Because $K_b = {b['kb_val']} \\ll 1$, only a tiny fraction of {b['name']} molecules accept protons from water, leaving the vast majority as unreacted molecules."
    )

    return {
        "id": f"g12_ps_ab_15_{r.randint(10000, 99999)}",
        "subskill": "15_base_dissociation_constant_kb_expression",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Kb expression: {b['kb_expr']}; [OH-] < 0,1 mol/dm3",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Kb expression", "prompt": "Write Kb expression.", "expected_answer": b['kb_expr'], "marks": 2},
            {"part": "2", "label": "2. Kb correlation with strength", "prompt": "How does Kb correlate with strength?", "expected_answer": "Larger Kb means stronger base", "marks": 1},
            {"part": "3", "label": "3. [OH-] comparison to initial conc", "prompt": "Is [OH-] greater, less, or equal?", "expected_answer": "Less than 0.1 mol/dm3", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct Kb expression: {b['kb_expr']}", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Statement that higher Kb corresponds to stronger base", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Deduction that [OH-] < initial conc due to incomplete ionisation", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "$K_b = \\frac{[\\text{BH}^+][\\text{OH}^-]}{[\\text{B}]}$.",
            "tier_2": "Because the base is weak ($K_b \\ll 1$), ionisation is very small, so $[OH^-] \\ll c_{\\text{initial}}$.",
            "tier_3": f"${b['kb_expr']}$; $[OH^-] < 0{{,}}1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ because $K_b = {b['kb_val']}$.",
        },
        "misconception_tags": ["kb_expression_error", "weak_base_100_percent_dissociation_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 16: Ranking Acid & Base Strength using Ka and Kb
# ==============================================================================
def build_16_ranking_acid_base_strength_ka_kb(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    acid_data = [
        {"name": "Hydrofluoric acid (HF)", "formula": r"\text{HF}", "ka": 6.8e-4, "ka_str": r"6{,}8 \times 10^{-4}", "conj_base": r"\text{F}^-"},
        {"name": "Methanoic acid (HCOOH)", "formula": r"\text{HCOOH}", "ka": 1.8e-4, "ka_str": r"1{,}8 \times 10^{-4}", "conj_base": r"\text{HCOO}^-"},
        {"name": "Ethanoic acid (CH3COOH)", "formula": r"\text{CH}_3\text{COOH}", "ka": 1.8e-5, "ka_str": r"1{,}8 \times 10^{-5}", "conj_base": r"\text{CH}_3\text{COO}^-"},
        {"name": "Hypochlorous acid (HOCl)", "formula": r"\text{HOCl}", "ka": 3.0e-8, "ka_str": r"3{,}0 \times 10^{-8}", "conj_base": r"\text{OCl}^-"},
    ]
    r.shuffle(acid_data)
    subset = acid_data[:3]
    # Sort by Ka descending
    sorted_acids = sorted(subset, key=lambda x: x["ka"], reverse=True)
    strongest_acid = sorted_acids[0]
    weakest_acid = sorted_acids[-1]

    prompt = (
        f"The table below lists the acid ionisation constants ($K_a$) for three weak acids at $25^\\circ\\text{{C}}$:\n\n"
        f"| Acid | Formula | $K_a$ value |\n"
        f"| :--- | :---: | :---: |\n"
        f"| {subset[0]['name']} | ${subset[0]['formula']}$ | ${subset[0]['ka_str']}$ |\n"
        f"| {subset[1]['name']} | ${subset[1]['formula']}$ | ${subset[1]['ka_str']}$ |\n"
        f"| {subset[2]['name']} | ${subset[2]['formula']}$ | ${subset[2]['ka_str']}$ |\n\n"
        f"1. Arrange the three acids in order of **decreasing acid strength** (strongest to weakest).\n"
        f"2. Identify the **strongest conjugate base** among the conjugate bases of these three acids. Explain your reasoning.\n"
        f"3. For equimolar solutions ($0{{,}}1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$) of these three acids, which one will have the **highest pH**?"
    )

    sol = (
        f"1. **Decreasing acid strength:**\n"
        f"   $${sorted_acids[0]['formula']} > {sorted_acids[1]['formula']} > {sorted_acids[2]['formula']}$$\n"
        f"   (Higher $K_a$ value indicates greater extent of ionisation, hence stronger acid).\n"
        f"2. **Strongest conjugate base:** **${weakest_acid['conj_base']}$** (conjugate base of ${weakest_acid['formula']}$).\n"
        f"   Reason: The weaker an acid, the stronger its conjugate base (since $K_a \\times K_b = K_w$). "
        f"Since ${weakest_acid['formula']}$ has the smallest $K_a$, its conjugate base has the largest $K_b$ and greatest affinity for protons.\n"
        f"3. **Highest pH:** **${weakest_acid['formula']}$**. The weakest acid produces the lowest $[\\text{{H}}_3\\text{{O}}^+]$, and because $\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+]$, the lowest hydronium concentration results in the highest pH."
    )

    return {
        "id": f"g12_ps_ab_16_{r.randint(10000, 99999)}",
        "subskill": "16_ranking_acid_base_strength_ka_kb",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Order: {sorted_acids[0]['formula']} > {sorted_acids[1]['formula']} > {sorted_acids[2]['formula']}; Strongest base: {weakest_acid['conj_base']}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Order of decreasing strength", "prompt": "Rank acids strongest to weakest.", "expected_answer": f"{sorted_acids[0]['formula']} > {sorted_acids[1]['formula']} > {sorted_acids[2]['formula']}", "marks": 2},
            {"part": "2", "label": "2. Strongest conjugate base and reason", "prompt": "Identify strongest conjugate base and justify.", "expected_answer": f"{weakest_acid['conj_base']} because weaker acid has stronger conjugate base", "marks": 2},
            {"part": "3", "label": "3. Highest pH solution", "prompt": "Which equimolar solution has highest pH?", "expected_answer": f"{weakest_acid['formula']} due to lowest [H3O+]", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Correct ranking of acids from highest to lowest Ka", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Identification of weakest acid's conjugate base as strongest base", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Weakest acid identified as having highest pH", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Larger $K_a$ = stronger acid = lower pH. The weaker the acid, the stronger its conjugate base.",
            "tier_2": "$K_a \\times K_b = K_w$. Therefore, the smallest $K_a$ gives the largest $K_b$.",
            "tier_3": f"Strongest acid: ${sorted_acids[0]['formula']}$; Strongest conjugate base: ${weakest_acid['conj_base']}$; Highest pH: ${weakest_acid['formula']}$.",
        },
        "misconception_tags": ["ka_ranking_inverted", "conjugate_pair_strength_inversion_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 17: Successive Ka Comparison for Polyprotic Acids
# ==============================================================================
def build_17_polyprotic_successive_ka_comparison(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    acids = [
        {
            "name": "oxalic acid (ethanedioic acid)",
            "formula": r"\text{H}_2\text{C}_2\text{O}_4",
            "ka1": r"5{,}6 \times 10^{-2}",
            "ka2": r"5{,}4 \times 10^{-5}",
            "step1_eq": r"\text{H}_2\text{C}_2\text{O}_4(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{HC}_2\text{O}_4^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
            "step2_eq": r"\text{HC}_2\text{O}_4^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{C}_2\text{O}_4^{2-}(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
        },
        {
            "name": "sulfurous acid",
            "formula": r"\text{H}_2\text{SO}_3",
            "ka1": r"1{,}4 \times 10^{-2}",
            "ka2": r"6{,}3 \times 10^{-8}",
            "step1_eq": r"\text{H}_2\text{SO}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{HSO}_3^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
            "step2_eq": r"\text{HSO}_3^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{SO}_3^{2-}(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
        },
        {
            "name": "carbonic acid",
            "formula": r"\text{H}_2\text{CO}_3",
            "ka1": r"4{,}3 \times 10^{-7}",
            "ka2": r"5{,}6 \times 10^{-11}",
            "step1_eq": r"\text{H}_2\text{CO}_3(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{HCO}_3^-(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
            "step2_eq": r"\text{HCO}_3^-(\text{aq}) + \text{H}_2\text{O}(\text{l}) \rightleftharpoons \text{CO}_3^{2-}(\text{aq}) + \text{H}_3\text{O}^+(\text{aq})",
        },
    ]
    ac = r.choice(acids)

    prompt = (
        f"**{ac['name']}** (${ac['formula']}$) is a diprotic acid that ionises in two successive stages:\n\n"
        f"Stage 1: $${ac['step1_eq']} \\quad (K_{{a1}} = {ac['ka1']})$$\n"
        f"Stage 2: $${ac['step2_eq']} \\quad (K_{{a2}} = {ac['ka2']})$$\n\n"
        f"1. Compare the numerical values of $K_{{a1}}$ and $K_{{a2}}$.\n"
        f"2. Explain, in terms of electrostatic forces and ionic charge, why $K_{{a1}} \\gg K_{{a2}}$ for all polyprotic acids.\n"
        f"3. In a solution of ${ac['formula']}$, which species will have a higher concentration: the intermediate mono-anion or the fully deprotonated di-anion?"
    )

    sol = (
        f"1. **Comparison:** $K_{{a1}}$ (${ac['ka1']}$) is several orders of magnitude greater than $K_{{a2}}$ (${ac['ka2']}$).\n"
        f"2. **Electrostatic explanation:**\n"
        f"   - In Stage 1, a positively charged proton ($H^+$) is removed from a neutral molecule (${ac['formula']}$).\n"
        f"   - In Stage 2, a proton ($H^+$) must be removed from an already negatively charged anion ($-1$ charge).\n"
        f"   - Strong electrostatic attraction between the negative anion and the positive proton makes removing the second proton significantly more difficult, resulting in a much smaller $K_{{a2}}$.\n"
        f"3. **Higher concentration:** The intermediate mono-anion. Because Stage 1 ionises to a far greater extent than Stage 2, very little of the intermediate is converted to the di-anion."
    )

    return {
        "id": f"g12_ps_ab_17_{r.randint(10000, 99999)}",
        "subskill": "17_polyprotic_successive_ka_comparison",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": "Ka1 >> Ka2; Electrostatic attraction to negative ion hinders second deprotonation",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Compare Ka1 and Ka2", "prompt": "Compare Ka1 and Ka2.", "expected_answer": "Ka1 is much greater than Ka2", "marks": 1},
            {"part": "2", "label": "2. Electrostatic explanation", "prompt": "Explain why Ka1 >> Ka2.", "expected_answer": "Removing H+ from a negative ion requires overcoming strong electrostatic attraction", "marks": 2},
            {"part": "3", "label": "3. Concentration comparison", "prompt": "Which ion has higher concentration?", "expected_answer": "The intermediate mono-anion", "marks": 1},
        ],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Statement that Ka1 >> Ka2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explanation: electrostatic attraction between negative anion and positive H+ hinders second deprotonation", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Deduction that mono-anion concentration is higher than di-anion", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "It is always easier to remove a positive proton from a neutral molecule than from a negative ion.",
            "tier_2": "Opposite charges attract: the negative charge on the intermediate holds onto the remaining proton tightly.",
            "tier_3": "$K_{a1} \\gg K_{a2}$ due to electrostatic attraction between $-1$ anion and $H^+$.",
        },
        "misconception_tags": ["electrostatic_ionisation_barrier_error", "equal_ka_fallacy"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 18: pH Calculation of Strong Monoprotic Acid
# ==============================================================================
def build_18_ph_strong_monoprotic_acid(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    acid = r.choice(["HCl", "HNO3", "HBr"])
    conc = r.choice([0.005, 0.01, 0.02, 0.035, 0.05, 0.08, 0.12, 0.25])
    h3o = conc
    ph = round(-math.log10(h3o), 2)

    prompt = (
        f"A laboratory assistant prepares a standard aqueous solution of **{acid}** with a concentration of "
        f"**${_fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** at $25^\\circ\\text{{C}}$.\n\n"
        f"1. Explain why **{acid}** is classified as a strong monoprotic acid.\n"
        f"2. Write down the concentration of hydronium ions ($[\\text{{H}}_3\\text{{O}}^+]$) in this solution.\n"
        f"3. Calculate the pH of the solution."
    )

    sol = (
        f"1. **Strong monoprotic acid:** {acid} ionises completely in water ($100\\%$ ionisation) and each molecule donates exactly one proton ($H^+$).\n"
        f"2. **Hydronium concentration:**\n"
        f"   $${acid}(\\text{{aq}}) + \\text{{H}}_2\\text{{O}}(\\text{{l}}) \\rightarrow \\text{{H}}_3\\text{{O}}^+(\\text{{aq}}) + \\text{{X}}^-(\\text{{aq}})$$\n"
        f"   Mole ratio of ${acid} : \\text{{H}}_3\\text{{O}}^+ = 1 : 1$\n"
        f"   $$[\\text{{H}}_3\\text{{O}}^+] = {_fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **pH calculation:**\n"
        f"   $$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = -\\log({_fmt_sa(conc)}) = {_fmt_sa(ph)}$$"
    )

    return {
        "id": f"g12_ps_ab_18_{r.randint(10000, 99999)}",
        "subskill": "18_ph_strong_monoprotic_acid",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"pH = {_fmt_sa(ph)}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Strong monoprotic classification", "prompt": "Why strong monoprotic?", "expected_answer": "Complete ionisation, donates one proton per molecule", "marks": 2},
            {"part": "2", "label": "2. [H3O+] value", "prompt": "State [H3O+].", "expected_answer": f"{_fmt_sa(conc)} mol/dm3", "marks": 1},
            {"part": "3", "label": "3. pH calculation", "prompt": "Calculate pH.", "expected_answer": _fmt_sa(ph), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Definition of strong monoprotic acid", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Correct [H3O+] = {_fmt_sa(conc)} mol/dm3", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Formula pH = -log[H3O+]", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final pH = {_fmt_sa(ph)}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "For a strong monoprotic acid, $[H_3O^+] = c_{\\text{acid}}$.",
            "tier_2": "Substitute directly into $pH = -\\log[H_3O^+]$.",
            "tier_3": f"$\\text{{pH}} = -\\log({_fmt_sa(conc)}) = {_fmt_sa(ph)}$.",
        },
        "misconception_tags": ["negative_log_sign_error", "rounding_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 19: pH Calculation of Strong Diprotic Acid (H2SO4)
# ==============================================================================
def build_19_ph_strong_diprotic_acid(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    conc = r.choice([0.005, 0.01, 0.015, 0.02, 0.025, 0.04, 0.05])
    h3o = 2 * conc
    ph = round(-math.log10(h3o), 2)

    prompt = (
        f"A solution of sulphuric acid, $\\text{{H}}_2\\text{{SO}}_4$, has a concentration of "
        f"**${_fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** at $25^\\circ\\text{{C}}$.\n\n"
        f"1. Explain why sulphuric acid is classified as a **diprotic** acid.\n"
        f"2. Assuming complete ionisation of both protons in aqueous solution, write down the concentration of hydronium ions ($[\\text{{H}}_3\\text{{O}}^+]$).\n"
        f"3. Calculate the pH of the solution."
    )

    sol = (
        f"1. **Diprotic acid:** Each molecule of $\\text{{H}}_2\\text{{SO}}_4$ can donate two protons ($2\\text{{ H}}^+$ ions) during complete ionisation.\n"
        f"2. **Hydronium concentration:**\n"
        f"   $$\\text{{H}}_2\\text{{SO}}_4(\\text{{aq}}) + 2\\text{{H}}_2\\text{{O}}(\\text{{l}}) \\rightarrow 2\\text{{H}}_3\\text{{O}}^+(\\text{{aq}}) + \\text{{SO}}_4^{{2-}}(\\text{{aq}})$$\n"
        f"   Mole ratio: $1\\text{{ mol }}\\text{{H}}_2\\text{{SO}}_4 : 2\\text{{ mol }}\\text{{H}}_3\\text{{O}}^+$\n"
        f"   $$[\\text{{H}}_3\\text{{O}}^+] = 2 \\times c = 2 \\times {_fmt_sa(conc)} = {_fmt_sa(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **pH calculation:**\n"
        f"   $$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = -\\log({_fmt_sa(h3o)}) = {_fmt_sa(ph)}$$"
    )

    return {
        "id": f"g12_ps_ab_19_{r.randint(10000, 99999)}",
        "subskill": "19_ph_strong_diprotic_acid",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"[H3O+] = {_fmt_sa(h3o)} mol/dm3; pH = {_fmt_sa(ph)}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Diprotic definition", "prompt": "Why diprotic?", "expected_answer": "Donates two protons per molecule", "marks": 1},
            {"part": "2", "label": "2. Hydronium concentration", "prompt": "State [H3O+].", "expected_answer": f"{_fmt_sa(h3o)} mol/dm3", "marks": 2},
            {"part": "3", "label": "3. pH calculation", "prompt": "Calculate pH.", "expected_answer": _fmt_sa(ph), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Diprotic: donates 2 protons per molecule", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Factor of 2 applied: [H3O+] = 2 x c = {_fmt_sa(h3o)}", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Formula pH = -log[H3O+]", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Final pH = {_fmt_sa(ph)}", "marks": 1, "editable": True},
            ],
            "deductions": [{"rule": "forgot_diprotic_factor_h2so4", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Warning: $\\text{H}_2\\text{SO}_4$ is diprotic—do not forget to multiply the concentration by 2!",
            "tier_2": "$[H_3O^+] = 2 \\times c_{\\text{acid}}$.",
            "tier_3": f"$[H_3O^+] = 2 \\times {_fmt_sa(conc)} = {_fmt_sa(h3o)}$; $pH = -\\log({_fmt_sa(h3o)}) = {_fmt_sa(ph)}$.",
        },
        "misconception_tags": ["forgot_diprotic_factor_h2so4", "h2so4_monoprotic_assumption"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 20: Hydronium and Hydroxide from Given pH
# ==============================================================================
def build_20_hydronium_concentration_from_ph(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    ph = round(r.uniform(1.8, 3.6), 2)
    h3o = 10.0 ** (-ph)
    oh = 1.0e-14 / h3o

    prompt = (
        f"A sample of lemon juice has a measured pH of **{_fmt_sa(ph)}** at $25^\\circ\\text{{C}}$.\n\n"
        f"1. State the relationship between $[\\text{{H}}_3\\text{{O}}^+]$ and pH.\n"
        f"2. Calculate the concentration of hydronium ions ($[\\text{{H}}_3\\text{{O}}^+]$) in the sample.\n"
        f"3. Using $K_w = [\\text{{H}}_3\\text{{O}}^+][\\text{{OH}}^-] = 1{{,}}0 \\times 10^{{-14}}$, calculate the hydroxide ion concentration ($[\\text{{OH}}^-]$)."
    )

    sol = (
        f"1. **Relationship:** $\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] \\iff [\\text{{H}}_3\\text{{O}}^+] = 10^{{-\\text{{pH}}}}$\n"
        f"2. **Hydronium concentration:**\n"
        f"   $$[\\text{{H}}_3\\text{{O}}^+] = 10^{{-{_fmt_sa(ph)}}} = {_fmt_sci(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **Hydroxide concentration:**\n"
        f"   $$[\\text{{OH}}^-] = \\frac{{K_w}}{{[\\text{{H}}_3\\text{{O}}^+]}} = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sci(h3o)}}} = {_fmt_sci(oh)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$"
    )

    return {
        "id": f"g12_ps_ab_20_{r.randint(10000, 99999)}",
        "subskill": "20_hydronium_concentration_from_ph",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"[H3O+] = {_fmt_sci(h3o)} mol/dm3; [OH-] = {_fmt_sci(oh)} mol/dm3",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Relationship formula", "prompt": "State formula relating [H3O+] and pH.", "expected_answer": "[H3O+] = 10^-pH", "marks": 1},
            {"part": "2", "label": "2. Calculate [H3O+]", "prompt": "Calculate [H3O+].", "expected_answer": _fmt_sci(h3o), "marks": 2},
            {"part": "3", "label": "3. Calculate [OH-]", "prompt": "Calculate [OH-].", "expected_answer": _fmt_sci(oh), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": "Inverse log formula: [H3O+] = 10^-pH", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculated [H3O+] = {_fmt_sci(h3o)}", "marks": 2, "editable": True},
                {"id": "mp3", "desc": "Kw expression: [OH-] = Kw / [H3O+]", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculated [OH-] = {_fmt_sci(oh)}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "To invert the log: $[H_3O^+] = 10^{-pH}$.",
            "tier_2": "Use the water ion product: $K_w = [H_3O^+][OH^-] = 1{{,}}0 \\times 10^{-14}$.",
            "tier_3": f"$[H_3O^+] = 10^{{-{_fmt_sa(ph)}}} = {_fmt_sci(h3o)}$; $[OH^-] = {_fmt_sci(oh)}$.",
        },
        "misconception_tags": ["antilog_calculator_error", "kw_substitution_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 21: pH of Strong Monobasic Base (NaOH / KOH)
# ==============================================================================
def build_21_ph_strong_monobasic_hydroxide(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    base = r.choice(["NaOH", "KOH", "LiOH"])
    conc = r.choice([0.01, 0.02, 0.04, 0.05, 0.08, 0.12, 0.25])
    oh = conc
    h3o = 1.0e-14 / oh
    ph = round(-math.log10(h3o), 2)

    prompt = (
        f"A standard aqueous solution of **{base}** has a concentration of "
        f"**${_fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** at $25^\\circ\\text{{C}}$.\n\n"
        f"1. State the hydroxide ion concentration ($[\\text{{OH}}^-]$) of the solution.\n"
        f"2. Calculate the hydronium ion concentration ($[\\text{{H}}_3\\text{{O}}^+]$) using $K_w = 1{{,}}0 \\times 10^{{-14}}$.\n"
        f"3. Calculate the pH of the solution."
    )

    sol = (
        f"1. **Hydroxide concentration:**\n"
        f"   {base} is a strong, completely dissociated monobasic hydroxide:\n"
        f"   $$[\\text{{OH}}^-] = {_fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"2. **Hydronium concentration:**\n"
        f"   $$[\\text{{H}}_3\\text{{O}}^+] = \\frac{{K_w}}{{[\\text{{OH}}^-]}} = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sa(conc)}}} = {_fmt_sci(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **pH calculation:**\n"
        f"   $$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = -\\log({_fmt_sci(h3o)}) = {_fmt_sa(ph)}$$"
    )

    return {
        "id": f"g12_ps_ab_21_{r.randint(10000, 99999)}",
        "subskill": "21_ph_strong_monobasic_hydroxide",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"[H3O+] = {_fmt_sci(h3o)} mol/dm3; pH = {_fmt_sa(ph)}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. [OH-] value", "prompt": "State [OH-].", "expected_answer": f"{_fmt_sa(conc)} mol/dm3", "marks": 1},
            {"part": "2", "label": "2. Calculate [H3O+]", "prompt": "Calculate [H3O+].", "expected_answer": _fmt_sci(h3o), "marks": 2},
            {"part": "3", "label": "3. Calculate pH", "prompt": "Calculate pH.", "expected_answer": _fmt_sa(ph), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct [OH-] = {_fmt_sa(conc)}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Kw expression: [H3O+] = Kw / [OH-]", "marks": 1, "editable": True},
                {"id": "mp3", "desc": f"Calculated [H3O+] = {_fmt_sci(h3o)}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Formula and final pH = {_fmt_sa(ph)}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Remember: For a base, first find $[OH^-]$, then find $[H_3O^+]$ using $K_w$, and finally find pH.",
            "tier_2": "Do NOT calculate $-\\log[OH^-]$ and call it pH! That gives pOH, so $\\text{pH} = 14 - \\text{pOH}$.",
            "tier_3": f"$[H_3O^+] = \\frac{{1{{,}}0 \\times 10^{-14}}}{{{_fmt_sa(conc)}}} = {_fmt_sci(h3o)}$; $pH = {_fmt_sa(ph)}$.",
        },
        "misconception_tags": ["poh_confused_with_ph", "kw_inversion_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
    }


# ==============================================================================
# Subskill 22: pH of Strong Dibasic Base (Ba(OH)2 / Ca(OH)2)
# ==============================================================================
def build_22_ph_strong_dibasic_hydroxide(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    base = r.choice(["Ba(OH)_2", "Ca(OH)_2"])
    base_name = "Barium hydroxide" if "Ba" in base else "Calcium hydroxide"
    conc = r.choice([0.005, 0.01, 0.015, 0.02, 0.035, 0.05])
    oh = 2 * conc
    h3o = 1.0e-14 / oh
    ph = round(-math.log10(h3o), 2)

    prompt = (
        f"A standard solution of **{base_name}** (${base}$) has a concentration of "
        f"**${_fmt_sa(conc)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** at $25^\\circ\\text{{C}}$.\n\n"
        f"1. Write down the dissociation equation for ${base}$ in water.\n"
        f"2. Calculate the concentration of hydroxide ions ($[\\text{{OH}}^-]$).\n"
        f"3. Calculate the pH of the solution at $25^\\circ\\text{{C}}$."
    )

    sol = (
        f"1. **Dissociation equation:**\n"
        f"   $${base}(\\text{{s}}) \\xrightarrow{{\\text{{H}}_2\\text{{O}}}} \\text{{M}}^{{2+}}(\\text{{aq}}) + 2\\text{{OH}}^-(\\text{{aq}})$$\n"
        f"2. **Hydroxide concentration:**\n"
        f"   Each mole of ${base}$ dissociates to produce $2\\text{{ moles}}$ of $\\text{{OH}}^-$.\n"
        f"   $$[\\text{{OH}}^-] = 2 \\times c = 2 \\times {_fmt_sa(conc)} = {_fmt_sa(oh)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **pH calculation:**\n"
        f"   $$[\\text{{H}}_3\\text{{O}}^+] = \\frac{{K_w}}{{[\\text{{OH}}^-]}} = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sa(oh)}}} = {_fmt_sci(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"   $$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = {_fmt_sa(ph)}$$"
    )

    return {
        "id": f"g12_ps_ab_22_{r.randint(10000, 99999)}",
        "subskill": "22_ph_strong_dibasic_hydroxide",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"[OH-] = {_fmt_sa(oh)} mol/dm3; pH = {_fmt_sa(ph)}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Dissociation equation", "prompt": "Write dissociation equation.", "expected_answer": f"{base} -> M2+ + 2OH-", "marks": 2},
            {"part": "2", "label": "2. [OH-] calculation", "prompt": "Calculate [OH-].", "expected_answer": f"{_fmt_sa(oh)} mol/dm3", "marks": 2},
            {"part": "3", "label": "3. pH calculation", "prompt": "Calculate pH.", "expected_answer": _fmt_sa(ph), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Balanced dissociation equation with 2OH-", "marks": 2, "editable": True},
                {"id": "mp2", "desc": f"Factor of 2 applied: [OH-] = 2 x c = {_fmt_sa(oh)}", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Kw substitution and final pH = {_fmt_sa(ph)}", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "forgot_dibasic_factor_base", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": f"${base}$ releases TWO hydroxide ions per formula unit: $[OH^-] = 2c$.",
            "tier_2": "Find $[H_3O^+]$ using $K_w / [OH^-]$, then take $-\\log[H_3O^+]$.",
            "tier_3": f"$[OH^-] = {_fmt_sa(oh)}$; $[H_3O^+] = {_fmt_sci(h3o)}$; $pH = {_fmt_sa(ph)}$.",
        },
        "misconception_tags": ["forgot_dibasic_factor_base", "poh_confused_with_ph"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 23: pH After Dilution with Water
# ==============================================================================
def build_23_ph_dilution_calculations(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    is_acid = r.choice([True, False])
    v1 = r.choice([20.0, 25.0, 50.0])
    v_added = r.choice([80.0, 150.0, 200.0, 250.0, 450.0])
    v2 = v1 + v_added

    if is_acid:
        substance = "hydrochloric acid (HCl)"
        c1 = r.choice([0.1, 0.2, 0.5])
        c2 = (c1 * v1) / v2
        ph1 = round(-math.log10(c1), 2)
        ph2 = round(-math.log10(c2), 2)
        prompt = (
            f"A learner has **${_fmt_sa(v1)}\\text{{ cm}}^3$** of a **${_fmt_sa(c1)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** solution of **{substance}**.\n"
            f"Distilled water of volume **${_fmt_sa(v_added)}\\text{{ cm}}^3$** is added to dilute the solution.\n\n"
            f"1. Calculate the initial pH of the solution before dilution.\n"
            f"2. Calculate the new concentration ($c_2$) of the acid after dilution.\n"
            f"3. Calculate the new pH of the diluted solution and state whether the pH increased or decreased."
        )
        sol = (
            f"1. **Initial pH:** $\\text{{pH}}_1 = -\\log({_fmt_sa(c1)}) = {_fmt_sa(ph1)}$\n"
            f"2. **Dilution formula:**\n"
            f"   $$c_1 V_1 = c_2 V_2 \\implies c_2 = \\frac{{c_1 V_1}}{{V_2}}$$\n"
            f"   Total volume $V_2 = V_1 + V_{{\\text{{added}}}} = {_fmt_sa(v1)} + {_fmt_sa(v_added)} = {_fmt_sa(v2)}\\text{{ cm}}^3$\n"
            f"   $$c_2 = \\frac{{{_fmt_sa(c1)} \\times {_fmt_sa(v1)}}}{{{_fmt_sa(v2)}}} = {_fmt_sa(c2, 4)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
            f"3. **Final pH:**\n"
            f"   $$\\text{{pH}}_2 = -\\log({_fmt_sa(c2, 4)}) = {_fmt_sa(ph2)}$$\n"
            f"   The pH **increased** toward neutral 7 (acidity decreased)."
        )
    else:
        substance = "sodium hydroxide (NaOH)"
        c1 = r.choice([0.1, 0.2, 0.5])
        c2 = (c1 * v1) / v2
        ph1 = round(14.0 - (-math.log10(c1)), 2)
        ph2 = round(14.0 - (-math.log10(c2)), 2)
        prompt = (
            f"A learner has **${_fmt_sa(v1)}\\text{{ cm}}^3$** of a **${_fmt_sa(c1)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** solution of **{substance}**.\n"
            f"Distilled water of volume **${_fmt_sa(v_added)}\\text{{ cm}}^3$** is added to dilute the solution.\n\n"
            f"1. Calculate the initial pH of the solution before dilution at $25^\\circ\\text{{C}}$.\n"
            f"2. Calculate the new concentration ($c_2$) of the base after dilution.\n"
            f"3. Calculate the new pH of the diluted solution and state whether the pH increased or decreased."
        )
        sol = (
            f"1. **Initial pH:** $[\\text{{H}}_3\\text{{O}}^+] = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sa(c1)}}} \\implies \\text{{pH}}_1 = {_fmt_sa(ph1)}$\n"
            f"2. **Dilution formula:**\n"
            f"   $$c_1 V_1 = c_2 V_2 \\implies c_2 = \\frac{{c_1 V_1}}{{V_2}}$$\n"
            f"   Total volume $V_2 = {_fmt_sa(v1)} + {_fmt_sa(v_added)} = {_fmt_sa(v2)}\\text{{ cm}}^3$\n"
            f"   $$c_2 = \\frac{{{_fmt_sa(c1)} \\times {_fmt_sa(v1)}}}{{{_fmt_sa(v2)}}} = {_fmt_sa(c2, 4)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
            f"3. **Final pH:**\n"
            f"   $$[\\text{{H}}_3\\text{{O}}^+] = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sa(c2, 4)}}} \\implies \\text{{pH}}_2 = {_fmt_sa(ph2)}$$\n"
            f"   The pH **decreased** toward neutral 7 (alkalinity decreased)."
        )

    return {
        "id": f"g12_ps_ab_23_{r.randint(10000, 99999)}",
        "subskill": "23_ph_dilution_calculations",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"Initial pH = {_fmt_sa(ph1)}; Diluted pH = {_fmt_sa(ph2)}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Initial pH calculation", "prompt": "Calculate initial pH.", "expected_answer": _fmt_sa(ph1), "marks": 2},
            {"part": "2", "label": "2. Concentration after dilution", "prompt": "Calculate new concentration c2.", "expected_answer": _fmt_sa(c2, 4), "marks": 2},
            {"part": "3", "label": "3. Final pH calculation", "prompt": "Calculate final pH and trend.", "expected_answer": _fmt_sa(ph2), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": f"Initial pH = {_fmt_sa(ph1)}", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Dilution equation c1V1 = c2V2 with V2 = V1 + V_added", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Final pH = {_fmt_sa(ph2)} and correct direction statement", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "forgot_to_add_initial_volume", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Careful: Total final volume $V_2 = V_1 + V_{\\text{added}}$, not just the added volume!",
            "tier_2": "Use $c_1 V_1 = c_2 V_2$ to find the new concentration $c_2$.",
            "tier_3": f"$V_2 = {_fmt_sa(v2)}$; $c_2 = {_fmt_sa(c2, 4)}$; final $pH = {_fmt_sa(ph2)}$.",
        },
        "misconception_tags": ["dilution_volume_addition_omission", "ph_dilution_trend_confusion"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Subskill 24: Weak Acid Equilibrium pH Calculation (Ka)
# ==============================================================================
def build_24_ph_weak_acid_equilibrium_calc(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    acids = [
        {"name": "ethanoic acid (CH3COOH)", "formula": r"\text{CH}_3\text{COOH}", "ka": 1.8e-5, "ka_str": r"1{,}8 \times 10^{-5}"},
        {"name": "methanoic acid (HCOOH)", "formula": r"\text{HCOOH}", "ka": 1.8e-4, "ka_str": r"1{,}8 \times 10^{-4}"},
        {"name": "hydrofluoric acid (HF)", "formula": r"\text{HF}", "ka": 6.8e-4, "ka_str": r"6{,}8 \times 10^{-4}"},
    ]
    ac = r.choice(acids)
    c = r.choice([0.05, 0.1, 0.15, 0.2, 0.25, 0.5])
    # Ka = x^2 / c => x = sqrt(Ka * c)
    h3o = math.sqrt(ac["ka"] * c)
    ph = round(-math.log10(h3o), 2)
    percent_ion = round((h3o / c) * 100, 2)

    prompt = (
        f"A chemist prepares a **${_fmt_sa(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** solution of **{ac['name']}** at $25^\\circ\\text{{C}}$.\n"
        f"The acid ionisation constant is **$K_a = {ac['ka_str']}$**.\n\n"
        f"1. Write down the $K_a$ equilibrium expression for ${ac['formula']}$.\n"
        f"2. Assuming that $[\\text{{H}}_3\\text{{O}}^+] \\ll {_fmt_sa(c)}$, calculate the hydronium ion concentration ($[\\text{{H}}_3\\text{{O}}^+]$) at equilibrium.\n"
        f"3. Calculate the pH of the solution and the percentage of acid molecules that have ionised."
    )

    sol = (
        f"1. **$K_a$ expression:**\n"
        f"   $$K_a = \\frac{{[\\text{{H}}_3\\text{{O}}^+][\\text{{A}}^-]}}{{[\\text{{HA}}]}}$$\n"
        f"2. **Equilibrium calculation:**\n"
        f"   Let $[\\text{{H}}_3\\text{{O}}^+] = [\\text{{A}}^-] = x$.\n"
        f"   At equilibrium, $[\\text{{HA}}] = c - x \\approx c = {_fmt_sa(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ (since $K_a \\ll 1$).\n"
        f"   $$K_a = \\frac{{x^2}}{{c}} \\implies x = \\sqrt{{K_a \\times c}} = \\sqrt{{{ac['ka_str']} \\times {_fmt_sa(c)}}} = {_fmt_sci(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **pH and percentage ionisation:**\n"
        f"   $$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = -\\log({_fmt_sci(h3o)}) = {_fmt_sa(ph)}$$\n"
        f"   $$\\% \\text{{ ionisation}} = \\frac{{[\\text{{H}}_3\\text{{O}}^+]}}{{c_{{\\text{{initial}}}}}} \\times 100 = \\frac{{{_fmt_sci(h3o)}}}{{{_fmt_sa(c)}}} \\times 100 = {_fmt_sa(percent_ion)}\\%$$"
    )

    return {
        "id": f"g12_ps_ab_24_{r.randint(10000, 99999)}",
        "subskill": "24_ph_weak_acid_equilibrium_calc",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"[H3O+] = {_fmt_sci(h3o)} mol/dm3; pH = {_fmt_sa(ph)}; % ionised = {_fmt_sa(percent_ion)}%",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Ka equilibrium expression", "prompt": "Write Ka expression.", "expected_answer": "Ka = [H3O+][A-] / [HA]", "marks": 1},
            {"part": "2", "label": "2. Calculate [H3O+]", "prompt": "Calculate [H3O+].", "expected_answer": _fmt_sci(h3o), "marks": 3},
            {"part": "3", "label": "3. Calculate pH and % ionisation", "prompt": "Calculate pH and % ionised.", "expected_answer": f"pH = {_fmt_sa(ph)}, % = {_fmt_sa(percent_ion)}%", "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Ka expression with products over reactants", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Approximation [HA] approx c and substitution x^2 / c = Ka", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Calculated [H3O+] = {_fmt_sci(h3o)}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Calculated pH = {_fmt_sa(ph)} and % ionisation = {_fmt_sa(percent_ion)}%", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "For a weak acid: $K_a \\approx \\frac{x^2}{c}$, where $x = [H_3O^+]$.",
            "tier_2": "$[H_3O^+] = \\sqrt{K_a \\times c}$. Then $pH = -\\log[H_3O^+]$.",
            "tier_3": f"$[H_3O^+] = {_fmt_sci(h3o)}$; $pH = {_fmt_sa(ph)}$; $\\% = {_fmt_sa(percent_ion)}\\%$.",
        },
        "misconception_tags": ["weak_acid_treated_as_strong", "quadratic_approximation_error"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 5,
    }


# ==============================================================================
# Subskill 25: Weak Base Equilibrium pH Calculation (Kb)
# ==============================================================================
def build_25_ph_weak_base_equilibrium_calc(seed: Optional[int] = None) -> Dict[str, Any]:
    r = _rng(seed)
    bases = [
        {"name": "ammonia (NH3)", "formula": r"\text{NH}_3", "kb": 1.8e-5, "kb_str": r"1{,}8 \times 10^{-5}"},
        {"name": "methylamine (CH3NH2)", "formula": r"\text{CH}_3\text{NH}_2", "kb": 4.4e-4, "kb_str": r"4{,}4 \times 10^{-4}"},
    ]
    b = r.choice(bases)
    c = r.choice([0.05, 0.1, 0.15, 0.2, 0.25])
    # Kb = x^2 / c => x = [OH-] = sqrt(Kb * c)
    oh = math.sqrt(b["kb"] * c)
    h3o = 1.0e-14 / oh
    ph = round(-math.log10(h3o), 2)

    prompt = (
        f"A cleaning solution contains aqueous **{b['name']}** with an initial concentration of "
        f"**${_fmt_sa(c)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$** at $25^\\circ\\text{{C}}$.\n"
        f"The base dissociation constant is **$K_b = {b['kb_str']}$**.\n\n"
        f"1. Write down the $K_b$ expression for ${b['formula']}$.\n"
        f"2. Calculate the hydroxide ion concentration ($[\\text{{OH}}^-]$) at equilibrium.\n"
        f"3. Calculate the pH of the cleaning solution."
    )

    sol = (
        f"1. **$K_b$ expression:**\n"
        f"   $$K_b = \\frac{{[\\text{{BH}}^+][\\text{{OH}}^-]}}{{[\\text{{B}}]}}$$\n"
        f"2. **Hydroxide calculation:**\n"
        f"   Let $[\\text{{OH}}^-] = [\\text{{BH}}^+] = x$.\n"
        f"   $$K_b = \\frac{{x^2}}{{c}} \\implies x = \\sqrt{{K_b \\times c}} = \\sqrt{{{b['kb_str']} \\times {_fmt_sa(c)}}} = {_fmt_sci(oh)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"3. **pH calculation:**\n"
        f"   $$[\\text{{H}}_3\\text{{O}}^+] = \\frac{{1{{,}}0 \\times 10^{{-14}}}}{{{_fmt_sci(oh)}}} = {_fmt_sci(h3o)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$\n"
        f"   $$\\text{{pH}} = -\\log[\\text{{H}}_3\\text{{O}}^+] = {_fmt_sa(ph)}$$"
    )

    return {
        "id": f"g12_ps_ab_25_{r.randint(10000, 99999)}",
        "subskill": "25_ph_weak_base_equilibrium_calc",
        "type": "compound",
        "prompt": prompt,
        "correct_answer": f"[OH-] = {_fmt_sci(oh)} mol/dm3; pH = {_fmt_sa(ph)}",
        "worked_solution": sol,
        "sub_parts": [
            {"part": "1", "label": "1. Kb expression", "prompt": "Write Kb expression.", "expected_answer": "Kb = [BH+][OH-] / [B]", "marks": 1},
            {"part": "2", "label": "2. Calculate [OH-]", "prompt": "Calculate [OH-].", "expected_answer": _fmt_sci(oh), "marks": 3},
            {"part": "3", "label": "3. Calculate pH", "prompt": "Calculate pH.", "expected_answer": _fmt_sa(ph), "marks": 2},
        ],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp1", "desc": "Kb expression with products over reactants", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Approximation and substitution x = sqrt(Kb * c)", "marks": 2, "editable": True},
                {"id": "mp3", "desc": f"Calculated [OH-] = {_fmt_sci(oh)}", "marks": 1, "editable": True},
                {"id": "mp4", "desc": f"Kw substitution and final pH = {_fmt_sa(ph)}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "For a weak base: $[OH^-] = \\sqrt{K_b \\times c}$.",
            "tier_2": "Convert $[OH^-]$ to $[H_3O^+]$ using $K_w = 1{{,}}0 \\times 10^{-14}$, then find pH.",
            "tier_3": f"$[OH^-] = {_fmt_sci(oh)}$; $[H_3O^+] = {_fmt_sci(h3o)}$; $pH = {_fmt_sa(ph)}$.",
        },
        "misconception_tags": ["weak_base_treated_as_strong", "poh_confused_with_ph"],
        "term": 2,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
    }


# ==============================================================================
# Mapping dictionary of builders 01 to 25
# ==============================================================================
BUILDERS_01_25 = {
    "01_arrhenius_acid_base_definitions": build_01_arrhenius_acid_base_definitions,
    "02_bronsted_lowry_proton_donor_acceptor": build_02_bronsted_lowry_proton_donor_acceptor,
    "03_conjugate_acid_base_pairs": build_03_conjugate_acid_base_pairs,
    "04_conjugate_pairs_organic_acids": build_04_conjugate_pairs_organic_acids,
    "05_conjugate_pairs_polyprotic": build_05_conjugate_pairs_polyprotic,
    "06_amphiprotic_water_behavior": build_06_amphiprotic_water_behavior,
    "07_amphiprotic_ions": build_07_amphiprotic_ions,
    "08_autoprotolysis_water_kw": build_08_autoprotolysis_water_kw,
    "09_temperature_dependence_kw": build_09_temperature_dependence_kw,
    "10_strong_vs_weak_acids_ionisation": build_10_strong_vs_weak_acids_ionisation,
    "11_strong_vs_weak_bases_dissociation": build_11_strong_vs_weak_bases_dissociation,
    "12_concentrated_vs_dilute_solutions": build_12_concentrated_vs_dilute_solutions,
    "13_electrical_conductivity_electrolytes": build_13_electrical_conductivity_electrolytes,
    "14_acid_ionisation_constant_ka_expression": build_14_acid_ionisation_constant_ka_expression,
    "15_base_dissociation_constant_kb_expression": build_15_base_dissociation_constant_kb_expression,
    "16_ranking_acid_base_strength_ka_kb": build_16_ranking_acid_base_strength_ka_kb,
    "17_polyprotic_successive_ka_comparison": build_17_polyprotic_successive_ka_comparison,
    "18_ph_strong_monoprotic_acid": build_18_ph_strong_monoprotic_acid,
    "19_ph_strong_diprotic_acid": build_19_ph_strong_diprotic_acid,
    "20_hydronium_concentration_from_ph": build_20_hydronium_concentration_from_ph,
    "21_ph_strong_monobasic_hydroxide": build_21_ph_strong_monobasic_hydroxide,
    "22_ph_strong_dibasic_hydroxide": build_22_ph_strong_dibasic_hydroxide,
    "23_ph_dilution_calculations": build_23_ph_dilution_calculations,
    "24_ph_weak_acid_equilibrium_calc": build_24_ph_weak_acid_equilibrium_calc,
    "25_ph_weak_base_equilibrium_calc": build_25_ph_weak_base_equilibrium_calc,
}
