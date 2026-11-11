"""Subskills 09 to 16: Independent vs dependent events, sampling with/without replacement, product rule, and the Gambler's fallacy."""
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


def generate_09_independent_events_classification(r: random.Random) -> Dict[str, Any]:
    """Classify real-world events as independent."""
    correct_ans = "Independent: The outcome of tossing a coin does not alter the physical composition or probabilities of rolling a die"

    custom_options = [
        correct_ans,
        "Dependent: Getting a head on the coin reduces the available numbers on the die from 6 to 5",
        "Mutually exclusive: A coin and a die cannot exist in the same classroom",
        "Complementary: Tossing a head guarantees rolling an even number on the die",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A learner tosses a fair coin and rolls a standard 6-sided die.\n\n"
        f"State whether the event of getting a Head on the coin and rolling a 6 on the die are independent or dependent, and justify your answer."
    )
    explanation = (
        f"Step 1: Check if the occurrence of the first event affects the sample space or probability of the second event [M].\n"
        f"Step 2: The outcome of the coin toss has zero effect on the die roll [M].\n"
        f"Step 3: Therefore, the events are independent [A]."
    )
    return _build_question_payload(
        subskill_id="09_independent_events_classification",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Ask: Does the result of the first action change the choices or chances for the second action?",
        tier_2="Flipping a coin does not affect the physical numbers on a die.",
        tier_3="They are independent events.",
        r=r,
    )


def generate_10_dependent_events_without_replacement(r: random.Random) -> Dict[str, Any]:
    """Classify events as dependent when sampling without replacement."""
    correct_ans = "Dependent: Removing the first student without replacement reduces the pool size and alters the probability for the second selection"

    custom_options = [
        correct_ans,
        "Independent: The election process is democratic so probabilities remain identical",
        "Mutually exclusive: Only one student can attend school on any given day",
        "Complementary: Electing a head boy guarantees the election of a head girl",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A representative council of learners (RCL) has 10 members. The council first elects a President, "
        f"and then from the remaining 9 members, elects a Secretary.\n\n"
        f"Explain why the selection of the President and the selection of the Secretary are classified as dependent events."
    )
    explanation = (
        f"Step 1: The person selected as President cannot also be chosen as Secretary (selection without replacement) [M].\n"
        f"Step 2: This reduces the available pool of candidates from 10 to 9, changing the second probability [M].\n"
        f"Step 3: Because the first event alters the conditions of the second, the events are dependent [A]."
    )
    return _build_question_payload(
        subskill_id="10_dependent_events_without_replacement",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice that the person chosen first is no longer available for the second choice.",
        tier_2="The sample space decreases from 10 to 9.",
        tier_3="Since the first selection changes the choices for the second, the events are dependent.",
        r=r,
    )


def generate_11_two_stage_draw_with_replacement(r: random.Random) -> Dict[str, Any]:
    """Calculate P(A and B) when sampling with replacement: P(A) x P(B)."""
    yellow = r.choice([2, 3, 4])
    black = r.choice([3, 4, 5])
    total = yellow + black
    p_num = yellow * black
    p_den = total * total
    frac_str = _fmt_frac(p_num, p_den)

    d_spec_11 = {
        "diagram_role": "context",
        "kind": "tree_diagram",
        "branches": [{"label": "Yellow", "sub": ["Yellow", "Black"]}, {"label": "Black", "sub": ["Yellow", "Black"]}],
        "outcomes": ["Yellow-Yellow", "Yellow-Black", "Black-Yellow", "Black-Black"],
        "title": f"Two-Stage Draw with Replacement ({yellow} Yellow, {black} Black)",
        "stages": [
            {"name": "First Draw", "outcomes": [{"name": "Yellow", "prob": f"{yellow}/{total}"}, {"name": "Black", "prob": f"{black}/{total}"}]},
            {"name": "Second Draw", "outcomes": [{"name": "Yellow", "prob": f"{yellow}/{total}"}, {"name": "Black", "prob": f"{black}/{total}"}]},
        ],
    }

    correct_ans = f"P(Yellow and Black) = {yellow}/{total} × {black}/{total} = {frac_str}"
    custom_options = [
        correct_ans,
        f"P(Yellow and Black) = 3/7 + 4/7 = 7/7 = 1,00",
        f"P(Yellow and Black) = 3/7 × 4/6 = 12/42 = 2/7",
        f"P(Yellow and Black) = 1/49",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"Refer to the tree diagram for drawing beads from a bag with replacement.\n"
        f"A bag contains {yellow} yellow beads and {black} black beads (total {total} beads).\n"
        f"A bead is drawn at random, its colour is recorded, and it is replaced back into the bag.\n"
        f"A second bead is then drawn and recorded.\n\n"
        f"Calculate the probability of drawing a yellow bead first AND a black bead second."
    )
    explanation = (
        f"Step 1: P(First bead Yellow) = 3/7 [M].\n"
        f"Step 2: Because the bead is replaced, P(Second bead Black) remains 4/7 [M].\n"
        f"Step 3: Since events are independent, P(Yellow and Black) = 3/7 × 4/7 = {frac_str} [A]."
    )
    return _build_question_payload(
        subskill_id="11_two_stage_draw_with_replacement",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="With replacement, the bag always has 7 beads for both draws.",
        tier_2="Multiply the probability of yellow (3/7) by the probability of black (4/7).",
        tier_3=f"3/7 × 4/7 = {frac_str}.",
        r=r,
        diagram_spec=d_spec_11,
    )


