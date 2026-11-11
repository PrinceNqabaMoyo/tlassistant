"""Cluster 1: Graphs that Tell a Story & Trend Interpretation (Subskills 1 to 9)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)

# --------------------------------------------------------------------------- #
# Subskill 1: Increasing, Decreasing or Constant Segments
# --------------------------------------------------------------------------- #
def _gen_pat_story_increasing_decreasing_constant_segments(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_increasing_decreasing_constant_segments"
    name = r.choice(SA_NAMES)
    scenario = r.choice([
        ("water level in a municipal reservoir during summer rains", "increasing", "slopes upward from left to right"),
        ("remaining fuel in a taxi petrol tank while driving", "decreasing", "slopes downward from left to right"),
        ("body temperature of a healthy hospital patient overnight at 37 °C", "constant", "is flat and horizontal with zero gradient"),
    ])
    context, correct_trend, desc = scenario
    correct_ans = correct_trend.capitalize()

    prompt = (
        f"Refer to the line graph below monitoring {context}.\n\n"
        f"If the line graph {desc}, identify whether the relationship is increasing, decreasing, or constant."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In graph interpretation:\n"
        f"  • Upward slope from left to right = Increasing (dependent variable rises as independent variable increases)\n"
        f"  • Downward slope from left to right = Decreasing (dependent variable falls)\n"
        f"  • Flat horizontal line = Constant (no change in value)\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The scenario states that the line {desc}.\n"
        f"Therefore, the trend represents a **{correct_trend}** relationship. ✓ [1 Mark: Method – matching graph direction to mathematical trend]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct classification]"
    )

    y_end = 8 if correct_trend == "increasing" else (2 if correct_trend == "constant" else 0)
    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Story Graph ({name}: {correct_ans})",
        "lines": [{"points": [[0, 2], [5, y_end]], "label": context}],
    }

    custom = [correct_ans, "Increasing", "Decreasing", "Constant", "Undefined"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at the direction of the line from left to right.",
        tier_2=f"A line that {desc} represents a {correct_trend} graph.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} is inspecting a line graph monitoring the {context}.\n\n"
        f"If the line graph {desc}, identify whether the relationship is increasing, decreasing, or constant."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In graph interpretation:\n"
        f"  • Upward slope from left to right = Increasing (dependent variable rises as independent variable increases)\n"
        f"  • Downward slope from left to right = Decreasing (dependent variable falls)\n"
        f"  • Flat horizontal line = Constant (no change in value)\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The scenario states that the line {desc}.\n"
        f"Therefore, the trend represents a **{correct_trend}** relationship. ✓ [1 Mark: Method – matching graph direction to mathematical trend]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct classification]"
    )

    custom = [correct_ans, "Increasing", "Decreasing", "Constant", "Undefined"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Look at the direction of the line from left to right.",
        tier_2=f"A line that {desc} represents a {correct_trend} graph.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 2: Steepness & Rate of Change
# --------------------------------------------------------------------------- #
def _gen_pat_story_steepness_and_rate_of_change(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_steepness_and_rate_of_change"
    name = r.choice(SA_NAMES)
    segment_a_speed = r.choice([80, 90, 100])
    segment_b_speed = r.choice([30, 40, 50])
    correct_ans = "Segment A (Highway)"

    prompt = (
        f"Refer to the distance-time graph below for {name}'s journey divided into two driving sections:\n"
        f"  • Segment A (Highway): steep upward slope (speed = {segment_a_speed} km/h)\n"
        f"  • Segment B (City Traffic): gentle upward slope (speed = {segment_b_speed} km/h)\n\n"
        f"Which segment represents a faster rate of travel (greater speed)?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In a distance-time graph, the gradient (steepness of the slope) represents speed: "
        f"$\text{{Speed}} = \frac{{\Delta \text{{distance}}}}{{\Delta \text{{time}}}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"A steeper line means more distance is covered in less time. Segment A has a steeper slope ({segment_a_speed} km/h) compared to Segment B ({segment_b_speed} km/h). "
        f"✓ [1 Mark: Method – associating steeper slope with higher rate of change]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct segment choice]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Distance-Time Rate of Change ({name})",
        "lines": [
            {"points": [[0, 0], [2, segment_a_speed * 2]], "label": f"Seg A ({segment_a_speed} km/h)"},
            {"points": [[2, segment_a_speed * 2], [5, segment_a_speed * 2 + segment_b_speed * 3]], "label": f"Seg B ({segment_b_speed} km/h)"},
        ],
    }

    custom = ["Segment A (Highway)", "Segment B (City Traffic)", "Both have equal speed", "Neither, speed is zero"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The steeper the slope on a distance-time graph, the faster the speed.",
        tier_2=f"Segment A has a steeper slope than Segment B.",
        tier_3=f"The faster segment is {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} analyzes a distance-time graph representing a journey divided into two driving sections:\n"
        f"  • Segment A (Highway): The graph has a very steep upward slope (speed = {segment_a_speed} km/h)\n"
        f"  • Segment B (City Traffic): The graph has a gentle, gradual upward slope (speed = {segment_b_speed} km/h)\n\n"
        f"Which segment represents a faster rate of travel (greater speed)?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"In a distance-time graph, the gradient (steepness of the slope) represents the rate of change of distance with time, which is speed: "
        f"$\\text{{Speed}} = \\frac{{\\Delta \\text{{distance}}}}{{\\Delta \\text{{time}}}}$.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"A steeper line means more distance is covered in less time. Segment A has a steeper slope ({segment_a_speed} km/h) compared to Segment B ({segment_b_speed} km/h). "
        f"✓ [1 Mark: Method – associating steeper slope with higher rate of change]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct segment choice]"
    )

    custom = ["Segment A (Highway)", "Segment B (City Traffic)", "Both have equal speed", "Neither, speed is zero"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="The steeper the slope on a distance-time graph, the faster the speed.",
        tier_2=f"Segment A has a steeper slope than Segment B.",
        tier_3=f"The faster segment is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 3: Meaning of Horizontal Segment
# --------------------------------------------------------------------------- #
def _gen_pat_story_horizontal_segment_meaning(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_horizontal_segment_meaning"
    name = r.choice(SA_NAMES)
    stopped_mins = r.choice([15, 20, 30, 45])
    correct_ans = "The vehicle is stationary (stopped / resting) — time passes but distance does not change"

    prompt = (
        f"Refer to the distance-time graph below where a delivery vehicle travels between towns.\n"
        f"Between t = 1 hour and t = 1 hour {stopped_mins} min, the graph forms a flat, horizontal line segment.\n\n"
        f"What physical event does this flat horizontal segment represent in real life?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"On a distance-time graph, the vertical axis represents distance and the horizontal axis represents time.\n"
        f"A flat horizontal line means distance remains constant while time continues to advance.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$\text{{Speed}} = \frac{{\Delta \text{{distance}}}}{{\Delta \text{{time}}}} = \frac{{0}}{{{stopped_mins}\text{{ min}}}} = 0\text{{ km/h}}$. "
        f"✓ [1 Mark: Method – identifying zero gradient as zero speed / stationary state]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct physical interpretation]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Stationary Interval Profile ({name})",
        "lines": [{"points": [[0, 0], [1, 80], [1.5, 80], [3, 180]], "label": "Distance (km)"}],
    }

    custom = [
        correct_ans,
        "The vehicle is travelling at maximum speed on a highway",
        "The vehicle is reversing back towards the starting point",
        "The vehicle is driving up an extremely steep mountain pass",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="What happens to your distance from home when you stop to buy lunch?",
        tier_2="Time continues to pass, but the distance does not increase.",
        tier_3=f"The vehicle is stationary (speed = 0).",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} is reviewing a distance-time graph of a mountain hike.\n"
        f"Between 12:00 and 12:{minutes:02d}, the graph displays a flat, horizontal line segment.\n\n"
        f"What does this horizontal line segment mean in the context of the hike?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"On a distance-time graph, a horizontal segment means that time is continuing to pass on the x-axis, "
        f"but distance from the starting point on the y-axis is not changing.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Rate of change}} = \\frac{{\\Delta \\text{{distance}}}}{{\\Delta \\text{{time}}}} = \\frac{{0\\text{{ km}}}}{{{minutes}\\text{{ min}}}} = 0\\text{{ km/h}}$$\n"
        f"Zero gradient indicates that the hiker was not moving. ✓ [1 Mark: Method – recognizing zero gradient corresponds to zero movement]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct physical interpretation]"
    )

    custom = [
        correct_ans,
        "The hiker was walking at a very high constant speed",
        "The hiker was walking backwards down the hill",
        "The hiker was accelerating uphill rapidly",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Notice that the distance on the vertical axis stays constant while time advances.",
        tier_2="No change in distance means no movement occurred.",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 4: Discrete vs Continuous Data Type
# --------------------------------------------------------------------------- #
def _gen_pat_story_discrete_vs_continuous_data_type(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_discrete_vs_continuous_data_type"
    name = r.choice(SA_NAMES)
    is_discrete = r.choice([True, False])

    if is_discrete:
        context = r.choice([
            "number of passengers boarding a Putco commuter bus",
            "number of beaded traditional necklaces sold at a craft market",
            "number of cellular phone contracts registered",
            "number of loaves of bread purchased at a bakery",
        ])
        correct_ans = "Discrete data"
        reason = "counted in whole distinct numbers (you cannot have fractions of a person or whole item)"
    else:
        context = r.choice([
            "outdoor ambient temperature in Bloemfontein over a 24-hour period",
            "distance run by an athlete during marathon training",
            "volume of petrol remaining in a motor vehicle fuel tank",
            "height of a growing sunflower seedling measured daily",
        ])
        correct_ans = "Continuous data"
        reason = "measured on a continuous numerical scale and can take any decimal value within a range"

    prompt = (
        f"{name} is classifying statistical variables for a Mathematical Literacy research project.\n\n"
        f"Classify the following variable as either **discrete** or **continuous**:\n"
        f"\"**{context}**\""
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"  • **Discrete data** consists of distinct, separate values that are counted in whole units (no intermediate fractions).\n"
        f"  • **Continuous data** consists of measurements on an unbroken continuum that can take any fractional or decimal value.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"The variable is '{context}', which is {reason}. ✓ [1 Mark: Method – applying discrete vs continuous test]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct classification]"
    )

    custom = [correct_ans, "Continuous data" if is_discrete else "Discrete data", "Categorical ordinal data", "Qualitative nominal data"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Ask yourself: is this counted in whole separate numbers, or measured on a continuous scale?",
        tier_2=f"Since it is {reason}, it must be {correct_ans}.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 5: Discrete vs Continuous Graph Style
# --------------------------------------------------------------------------- #
def _gen_pat_story_discrete_vs_continuous_graph_style(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_discrete_vs_continuous_graph_style"
    ticket_cost = r.choice([25, 30, 40, 50])
    correct_ans = "Discrete graph (isolated dots / plotted points only, NOT connected by a solid line)"

    prompt = (
        f"A school sells concert tickets at R {ticket_cost} per ticket. A learner plots a graph of Total Cost (y) versus Number of Tickets Sold (x).\n\n"
        f"Refer to the graph style plot below.\n\n"
        f"Should this graph be drawn as a continuous solid line, or as discrete points (separate dots), and why?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Tickets can only be sold in whole integer quantities (1, 2, 3 tickets). You cannot purchase 2,4 or 3,75 tickets.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"A continuous solid line would imply that fractional ticket quantities are valid and available. "
        f"Therefore, discrete countable data must be represented by isolated points/dots only. ✓ [1 Mark: Method – discrete variable identification]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct graph style designation]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Concert Tickets (R {ticket_cost}/ticket)",
        "lines": [{"points": [[1, ticket_cost], [2, ticket_cost * 2], [3, ticket_cost * 3], [4, ticket_cost * 4]], "label": "Discrete Points"}],
    }

    custom = [
        correct_ans,
        "Continuous graph (solid unbroken line passing through all fractions)",
        "Curved parabola connecting only even ticket numbers",
        "Horizontal step tariff with infinite vertical jumps",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Can someone buy half a concert ticket?",
        tier_2="Because tickets are discrete whole items, do not connect the points with a solid line.",
        tier_3=f"Correct style: {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} collects data showing the number of movie tickets sold and the total income collected.\n\n"
        f"Why should the graph of this relationship be plotted as **{correct_ans.lower()}** rather than an unbroken continuous solid line?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Tickets are discrete physical items that can only be bought in whole integer numbers (e.g. 1, 2, 3 tickets).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"If a solid unbroken line were drawn connecting the points, points on that line would imply that fractions of tickets (e.g. 2,4 tickets) "
        f"could be purchased, which is physically impossible in the real world. ✓ [1 Mark: Method – articulating why discrete points prevent fractional fallacies]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct graphical convention]"
    )

    custom = [
        correct_ans,
        "A continuous unbroken solid line connecting all coordinates",
        "A curved parabolic line opening downwards",
        "A horizontal stepped line with alternating colours",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Because ticket sales cannot take fractional values, points cannot be connected by a solid line.",
        tier_2="Discrete data must be plotted as separate distinct points/dots.",
        tier_3=f"The correct format is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 6: Independent vs Dependent Variables
# --------------------------------------------------------------------------- #
def _gen_pat_story_independent_vs_dependent_variable_identification(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_independent_vs_dependent_variable_identification"
    name = r.choice(SA_NAMES)
    pair = r.choice([
        ("mass of potatoes purchased (kg)", "total cost paid (Rands)", "mass of potatoes purchased (kg)", "total cost paid (Rands)"),
        ("number of hours worked", "total wages earned (Rands)", "number of hours worked", "total wages earned (Rands)"),
        ("distance driven (km)", "litres of petrol consumed", "distance driven (km)", "litres of petrol consumed"),
        ("duration of cellphone call (minutes)", "cost of the call (Rands)", "duration of cellphone call (minutes)", "cost of the call (Rands)"),
    ])
    v1, v2, indep, dep = pair
    ask_indep = r.choice([True, False])

    if ask_indep:
        correct_ans = indep
        prompt = (
            f"{name} investigates the relationship between the {v1} and the {v2}.\n\n"
            f"Identify the **independent variable** (the variable plotted on the horizontal x-axis)."
        )
        explanation = (
            f"**Step 1: Conceptual Reasoning & Identification**\n"
            f"The independent variable is the variable that changes freely or is chosen first (the cause), "
            f"and is placed on the horizontal axis ($x$-axis).\n\n"
            f"**Step 2: Technical Method & Working Setup**\n"
            f"Here, the '{dep}' depends upon the '{indep}'. "
            f"Therefore, '{indep}' is the independent variable. ✓ [1 Mark: Method – identifying input variable]\n\n"
            f"**Step 3: Final Calculation & Answer**\n"
            f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct independent variable]"
        )
    else:
        correct_ans = dep
        prompt = (
            f"{name} investigates the relationship between the {v1} and the {v2}.\n\n"
            f"Identify the **dependent variable** (the outcome variable plotted on the vertical y-axis)."
        )
        explanation = (
            f"**Step 1: Conceptual Reasoning & Identification**\n"
            f"The dependent variable is the outcome being measured (the effect), which depends on the independent variable, "
            f"and is plotted on the vertical axis ($y$-axis).\n\n"
            f"**Step 2: Technical Method & Working Setup**\n"
            f"The '{dep}' changes as a consequence of '{indep}'. "
            f"Therefore, '{dep}' is the dependent variable. ✓ [1 Mark: Method – identifying outcome variable]\n\n"
            f"**Step 3: Final Calculation & Answer**\n"
            f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct dependent variable]"
        )

    custom = [indep, dep, "Neither, both are constant", "Both are independent"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Ask: which variable depends on the other?",
        tier_2=f"The {dep} depends on the {indep}.",
        tier_3=f"The answer is {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 7: Vertical Intercept Interpretation
# --------------------------------------------------------------------------- #
def _gen_pat_story_vertical_intercept_interpretation(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_vertical_intercept_interpretation"
    name = r.choice(SA_NAMES)
    callout_fee = r.choice([250, 300, 350, 400])
    hourly_rate = r.choice([150, 200, 250])
    correct_ans = f"R {_fmt(callout_fee)} — The fixed call-out fee charged before any work begins (at 0 hours)"

    prompt = (
        f"{name} hires a plumber who charges according to the cost graph below:\n"
        f"The line intersects the vertical y-axis at (0; {callout_fee}) and rises at R {hourly_rate} per hour.\n\n"
        f"What real-world financial cost does the vertical intercept (0; {callout_fee}) represent?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The vertical y-intercept occurs where the independent variable x = 0 (hours worked = 0).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"At x = 0, the cost is already R {callout_fee}. This represents the base fixed call-out / booking fee before any hours are logged. "
        f"✓ [1 Mark: Method – connecting y-intercept to zero-input fixed cost]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct financial interpretation]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Plumber Fee Schedule ({name}: y-int = R{callout_fee})",
        "lines": [{"points": [[0, callout_fee], [4, callout_fee + hourly_rate * 4]], "label": "Total Cost (R)"}],
    }

    custom = [
        correct_ans,
        f"The hourly labour rate of R {hourly_rate} per hour",
        f"The maximum total fee the plumber can charge",
        "The cost of replacement copper pipes and materials",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="What is the value of x (hours) at the y-axis intercept?",
        tier_2="At 0 hours, the cost is the fixed starting call-out fee.",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} hires a plumber. The graph of total cost against hours worked touches the vertical axis at the point $(0; {callout})$.\n\n"
        f"Explain the practical meaning of this vertical intercept ($y$-intercept) in the context of the plumber's charges."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The vertical intercept occurs where the horizontal independent variable ($x$) is zero.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"At $x = 0$ hours of work, the customer must already pay R {callout}. "
        f"This represents the basic fixed call-out fee (or minimum booking charge) that applies regardless of hours worked. "
        f"✓ [1 Mark: Method – connecting y-intercept to fixed base fee at x = 0]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct contextual explanation]"
    )

    custom = [
        correct_ans,
        f"The hourly rate charged per hour of plumbing work (R {callout}/h)",
        "The total maximum fee the plumber is allowed to charge",
        "The deposit refunded to the customer when the job finishes",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="At the vertical axis, the hours worked is zero.",
        tier_2=f"If hours = 0, the cost of R {callout} is the fixed call-out fee.",
        tier_3=f"The correct interpretation is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 8: Horizontal Intercept Interpretation
# --------------------------------------------------------------------------- #
def _gen_pat_story_horizontal_intercept_interpretation(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_horizontal_intercept_interpretation"
    name = r.choice(SA_NAMES)
    initial_fuel = r.choice([45, 50, 60, 70])
    burn_rate = r.choice([5, 6, 8])
    run_hours = initial_fuel / burn_rate
    correct_ans = f"{_fmt(run_hours)} hours — The point in time when the petrol tank is completely empty (0 litres remaining)"

    prompt = (
        f"{name} operates an emergency backup electricity generator with a full tank of {initial_fuel} litres of petrol.\n"
        f"A line graph tracks remaining petrol over time, intersecting the horizontal time axis at ({_fmt(run_hours)}; 0).\n\n"
        f"Refer to the fuel depletion line graph below.\n\n"
        f"What physical event does this horizontal x-intercept ({_fmt(run_hours)}; 0) represent?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The horizontal x-intercept occurs where the dependent variable y = 0 (remaining petrol = 0 litres).\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"When y = 0, all fuel has been consumed. The time coordinate ({_fmt(run_hours)} hours) is when the generator runs out of fuel and shuts down. "
        f"✓ [1 Mark: Method – identifying x-intercept as zero-fuel depletion state]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct physical explanation]"
    )

    diagram_spec = {
        "diagram_role": "context",
        "kind": "cartesian_system",
        "title": f"Fuel Depletion Profile ({name}: {_fmt(run_hours)}h)",
        "lines": [{"points": [[0, initial_fuel], [run_hours, 0]], "label": "Fuel Remaining (L)"}],
    }

    custom = [
        correct_ans,
        f"The generator starting up with {initial_fuel} litres",
        f"The generator running at maximum electrical wattage",
        "The moment the oil filter must be replaced",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="What is the value of y (petrol) at the x-axis intercept?",
        tier_2="When y = 0 litres, the fuel tank is completely empty.",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

    prompt = (
        f"{name} is studying a graph showing the volume of fuel remaining in a car's tank against distance driven in kilometres.\n"
        f"The graph touches the horizontal axis at the coordinate point $({km}; 0)$.\n\n"
        f"What is the practical real-world meaning of this horizontal intercept ($x$-intercept)?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"The horizontal intercept occurs where the vertical dependent variable ($y$) equals zero.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"At distance $x = {km}$ km, the remaining fuel volume $y = 0$ litres. "
        f"This means the fuel tank is completely empty after driving {km} km. "
        f"✓ [1 Mark: Method – interpreting y = 0 as an empty fuel tank at the intercept]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – accurate contextual deduction]"
    )

    custom = [
        correct_ans,
        f"The car's fuel tank holds a maximum capacity of {km} litres",
        f"The car travels at an average speed of {km} km/h",
        "The car was stationary for 0 hours",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="At the horizontal axis, the remaining fuel is 0 litres.",
        tier_2=f"When distance reaches {km} km, fuel is 0 litres (empty tank).",
        tier_3=f"The answer is: {correct_ans}.",
        r=r,
    )

# --------------------------------------------------------------------------- #
# Subskill 9: Average Speed from Distance-Time Segment
# --------------------------------------------------------------------------- #
def _gen_pat_story_distance_time_average_speed_segment(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_distance_time_average_speed_segment"
    name = r.choice(SA_NAMES)
    time_hrs = r.choice([2, 3, 4])
    speed = r.choice([60, 70, 80, 90, 100])
    dist_km = speed * time_hrs
    correct_ans = f"{speed} km/h"

    prompt = (
        f"{name} is analyzing a distance-time graph of a delivery van.\n"
        f"Between time $t = 1$ hour (at distance 50 km) and $t = {1 + time_hrs}$ hours (at distance {50 + dist_km} km), the line is straight.\n\n"
        f"Calculate the average speed of the van during this {time_hrs}-hour segment.\n\n"
        f"**Formula**: $\\text{{Average Speed}} = \\frac{{\\Delta \\text{{distance}}}}{{\\Delta \\text{{time}}}}$"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Average speed is the gradient of the line on a distance-time graph: change in distance divided by change in time.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\Delta \\text{{distance}} = {50 + dist_km} - 50 = {dist_km}\\text{{ km}}$$\n"
        f"$$\\Delta \\text{{time}} = {1 + time_hrs} - 1 = {time_hrs}\\text{{ hours}}$$\n"
        f"$$\\text{{Average Speed}} = \\frac{{{dist_km}}}{{{time_hrs}}}$$ ✓ [1 Mark: Method – dividing change in distance by change in time]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Average Speed}} = {speed}\\text{{ km/h}}$$ ✓ [1 Mark: Accuracy – accurate speed with units]"
    )

    d1 = f"{speed + 15} km/h"
    d2 = f"{speed - 10} km/h"
    d3 = f"{dist_km} km/h"
    options, _ = _build_options(correct_ans, r, [correct_ans, d1, d2, d3])

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Change in distance = final distance - initial distance.",
        tier_2=f"Distance = {dist_km} km, Time = {time_hrs} h. Calculate {dist_km} ÷ {time_hrs}.",
        tier_3=f"Average speed = {correct_ans}.",
        r=r,
    )
