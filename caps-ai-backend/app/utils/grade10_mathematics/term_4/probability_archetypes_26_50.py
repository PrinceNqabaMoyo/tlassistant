"""Grade 10 Mathematics — Term 4: Probability Archetypes 26 to 50.
100% aligned with South African CAPS Curriculum (Grade 10 Mathematics: Probability).
Covers:
- Two-stage sample space grids (two dice sums and differences)
- Tree diagrams: fair coin tosses, marbles with and without replacement, weather/sports sequences
- Joint probabilities along tree branches (both same, at least one)
- Venn diagrams with visual region shading/identification (union, intersection, A only, neither, exactly one)
- Algebraic probability ratios
- Compound events with standard 52-card deck
- Experimental bias vs fairness simulations
- Probability conversions (fractions, decimals, percentages)
- Odds vs probability
- Comprehensive multi-part exam synthesis
"""
from __future__ import annotations

from fractions import Fraction
import random
from typing import Any, Dict, List, Optional, Tuple

TOPIC = "Probability"
TOPIC_ID = "grade10_math_probability"
LO = "math10_probability_venn"


def _fmt_frac(f: Fraction) -> str:
    """Format Fraction as KaTeX fraction or integer."""
    if f.denominator == 1:
        return str(f.numerator)
    return rf"\frac{{{f.numerator}}}{{{f.denominator}}}"


def _fmt_dec(val: float | int, places: int = 2) -> str:
    """Format number with South African comma decimal."""
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    s = f"{val:.{places}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _fmt_katex(val: float | int, places: int = 2) -> str:
    """Format number for KaTeX with {{,}} separator."""
    dec = _fmt_dec(val, places)
    return dec.replace(",", "{,}")


def _make_shaded_venn_svg(
    n_a_only: int,
    n_inter: int,
    n_b_only: int,
    n_neither: int,
    label_a: str = "A",
    label_b: str = "B",
    highlight: str = "none",
    title: str = "Venn Diagram",
) -> str:
    """Generates an SVG Venn diagram with optional region shading."""
    # Shading styles
    c_a_fill = "#BEE3F8" if highlight in ("union", "a_only", "exactly_one") else "#EDF2F7"
    c_b_fill = "#C6F6D5" if highlight in ("union", "b_only", "exactly_one") else "#EDF2F7"
    box_fill = "#FEFCBF" if highlight == "neither" else "#F7FAFC"
    inter_fill = "#FEB2B2" if highlight in ("union", "intersection") else "none"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 220" width="100%" height="auto" style="background:#FFFFFF; font-family:sans-serif;">
    <text x="250" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1A202C">{title}</text>
    <!-- Sample Space Box -->
    <rect x="40" y="30" width="420" height="175" rx="8" fill="{box_fill}" stroke="#4A5568" stroke-width="2"/>
    <text x="55" y="52" font-size="14" font-weight="bold" fill="#2D3748">S</text>
    <!-- Circle A -->
    <circle cx="190" cy="120" r="65" fill="{c_a_fill}" fill-opacity="0.5" stroke="#2B6CB0" stroke-width="2.5"/>
    <text x="155" y="60" text-anchor="middle" font-size="13" font-weight="bold" fill="#2B6CB0">{label_a}</text>
    <!-- Circle B -->
    <circle cx="290" cy="120" r="65" fill="{c_b_fill}" fill-opacity="0.5" stroke="#2F855A" stroke-width="2.5"/>
    <text x="325" y="60" text-anchor="middle" font-size="13" font-weight="bold" fill="#2F855A">{label_b}</text>
    <!-- Counts -->
    <text x="155" y="125" text-anchor="middle" font-size="14" font-weight="bold" fill="#1A202C">{n_a_only}</text>
    <text x="240" y="125" text-anchor="middle" font-size="14" font-weight="bold" fill="#C53030">{n_inter}</text>
    <text x="325" y="125" text-anchor="middle" font-size="14" font-weight="bold" fill="#1A202C">{n_b_only}</text>
    <text x="80" y="185" text-anchor="middle" font-size="13" font-weight="bold" fill="#4A5568">{n_neither}</text>
</svg>"""
    return svg


def _make_tree_diagram_svg(
    b1_label: str,
    b1_prob: str,
    b2_label: str,
    b2_prob: str,
    sub_probs: List[Tuple[str, str, str]],  # (branch_label, prob_str, outcome_str)
    title: str = "Tree Diagram",
) -> str:
    """Generates an SVG Tree Diagram for a two-stage experiment."""
    # sub_probs has 4 tuples: [ (label_top_top, prob, outcome), (label_top_bot, prob, outcome), (label_bot_top, prob, outcome), (label_bot_bot, prob, outcome) ]
    s0 = sub_probs[0]
    s1 = sub_probs[1]
    s2 = sub_probs[2]
    s3 = sub_probs[3]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" style="background:#FFFFFF; font-family:sans-serif;">
    <text x="260" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1A202C">{title}</text>
    <!-- Stage 1 Branches -->
    <line x1="50" y1="110" x2="180" y2="60" stroke="#2B6CB0" stroke-width="2.5"/>
    <line x1="50" y1="110" x2="180" y2="160" stroke="#2F855A" stroke-width="2.5"/>
    <!-- Stage 1 Labels & Probs -->
    <text x="110" y="75" font-size="11" font-weight="bold" fill="#2B6CB0">{b1_prob}</text>
    <text x="195" y="65" font-size="12" font-weight="bold" fill="#2B6CB0">{b1_label}</text>
    <text x="110" y="150" font-size="11" font-weight="bold" fill="#2F855A">{b2_prob}</text>
    <text x="195" y="165" font-size="12" font-weight="bold" fill="#2F855A">{b2_label}</text>
    <!-- Stage 2 Branches Top -->
    <line x1="210" y1="60" x2="340" y2="35" stroke="#2B6CB0" stroke-width="2"/>
    <line x1="210" y1="60" x2="340" y2="85" stroke="#2B6CB0" stroke-width="2"/>
    <text x="270" y="42" font-size="10" fill="#4A5568">{s0[1]}</text>
    <text x="350" y="38" font-size="11" font-weight="bold" fill="#1A202C">{s0[0]} -> {s0[2]}</text>
    <text x="270" y="80" font-size="10" fill="#4A5568">{s1[1]}</text>
    <text x="350" y="88" font-size="11" font-weight="bold" fill="#1A202C">{s1[0]} -> {s1[2]}</text>
    <!-- Stage 2 Branches Bottom -->
    <line x1="210" y1="160" x2="340" y2="135" stroke="#2F855A" stroke-width="2"/>
    <line x1="210" y1="160" x2="340" y2="185" stroke="#2F855A" stroke-width="2"/>
    <text x="270" y="142" font-size="10" fill="#4A5568">{s2[1]}</text>
    <text x="350" y="138" font-size="11" font-weight="bold" fill="#1A202C">{s2[0]} -> {s2[2]}</text>
    <text x="270" y="180" font-size="10" fill="#4A5568">{s3[1]}</text>
    <text x="350" y="188" font-size="11" font-weight="bold" fill="#1A202C">{s3[0]} -> {s3[2]}</text>
</svg>"""
    return svg


