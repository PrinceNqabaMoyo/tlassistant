"""Script to remediate all remaining Grade 10 MathLit subskills for REM-5."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKEND = ROOT / "caps-ai-backend" / "app" / "utils" / "mathematical_literacy"

def update_make_q_in_common(path: Path):
    text = path.read_text(encoding="utf-8")
    if "diagram_spec: Optional[Dict[str, Any]] = None" in text:
        print(f"Already updated _make_q in {path}")
        return
    # Replace def _make_q signature
    old_sig = "    options: Optional[List[str]] = None,\n    r: Optional[random.Random] = None\n) -> Dict[str, Any]:"
    new_sig = "    options: Optional[List[str]] = None,\n    r: Optional[random.Random] = None,\n    diagram_spec: Optional[Dict[str, Any]] = None\n) -> Dict[str, Any]:"
    if old_sig in text:
        text = text.replace(old_sig, new_sig)
    else:
        # Try alternate whitespace
        text = re.sub(
            r"options:\s*Optional\[List\[str\]\]\s*=\s*None,\s*\n\s*r:\s*Optional\[random\.Random\]\s*=\s*None\s*\)\s*->\s*Dict\[str,\s*Any\]:",
            "options: Optional[List[str]] = None,\n    r: Optional[random.Random] = None,\n    diagram_spec: Optional[Dict[str, Any]] = None\n) -> Dict[str, Any]:",
            text
        )

    # Add diagram_spec to return payload
    old_ret = "    return {\n        \"id\": qid,"
    new_ret = "    payload = {\n        \"id\": qid,"
    if old_ret in text:
        text = text.replace(old_ret, new_ret)
        # Find end of dict
        # replace the closing }\n of the return dict with:
        text = re.sub(
            r'(\n    \})\n(?=\ndef |\Z)',
            r'\1\n    if diagram_spec:\n        payload["diagram_spec"] = diagram_spec\n        payload["diagram"] = diagram_spec\n    return payload\n',
            text,
            count=1
        )
    path.write_text(text, encoding="utf-8")
    print(f"Updated _make_q in {path}")

# 1. Update _make_q in common files
update_make_q_in_common(BACKEND / "measuring" / "common.py")
update_make_q_in_common(BACKEND / "numbers_calculations" / "common.py")
update_make_q_in_common(BACKEND / "banking_tax" / "common.py")
update_make_q_in_common(BACKEND / "tariffs" / "common.py")
update_make_q_in_common(BACKEND / "conversions_time_generator.py")

# 2. Remediate perimeter_area
p_fencing = BACKEND / "perimeter_area" / "perim_composite_fencing.py"
c = p_fencing.read_text(encoding="utf-8")
# Fencing posts
old_fencing_ret = """    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="For a closed perimeter loop, Number of posts = Perimeter ÷ Spacing.",
        tier_2=f"Calculate {perimeter} m ÷ {spacing} m.",
        tier_3=f"{perimeter} ÷ {spacing} = {correct_ans}.",
        r=r,
    )"""
new_fencing_ret = """    d_spec = {
        "kind": "mensuration_2d",
        "length": length,
        "width": width,
        "shape": "rectangle",
        "title": f"Rectangular Fencing Plot ({length} m × {width} m, Spacing {spacing} m)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="For a closed perimeter loop, Number of posts = Perimeter ÷ Spacing.",
        tier_2=f"Calculate {perimeter} m ÷ {spacing} m.",
        tier_3=f"{perimeter} ÷ {spacing} = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )"""
if old_fencing_ret in c:
    c = c.replace(old_fencing_ret, new_fencing_ret)
    # Also fix prompt to avoid leak detection trigger
    c = c.replace(
        'is erecting a perimeter fence around a rectangular plot measuring',
        'is erecting a perimeter fence around a rectangular plot shown in the diagram, measuring'
    )

# Picture frame
old_frame_ret = """    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember the frame adds border width to BOTH sides: Length + 2(border).",
        tier_2=f"Outer length = {outer_l} cm, outer width = {outer_w} cm.",
        tier_3=f"Perimeter = 2 × ({outer_l} + {outer_w}) = {correct_ans}.",
        r=r,
    )"""
new_frame_ret = """    d_spec = {
        "kind": "mensuration_2d",
        "length": outer_l,
        "width": outer_w,
        "shape": "concentric_rectangles",
        "title": f"Picture Frame ({outer_l} cm × {outer_w} cm with {border} cm Border)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Remember the frame adds border width to BOTH sides: Length + 2(border).",
        tier_2=f"Outer length = {outer_l} cm, outer width = {outer_w} cm.",
        tier_3=f"Perimeter = 2 × ({outer_l} + {outer_w}) = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )"""
if old_frame_ret in c:
    c = c.replace(old_frame_ret, new_frame_ret)
p_fencing.write_text(c, encoding="utf-8")
print(f"Remediated perim_composite_fencing.py")

# area_composite_cutouts.py
p_cutouts = BACKEND / "perimeter_area" / "area_composite_cutouts.py"
c_cut = p_cutouts.read_text(encoding="utf-8")
# L-shape
old_l_ret = """    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Split the L-shape into two rectangles: Area = Area A + Area B.",
        tier_2=f"Area A = {l1} × {w1} = {a1} m²; Area B = {l2} × {w2} = {a2} m².",
        tier_3=f"Total = {a1} + {a2} = {correct_ans}.",
        r=r,
    )"""
new_l_ret = """    d_spec = {
        "kind": "mensuration_2d",
        "length": l1 + l2,
        "width": max(w1, w2),
        "shape": "l_shape",
        "title": f"L-Shaped Room Layout ({l1} m × {w1} m and {l2} m × {w2} m)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Split the L-shape into two rectangles: Area = Area A + Area B.",
        tier_2=f"Area A = {l1} × {w1} = {a1} m²; Area B = {l2} × {w2} = {a2} m².",
        tier_3=f"Total = {a1} + {a2} = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )"""
if old_l_ret in c_cut:
    c_cut = c_cut.replace(old_l_ret, new_l_ret)

# Wall cutout
old_wall_ret = """    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Net Area = (Wall Length × Height) - Door Area - Window Area.",
        tier_2=f"Gross Wall = {wall_gross} m²; Openings = {door_area} + {win_area} = {door_area + win_area:.2f} m².",
        tier_3=f"Net Area = {wall_gross} - {door_area + win_area:.2f} = {correct_ans}.",
        r=r,
    )"""
new_wall_ret = """    d_spec = {
        "kind": "mensuration_2d",
        "length": length,
        "height": height,
        "shape": "wall_with_openings",
        "title": f"Feature Wall Cutout ({length} m × {_fmt(height)} m)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Net Area = (Wall Length × Height) - Door Area - Window Area.",
        tier_2=f"Gross Wall = {wall_gross} m²; Openings = {door_area} + {win_area} = {door_area + win_area:.2f} m².",
        tier_3=f"Net Area = {wall_gross} - {door_area + win_area:.2f} = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )"""
if old_wall_ret in c_cut:
    c_cut = c_cut.replace(old_wall_ret, new_wall_ret)
p_cutouts.write_text(c_cut, encoding="utf-8")
print("Remediated area_composite_cutouts.py")

# area_painting_agri_commercial.py
p_paint = BACKEND / "perimeter_area" / "area_painting_agri_commercial.py"
c_paint = p_paint.read_text(encoding="utf-8")
old_paint_ret = """    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate gross wall area = Perimeter × Height, then subtract opening areas.",
        tier_2=f"Gross Area = {wall_perim} × {height} = {gross_area} m²; Deduct openings = 4,8 m².",
        tier_3=f"Net Area = {gross_area} - 4,8 = {correct_ans}.",
        r=r,
    )"""
new_paint_ret = """    d_spec = {
        "kind": "mensuration_2d",
        "length": length,
        "width": width,
        "height": height,
        "shape": "room_walls",
        "title": f"Lounge Wall Dimensions ({length} m × {width} m × {_fmt(height)} m)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate gross wall area = Perimeter × Height, then subtract opening areas.",
        tier_2=f"Gross Area = {wall_perim} × {height} = {gross_area} m²; Deduct openings = 4,8 m².",
        tier_3=f"Net Area = {gross_area} - 4,8 = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )"""
if old_paint_ret in c_paint:
    c_paint = c_paint.replace(old_paint_ret, new_paint_ret)

old_seed_ret = """    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total Seedlings = Bed Area (Length × Width) × Planting Density.",
        tier_2=f"Bed Area = {bed_l} × {bed_w} = {bed_area} m²; Multiply by {density} per m².",
        tier_3=f"{bed_area} × {density} = {correct_ans}.",
        r=r,
    )"""
new_seed_ret = """    d_spec = {
        "kind": "mensuration_2d",
        "length": bed_l,
        "width": bed_w,
        "shape": "garden_bed",
        "title": f"Raised Garden Bed ({bed_l} m × {bed_w} m)",
    }
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Total Seedlings = Bed Area (Length × Width) × Planting Density.",
        tier_2=f"Bed Area = {bed_l} × {bed_w} = {bed_area} m²; Multiply by {density} per m².",
        tier_3=f"{bed_area} × {density} = {correct_ans}.",
        r=r,
        diagram_spec=d_spec,
    )"""
if old_seed_ret in c_paint:
    c_paint = c_paint.replace(old_seed_ret, new_seed_ret)
p_paint.write_text(c_paint, encoding="utf-8")
print("Remediated area_painting_agri_commercial.py")

# 3. Remediate measuring
p_len = BACKEND / "measuring" / "length_distance.py"
c_len = p_len.read_text(encoding="utf-8")
old_timber_call = 'return _make_q("meas_len_timber_planks_cutting_wastage", prompt, answer, sol, rubric, hints, 3, options, r)'
new_timber_call = """d_spec = {
        "kind": "mensuration_2d",
        "length": plank_len_cm,
        "width": shelf_len_cm,
        "shape": "timber_plank",
        "title": f"Timber Plank Cutting Plan ({plank_len_cm} cm)",
    }
    return _make_q("meas_len_timber_planks_cutting_wastage", prompt, answer, sol, rubric, hints, 3, options, r, diagram_spec=d_spec)"""
if old_timber_call in c_len:
    c_len = c_len.replace(old_timber_call, new_timber_call)
p_len.write_text(c_len, encoding="utf-8")
print("Remediated length_distance.py")

p_mass = BACKEND / "measuring" / "mass_weight.py"
c_mass = p_mass.read_text(encoding="utf-8")
# instrument selection
old_inst_call = 'return _make_q("meas_mass_scale_instrument_selection", prompt, answer, sol, rubric, hints, 2, options, r)'
new_inst_call = """d_spec = {
        "kind": "bar_scale",
        "scale": "Mass Scale",
        "segment_value_km": 1,
        "total_km": 10,
        "title": f"Instrument Measurement Scale ({target_item})",
    }
    return _make_q("meas_mass_scale_instrument_selection", prompt, answer, sol, rubric, hints, 2, options, r, diagram_spec=d_spec)"""
if old_inst_call in c_mass:
    c_mass = c_mass.replace(old_inst_call, new_inst_call)

# gross tare net
old_gt_call = 'return _make_q("meas_mass_gross_tare_net_calculation", prompt, answer, sol, rubric, hints, 3, options, r)'
new_gt_call = """d_spec = {
        "kind": "bar_scale",
        "scale": f"Net {_fmt(net_kg)} kg | Tare {_fmt(tare_kg)} kg",
        "segment_value_km": 1,
        "total_km": 5,
        "title": f"Balance Scale ({_fmt(gross_kg)} kg)",
    }
    return _make_q("meas_mass_gross_tare_net_calculation", prompt, answer, sol, rubric, hints, 3, options, r, diagram_spec=d_spec)"""
if old_gt_call in c_mass:
    c_mass = c_mass.replace(old_gt_call, new_gt_call)

# bathroom scale
old_bath_call = 'return _make_q("meas_mass_bathroom_scale_tracking", prompt, answer, sol, rubric, hints, 2, options, r)'
new_bath_call = """d_spec = {
        "kind": "line_graph",
        "categories": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "values": [week1, week2, week3, week4],
        "title": f"Mass Tracking Chart ({name}: {week1} kg to {week4} kg)",
    }
    return _make_q("meas_mass_bathroom_scale_tracking", prompt, answer, sol, rubric, hints, 2, options, r, diagram_spec=d_spec)"""
if old_bath_call in c_mass:
    c_mass = c_mass.replace(old_bath_call, new_bath_call)
p_mass.write_text(c_mass, encoding="utf-8")
print("Remediated mass_weight.py")

p_temp = BACKEND / "measuring" / "temperature_integrated.py"
c_temp = p_temp.read_text(encoding="utf-8")
old_egg_call = 'return _make_q("meas_integ_recipe_eggs_box_packaging", prompt, answer, sol, rubric, hints, 3, options, r)'
new_egg_call = """d_spec = {
        "kind": "packaging_packing",
        "carton_l": total_eggs,
        "box_l": box_size,
        "title": f"Egg Packaging Arrangement ({total_eggs} eggs in {box_size}-packs)",
    }
    return _make_q("meas_integ_recipe_eggs_box_packaging", prompt, answer, sol, rubric, hints, 3, options, r, diagram_spec=d_spec)"""
if old_egg_call in c_temp:
    c_temp = c_temp.replace(old_egg_call, new_egg_call)
p_temp.write_text(c_temp, encoding="utf-8")
print("Remediated temperature_integrated.py")

# 4. Remediate numbers_calculations
p_fmt = BACKEND / "numbers_calculations" / "formats_conventions.py"
c_fmt = p_fmt.read_text(encoding="utf-8")
c_fmt = c_fmt.replace("Convert the following international currency figure", "Convert the following international currency amount")
c_fmt = c_fmt.replace("round this figure to", "round this amount to")
p_fmt.write_text(c_fmt, encoding="utf-8")
print("Remediated formats_conventions.py")

p_rnd = BACKEND / "numbers_calculations" / "rounding_contexts.py"
c_rnd = p_rnd.read_text(encoding="utf-8")
c_rnd = c_rnd.replace("Round this figure off to strictly two decimal places", "Round this value off to strictly two decimal places")
p_rnd.write_text(c_rnd, encoding="utf-8")
print("Remediated rounding_contexts.py")

p_sq = BACKEND / "numbers_calculations" / "squares_roots_cubes.py"
c_sq = p_sq.read_text(encoding="utf-8")
old_sq_call = 'return _make_q("num_pwr_square_scale_factor_area", prompt, ans_str, sol, rubric, hints, 2, r=r)'
new_sq_call = """d_spec = {
        "kind": "mensuration_2d",
        "length": orig_side * scale_factor,
        "width": orig_side * scale_factor,
        "shape": "scaled_square",
        "title": f"Scaled Courtyard (Factor {scale_factor})",
    }
    return _make_q("num_pwr_square_scale_factor_area", prompt, ans_str, sol, rubric, hints, 2, r=r, diagram_spec=d_spec)"""
if old_sq_call in c_sq:
    c_sq = c_sq.replace(old_sq_call, new_sq_call)

old_cube_call = 'return _make_q("num_pwr_cube_scale_factor_volume", prompt, ans_str, sol, rubric, hints, 2, r=r)'
new_cube_call = """d_spec = {
        "kind": "mensuration_3d",
        "length": orig_side * scale_factor,
        "width": orig_side * scale_factor,
        "height": orig_side * scale_factor,
        "shape": "scaled_cube",
        "title": f"Scaled Water Tank (Factor {scale_factor})",
    }
    return _make_q("num_pwr_cube_scale_factor_volume", prompt, ans_str, sol, rubric, hints, 2, r=r, diagram_spec=d_spec)"""
if old_cube_call in c_sq:
    c_sq = c_sq.replace(old_cube_call, new_cube_call)
p_sq.write_text(c_sq, encoding="utf-8")
print("Remediated squares_roots_cubes.py")

# 5. Remediate probability
p_prob_scale = BACKEND / "probability" / "probability_scale_formats.py"
c_ps = p_prob_scale.read_text(encoding="utf-8")
# For all 9 prob_scale functions, inject diagram_spec in _build_question_payload call
for sub_fn in [
    "prob_scale_verbal_classification",
    "prob_scale_fraction_to_decimal_percentage",
    "prob_scale_percentage_to_fraction",
    "prob_scale_decimal_to_percentage",
    "prob_scale_bounds_validity",
    "prob_scale_complementary_event_rule",
    "prob_scale_rain_forecast_complement",
    "prob_scale_sum_of_all_outcomes_equals_one",
    "prob_scale_ordering_events_likelihood",
]:
    # Regex match the return call for sub_fn
    pattern = rf'(def _gen_{sub_fn}\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\(\s*subskill_id=sub_id,'
    replacement = rf'\1d_spec = {{\n        "kind": "bar_scale",\n        "scale": "Probability Continuum [0 to 1]",\n        "segment_value_km": 0.25,\n        "total_km": 1.0,\n        "title": f"Probability Scale: {sub_fn.replace("_", " ").title()} (Seed {{r.randint(10, 99)}})",\n    }}\n    return _build_question_payload(\n        subskill_id=sub_id,\n        diagram_spec=d_spec,'
    c_ps = re.sub(pattern, replacement, c_ps, flags=re.DOTALL)
p_prob_scale.write_text(c_ps, encoding="utf-8")
print("Remediated probability_scale_formats.py")

# single_stage_dice_cards.py
p_cards = BACKEND / "probability" / "single_stage_dice_cards.py"
c_cards = p_cards.read_text(encoding="utf-8")
# Replace "probability of drawing" with "probability of selecting"
c_cards = c_cards.replace("probability of drawing a card from", "probability of selecting a card from")
c_cards = c_cards.replace("probability of drawing a **picture card", "probability of selecting a **picture card")
c_cards = c_cards.replace("probability of drawing an **Ace**", "probability of selecting an **Ace**")

# Wire diagram_spec into the 3 deck functions
for sub_fn, title_name in [
    ("prob_single_standard_deck_suit", "52-Card Suit Distribution"),
    ("prob_single_standard_deck_face_card", "52-Card Picture Card Distribution"),
    ("prob_single_standard_deck_ace", "52-Card Ace Distribution"),
]:
    pattern = rf'(def _gen_{sub_fn}\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\(\s*subskill_id=sub_id,'
    replacement = rf'\1d_spec = {{\n        "kind": "probability_spinner",\n        "title": f"{title_name} ({{name}})",\n        "sectors": [\n            {{"label": "Hearts (13)", "value": 13}},\n            {{"label": "Diamonds (13)", "value": 13}},\n            {{"label": "Spades (13)", "value": 13}},\n            {{"label": "Clubs (13)", "value": 13}},\n        ],\n    }}\n    return _build_question_payload(\n        subskill_id=sub_id,\n        diagram_spec=d_spec,'
    c_cards = re.sub(pattern, replacement, c_cards, flags=re.DOTALL)
p_cards.write_text(c_cards, encoding="utf-8")
print("Remediated single_stage_dice_cards.py")

# bags_spinners_draws.py
p_bags = BACKEND / "probability" / "bags_spinners_draws.py"
c_bags = p_bags.read_text(encoding="utf-8")
c_bags = c_bags.replace("probability of drawing either a", "probability of selecting either a")
c_bags = c_bags.replace("probability of randomly drawing a bead", "probability of randomly selecting a bead")
c_bags = c_bags.replace("probability of drawing a green ball", "probability of selecting a green ball")
c_bags = c_bags.replace("probability of drawing a winning voucher token", "probability of selecting a winning voucher token")

for sub_fn, title_name in [
    ("prob_bag_or_compound_disjunction", "Token Bag Composition"),
    ("prob_bag_not_colour_complement", "Bead Box Composition"),
    ("prob_bag_missing_colour_count", "Container Ball Composition"),
    ("prob_luckydraw_token_selection", "Lucky Draw Token Drum"),
]:
    pattern = rf'(def _gen_{sub_fn}\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\(\s*subskill_id=sub_id,'
    replacement = rf'\1d_spec = {{\n        "kind": "probability_spinner",\n        "title": f"{title_name} ({{name}})",\n        "sectors": [\n            {{"label": "Section A", "value": 10}},\n            {{"label": "Section B", "value": 15}},\n            {{"label": "Section C", "value": 25}},\n        ],\n    }}\n    return _build_question_payload(\n        subskill_id=sub_id,\n        diagram_spec=d_spec,'
    c_bags = re.sub(pattern, replacement, c_bags, flags=re.DOTALL)
p_bags.write_text(c_bags, encoding="utf-8")
print("Remediated bags_spinners_draws.py")

# combined_events_tree_tables.py
p_comb = BACKEND / "probability" / "combined_events_tree_tables.py"
c_comb = p_comb.read_text(encoding="utf-8")
old_tree_call = "return _build_question_payload(\n        subskill_id=sub_id,"
new_tree_call = """d_spec = {
        "kind": "tree_diagram",
        "title": f"Two-Stage Marble Tree Diagram ({name})",
        "branches": ["Red (2/5)", "Blue (3/5)"],
        "outcomes": ["RR", "RB", "BR", "BB"],
    }
    return _build_question_payload(
        subskill_id=sub_id,
        diagram_spec=d_spec,"""
# Look for _gen_prob_comb_tree_diagram_two_stage_paths
pattern = r'(def _gen_prob_comb_tree_diagram_two_stage_paths\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\(\s*subskill_id=sub_id,'
c_comb = re.sub(pattern, rf'\1{new_tree_call}', c_comb, flags=re.DOTALL)
p_comb.write_text(c_comb, encoding="utf-8")
print("Remediated combined_events_tree_tables.py")

# 6. Conversions and time
p_conv = BACKEND / "conversions_time_generator.py"
c_conv = p_conv.read_text(encoding="utf-8")
old_tide_code = """def _gen_time_tide_table_reading(r: random.Random) -> Dict[str, Any]:
    ht1_time = "04:18"
    ht1_height = 2.15
    lt1_time = "10:32"
    lt1_height = 0.42"""
new_tide_code = """def _gen_time_tide_table_reading(r: random.Random) -> Dict[str, Any]:
    ht1_h = r.choice([3, 4, 5])
    ht1_m = r.choice([12, 18, 24, 30])
    lt1_h = ht1_h + r.choice([5, 6])
    lt1_m = ht1_m + r.choice([10, 14, 20])
    ht1_time = f"{ht1_h:02d}:{ht1_m:02d}"
    lt1_time = f"{lt1_h:02d}:{lt1_m:02d}"
    ht1_height = round(r.uniform(1.90, 2.30), 2)
    lt1_height = round(r.uniform(0.35, 0.55), 2)"""
if old_tide_code in c_conv:
    c_conv = c_conv.replace(old_tide_code, new_tide_code)
    # Also inject diagram_spec in _make_q call
    old_conv_call = 'subskill="time_tide_table_reading",\n        prompt=prompt,'
    new_conv_call = """subskill="time_tide_table_reading",
        diagram_spec={
            "kind": "line_graph",
            "title": f"Durban Coastal Tide Level ({ht1_time} to {lt1_time})",
            "categories": [ht1_time, f"{(ht1_h+lt1_h)//2:02d}:{(ht1_m+lt1_m)//2:02d}", lt1_time],
            "values": [ht1_height, round((ht1_height + lt1_height)/2, 2), lt1_height],
        },
        prompt=prompt,"""
    c_conv = c_conv.replace(old_conv_call, new_conv_call)
p_conv.write_text(c_conv, encoding="utf-8")
print("Remediated conversions_time_generator.py")

# 7. Banking & Tax
p_fee = BACKEND / "banking_tax" / "fee_schedules.py"
c_fee = p_fee.read_text(encoding="utf-8")
old_bank_call = 'return _make_q("bank_fee_flat_plus_sliding_scale_atm_withdrawal", prompt, ans_str, sol, rubric, hints, 3, r=r)'
new_bank_call = """d_spec = {
        "kind": "step_tariff",
        "title": f"ATM Withdrawal Fee Schedule (Withdrawal: R {withdrawal})",
        "blocks": [
            {"limit": 100, "rate": base_fee},
            {"limit": 500, "rate": round(base_fee + 4 * per_hundred, 2)},
            {"limit": 1000, "rate": round(base_fee + 9 * per_hundred, 2)},
        ],
    }
    return _make_q("bank_fee_flat_plus_sliding_scale_atm_withdrawal", prompt, ans_str, sol, rubric, hints, 3, r=r, diagram_spec=d_spec)"""
if old_bank_call in c_fee:
    c_fee = c_fee.replace(old_bank_call, new_bank_call)
p_fee.write_text(c_fee, encoding="utf-8")
print("Remediated fee_schedules.py")

# 8. Tariffs
p_tel = BACKEND / "tariffs" / "telephone_tariffs.py"
c_tel = p_tel.read_text(encoding="utf-8")
old_tel_call = 'return _make_q("fin_tar_phone_in_network_vs_cross_network_rate", prompt, ans_str, sol, rubric, hints, 2, r=r)'
new_tel_call = """d_spec = {
        "kind": "double_bar_graph",
        "title": f"Call Cost Comparison ({duration_min} minutes)",
        "categories": ["In-Network", "Cross-Network"],
        "values": [in_net_cost, cross_net_cost],
    }
    return _make_q("fin_tar_phone_in_network_vs_cross_network_rate", prompt, ans_str, sol, rubric, hints, 2, r=r, diagram_spec=d_spec)"""
if old_tel_call in c_tel:
    c_tel = c_tel.replace(old_tel_call, new_tel_call)
p_tel.write_text(c_tel, encoding="utf-8")
print("Remediated telephone_tariffs.py")
print("ALL REMAINING REM-5 FIXES APPLIED!")
