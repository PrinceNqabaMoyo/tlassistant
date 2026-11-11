from __future__ import annotations
import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

# CLUSTER 1: LENGTH & DISTANCE MEASUREMENT & ESTIMATION (12 Archetypes)
# ==============================================================================

def _gen_meas_len_est_body_parts(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    benchmarks = [
        ("the width of a standard doorway", "outstretched arm from shoulder to fingertips", 1.0, "1 metre (1 m)", ["10 cm", "1 metre (1 m)", "3 metres", "5 metres"]),
        ("the length of a classroom chalkboard", "adult paces (steps)", 4.0, "4 metres (4 m)", ["40 cm", "4 metres (4 m)", "14 metres", "40 metres"]),
        ("the width of a standard postage stamp", "thumb width", 2.0, "2 cm", ["2 mm", "2 cm", "20 cm", "2 m"]),
        ("the height of a classroom ceiling", "adult arm-spans", 3.0, "3 metres", ["30 cm", "1 metre", "3 metres", "10 metres"])
    ]
    item, part, approx_val, ans_str, options = r.choice(benchmarks)
    prompt = (
        f"{name} wants to quickly estimate {item} without a measuring tape and uses their {part} as a body benchmark.\n\n"
        f"Which of the following is the most reasonable estimate?"
    )
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• In Mathematical Literacy, body reference benchmarks provide useful everyday estimates:\n"
        f"  - Adult thumb width ≈ 1 cm to 2 cm\n"
        f"  - Outstretched arm (shoulder to fingertip) ≈ 1 m\n"
        f"  - One large adult pace (step) ≈ 1 m\n\n"
        f"**Step 2: Method Setup & Application**\n"
        f"• Applying the body benchmark to {item} yields an approximate measurement of **{ans_str}**.\n"
        f"✓ **[1 Mark: Method – applying correct body reference benchmark]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – selecting the correct realistic estimate]**"
    )
    return _make_q(
        subskill="meas_len_est_body_parts",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – correct body benchmark", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "1 large pace or an outstretched arm from shoulder to fingertips is roughly 1 metre.",
            "tier_2": f"Estimate the reasonable size of {item}.",
            "tier_3": f"The standard benchmark estimate is {ans_str}."
        },
        options=options,
        r=r
    )

def _gen_meas_len_instrument_selection(r: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("measuring the boundary perimeter of a full-sized school soccer field", "Trundle wheel", ["30 cm plastic ruler", "Sewing tape measure", "Trundle wheel", "Vernier caliper"]),
        ("measuring the waist and hip circumference for tailoring a matric dance dress", "Dressmaker's flexible tape measure", ["30 cm wooden ruler", "Dressmaker's flexible tape measure", "Trundle wheel", "Builder's steel tape"]),
        ("measuring the thickness of a single sheet of cardboard in art class", "Vernier caliper or 30 cm ruler with mm subdivisions", ["Odometer", "Trundle wheel", "5 m builder's tape measure", "Vernier caliper or 30 cm ruler with mm subdivisions"]),
        ("measuring the total driving distance travelled between Johannesburg and Durban", "Vehicle odometer", ["Trundle wheel", "10 m tape measure", "Vehicle odometer", "Meter stick"])
    ]
    task, correct_tool, opts = r.choice(scenarios)
    prompt = (
        f"A learner needs to select an appropriate instrument for: **{task}**.\n\n"
        f"Identify the most suitable measuring tool from the choices below."
    )
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The selection of a measuring instrument depends on the magnitude of the distance and whether the surface is curved or flat:\n"
        f"  - Millimetres / small objects: Ruler or caliper\n"
        f"  - Curved bodies / clothing: Flexible cloth tape measure\n"
        f"  - Large outdoor fields / tracks: Trundle wheel\n"
        f"  - Road travel distances (kilometres): Vehicle odometer\n\n"
        f"**Step 2: Evaluation of Options**\n"
        f"• For {task}, the instrument designed specifically for this purpose is the **{correct_tool}**.\n"
        f"✓ **[1 Mark: Method – evaluating appropriate scale and instrument modality]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{correct_tool}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct instrument identification]**"
    )
    return _make_q(
        subskill="meas_len_instrument_selection",
        prompt=prompt,
        answer=correct_tool,
        sol=sol,
        rubric=["1 Mark: Method – correct instrument rationale", f"1 Mark: Accuracy – {correct_tool}"],
        hints={
            "tier_1": "Consider whether the distance is small (mm/cm), flexible (curves), large outdoor (m), or vehicle (km).",
            "tier_2": f"Which tool is specifically designed for {task}?",
            "tier_3": f"Correct tool: {correct_tool}."
        },
        options=opts,
        r=r
    )