# -----------------------------------------------------------------------------
# 26. Two-stage sample space grid two dice
# -----------------------------------------------------------------------------
def arch_26_two_stage_sample_space_grid_two_dice(rng: random.Random) -> Dict[str, Any]:
    target_sum = rng.choice([7, 8, 9, 10])
    pairs = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7) if d1 + d2 == target_sum]
    n_favour = len(pairs)
    p_sum = Fraction(n_favour, 36)
    pairs_str = ", ".join(f"({a}, {b})" for a, b in pairs)

    prompt = (
        "Two fair six-sided dice are rolled simultaneously. A 6x6 grid can represent all 36 equally likely outcomes.\n\n"
        f"1. State the total number of outcomes in the sample space, $n(S)$.\n"
        f"2. List all the outcome pairs $(d_1, d_2)$ whose sum equals {target_sum}.\n"
        f"3. Calculate the probability of rolling a sum equal to {target_sum}, as a simplified fraction."
    )

    worked = (
        "**1. Sample Space:**\n"
        "$$n(S) = 6 \\times 6 = 36$$\n\n"
        f"**2. Outcomes with sum {target_sum}:**\n"
        f"$$\\{{{pairs_str}\\}}$$\n"
        f"There are {n_favour} favourable outcomes.\n\n"
        f"**3. Probability:**\n"
        f"$$P(\\text{{Sum}} = {target_sum}) = \\frac{{{n_favour}}}{{36}} = {_fmt_frac(p_sum)}$$"
    )

    ans = f"n(S)=36, P(Sum={target_sum})={_fmt_frac(p_sum)}"

    return {
        "id": f"g10_prob_26_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "26_two_stage_sample_space_grid_two_dice",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Total outcomes n(S) = 36", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct list of pairs with sum {target_sum}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct probability ({_fmt_frac(p_sum)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "There are 6 * 6 = 36 total outcomes. Find all pairs of dice numbers that add up to the target sum.",
            "2_concept": "P(E) = n(favourable) / 36.",
            "3_breakdown": f"Pairs with sum {target_sum}: {pairs_str}. Probability = {n_favour}/36 = {_fmt_frac(p_sum)}.",
        },
        "misconception_tags": ["two_dice_sample_space_size_error"],
    }


# -----------------------------------------------------------------------------
# 27. Tree diagram two coin tosses
# -----------------------------------------------------------------------------
def arch_27_tree_diagram_two_coin_tosses(rng: random.Random) -> Dict[str, Any]:
    target_face = rng.choice(["heads", "tails"])
    target_letter = "H" if target_face == "heads" else "T"
    pair_str = target_letter + target_letter
    trial_id = rng.randint(10, 99)

    sub_probs = [
        ("H", "1/2", "HH (1/4)"),
        ("T", "1/2", "HT (1/4)"),
        ("H", "1/2", "TH (1/4)"),
        ("T", "1/2", "TT (1/4)"),
    ]
    svg = _make_tree_diagram_svg("H", "1/2", "T", "1/2", sub_probs, title=f"Two Coin Tosses Tree Diagram (Trial {trial_id})")

    p_both = Fraction(1, 4)
    p_at_least_one = Fraction(3, 4)

    prompt = (
        "A fair coin is tossed twice. A tree diagram represents the two-stage experiment:\n\n"
        "The first toss branches into H and T with probabilities 1/2 each, and each subsequent toss branches into H and T.\n\n"
        "1. List the four outcomes in the sample space $S$.\n"
        f"2. Calculate the probability of getting TWO {target_face.upper()} (${pair_str}$).\n"
        f"3. Calculate the probability of getting AT LEAST ONE {target_face[:-1]}."
    )

    worked = (
        "**1. Sample Space:**\n"
        "$$S = \\{HH, HT, TH, TT\\}$$\n"
        "Each outcome has probability $\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$.\n\n"
        f"**2. Probability of Two {target_face.capitalize()} (${pair_str}$):**\n"
        f"$$P({pair_str}) = \\frac{{1}}{{2}} \\times \\frac{{1}}{{2}} = \\frac{{1}}{{4}}$$\n\n"
        f"**3. At least one {target_face[:-1]}:**\n"
        f"$$P(\\text{{At least one }} {target_letter}) = 1 - \\frac{{1}}{{4}} = \\frac{{3}}{{4}}$$"
    )

    ans = f"P({pair_str}) = 1/4, P(at least one {target_letter}) = 3/4"

    return {
        "id": f"g10_prob_27_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": r"P(HH) = \frac{1}{4}, \quad P(\text{at least one } H) = \frac{3}{4}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "27_tree_diagram_two_coin_tosses",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Listing 4 outcomes in sample space", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "P(HH) = 1/4", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "P(at least one H) = 3/4", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Multiply branch probabilities to find outcome probabilities.",
            "2_concept": "At least one Head is the complement of No Heads (TT).",
            "3_breakdown": "P(HH) = 1/4. P(at least one H) = 1 - P(TT) = 1 - 1/4 = 3/4.",
        },
        "misconception_tags": ["at_least_one_head_interpretation_error"],
    }


# -----------------------------------------------------------------------------
# 28. Tree diagram coin and die
# -----------------------------------------------------------------------------
def arch_28_tree_diagram_coin_and_die(rng: random.Random) -> Dict[str, Any]:
    coin_face = rng.choice(["Head", "Tail"])
    p_even = Fraction(3, 6)
    p_face = Fraction(1, 2)
    p_combined = p_face * p_even  # 1/4

    prompt = (
        f"A fair coin is tossed and a fair six-sided die is rolled.\n\n"
        f"1. State the total number of possible outcomes in this two-stage experiment.\n"
        f"2. Calculate the probability of getting a **{coin_face} and an even number**.\n"
        f"3. Are the outcome of the coin toss and the outcome of the die roll independent? Explain."
    )

    worked = (
        "**1. Total Outcomes:**\n"
        "$$n(S) = 2 \\times 6 = 12$$\n\n"
        f"**2. Probability:**\n"
        f"$$P(\\text{{{coin_face}}} \\cap \\text{{Even}}) = P(\\text{{{coin_face}}}) \\times P(\\text{{Even}}) = \\frac{{1}}{{2}} \\times \\frac{{3}}{{6}} = {_fmt_frac(p_combined)}$$\n\n"
        "**3. Independence:**\n"
        "Yes, the coin toss does not affect the outcome of rolling the die."
    )

    ans = f"n(S)=12, P={_fmt_frac(p_combined)}, Independent"

    return {
        "id": f"g10_prob_28_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "28_tree_diagram_coin_and_die",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Total outcomes n(S) = 12", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Probability calculation ({_fmt_frac(p_combined)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Statement of independence with valid reason", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Multiply the probability of the coin result by the probability of the die result.",
            "2_concept": "For independent events, P(A and B) = P(A) * P(B).",
            "3_breakdown": f"Total = 12. P({coin_face} and Even) = (1/2) * (3/6) = {_fmt_frac(p_combined)}.",
        },
        "misconception_tags": ["independent_events_multiplication_rule"],
    }


# -----------------------------------------------------------------------------
# 29. Tree diagram marbles with replacement
# -----------------------------------------------------------------------------
def arch_29_tree_diagram_marbles_with_replacement(rng: random.Random) -> Dict[str, Any]:
    n_red = rng.randint(3, 5)
    n_blue = rng.randint(4, 6)
    total = n_red + n_blue

    p_r = Fraction(n_red, total)
    p_b = Fraction(n_blue, total)
    p_rr = p_r * p_r

    sub_probs = [
        ("R", str(p_r), f"RR ({p_rr})"),
        ("B", str(p_b), f"RB ({p_r * p_b})"),
        ("R", str(p_r), f"BR ({p_b * p_r})"),
        ("B", str(p_b), f"BB ({p_b * p_b})"),
    ]
    svg = _make_tree_diagram_svg("Red", str(p_r), "Blue", str(p_b), sub_probs, title="Draws With Replacement")

    prompt = (
        f"A bag contains {n_red} red marbles and {n_blue} blue marbles (total of {total} marbles). "
        f"A marble is drawn at random, its colour is noted, and it is **replaced** before a second marble is drawn.\n\n"
        f"1. State the probability of drawing a red marble on the second draw.\n"
        f"2. Calculate the probability of drawing TWO red marbles ($RR$).\n"
        f"3. Explain why the probabilities on the second stage branches are identical to those on the first stage."
    )

    worked = (
        f"Total marbles = {total}.\n\n"
        f"**1. Second draw probability:**\n"
        f"Because the marble is replaced, the bag still has {n_red} red out of {total}:\n"
        f"$$P(R_2) = \\frac{{{n_red}}}{{{total}}} = {_fmt_frac(p_r)}$$\n\n"
        f"**2. Probability of $RR$:**\n"
        f"$$P(RR) = P(R) \\times P(R) = {_fmt_frac(p_r)} \\times {_fmt_frac(p_r)} = {_fmt_frac(p_rr)}$$\n\n"
        f"**3. Reason:**\n"
        f"The draws are **independent** because replacing the marble restores the composition of the bag."
    )

    ans = f"P(R2)={_fmt_frac(p_r)}, P(RR)={_fmt_frac(p_rr)}, Independent"

    return {
        "id": f"g10_prob_29_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "29_tree_diagram_marbles_with_replacement",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct second draw probability ({_fmt_frac(p_r)})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct joint probability P(RR) ({_fmt_frac(p_rr)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Explanation referencing replacement and independence", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "With replacement means the bag stays exactly the same for the second draw.",
            "2_concept": "Draws with replacement are independent events.",
            "3_breakdown": f"P(RR) = ({n_red}/{total}) * ({n_red}/{total}) = {_fmt_frac(p_rr)}.",
        },
        "misconception_tags": ["with_replacement_denominator_reduction"],
    }


