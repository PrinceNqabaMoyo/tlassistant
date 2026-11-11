"""Cluster 5: Combined Events, Tree Diagrams & Two-Way Tables (Subskills 37 to 44)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)

# --------------------------------------------------------------------------- #
# Subskill 37: Sample Space Enumeration Two Coins
# --------------------------------------------------------------------------- #
def _gen_prob_comb_sample_space_enumeration_two_coins(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_sample_space_enumeration_two_coins"
    name = r.choice(SA_NAMES)
    correct_ans = "{HH; HT; TH; TT} (4 outcomes)"

    prompt = (
        f"{name} tosses two fair South African coins simultaneously.\n\n"
        f"List the complete **sample space** ($S$) of all possible combined outcomes (where H = Heads, T = Tails)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Each coin has 2 independent possible outcomes: Heads (H) or Tails (T).\n"
        f"By the fundamental counting principle, total possible outcomes = $2 \\times 2 = 4$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"Listing all combinations systematically:\n"
        f"  • Coin 1 Heads, Coin 2 Heads: HH\n"
        f"  • Coin 1 Heads, Coin 2 Tails: HT\n"
        f"  • Coin 1 Tails, Coin 2 Heads: TH\n"
        f"  • Coin 1 Tails, Coin 2 Tails: TT\n"
        f"$$S = \\{{ \\text{{HH}}; \\text{{HT}}; \\text{{TH}}; \\text{{TT}} \\}}$$ ✓ [1 Mark: Method – enumerating all 2×2 combinations without omission]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct sample space set]"
    )

    custom = [
        "{HH; HT; TH; TT} (4 outcomes)",
        "{HH; TT} (2 outcomes)",
        "{HH; HT; TT} (3 outcomes)",
        "{H; T} (2 outcomes)",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 2 outcomes for coin 1 and 2 for coin 2: 2 × 2 = 4 outcomes.",
        tier_2="List them: HH, HT, TH, TT.",
        tier_3=f"Sample space = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 38: Two Coins Both Heads
# --------------------------------------------------------------------------- #
def _gen_prob_comb_two_coins_both_heads(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_two_coins_both_heads"
    name = r.choice(SA_NAMES)
    correct_ans = "1/4 (25%)"

    prompt = (
        f"{name} tosses two fair coins.\n\n"
        f"Calculate the theoretical probability that **both coins land on Heads (HH)**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The sample space contains 4 equally likely outcomes: $S = \\{{ \\text{{HH}}; \\text{{HT}}; \\text{{TH}}; \\text{{TT}} \\}}$ ($n(S) = 4$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"There is exactly 1 favourable outcome (HH): $n(\\text{{HH}}) = 1$.\n"
        f"$$P(\\text{{both Heads}}) = \\frac{{1}}{{4}}$$ ✓ [1 Mark: Method – dividing favourable outcome HH by 4]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{both Heads}}) = \\frac{{1}}{{4}} = 0,25 = 25\\%$$ ✓ [1 Mark: Accuracy – accurate fraction and percentage]"
    )

    custom = ["1/4 (25%)", "1/2 (50%)", "3/4 (75%)", "1/3 (33,3%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 4 possible outcomes: HH, HT, TH, TT.",
        tier_2="Only 1 outcome is HH.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 39: Two Coins At Least One Head
# --------------------------------------------------------------------------- #
def _gen_prob_comb_two_coins_at_least_one_head(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_two_coins_at_least_one_head"
    name = r.choice(SA_NAMES)
    correct_ans = "3/4 (75%)"

    prompt = (
        f"{name} flips two standard coins.\n\n"
        f"Calculate the theoretical probability of obtaining **at least one Head**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The phrase 'at least one Head' means getting either 1 Head or 2 Heads.\n"
        f"In the sample space $S = \\{{ \\text{{HH}}; \\text{{HT}}; \\text{{TH}}; \\text{{TT}} \\}}$, the matching outcomes are $\\{{ \\text{{HH}}; \\text{{HT}}; \\text{{TH}} \\}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"There are 3 favourable outcomes out of 4 total outcomes.\n"
        f"$$P(\\text{{at least 1 Head}}) = \\frac{{3}}{{4}}$$ (or $1 - P(\\text{{TT}}) = 1 - \\frac{{1}}{{4}} = \\frac{{3}}{{4}}$) "
        f"✓ [1 Mark: Method – identifying 3 favourable outcomes or using complement]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{at least 1 Head}}) = \\frac{{3}}{{4}} = 75\\%$$ ✓ [1 Mark: Accuracy – accurate fraction and percentage]"
    )

    custom = ["3/4 (75%)", "1/2 (50%)", "1/4 (25%)", "2/3 (66,7%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="'At least one Head' includes HH, HT, and TH.",
        tier_2="3 outcomes out of 4.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 40: Coin and 6-Sided Die Combined Grid
# --------------------------------------------------------------------------- #
def _gen_prob_comb_coin_and_die_outcomes_grid(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_coin_and_die_outcomes_grid"
    name = r.choice(SA_NAMES)
    target_num = r.choice([2, 4, 6])
    correct_ans = "1/12 (8,3%)"

    prompt = (
        f"{name} flips a coin and simultaneously rolls a 6-sided die.\n\n"
        f"Calculate the theoretical probability of getting **Heads on the coin AND the number {target_num} on the die**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The coin has 2 outcomes and the die has 6 outcomes. "
        f"Total possible outcomes in the combined sample space = $2 \\times 6 = 12$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"There is only 1 favourable outcome: (Heads; {target_num}).\n"
        f"$$P(\\text{{Heads and }}{target_num}) = P(\\text{{Heads}}) \\times P({target_num}) = \\frac{{1}}{{2}} \\times \\frac{{1}}{{6}} = \\frac{{1}}{{12}}$$ "
        f"✓ [1 Mark: Method – multiplying independent probabilities or dividing 1 by 12]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P = \\frac{{1}}{{12}} \\approx 8,3\\%$$ ✓ [1 Mark: Accuracy – accurate combined probability]"
    )

    custom = ["1/12 (8,3%)", "1/8 (12,5%)", "2/12 (16,7%)", "1/6 (16,7%)"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total outcomes = 2 × 6 = 12.",
        tier_2=f"Only 1 combination is (Heads; {target_num}).",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 41: Two Dice Sum Grid
# --------------------------------------------------------------------------- #
def _gen_prob_comb_two_dice_sum_grid(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_two_dice_sum_grid"
    name = r.choice(SA_NAMES)
    sum_choice = r.choice([
        (7, 6, "6/36 = 1/6 (16,7%)", "(1;6), (2;5), (3;4), (4;3), (5;2), (6;1)"),
        (2, 1, "1/36 (2,8%)", "(1;1)"),
        (12, 1, "1/36 (2,8%)", "(6;6)"),
        (10, 3, "3/36 = 1/12 (8,3%)", "(4;6), (5;5), (6;4)"),
        (6, 5, "5/36 (13,9%)", "(1;5), (2;4), (3;3), (4;2), (5;1)"),
    ])
    target_sum, ways, correct_str, combinations = sum_choice
    correct_ans = correct_str

    prompt = (
        f"{name} rolls two standard six-sided dice and adds the two numbers together.\n"
        f"There are $6 \\times 6 = 36$ equally likely outcome pairs in the two-way table.\n\n"
        f"Calculate the theoretical probability that the **sum of the two dice equals {target_sum}**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In a $6 \\times 6$ sum grid, total possible outcomes = 36.\n"
        f"The combinations yielding a sum of {target_sum} are: {combinations} ($n = {ways}$ pairs).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Sum }} = {target_sum}) = \\frac{{{ways}}}{{36}}$$ ✓ [1 Mark: Method – dividing favorable pairs by 36]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Sum }} = {target_sum}) = {correct_str}$$ ✓ [1 Mark: Accuracy – accurate probability fraction]"
    )

    custom = [correct_str, "1/6 (16,7%)", "1/12 (8,3%)", "1/36 (2,8%)", "5/36 (13,9%)"]
    options, _ = _build_options(correct_ans, r, [correct_ans, "1/6 (16,7%)", "1/18 (5,6%)", "2/36 (5,6%)"])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="There are 36 total outcomes when rolling two dice.",
        tier_2=f"Pairs adding to {target_sum}: {combinations} ({ways} pairs).",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 42: Two-Way Contingency Table Subgroup Probability
# --------------------------------------------------------------------------- #
def _gen_prob_comb_two_way_table_gender_sport(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_two_way_table_gender_sport"
    name = r.choice(SA_NAMES)
    # 2x2 contingency table: Boys/Girls vs Soccer/Netball
    boys_soc, boys_net = 25, 5
    girls_soc, girls_net = 15, 35
    total = boys_soc + boys_net + girls_soc + girls_net  # 80
    correct_ans = f"25/80 = 5/16 (31,3%)"

    prompt = (
        f"{name} tabulates sports choices for 80 Grade 10 learners in a two-way table:\n\n"
        f"| Category | Soccer | Netball | Total |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| Boys | 25 | 5 | 30 |\n"
        f"| Girls | 15 | 35 | 50 |\n"
        f"| **Total** | **40** | **40** | **80** |\n\n"
        f"Calculate the probability that a learner chosen at random from the entire grade is a **Boy who plays Soccer**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Locate the cell corresponding to the intersection of the 'Boys' row and 'Soccer' column, "
        f"then divide by the grand total of learners ($N = 80$).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Favourable learners (Boys and Soccer)}} = 25$$\n"
        f"$$P(\\text{{Boy and Soccer}}) = \\frac{{25}}{{80}} = \\frac{{5}}{{16}} = 0,3125$$ ✓ [1 Mark: Method – dividing intersecting cell by grand total]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Boy and Soccer}}) = \\frac{{5}}{{16}} \\approx 31,3\\%$$ ✓ [1 Mark: Accuracy – accurate fraction and percentage]"
    )

    d1 = "25/30 = 5/6 (83,3%)"  # divided by row total only
    d2 = "25/40 = 5/8 (62,5%)"  # divided by column total only
    d3 = "40/80 = 1/2 (50%)"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Read the intersection cell: Boys who play Soccer = 25.",
        tier_2="Divide by the grand total 80 learners: 25/80.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 43: Tree Diagram Two-Stage Paths
# --------------------------------------------------------------------------- #
def _gen_prob_comb_tree_diagram_two_stage_paths(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_tree_diagram_two_stage_paths"
    name = r.choice(SA_NAMES)
    # Tree diagram: 2 red, 3 blue marbles in a bag. Draw 2 with replacement.
    p_red = 0.4  # 2/5
    p_both_red = round(p_red * p_red, 2)  # 4/25 = 0.16 = 16%
    correct_ans = "4/25 (16%)"

    prompt = (
        f"{name} draws two marbles from a bag containing 2 Red and 3 Blue marbles, **with replacement** "
        f"(the first marble is put back before drawing the second).\n"
        f"A tree diagram branches into Red ($\\frac{{2}}{{5}}$) and Blue ($\\frac{{3}}{{5}}$) at each stage.\n\n"
        f"Calculate the theoretical probability that **both marbles drawn are Red**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Because the marble is replaced, the draws are independent events. "
        f"Multiply along the branch path: $P(\\text{{Red, Red}}) = P(\\text{{Red}}) \\times P(\\text{{Red}})$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{First Red}}) = \\frac{{2}}{{5}}$$\n"
        f"$$P(\\text{{Second Red}}) = \\frac{{2}}{{5}}$$\n"
        f"$$P(\\text{{Both Red}}) = \\frac{{2}}{{5}} \\times \\frac{{2}}{{5}} = \\frac{{4}}{{25}}$$ ✓ [1 Mark: Method – multiplying branch probabilities along tree path]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Both Red}}) = \\frac{{4}}{{25}} = 0,16 = 16\\%$$ ✓ [1 Mark: Accuracy – accurate product fraction and percentage]"
    )

    d1 = "2/5 (40%)"  # single draw
    d2 = "4/10 = 2/5 (40%)"  # added denominators
    d3 = "6/25 (24%)"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "tree_diagram",
        "title": f"Two-Stage Marble Tree Diagram ({name})",
        "branches": ["Red (2/5)", "Blue (3/5)"],
        "outcomes": ["RR", "RB", "BR", "BB"],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply along the branches of the tree diagram.",
        tier_2="Calculate (2/5) × (2/5) = 4/25.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 44: Fair Game Rules Audit
# --------------------------------------------------------------------------- #
def _gen_prob_comb_fair_game_rules_audit(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_comb_fair_game_rules_audit"
    name = r.choice(SA_NAMES)
    correct_ans = "Unfair: Player A has 18/36 (50%) chance while Player B has only 6/36 (16,7%) chance"

    prompt = (
        f"{name} invents a game for two players rolling two 6-sided dice:\n"
        f"  • Player A wins if the sum of the two dice is an EVEN number (18 out of 36 outcomes)\n"
        f"  • Player B wins if the sum of the two dice is exactly 7 (6 out of 36 outcomes)\n\n"
        f"Is this a **fair game**? Explain your reasoning."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A game is mathematically fair if all participating players have an equal probability of winning: "
        f"$P(\\text{{Player A wins}}) = P(\\text{{Player B wins}})$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Player A wins}}) = \\frac{{18}}{{36}} = 50\\%$$\n"
        f"$$P(\\text{{Player B wins}}) = \\frac{{6}}{{36}} \\approx 16,7\\%$$\n"
        f"Because $50\\% \\ne 16,7\\%$, Player A has three times higher probability of winning. "
        f"✓ [1 Mark: Method – comparing winning probabilities of both players against 50/50 equality]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct unfairness conclusion with evidence]"
    )

    custom = [
        correct_ans,
        "Fair: Both players have an equal chance because 7 is a lucky number",
        "Fair: Any game involving standard dice is automatically fair",
        "Unfair: Player B has a higher chance of winning than Player A",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="A fair game requires both players to have an equal chance of winning.",
        tier_2="Player A wins on 18 outcomes; Player B wins on only 6 outcomes.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )
