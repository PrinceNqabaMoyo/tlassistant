"""Grade 10 Mathematics — Term 4: Probability Archetypes 01 to 25.
100% aligned with South African CAPS Curriculum (Grade 10 Mathematics: Probability).
Covers:
- Relative frequency vs theoretical probability, Law of Large Numbers
- Sample space and theoretical probability for single-stage experiments (dice, words, cards)
- Complementary, impossible, and certain events
- Addition rule: general formula, solving for union, intersection, and individual events
- Mutually exclusive events: definition, testing, and addition rule
- Exhaustive events
- Two-event Venn diagrams: reading values, probabilities, solving for unknown x, solving for neither
- Two-way contingency tables: marginal totals, single events, intersections, unions, complements
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


def _make_venn_diagram_svg(
    n_a_only: int,
    n_inter: int,
    n_b_only: int,
    n_neither: int,
    label_a: str = "A",
    label_b: str = "B",
    title: str = "Venn Diagram of Two Events",
) -> str:
    """Generates an SVG Venn diagram for two overlapping events in sample space S."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 220" width="100%" height="auto" style="background:#FFFFFF; font-family:sans-serif;">
    <text x="250" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1A202C">{title}</text>
    <!-- Sample Space Box -->
    <rect x="40" y="30" width="420" height="175" rx="8" fill="#F8FAFC" stroke="#4A5568" stroke-width="2"/>
    <text x="55" y="52" font-size="14" font-weight="bold" fill="#2D3748">S</text>
    <!-- Circle A -->
    <circle cx="190" cy="120" r="65" fill="#3182CE" fill-opacity="0.2" stroke="#2B6CB0" stroke-width="2.5"/>
    <text x="155" y="60" text-anchor="middle" font-size="13" font-weight="bold" fill="#2B6CB0">{label_a}</text>
    <!-- Circle B -->
    <circle cx="290" cy="120" r="65" fill="#38A169" fill-opacity="0.2" stroke="#2F855A" stroke-width="2.5"/>
    <text x="325" y="60" text-anchor="middle" font-size="13" font-weight="bold" fill="#2F855A">{label_b}</text>
    <!-- Counts -->
    <text x="155" y="125" text-anchor="middle" font-size="14" font-weight="bold" fill="#1A202C">{n_a_only}</text>
    <text x="240" y="125" text-anchor="middle" font-size="14" font-weight="bold" fill="#C53030">{n_inter}</text>
    <text x="325" y="125" text-anchor="middle" font-size="14" font-weight="bold" fill="#1A202C">{n_b_only}</text>
    <text x="80" y="185" text-anchor="middle" font-size="13" font-weight="bold" fill="#4A5568">{n_neither}</text>
