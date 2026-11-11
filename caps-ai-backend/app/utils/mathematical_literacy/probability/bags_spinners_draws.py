"""Cluster 3: Coloured Objects, Bags & Spinners (Subskills 19 to 27)."""
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
# Subskill 19: Bag Single Colour Probability
# --------------------------------------------------------------------------- #
def _gen_prob_bag_single_colour_from_total(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_bag_single_colour_from_total"
    name = r.choice(SA_NAMES)
    red = r.choice([3, 4, 5])
    blue = r.choice([5, 6, 8])
    green = r.choice([2, 4, 7])
    total = red + blue + green
    correct_ans = f"{blue}/{total}"

    prompt = (
        f"{name} has an opaque bag containing coloured marbles:\n"
        f"  • {red} Red marbles\n"
        f"  • {blue} Blue marbles\n"
        f"  • {green} Green marbles\n\n"
        f"If one marble is drawn at random from the bag, calculate the theoretical probability of selecting a **Blue marble**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Find total outcomes $N$ by adding all marbles together, then divide the number of blue marbles by the total.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total marbles}} = {red} + {blue} + {green} = {total}$$\n"
        f"$$P(\\text{{Blue}}) = \\frac{{{blue}}}{{{total}}}$$ ✓ [1 Mark: Method – summing marbles and writing favourable-to-total ratio]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Blue}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate probability fraction]"
    )

    d1 = f"{red}/{total}"
    d2 = f"{green}/{total}"
    d3 = f"{blue}/{total - 1}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the total number of marbles first.",
        tier_2=f"Total = {red} + {blue} + {green} = {total}.",
        tier_3=f"P(Blue) = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 20: Bag OR Compound Disjunction
# --------------------------------------------------------------------------- #
def _gen_prob_bag_or_compound_disjunction(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_bag_or_compound_disjunction"
    name = r.choice(SA_NAMES)
    red = r.choice([4, 6])
    yellow = r.choice([5, 7])
    black = r.choice([5, 7])
    total = red + yellow + black
    fav = red + yellow
    correct_ans = f"{fav}/{total}"

    prompt = (
        f"{name} has a bag with {red} red tokens, {yellow} yellow tokens, and {black} black tokens (total = {total} tokens).\n\n"
        f"Calculate the probability of selecting either a **Red OR Yellow token** on a single random draw."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The word 'OR' indicates the union of mutually exclusive events: add the favourable counts together: $P(A \\text{{ or }} B) = \\frac{{n(A) + n(B)}}{{N}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Favourable tokens}} = {red} + {yellow} = {fav}$$\n"
        f"$$P(\\text{{Red or Yellow}}) = \\frac{{{fav}}}{{{total}}}$$ ✓ [1 Mark: Method – summing favourable counts over total tokens]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Red or Yellow}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate probability fraction]"
    )

    d1 = f"{red}/{total}"
    d2 = f"{yellow}/{total}"
    d3 = f"{black}/{total}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "probability_spinner",
        "title": f"Token Bag Composition ({name})",
        "sectors": [
            {"label": "Section A", "value": 10},
            {"label": "Section B", "value": 15},
            {"label": "Section C", "value": 25},
        ],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the red and yellow tokens together.",
        tier_2=f"Favourable = {red} + {yellow} = {fav} out of {total}.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 21: Bag NOT Colour Complement
# --------------------------------------------------------------------------- #
def _gen_prob_bag_not_colour_complement(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_bag_not_colour_complement"
    name = r.choice(SA_NAMES)
    white = r.choice([3, 4, 5])
    other = r.choice([12, 15, 16])
    total = white + other
    correct_ans = f"{other}/{total}"

    prompt = (
        f"A box contains {white} white beads and {other} coloured beads (total = {total} beads).\n\n"
        f"Calculate the probability of randomly selecting a bead that is **NOT white**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The probability of NOT drawing white is the complement of drawing white: $P(\\text{{Not White}}) = 1 - P(\\text{{White}}) = \\frac{{N - \\text{{white}}}}{{N}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Non-white beads}} = {total} - {white} = {other}$$\n"
        f"$$P(\\text{{Not White}}) = \\frac{{{other}}}{{{total}}}$$ ✓ [1 Mark: Method – calculating non-white count over total]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Not White}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate fraction]"
    )

    d1 = f"{white}/{total}"  # probability of drawing white
    d2 = f"{other - 2}/{total}"
    d3 = f"{other}/{total - white}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "probability_spinner",
        "title": f"Bead Box Composition ({name})",
        "sectors": [
            {"label": "Section A", "value": 10},
            {"label": "Section B", "value": 15},
            {"label": "Section C", "value": 25},
        ],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract white beads from the total to find non-white beads.",
        tier_2=f"{total} - {white} = {other} non-white beads.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 22: Missing Colour Count from Probability
# --------------------------------------------------------------------------- #
def _gen_prob_bag_missing_colour_count(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_bag_missing_colour_count"
    name = r.choice(SA_NAMES)
    total_balls = r.choice([20, 24, 30, 40, 50])
    pct = r.choice([20, 25, 40, 50, 60])
    count = int((pct / 100) * total_balls)
    correct_ans = f"{count} green balls"

    prompt = (
        f"{name} knows that a container holds {total_balls} balls in total.\n"
        f"The probability of selecting a green ball is **{pct}%** (or $\\frac{{{pct}}}{{100}}$).\n\n"
        f"Calculate the actual number of green balls in the container."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To find the count from a probability percentage, multiply the total items by the probability fraction: $\\text{{Count}} = P(E) \\times N$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Green balls}} = \\frac{{{pct}}}{{100}} \\times {total_balls}$$ ✓ [1 Mark: Method – multiplying total balls by probability]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Green balls}} = {count}\\text{{ balls}}$$ ✓ [1 Mark: Accuracy – accurate integer count]"
    )

    d1 = f"{count + 2} green balls"
    d2 = f"{count - 2} green balls"
    d3 = f"{pct} green balls"  # confused percentage with count
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "probability_spinner",
        "title": f"Container Ball Composition ({name})",
        "sectors": [
            {"label": "Section A", "value": 10},
            {"label": "Section B", "value": 15},
            {"label": "Section C", "value": 25},
        ],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply total balls by the probability percentage.",
        tier_2=f"Calculate ({pct} ÷ 100) × {total_balls}.",
        tier_3=f"Green balls = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 23: Spinner with Equal Sectors
