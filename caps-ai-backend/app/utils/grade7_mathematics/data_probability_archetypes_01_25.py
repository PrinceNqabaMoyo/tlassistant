"""Grade 7 Mathematics - Probability: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/02. Probability.md & Probability Studio.md
Focus: Probability scale (0 to 1), theoretical probability definition, sample spaces, coins, dice (even, odd, prime, multiples), spinners with clean SVGs, coloured marbles/buttons, playing cards, and letter tiles.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


def _svg_spinner(sectors: List[Dict[str, Any]]) -> str:
    """Renders a clean static 2D SVG circular spinner with coloured sectors."""
    w, h = 260, 260
    cx, cy, r = 130, 130, 100
    n = len(sectors)
    angle_step = 360 / n

    paths = []
    for i, sec in enumerate(sectors):
        start_deg = i * angle_step
        end_deg = (i + 1) * angle_step
        s_rad = math.radians(start_deg)
        e_rad = math.radians(end_deg)
        x1 = cx + r * math.cos(s_rad)
        y1 = cy + r * math.sin(s_rad)
        x2 = cx + r * math.cos(e_rad)
        y2 = cy + r * math.sin(e_rad)
        color = sec.get("color", "#3b82f6")
        label = sec.get("label", str(i + 1))

        # SVG arc path
        d = f"M {cx} {cy} L {x1:.1f} {y1:.1f} A {r} {r} 0 0 1 {x2:.1f} {y2:.1f} Z"
        paths.append(f'<path d="{d}" fill="{color}" stroke="#ffffff" stroke-width="2"/>')

        # Label position
        mid_rad = math.radians((start_deg + end_deg) / 2)
        lx = cx + (r * 0.65) * math.cos(mid_rad)
        ly = cy + (r * 0.65) * math.sin(mid_rad)
        paths.append(f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="middle" font-size="12" font-weight="bold" fill="#ffffff">{label}</text>')

    # Pointer arrow
    pointer = (
        f'<polygon points="{cx-6},{cy-15} {cx+6},{cy-15} {cx},{cy-r+15}" fill="#1e293b"/>'
        f'<circle cx="{cx}" cy="{cy}" r="8" fill="#1e293b"/>'
    )

    return (
        f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'{"".join(paths)}{pointer}'
        f'</svg>'
    )


# 01. Probability scale impossible certain likely unlikely
def arch_01_probability_scale_impossible_certain_likely_unlikely(rng: random.Random) -> Dict[str, Any]:
    ans = "Impossible: 0; Unlikely: between 0 and 0,5; Even chance: 0,5 (50%); Likely: between 0,5 and 1; Certain: 1 (100%)"
    prompt = (
        "In probability theory, the likelihood of any event lies on a scale from $0$ to $1$ (or $0\\%$ to $100\\%$).\n\n"
        "State the numerical probability (as a decimal or percentage) associated with each probability term:\n"
        "1. **Impossible event**\n"
        "2. **Even chance (equally likely)**\n"
        "3. **Certain event**\n"
        "4. Where do **unlikely** and **likely** events lie on this scale?"
    )
    sol = (
        "**The Probability Scale:**\n"
        "1. **Impossible event:** $P = 0$ ($0\\%$ chance of occurring).\n"
        "2. **Even chance:** $P = 0{,}5$ (or $\\frac{1}{2}$, $50\\%$ chance).\n"
        "3. **Certain event:** $P = 1$ ($100\\%$ certainty of occurring).\n"
        "4. **Unlikely events:** Lie between $0$ and $0{,}5$ ($0\\% < P < 50\\%$).\n"
        "5. **Likely events:** Lie between $0{,}5$ and $1$ ($50\\% < P < 100\\%$)."
    )
    return {
        "id": f"g7_pr_01_{rng.randint(100000, 999999)}",
        "subskill": "01_probability_scale_impossible_certain_likely_unlikely",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Impossible is 0; Even chance is 0,5; Certain is 1; Unlikely is 0 to 0,5; Likely is 0,5 to 1",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pr_01",
        "hints": {
            "tier_1": "Can a probability ever be less than 0 or greater than 1?",
            "tier_2": "0 is impossible, 0,5 is fifty-fifty, 1 is guaranteed.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["probability_outside_0_to_1_range"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Assigns 0 to impossible and 1 to certain", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Assigns 0,5 (50%) to even chance", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Positions unlikely and likely in correct intervals", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 02. Theoretical probability definition formula
def arch_02_theoretical_probability_definition_formula(rng: random.Random) -> Dict[str, Any]:
    ans = "P(E) = (Number of favourable outcomes) / (Total number of possible outcomes)"
    prompt = (
        "State the mathematical formula used to calculate the **theoretical probability** of an event $E$ "
        "when all possible outcomes are equally likely."
    )
    sol = (
        "**Formula for Theoretical Probability:**\n"
        "$$P(E) = \\frac{\\text{Number of favourable outcomes}}{\\text{Total number of possible outcomes}} = \\frac{n(E)}{n(S)}$$\n\n"
        "where $n(E)$ is the count of successful outcomes and $n(S)$ is the total size of the sample space."
    )
    return {
        "id": f"g7_pr_02_{rng.randint(100000, 999999)}",
        "subskill": "02_theoretical_probability_definition_formula",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "P(E) = Number of favourable outcomes / Total number of possible outcomes",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_02",
        "hints": {
            "tier_1": "Favourable outcomes divided by total possible outcomes.",
            "tier_2": "Fraction: n(E) / n(S).",
            "tier_3": "P(E) = Favourable / Total."
        },
        "misconception_tags": ["inverting_probability_ratio"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States favourable outcomes as numerator", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States total possible outcomes as denominator", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 03. Sample space listing fair die
def arch_03_sample_space_listing_fair_die(rng: random.Random) -> Dict[str, Any]:
    ans = "S = {1; 2; 3; 4; 5; 6}; n(S) = 6"
    prompt = (
        "A fair standard six-sided die is rolled once.\n\n"
        "1. Define what a **sample space** ($S$) is in probability.\n"
        "2. List all the elements of the sample space $S$ for rolling a six-sided die, and state $n(S)$."
    )
    sol = (
        "**1. Definition:**\n"
        "The sample space ($S$) is the set of all possible outcomes of a probability experiment.\n\n"
        "**2. Sample Space for a 6-sided die:**\n"
        "$$S = \\{1;\\; 2;\\; 3;\\; 4;\\; 5;\\; 6\\}$$\n"
        "$$\\text{Total number of outcomes: } n(S) = 6$$"
    )
    return {
        "id": f"g7_pr_03_{rng.randint(100000, 999999)}",
        "subskill": "03_sample_space_listing_fair_die",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Sample space is set of all outcomes; S = {1; 2; 3; 4; 5; 6}, n(S) = 6",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_03",
        "hints": {
            "tier_1": "What are all the numbers on a standard die?",
            "tier_2": "1, 2, 3, 4, 5, 6.",
            "tier_3": "S = {1, 2, 3, 4, 5, 6}; n(S) = 6."
        },
        "misconception_tags": ["omitting_elements_from_sample_space"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Defines sample space as set of all possible outcomes", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Lists {1, 2, 3, 4, 5, 6} with n(S) = 6", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 04. Sample space listing fair coin
def arch_04_sample_space_listing_fair_coin(rng: random.Random) -> Dict[str, Any]:
    ans = "S = {Head, Tail}; n(S) = 2; P(Head) = 1/2 or 50%"
    prompt = (
        "A standard South African coin is tossed into the air.\n\n"
        "1. Write down the sample space for this experiment.\n"
        "2. What is the theoretical probability of getting a Head? Express your answer as a simplified fraction and as a percentage."
    )
    sol = (
        "**1. Sample Space:**\n"
        "$$S = \\{\\text{Head};\\; \\text{Tail}\\}$$\n"
        "$$n(S) = 2$$\n\n"
        "**2. Probability of a Head:**\n"
        "$$P(\\text{Head}) = \\frac{1}{2} = 0{,}5 = 50\\%$$"
    )
    return {
        "id": f"g7_pr_04_{rng.randint(100000, 999999)}",
        "subskill": "04_sample_space_listing_fair_coin",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "S = {Head, Tail}; P(Head) = 1/2 = 50%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_04",
        "hints": {
            "tier_1": "A coin has only two sides: Heads or Tails.",
            "tier_2": "Favourable = 1; Total = 2.",
            "tier_3": "1/2 or 50%."
        },
        "misconception_tags": ["coin_landing_on_edge_misconception"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Lists sample space {Head, Tail}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States probability = 1/2 (50%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 05. Probability coin toss head tail
def arch_05_probability_coin_toss_head_tail(rng: random.Random) -> Dict[str, Any]:
    ans = "1/2 (or 0,5 or 50%)"
    prompt = (
        "A fair coin is tossed. What is the probability of landing on **Tails**?\n"
        "Provide your answer as a simplified fraction."
    )
    sol = (
        "$$P(\\text{Tail}) = \\frac{\\text{Number of Tails}}{\\text{Total Outcomes}} = \\frac{1}{2}$$"
    )
    return {
        "id": f"g7_pr_05_{rng.randint(100000, 999999)}",
        "subskill": "05_probability_coin_toss_head_tail",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1/2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_pr_05",
        "hints": {
            "tier_1": "1 tail out of 2 sides.",
            "tier_2": "Fraction is 1/2.",
            "tier_3": "1/2."
        },
        "misconception_tags": ["arithmetic_probability_fraction_error"],
        "marking_schema": {
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": "States 1/2 (0,5 or 50%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 06. Probability fair die single number
def arch_06_probability_fair_die_single_number(rng: random.Random) -> Dict[str, Any]:
    target_num = rng.randint(1, 6)
    ans = "1/6"
    prompt = (
        f"A fair six-sided die is rolled once. What is the probability of rolling a **{target_num}**?"
    )
    sol = (
        f"**Calculation:**\n"
        f"Total possible outcomes $n(S) = 6$ (numbers $1$ to $6$).\n"
        f"There is only one face with the number ${target_num}$, so $n(E) = 1$.\n\n"
        f"$$P(\\text{{rolling a {target_num}}}) = \\frac{{1}}{{6}}$$"
    )
    return {
        "id": f"g7_pr_06_{rng.randint(100000, 999999)}",
        "subskill": "06_probability_fair_die_single_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1/6",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "math_g7_pr_06",
        "hints": {
            "tier_1": f"How many {target_num}s are on a die? Only 1.",
            "tier_2": "How many total faces? 6.",
            "tier_3": "1/6."
        },
        "misconception_tags": ["die_number_substituted_for_probability"],
        "marking_schema": {
            "total_marks": 1,
            "marking_points": [
                {"id": "mp1", "desc": "States 1/6", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 07. Probability fair die even odd
def arch_07_probability_fair_die_even_odd(rng: random.Random) -> Dict[str, Any]:
    p_type = rng.choice(["even", "odd"])
    nums = "{2; 4; 6}" if p_type == "even" else "{1; 3; 5}"
    ans = "1/2 (or 3/6)"
    prompt = (
        f"A fair six-sided die is rolled once.\n\n"
        f"1. List all the **{p_type} numbers** on the die.\n"
        f"2. Calculate the probability of rolling an {p_type} number as a simplified fraction."
    )
    sol = (
        f"**1. Favourable Outcomes:**\n"
        f"The {p_type} numbers are ${nums}$. There are $3$ favourable outcomes.\n\n"
        f"**2. Probability Calculation:**\n"
        f"$$P(\\text{{{p_type}}}) = \\frac{{3}}{{6}} = \\frac{{1}}{{2}}$$"
    )
    return {
        "id": f"g7_pr_07_{rng.randint(100000, 999999)}",
        "subskill": "07_probability_fair_die_even_odd",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Numbers are {nums}; P = 3/6 = 1/2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_07",
        "hints": {
            "tier_1": f"Count how many {p_type} numbers exist between 1 and 6.",
            "tier_2": "There are 3 out of 6.",
            "tier_3": "3/6 simplifies to 1/2."
        },
        "misconception_tags": ["forgetting_to_simplify_probability_fraction"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Lists favourable {p_type} numbers", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates simplified probability = 1/2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 08. Probability fair die prime number
def arch_08_probability_fair_die_prime_number(rng: random.Random) -> Dict[str, Any]:
    ans = "Prime numbers: {2; 3; 5}; P(prime) = 3/6 = 1/2"
    prompt = (
        "A fair standard die is rolled.\n\n"
        "1. List all the **prime numbers** on a standard six-sided die.\n"
        "(Remember: $1$ is neither prime nor composite!).\n"
        "2. Calculate the probability of rolling a prime number."
    )
    sol = (
        "**1. Prime Numbers on a Die:**\n"
        "A prime number has exactly two distinct factors ($1$ and itself).\n"
        "On a die, the prime numbers are: **$2, 3, 5$** (total = $3$ numbers).\n"
        "*(Note: 1 is not a prime number)*.\n\n"
        "**2. Probability Calculation:**\n"
        "$$P(\\text{Prime}) = \\frac{3}{6} = \\frac{1}{2}$$"
    )
    return {
        "id": f"g7_pr_08_{rng.randint(100000, 999999)}",
        "subskill": "08_probability_fair_die_prime_number",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Primes are 2, 3, 5; P(prime) = 3/6 = 1/2",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_08",
        "hints": {
            "tier_1": "Is 1 a prime number? No. The primes between 1 and 6 are 2, 3, and 5.",
            "tier_2": "There are 3 primes out of 6 possible numbers.",
            "tier_3": "P(prime) = 3/6 = 1/2."
        },
        "misconception_tags": ["treating_1_as_prime_number"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies primes {2, 3, 5} and excludes 1", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates probability = 1/2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 09. Probability fair die greater than threshold
def arch_09_probability_fair_die_greater_than_threshold(rng: random.Random) -> Dict[str, Any]:
    thresh = rng.choice([2, 4])
    if thresh == 2:
        favs = "{3; 4; 5; 6}"
        count = 4
        ans = "4/6 = 2/3"
    else:  # thresh == 4
        favs = "{5; 6}"
        count = 2
        ans = "2/6 = 1/3"
    prompt = (
        f"A standard die is rolled. What is the probability of rolling a number **strictly greater than {thresh}**?\n"
        f"Give your answer as a simplified fraction."
    )
    sol = (
        f"**Calculation:**\n"
        f"Numbers strictly greater than ${thresh}$ are: ${favs}$ ($n = {count}$).\n"
        f"$$P(> {thresh}) = \\frac{{{count}}}{{6}} = {ans}$$"
    )
    return {
        "id": f"g7_pr_09_{rng.randint(100000, 999999)}",
        "subskill": "09_probability_fair_die_greater_than_threshold",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_09",
        "hints": {
            "tier_1": f"Do not include {thresh}! Strictly greater than {thresh}.",
            "tier_2": f"Favourable numbers: {favs}.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["including_boundary_in_strictly_greater"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identifies {count} favourable outcomes", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Simplifies to {ans}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 10. Probability fair die multiples
def arch_10_probability_fair_die_multiples(rng: random.Random) -> Dict[str, Any]:
    ans = "Multiples of 3: {3; 6}; P(multiple of 3) = 2/6 = 1/3"
    prompt = (
        "A fair die is rolled. What is the probability of rolling a **multiple of 3**?\n"
        "State the favourable outcomes and simplify your fraction."
    )
    sol = (
        "**Multiples of 3 between 1 and 6:**\n"
        "The multiples are **$3$ and $6$** ($2$ favourable outcomes).\n\n"
        "$$P(\\text{Multiple of 3}) = \\frac{2}{6} = \\frac{1}{3}$$"
    )
    return {
        "id": f"g7_pr_10_{rng.randint(100000, 999999)}",
        "subskill": "10_probability_fair_die_multiples",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Multiples are 3 and 6; P = 2/6 = 1/3",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_10",
        "hints": {
            "tier_1": "Which numbers on a die divide by 3 with no remainder? 3 and 6.",
            "tier_2": "2 out of 6 numbers.",
            "tier_3": "2/6 = 1/3."
        },
        "misconception_tags": ["factor_multiple_confusion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies favourable multiples {3, 6}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates simplified probability = 1/3", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 11. Probability fair die impossible and certain
def arch_11_probability_fair_die_impossible_and_certain(rng: random.Random) -> Dict[str, Any]:
    ans = "1. P(rolling a 7) = 0 (Impossible); 2. P(rolling a number between 1 and 6) = 1 (Certain)"
    prompt = (
        "For a standard fair six-sided die:\n\n"
        "1. What is the probability of rolling a **$7$**? Name the type of event.\n"
        "2. What is the probability of rolling a **number between $1$ and $6$** inclusive? Name the type of event."
    )
    sol = (
        "**1. Rolling a 7:**\n"
        "There is no face with $7$ on a standard die ($n = 0$).\n"
        "$$P(7) = \\frac{0}{6} = 0$$\n"
        "This is an **impossible event**.\n\n"
        "**2. Rolling a number between 1 and 6:**\n"
        "All $6$ faces satisfy this condition ($n = 6$).\n"
        "$$P(1 \\le x \\le 6) = \\frac{6}{6} = 1$$\n"
        "This is a **certain event**."
    )
    return {
        "id": f"g7_pr_11_{rng.randint(100000, 999999)}",
        "subskill": "11_probability_fair_die_impossible_and_certain",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "P(7) = 0 (impossible); P(1 to 6) = 1 (certain)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_11",
        "hints": {
            "tier_1": "Can you ever roll a 7 on a normal die?",
            "tier_2": "Will you always roll between 1 and 6?",
            "tier_3": "P = 0 is impossible; P = 1 is certain."
        },
        "misconception_tags": ["probability_outside_0_to_1_range"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States P = 0 and impossible for rolling a 7", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States P = 1 and certain for 1 to 6", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 12. Probability spinner equal sectors SVG
def arch_12_probability_spinner_equal_sectors_svg(rng: random.Random) -> Dict[str, Any]:
    # Parameterize sectors and target color so diagram and answer vary with seed
    colors_pool = [
        ("#ef4444", "Red"),
        ("#3b82f6", "Blue"),
        ("#10b981", "Green"),
        ("#f59e0b", "Yellow"),
        ("#8b5cf6", "Purple"),
        ("#ec4899", "Pink")
    ]
    chosen = rng.sample(colors_pool, 4)
    sectors = [{"color": c[0], "label": c[1]} for c in chosen]
    target_color = rng.choice(chosen)[1]

    svg = _svg_spinner(sectors)
    ans = "1/4 (or 25% or 0,25)"
    prompt = (
        f"Inspect the 4-sector circular spinner in the diagram, divided into equal quadrants labeled "
        f"{', '.join(c[1] for c in chosen)}:\n\n"
        f"1. What is the total number of equally likely outcomes?\n"
        f"2. What is the probability that the pointer lands on **{target_color}** when spun once?"
    )
    sol = (
        f"**1. Total Outcomes:**\n"
        f"The spinner has $4$ equal sectors, so $n(S) = 4$.\n\n"
        f"**2. Probability of {target_color}:**\n"
        f"There is $1$ {target_color.lower()} sector ($n = 1$):\n"
        f"$$P(\\text{{{target_color}}}) = \\frac{{1}}{{4}} = 0{{,}}25 = 25\\%$$"
    )
    return {
        "id": f"g7_pr_12_{rng.randint(100000, 999999)}",
        "subskill": "12_probability_spinner_equal_sectors_svg",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Total outcomes = 4; P({target_color}) = 1/4 = 25%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_12",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Count how many equal sectors there are.",
            "tier_2": f"1 {target_color.lower()} sector out of 4 total equal sectors.",
            "tier_3": "1/4 or 25%."
        },
        "misconception_tags": ["spinner_sector_count_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies total outcomes = 4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates P({target_color}) = 1/4 (25%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 13. Probability spinner unequal sectors
def arch_13_probability_spinner_unequal_sectors(rng: random.Random) -> Dict[str, Any]:
    ans = "Red = 1/2 (180 deg); Blue = 1/4 (90 deg); Green = 1/4 (90 deg)"
    prompt = (
        "A circular spinner is divided into three unequal sectors:\n"
        "- Red occupies half of the circle ($180^\\circ$).\n"
        "- Blue occupies one quarter of the circle ($90^\\circ$).\n"
        "- Green occupies the remaining quarter of the circle ($90^\\circ$).\n\n"
        "1. What is the probability of the spinner landing on **Red**?\n"
        "2. What is the probability of landing on **Blue**?\n"
        "3. Are all three colors equally likely to occur? Explain."
    )
    sol = (
        "**1. Probability of Red:**\n"
        "$$P(\\text{Red}) = \\frac{180^\\circ}{360^\\circ} = \\frac{1}{2}$$\n\n"
        "**2. Probability of Blue:**\n"
        "$$P(\\text{Blue}) = \\frac{90^\\circ}{360^\\circ} = \\frac{1}{4}$$\n\n"
        "**3. Equally Likely:**\n"
        "No. Red is twice as likely to occur ($1/2 = 2/4$) as Blue or Green ($1/4$). "
        "Outcomes are only equally likely when sectors have equal areas (equal angles)."
    )
    return {
        "id": f"g7_pr_13_{rng.randint(100000, 999999)}",
        "subskill": "13_probability_spinner_unequal_sectors",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "P(Red) = 1/2, P(Blue) = 1/4; not equally likely because sector sizes differ",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pr_13",
        "hints": {
            "tier_1": "Divide each sector angle by 360°.",
            "tier_2": "180/360 = 1/2; 90/360 = 1/4.",
            "tier_3": "Red: 1/2, Blue: 1/4; not equally likely."
        },
        "misconception_tags": ["assuming_all_spinner_sectors_equally_likely"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates P(Red) = 1/2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates P(Blue) = 1/4", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Explains unequal likelihood due to unequal sector sizes", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 14. Probability spinner composite regions
def arch_14_probability_spinner_composite_regions(rng: random.Random) -> Dict[str, Any]:
    # 8-sector spinner: 3 Red, 2 Blue, 2 Green, 1 Yellow
    # P(Red or Blue) = (3 + 2) / 8 = 5/8
    ans = "5/8"
    prompt = (
        "A spinner is divided into $8$ equal sectors:\n"
        "- $3$ sectors are Red\n"
        "- $2$ sectors are Blue\n"
        "- $2$ sectors are Green\n"
        "- $1$ sector is Yellow\n\n"
        "What is the probability of spinning **Red OR Blue** on a single spin?"
    )
    sol = (
        "**Calculation:**\n"
        "Favourable sectors = $3\\text{ (Red)} + 2\\text{ (Blue)} = 5$.\n"
        "Total equal sectors = $8$.\n\n"
        "$$P(\\text{Red or Blue}) = \\frac{3 + 2}{8} = \\frac{5}{8}$$"
    )
    return {
        "id": f"g7_pr_14_{rng.randint(100000, 999999)}",
        "subskill": "14_probability_spinner_composite_regions",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "5/8",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_14",
        "hints": {
            "tier_1": "Add the Red sectors and Blue sectors together.",
            "tier_2": "3 + 2 = 5 favourable sectors out of 8.",
            "tier_3": "5/8."
        },
        "misconception_tags": ["multiplying_instead_of_adding_for_or_events"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Adds favourable sectors 3 + 2 = 5", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Expresses as fraction 5/8", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 15. Probability marbles bag single color
def arch_15_probability_marbles_bag_single_color(rng: random.Random) -> Dict[str, Any]:
    red = rng.choice([3, 4, 5])
    blue = rng.choice([4, 6, 8])
    green = rng.choice([3, 5, 7])
    total = red + blue + green
    g = math.gcd(blue, total)
    s_num, s_den = blue // g, total // g
    ans = f"{s_num}/{s_den}"
    prompt = (
        f"A bag contains {red} red marbles, {blue} blue marbles, and {green} green marbles.\n"
        f"A marble is selected at random from the bag.\n\n"
        f"1. What is the total number of marbles in the bag?\n"
        f"2. Calculate the probability of selecting a **blue marble** as a fully simplified fraction."
    )
    sol = (
        f"**Step 1: Total Marbles:**\n"
        f"$$\\text{{Total}} = {red} + {blue} + {green} = {total}\\text{{ marbles}}$$\n\n"
        f"**Step 2: Probability of Blue:**\n"
        f"$$P(\\text{{Blue}}) = \\frac{{{blue}}}{{{total}}} = \\frac{{{s_num}}}{{{s_den}}}$$"
    )
    return {
        "id": f"g7_pr_15_{rng.randint(100000, 999999)}",
        "subskill": "15_probability_marbles_bag_single_color",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Total = {total}; P(Blue) = {blue}/{total} = {s_num}/{s_den}",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_15",
        "hints": {
            "tier_1": f"Add all marbles: {red} + {blue} + {green} = {total}.",
            "tier_2": f"Fraction is {blue} / {total}.",
            "tier_3": f"Simplified fraction = {s_num}/{s_den}."
        },
        "misconception_tags": ["dividing_favourable_by_remaining_instead_of_total"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates total marbles = {total}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Simplifies probability = {s_num}/{s_den}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


# 16. Probability marbles bag simplified fraction
def arch_16_probability_marbles_bag_simplified_fraction(rng: random.Random) -> Dict[str, Any]:
    # 6 red, 14 black -> total 20; P(red) = 6/20 = 3/10
    red, black = 6, 14
    total = 20
    ans = "3/10"
    prompt = (
        f"A box contains {red} red beads and {black} black beads.\n\n"
        f"Calculate the probability of randomly choosing a red bead, giving your answer as a **fraction in simplest form**."
    )
    sol = (
        f"**Step 1:** Total beads $= {red} + {black} = {total}$.\n\n"
        f"**Step 2:** Fraction of red beads:\n"
        f"$$P(\\text{{Red}}) = \\frac{{{red}}}{{{total}}}$$\n\n"
        f"**Step 3:** Simplify by dividing numerator and denominator by $2$:\n"
        f"$$P(\\text{{Red}}) = \\frac{{{red} \\div 2}}{{{total} \\div 2}} = \\frac{{3}}{{10}}$$"
    )
    return {
        "id": f"g7_pr_16_{rng.randint(100000, 999999)}",
        "subskill": "16_probability_marbles_bag_simplified_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "3/10",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_16",
        "hints": {
            "tier_1": f"Total beads = {total}.",
            "tier_2": f"6 / 20. Divide top and bottom by 2.",
            "tier_3": "3/10."
        },
        "misconception_tags": ["forgetting_to_simplify_probability_fraction"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Sets up 6 / 20", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 3/10", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 17. Probability marbles bag decimal and percentage
def arch_17_probability_marbles_bag_decimal_and_percentage(rng: random.Random) -> Dict[str, Any]:
    # 1 out of 5 -> 1/5 = 0,2 = 20%
    ans = "Fraction: 1/5; Decimal: 0,2; Percentage: 20%"
    prompt = (
        "In a raffle box of $50$ tickets, $10$ are winning tickets.\n\n"
        "Express the probability of selecting a winning ticket in three forms:\n"
        "1. As a simplified common fraction\n"
        "2. As a decimal (using decimal comma)\n"
        "3. As a percentage"
    )
    sol = (
        "**1. Simplified Fraction:**\n"
        "$$P(\\text{Win}) = \\frac{10}{50} = \\frac{1}{5}$$\n\n"
        "**2. Decimal:**\n"
        "$$\\frac{1}{5} = \\frac{2}{10} = 0{,}2$$\n\n"
        "**3. Percentage:**\n"
        "$$0{,}2 \\times 100\\% = 20\\%$$"
    )
    return {
        "id": f"g7_pr_17_{rng.randint(100000, 999999)}",
        "subskill": "17_probability_marbles_bag_decimal_and_percentage",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1/5; 0,2; 20%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pr_17",
        "hints": {
            "tier_1": "10 out of 50 simplifies to 1 out of 5.",
            "tier_2": "1 ÷ 5 = 0,2.",
            "tier_3": "0,2 = 20%."
        },
        "misconception_tags": ["decimal_percentage_conversion_error"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "States simplified fraction 1/5", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States decimal 0,2", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "States percentage 20%", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 18. Probability marbles bag or event
def arch_18_probability_marbles_bag_or_event(rng: random.Random) -> Dict[str, Any]:
    # 5 yellow, 3 red, 2 blue -> total 10. P(yellow or red) = (5+3)/10 = 8/10 = 4/5
    ans = "4/5 (or 8/10 or 80%)"
    prompt = (
        "A cloth bag holds $5$ yellow tokens, $3$ red tokens, and $2$ blue tokens.\n\n"
        "Calculate the probability of selecting a token that is **Yellow OR Red**."
    )
    sol = (
        "**Step 1: Total tokens:**\n"
        "$$5 + 3 + 2 = 10$$\n\n"
        "**Step 2: Favourable tokens:**\n"
        "$$\\text{Yellow or Red} = 5 + 3 = 8$$\n\n"
        "**Step 3: Probability:**\n"
        "$$P(\\text{Yellow or Red}) = \\frac{8}{10} = \\frac{4}{5} = 80\\%$$"
    )
    return {
        "id": f"g7_pr_18_{rng.randint(100000, 999999)}",
        "subskill": "18_probability_marbles_bag_or_event",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "4/5 (or 80%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_18",
        "hints": {
            "tier_1": "Add the yellow (5) and red (3) tokens together.",
            "tier_2": "8 out of 10 tokens.",
            "tier_3": "8/10 = 4/5."
        },
        "misconception_tags": ["multiplying_instead_of_adding_for_or_events"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Adds yellow and red counts 5 + 3 = 8", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates simplified probability = 4/5", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 19. Probability marbles bag complementary not event
def arch_19_probability_marbles_bag_complementary_not_event(rng: random.Random) -> Dict[str, Any]:
    # 4 green, 16 other -> total 20. P(not green) = 1 - 4/20 = 16/20 = 4/5
    ans = "4/5 (or 16/20 or 80%)"
    prompt = (
        "A jar contains $20$ sweets of which $4$ are green and the rest are other flavours.\n\n"
        "1. What is the probability of picking a sweet that is **NOT green**?\n"
        "2. Explain how to calculate this using complementary events: $P(\\text{not } E) = 1 - P(E)$."
    )
    sol = (
        "**1. Complementary Event Rule:**\n"
        "$$P(\\text{Green}) = \\frac{4}{20} = \\frac{1}{5}$$\n\n"
        "$$P(\\text{NOT Green}) = 1 - P(\\text{Green}) = 1 - \\frac{1}{5} = \\frac{4}{5}$$\n\n"
        "**2. Direct Counting Method:**\n"
        "Non-green sweets $= 20 - 4 = 16$.\n"
        "$$P(\\text{NOT Green}) = \\frac{16}{20} = \\frac{4}{5} = 80\\%$$"
    )
    return {
        "id": f"g7_pr_19_{rng.randint(100000, 999999)}",
        "subskill": "19_probability_marbles_bag_complementary_not_event",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "P(not green) = 1 - 4/20 = 16/20 = 4/5",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_19",
        "hints": {
            "tier_1": "How many sweets are NOT green? 20 - 4 = 16.",
            "tier_2": "Fraction is 16/20. Simplify.",
            "tier_3": "4/5."
        },
        "misconception_tags": ["complementary_event_subtraction_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses 1 - P(green) or 16/20", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 4/5", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 20. Probability buttons colored proportions
def arch_20_probability_buttons_colored_proportions(rng: random.Random) -> Dict[str, Any]:
    # 15 white buttons, 10 brown buttons, 25 black buttons -> total 50
    # P(black) = 25/50 = 1/2 = 50%
    ans = "1/2 (or 50%)"
    prompt = (
        "A sewing tin contains $15$ white buttons, $10$ brown buttons, and $25$ black buttons.\n\n"
        "What is the probability that a tailor randomly picks a **black button**?"
    )
    sol = (
        "**Calculation:**\n"
        "Total buttons $= 15 + 10 + 25 = 50$.\n"
        "Black buttons $= 25$.\n\n"
        "$$P(\\text{Black}) = \\frac{25}{50} = \\frac{1}{2} = 50\\%$$"
    )
    return {
        "id": f"g7_pr_20_{rng.randint(100000, 999999)}",
        "subskill": "20_probability_buttons_colored_proportions",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1/2 (or 50%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_20",
        "hints": {
            "tier_1": "Total buttons = 15 + 10 + 25 = 50.",
            "tier_2": "25 out of 50.",
            "tier_3": "25/50 = 1/2 (50%)."
        },
        "misconception_tags": ["arithmetic_addition_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates total = 50", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates simplified probability = 1/2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 21. Probability cards red or black color
def arch_21_probability_cards_red_or_black_color(rng: random.Random) -> Dict[str, Any]:
    ans = "26/52 = 1/2 (or 50%)"
    prompt = (
        "A standard deck of playing cards contains $52$ cards divided equally into red and black suits.\n\n"
        "What is the probability of selecting a **Red card** at random from a shuffled deck?"
    )
    sol = (
        "**Analysis of Standard Deck:**\n"
        "Total cards $= 52$.\n"
        "Red cards (Hearts and Diamonds) $= 13 + 13 = 26$.\n\n"
        "$$P(\\text{Red}) = \\frac{26}{52} = \\frac{1}{2} = 50\\%$$"
    )
    return {
        "id": f"g7_pr_21_{rng.randint(100000, 999999)}",
        "subskill": "21_probability_cards_red_or_black_color",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "26/52 = 1/2 = 50%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_21",
        "hints": {
            "tier_1": "Half the cards are red and half are black.",
            "tier_2": "26 red cards out of 52.",
            "tier_3": "1/2 or 50%."
        },
        "misconception_tags": ["wrong_deck_card_count"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 26 red cards out of 52", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 1/2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 22. Probability cards specific suit
def arch_22_probability_cards_specific_suit(rng: random.Random) -> Dict[str, Any]:
    suit = rng.choice(["Hearts", "Diamonds", "Clubs", "Spades"])
    ans = "13/52 = 1/4 (or 25%)"
    prompt = (
        f"A standard deck contains $52$ cards divided into $4$ suits (Hearts, Diamonds, Clubs, Spades).\n\n"
        f"What is the probability of randomly selecting a card of the **{suit}** suit?"
    )
    sol = (
        f"**Calculation:**\n"
        f"Each suit contains $13$ cards.\n"
        f"$$P(\\text{{{suit}}}) = \\frac{{13}}{{52}} = \\frac{{1}}{{4}} = 25\\%$$"
    )
    return {
        "id": f"g7_pr_22_{rng.randint(100000, 999999)}",
        "subskill": "22_probability_cards_specific_suit",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1/4 (or 25%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_22",
        "hints": {
            "tier_1": "There are 4 equal suits in a deck.",
            "tier_2": f"13 {suit} cards out of 52.",
            "tier_3": "13/52 = 1/4."
        },
        "misconception_tags": ["wrong_suit_card_count"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States 13 cards in suit", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 1/4", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 23. Probability cards ace or face card
def arch_23_probability_cards_ace_or_face_card(rng: random.Random) -> Dict[str, Any]:
    card_type = rng.choice(["an Ace", "a Face Card (Jack, Queen, or King)"])
    if "Ace" in card_type:
        count = 4
        ans = "4/52 = 1/13"
    else:
        count = 12  # 3 in each of 4 suits
        ans = "12/52 = 3/13"
    prompt = (
        f"From a standard deck of $52$ playing cards, what is the probability of selecting **{card_type}**?\n"
        f"Provide your answer as a simplified fraction."
    )
    sol = (
        f"**Calculation:**\n"
        f"Count of {card_type}s in deck $= {count}$.\n"
        f"Total cards $= 52$.\n\n"
        f"$$P = \\frac{{{count}}}{{52}} = {ans}$$"
    )
    return {
        "id": f"g7_pr_23_{rng.randint(100000, 999999)}",
        "subskill": "23_probability_cards_ace_or_face_card",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_23",
        "hints": {
            "tier_1": f"How many {card_type}s exist in the entire deck of 52 cards?",
            "tier_2": f"Favourable count = {count}. Divide by 52.",
            "tier_3": f"{ans}."
        },
        "misconception_tags": ["face_card_count_confusion"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Identifies {count} favourable cards", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Simplifies to {ans}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 24. Probability cards number card
def arch_24_probability_cards_number_card(rng: random.Random) -> Dict[str, Any]:
    # Number cards 2 to 10 (9 cards per suit * 4 suits = 36 number cards)
    # P(number card) = 36/52 = 9/13
    ans = "36/52 = 9/13"
    prompt = (
        "In a 52-card deck, cards numbered $2, 3, 4, 5, 6, 7, 8, 9, 10$ in all 4 suits are called number cards.\n\n"
        "Calculate the probability of selecting a **number card** at random."
    )
    sol = (
        "**Calculation:**\n"
        "Number of cards per suit $= 9$ (from $2$ to $10$).\n"
        "Total number cards across $4$ suits $= 9 \\times 4 = 36$.\n\n"
        "$$P(\\text{Number Card}) = \\frac{36}{52} = \\frac{9}{13}$$"
    )
    return {
        "id": f"g7_pr_24_{rng.randint(100000, 999999)}",
        "subskill": "24_probability_cards_number_card",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "9/13",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_24",
        "hints": {
            "tier_1": "There are 9 number cards in each of the 4 suits: 9 × 4 = 36.",
            "tier_2": "Fraction: 36 / 52.",
            "tier_3": "Simplifies to 9/13."
        },
        "misconception_tags": ["counting_ace_as_number_card"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates 36 number cards", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 9/13", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 25. Probability letter tiles word vowels
def arch_25_probability_letter_tiles_word_vowels(rng: random.Random) -> Dict[str, Any]:
    # Word: "PROBABILITY" -> 11 letters
    # Vowels: O, A, I, I (4 vowels)
    # P(vowel) = 4/11
    ans = "4/11"
    prompt = (
        "The individual letter tiles spelling the word **P R O B A B I L I T Y** are placed in a bag.\n"
        "One letter tile is selected at random.\n\n"
        "1. How many total letter tiles are in the word?\n"
        "2. List all the vowels in the word.\n"
        "3. Calculate the probability of selecting a **vowel**."
    )
    sol = (
        "**1. Total Letters:**\n"
        "There are $11$ letters in PROBABILITY ($n(S) = 11$).\n\n"
        "**2. Vowels:**\n"
        "The vowels are **O, A, I, I** ($4$ vowels).\n\n"
        "**3. Probability:**\n"
        "$$P(\\text{Vowel}) = \\frac{4}{11}$$"
    )
    return {
        "id": f"g7_pr_25_{rng.randint(100000, 999999)}",
        "subskill": "25_probability_letter_tiles_word_vowels",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Total = 11; Vowels are O, A, I, I (4 vowels); P = 4/11",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pr_25",
        "hints": {
            "tier_1": "Count total letters: P-R-O-B-A-B-I-L-I-T-Y = 11.",
            "tier_2": "Vowels: O, A, I, I (both Is count!).",
            "tier_3": "4/11."
        },
        "misconception_tags": ["counting_repeated_letter_only_once"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Counts 11 total letters", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Identifies 4 vowels (including repeated I)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Calculates probability = 4/11", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