# -----------------------------------------------------------------------------
# 30. Tree diagram marbles without replacement
# -----------------------------------------------------------------------------
def arch_30_tree_diagram_marbles_without_replacement(rng: random.Random) -> Dict[str, Any]:
    n_red = rng.randint(4, 6)
    n_blue = rng.randint(3, 5)
    total = n_red + n_blue

    p_r1 = Fraction(n_red, total)
    p_b1 = Fraction(n_blue, total)
    # Stage 2 after Red:
    p_r2_given_r1 = Fraction(n_red - 1, total - 1)
    p_b2_given_r1 = Fraction(n_blue, total - 1)
    # Stage 2 after Blue:
    p_r2_given_b1 = Fraction(n_red, total - 1)
    p_b2_given_b1 = Fraction(n_blue - 1, total - 1)

    p_rr = p_r1 * p_r2_given_r1

    sub_probs = [
        ("R", str(p_r2_given_r1), f"RR ({p_rr})"),
        ("B", str(p_b2_given_r1), f"RB ({p_r1 * p_b2_given_r1})"),
        ("R", str(p_r2_given_b1), f"BR ({p_b1 * p_r2_given_b1})"),
        ("B", str(p_b2_given_b1), f"BB ({p_b1 * p_b2_given_b1})"),
    ]
    svg = _make_tree_diagram_svg("Red", str(p_r1), "Blue", str(p_b1), sub_probs, title="Draws Without Replacement")

    prompt = (
        f"A bag contains {n_red} red marbles and {n_blue} blue marbles (total of {total} marbles). "
        f"Two marbles are drawn at random **without replacement**.\n\n"
        f"1. What is the total number of marbles remaining in the bag for the second draw?\n"
        f"2. Calculate the probability that the second marble is red, GIVEN that the first marble was red.\n"
        f"3. Calculate the probability of drawing TWO red marbles ($RR$)."
    )

    worked = (
        f"**1. Remaining marbles:** {total} $- 1 = {total - 1}$ marbles.\n\n"
        f"**2. Second draw red given first was red:**\n"
        f"There are now {n_red - 1} red marbles remaining out of {total - 1}:\n"
        f"$$P(R_2 \\mid R_1) = \\frac{{{n_red - 1}}}{{{total - 1}}} = {_fmt_frac(p_r2_given_r1)}$$\n\n"
        f"**3. Joint Probability $P(RR)$:**\n"
        f"$$P(RR) = P(R_1) \\times P(R_2 \\mid R_1) = \\frac{{{n_red}}}{{{total}}} \\times \\frac{{{n_red - 1}}}{{{total - 1}}} = {_fmt_frac(p_rr)}$$"
    )

    ans = f"Remaining={total - 1}, P(R2|R1)={_fmt_frac(p_r2_given_r1)}, P(RR)={_fmt_frac(p_rr)}"

    return {
        "id": f"g10_prob_30_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "30_tree_diagram_marbles_without_replacement",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "hard",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct remaining count ({total - 1})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Conditional branch probability ({_fmt_frac(p_r2_given_r1)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Joint probability P(RR) = {_fmt_frac(p_rr)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Without replacement means both the numerator and denominator decrease by 1 for the second red marble.",
            "2_concept": "P(RR) = (red/total) * ((red - 1)/(total - 1)).",
            "3_breakdown": f"P(RR) = ({n_red}/{total}) * ({n_red - 1}/{total - 1}) = {_fmt_frac(p_rr)}.",
        },
        "misconception_tags": ["without_replacement_static_denominator_error"],
    }


# -----------------------------------------------------------------------------
# 31. Tree diagram both same outcome
# -----------------------------------------------------------------------------
def arch_31_tree_diagram_both_same_outcome(rng: random.Random) -> Dict[str, Any]:
    n_w = rng.randint(3, 5)
    n_b = rng.randint(4, 6)
    total = n_w + n_b

    p_w = Fraction(n_w, total)
    p_b = Fraction(n_b, total)
    p_same = (p_w * p_w) + (p_b * p_b)

    prompt = (
        f"A box contains {n_w} white balls and {n_b} black balls (total of {total} balls). "
        f"A ball is chosen, replaced, and a second ball is chosen.\n\n"
        f"1. Calculate the probability of selecting two white balls ($WW$).\n"
        f"2. Calculate the probability of selecting two black balls ($BB$).\n"
        f"3. Calculate the probability that BOTH balls chosen are the **same colour**."
    )

    p_ww = p_w * p_w
    p_bb = p_b * p_b

    worked = (
        f"**1. Two white balls ($WW$):**\n"
        f"$$P(WW) = \\frac{{{n_w}}}{{{total}}} \\times \\frac{{{n_w}}}{{{total}}} = {_fmt_frac(p_ww)}$$\n\n"
        f"**2. Two black balls ($BB$):**\n"
        f"$$P(BB) = \\frac{{{n_b}}}{{{total}}} \\times \\frac{{{n_b}}}{{{total}}} = {_fmt_frac(p_bb)}$$\n\n"
        f"**3. Both balls same colour:**\n"
        f"Since $WW$ and $BB$ are mutually exclusive outcomes:\n"
        f"$$P(\\text{{Same colour}}) = P(WW) + P(BB) = {_fmt_frac(p_ww)} + {_fmt_frac(p_bb)} = {_fmt_frac(p_same)}$$"
    )

    ans = f"P(same) = {_fmt_frac(p_same)}"

    return {
        "id": f"g10_prob_31_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_frac(p_same),
        "answer_latex": rf"P(\text{{same}}) = {_fmt_frac(p_same)}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "31_tree_diagram_both_same_outcome",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct P(WW) = {_fmt_frac(p_ww)}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct P(BB) = {_fmt_frac(p_bb)}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct sum P(same) = {_fmt_frac(p_same)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add the probability of getting two white balls to the probability of getting two black balls.",
            "2_concept": "P(same colour) = P(WW) + P(BB).",
            "3_breakdown": f"P(WW) = {_fmt_frac(p_ww)}, P(BB) = {_fmt_frac(p_bb)}. Sum = {_fmt_frac(p_same)}.",
        },
        "misconception_tags": ["same_colour_single_branch_error"],
    }


# -----------------------------------------------------------------------------
# 32. Tree diagram at least one outcome
# -----------------------------------------------------------------------------
def arch_32_tree_diagram_at_least_one_outcome(rng: random.Random) -> Dict[str, Any]:
    p_green = Fraction(1, 3)
    p_not_green = 1 - p_green  # 2/3
    p_no_green = p_not_green * p_not_green  # 4/9
    p_at_least_one = 1 - p_no_green  # 5/9

    prompt = (
        "In a game, the probability of winning a green token on any turn is $P(G) = \\frac{1}{3}$. "
        "A player takes two independent turns.\n\n"
        "1. Calculate the probability of NOT getting a green token on a single turn.\n"
        "2. Calculate the probability of getting NO green tokens in two turns.\n"
        "3. Use the complement rule to calculate the probability of getting **at least one green token** in the two turns."
    )

    worked = (
        f"**1. Not green on 1 turn:**\n"
        f"$$P(G') = 1 - \\frac{{1}}{{3}} = {_fmt_frac(p_not_green)}$$\n\n"
        f"**2. No green in two turns:**\n"
        f"$$P(\\text{{No }} G) = P(G') \\times P(G') = {_fmt_frac(p_not_green)} \\times {_fmt_frac(p_not_green)} = {_fmt_frac(p_no_green)}$$\n\n"
        f"**3. At least one green:**\n"
        f"$$P(\\text{{At least one }} G) = 1 - P(\\text{{No }} G) = 1 - {_fmt_frac(p_no_green)} = {_fmt_frac(p_at_least_one)}$$"
    )

    ans = f"P(at least one G) = {_fmt_frac(p_at_least_one)}"

    return {
        "id": f"g10_prob_32_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_frac(p_at_least_one),
        "answer_latex": rf"P(\text{{at least one }} G) = {_fmt_frac(p_at_least_one)}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "32_tree_diagram_at_least_one_outcome",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"P(not green) = {_fmt_frac(p_not_green)}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"P(no green) = {_fmt_frac(p_no_green)}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"P(at least one green) = {_fmt_frac(p_at_least_one)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "P(at least one) = 1 - P(none).",
            "2_concept": "The easiest way to find 'at least one' is to subtract 'none' from 1.",
            "3_breakdown": f"P(none) = (2/3) * (2/3) = 4/9. P(at least one) = 1 - 4/9 = {_fmt_frac(p_at_least_one)}.",
        },
        "misconception_tags": ["at_least_one_complement_error"],
    }