def _gen_meas_len_ruler_reading_subdivisions(r: random.Random) -> Dict[str, Any]:
    cm_base = r.randint(3, 14)
    mm_ticks = r.randint(1, 9)
    total_cm = round(cm_base + (mm_ticks / 10.0), 1)
    name = r.choice(SA_NAMES)
    items = ["an eraser", "a wooden dowel", "a pencil sharpener", "a strip of copper foil"]
    item = r.choice(items)
    prompt = (
        f"{name} measures the length of {item} using a standard centimetre ruler.\n\n"
        f"The item aligns with 0 cm at one end, and the other end reaches the **{cm_base} cm mark plus {mm_ticks} small millimetre subdivisions**.\n\n"
        f"Record the exact measurement in centimetres (**cm**)."
    )
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• On a standard 30 cm school ruler, 1 centimetre is divided into 10 equal millimetre intervals.\n"
        f"• Each small subdivision represents $0{{,}}1\\text{{ cm}}$ (or $1\\text{{ mm}}$).\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total length}} = {cm_base}\\text{{ cm}} + ({mm_ticks} \\times 0{{,}}1\\text{{ cm}}) = {cm_base} + {_fmt(round(mm_ticks * 0.1, 1))}\\text{{ cm}} = {_fmt(total_cm)}\\text{{ cm}}$$\n"
        f"✓ **[1 Mark: Method – interpreting mm subdivisions as tenths of a centimetre]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(total_cm)}\\text{{ cm}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct decimal measurement]**"
    )
    return _make_q(
        subskill="meas_len_ruler_reading_subdivisions",
        prompt=prompt,
        answer=f"{_fmt(total_cm)} cm",
        sol=sol,
        rubric=["1 Mark: Method – reading tenths of a cm", f"1 Mark: Accuracy – {_fmt(total_cm)} cm"],
        hints={
            "tier_1": "Each small tick mark on a centimetre ruler represents 0,1 cm (1 mm).",
            "tier_2": f"Add {mm_ticks} mm (0,{mm_ticks} cm) to {cm_base} cm.",
            "tier_3": f"{cm_base} + 0,{mm_ticks} = {_fmt(total_cm)} cm."
        },
        r=r
    )

