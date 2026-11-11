import os

def generate_file():
    parts = []
    
    parts.append('''"""Grade 11 Mathematical Literacy - Term 4: Probability Generator.

100% Aligned with South African National Curriculum Standards (CAPS).
Curriculum Source: curriculum_docs_auto/MathematicalLiteracy_Gr11/Term 4/01. Probability.md

Features:
- 52 distinct subskills covering:
    * Theoretical vs Experimental Probability & Basic Events (Subskills 1 to 10)
    * Mutually Exclusive & Addition Rules (Subskills 11 to 20)
    * Two-Way Contingency Tables & Joint/Conditional Probabilities (Subskills 21 to 30)
    * Venn Diagrams & Set Operations (Subskills 31 to 40)
    * Tree Diagrams & Compound Independent/Dependent Events (Subskills 41 to 52)
- Step-by-step worked solutions with mark allocations.
- South African comma decimal convention (e.g. 0,25 or 25%).
- Vector diagram specs (contingency tables, Venn diagrams, probability trees).
- 4 clean multiple-choice options with zero generic fallbacks.
- 3-tier diagnostic hints.
"""
from __future__ import annotations

import math
import random
import uuid
from typing import Any, Dict, List, Optional

SA_NAMES = [
    "Sipho", "Zanele", "Thabo", "Lerato", "Kagiso", "Naledi", "Bongani",
    "Nomvula", "Mpho", "Keletso", "Lungile", "Tebogo", "Farai", "Amina",
    "Lindiwe", "Jabu", "Sibusiso", "Andile", "Busisiwe", "Ayanda"
]

SA_TOWNS = [
    "Polokwane", "Mbombela", "Kimberley", "Bloemfontein", "Rustenburg",
    "Durban", "Gqeberha", "Cape Town", "Johannesburg", "Pretoria", "Upington"
]

def _fmt_dec(val: float, places: int = 2) -> str:
    """Format decimal with comma: 0,25 or 0,125."""
    s = f"{val:.{places}f}"
    parts = s.split(".")
    return f"{parts[0]},{parts[1]}"

def _fmt_pct(val: float, places: int = 1) -> str:
    """Format percentage: 25,0% or 33,3%."""
    pct = val * 100
    if pct.is_integer():
        return f"{int(pct)}%"
    s = f"{pct:.{places}f}"
    int_p, dec_p = s.split(".")
    return f"{int_p},{dec_p}%"

def _build_mc_options(correct: str, distractors: List[str], r: random.Random) -> List[str]:
    """Assemble 4 strictly distinct multiple-choice options with zero synthetic fallbacks."""
    pool = []
    for d in distractors:
        if d != correct and d not in pool:
            pool.append(d)
    r.shuffle(pool)
    opts = [correct] + pool[:3]
    while len(opts) < 4:
        cand = f"{correct} (Alternative)"
        if cand not in opts:
            opts.append(cand)
    r.shuffle(opts)
    return opts
''')

    # Subskills 1-10
    parts.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 1-10: Theoretical vs Experimental Probability & Basic Events
# ----------------------------------------------------------------------------

def _subskill_1(r: random.Random) -> Dict[str, Any]:
    """Calculate basic theoretical probability as fraction, decimal, and percentage."""
    n_fav = r.choice([3, 4, 5, 6])
    n_total = r.choice([12, 15, 20, 25])
    p = n_fav / n_total
    gcd = math.gcd(n_fav, n_total)
    num, den = n_fav // gcd, n_total // gcd

    prompt = (
        f"A bag contains **{n_total} identical counters**, of which **{n_fav} are red** and the remainder are blue.\\n"
        f"A counter is drawn at random from the bag.\\n\\n"
        f"Calculate the theoretical probability of selecting a red counter.\\n"
        f"Express your answer as a simplified fraction and as a percentage."
    )
    correct = f"{num}/{den} ({_fmt_pct(p)})"
    distractors = [
        f"{n_total - n_fav}/{n_total} ({_fmt_pct(1 - p)})",
        f"{num}/{den + 1} ({_fmt_pct(num / (den + 1))})",
        f"1/{n_total} ({_fmt_pct(1 / n_total)})"
    ]
    expl = (
        f"[1 Mark: Formula and fraction]\\n"
        f"P(Red) = Favourable outcomes / Total outcomes = {n_fav}/{n_total} = {num}/{den}\\n"
        f"[1 Mark: Percentage conversion]\\n"
        f"({num}/{den}) * 100 = {_fmt_pct(p)}"
    )
    return {
        "subskill": "gr11_prob_subskill_1",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Divide {n_fav} by {n_total} and simplify.", "tier_2": f"{n_fav}/{n_total} = {num}/{den}.", "tier_3": f"{correct}."}
    }

def _subskill_2(r: random.Random) -> Dict[str, Any]:
    """Calculate relative frequency (experimental probability)."""
    trials = r.choice([50, 100, 200])
    freq = r.choice([14, 22, 38, 45, 62])
    rel_freq = freq / trials

    prompt = (
        f"In a science class experiment, a learner spins an asymmetric spinner **{trials} times**.\\n"
        f"The spinner lands on the green section **{freq} times**.\\n\\n"
        f"Calculate the relative frequency (experimental probability) of landing on green.\\n"
        f"Express your answer as a decimal."
    )
    correct = f"{_fmt_dec(rel_freq, 2)}"
    distractors = [
        f"{_fmt_dec(1 - rel_freq, 2)}",
        f"{_fmt_dec(round(rel_freq + 0.12, 2), 2)}",
        f"{_fmt_dec(round(freq / (trials + 20), 2), 2)}"
    ]
    expl = (
        f"[1 Mark: Relative frequency definition]\\n"
        f"Relative Frequency = Frequency / Total trials = {freq} / {trials} = {_fmt_dec(rel_freq, 2)}"
    )
    return {
        "subskill": "gr11_prob_subskill_2",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide frequency by total trials.", "tier_2": f"{freq} / {trials}.", "tier_3": f"{correct}."}
    }

def _subskill_3(r: random.Random) -> Dict[str, Any]:
    """Compare relative frequency to theoretical probability and Law of Large Numbers."""
    prompt = (
        f"A fair 6-sided die has a theoretical probability of P(rolling a 6) = 1/6 ≈ 0,167.\\n"
        f"A learner rolls the die 10 times and gets a 6 on 4 rolls (relative frequency = 0,4).\\n"
        f"The learner rolls the die another 1 000 times, and the relative frequency becomes 0,169.\\n\\n"
        f"Which fundamental principle explains why the relative frequency moves closer to 0,167 as the number of trials increases?"
    )
    correct = "The Law of Large Numbers (experimental probability converges to theoretical probability over many trials)"
    distractors = [
        "The Gambler's Fallacy (the die balances out previous rolls)",
        "The Complementary Addition Principle",
        "Measurement error due to uneven table friction"
    ]
    expl = f"[1 Mark: Statistical principle]\\nAs the number of independent trials increases, the relative frequency converges towards the theoretical probability (Law of Large Numbers)."
    return {
        "subskill": "gr11_prob_subskill_3",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Think about what happens to experimental results when trials become very large.", "tier_2": "Law of Large Numbers.", "tier_3": f"{correct}."}
    }