def generate_12_two_stage_draw_without_replacement(r: random.Random) -> Dict[str, Any]:
    """Calculate P(Red first and Green second) when sampling without replacement."""
    red = 3
    green = 5
    total = red + green  # 8

    # First red: 3/8. Second green: 5/7.
    num = red * green  # 15
    den = total * (total - 1)  # 56
    frac_str = _fmt_frac(num, den)

    correct_ans = f"P(Red and Green) = 3/8 × 5/7 = {frac_str}"
    custom_options = [
        correct_ans,
        f"P(Red and Green) = 3/8 × 5/8 = 15/64",
        f"P(Red and Green) = 3/8 + 5/7 = 61/56",
        f"P(Red and Green) = 1/56",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A box contains 3 red apples and 5 green apples (total 8 apples).\n"
        f"A learner takes one apple and eats it (without replacement). They then take a second apple.\n\n"
        f"Calculate the probability that the first apple is red AND the second apple is green."
    )
    explanation = (
        f"Step 1: P(First apple Red) = 3/8 [M].\n"
        f"Step 2: After eating a red apple, 7 apples remain in total, of which 5 are green: P(Second Green) = 5/7 [M].\n"
        f"Step 3: P(Red and Green) = 3/8 × 5/7 = {frac_str} [A]."
    )
    return _build_question_payload(
        subskill_id="12_two_stage_draw_without_replacement",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember that without replacement, the total number of apples drops from 8 to 7 for the second draw.",
        tier_2="First draw is 3/8. Second draw is 5/7.",
        tier_3=f"Multiply: 3/8 × 5/7 = {frac_str}.",
        r=r,
    )


