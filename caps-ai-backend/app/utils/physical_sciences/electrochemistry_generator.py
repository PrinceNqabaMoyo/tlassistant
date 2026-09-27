"""Electrochemistry & Chemical Change Generator (Grades 9 & 12 Physical/Natural Sciences).

Complies with the 6-pillar South African CAPS contract:
- Term & calendar metadata
- Deconstructible compound and elementary sub-drills
- Standardized misconception taxonomy
- Teacher-editable marking schema with official [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention
"""

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float, decimals: int = 2) -> str:
    """Formats a float using South African comma decimal convention."""
    if abs(val - round(val)) < 1e-6:
        return str(int(round(val)))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    return f"{prefix}_{seed or 'rnd'}_{idx}"


STANDARD_REDUCTION_POTENTIALS = {
    "Zn": {"symbol": "Zn", "half_rx": "\\text{Zn}^{2+} + 2e^- \\rightleftharpoons \\text{Zn}", "e0": -0.76, "name": "zinc"},
    "Cu": {"symbol": "Cu", "half_rx": "\\text{Cu}^{2+} + 2e^- \\rightleftharpoons \\text{Cu}", "e0": 0.34, "name": "copper"},
    "Mg": {"symbol": "Mg", "half_rx": "\\text{Mg}^{2+} + 2e^- \\rightleftharpoons \\text{Mg}", "e0": -2.37, "name": "magnesium"},
    "Ag": {"symbol": "Ag", "half_rx": "\\text{Ag}^+ + e^- \\rightleftharpoons \\text{Ag}", "e0": 0.80, "name": "silver"},
    "Pb": {"symbol": "Pb", "half_rx": "\\text{Pb}^{2+} + 2e^- \\rightleftharpoons \\text{Pb}", "e0": -0.13, "name": "lead"},
    "Ni": {"symbol": "Ni", "half_rx": "\\text{Ni}^{2+} + 2e^- \\rightleftharpoons \\text{Ni}", "e0": -0.27, "name": "nickel"},
    "Al": {"symbol": "Al", "half_rx": "\\text{Al}^{3+} + 3e^- \\rightleftharpoons \\text{Al}", "e0": -1.66, "name": "aluminium"},
}