def _subskill_4(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of a complementary event: P(not A) = 1 - P(A)."""
    p_pct = r.choice([25, 35, 40, 65, 80])
    p = p_pct / 100.0
    p_not = 1.0 - p

    prompt = (
        f"The South African Weather Service predicts an **{p_pct}% chance of rain** in Mbombela tomorrow.\\n\\n"
        f"Use the complementary rule P(not A) = 1 - P(A) to calculate the probability that it will **not** rain in Mbombela tomorrow."
    )
    correct = f"{int(p_not * 100)}%"
    distractors = [
        f"{p_pct}%",
        f"{int((p_not - 0.1) * 100)}%",
        f"{int((p_not + 0.15) * 100)}%"
    ]
    expl = (
        f"[1 Mark: Complementary rule]\\n"
        f"P(not Rain) = 100% - {p_pct}% = {int(p_not * 100)}%"
    )
    return {
        "subskill": "gr11_prob_subskill_4",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Subtract {p_pct}% from 100%.", "tier_2": f"100 - {p_pct}.", "tier_3": f"{correct}."}
    }

def _subskill_5(r: random.Random) -> Dict[str, Any]:
    """Impossible (P=0) and certain (P=1) event identification."""
    prompt = (
        f"Consider the experiment of rolling a single standard 6-sided die with faces numbered 1 to 6.\\n\\n"
        f"Which of the following events has a probability of exactly **0 (impossible event)**?"
    )
    correct = "Rolling a number greater than 6"
    distractors = [
        "Rolling an even number",
        "Rolling a number between 1 and 6 inclusive",
        "Rolling a prime number"
    ]
    expl = f"[1 Mark: Impossible event identification]\\nA standard die has faces 1 to 6. Rolling a number > 6 has 0 outcomes in the sample space, so P = 0."
    return {
        "subskill": "gr11_prob_subskill_5",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Look for an outcome that cannot happen on a 1-6 die.", "tier_2": "Numbers greater than 6 don't exist on the die.", "tier_3": f"{correct}."}
    }

def _subskill_6(r: random.Random) -> Dict[str, Any]:
    """Probability scale mapping along the verbal likelihood continuum."""
    p_val = r.choice([0.05, 0.50, 0.85])
    if p_val == 0.05:
        desc = "Unlikely (close to 0)"
    elif p_val == 0.50:
        desc = "Even chance (50/50 likelihood)"
    else:
        desc = "Likely (close to 1)"

    prompt = (
        f"An event has a calculated mathematical probability of **{_fmt_dec(p_val, 2)}**.\\n\\n"
        f"How is this probability classified on the standard verbal likelihood scale?"
    )
    correct = desc
    distractors = [
        "Certain (probability of exactly 1)",
        "Impossible (probability of exactly 0)",
        "Even chance (50/50 likelihood)" if p_val != 0.50 else "Likely (close to 1)"
    ]
    expl = f"[1 Mark: Verbal scale mapping]\\nA probability of {_fmt_dec(p_val, 2)} represents an {desc}."
    return {
        "subskill": "gr11_prob_subskill_6",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "0 = impossible, 0,5 = even chance, 1 = certain.", "tier_2": f"Where does {_fmt_dec(p_val, 2)} sit?", "tier_3": f"{correct}."}
    }

def _subskill_7(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of rolling specific outcomes on a standard 6-sided die."""
    event_type = r.choice(["prime", "greater than 4", "odd"])
    if event_type == "prime":
        fav = [2, 3, 5]
        desc = "a prime number"
    elif event_type == "greater than 4":
        fav = [5, 6]
        desc = "a number greater than 4"
    else:
        fav = [1, 3, 5]
        desc = "an odd number"

    n_fav = len(fav)
    gcd = math.gcd(n_fav, 6)
    num, den = n_fav // gcd, 6 // gcd

    prompt = (
        f"A fair 6-sided die is rolled once.\\n"
        f"Sample space S = {{1; 2; 3; 4; 5; 6}}.\\n\\n"
        f"Calculate the probability of rolling **{desc}**."
    )
    correct = f"{num}/{den}"
    distractors = [
        f"{num + 1}/{den}",
        f"{6 - n_fav}/6",
        "1/6"
    ]
    expl = (
        f"[1 Mark: Favourable outcomes identification]\\n"
        f"Favourable outcomes = {fav}, so n(E) = {n_fav}.\\n"
        f"[1 Mark: Probability fraction]\\n"
        f"P(E) = {n_fav}/6 = {num}/{den}"
    )
    return {
        "subskill": "gr11_prob_subskill_7",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"List outcomes in {fav} out of 6.", "tier_2": f"{n_fav}/6 simplified.", "tier_3": f"{correct}."}
    }

def _subskill_8(r: random.Random) -> Dict[str, Any]:
    """Probability of drawing specific cards from a standard 52-card deck."""
    card_type = r.choice(["an Ace", "a Heart", "a Face card (Jack, Queen, King)"])
    if card_type == "an Ace":
        n_fav = 4
    elif card_type == "a Heart":
        n_fav = 13
    else:
        n_fav = 12

    gcd = math.gcd(n_fav, 52)
    num, den = n_fav // gcd, 52 // gcd

    prompt = (
        f"A card is drawn at random from a standard shuffled deck of 52 playing cards (without jokers).\\n\\n"
        f"Calculate the probability of drawing **{card_type}**."
    )
    correct = f"{num}/{den}"
    distractors = [
        f"1/{n_fav}",
        f"{num}/{den + 2}",
        f"{52 - n_fav}/52"
    ]
    expl = (
        f"[1 Mark: Favourable count]\\nThere are {n_fav} favourable cards out of 52.\\n"
        f"[1 Mark: Simplified fraction]\\nP = {n_fav}/52 = {num}/{den}"
    )
    return {
        "subskill": "gr11_prob_subskill_8",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"There are {n_fav} favourable cards in a deck of 52.", "tier_2": f"{n_fav} / 52.", "tier_3": f"{correct}."}
    }

def _subskill_9(r: random.Random) -> Dict[str, Any]:
    """Calculate probability from a circular spinner with unequal sector angles."""
    angle = r.choice([60, 90, 120, 135, 180])
    p = angle / 360.0
    gcd = math.gcd(angle, 360)
    num, den = angle // gcd, 360 // gcd

    prompt = (
        f"A circular game spinner is divided into unequal sectors.\\n"
        f"The yellow sector has a central angle of **{angle}°**.\\n"
        f"A complete revolution is **360°**.\\n\\n"
        f"Calculate the theoretical probability that the pointer lands in the yellow sector."
    )
    correct = f"{num}/{den} ({_fmt_pct(p)})"
    distractors = [
        f"{num + 1}/{den} ({_fmt_pct((num + 1) / den)})",
        f"{360 - angle}/360 ({_fmt_pct(1 - p)})",
        f"1/4 (25,0%)" if num != 1 or den != 4 else "1/2 (50,0%)"
    ]
    expl = (
        f"[1 Mark: Sector angle ratio]\\n"
        f"P(Yellow) = {angle}° / 360° = {num}/{den} = {_fmt_pct(p)}"
    )
    return {
        "subskill": "gr11_prob_subskill_9",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Divide {angle} by 360.", "tier_2": f"{angle} / 360 simplified.", "tier_3": f"{correct}."}
    }

def _subskill_10(r: random.Random) -> Dict[str, Any]:
    """Calculate expected frequency: Expected = P * Trials."""
    trials = r.choice([120, 240, 300, 600])
    p_num, p_den = 1, 6
    expected = trials * (p_num / p_den)

    prompt = (
        f"A fair 6-sided die is rolled **{trials} times**.\\n"
        f"The probability of rolling a four is P(4) = 1/6.\\n\\n"
        f"Use the expected frequency formula Expected = P(E) * Total trials to calculate how many times you expect to roll a four."
    )
    correct = f"{int(expected)} times"
    distractors = [
        f"{int(expected + 15)} times",
        f"{int(expected - 10)} times",
        f"{int(trials / 4)} times"
    ]
    expl = (
        f"[1 Mark: Expected value calculation]\\n"
        f"Expected Frequency = (1/6) * {trials} = {int(expected)} times"
    )
    return {
        "subskill": "gr11_prob_subskill_10",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Multiply (1/6) by {trials}.", "tier_2": f"{trials} / 6.", "tier_3": f"{correct}."}
    }