# -----------------------------------------------------------------------------
# 33. Venn diagram shading union
# -----------------------------------------------------------------------------
def arch_33_venn_diagram_shading_union(rng: random.Random) -> Dict[str, Any]:
    n_a = rng.randint(18, 25)
    n_ab = rng.randint(8, 14)
    n_b = rng.randint(15, 22)
    n_neither = rng.randint(10, 18)
    total = n_a + n_ab + n_b + n_neither

    svg = _make_shaded_venn_svg(n_a, n_ab, n_b, n_neither, label_a="A", label_b="B", highlight="union", title="Union Region A U B")
    tot_union = n_a + n_ab + n_b
    p_union = Fraction(tot_union, total)

    prompt = (
        "In a Venn diagram, the union of two events $A$ and $B$, denoted $A \\cup B$, represents elements that belong to $A$, $B$, or both.\n\n"
        f"The counts in the regions are: $A$ only = {n_a}, both = {n_ab}, $B$ only = {n_b}, neither = {n_neither} (total $n(S) = {total}$).\n\n"
        "1. Write down the number of elements belonging to $A \\cup B$.\n"
        "2. Calculate $P(A \\cup B)$ as a simplified fraction.\n"
        "3. State which regions of the Venn diagram are included in $A \\cup B$."
    )

    worked = (
        f"**1. Count in $A \\cup B$:**\n"
        f"$$n(A \\cup B) = {n_a} + {n_ab} + {n_b} = {tot_union}$$\n\n"
        f"**2. Probability:**\n"
        f"$$P(A \\cup B) = \\frac{{{tot_union}}}{{{total}}} = {_fmt_frac(p_union)}$$\n\n"
        f"**3. Regions included:**\n"
        f"$A \\cup B$ includes: $A$ only, $B$ only, and the intersection $A \\cap B$."
    )

    ans = f"n(A U B) = {tot_union}, P(A U B) = {_fmt_frac(p_union)}"

    return {
        "id": f"g10_prob_33_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "33_venn_diagram_shading_union",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct count n(A U B) = {tot_union}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct probability P(A U B) = {_fmt_frac(p_union)}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Correct regions identification (A only, B only, and intersection)", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The union combines everything inside both circles.",
            "2_concept": "n(A U B) = n(A only) + n(both) + n(B only).",
            "3_breakdown": f"Count = {n_a} + {n_ab} + {n_b} = {tot_union}. P(A U B) = {tot_union}/{total} = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["venn_union_shading_error"],
    }


# -----------------------------------------------------------------------------
# 34. Venn diagram shading intersection
# -----------------------------------------------------------------------------
def arch_34_venn_diagram_shading_intersection(rng: random.Random) -> Dict[str, Any]:
    n_a = rng.randint(20, 28)
    n_ab = rng.randint(10, 16)
    n_b = rng.randint(16, 24)
    n_neither = rng.randint(12, 18)
    total = n_a + n_ab + n_b + n_neither

    svg = _make_shaded_venn_svg(n_a, n_ab, n_b, n_neither, label_a="A", label_b="B", highlight="intersection", title="Intersection Region A and B")
    p_inter = Fraction(n_ab, total)

    prompt = (
        "In a Venn diagram, the intersection of two events $A$ and $B$, denoted $A \\cap B$, represents elements belonging to BOTH $A$ and $B$.\n\n"
        f"The counts are: $A$ only = {n_a}, both = {n_ab}, $B$ only = {n_b}, neither = {n_neither} (total $n(S) = {total}$).\n\n"
        "1. State the number of elements in the intersection $A \\cap B$.\n"
        "2. Calculate the probability $P(A \\cap B)$.\n"
        "3. State the word commonly used in probability questions to denote intersection ('and' or 'or')."
    )

    worked = (
        f"**1. Count in $A \\cap B$:**\n"
        f"$$n(A \\cap B) = {n_ab}$$\n\n"
        f"**2. Probability:**\n"
        f"$$P(A \\cap B) = \\frac{{{n_ab}}}{{{total}}} = {_fmt_frac(p_inter)}$$\n\n"
        "**3. Word representation:**\n"
        "The word **'and'** represents intersection ($A$ and $B$)."
    )

    ans = f"n(inter)={n_ab}, P(inter)={_fmt_frac(p_inter)}, 'and'"

    return {
        "id": f"g10_prob_34_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "34_venn_diagram_shading_intersection",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct intersection count ({n_ab})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct probability ({_fmt_frac(p_inter)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Statement that 'and' denotes intersection", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The intersection is the overlapping area in the middle of the two circles.",
            "2_concept": "'And' means intersection (both events happen).",
            "3_breakdown": f"Count = {n_ab}, Probability = {n_ab}/{total} = {_fmt_frac(p_inter)}.",
        },
        "misconception_tags": ["intersection_and_or_confusion"],
    }


# -----------------------------------------------------------------------------
# 35. Venn diagram shading only one event
# -----------------------------------------------------------------------------
def arch_35_venn_diagram_shading_only_one_event(rng: random.Random) -> Dict[str, Any]:
    n_a = rng.randint(22, 32)
    n_ab = rng.randint(10, 16)
    n_b = rng.randint(18, 26)
    n_neither = rng.randint(10, 18)
    total = n_a + n_ab + n_b + n_neither

    svg = _make_shaded_venn_svg(n_a, n_ab, n_b, n_neither, label_a="A", label_b="B", highlight="a_only", title="Event A ONLY Region")
    p_a_only = Fraction(n_a, total)

    prompt = (
        "In a Venn diagram, the region representing '$A$ ONLY' corresponds to elements in $A$ but NOT in $B$ ($A \\cap B'$).\n\n"
        f"The counts are: $A$ only = {n_a}, both = {n_ab}, $B$ only = {n_b}, neither = {n_neither} (total $n(S) = {total}$).\n\n"
        "1. State the number of elements in '$A$ only'.\n"
        "2. Calculate the probability $P(A \\text{ only}) = P(A \\cap B')$.\n"
        "3. Express $n(A \\text{ only})$ in terms of $n(A)$ and $n(A \\cap B)$."
    )

    worked = (
        f"**1. Count in '$A$ only':**\n"
        f"$$n(A \\cap B') = {n_a}$$\n\n"
        f"**2. Probability:**\n"
        f"$$P(A \\text{{ only}}) = \\frac{{{n_a}}}{{{total}}} = {_fmt_frac(p_a_only)}$$\n\n"
        "**3. Relationship:**\n"
        f"$$n(A \\text{{ only}}) = n(A) - n(A \\cap B) = {n_a + n_ab} - {n_ab} = {n_a}$$"
    )

    ans = f"n(A only)={n_a}, P(A only)={_fmt_frac(p_a_only)}"

    return {
        "id": f"g10_prob_35_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "35_venn_diagram_shading_only_one_event",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct count n(A only) = {n_a}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct probability ({_fmt_frac(p_a_only)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Formula: n(A only) = n(A) - n(A and B)", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "A only is the left crescent (circle A without the overlap).",
            "2_concept": "n(A only) = n(A) - n(A and B).",
            "3_breakdown": f"Count = {n_a}. P(A only) = {n_a}/{total} = {_fmt_frac(p_a_only)}.",
        },
        "misconception_tags": ["a_only_includes_intersection_error"],
    }


# -----------------------------------------------------------------------------
# 36. Venn diagram shading neither complement
# -----------------------------------------------------------------------------
def arch_36_venn_diagram_shading_neither_complement(rng: random.Random) -> Dict[str, Any]:
    n_a = rng.randint(20, 30)
    n_ab = rng.randint(10, 16)
    n_b = rng.randint(18, 28)
    n_neither = rng.randint(14, 22)
    total = n_a + n_ab + n_b + n_neither

    svg = _make_shaded_venn_svg(n_a, n_ab, n_b, n_neither, label_a="A", label_b="B", highlight="neither", title="Neither Event (A U B)'")
    p_neither = Fraction(n_neither, total)

    prompt = (
        "In a Venn diagram, the region outside both circles represents elements that belong to NEITHER $A$ nor $B$, denoted $(A \\cup B)'$.\n\n"
        f"The counts are: $A$ only = {n_a}, both = {n_ab}, $B$ only = {n_b}, neither = {n_neither} (total $n(S) = {total}$).\n\n"
        "1. State the number of elements in $(A \\cup B)'$.\n"
        "2. Calculate $P((A \\cup B)')$.\n"
        "3. Verify that $P((A \\cup B)') = 1 - P(A \\cup B)$."
    )

    tot_union = n_a + n_ab + n_b
    p_union = Fraction(tot_union, total)

    worked = (
        f"**1. Count in $(A \\cup B)'$:**\n"
        f"$$n((A \\cup B)') = {n_neither}$$\n\n"
        f"**2. Probability:**\n"
        f"$$P((A \\cup B)') = \\frac{{{n_neither}}}{{{total}}} = {_fmt_frac(p_neither)}$$\n\n"
        f"**3. Verification with complement rule:**\n"
        f"$$P(A \\cup B) = \\frac{{{tot_union}}}{{{total}}} = {_fmt_frac(p_union)}$$\n"
        f"$$1 - P(A \\cup B) = 1 - {_fmt_frac(p_union)} = {_fmt_frac(p_neither)}$$\n"
        f"Both values are identical ({_fmt_frac(p_neither)})."
    )

    ans = f"n(neither)={n_neither}, P(neither)={_fmt_frac(p_neither)}"

    return {
        "id": f"g10_prob_36_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "36_venn_diagram_shading_neither_complement",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct count n(neither) = {n_neither}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct probability ({_fmt_frac(p_neither)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Verification using complement rule 1 - P(union)", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The region outside both circles is the complement of the union.",
            "2_concept": "P(neither) = 1 - P(A or B).",
            "3_breakdown": f"Count = {n_neither}. Probability = {n_neither}/{total} = {_fmt_frac(p_neither)}.",
        },
        "misconception_tags": ["venn_outside_region_complement_error"],
    }


