"""Remediate all remaining Grade 10 subskills for REM-5."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ML_BASE = os.path.join(ROOT, "caps-ai-backend", "app", "utils", "mathematical_literacy")

def remediate_patterns():
    base = os.path.join(ML_BASE, "patterns_relationships")
    
    # 1. story_graphs_trends.py (Subskills 1 to 6)
    p = os.path.join(base, "story_graphs_trends.py")
    c = open(p, encoding="utf-8").read()

    # Subskill 1: pat_story_increasing_decreasing_constant_segments
    old_s1 = re.search(r'def _gen_pat_story_increasing_decreasing_constant_segments\(.*?\n\n', c, re.S).group(0)
    new_s1 = '''def _gen_pat_story_increasing_decreasing_constant_segments(r: random.Random) -> Dict[str, Any]:
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
        f"Refer to the line graph below monitoring {context}.\\n\\n"
        f"If the line graph {desc}, identify whether the relationship is increasing, decreasing, or constant."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"In graph interpretation:\\n"
        f"  • Upward slope from left to right = Increasing (dependent variable rises as independent variable increases)\\n"
        f"  • Downward slope from left to right = Decreasing (dependent variable falls)\\n"
        f"  • Flat horizontal line = Constant (no change in value)\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"The scenario states that the line {desc}.\\n"
        f"Therefore, the trend represents a **{correct_trend}** relationship. ✓ [1 Mark: Method – matching graph direction to mathematical trend]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct classification]"
    )

    y_end = 8 if correct_trend == "increasing" else (2 if correct_trend == "constant" else 0)
    diagram_spec = {
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

'''
    c = c.replace(old_s1, new_s1)

    # Subskill 2: pat_story_steepness_and_rate_of_change
    old_s2 = re.search(r'def _gen_pat_story_steepness_and_rate_of_change\(.*?\n\n', c, re.S).group(0)
    new_s2 = '''def _gen_pat_story_steepness_and_rate_of_change(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_steepness_and_rate_of_change"
    name = r.choice(SA_NAMES)
    segment_a_speed = r.choice([80, 90, 100])
    segment_b_speed = r.choice([30, 40, 50])
    correct_ans = "Segment A (Highway)"

    prompt = (
        f"Refer to the distance-time graph below for {name}'s journey divided into two driving sections:\\n"
        f"  • Segment A (Highway): steep upward slope (speed = {segment_a_speed} km/h)\\n"
        f"  • Segment B (City Traffic): gentle upward slope (speed = {segment_b_speed} km/h)\\n\\n"
        f"Which segment represents a faster rate of travel (greater speed)?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"In a distance-time graph, the gradient (steepness of the slope) represents speed: "
        f"$\\text{{Speed}} = \\frac{{\\Delta \\text{{distance}}}}{{\\Delta \\text{{time}}}}$.\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"A steeper line means more distance is covered in less time. Segment A has a steeper slope ({segment_a_speed} km/h) compared to Segment B ({segment_b_speed} km/h). "
        f"✓ [1 Mark: Method – associating steeper slope with higher rate of change]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct segment choice]"
    )

    diagram_spec = {
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

'''
    c = c.replace(old_s2, new_s2)

    # Subskill 3: pat_story_horizontal_segment_meaning
    old_s3 = re.search(r'def _gen_pat_story_horizontal_segment_meaning\(.*?\n\n', c, re.S).group(0)
    new_s3 = '''def _gen_pat_story_horizontal_segment_meaning(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_horizontal_segment_meaning"
    name = r.choice(SA_NAMES)
    stopped_mins = r.choice([15, 20, 30, 45])
    correct_ans = "The vehicle is stationary (stopped / resting) — time passes but distance does not change"

    prompt = (
        f"Refer to the distance-time graph below where a delivery vehicle travels between towns.\\n"
        f"Between t = 1 hour and t = 1 hour {stopped_mins} min, the graph forms a flat, horizontal line segment.\\n\\n"
        f"What physical event does this flat horizontal segment represent in real life?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"On a distance-time graph, the vertical axis represents distance and the horizontal axis represents time.\\n"
        f"A flat horizontal line means distance remains constant while time continues to advance.\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"$\\text{{Speed}} = \\frac{{\\Delta \\text{{distance}}}}{{\\Delta \\text{{time}}}} = \\frac{{0}}{{{stopped_mins}\\text{{ min}}}} = 0\\text{{ km/h}}$. "
        f"✓ [1 Mark: Method – identifying zero gradient as zero speed / stationary state]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct physical interpretation]"
    )

    diagram_spec = {
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

'''
    c = c.replace(old_s3, new_s3)

    # Subskill 4: pat_story_discrete_vs_continuous_graph_style
    old_s4 = re.search(r'def _gen_pat_story_discrete_vs_continuous_graph_style\(.*?\n\n', c, re.S).group(0)
    new_s4 = '''def _gen_pat_story_discrete_vs_continuous_graph_style(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_discrete_vs_continuous_graph_style"
    ticket_cost = r.choice([25, 30, 40, 50])
    correct_ans = "Discrete graph (isolated dots / plotted points only, NOT connected by a solid line)"

    prompt = (
        f"A school sells concert tickets at R {ticket_cost} per ticket. A learner plots a graph of Total Cost (y) versus Number of Tickets Sold (x).\\n\\n"
        f"Refer to the graph style plot below.\\n\\n"
        f"Should this graph be drawn as a continuous solid line, or as discrete points (separate dots), and why?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"Tickets can only be sold in whole integer quantities (1, 2, 3 tickets). You cannot purchase 2,4 or 3,75 tickets.\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"A continuous solid line would imply that fractional ticket quantities are valid and available. "
        f"Therefore, discrete countable data must be represented by isolated points/dots only. ✓ [1 Mark: Method – discrete variable identification]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct graph style designation]"
    )

    diagram_spec = {
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

'''
    c = c.replace(old_s4, new_s4)

    # Subskill 5: pat_story_vertical_intercept_interpretation
    old_s5 = re.search(r'def _gen_pat_story_vertical_intercept_interpretation\(.*?\n\n', c, re.S).group(0)
    new_s5 = '''def _gen_pat_story_vertical_intercept_interpretation(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_vertical_intercept_interpretation"
    name = r.choice(SA_NAMES)
    callout_fee = r.choice([250, 300, 350, 400])
    hourly_rate = r.choice([150, 200, 250])
    correct_ans = f"R {_fmt(callout_fee)} — The fixed call-out fee charged before any work begins (at 0 hours)"

    prompt = (
        f"{name} hires a plumber who charges according to the cost graph below:\\n"
        f"The line intersects the vertical y-axis at (0; {callout_fee}) and rises at R {hourly_rate} per hour.\\n\\n"
        f"What real-world financial cost does the vertical intercept (0; {callout_fee}) represent?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"The vertical y-intercept occurs where the independent variable x = 0 (hours worked = 0).\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"At x = 0, the cost is already R {callout_fee}. This represents the base fixed call-out / booking fee before any hours are logged. "
        f"✓ [1 Mark: Method – connecting y-intercept to zero-input fixed cost]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct financial interpretation]"
    )

    diagram_spec = {
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

'''
    c = c.replace(old_s5, new_s5)

    # Subskill 6: pat_story_horizontal_intercept_interpretation
    old_s6 = re.search(r'def _gen_pat_story_horizontal_intercept_interpretation\(.*?\n\n', c, re.S).group(0)
    new_s6 = '''def _gen_pat_story_horizontal_intercept_interpretation(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_story_horizontal_intercept_interpretation"
    name = r.choice(SA_NAMES)
    initial_fuel = r.choice([45, 50, 60, 70])
    burn_rate = r.choice([5, 6, 8])
    run_hours = initial_fuel / burn_rate
    correct_ans = f"{_fmt(run_hours)} hours — The point in time when the petrol tank is completely empty (0 litres remaining)"

    prompt = (
        f"{name} operates an emergency backup electricity generator with a full tank of {initial_fuel} litres of petrol.\\n"
        f"A line graph tracks remaining petrol over time, intersecting the horizontal time axis at ({_fmt(run_hours)}; 0).\\n\\n"
        f"Refer to the fuel depletion line graph below.\\n\\n"
        f"What physical event does this horizontal x-intercept ({_fmt(run_hours)}; 0) represent?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"The horizontal x-intercept occurs where the dependent variable y = 0 (remaining petrol = 0 litres).\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"When y = 0, all fuel has been consumed. The time coordinate ({_fmt(run_hours)} hours) is when the generator runs out of fuel and shuts down. "
        f"✓ [1 Mark: Method – identifying x-intercept as zero-fuel depletion state]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct physical explanation]"
    )

    diagram_spec = {
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

'''
    c = c.replace(old_s6, new_s6)
    open(p, "w", encoding="utf-8").write(c)
    print("remediated story_graphs_trends.py")

    # 2. linear_tables_patterns.py: pat_linear_direct_proportion_origin_property
    p_lin = os.path.join(base, "linear_tables_patterns.py")
    c_lin = open(p_lin, encoding="utf-8").read()
    old_lin = re.search(r'def _gen_pat_linear_direct_proportion_origin_property\(.*?\n\n', c_lin, re.S).group(0)
    new_lin = '''def _gen_pat_linear_direct_proportion_origin_property(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_linear_direct_proportion_origin_property"
    k = r.choice([15, 20, 25, 30])
    correct_ans = "It is a straight line that passes through the origin (0; 0)"

    prompt = (
        f"Refer to the direct proportion graph below (y = {k}x).\\n\\n"
        f"What fundamental geometric property must be true for the graph of any direct proportion relationship?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"A direct proportion has the algebraic formula y = kx.\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"When x = 0, y = k(0) = 0. Therefore the line must be straight and pass through (0; 0). "
        f"✓ [1 Mark: Method – identifying direct proportion origin constraint]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct geometric property]"
    )

    diagram_spec = {
        "kind": "cartesian_system",
        "title": f"Direct Proportion (y = {k}x)",
        "lines": [{"points": [[0, 0], [4, k * 4]], "label": f"y = {k}x"}],
    }

    custom = [
        correct_ans,
        "It is a curved hyperbola that never touches the axes",
        "It is a horizontal line with a y-intercept greater than zero",
        "It is a stepped line with discontinuous jumps",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="What is y when x = 0 in y = kx?",
        tier_2="When x = 0, y = 0, so the line passes through (0; 0).",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

'''
    c_lin = c_lin.replace(old_lin, new_lin)
    open(p_lin, "w", encoding="utf-8").write(c_lin)
    print("remediated linear_tables_patterns.py")

    # 3. inverse_proportion.py: pat_inv_graph_characteristics_and_shape
    p_inv = os.path.join(base, "inverse_proportion.py")
    c_inv = open(p_inv, encoding="utf-8").read()
    old_inv = re.search(r'def _gen_pat_inv_graph_characteristics_and_shape\(.*?\n\n', c_inv, re.S).group(0)
    new_inv = '''def _gen_pat_inv_graph_characteristics_and_shape(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_inv_graph_characteristics_and_shape"
    k_val = r.choice([60, 100, 120, 240])
    correct_ans = "A smooth, downward-sloping curve (hyperbola) that approaches both axes but never touches or intersects them"

    prompt = (
        f"Refer to the inverse proportion graph below (xy = {k_val}).\\n\\n"
        f"Which statement accurately describes the shape and characteristics of an **Inverse Proportion** graph?"
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"An inverse proportion has the equation y = k ÷ x.\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"As x increases, y decreases asymptotically. The curve is a hyperbola that never touches x=0 or y=0. "
        f"✓ [1 Mark: Method – identifying hyperbolic asymptotic behavior]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct curve description]"
    )

    diagram_spec = {
        "kind": "cartesian_system",
        "title": f"Inverse Proportion (xy = {k_val})",
        "lines": [{"points": [[1, k_val], [2, k_val // 2], [4, k_val // 4], [5, k_val // 5]], "label": f"y = {k_val}/x"}],
    }

    custom = [
        correct_ans,
        "A straight line passing through the origin (0; 0)",
        "A vertical straight line parallel to the y-axis",
        "A series of discrete horizontal steps",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Does the product x × y equal a constant?",
        tier_2="As x gets bigger, y gets smaller, creating a smooth downward curve called a hyperbola.",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

'''
    c_inv = c_inv.replace(old_inv, new_inv)
    open(p_inv, "w", encoding="utf-8").write(c_inv)
    print("remediated inverse_proportion.py")

    # 4. breakeven_comparisons.py: pat_comp_car_rental_plan_comparison, pat_comp_income_formula_and_graph, pat_comp_production_cost_formula_and_graph
    p_brk = os.path.join(base, "breakeven_comparisons.py")
    c_brk = open(p_brk, encoding="utf-8").read()

    # pat_comp_car_rental_plan_comparison
    old_cr = re.search(r'def _gen_pat_comp_car_rental_plan_comparison\(.*?\n\n', c_brk, re.S).group(0)
    new_cr = '''def _gen_pat_comp_car_rental_plan_comparison(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_car_rental_plan_comparison"
    name = r.choice(SA_NAMES)
    flat_fee = r.choice([250, 300, 350])
    rate_a = 2.00
    rate_b = 3.50
    # Break-even: flat_fee + rate_a * x = rate_b * x => x = flat_fee / (rate_b - rate_a) = flat_fee / 1.5
    break_even_km = round(flat_fee / (rate_b - rate_a))
    test_km = break_even_km + r.choice([40, 60, 80])

    cost_a = flat_fee + rate_a * test_km
    cost_b = rate_b * test_km
    cheaper = "Option A" if cost_a < cost_b else "Option B"
    correct_ans = f"{cheaper} is cheaper for {_fmt(test_km)} km (Option A: R {_fmt(cost_a)}, Option B: R {_fmt(cost_b)})"

    prompt = (
        f"{name} is comparing two car rental options for a trip of {_fmt(test_km)} km:\\n"
        f"• Option A: Flat fee of R {flat_fee} plus R {_fmt(rate_a)} per km\\n"
        f"• Option B: No flat fee (R 0), but R {_fmt(rate_b)} per km\\n\\n"
        f"Refer to the car rental comparison graph below.\\n\\n"
        f"Determine which option is cheaper for a {_fmt(test_km)} km trip and calculate the total cost for both options."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"Calculate cost for each option at x = {test_km} km and compare.\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"Cost A = R {flat_fee} + ({rate_a} × {test_km}) = R {_fmt(cost_a)}.\\n"
        f"Cost B = {rate_b} × {test_km} = R {_fmt(cost_b)}. ✓ [1 Mark: Method – evaluating both cost functions]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct comparison]"
    )

    diagram_spec = {
        "kind": "cartesian_system",
        "title": f"Car Rental Comparison ({name}: {test_km} km)",
        "lines": [
            {"points": [[0, flat_fee], [test_km, cost_a]], "label": "Option A"},
            {"points": [[0, 0], [test_km, cost_b]], "label": "Option B"},
        ],
    }

    custom = [
        correct_ans,
        f"Option B is cheaper for {_fmt(test_km)} km",
        "Both options have identical total cost",
        "Neither option is viable",
    ]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the cost for each option at the given distance.",
        tier_2=f"Option A = {flat_fee} + ({rate_a} × {test_km}); Option B = {rate_b} × {test_km}.",
        tier_3=f"{correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

'''
    c_brk = c_brk.replace(old_cr, new_cr)

    # pat_comp_income_formula_and_graph
    old_inc = re.search(r'def _gen_pat_comp_income_formula_and_graph\(.*?\n\n', c_brk, re.S).group(0)
    new_inc = '''def _gen_pat_comp_income_formula_and_graph(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_income_formula_and_graph"
    name = r.choice(SA_NAMES)
    selling_price = r.choice([25, 30, 40, 50])
    items = r.choice([50, 80, 100, 120])
    total_income = selling_price * items
    correct_ans = f"R {_fmt(total_income)}"

    prompt = (
        f"{name} runs a small business selling handmade crafts at R {selling_price} each.\\n"
        f"Refer to the business income graph below (Income = {selling_price} × items sold).\\n\\n"
        f"Calculate the total income when {items} craft items are sold."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"Income is directly proportional to units sold: Income = Price × Quantity.\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"Income = R {selling_price} × {items} = R {_fmt(total_income)}. ✓ [1 Mark: Method – linear income evaluation]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct Rand income]"
    )

    diagram_spec = {
        "kind": "cartesian_system",
        "title": f"Business Income Profile ({name}: R{selling_price}/unit)",
        "lines": [{"points": [[0, 0], [items, total_income]], "label": "Income Line"}],
    }

    custom = [correct_ans, f"R {_fmt(total_income + selling_price)}", f"R {_fmt(total_income - selling_price)}", f"R {_fmt(total_income // 2)}"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Multiply selling price (R {selling_price}) by items sold ({items}).",
        tier_2=f"Income = {selling_price} × {items}.",
        tier_3=f"Total income = {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

'''
    c_brk = c_brk.replace(old_inc, new_inc)

    # pat_comp_production_cost_formula_and_graph
    old_prod = re.search(r'def _gen_pat_comp_production_cost_formula_and_graph\(.*?\n\n', c_brk, re.S).group(0)
    new_prod = '''def _gen_pat_comp_production_cost_formula_and_graph(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_comp_production_cost_formula_and_graph"
    name = r.choice(SA_NAMES)
    fixed_cost = r.choice([400, 500, 600, 800])
    var_cost = r.choice([12, 15, 18, 20])
    items = r.choice([30, 40, 50, 60])
    total_cost = fixed_cost + var_cost * items
    correct_ans = f"R {_fmt(total_cost)}"

    prompt = (
        f"{name} bakes and sells artisan pies. Production costs follow the cost graph below:\\n"
        f"Formula: Total Cost = R {fixed_cost} (fixed equipment) + (R {var_cost} × pies produced)\\n\\n"
        f"Calculate the total production cost to bake {items} pies."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\\n"
        f"Total Cost = Fixed Cost + (Variable Cost per unit × Number of Units).\\n\\n"
        f"**Step 2: Technical Method & Working Setup**\\n"
        f"Total Cost = R {fixed_cost} + ({var_cost} × {items}) = R {fixed_cost} + R {var_cost * items} = R {_fmt(total_cost)}. "
        f"✓ [1 Mark: Method – substituting into linear cost equation]\\n\\n"
        f"**Step 3: Final Calculation & Answer**\\n"
        f"**{correct_ans}** ✓ [1 Mark: Accuracy – correct total production cost]"
    )

    diagram_spec = {
        "kind": "cartesian_system",
        "title": f"Artisan Bakery Production Cost ({name})",
        "lines": [{"points": [[0, fixed_cost], [items, total_cost]], "label": "Total Cost Line"}],
    }

    custom = [correct_ans, f"R {_fmt(total_cost + var_cost)}", f"R {_fmt(total_cost - fixed_cost)}", f"R {_fmt(total_cost + 100)}"]
    options, _ = _build_options(correct_ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Add fixed cost (R {fixed_cost}) to variable cost ({var_cost} × {items}).",
        tier_2=f"Cost = {fixed_cost} + ({var_cost} × {items}).",
        tier_3=f"Total cost = {correct_ans}.",
        r=r,
        diagram_spec=diagram_spec,
    )

'''
    c_brk = c_brk.replace(old_prod, new_prod)
    open(p_brk, "w", encoding="utf-8").write(c_brk)
    print("remediated breakeven_comparisons.py")

    # 5. stepped_graphs_modeling.py: pat_rep_water_tiered_consumption_graph
    p_stp = os.path.join(base, "stepped_graphs_modeling.py")
    c_stp = open(p_stp, encoding="utf-8").read()
    old_stp = re.search(r'def _gen_pat_rep_water_tiered_consumption_graph\(.*?\n\n', c_stp, re.S).group(0)
    new_stp = '''def _gen_pat_rep_water_tiered_consumption_graph(r: random.Random) -> Dict[str, Any]:
    sub_id = "pat_rep_water_tiered_consumption_graph"
    name = r.choice(SA_NAMES)
    step1_rate = 0.00
    step2_rate = r.choice([15.50, 18.00, 20.00])
    step3_rate = r.choice([25.00, 28.50, 32.00])

    prompt = (
        f"Refer to the municipal stepped water tariff graph below for domestic households in {name}'s town:\\n"
        f"• Block 1 (0 to 6 kL): R {_fmt_curr(step1_rate)} per kL (Free basic water)\\n"
        f"• Block 2 (>6 to 20 kL): R {_fmt_curr(step2_rate)} per kL\\n"
        f"• Block 3 (>20 kL): R {_fmt_curr(step3_rate)} per kL\\n\\n"
        f"Why is a tiered water consumption tariff drawn as a stepped graph with horizontal line segments rather than a continuous straight line?"
    )
    ans = "The tariff rate per kilolitre remains constant within each consumption bracket (block), then abruptly jumps to a higher rate when crossing into the next bracket."
    opts = [
        "The tariff rate per kilolitre remains constant within each consumption bracket (block), then abruptly jumps to a higher rate when crossing into the next bracket.",
        "Water meters only register water flow on Sundays.",
        "The municipality changes prices every hour of the day.",
        "Stepped lines indicate that water is free of bacteria.",
    ]

    s1 = f"Understand piecewise step functions: rates are fixed within discrete interval intervals, causing discontinuous step jumps."
    s2 = f"✓ [1 Mark: Method – Identifying constant block rate property]\\nTariff is constant within blocks, jumping between blocks."
    s3 = f"✓ [1 Mark: Accuracy – Correct rationale]\\n{ans}"

    diagram_spec = {
        "kind": "step_tariff",
        "title": f"Municipal Water Step Tariff ({name})",
        "steps": [
            {"from_kl": 0, "to_kl": 6, "rate": step1_rate},
            {"from_kl": 6, "to_kl": 20, "rate": step2_rate},
            {"from_kl": 20, "to_kl": 40, "rate": step3_rate},
        ],
    }

    custom = [ans] + opts[1:]
    options, _ = _build_options(ans, r, custom)

    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=ans,
        options=options,
        explanation=f"Step 1: {s1}\\nStep 2: {s2}\\nStep 3: {s3}",
        tier_1="What happens to the price per kL when you cross into a higher block?",
        tier_2="The price stays fixed in each block, then jumps up.",
        tier_3=f"{ans}",
        r=r,
        diagram_spec=diagram_spec,
    )

'''
    c_stp = c_stp.replace(old_stp, new_stp)
    open(p_stp, "w", encoding="utf-8").write(c_stp)
    print("remediated stepped_graphs_modeling.py")

remediate_patterns()