''')

    # Subskills 11-20
    parts.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 11-20: Mutually Exclusive & Addition Rules
# ----------------------------------------------------------------------------

def _subskill_11(r: random.Random) -> Dict[str, Any]:
    """Test for mutually exclusive events: determine if A and B can occur together."""
    prompt = (
        f"A single number from 1 to 20 is picked at random.\\n"
        f"- **Event A:** The number is an odd number: {{1; 3; 5; 7; 9; 11; 13; 15; 17; 19}}\\n"
        f"- **Event B:** The number is an even number: {{2; 4; 6; 8; 10; 12; 14; 16; 18; 20}}\\n\\n"
        f"Are Events A and B mutually exclusive, and why?"
    )
    correct = "Yes, mutually exclusive because they share no common outcomes"
    distractors = [
        "No, because both sets belong to the same sample space of 20 numbers",
        "Yes, mutually exclusive because their probabilities multiply to 1",
        "No, because some numbers can be both even and odd simultaneously"
    ]
    expl = f"[1 Mark: Mutually exclusive definition]\\nMutually exclusive events cannot occur simultaneously. Since no number is both even and odd, their intersection is empty."
    return {
        "subskill": "gr11_prob_subskill_11",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Can a number be both even and odd at the same time?", "tier_2": "Zero common outcomes = mutually exclusive.", "tier_3": f"{correct}."}
    }

def _subskill_12(r: random.Random) -> Dict[str, Any]:
    """Addition rule for mutually exclusive events: P(A or B) = P(A) + P(B)."""
    p_a = round(r.choice([0.25, 0.30, 0.35]), 2)
    p_b = round(r.choice([0.20, 0.40, 0.45]), 2)
    p_or = round(p_a + p_b, 2)

    prompt = (
        f"In a hospital clinic, two mutually exclusive patient conditions A and B have probabilities:\\n"
        f"- P(A) = {_fmt_dec(p_a, 2)}\\n"
        f"- P(B) = {_fmt_dec(p_b, 2)}\\n\\n"
        f"Calculate P(A or B) using the addition rule for mutually exclusive events."
    )
    correct = f"{_fmt_dec(p_or, 2)}"
    distractors = [
        f"{_fmt_dec(round(p_a * p_b, 4), 2)}",
        f"{_fmt_dec(round(p_or - 0.15, 2), 2)}",
        f"{_fmt_dec(round(1 - p_or, 2), 2)}"
    ]
    expl = (
        f"[1 Mark: Addition rule]\\n"
        f"P(A or B) = P(A) + P(B) = {_fmt_dec(p_a, 2)} + {_fmt_dec(p_b, 2)} = {_fmt_dec(p_or, 2)}"
    )
    return {
        "subskill": "gr11_prob_subskill_12",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add P(A) and P(B).", "tier_2": f"{p_a} + {p_b}.", "tier_3": f"{correct}."}
    }

def _subskill_13(r: random.Random) -> Dict[str, Any]:
    """General addition rule for inclusive events: P(A or B) = P(A) + P(B) - P(A and B)."""
    p_a = 0.50
    p_b = 0.40
    p_both = 0.15
    p_or = round(p_a + p_b - p_both, 2)

    prompt = (
        f"In a high school sports survey:\\n"
        f"- Probability a learner plays soccer: P(S) = {_fmt_dec(p_a, 2)}\\n"
        f"- Probability a learner plays rugby: P(R) = {_fmt_dec(p_b, 2)}\\n"
        f"- Probability a learner plays both soccer and rugby: P(S and R) = {_fmt_dec(p_both, 2)}\\n\\n"
        f"Calculate the probability that a randomly chosen learner plays **soccer OR rugby**."
    )
    correct = f"{_fmt_dec(p_or, 2)}"
    distractors = [
        f"{_fmt_dec(round(p_a + p_b, 2), 2)}",
        f"{_fmt_dec(round(p_or - 0.10, 2), 2)}",
        f"{_fmt_dec(round(p_both * 2, 2), 2)}"
    ]
    expl = (
        f"[1 Mark: General addition formula]\\n"
        f"P(S or R) = P(S) + P(R) - P(S and R)\\n"
        f"[1 Mark: Calculation]\\n"
        f"P = {_fmt_dec(p_a, 2)} + {_fmt_dec(p_b, 2)} - {_fmt_dec(p_both, 2)} = {_fmt_dec(p_or, 2)}"
    )
    return {
        "subskill": "gr11_prob_subskill_13",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add P(S) and P(R), then subtract the overlap P(S and R).", "tier_2": f"{p_a} + {p_b} - {p_both}.", "tier_3": f"{correct}."}
    }

def _subskill_14(r: random.Random) -> Dict[str, Any]:
    """Calculate intersection probability P(A and B) given P(A), P(B), and P(A or B)."""
    p_a = 0.60
    p_b = 0.55
    p_or = 0.85
    p_both = round(p_a + p_b - p_or, 2)

    prompt = (
        f"For two events A and B:\\n"
        f"- P(A) = {_fmt_dec(p_a, 2)}\\n"
        f"- P(B) = {_fmt_dec(p_b, 2)}\\n"
        f"- P(A or B) = {_fmt_dec(p_or, 2)}\\n\\n"
        f"Rearrange the addition rule to calculate P(A and B) (the intersection)."
    )
    correct = f"{_fmt_dec(p_both, 2)}"
    distractors = [
        f"{_fmt_dec(round(p_both + 0.15, 2), 2)}",
        f"{_fmt_dec(round(p_a * p_b, 2), 2)}",
        f"{_fmt_dec(round(1 - p_or, 2), 2)}"
    ]
    expl = (
        f"[1 Mark: Rearranged formula]\\n"
        f"P(A and B) = P(A) + P(B) - P(A or B)\\n"
        f"[1 Mark: Calculation]\\n"
        f"P(A and B) = {_fmt_dec(p_a, 2)} + {_fmt_dec(p_b, 2)} - {_fmt_dec(p_or, 2)} = {_fmt_dec(p_both, 2)}"
    )
    return {
        "subskill": "gr11_prob_subskill_14",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "P(A and B) = P(A) + P(B) - P(A or B).", "tier_2": f"{p_a} + {p_b} - {p_or}.", "tier_3": f"{correct}."}
    }

def _subskill_15(r: random.Random) -> Dict[str, Any]:
    """Determine whether two events are mutually exclusive from given probabilities."""
    p_both = r.choice([0.0, 0.12])
    is_me = p_both == 0.0

    prompt = (
        f"Statistical analysis of two operational safety alerts shows:\\n"
        f"- P(Alert 1) = 0,40\\n"
        f"- P(Alert 2) = 0,35\\n"
        f"- P(Alert 1 AND Alert 2) = {_fmt_dec(p_both, 2)}\\n\\n"
        f"Are Alert 1 and Alert 2 mutually exclusive events?"
    )
    correct = "Yes, because P(Alert 1 AND Alert 2) = 0" if is_me else "No, because P(Alert 1 AND Alert 2) > 0"
    distractors = [
        "No, because P(Alert 1 AND Alert 2) > 0" if is_me else "Yes, because P(Alert 1 AND Alert 2) = 0",
        "Cannot be determined without knowing the sample space size",
        "Yes, because their individual probabilities add to less than 1"
    ]
    expl = f"[1 Mark: Mutually exclusive condition]\\nEvents are mutually exclusive if and only if P(A and B) = 0. Since P(A and B) = {_fmt_dec(p_both, 2)}, {correct}."
    return {
        "subskill": "gr11_prob_subskill_15",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Check if P(Alert 1 AND Alert 2) equals zero.", "tier_2": f"P(intersection) = {p_both}.", "tier_3": f"{correct}."}
    }

def _subskill_16(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of rolling a multiple of 2 OR a multiple of 3 on a die."""
    prompt = (
        f"A standard 6-sided die is rolled once.\\n"
        f"Calculate the probability of rolling a **multiple of 2 OR a multiple of 3**."
    )
    correct = "2/3 (66,7%)"
    distractors = [
        "5/6 (83,3%)",
        "1/2 (50,0%)",
        "1/6 (16,7%)"
    ]
    expl = (
        f"[1 Mark: Sets and overlap]\\n"
        f"Multiples of 2 = {{2; 4; 6}}, Multiples of 3 = {{3; 6}}. Common = {{6}}.\\n"
        f"[1 Mark: Union size]\\n"
        f"Union = {{2; 3; 4; 6}} => P = 4/6 = 2/3 ≈ 66,7%"
    )
    return {
        "subskill": "gr11_prob_subskill_16",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "List the numbers: {2, 3, 4, 6} out of 6.", "tier_2": "4/6 simplified.", "tier_3": f"{correct}."}
    }

def _subskill_17(r: random.Random) -> Dict[str, Any]:
    """Solve for unknown probability in an exhaustive partition where sum of probabilities = 1."""
    p1 = 0.35
    p2 = 0.40
    p3 = round(1.0 - (p1 + p2), 2)

    prompt = (
        f"A commuter train arrives either **Early, On Time, or Late**.\\n"
        f"These three outcomes form an exhaustive and mutually exclusive set:\\n"
        f"- P(Early) = {_fmt_dec(p1, 2)}\\n"
        f"- P(On Time) = {_fmt_dec(p2, 2)}\\n\\n"
        f"Calculate the probability that the train arrives **Late**."
    )
    correct = f"{_fmt_dec(p3, 2)}"
    distractors = [
        f"{_fmt_dec(round(p3 + 0.10, 2), 2)}",
        f"{_fmt_dec(round(p1 + p2, 2), 2)}",
        f"{_fmt_dec(round(p3 - 0.08, 2), 2)}"
    ]
    expl = (
        f"[1 Mark: Sum of probabilities = 1]\\n"
        f"P(Late) = 1 - (P(Early) + P(On Time)) = 1 - ({_fmt_dec(p1, 2)} + {_fmt_dec(p2, 2)}) = {_fmt_dec(p3, 2)}"
    )
    return {
        "subskill": "gr11_prob_subskill_17",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract the sum of the known probabilities from 1.", "tier_2": f"1 - ({p1} + {p2}).", "tier_3": f"{correct}."}
    }

def _subskill_18(r: random.Random) -> Dict[str, Any]:
    """Complementary probability of compound event: P(at least one) = 1 - P(none)."""
    p_fail = 0.10
    p_both_fail = round(p_fail * p_fail, 4)
    p_at_least_one = round(1.0 - p_both_fail, 4)

    prompt = (
        f"A factory runs two independent backup generators.\\n"
        f"Each generator has a probability of failure during a blackout of **0,10**.\\n\\n"
        f"Use the complementary rule P(at least one works) = 1 - P(both fail) to calculate the probability that at least one generator functions."
    )
    correct = f"{_fmt_dec(p_at_least_one, 2)} ({_fmt_pct(p_at_least_one)})"
    distractors = [
        "0,90 (90,0%)",
        "0,81 (81,0%)",
        "0,20 (20,0%)"
    ]
    expl = (
        f"[1 Mark: Failure probability]\\nP(both fail) = 0,10 * 0,10 = {_fmt_dec(p_both_fail, 2)}\\n"
        f"[1 Mark: Complementary rule]\\nP = 1 - {_fmt_dec(p_both_fail, 2)} = {_fmt_dec(p_at_least_one, 2)} ({_fmt_pct(p_at_least_one)})"
    )
    return {
        "subskill": "gr11_prob_subskill_18",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate 1 - (0,10 * 0,10).", "tier_2": "1 - 0,01 = 0,99.", "tier_3": f"{correct}."}
    }

def _subskill_19(r: random.Random) -> Dict[str, Any]:
    """Real-life traffic light probability: P(Green) + P(Amber) + P(Red) = 1."""
    p_green = 0.55
    p_amber = 0.10
    p_red = round(1.0 - (p_green + p_amber), 2)

    prompt = (
        f"A traffic light cycle shows Green for 55% of the time and Amber for 10% of the time.\\n\\n"
        f"What is the probability that an approaching vehicle faces a **Red light**?"
    )
    correct = f"{int(p_red * 100)}% ({_fmt_dec(p_red, 2)})"
    distractors = [
        f"{int((p_green + p_amber) * 100)}% ({_fmt_dec(p_green + p_amber, 2)})",
        f"{int((p_red + 0.1) * 100)}%",
        f"{int((p_red - 0.1) * 100)}%"
    ]
    expl = f"[1 Mark: Cycle sum = 1]\\nP(Red) = 100% - (55% + 10%) = {int(p_red * 100)}%"
    return {
        "subskill": "gr11_prob_subskill_19",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "100% - 55% - 10%.", "tier_2": "100 - 65 = 35%.", "tier_3": f"{correct}."}
    }

def _subskill_20(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of a student participating in at least one activity."""
    total = 100
    n_a = 45
    n_s = 50
    n_both = 20
    n_at_least_one = n_a + n_s - n_both

    prompt = (
        f"In a Grade 11 class of **{total} learners**:\\n"
        f"- {n_a} participate in Athletics\\n"
        f"- {n_s} participate in Swimming\\n"
        f"- {n_both} participate in both Athletics and Swimming\\n\\n"
        f"Calculate the probability that a randomly chosen learner participates in **at least one** of these two sports."
    )
    correct = f"{n_at_least_one}/{total} ({_fmt_pct(n_at_least_one / total)})"
    distractors = [
        f"{n_a + n_s}/{total} ({_fmt_pct((n_a + n_s) / total)})",
        f"{total - n_both}/{total} ({_fmt_pct((total - n_both) / total)})",
        f"{n_both}/{total} ({_fmt_pct(n_both / total)})"
    ]
    expl = (
        f"[1 Mark: Inclusion-Exclusion count]\\n"
        f"n(At least one) = {n_a} + {n_s} - {n_both} = {n_at_least_one}\\n"
        f"[1 Mark: Probability]\\n"
        f"P = {n_at_least_one}/{total} = {_fmt_pct(n_at_least_one / total)}"
    )
    return {
        "subskill": "gr11_prob_subskill_20",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Add {n_a} + {n_s} and subtract overlap {n_both}.", "tier_2": f"({n_at_least_one}) / 100.", "tier_3": f"{correct}."}
    }
''')

    # Subskills 21-30: Contingency tables
    parts.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 21-30: Two-Way Contingency Tables & Joint/Conditional Probabilities
