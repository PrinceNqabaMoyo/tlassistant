"""Subskills 25 to 32: Tree diagrams, multi-stage branching, product rule along branches, and summing end-nodes."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_frac,
    _fmt_pct,
)


def generate_25_tree_branch_probabilities(r: random.Random) -> Dict[str, Any]:
    """Verify that branch probabilities emanating from any node sum to exactly 1,0."""
    p1 = r.choice([0.60, 0.65, 0.70, 0.75])
    p2 = round(1.0 - p1, 2)
    d_spec_25 = {
        "diagram_role": "context",
        "kind": "tree_diagram",
        "branches": [{"label": "Branch A", "sub": ["Success", "Failure"]}, {"label": "Branch B", "sub": ["Success", "Failure"]}],
        "outcomes": ["A", "B"],
        "title": f"Branch Probabilities ({_fmt(p1, 2)} + {_fmt(p2, 2)} = 1,00)",
        "stages": [
            {"name": "Stage 1", "outcomes": [{"name": "Branch A", "prob": f"{_fmt(p1, 2)}"}, {"name": "Branch B", "prob": f"{_fmt(p2, 2)}"}]}
        ],
    }
    correct_ans = f"Branch probabilities at every node must sum to 1,00 (100%): {_fmt(p1, 2)} + {_fmt(p2, 2)} = 1,00"

    custom_options = [
        correct_ans,
        f"Branch probabilities must sum to 0,00",
        f"Branch probabilities multiply to 1,00 at every junction",
        f"Branch probabilities can sum to any arbitrary number depending on tree height",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the tree diagram for a two-stage decision process.\n"
        f"The first stage splits into two mutually exclusive branches with probabilities {_fmt(p1, 2)} and {_fmt(p2, 2)}.\n\n"
        f"State the mathematical rule that governs the sum of branch probabilities originating from any single node."
    )
    explanation = (
        f"Step 1: The branches leaving a single node represent all mutually exclusive and exhaustive outcomes of that event [M].\n"
        f"Step 2: Therefore, their individual probabilities must sum to certainty: {_fmt(p1, 2)} + {_fmt(p2, 2)} = 1,00 (100%) [M].\n"
        f"Step 3: Branch probabilities must always sum to 1,00 [A]."
    )
    return _build_question_payload(
        subskill_id="25_tree_branch_probabilities",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember that all possible outcomes from one starting point must cover everything (100%).",
        tier_2=f"0,70 + 0,30 = 1,00.",
        tier_3="The branches emanating from any node must sum to 1,00.",
        r=r,
        diagram_spec=d_spec_25,
    )


def generate_26_multiplying_along_branches(r: random.Random) -> Dict[str, Any]:
    """Calculate the compound probability of a specific path on a tree diagram by multiplying along branches."""
    p_stage1 = 0.80  # passes paper 1
    p_stage2 = 0.75  # passes paper 2 given pass paper 1
    p_both = p_stage1 * p_stage2
    pct = p_both * 100.0

    correct_ans = f"P(Path) = {_fmt(p_stage1, 2)} × {_fmt(p_stage2, 2)} = {_fmt(p_both, 2)} ({_fmt_pct(pct, 1)})"
    custom_options = [
        correct_ans,
        f"P(Path) = {_fmt(p_stage1, 2)} + {_fmt(p_stage2, 2)} = {_fmt(p_stage1 + p_stage2, 2)}",
        f"P(Path) = {_fmt(p_stage1 - p_stage2, 2)}",
        f"P(Path) = 1,00",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"On a tree diagram tracing learner success in Mathematical Literacy:\n"
        f"• Stage 1 (Paper 1): P(Pass) = {_fmt(p_stage1, 2)} (80%)\n"
        f"• Stage 2 (Paper 2): P(Pass) = {_fmt(p_stage2, 2)} (75%)\n\n"
        f"Calculate the compound probability that a learner follows the branch path of passing BOTH Paper 1 and Paper 2."
    )
    explanation = (
        f"Step 1: Multiplication rule along tree branches: P(A and B) = P(A) × P(B | A) [M].\n"
        f"Step 2: Substitute: {_fmt(p_stage1, 2)} × {_fmt(p_stage2, 2)} [M].\n"
        f"Step 3: P(Pass Both) = {_fmt(p_both, 2)} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="26_multiplying_along_branches",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Follow the branches from start to end and multiply the probabilities together.",
        tier_2=f"Calculate {_fmt(p_stage1, 2)} × {_fmt(p_stage2, 2)}.",
        tier_3=f"The probability is {_fmt(p_both, 2)} ({_fmt_pct(pct, 1)}).",
        r=r,
    )


def generate_27_summing_across_end_nodes(r: random.Random) -> Dict[str, Any]:
    """Sum probabilities across multiple distinct favorable end-nodes in a tree diagram."""
    # Outcome 1 (Pass P1, Fail P2) = 0.80 * 0.25 = 0.20
    # Outcome 2 (Fail P1, Pass P2) = 0.20 * 0.70 = 0.14
    # P(Pass exactly one paper) = 0.20 + 0.14 = 0.34
    p_path1 = 0.20
    p_path2 = 0.14
    total_p = p_path1 + p_path2

    correct_ans = f"P(Pass exactly one) = {_fmt(p_path1, 2)} + {_fmt(p_path2, 2)} = {_fmt(total_p, 2)} ({_fmt_pct(total_p * 100, 1)})"
    custom_options = [
        correct_ans,
        f"P(Pass exactly one) = {_fmt(p_path1, 2)} × {_fmt(p_path2, 2)} = {_fmt(p_path1 * p_path2, 4)}",
        f"P(Pass exactly one) = {_fmt(p_path1 - p_path2, 2)}",
        f"P(Pass exactly one) = 0,50",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A tree diagram evaluates candidate exam results across two exam papers.\n"
        f"Two mutually exclusive end-nodes satisfy the condition 'passed exactly one paper':\n"
        f"• Path 1 (Pass P1 and Fail P2): Probability = {_fmt(p_path1, 2)} (20%)\n"
        f"• Path 2 (Fail P1 and Pass P2): Probability = {_fmt(p_path2, 2)} (14%)\n\n"
        f"Calculate the total probability that a candidate passes exactly one paper."
    )
    explanation = (
        f"Step 1: Identify that the two favorable end-node paths are mutually exclusive [M].\n"
        f"Step 2: Sum the end-node probabilities: {_fmt(p_path1, 2)} + {_fmt(p_path2, 2)} [M].\n"
        f"Step 3: Total Probability = {_fmt(total_p, 2)} ({_fmt_pct(total_p * 100, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="27_summing_across_end_nodes",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="When multiple paths satisfy the requirement, add their final probabilities together.",
        tier_2=f"Calculate {_fmt(p_path1, 2)} + {_fmt(p_path2, 2)}.",
        tier_3=f"The total probability is {_fmt(total_p, 2)} ({_fmt_pct(total_p * 100, 1)}).",
        r=r,
    )


def generate_28_weather_forecast_consecutive_rain(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of consecutive rainy days from a weather tree diagram."""
    p_sat = 0.60
    p_sun_given_rain = 0.50
    p_both = p_sat * p_sun_given_rain
    pct = p_both * 100.0

    correct_ans = f"P(Rain Sat and Rain Sun) = 0,60 × 0,50 = 0,30 (30,0%)"
    custom_options = [
        correct_ans,
        f"P(Rain Sat and Rain Sun) = 0,60 + 0,50 = 1,10 (110%)",
        f"P(Rain Sat and Rain Sun) = 0,60 - 0,50 = 0,10 (10,0%)",
        f"P(Rain Sat and Rain Sun) = 0,50",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A weather tree diagram forecasts weekend weather in the Drakensberg:\n"
        f"• Saturday: P(Rain) = 0,60 (60%)\n"
        f"• If it rains on Saturday, Sunday's probability of rain is P(Rain | Sat Rain) = 0,50 (50%)\n\n"
        f"Calculate the probability that it rains on both Saturday and Sunday."
    )
    explanation = (
        f"Step 1: Product rule along the 'Rain-Rain' branch: P(Sat Rain) × P(Sun Rain | Sat Rain) [M].\n"
        f"Step 2: Multiply: 0,60 × 0,50 = 0,30 [M].\n"
        f"Step 3: P(Rain both days) = 0,30 (30,0%) [A]."
    )
    return _build_question_payload(
        subskill_id="28_weather_forecast_consecutive_rain",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the probability of rain on Saturday by the probability of rain on Sunday.",
        tier_2="0,60 × 0,50 = 0,30.",
        tier_3="The probability of rain on both days is 30,0%.",
        r=r,
    )