# --------------------------------------------------------------------------- #
def _gen_prob_spinner_equal_sectors(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_spinner_equal_sectors"
    name = r.choice(SA_NAMES)
    total_sectors = r.choice([4, 6, 8, 10])
    fav_sectors = r.choice([1, 2, 3])
    while fav_sectors >= total_sectors:
        fav_sectors = 1
    # reduce fraction if possible
    gcd = math.gcd(fav_sectors, total_sectors)
    rf_num = fav_sectors // gcd
    rf_den = total_sectors // gcd
    correct_ans = f"{rf_num}/{rf_den}"

    prompt = (
        f"{name} spins a circular prize wheel divided into **{total_sectors} equal sectors**.\n"
        f"Exactly {fav_sectors} of the sectors are shaded Gold.\n\n"
        f"Calculate the theoretical probability that the pointer lands on a **Gold sector** (in simplest fractional form)."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Because all {total_sectors} sectors are identical in size, each sector has an equal probability of being chosen.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Gold}}) = \\frac{{\\text{{Gold sectors}}}}{{\\text{{Total sectors}}}} = \\frac{{{fav_sectors}}}{{{total_sectors}}}$$ ✓ [1 Mark: Method – dividing gold sectors by total equal sectors]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Gold}}) = \\frac{{{rf_num}}}{{{rf_den}}}$$ ✓ [1 Mark: Accuracy – accurate simplified fraction]"
    )

    d1 = f"{fav_sectors}/{total_sectors + 1}"
    d2 = f"{total_sectors - fav_sectors}/{total_sectors}"
    d3 = f"1/{total_sectors}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    spinner_diag = {
        "kind": "probability_spinner",
        "sectors": total_sectors,
        "labels": [f"S{i+1}" for i in range(total_sectors)],
        "caption": f"Equal {total_sectors}-Sector Circular Probability Spinner",
    }

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the number of gold sectors by total sectors.",
        tier_2=f"{fav_sectors} ÷ {total_sectors} and simplify.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
        diagram_spec=spinner_diag,
    )

# --------------------------------------------------------------------------- #
# Subskill 24: Spinner with Unequal Sectors (Angles)
# --------------------------------------------------------------------------- #
def _gen_prob_spinner_unequal_sectors_angles(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_spinner_unequal_sectors_angles"
    name = r.choice(SA_NAMES)
    angle = r.choice([45, 60, 90, 120, 180])
    frac_map = {
        45: ("1/8", "12,5%"),
        60: ("1/6", "16,7%"),
        90: ("1/4", "25%"),
        120: ("1/3", "33,3%"),
        180: ("1/2", "50%"),
    }
    simp_frac, pct_str = frac_map[angle]
    correct_ans = f"{simp_frac} ({pct_str})"

    prompt = (
        f"{name} spins a spinner where the sectors have different sizes.\n"
        f"The Red sector has a central angle of **{angle}°** out of the full 360° circle.\n\n"
        f"Calculate the theoretical probability of the spinner stopping on the Red sector."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"A full circle has 360°. The probability of landing on any sector is proportional to its central angle: $P = \\frac{{\\theta}}{{360^\\circ}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Red}}) = \\frac{{{angle}^\\circ}}{{360^\\circ}} = \\frac{{{angle} \\div {angle}}}{{360 \\div {angle}}}$$ ✓ [1 Mark: Method – dividing central angle by 360°]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Red}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate simplified fraction and percentage]"
    )

    custom = [f"{simp_frac} ({pct_str})", "1/4 (25%)", "1/2 (50%)", "1/8 (12,5%)", "1/3 (33,3%)"]
    options, _ = _build_options(correct_ans, r, [correct_ans, "1/4 (25%)", "1/2 (50%)", "1/10 (10%)"])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the sector's angle by 360°.",
        tier_2=f"{angle}° ÷ 360° = {simp_frac}.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 25: Raffle Single Ticket Winning Chance
# --------------------------------------------------------------------------- #
def _gen_prob_raffle_single_ticket_winning_chance(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_raffle_single_ticket_winning_chance"
    name = r.choice(SA_NAMES)
    total_tickets = r.choice([250, 500, 800, 1000, 2000])
    correct_ans = f"1/{total_tickets}"

    prompt = (
        f"{name} buys **one ticket** in a school fundraising raffle where **{total_tickets} tickets** were sold in total.\n"
        f"There is only one grand prize drawn.\n\n"
        f"Calculate the theoretical probability that {name} wins the grand prize."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The probability is the number of tickets owned divided by the total number of tickets sold: $P = \\frac{{1}}{{N}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Win}}) = \\frac{{1}}{{{total_tickets}}}$$ ✓ [1 Mark: Method – dividing 1 ticket by total tickets sold]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Win}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate fraction]"
    )

    d1 = f"1/{total_tickets - 1}"
    d2 = f"10/{total_tickets}"
    d3 = f"{total_tickets}/1"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Probability = Number of tickets owned ÷ Total tickets sold.",
        tier_2=f"1 ticket out of {total_tickets}.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 26: Raffle Multiple Tickets Winning Chance
