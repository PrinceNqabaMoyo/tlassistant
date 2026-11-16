"""Physical Sciences Grade 11 Term 3 — Types of Reaction & Volumetric Titrations.
Archetypes 01 to 25: Arrhenius and Brønsted-Lowry acid-base models, amphiprotic species,
conjugate acid-base pairs, polyprotic acids, neutralisation reactions, acid-metal/carbonate reactions,
standard solution preparation, titration technique and indicators, volumetric titration calculations,
oxidation numbers, and redox reactions (half-reactions, electron transfer, and displacement).

Complies with the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import fmt_sa, make_science_question

TOPIC = "grade11_physical_sciences_acids_bases_stoichiometry"
LO = "ps11_types_of_reaction"


def _build_q(
    subskill: str,
    prompt: str,
    ans: str,
    hints: Dict[str, str],
    schema: Dict[str, Any],
    diag: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    marks = schema.get("total_marks", 7)
    return make_science_question(
        prefix="ps11_ab",
        topic=TOPIC,
        subskill=subskill,
        learning_objective_id=LO,
        prompt=prompt,
        prompt_latex=prompt,
        answer_latex=ans,
        sample_answer=ans,
        marking_schema=schema,
        hints=hints,
        misconception_tags=[f"{subskill}_concept_error"],
        keywords=[subskill, TOPIC],
        term=3,
        caps_weight_percent=20,
        suggested_duration_mins=7,
        marks=marks,
        diagram_spec=diag,
    )


# --------------------------------------------------------------------------- #
# Subskill 01: Arrhenius Acid-Base Definitions & Limitations
# --------------------------------------------------------------------------- #
def builder_01_arrhenius_acid_base_definitions(rng: random.Random) -> Dict[str, Any]:
    acids = [
        ("hydrochloric acid", "\\text{HCl}", "\\text{H}^+"),
        ("nitric acid", "\\text{HNO}_3", "\\text{H}^+"),
        ("hydrobromic acid", "\\text{HBr}", "\\text{H}^+"),
    ]
    bases = [
        ("sodium hydroxide", "\\text{NaOH}", "\\text{OH}^-"),
        ("potassium hydroxide", "\\text{KOH}", "\\text{OH}^-"),
        ("lithium hydroxide", "\\text{LiOH}", "\\text{OH}^-"),
    ]
    acid_name, acid_form, acid_ion = rng.choice(acids)
    base_name, base_form, base_ion = rng.choice(bases)

    prompt = (
        f"In aqueous solution, {acid_name} ({acid_form}) and {base_name} ({base_form}) dissolve and undergo ionisation or dissociation.\n\n"
        f"1. State the Arrhenius definition of an acid.\n"
        f"2. State the Arrhenius definition of a base.\n"
        f"3. Write down the chemical formula of the characteristic ion responsible for the acidic behaviour of aqueous {acid_form}.\n"
        f"4. State one primary limitation of the Arrhenius model regarding non-aqueous solvents and substances such as gaseous ammonia."
    )
    ans = (
        f"1. An acid is a substance that produces hydrogen ions (H+ or H3O+) when dissolved in water; "
        f"2. A base is a substance that produces hydroxide ions (OH-) when dissolved in water; "
        f"3. {acid_ion} (or H3O+); "
        f"4. The Arrhenius model is strictly limited to aqueous solutions and fails to explain basicity in substances without OH- groups (like NH3) or in non-aqueous solvents."
    )
    memo = (
        f"1. Arrhenius acid definition [2]: A substance that produces hydrogen ions ($\\text{{H}}^+$ / $\\text{{H}}_3\\text{{O}}^+$) in aqueous solution. [2]\n"
        f"2. Arrhenius base definition [2]: A substance that produces hydroxide ions ($\\text{{OH}}^-$) in aqueous solution. [2]\n"
        f"3. Characteristic ion [1]: ${acid_ion}$ (or $\\text{{H}}_3\\text{{O}}^+$). [1]\n"
        f"4. Limitation [2]: Limited strictly to aqueous solutions; cannot explain acid-base reactions in the gas phase or non-aqueous media, or bases lacking hydroxide groups like $\\text{{NH}}_3$. [2]"
    )
    hints = {
        "tier_1": "Recall what ions are released into water according to Svante Arrhenius.",
        "tier_2": "Acids increase [H+]/[H3O+], while bases increase [OH-] in aqueous solution.",
        "tier_3": "Arrhenius applies only to aqueous solutions and requires OH- in the chemical formula of a base.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Arrhenius acid definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Arrhenius base definition", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Formula of hydrogen or hydronium ion", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Limitation of Arrhenius model", "marks": 2, "editable": True},
        ],
    }
    return _build_q("01_arrhenius_acid_base_definitions", prompt, ans, hints, schema)


# --------------------------------------------------------------------------- #
# Subskill 02: Brønsted-Lowry Proton Transfer
# --------------------------------------------------------------------------- #
def builder_02_bronsted_lowry_proton_transfer(rng: random.Random) -> Dict[str, Any]:
    systems = [
        {
            "eq": "\\text{NH}_3\\text{(aq)} + \\text{H}_2\\text{O(l)} \\rightleftharpoons \\text{NH}_4^+\\text{(aq)} + \\text{OH}^-\\text{(aq)}",
            "acid": "\\text{H}_2\\text{O}",
            "base": "\\text{NH}_3",
            "acid_reason": "donates a proton (H+) to NH3",
            "base_reason": "accepts a proton (H+) from H2O",
        },
        {
            "eq": "\\text{HCl(g)} + \\text{NH}_3\\text{(g)} \\rightarrow \\text{NH}_4\\text{Cl(s)}",
            "acid": "\\text{HCl}",
            "base": "\\text{NH}_3",
            "acid_reason": "donates a proton (H+) to NH3",
            "base_reason": "accepts a proton (H+) from HCl",
        },
        {
            "eq": "\\text{HCOOH(aq)} + \\text{H}_2\\text{O(l)} \\rightleftharpoons \\text{HCOO}^-\\text{(aq)} + \\text{H}_3\\text{O}^+\\text{(aq)}",
            "acid": "\\text{HCOOH}",
            "base": "\\text{H}_2\\text{O}",
            "acid_reason": "donates a proton (H+) to H2O",
            "base_reason": "accepts a proton (H+) from HCOOH",
        },
        {
            "eq": "\\text{CH}_3\\text{COOH(aq)} + \\text{H}_2\\text{O(l)} \\rightleftharpoons \\text{CH}_3\\text{COO}^-\\text{(aq)} + \\text{H}_3\\text{O}^+\\text{(aq)}",
            "acid": "\\text{CH}_3\\text{COOH}",
            "base": "\\text{H}_2\\text{O}",
            "acid_reason": "donates a proton (H+) to H2O",
            "base_reason": "accepts a proton (H+) from CH3COOH",
        },
    ]
    sys = rng.choice(systems)

    prompt = (
        f"Consider the chemical system represented by the equation:\n"
        f"$${sys['eq']}$$\n\n"
        f"1. Define an acid according to the Brønsted-Lowry theory.\n"
        f"2. Define a base according to the Brønsted-Lowry theory.\n"
        f"3. Identify the Brønsted-Lowry acid in the forward reaction and justify your choice in terms of proton transfer.\n"
        f"4. Identify the Brønsted-Lowry base in the forward reaction and justify your choice in terms of proton transfer."
    )
    ans = (
        f"1. A Brønsted-Lowry acid is a proton (H+) donor; "
        f"2. A Brønsted-Lowry base is a proton (H+) acceptor; "
        f"3. Acid: {sys['acid']} because it {sys['acid_reason']}; "
        f"4. Base: {sys['base']} because it {sys['base_reason']}."
    )
    memo = (
        f"1. Brønsted-Lowry acid definition [2]: A proton ($\\text{{H}}^+$) donor. [2]\n"
        f"2. Brønsted-Lowry base definition [2]: A proton ($\\text{{H}}^+$) acceptor. [2]\n"
        f"3. Acid identification & justification [2]: ${sys['acid']}$ [1]; it {sys['acid_reason']}. [1]\n"
        f"4. Base identification & justification [2]: ${sys['base']}$ [1]; it {sys['base_reason']}. [1]"
    )
    hints = {
        "tier_1": "Recall which species loses a hydrogen ion and which species gains one.",
        "tier_2": "Proton donor = acid; proton acceptor = base.",
        "tier_3": f"In this reaction, {sys['acid']} donates a proton to {sys['base']}.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Brønsted-Lowry acid definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Brønsted-Lowry base definition", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Acid identification and reason", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Base identification and reason", "marks": 2, "editable": True},
        ],
    }
    return _build_q("02_bronsted_lowry_proton_transfer", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 03: Amphiprotic / Amphoteric Substances
# --------------------------------------------------------------------------- #
def builder_03_amphiprotic_amphoteric_substances(rng: random.Random) -> Dict[str, Any]:
    ampholytes = [
        {
            "species": "\\text{HSO}_4^-",
            "name": "hydrogen sulphate ion",
            "acid_eq": "\\text{HSO}_4^- + \\text{H}_2\\text{O} \\rightleftharpoons \\text{SO}_4^{2-} + \\text{H}_3\\text{O}^+",
            "base_eq": "\\text{HSO}_4^- + \\text{H}_3\\text{O}^+ \\rightleftharpoons \\text{H}_2\\text{SO}_4 + \\text{H}_2\\text{O}",
            "base_partner": "\\text{H}_3\\text{O}^+",
        },
        {
            "species": "\\text{HCO}_3^-",
            "name": "hydrogen carbonate ion",
            "acid_eq": "\\text{HCO}_3^- + \\text{OH}^- \\rightleftharpoons \\text{CO}_3^{2-} + \\text{H}_2\\text{O}",
            "base_eq": "\\text{HCO}_3^- + \\text{HCl} \\rightarrow \\text{H}_2\\text{CO}_3 + \\text{Cl}^-",
            "base_partner": "\\text{HCl}",
        },
        {
            "species": "\\text{H}_2\\text{O}",
            "name": "water",
            "acid_eq": "\\text{H}_2\\text{O} + \\text{NH}_3 \\rightleftharpoons \\text{OH}^- + \\text{NH}_4^+",
            "base_eq": "\\text{H}_2\\text{O} + \\text{HCl} \\rightarrow \\text{H}_3\\text{O}^+ + \\text{Cl}^-",
            "base_partner": "\\text{HCl}",
        },
        {
            "species": "\\text{HPO}_4^{2-}",
            "name": "hydrogen phosphate ion",
            "acid_eq": "\\text{HPO}_4^{2-} + \\text{OH}^- \\rightleftharpoons \\text{PO}_4^{3-} + \\text{H}_2\\text{O}",
            "base_eq": "\\text{HPO}_4^{2-} + \\text{H}_3\\text{O}^+ \\rightleftharpoons \\text{H}_2\\text{PO}_4^- + \\text{H}_2\\text{O}",
            "base_partner": "\\text{H}_3\\text{O}^+",
        },
    ]
    item = rng.choice(ampholytes)

    prompt = (
        f"Certain chemical species exhibit the ability to act as either an acid or a base depending on the reacting partner.\n\n"
        f"1. Define an *amphiprotic substance* (ampholyte).\n"
        f"2. Explain why the {item['name']} (${item['species']}$) is classified as an amphiprotic substance.\n"
        f"3. Write a balanced chemical equation demonstrating ${item['species']}$ acting as an acid.\n"
        f"4. Write a balanced chemical equation demonstrating ${item['species']}$ acting as a base."
    )
    ans = (
        f"1. An amphiprotic substance is a substance that can act as either a proton donor (acid) or a proton acceptor (base); "
        f"2. {item['name']} ({item['species']}) has an ionisable hydrogen atom to donate and a negative charge/lone pair to accept a proton; "
        f"3. As acid: {item['acid_eq']}; "
        f"4. As base: {item['base_eq']}."
    )
    memo = (
        f"1. Amphiprotic definition [2]: A substance that can act as either a proton ($\\text{{H}}^+$) donor or a proton acceptor. [2]\n"
        f"2. Explanation [2]: It possesses an ionisable proton that it can donate, and can also accept a proton into its structure. [2]\n"
        f"3. Equation as acid [2]: $${item['acid_eq']}$$ (Correct reactants & products [1], balanced [1])\n"
        f"4. Equation as base [2]: $${item['base_eq']}$$ (Correct reactants & products [1], balanced [1])"
    )
    hints = {
        "tier_1": "Recall what amphiprotic means in terms of protons (H+).",
        "tier_2": "Show one equation where the species loses H+ and one equation where it gains H+.",
        "tier_3": f"When {item['species']} acts as an acid it becomes the deprotonated form; when acting as a base it gains H+.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Amphiprotic definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Explanation of dual capability", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Balanced equation as acid", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Balanced equation as base", "marks": 2, "editable": True},
        ],
    }
    return _build_q("03_amphiprotic_amphoteric_substances", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 04: Conjugate Acid-Base Pairs
# --------------------------------------------------------------------------- #
def builder_04_conjugate_acid_base_pairs(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "eq": "\\text{HNO}_2\\text{(aq)} + \\text{H}_2\\text{O(l)} \\rightleftharpoons \\text{NO}_2^-\\text{(aq)} + \\text{H}_3\\text{O}^+\\text{(aq)}",
            "acid_1": "\\text{HNO}_2",
            "base_1": "\\text{NO}_2^-",
            "base_2": "\\text{H}_2\\text{O}",
            "acid_2": "\\text{H}_3\\text{O}^+",
        },
        {
            "eq": "\\text{HSO}_4^-\\text{(aq)} + \\text{NH}_3\\text{(aq)} \\rightleftharpoons \\text{SO}_4^{2-}\\text{(aq)} + \\text{NH}_4^+\\text{(aq)}",
            "acid_1": "\\text{HSO}_4^-",
            "base_1": "\\text{SO}_4^{2-}",
            "base_2": "\\text{NH}_3",
            "acid_2": "\\text{NH}_4^+",
        },
        {
            "eq": "\\text{H}_2\\text{S(aq)} + \\text{H}_2\\text{O(l)} \\rightleftharpoons \\text{HS}^-\\text{(aq)} + \\text{H}_3\\text{O}^+\\text{(aq)}",
            "acid_1": "\\text{H}_2\\text{S}",
            "base_1": "\\text{HS}^-",
            "base_2": "\\text{H}_2\\text{O}",
            "acid_2": "\\text{H}_3\\text{O}^+",
        },
        {
            "eq": "\\text{CH}_3\\text{COOH(aq)} + \\text{CN}^-\\text{(aq)} \\rightleftharpoons \\text{CH}_3\\text{COO}^-\\text{(aq)} + \\text{HCN(aq)}",
            "acid_1": "\\text{CH}_3\\text{COOH}",
            "base_1": "\\text{CH}_3\\text{COO}^-",
            "base_2": "\\text{CN}^-",
            "acid_2": "\\text{HCN}",
        },
    ]
    rxn = rng.choice(reactions)

    prompt = (
        f"Consider the reversible acid-base reaction:\n"
        f"$${rxn['eq']}$$\n\n"
        f"1. Define a *conjugate acid-base pair*.\n"
        f"2. Identify the first conjugate acid-base pair in the reaction.\n"
        f"3. Identify the second conjugate acid-base pair in the reaction.\n"
        f"4. Write down the chemical formula of the conjugate base of ${rxn['acid_1']}$."
    )
    ans = (
        f"1. A conjugate acid-base pair consists of two substances that differ from each other by a single proton (H+); "
        f"2. Pair 1: {rxn['acid_1']} / {rxn['base_1']}; "
        f"3. Pair 2: {rxn['acid_2']} / {rxn['base_2']}; "
        f"4. Conjugate base: {rxn['base_1']}."
    )
    memo = (
        f"1. Conjugate acid-base pair definition [2]: Two compounds or ions that differ from each other by the presence or absence of a single proton ($\\text{{H}}^+$). [2]\n"
        f"2. Conjugate Pair 1 [2]: ${rxn['acid_1']}$ (acid) and ${rxn['base_1']}$ (conjugate base). [2]\n"
        f"3. Conjugate Pair 2 [2]: ${rxn['acid_2']}$ (conjugate acid) and ${rxn['base_2']}$ (base). [2]\n"
        f"4. Formula of conjugate base [1]: ${rxn['base_1']}$. [1]"
    )
    hints = {
        "tier_1": "Two species forming a conjugate pair differ by exactly one H+.",
        "tier_2": "Removing H+ from an acid gives its conjugate base; adding H+ to a base gives its conjugate acid.",
        "tier_3": f"For {rxn['acid_1']}, removing H+ leaves {rxn['base_1']}.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Conjugate acid-base pair definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Identification of conjugate pair 1", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Identification of conjugate pair 2", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Conjugate base formula", "marks": 1, "editable": True},
        ],
    }
    return _build_q("04_conjugate_acid_base_pairs", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 05: Monoprotic vs Polyprotic Acids Dissociation
# --------------------------------------------------------------------------- #
def builder_05_polyprotic_acids_dissociation(rng: random.Random) -> Dict[str, Any]:
    acids = [
        {
            "name": "sulphuric acid",
            "formula": "\\text{H}_2\\text{SO}_4",
            "protic": "diprotic",
            "step1": "\\text{H}_2\\text{SO}_4 + \\text{H}_2\\text{O} \\rightarrow \\text{HSO}_4^- + \\text{H}_3\\text{O}^+",
            "step2": "\\text{HSO}_4^- + \\text{H}_2\\text{O} \\rightleftharpoons \\text{SO}_4^{2-} + \\text{H}_3\\text{O}^+",
            "protons": 2,
        },
        {
            "name": "oxalic acid (ethanedioic acid)",
            "formula": "(\\text{COOH})_2",
            "protic": "diprotic",
            "step1": "(\\text{COOH})_2 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HOOC-COO}^- + \\text{H}_3\\text{O}^+",
            "step2": "\\text{HOOC-COO}^- + \\text{H}_2\\text{O} \\rightleftharpoons \\text{C}_2\\text{O}_4^{2-} + \\text{H}_3\\text{O}^+",
            "protons": 2,
        },
        {
            "name": "carbonic acid",
            "formula": "\\text{H}_2\\text{CO}_3",
            "protic": "diprotic",
            "step1": "\\text{H}_2\\text{CO}_3 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HCO}_3^- + \\text{H}_3\\text{O}^+",
            "step2": "\\text{HCO}_3^- + \\text{H}_2\\text{O} \\rightleftharpoons \\text{CO}_3^{2-} + \\text{H}_3\\text{O}^+",
            "protons": 2,
        },
    ]
    acid = rng.choice(acids)

    prompt = (
        f"Acids can be classified according to the number of ionisable protons they possess per molecule.\n\n"
        f"1. Define a *diprotic acid*.\n"
        f"2. Classify {acid['name']} (${acid['formula']}$) as monoprotic, diprotic, or triprotic.\n"
        f"3. Write down a balanced chemical equation for the first ionisation step of ${acid['formula']}$ in water.\n"
        f"4. Write down a balanced chemical equation for the second ionisation step in water."
    )
    ans = (
        f"1. A diprotic acid is an acid that can donate two protons (H+) per molecule in successive stages; "
        f"2. {acid['protic']}; "
        f"3. Step 1: {acid['step1']}; "
        f"4. Step 2: {acid['step2']}."
    )
    memo = (
        f"1. Diprotic acid definition [2]: An acid capable of donating two protons ($\\text{{H}}^+$) per molecule during ionisation. [2]\n"
        f"2. Classification [1]: ${acid['protic']}$. [1]\n"
        f"3. Step 1 ionisation [2]: $${acid['step1']}$$ [2]\n"
        f"4. Step 2 ionisation [2]: $${acid['step2']}$$ [2]"
    )
    hints = {
        "tier_1": "Look at the number of hydrogen atoms available to ionise in the formula.",
        "tier_2": "Each ionisation step transfers one proton (H+) to water to form H3O+.",
        "tier_3": f"{acid['formula']} donates its first proton to form the mono-anion, which then donates a second proton.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Diprotic acid definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Classification of acid", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "First ionisation step equation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Second ionisation step equation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("05_polyprotic_acids_dissociation", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 06: Acid + Metal Hydroxide Neutralisation
# --------------------------------------------------------------------------- #
def builder_06_acid_metal_hydroxide_neutralisation(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        {
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "base": "\\text{NaOH}",
            "base_name": "sodium hydroxide",
            "salt": "\\text{NaCl}",
            "salt_name": "sodium chloride",
            "eq": "\\text{HCl(aq)} + \\text{NaOH(aq)} \\rightarrow \\text{NaCl(aq)} + \\text{H}_2\\text{O(l)}",
            "net_ionic": "\\text{H}^+\\text{(aq)} + \\text{OH}^-\\text{(aq)} \\rightarrow \\text{H}_2\\text{O(l)}",
        },
        {
            "acid": "\\text{HNO}_3",
            "acid_name": "nitric acid",
            "base": "\\text{KOH}",
            "base_name": "potassium hydroxide",
            "salt": "\\text{KNO}_3",
            "salt_name": "potassium nitrate",
            "eq": "\\text{HNO}_3\\text{(aq)} + \\text{KOH(aq)} \\rightarrow \\text{KNO}_3\\text{(aq)} + \\text{H}_2\\text{O(l)}",
            "net_ionic": "\\text{H}^+\\text{(aq)} + \\text{OH}^-\\text{(aq)} \\rightarrow \\text{H}_2\\text{O(l)}",
        },
        {
            "acid": "\\text{H}_2\\text{SO}_4",
            "acid_name": "sulphuric acid",
            "base": "\\text{NaOH}",
            "base_name": "sodium hydroxide",
            "salt": "\\text{Na}_2\\text{SO}_4",
            "salt_name": "sodium sulphate",
            "eq": "\\text{H}_2\\text{SO}_4\\text{(aq)} + 2\\text{NaOH(aq)} \\rightarrow \\text{Na}_2\\text{SO}_4\\text{(aq)} + 2\\text{H}_2\\text{O(l)}",
            "net_ionic": "\\text{H}^+\\text{(aq)} + \\text{OH}^-\\text{(aq)} \\rightarrow \\text{H}_2\\text{O(l)}",
        },
        {
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "base": "\\text{Ba(OH)}_2",
            "base_name": "barium hydroxide",
            "salt": "\\text{BaCl}_2",
            "salt_name": "barium chloride",
            "eq": "2\\text{HCl(aq)} + \\text{Ba(OH)}_2\\text{(aq)} \\rightarrow \\text{BaCl}_2\\text{(aq)} + 2\\text{H}_2\\text{O(l)}",
            "net_ionic": "\\text{H}^+\\text{(aq)} + \\text{OH}^-\\text{(aq)} \\rightarrow \\text{H}_2\\text{O(l)}",
        },
    ]
    p = rng.choice(pairs)

    prompt = (
        f"A laboratory experiment involves the neutralisation reaction between {p['acid_name']} ({p['acid']}) and {p['base_name']} ({p['base']}).\n\n"
        f"1. Define a *neutralisation reaction*.\n"
        f"2. Write a balanced chemical equation for this reaction, including state symbols.\n"
        f"3. Write down the chemical name and formula of the salt formed.\n"
        f"4. Write down an overall balanced net ionic equation for the reaction."
    )
    ans = (
        f"1. A neutralisation reaction is a reaction between an acid and a base forming a salt and water; "
        f"2. {p['eq']}; "
        f"3. Salt: {p['salt_name']} ({p['salt']}); "
        f"4. Net ionic equation: {p['net_ionic']}."
    )
    memo = (
        f"1. Neutralisation definition [2]: A chemical reaction where an acid and a base react quantitatively with each other to produce a salt and water. [2]\n"
        f"2. Balanced chemical equation [3]: $${p['eq']}$$ (Reactants & products [1], balancing coefficients [1], state symbols [1])\n"
        f"3. Salt identification [2]: {p['salt_name']} [1], ${p['salt']}$ [1]\n"
        f"4. Net ionic equation [2]: $${p['net_ionic']}$$ [2]"
    )
    hints = {
        "tier_1": "Recall the general word equation: acid + metal hydroxide -> salt + water.",
        "tier_2": "The metal cation from the base combines with the non-metal anion from the acid.",
        "tier_3": f"The spectator ions cancel out, leaving H+ + OH- -> H2O as the net equation.",
    }
    schema = {
        "total_marks": 9,
        "marking_points": [
            {"id": "mp1", "desc": "Neutralisation definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Balanced equation with state symbols", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Salt name and formula", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Net ionic equation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("06_acid_metal_hydroxide_neutralisation", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 07: Acid + Metal Oxide Reactions
# --------------------------------------------------------------------------- #
def builder_07_acid_metal_oxide_reaction(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "oxide": "\\text{CuO}",
            "oxide_name": "copper(II) oxide",
            "acid": "\\text{H}_2\\text{SO}_4",
            "acid_name": "sulphuric acid",
            "salt": "\\text{CuSO}_4",
            "salt_name": "copper(II) sulphate",
            "color": "blue",
            "eq": "\\text{CuO(s)} + \\text{H}_2\\text{SO}_4\\text{(aq)} \\rightarrow \\text{CuSO}_4\\text{(aq)} + \\text{H}_2\\text{O(l)}",
        },
        {
            "oxide": "\\text{MgO}",
            "oxide_name": "magnesium oxide",
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "salt": "\\text{MgCl}_2",
            "salt_name": "magnesium chloride",
            "color": "colourless",
            "eq": "\\text{MgO(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{MgCl}_2\\text{(aq)} + \\text{H}_2\\text{O(l)}",
        },
        {
            "oxide": "\\text{Fe}_2\\text{O}_3",
            "oxide_name": "iron(III) oxide",
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "salt": "\\text{FeCl}_3",
            "salt_name": "iron(III) chloride",
            "color": "yellow-brown",
            "eq": "\\text{Fe}_2\\text{O}_3\\text{(s)} + 6\\text{HCl(aq)} \\rightarrow 2\\text{FeCl}_3\\text{(aq)} + 3\\text{H}_2\\text{O(l)}",
        },
    ]
    r = rng.choice(reactions)

    prompt = (
        f"Solid {r['oxide_name']} ({r['oxide']}) is added to a beaker containing warm dilute {r['acid_name']} ({r['acid']}).\n\n"
        f"1. State the general reaction scheme for an acid reacting with a metal oxide.\n"
        f"2. Write a balanced chemical equation for the reaction between {r['oxide']} and {r['acid']}.\n"
        f"3. State one macroscopic observation confirming that a reaction has occurred.\n"
        f"4. Classify the metal oxide as acidic, basic, or neutral based on its chemical behaviour."
    )
    ans = (
        f"1. Acid + metal oxide -> salt + water; "
        f"2. {r['eq']}; "
        f"3. The solid dissolves and the solution forms a characteristic {r['color']} colour; "
        f"4. Basic oxide (metal oxides act as basic anhydrides that neutralise acids)."
    )
    memo = (
        f"1. General scheme [1]: Acid + metal oxide $\\rightarrow$ salt + water. [1]\n"
        f"2. Balanced equation [3]: $${r['eq']}$$ [3]\n"
        f"3. Observation [1]: Solid dissolves / solution turns {r['color']} / temperature increases. [1]\n"
        f"4. Classification [1]: Basic oxide (acts as a Brønsted-Lowry base / proton acceptor). [1]"
    )
    hints = {
        "tier_1": "Metal oxides react with acids in a neutralisation reaction producing salt and water.",
        "tier_2": "Balance both the metal ions, oxygen, and hydrogen atoms carefully.",
        "tier_3": f"Solid {r['oxide']} dissolves in {r['acid']} to yield aqueous {r['salt']} and water.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "General word scheme", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Balanced chemical equation", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Macroscopic observation", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Classification as basic oxide", "marks": 1, "editable": True},
        ],
    }
    return _build_q("07_acid_metal_oxide_reaction", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 08: Acid + Metal Carbonate Reactions
# --------------------------------------------------------------------------- #
def builder_08_acid_metal_carbonate_reaction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {
            "carbonate": "\\text{CaCO}_3",
            "name": "calcium carbonate (marble chips)",
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "eq": "\\text{CaCO}_3\\text{(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{CaCl}_2\\text{(aq)} + \\text{H}_2\\text{O(l)} + \\text{CO}_2\\text{(g)}",
            "salt": "\\text{CaCl}_2",
            "gas": "\\text{CO}_2",
        },
        {
            "carbonate": "\\text{Na}_2\\text{CO}_3",
            "name": "sodium carbonate",
            "acid": "\\text{H}_2\\text{SO}_4",
            "acid_name": "sulphuric acid",
            "eq": "\\text{Na}_2\\text{CO}_3\\text{(s)} + \\text{H}_2\\text{SO}_4\\text{(aq)} \\rightarrow \\text{Na}_2\\text{SO}_4\\text{(aq)} + \\text{H}_2\\text{O(l)} + \\text{CO}_2\\text{(g)}",
            "salt": "\\text{Na}_2\\text{SO}_4",
            "gas": "\\text{CO}_2",
        },
        {
            "carbonate": "\\text{NaHCO}_3",
            "name": "sodium hydrogen carbonate",
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "eq": "\\text{NaHCO}_3\\text{(s)} + \\text{HCl(aq)} \\rightarrow \\text{NaCl(aq)} + \\text{H}_2\\text{O(l)} + \\text{CO}_2\\text{(g)}",
            "salt": "\\text{NaCl}",
            "gas": "\\text{CO}_2",
        },
    ]
    c = rng.choice(cases)

    prompt = (
        f"A learner adds dilute {c['acid_name']} ({c['acid']}) to a test tube containing solid {c['name']} ({c['carbonate']}). Effervescence is observed immediately.\n\n"
        f"1. State the general reaction scheme for an acid reacting with a metal carbonate.\n"
        f"2. Write a balanced chemical equation for the reaction, including state symbols.\n"
        f"3. Identify the gas evolved during the reaction.\n"
        f"4. Describe the standard qualitative chemical test used to confirm the identity of this gas, including the expected positive observation."
    )
    ans = (
        f"1. Acid + metal carbonate -> salt + water + carbon dioxide; "
        f"2. {c['eq']}; "
        f"3. Carbon dioxide (CO2); "
        f"4. Bubble the gas through clear limewater (aqueous calcium hydroxide). The limewater turns milky/cloudy due to the formation of insoluble calcium carbonate."
    )
    memo = (
        f"1. General scheme [1]: Acid + metal carbonate $\\rightarrow$ salt + water + carbon dioxide. [1]\n"
        f"2. Balanced chemical equation [3]: $${c['eq']}$$ [3]\n"
        f"3. Gas identity [1]: Carbon dioxide ($\\text{{CO}}_2$). [1]\n"
        f"4. Qualitative test [2]: Bubble the gas through clear limewater ($\\text{{Ca(OH)}}_2$) [1]; it turns cloudy/milky. [1]"
    )
    hints = {
        "tier_1": "Recall what products form when carbonates react with acids: a salt, water, and an odorless gas.",
        "tier_2": "The gas causes rapid bubbling (effervescence) and reacts with limewater.",
        "tier_3": f"Carbon dioxide gas turns clear limewater milky due to precipitate formation.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "General word scheme", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Balanced equation with state symbols", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Gas identity", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Limewater test and observation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("08_acid_metal_carbonate_reaction", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 09: Acid + Metal Displacement Reactions
# --------------------------------------------------------------------------- #
def builder_09_acid_metal_displacement_reaction(rng: random.Random) -> Dict[str, Any]:
    metals = [
        {
            "metal": "\\text{Mg}",
            "metal_name": "magnesium ribbon",
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "salt": "\\text{MgCl}_2",
            "eq": "\\text{Mg(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{MgCl}_2\\text{(aq)} + \\text{H}_2\\text{(g)}",
        },
        {
            "metal": "\\text{Zn}",
            "metal_name": "zinc granules",
            "acid": "\\text{H}_2\\text{SO}_4",
            "acid_name": "sulphuric acid",
            "salt": "\\text{ZnSO}_4",
            "eq": "\\text{Zn(s)} + \\text{H}_2\\text{SO}_4\\text{(aq)} \\rightarrow \\text{ZnSO}_4\\text{(aq)} + \\text{H}_2\\text{(g)}",
        },
        {
            "metal": "\\text{Fe}",
            "metal_name": "iron filings",
            "acid": "\\text{HCl}",
            "acid_name": "hydrochloric acid",
            "salt": "\\text{FeCl}_2",
            "eq": "\\text{Fe(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{FeCl}_2\\text{(aq)} + \\text{H}_2\\text{(g)}",
        },
    ]
    m = rng.choice(metals)

    prompt = (
        f"A piece of {m['metal_name']} ({m['metal']}) is dropped into a test tube containing dilute {m['acid_name']} ({m['acid']}). Gas bubbles rapidly form on the metal surface.\n\n"
        f"1. State the general reaction scheme for an acid reacting with a reactive metal.\n"
        f"2. Write a balanced chemical equation for the reaction, including state symbols.\n"
        f"3. Identify the gas produced in this reaction.\n"
        f"4. Describe the experimental test used to confirm the identity of this gas and the characteristic result."
    )
    ans = (
        f"1. Acid + reactive metal -> salt + hydrogen gas; "
        f"2. {m['eq']}; "
        f"3. Hydrogen gas (H2); "
        f"4. Bring a burning wooden splint to the mouth of the test tube. The gas ignites with a characteristic 'pop' sound."
    )
    memo = (
        f"1. General scheme [1]: Acid + reactive metal $\\rightarrow$ salt + hydrogen gas. [1]\n"
        f"2. Balanced chemical equation [3]: $${m['eq']}$$ [3]\n"
        f"3. Gas identity [1]: Hydrogen gas ($\\text{{H}}_2$). [1]\n"
        f"4. Pop test [2]: Insert a lighted splint [1]; hearing a sharp pop sound confirms hydrogen. [1]"
    )
    hints = {
        "tier_1": "Reactive metals displace hydrogen from acids.",
        "tier_2": "The gas released is flammable and ignites when a flame is introduced.",
        "tier_3": "Hydrogen gas makes a distinctive 'pop' sound with a burning splint.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "General word scheme", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Balanced equation with state symbols", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Gas identity", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Pop test description and result", "marks": 2, "editable": True},
        ],
    }
    return _build_q("09_acid_metal_displacement_reaction", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 10: Standard Solution Preparation
# --------------------------------------------------------------------------- #
def builder_10_standard_solution_preparation(rng: random.Random) -> Dict[str, Any]:
    solutes = [
        {
            "name": "oxalic acid dihydrate",
            "formula": "(\\text{COOH})_2 \\cdot 2\\text{H}_2\\text{O}",
            "molar_mass": 126.07,
            "m_str": "126{{,}}07",
        },
        {
            "name": "anhydrous sodium carbonate",
            "formula": "\\text{Na}_2\\text{CO}_3",
            "molar_mass": 105.99,
            "m_str": "105{{,}}99",
        },
        {
            "name": "sodium hydrogen carbonate",
            "formula": "\\text{NaHCO}_3",
            "molar_mass": 84.01,
            "m_str": "84{{,}}01",
        },
    ]
    sol = rng.choice(solutes)
    vol_cm3 = rng.choice([250.0, 500.0, 1000.0])
    conc = rng.choice([0.050, 0.100, 0.200, 0.250])
    vol_dm3 = vol_cm3 / 1000.0
    mass_g = conc * sol["molar_mass"] * vol_dm3

    prompt = (
        f"A chemistry educator instructs learners to prepare a primary standard solution of {sol['name']} ({sol['formula']}) "
        f"with a concentration of {fmt_sa(conc, 3)} mol·dm⁻³ in a volumetric flask of capacity {fmt_sa(vol_cm3, 0)} cm³.\n\n"
        f"1. Define a *standard solution*.\n"
        f"2. State two essential properties of a primary standard substance.\n"
        f"3. Calculate the exact mass of {sol['formula']} required to prepare this solution (Molar mass = {sol['m_str']} g·mol⁻¹).\n"
        f"4. Name the specific calibrated glassware item in which the final solution must be made up to the graduation mark."
    )
    ans = (
        f"1. A standard solution is a solution whose concentration is precisely and accurately known; "
        f"2. High purity (>99.9%), high stability (does not absorb moisture or react with air), and high molar mass; "
        f"3. m = c * M * V = {fmt_sa(conc, 3)} * {sol['m_str']} * {fmt_sa(vol_dm3, 3)} = {fmt_sa(mass_g, 2)} g; "
        f"4. Volumetric flask."
    )
    memo = (
        f"1. Standard solution definition [2]: A solution of precisely and accurately known concentration. [2]\n"
        f"2. Primary standard properties [2]: High purity / chemical stability / high molar mass / non-hygroscopic. [2]\n"
        f"3. Mass calculation [3]:\n"
        f"   $$V = \\frac{{{fmt_sa(vol_cm3, 0)}}}{{1000}} = {fmt_sa(vol_dm3, 3)}\\text{{ dm}}^3$$\n"
        f"   $$n = c \\cdot V = ({fmt_sa(conc, 3)})({fmt_sa(vol_dm3, 3)}) = {fmt_sa(conc * vol_dm3, 4)}\\text{{ mol}}$$ [1M]\n"
        f"   $$m = n \\cdot M = ({fmt_sa(conc * vol_dm3, 4)})({sol['m_str']}) = {fmt_sa(mass_g, 2)}\\text{{ g}}$$ [2A]\n"
        f"4. Glassware [1]: Volumetric flask. [1]"
    )
    hints = {
        "tier_1": "Convert cm³ to dm³ by dividing by 1000.",
        "tier_2": "Use the formula m = c * M * V.",
        "tier_3": f"m = ({fmt_sa(conc, 3)}) * ({sol['m_str']}) * ({fmt_sa(vol_dm3, 3)}) = {fmt_sa(mass_g, 2)} g.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Standard solution definition", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Properties of primary standard", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Mass calculation formula, substitution, answer", "marks": 3, "editable": True},
            {"id": "mp4", "desc": "Volumetric flask identification", "marks": 1, "editable": True},
        ],
    }
    return _build_q("10_standard_solution_preparation", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 11: Titration Apparatus & Technique (with Inline SVG Diagram)
# --------------------------------------------------------------------------- #
def _generate_titration_apparatus_svg(rng: random.Random, burette_val: float) -> str:
    seed_offset = rng.randint(0, 10)
    b_str = f"{burette_val:.1f}".replace(".", ",")
    return (
        f'<svg viewBox="0 0 450 360" width="100%" height="300" xmlns="http://www.w3.org/2000/svg" '
        f'style="background-color: #ffffff; font-family: sans-serif;">'
        f'<rect x="10" y="10" width="430" height="340" rx="8" fill="#fafafa" stroke="#e2e8f0" stroke-width="1.5"/>'
        f'<text x="225" y="32" font-size="14" font-weight="bold" text-anchor="middle" fill="#0f172a">Acid-Base Titration Apparatus Setup</text>'
        # Retort Stand
        f'<rect x="60" y="310" width="140" height="14" rx="2" fill="#475569"/>'
        f'<line x1="90" y1="310" x2="90" y2="45" stroke="#475569" stroke-width="6"/>'
        # Clamp
        f'<line x1="90" y1="130" x2="190" y2="130" stroke="#64748b" stroke-width="4"/>'
        f'<rect x="186" y="120" width="12" height="20" fill="#334155"/>'
        # Burette
        f'<rect x="188" y="55" width="14" height="175" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>'
        f'<polygon points="188,230 202,230 197,250 193,250" fill="#f8fafc" stroke="#1e293b" stroke-width="1.5"/>'
        # Stopcock
        f'<circle cx="195" cy="240" r="4" fill="#ef4444"/>'
        # Burette meniscus level
        f'<line x1="189" y1="95" x2="201" y2="95" stroke="#2563eb" stroke-width="2"/>'
        f'<text x="220" y="100" font-size="11" font-weight="bold" fill="#2563eb">Burette reading: {b_str} cm³</text>'
        # White tile beneath flask
        f'<rect x="155" y="300" width="80" height="8" rx="1" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>'
        f'<text x="250" y="308" font-size="10" fill="#64748b">White tile</text>'
        # Conical Flask
        f'<path d="M 188 258 L 202 258 L 202 268 L 222 298 L 168 298 L 188 268 Z" fill="#e0f2fe" stroke="#1e293b" stroke-width="1.5"/>'
        f'<text x="235" y="280" font-size="10" fill="#475569">Conical flask (analyte)</text>'
        # Labels A, B, C
        f'<circle cx="150" cy="90" r="12" fill="#3b82f6"/>'
        f'<text x="150" y="95" font-size="11" font-weight="bold" text-anchor="middle" fill="#ffffff">A</text>'
        f'<circle cx="140" cy="280" r="12" fill="#3b82f6"/>'
        f'<text x="140" y="285" font-size="11" font-weight="bold" text-anchor="middle" fill="#ffffff">B</text>'
        f'<circle cx="210" cy="325" r="12" fill="#3b82f6"/>'
        f'<text x="210" y="330" font-size="11" font-weight="bold" text-anchor="middle" fill="#ffffff">C</text>'
        f'</svg>'
    )


def builder_11_titration_apparatus_identification(rng: random.Random) -> Dict[str, Any]:
    b_val = rng.choice([21.4, 23.8, 24.5, 26.2, 28.0])
    svg = _generate_titration_apparatus_svg(rng, b_val)

    prompt = (
        f"Examine the titration apparatus setup shown in the diagram with labelled components A, B, and C.\n\n"
        f"1. Identify the piece of apparatus labelled A.\n"
        f"2. Identify the piece of apparatus labelled B.\n"
        f"3. Identify the item labelled C and explain its functional purpose during the titration.\n"
        f"4. State the standard laboratory liquid used to rinse apparatus A before filling it with standard acid.\n"
        f"5. Read and record the initial liquid volume shown in apparatus A ({fmt_sa(b_val, 1)} cm³)."
    )
    ans = (
        f"1. Apparatus A: Burette; "
        f"2. Apparatus B: Conical flask (Erlenmeyer flask); "
        f"3. Item C: White tile, used to provide a neutral white reflective background to clearly observe the sharp indicator endpoint colour transition; "
        f"4. First rinse with deionised/distilled water, then final rinse with the standard acid solution to be placed inside; "
        f"5. Reading = {fmt_sa(b_val, 1)} cm³."
    )
    memo = (
        f"1. Apparatus A [1]: Burette. [1]\n"
        f"2. Apparatus B [1]: Conical flask (Erlenmeyer flask). [1]\n"
        f"3. Item C & purpose [2]: White tile [1]; provides a neutral reflective background to detect the exact dropwise indicator colour change at equivalence. [1]\n"
        f"4. Rinsing protocol [2]: Rinse with deionised water [1], then rinse with the acid solution to prevent dilution. [1]\n"
        f"5. Scale reading [1]: {fmt_sa(b_val, 1)} cm³. [1]"
    )
    hints = {
        "tier_1": "Apparatus A is calibrated to deliver variable volumes dropwise.",
        "tier_2": "The white tile beneath the flask helps the human eye observe the indicator color change.",
        "tier_3": "A burette must be rinsed with the solution it will contain so its concentration is not altered.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Burette identification", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Conical flask identification", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "White tile identification and purpose", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Rinsing protocol for burette", "marks": 2, "editable": True},
        ],
    }
    diag_spec = {
        "kind": "inline_svg",
        "svg": svg,
        "diagram_role": "context",
        "diagram_type": "titration_apparatus",
        "burette_reading": b_val,
    }
    return _build_q("11_titration_apparatus_identification", prompt, ans, hints, schema, diag=diag_spec)


# --------------------------------------------------------------------------- #
# Subskill 12: Pipette and Burette Technique & Rinsing Protocols
# --------------------------------------------------------------------------- #
def builder_12_titration_pipette_burette_technique(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a quantitative titration analysis, high precision depends on the correct handling and rinsing of volumetric glassware.\n\n"
        f"1. Explain why a volumetric pipette must be rinsed with the specific alkaline solution it will transfer, rather than only deionised water.\n"
        f"2. Explain why the conical flask must NOT be rinsed with the base solution prior to titration, but only with deionised water.\n"
        f"3. Explain why the small residual droplet remaining in the tip of a calibrated volumetric pipette must NOT be blown out into the flask.\n"
        f"4. State the correct procedure for reading the liquid meniscus in a burette."
    )
    ans = (
        f"1. Rinsing with deionised water leaves residual water droplets that would dilute the base and change its concentration; "
        f"2. Residual base in the conical flask would introduce extra unmeasured moles of base, causing a systematic error; "
        f"3. Volumetric pipettes are calibrated to deliver (TD) a fixed volume taking into account capillary retention in the tip; "
        f"4. View at eye level perpendicular to the scale and read the lowest point of the concave liquid meniscus."
    )
    memo = (
        f"1. Pipette rinsing [2]: Residual water droplets would dilute the alkaline solution, altering the known concentration/moles transferred. [2]\n"
        f"2. Conical flask rinsing [2]: Rinsing with base leaves extra unknown moles of base, resulting in an erroneously high volume of acid needed. [2]\n"
        f"3. Pipette tip droplet [2]: Pipettes are calibrated to deliver (TD) the stated volume with the droplet retained by capillary action; blowing it out over-delivers. [2]\n"
        f"4. Meniscus reading [2]: Eye positioned perpendicular to prevent parallax error [1]; reading taken at bottom of concave meniscus [1]."
    )
    hints = {
        "tier_1": "Think about what residual liquid droplets do to the concentration or number of moles.",
        "tier_2": "The conical flask receives an exact measured mole quantity; any extra droplets distort the mole balance.",
        "tier_3": "Volumetric pipettes are calibrated 'to deliver' (TD), not 'to contain' (TC).",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Pipette rinsing explanation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Conical flask rinsing explanation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Pipette droplet calibrated retention", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Meniscus reading at eye level", "marks": 2, "editable": True},
        ],
    }
    return _build_q("12_titration_pipette_burette_technique", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 13: Indicator Selection: Strong Acid vs Strong Base
# --------------------------------------------------------------------------- #
def builder_13_indicator_selection_strong_acid_strong_base(rng: random.Random) -> Dict[str, Any]:
    acids = [("hydrochloric acid", "\\text{HCl}"), ("nitric acid", "\\text{HNO}_3")]
    bases = [("sodium hydroxide", "\\text{NaOH}"), ("potassium hydroxide", "\\text{KOH}")]
    a_name, a_form = rng.choice(acids)
    b_name, b_form = rng.choice(bases)

    prompt = (
        f"A learner titrates a standard solution of {a_name} ({a_form}) against {b_name} ({b_form}).\n\n"
        f"1. Classify both reactants as strong or weak electrolytes.\n"
        f"2. State the expected pH of the solution at the equivalence point at 25 °C.\n"
        f"3. State the most suitable indicator for this titration.\n"
        f"4. Describe the colour transition observed as the equivalence point is reached when acid is added from the burette to the base in the flask."
    )
    ans = (
        f"1. Both {a_form} and {b_form} are strong electrolytes (strong acid and strong base); "
        f"2. pH = 7 (neutral equivalence point); "
        f"3. Bromothymol blue; "
        f"4. The indicator changes from blue in alkaline solution to green at the exact neutral equivalence endpoint (and turns yellow if over-titrated)."
    )
    memo = (
        f"1. Electrolyte classification [2]: {a_name} is a strong acid [1]; {b_name} is a strong base [1].\n"
        f"2. Equivalence pH [1]: $\\text{{pH}} = 7$ (neutral). [1]\n"
        f"3. Indicator selection [1]: Bromothymol blue (pH transition range 6,0 - 7,6). [1]\n"
        f"4. Colour transition [2]: Blue (alkaline) $\\rightarrow$ Green (equivalence endpoint). [2]"
    )
    hints = {
        "tier_1": "Strong acid + strong base produces a neutral salt that does not undergo hydrolysis.",
        "tier_2": "At pH 7, bromothymol blue displays its transition color.",
        "tier_3": "Bromothymol blue transitions from blue to green at the endpoint.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Strong acid/base classification", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Equivalence pH statement", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Bromothymol blue indicator selection", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Colour change description", "marks": 2, "editable": True},
        ],
    }
    return _build_q("13_indicator_selection_strong_acid_strong_base", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 14: Indicator Selection: Strong Acid vs Weak Base
# --------------------------------------------------------------------------- #
def builder_14_indicator_selection_strong_acid_weak_base(rng: random.Random) -> Dict[str, Any]:
    acids = [("hydrochloric acid", "\\text{HCl}"), ("nitric acid", "\\text{HNO}_3")]
    bases = [("aqueous ammonia", "\\text{NH}_3\\text{(aq)}"), ("sodium carbonate", "\\text{Na}_2\\text{CO}_3")]
    a_name, a_form = rng.choice(acids)
    b_name, b_form = rng.choice(bases)

    prompt = (
        f"In a titration experiment, a standard {a_name} ({a_form}) solution is titrated against {b_name} ({b_form}).\n\n"
        f"1. State whether the pH at the equivalence point will be GREATER THAN 7, EQUAL TO 7, or LESS THAN 7.\n"
        f"2. Explain your answer to question 1 in terms of salt hydrolysis.\n"
        f"3. State the most appropriate indicator for this titration.\n"
        f"4. State the distinct colour transition of this indicator at the titration endpoint."
    )
    ans = (
        f"1. LESS THAN 7 (acidic);\n"
        f"2. The conjugate acid of the weak base hydrolyses in water producing H3O+ ions, making the equivalence solution acidic;\n"
        f"3. Methyl orange;\n"
        f"4. Yellow to orange (or red with slight excess acid)."
    )
    memo = (
        f"1. Equivalence pH [1]: LESS THAN 7. [1]\n"
        f"2. Salt hydrolysis explanation [2]: The conjugate acid formed from the weak base reacts with water: "
        f"$$\\text{{NH}}_4^+ + \\text{{H}}_2\\text{{O}} \\rightleftharpoons \\text{{NH}}_3 + \\text{{H}}_3\\text{{O}}^+$$ yielding hydronium ions. [2]\n"
        f"3. Indicator selection [1]: Methyl orange (pH transition range 3,1 - 4,4). [1]\n"
        f"4. Colour transition [2]: Yellow $\\rightarrow$ Orange at the endpoint. [2]"
    )
    hints = {
        "tier_1": "Strong acid + weak base yields an acidic salt solution.",
        "tier_2": "Select an indicator that transitions in the acidic pH range (below 7).",
        "tier_3": "Methyl orange operates between pH 3,1 and 4,4, turning orange at equivalence.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "pH statement less than 7", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Salt hydrolysis explanation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Methyl orange indicator selection", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Colour transition description", "marks": 2, "editable": True},
        ],
    }
    return _build_q("14_indicator_selection_strong_acid_weak_base", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 15: Indicator Selection: Weak Acid vs Strong Base
# --------------------------------------------------------------------------- #
def builder_15_indicator_selection_weak_acid_strong_base(rng: random.Random) -> Dict[str, Any]:
    acids = [
        ("ethanoic acid (acetic acid)", "\\text{CH}_3\\text{COOH}"),
        ("oxalic acid", "(\\text{COOH})_2"),
    ]
    bases = [("sodium hydroxide", "\\text{NaOH}"), ("potassium hydroxide", "\\text{KOH}")]
    a_name, a_form = rng.choice(acids)
    b_name, b_form = rng.choice(bases)

    prompt = (
        f"A titration is carried out between {a_name} ({a_form}) and a standard solution of {b_name} ({b_form}).\n\n"
        f"1. State whether the pH at the equivalence point is GREATER THAN 7, EQUAL TO 7, or LESS THAN 7.\n"
        f"2. Explain why the equivalence point has this pH in terms of salt hydrolysis.\n"
        f"3. State the most appropriate indicator for this titration.\n"
        f"4. State the colour change observed at the endpoint when base is titrated into the acid."
    )
    ans = (
        f"1. GREATER THAN 7 (basic/alkaline); "
        f"2. The conjugate base of the weak acid undergoes hydrolysis with water producing hydroxide ions (OH-); "
        f"3. Phenolphthalein; "
        f"4. Colourless to pale pink."
    )
    memo = (
        f"1. Equivalence pH [1]: GREATER THAN 7. [1]\n"
        f"2. Salt hydrolysis explanation [2]: The conjugate base anion hydrolyses in water: "
        f"$$\\text{{CH}}_3\\text{{COO}}^- + \\text{{H}}_2\\text{{O}} \\rightleftharpoons \\text{{CH}}_3\\text{{COOH}} + \\text{{OH}}^-$$ producing hydroxide ions. [2]\n"
        f"3. Indicator selection [1]: Phenolphthalein (pH transition range 8,3 - 10,0). [1]\n"
        f"4. Colour change [2]: Colourless $\\rightarrow$ Persistent pale pink. [2]"
    )
    hints = {
        "tier_1": "Weak acid + strong base produces a basic salt solution at equivalence.",
        "tier_2": "Select an indicator that transitions in the alkaline range (pH 8 to 10).",
        "tier_3": "Phenolphthalein transitions from colourless to pale pink at pH 8,3-10,0.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "pH statement greater than 7", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Salt hydrolysis explanation with OH- formation", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Phenolphthalein indicator selection", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Colour change colourless to pale pink", "marks": 2, "editable": True},
        ],
    }
    return _build_q("15_indicator_selection_weak_acid_strong_base", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 16: Volumetric Titration Calculation: Monoprotic 1:1
# --------------------------------------------------------------------------- #
def builder_16_titration_volumetric_calculation_monoprotic(rng: random.Random) -> Dict[str, Any]:
    vb_cm3 = rng.choice([20.0, 25.0])
    ca = rng.choice([0.100, 0.125, 0.150, 0.200])
    va_cm3 = rng.choice([18.5, 21.2, 23.6, 24.8, 26.5])
    # 1:1 stoichiometry: ca * va = cb * vb
    cb = (ca * va_cm3) / vb_cm3

    prompt = (
        f"In a volumetric titration experiment, a {fmt_sa(vb_cm3, 0)} cm³ sample of an unknown sodium hydroxide (NaOH) "
        f"solution is neutralised by exactly {fmt_sa(va_cm3, 1)} cm³ of a standard hydrochloric acid (HCl) "
        f"solution of concentration {fmt_sa(ca, 3)} mol·dm⁻³ according to the balanced equation:\n"
        f"$$\\text{{HCl(aq)}} + \\text{{NaOH(aq)}} \\rightarrow \\text{{NaCl(aq)}} + \\text{{H}}_2\\text{{O(l)}}$$\n\n"
        f"1. Calculate the number of moles of standard hydrochloric acid added.\n"
        f"2. Determine the number of moles of sodium hydroxide neutralised.\n"
        f"3. Calculate the concentration of the sodium hydroxide solution in mol·dm⁻³."
    )
    ans = (
        f"1. na = ca * Va = {fmt_sa(ca, 3)} * {fmt_sa(va_cm3 / 1000, 4)} = {fmt_sa(ca * va_cm3 / 1000, 4)} mol; "
        f"2. nb = na = {fmt_sa(ca * va_cm3 / 1000, 4)} mol (1:1 ratio); "
        f"3. cb = nb / Vb = {fmt_sa(cb, 3)} mol·dm⁻³."
    )
    memo = (
        f"1. Moles of acid [2]:\n"
        f"   $$n_a = c_a \\cdot V_a = ({fmt_sa(ca, 3)})({fmt_sa(va_cm3 / 1000, 4)}) = {fmt_sa(ca * va_cm3 / 1000, 4)}\\text{{ mol}}$$ [2]\n"
        f"2. Mole ratio [1]: From balanced equation, $n_b : n_a = 1 : 1$, so $n_b = {fmt_sa(ca * va_cm3 / 1000, 4)}\\text{{ mol}}$. [1]\n"
        f"3. Concentration of base [2]:\n"
        f"   $$c_b = \\frac{{n_b}}{{V_b}} = \\frac{{{fmt_sa(ca * va_cm3 / 1000, 4)}}}{{{fmt_sa(vb_cm3 / 1000, 4)}}} = {fmt_sa(cb, 3)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$ [2]"
    )
    hints = {
        "tier_1": "Use the formula n = c * V, converting cm³ to dm³.",
        "tier_2": "The stoichiometric mole ratio between HCl and NaOH is 1:1.",
        "tier_3": f"cb = (ca * Va) / Vb = ({fmt_sa(ca, 3)} * {fmt_sa(va_cm3, 1)}) / {fmt_sa(vb_cm3, 0)} = {fmt_sa(cb, 3)} mol·dm⁻³.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Moles of acid calculation", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Mole ratio application", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Concentration of base calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("16_titration_volumetric_calculation_monoprotic", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 17: Volumetric Titration Calculation: Diprotic Acid
# --------------------------------------------------------------------------- #
def builder_17_titration_volumetric_calculation_diprotic(rng: random.Random) -> Dict[str, Any]:
    acids = [
        ("sulphuric acid", "\\text{H}_2\\text{SO}_4", "\\text{Na}_2\\text{SO}_4"),
        ("ethanedioic acid", "(\\text{COOH})_2", "(\\text{COONa})_2"),
    ]
    a_name, a_form, salt_form = rng.choice(acids)
    vb_cm3 = rng.choice([20.0, 25.0])
    ca = rng.choice([0.080, 0.100, 0.120, 0.150])
    va_cm3 = rng.choice([16.4, 18.2, 22.5, 24.0])
    # na / nb = 1 / 2 => (ca * va) / (cb * vb) = 1 / 2 => cb = (2 * ca * va) / vb
    cb = (2.0 * ca * va_cm3) / vb_cm3

    prompt = (
        f"A learner titrates a {fmt_sa(vb_cm3, 0)} cm³ sample of sodium hydroxide (NaOH) solution against a standard "
        f"{a_name} ({a_form}) solution of concentration {fmt_sa(ca, 3)} mol·dm⁻³.\n"
        f"The balanced equation is:\n"
        f"$${a_form}\\text{{(aq)}} + 2\\text{{NaOH(aq)}} \\rightarrow {salt_form}\\text{{(aq)}} + 2\\text{{H}}_2\\text{{O(l)}}$$\n"
        f"An average titre volume of {fmt_sa(va_cm3, 1)} cm³ of {a_form} is required to reach the equivalence endpoint.\n\n"
        f"1. Write down the mole ratio of acid to base ($n_a : n_b$) from the balanced equation.\n"
        f"2. Calculate the concentration of the sodium hydroxide solution using $\\frac{{c_a V_a}}{{c_b V_b}} = \\frac{{n_a}}{{n_b}}$."
    )
    ans = (
        f"1. na : nb = 1 : 2; "
        f"2. cb = (ca * Va * nb) / (Vb * na) = ({fmt_sa(ca, 3)} * {fmt_sa(va_cm3, 1)} * 2) / ({fmt_sa(vb_cm3, 0)} * 1) = {fmt_sa(cb, 3)} mol·dm⁻³."
    )
    memo = (
        f"1. Mole ratio [1]: $n_a : n_b = 1 : 2$. [1]\n"
        f"2. Titration calculation [4]:\n"
        f"   $$\\frac{{c_a \\cdot V_a}}{{c_b \\cdot V_b}} = \\frac{{n_a}}{{n_b}}$$ [1M]\n"
        f"   $$\\frac{{({fmt_sa(ca, 3)})({fmt_sa(va_cm3, 1)})}}{{c_b ({fmt_sa(vb_cm3, 0)})}} = \\frac{{1}}{{2}}$$ [1M]\n"
        f"   $$c_b = \\frac{{({fmt_sa(ca, 3)})({fmt_sa(va_cm3, 1)}) \\times 2}}{{{fmt_sa(vb_cm3, 0)} \\times 1}} = {fmt_sa(cb, 3)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$ [2A]"
    )
    hints = {
        "tier_1": "Notice that 1 mole of diprotic acid reacts with 2 moles of base.",
        "tier_2": "Substitute into (ca * Va) / (cb * Vb) = 1 / 2.",
        "tier_3": f"cb = (2 * ca * Va) / Vb = {fmt_sa(cb, 3)} mol·dm⁻³.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Mole ratio from balanced equation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Titration formula and substitution", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Final concentration answer with units", "marks": 2, "editable": True},
        ],
    }
    return _build_q("17_titration_volumetric_calculation_diprotic", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 18: Volumetric Titration Calculation: Carbonate Base
# --------------------------------------------------------------------------- #
def builder_18_titration_volumetric_calculation_carbonate(rng: random.Random) -> Dict[str, Any]:
    vb_cm3 = rng.choice([25.0, 20.0])
    cb = rng.choice([0.050, 0.080, 0.100, 0.125])
    va_cm3 = rng.choice([19.2, 22.4, 25.6, 28.0])
    # 2 HCl + Na2CO3 -> 2 NaCl + H2O + CO2 => na / nb = 2 / 1
    # ca = (2 * cb * vb) / va
    ca = (2.0 * cb * vb_cm3) / va_cm3

    prompt = (
        f"A standard solution of sodium carbonate (Na₂CO₃) of concentration {fmt_sa(cb, 3)} mol·dm⁻³ is used to standardise "
        f"a hydrochloric acid (HCl) solution of unknown concentration.\n"
        f"The balanced equation for the reaction is:\n"
        f"$$2\\text{{HCl(aq)}} + \\text{{Na}}_2\\text{{CO}}_3\\text{{(aq)}} \\rightarrow 2\\text{{NaCl(aq)}} + \\text{{H}}_2\\text{{O(l)}} + \\text{{CO}}_2\\text{{(g)}}$$\n"
        f"Exactly {fmt_sa(vb_cm3, 0)} cm³ of the standard sodium carbonate solution requires {fmt_sa(va_cm3, 1)} cm³ of hydrochloric acid to reach the endpoint.\n\n"
        f"1. State the stoichiometric mole ratio of acid to base ($n_a : n_b$).\n"
        f"2. Calculate the concentration of the hydrochloric acid solution in mol·dm⁻³."
    )
    ans = (
        f"1. na : nb = 2 : 1; "
        f"2. ca = (2 * cb * Vb) / Va = (2 * {fmt_sa(cb, 3)} * {fmt_sa(vb_cm3, 0)}) / {fmt_sa(va_cm3, 1)} = {fmt_sa(ca, 3)} mol·dm⁻³."
    )
    memo = (
        f"1. Mole ratio [1]: $n_a : n_b = 2 : 1$. [1]\n"
        f"2. Titration calculation [4]:\n"
        f"   $$\\frac{{c_a \\cdot V_a}}{{c_b \\cdot V_b}} = \\frac{{n_a}}{{n_b}}$$ [1M]\n"
        f"   $$\\frac{{c_a ({fmt_sa(va_cm3, 1)})}}{{({fmt_sa(cb, 3)})({fmt_sa(vb_cm3, 0)})}} = \\frac{{2}}{{1}}$$ [1M]\n"
        f"   $$c_a = \\frac{{2 \\times ({fmt_sa(cb, 3)})({fmt_sa(vb_cm3, 0)})}}{{{fmt_sa(va_cm3, 1)}}} = {fmt_sa(ca, 3)}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}}$$ [2A]"
    )
    hints = {
        "tier_1": "Check the stoichiometric coefficients in 2HCl + Na2CO3.",
        "tier_2": "Here na = 2 and nb = 1. Substitute into (ca * Va) / (cb * Vb) = 2 / 1.",
        "tier_3": f"ca = (2 * cb * Vb) / Va = {fmt_sa(ca, 3)} mol·dm⁻³.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Mole ratio statement 2:1", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Formula and substitution", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Acid concentration calculation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("18_titration_volumetric_calculation_carbonate", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 19: Oxidation Numbers Rules in Neutral Compounds
# --------------------------------------------------------------------------- #
def builder_19_oxidation_number_rules(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        {
            "form": "\\text{KMnO}_4",
            "name": "potassium permanganate",
            "element": "manganese (Mn)",
            "calc": "(+1) + x + 4(-2) = 0 => x - 7 = 0 => x = +7",
            "ox": "+7",
        },
        {
            "form": "\\text{K}_2\\text{Cr}_2\\text{O}_7",
            "name": "potassium dichromate",
            "element": "chromium (Cr)",
            "calc": "2(+1) + 2x + 7(-2) = 0 => 2 + 2x - 14 = 0 => 2x = +12 => x = +6",
            "ox": "+6",
        },
        {
            "form": "\\text{H}_2\\text{SO}_4",
            "name": "sulphuric acid",
            "element": "sulphur (S)",
            "calc": "2(+1) + x + 4(-2) = 0 => 2 + x - 8 = 0 => x = +6",
            "ox": "+6",
        },
        {
            "form": "\\text{HNO}_3",
            "name": "nitric acid",
            "element": "nitrogen (N)",
            "calc": "(+1) + x + 3(-2) = 0 => 1 + x - 6 = 0 => x = +5",
            "ox": "+5",
        },
        {
            "form": "\\text{H}_2\\text{O}_2",
            "name": "hydrogen peroxide",
            "element": "oxygen (O)",
            "calc": "2(+1) + 2x = 0 => 2x = -2 => x = -1",
            "ox": "-1",
        },
    ]
    c = rng.choice(compounds)

    prompt = (
        f"Oxidation numbers represent the hypothetical charge an atom would have if all bonds were purely ionic.\n\n"
        f"1. State the rule for the sum of the oxidation numbers of all atoms in a neutral compound.\n"
        f"2. State the typical oxidation number assigned to oxygen in most compounds, and state one exception.\n"
        f"3. Determine the oxidation number of {c['element']} in {c['name']} (${c['form']}$), showing all calculation steps."
    )
    ans = (
        f"1. The sum of the oxidation numbers of all atoms in a neutral compound equals zero; "
        f"2. Oxygen is -2 in most compounds; exception: -1 in peroxides (e.g. H2O2) or +2 with fluorine (OF2); "
        f"3. {c['calc']}. The oxidation number of {c['element']} is {c['ox']}."
    )
    memo = (
        f"1. Neutral compound rule [1]: The algebraic sum of oxidation numbers is 0. [1]\n"
        f"2. Oxygen rule & exception [2]: Oxygen is -2 [1]; exception: -1 in peroxides like $\\text{{H}}_2\\text{{O}}_2$ [1].\n"
        f"3. Calculation [3]:\n"
        f"   $$\\text{{Equation: }} {c['calc']}$$ [2M]\n"
        f"   $$\\text{{Oxidation number}} = {c['ox']}$$ [1A]"
    )
    hints = {
        "tier_1": "Assign known values first: Group 1 metals are +1, hydrogen is +1, oxygen is usually -2.",
        "tier_2": "Set the sum of all oxidation numbers equal to zero.",
        "tier_3": f"For {c['form']}, solve for x: {c['calc']}.",
    }
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": "Sum rule for neutral compound", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Oxygen oxidation state and peroxide exception", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Stepwise oxidation number calculation and answer", "marks": 3, "editable": True},
        ],
    }
    return _build_q("19_oxidation_number_rules", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 20: Oxidation Numbers in Polyatomic Ions
# --------------------------------------------------------------------------- #
def builder_20_oxidation_number_polyatomic_ions(rng: random.Random) -> Dict[str, Any]:
    ions = [
        {
            "form": "\\text{SO}_4^{2-}",
            "name": "sulphate ion",
            "element": "sulphur (S)",
            "calc": "x + 4(-2) = -2 => x - 8 = -2 => x = +6",
            "ox": "+6",
        },
        {
            "form": "\\text{SO}_3^{2-}",
            "name": "sulphite ion",
            "element": "sulphur (S)",
            "calc": "x + 3(-2) = -2 => x - 6 = -2 => x = +4",
            "ox": "+4",
        },
        {
            "form": "\\text{NO}_3^-",
            "name": "nitrate ion",
            "element": "nitrogen (N)",
            "calc": "x + 3(-2) = -1 => x - 6 = -1 => x = +5",
            "ox": "+5",
        },
        {
            "form": "\\text{Cr}_2\\text{O}_7^{2-}",
            "name": "dichromate ion",
            "element": "chromium (Cr)",
            "calc": "2x + 7(-2) = -2 => 2x - 14 = -2 => 2x = +12 => x = +6",
            "ox": "+6",
        },
        {
            "form": "\\text{MnO}_4^-",
            "name": "permanganate ion",
            "element": "manganese (Mn)",
            "calc": "x + 4(-2) = -1 => x - 8 = -1 => x = +7",
            "ox": "+7",
        },
    ]
    ion = rng.choice(ions)

    prompt = (
        f"Consider the polyatomic ion {ion['name']} (${ion['form']}$).\n\n"
        f"1. State the rule for the sum of the oxidation numbers of the constituent atoms in a polyatomic ion.\n"
        f"2. Calculate the oxidation number of {ion['element']} in the ${ion['form']}$ ion, clearly showing your mathematical working.\n"
        f"3. State whether the sign (+ or -) is mandatory when reporting an oxidation number."
    )
    ans = (
        f"1. The sum of the oxidation numbers in a polyatomic ion equals the charge of the ion; "
        f"2. {ion['calc']}. The oxidation number of {ion['element']} is {ion['ox']}; "
        f"3. Yes, the sign is mandatory to distinguish oxidation state from valence/atomic number."
    )
    memo = (
        f"1. Polyatomic sum rule [1]: The sum of the oxidation numbers equals the net charge on the ion. [1]\n"
        f"2. Working and calculation [3]:\n"
        f"   $$\\text{{Equation: }} {ion['calc']}$$ [2M]\n"
        f"   $$\\text{{Oxidation number of {ion['element']}}} = {ion['ox']}$$ [1A]\n"
        f"3. Mandatory sign [1]: Yes, the '+' or '-' sign must be explicitly written. [1]"
    )
    hints = {
        "tier_1": "Set the sum of the oxidation numbers equal to the net charge of the ion, not zero.",
        "tier_2": "Each oxygen has an oxidation number of -2.",
        "tier_3": f"For {ion['form']}: {ion['calc']}.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Sum rule for polyatomic ion", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Working equation and algebra", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Correct oxidation number with sign", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Mandatory sign rule", "marks": 1, "editable": True},
        ],
    }
    return _build_q("20_oxidation_number_polyatomic_ions", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 21: Redox: Identifying Oxidising and Reducing Agents
# --------------------------------------------------------------------------- #
def builder_21_redox_identifying_oxidising_reducing_agents(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        {
            "eq": "\\text{Zn(s)} + \\text{Cu}^{2+}\\text{(aq)} \\rightarrow \\text{Zn}^{2+}\\text{(aq)} + \\text{Cu(s)}",
            "ox_species": "\\text{Zn}",
            "red_species": "\\text{Cu}^{2+}",
            "oa": "\\text{Cu}^{2+}",
            "ra": "\\text{Zn}",
            "oa_reason": "gains electrons (oxidation number decreases from +2 to 0)",
            "ra_reason": "loses electrons (oxidation number increases from 0 to +2)",
        },
        {
            "eq": "\\text{Mg(s)} + 2\\text{H}^+\\text{(aq)} \\rightarrow \\text{Mg}^{2+}\\text{(aq)} + \\text{H}_2\\text{(g)}",
            "ox_species": "\\text{Mg}",
            "red_species": "\\text{H}^+",
            "oa": "\\text{H}^+",
            "ra": "\\text{Mg}",
            "oa_reason": "gains electrons (oxidation number decreases from +1 to 0)",
            "ra_reason": "loses electrons (oxidation number increases from 0 to +2)",
        },
        {
            "eq": "\\text{Cl}_2\\text{(g)} + 2\\text{Br}^-\\text{(aq)} \\rightarrow 2\\text{Cl}^-\\text{(aq)} + \\text{Br}_2\\text{(aq)}",
            "ox_species": "\\text{Br}^-",
            "red_species": "\\text{Cl}_2",
            "oa": "\\text{Cl}_2",
            "ra": "\\text{Br}^-",
            "oa_reason": "gains electrons (oxidation number decreases from 0 to -1)",
            "ra_reason": "loses electrons (oxidation number increases from -1 to 0)",
        },
    ]
    r = rng.choice(reactions)

    prompt = (
        f"Consider the redox reaction represented by the equation:\n"
        f"$${r['eq']}$$\n\n"
        f"1. Define *oxidation* in terms of electron transfer.\n"
        f"2. Define a *reducing agent* in terms of oxidation numbers.\n"
        f"3. Identify the species that is oxidised and the species that is reduced.\n"
        f"4. Identify the oxidising agent and the reducing agent, justifying each in terms of electron transfer."
    )
    ans = (
        f"1. Oxidation is the loss of electrons; "
        f"2. A reducing agent is a substance that undergoes an increase in oxidation number (by donating electrons); "
        f"3. Oxidised: {r['ox_species']}; Reduced: {r['red_species']}; "
        f"4. Oxidising agent: {r['oa']} (it {r['oa_reason']}); Reducing agent: {r['ra']} (it {r['ra_reason']})."
    )
    memo = (
        f"1. Oxidation definition [2]: The loss of electrons. [2]\n"
        f"2. Reducing agent definition [2]: A substance that loses electrons / whose oxidation number increases. [2]\n"
        f"3. Species oxidised & reduced [2]: Oxidised: ${r['ox_species']}$ [1]; Reduced: ${r['red_species']}$ [1].\n"
        f"4. Agents and justification [4]:\n"
        f"   - Oxidising agent: ${r['oa']}$ [1], because it {r['oa_reason']} [1].\n"
        f"   - Reducing agent: ${r['ra']}$ [1], because it {r['ra_reason']} [1]."
    )
    hints = {
        "tier_1": "Remember OIL RIG: Oxidation Is Loss, Reduction Is Gain of electrons.",
        "tier_2": "The substance that is oxidised acts as the reducing agent; the substance that is reduced acts as the oxidising agent.",
        "tier_3": f"{r['ox_species']} loses electrons to become {r['ra']}, while {r['red_species']} gains electrons.",
    }
    schema = {
        "total_marks": 10,
        "marking_points": [
            {"id": "mp1", "desc": "Oxidation definition in terms of electrons", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Reducing agent definition", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Identification of oxidised and reduced species", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Oxidising agent and justification", "marks": 2, "editable": True},
            {"id": "mp5", "desc": "Reducing agent and justification", "marks": 2, "editable": True},
        ],
    }
    return _build_q("21_redox_identifying_oxidising_reducing_agents", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 22: Redox: Writing Oxidation and Reduction Half-Reactions
# --------------------------------------------------------------------------- #
def builder_22_redox_half_reactions_electron_transfer(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        {
            "full": "\\text{Fe(s)} + \\text{Cu}^{2+}\\text{(aq)} \\rightarrow \\text{Fe}^{2+}\\text{(aq)} + \\text{Cu(s)}",
            "ox_half": "\\text{Fe} \\rightarrow \\text{Fe}^{2+} + 2e^-",
            "red_half": "\\text{Cu}^{2+} + 2e^- \\rightarrow \\text{Cu}",
            "e_transferred": 2,
        },
        {
            "full": "2\\text{Al(s)} + 3\\text{Zn}^{2+}\\text{(aq)} \\rightarrow 2\\text{Al}^{3+}\\text{(aq)} + 3\\text{Zn(s)}",
            "ox_half": "\\text{Al} \\rightarrow \\text{Al}^{3+} + 3e^-",
            "red_half": "\\text{Zn}^{2+} + 2e^- \\rightarrow \\text{Zn}",
            "e_transferred": 6,
        },
        {
            "full": "\\text{Mg(s)} + \\text{Pb}^{2+}\\text{(aq)} \\rightarrow \\text{Mg}^{2+}\\text{(aq)} + \\text{Pb(s)}",
            "ox_half": "\\text{Mg} \\rightarrow \\text{Mg}^{2+} + 2e^-",
            "red_half": "\\text{Pb}^{2+} + 2e^- \\rightarrow \\text{Pb}",
            "e_transferred": 2,
        },
    ]
    p = rng.choice(pairs)

    prompt = (
        f"Consider the overall chemical redox reaction:\n"
        f"$${p['full']}$$\n\n"
        f"1. Write down the oxidation half-reaction.\n"
        f"2. Write down the reduction half-reaction.\n"
        f"3. State the total number of electrons transferred in the balanced overall reaction equation."
    )
    ans = (
        f"1. Oxidation half-reaction: {p['ox_half']}; "
        f"2. Reduction half-reaction: {p['red_half']}; "
        f"3. Total electrons transferred: {p['e_transferred']} electrons."
    )
    memo = (
        f"1. Oxidation half-reaction [2]: $${p['ox_half']}$$ [2]\n"
        f"2. Reduction half-reaction [2]: $${p['red_half']}$$ [2]\n"
        f"3. Electrons transferred [1]: {p['e_transferred']} electrons. [1]"
    )
    hints = {
        "tier_1": "In oxidation, electrons are on the right-hand product side; in reduction, electrons are on the left-hand reactant side.",
        "tier_2": "Equalize the number of electrons lost and gained.",
        "tier_3": f"The lowest common multiple of electrons transferred is {p['e_transferred']}.",
    }
    schema = {
        "total_marks": 5,
        "marking_points": [
            {"id": "mp1", "desc": "Oxidation half-reaction", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Reduction half-reaction", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Total electrons transferred", "marks": 1, "editable": True},
        ],
    }
    return _build_q("22_redox_half_reactions_electron_transfer", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 23: Balancing Redox Reactions in Acidic Conditions
# --------------------------------------------------------------------------- #
def builder_23_redox_balancing_acidic_medium(rng: random.Random) -> Dict[str, Any]:
    cases = [
        {
            "reactants": "\\text{MnO}_4^- + \\text{Fe}^{2+}",
            "products": "\\text{Mn}^{2+} + \\text{Fe}^{3+}",
            "ox_half": "\\text{Fe}^{2+} \\rightarrow \\text{Fe}^{3+} + e^-",
            "red_half": "\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\rightarrow \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}",
            "balanced": "\\text{MnO}_4^- + 5\\text{Fe}^{2+} + 8\\text{H}^+ \\rightarrow \\text{Mn}^{2+} + 5\\text{Fe}^{3+} + 4\\text{H}_2\\text{O}",
        },
        {
            "reactants": "\\text{Cr}_2\\text{O}_7^{2-} + \\text{Fe}^{2+}",
            "products": "2\\text{Cr}^{3+} + \\text{Fe}^{3+}",
            "ox_half": "\\text{Fe}^{2+} \\rightarrow \\text{Fe}^{3+} + e^-",
            "red_half": "\\text{Cr}_2\\text{O}_7^{2-} + 14\\text{H}^+ + 6e^- \\rightarrow 2\\text{Cr}^{3+} + 7\\text{H}_2\\text{O}",
            "balanced": "\\text{Cr}_2\\text{O}_7^{2-} + 6\\text{Fe}^{2+} + 14\\text{H}^+ \\rightarrow 2\\text{Cr}^{3+} + 6\\text{Fe}^{3+} + 7\\text{H}_2\\text{O}",
        },
    ]
    c = rng.choice(cases)

    prompt = (
        f"A laboratory experiment studies the oxidation of iron(II) ions by an acidified oxyanion according to the unbalanced skeleton equation:\n"
        f"$${c['reactants']} \\rightarrow {c['products']}\\text{{ (in acidic solution)}}$$\n\n"
        f"1. Write down the balanced oxidation half-reaction.\n"
        f"2. Write down the balanced reduction half-reaction in acidic medium.\n"
        f"3. Combine both half-reactions to produce the overall balanced ionic equation."
    )
    ans = (
        f"1. Oxidation half-reaction: {c['ox_half']}; "
        f"2. Reduction half-reaction: {c['red_half']}; "
        f"3. Overall balanced equation: {c['balanced']}."
    )
    memo = (
        f"1. Oxidation half-reaction [2]: $${c['ox_half']}$$ [2]\n"
        f"2. Reduction half-reaction [3]: $${c['red_half']}$$ [3]\n"
        f"3. Overall equation [3]: $${c['balanced']}$$ [3]"
    )
    hints = {
        "tier_1": "Balance oxygen atoms using H2O and hydrogen atoms using H+.",
        "tier_2": "Balance electrical charges by adding electrons.",
        "tier_3": f"Multiply the oxidation half-reaction so electron counts cancel out: {c['balanced']}.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Oxidation half-reaction", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Reduction half-reaction with H+ and H2O", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Overall balanced equation", "marks": 3, "editable": True},
        ],
    }
    return _build_q("23_redox_balancing_acidic_medium", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 24: Redox: Metal and Halogen Displacement & Spectator Ions
# --------------------------------------------------------------------------- #
def builder_24_redox_displacement_spectator_ions(rng: random.Random) -> Dict[str, Any]:
    systems = [
        {
            "metal": "\\text{Zn}",
            "solution": "copper(II) sulphate (CuSO4)",
            "sol_form": "\\text{CuSO}_4",
            "obs": "Zinc acquires a reddish-brown copper deposit; the blue solution fades to colourless.",
            "full_eq": "\\text{Zn(s)} + \\text{CuSO}_4\\text{(aq)} \\rightarrow \\text{ZnSO}_4\\text{(aq)} + \\text{Cu(s)}",
            "net_eq": "\\text{Zn(s)} + \\text{Cu}^{2+}\\text{(aq)} \\rightarrow \\text{Zn}^{2+}\\text{(aq)} + \\text{Cu(s)}",
            "spectator": "\\text{SO}_4^{2-}",
        },
        {
            "metal": "\\text{Cu}",
            "solution": "silver nitrate (AgNO3)",
            "sol_form": "\\text{AgNO}_3",
            "obs": "Copper turns grey with shiny silver needles; solution gradually turns pale blue.",
            "full_eq": "\\text{Cu(s)} + 2\\text{AgNO}_3\\text{(aq)} \\rightarrow \\text{Cu(NO}_3)_2\\text{(aq)} + 2\\text{Ag(s)}",
            "net_eq": "\\text{Cu(s)} + 2\\text{Ag}^+\\text{(aq)} \\rightarrow \\text{Cu}^{2+}\\text{(aq)} + 2\\text{Ag(s)}",
            "spectator": "\\text{NO}_3^-",
        },
    ]
    s = rng.choice(systems)

    prompt = (
        f"A strip of clean {s['metal']} is immersed into an aqueous solution of {s['solution']}.\n\n"
        f"1. State one visible macroscopic observation that confirms a chemical reaction has taken place.\n"
        f"2. Write a balanced molecular equation for the displacement reaction.\n"
        f"3. Identify the spectator ion(s) in this reaction.\n"
        f"4. Write down an overall balanced net ionic equation for the reaction."
    )
    ans = (
        f"1. Observation: {s['obs']}; "
        f"2. Full equation: {s['full_eq']}; "
        f"3. Spectator ion: {s['spectator']}; "
        f"4. Net ionic equation: {s['net_eq']}."
    )
    memo = (
        f"1. Observation [1]: {s['obs']} [1]\n"
        f"2. Molecular equation [3]: $${s['full_eq']}$$ [3]\n"
        f"3. Spectator ion [1]: ${s['spectator']}$. [1]\n"
        f"4. Net ionic equation [2]: $${s['net_eq']}$$ [2]"
    )
    hints = {
        "tier_1": "Spectator ions do not change oxidation state and remain unchanged in solution.",
        "tier_2": "Cancel out the identical aqueous ions from both sides of the ionic equation.",
        "tier_3": f"The spectator ion is {s['spectator']}.",
    }
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Macroscopic observation", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Full molecular equation", "marks": 3, "editable": True},
            {"id": "mp3", "desc": "Spectator ion identification", "marks": 1, "editable": True},
            {"id": "mp4", "desc": "Net ionic equation", "marks": 2, "editable": True},
        ],
    }
    return _build_q("24_redox_displacement_spectator_ions", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Subskill 25: Types of Reaction Synthesis & Autopsy
# --------------------------------------------------------------------------- #
def builder_25_types_of_reaction_synthesis_autopsy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner analyses two unknown clear solutions, Solution X and Solution Y. Solution X has a pH of 2,4, while Solution Y has a pH of 11,8.\n\n"
        f"1. Classify Solution X and Solution Y as acidic or alkaline.\n"
        f"2. Solution X is added to solid sodium carbonate. State the gas produced and the chemical formula of the salt formed if Solution X is dilute nitric acid.\n"
        f"3. A copper wire is placed in Solution X (nitric acid), producing brown nitrogen dioxide gas (NO2). State whether this is an acid-base neutralisation reaction or a redox reaction, and justify your answer.\n"
        f"4. In an exam diagnostic triage, a learner claims that all neutralisation reactions produce an exact neutral solution of pH 7 at equivalence. Explain why this claim is a scientific misconception."
    )
    ans = (
        f"1. Solution X is acidic (pH < 7); Solution Y is alkaline/basic (pH > 7); "
        f"2. Gas: Carbon dioxide (CO2); Salt: Sodium nitrate (NaNO3); "
        f"3. Redox reaction: Copper undergoes an increase in oxidation number from 0 to +2 (oxidation), while nitrogen decreases from +5 to +4 (reduction); "
        f"4. The claim is false because salt hydrolysis occurs when a weak acid reacts with a strong base (pH > 7) or a strong acid reacts with a weak base (pH < 7)."
    )
    memo = (
        f"1. Classification [2]: Solution X is acidic [1]; Solution Y is alkaline/basic [1].\n"
        f"2. Carbonate reaction [2]: Gas is $\\text{{CO}}_2$ [1]; Salt is $\\text{{NaNO}}_3$ [1].\n"
        f"3. Redox justification [2]: Redox reaction [1]; oxidation states change (Cu from 0 to +2; N from +5 to +4 in $\\text{{NO}}_2$) [1].\n"
        f"4. Misconception analysis [2]: False; salt hydrolysis alters the equivalence pH away from 7 unless both acid and base are strong electrolytes. [2]"
    )
    hints = {
        "tier_1": "Recall the pH scale where 7 is neutral.",
        "tier_2": "Check if oxidation states change: acid-base reactions involve proton transfer without changing oxidation states, while redox reactions involve electron transfer.",
        "tier_3": "Salt hydrolysis explains why weak acid / strong base equivalence is alkaline, and strong acid / weak base is acidic.",
    }
    schema = {
        "total_marks": 8,
        "marking_points": [
            {"id": "mp1", "desc": "Solution acidity classification", "marks": 2, "editable": True},
            {"id": "mp2", "desc": "Gas and salt identification", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Redox classification and oxidation number justification", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Autopsy refutation of pH 7 equivalence misconception", "marks": 2, "editable": True},
        ],
    }
    return _build_q("25_types_of_reaction_synthesis_autopsy", prompt, ans, hints, schema, diag=None)


# --------------------------------------------------------------------------- #
# Export Map
# --------------------------------------------------------------------------- #
BUILDERS_01_25 = {
    "01_arrhenius_acid_base_definitions": builder_01_arrhenius_acid_base_definitions,
    "02_bronsted_lowry_proton_transfer": builder_02_bronsted_lowry_proton_transfer,
    "03_amphiprotic_amphoteric_substances": builder_03_amphiprotic_amphoteric_substances,
    "04_conjugate_acid_base_pairs": builder_04_conjugate_acid_base_pairs,
    "05_polyprotic_acids_dissociation": builder_05_polyprotic_acids_dissociation,
    "06_acid_metal_hydroxide_neutralisation": builder_06_acid_metal_hydroxide_neutralisation,
    "07_acid_metal_oxide_reaction": builder_07_acid_metal_oxide_reaction,
    "08_acid_metal_carbonate_reaction": builder_08_acid_metal_carbonate_reaction,
    "09_acid_metal_displacement_reaction": builder_09_acid_metal_displacement_reaction,
    "10_standard_solution_preparation": builder_10_standard_solution_preparation,
    "11_titration_apparatus_identification": builder_11_titration_apparatus_identification,
    "12_titration_pipette_burette_technique": builder_12_titration_pipette_burette_technique,
    "13_indicator_selection_strong_acid_strong_base": builder_13_indicator_selection_strong_acid_strong_base,
    "14_indicator_selection_strong_acid_weak_base": builder_14_indicator_selection_strong_acid_weak_base,
    "15_indicator_selection_weak_acid_strong_base": builder_15_indicator_selection_weak_acid_strong_base,
    "16_titration_volumetric_calculation_monoprotic": builder_16_titration_volumetric_calculation_monoprotic,
    "17_titration_volumetric_calculation_diprotic": builder_17_titration_volumetric_calculation_diprotic,
    "18_titration_volumetric_calculation_carbonate": builder_18_titration_volumetric_calculation_carbonate,
    "19_oxidation_number_rules": builder_19_oxidation_number_rules,
    "20_oxidation_number_polyatomic_ions": builder_20_oxidation_number_polyatomic_ions,
    "21_redox_identifying_oxidising_reducing_agents": builder_21_redox_identifying_oxidising_reducing_agents,
    "22_redox_half_reactions_electron_transfer": builder_22_redox_half_reactions_electron_transfer,
    "23_redox_balancing_acidic_medium": builder_23_redox_balancing_acidic_medium,
    "24_redox_displacement_spectator_ions": builder_24_redox_displacement_spectator_ions,
    "25_types_of_reaction_synthesis_autopsy": builder_25_types_of_reaction_synthesis_autopsy,
}
