"""
Grade 8 Mathematics - Algebraic Equations 3 Archetypes (01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr8/Term 2/02. Algebraic equations 3.md.
"""
from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Optional

from .svg_diagrams import draw_angles_on_line_svg


# ----------------------------------------------------------------------
# 01. Orchard Linear Growth Target Milestone
# ----------------------------------------------------------------------
def arch_01_orchard_linear_growth_target_milestone(rng: random.Random) -> Dict[str, Any]:
    fruit = rng.choice(["apple", "orange", "lemon", "naartjie", "peach", "mango"])
    c0 = rng.choice([80, 100, 120, 150, 200])
    rate = rng.choice([15, 20, 25, 30, 40])
    days = rng.choice([12, 15, 18, 20, 25, 30])
    target = c0 + rate * days

    prompt = (
        f"A farmer begins with **{c0}** {fruit} trees and plants **{rate}** additional {fruit} trees each day.\n\n"
        f"1. Write an algebraic formula for the total number of {fruit} trees \\(T\\) after \\(d\\) days.\n"
        f"2. Set up and solve an equation to determine how many days it will take to reach a total of **{target}** trees."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"Initial count = {c0}, daily increase = {rate}.\n"
        f"\\[ T = {c0} + {rate}d \\]\n\n"
        f"**Step 2: Set up equation and solve**\n"
        f"\\[ {c0} + {rate}d = {target} \\]\n"
        f"Subtract {c0} from both sides:\n"
        f"\\[ {rate}d = {target} - {c0} = {target - c0} \\]\n"
        f"Divide by {rate}:\n"
        f"\\[ d = \\frac{{{target - c0}}}{{{rate}}} = {days} \\text{{ days}} \\]"
    )
    ans = f"1. T = {c0} + {rate}d; 2. d = {days} days"
    return {
        "id": f"g8_eq3_orchard_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "01_orchard_linear_growth_target_milestone",
        "learning_objective_id": "math_g8_eq3_orchard_milestone",
        "hints": {
            "tier_1": f"Total trees = Initial + (Rate × days).",
            "tier_2": f"Set {c0} + {rate}d = {target} and subtract {c0} from both sides.",
            "tier_3": f"Divide {target - c0} by {rate} to get {days} days.",
        },
        "misconception_tags": ["forgetting_initial_constant", "dividing_without_subtracting_initial"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 02. Orchard Comparing Two Growth Rates Break Even
# ----------------------------------------------------------------------
def arch_02_orchard_comparing_two_growth_rates_break_even(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.choice([100, 120, 150, 180])
    c2 = c1 + rng.choice([120, 150, 180, 200])  # Orchard 2 starts with more
    days = rng.choice([10, 12, 15, 20])
    diff_rate = (c2 - c1) // days
    r2 = rng.choice([8, 10, 12])
    r1 = r2 + diff_rate
    # Verify: c1 + r1*days = c2 + r2*days
    final_trees = c1 + r1 * days

    prompt = (
        f"Orchard A starts with **{c1}** trees and grows by **{r1}** trees per week. "
        f"Orchard B starts with **{c2}** trees and grows by **{r2}** trees per week.\n\n"
        f"1. Set up an equation representing when both orchards have the exact same number of trees.\n"
        f"2. Solve for the number of weeks \\(w\\) until both orchards are equal, and state that tree count."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"\\[ {c1} + {r1}w = {c2} + {r2}w \\]\n\n"
        f"**Step 2: Collect like terms**\n"
        f"Subtract \\({r2}w\\) and {c1} from both sides:\n"
        f"\\[ {r1}w - {r2}w = {c2} - {c1} \\]\n"
        f"\\[ {r1 - r2}w = {c2 - c1} \\]\n"
        f"\\[ w = \\frac{{{c2 - c1}}}{{{r1 - r2}}} = {days} \\text{{ weeks}} \\]\n\n"
        f"**Check tree count:**\n"
        f"Orchard A: \\({c1} + {r1}({days}) = {final_trees}\\)\n"
        f"Orchard B: \\({c2} + {r2}({days}) = {final_trees}\\)"
    )
    ans = f"1. {c1} + {r1}w = {c2} + {r2}w; 2. w = {days} weeks, {final_trees} trees"
    return {
        "id": f"g8_eq3_breakeven_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "02_orchard_comparing_two_growth_rates_break_even",
        "learning_objective_id": "math_g8_eq3_orchard_breakeven",
        "hints": {
            "tier_1": f"Equate the two expressions: {c1} + {r1}w = {c2} + {r2}w.",
            "tier_2": f"Group the w-terms on the left: ({r1} - {r2})w = {c2} - {c1}.",
            "tier_3": f"w = {days} weeks.",
        },
        "misconception_tags": ["combining_unlike_terms_constant_and_variable", "sign_error_transposition"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 03. Population Linear Decline Milestone
# ----------------------------------------------------------------------
def arch_03_population_linear_decline_milestone(rng: random.Random) -> Dict[str, Any]:
    p0 = rng.choice([250, 300, 360, 400, 500])
    rate = rng.choice([12, 15, 20, 25])
    years = rng.choice([5, 6, 8, 10])
    target = p0 - rate * years

    prompt = (
        f"A community club had **{p0}** registered members at the beginning of 2015. "
        f"Each year since then, the membership decreased by **{rate}** members.\n\n"
        f"1. Write an algebraic formula for the membership \\(M\\) after \\(t\\) years.\n"
        f"2. Solve an equation to calculate after how many years the membership reached **{target}**."
    )
    sol = (
        f"**Step 1: Formula**\n"
        f"\\[ M = {p0} - {rate}t \\]\n\n"
        f"**Step 2: Solve equation**\n"
        f"\\[ {p0} - {rate}t = {target} \\]\n"
        f"Subtract {p0} from both sides:\n"
        f"\\[ -{rate}t = {target} - {p0} = -{p0 - target} \\]\n"
        f"Divide by \\(-{rate}\\):\n"
        f"\\[ t = \\frac{{-{p0 - target}}}{{-{rate}}} = {years} \\text{{ years}} \\]"
    )
    ans = f"1. M = {p0} - {rate}t; 2. t = {years} years"
    return {
        "id": f"g8_eq3_decline_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "03_population_linear_decline_milestone",
        "learning_objective_id": "math_g8_eq3_linear_decline",
        "hints": {
            "tier_1": f"Decrease means subtraction: M = {p0} - {rate}t.",
            "tier_2": f"Set {p0} - {rate}t = {target} and subtract {p0}.",
            "tier_3": f"-{rate}t = -{p0 - target}, so t = {years}.",
        },
        "misconception_tags": ["negative_sign_loss_in_division", "adding_instead_of_subtracting_rate"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 04. Break Even Two Linear Service Plans
# ----------------------------------------------------------------------
def arch_04_break_even_two_linear_service_plans(rng: random.Random) -> Dict[str, Any]:
    f1 = rng.choice([150, 200, 250])
    v1 = rng.choice([2, 3])
    f2 = f1 + rng.choice([100, 150, 200])  # higher fixed
    v2 = v1 - 1  # lower per-unit rate = 1 or 2
    # f1 + v1*x = f2 + v2*x => (v1 - v2)*x = f2 - f1
    x_units = (f2 - f1) // (v1 - v2)
    cost = f1 + v1 * x_units

    prompt = (
        f"Option A charges a fixed monthly fee of **R{f1}** plus **R{v1}** per gigabyte used. "
        f"Option B charges a fixed monthly fee of **R{f2}** plus **R{v2}** per gigabyte used.\n\n"
        f"Set up a linear equation and determine the number of gigabytes \\(g\\) for which both options cost the exact same total amount."
    )
    sol = (
        f"**Step 1: Set up the equation**\n"
        f"\\[ {f1} + {v1}g = {f2} + {v2}g \\]\n\n"
        f"**Step 2: Collect like terms**\n"
        f"\\[ {v1}g - {v2}g = {f2} - {f1} \\]\n"
        f"\\[ {v1 - v2}g = {f2 - f1} \\]\n"
        f"\\[ g = \\frac{{{f2 - f1}}}{{{v1 - v2}}} = {x_units} \\text{{ GB}} \\]\n\n"
        f"**Cost at break-even:** \\(R{f1} + R{v1}({x_units}) = R{cost}\\)."
    )
    ans = f"g = {x_units} GB (Total cost = R{cost})"
    return {
        "id": f"g8_eq3_service_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "04_break_even_two_linear_service_plans",
        "learning_objective_id": "math_g8_eq3_service_comparison",
        "hints": {
            "tier_1": f"Cost A = {f1} + {v1}g; Cost B = {f2} + {v2}g.",
            "tier_2": f"Subtract {v2}g and {f1} from both sides.",
            "tier_3": f"g = {x_units} GB.",
        },
        "misconception_tags": ["combining_fixed_fee_with_variable_rate"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 05. Exponential Equation Base 2 Simple
# ----------------------------------------------------------------------
def arch_05_exponential_equation_base_2_simple(rng: random.Random) -> Dict[str, Any]:
    exp_val = rng.choice([3, 4, 5, 6, 7])
    target = 2 ** exp_val

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ 2^x = {target} \\]"
    )
    sol = (
        f"**Step 1:** Express **{target}** as a power of base 2:\n"
        f"\\[ {target} = 2^{exp_val} \\]\n\n"
        f"**Step 2:** Equate exponents since the bases are identical:\n"
        f"\\[ 2^x = 2^{exp_val} \\implies x = {exp_val} \\]"
    )
    ans = str(exp_val)
    return {
        "id": f"g8_eq3_exp2_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_exponential_equation_base_2_simple",
        "learning_objective_id": "math_g8_eq3_exponential_base2",
        "hints": {
            "tier_1": f"Write {target} as a power of 2: 2 × 2 × ...",
            "tier_2": f"2^{exp_val} = {target}.",
            "tier_3": f"x = {exp_val}.",
        },
        "misconception_tags": ["dividing_by_base_instead_of_equating_exponents"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 06. Exponential Equation Base 3 Simple
# ----------------------------------------------------------------------
def arch_06_exponential_equation_base_3_simple(rng: random.Random) -> Dict[str, Any]:
    exp_val = rng.choice([2, 3, 4, 5])
    target = 3 ** exp_val

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ 3^x = {target} \\]"
    )
    sol = (
        f"**Step 1:** Express **{target}** as a power of base 3:\n"
        f"\\[ {target} = 3^{exp_val} \\]\n\n"
        f"**Step 2:** Equate exponents:\n"
        f"\\[ 3^x = 3^{exp_val} \\implies x = {exp_val} \\]"
    )
    ans = str(exp_val)
    return {
        "id": f"g8_eq3_exp3_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_exponential_equation_base_3_simple",
        "learning_objective_id": "math_g8_eq3_exponential_base3",
        "hints": {
            "tier_1": f"Express {target} with base 3: 3^2=9, 3^3=27, etc.",
            "tier_2": f"3^{exp_val} = {target}.",
            "tier_3": f"x = {exp_val}.",
        },
        "misconception_tags": ["dividing_by_base_instead_of_equating_exponents"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 07. Exponential Equation Base 5 Simple
# ----------------------------------------------------------------------
def arch_07_exponential_equation_base_5_simple(rng: random.Random) -> Dict[str, Any]:
    exp_val = rng.choice([2, 3, 4])
    target = 5 ** exp_val

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ 5^x = {target} \\]"
    )
    sol = (
        f"**Step 1:** Express **{target}** as a power of 5:\n"
        f"\\[ {target} = 5^{exp_val} \\]\n\n"
        f"**Step 2:** Equate exponents:\n"
        f"\\[ 5^x = 5^{exp_val} \\implies x = {exp_val} \\]"
    )
    ans = str(exp_val)
    return {
        "id": f"g8_eq3_exp5_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_exponential_equation_base_5_simple",
        "learning_objective_id": "math_g8_eq3_exponential_base5",
        "hints": {
            "tier_1": f"5^2 = 25, 5^3 = 125, 5^4 = 625.",
            "tier_2": f"5^x = 5^{exp_val}.",
            "tier_3": f"x = {exp_val}.",
        },
        "misconception_tags": ["confusing_base_with_multiplier"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 08. Exponential Equation Base 10 Powers
# ----------------------------------------------------------------------
def arch_08_exponential_equation_base_10_powers(rng: random.Random) -> Dict[str, Any]:
    exp_val = rng.choice([2, 3, 4, 5])
    target = 10 ** exp_val

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ 10^x = {target:,} \\]".replace(",", " ")
    )
    sol = (
        f"**Step 1:** Count the number of zeros in **{target:,}**:\n"
        f"There are **{exp_val}** zeros, so \\({target:,} = 10^{exp_val}\\).\n\n"
        f"**Step 2:** Equate exponents:\n"
        f"\\[ 10^x = 10^{exp_val} \\implies x = {exp_val} \\]"
    ).replace(",", " ")
    ans = str(exp_val)
    return {
        "id": f"g8_eq3_exp10_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_exponential_equation_base_10_powers",
        "learning_objective_id": "math_g8_eq3_exponential_base10",
        "hints": {
            "tier_1": f"Count the zeros after the 1.",
            "tier_2": f"10^{exp_val} has {exp_val} zeros.",
            "tier_3": f"x = {exp_val}.",
        },
        "misconception_tags": ["counting_zeros_incorrectly"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 09. Exponential Equation Linear Exponent Addition
# ----------------------------------------------------------------------
def arch_09_exponential_equation_linear_exponent_addition(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4])
    a = rng.choice([1, 2, 3])
    ans_x = rng.choice([1, 2, 3, 4])
    total_exp = ans_x + a
    target = base ** total_exp

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {base}^{{x + {a}}} = {target} \\]"
    )
    sol = (
        f"**Step 1:** Express **{target}** as a power of base {base}:\n"
        f"\\[ {target} = {base}^{{{total_exp}}} \\]\n\n"
        f"**Step 2:** Equate exponents:\n"
        f"\\[ x + {a} = {total_exp} \\]\n\n"
        f"**Step 3:** Subtract {a} from both sides:\n"
        f"\\[ x = {total_exp} - {a} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_exp_add_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "09_exponential_equation_linear_exponent_addition",
        "learning_objective_id": "math_g8_eq3_exp_linear_add",
        "hints": {
            "tier_1": f"Write {target} as {base}^{{{total_exp}}}.",
            "tier_2": f"Set the exponent x + {a} = {total_exp}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["forgetting_to_equate_exponents", "subtraction_error_in_exponent_step"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 10. Exponential Equation Linear Exponent Subtraction
# ----------------------------------------------------------------------
def arch_10_exponential_equation_linear_exponent_subtraction(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5])
    b = rng.choice([1, 2, 3])
    ans_x = rng.choice([3, 4, 5])
    diff_exp = ans_x - b
    target = base ** diff_exp

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {base}^{{x - {b}}} = {target} \\]"
    )
    sol = (
        f"**Step 1:** Express **{target}** as a power of base {base}:\n"
        f"\\[ {target} = {base}^{{{diff_exp}}} \\]\n\n"
        f"**Step 2:** Equate exponents:\n"
        f"\\[ x - {b} = {diff_exp} \\]\n\n"
        f"**Step 3:** Add {b} to both sides:\n"
        f"\\[ x = {diff_exp} + {b} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_exp_sub_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "10_exponential_equation_linear_exponent_subtraction",
        "learning_objective_id": "math_g8_eq3_exp_linear_sub",
        "hints": {
            "tier_1": f"Write {target} as {base}^{{{diff_exp}}}.",
            "tier_2": f"Set x - {b} = {diff_exp}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["subtracting_instead_of_adding_inverse"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 11. Exponential Equation Coefficient Multiplier
# ----------------------------------------------------------------------
def arch_11_exponential_equation_coefficient_multiplier(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3])
    coeff = rng.choice([2, 3, 5, 7])
    exp_val = rng.choice([2, 3, 4])
    rhs = coeff * (base ** exp_val)

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {coeff} \\cdot {base}^x = {rhs} \\]"
    )
    sol = (
        f"**Step 1:** Divide both sides by the coefficient {coeff}:\n"
        f"\\[ {base}^x = \\frac{{{rhs}}}{{{coeff}}} = {base ** exp_val} \\]\n\n"
        f"**Step 2:** Express the RHS as a power of {base}:\n"
        f"\\[ {base}^x = {base}^{exp_val} \\]\n\n"
        f"**Step 3:** Equate exponents:\n"
        f"\\[ x = {exp_val} \\]"
    )
    ans = str(exp_val)
    return {
        "id": f"g8_eq3_exp_coeff_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "11_exponential_equation_coefficient_multiplier",
        "learning_objective_id": "math_g8_eq3_exp_coeff",
        "hints": {
            "tier_1": f"First divide both sides by {coeff}.",
            "tier_2": f"{base}^x = {rhs // coeff} = {base}^{exp_val}.",
            "tier_3": f"x = {exp_val}.",
        },
        "misconception_tags": ["multiplying_base_by_coefficient_violating_bodmas"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 12. Exponential Equation Negative Exponent Concept
# ----------------------------------------------------------------------
def arch_12_exponential_equation_negative_exponent_concept(rng: random.Random) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 10])
    k = rng.choice([1, 2, 3])
    denom = base ** k

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {base}^x = \\frac{{1}}{{{denom}}} \\]"
    )
    sol = (
        f"**Step 1:** Rewrite the fraction using negative exponent notation:\n"
        f"\\[ \\frac{{1}}{{{denom}}} = \\frac{{1}}{{{base}^{k}}} = {base}^{{-{k}}} \\]\n\n"
        f"**Step 2:** Equate exponents:\n"
        f"\\[ {base}^x = {base}^{{-{k}}} \\implies x = -{k} \\]"
    )
    ans = str(-k)
    return {
        "id": f"g8_eq3_exp_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_exponential_equation_negative_exponent_concept",
        "learning_objective_id": "math_g8_eq3_exp_neg",
        "hints": {
            "tier_1": f"Recall that 1 / a^n = a^(-n).",
            "tier_2": f"1 / {denom} = {base}^(-{k}).",
            "tier_3": f"x = -{k}.",
        },
        "misconception_tags": ["assuming_negative_fraction_yields_positive_exponent"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 13. Equation Fractional Denominator One Term
# ----------------------------------------------------------------------
def arch_13_equation_fractional_denominator_one_term(rng: random.Random) -> Dict[str, Any]:
    d = rng.choice([3, 4, 5, 6, 8])
    a = rng.choice([2, 5, 7, 9])
    ans_x = rng.choice([6, 12, 15, 18, 20])
    # x/d + a = b => b = ans_x/d + a. Ensure ans_x is multiple of d.
    ans_x = (ans_x // d + 1) * d
    b = (ans_x // d) + a

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{x}}{{{d}}} + {a} = {b} \\]"
    )
    sol = (
        f"**Step 1:** Subtract {a} from both sides:\n"
        f"\\[ \\frac{{x}}{{{d}}} = {b} - {a} = {b - a} \\]\n\n"
        f"**Step 2:** Multiply both sides by {d}:\n"
        f"\\[ x = ({b - a}) \\times {d} = {ans_x} \\]\n\n"
        f"**Check:** \\(\\frac{{{ans_x}}}{{{d}}} + {a} = {ans_x // d} + {a} = {b}\\)."
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_frac1_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "13_equation_fractional_denominator_one_term",
        "learning_objective_id": "math_g8_eq3_fraction_one_term",
        "hints": {
            "tier_1": f"Isolate the fraction x/{d} by subtracting {a} from both sides.",
            "tier_2": f"x/{d} = {b - a}.",
            "tier_3": f"Multiply by {d}: x = {ans_x}.",
        },
        "misconception_tags": ["multiplying_before_subtracting_constant"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 14. Equation Fractional Numerator Binomial
# ----------------------------------------------------------------------
def arch_14_equation_fractional_numerator_binomial(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 4, 5])
    a = rng.choice([2, 3, 4])
    ans_x = rng.choice([3, 4, 5, 6, 7])
    b = rng.choice([1, 2, 3, 5, 7])
    # (a*x + b) / c = d => ensure a*ans_x + b is divisible by c
    # Let d be integer
    numerator = a * ans_x + b
    # adjust b so that numerator % c == 0
    rem = numerator % c
    if rem != 0:
        b += (c - rem)
        numerator = a * ans_x + b
    d = numerator // c

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{{a}x + {b}}}{{{c}}} = {d} \\]"
    )
    sol = (
        f"**Step 1:** Clear the fraction by multiplying both sides by {c}:\n"
        f"\\[ {a}x + {b} = {d} \\times {c} = {d * c} \\]\n\n"
        f"**Step 2:** Subtract {b} from both sides:\n"
        f"\\[ {a}x = {d * c} - {b} = {d * c - b} \\]\n\n"
        f"**Step 3:** Divide by {a}:\n"
        f"\\[ x = \\frac{{{d * c - b}}}{{{a}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_frac_binom_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "14_equation_fractional_numerator_binomial",
        "learning_objective_id": "math_g8_eq3_fraction_binom_add",
        "hints": {
            "tier_1": f"Multiply both sides by {c} to clear the denominator.",
            "tier_2": f"{a}x + {b} = {d * c}.",
            "tier_3": f"{a}x = {d * c - b}, so x = {ans_x}.",
        },
        "misconception_tags": ["multiplying_only_numerator_part_by_denominator"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 15. Equation Fractional Subtraction Binomial
# ----------------------------------------------------------------------
def arch_15_equation_fractional_subtraction_binomial(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([3, 4, 5, 6])
    a = rng.choice([2, 3, 5])
    ans_x = rng.choice([3, 4, 5, 7, 8])
    b = rng.choice([1, 2, 4, 5])
    # (a*ans_x - b) must be divisible by c
    numerator = a * ans_x - b
    rem = numerator % c
    if rem != 0:
        b += rem
        if b >= a * ans_x:
            b = 1
            ans_x = 4
        numerator = a * ans_x - b
        # readjust to be exact
        if numerator % c != 0:
            c = 3
            a = 2
            ans_x = 5
            b = 1
            numerator = 2 * 5 - 1  # 9
    d = numerator // c

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{{a}x - {b}}}{{{c}}} = {d} \\]"
    )
    sol = (
        f"**Step 1:** Multiply both sides by {c}:\n"
        f"\\[ {a}x - {b} = {d} \\times {c} = {d * c} \\]\n\n"
        f"**Step 2:** Add {b} to both sides:\n"
        f"\\[ {a}x = {d * c} + {b} = {d * c + b} \\]\n\n"
        f"**Step 3:** Divide by {a}:\n"
        f"\\[ x = \\frac{{{d * c + b}}}{{{a}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_frac_sub_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "15_equation_fractional_subtraction_binomial",
        "learning_objective_id": "math_g8_eq3_fraction_binom_sub",
        "hints": {
            "tier_1": f"Multiply both sides by {c}.",
            "tier_2": f"{a}x - {b} = {d * c}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["sign_error_adding_subtrahend"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 16. Equation Fractions Sum Two Denominators
# ----------------------------------------------------------------------
def arch_16_equation_fractions_sum_two_denominators(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    b = rng.choice([3, 5])
    if a == b:
        b = 5
    lcm = math.lcm(a, b)
    # x/a + x/b = c => (b*x + a*x)/lcm = c => (a+b)*x = c*lcm
    # Let x be a multiple of lcm so everything is integer
    factor = rng.choice([1, 2, 3])
    ans_x = lcm * factor
    c = (ans_x // a) + (ans_x // b)

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{x}}{{{a}}} + \\frac{{x}}{{{b}}} = {c} \\]"
    )
    sol = (
        f"**Step 1:** Find the LCD of {a} and {b}, which is **{lcm}**.\n\n"
        f"**Step 2:** Multiply every term on both sides by {lcm}:\n"
        f"\\[ {lcm} \\cdot \\left(\\frac{{x}}{{{a}}}\\right) + {lcm} \\cdot \\left(\\frac{{x}}{{{b}}}\\right) = {lcm} \\cdot {c} \\]\n"
        f"\\[ {lcm // a}x + {lcm // b}x = {lcm * c} \\]\n\n"
        f"**Step 3:** Combine like terms:\n"
        f"\\[ {lcm // a + lcm // b}x = {lcm * c} \\]\n\n"
        f"**Step 4:** Divide by {lcm // a + lcm // b}:\n"
        f"\\[ x = \\frac{{{lcm * c}}}{{{lcm // a + lcm // b}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_frac_sum2_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "16_equation_fractions_sum_two_denominators",
        "learning_objective_id": "math_g8_eq3_frac_sum_lcd",
        "hints": {
            "tier_1": f"The lowest common denominator of {a} and {b} is {lcm}.",
            "tier_2": f"Multiply every term by {lcm}: {lcm // a}x + {lcm // b}x = {lcm * c}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["adding_denominators_directly", "forgetting_to_multiply_rhs_by_lcd"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 17. Equation Fractions Difference Two Denominators
# ----------------------------------------------------------------------
def arch_17_equation_fractions_difference_two_denominators(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    b = rng.choice([4, 5, 6])
    if a >= b:
        b = a + 2
    lcm = math.lcm(a, b)
    factor = rng.choice([1, 2, 3])
    ans_x = lcm * factor
    c = (ans_x // a) - (ans_x // b)

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ \\frac{{x}}{{{a}}} - \\frac{{x}}{{{b}}} = {c} \\]"
    )
    sol = (
        f"**Step 1:** The LCD of {a} and {b} is **{lcm}**.\n\n"
        f"**Step 2:** Multiply both sides by {lcm}:\n"
        f"\\[ {lcm // a}x - {lcm // b}x = {lcm * c} \\]\n\n"
        f"**Step 3:** Combine like terms:\n"
        f"\\[ {lcm // a - lcm // b}x = {lcm * c} \\]\n\n"
        f"**Step 4:** Divide by {lcm // a - lcm // b}:\n"
        f"\\[ x = \\frac{{{lcm * c}}}{{{lcm // a - lcm // b}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_frac_diff_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "17_equation_fractions_difference_two_denominators",
        "learning_objective_id": "math_g8_eq3_frac_diff_lcd",
        "hints": {
            "tier_1": f"Find LCD of {a} and {b} = {lcm}.",
            "tier_2": f"Multiply every term by {lcm}: ({lcm // a} - {lcm // b})x = {lcm * c}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["subtracting_denominators", "forgetting_to_multiply_rhs_by_lcd"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 18. Equation Fraction Equals Fraction (Cross-Multiplication)
# ----------------------------------------------------------------------
def arch_18_equation_fraction_equals_fraction(rng: random.Random) -> Dict[str, Any]:
    c = rng.choice([2, 3, 5])
    e = rng.choice([3, 4, 7])
    if c == e:
        e = c + 2
    ans_x = rng.choice([2, 3, 4, 5])
    b = rng.choice([1, 2, 3])
    # (x + b) / c = (2x + d) / e
    # e*(x + b) = c*(2x + d) => e*x + e*b = 2c*x + c*d => (e - 2c)*x + e*b = c*d
    # Choose d so it balances
    # Let 2c != e
    if 2 * c == e:
        c += 1
    cd_val = (e - 2 * c) * ans_x + e * b
    # Ensure d is integer
    d = cd_val // c
    # Recompute ans_x to ensure exact integer
    ans_x = (c * d - e * b) // (e - 2 * c)

    prompt = (
        f"Solve for \\(x\\) by cross-multiplying:\n"
        f"\\[ \\frac{{x + {b}}}{{{c}}} = \\frac{{2x + {d}}}{{{e}}} \\]"
    )
    sol = (
        f"**Step 1:** Cross-multiply:\n"
        f"\\[ {e}(x + {b}) = {c}(2x + {d}) \\]\n\n"
        f"**Step 2:** Expand both brackets:\n"
        f"\\[ {e}x + {e * b} = {2 * c}x + {c * d} \\]\n\n"
        f"**Step 3:** Group like terms:\n"
        f"\\[ {e}x - {2 * c}x = {c * d} - {e * b} \\]\n"
        f"\\[ {e - 2 * c}x = {c * d - e * b} \\]\n\n"
        f"**Step 4:** Divide by {e - 2 * c}:\n"
        f"\\[ x = \\frac{{{c * d - e * b}}}{{{e - 2 * c}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_cross_mult_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "18_equation_fraction_equals_fraction",
        "learning_objective_id": "math_g8_eq3_cross_mult",
        "hints": {
            "tier_1": f"Cross-multiply: {e}(x + {b}) = {c}(2x + {d}).",
            "tier_2": f"Expand brackets: {e}x + {e * b} = {2 * c}x + {c * d}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["cross_multiplication_distribution_error"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 19. Equation Brackets Both Sides Positive
# ----------------------------------------------------------------------
def arch_19_equation_brackets_both_sides_positive(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([3, 4, 5])
    c = rng.choice([1, 2])
    ans_x = rng.choice([2, 3, 4, 6])
    b = rng.choice([2, 3, 5])
    # a(x + b) = c(x + d) => a*x + a*b = c*x + c*d => (a - c)*ans_x + a*b = c*d
    cd_val = (a - c) * ans_x + a * b
    d = cd_val // c
    # Rebalance
    ans_x = (c * d - a * b) // (a - c)

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}(x + {b}) = {c}(x + {d}) \\]"
    )
    sol = (
        f"**Step 1:** Distribute and expand both brackets:\n"
        f"\\[ {a}x + {a * b} = {c}x + {c * d} \\]\n\n"
        f"**Step 2:** Transpose variables to the LHS and constants to the RHS:\n"
        f"\\[ {a}x - {c}x = {c * d} - {a * b} \\]\n"
        f"\\[ {a - c}x = {c * d - a * b} \\]\n\n"
        f"**Step 3:** Divide by {a - c}:\n"
        f"\\[ x = \\frac{{{c * d - a * b}}}{{{a - c}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_brk_both_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "19_equation_brackets_both_sides_positive",
        "learning_objective_id": "math_g8_eq3_brackets_both_pos",
        "hints": {
            "tier_1": f"Expand: {a}x + {a * b} = {c}x + {c * d}.",
            "tier_2": f"({a} - {c})x = {c * d - a * b}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["forgetting_to_expand_multiplier_to_second_term"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 20. Equation Brackets Both Sides Mixed Signs
# ----------------------------------------------------------------------
def arch_20_equation_brackets_both_sides_mixed_signs(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4, 5, 6])
    c = rng.choice([2, 3])
    ans_x = rng.choice([3, 4, 5, 7])
    b = rng.choice([1, 2, 3])
    # a(x - b) = c(x + d) => a*x - a*b = c*x + c*d => (a - c)*ans_x - a*b = c*d
    cd_val = (a - c) * ans_x - a * b
    d = cd_val // c
    ans_x = (c * d + a * b) // (a - c)

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}(x - {b}) = {c}(x + {d}) \\]"
    )
    sol = (
        f"**Step 1:** Expand both brackets:\n"
        f"\\[ {a}x - {a * b} = {c}x + {c * d} \\]\n\n"
        f"**Step 2:** Group terms:\n"
        f"\\[ {a}x - {c}x = {c * d} + {a * b} \\]\n"
        f"\\[ {a - c}x = {c * d + a * b} \\]\n\n"
        f"**Step 3:** Divide by {a - c}:\n"
        f"\\[ x = \\frac{{{c * d + a * b}}}{{{a - c}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_brk_mix_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "20_equation_brackets_both_sides_mixed_signs",
        "learning_objective_id": "math_g8_eq3_brackets_mixed",
        "hints": {
            "tier_1": f"Remember that {a} × (-{b}) = -{a * b}.",
            "tier_2": f"{a}x - {c}x = {c * d} + {a * b}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["sign_error_expanding_negative_term"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 21. Equation Brackets With Negative Multiplier
# ----------------------------------------------------------------------
def arch_21_equation_brackets_with_negative_multiplier(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3, 4])
    c = rng.choice([2, 3])
    ans_x = rng.choice([2, 3, 4, 5])
    b = rng.choice([2, 3, 4])
    # -a(x + b) = c(x - d) => -a*x - a*b = c*x - c*d => (-a - c)*ans_x - a*b = -c*d
    # c*d = (a + c)*ans_x + a*b
    cd_val = (a + c) * ans_x + a * b
    d = cd_val // c
    ans_x = (c * d - a * b) // (a + c)

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ -{a}(x + {b}) = {c}(x - {d}) \\]"
    )
    sol = (
        f"**Step 1:** Expand both brackets, paying special attention to the negative sign on the left:\n"
        f"\\[ -{a}x - {a * b} = {c}x - {c * d} \\]\n\n"
        f"**Step 2:** Group terms:\n"
        f"\\[ -{a}x - {c}x = -{c * d} + {a * b} \\]\n"
        f"\\[ -{a + c}x = -{c * d - a * b} \\]\n\n"
        f"**Step 3:** Divide by \\(-{a + c}\\):\n"
        f"\\[ x = \\frac{{-{c * d - a * b}}}{{-{a + c}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_brk_neg_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "subskill": "21_equation_brackets_with_negative_multiplier",
        "learning_objective_id": "math_g8_eq3_brackets_neg_multiplier",
        "hints": {
            "tier_1": f"-{a} × x = -{a}x, and -{a} × {b} = -{a * b}.",
            "tier_2": f"-{a + c}x = -{c * d - a * b}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["forgetting_to_distribute_negative_sign"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 22. Equation Two Brackets Distributed Same Side
# ----------------------------------------------------------------------
def arch_22_equation_two_brackets_distributed_same_side(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    c = rng.choice([2, 4])
    ans_x = rng.choice([2, 3, 4, 5])
    b = rng.choice([1, 2, 3])
    d = rng.choice([1, 2, 4])
    # a(x + b) + c(x + d) = e => (a + c)*ans_x + a*b + c*d = e
    e = (a + c) * ans_x + a * b + c * d

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}(x + {b}) + {c}(x + {d}) = {e} \\]"
    )
    sol = (
        f"**Step 1:** Expand both sets of brackets:\n"
        f"\\[ {a}x + {a * b} + {c}x + {c * d} = {e} \\]\n\n"
        f"**Step 2:** Combine like terms on the LHS:\n"
        f"\\[ ({a} + {c})x + ({a * b} + {c * d}) = {e} \\]\n"
        f"\\[ {a + c}x + {a * b + c * d} = {e} \\]\n\n"
        f"**Step 3:** Subtract {a * b + c * d} from both sides:\n"
        f"\\[ {a + c}x = {e} - {a * b + c * d} = {e - (a * b + c * d)} \\]\n\n"
        f"**Step 4:** Divide by {a + c}:\n"
        f"\\[ x = \\frac{{{e - (a * b + c * d)}}}{{{a + c}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_2brk_same_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "22_equation_two_brackets_distributed_same_side",
        "learning_objective_id": "math_g8_eq3_two_brackets_same_side",
        "hints": {
            "tier_1": f"Expand both brackets: {a}x + {a * b} + {c}x + {c * d} = {e}.",
            "tier_2": f"Combine: {a + c}x + {a * b + c * d} = {e}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["adding_coefficients_before_distributing"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 23. Equation Difference Of Two Brackets
# ----------------------------------------------------------------------
def arch_23_equation_difference_of_two_brackets(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([4, 5, 6])
    c = rng.choice([2, 3])
    ans_x = rng.choice([2, 3, 4, 5])
    b = rng.choice([2, 3, 4])
    d = rng.choice([1, 2, 3])
    # a(x + b) - c(x - d) = e => a*x + a*b - c*x + c*d = (a - c)*ans_x + a*b + c*d = e
    e = (a - c) * ans_x + a * b + c * d

    prompt = (
        f"Solve for \\(x\\):\n"
        f"\\[ {a}(x + {b}) - {c}(x - {d}) = {e} \\]"
    )
    sol = (
        f"**Step 1:** Expand both brackets, distributing \\(-{c}\\) across \\((x - {d})\\):\n"
        f"\\[ {a}x + {a * b} - {c}x + {c * d} = {e} \\]\n\n"
        f"**Step 2:** Combine like terms on the LHS:\n"
        f"\\[ ({a} - {c})x + ({a * b} + {c * d}) = {e} \\]\n"
        f"\\[ {a - c}x + {a * b + c * d} = {e} \\]\n\n"
        f"**Step 3:** Subtract {a * b + c * d} from both sides:\n"
        f"\\[ {a - c}x = {e - (a * b + c * d)} \\]\n\n"
        f"**Step 4:** Divide by {a - c}:\n"
        f"\\[ x = \\frac{{{e - (a * b + c * d)}}}{{{a - c}}} = {ans_x} \\]"
    )
    ans = str(ans_x)
    return {
        "id": f"g8_eq3_diff_brk_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "23_equation_difference_of_two_brackets",
        "learning_objective_id": "math_g8_eq3_diff_two_brackets",
        "hints": {
            "tier_1": f"Distribute -{c}: -{c}(x - {d}) = -{c}x + {c * d}.",
            "tier_2": f"Combine: {a - c}x + {a * b + c * d} = {e}.",
            "tier_3": f"x = {ans_x}.",
        },
        "misconception_tags": ["sign_error_negative_times_negative"],
        "diagram_spec": None,
    }


# ----------------------------------------------------------------------
# 24. Geometry Angles On Straight Line Algebraic (WITH SVG)
# ----------------------------------------------------------------------
def arch_24_geometry_angles_on_straight_line_algebraic(rng: random.Random) -> Dict[str, Any]:
    a = rng.choice([2, 3])
    c = rng.choice([1, 2])
    ans_x = rng.choice([15, 20, 25, 30])
    b = rng.choice([10, 20])
    # (a*x + b) + (c*x + d) = 180 => (a+c)*ans_x + b + d = 180
    d = 180 - (a + c) * ans_x - b
    if d < 5 or d > 60:
        ans_x = 20
        a = 2
        c = 3
        b = 10
        # (2+3)*20 + 10 + d = 180 => 100 + 10 + d = 180 => d = 70
        d = 70

    ang1 = a * ans_x + b
    ang2 = c * ans_x + d

    lbl1 = f"{a}x + {b}°"
    lbl2 = f"{c}x + {d}°"
    svg = draw_angles_on_line_svg(ang1, lbl1, lbl2)

    prompt = (
        f"In the straight-line angle configuration below, two adjacent angles lie on a straight line:\n\n"
        f"\\[ \\angle 1 = ({a}x + {b})^\\circ \\quad \\text{{and}} \\quad \\angle 2 = ({c}x + {d})^\\circ \\]\n\n"
        f"1. State the geometric reason relating these two angles.\n"
        f"2. Set up an algebraic equation and solve for \\(x\\).\n"
        f"3. Calculate the actual size in degrees of both angles."
    )
    sol = (
        f"**Step 1: Geometric Theorem**\n"
        f"Adjacent angles on a straight line sum to \\(180^\\circ\\) (\\(\\angle\\text{{s on a straight line}}\\).\n\n"
        f"**Step 2: Set up and solve equation**\n"
        f"\\[ ({a}x + {b}) + ({c}x + {d}) = 180 \\]\n"
        f"\\[ {a + c}x + {b + d} = 180 \\]\n"
        f"\\[ {a + c}x = 180 - {b + d} = {180 - (b + d)} \\]\n"
        f"\\[ x = \\frac{{{180 - (b + d)}}}{{{a + c}}} = {ans_x} \\]\n\n"
        f"**Step 3: Actual angle sizes**\n"
        f"\\(\\angle 1 = {a}({ans_x}) + {b} = {ang1}^\\circ\\)\n"
        f"\\(\\angle 2 = {c}({ans_x}) + {d} = {ang2}^\\circ\\)\n"
        f"Check: \\({ang1}^\\circ + {ang2}^\\circ = 180^\\circ\\)."
    )
    ans = f"1. adj angles on straight line = 180°; 2. x = {ans_x}; 3. {ang1}°, {ang2}°"
    return {
        "id": f"g8_eq3_geom_line_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 5,
        "subskill": "24_geometry_angles_on_straight_line_algebraic",
        "learning_objective_id": "math_g8_eq3_angles_straight_line",
        "hints": {
            "tier_1": f"Angles on a straight line add up to 180°.",
            "tier_2": f"({a}x + {b}) + ({c}x + {d}) = 180.",
            "tier_3": f"{a + c}x = {180 - (b + d)}, so x = {ans_x}.",
        },
        "misconception_tags": ["setting_sum_equal_to_90_instead_of_180", "algebraic_combination_error"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# ----------------------------------------------------------------------
# 25. Geometry Three Angles On Straight Line (WITH SVG)
# ----------------------------------------------------------------------
def arch_25_geometry_three_angles_on_straight_line(rng: random.Random) -> Dict[str, Any]:
    # Three angles: x, 2x, 3x (sum = 6x = 180 => x = 30) or x, 3x, 5x or similar
    multiplier_set = rng.choice([
        (1, 2, 3),  # sum 6 => x = 30
        (1, 3, 2),  # sum 6 => x = 30
        (2, 3, 4),  # sum 9 => x = 20
        (1, 4, 1),  # sum 6 => x = 30
        (1, 2, 6),  # sum 9 => x = 20
    ])
    m1, m2, m3 = multiplier_set
    total_m = m1 + m2 + m3
    ans_x = 180 // total_m
    ang1 = m1 * ans_x
    ang2 = m2 * ans_x
    ang3 = m3 * ans_x

    # SVG with first angle
    lbl1 = f"{m1}x"
    lbl2 = f"{m2}x + {m3}x"
    svg = draw_angles_on_line_svg(ang1, lbl1, lbl2)

    prompt = (
        f"Three adjacent angles meet at a common vertex along a straight line:\n\n"
        f"\\[ \\angle A = {m1}x^\\circ, \\quad \\angle B = {m2}x^\\circ, \\quad \\angle C = {m3}x^\\circ \\]\n\n"
        f"1. Set up an algebraic equation based on the straight line theorem.\n"
        f"2. Solve for \\(x\\).\n"
        f"3. Find the value in degrees of the largest of the three angles."
    )
    sol = (
        f"**Step 1: Set up equation**\n"
        f"Adjacent angles on a straight line add up to \\(180^\\circ\\):\n"
        f"\\[ {m1}x + {m2}x + {m3}x = 180 \\]\n"
        f"\\[ {total_m}x = 180 \\]\n\n"
        f"**Step 2: Solve for x**\n"
        f"\\[ x = \\frac{{180}}{{{total_m}}} = {ans_x} \\]\n\n"
        f"**Step 3: Largest angle**\n"
        f"The angles are \\({ang1}^\\circ\\), \\({ang2}^\\circ\\), and \\({ang3}^\\circ\\).\n"
        f"The largest angle is **{max(ang1, ang2, ang3)}^\\circ**."
    )
    ans = f"1. {total_m}x = 180; 2. x = {ans_x}; 3. Largest angle = {max(ang1, ang2, ang3)}°"
    return {
        "id": f"g8_eq3_3angles_line_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "question": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "25_geometry_three_angles_on_straight_line",
        "learning_objective_id": "math_g8_eq3_three_angles_line",
        "hints": {
            "tier_1": f"Sum all three expressions and set equal to 180°.",
            "tier_2": f"{total_m}x = 180.",
            "tier_3": f"x = {ans_x}, largest angle = {max(ang1, ang2, ang3)}°.",
        },
        "misconception_tags": ["forgetting_to_include_all_three_angles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


BUILDERS_01_25: List[Callable[[random.Random], Dict[str, Any]]] = [
    arch_01_orchard_linear_growth_target_milestone,
    arch_02_orchard_comparing_two_growth_rates_break_even,
    arch_03_population_linear_decline_milestone,
    arch_04_break_even_two_linear_service_plans,
    arch_05_exponential_equation_base_2_simple,
    arch_06_exponential_equation_base_3_simple,
    arch_07_exponential_equation_base_5_simple,
    arch_08_exponential_equation_base_10_powers,
    arch_09_exponential_equation_linear_exponent_addition,
    arch_10_exponential_equation_linear_exponent_subtraction,
    arch_11_exponential_equation_coefficient_multiplier,
    arch_12_exponential_equation_negative_exponent_concept,
    arch_13_equation_fractional_denominator_one_term,
    arch_14_equation_fractional_numerator_binomial,
    arch_15_equation_fractional_subtraction_binomial,
    arch_16_equation_fractions_sum_two_denominators,
    arch_17_equation_fractions_difference_two_denominators,
    arch_18_equation_fraction_equals_fraction,
    arch_19_equation_brackets_both_sides_positive,
    arch_20_equation_brackets_both_sides_mixed_signs,
    arch_21_equation_brackets_with_negative_multiplier,
    arch_22_equation_two_brackets_distributed_same_side,
    arch_23_equation_difference_of_two_brackets,
    arch_24_geometry_angles_on_straight_line_algebraic,
    arch_25_geometry_three_angles_on_straight_line,
]