</svg>"""
    return svg


# -----------------------------------------------------------------------------
# 01. Relative frequency calculation
# -----------------------------------------------------------------------------
def arch_01_relative_frequency_calculation(rng: random.Random) -> Dict[str, Any]:
    trials = rng.choice([50, 80, 100, 200])
    successes = rng.randint(int(0.35 * trials), int(0.65 * trials))
    f_frac = Fraction(successes, trials)
    dec_val = successes / trials
    dec_str = _fmt_katex(dec_val)

    prompt = (
        f"A learner tosses a coin {trials} times and observes that it lands heads up {successes} times.\n\n"
        f"1. State the formula for the relative frequency of an event.\n"
        f"2. Calculate the relative frequency of getting heads, expressed as a simplified fraction.\n"
        f"3. Express this relative frequency as a decimal."
    )

    worked = (
        f"**1. Formula:**\n"
        f"$$\\text{{Relative Frequency}} = \\frac{{\\text{{Number of successful trials}}}}{{\\text{{Total number of trials}}}}$$\n\n"
        f"**2. Calculation as a simplified fraction:**\n"
        f"$$\\text{{Relative Frequency}} = \\frac{{{successes}}}{{{trials}}} = {_fmt_frac(f_frac)}$$\n\n"
        f"**3. Decimal representation:**\n"
        f"$$\\text{{Relative Frequency}} = {dec_str}$$"
    )

    ans = f"{_fmt_frac(f_frac)} or {_fmt_dec(dec_val)}"

    return {
        "id": f"g10_prob_01_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"\text{{Relative Frequency}} = {_fmt_frac(f_frac)} = {dec_str}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "01_relative_frequency_calculation",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of relative frequency formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct simplified fraction ({_fmt_frac(f_frac)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct decimal ({_fmt_dec(dec_val)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Divide the number of times heads occurred by the total number of tosses.",
            "2_concept": "Relative frequency = (number of occurrences) / (total trials).",
            "3_breakdown": f"Relative frequency = {successes}/{trials} = {_fmt_frac(f_frac)}.",
        },
        "misconception_tags": ["relative_frequency_ratio_inversion"],
    }


# -----------------------------------------------------------------------------
# 02. Relative vs theoretical probability comparison
# -----------------------------------------------------------------------------
def arch_02_relative_vs_theoretical_probability_comparison(rng: random.Random) -> Dict[str, Any]:
    trials_small = 20
    heads_small = rng.choice([7, 8, 12, 13])
    rf_small = heads_small / trials_small

    trials_large = 1000
    heads_large = rng.choice([495, 502, 508, 492])
    rf_large = heads_large / trials_large

    prompt = (
        f"A fair coin is tossed in two separate experiments:\n\n"
        f"- Experiment 1: {trials_small} tosses resulted in {heads_small} heads (Relative Frequency = {_fmt_katex(rf_small)}).\n"
        f"- Experiment 2: {trials_large} tosses resulted in {heads_large} heads (Relative Frequency = {_fmt_katex(rf_large)}).\n\n"
        f"1. State the theoretical probability of tossing heads with a fair coin.\n"
        f"2. Which experiment yielded a relative frequency closer to the theoretical probability?\n"
        f"3. Explain this observation using the Law of Large Numbers."
    )

    worked = (
        f"**1. Theoretical Probability:**\n"
        f"$$P(\\text{{Heads}}) = \\frac{{1}}{{2}} = 0{{,}}5$$\n\n"
        f"**2. Comparison:**\n"
        f"- Experiment 1 relative frequency: {_fmt_katex(rf_small)}\n"
        f"- Experiment 2 relative frequency: {_fmt_katex(rf_large)}\n"
        f"**Experiment 2** is much closer to $0{{,}}5$.\n\n"
        f"**3. Law of Large Numbers:**\n"
        f"As the number of trials increases, the empirical relative frequency of an event approaches "
        f"its theoretical probability."
    )

    ans = f"P(Heads)=0,5; Experiment 2 is closer; Law of Large Numbers"

    return {
        "id": f"g10_prob_02_{rng.randint(100000, 999999)}",
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
        "subskill": "02_relative_vs_theoretical_probability_comparison",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Theoretical probability P(Heads) = 1/2 or 0,5", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Identification of Experiment 2 as closer", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Explanation referencing Law of Large Numbers / more trials", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "The theoretical probability of getting heads is 1/2 = 0,5.",
            "2_concept": "With a large number of trials, relative frequency gets closer to the theoretical probability.",
            "3_breakdown": f"Experiment 2 has {trials_large} trials, making its relative frequency {_fmt_dec(rf_large)} very close to 0,5.",
        },
        "misconception_tags": ["law_of_large_numbers_misconception"],
    }


# -----------------------------------------------------------------------------
# 03. Sample space listing single stage
# -----------------------------------------------------------------------------
def arch_03_sample_space_listing_single_stage(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice(["spinner", "cards_suits", "months", "days"])
    if context == "spinner":
        n_sectors = rng.choice([6, 8, 10])
        elements = [str(i) for i in range(1, n_sectors + 1)]
        desc = f"spinning an equal-section spinner numbered 1 to {n_sectors}"
    elif context == "cards_suits":
        elements = ["Hearts", "Diamonds", "Clubs", "Spades"]
        desc = "selecting the suit of a card from a standard deck"
    elif context == "months":
        elements = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        desc = "selecting a month of the year at random"
    else:
        elements = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        desc = "selecting a day of the week at random"

    n_s = len(elements)
    s_set = "{" + ", ".join(elements) + "}"

    prompt = (
        f"Consider the random experiment of {desc}.\n\n"
        f"1. Write down the sample space $S$ using set notation.\n"
        f"2. State the total number of possible outcomes, $n(S)$."
    )

    worked = (
        f"**1. Sample Space $S$:**\n"
        f"$$S = {s_set}$$\n\n"
        f"**2. Number of outcomes:**\n"
        f"$$n(S) = {n_s}$$"
    )

    ans = f"n(S) = {n_s}"

    return {
        "id": f"g10_prob_03_{rng.randint(100000, 999999)}",
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
        "subskill": "03_sample_space_listing_single_stage",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 2,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 2,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct list of outcomes in sample space S", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct count n(S) = {n_s}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "List all possible distinct outcomes inside curly brackets { }.",
            "2_concept": "The sample space S is the set of all possible outcomes of an experiment.",
            "3_breakdown": f"S = {s_set}, so n(S) = {n_s}.",
        },
        "misconception_tags": ["sample_space_omission"],
    }


# -----------------------------------------------------------------------------
# 04. Theoretical probability fair die
# -----------------------------------------------------------------------------
def arch_04_theoretical_probability_fair_die(rng: random.Random) -> Dict[str, Any]:
    events = [
        ("rolling an even number", [2, 4, 6]),
        ("rolling a prime number", [2, 3, 5]),
        ("rolling a number greater than 4", [5, 6]),
        ("rolling a factor of 6", [1, 2, 3, 6]),
        ("rolling a multiple of 3", [3, 6]),
        ("rolling an odd number", [1, 3, 5]),
    ]
    chosen = rng.sample(events, 2)
    ev1_name, ev1_pts = chosen[0]
    ev2_name, ev2_pts = chosen[1]

    p1 = Fraction(len(ev1_pts), 6)
    p2 = Fraction(len(ev2_pts), 6)

    prompt = (
        "A fair six-sided die with faces numbered 1 to 6 is rolled once. "
        "Calculate the theoretical probability of:\n\n"
        f"1. {ev1_name}.\n"
        f"2. {ev2_name}.\n\n"
        "Give your answers as simplified fractions."
    )

    worked = (
        "Sample space: $S = \\{1, 2, 3, 4, 5, 6\\}$, so $n(S) = 6$.\n\n"
        f"**1. {ev1_name.capitalize()}:**\n"
        f"Favourable outcomes: $\\{{{', '.join(str(x) for x in ev1_pts)}\\}}$, so $n(E_1) = {len(ev1_pts)}$.\n"
        f"$$P(E_1) = \\frac{{{len(ev1_pts)}}}{{6}} = {_fmt_frac(p1)}$$\n\n"
        f"**2. {ev2_name.capitalize()}:**\n"
        f"Favourable outcomes: $\\{{{', '.join(str(x) for x in ev2_pts)}\\}}$, so $n(E_2) = {len(ev2_pts)}$.\n"
        f"$$P(E_2) = \\frac{{{len(ev2_pts)}}}{{6}} = {_fmt_frac(p2)}$$"
    )

    ans = f"1: {_fmt_frac(p1)}, 2: {_fmt_frac(p2)}"

    return {
        "id": f"g10_prob_04_{rng.randint(100000, 999999)}",
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
        "subskill": "04_theoretical_probability_fair_die",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct probability for {ev1_name} ({_fmt_frac(p1)})", "marks": 1.5, "editable": True},
                {"id": "mp_2", "desc": f"Correct probability for {ev2_name} ({_fmt_frac(p2)})", "marks": 1.5, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Count how many numbers on the die satisfy each condition and divide by 6.",
            "2_concept": "P(E) = n(E) / n(S) where n(S) = 6.",
            "3_breakdown": f"Outcomes for 1: {ev1_pts} -> {_fmt_frac(p1)}. Outcomes for 2: {ev2_pts} -> {_fmt_frac(p2)}.",
        },
        "misconception_tags": ["prime_number_1_confusion", "die_probability_denominator_error"],
    }


# -----------------------------------------------------------------------------
# 05. Theoretical probability word letters
# -----------------------------------------------------------------------------
def arch_05_theoretical_probability_word_letters(rng: random.Random) -> Dict[str, Any]:
    words = ["ALGEBRA", "STATISTICS", "PROBABILITY", "MATHEMATICS", "GEOMETRY"]
    word = rng.choice(words)
    letters = list(word)
    total_n = len(letters)
    vowels = [ch for ch in letters if ch in "AEIOU"]
    consonants = [ch for ch in letters if ch not in "AEIOU"]

    # Pick a specific letter that appears
    target_char = rng.choice(list(set(letters)))
    count_target = letters.count(target_char)

    p_target = Fraction(count_target, total_n)
    p_vowel = Fraction(len(vowels), total_n)
    p_consonant = Fraction(len(consonants), total_n)

    prompt = (
        f"A letter is chosen at random from the word **{word}**.\n\n"
        f"1. State the total number of letters in the word, $n(S)$.\n"
        f"2. Calculate the probability that the chosen letter is the letter **{target_char}**.\n"
        f"3. Calculate the probability that the chosen letter is a vowel.\n"
        f"4. Calculate the probability that the chosen letter is a consonant."
    )

    worked = (
        f"Total letters: $n(S) = {total_n}$.\n\n"
        f"**2. Letter '{target_char}':**\n"
        f"The letter '{target_char}' appears {count_target} time(s).\n"
        f"$$P(\\text{{'{target_char}'}}) = \\frac{{{count_target}}}{{{total_n}}} = {_fmt_frac(p_target)}$$\n\n"
        f"**3. Vowel:**\n"
        f"Vowels in {word}: {vowels} ($n = {len(vowels)}$).\n"
        f"$$P(\\text{{Vowel}}) = \\frac{{{len(vowels)}}}{{{total_n}}} = {_fmt_frac(p_vowel)}$$\n\n"
        f"**4. Consonant:**\n"
        f"$$P(\\text{{Consonant}}) = 1 - P(\\text{{Vowel}}) = \\frac{{{len(consonants)}}}{{{total_n}}} = {_fmt_frac(p_consonant)}$$"
    )

    ans = f"n(S)={total_n}, P({target_char})={_fmt_frac(p_target)}, P(Vowel)={_fmt_frac(p_vowel)}, P(Consonant)={_fmt_frac(p_consonant)}"

    return {
        "id": f"g10_prob_05_{rng.randint(100000, 999999)}",
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
        "subskill": "05_theoretical_probability_word_letters",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct n(S) = {total_n}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Probability of letter {target_char} ({_fmt_frac(p_target)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Probability of vowel ({_fmt_frac(p_vowel)})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Probability of consonant ({_fmt_frac(p_consonant)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Count the total number of letters and how many times the target letter or vowels appear.",
            "2_concept": "P(E) = n(E) / n(S). Vowels and consonants are complementary.",
            "3_breakdown": f"Total = {total_n}. '{target_char}' count = {count_target}. Vowels = {len(vowels)}.",
        },
        "misconception_tags": ["repeated_letter_counting_error"],
    }


# -----------------------------------------------------------------------------
# 06. Theoretical probability deck of cards
# -----------------------------------------------------------------------------
def arch_06_theoretical_probability_deck_of_cards(rng: random.Random) -> Dict[str, Any]:
    card_events = [
        ("a Heart", 13, Fraction(13, 52)),
        ("an Ace", 4, Fraction(4, 52)),
        ("a King or Queen", 8, Fraction(8, 52)),
        ("a black card", 26, Fraction(26, 52)),
        ("a picture card (Jack, Queen, or King)", 12, Fraction(12, 52)),
    ]
    chosen = rng.sample(card_events, 2)
    ev1, c1, p1 = chosen[0]
    ev2, c2, p2 = chosen[1]

    prompt = (
        "A card is chosen at random from a standard, well-shuffled pack of 52 playing cards. "
        "Calculate the probability of selecting:\n\n"
        f"1. {ev1.capitalize()}.\n"
        f"2. {ev2.capitalize()}.\n\n"
        "Give your answers as simplified fractions."
    )

    worked = (
        "A standard pack has $n(S) = 52$ cards.\n\n"
        f"**1. Probability of {ev1}:**\n"
        f"There are {c1} such cards in the deck.\n"
        f"$$P(\\text{{{ev1}}}) = \\frac{{{c1}}}{{52}} = {_fmt_frac(p1)}$$\n\n"
        f"**2. Probability of {ev2}:**\n"
        f"There are {c2} such cards in the deck.\n"
        f"$$P(\\text{{{ev2}}}) = \\frac{{{c2}}}{{52}} = {_fmt_frac(p2)}$$"
    )

    ans = f"1: {_fmt_frac(p1)}, 2: {_fmt_frac(p2)}"

    return {
        "id": f"g10_prob_06_{rng.randint(100000, 999999)}",
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
        "subskill": "06_theoretical_probability_deck_of_cards",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct probability for {ev1} ({_fmt_frac(p1)})", "marks": 1.5, "editable": True},
                {"id": "mp_2", "desc": f"Correct probability for {ev2} ({_fmt_frac(p2)})", "marks": 1.5, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "A standard deck has 52 cards: 4 suits of 13 cards each, and 4 of each card rank.",
            "2_concept": "P(E) = n(E) / 52.",
            "3_breakdown": f"Counts: {ev1} = {c1} -> {_fmt_frac(p1)}; {ev2} = {c2} -> {_fmt_frac(p2)}.",
        },
        "misconception_tags": ["standard_deck_structure_confusion"],
    }


# -----------------------------------------------------------------------------
# 07. Complementary event probability
# -----------------------------------------------------------------------------
def arch_07_complementary_event_probability(rng: random.Random) -> Dict[str, Any]:
    denom = rng.choice([5, 8, 10, 12, 20])
    num = rng.randint(1, denom - 1)
    p_a = Fraction(num, denom)
    p_not_a = 1 - p_a

    prompt = (
        f"The probability that it will rain in Johannesburg on a particular afternoon is "
        f"$P(\\text{{Rain}}) = {_fmt_frac(p_a)}$.\n\n"
        f"1. State the formula for the probability of the complementary event, $P(\\text{{not }} A)$.\n"
        f"2. Calculate the probability that it will NOT rain.\n"
        f"3. Express your answer as both a fraction and a percentage."
    )

    pct = float(p_not_a) * 100.0
    pct_str = _fmt_katex(pct)

    worked = (
        f"**1. Formula:**\n"
        f"$$P(\\text{{not }} A) = 1 - P(A)$$\n\n"
        f"**2. Calculation:**\n"
        f"$$P(\\text{{No rain}}) = 1 - {_fmt_frac(p_a)} = {_fmt_frac(p_not_a)}$$\n\n"
        f"**3. Percentage:**\n"
        f"$${_fmt_frac(p_not_a)} \\times 100\\% = {pct_str}\\%$$"
    )

    ans = f"{_fmt_frac(p_not_a)} or {_fmt_dec(pct)}%"

    return {
        "id": f"g10_prob_07_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"P(\text{{not Rain}}) = {_fmt_frac(p_not_a)} = {pct_str}\%",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "07_complementary_event_probability",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of complement rule P(not A) = 1 - P(A)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct fraction ({_fmt_frac(p_not_a)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct percentage ({_fmt_dec(pct)}%)", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Subtract the given probability from 1.",
            "2_concept": "P(not A) = 1 - P(A). The sum of an event and its complement is always 1.",
            "3_breakdown": f"1 - {_fmt_frac(p_a)} = {_fmt_frac(p_not_a)}.",
        },
        "misconception_tags": ["complement_subtraction_from_one_error"],
    }


# -----------------------------------------------------------------------------
# 08. Impossible and certain events
# -----------------------------------------------------------------------------
def arch_08_impossible_and_certain_events(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Consider a standard six-sided die with numbers 1 to 6.\n\n"
        "1. What is the probability of rolling a number greater than 6? What term describes this type of event?\n"
        "2. What is the probability of rolling a number less than 7? What term describes this type of event?\n"
        "3. Complete the statement: For any event $E$, the probability must satisfy $a \\le P(E) \\le b$. State the values of $a$ and $b$."
    )

    worked = (
        "**1. Rolling a number > 6:**\n"
        "Favourable outcomes = 0. $$P(E) = \\frac{0}{6} = 0$$\n"
        "This is an **impossible event**.\n\n"
        "**2. Rolling a number < 7:**\n"
        "Favourable outcomes = 6. $$P(E) = \\frac{6}{6} = 1$$\n"
        "This is a **certain event**.\n\n"
        "**3. Probability bounds:**\n"
        "$$0 \\le P(E) \\le 1$$\n"
        "So $a = 0$ and $b = 1$."
    )

    ans = "1: 0 (impossible), 2: 1 (certain), 3: a=0, b=1"

    return {
        "id": f"g10_prob_08_{rng.randint(100000, 999999)}",
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
        "subskill": "08_impossible_and_certain_events",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "P = 0 and 'impossible event'", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "P = 1 and 'certain event'", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Bounds: a = 0 and b = 1", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "An impossible event has probability 0; a certain event has probability 1.",
            "2_concept": "Probabilities always range from 0 (impossible) to 1 (certain).",
            "3_breakdown": "P(>6) = 0 (impossible). P(<7) = 1 (certain). Bounds are [0, 1].",
        },
        "misconception_tags": ["probability_bounds_scale_error"],
    }


# -----------------------------------------------------------------------------
# 09. Addition rule general calculation
# -----------------------------------------------------------------------------
def arch_09_addition_rule_general_calculation(rng: random.Random) -> Dict[str, Any]:
    denom = 20
    p_inter_n = rng.choice([2, 3, 4])
    p_a_n = p_inter_n + rng.randint(4, 7)
    p_b_n = p_inter_n + rng.randint(3, 6)
    p_union_n = p_a_n + p_b_n - p_inter_n

    p_a = Fraction(p_a_n, denom)
    p_b = Fraction(p_b_n, denom)
    p_inter = Fraction(p_inter_n, denom)
    p_union = Fraction(p_union_n, denom)

    prompt = (
        f"Two events $A$ and $B$ in a sample space satisfy:\n\n"
        f"$$P(A) = {_fmt_frac(p_a)}, \\quad P(B) = {_fmt_frac(p_b)}, \\quad P(A \\cap B) = {_fmt_frac(p_inter)}$$\n\n"
        f"1. Write down the general addition rule for any two events $A$ and $B$.\n"
        f"2. Calculate $P(A \\cup B)$.\n"
        f"3. State whether events $A$ and $B$ are mutually exclusive, with reason."
    )

    worked = (
        f"**1. General Addition Rule:**\n"
        f"$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$\n\n"
        f"**2. Calculation:**\n"
        f"$$P(A \\cup B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - {_fmt_frac(p_inter)} = {_fmt_frac(p_union)}$$\n\n"
        f"**3. Mutual Exclusivity:**\n"
        f"No, because $P(A \\cap B) = {_fmt_frac(p_inter)} \\neq 0$."
    )

    ans = f"P(A U B) = {_fmt_frac(p_union)}, Not mutually exclusive"

    return {
        "id": f"g10_prob_09_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"P(A \cup B) = {_fmt_frac(p_union)}, \, \text{{Not mutually exclusive}}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "09_addition_rule_general_calculation",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement of addition rule formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct substitution and calculation ({_fmt_frac(p_union)})", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Correct statement that events are not mutually exclusive", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add P(A) and P(B), then subtract P(A and B).",
            "2_concept": "P(A or B) = P(A) + P(B) - P(A and B).",
            "3_breakdown": f"P(A U B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - {_fmt_frac(p_inter)} = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["addition_rule_intersection_omission"],
    }


# -----------------------------------------------------------------------------
# 10. Addition rule solve intersection
# -----------------------------------------------------------------------------
def arch_10_addition_rule_solve_intersection(rng: random.Random) -> Dict[str, Any]:
    p_a = Fraction(rng.randint(5, 7), 10)
    p_b = Fraction(rng.randint(4, 6), 10)
    # P(A U B) must be <= 1 and >= max(P(A), P(B))
    p_union = Fraction(rng.randint(max(p_a.numerator, p_b.numerator), 9), 10)
    p_inter = p_a + p_b - p_union

    prompt = (
        f"For two events $A$ and $B$, it is given that:\n\n"
        f"$$P(A) = {_fmt_frac(p_a)}, \\quad P(B) = {_fmt_frac(p_b)}, \\quad P(A \\cup B) = {_fmt_frac(p_union)}$$\n\n"
        f"1. Rearrange the addition rule to express $P(A \\cap B)$ in terms of $P(A)$, $P(B)$, and $P(A \\cup B)$.\n"
        f"2. Calculate $P(A \\cap B)$."
    )

    worked = (
        f"**1. Rearranged Addition Rule:**\n"
        f"$$P(A \\cap B) = P(A) + P(B) - P(A \\cup B)$$\n\n"
        f"**2. Calculation:**\n"
        f"$$P(A \\cap B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - {_fmt_frac(p_union)} = {_fmt_frac(p_inter)}$$"
    )

    ans = f"P(A and B) = {_fmt_frac(p_inter)}"

    return {
        "id": f"g10_prob_10_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_frac(p_inter),
        "answer_latex": rf"P(A \cap B) = {_fmt_frac(p_inter)}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "10_addition_rule_solve_intersection",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct rearranged formula for P(A and B)", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct calculation P(A and B) = {_fmt_frac(p_inter)}", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "P(A and B) = P(A) + P(B) - P(A or B).",
            "2_concept": "The overlap is found by adding the individual probabilities and subtracting the union.",
            "3_breakdown": f"P(A and B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - {_fmt_frac(p_union)} = {_fmt_frac(p_inter)}.",
        },
        "misconception_tags": ["intersection_rearrangement_sign_error"],
    }


# -----------------------------------------------------------------------------
# 11. Addition rule solve single event
# -----------------------------------------------------------------------------
def arch_11_addition_rule_solve_single_event(rng: random.Random) -> Dict[str, Any]:
    p_b = Fraction(rng.randint(3, 5), 10)
    p_inter = Fraction(rng.randint(1, 2), 10)
    p_union = Fraction(rng.randint(7, 9), 10)
    p_a = p_union - p_b + p_inter

    prompt = (
        f"For two events $A$ and $B$ in a sample space:\n\n"
        f"$$P(B) = {_fmt_frac(p_b)}, \\quad P(A \\cap B) = {_fmt_frac(p_inter)}, \\quad P(A \\cup B) = {_fmt_frac(p_union)}$$\n\n"
        f"Use the addition rule to set up an equation and solve for $P(A)$."
    )

    worked = (
        f"**Step 1: Write the addition rule:**\n"
        f"$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$\n\n"
        f"**Step 2: Substitute known values:**\n"
        f"$${_fmt_frac(p_union)} = P(A) + {_fmt_frac(p_b)} - {_fmt_frac(p_inter)}$$\n\n"
        f"**Step 3: Solve for $P(A)$:**\n"
        f"$$P(A) = {_fmt_frac(p_union)} - {_fmt_frac(p_b)} + {_fmt_frac(p_inter)} = {_fmt_frac(p_a)}$$"
    )

    return {
        "id": f"g10_prob_11_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_frac(p_a),
        "answer_latex": rf"P(A) = {_fmt_frac(p_a)}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "11_addition_rule_solve_single_event",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Correct addition rule substitution", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct solution P(A) = {_fmt_frac(p_a)}", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Substitute the given values into P(A or B) = P(A) + P(B) - P(A and B).",
            "2_concept": "P(A) = P(A U B) - P(B) + P(A and B).",
            "3_breakdown": f"P(A) = {_fmt_frac(p_union)} - {_fmt_frac(p_b)} + {_fmt_frac(p_inter)} = {_fmt_frac(p_a)}.",
        },
        "misconception_tags": ["addition_rule_algebraic_rearrangement"],
    }


# -----------------------------------------------------------------------------
# 12. Mutually exclusive addition rule
# -----------------------------------------------------------------------------
def arch_12_mutually_exclusive_addition_rule(rng: random.Random) -> Dict[str, Any]:
    p_a_n = rng.randint(2, 4)
    p_b_n = rng.randint(3, 5)
    p_a = Fraction(p_a_n, 10)
    p_b = Fraction(p_b_n, 10)
    p_union = p_a + p_b

    prompt = (
        f"Two events $A$ and $B$ are **mutually exclusive**.\n\n"
        f"It is given that $P(A) = {_fmt_frac(p_a)}$ and $P(B) = {_fmt_frac(p_b)}$.\n\n"
        f"1. State the value of $P(A \\cap B)$.\n"
        f"2. State the special addition rule for mutually exclusive events.\n"
        f"3. Calculate $P(A \\cup B)$."
    )

    worked = (
        f"**1. Intersection value:**\n"
        f"Since $A$ and $B$ are mutually exclusive, they cannot occur together:\n"
        f"$$P(A \\cap B) = 0$$\n\n"
        f"**2. Special Addition Rule:**\n"
        f"$$P(A \\cup B) = P(A) + P(B)$$\n\n"
        f"**3. Calculation:**\n"
        f"$$P(A \\cup B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} = {_fmt_frac(p_union)}$$"
    )

    ans = f"P(A and B)=0, P(A U B)={_fmt_frac(p_union)}"

    return {
        "id": f"g10_prob_12_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"P(A \cap B) = 0, \quad P(A \cup B) = {_fmt_frac(p_union)}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "12_mutually_exclusive_addition_rule",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Statement that P(A and B) = 0", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Special addition rule formula", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct union calculation ({_fmt_frac(p_union)})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Mutually exclusive means they cannot happen at the same time: P(A and B) = 0.",
            "2_concept": "For mutually exclusive events, P(A or B) = P(A) + P(B).",
            "3_breakdown": f"P(A U B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["mutually_exclusive_intersection_nonzero"],
    }


# -----------------------------------------------------------------------------
# 13. Mutually exclusive identification and proof
# -----------------------------------------------------------------------------
def arch_13_mutually_exclusive_identification_and_proof(rng: random.Random) -> Dict[str, Any]:
    is_me = rng.choice([True, False])
    p_a = Fraction(3, 10)
    p_b = Fraction(4, 10)
    if is_me:
        p_union = Fraction(7, 10)
        p_inter = Fraction(0, 1)
        reason = "P(A) + P(B) = 3/10 + 4/10 = 7/10 = P(A or B), which implies P(A and B) = 0."
        conclusion = "Yes, events A and B are mutually exclusive."
    else:
        p_union = Fraction(6, 10)
        p_inter = Fraction(1, 10)
        reason = "P(A and B) = P(A) + P(B) - P(A or B) = 3/10 + 4/10 - 6/10 = 1/10 != 0."
        conclusion = "No, events A and B are NOT mutually exclusive."

    prompt = (
        f"Two events $A$ and $B$ have probabilities:\n\n"
        f"$$P(A) = {_fmt_frac(p_a)}, \\quad P(B) = {_fmt_frac(p_b)}, \\quad P(A \\cup B) = {_fmt_frac(p_union)}$$\n\n"
        "1. Calculate $P(A) + P(B)$.\n"
        "2. State whether events $A$ and $B$ are mutually exclusive.\n"
        "3. Justify your answer mathematically using the condition for mutually exclusive events."
    )

    worked = (
        f"**1. Sum of probabilities:**\n"
        f"$$P(A) + P(B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} = {_fmt_frac(p_a + p_b)}$$\n\n"
        f"**2 & 3. Mutual Exclusivity Check:**\n"
        f"{reason}\n"
        f"**Conclusion:** {conclusion}"
    )

    ans = "Yes, mutually exclusive" if is_me else "No, not mutually exclusive"

    return {
        "id": f"g10_prob_13_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"\text{{{ans}}}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "13_mutually_exclusive_identification_and_proof",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct sum P(A) + P(B) = {_fmt_frac(p_a + p_b)}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct conclusion ({ans})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Valid mathematical justification based on P(A and B)", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Check whether P(A) + P(B) equals P(A U B).",
            "2_concept": "Events are mutually exclusive if and only if P(A and B) = 0.",
            "3_breakdown": f"P(A) + P(B) = {_fmt_frac(p_a + p_b)} vs P(A U B) = {_fmt_frac(p_union)}. Result: {ans}.",
        },
        "misconception_tags": ["mutually_exclusive_test_failure"],
    }


# -----------------------------------------------------------------------------
# 14. Complementary vs mutually exclusive distinction
# -----------------------------------------------------------------------------
def arch_14_complementary_vs_mutually_exclusive_distinction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Explain the key difference between **mutually exclusive events** and **complementary events**:\n\n"
        "1. State the condition for two events $A$ and $B$ to be mutually exclusive.\n"
        "2. State the TWO conditions for two events $A$ and $B$ to be complementary.\n"
        "3. True or False: All complementary events are mutually exclusive, but not all mutually exclusive events are complementary. Explain."
    )

    worked = (
        "**1. Mutually Exclusive Condition:**\n"
        "$$P(A \\cap B) = 0$$\n"
        "(The events cannot occur simultaneously).\n\n"
        "**2. Complementary Conditions:**\n"
        "Two events are complementary if:\n"
        "1. They are mutually exclusive: $P(A \\cap B) = 0$\n"
        "2. They are exhaustive: $P(A) + P(B) = 1$ (or $P(A \\cup B) = 1$).\n\n"
        "**3. True:**\n"
        "Every complementary pair is mutually exclusive because they have no common outcomes. "
        "However, two mutually exclusive events might not cover the entire sample space (their sum could be less than 1)."
    )

    ans = "True: Complementary requires both mutually exclusive and exhaustive"

    return {
        "id": f"g10_prob_14_{rng.randint(100000, 999999)}",
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
        "subskill": "14_complementary_vs_mutually_exclusive_distinction",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Mutually exclusive condition: P(A and B) = 0", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Complementary conditions: P(A and B) = 0 and P(A) + P(B) = 1", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Statement that statement is True with valid explanation", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Complementary events must add up to 1 and have no overlap.",
            "2_concept": "Complementary = Mutually Exclusive + Exhaustive.",
            "3_breakdown": "Mutually exclusive means P(A and B)=0. Complementary means P(A and B)=0 AND P(A)+P(B)=1.",
        },
        "misconception_tags": ["complementary_exhaustive_omission"],
    }


# -----------------------------------------------------------------------------
# 15. Exhaustive events condition
# -----------------------------------------------------------------------------
def arch_15_exhaustive_events_condition(rng: random.Random) -> Dict[str, Any]:
    p_a_n = rng.randint(4, 6)
    p_a = Fraction(p_a_n, 10)
    p_b_n = rng.randint(5, 7)
    p_b = Fraction(p_b_n, 10)
    # exhaustive means P(A U B) = 1
    p_union = Fraction(1, 1)
    p_inter = p_a + p_b - 1

    prompt = (
        f"Two events $A$ and $B$ are known to be **exhaustive** in a sample space $S$.\n\n"
        f"It is given that $P(A) = {_fmt_frac(p_a)}$ and $P(B) = {_fmt_frac(p_b)}$.\n\n"
        "1. State what it means mathematically for two events to be exhaustive.\n"
        "2. State the value of $P(A \\cup B)$.\n"
        "3. Calculate $P(A \\cap B)$."
    )

    worked = (
        "**1. Exhaustive Definition:**\n"
        "Events are exhaustive if together they cover the entire sample space: $$P(A \\cup B) = 1$$\n\n"
        "**2. Value of $P(A \\cup B)$:**\n"
        "$$P(A \\cup B) = 1$$\n\n"
        "**3. Intersection Calculation:**\n"
        "$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$\n"
        f"$$1 = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - P(A \\cap B)$$\n"
        f"$$P(A \\cap B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - 1 = {_fmt_frac(p_inter)}$$"
    )

    ans = f"P(A U B)=1, P(A and B)={_fmt_frac(p_inter)}"

    return {
        "id": f"g10_prob_15_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": ans,
        "answer_latex": rf"P(A \cup B) = 1, \quad P(A \\cap B) = {_fmt_frac(p_inter)}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "15_exhaustive_events_condition",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Definition of exhaustive: P(A or B) = 1", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Statement that P(A U B) = 1", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Calculation of P(A and B) = {_fmt_frac(p_inter)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Exhaustive means P(A or B) = 1.",
            "2_concept": "When P(A U B) = 1, P(A and B) = P(A) + P(B) - 1.",
            "3_breakdown": f"P(A and B) = {_fmt_frac(p_a)} + {_fmt_frac(p_b)} - 1 = {_fmt_frac(p_inter)}.",
        },
        "misconception_tags": ["exhaustive_events_union_not_one"],
    }


# -----------------------------------------------------------------------------
# 16. Two event venn read counts
# -----------------------------------------------------------------------------
def arch_16_two_event_venn_read_counts(rng: random.Random) -> Dict[str, Any]:
    n_a_only = rng.randint(18, 30)
    n_inter = rng.randint(8, 16)
    n_b_only = rng.randint(15, 25)
    n_neither = rng.randint(6, 14)
    total_n = n_a_only + n_inter + n_b_only + n_neither

    svg = _make_venn_diagram_svg(n_a_only, n_inter, n_b_only, n_neither, label_a="Music", label_b="Drama", title="Learner Activity Participation")

    prompt = (
        "A Venn diagram displays the participation of learners in Music ($M$) and Drama ($D$):\n\n"
        f"The counts shown in the regions are: Music only ({n_a_only}), Both ({n_inter}), Drama only ({n_b_only}), and Neither ({n_neither}).\n\n"
        "1. How many learners take Music ONLY?\n"
        "2. How many learners take BOTH Music and Drama?\n"
        "3. How many learners participate in Drama in total?\n"
        "4. Calculate the total number of learners surveyed, $n(S)$."
    )

    tot_drama = n_b_only + n_inter
    worked = (
        f"**1. Music ONLY:** $n(M \\cap D') = **{n_a_only}**$\n\n"
        f"**2. Both activities:** $n(M \\cap D) = **{n_inter}**$\n\n"
        f"**3. Total Drama:**\n"
        f"$$n(D) = n(D \\text{{ only}}) + n(M \\cap D) = {n_b_only} + {n_inter} = **{tot_drama}**$$\n\n"
        f"**4. Total learners surveyed ($n(S)$):**\n"
        f"$$n(S) = {n_a_only} + {n_inter} + {n_b_only} + {n_neither} = **{total_n}**$$"
    )

    ans = f"Music only={n_a_only}, Both={n_inter}, Total Drama={tot_drama}, Total={total_n}"

    return {
        "id": f"g10_prob_16_{rng.randint(100000, 999999)}",
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
        "subskill": "16_two_event_venn_read_counts",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "easy",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Music only count ({n_a_only})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Both count ({n_inter})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Total Drama count ({tot_drama})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Total sample space count n(S) = {total_n}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Read the numbers directly from the regions: left circle only, intersection, right circle only, and outside.",
            "2_concept": "Total Drama includes both Drama only and the intersection.",
            "3_breakdown": f"Music only = {n_a_only}, Both = {n_inter}, Total Drama = {tot_drama}, Total = {total_n}.",
        },
        "misconception_tags": ["venn_region_total_confusion"],
    }


# -----------------------------------------------------------------------------
# 17. Two event venn calculate probabilities
# -----------------------------------------------------------------------------
def arch_17_two_event_venn_calculate_probabilities(rng: random.Random) -> Dict[str, Any]:
    n_a_only = 25
    n_inter = 15
    n_b_only = 20
    n_neither = rng.choice([20, 40])
    total_n = n_a_only + n_inter + n_b_only + n_neither

    svg = _make_venn_diagram_svg(n_a_only, n_inter, n_b_only, n_neither, label_a="A", label_b="B", title="Two Events Venn Diagram")

    p_a = Fraction(n_a_only + n_inter, total_n)
    p_inter = Fraction(n_inter, total_n)
    p_union = Fraction(n_a_only + n_inter + n_b_only, total_n)
    p_neither = Fraction(n_neither, total_n)

    prompt = (
        "A Venn diagram shows the number of elements in events $A$ and $B$ within sample space $S$:\n\n"
        f"The counts are: $A$ only = {n_a_only}, $A \\cap B$ = {n_inter}, $B$ only = {n_b_only}, neither = {n_neither}.\n\n"
        f"A learner is selected at random from the total of {total_n} learners. Calculate:\n"
        f"1. $P(A)$\n"
        f"2. $P(A \\cap B)$\n"
        f"3. $P(A \\cup B)$\n"
        f"4. $P(\\text{{neither }} A \\text{{ nor }} B)$"
    )

    worked = (
        f"Total outcomes: $n(S) = {total_n}$.\n\n"
        f"**1. $P(A)$:** $n(A) = {n_a_only} + {n_inter} = {n_a_only + n_inter}$\n"
        f"$$P(A) = \\frac{{{n_a_only + n_inter}}}{{{total_n}}} = {_fmt_frac(p_a)}$$\n\n"
        f"**2. $P(A \\cap B)$:**\n"
        f"$$P(A \\cap B) = \\frac{{{n_inter}}}{{{total_n}}} = {_fmt_frac(p_inter)}$$\n\n"
        f"**3. $P(A \\cup B)$:** $n(A \\cup B) = {n_a_only} + {n_inter} + {n_b_only} = {n_a_only + n_inter + n_b_only}$\n"
        f"$$P(A \\cup B) = \\frac{{{n_a_only + n_inter + n_b_only}}}{{{total_n}}} = {_fmt_frac(p_union)}$$\n\n"
        f"**4. $P((A \\cup B)')$:**\n"
        f"$$P(\\text{{neither}}) = \\frac{{{n_neither}}}{{{total_n}}} = {_fmt_frac(p_neither)}$$"
    )

    ans = f"P(A)={_fmt_frac(p_a)}, P(inter)={_fmt_frac(p_inter)}, P(union)={_fmt_frac(p_union)}, P(neither)={_fmt_frac(p_neither)}"

    return {
        "id": f"g10_prob_17_{rng.randint(100000, 999999)}",
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
        "subskill": "17_two_event_venn_calculate_probabilities",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "medium",
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct P(A) = {_fmt_frac(p_a)}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct P(A and B) = {_fmt_frac(p_inter)}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct P(A or B) = {_fmt_frac(p_union)}", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Correct P(neither) = {_fmt_frac(p_neither)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Divide each region count by the total sample space size.",
            "2_concept": "P(E) = n(E) / n(S).",
            "3_breakdown": f"P(A) = {_fmt_frac(p_a)}, P(A and B) = {_fmt_frac(p_inter)}, P(A or B) = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["venn_probability_denominator_error"],
    }


# -----------------------------------------------------------------------------
# 18. Two event venn solve for unknown x intersection
# -----------------------------------------------------------------------------
def arch_18_two_event_venn_solve_for_unknown_x_intersection(rng: random.Random) -> Dict[str, Any]:
    total_n = rng.choice([80, 100, 120])
    x_val = rng.randint(12, 22)
    tot_s = x_val + rng.randint(20, 35)
    tot_d = x_val + rng.randint(18, 30)
    neither = total_n - (tot_s + tot_d - x_val)

    prompt = (
        f"In a survey of {total_n} Grade 10 learners:\n\n"
        f"- {tot_s} learners play Soccer ($S$)\n"
        f"- {tot_d} learners play Drama/Debating ($D$)\n"
        f"- {neither} learners participate in neither activity\n"
        f"- $x$ learners participate in BOTH activities\n\n"
        f"1. Express the number of learners who participate in Soccer ONLY in terms of $x$.\n"
        f"2. Set up an algebraic equation for the total number of learners.\n"
        f"3. Solve for $x$ (the number who participate in both activities)."
    )

    s_only_expr = f"{tot_s} - x"
    d_only_expr = f"{tot_d} - x"

    worked = (
        f"**1. Soccer ONLY:**\n"
        f"$$n(S \\text{{ only}}) = {tot_s} - x$$\n\n"
        f"**2. Equation:**\n"
        f"The sum of all four disjoint regions equals the total sample space $n(S) = {total_n}$:\n"
        f"$$({tot_s} - x) + x + ({tot_d} - x) + {neither} = {total_n}$$\n"
        f"$${tot_s + tot_d + neither} - x = {total_n}$$\n\n"
        f"**3. Solve for $x$:**\n"
        f"$$x = {tot_s + tot_d + neither} - {total_n} = {x_val}$$"
    )

    ans = f"x = {x_val}"

    return {
        "id": f"g10_prob_18_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(x_val),
        "answer_latex": rf"x = {x_val}",
        "worked_solution": worked,
        "marks": 4,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "18_two_event_venn_solve_for_unknown_x_intersection",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 4,
        "difficulty": "hard",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct expression for Soccer only: {s_only_expr}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Setting up equation equating sum of regions to total", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct solution x = {x_val}", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Express 'Soccer only' as (total Soccer - x) and 'Drama only' as (total Drama - x).",
            "2_concept": "(Soccer only) + x + (Drama only) + neither = Total.",
            "3_breakdown": f"({tot_s} - x) + x + ({tot_d} - x) + {neither} = {total_n} -> x = {x_val}.",
        },
        "misconception_tags": ["venn_algebraic_intersection_setup_error"],
    }


# -----------------------------------------------------------------------------
# 19. Two event venn solve for neither
# -----------------------------------------------------------------------------
def arch_19_two_event_venn_solve_for_neither(rng: random.Random) -> Dict[str, Any]:
    total_n = rng.choice([70, 90, 110])
    inter = rng.randint(10, 18)
    a_only = rng.randint(20, 30)
    b_only = rng.randint(15, 25)
    neither = total_n - (a_only + inter + b_only)

    tot_a = a_only + inter
    tot_b = b_only + inter

    prompt = (
        f"In a survey of {total_n} learners:\n\n"
        f"- {tot_a} study Accounting ($A$)\n"
        f"- {tot_b} study Business Studies ($B$)\n"
        f"- {inter} study BOTH subjects\n\n"
        f"1. Calculate the number of learners who study Accounting ONLY.\n"
        f"2. Calculate the number of learners who study Business Studies ONLY.\n"
        f"3. Calculate the number of learners who study NEITHER of these two subjects."
    )

    worked = (
        f"**1. Accounting ONLY:**\n"
        f"$$n(A \\text{{ only}}) = n(A) - n(A \\cap B) = {tot_a} - {inter} = {a_only}$$\n\n"
        f"**2. Business Studies ONLY:**\n"
        f"$$n(B \\text{{ only}}) = n(B) - n(A \\cap B) = {tot_b} - {inter} = {b_only}$$\n\n"
        f"**3. NEITHER subject:**\n"
        f"$$n(A \\cup B) = n(A \\text{{ only}}) + n(A \\cap B) + n(B \\text{{ only}}) = {a_only} + {inter} + {b_only} = {a_only + inter + b_only}$$\n"
        f"$$n(\\text{{Neither}}) = {total_n} - n(A \\cup B) = {total_n} - {a_only + inter + b_only} = {neither}$$"
    )

    ans = f"Accounting only={a_only}, Business only={b_only}, Neither={neither}"

    return {
        "id": f"g10_prob_19_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": str(neither),
        "answer_latex": rf"n(\text{{Neither}}) = {neither}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "19_two_event_venn_solve_for_neither",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct Accounting only count ({a_only})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct Business only count ({b_only})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct Neither count ({neither})", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Subtract the intersection from each total, then subtract the union from the overall total.",
            "2_concept": "Neither = Total - (A only + Both + B only).",
            "3_breakdown": f"A only = {a_only}, B only = {b_only}. Union = {a_only + inter + b_only}. Neither = {neither}.",
        },
        "misconception_tags": ["venn_neither_region_calculation_error"],
    }


# -----------------------------------------------------------------------------
# 20. Two event venn mutually exclusive case
# -----------------------------------------------------------------------------
def arch_20_two_event_venn_mutually_exclusive_case(rng: random.Random) -> Dict[str, Any]:
    n_a = rng.randint(20, 35)
    n_b = rng.randint(15, 30)
    neither = rng.randint(10, 20)
    total_n = n_a + n_b + neither

    svg = _make_venn_diagram_svg(n_a, 0, n_b, neither, label_a="Chess", label_b="Rugby", title="Mutually Exclusive Events")

    prompt = (
        "A Venn diagram displays learner participation where the circles for Chess ($C$) and Rugby ($R$) do not overlap:\n\n"
        f"The counts are: Chess = {n_a}, Both = 0, Rugby = {n_b}, Neither = {neither}.\n\n"
        f"1. Explain why the intersection region is 0.\n"
        f"2. Calculate $P(C \\cup R)$ as a fraction in simplest form.\n"
        f"3. State the term used to describe two events that have no outcomes in common."
    )

    p_union = Fraction(n_a + n_b, total_n)
    worked = (
        f"**1. Explanation:**\n"
        f"No learner plays both Chess and Rugby; the sets are disjoint, so $n(C \\cap R) = 0$.\n\n"
        f"**2. Union Probability:**\n"
        f"$$P(C \\cup R) = \\frac{{{n_a} + {n_b}}}{{{total_n}}} = \\frac{{{n_a + n_b}}}{{{total_n}}} = {_fmt_frac(p_union)}$$\n\n"
        f"**3. Term:** **Mutually exclusive events**."
    )

    ans = f"P(union)={_fmt_frac(p_union)}, Mutually exclusive"

    return {
        "id": f"g10_prob_20_{rng.randint(100000, 999999)}",
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
        "subskill": "20_two_event_venn_mutually_exclusive_case",
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
                {"id": "mp_1", "desc": "Valid explanation for zero intersection", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct union probability ({_fmt_frac(p_union)})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Identification as 'mutually exclusive'", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "When circles do not overlap, the events cannot happen together.",
            "2_concept": "Disjoint events are mutually exclusive.",
            "3_breakdown": f"Intersection = 0. Union = ({n_a} + {n_b}) / {total_n} = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["disjoint_sets_terminology_confusion"],
    }


# -----------------------------------------------------------------------------
# 21. Two-way contingency table marginal totals
# -----------------------------------------------------------------------------
def arch_21_two_way_contingency_table_marginal_totals(rng: random.Random) -> Dict[str, Any]:
    # 2x2 table: Gender (Boys/Girls) vs Device (Tablet/Laptop)
    b_tab = rng.randint(15, 30)
    b_lap = rng.randint(20, 35)
    g_tab = rng.randint(18, 32)
    g_lap = rng.randint(22, 38)

    tot_boys = b_tab + b_lap
    tot_girls = g_tab + g_lap
    tot_tab = b_tab + g_tab
    tot_lap = b_lap + g_lap
    grand_tot = tot_boys + tot_girls

    prompt = (
        "The following two-way table shows device preferences for a group of Grade 10 learners:\n\n"
        "| Gender | Tablet | Laptop | Total |\n"
        "| :--- | :--- | :--- | :--- |\n"
        f"| Boys | {b_tab} | {b_lap} | $a$ |\n"
        f"| Girls | {g_tab} | {g_lap} | $b$ |\n"
        "| **Total** | $c$ | $d$ | $T$ |\n\n"
        "Calculate the marginal totals $a, b, c, d$ and the grand total $T$."
    )

    worked = (
        f"**Marginal Totals:**\n"
        f"- $a = \\text{{Total Boys}} = {b_tab} + {b_lap} = {tot_boys}$\n"
        f"- $b = \\text{{Total Girls}} = {g_tab} + {g_lap} = {tot_girls}$\n"
        f"- $c = \\text{{Total Tablet}} = {b_tab} + {g_tab} = {tot_tab}$\n"
        f"- $d = \\text{{Total Laptop}} = {b_lap} + {g_lap} = {tot_lap}$\n"
        f"- $T = \\text{{Grand Total}} = {tot_boys} + {tot_girls} = {grand_tot}$"
    )

    ans = f"a={tot_boys}, b={tot_girls}, c={tot_tab}, d={tot_lap}, T={grand_tot}"

    return {
        "id": f"g10_prob_21_{rng.randint(100000, 999999)}",
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
        "subskill": "21_two_way_contingency_table_marginal_totals",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct row totals a={tot_boys}, b={tot_girls}", "marks": 1.5, "editable": True},
                {"id": "mp_2", "desc": f"Correct column totals c={tot_tab}, d={tot_lap}", "marks": 1.5, "editable": True},
                {"id": "mp_3", "desc": f"Correct grand total T={grand_tot}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add across each row and down each column.",
            "2_concept": "Marginal totals are row and column sums; both sets must sum to the same grand total.",
            "3_breakdown": f"Totals: Boys = {tot_boys}, Girls = {tot_girls}, Tablet = {tot_tab}, Laptop = {tot_lap}, Grand Total = {grand_tot}.",
        },
        "misconception_tags": ["contingency_table_marginal_sum_error"],
    }


# -----------------------------------------------------------------------------
# 22. Two-way table single event probability
# -----------------------------------------------------------------------------
def arch_22_two_way_table_single_event_probability(rng: random.Random) -> Dict[str, Any]:
    b_tab = 20
    b_lap = 30
    g_tab = 25
    g_lap = 25
    tot_boys = 50
    tot_girls = 50
    tot_tab = 45
    tot_lap = 55
    grand_tot = 100

    prompt = (
        "The table summarizes 100 learners by gender and preference:\n\n"
        "| Gender | Tablet | Laptop | Total |\n"
        "| :--- | :--- | :--- | :--- |\n"
        f"| Boys | {b_tab} | {b_lap} | {tot_boys} |\n"
        f"| Girls | {g_tab} | {g_lap} | {tot_girls} |\n"
        f"| **Total** | {tot_tab} | {tot_lap} | {grand_tot} |\n\n"
        "A learner is selected at random from the 100 learners. Calculate:\n"
        "1. $P(\\text{Boy})$\n"
        "2. $P(\\text{Prefers Laptop})$"
    )

    p_boy = Fraction(tot_boys, grand_tot)
    p_lap = Fraction(tot_lap, grand_tot)

    worked = (
        f"**1. Probability of selecting a Boy:**\n"
        f"$$P(\\text{{Boy}}) = \\frac{{\\text{{Total Boys}}}}{{\\text{{Grand Total}}}} = \\frac{{{tot_boys}}}{{{grand_tot}}} = {_fmt_frac(p_boy)}$$\n\n"
        f"**2. Probability of selecting someone who prefers Laptop:**\n"
        f"$$P(\\text{{Laptop}}) = \\frac{{\\text{{Total Laptop}}}}{{\\text{{Grand Total}}}} = \\frac{{{tot_lap}}}{{{grand_tot}}} = {_fmt_frac(p_lap)}$$"
    )

    ans = f"P(Boy)={_fmt_frac(p_boy)}, P(Laptop)={_fmt_frac(p_lap)}"

    return {
        "id": f"g10_prob_22_{rng.randint(100000, 999999)}",
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
        "subskill": "22_two_way_table_single_event_probability",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "easy",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct P(Boy) = {_fmt_frac(p_boy)}", "marks": 1.5, "editable": True},
                {"id": "mp_2", "desc": f"Correct P(Laptop) = {_fmt_frac(p_lap)}", "marks": 1.5, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Divide the row or column total by the grand total 100.",
            "2_concept": "Single event probability = (row or column total) / (grand total).",
            "3_breakdown": f"P(Boy) = {tot_boys}/{grand_tot} = {_fmt_frac(p_boy)}. P(Laptop) = {tot_lap}/{grand_tot} = {_fmt_frac(p_lap)}.",
        },
        "misconception_tags": ["contingency_table_single_event_cell_selection"],
    }


# -----------------------------------------------------------------------------
# 23. Two-way table intersection probability
# -----------------------------------------------------------------------------
def arch_23_two_way_table_intersection_probability(rng: random.Random) -> Dict[str, Any]:
    b_tab = rng.randint(12, 22)
    b_lap = rng.randint(18, 28)
    g_tab = rng.randint(15, 25)
    g_lap = rng.randint(20, 30)

    tot_boys = b_tab + b_lap
    tot_girls = g_tab + g_lap
    tot_tab = b_tab + g_tab
    tot_lap = b_lap + g_lap
    grand_tot = tot_boys + tot_girls

    prompt = (
        "The table displays survey results for learners:\n\n"
        "| Gender | Tablet | Laptop | Total |\n"
        "| :--- | :--- | :--- | :--- |\n"
        f"| Boys | {b_tab} | {b_lap} | {tot_boys} |\n"
        f"| Girls | {g_tab} | {g_lap} | {tot_girls} |\n"
        f"| **Total** | {tot_tab} | {tot_lap} | {grand_tot} |\n\n"
        "A learner is selected at random. Calculate the probability that the learner is:\n"
        "1. A Boy who prefers a Tablet.\n"
        "2. A Girl who prefers a Laptop."
    )

    p_b_tab = Fraction(b_tab, grand_tot)
    p_g_lap = Fraction(g_lap, grand_tot)

    worked = (
        f"**1. Boy and Tablet (intersection cell):**\n"
        f"$$P(\\text{{Boy}} \\cap \\text{{Tablet}}) = \\frac{{{b_tab}}}{{{grand_tot}}} = {_fmt_frac(p_b_tab)}$$\n\n"
        f"**2. Girl and Laptop (intersection cell):**\n"
        f"$$P(\\text{{Girl}} \\cap \\text{{Laptop}}) = \\frac{{{g_lap}}}{{{grand_tot}}} = {_fmt_frac(p_g_lap)}$$"
    )

    ans = f"1: {_fmt_frac(p_b_tab)}, 2: {_fmt_frac(p_g_lap)}"

    return {
        "id": f"g10_prob_23_{rng.randint(100000, 999999)}",
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
        "subskill": "23_two_way_table_intersection_probability",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct P(Boy and Tablet) = {_fmt_frac(p_b_tab)}", "marks": 1.5, "editable": True},
                {"id": "mp_2", "desc": f"Correct P(Girl and Laptop) = {_fmt_frac(p_g_lap)}", "marks": 1.5, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Find the cell where the row and column intersect and divide by the grand total.",
            "2_concept": "Intersection probability is the cell count divided by grand total.",
            "3_breakdown": f"Boy & Tablet = {b_tab}/{grand_tot}. Girl & Laptop = {g_lap}/{grand_tot}.",
        },
        "misconception_tags": ["contingency_table_intersection_confusion"],
    }


# -----------------------------------------------------------------------------
# 24. Two-way table union probability
# -----------------------------------------------------------------------------
def arch_24_two_way_table_union_probability(rng: random.Random) -> Dict[str, Any]:
    b_tab = 15
    b_lap = 25
    g_tab = 20
    g_lap = 40
    tot_boys = 40
    tot_girls = 60
    tot_tab = 35
    tot_lap = 65
    grand_tot = 100

    prompt = (
        "The table displays survey results for 100 learners:\n\n"
        "| Gender | Tablet | Laptop | Total |\n"
        "| :--- | :--- | :--- | :--- |\n"
        f"| Boys | {b_tab} | {b_lap} | {tot_boys} |\n"
        f"| Girls | {g_tab} | {g_lap} | {tot_girls} |\n"
        f"| **Total** | {tot_tab} | {tot_lap} | {grand_tot} |\n\n"
        "A learner is selected at random. Calculate the probability that the learner is a **Girl OR prefers a Tablet**.\n"
        "Show your working using the addition rule formula."
    )

    p_girl = Fraction(tot_girls, grand_tot)
    p_tab = Fraction(tot_tab, grand_tot)
    p_inter = Fraction(g_tab, grand_tot)
    p_union = p_girl + p_tab - p_inter

    worked = (
        "**Step 1: Write the addition rule:**\n"
        "$$P(\\text{Girl} \\cup \\text{Tablet}) = P(\\text{Girl}) + P(\\text{Tablet}) - P(\\text{Girl} \\cap \\text{Tablet})$$\n\n"
        "**Step 2: Read values from the table:**\n"
        f"- $P(\\text{{Girl}}) = \\frac{{{tot_girls}}}{{{grand_tot}}}$\n"
        f"- $P(\\text{{Tablet}}) = \\frac{{{tot_tab}}}{{{grand_tot}}}$\n"
        f"- $P(\\text{{Girl}} \\cap \\text{{Tablet}}) = \\frac{{{g_tab}}}{{{grand_tot}}}$\n\n"
        "**Step 3: Calculate:**\n"
        f"$$P(\\text{{Girl}} \\cup \\text{{Tablet}}) = \\frac{{{tot_girls}}}{{{grand_tot}}} + \\frac{{{tot_tab}}}{{{grand_tot}}} - \\frac{{{g_tab}}}{{{grand_tot}}} = \\frac{{{tot_girls + tot_tab - g_tab}}}{{{grand_tot}}} = {_fmt_frac(p_union)}$$"
    )

    return {
        "id": f"g10_prob_24_{rng.randint(100000, 999999)}",
        "question_type": "typed",
        "prompt": prompt,
        "prompt_latex": prompt,
        "answer_mode": "text",
        "correct_answer": _fmt_frac(p_union),
        "answer_latex": rf"P(\text{{Girl}} \cup \text{{Tablet}}) = {_fmt_frac(p_union)}",
        "worked_solution": worked,
        "marks": 3,
        "topic": TOPIC,
        "topic_id": TOPIC_ID,
        "learning_objective_id": LO,
        "subskill": "24_two_way_table_union_probability",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": "Addition rule formula", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Subtracting intersection cell (Girl & Tablet)", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct quotient {_fmt_frac(p_union)}", "marks": 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Add the row total and column total, but don't forget to subtract the cell where they overlap.",
            "2_concept": "P(A or B) = P(A) + P(B) - P(A and B).",
            "3_breakdown": f"P(Girl or Tablet) = {tot_girls}/100 + {tot_tab}/100 - {g_tab}/100 = {_fmt_frac(p_union)}.",
        },
        "misconception_tags": ["contingency_table_double_counting_union"],
    }


# -----------------------------------------------------------------------------
# 25. Two-way table complement probability
# -----------------------------------------------------------------------------
def arch_25_two_way_table_complement_probability(rng: random.Random) -> Dict[str, Any]:
    b_tab = 18
    b_lap = 32
    g_tab = 22
    g_lap = 28
    tot_boys = 50
    tot_girls = 50
    tot_tab = 40
    tot_lap = 60
    grand_tot = 100

    prompt = (
        "The table displays preferences for 100 learners:\n\n"
        "| Gender | Tablet | Laptop | Total |\n"
        "| :--- | :--- | :--- | :--- |\n"
        f"| Boys | {b_tab} | {b_lap} | {tot_boys} |\n"
        f"| Girls | {g_tab} | {g_lap} | {tot_girls} |\n"
        f"| **Total** | {tot_tab} | {tot_lap} | {grand_tot} |\n\n"
        "A learner is chosen at random. Calculate the probability that the learner:\n"
        "1. Does NOT prefer a Tablet.\n"
        "2. Is NOT a Boy who prefers a Laptop."
    )

    p_not_tab = Fraction(tot_lap, grand_tot)
    p_b_lap = Fraction(b_lap, grand_tot)
    p_not_b_lap = 1 - p_b_lap

    worked = (
        f"**1. Not Tablet:**\n"
        f"$$P(\\text{{not Tablet}}) = 1 - P(\\text{{Tablet}}) = 1 - \\frac{{{tot_tab}}}{{{grand_tot}}} = \\frac{{{tot_lap}}}{{{grand_tot}}} = {_fmt_frac(p_not_tab)}$$\n\n"
        f"**2. Not a Boy who prefers Laptop:**\n"
        f"$$P(\\text{{Boy}} \\cap \\text{{Laptop}}) = \\frac{{{b_lap}}}{{{grand_tot}}}$$\n"
        f"$$P(\\text{{not (Boy and Laptop)}}) = 1 - \\frac{{{b_lap}}}{{{grand_tot}}} = {_fmt_frac(p_not_b_lap)}$$"
    )

    ans = f"1: {_fmt_frac(p_not_tab)}, 2: {_fmt_frac(p_not_b_lap)}"

    return {
        "id": f"g10_prob_25_{rng.randint(100000, 999999)}",
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
        "subskill": "25_two_way_table_complement_probability",
        "term": 4,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "difficulty": "medium",
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct P(not Tablet) = {_fmt_frac(p_not_tab)}", "marks": 1.5, "editable": True},
                {"id": "mp_2", "desc": f"Correct P(not Boy & Laptop) = {_fmt_frac(p_not_b_lap)}", "marks": 1.5, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": {
            "1_nudge": "Subtract the event probability from 1.",
            "2_concept": "P(not E) = 1 - P(E).",
            "3_breakdown": f"P(not Tablet) = 1 - {tot_tab}/100 = {_fmt_frac(p_not_tab)}. P(not (Boy and Laptop)) = 1 - {b_lap}/100 = {_fmt_frac(p_not_b_lap)}.",
        },
        "misconception_tags": ["complementary_table_event_subtraction"],
    }
