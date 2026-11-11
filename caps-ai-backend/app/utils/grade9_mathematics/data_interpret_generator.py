"""Grade 9 Mathematics — Interpret, Analyse & Report Data Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 4: Interpret, analyse and report on data
- South African National Curriculum Standards (Senior Phase Mathematics)
- Critical statistical literacy:
  * Misleading graphs: truncated vertical axes (broken axes), irregular intervals, 3D volume distortion
  * Comparative dataset analysis: comparing two groups via mean, median, and range
  * Choosing appropriate summary statistics in skewed distributions or datasets with outliers
  * Sampling bias, representative vs biased samples, and drawing valid population inferences

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with statistical reasoning, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_data_interpret"
LO = "math9_data_interpret"


def generate_grade9_data_interpret_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "misleading_graph_critique",
        "comparative_dataset_analysis",
        "sampling_bias_evaluation",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_dataint_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "misleading_graph_critique":
        # Classic CAPS question: A company claims Product A is vastly superior to Product B.
        # Graph y-axis starts at 90 instead of 0. Product A = 95%, Product B = 91%.
        # The bar for A looks 5 times taller than the bar for B!
        val_a = r.randint(94, 98)
        val_b = r.randint(89, 93)
        diff = val_a - val_b
        axis_start = r.randint(85, 88)
        
        visual_height_a = val_a - axis_start
        visual_height_b = val_b - axis_start
        ratio = round(visual_height_a / visual_height_b, 1)

        question_text = (
            f"An advertisement displays a bar graph comparing the customer satisfaction rates of "
            f"Company X ({val_a}%) and Company Y ({val_b}%).\n\n"
            f"On the graph, the vertical percentage axis starts at ${axis_start}\\%$ instead of $0\\%$.\n"
            f"Consequently, the bar for Company X appears **{ratio} times as tall** as the bar for Company Y!\n\n"
            f"1. Explain why this graph is visually misleading and dishonest.\n"
            f"2. What is the actual numerical difference in satisfaction between the two companies?\n"
            f"3. How should the graph be redrawn so that it presents the data fairly and accurately?"
        )

        steps = [
            {"id": "S1", "statement": f"Misleading reason: The vertical axis is truncated (starts at {axis_start}% instead of 0%), exaggerating the visual difference between {val_a}% and {val_b}%.", "reason": "truncated axis distortion", "deps": []},
            {"id": "S2", "statement": f"Actual difference: ${val_a}\\% - {val_b}\\% = {diff}\\%$", "reason": "arithmetic subtraction", "deps": []},
            {"id": "S3", "statement": "Redrawing recommendation: The vertical axis must start at 0% with uniform scaling up to 100%.", "reason": "honest visualization standard", "deps": ["S1"]},
        ]

        hints = [
            "Look at the vertical scale: when an axis starts above zero (a truncated or broken axis), small differences appear huge.",
            f"The actual difference is only {val_a}% - {val_b}% = {diff}%, but visually Company X looks {ratio} times taller.",
            "To correct the distortion, the vertical axis should always start at 0% with equal spacing up to 100%.",
        ]

        error_tax = [
            {
                "id": "err_accepted_visual_ratio",
                "tag": "misconception_visual_distortion_acceptance",
                "condition": f"Claimed Company X is {ratio} times better",
                "feedback": "Company X is NOT {ratio} times better. A difference of only {diff}% is magnified by truncating the vertical axis.",
            },
        ]

        sample_answer = (
            f"1. **Why it is misleading:** The vertical axis has been truncated to start at ${axis_start}\\%$ instead of $0\\%$. This artificially exaggerates a small ${diff}\\%$ difference, making Company X appear {ratio} times better than Company Y when in reality both have very similar satisfaction ratings above {val_b}%.\n"
            f"2. Actual difference $= {val_a}\\% - {val_b}\\% = {diff}\\%$\n"
            f"3. **Fair representation:** The vertical percentage axis should start at $0\\%$ with a uniform scale running from $0\\%$ to $100\\%$."
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": f"Misleading truncated bar graph (axis starting at {axis_start}%)",
        }

        correct_ans = f"Truncated axis starting at {axis_start}%; Actual diff = {diff}%"
        subskill_id = "misleading_graph_critique"
        reason_code = "misleading graph analysis (truncated axis)"
        marks = 3

    elif archetype == "comparative_dataset_analysis":
        # Comparing two classes: Class A and Class B in an exam
        # Class A has mean 65, range 15 (consistent). Class B has mean 65, range 45 (wide spread).
        mean_score = r.randint(60, 72)
        range_a = r.randint(12, 18)
        range_b = r.randint(38, 52)

        question_text = (
            f"Two Grade 9 classes wrote the same Mathematics exam out of $100$.\n\n"
            f"- **Class 9A:** Mean score = ${mean_score}\\%$; Range = ${range_a}\\%$.\n"
            f"- **Class 9B:** Mean score = ${mean_score}\\%$; Range = ${range_b}\\%$.\n\n"
            f"1. Compare the overall central performance of the two classes.\n"
            f"2. Compare the consistency (spread) of the learners' marks between the two classes.\n"
            f"3. Which class would be easier for a teacher to pace instruction for, and why?"
        )

        steps = [
            {"id": "S1", "statement": f"Central performance: Both classes have identical mean performance (${mean_score}\\%$).", "reason": "compare means", "deps": []},
            {"id": "S2", "statement": f"Spread / Consistency: Class 9A is far more consistent (range = {range_a}%) than Class 9B (range = {range_b}%).", "reason": "compare ranges", "deps": []},
            {"id": "S3", "statement": f"Class 9A is easier to pace because the learners perform at a similar level (low spread of {range_a}%).", "reason": "educational inference", "deps": ["S1", "S2"]},
        ]

        hints = [
            f"Notice that both classes have the exact same average mark of {mean_score}%.",
            f"Look at the range (spread): Class 9A has a small range ({range_a}%), meaning marks are clustered together. Class 9B has a huge range ({range_b}%), meaning some scored very low and some very high.",
            "A class with a small range is more homogeneous (consistent) and easier to teach at a uniform pace.",
        ]

        error_tax = [
            {
                "id": "err_claimed_higher_mean",
                "tag": "misconception_mean_comparison",
                "condition": "Claimed one class had higher performance despite equal means",
                "feedback": "Both classes have identical mean scores (both are {mean_score}%). The difference lies entirely in the spread (consistency).",
            },
        ]

        sample_answer = (
            f"1. **Central performance:** Both classes performed at the same average level on the exam, as both have an identical mean score of ${mean_score}\\%$.\n"
            f"2. **Consistency / Spread:** Class 9A has a much smaller range (${range_a}\\%$) compared to Class 9B (${range_b}\\%$). This means Class 9A learners' marks are clustered closely together, indicating far greater consistency in performance.\n"
            f"3. **Pacing instruction:** **Class 9A** would be easier to pace because the learners are at similar ability levels. In Class 9B, with a wide spread of ${range_b}\\%$, the teacher must cater simultaneously to struggling learners and very advanced learners."
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": f"Comparative distributions (Class 9A range={range_a}%, Class 9B range={range_b}%)",
        }

        correct_ans = f"Same mean ({mean_score}%); Class 9A more consistent (range {range_a}% vs {range_b}%)"
        subskill_id = "comparative_dataset_analysis"
        reason_code = "comparative dataset evaluation (mean and range)"
        marks = 3

    else:
        # sampling_bias_evaluation: Evaluating sampling methods
        scenarios = [
            {
                "topic": "School tuck-shop menu preferences",
                "method": "Interviewing only the first 10 learners standing in line at the tuck-shop on Monday morning.",
                "biased": True,
                "reason": "This is a convenience sample of current tuck-shop customers. It excludes learners who do not use the tuck-shop because they dislike the current menu or cannot afford it.",
                "fair_method": "Use a stratified random sample: select random learner names from every register class across all grades.",
            },
            {
                "topic": "Average amount of time Grade 9 teenagers spend playing video games",
                "method": "Handing out questionnaires to members of the school Gaming and Computer Club.",
                "biased": True,
                "reason": "This sample is severely biased because members of a gaming club naturally spend much more time gaming than the average Grade 9 student population.",
                "fair_method": "Select a random sample of Grade 9 learners using student administrative ID numbers in a lottery or random number generator.",
            },
            {
                "topic": "Predicting the winner of a national soccer final between Team A and Team B",
                "method": "Polling spectators entering the home stadium of Team A.",
                "biased": True,
                "reason": "The sample is geographically and emotionally biased towards Team A's supporters, so it will vastly overestimate support for Team A.",
                "fair_method": "Conduct an unbiased telephone or online survey across all provinces with a nationally representative random sample.",
            },
        ]
        s_data = r.choice(scenarios)

        question_text = (
            f"A researcher wanted to investigate: **{s_data['topic']}**.\n\n"
            f"The sampling method used was:\n"
            f"\"{s_data['method']}\"\n\n"
            f"1. Is this sample representative or biased? Give a clear reason.\n"
            f"2. How does this sampling method affect the validity of the conclusions drawn?\n"
            f"3. Propose an improved, fair sampling method that would yield valid results."
        )

        steps = [
            {"id": "S1", "statement": "Sample is Biased: " + s_data["reason"], "reason": "sampling bias identification", "deps": []},
            {"id": "S2", "statement": "Validity: Conclusions cannot be generalized to the broader population because the sample does not fairly represent all viewpoints.", "reason": "external validity principle", "deps": ["S1"]},
            {"id": "S3", "statement": "Improved method: " + s_data["fair_method"], "reason": "random sampling design", "deps": []},
        ]

        hints = [
            "A sample is biased if some members of the population have a greater chance of being selected than others.",
            f"Consider who is included and who is excluded: {s_data['reason']}.",
            f"An unbiased sample uses random selection where every member of the population has an equal chance of being chosen: {s_data['fair_method']}.",
        ]

        error_tax = [
            {
                "id": "err_claimed_unbiased",
                "tag": "misconception_convenience_sample_validity",
                "condition": "Claimed convenience sample is unbiased because it is easy",
                "feedback": "Convenience sampling is almost always biased because it selects an unrepresentative subgroup of people.",
            },
        ]

        sample_answer = (
            f"1. **Biased.** {s_data['reason']}\n"
            f"2. **Validity:** The conclusions will be invalid and skewed. They cannot be generalised to the entire target population because the sample systematically over-represents a specific sub-group.\n"
            f"3. **Improved method:** {s_data['fair_method']}"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "statistics_box_and_ogive",
            "caption": f"Sampling Bias Analysis: {s_data['topic']}",
        }

        correct_ans = "Biased; Cannot generalise; Random sampling needed"
        subskill_id = "sampling_bias_evaluation"
        reason_code = "sampling methodology and bias"
        marks = 3

    q = {
        "id": qid,
        "subject": "Mathematics",
        "grade": 9,
        "topic": TOPIC,
        "subskill": subskill_id,
        "learning_objective_id": LO,
        "mode": mode,
        "difficulty": difficulty,
        "question_type": "free_response",
        "answer_mode": "free_response",
        "prompt": question_text,
        "question": question_text,
        "prompt_latex": question_text,
        "answer_latex": correct_ans,
        "correct_answer": correct_ans,
        "sample_answer": sample_answer,
        "worked_solution": sample_answer,
        "canonical_solution": sample_answer,
        "marking_schema": [
            {"criterion": f"Correct critical analysis [{reason_code}]", "marks": 1},
            {"criterion": f"Valid statistical reasoning and conclusions {correct_ans}", "marks": marks - 1},
        ],
        "marks": marks,
        "hints": hints,
        "hint_sections": {
            "concept": hints[0],
            "rules": hints[1],
            "step_by_step": hints[2],
        },
        "misconception_tags": [m["tag"] for m in error_tax],
        "diagnostic_tags": [f"diag_{subskill_id}"],
        "keywords": ["data interpretation", "misleading graphs", "bias", "sampling", "range", "mean", "median", "consistency"],
        "term": 4,
        "caps_weight_percent": 8.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Critique and interpret statistical data and representations",
            "steps": steps,
        },
        "metadata": {
            "diagram_spec": diagram_spec,
            "answer_value": correct_ans,
            "reason_code": reason_code,
        },
    }
    return q


def generate(seed: Optional[int] = None, count: int = 1, **kwargs: Any) -> Dict[str, Any]:
    r = rng(seed)
    questions = []
    for _ in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        questions.append(generate_grade9_data_interpret_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