def _gen_meas_len_tape_measure_furniture(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    width_mm = r.choice([750, 780, 820, 850, 890])
    width_cm = width_mm / 10.0
    door_cm = r.choice([80, 85, 90])
    fits = width_cm <= door_cm
    item = r.choice(["a new washing machine", "a double-door refrigerator", "a wardrobe unit", "a chest of drawers"])
    prompt = (
        f"{name} uses a steel tape measure to check the dimensions of {item}. "
        f"The tape shows a width of **{width_mm} mm**.\n\n"
        f"Convert this width to centimetres (**cm**) and determine if it can pass through a doorway of width **{door_cm} cm**."
    )
    ans_text = f"{_fmt(width_cm)} cm ({'Passes through' if fits else 'Does not fit'})"
    wrong_pass = f"{_fmt(width_cm)} cm ({'Does not fit' if fits else 'Passes through'})"
    wrong_conv1 = f"{_fmt(width_mm / 100.0)} cm ({'Passes through' if fits else 'Does not fit'})"
    wrong_conv2 = f"{width_mm * 10} cm ({'Passes through' if fits else 'Does not fit'})"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To convert from millimetres (mm) to centimetres (cm), divide by 10 (since $1\\text{{ cm}} = 10\\text{{ mm}}$).\n"
        f"• Compare the converted width against the doorway clearance width ({door_cm} cm).\n\n"
        f"**Step 2: Method Setup & Comparison**\n"
        f"$$\\text{{Width in cm}} = \\frac{{{width_mm}}}{{10}} = {_fmt(width_cm)}\\text{{ cm}}$$\n"
        f"• Comparison: {_fmt(width_cm)} cm {'≤' if fits else '>'} {door_cm} cm $\\implies$ **{'Passes through' if fits else 'Does not fit'}**.\n"
        f"✓ **[1 Mark: Method – dividing mm by 10 and comparing to clearance]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_text}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct converted value and clearance conclusion]**"
    )
    return _make_q(
        subskill="meas_len_tape_measure_furniture",
        prompt=prompt,
        answer=ans_text,
        sol=sol,
        rubric=["1 Mark: Method – convert mm to cm and compare", f"1 Mark: Accuracy – {ans_text}"],
        hints={
            "tier_1": "Divide millimetres by 10 to obtain centimetres.",
            "tier_2": f"{width_mm} ÷ 10 = {_fmt(width_cm)} cm. Check if {_fmt(width_cm)} <= {door_cm}.",
            "tier_3": f"Result: {ans_text}."
        },
        options=[ans_text, wrong_pass, wrong_conv1, wrong_conv2],
        r=r
    )

def _gen_meas_len_trundle_wheel_sports_field(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    clicks = r.randint(45, 120)
    meters = clicks * 1  # 1 click = 1 circumference revolution = 1 m
    context = r.choice([
        "the boundary of a school sports athletics sprint track",
        "a commercial tomato planting strip on an agricultural smallholding",
        "a row of maize and bean crops on a community farm",
        "the perimeter of a school soccer field"
    ])
    prompt = (
        f"{name} uses a trundle wheel to measure the length of {context}. "
        f"The trundle wheel has a circumference of 1 metre and makes an audible click each time the wheel completes one full revolution ($1\\text{{ metre}}$).\n\n"
        f"If the trundle wheel clicks **{clicks} times**, calculate the total distance measured in metres (**m**)."
    )
    ans_m = f"{clicks} m"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• A standard educational trundle wheel has a circumference of exactly $1\\text{{ metre}}$.\n"
        f"• Each complete revolution (click) corresponds to $1\\text{{ m}}$ of ground distance.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total distance}} = {clicks}\\text{{ clicks}} \\times 1\\text{{ m/click}} = {clicks}\\text{{ m}}$$\n"
        f"✓ **[1 Mark: Method – multiplying clicks by 1 metre per revolution]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{clicks}\\text{{ m}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct distance in metres]**"
    )
    return _make_q(
        subskill="meas_len_trundle_wheel_sports_field",
        prompt=prompt,
        answer=ans_m,
        sol=sol,
        rubric=["1 Mark: Method – 1 click = 1 m", f"1 Mark: Accuracy – {ans_m}"],
        hints={
            "tier_1": "Each revolution or click of a trundle wheel equals 1 metre.",
            "tier_2": f"Multiply {clicks} clicks by 1 m.",
            "tier_3": f"{clicks} clicks = {clicks} m."
        },
        r=r
    )

