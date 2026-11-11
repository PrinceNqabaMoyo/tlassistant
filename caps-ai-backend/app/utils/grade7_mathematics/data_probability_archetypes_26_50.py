"""Grade 7 Mathematics - Probability: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/Mathematics_Gr7/Term 4/02. Probability.md & Probability Studio.md
Focus: Consonant letters, complementary events (P(E) + P(not E) = 1), relative frequency vs theoretical probability, two coin toss trees, coin & die compound events, two-way tables, predicting frequencies, and diagnostic autopsy.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional


# 26. Probability letter tiles word consonants
def arch_26_probability_letter_tiles_word_consonants(rng: random.Random) -> Dict[str, Any]:
    # Word: "PROBABILITY" -> 11 letters, 4 vowels, 7 consonants
    ans = "7/11"
    prompt = (
        "The letter tiles of the word **P R O B A B I L I T Y** are placed in a bag.\n\n"
        "Calculate the probability of selecting a **consonant**."
    )
    sol = (
        "**Calculation:**\n"
        "Total letters $n(S) = 11$.\n"
        "Consonants: **P, R, B, B, L, T, Y** ($7$ consonants).\n\n"
        "$$P(\\text{Consonant}) = \\frac{7}{11}$$"
    )
    return {
        "id": f"g7_pr_26_{rng.randint(100000, 999999)}",
        "subskill": "26_probability_letter_tiles_word_consonants",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "7/11",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_26",
        "hints": {
            "tier_1": "11 total letters minus 4 vowels = 7 consonants.",
            "tier_2": "Fraction: 7 / 11.",
            "tier_3": "7/11."
        },
        "misconception_tags": ["counting_y_as_vowel_in_consonants"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 7 consonants", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates probability = 7/11", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 27. Probability letter tiles specific letter multiplicity
def arch_27_probability_letter_tiles_specific_letter_multiplicity(rng: random.Random) -> Dict[str, Any]:
    # Word: "MATHEMATICS" -> 11 letters; M: 2, A: 2, T: 2, H: 1, E: 1, I: 1, C: 1, S: 1
    # P(T) = 2/11
    ans = "2/11"
    prompt = (
        "Each letter of the word **M A T H E M A T I C S** is written on a separate card and placed in a box.\n"
        "A card is selected at random.\n\n"
        "What is the probability of selecting the letter **T**?"
    )
    sol = (
        "**Calculation:**\n"
        "Total letters in MATHEMATICS $= 11$.\n"
        "The letter **T** appears twice ($2$ favourable outcomes).\n\n"
        "$$P(\\text{T}) = \\frac{2}{11}$$"
    )
    return {
        "id": f"g7_pr_27_{rng.randint(100000, 999999)}",
        "subskill": "27_probability_letter_tiles_specific_letter_multiplicity",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "2/11",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_27",
        "hints": {
            "tier_1": "Count how many times 'T' appears in MATHEMATICS.",
            "tier_2": "T appears 2 times out of 11 total letters.",
            "tier_3": "2/11."
        },
        "misconception_tags": ["counting_letter_only_once_ignoring_duplicates"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 2 occurrences of T", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates probability = 2/11", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 28. Complementary events sum to one rule
def arch_28_complementary_events_sum_to_one_rule(rng: random.Random) -> Dict[str, Any]:
    ans = "P(E) + P(not E) = 1; the sum of the probabilities of an event and its complement always equals 1"
    prompt = (
        "In probability theory, what is the fundamental mathematical relationship between "
        "an event $E$ and its complement $\\text{not } E$?\n\n"
        "State the equation and explain what it means."
    )
    sol = (
        "**Complementary Events Law:**\n"
        "$$P(E) + P(\\text{not } E) = 1$$\n\n"
        "**Explanation:**\n"
        "Either event $E$ occurs or it does not occur. Together, an event and its complement "
        "cover the entire sample space ($100\\%$ certainty), so their probabilities must always add up to $1$."
    )
    return {
        "id": f"g7_pr_28_{rng.randint(100000, 999999)}",
        "subskill": "28_complementary_events_sum_to_one_rule",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "P(E) + P(not E) = 1; together they cover all possible outcomes",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_28",
        "hints": {
            "tier_1": "If chance of rain is 30%, what is chance of no rain?",
            "tier_2": "30% + 70% = 100% (or 0,3 + 0,7 = 1).",
            "tier_3": "P(E) + P(not E) = 1."
        },
        "misconception_tags": ["complementary_sum_not_equaling_one"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States formula P(E) + P(not E) = 1", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains they cover all possible outcomes", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 29. Complementary events find not a
def arch_29_complementary_events_find_not_a(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice([25, 35, 40, 65, 80])
    comp_pct = 100 - pct
    dec = pct / 100
    comp_dec = round(1 - dec, 2)
    dec_str = str(dec).replace(".", "{,}")
    comp_str = str(comp_dec).replace(".", "{,}")
    ans = f"{comp_str} (or {comp_pct}%)"
    prompt = (
        f"The probability that it will rain tomorrow in Rustenburg is $P(\\text{{Rain}}) = {dec_str}$ (or ${pct}\\%$).\n\n"
        f"Calculate the probability that it will **NOT rain** tomorrow."
    )
    sol = (
        f"**Calculation using Complementary Events:**\n"
        f"$$P(\\text{{No Rain}}) = 1 - P(\\text{{Rain}})$$\n"
        f"$$P(\\text{{No Rain}}) = 1 - {dec_str} = {comp_str} \\quad (\\text{{or }} 100\\% - {pct}\\% = {comp_pct}\\%)$$"
    )
    return {
        "id": f"g7_pr_29_{rng.randint(100000, 999999)}",
        "subskill": "29_complementary_events_find_not_a",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{comp_str} (or {comp_pct}%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_29",
        "hints": {
            "tier_1": f"Subtract {dec_str} from 1 (or {pct}% from 100%).",
            "tier_2": f"1 - {dec_str} = {comp_str}.",
            "tier_3": f"{comp_str} (or {comp_pct}%)."
        },
        "misconception_tags": ["arithmetic_subtraction_error_decimals"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Uses 1 - P(Rain)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates {comp_str} ({comp_pct}%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 30. Experimental probability relative frequency definition
def arch_30_experimental_probability_relative_frequency_definition(rng: random.Random) -> Dict[str, Any]:
    ans = "Relative frequency = (Number of times event occurred) / (Total number of trials conducted)"
    prompt = (
        "In probability experiments:\n\n"
        "1. Define what **relative frequency** (experimental probability) is.\n"
        "2. State its calculation formula."
    )
    sol = (
        "**1. Definition:**\n"
        "Relative frequency is the estimate of probability based on the actual observed results of conducting an experiment.\n\n"
        "**2. Formula:**\n"
        "$$\\text{Relative Frequency} = \\frac{\\text{Number of times event occurred}}{\\text{Total number of trials (repetitions)}} = \\frac{f}{n}$$"
    )
    return {
        "id": f"g7_pr_30_{rng.randint(100000, 999999)}",
        "subskill": "30_experimental_probability_relative_frequency_definition",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Relative frequency = Observed frequency / Total trials",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_30",
        "hints": {
            "tier_1": "How many times did it actually happen divided by how many times you tried?",
            "tier_2": "Frequency divided by number of trials.",
            "tier_3": f"{ans}"
        },
        "misconception_tags": ["confusing_experimental_with_theoretical_probability"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Defines experimental probability based on observed results", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States formula f / n", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 31. Experimental probability calculate relative frequency
def arch_31_experimental_probability_calculate_relative_frequency(rng: random.Random) -> Dict[str, Any]:
    trials = 50
    heads = rng.randint(22, 28)
    dec = round(heads / trials, 2)
    dec_str = str(dec).replace(".", "{,}")
    ans = f"{heads}/50 = {dec_str} (or {int(dec*100)}%)"
    prompt = (
        f"A learner tosses a coin {trials} times and records that Heads appeared **{heads} times**.\n\n"
        f"1. Calculate the **relative frequency** of Heads for this experiment as a decimal.\n"
        f"2. How does this compare with the theoretical probability of $0{{,}}5$?"
    )
    sol = (
        f"**1. Relative Frequency Calculation:**\n"
        f"$$\\text{{Relative Frequency}} = \\frac{{{heads}}}{{{trials}}} = \\frac{{{heads * 2}}}{{100}} = {dec_str}$$\n\n"
        f"**2. Comparison:**\n"
        f"The experimental relative frequency is ${dec_str}$, which is very close to the theoretical probability of $0{{,}}5$ ($50\\%$)."
    )
    return {
        "id": f"g7_pr_31_{rng.randint(100000, 999999)}",
        "subskill": "31_experimental_probability_calculate_relative_frequency",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"Relative frequency = {heads}/50 = {dec_str}; close to theoretical 0,5",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_31",
        "hints": {
            "tier_1": f"Divide {heads} by {trials}.",
            "tier_2": f"{heads} / 50 = {dec_str}.",
            "tier_3": f"{dec_str} is close to 0,5."
        },
        "misconception_tags": ["relative_frequency_calculation_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Calculates relative frequency = {dec_str}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Compares with theoretical probability 0,5", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 32. Law of large numbers experimental vs theoretical
def arch_32_law_of_large_numbers_experimental_vs_theoretical(rng: random.Random) -> Dict[str, Any]:
    ans = "As the number of trials increases, the relative frequency gets closer and closer to the theoretical probability"
    prompt = (
        "A learner rolls a fair die 10 times and gets a '6' only once (relative frequency = 1/10 = 0,1).\n"
        "Another learner rolls the die 1 000 times and gets a '6' 165 times (relative frequency = 165/1 000 = 0,165).\n\n"
        "Explain what happens to the relative frequency of an event as the number of experimental trials increases "
        "(The Law of Large Numbers)."
    )
    sol = (
        "**The Law of Large Numbers:**\n"
        "When an experiment is repeated a small number of times, random fluctuations can cause the relative frequency "
        "to differ noticeably from the theoretical probability ($1/6 \\approx 0{,}167$).\n\n"
        "However, as the number of trials increases significantly (e.g. from 10 to 1 000+ trials), "
        "the **relative frequency becomes closer and closer to the theoretical probability**."
    )
    return {
        "id": f"g7_pr_32_{rng.randint(100000, 999999)}",
        "subskill": "32_law_of_large_numbers_experimental_vs_theoretical",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "As trials increase, relative frequency converges to theoretical probability",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_32",
        "hints": {
            "tier_1": "Does flipping a coin 1 000 times give closer to 50% than flipping it 4 times?",
            "tier_2": "More trials smooth out random luck.",
            "tier_3": "Relative frequency approaches theoretical probability as trials increase."
        },
        "misconception_tags": ["expecting_exact_theoretical_in_small_trials"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States relative frequency approaches theoretical probability", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Specifies that this occurs as number of trials increases", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 33. Fair vs biased coin experiment
def arch_33_fair_vs_biased_coin_experiment(rng: random.Random) -> Dict[str, Any]:
    ans = "Biased; Heads appeared 85% of the time in 100 tosses, which deviates far beyond random chance"
    prompt = (
        "In a coin-tossing experiment, a coin is flipped $100$ times. It lands on Heads $85$ times and Tails $15$ times.\n\n"
        "1. Is this coin likely to be **fair** or **biased**? Justify your conclusion.\n"
        "2. What results would you expect from a fair coin tossed $100$ times?"
    )
    sol = (
        "**1. Evaluation:**\n"
        "The coin is almost certainly **biased**.\n"
        "- **Justification:** The relative frequency of Heads is $\\frac{85}{100} = 85\\%$, "
        "which deviates hugely from the expected theoretical probability of $50\\%$.\n\n"
        "**2. Expected Results for a Fair Coin:**\n"
        "For a fair coin, we would expect roughly $50$ Heads and $50$ Tails (e.g. between $45$ and $55$ Heads)."
    )
    return {
        "id": f"g7_pr_33_{rng.randint(100000, 999999)}",
        "subskill": "33_fair_vs_biased_coin_experiment",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Biased because 85% is far from 50%; fair coin would yield roughly 50 heads",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_33",
        "hints": {
            "tier_1": "Is 85 heads out of 100 normal for a fair coin?",
            "tier_2": "No, a fair coin should give around 50 heads.",
            "tier_3": "Biased coin."
        },
        "misconception_tags": ["failing_to_detect_statistical_bias"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies coin as biased with 85% justification", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States expected ~50 heads for fair coin", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 34. Fair vs biased die experiment
def arch_34_fair_vs_biased_die_experiment(rng: random.Random) -> Dict[str, Any]:
    ans = "Fair die: each number appears roughly 100 times (1/6 of 600); Biased if one number heavily dominates"
    prompt = (
        "A player rolls a standard die $600$ times.\n\n"
        "1. For a **fair** die, approximately how many times should each number ($1$ to $6$) appear?\n"
        "2. If the number '6' appeared $350$ times, what conclusion can be drawn?"
    )
    sol = (
        "**1. Fair Die Expected Frequency:**\n"
        "Each face has probability $P = \\frac{1}{6}$.\n"
        "$$\\text{Expected Count} = 600 \\times \\frac{1}{6} = 100\\text{ times each}$$\n\n"
        "**2. Conclusion:**\n"
        "If '6' appears $350$ times out of $600$ ($58\\%$ of all rolls instead of $16{,}7\\%$), "
        "the die is heavily **biased (loaded)** toward the number 6."
    )
    return {
        "id": f"g7_pr_34_{rng.randint(100000, 999999)}",
        "subskill": "34_fair_vs_biased_die_experiment",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Expected 100 times each; 350 times means die is heavily biased/loaded",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_34",
        "hints": {
            "tier_1": "Divide 600 by 6.",
            "tier_2": "Each face should appear about 100 times.",
            "tier_3": "Expected is 100; 350 means loaded/biased."
        },
        "misconception_tags": ["expected_frequency_calculation_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates expected frequency = 100 times", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Concludes die is biased/loaded", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 35. Two coins sample space listing tree
def arch_35_two_coins_sample_space_listing_tree(rng: random.Random) -> Dict[str, Any]:
    ans = "S = {(H; H); (H; T); (T; H); (T; T)}; n(S) = 4"
    prompt = (
        "Two fair coins are tossed simultaneously.\n\n"
        "1. List all the possible outcomes in the sample space $S$.\n"
        "2. What is the total number of possible outcomes $n(S)$?"
    )
    sol = (
        "**Sample Space for Two Coins:**\n"
        "Using $H$ for Heads and $T$ for Tails:\n"
        "$$S = \\{(H; H);\\; (H; T);\\; (T; H);\\; (T; T)\\}$$\n"
        "$$\\text{Total outcomes: } n(S) = 2 \\times 2 = 4$$"
    )
    return {
        "id": f"g7_pr_35_{rng.randint(100000, 999999)}",
        "subskill": "35_two_coins_sample_space_listing_tree",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "S = {(H; H); (H; T); (T; H); (T; T)}; n(S) = 4",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_35",
        "hints": {
            "tier_1": "First coin can be H or T. Second coin can be H or T.",
            "tier_2": "Combinations: HH, HT, TH, TT.",
            "tier_3": "4 outcomes."
        },
        "misconception_tags": ["treating_HT_and_TH_as_identical_in_sample_space"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Lists all 4 outcomes {(H,H), (H,T), (T,H), (T,T)}", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States n(S) = 4", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 36. Two coins probability both heads
def arch_36_two_coins_probability_both_heads(rng: random.Random) -> Dict[str, Any]:
    ans = "1/4 (or 25% or 0,25)"
    prompt = (
        "Two fair coins are flipped at the same time.\n\n"
        "What is the probability that **both coins land on Heads**?"
    )
    sol = (
        "**Calculation:**\n"
        "Sample space $S = \\{(H; H); (H; T); (T; H); (T; T)\\}$, so $n(S) = 4$.\n"
        "Only $(H; H)$ satisfies the condition ($1$ outcome).\n\n"
        "$$P(\\text{Both Heads}) = \\frac{1}{4} = 0{,}25 = 25\\%$$"
    )
    return {
        "id": f"g7_pr_36_{rng.randint(100000, 999999)}",
        "subskill": "36_two_coins_probability_both_heads",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1/4 (or 25%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_36",
        "hints": {
            "tier_1": "How many outcomes have two heads? Only 1: (H, H).",
            "tier_2": "1 out of 4 total outcomes.",
            "tier_3": "1/4."
        },
        "misconception_tags": ["assuming_1_in_3_chance_for_two_heads"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 1 favourable outcome out of 4", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States probability = 1/4 (25%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 37. Two coins probability one head one tail
def arch_37_two_coins_probability_one_head_one_tail(rng: random.Random) -> Dict[str, Any]:
    ans = "2/4 = 1/2 (or 50%)"
    prompt = (
        "Two fair coins are flipped.\n\n"
        "What is the probability of getting **exactly one Head and one Tail** (in either order)?"
    )
    sol = (
        "**Calculation:**\n"
        "Favourable outcomes: $(H; T)$ and $(T; H)$ ($2$ outcomes).\n"
        "Total outcomes $= 4$.\n\n"
        "$$P(\\text{one Head, one Tail}) = \\frac{2}{4} = \\frac{1}{2} = 50\\%$$"
    )
    return {
        "id": f"g7_pr_37_{rng.randint(100000, 999999)}",
        "subskill": "37_two_coins_probability_one_head_one_tail",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "2/4 = 1/2 = 50%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_37",
        "hints": {
            "tier_1": "Remember order: (H, T) and (T, H) are both favourable!",
            "tier_2": "2 out of 4 outcomes.",
            "tier_3": "2/4 = 1/2 (50%)."
        },
        "misconception_tags": ["counting_only_one_order_for_mixed_coins"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies both (H,T) and (T,H)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies probability to 1/2", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 38. Two coins probability at least one tail
def arch_38_two_coins_probability_at_least_one_tail(rng: random.Random) -> Dict[str, Any]:
    ans = "3/4 (or 75%)"
    prompt = (
        "Two coins are tossed. What is the probability of getting **at least one Tail**?"
    )
    sol = (
        "**Calculation:**\n"
        "'At least one Tail' means $1$ or $2$ tails.\n"
        "Favourable outcomes: $(H; T), (T; H), (T; T)$ ($3$ outcomes).\n"
        "$$\\text{Total outcomes} = 4$$\n\n"
        "$$P(\\text{at least one Tail}) = \\frac{3}{4} = 75\\%$$"
    )
    return {
        "id": f"g7_pr_38_{rng.randint(100000, 999999)}",
        "subskill": "38_two_coins_probability_at_least_one_tail",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "3/4 (or 75%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_38",
        "hints": {
            "tier_1": "The only outcome without a tail is (H, H).",
            "tier_2": "3 out of 4 outcomes have at least one tail.",
            "tier_3": "3/4 (75%)."
        },
        "misconception_tags": ["confusing_at_least_with_exactly"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 3 favourable outcomes", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates probability = 3/4", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 39. Coin and die combined sample space
def arch_39_coin_and_die_combined_sample_space(rng: random.Random) -> Dict[str, Any]:
    ans = "Total outcomes = 2 × 6 = 12 outcomes; {(H; 1), (H; 2), ..., (T; 6)}"
    prompt = (
        "A fair coin is tossed and a fair six-sided die is rolled at the same time.\n\n"
        "1. How many total possible outcomes exist in the combined sample space?\n"
        "2. List three examples of outcomes in this sample space."
    )
    sol = (
        "**1. Total Combined Outcomes:**\n"
        "$$\\text{Total outcomes} = (\\text{Coin outcomes}) \\times (\\text{Die outcomes}) = 2 \\times 6 = 12$$\n\n"
        "**2. Example Outcomes:**\n"
        "Examples include $(H; 1), (H; 6), (T; 4)$."
    )
    return {
        "id": f"g7_pr_39_{rng.randint(100000, 999999)}",
        "subskill": "39_coin_and_die_combined_sample_space",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "12 total outcomes (2 × 6 = 12); e.g. (H; 1), (H; 2), (T; 3)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_39",
        "hints": {
            "tier_1": "Multiply the number of coin sides (2) by die faces (6).",
            "tier_2": "2 × 6 = 12.",
            "tier_3": "12 outcomes."
        },
        "misconception_tags": ["adding_instead_of_multiplying_sample_spaces"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Calculates 2 * 6 = 12 total outcomes", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Provides valid outcome pairs", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 40. Coin and die probability head and even
def arch_40_coin_and_die_probability_head_and_even(rng: random.Random) -> Dict[str, Any]:
    ans = "3/12 = 1/4 (or 25%)"
    prompt = (
        "A fair coin is tossed and a fair six-sided die is rolled.\n\n"
        "What is the probability of obtaining a **Head on the coin AND an even number on the die**?"
    )
    sol = (
        "**Calculation:**\n"
        "Total combined outcomes $= 2 \\times 6 = 12$.\n"
        "Favourable outcomes: $(H; 2), (H; 4), (H; 6)$ ($3$ outcomes).\n\n"
        "$$P(\\text{Head and Even}) = \\frac{3}{12} = \\frac{1}{4} = 25\\%$$"
    )
    return {
        "id": f"g7_pr_40_{rng.randint(100000, 999999)}",
        "subskill": "40_coin_and_die_probability_head_and_even",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "3/12 = 1/4 = 25%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_40",
        "hints": {
            "tier_1": "Head + 2, Head + 4, Head + 6.",
            "tier_2": "3 favourable outcomes out of 12.",
            "tier_3": "3/12 = 1/4."
        },
        "misconception_tags": ["wrong_favourable_count_in_compound_event"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies 3 favourable outcomes", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 1/4", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 41. Two-way table transport survey probability
def arch_41_two_way_table_transport_survey_probability(rng: random.Random) -> Dict[str, Any]:
    # Table: 100 learners total
    # Boys: 30 Bus, 20 Walk (50 boys)
    # Girls: 25 Bus, 25 Walk (50 girls)
    # Total Bus = 55, Total Walk = 45
    ans = "55/100 = 11/20 (or 55%)"
    prompt = (
        "A survey of $100$ Grade 7 learners recorded transport methods:\n\n"
        "| Gender | Bus | Walk | Total |\n"
        "| :--- | :--- | :--- | :--- |\n"
        "| Boys | 30 | 20 | 50 |\n"
        "| Girls | 25 | 25 | 50 |\n"
        "| Total | 55 | 45 | 100 |\n\n"
        "If a learner is chosen at random from the whole group, what is the probability "
        "that the learner **travels by bus**?"
    )
    sol = (
        "**Calculation from Two-Way Table:**\n"
        "Total learners $= 100$.\n"
        "Total learners who travel by bus $= 30 + 25 = 55$.\n\n"
        "$$P(\\text{Bus}) = \\frac{55}{100} = \\frac{11}{20} = 55\\%$$"
    )
    return {
        "id": f"g7_pr_41_{rng.randint(100000, 999999)}",
        "subskill": "41_two_way_table_transport_survey_probability",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "55/100 = 11/20 = 55%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_41",
        "hints": {
            "tier_1": "Look at the 'Total' row under 'Bus'.",
            "tier_2": "55 out of 100.",
            "tier_3": "55/100 = 11/20."
        },
        "misconception_tags": ["reading_single_cell_instead_of_marginal_total"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies total bus riders = 55", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Calculates probability = 11/20 (55%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 42. Two-way table sports gender probability
def arch_42_two_way_table_sports_gender_probability(rng: random.Random) -> Dict[str, Any]:
    # Boys playing soccer = 30 out of 100 -> 30/100 = 3/10
    ans = "30/100 = 3/10 (or 30%)"
    prompt = (
        "Refer to the sports survey table of $100$ learners:\n\n"
        "| Gender | Soccer | Netball | Total |\n"
        "| :--- | :--- | :--- | :--- |\n"
        "| Boys | 30 | 10 | 40 |\n"
        "| Girls | 20 | 40 | 60 |\n"
        "| Total | 50 | 50 | 100 |\n\n"
        "What is the probability that a randomly chosen learner is a **Boy who plays Soccer**?"
    )
    sol = (
        "**Calculation:**\n"
        "The cell for Boys AND Soccer contains $30$ learners.\n"
        "Total learners $= 100$.\n\n"
        "$$P(\\text{Boy and Soccer}) = \\frac{30}{100} = \\frac{3}{10} = 30\\%$$"
    )
    return {
        "id": f"g7_pr_42_{rng.randint(100000, 999999)}",
        "subskill": "42_two_way_table_sports_gender_probability",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "30/100 = 3/10 = 30%",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_42",
        "hints": {
            "tier_1": "Find the intersection cell for Boys and Soccer: 30.",
            "tier_2": "Divide 30 by total 100.",
            "tier_3": "3/10 or 30%."
        },
        "misconception_tags": ["dividing_by_row_total_instead_of_grand_total"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies cell count = 30", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 3/10 (30%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 43. Predicting frequencies from probability
def arch_43_predicting_frequencies_from_probability(rng: random.Random) -> Dict[str, Any]:
    rolls = rng.choice([300, 600, 900, 1200])
    expected_evens = rolls // 2
    ans = f"{expected_evens} times"
    prompt = (
        f"A fair six-sided die is rolled **{rolls} times**.\n\n"
        f"Predict how many times you would expect to roll an **even number**."
    )
    sol = (
        f"**Step 1: Theoretical Probability:**\n"
        f"$$P(\\text{{Even}}) = \\frac{{3}}{{6}} = \\frac{{1}}{{2}}$$\n\n"
        f"**Step 2: Expected Frequency:**\n"
        f"$$\\text{{Expected Frequency}} = n \\times P = {rolls} \\times \\frac{{1}}{{2}} = {expected_evens}\\text{{ times}}$$"
    )
    return {
        "id": f"g7_pr_43_{rng.randint(100000, 999999)}",
        "subskill": "43_predicting_frequencies_from_probability",
        "question_type": "numeric",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{expected_evens} times",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_43",
        "hints": {
            "tier_1": f"Multiply total rolls ({rolls}) by probability (1/2).",
            "tier_2": f"{rolls} ÷ 2 = {expected_evens}.",
            "tier_3": f"{expected_evens} times."
        },
        "misconception_tags": ["multiplying_by_wrong_probability_fraction"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies P(Even) = 1/2", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Calculates expected count = {expected_evens}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 44. Predicting raffle tickets winner probability
def arch_44_predicting_raffle_tickets_winner_probability(rng: random.Random) -> Dict[str, Any]:
    bought = rng.choice([5, 10, 20])
    total_tickets = 200
    pct = round((bought / total_tickets) * 100, 1)
    ans = f"{bought}/200 = {bought // math.gcd(bought, total_tickets)}/{total_tickets // math.gcd(bought, total_tickets)} (or {pct}%)"
    prompt = (
        f"A charity sells $200$ numbered raffle tickets to raise funds for library books.\n"
        f"Zanele buys **{bought} tickets**.\n\n"
        f"What is the probability that Zanele will win the first prize?"
    )
    g = math.gcd(bought, total_tickets)
    s_num = bought // g
    s_den = total_tickets // g
    sol = (
        f"**Calculation:**\n"
        f"Favourable outcomes $= {bought}$ tickets.\n"
        f"Total outcomes $= 200$ tickets.\n\n"
        f"$$P(\\text{{Win}}) = \\frac{{{bought}}}{{200}} = \\frac{{{s_num}}}{{{s_den}}} \\quad (\\text{{or }} {pct}\\%)$$"
    )
    return {
        "id": f"g7_pr_44_{rng.randint(100000, 999999)}",
        "subskill": "44_predicting_raffle_tickets_winner_probability",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": f"{s_num}/{s_den} (or {pct}%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_44",
        "hints": {
            "tier_1": f"Zanele has {bought} chances out of 200.",
            "tier_2": f"Fraction: {bought} / 200. Simplify.",
            "tier_3": f"{s_num}/{s_den}."
        },
        "misconception_tags": ["raffle_probability_fraction_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": f"Sets up {bought}/200", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"Simplifies to {s_num}/{s_den}", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 45. Common misconception Gambler's Fallacy
def arch_45_common_misconception_gamblers_fallacy(rng: random.Random) -> Dict[str, Any]:
    ans = "Probability remains exactly 1/2 (50%); coin tosses are independent and have no memory"
    prompt = (
        "A player tosses a fair coin $4$ times, and it lands on **Heads all 4 times**.\n"
        "The player claims: *'Tails is definitely due on the 5th toss because we have had too many Heads!'*\n\n"
        "1. Is the player's claim mathematically correct?\n"
        "2. What is the actual probability of getting Tails on the 5th toss?\n"
        "3. Explain why the player's thinking is flawed (the Gambler's Fallacy)."
    )
    sol = (
        "**1. Evaluation:**\n"
        "No, the player's claim is incorrect.\n\n"
        "**2. True Probability:**\n"
        "$$P(\\text{Tail on 5th toss}) = \\frac{1}{2} = 50\\%$$\n\n"
        "**3. Explanation (Gambler's Fallacy):**\n"
        "Each toss of a coin is an **independent event**. The coin has no memory of past tosses. "
        "The previous $4$ heads do not affect the physical outcome of the $5$th toss."
    )
    return {
        "id": f"g7_pr_45_{rng.randint(100000, 999999)}",
        "subskill": "45_common_misconception_gamblers_fallacy",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Incorrect; probability is still 1/2; coin has no memory (independent events)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pr_45",
        "hints": {
            "tier_1": "Does the coin remember what it landed on previously?",
            "tier_2": "Every toss is completely independent.",
            "tier_3": "Probability is still 1/2. Coin has no memory."
        },
        "misconception_tags": ["gamblers_fallacy_independence_misconception"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Refutes player claim as incorrect", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States 5th toss probability is still 1/2 (50%)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Explains coin has no memory / events are independent", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 46. Common misconception probability greater than one
def arch_46_common_misconception_probability_greater_than_one(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: Probability cannot exceed 1 (or 100%); a fraction of 8/5 means 160%, which is mathematically impossible"
    prompt = (
        "A learner calculates the probability of selecting a red pen from a pencil case and gives the answer as **$\\frac{8}{5}$**.\n\n"
        "1. Explain why an answer of $\\frac{8}{5}$ is mathematically impossible for a probability.\n"
        "2. What is the maximum possible value any probability can take?"
    )
    sol = (
        "**1. Why $\\frac{8}{5}$ is Impossible:**\n"
        "The number of favourable outcomes cannot exceed the total number of possible outcomes ($n(E) \\le n(S)$). "
        "The value $\\frac{8}{5} = 1{,}6 = 160\\%$, which is greater than $1$. In probability theory, an event cannot occur "
        "more than with $100\\%$ certainty.\n\n"
        "**2. Maximum Value:**\n"
        "The maximum possible probability is **$1$** (or $100\\%$), representing a certain event."
    )
    return {
        "id": f"g7_pr_46_{rng.randint(100000, 999999)}",
        "subskill": "46_common_misconception_probability_greater_than_one",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Probability cannot exceed 1; maximum value is 1 (100%)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_46",
        "hints": {
            "tier_1": "Can something happen 160% of the time?",
            "tier_2": "Favourable items cannot be more than total items.",
            "tier_3": "Maximum probability is 1 (100%)."
        },
        "misconception_tags": ["probability_greater_than_one"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Explains favourable outcomes cannot exceed total outcomes", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States maximum probability is 1 (100%)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 47. Common misconception 50-50 fallacy
def arch_47_common_misconception_50_50_fallacy(rng: random.Random) -> Dict[str, Any]:
    ans = "False; two possible outcomes does not mean they are equally likely"
    prompt = (
        "A person says: *'Tomorrow I will either win the national lottery or I won't win. "
        "Since there are only two outcomes, the probability of winning is 50%.'*\n\n"
        "Explain the mathematical fallacy in this reasoning."
    )
    sol = (
        "**The 50-50 Fallacy:**\n"
        "Just because an experiment has only two possible outcomes does **not** mean the outcomes are equally likely. "
        "The theoretical formula $P = \\frac{1}{2}$ applies *only* when outcomes have the exact same likelihood of occurring "
        "(such as a balanced fair coin). "
        "In the lottery, there are millions of losing combinations and only one winning combination, so the probability of winning "
        "is extremely close to $0$, not $50\\%$."
    )
    return {
        "id": f"g7_pr_47_{rng.randint(100000, 999999)}",
        "subskill": "47_common_misconception_50_50_fallacy",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Two outcomes does not mean equally likely; winning lottery has millions of losing possibilities",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_47",
        "hints": {
            "tier_1": "You will either sprout wings and fly to school or you won't. Is that 50%?",
            "tier_2": "Two possibilities do not mean equal chances.",
            "tier_3": "Fallacy: outcomes are not equally likely."
        },
        "misconception_tags": ["assuming_binary_outcomes_are_equally_likely"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States having two outcomes does not imply equal likelihood", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Explains lottery winning outcomes are far less frequent than losing", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 48. Common misconception negative probability
def arch_48_common_misconception_negative_probability(rng: random.Random) -> Dict[str, Any]:
    ans = "Error: Probability cannot be negative; minimum possible probability is 0 (impossible event)"
    prompt = (
        "A student calculates a probability of **$-0{,}25$**.\n\n"
        "State whether this is possible, and explain the mathematical constraint on probability values."
    )
    sol = (
        "**Mathematical Constraint:**\n"
        "A probability cannot be negative. For any event $E$:\n"
        "$$0 \\le P(E) \\le 1$$\n"
        "The minimum possible probability is $0$, which corresponds to an **impossible event**. "
        "A negative count of outcomes is physically and mathematically meaningless."
    )
    return {
        "id": f"g7_pr_48_{rng.randint(100000, 999999)}",
        "subskill": "48_common_misconception_negative_probability",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "Impossible; probability must lie between 0 and 1 inclusive",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_48",
        "hints": {
            "tier_1": "Can a probability be below zero?",
            "tier_2": "0 is the lowest possible probability.",
            "tier_3": "0 <= P(E) <= 1."
        },
        "misconception_tags": ["negative_probability_error"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "States probability cannot be negative", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "States range constraint 0 <= P(E) <= 1", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 49. Common misconception forgetting to simplify fraction
def arch_49_common_misconception_forgetting_to_simplify_fraction(rng: random.Random) -> Dict[str, Any]:
    ans = "4/12 simplifies to 1/3 (divide numerator and denominator by HCF = 4)"
    prompt = (
        "A learner solves a probability question and writes the final answer as **$\\frac{4}{12}$**.\n\n"
        "1. Is $\\frac{4}{12}$ in simplest form?\n"
        "2. Provide the fully simplified fraction and state the highest common factor (HCF) used."
    )
    sol = (
        "**1. Simplest Form Check:**\n"
        "No, $\\frac{4}{12}$ is not in simplest form because both numbers share a common factor greater than $1$.\n\n"
        "**2. Simplification:**\n"
        "The highest common factor (HCF) of $4$ and $12$ is **$4$**.\n"
        "$$\\frac{4 \\div 4}{12 \\div 4} = \\frac{1}{3}$$"
    )
    return {
        "id": f"g7_pr_49_{rng.randint(100000, 999999)}",
        "subskill": "49_common_error_forgetting_to_simplify_fraction",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "No; simplifies to 1/3 using HCF = 4",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "math_g7_pr_49",
        "hints": {
            "tier_1": "Divide both numbers by 4.",
            "tier_2": "4 ÷ 4 = 1, 12 ÷ 4 = 3.",
            "tier_3": "1/3."
        },
        "misconception_tags": ["forgetting_to_simplify_probability_fraction"],
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp1", "desc": "Identifies fraction is not simplified", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Simplifies to 1/3 using HCF = 4", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }


# 50. Probability comprehensive diagnostic autopsy
def arch_50_probability_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    ans = "Statement 1: False (coin has no memory); Statement 2: True (P + P_comp = 1); Statement 3: False (P <= 1)"
    prompt = (
        "Evaluate whether each of the following three probability statements is True or False, "
        "and provide a concise mathematical reason:\n\n"
        "1. **Statement 1:** 'After rolling five 6s in a row on a fair die, the probability of rolling another 6 on the next roll is much less than 1/6.'\n"
        "2. **Statement 2:** 'If the probability of rain is 0,35, the probability that it will not rain is 0,65.'\n"
        "3. **Statement 3:** 'A probability of 1,2 means that an event is 20% more than certain.'"
    )
    sol = (
        "**Diagnostic Autopsy:**\n\n"
        "**1. Statement 1: False.**\n"
        "Each roll of a fair die is an independent event with no memory of past rolls. The probability remains strictly $\\frac{1}{6}$.\n\n"
        "**2. Statement 2: True.**\n"
        "By the complementary event rule: $P(\\text{no rain}) = 1 - 0{,}35 = 0{,}65$.\n\n"
        "**3. Statement 3: False.**\n"
        "Probability cannot exceed $1$ (or $100\\%$). An event cannot be 'more than certain'."
    )
    return {
        "id": f"g7_pr_50_{rng.randint(100000, 999999)}",
        "subskill": "50_probability_comprehensive_diagnostic_autopsy",
        "question_type": "paragraph",
        "prompt": prompt,
        "prompt_latex": prompt,
        "correct_answer": ans,
        "sample_answer": "1. False (independent rolls); 2. True (1 - 0,35 = 0,65); 3. False (P cannot exceed 1)",
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "math_g7_pr_50",
        "hints": {
            "tier_1": "Test each against the axioms of probability: independent trials, complement law, 0 <= P <= 1.",
            "tier_2": "Statement 1 is False, 2 is True, 3 is False.",
            "tier_3": "False, True, False."
        },
        "misconception_tags": ["gamblers_fallacy_independence_misconception", "probability_greater_than_one"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Refutes Statement 1 (independent rolls)", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Confirms Statement 2 (complement law 1 - 0,35 = 0,65)", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Refutes Statement 3 (probability cannot exceed 1)", "marks": 1, "editable": True}
            ],
            "carry_forward_rule": "none"
        }
    }