def generate_13_identical_items_without_replacement(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of drawing two identical items without replacement (e.g. two reds)."""
    red = 4
    blue = 6
    total = red + blue  # 10

    # Draw two reds: (4/10) * (3/9) = 12/90 = 2/15
    num = red * (red - 1)
    den = total * (total - 1)
    frac_str = _fmt_frac(num, den)

    correct_ans = f"P(Both Red) = 4/10 × 3/9 = {frac_str}"
    custom_options = [
        correct_ans,
        f"P(Both Red) = 4/10 × 4/10 = 16/100 = 4/25",
        f"P(Both Red) = 4/10 + 3/9 = 66/90 = 11/15",
        f"P(Both Red) = 1/90",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A bag contains 4 red marbles and 6 blue marbles.\n"
        f"Two marbles are drawn successively without replacement.\n\n"
        f"Calculate the probability that BOTH marbles drawn are red."
    )
    explanation = (
        f"Step 1: P(First marble Red) = 4/10 [M].\n"
        f"Step 2: P(Second marble Red) = (4 - 1)/(10 - 1) = 3/9 [M].\n"
        f"Step 3: P(Both Red) = 4/10 × 3/9 = 12/90 = {frac_str} [A]."
    )
    return _build_question_payload(
        subskill_id="13_identical_items_without_replacement",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Both the numerator (number of reds) and the denominator (total marbles) decrease by 1 on the second draw.",
        tier_2="Calculate (4/10) × (3/9).",
        tier_3=f"The simplified probability is {frac_str}.",
        r=r,
    )


def generate_14_at_least_one_desired_outcome(r: random.Random) -> Dict[str, Any]:
    """Calculate probability of 'at least one' using complement: 1 - P(none)."""
    # Toss coin 3 times: P(at least one head) = 1 - P(no heads / all tails) = 1 - (1/2)^3 = 7/8
    p_none = "1/8"
    p_at_least_one = "7/8"
    pct = "87,5%"

    correct_ans = f"P(At least one Head) = 1 - P(All Tails) = 1 - 1/8 = {p_at_least_one} ({pct})"
    custom_options = [
        correct_ans,
        f"P(At least one Head) = 1/2 × 3 = 3/2 = 150%",
        f"P(At least one Head) = 1/8 (12,5%)",
        f"P(At least one Head) = 1/3 (33,3%)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A fair coin is tossed 3 times in succession.\n\n"
        f"Using the complementary probability rule:\n"
        f"P(At least one Head) = 1 - P(No Heads)\n"
        f"calculate the probability of tossing at least one Head."
    )
    explanation = (
        f"Step 1: P(Tail on one toss) = 1/2 [M].\n"
        f"Step 2: P(Three Tails) = 1/2 × 1/2 × 1/2 = 1/8 [M].\n"
        f"Step 3: P(At least one Head) = 1 - 1/8 = {p_at_least_one} ({pct}) [A]."
    )
    return _build_question_payload(
        subskill_id="14_at_least_one_desired_outcome",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The only outcome with no heads is getting three tails in a row (TTT).",
        tier_2="P(TTT) = (1/2)³ = 1/8. Subtract this from 1.",
        tier_3=f"1 - 1/8 = {p_at_least_one} ({pct}).",
        r=r,
    )


def generate_15_testing_independence_rule(r: random.Random) -> Dict[str, Any]:
    """Mathematically verify whether two events are independent using P(A and B) == P(A) x P(B)."""
    p_a = 0.50
    p_b = 0.30
    prod = p_a * p_b  # 0.15
    p_both = 0.15

    correct_ans = f"Independent: Because P(A and B) = 0,15 equals P(A) × P(B) = 0,50 × 0,30 = 0,15"
    custom_options = [
        correct_ans,
        f"Dependent: Because P(A) and P(B) are not equal",
        f"Mutually exclusive: Because P(A and B) is greater than zero",
        f"Indeterminate: Independence can only be proven with a physical die",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"For two events A and B in a statistical experiment:\n"
        f"• P(A) = 0,50\n"
        f"• P(B) = 0,30\n"
        f"• P(A and B) = 0,15\n\n"
        f"Determine mathematically whether events A and B are independent or dependent."
    )
    explanation = (
        f"Step 1: Recall the independence criterion: Events are independent if and only if P(A and B) = P(A) × P(B) [M].\n"
        f"Step 2: Calculate product: P(A) × P(B) = 0,50 × 0,30 = 0,15 [M].\n"
        f"Step 3: Since P(A and B) = 0,15 matches the product exactly, the events are independent [A]."
    )
    return _build_question_payload(
        subskill_id="15_testing_independence_rule",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply P(A) by P(B) and compare the product to P(A and B).",
        tier_2="0,50 × 0,30 = 0,15. This is identical to P(A and B).",
        tier_3="Since P(A and B) = P(A) × P(B), the events are independent.",
        r=r,
    )


def generate_16_gamblers_fallacy_misconception(r: random.Random) -> Dict[str, Any]:
    """Identify the Gambler's Fallacy misconception in independent trials."""
    correct_ans = "Gambler's fallacy: The coin has no memory; each toss is independent, so the probability of Heads remains strictly 0,50 (50%)"

    custom_options = [
        correct_ans,
        "True expectation: Because tails appeared 6 times, the physics of the coin makes Heads 90% likely",
        "Deterministic balance: The coin must alternate immediately to satisfy probability laws",
        "Biased coin rule: After 6 tails, the probability of Tails becomes 1,00",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A gambler tosses an unbiased coin and observes Tails 6 times in a row. "
        f"He asserts: 'A Head is definitely due on the 7th toss because of the law of averages.'\n\n"
        f"Evaluate this claim from a probability perspective and state the exact probability of tossing Heads on the 7th toss."
    )
    explanation = (
        f"Step 1: Each coin toss is physically independent of previous outcomes [M].\n"
        f"Step 2: Believing previous results influence future independent events is the 'Gambler's Fallacy' [M].\n"
        f"Step 3: The probability of Heads on the 7th toss remains strictly 1/2 (50%) [A]."
    )
    return _build_question_payload(
        subskill_id="16_gamblers_fallacy_misconception",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember: Coins do not have memories.",
        tier_2="Previous tosses have zero effect on future independent tosses.",
        tier_3="Believing a head is 'due' is the Gambler's Fallacy; P(Head) is still 50%.",
        r=r,
    )