def _gen_meas_len_odometer_reading_trip(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    start_km = r.randint(35000, 85000)
    trip_km = r.randint(120, 680)
    end_km = start_km + trip_km
    route = r.choice(["Durban to Richards Bay", "Polokwane to Pretoria", "Bloemfontein to Kimberley", "Cape Town to Hermanus"])
    prompt = (
        f"{name} drives from {route}. Before departing, the vehicle's odometer displays **{_fmt(start_km)} km**. "
        f"Upon arriving at the destination, the odometer displays **{_fmt(end_km)} km**.\n\n"
        f"Calculate the total journey distance in kilometres (**km**)."
    )
    ans_str = f"{_fmt(trip_km)} km"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• A vehicle odometer records total cumulative distance travelled.\n"
        f"• The distance of an individual trip is found by subtracting the starting reading from the final reading:\n"
        f"  $$\\text{{Trip Distance}} = \\text{{Final Reading}} - \\text{{Starting Reading}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Trip Distance}} = {_fmt(end_km)}\\text{{ km}} - {_fmt(start_km)}\\text{{ km}} = {_fmt(trip_km)}\\text{{ km}}$$\n"
        f"✓ **[1 Mark: Method – subtracting starting odometer from ending odometer]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(trip_km)}\\text{{ km}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct journey distance]**"
    )
    return _make_q(
        subskill="meas_len_odometer_reading_trip",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – subtraction of odometer values", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Trip distance = Ending odometer reading - Starting odometer reading.",
            "tier_2": f"Subtract {_fmt(start_km)} from {_fmt(end_km)}.",
            "tier_3": f"{_fmt(end_km)} - {_fmt(start_km)} = {_fmt(trip_km)} km."
        },
        r=r
    )

def _gen_meas_len_cost_per_metre_fabric(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    actual_width = round(r.choice([1.8, 2.2, 2.6, 3.1, 3.4]), 1)
    price_per_m = r.choice([45.00, 55.00, 65.00, 75.00, 89.50])
    metres_to_buy = math.ceil(actual_width)
    total_cost = metres_to_buy * price_per_m
    mat_type = r.choice([
        ("curtain material for bedroom windows", "curtains"),
        ("80% UV-block agricultural shade cloth netting to protect tomato seedlings in a nursery tunnel", "shade cloth"),
    ])
    prompt = (
        f"{name} measures a required width of **{_fmt(actual_width)} m** for {mat_type[0]}. "
        f"The supplier sells this material at **{_fmt_curr(price_per_m)} per metre**, and it is sold **only in full metre units**.\n\n"
        f"1. How many metres of material must {name} buy?\n"
        f"2. Calculate the total cost of the material."
    )
    ans_str = f"{metres_to_buy} m ({_fmt_curr(total_cost)})"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The required width is {_fmt(actual_width)} m. Because material is sold only in whole metre units, the quantity must be rounded UP to the next whole metre:\n"
        f"  $$\\lceil {_fmt(actual_width)} \\rceil = {metres_to_buy}\\text{{ metres}}$$\n\n"
        f"**Step 2: Method Setup & Cost Calculation**\n"
        f"$$\\text{{Total Cost}} = {metres_to_buy}\\text{{ m}} \\times \\text{{{_fmt_curr(price_per_m)}}} = \\text{{{_fmt_curr(total_cost)}}}$\n"
        f"✓ **[1 Mark: Method – rounding up to whole metres and multiplying by unit price]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{metres_to_buy}\\text{{ m}} \\ (\\text{{{_fmt_curr(total_cost)}}})}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct metres and total price]**"
    )
    opts = [
        f"{metres_to_buy} m ({_fmt_curr(total_cost)})",
        f"{metres_to_buy + 1} m ({_fmt_curr((metres_to_buy + 1) * price_per_m)})",
        f"{max(1, metres_to_buy - 1)} m ({_fmt_curr(max(1, metres_to_buy - 1) * price_per_m)})",
        f"{metres_to_buy + 2} m ({_fmt_curr((metres_to_buy + 2) * price_per_m)})"
    ]
    return _make_q(
        subskill="meas_len_cost_per_metre_fabric",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – rounding up and multiplying", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "You cannot buy a fraction of a metre; round up to the next whole metre.",
            "tier_2": f"Round {_fmt(actual_width)} m up to {metres_to_buy} m, then multiply by {_fmt_curr(price_per_m)}.",
            "tier_3": f"{metres_to_buy} × {_fmt_curr(price_per_m)} = {_fmt_curr(total_cost)}."
        },
        options=opts,
        r=r
    )

def _gen_meas_len_cost_ribbon_binding(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    items_count = r.choice([2, 3, 4, 5])
    m_per_item = r.choice([2.5, 3.0, 3.5, 4.0])
    roll_len = 5  # rolls of 5 m
    price_per_roll = r.choice([15.50, 18.00, 22.50, 25.00])
    total_m_needed = round(items_count * m_per_item, 1)
    rolls_to_buy = math.ceil(total_m_needed / roll_len)
    total_cost = rolls_to_buy * price_per_roll
    prompt = (
        f"{name} is sewing **{items_count} traditional aprons**. Each apron requires **{_fmt(m_per_item)} m** of decorative ribbon binding. "
        f"Ribbon is sold in rolls of **{roll_len} metres** at **{_fmt_curr(price_per_roll)} per roll**.\n\n"
        f"Calculate the total number of rolls {name} must purchase and the total cost."
    )
    ans_str = f"{rolls_to_buy} rolls ({_fmt_curr(total_cost)})"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• First find total metres required: ${items_count} \\times {_fmt(m_per_item)}\\text{{ m}} = {_fmt(total_m_needed)}\\text{{ m}}$.\n"
        f"• Determine rolls needed by dividing by roll length ({roll_len} m) and rounding UP to the nearest whole roll.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Rolls required}} = \\frac{{{_fmt(total_m_needed)}}}{{{roll_len}}} = {_fmt(round(total_m_needed / roll_len, 2))} \\implies {rolls_to_buy}\\text{{ rolls}}$$\n"
        f"$$\\text{{Total cost}} = {rolls_to_buy} \\times \\text{{{_fmt_curr(price_per_roll)}}} = \\text{{{_fmt_curr(total_cost)}}}$\n"
        f"✓ **[1 Mark: Method – dividing total length by roll size, rounding up, and multiplying]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{rolls_to_buy}\\text{{ rolls}} \\ (\\text{{{_fmt_curr(total_cost)}}})}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct rolls and total cost]**"
    )
    opts = [
        f"{rolls_to_buy} rolls ({_fmt_curr(total_cost)})",
        f"{rolls_to_buy + 1} rolls ({_fmt_curr((rolls_to_buy + 1) * price_per_roll)})",
        f"{max(1, rolls_to_buy - 1)} rolls ({_fmt_curr(max(1, rolls_to_buy - 1) * price_per_roll)})",
        f"{rolls_to_buy + 2} rolls ({_fmt_curr((rolls_to_buy + 2) * price_per_roll)})"
    ]
    return _make_q(
        subskill="meas_len_cost_ribbon_binding",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total length ÷ roll length, round up", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Calculate total metres: {items_count} × {_fmt(m_per_item)} m = {_fmt(total_m_needed)} m.",
            "tier_2": f"Divide {_fmt(total_m_needed)} by {roll_len} m and round up to whole rolls.",
            "tier_3": f"{rolls_to_buy} rolls × {_fmt_curr(price_per_roll)} = {_fmt_curr(total_cost)}."
        },
        options=opts,
        r=r
    )

def _gen_meas_len_fencing_perimeter_wire(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    length = r.randint(12, 35)
    width = r.randint(8, 20)
    strands = r.choice([3, 4, 5])
    perimeter = 2 * (length + width)
    total_wire = perimeter * strands
    plot_type = r.choice([
        "an open-field tomato and spinach vegetable plot",
        "a free-range poultry run (chicken coop) to protect hens from predators",
        "a community vegetable garden growing tomatoes and cabbages",
        "a smallholding chicken broiler run"
    ])
    prompt = (
        f"{name} encloses a rectangular {plot_type} of length **{length} m** and width **{width} m**. "
        f"The protective boundary fence consists of **{strands} horizontal strands of galvanized wire** around the entire perimeter.\n\n"
        f"Calculate the total length of fencing wire required in metres (**m**)."
    )
    ans_str = f"{total_wire} m"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The perimeter of a rectangle is the distance all the way around:\n"
        f"  $$\\text{{Perimeter}} = 2 \\times (\\text{{length}} + \\text{{width}}) = 2 \\times ({length} + {width}) = 2 \\times {length + width} = {perimeter}\\text{{ m}}$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"• Because there are {strands} strands of wire around the entire perimeter:\n"
        f"  $$\\text{{Total wire}} = {perimeter}\\text{{ m}} \\times {strands} = {total_wire}\\text{{ m}}$$\n"
        f"✓ **[1 Mark: Method – calculating perimeter and multiplying by number of strands]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{total_wire}\\text{{ m}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total metres of wire]**"
    )
    return _make_q(
        subskill="meas_len_fencing_perimeter_wire",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 2(L+W) × strands", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Perimeter = 2 × (Length + Width) = 2 × ({length} + {width}) = {perimeter} m.",
            "tier_2": f"Multiply the perimeter ({perimeter} m) by {strands} strands.",
            "tier_3": f"{perimeter} × {strands} = {total_wire} m."
        },
        r=r
    )

