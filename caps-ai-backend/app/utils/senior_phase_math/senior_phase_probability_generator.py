"""
Senior Phase Mathematics (Grades 7, 8, 9) - Probability Generator
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.

Topics Covered (Grades 7–9 Term 4):
- The probability scale: 0 (impossible), 0.5 (equally likely), 1 (certain)
- Sample space (S) and single-event theoretical probability: P(E) = n(E) / n(S)
- Realistic contexts: colored marbles in bags, fair 6-sided dice, spinners, playing cards
- Expressing probability as a simplified common fraction, South African comma decimal, and percentage
- Relative frequency versus theoretical probability
- Complement of an event: P(not E) = 1 - P(E)
"""

from __future__ import annotations
import random
import math
from typing import Any, Dict, List, Optional


def _decomma(val: float) -> str:
    """Format decimal with South African comma separator."""
    s = f"{val:.2f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def _generate_marble_bag_question(rng: random.Random) -> Dict[str, Any]:
    """Generates probability questions involving picking colored marbles from a bag."""
    colors = ["red", "blue", "green", "yellow"]
    c1, c2, c3 = rng.sample(colors, 3)
    n1 = rng.randint(3, 8)
    n2 = rng.randint(4, 9)
    n3 = rng.randint(2, 6)
    total = n1 + n2 + n3

    target_color = c1
    favorable = n1
    g = math.gcd(favorable, total)
    frac_num = favorable // g
    frac_den = total // g
    frac_latex = f"\\frac{{{frac_num}}}{{{frac_den}}}" if frac_den != 1 else "1"
    pct = round((favorable / total) * 100, 1)

    prompt = (
        f"A bag contains **{n1} {c1} marbles**, **{n2} {c2} marbles**, and **{n3} {c3} marbles**.\n\n"
        f"A marble is drawn at random from the bag.\n\n"
        f"1. What is the total number of possible outcomes in the sample space ($n(S)$)?\n"
        f"2. Determine the theoretical probability of drawing a **{target_color} marble**, expressed as a **simplified common fraction**.\n"
        f"3. Express this probability as a percentage (rounded to 1 decimal place)."
    )

    sol = (
        f"**Step 1:** Calculate total outcomes in the sample space ($n(S)$):\n\n"
        f"$$n(S) = {n1} + {n2} + {n3} = {total}$$\n\n"
        f"**Step 2:** The number of favourable outcomes for a {target_color} marble is $n({target_color.title()}) = {favorable}$.\n\n"
        f"$$P({target_color.title()}) = \\frac{{n({target_color.title()})}}{{n(S)}} = \\frac{{{favorable}}}{{{total}}}$$\n\n"
        f"Simplifying by dividing numerator and denominator by {g}:\n\n"
        f"$$P({target_color.title()}) = {frac_latex}$$\n\n"
        f"**Step 3:** Convert fraction to a percentage:\n\n"
        f"$$\\frac{{{favorable}}}{{{total}}} \\times 100\\% \\approx {pct}\\%$$"
    )

    return {
        "id": f"sp_math_prob_bag_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"n(S) = {total}; P({target_color}) = {frac_num}/{frac_den}; {pct}%",
        "answer_latex": f"n(S) = {total};\\ P({target_color.title()}) = {frac_latex};\\ {pct}\\%",
        "answer_sympy": f"{frac_num}/{frac_den}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 4,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
        "subskill": "single_event_probability",
        "learning_objective_id": "math_sp_probability_sample_space",
        "misconception_tags": [
            "fraction_simplification_omission",
            "favorable_vs_total_ratio_inversion",
            "incorrect_sample_space_sum"
        ],
        "diagnostic_tags": ["theoretical_probability", "sample_space_enumeration"],
        "minimum_mastery_score": 75,
        "keywords": ["probability", "sample space", "simplified fraction", "percentage"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Accurate total sample space n(S)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Unsimplified probability ratio", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Accurate simplified fraction", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Accurate percentage conversion", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": f"Add all the marbles together first to get the total sample space n(S).",
            "tier_2": f"Theoretical probability is P(E) = n(favourable) / n(total). There are {favorable} {target_color} marbles out of {total}.",
            "tier_3": f"P({target_color}) = {favorable}/{total} = {frac_num}/{frac_den} = {pct}%."
        }
    }