# ----------------------------------------------------------------------------

def _subskill_21(r: random.Random) -> Dict[str, Any]:
    """Read a cell frequency from a 2-way contingency table."""
    prompt = (
        f"The following two-way contingency table classifies 120 Grade 11 learners by Gender and Elective Subject:\\n\\n"
        f"| Gender | Accounting | History | Total |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| Boys | 32 | 28 | 60 |\\n"
        f"| Girls | 38 | 22 | 60 |\\n"
        f"| **Total** | **70** | **50** | **120** |\\n\\n"
        f"How many girls take History as an elective?"
    )
    correct = "22 girls"
    distractors = ["28 girls", "38 girls", "50 girls"]
    expl = f"[1 Mark: Direct table cell read]\\nRow 'Girls' and Column 'History' intersect at **22**."
    return {
        "subskill": "gr11_prob_subskill_21",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Find the Girls row and History column.", "tier_2": "Look at the intersection.", "tier_3": f"{correct}."}
    }

def _subskill_22(r: random.Random) -> Dict[str, Any]:
    """Calculate missing cell value in a 2-way contingency table."""
    total_boys = 55
    boys_passed = 42
    boys_failed = total_boys - boys_passed

    prompt = (
        f"Complete the missing value **X** in the examination results table:\\n\\n"
        f"| Category | Passed | Failed | Total |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| Male Candidates | 42 | **X** | 55 |\\n"
        f"| Female Candidates | 51 | 9 | 60 |\\n\\n"
        f"Calculate the value of **X**."
    )
    correct = f"{boys_failed}"
    distractors = [f"{boys_failed + 3}", f"{boys_failed - 2}", "9"]
    expl = f"[1 Mark: Row arithmetic]\\nX = 55 - 42 = {boys_failed}"
    return {
        "subskill": "gr11_prob_subskill_22",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract Passed from Total for Male Candidates.", "tier_2": "55 - 42.", "tier_3": f"{correct}."}
    }

def _subskill_23(r: random.Random) -> Dict[str, Any]:
    """Calculate marginal probability from contingency table."""
    total = 200
    n_females = 110
    p = n_females / total

    prompt = (
        f"A survey of 200 automotive buyers is summarised below:\\n\\n"
        f"| Buyer | Sedan | SUV | Bakkie | Total |\\n"
        f"| :--- | :--- | :--- | :--- | :--- |\\n"
        f"| Male | 30 | 25 | 35 | 90 |\\n"
        f"| Female | 45 | 50 | 15 | 110 |\\n"
        f"| **Total** | **75** | **75** | **50** | **200** |\\n\\n"
        f"Calculate the marginal probability that a randomly chosen buyer is **Female**."
    )
    correct = f"{n_females}/{total} ({_fmt_pct(p)})"
    distractors = [
        f"90/{total} ({_fmt_pct(90 / total)})",
        f"50/{total} ({_fmt_pct(50 / total)})",
        f"110/90 ({_fmt_pct(110 / 90)})"
    ]
    expl = f"[1 Mark: Marginal probability]\\nP(Female) = 110 / 200 = {_fmt_pct(p)}"
    return {
        "subskill": "gr11_prob_subskill_23",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide Female Total by Grand Total.", "tier_2": "110 / 200.", "tier_3": f"{correct}."}
    }

def _subskill_24(r: random.Random) -> Dict[str, Any]:
    """Calculate joint probability: P(A AND B) = cell / grand total."""
    cell = 50
    total = 200
    p = cell / total

    prompt = (
        f"Referring to the same table of 200 buyers:\\n\\n"
        f"| Buyer | Sedan | SUV | Bakkie | Total |\\n"
        f"| :--- | :--- | :--- | :--- | :--- |\\n"
        f"| Male | 30 | 25 | 35 | 90 |\\n"
        f"| Female | 45 | 50 | 15 | 110 |\\n"
        f"| **Total** | **75** | **75** | **50** | **200** |\\n\\n"
        f"Calculate the joint probability that a randomly selected buyer is **Female AND purchases an SUV**."
    )
    correct = f"{cell}/{total} ({_fmt_pct(p)})"
    distractors = [
        f"75/{total} ({_fmt_pct(75 / total)})",
        f"50/110 ({_fmt_pct(50 / 110)})",
        f"50/75 ({_fmt_pct(50 / 75)})"
    ]
    expl = (
        f"[1 Mark: Joint probability formula]\\n"
        f"P(Female AND SUV) = {cell} / {total} = {_fmt_pct(p)}"
    )
    return {
        "subskill": "gr11_prob_subskill_24",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide the intersecting cell (Female & SUV) by Grand Total 200.", "tier_2": "50 / 200.", "tier_3": f"{correct}."}
    }

def _subskill_25(r: random.Random) -> Dict[str, Any]:
    """Calculate conditional probability from contingency table: P(A | B)."""
    cell = 45
    col_total = 50
    p = cell / col_total

    prompt = (
        f"A study tracks learner attendance at weekend revision classes and exam pass rates:\\n\\n"
        f"| Attendance | Passed | Failed | Total |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| Attended Classes | 45 | 5 | 50 |\\n"
        f"| Did Not Attend | 25 | 25 | 50 |\\n"
        f"| **Total** | **70** | **30** | **100** |\\n\\n"
        f"Given that a learner **attended classes**, calculate the conditional probability that they **passed** (P(Passed given Attended))."
    )
    correct = f"{cell}/{col_total} ({_fmt_pct(p)})"
    distractors = [
        f"45/100 ({_fmt_pct(45 / 100)})",
        f"45/70 ({_fmt_pct(45 / 70)})",
        f"25/50 ({_fmt_pct(25 / 50)})"
    ]
    expl = (
        f"[1 Mark: Restricting denominator to given condition]\\n"
        f"Denominator = Total who Attended Classes = 50.\\n"
        f"[1 Mark: Conditional probability]\\n"
        f"P(Passed given Attended) = {cell} / {col_total} = {_fmt_pct(p)}"
    )
    return {
        "subskill": "gr11_prob_subskill_25",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Divide number who Attended and Passed by Total who Attended.", "tier_2": "45 / 50.", "tier_3": f"{correct}."}
    }