def _generate_gr9_acids_bases(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 9 Natural Sciences: Acids, bases, pH scale and neutralisation."""
    acid_pairs = [
        ("hydrochloric acid (HCl)", "sodium hydroxide (NaOH)", "sodium chloride (NaCl)", "water (H2O)"),
        ("sulfuric acid (H2SO4)", "potassium hydroxide (KOH)", "potassium sulfate (K2SO4)", "water (H2O)"),
        ("nitric acid (HNO3)", "sodium hydroxide (NaOH)", "sodium nitrate (NaNO3)", "water (H2O)"),
    ]
    acid, base, salt, water = r.choice(acid_pairs)
    test_ph = r.choice([2, 4, 7, 9, 12])

    qid = _make_id("ns9_acids_bases", seed, idx)

    if mode == "elementary_ph_scale":
        prompt = (
            f"A learner tests the pH of an unknown clear household cleaning solution using a calibrated digital pH meter and records a value of ${_fmt_sa(test_ph)}.\n\n"
            f"1. Classify the solution as acidic, neutral, or alkaline (basic).\n"
            f"2. State what color bromothymol blue indicator would turn when added to this solution."
        )
        if test_ph < 7:
            nature = "acidic"
            indicator_color = "yellow"
        elif test_ph == 7:
            nature = "neutral"
            indicator_color = "green"
        else:
            nature = "alkaline (basic)"
            indicator_color = "blue"

        ans_str = f"1. {nature}; 2. {indicator_color}"
        memo = (
            f"1. Classification [1]: pH {_fmt_sa(test_ph)} is {nature} (pH < 7 is acidic, pH = 7 is neutral, pH > 7 is alkaline). [1]\n"
            f"2. Bromothymol blue color [1]: {indicator_color}. [1]"
        )
        hints = {
            "tier_1": "Recall the pH scale from 0 to 14. 7 is neutral, below 7 is acidic, above 7 is basic.",
            "tier_2": "Bromothymol blue is yellow in acid, green in neutral, and blue in base.",
            "tier_3": f"pH = {test_ph} is {nature}. Indicator turns {indicator_color}.",
        }
        marks = 2
    else:
        prompt = (
            f"A Grade 9 learner carries out a neutralisation reaction between {acid} and {base}.\n\n"
            f"1. Define the term *neutralisation reaction*.\n"
            f"2. Write a general word equation for the reaction between an acid and a metal hydroxide.\n"
            f"3. Name the specific salt produced in this reaction.\n"
            f"4. If equal amounts of concentrated {acid} and {base} react completely, what will the approximate pH of the resulting solution be?"
        )
        ans_str = (
            f"1. Chemical reaction where an acid and a base react to form a salt and water; "
            f"2. Acid + Base -> Salt + Water; "
            f"3. {salt}; "
            f"4. pH = 7"
        )
        memo = (
            f"1. Definition [2]: A chemical reaction in which an acid reacts with a base to produce a salt and water (neutralising each other's properties). [2]\n"
            f"2. General word equation [2]: $$\\text{{Acid}} + \\text{{Base (metal hydroxide)}} \\to \\text{{Salt}} + \\text{{Water}}$$ [2]\n"
            f"3. Specific salt formed [1]: {salt}. [1]\n"
            f"4. Resulting pH [1]: pH 7 (neutral solution). [1]"
        )
        hints = {
            "tier_1": "Neutralisation produces two main products: a salt and water.",
            "tier_2": "The metal from the base replaces hydrogen in the acid to form the salt.",
            "tier_3": f"Salt: {salt}. Resulting pH is 7.",
        }
        marks = 6

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["acid_base_salt_naming_error", "confused_indicator_color_ranges", "ph_scale_interpretation_error"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of neutralisation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "General word equation", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Specific salt identification and pH", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr12_galvanic_cell(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 12: Galvanic electrochemical cells, standard potentials, and cell notation."""
    pairs = [
        ("Zn", "Cu"),
        ("Mg", "Cu"),
        ("Al", "Cu"),
        ("Pb", "Ag"),
        ("Ni", "Ag"),
        ("Zn", "Ag"),
    ]
    anode_key, cathode_key = r.choice(pairs)
    anode_data = STANDARD_REDUCTION_POTENTIALS[anode_key]
    cathode_data = STANDARD_REDUCTION_POTENTIALS[cathode_key]

    e0_anode = anode_data["e0"]
    e0_cathode = cathode_data["e0"]
    e0_cell = round(e0_cathode - e0_anode, 2)

    qid = _make_id("ps12_galvanic", seed, idx)

    if mode == "elementary_galvanic_cell_potential":
        prompt = (
            f"A standard electrochemical cell is set up consisting of a {anode_data['name']} half-cell "
            f"($E^\\circ = {_fmt_sa(e0_anode)}\\text{{ V}}$) and a {cathode_data['name']} half-cell "
            f"($E^\\circ = {_fmt_sa(e0_cathode)}\\text{{ V}}$).\n\n"
            f"1. Identify which electrode acts as the cathode.\n"
            f"2. Calculate the standard cell potential ($E^\\circ_{{\\text{{cell}}}}$) of this cell."
        )
        ans_str = f"1. Cathode: {cathode_data['name']} ({cathode_key}); 2. E0_cell = {_fmt_sa(e0_cell)} V"
        memo = (
            f"1. Cathode identification [1]: {cathode_data['name']} ({cathode_key}) has the more positive standard reduction potential "
            f"(${_fmt_sa(e0_cathode)}\\text{{ V}} > {_fmt_sa(e0_anode)}\\text{{ V}}$), hence it undergoes reduction at the cathode. [1]\n"
            f"2. Cell potential calculation [2]:\n"
            f"   $$E^\\circ_{{\\text{{cell}}}} = E^\\circ_{{\\text{{cathode}}}} - E^\\circ_{{\\text{{anode}}}} = ({_fmt_sa(e0_cathode)}) - ({_fmt_sa(e0_anode)}) = {_fmt_sa(e0_cell)}\\text{{ V}}$$ [M+A]"
        )
        hints = {
            "tier_1": "The half-cell with the higher (more positive) reduction potential is the cathode.",
            "tier_2": "Formula: E0_cell = E0_cathode - E0_anode.",
            "tier_3": f"E0_cell = {e0_cathode} - ({e0_anode}) = {e0_cell:.2f} V.",
        }
        marks = 3
    else:
        # Full compound 11-mark Grade 12 exam question
        prompt = (
            f"An electrochemical cell is set up under standard conditions using a {anode_data['name']} ({anode_key}) electrode dipped into a "
            f"$1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ {anode_key}$^{{2+}}$ solution and a {cathode_data['name']} ({cathode_key}) electrode "
            f"dipped into a $1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ {cathode_key}$^{{2+}}$ solution. "
            f"A salt bridge containing concentrated potassium chloride ($\\text{{KCl}}$) connects the two beakers.\n\n"
            f"1. State the TWO standard conditions applicable to solutions and temperature in this cell.\n"
            f"2. Identify the ANODE in this cell and write down the oxidation half-reaction taking place.\n"
            f"3. Write down the reduction half-reaction taking place at the cathode.\n"
            f"4. Write down the overall balanced net ionic cell reaction.\n"
            f"5. Write down the cell notation for this galvanic cell.\n"
            f"6. State TWO functions of the salt bridge.\n"
            f"7. Calculate the standard cell potential ($E^\\circ_{{\\text{{cell}}}}$)."
        )
        ans_str = (
            f"1. Temp = 25 C (298 K), Concentration = 1 mol/dm3; "
            f"2. Anode: {anode_key}, {anode_key} -> {anode_key}^(2+) + 2e-; "
            f"3. {cathode_key}^(2+) + 2e- -> {cathode_key}; "
            f"4. {anode_key}(s) + {cathode_key}^(2+)(aq) -> {anode_key}^(2+)(aq) + {cathode_key}(s); "
            f"5. {anode_key}(s) | {anode_key}^(2+)(1 mol/dm3) || {cathode_key}^(2+)(1 mol/dm3) | {cathode_key}(s); "
            f"6. Completes circuit, maintains electrical neutrality; "
            f"7. E0_cell = {_fmt_sa(e0_cell)} V"
        )
        memo = (
            f"1. Standard conditions [2]:\n"
            f"   - Temperature: $25^\\circ\\text{{C}}$ (or $298\\text{{ K}}$) [1]\n"
            f"   - Concentration of electrolytes: $1\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$ [1]\n"
            f"2. Anode & Oxidation half-reaction [2]:\n"
            f"   - Anode: {anode_key} (has lower reduction potential ${_fmt_sa(e0_anode)}\\text{{ V}}$) [1]\n"
            f"   - Half-reaction: $$\\text{{{anode_key}(s)}} \\to \\text{{{anode_key}}}^{{2+}}\\text{{(aq)}} + 2e^-$$ [1]\n"
            f"3. Cathode & Reduction half-reaction [1]:\n"
            f"   $$\\text{{{cathode_key}}}^{{2+}}\\text{{(aq)}} + 2e^- \\to \\text{{{cathode_key}(s)}}$$ [1]\n"
            f"4. Overall balanced net cell reaction [2]:\n"
            f"   $$\\text{{{anode_key}(s)}} + \\text{{{cathode_key}}}^{{2+}}\\text{{(aq)}} \\to \\text{{{anode_key}}}^{{2+}}\\text{{(aq)}} + \\text{{{cathode_key}(s)}}$$ [2]\n"
            f"5. Standard cell notation [2]:\n"
            f"   $$\\text{{{anode_key}(s)}} \\mid \\text{{{anode_key}}}^{{2+}}\\text{{(aq, 1 mol}}\\cdot\\text{{dm}}^{{-3}}\\text{{)}} \\parallel \\text{{{cathode_key}}}^{{2+}}\\text{{(aq, 1 mol}}\\cdot\\text{{dm}}^{{-3}}\\text{{)}} \\mid \\text{{{cathode_key}(s)}}$$ [2]\n"
            f"6. Functions of the salt bridge [2]:\n"
            f"   - Completes the electric circuit [1]\n"
            f"   - Maintains electrical neutrality in both half-cells by ion migration [1]\n"
            f"7. Cell potential calculation [2]:\n"
            f"   $$E^\\circ_{{\\text{{cell}}}} = E^\\circ_{{\\text{{cathode}}}} - E^\\circ_{{\\text{{anode}}}} = ({_fmt_sa(e0_cathode)}) - ({_fmt_sa(e0_anode)}) = {_fmt_sa(e0_cell)}\\text{{ V}}$$ [M+A]"
        )
        hints = {
            "tier_1": "Recall: Anode is oxidation (loss of electrons). Cathode is reduction (gain of electrons).",
            "tier_2": "Cell notation is always written: Anode | Anode ion || Cathode ion | Cathode.",
            "tier_3": f"E0_cell = {e0_cathode} - ({e0_anode}) = {e0_cell:.2f} V.",
        }
        marks = 13

    return {
        "id": qid,
        "question_id": qid,
        "term": 3,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 14,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": [
            "anode_cathode_inversion",
            "sign_error_standard_potential",
            "cell_notation_phase_boundary_inverted",
            "salt_bridge_function_misunderstood",
        ],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Standard conditions statements", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Anode and oxidation half-reaction", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Cathode reduction half-reaction", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Overall balanced net ionic equation", "marks": 2, "editable": True},
                {"id": "mp_5", "desc": "Standard cell notation formatting", "marks": 2, "editable": True},
                {"id": "mp_6", "desc": "Salt bridge dual functions", "marks": 2, "editable": True},
                {"id": "mp_7", "desc": "Standard cell potential calculation", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_cell_potential_unit_volt", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "12",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Electrochemistry & Chemical Change."""
    r = random.Random(seed)
    questions = []

    for i in range(count):
        gr_str = str(grade).strip()
        if gr_str == "9":
            q = _generate_gr9_acids_bases(r, seed, i, mode)
        else:
            q = _generate_gr12_galvanic_cell(r, seed, i, mode)
        questions.append(q)

    return questions