# --------------------------------------------------------------------------- #
def _gen_prob_raffle_multiple_tickets_winning_chance(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_raffle_multiple_tickets_winning_chance"
    name = r.choice(SA_NAMES)
    bought = r.choice([5, 10, 20, 25, 50])
    total_tickets = r.choice([500, 1000, 2000])
    pct = round((bought / total_tickets) * 100, 1)
    correct_ans = f"{bought}/{total_tickets} ({_fmt(pct)}%)"

    prompt = (
        f"{name} buys **{bought} tickets** in a community charity raffle where **{total_tickets} tickets** were sold.\n"
        f"One winning ticket will be drawn at random.\n\n"
        f"Calculate the probability that {name} holds the winning ticket."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Buying multiple tickets increases the number of favourable outcomes: $P(\\text{{Win}}) = \\frac{{\\text{{Tickets bought}}}}{{\\text{{Total tickets sold}}}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$P(\\text{{Win}}) = \\frac{{{bought}}}{{{total_tickets}}} = {_fmt(bought / total_tickets, 4)}$$\n"
        f"$$\\text{{Percentage}} = {_fmt(bought / total_tickets, 4)} \\times 100\\% = {_fmt(pct)}\\%$$ ✓ [1 Mark: Method – dividing bought tickets by total tickets and converting to %]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Win}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate fraction and percentage]"
    )

    d1 = f"1/{total_tickets} ({_fmt(round(100/total_tickets, 2))}%)"
    d2 = f"{bought * 2}/{total_tickets} ({_fmt(pct * 2)}%)"
    d3 = f"{bought}/{total_tickets - bought}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the tickets bought by total tickets sold.",
        tier_2=f"Calculate {bought} ÷ {total_tickets}.",
        tier_3=f"Winning chance = {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 27: Lucky Draw Token Selection
# --------------------------------------------------------------------------- #
def _gen_prob_luckydraw_token_selection(r: random.Random) -> Dict[str, Any]:
    sub_id = "prob_luckydraw_token_selection"
    name = r.choice(SA_NAMES)
    winning = r.choice([15, 20, 25])
    blank = r.choice([60, 75, 80])
    total = winning + blank
    pct = round((winning / total) * 100, 1)
    correct_ans = f"{winning}/{total} ({_fmt(pct)}%)"

    prompt = (
        f"At a church fête lucky draw, an urn contains {winning} winning prize tokens and {blank} blank tokens.\n\n"
        f"Calculate the probability of drawing a **winning token** on the first attempt."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Calculate the total number of tokens in the urn, then find the ratio of winning tokens to total tokens.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total tokens}} = {winning} + {blank} = {total}$$\n"
        f"$$P(\\text{{Winning}}) = \\frac{{{winning}}}{{{total}}} = {_fmt(pct)}\\%$$ ✓ [1 Mark: Method – dividing winning tokens by total urn tokens]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$P(\\text{{Winning}}) = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate fraction and percentage]"
    )

    d1 = f"{winning}/{blank}"
    d2 = f"{blank}/{total}"  # probability of blank
    d3 = f"{winning + 5}/{total}"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    d_spec = {
        "diagram_role": "context",
        "kind": "probability_spinner",
        "title": f"Lucky Draw Token Drum ({name})",
        "sectors": [
            {"label": "Section A", "value": 10},
            {"label": "Section B", "value": 15},
            {"label": "Section C", "value": 25},
        ],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find total tokens: winning + blank.",
        tier_2=f"Total = {winning} + {blank} = {total}.",
        tier_3=f"Probability = {correct_ans}.",
        r=r,
    )