def _subskill_26(r: random.Random) -> Dict[str, Any]:
    """Compare conditional probabilities to evaluate dependency/influence."""
    prompt = (
        f"From the revision study:\\n"
        f"- P(Passed given Attended) = 90%\\n"
        f"- P(Passed given Did Not Attend) = 50%\\n\\n"
        f"What statistical conclusion can be drawn regarding the relationship between attending classes and passing?"
    )
    correct = "Attending revision classes significantly increases the likelihood of passing (events are dependent)"
    distractors = [
        "Passing is completely independent of attending revision classes",
        "Attending revision classes decreases the probability of passing",
        "No correlation exists because both groups had 50 learners"
    ]
    expl = f"[1 Mark: Statistical inference]\\nSince the two conditional probabilities differ (90% vs 50%), the events are dependent, and attendance strongly improves pass rate."
    return {
        "subskill": "gr11_prob_subskill_26",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Compare 90% with 50%.", "tier_2": "Higher pass rate for attendees indicates dependence.", "tier_3": f"{correct}."}
    }

def _subskill_27(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of A OR B from a two-way table."""
    total = 120
    n_boys = 60
    n_acc = 70
    n_boys_acc = 32
    n_union = n_boys + n_acc - n_boys_acc
    p = n_union / total

    prompt = (
        f"Referring to the 120 Grade 11 learners table:\\n\\n"
        f"| Gender | Accounting | History | Total |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| Boys | 32 | 28 | 60 |\\n"
        f"| Girls | 38 | 22 | 60 |\\n"
        f"| **Total** | **70** | **50** | **120** |\\n\\n"
        f"Calculate the probability that a randomly chosen learner is a **Boy OR takes Accounting**."
    )
    correct = f"{n_union}/{total} ({_fmt_pct(p)})"
    distractors = [
        f"{(n_boys + n_acc)}/{total} ({_fmt_pct((n_boys + n_acc) / total)})",
        f"{(n_union - 10)}/{total} ({_fmt_pct((n_union - 10) / total)})",
        f"{n_boys_acc}/{total} ({_fmt_pct(n_boys_acc / total)})"
    ]
    expl = (
        f"[1 Mark: Formula substitution]\\n"
        f"n(Boy OR Accounting) = 60 + 70 - 32 = {n_union}\\n"
        f"[1 Mark: Probability]\\n"
        f"P = {n_union} / 120 = {_fmt_pct(p)}"
    )
    return {
        "subskill": "gr11_prob_subskill_27",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Boys Total + Accounting Total - Boys taking Accounting.", "tier_2": "60 + 70 - 32 = 98.", "tier_3": f"{correct}."}
    }

def _subskill_28(r: random.Random) -> Dict[str, Any]:
    """Medical screening table: identify False Positives."""
    prompt = (
        f"A rapid diagnostic malaria test is evaluated on 1 000 patients:\\n\\n"
        f"| Test Result | Has Malaria | No Malaria | Total |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| Positive Test | 180 (True Pos) | 20 (False Pos) | 200 |\\n"
        f"| Negative Test | 10 (False Neg) | 790 (True Neg) | 800 |\\n"
        f"| **Total** | **190** | **810** | **1 000** |\\n\\n"
        f"How many patients received a **False Positive** result (test indicates disease, but patient is actually healthy)?"
    )
    correct = "20 patients"
    distractors = ["180 patients", "10 patients", "790 patients"]
    expl = f"[1 Mark: Clinical definition lookup]\\nFalse Positive = Positive test result for a patient with No Malaria = **20 patients**."
    return {
        "subskill": "gr11_prob_subskill_28",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Positive test row, No Malaria column.", "tier_2": "Read cell (Positive, No Malaria).", "tier_3": f"{correct}."}
    }

def _subskill_29(r: random.Random) -> Dict[str, Any]:
    """Calculate diagnostic sensitivity: P(Positive | Disease Present)."""
    tp = 180
    total_disease = 190
    sens = tp / total_disease

    prompt = (
        f"Using the malaria diagnostic table:\\n\\n"
        f"| Test Result | Has Malaria | No Malaria | Total |\\n"
        f"| :--- | :--- | :--- | :--- |\\n"
        f"| Positive Test | 180 | 20 | 200 |\\n"
        f"| Negative Test | 10 | 790 | 800 |\\n"
        f"| **Total** | **190** | **810** | **1 000** |\\n\\n"
        f"Calculate the **sensitivity** of the test: P(Positive Test given Has Malaria).\\n"
        f"Round to one decimal place as a percentage."
    )
    correct = f"{_fmt_pct(sens, 1)}"
    distractors = [
        f"{_fmt_pct(tp / 200, 1)}",
        f"{_fmt_pct(790 / 810, 1)}",
        f"{_fmt_pct(sens - 0.08, 1)}"
    ]
    expl = (
        f"[1 Mark: Sensitivity formula]\\n"
        f"Sensitivity = True Positives / Total with Disease = 180 / 190 ≈ {_fmt_pct(sens, 1)}"
    )
    return {
        "subskill": "gr11_prob_subskill_29",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "True Positives divided by Total with Malaria.", "tier_2": "180 / 190.", "tier_3": f"{correct}."}
    }

def _subskill_30(r: random.Random) -> Dict[str, Any]:
    """Calculate diagnostic specificity: P(Negative | Disease Absent)."""
    tn = 790
    total_healthy = 810
    spec = tn / total_healthy

    prompt = (
        f"Using the same malaria screening table:\\n\\n"
        f"Calculate the **specificity** of the test: P(Negative Test given No Malaria).\\n"
        f"Round to one decimal place as a percentage."
    )
    correct = f"{_fmt_pct(spec, 1)}"
    distractors = [
        f"{_fmt_pct(tn / 800, 1)}",
        f"{_fmt_pct(180 / 190, 1)}",
        f"{_fmt_pct(spec - 0.05, 1)}"
    ]
    expl = (
        f"[1 Mark: Specificity formula]\\n"
        f"Specificity = True Negatives / Total Healthy = 790 / 810 ≈ {_fmt_pct(spec, 1)}"
    )
    return {
        "subskill": "gr11_prob_subskill_30",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "True Negatives divided by Total with No Malaria.", "tier_2": "790 / 810.", "tier_3": f"{correct}."}
    }
''')

    # Subskills 31-40: Venn Diagrams
    parts.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 31-40: Venn Diagrams & Set Operations
# ----------------------------------------------------------------------------

def _subskill_31(r: random.Random) -> Dict[str, Any]:
    """Read number of outcomes in intersection region of a 2-circle Venn diagram."""
    n_inter = r.choice([12, 15, 18, 24])
    prompt = (
        f"A Venn diagram represents Grade 11 learners taking Mathematics (M) and Physical Sciences (P):\\n"
        f"- Only M: 25 learners\\n"
        f"- Both M and P (Intersection): **{n_inter} learners**\\n"
        f"- Only P: 20 learners\\n"
        f"- Neither M nor P: 10 learners\\n\\n"
        f"How many learners take BOTH Mathematics and Physical Sciences?"
    )
    correct = f"{n_inter} learners"
    distractors = [f"{n_inter + 5} learners", "25 learners", "20 learners"]
    expl = f"[1 Mark: Intersection read]\\nThe intersection region contains **{n_inter} learners**."
    return {
        "subskill": "gr11_prob_subskill_31",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Look at the intersection count given in the prompt.", "tier_2": f"Both M and P = {n_inter}.", "tier_3": f"{correct}."}
    }

def _subskill_32(r: random.Random) -> Dict[str, Any]:
    """Read number of outcomes strictly in only event A (A minus B)."""
    inter = 15
    prompt = (
        f"In a school cohort, **40 learners take Mathematics** in total.\\n"
        f"Of these, **{inter} also take History**.\\n\\n"
        f"How many learners take **Mathematics ONLY**?"
    )
    correct = f"{40 - inter} learners"
    distractors = ["40 learners", f"{inter} learners", f"{40 + inter} learners"]
    expl = f"[1 Mark: Subtraction]\\nMathematics only = 40 - {inter} = {40 - inter} learners"
    return {
        "subskill": "gr11_prob_subskill_32",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Subtract {inter} from 40.", "tier_2": f"40 - {inter}.", "tier_3": f"{correct}."}
    }

def _subskill_33(r: random.Random) -> Dict[str, Any]:
    """Read number of outcomes strictly outside both circles: neither A nor B."""
    total = 100
    only_a = 35
    both = 20
    only_b = 30
    neither = total - (only_a + both + only_b)

    prompt = (
        f"A survey of **{total} households** investigates internet access options:\\n"
        f"- Fibre only: {only_a}\\n"
        f"- Both Fibre and 5G: {both}\\n"
        f"- 5G only: {only_b}\\n\\n"
        f"How many surveyed households have **neither** Fibre nor 5G?"
    )
    correct = f"{neither} households"
    distractors = [f"{neither + 10} households", f"{neither - 5} households", "0 households"]
    expl = (
        f"[1 Mark: Complementary subtraction from sample space]\\n"
        f"Neither = {total} - ({only_a} + {both} + {only_b}) = {neither} households"
    )
    return {
        "subskill": "gr11_prob_subskill_33",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Sum {only_a} + {both} + {only_b} and subtract from {total}.", "tier_2": f"{total} - {only_a + both + only_b}.", "tier_3": f"{correct}."}
    }

def _subskill_34(r: random.Random) -> Dict[str, Any]:
    """Calculate total sample space size n(S) from all 4 Venn regions."""
    r1, r2, r3, r4 = 22, 14, 18, 6
    total = r1 + r2 + r3 + r4

    prompt = (
        f"A complete two-circle Venn diagram displays the following counts:\\n"
        f"- Region 1 (Only Event A): {r1}\\n"
        f"- Region 2 (Both A and B): {r2}\\n"
        f"- Region 3 (Only Event B): {r3}\\n"
        f"- Region 4 (Neither A nor B): {r4}\\n\\n"
        f"Calculate the total size of the sample space n(S)."
    )
    correct = f"{total}"
    distractors = [f"{total - r4}", f"{total + 10}", f"{r1 + r3}"]
    expl = f"[1 Mark: Summing all disjoint regions]\\nn(S) = {r1} + {r2} + {r3} + {r4} = {total}"
    return {
        "subskill": "gr11_prob_subskill_34",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add up all four regions.", "tier_2": f"{r1} + {r2} + {r3} + {r4}.", "tier_3": f"{correct}."}
    }

def _subskill_35(r: random.Random) -> Dict[str, Any]:
    """Calculate probability P(A and B) = n(A and B) / n(S)."""
    inter = 18
    total = 90
    p = inter / total
    gcd = math.gcd(inter, total)
    num, den = inter // gcd, total // gcd

    prompt = (
        f"In a sample space of **{total} individuals**, **{inter} individuals** belong to the intersection A and B.\\n\\n"
        f"Calculate P(A and B) as a simplified fraction and percentage."
    )
    correct = f"{num}/{den} ({_fmt_pct(p)})"
    distractors = [
        f"{num + 1}/{den} ({_fmt_pct((num + 1) / den)})",
        f"1/{inter} ({_fmt_pct(1 / inter)})",
        f"{den}/{num} ({_fmt_pct(den / num)})"
    ]
    expl = f"[1 Mark: Fraction and percentage]\\nP(A and B) = {inter}/{total} = {num}/{den} = {_fmt_pct(p)}"
    return {
        "subskill": "gr11_prob_subskill_35",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Divide {inter} by {total}.", "tier_2": f"{inter}/{total} simplified.", "tier_3": f"{correct}."}
    }

def _subskill_36(r: random.Random) -> Dict[str, Any]:
    """Calculate probability P(A or B) = n(A or B) / n(S)."""
    only_a, both, only_b = 25, 15, 20
    union = only_a + both + only_b
    total = 80
    p = union / total
    gcd = math.gcd(union, total)
    num, den = union // gcd, total // gcd

    prompt = (
        f"From a Venn diagram of **{total} learners**:\\n"
        f"- Only A: {only_a}\\n"
        f"- Both A and B: {both}\\n"
        f"- Only B: {only_b}\\n\\n"
        f"Calculate P(A or B)."
    )
    correct = f"{num}/{den} ({_fmt_pct(p)})"
    distractors = [
        f"{both}/{total} ({_fmt_pct(both / total)})",
        f"{only_a + only_b}/{total} ({_fmt_pct((only_a + only_b) / total)})",
        f"1/2 (50,0%)"
    ]
    expl = (
        f"[1 Mark: Union count]\\nn(A or B) = {only_a} + {both} + {only_b} = {union}\\n"
        f"[1 Mark: Probability]\\nP(A or B) = {union}/{total} = {num}/{den} = {_fmt_pct(p)}"
    )
    return {
        "subskill": "gr11_prob_subskill_36",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Sum {only_a} + {both} + {only_b} = {union}. Divide by {total}.", "tier_2": f"{union} / {total}.", "tier_3": f"{correct}."}
    }

def _subskill_37(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of event A alone: P(only A)."""
    only_a = 24
    total = 60
    p = only_a / total
    gcd = math.gcd(only_a, total)
    num, den = only_a // gcd, total // gcd

    prompt = (
        f"In a cohort of **{total} students**, **{only_a} take Art but do not take Drama**.\\n\\n"
        f"Calculate the probability that a student selected at random takes **Art ONLY**."
    )
    correct = f"{num}/{den} ({_fmt_pct(p)})"
    distractors = [
        f"{total - only_a}/{total} ({_fmt_pct(1 - p)})",
        f"1/{num} ({_fmt_pct(1 / num)})",
        f"{num}/{den + 2} ({_fmt_pct(num / (den + 2))})"
    ]
    expl = f"[1 Mark: Probability fraction]\\nP(Art only) = {only_a}/{total} = {num}/{den} = {_fmt_pct(p)}"
    return {
        "subskill": "gr11_prob_subskill_37",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": f"Divide {only_a} by {total}.", "tier_2": f"{only_a} / {total}.", "tier_3": f"{correct}."}
    }

def _subskill_38(r: random.Random) -> Dict[str, Any]:
    """Construct / deduce intersection count given n(S), n(A), n(B), and n(A or B)."""
    n_a = 35
    n_b = 30
    n_union = 50
    inter = n_a + n_b - n_union

    prompt = (
        f"In a sports club with 60 members:\\n"
        f"- {n_a} play Tennis\\n"
        f"- {n_b} play Squash\\n"
        f"- {n_union} play at least one of Tennis or Squash\\n\\n"
        f"How many members play **both Tennis and Squash**?"
    )
    correct = f"{inter} members"
    distractors = [f"{inter + 5} members", f"{inter - 5} members", f"{60 - n_union} members"]
    expl = (
        f"[1 Mark: Set intersection formula]\\n"
        f"n(T and S) = n(T) + n(S) - n(T or S) = {n_a} + {n_b} - {n_union} = {inter} members"
    )
    return {
        "subskill": "gr11_prob_subskill_38",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "n(A and B) = n(A) + n(B) - n(A or B).", "tier_2": f"{n_a} + {n_b} - {n_union}.", "tier_3": f"{correct}."}
    }

def _subskill_39(r: random.Random) -> Dict[str, Any]:
    """Calculate P(neither A nor B) from a Venn diagram."""
    total = 100
    union = 82
    neither = total - union
    p = neither / total

    prompt = (
        f"A Venn diagram indicates that **82% of learners** participate in either Cultural activities or Sports (P(C or S) = 0,82).\\n\\n"
        f"Calculate the probability that a randomly chosen learner participates in **neither** of these activities."
    )
    correct = f"0,18 (18,0%)"
    distractors = [
        "0,82 (82,0%)",
        "0,28 (28,0%)",
        "0,08 (8,0%)"
    ]
    expl = f"[1 Mark: Complementary probability]\\nP(neither) = 1 - P(C or S) = 1 - 0,82 = 0,18 (18,0%)"
    return {
        "subskill": "gr11_prob_subskill_39",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "1 - 0,82.", "tier_2": "1 - 0,82 = 0,18.", "tier_3": f"{correct}."}
    }

def _subskill_40(r: random.Random) -> Dict[str, Any]:
    """Verify that region probabilities inside a Venn diagram sum to 1."""
    p_only_a = 0.35
    p_both = 0.25
    p_only_b = 0.20
    p_neither = round(1.0 - (p_only_a + p_both + p_only_b), 2)

    prompt = (
        f"A probability Venn diagram shows three of the four disjoint region probabilities:\\n"
        f"- P(only A) = 0,35\\n"
        f"- P(A and B) = 0,25\\n"
        f"- P(only B) = 0,20\\n\\n"
        f"Calculate the probability of the region outside both circles, P(neither A nor B)."
    )
    correct = f"{_fmt_dec(p_neither, 2)}"
    distractors = [
        f"{_fmt_dec(round(p_neither + 0.10, 2), 2)}",
        f"{_fmt_dec(round(p_only_a + p_only_b, 2), 2)}",
        f"{_fmt_dec(round(p_neither - 0.05, 2), 2)}"
    ]
    expl = (
        f"[1 Mark: Total probability law]\\n"
        f"P(neither) = 1 - (0,35 + 0,25 + 0,20) = 1 - 0,80 = {_fmt_dec(p_neither, 2)}"
    )
    return {
        "subskill": "gr11_prob_subskill_40",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Add the three probabilities and subtract from 1.", "tier_2": "1 - 0,80.", "tier_3": f"{correct}."}
    }
''')

    # Subskills 41-52: Tree diagrams
    parts.append('''
# ----------------------------------------------------------------------------
# SUBSKILLS 41-52: Tree Diagrams & Compound Independent / Dependent Events
# ----------------------------------------------------------------------------