def _gen_meas_len_fencing_poles_spacing(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    spacing = r.choice([2, 3, 4])
    intervals = r.randint(6, 15)
    boundary_len = spacing * intervals
    posts_needed = intervals + 1  # includes post at start and end
    fence_context = r.choice([
        "along the boundary of a free-range poultry chicken run",
        "around a commercial tomato growing patch",
        "along the boundary of a farm vegetable garden",
        "for an agricultural livestock holding paddock"
    ])
    prompt = (
        f"{name} erects a straight boundary fence {fence_context} measuring **{boundary_len} m** in length. "
        f"Treated wooden fence posts must be placed at intervals of **{spacing} m**, with a post placed at the very beginning and at the very end of the fence line.\n\n"
        f"How many wooden fence posts will be needed in total?"
    )
    ans_str = f"{posts_needed} posts"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• To find the number of intervals along a straight line, divide total length by post spacing:\n"
        f"  $$\\text{{Intervals}} = \\frac{{{boundary_len}\\text{{ m}}}}{{{spacing}\\text{{ m}}}} = {intervals}$$\n"
        f"• When posts are placed at both the beginning and the end, the total number of posts is always:\n"
        f"  $$\\text{{Total posts}} = \\text{{Intervals}} + 1$$\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Total posts}} = {intervals} + 1 = {posts_needed}\\text{{ posts}}$$\n"
        f"✓ **[1 Mark: Method – dividing total length by spacing and adding 1 for the end post]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{posts_needed}\\text{{ posts}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct number of fence posts]**"
    )
    return _make_q(
        subskill="meas_len_fencing_poles_spacing",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (length ÷ spacing) + 1", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide total length by spacing: {boundary_len} ÷ {spacing} = {intervals} intervals.",
            "tier_2": "Add 1 to include the initial post at the start of the fence.",
            "tier_3": f"{intervals} + 1 = {posts_needed} posts."
        },
        r=r
    )

def _gen_meas_len_timber_planks_cutting_wastage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    plank_len_m = 2.4
    plank_len_cm = 240
    shelf_len_cm = r.choice([40, 50, 60, 70])
    shelves_cut = plank_len_cm // shelf_len_cm
    wastage_cm = plank_len_cm % shelf_len_cm
    prompt = (
        f"{name} is building shelving and buys a standard timber plank of length **{_fmt(plank_len_m)} m** ({plank_len_cm} cm). "
        f"Each bookshelf requires a cut length of **{shelf_len_cm} cm**.\n\n"
        f"1. How many complete shelves can {name} cut from one plank?\n"
        f"2. How many centimetres of offcut wood (wastage) will remain?"
    )
    ans_str = f"{shelves_cut} shelves ({wastage_cm} cm wastage)"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• Convert or use consistent units: Plank length = ${plank_len_cm}\\text{{ cm}}$.\n"
        f"• Use integer division to determine complete shelves, and the remainder represents offcut wastage.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Shelves}} = \\lfloor \\frac{{{plank_len_cm}}}{{{shelf_len_cm}}} \\rfloor = {shelves_cut}\\text{{ complete shelves}}$$\n"
        f"$$\\text{{Wastage}} = {plank_len_cm} - ({shelves_cut} \\times {shelf_len_cm}) = {plank_len_cm} - {shelves_cut * shelf_len_cm} = {wastage_cm}\\text{{ cm}}$$\n"
        f"✓ **[1 Mark: Method – integer division and remainder calculation]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{shelves_cut}\\text{{ shelves}} \\ (\\text{{{wastage_cm} cm wastage}})}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct shelves count and offcut wastage]**"
    )
    d_spec = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "length": plank_len_cm,
        "width": shelf_len_cm,
        "shape": "timber_plank",
        "title": f"Timber Plank Cutting Plan ({plank_len_cm} cm)",
    }
    return _make_q(
        diagram_spec=d_spec,
        subskill="meas_len_timber_planks_cutting_wastage",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – 240 ÷ shelf length with remainder", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Divide {plank_len_cm} cm by {shelf_len_cm} cm using integer division.",
            "tier_2": f"{plank_len_cm} ÷ {shelf_len_cm} = {shelves_cut} with remainder {wastage_cm}.",
            "tier_3": f"Result: {ans_str}."
        },
        r=r
    )