# -----------------------------------------------------------------------------
# 37. Venn diagram at most one event
# -----------------------------------------------------------------------------
def arch_37_venn_diagram_at_most_one_event(rng: random.Random) -> Dict[str, Any]:
    n_a = rng.randint(20, 30)
    n_ab = rng.randint(10, 16)
    n_b = rng.randint(15, 25)
    n_neither = rng.randint(12, 20)
    total = n_a + n_ab + n_b + n_neither

    svg = _make_shaded_venn_svg(n_a, n_ab, n_b, n_neither, label_a="A", label_b="B", title="Two Events")
    n_at_most_one = n_a + n_b + n_neither  # everything except intersection
    p_at_most_one = Fraction(n_at_most_one, total)

    prompt = (
        "In a survey of learners, participation in two sports $A$ and $B$ is shown on a Venn diagram:\n\n"
        f"Counts: $A$ only = {n_a}, both = {n_ab}, $B$ only = {n_b}, neither = {n_neither} (total $n(S) = {total}$).\n\n"
        "1. Explain what outcomes are included in the event **'participates in at most one sport'**.\n"
        "2. Calculate the number of learners who participate in at most one sport.\n"
        "3. Calculate the probability that a randomly chosen learner participates in at most one sport."
    )

    worked = (
        "**1. Explanation:**\n"
        "'At most one' means 0 sports or 1 sport. This includes: $A$ only, $B$ only, and neither "
        "(everything except both).\n\n"
        f"**2. Count:**\n"
        f"$$n(\\text{{At most one}}) = {n_a} + {n_b} + {n_neither} = {total} - {n_ab} = {n_at_most_one}$$\n\n"
        f"**3. Probability:**\n"
        f"$$P(\\text{{At most one}}) = 1 - P(A \\cap B) = 1 - \\frac{{{n_ab}}}{{{total}}} = \\frac{{{n_at_most_one}}}{{{total}}} = {_fmt_frac(p_at_most_one)}$$"
    )

    ans = f"Count = {n_at_most_one}, P = {_fmt_frac(p_at_most_one)}"

    return {
        "id": f"g10_prob_37_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "37_venn_diagram_at_most_one_event",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Valid explanation: 0 or 1 sport (excludes both)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct count ({n_at_most_one})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct probability ({_fmt_frac(p_at_most_one)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "'At most one' means 0 or 1: subtract the intersection from the total.",
            "2_concept": "P(at most one) = 1 - P(both).",
            "3_breakdown": f"Total - both = {total} - {n_ab} = {n_at_most_one}. P = {n_at_most_one}/{total} = {_fmt_frac(p_at_most_one)}.",
        },
        "misconception_tags": ["at_most_one_excludes_zero_error"],
    }


# -----------------------------------------------------------------------------
# 38. Venn diagram exactly one event
# -----------------------------------------------------------------------------
def arch_38_venn_diagram_exactly_one_event(rng: random.Random) -> Dict[str, Any]:
    n_a = rng.randint(22, 34)
    n_ab = rng.randint(12, 18)
    n_b = rng.randint(16, 26)
    n_neither = rng.randint(10, 18)
    total = n_a + n_ab + n_b + n_neither

    svg = _make_shaded_venn_svg(n_a, n_ab, n_b, n_neither, label_a="A", label_b="B", highlight="exactly_one", title="Exactly One Event")
    n_exact = n_a + n_b
    p_exact = Fraction(n_exact, total)

    prompt = (
        "A Venn diagram shows the distribution of learners participating in two clubs $A$ and $B$:\n\n"
        f"Counts: $A$ only = {n_a}, both = {n_ab}, $B$ only = {n_b}, neither = {n_neither} (total $n(S) = {total}$).\n\n"
        "1. How many learners participate in **EXACTLY ONE** club?\n"
        "2. Calculate the probability that a randomly chosen learner participates in exactly one club."
    )

    worked = (
        f"**1. Count for Exactly One:**\n"
        f"$$n(\\text{{Exactly one}}) = n(A \\text{{ only}}) + n(B \\text{{ only}}) = {n_a} + {n_b} = {n_exact}$$\n\n"
        f"**2. Probability:**\n"
        f"$$P(\\text{{Exactly one}}) = \\frac{{{n_exact}}}{{{total}}} = {_fmt_frac(p_exact)}$$"
    )

    ans = f"Count={n_exact}, P={_fmt_frac(p_exact)}"

    return {
        "id": f"g10_prob_38_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 2,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "38_venn_diagram_exactly_one_event",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 2,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct count n(exactly one) = {n_exact}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct probability ({_fmt_frac(p_exact)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add the counts for A only and B only.",
            "2_concept": "Exactly one = (A only) + (B only). Do not include both or neither.",
            "3_breakdown": f"Count = {n_a} + {n_b} = {n_exact}. P = {n_exact}/{total} = {_fmt_frac(p_exact)}.",
        },
        "misconception_tags": ["exactly_one_includes_both_error"],
    }


# -----------------------------------------------------------------------------
# 39. Probability with ratios and algebra
# -----------------------------------------------------------------------------
def arch_39_probability_with_ratios_and_algebra(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.choice([2, 3])
    r2 = rng.choice([4, 5])
    total_mult = r1 + r2
    k = rng.choice([10, 15, 20])
    n_a = r1 * k
    n_b = r2 * k
    total_n = n_a + n_b

    p_a = Fraction(r1, total_mult)
    p_b = Fraction(r2, total_mult)

    prompt = (
        f"In a school sports academy of {total_n} athletes, the ratio of runners to swimmers is {r1} : {r2}.\n\n"
        f"Every athlete is either a runner or a swimmer, but none does both.\n\n"
        f"1. Set up an equation using a variable $x$ to find the number of runners and swimmers.\n"
        f"2. Calculate the number of runners.\n"
        f"3. Calculate the probability that a randomly chosen athlete is a runner."
    )

    worked = (
        f"**1. Equation:**\n"
        f"Let the parts be {r1}$x$ and {r2}$x$:\n"
        f"$${r1}x + {r2}x = {total_n}$$\n"
        f"$${total_mult}x = {total_n} \\implies x = {k}$$\n\n"
        f"**2. Number of runners:**\n"
        f"$$\\text{{Runners}} = {r1} \\times {k} = {n_a}$$\n\n"
        f"**3. Probability:**\n"
        f"$$P(\\text{{Runner}}) = \\frac{{{n_a}}}{{{total_n}}} = \\frac{{{r1}}}{{{total_mult}}} = {_fmt_frac(p_a)}$$"
    )

    ans = f"Runners = {n_a}, P(Runner) = {_fmt_frac(p_a)}"

    return {
        "id": f"g10_prob_39_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "39_probability_with_ratios_and_algebra",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct algebraic setup: {r1}x + {r2}x = {total_n}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Number of runners = {n_a}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Probability P(Runner) = {_fmt_frac(p_a)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add the ratio parts together to find the fraction of the total.",
            "2_concept": "Probability from ratio a : b is a / (a + b).",
            "3_breakdown": f"Total parts = {total_mult}. Probability = {r1}/{total_mult} = {_fmt_frac(p_a)}.",
        },
        "misconception_tags": ["ratio_probability_denominator_confusion"],
    }


# -----------------------------------------------------------------------------
# 40. Two event probability word problem survey
# -----------------------------------------------------------------------------
def arch_40_two_event_probability_word_problem_survey(rng: random.Random) -> Dict[str, Any]:
    total_n = 100
    x_both = rng.randint(15, 25)
    tot_coffee = x_both + rng.randint(25, 35)
    tot_tea = x_both + rng.randint(20, 30)
    neither = total_n - (tot_coffee + tot_tea - x_both)

    prompt = (
        f"A survey of {total_n} teachers regarding beverage consumption showed:\n\n"
        f"- {tot_coffee} drink Coffee ($C$)\n"
        f"- {tot_tea} drink Tea ($T$)\n"
        f"- {neither} drink neither coffee nor tea\n\n"
        f"1. Determine the number of teachers who drink BOTH coffee and tea.\n"
        f"2. Calculate the probability that a teacher chosen at random drinks Coffee ONLY.\n"
        f"3. Calculate the probability that a teacher drinks Coffee OR Tea."
    )

    c_only = tot_coffee - x_both
    p_c_only = Fraction(c_only, total_n)
    tot_union = total_n - neither
    p_union = Fraction(tot_union, total_n)

    worked = (
        f"**1. Both Coffee and Tea:**\n"
        f"$$n(C \\cup T) = {total_n} - {neither} = {tot_union}$$\n"
        f"$$n(C \\cap T) = n(C) + n(T) - n(C \\cup T) = {tot_coffee} + {tot_tea} - {tot_union} = {x_both}$$\n\n"
        f"**2. Coffee ONLY:**\n"
        f"$$n(C \\text{{ only}}) = {tot_coffee} - {x_both} = {c_only}$$\n"
        f"$$P(C \\text{{ only}}) = \\frac{{{c_only}}}{{{total_n}}} = {_fmt_frac(p_c_only)}$$\n\n"
        f"**3. Coffee OR Tea:**\n"
        f"$$P(C \\cup T) = \\frac{{{tot_union}}}{{{total_n}}} = {_fmt_frac(p_union)}$$"
    )

    ans = f"Both={x_both}, P(Coffee only)={_fmt_frac(p_c_only)}, P(C or T)={_fmt_frac(p_union)}"

    return {
        "id": f"g10_prob_40_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "40_two_event_probability_word_problem_survey",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "hard",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct intersection count ({x_both})", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"P(Coffee only) = {_fmt_frac(p_c_only)}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"P(Coffee or Tea) = {_fmt_frac(p_union)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "First find the union (Total - Neither), then find the intersection using n(A) + n(B) - Union.",
            "2_concept": "Both = n(Coffee) + n(Tea) - (Total - Neither).",
            "3_breakdown": f"Both = {tot_coffee} + {tot_tea} - {tot_union} = {x_both}. Coffee only = {c_only}.",
        },
        "misconception_tags": ["survey_intersection_deduction_error"],
    }


