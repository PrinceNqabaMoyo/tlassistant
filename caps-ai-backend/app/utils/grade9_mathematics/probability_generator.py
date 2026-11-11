"""Grade 9 Mathematics — Probability Generator (Deterministic 6-Pillar Contract).

Curriculum Alignment:
- Grade 9 Term 4: Probability
- South African National Curriculum Standards (Senior Phase Mathematics)
- Single and Compound Event Probability:
  * Relative frequency (experimental) vs theoretical probability P(E) = n(E) / n(S)
  * Probability scale from 0 (impossible) to 1 (certain)
  * Complementary events: P(not E) = 1 - P(E)
  * Two-way contingency tables: joint and marginal probabilities
  * Tree diagrams for compound events: with replacement (independent) and without replacement (dependent)

6 Pillars:
- Deterministic seed generation with zero LLM authority
- Directed solution graph with dependency tracking
- Adaptive deconstruction (atomic elementary sub-drills on error)
- Rich 3-tier hints (Conceptual, Procedural with probability formula, Concrete Step-by-Step with actual numbers)
- Misconception-targeted error taxonomy
- Native DiagramRenderer specs (kind: 'probability_spinner', 'contingency_table_and_tree', 'contingency_table')
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.grade9_mathematics._math_common import rng

TOPIC = "grade9_math_probability"
LO = "math9_probability"


def generate_grade9_probability_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = rng(seed)

    archetype_choices = [
        "theoretical_vs_experimental",
        "bag_marbles_without_replacement",
        "contingency_table_probability",
        "tree_diagram_two_coin_dice",
    ]

    selected_subskill = subskill or mode
    if selected_subskill in archetype_choices:
        archetype = selected_subskill
    else:
        archetype = r.choice(archetype_choices)

    qid = f"g9_prob_{seed or r.randint(1000, 9999)}_{uuid.uuid4().hex[:6]}"

    if archetype == "theoretical_vs_experimental":
        # Spinner with colored sectors (e.g., Red, Blue, Green, Yellow)
        # 8 equal sectors: 3 Red, 2 Blue, 2 Green, 1 Yellow
        sectors = {"Red": 3, "Blue": 2, "Green": 2, "Yellow": 1}
        total_sectors = 8
        target_color = r.choice(["Red", "Blue", "Green", "Yellow"])
        n_target = sectors[target_color]
        
        # Experimental trial: spinner spun 200 times
        total_spins = 200
        # Expected count = total_spins * (n_target / 8)
        exp_count = int(total_spins * (n_target / total_sectors))
        actual_spins = exp_count + r.choice([-6, -4, -2, 2, 4, 6])
        rel_freq = round(actual_spins / total_spins, 3)
        theo_prob = round(n_target / total_sectors, 3)

        question_text = (
            f"A fair circular spinner has $8$ identical, equal sectors labelled as follows:\n"
            f"- $3$ Red sectors\n"
            f"- $2$ Blue sectors\n"
            f"- $2$ Green sectors\n"
            f"- $1$ Yellow sector\n\n"
            f"1. Calculate the **theoretical probability** of landing on **{target_color}** on a single spin, "
            f"expressing your answer as a simplified fraction.\n"
            f"2. In an experiment, the spinner was spun $N = {total_spins}$ times and landed on {target_color} "
            f"a total of ${actual_spins}$ times. Calculate the **relative frequency** (experimental probability).\n"
            f"3. Explain what happens to the relative frequency as the number of spins increases from $200$ to $10\\,000$."
        )

        gcd_val = math.gcd(n_target, total_sectors)
        simp_num = n_target // gcd_val
        simp_den = total_sectors // gcd_val
        frac_str = f"\\frac{{{simp_num}}}{{{simp_den}}}"

        steps = [
            {"id": "S1", "statement": f"Theoretical $P(\\text{{{target_color}}}) = \\frac{{n(\\text{{{target_color}}})}}{{n(S)}} = \\frac{{{n_target}}}{{{total_sectors}}} = {frac_str}$", "reason": "classical probability formula", "deps": []},
            {"id": "S2", "statement": f"Relative Frequency $= \\frac{{{actual_spins}}}{{{total_spins}}} = {rel_freq}$", "reason": "experimental probability formula", "deps": []},
            {"id": "S3", "statement": f"Law of Large Numbers: As the number of trials increases, the relative frequency gets closer and closer to the theoretical probability ({frac_str} = {theo_prob}).", "reason": "Law of Large Numbers", "deps": ["S1", "S2"]},
        ]

        hints = [
            f"Theoretical probability = (Number of favorable sectors) ÷ (Total sectors) = {n_target} ÷ 8.",
            f"Relative frequency = (Observed count) ÷ (Total trials) = {actual_spins} ÷ {total_spins}.",
            "The Law of Large Numbers states that with more trials, experimental relative frequency converges to theoretical probability.",
        ]

        error_tax = [
            {
                "id": "err_inverted_probability",
                "tag": "misconception_probability_inversion",
                "condition": f"Wrote 8 / {n_target}",
                "feedback": "Probability is always favorable outcomes divided by total outcomes (a number between 0 and 1). Never divide total by favorable.",
            },
        ]

        sample_answer = (
            f"1. Theoretical $P(\\text{{{target_color}}}) = \\frac{{{n_target}}}{{{total_sectors}}} = {frac_str}$\n"
            f"2. Relative frequency $= \\frac{{{actual_spins}}}{{{total_spins}}} = {rel_freq}$\n"
            f"3. By the **Law of Large Numbers**, as the number of trials increases, the experimental relative frequency becomes more reliable and converges closer and closer to the theoretical probability (${frac_str}$ or ${theo_prob}$).",
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "probability_spinner",
            "caption": "8-sector spinner (3 Red, 2 Blue, 2 Green, 1 Yellow)",
            "sectors": [
                {"label": "Red", "color": "#ef4444", "weight": 3},
                {"label": "Blue", "color": "#3b82f6", "weight": 2},
                {"label": "Green", "color": "#10b981", "weight": 2},
                {"label": "Yellow", "color": "#eab308", "weight": 1},
            ],
        }

        correct_ans = f"Theoretical: {simp_num}/{simp_den}; Relative Freq: {rel_freq}"
        subskill_id = "theoretical_vs_experimental"
        reason_code = "P(E) = n(E)/n(S) and Law of Large Numbers"
        marks = 4

    elif archetype == "bag_marbles_without_replacement":
        # Dependent compound events: Drawing 2 marbles without replacement
        num_red = r.randint(4, 7)
        num_blue = r.randint(3, 5)
        total_marbles = num_red + num_blue
        
        # Scenario: Probability of drawing two Red marbles (RR) or two Blue marbles (BB)
        # P(RR) = (num_red / total) * ((num_red - 1) / (total - 1))
        p_rr_num = num_red * (num_red - 1)
        p_rr_den = total_marbles * (total_marbles - 1)
        gcd_rr = math.gcd(p_rr_num, p_rr_den)
        simp_rr_num = p_rr_num // gcd_rr
        simp_rr_den = p_rr_den // gcd_rr

        question_text = (
            f"A bag contains ${num_red}$ Red marbles and ${num_blue}$ Blue marbles "
            f"(total of ${total_marbles}$ marbles).\n\n"
            f"Two marbles are drawn at random from the bag **one after the other without replacement**.\n\n"
            f"1. What is the probability that the first marble drawn is Red?\n"
            f"2. Given that the first marble is Red, what is the probability that the second marble drawn is also Red?\n"
            f"3. Calculate the probability of drawing two Red marbles in a row ($P(\\text{{Red and Red}})$)."
        )

        steps = [
            {"id": "S1", "statement": f"$P(\\text{{1st Red}}) = \\frac{{{num_red}}}{{{total_marbles}}}$", "reason": "first draw probability", "deps": []},
            {"id": "S2", "statement": f"$P(\\text{{2nd Red}} \\mid \\text{{1st Red}}) = \\frac{{{num_red - 1}}}{{{total_marbles - 1}}}$", "reason": "without replacement reduction", "deps": ["S1"]},
            {"id": "S3", "statement": f"$P(\\text{{Red and Red}}) = \\frac{{{num_red}}}{{{total_marbles}}} \\times \\frac{{{num_red - 1}}}{{{total_marbles - 1}}} = \\frac{{{p_rr_num}}}{{{p_rr_den}}} = \\frac{{{simp_rr_num}}}{{{simp_rr_den}}}$", "reason": "multiplication rule for dependent events", "deps": ["S1", "S2"]},
        ]

        hints = [
            "Because the marble is NOT replaced, both the number of red marbles and the total number of marbles decrease by 1 for the second draw.",
            f"1st Red: $\\frac{{{num_red}}}{{{total_marbles}}}$. 2nd Red: $\\frac{{{num_red - 1}}}{{{total_marbles - 1}}}$.",
            f"Multiply the two probabilities: $\\frac{{{num_red}}}{{{total_marbles}}} \\times \\frac{{{num_red - 1}}}{{{total_marbles - 1}}} = \\frac{{{simp_rr_num}}}{{{simp_rr_den}}}$.",
        ]

        error_tax = [
            {
                "id": "err_treated_as_with_replacement",
                "tag": "misconception_without_replacement",
                "condition": f"Calculated ({num_red}/{total_marbles})^2",
                "feedback": "The question states WITHOUT replacement. The second marble is drawn from a smaller bag of {total_marbles - 1} marbles, with {num_red - 1} red marbles remaining.",
            },
        ]

        sample_answer = (
            f"1. $P(\\text{{1st Red}}) = \\frac{{{num_red}}}{{{total_marbles}}}$\n"
            f"2. $P(\\text{{2nd Red}} \\mid \\text{{1st Red}}) = \\frac{{{num_red - 1}}}{{{total_marbles - 1}}}$\n"
            f"3. $P(\\text{{Red and Red}}) = \\frac{{{num_red}}}{{{total_marbles}}} \\times \\frac{{{num_red - 1}}}{{{total_marbles - 1}}} = \\frac{{{p_rr_num}}}{{{p_rr_den}}} = \\frac{{{simp_rr_num}}}{{{simp_rr_den}}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "contingency_table_and_tree",
            "caption": f"Tree diagram for 2 draws without replacement ({num_red} Red, {num_blue} Blue)",
        }

        correct_ans = f"{simp_rr_num}/{simp_rr_den}"
        subskill_id = "bag_marbles_without_replacement"
        reason_code = "dependent events: P(A and B) = P(A) * P(B|A)"
        marks = 4

    elif archetype == "contingency_table_probability":
        # Two-way contingency table: e.g. Activity chosen (Music vs Sport) by Boys vs Girls
        b_music = r.randint(15, 25)
        b_sport = r.randint(30, 45)
        g_music = r.randint(25, 35)
        g_sport = r.randint(20, 30)
        
        tot_boys = b_music + b_sport
        tot_girls = g_music + g_sport
        tot_music = b_music + g_music
        tot_sport = b_sport + g_sport
        grand_total = tot_boys + tot_girls

        question_text = (
            f"A two-way table shows the extracurricular choices of $N = {grand_total}$ Grade 9 learners:\n\n"
            f"| Gender | Music | Sport | Total |\n"
            f"| :--- | :---: | :---: | :---: |\n"
            f"| Boys | ${b_music}$ | ${b_sport}$ | ${tot_boys}$ |\n"
            f"| Girls | ${g_music}$ | ${g_sport}$ | ${tot_girls}$ |\n"
            f"| **Total** | **${tot_music}$** | **${tot_sport}$** | **${grand_total}$** |\n\n"
            f"A learner is selected at random from the entire group.\n"
            f"1. What is the probability that the selected learner is a Girl ($P(\\text{{Girl}})$)?\n"
            f"2. What is the probability that the learner chose Music ($P(\\text{{Music}})$)?\n"
            f"3. What is the probability that the learner is a Boy who chose Sport ($P(\\text{{Boy and Sport}})$)?\n"
            f"4. If it is known that the selected learner is a Girl, what is the probability she chose Sport ($P(\\text{{Sport}} \\mid \\text{{Girl}})$)?"
        )

        steps = [
            {"id": "S1", "statement": f"$P(\\text{{Girl}}) = \\frac{{\\text{{Total Girls}}}}{{\\text{{Grand Total}}}} = \\frac{{{tot_girls}}}{{{grand_total}}}$", "reason": "marginal probability", "deps": []},
            {"id": "S2", "statement": f"$P(\\text{{Music}}) = \\frac{{\\text{{Total Music}}}}{{\\text{{Grand Total}}}} = \\frac{{{tot_music}}}{{{grand_total}}}$", "reason": "marginal probability", "deps": []},
            {"id": "S3", "statement": f"$P(\\text{{Boy and Sport}}) = \\frac{{{b_sport}}}{{{grand_total}}}$", "reason": "joint probability", "deps": []},
            {"id": "S4", "statement": f"$P(\\text{{Sport}} \\mid \\text{{Girl}}) = \\frac{{{g_sport}}}{{{tot_girls}}}$", "reason": "conditional probability", "deps": []},
        ]

        hints = [
            f"For questions 1-3, divide by the grand total ({grand_total}).",
            "For question 4, you are given that the learner is a Girl, so restrict the denominator to the row total for Girls only.",
            f"P(Girl) = {tot_girls}/{grand_total}; P(Music) = {tot_music}/{grand_total}; P(Boy and Sport) = {b_sport}/{grand_total}; P(Sport | Girl) = {g_sport}/{tot_girls}.",
        ]

        error_tax = [
            {
                "id": "err_conditional_denominator",
                "tag": "misconception_conditional_denominator",
                "condition": f"Divided conditional probability by grand total {grand_total} instead of row total {tot_girls}",
                "feedback": "When given a condition (e.g., 'Given that the learner is a Girl'), your denominator becomes the total for that specific sub-group (Total Girls), NOT the grand total.",
            },
        ]

        sample_answer = (
            f"1. $P(\\text{{Girl}}) = \\frac{{{tot_girls}}}{{{grand_total}}}$\n"
            f"2. $P(\\text{{Music}}) = \\frac{{{tot_music}}}{{{grand_total}}}$\n"
            f"3. $P(\\text{{Boy and Sport}}) = \\frac{{{b_sport}}}{{{grand_total}}}$\n"
            f"4. $P(\\text{{Sport}} \\mid \\text{{Girl}}) = \\frac{{{g_sport}}}{{{tot_girls}}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "contingency_table",
            "caption": f"Two-way table of {grand_total} learners",
        }

        correct_ans = f"P(Girl) = {tot_girls}/{grand_total}; P(Sport|Girl) = {g_sport}/{tot_girls}"
        subskill_id = "contingency_table_probability"
        reason_code = "contingency table and conditional probability"
        marks = 4

    else:
        # tree_diagram_two_coin_dice: Two independent events (e.g. Tossing a coin and rolling a die)
        # Coin: H, T. Die: 1, 2, 3, 4, 5, 6. Total outcomes = 2 * 6 = 12.
        die_cond = r.choice(["even number", "prime number", "number greater than 4"])
        if die_cond == "even number":
            fav_die = [2, 4, 6]
        elif die_cond == "prime number":
            fav_die = [2, 3, 5]
        else:
            fav_die = [5, 6]
        
        n_die = len(fav_die)
        coin_side = r.choice(["Heads", "Tails"])
        fav_combos = n_die  # e.g. (Heads, 2), (Heads, 4), (Heads, 6)
        total_outcomes = 12
        gcd_val = math.gcd(fav_combos, total_outcomes)

        question_text = (
            f"An experiment consists of tossing a fair coin once and rolling a fair 6-sided die once.\n\n"
            f"1. Draw a tree diagram or list the complete sample space ($S$) of all possible outcomes.\n"
            f"2. State the total number of outcomes in the sample space ($n(S)$).\n"
            f"3. Calculate the probability of getting **{coin_side}** on the coin and a **{die_cond}** on the die."
        )

        steps = [
            {"id": "S1", "statement": f"Sample space $n(S) = 2 \\times 6 = {total_outcomes}$ outcomes", "reason": "fundamental counting principle", "deps": []},
            {"id": "S2", "statement": f"Favorable die outcomes ({die_cond}): {fav_die} ($n = {n_die}$)", "reason": "die event subset", "deps": []},
            {"id": "S3", "statement": f"$P({coin_side} \\text{{ and }} {die_cond}) = P({coin_side}) \\times P({die_cond}) = \\frac{{1}}{{2}} \\times \\frac{{{n_die}}}{{6}} = \\frac{{{fav_combos}}}{{{total_outcomes}}} = \\frac{{{fav_combos // gcd_val}}}{{{total_outcomes // gcd_val}}}$", "reason": "independent event multiplication", "deps": ["S1", "S2"]},
        ]

        hints = [
            "Tossing a coin has 2 outcomes (H, T); rolling a die has 6 outcomes (1, 2, 3, 4, 5, 6). Total outcomes = 2 × 6 = 12.",
            f"Favorable outcomes with {coin_side} and a {die_cond}: {', '.join(f'({coin_side[0]}, {d})' for d in fav_die)} (total {fav_combos} outcomes).",
            f"Probability = {fav_combos} / 12 = {fav_combos // gcd_val}/{total_outcomes // gcd_val}.",
        ]

        error_tax = [
            {
                "id": "err_added_outcomes",
                "tag": "misconception_sample_space_addition",
                "condition": "Stated sample space is 2 + 6 = 8",
                "feedback": "For compound independent events, MULTIPLY the number of outcomes for each stage: 2 × 6 = 12, do not add.",
            },
        ]

        sample_answer = (
            r"1. Sample space: $\{(H; 1), (H; 2), (H; 3), (H; 4), (H; 5), (H; 6), (T; 1), (T; 2), (T; 3), (T; 4), (T; 5), (T; 6)\}" + "\n"
            f"2. $n(S) = 2 \\times 6 = {total_outcomes}$\n"
            f"3. $P({coin_side} \\text{{ and }} {die_cond}) = \\frac{{1}}{{2}} \\times \\frac{{{n_die}}}{{6}} = \\frac{{{fav_combos}}}{{{total_outcomes}}} = \\frac{{{fav_combos // gcd_val}}}{{{total_outcomes // gcd_val}}}$"
        )

        diagram_spec = {
            "diagram_role": "context",
            "kind": "contingency_table_and_tree",
            "caption": "Tree diagram: Coin toss and 6-sided die",
        }

        correct_ans = f"{fav_combos // gcd_val}/{total_outcomes // gcd_val}"
        subskill_id = "tree_diagram_two_coin_dice"
        reason_code = "independent compound events: P(A) * P(B)"
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
            {"criterion": f"Correct probability formula [{reason_code}]", "marks": 1},
            {"criterion": f"Accurate calculation and simplified fraction {correct_ans}", "marks": marks - 1},
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
        "keywords": ["probability", "relative frequency", "theoretical", "tree diagram", "contingency table", "independent events", "dependent events"],
        "term": 4,
        "caps_weight_percent": 10.0,
        "suggested_duration_mins": 5,
        "minimum_mastery_score": 75,
        "diagram_spec": diagram_spec,
        "modality": "math",
        "seed": seed,
        "solution_graph": {
            "goal": "Calculate single and compound event probabilities",
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
        questions.append(generate_grade9_probability_question(seed=sub_seed, **kwargs))
    return {"questions": questions}