def _gen_meas_len_tablecloth_overhang(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    table_l = round(r.choice([1.6, 1.8, 2.0, 2.2]), 1)
    table_w = round(r.choice([0.9, 1.0, 1.1]), 1)
    overhang_cm = r.choice([20, 25, 30])
    overhang_m = overhang_cm / 100.0
    cloth_l = round(table_l + (2 * overhang_m), 2)
    cloth_w = round(table_w + (2 * overhang_m), 2)
    prompt = (
        f"{name} is sewing a custom rectangular tablecloth for a dining table measuring **{_fmt(table_l)} m in length** and **{_fmt(table_w)} m in width**. "
        f"The design requires an overhang of **{overhang_cm} cm** ({_fmt(overhang_m)} m) along **all four sides** of the table.\n\n"
        f"Calculate the required length and width of the finished tablecloth in metres (**m**)."
    )
    ans_str = f"{_fmt(cloth_l)} m by {_fmt(cloth_w)} m"
    sol = (
        f"**Step 1: Measurement Principle & Thought Process**\n"
        f"• The tablecloth overhangs on BOTH ends of the length and BOTH ends of the width.\n"
        f"• Therefore, add twice the overhang ($2 \\times {_fmt(overhang_m)}\\text{{ m}} = {_fmt(round(2 * overhang_m, 2))}\\text{{ m}}$) to both the table length and table width.\n\n"
        f"**Step 2: Method Setup & Calculation**\n"
        f"$$\\text{{Tablecloth Length}} = {_fmt(table_l)} + (2 \\times {_fmt(overhang_m)}) = {_fmt(table_l)} + {_fmt(round(2 * overhang_m, 2))} = {_fmt(cloth_l)}\\text{{ m}}$$\n"
        f"$$\\text{{Tablecloth Width}} = {_fmt(table_w)} + (2 \\times {_fmt(overhang_m)}) = {_fmt(table_w)} + {_fmt(round(2 * overhang_m, 2))} = {_fmt(cloth_w)}\\text{{ m}}$$\n"
        f"✓ **[1 Mark: Method – adding 2 × overhang to both dimensions]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{_fmt(cloth_l)}\\text{{ m by }} {_fmt(cloth_w)}\\text{{ m}}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct tablecloth length and width]**"
    )
    return _make_q(
        subskill="meas_len_tablecloth_overhang",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – adding overhang to both sides", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Remember to add {overhang_cm} cm ({_fmt(overhang_m)} m) to BOTH sides (2 × {_fmt(overhang_m)} = {_fmt(round(2 * overhang_m, 2))} m).",
            "tier_2": f"Length = {_fmt(table_l)} + {_fmt(round(2 * overhang_m, 2))} m; Width = {_fmt(table_w)} + {_fmt(round(2 * overhang_m, 2))} m.",
            "tier_3": f"Result: {ans_str}."
        },
        r=r
    )

# ==============================================================================