# -----------------------------------------------------------------------------
# 41. Contingency table mutual exclusivity test
# -----------------------------------------------------------------------------
def arch_41_contingency_table_mutual_exclusivity_test(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a contingency table classifying learners by Gender (Boy / Girl) and Grade (Grade 10 / Grade 11):\n\n"
        "1. Are the events 'being a Boy' and 'being a Girl' mutually exclusive? Justify with a reason.\n"
        "2. Are the events 'being a Boy' and 'being in Grade 10' mutually exclusive? Justify with a reason.\n"
        "3. State the rule for determining mutual exclusivity from a contingency table."
    )

    worked = (
        "**1. Boy and Girl:**\n"
        "**Yes, mutually exclusive.** A learner cannot be both in this two-category classification "
        "($P(\\text{Boy} \\cap \\text{Girl}) = 0$).\n\n"
        "**2. Boy and Grade 10:**\n"
        "**No, NOT mutually exclusive.** A learner can be both a Boy and in Grade 10 "
        "($P(\\text{Boy} \\cap \\text{Grade 10}) > 0$; their intersection cell has positive count).\n\n"
        "**3. General Rule:**\n"
        "Two events from a contingency table are mutually exclusive if their intersection cell has a frequency of 0."
    )

    ans = "1: Yes, 2: No, 3: Intersection cell frequency must be 0"

    return {
        "id": f"g10_prob_41_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "41_contingency_table_mutual_exclusivity_test",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Boy and Girl are mutually exclusive with valid reason", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Boy and Grade 10 are not mutually exclusive with valid reason", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "General rule stated correctly", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Can the two events happen at the same time? Look at the intersection cell in the table.",
            "2_concept": "Events are mutually exclusive if their intersection is 0.",
            "3_breakdown": "Categories in the same variable are mutually exclusive; categories across different variables overlap.",
        },
        "misconception_tags": ["contingency_table_mutual_exclusivity_confusion"],
    }


# -----------------------------------------------------------------------------
# 42. Simulation vs probability model
# -----------------------------------------------------------------------------
def arch_42_simulation_vs_probability_model(rng: random.Random) -> Dict[str, Any]:
    rolls = 600
    expected = 100
    observed_6 = rng.choice([104, 98, 102, 95])
    diff = abs(observed_6 - expected)

    prompt = (
        f"A learner conducts a simulation by rolling a die {rolls} times to test whether it is fair.\n\n"
        f"The number 6 appeared {observed_6} times.\n\n"
        f"1. What is the theoretical expected frequency of rolling a 6 in {rolls} rolls of a fair die?\n"
        f"2. Calculate the difference between the observed frequency and the expected frequency.\n"
        f"3. Does this result provide evidence that the die is biased, or is this minor variation normal? Explain."
    )

    worked = (
        f"**1. Expected frequency:**\n"
        f"$$\\text{{Expected}} = P(6) \\times {rolls} = \\frac{{1}}{{6}} \\times {rolls} = {expected}\\text{{ times}}$$\n\n"
        f"**2. Difference:**\n"
        f"$$|{observed_6} - {expected}| = {diff}$$\n\n"
        f"**3. Evaluation:**\n"
        f"The variation of only {diff} from the expected 100 is very small ({_fmt_dec(diff / expected * 100)}%). "
        f"In real-world random simulations, minor natural fluctuations are entirely expected, so there is "
        f"**no evidence of bias**; the die appears fair."
    )

    ans = f"Expected={expected}, Difference={diff}, No evidence of bias (normal variation)"

    return {
        "id": f"g10_prob_42_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "42_simulation_vs_probability_model",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct expected frequency ({expected})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct difference ({diff})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Valid conclusion regarding normal experimental fluctuation", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Expected frequency = Probability * Number of trials.",
            "2_concept": "Small natural variations around the expected value are normal in random trials.",
            "3_breakdown": f"Expected = (1/6) * 600 = 100. Observed = {observed_6}. Variation is normal.",
        },
        "misconception_tags": ["simulation_exact_frequency_fallacy"],
    }


# -----------------------------------------------------------------------------
# 43. Two dice sum distribution
# -----------------------------------------------------------------------------
def arch_43_two_dice_sum_distribution(rng: random.Random) -> Dict[str, Any]:
    threshold = rng.choice([9, 10])
    # sum > threshold
    favour_pairs = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7) if d1 + d2 > threshold]
    n_favour = len(favour_pairs)
    p_favour = Fraction(n_favour, 36)

    prompt = (
        f"Two fair dice are rolled.\n\n"
        f"1. How many total outcomes are possible in the sample space?\n"
        f"2. List all the outcomes where the sum of the two dice is **strictly greater than {threshold}**.\n"
        f"3. Calculate the probability of getting a sum strictly greater than {threshold}."
    )

    pairs_str = ", ".join(f"({a}, {b})" for a, b in favour_pairs)
    worked = (
        "**1. Sample Space:** $n(S) = 36$\n\n"
        f"**2. Outcomes with sum > {threshold}:**\n"
        f"$$\\{{{pairs_str}\\}}$$\n"
        f"Count = {n_favour}\n\n"
        f"**3. Probability:**\n"
        f"$$P(\\text{{Sum}} > {threshold}) = \\frac{{{n_favour}}}{{36}} = {_fmt_frac(p_favour)}$$"
    )

    ans = f"n(S)=36, P={_fmt_frac(p_favour)}"

    return {
        "id": f"g10_prob_43_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "43_two_dice_sum_distribution",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Total outcomes n(S) = 36", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Listing favourable pairs correctly", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct probability ({_fmt_frac(p_favour)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Count all pairs whose sum exceeds the threshold.",
            "2_concept": "P(E) = n(favourable) / 36.",
            "3_breakdown": f"Favourable pairs: {pairs_str}. Probability = {n_favour}/36 = {_fmt_frac(p_favour)}.",
        },
        "misconception_tags": ["dice_sum_strict_inequality_inclusion"],
    }


# -----------------------------------------------------------------------------
# 44. Cards and compound events
# -----------------------------------------------------------------------------
def arch_44_cards_and_compound_events(rng: random.Random) -> Dict[str, Any]:
    suit = rng.choice(["Heart", "Spade", "Club", "Diamond"])
    rank = rng.choice(["King", "Ace", "Queen"])

    p_suit = Fraction(13, 52)
    p_rank = Fraction(4, 52)
    p_inter = Fraction(1, 52)  # exactly 1 card has both
    p_union = p_suit + p_rank - p_inter  # 16/52 = 4/13

    prompt = (
        f"A single card is chosen at random from a standard 52-card deck.\n\n"
        f"1. State the probability of selecting a **{suit}**, $P({suit})$.\n"
        f"2. State the probability of selecting a **{rank}**, $P({rank})$.\n"
        f"3. State the probability of selecting the **{rank} of {suit}s**, $P({suit} \\cap {rank})$.\n"
        f"4. Use the addition rule to calculate the probability of selecting a **{suit} OR a {rank}**."
    )

    worked = (
        f"**1. $P({suit})$:** $\\frac{{13}}{{52}} = {_fmt_frac(p_suit)}$\n\n"
        f"**2. $P({rank})$:** $\\frac{{4}}{{52}} = {_fmt_frac(p_rank)}$\n\n"
        f"**3. Intersection:** There is exactly 1 such card:\n"
        f"$$P({suit} \\cap {rank}) = \\frac{{1}}{{52}}$$\n\n"
        f"**4. Addition Rule:**\n"
        f"$$P({suit} \\cup {rank}) = P({suit}) + P({rank}) - P({suit} \\cap {rank})$$\n"
        f"$$P({suit} \\cup {rank}) = \\frac{{13}}{{52}} + \\frac{{4}}{{52}} - \\frac{{1}}{{52}} = \\frac{{16}}{{52}} = {_fmt_frac(p_union)}$$"
    )

    ans = f"P({suit} or {rank}) = {_fmt_frac(p_union)}"

    return {
        "id": f"g10_prob_44_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"P({suit} \cup {rank}) = {_fmt_frac(p_union)}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "44_cards_and_compound_events",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"P({suit}) = 13/52", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"P({rank}) = 4/52", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Intersection = 1/52", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Union = {_fmt_frac(p_union)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Don't forget to subtract the 1 card that is both the chosen suit and rank.",
            "2_concept": "P(A or B) = P(A) + P(B) - P(A and B).",
            "3_breakdown": f"13/52 + 4/52 - 1/52 = 16/52 = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["card_compound_intersection_double_counting"],
    }