def generate_29_medical_screening_tree_diagram(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of a false positive in a medical diagnostic tree diagram."""
    healthy_pct = r.choice([95, 98, 99])
    false_pos_pct = r.choice([2, 4, 5])
    p_healthy = healthy_pct / 100.0
    p_false_pos = false_pos_pct / 100.0
    p_healthy_tested_pos = round(p_healthy * p_false_pos, 4)

    correct_ans = f"P(Healthy and Tests Positive) = {p_healthy:.2f} × {p_false_pos:.2f} = {p_healthy_tested_pos:.4f} (or {p_healthy_tested_pos * 100:.2f}%)".replace(".", ",")
    custom_options = [
        correct_ans,
        f"P(Healthy and Tests Positive) = {p_healthy:.2f} + {p_false_pos:.2f} = {p_healthy + p_false_pos:.2f}".replace(".", ","),
        f"P(Healthy and Tests Positive) = {p_false_pos:.2f} ({false_pos_pct:.2f}%)".replace(".", ","),
        f"P(Healthy and Tests Positive) = {p_healthy_tested_pos / 10:.4f}".replace(".", ","),
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    d_spec_29 = {
        "diagram_role": "context",
        "kind": "tree_diagram",
        "title": f"Medical Screening Tree (Prevalence: {100 - healthy_pct}%, False Pos: {false_pos_pct}%)",
        "branches": [
            {"label": f"Healthy ({p_healthy:.2f})", "sub": [f"Test Pos ({p_false_pos:.2f})", f"Test Neg ({1 - p_false_pos:.2f})"]},
            {"label": f"Condition ({1 - p_healthy:.2f})", "sub": ["Test Pos (0,95)", "Test Neg (0,05)"]},
        ],
        "outcomes": ["Healthy & Pos", "Healthy & Neg", "Condition & Pos", "Condition & Neg"],
    }

    prompt = (
        f"Refer to the medical screening tree diagram shown in the figure.\n"
        f"A clinic runs screening tests for a condition:\n"
        f"• {healthy_pct}% of patients tested do NOT have the condition (P(Healthy) = {p_healthy:.2f})\n"
        f"• For a healthy person, the test has a {false_pos_pct}% false positive rate (P(Positive | Healthy) = {p_false_pos:.2f})\n\n"
        f"Calculate the probability that a randomly chosen patient is Healthy BUT tests Positive."
    ).replace(".", ",")
    explanation = (
        f"Step 1: Multiply along the Healthy → Test Positive branch [M].\n"
        f"Step 2: Calculate: {p_healthy:.2f} × {p_false_pos:.2f} = {p_healthy_tested_pos:.4f} [M].\n"
        f"Step 3: Probability = {p_healthy_tested_pos:.4f} ({p_healthy_tested_pos * 100:.2f}%) [A]."
    ).replace(".", ",")
    return _build_question_payload(
        subskill_id="29_medical_screening_tree_diagram",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the probability of being healthy by the false positive rate.",
        tier_2=f"{p_healthy:.2f} × {p_false_pos:.2f} = {p_healthy_tested_pos:.4f}".replace(".", ","),
        tier_3=f"The probability is {p_healthy_tested_pos * 100:.2f}%.".replace(".", ","),
        r=r,
        diagram_spec=d_spec_29,
    )


def generate_30_three_offspring_gender_outcomes(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of all 3 children being girls from a binary tree diagram."""
    p_girl = 0.50
    p_all_girls = 0.50 ** 3  # 0.125 = 1/8
    pct = p_all_girls * 100.0

    correct_ans = f"P(3 Girls) = 1/2 × 1/2 × 1/2 = 1/8 (or {_fmt(p_all_girls, 3)}; {_fmt_pct(pct, 1)})"
    custom_options = [
        correct_ans,
        f"P(3 Girls) = 1/2 × 3 = 3/2 (150%)",
        f"P(3 Girls) = 1/3 (33,3%)",
        f"P(3 Girls) = 1/6 (16,7%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A genetic counsellor uses a tree diagram to model the genders of three consecutive children in a family.\n"
        f"Assume the probability of having a boy or a girl on each birth is equally likely at 1/2 (50%).\n\n"
        f"Calculate the probability that all three children are girls (GGG)."
    )
    explanation = (
        f"Step 1: Total possible outcomes in 3-child sample space = 2³ = 8 equally likely outcomes [M].\n"
        f"Step 2: Multiply along the Girl → Girl → Girl branches: 1/2 × 1/2 × 1/2 = 1/8 [M].\n"
        f"Step 3: P(3 Girls) = 1/8 = {_fmt(p_all_girls, 3)} ({_fmt_pct(pct, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="30_three_offspring_gender_outcomes",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply 1/2 by 1/2 by 1/2.",
        tier_2="(1/2)³ = 1/8.",
        tier_3="The probability is 1/8 (12,5%).",
        r=r,
    )


def generate_31_quality_control_inspection_stages(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of passing two successive quality control stages in manufacturing."""
    p_stage1 = 0.95  # 95% pass electronic check
    p_stage2 = 0.98  # 98% pass physical packaging check
    p_pass_both = p_stage1 * p_stage2  # 0.931 = 93.1%

    correct_ans = f"P(Approved for sale) = 0,95 × 0,98 = {_fmt(p_pass_both, 3)} ({_fmt_pct(p_pass_both * 100, 1)})"
    custom_options = [
        correct_ans,
        f"P(Approved for sale) = 0,95 + 0,98 = 1,93",
        f"P(Approved for sale) = 0,95 (95,0%)",
        f"P(Approved for sale) = 0,05 × 0,02 = 0,001 (0,1%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An electronics assembly line in Port Elizabeth tests manufactured circuit boards in two successive stages:\n"
        f"• Stage 1 (Automated diagnostic): 95% pass rate (P = 0,95)\n"
        f"• Stage 2 (Physical stress test): 98% pass rate among Stage 1 survivors (P = 0,98)\n\n"
        f"Calculate the overall probability that a manufactured board passes both inspection stages and is approved for sale."
    )
    explanation = (
        f"Step 1: Multiply branch probabilities: P(Stage 1 Pass) × P(Stage 2 Pass | Stage 1 Pass) [M].\n"
        f"Step 2: Calculate: 0,95 × 0,98 = {_fmt(p_pass_both, 3)} [M].\n"
        f"Step 3: Approval probability = {_fmt(p_pass_both, 3)} ({_fmt_pct(p_pass_both * 100, 1)}) [A]."
    )
    return _build_question_payload(
        subskill_id="31_quality_control_inspection_stages",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the two passing probabilities together.",
        tier_2="0,95 × 0,98 = 0,931.",
        tier_3="Overall probability is 93,1%.",
        r=r,
    )


def generate_32_successive_draw_tree_diagram(r: random.Random) -> Dict[str, Any]:
    """Trace a tree diagram path without replacement for two successive draws."""
    blue = r.choice([4, 5, 6])
    red = r.choice([3, 4])
    total = blue + red
    p_num = blue * red
    p_den = total * (total - 1)
    frac_str = _fmt_frac(p_num, p_den)

    d_spec_32 = {
        "diagram_role": "context",
        "kind": "tree_diagram",
        "branches": [{"label": "Blue", "sub": ["Blue", "Red"]}, {"label": "Red", "sub": ["Blue", "Red"]}],
        "outcomes": ["Blue-Blue", "Blue-Red", "Red-Blue", "Red-Red"],
        "title": f"Successive Draws Without Replacement ({blue} Blue, {red} Red)",
        "stages": [
            {"name": "First Draw", "outcomes": [{"name": "Blue", "prob": f"{blue}/{total}"}, {"name": "Red", "prob": f"{red}/{total}"}]},
            {"name": "Second Draw", "outcomes": [{"name": "Red", "prob": f"{red}/{total - 1}"}]},
        ],
    }
    correct_ans = f"P(Blue then Red) = {blue}/{total} × {red}/{total - 1} = {frac_str}"

    custom_options = [
        correct_ans,
        f"P(Blue then Red) = 5/8 × 3/8 = 15/64",
        f"P(Blue then Red) = 5/8 + 3/7 = 59/56",
        f"P(Blue then Red) = 1/56",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the tree diagram for drawing pens without replacement.\n"
        f"A bag contains {blue} blue pens and {red} red pens (total {total} pens).\n"
        f"Two pens are drawn one after the other without replacement.\n\n"
        f"Using tree diagram branching principles, state the branch probabilities and calculate P(Blue first and Red second)."
    )
    explanation = (
        f"Step 1: First branch P(Blue) = 5/8 [M].\n"
        f"Step 2: Second branch P(Red | Blue first) = 3/7 (total pens reduced to 7) [M].\n"
        f"Step 3: P(Blue and Red) = 5/8 × 3/7 = 15/56 [A]."
    )
    return _build_question_payload(
        subskill_id="32_successive_draw_tree_diagram",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The first branch is 5/8. After removing one pen, 7 pens remain, so the second branch is 3/7.",
        tier_2="Multiply the two branches: (5/8) × (3/7).",
        tier_3="The probability is 15/56.",
        r=r,
        diagram_spec=d_spec_32,
    )