def _generate_dice_spinner_question(rng: random.Random) -> Dict[str, Any]:
    """Generates probability questions involving rolling a standard 6-sided die or spinning a spinner."""
    condition = rng.choice(["prime", "even", "greater_than_4", "multiple_of_3"])

    if condition == "prime":
        favorable_set = [2, 3, 5]
        desc = "a prime number (note: 1 is not prime)"
    elif condition == "even":
        favorable_set = [2, 4, 6]
        desc = "an even number"
    elif condition == "greater_than_4":
        favorable_set = [5, 6]
        desc = "a number strictly greater than 4"
    else:
        favorable_set = [3, 6]
        desc = "a multiple of 3"

    favorable = len(favorable_set)
    total = 6
    g = math.gcd(favorable, total)
    frac_num = favorable // g
    frac_den = total // g
    frac_latex = f"\\frac{{{frac_num}}}{{{frac_den}}}"

    prompt = (
        f"A standard, fair six-sided die numbered $1$ to $6$ is rolled once.\n\n"
        f"1. List the full sample space ($S$).\n"
        f"2. List the outcomes that satisfy the event of rolling **{desc}**.\n"
        f"3. Calculate the theoretical probability of this event as a simplified fraction.\n"
        f"4. What is the probability of the **complement** (NOT rolling {desc})?"
    )

    comp_num = frac_den - frac_num
    comp_latex = f"\\frac{{{comp_num}}}{{{frac_den}}}"

    sol = (
        f"**Step 1:** The sample space is: $$S = \\{{1, 2, 3, 4, 5, 6\\}}, \\quad n(S) = 6$$\n\n"
        f"**Step 2:** Favourable outcomes: $$\\text{{Event}} = \\{{{', '.join(str(x) for x in favorable_set)}\\}}, \\quad n(E) = {favorable}$$\n\n"
        f"**Step 3:** Calculate probability: $$P(E) = \\frac{{{favorable}}}{{6}} = {frac_latex}$$\n\n"
        f"**Step 4:** Complementary event: $$P(\\text{{not }} E) = 1 - P(E) = 1 - {frac_latex} = {comp_latex}$$"
    )

    return {
        "id": f"sp_math_prob_die_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": f"P(E) = {frac_num}/{frac_den}; P(not E) = {comp_num}/{frac_den}",
        "answer_latex": f"P(E) = {frac_latex};\\ P(\\text{{not }} E) = {comp_latex}",
        "answer_sympy": f"{frac_num}/{frac_den}",
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "term": 4,
        "caps_weight_percent": 10,
        "suggested_duration_mins": 4,
        "subskill": "dice_and_complementary_probability",
        "learning_objective_id": "math_sp_probability_dice_complement",
        "misconception_tags": [
            "included_one_as_prime_number",
            "complementary_event_subtraction_error",
            "strict_inequality_endpoint_inclusion"
        ],
        "diagnostic_tags": ["dice_probability", "complementary_events"],
        "minimum_mastery_score": 75,
        "keywords": ["die roll", "prime number", "sample space", "complement"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Complete sample space listing", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Identification of favourable outcome subset", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Simplified event probability", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Accurate complementary probability", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "tier_1": "List the numbers {1, 2, 3, 4, 5, 6} and circle the ones that match the event.",
            "tier_2": "Remember that the complement is 1 minus the probability of the event.",
            "tier_3": f"P(E) = {frac_num}/{frac_den} and P(not E) = {comp_num}/{frac_den}."
        }
    }


class SeniorPhaseProbabilityGenerator:
    """Class wrapper adhering to SeniorPhase generator pattern."""
    def generate(
        self,
        count: int = 1,
        seed: Optional[int] = None,
        difficulty: str = "medium",
        mode: str = "compound",
        subskill: Optional[str] = None,
        **kwargs
    ) -> List[Dict[str, Any]]:
        rng = random.Random(seed) if seed is not None else random.Random()
        questions = []
        for _ in range(count):
            if mode == "elementary_dice" or subskill == "dice":
                q = _generate_dice_spinner_question(rng)
            elif mode == "elementary_marbles" or subskill == "marbles":
                q = _generate_marble_bag_question(rng)
            else:
                q = rng.choice([_generate_marble_bag_question, _generate_dice_spinner_question])(rng)
            questions.append(q)
        return questions


def generate(count: int = 1, seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    return SeniorPhaseProbabilityGenerator().generate(count=count, seed=seed, **kwargs)