# -----------------------------------------------------------------------------
# 45. Venn diagram reconstruct from probabilities
# -----------------------------------------------------------------------------
def arch_45_venn_diagram_reconstruct_from_probabilities(rng: random.Random) -> Dict[str, Any]:
    p_a = Fraction(6, 10)
    p_b = Fraction(5, 10)
    p_union = Fraction(8, 10)

    p_inter = p_a + p_b - p_union  # 3/10
    p_a_only = p_a - p_inter  # 3/10
    p_b_only = p_b - p_inter  # 2/10
    p_neither = 1 - p_union  # 2/10

    prompt = (
        f"Two events $A$ and $B$ in sample space $S$ satisfy:\n\n"
        f"$$P(A) = {_fmt_frac(p_a)}, \\quad P(B) = {_fmt_frac(p_b)}, \\quad P(A \\cup B) = {_fmt_frac(p_union)}$$\n\n"
        "1. Calculate $P(A \\cap B)$.\n"
        "2. Calculate $P(A \\text{ only}) = P(A \\cap B')$.\n"
        "3. Calculate $P(B \\text{ only}) = P(B \\cap A')$.\n"
        "4. Calculate $P(\\text{neither } A \\text{ nor } B) = P((A \\cup B)')$."
    )

    worked = (
        f"**1. Intersection:**\n"
        f"$$P(A \\cap B) = P(A) + P(B) - P(A \\cup B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - {_fmt_frac(p_union)} = {_fmt_frac(p_inter)}$$\n\n"
        f"**2. $A$ only:**\n"
        f"$$P(A \\cap B') = P(A) - P(A \\cap B) = {_fmt_frac(p_a)} - {_fmt_frac(p_inter)} = {_fmt_frac(p_a_only)}$$\n\n"
        f"**3. $B$ only:**\n"
        f"$$P(B \\cap A') = P(B) - P(A \\cap B) = {_fmt_frac(p_b)} - {_fmt_frac(p_inter)} = {_fmt_frac(p_b_only)}$$\n\n"
        f"**4. Neither:**\n"
        f"$$P((A \\cup B)') = 1 - P(A \\cup B) = 1 - {_fmt_frac(p_union)} = {_fmt_frac(p_neither)}$$"
    )

    ans = f"Inter={_fmt_frac(p_inter)}, A_only={_fmt_frac(p_a_only)}, B_only={_fmt_frac(p_b_only)}, Neither={_fmt_frac(p_neither)}"

    return {
        "id": f"g10_prob_45_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "45_venn_diagram_reconstruct_from_probabilities",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "hard",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct intersection ({_fmt_frac(p_inter)})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct A only ({_fmt_frac(p_a_only)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct B only ({_fmt_frac(p_b_only)})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Correct Neither ({_fmt_frac(p_neither)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "First find the intersection, then subtract it from each individual event.",
            "2_concept": "The 4 regions of a Venn diagram partition the sample space and add up to 1.",
            "3_breakdown": f"Inter = {_fmt_frac(p_inter)}, A only = {_fmt_frac(p_a_only)}, B only = {_fmt_frac(p_b_only)}, Neither = {_fmt_frac(p_neither)}.",
        },
        "misconception_tags": ["venn_probability_partition_sum_error"],
    }


# -----------------------------------------------------------------------------
# 46. Tree diagram weather forecast
# -----------------------------------------------------------------------------
def arch_46_tree_diagram_weather_forecast(rng: random.Random) -> Dict[str, Any]:
    p_rain_sat = Fraction(rng.choice([3, 4]), 10)
    p_dry_sat = 1 - p_rain_sat

    p_rain_sun = Fraction(rng.choice([5, 6]), 10)
    p_dry_sun = 1 - p_rain_sun

    p_both_rain = p_rain_sat * p_rain_sun

    prompt = (
        f"A weather forecast for a weekend predicts:\n\n"
        f"- Saturday: Probability of rain $P(\\text{{Rain}}) = {_fmt_frac(p_rain_sat)}$\n"
        f"- Sunday: Probability of rain $P(\\text{{Rain}}) = {_fmt_frac(p_rain_sun)}$\n\n"
        "Assuming the weather on Sunday is independent of Saturday:\n"
        "1. Calculate the probability that it rains on BOTH Saturday and Sunday.\n"
        "2. Calculate the probability that it does NOT rain on either day."
    )

    p_both_dry = p_dry_sat * p_dry_sun

    worked = (
        f"**1. Rains on both days:**\n"
        f"$$P(\\text{{Rain Sat}} \\cap \\text{{Rain Sun}}) = {_fmt_frac(p_rain_sat)} \\times {_fmt_frac(p_rain_sun)} = {_fmt_frac(p_both_rain)}$$\n\n"
        f"**2. Dry on both days:**\n"
        f"$$P(\\text{{Dry Sat}}) = 1 - {_fmt_frac(p_rain_sat)} = {_fmt_frac(p_dry_sat)}$$\n"
        f"$$P(\\text{{Dry Sun}}) = 1 - {_fmt_frac(p_rain_sun)} = {_fmt_frac(p_dry_sun)}$$\n"
        f"$$P(\\text{{Dry both}}) = {_fmt_frac(p_dry_sat)} \\times {_fmt_frac(p_dry_sun)} = {_fmt_frac(p_both_dry)}$$"
    )

    ans = f"P(Both rain) = {_fmt_frac(p_both_rain)}, P(Both dry) = {_fmt_frac(p_both_dry)}"

    return {
        "id": f"g10_prob_46_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "46_tree_diagram_weather_forecast",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"P(both rain) = {_fmt_frac(p_both_rain)}", "marks": 1.5, "editable": True},
                {"id": "mp_2", "desc": f"P(both dry) = {_fmt_frac(p_both_dry)}", "marks": 1.5, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Multiply the probabilities of each independent day.",
            "2_concept": "For independent events, P(A and B) = P(A) * P(B).",
            "3_breakdown": f"Both rain: {_fmt_frac(p_rain_sat)} * {_fmt_frac(p_rain_sun)} = {_fmt_frac(p_both_rain)}. Both dry: {_fmt_frac(p_dry_sat)} * {_fmt_frac(p_dry_sun)} = {_fmt_frac(p_both_dry)}.",
        },
        "misconception_tags": ["independent_probability_addition_error"],
    }


# -----------------------------------------------------------------------------
# 47. Tree diagram successive sports matches
# -----------------------------------------------------------------------------
def arch_47_tree_diagram_successive_sports_matches(rng: random.Random) -> Dict[str, Any]:
    p_w = Fraction(rng.choice([3, 4]), 5)
    p_l = 1 - p_w

    p_wl = p_w * p_l
    p_lw = p_l * p_w
    p_one_win = p_wl + p_lw

    prompt = (
        f"A rugby team has a probability of winning any match of $P(\\text{{Win}}) = {_fmt_frac(p_w)}$. "
        f"Assume each match is independent and the team plays 2 matches (no draws).\n\n"
        f"1. List all four possible match sequences for the two matches.\n"
        f"2. Calculate the probability that the team wins BOTH matches.\n"
        f"3. Calculate the probability that the team wins EXACTLY ONE match."
    )

    p_ww = p_w * p_w

    worked = (
        f"Match probabilities: $P(W) = {_fmt_frac(p_w)}$, $P(L) = {_fmt_frac(p_l)}$.\n\n"
        f"**1. Sequences:** $WW, WL, LW, LL$.\n\n"
        f"**2. Both matches won ($WW$):**\n"
        f"$$P(WW) = {_fmt_frac(p_w)} \\times {_fmt_frac(p_w)} = {_fmt_frac(p_ww)}$$\n\n"
        f"**3. Exactly one match won ($WL$ or $LW$):**\n"
        f"$$P(WL) = {_fmt_frac(p_w)} \\times {_fmt_frac(p_l)} = {_fmt_frac(p_wl)}$$\n"
        f"$$P(LW) = {_fmt_frac(p_l)} \\times {_fmt_frac(p_w)} = {_fmt_frac(p_lw)}$$\n"
        f"$$P(\\text{{Exactly one}}) = {_fmt_frac(p_wl)} + {_fmt_frac(p_lw)} = {_fmt_frac(p_one_win)}$$"
    )

    ans = f"P(WW)={_fmt_frac(p_ww)}, P(exactly one)={_fmt_frac(p_one_win)}"

    return {
        "id": f"g10_prob_47_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "47_tree_diagram_successive_sports_matches",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct list of 4 sequences (WW, WL, LW, LL)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct P(WW) = {_fmt_frac(p_ww)}", "marks": 1.5, "editable": True},
                {"id": "mp_3", "desc": f"Correct P(exactly one) = {_fmt_frac(p_one_win)}", "marks": 1.5, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Exactly one win means either Win then Lose, or Lose then Win.",
            "2_concept": "Add P(WL) and P(LW) together for exactly one win.",
            "3_breakdown": f"P(WW) = {_fmt_frac(p_ww)}. P(WL) + P(LW) = {_fmt_frac(p_one_win)}.",
        },
        "misconception_tags": ["single_permutation_omission_tree"],
    }