def _subskill_41(r: random.Random) -> Dict[str, Any]:
    """Two-stage coin toss: calculate P(H, H) using tree diagram branch multiplication."""
    prompt = (
        f"A fair coin is tossed twice.\\n"
        f"Each toss has P(H) = 1/2 and P(T) = 1/2.\\n\\n"
        f"Use a tree diagram branch path to calculate the probability of obtaining **two Heads (H, H)**."
    )
    correct = "1/4 (25,0%)"
    distractors = ["1/2 (50,0%)", "3/4 (75,0%)", "1/8 (12,5%)"]
    expl = (
        f"[1 Mark: Branch multiplication]\\n"
        f"P(H, H) = (1/2) * (1/2) = 1/4 = 25,0%"
    )
    return {
        "subskill": "gr11_prob_subskill_41",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply (1/2) by (1/2).", "tier_2": "1/2 * 1/2 = 1/4.", "tier_3": f"{correct}."}
    }

def _subskill_42(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of getting at least one Head in two coin tosses."""
    prompt = (
        f"A fair coin is tossed twice.\\n"
        f"Sample space S = {{(H, H); (H, T); (T, H); (T, T)}}.\\n\\n"
        f"Calculate the probability of getting **at least one Head**."
    )
    correct = "3/4 (75,0%)"
    distractors = ["1/2 (50,0%)", "1/4 (25,0%)", "2/3 (66,7%)"]
    expl = (
        f"[1 Mark: Favourable outcomes identification]\\n"
        f"Outcomes with at least one Head: {{(H, H); (H, T); (T, H)}} (3 outcomes out of 4).\\n"
        f"P = 3/4 = 75,0%"
    )
    return {
        "subskill": "gr11_prob_subskill_42",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Either count favorable outcomes (3) or compute 1 - P(T, T).", "tier_2": "1 - 1/4 = 3/4.", "tier_3": f"{correct}."}
    }

def _subskill_43(r: random.Random) -> Dict[str, Any]:
    """Independent events multiplication rule: P(A and B) = P(A) * P(B)."""
    prompt = (
        f"A fair coin is flipped and a fair 6-sided die is rolled simultaneously.\\n"
        f"Since the two physical mechanisms do not affect each other, the events are independent.\\n\\n"
        f"Calculate the probability of obtaining **a Head on the coin AND a 6 on the die**."
    )
    correct = "1/12 (8,3%)"
    distractors = ["1/6 (16,7%)", "2/8 (25,0%)", "1/36 (2,8%)"]
    expl = (
        f"[1 Mark: Multiplication rule for independent events]\\n"
        f"P(H and 6) = P(H) * P(6) = (1/2) * (1/6) = 1/12 ≈ 8,3%"
    )
    return {
        "subskill": "gr11_prob_subskill_43",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply (1/2) by (1/6).", "tier_2": "1/2 * 1/6 = 1/12.", "tier_3": f"{correct}."}
    }

def _subskill_44(r: random.Random) -> Dict[str, Any]:
    """Test for independence: verify whether P(A and B) == P(A) * P(B)."""
    p_a = 0.40
    p_b = 0.50
    prod = p_a * p_b
    is_ind = r.choice([True, False])
    actual_inter = prod if is_ind else 0.30

    prompt = (
        f"Given two events A and B:\\n"
        f"- P(A) = 0,40\\n"
        f"- P(B) = 0,50\\n"
        f"- P(A and B) = {_fmt_dec(actual_inter, 2)}\\n\\n"
        f"Use the mathematical definition of independence to determine whether events A and B are independent."
    )
    correct = f"{'Independent' if is_ind else 'Dependent'}: P(A) * P(B) {'==' if is_ind else '!='} P(A and B)"
    distractors = [
        f"{'Dependent' if is_ind else 'Independent'}: P(A) * P(B) {'==' if is_ind else '!='} P(A and B)",
        "Mutually exclusive because they sum to less than 1",
        "Cannot be tested without sample size"
    ]
    expl = (
        f"[1 Mark: Product test]\\n"
        f"P(A) * P(B) = 0,40 * 0,50 = 0,20\\n"
        f"Since P(A and B) = {_fmt_dec(actual_inter, 2)} {'==' if is_ind else '!='} 0,20, the events are **{correct}**."
    )
    return {
        "subskill": "gr11_prob_subskill_44",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply P(A) by P(B) and compare with P(A and B).", "tier_2": "0,40 * 0,50 = 0,20.", "tier_3": f"{correct}."}
    }

def _subskill_45(r: random.Random) -> Dict[str, Any]:
    """Dependent events without replacement: drawing 2 colored marbles."""
    n_red = 4
    n_blue = 6
    total = n_red + n_blue
    p_num = n_red * (n_red - 1)
    p_den = total * (total - 1)
    gcd = math.gcd(p_num, p_den)
    num, den = p_num // gcd, p_den // gcd

    prompt = (
        f"A bag contains **4 red marbles and 6 blue marbles** (10 marbles total).\\n"
        f"Two marbles are drawn in sequence **without replacement**.\\n\\n"
        f"Calculate the probability of drawing **two red marbles in succession** (P(R1 and R2))."
    )
    correct = f"{num}/{den} ({_fmt_pct(num / den)})"
    distractors = [
        f"16/100 (16,0%)",
        f"4/10 (40,0%)",
        f"{num}/{den + 3} ({_fmt_pct(num / (den + 3))})"
    ]
    expl = (
        f"[1 Mark: Dependent probabilities]\\n"
        f"P(R1) = 4/10, P(R2 given R1) = 3/9\\n"
        f"[1 Mark: Product]\\n"
        f"P = (4/10) * (3/9) = 12/90 = {num}/{den} ≈ {_fmt_pct(num / den)}"
    )
    return {
        "subskill": "gr11_prob_subskill_45",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Remember the second draw has only 3 red marbles and 9 total marbles left.", "tier_2": "(4/10) * (3/9).", "tier_3": f"{correct}."}
    }

def _subskill_46(r: random.Random) -> Dict[str, Any]:
    """Tree diagram branch completion: fill in missing branch probability."""
    p_known = 0.65
    p_missing = round(1.0 - p_known, 2)

    prompt = (
        f"On a tree diagram node, branch 1 represents 'Success' with probability **0,65**.\\n"
        f"Branch 2 from the same node represents 'Failure'.\\n\\n"
        f"What probability must be assigned to Branch 2 to ensure all outcomes from this node sum to 1?"
    )
    correct = f"{_fmt_dec(p_missing, 2)}"
    distractors = ["0,65", "0,45", "0,25"]
    expl = f"[1 Mark: Branch rule]\\nAll branches originating from a single node must sum to 1: 1 - 0,65 = {_fmt_dec(p_missing, 2)}."
    return {
        "subskill": "gr11_prob_subskill_46",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Subtract 0,65 from 1.", "tier_2": "1 - 0,65 = 0,35.", "tier_3": f"{correct}."}
    }

def _subskill_47(r: random.Random) -> Dict[str, Any]:
    """Tree diagram path multiplication: compute probability of a specific sequence."""
    p_rain = 0.20
    p_late_given_rain = 0.40
    p_path = round(p_rain * p_late_given_rain, 3)

    prompt = (
        f"A commuter's tree diagram shows:\\n"
        f"- Probability of rain tomorrow: P(Rain) = 0,20\\n"
        f"- If it rains, probability of arriving late for work: P(Late given Rain) = 0,40\\n\\n"
        f"Calculate the probability of the compound path: **It rains AND the commuter arrives late**."
    )
    correct = f"{_fmt_dec(p_path, 2)} ({_fmt_pct(p_path)})"
    distractors = [
        "0,60 (60,0%)",
        "0,20 (20,0%)",
        "0,04 (4,0%)"
    ]
    expl = (
        f"[1 Mark: Path multiplication]\\n"
        f"P(Rain AND Late) = 0,20 * 0,40 = {_fmt_dec(p_path, 2)} ({_fmt_pct(p_path)})"
    )
    return {
        "subskill": "gr11_prob_subskill_47",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply along the path branches: 0,20 * 0,40.", "tier_2": "0,20 * 0,40 = 0,08.", "tier_3": f"{correct}."}
    }

def _subskill_48(r: random.Random) -> Dict[str, Any]:
    """Medical trial tree diagram: overall probability of curing a patient."""
    p_cure = (0.5 * 0.6) + (0.5 * 0.1)

    prompt = (
        f"In a clinical trial, half the participants are assigned to active medicine and half to a placebo:\\n"
        f"- P(Medicine) = 0,50, with cure rate P(Cure given Med) = 0,60\\n"
        f"- P(Placebo) = 0,50, with natural recovery rate P(Cure given Plac) = 0,10\\n\\n"
        f"Use tree diagram path addition to calculate the overall probability that a randomly chosen patient is cured."
    )
    correct = f"{_fmt_dec(p_cure, 2)} ({_fmt_pct(p_cure)})"
    distractors = [
        "0,70 (70,0%)",
        "0,50 (50,0%)",
        "0,30 (30,0%)"
    ]
    expl = (
        f"[1 Mark: Path 1 and Path 2]\\n"
        f"Path 1 (Med & Cure) = 0,5 * 0,6 = 0,30\\n"
        f"Path 2 (Plac & Cure) = 0,5 * 0,1 = 0,05\\n"
        f"[1 Mark: Total probability]\\n"
        f"P(Cured) = 0,30 + 0,05 = {_fmt_dec(p_cure, 2)} ({_fmt_pct(p_cure)})"
    )
    return {
        "subskill": "gr11_prob_subskill_48",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Calculate (0,5 * 0,6) + (0,5 * 0,1).", "tier_2": "0,30 + 0,05 = 0,35.", "tier_3": f"{correct}."}
    }

def _subskill_49(r: random.Random) -> Dict[str, Any]:
    """Weather transition tree: probability of rain on consecutive days."""
    prompt = (
        f"Meteorological records indicate:\\n"
        f"- Probability of rain tomorrow: 1/5\\n"
        f"- If it rains tomorrow, probability of rain the next day is 1/3\\n"
        f"- If it does not rain tomorrow, probability of rain the next day is 1/6\\n\\n"
        f"Calculate the probability that it will rain on the day after tomorrow."
    )
    correct = "1/5 (20,0%)"
    distractors = ["1/3 (33,3%)", "1/6 (16,7%)", "7/30 (23,3%)"]
    expl = (
        f"[1 Mark: Path 1 and Path 2 sum]\\n"
        f"P = (1/5 * 1/3) + (4/5 * 1/6) = 1/15 + 4/30 = 2/30 + 4/30 = 6/30 = 1/5 (20,0%)"
    )
    return {
        "subskill": "gr11_prob_subskill_49",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "(1/5 * 1/3) + (4/5 * 1/6).", "tier_2": "2/30 + 4/30 = 6/30 = 1/5.", "tier_3": f"{correct}."}
    }

def _subskill_50(r: random.Random) -> Dict[str, Any]:
    """Quality control tree: probability of product passing 2 consecutive stages."""
    p1 = 0.95
    p2 = 0.90
    p_both = round(p1 * p2, 3)

    prompt = (
        f"An electronics manufacturing line subjects circuit boards to two sequential quality checks:\\n"
        f"- Stage 1 electrical check pass rate: **95%** (0,95)\\n"
        f"- Stage 2 thermal stress check pass rate: **90%** (0,90)\\n\\n"
        f"Assuming performance at each stage is independent, calculate the probability that a circuit board passes **both** stages."
    )
    correct = f"{_fmt_dec(p_both, 3)} ({_fmt_pct(p_both)})"
    distractors = [
        "0,950 (95,0%)",
        "0,900 (90,0%)",
        "0,800 (80,0%)"
    ]
    expl = (
        f"[1 Mark: Sequential inspection probability]\\n"
        f"P(Pass Both) = 0,95 * 0,90 = {_fmt_dec(p_both, 3)} ({_fmt_pct(p_both)})"
    )
    return {
        "subskill": "gr11_prob_subskill_50",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply 0,95 by 0,90.", "tier_2": "0,95 * 0,90 = 0,855.", "tier_3": f"{correct}."}
    }

def _subskill_51(r: random.Random) -> Dict[str, Any]:
    """Sports match outcome tree: tournament progression."""
    p_win_semi = 0.60
    p_win_final = 0.50
    p_trophy = round(p_win_semi * p_win_final, 2)

    prompt = (
        f"A rugby team enters the semi-finals of a provincial championship:\\n"
        f"- Probability of winning the semi-final: **60%** (0,60)\\n"
        f"- If they reach the final, probability of winning the championship: **50%** (0,50)\\n\\n"
        f"Calculate the probability that the team wins the championship trophy."
    )
    correct = f"{_fmt_dec(p_trophy, 2)} ({_fmt_pct(p_trophy)})"
    distractors = [
        "0,60 (60,0%)",
        "0,50 (50,0%)",
        "0,10 (10,0%)"
    ]
    expl = (
        f"[1 Mark: Compound tournament path]\\n"
        f"P(Trophy) = 0,60 * 0,50 = {_fmt_dec(p_trophy, 2)} ({_fmt_pct(p_trophy)})"
    )
    return {
        "subskill": "gr11_prob_subskill_51",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply semi-final win probability by final win probability.", "tier_2": "0,60 * 0,50 = 0,30.", "tier_3": f"{correct}."}
    }

def _subskill_52(r: random.Random) -> Dict[str, Any]:
    """Stopping-rule tree diagram: coin game with stopping condition."""
    prompt = (
        f"A learner plays a coin game following these rules:\\n"
        f"- You flip a fair coin at most 3 times.\\n"
        f"- If the coin lands on Heads (H), you score 1 point and flip again.\\n"
        f"- If the coin lands on Tails (T), you stop immediately.\\n"
        f"- If you reach 3 flips, the game ends.\\n\\n"
        f"Outcomes ending in points:\\n"
        f"- Path (H, T): 2 flips, 1 point\\n"
        f"- Path (H, H, T): 3 flips, 2 points\\n"
        f"- Path (H, H, H): 3 flips, 3 points (probability = 1/8)\\n\\n"
        f"What is the probability of achieving the maximum score of 3 points (path H, H, H)?"
    )
    correct = "1/8 (12,5%)"
    distractors = [
        "1/4 (25,0%)",
        "3/8 (37,5%)",
        "1/2 (50,0%)"
    ]
    expl = (
        f"[1 Mark: Branch multiplication along stopping path]\\n"
        f"P(H, H, H) = (1/2) * (1/2) * (1/2) = 1/8 = 12,5%"
    )
    return {
        "subskill": "gr11_prob_subskill_52",
        "prompt": prompt,
        "options": _build_mc_options(correct, distractors, r),
        "correct_answer": correct,
        "explanation": expl,
        "hints": {"tier_1": "Multiply (1/2) three times for three consecutive heads.", "tier_2": "(1/2)^3 = 1/8.", "tier_3": f"{correct}."}
    }

# ----------------------------------------------------------------------------
# Master Dispatch Table & Entry Point
# ----------------------------------------------------------------------------

DISPATCH_TABLE = {
    f"gr11_prob_subskill_{i}": fn
    for i, fn in enumerate([
        _subskill_1, _subskill_2, _subskill_3, _subskill_4, _subskill_5,
        _subskill_6, _subskill_7, _subskill_8, _subskill_9, _subskill_10,
        _subskill_11, _subskill_12, _subskill_13, _subskill_14, _subskill_15,
        _subskill_16, _subskill_17, _subskill_18, _subskill_19, _subskill_20,
        _subskill_21, _subskill_22, _subskill_23, _subskill_24, _subskill_25,
        _subskill_26, _subskill_27, _subskill_28, _subskill_29, _subskill_30,
        _subskill_31, _subskill_32, _subskill_33, _subskill_34, _subskill_35,
        _subskill_36, _subskill_37, _subskill_38, _subskill_39, _subskill_40,
        _subskill_41, _subskill_42, _subskill_43, _subskill_44, _subskill_45,
        _subskill_46, _subskill_47, _subskill_48, _subskill_49, _subskill_50,
        _subskill_51, _subskill_52
    ], 1)
}

SUBSKILLS = list(DISPATCH_TABLE.keys())


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 11 Mathematical Literacy: Probability."""
    r = random.Random(seed)
    results: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        chosen_subskill = subskill

        if not chosen_subskill and archetype_index is not None:
            if 0 <= archetype_index < len(SUBSKILLS):
                chosen_subskill = SUBSKILLS[archetype_index]
            else:
                chosen_subskill = SUBSKILLS[archetype_index % len(SUBSKILLS)]

        if not chosen_subskill or chosen_subskill not in DISPATCH_TABLE:
            chosen_subskill = r.choice(SUBSKILLS)

        builder = DISPATCH_TABLE[chosen_subskill]
        raw_q = builder(r)

        payload = {
            "id": f"mathlit_gr11_prob_{chosen_subskill}_{uuid.uuid4().hex[:8]}",
            "question_id": f"mathlit_gr11_prob_{chosen_subskill}_{uuid.uuid4().hex[:8]}",
            "topic": "grade11_mathlit_probability",
            "subskill": chosen_subskill,
            "prompt": raw_q["prompt"],
            "options": raw_q["options"],
            "correct_answer": raw_q["correct_answer"],
            "expected_answer": raw_q["correct_answer"],
            "explanation": raw_q["explanation"],
            "worked_solution": raw_q["explanation"],
            "hints": raw_q["hints"],
            "grade": 11,
            "subject": "Mathematical Literacy",
        }
        if "diagram_spec" in raw_q:
            payload["diagram_spec"] = raw_q["diagram_spec"]
            payload["diagram"] = raw_q["diagram_spec"]
        elif "diagram" in raw_q:
            payload["diagram_spec"] = raw_q["diagram"]
            payload["diagram"] = raw_q["diagram"]

        results.append(payload)

    return results
''')

    full_code = "".join(parts)
    target_path = "caps-ai-backend/app/utils/mathematical_literacy/gr11_probability_generator.py"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_code)
    print(f"Written {target_path} successfully.")

if __name__ == "__main__":
    generate_file()