# -----------------------------------------------------------------------------
# 48. Probability fractions to decimals and percentages
# -----------------------------------------------------------------------------
def arch_48_probability_fractions_to_decimals_and_percentages(rng: random.Random) -> Dict[str, Any]:
    f = rng.choice([Fraction(3, 8), Fraction(7, 20), Fraction(9, 25), Fraction(11, 40)])
    dec_val = float(f)
    pct_val = dec_val * 100.0

    dec_str = _fmt_katex(dec_val)
    pct_str = _fmt_katex(pct_val)

    prompt = (
        f"An event has a calculated theoretical probability of $P(E) = {_fmt_frac(f)}$.\n\n"
        f"1. Convert this probability into a decimal, using the South African decimal comma.\n"
        f"2. Convert this probability into a percentage.\n"
        f"3. Explain why probabilities can be represented in any of these three forms (fraction, decimal, or percentage)."
    )

    worked = (
        f"**1. Decimal representation:**\n"
        f"$$\\frac{{{f.numerator}}}{{{f.denominator}}} = {dec_str}$$\n\n"
        f"**2. Percentage representation:**\n"
        f"$${dec_str} \\times 100\\% = {pct_str}\\%$$\n\n"
        f"**3. Equivalence:**\n"
        f"All three represent the same proportional value: a part divided by the whole on a scale from 0 to 1 (or 0% to 100%)."
    )

    ans = f"Decimal={_fmt_dec(dec_val)}, Percentage={_fmt_dec(pct_val)}%"

    return {
        "id": f"g10_prob_48_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "48_probability_fractions_to_decimals_and_percentages",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct decimal representation ({_fmt_dec(dec_val)})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct percentage ({_fmt_dec(pct_val)}%)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Valid explanation of proportional equivalence", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Divide the numerator by the denominator, then multiply by 100 to get percentage.",
            "2_concept": "Fraction = numerator/denominator; Decimal = float; Percentage = Decimal * 100%.",
            "3_breakdown": f"Decimal = {_fmt_dec(dec_val)}, Percentage = {_fmt_dec(pct_val)}%.",
        },
        "misconception_tags": ["probability_form_conversion_error"],
    }


# -----------------------------------------------------------------------------
# 49. Odds vs probability conceptual check
# -----------------------------------------------------------------------------
def arch_49_odds_vs_probability_conceptual_check(rng: random.Random) -> Dict[str, Any]:
    favour = rng.choice([2, 3, 4])
    against = rng.choice([3, 5, 7])
    total = favour + against
    p = Fraction(favour, total)

    prompt = (
        f"A game of chance has **odds in favour** of winning given as {favour} : {against}.\n\n"
        f"1. Explain the distinction between 'odds in favour' and 'probability'.\n"
        f"2. Calculate the total number of outcomes, $n(S)$.\n"
        f"3. Calculate the probability of winning the game, $P(\\text{{Win}})$, as a simplified fraction."
    )

    worked = (
        "**1. Distinction:**\n"
        "- **Odds in favour** compares favourable outcomes directly to unfavourable outcomes ($n(E) : n(E')$).\n"
        "- **Probability** compares favourable outcomes to the TOTAL sample space ($n(E) / n(S)$).\n\n"
        f"**2. Total outcomes:**\n"
        f"$$n(S) = {favour} + {against} = {total}$$\n\n"
        f"**3. Probability of winning:**\n"
        f"$$P(\\text{{Win}}) = \\frac{{{favour}}}{{{total}}} = {_fmt_frac(p)}$$"
    )

    ans = f"Total={total}, P(Win)={_fmt_frac(p)}"

    return {
        "id": f"g10_prob_49_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "49_odds_vs_probability_conceptual_check",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Valid explanation distinguishing odds from probability", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct total n(S) = {total}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct probability P(Win) = {_fmt_frac(p)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Odds compare success : failure; probability divides success by total.",
            "2_concept": "If odds are a : b, probability is a / (a + b).",
            "3_breakdown": f"Total = {favour} + {against} = {total}. P(Win) = {favour}/{total} = {_fmt_frac(p)}.",
        },
        "misconception_tags": ["odds_vs_probability_confusion"],
    }


# -----------------------------------------------------------------------------
# 50. Comprehensive exam probability synthesis
# -----------------------------------------------------------------------------
def arch_50_comprehensive_exam_probability_synthesis(rng: random.Random) -> Dict[str, Any]:
    total = rng.choice([80, 100, 120])
    x_val = rng.randint(12, 20)
    a_tot = x_val + rng.randint(22, 32)
    b_tot = x_val + rng.randint(18, 28)
    neither = total - (a_tot + b_tot - x_val)

    a_only = a_tot - x_val
    b_only = b_tot - x_val

    svg = _make_shaded_venn_svg(a_only, x_val, b_only, neither, label_a="Athletics", label_b="Swimming", title="Grade 10 Sports Survey")

    p_union = Fraction(total - neither, total)
    p_inter = Fraction(x_val, total)
    p_a_only = Fraction(a_only, total)

    prompt = (
        f"In a Grade 10 class survey of {total} learners:\n\n"
        f"- {a_tot} participate in Athletics ($A$)\n"
        f"- {b_tot} participate in Swimming ($S$)\n"
        f"- {neither} participate in neither sport\n"
        f"- $x$ participate in BOTH sports\n\n"
        f"1. Set up an equation and solve for $x$.\n"
        f"2. Calculate the probability that a learner chosen at random participates in Athletics ONLY.\n"
        f"3. Calculate the probability that a learner participates in AT LEAST ONE of the sports ($A \\cup S$).\n"
        f"4. Are the events $A$ and $S$ mutually exclusive? Justify with a mathematical reason."
    )

    worked = (
        f"**1. Solving for $x$:**\n"
        f"$$({a_tot} - x) + x + ({b_tot} - x) + {neither} = {total}$$\n"
        f"$${a_tot + b_tot + neither} - x = {total} \\implies x = {x_val}$$\n\n"
        f"**2. Athletics ONLY:**\n"
        f"$$n(A \\text{{ only}}) = {a_tot} - {x_val} = {a_only}$$\n"
        f"$$P(A \\text{{ only}}) = \\frac{{{a_only}}}{{{total}}} = {_fmt_frac(p_a_only)}$$\n\n"
        f"**3. At least one sport ($A \\cup S$):**\n"
        f"$$P(A \\cup S) = \\frac{{{total} - {neither}}}{{{total}}} = \\frac{{{total - neither}}}{{{total}}} = {_fmt_frac(p_union)}$$\n\n"
        f"**4. Mutual Exclusivity:**\n"
        f"No, because $P(A \\cap S) = {_fmt_frac(p_inter)} \\neq 0$ (there are {x_val} learners who do both)."
    )

    ans = f"x={x_val}, P(A only)={_fmt_frac(p_a_only)}, P(union)={_fmt_frac(p_union)}, Mutually exclusive: No"

    return {
        "id": f"g10_prob_50_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": ans,
        "worked_solution": worked,
        "marks": 6,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "50_comprehensive_exam_probability_synthesis",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 6,
        "difficulty": "hard",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct equation and solution x = {x_val}", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"Correct P(Athletics only) = {_fmt_frac(p_a_only)}", "marks": 1.5, "editable": True},
                {"id": "mp_3", "desc": f"Correct P(union) = {_fmt_frac(p_union)}", "marks": 1.5, "editable": True},
                {"id": "mp_4", "desc": "Mutually exclusive check with reason P(A and S) != 0", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Set up the sum of the 4 regions equal to the total to find x.",
            "2_concept": "P(A only) = (total A - x) / total. Union is 1 - Neither / total.",
            "3_breakdown": f"x = {x_val}. Athletics only = {a_only}. P(union) = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["comprehensive_probability_exam_error"],
    }
