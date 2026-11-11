"""Remediate all 30 missing subskills in gr12_plans_and_scale.
Attaches valid seeded diagram_spec and rewrites narrated prompt text.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# 1. determining_number_scale.py (subskills 01-08)
# ---------------------------------------------------------------------------
p_dns = "caps-ai-backend/app/utils/mathematical_literacy/gr12_plans_and_scale/determining_number_scale.py"
c_dns = open(p_dns, "r", encoding="utf-8").read()

# Subskill 01
old_01 = '''    prompt = (
        f"A learner measures the length of an external cottage wall on a printed architectural plan using a plastic ruler.\\n"
        f"The measurement on the plan is {_fmt(measured_cm, 1)} cm.\\n"
        f"The actual real-life length of the wall on site is {_fmt(real_m, 1)} m.\\n\\n"
        f"Calculate the scale of the plan in the standard ratio format 1 : x."
    )'''
new_01 = '''    prompt = (
        f"Refer to the cottage plan measurement shown in the diagram. "
        f"The external wall measures {_fmt(measured_cm, 1)} cm on paper, "
        f"while the actual real-life length on site is {_fmt(real_m, 1)} m.\\n\\n"
        f"Calculate the scale of the plan in the standard ratio format 1 : x."
    )
    d_spec_01 = {
        "kind": "mensuration_2d",
        "title": f"Cottage Wall Plan Measurement ({_fmt(measured_cm, 1)} cm)",
        "shape": "rectangle",
        "width": measured_cm * 10,
        "height": 20,
        "labels": {"width": f"{_fmt(measured_cm, 1)} cm", "real": f"Actual {_fmt(real_m, 1)} m"},
    }'''

assert old_01 in c_dns, "old_01 not found"
c_dns = c_dns.replace(old_01, new_01)
c_dns = c_dns.replace('difficulty="easy",\n    )', 'difficulty="easy",\n        diagram_spec=d_spec_01,\n    )', 1)

# Subskill 02
old_02 = '''    prompt = (
        f"On a South elevation plan of a house, the vertical height of the roof from eaves to ridge is measured "
        f"with a ruler as exactly {_fmt(measured_cm, 1)} cm.\\n"
        f"The actual construction dimension marked in the builder's specification is {_fmt(real_m, 2)} m.\\n\\n"
        f"Calculate the exact ratio scale (rounded to one decimal place), and state the nearest standard architectural scale."
    )'''
new_02 = '''    measured_cm = r.choice([2.5, 2.9, 3.2, 3.5])
    real_m = r.choice([3.20, 3.53, 3.80, 4.20])
    real_cm = real_m * 100.0
    exact_ratio = real_cm / measured_cm
    rounded_scale = 100 if exact_ratio < 110 else (120 if exact_ratio < 135 else 150)

    prompt = (
        f"Refer to the South elevation plan shown in the diagram. The vertical height of the roof from eaves to ridge "
        f"measures exactly {_fmt(measured_cm, 1)} cm with a ruler on the drawing, "
        f"while the actual construction dimension is {_fmt(real_m, 2)} m.\\n\\n"
        f"Calculate the exact ratio scale (rounded to one decimal place), and state the nearest standard architectural scale."
    )
    d_spec_02 = {
        "kind": "elevation_view",
        "title": f"South Elevation Roof Ridge (Measured {_fmt(measured_cm, 1)} cm)",
        "roof_type": "pitched",
        "measured_height_cm": measured_cm,
        "real_height_m": real_m,
    }'''

assert old_02 in c_dns, "old_02 not found"
c_dns = c_dns.replace(old_02, new_02)
c_dns = c_dns.replace('difficulty="medium",\n    )', 'difficulty="medium",\n        diagram_spec=d_spec_02,\n    )', 1)

# Subskill 03
old_03 = '''    prompt = (
        f"Due to minor paper shrinkage and manual ruler measuring tolerances, a learner calculates a scale ratio "
        f"of 1 : {_fmt(calculated_denom, 1)} for an architectural plan.\\n\\n"
        f"To which standard commercial architectural drawing scale should this calculation be rounded, "
        f"and what accounts for the minor discrepancy?"
    )'''
new_03 = '''    prompt = (
        f"Refer to the drawing scale comparison diagram shown. Due to paper shrinkage and ruler measuring tolerances, "
        f"a learner calculates a scale ratio of 1 : {_fmt(calculated_denom, 1)} for an architectural plan.\\n\\n"
        f"To which standard commercial architectural drawing scale should this calculation be rounded, "
        f"and what accounts for the minor discrepancy?"
    )
    d_spec_03 = {
        "kind": "bar_scale",
        "title": f"Drawing Scale Comparison (Calculated 1 : {_fmt(calculated_denom, 1)})",
        "ratio_str": f"1 : {std_scale}",
        "segments": [{"length_cm": 2.0, "real_val": std_scale * 2 / 100, "unit": "m"}],
    }'''

assert old_03 in c_dns, "old_03 not found"
c_dns = c_dns.replace(old_03, new_03)
# Replace second occurrence of difficulty="easy"
idx_03 = c_dns.find('gr12_plans_subskill_03')
idx_diff_03 = c_dns.find('difficulty="easy",\n    )', idx_03)
c_dns = c_dns[:idx_diff_03] + 'difficulty="easy",\n        diagram_spec=d_spec_03,\n    )' + c_dns[idx_diff_03 + len('difficulty="easy",\n    )'):]

# Subskill 04
old_04 = '''    prompt = (
        f"On a detailed residential floor plan drawn to a scale of 1 : {scale}, the length of a bedroom window "
        f"measures {_fmt(plan_cm, 1)} cm.\\n\\n"
        f"Calculate the ACTUAL real-life length of the window in metres (m)."
    )'''
new_04 = '''    prompt = (
        f"Refer to the residential floor plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The bedroom window measures {_fmt(plan_cm, 1)} cm on paper.\\n\\n"
        f"Calculate the ACTUAL real-life length of the window in metres (m)."
    )
    d_spec_04 = {
        "kind": "floor_plan",
        "title": f"Bedroom Window Plan Detail (Scale 1 : {scale})",
        "rooms": [{"name": "Bedroom", "width": plan_cm * 2, "length": plan_cm * 2}],
        "annotations": [{"text": f"Window: {_fmt(plan_cm, 1)} cm"}],
    }'''

assert old_04 in c_dns, "old_04 not found"
c_dns = c_dns.replace(old_04, new_04)
idx_04 = c_dns.find('gr12_plans_subskill_04')
idx_diff_04 = c_dns.find('difficulty="easy",\n    )', idx_04)
c_dns = c_dns[:idx_diff_04] + 'difficulty="easy",\n        diagram_spec=d_spec_04,\n    )' + c_dns[idx_diff_04 + len('difficulty="easy",\n    )'):]

# Subskill 05
old_05 = '''    prompt = (
        f"A municipal building plan is drawn to a scale of 1 : {scale}.\\n"
        f"A learner measures the total length of the front veranda on the plan as {_fmt(plan_cm, 1)} cm.\\n\\n"
        f"Calculate the actual ground length of the veranda in metres (m)."
    )'''
new_05 = '''    prompt = (
        f"Refer to the municipal building plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The front veranda measures {_fmt(plan_cm, 1)} cm on paper.\\n\\n"
        f"Calculate the actual ground length of the veranda in metres (m)."
    )
    d_spec_05 = {
        "kind": "floor_plan",
        "title": f"Veranda Plan Detail (Scale 1 : {scale})",
        "rooms": [{"name": "Veranda", "width": plan_cm * 2, "length": 15}],
        "annotations": [{"text": f"Veranda: {_fmt(plan_cm, 1)} cm"}],
    }'''

assert old_05 in c_dns, "old_05 not found"
c_dns = c_dns.replace(old_05, new_05)
idx_05 = c_dns.find('gr12_plans_subskill_05')
idx_diff_05 = c_dns.find('difficulty="easy",\n    )', idx_05)
c_dns = c_dns[:idx_diff_05] + 'difficulty="easy",\n        diagram_spec=d_spec_05,\n    )' + c_dns[idx_diff_05 + len('difficulty="easy",\n    )'):]

# Subskill 06
old_06 = '''    prompt = (
        f"On an official municipal erf site plan drawn to a scale of 1 : {scale}, the distance between "
        f"the rear boundary wall and the back of the house measures {_fmt(plan_cm, 1)} cm.\\n\\n"
        f"Calculate the actual ground distance in metres (m)."
    )'''
new_06 = '''    prompt = (
        f"Refer to the municipal erf site plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The distance between the rear boundary wall and the back of the house measures {_fmt(plan_cm, 1)} cm on paper.\\n\\n"
        f"Calculate the actual ground distance in metres (m)."
    )
    d_spec_06 = {
        "kind": "site_plan",
        "title": f"Erf Site Plan (Scale 1 : {scale})",
        "boundary": {"width": 80, "length": 120},
        "annotations": [{"text": f"Rear distance: {_fmt(plan_cm, 1)} cm"}],
    }'''

assert old_06 in c_dns, "old_06 not found"
c_dns = c_dns.replace(old_06, new_06)
idx_06 = c_dns.find('gr12_plans_subskill_06')
idx_diff_06 = c_dns.find('difficulty="easy",\n    )', idx_06)
c_dns = c_dns[:idx_diff_06] + 'difficulty="easy",\n        diagram_spec=d_spec_06,\n    )' + c_dns[idx_diff_06 + len('difficulty="easy",\n    )'):]

# Subskill 07
old_07 = '''    prompt = (
        f"A draftsman is drawing a detailed kitchen layout at a scale of 1 : {scale}.\\n"
        f"A row of kitchen floor cupboards has an actual length of {_fmt(real_m, 2)} m.\\n\\n"
        f"What should be the length of this cupboard unit on the drawing, in millimetres (mm)?"
    )'''
new_07 = '''    prompt = (
        f"Refer to the kitchen layout plan shown in the diagram (scale ratio 1 : {scale}). "
        f"A row of kitchen floor cupboards has an actual ground length of {_fmt(real_m, 2)} m.\\n\\n"
        f"What should be the length of this cupboard unit on the drawing, in millimetres (mm)?"
    )
    d_spec_07 = {
        "kind": "floor_plan",
        "title": f"Kitchen Cupboard Layout (Scale 1 : {scale})",
        "rooms": [{"name": "Kitchen", "width": 40, "length": 50}],
        "annotations": [{"text": f"Cupboard Ground: {_fmt(real_m, 2)} m"}],
    }'''

assert old_07 in c_dns, "old_07 not found"
c_dns = c_dns.replace(old_07, new_07)
idx_07 = c_dns.find('gr12_plans_subskill_07')
idx_diff_07 = c_dns.find('difficulty="easy",\n    )', idx_07)
c_dns = c_dns[:idx_diff_07] + 'difficulty="easy",\n        diagram_spec=d_spec_07,\n    )' + c_dns[idx_diff_07 + len('difficulty="easy",\n    )'):]

# Subskill 08
old_08 = '''    prompt = (
        "When taking manual measurements with a ruler graduated in 1 mm increments:\\n"
        "  - On Plan A (Scale 1 : 50), a 1 mm measurement error corresponds to 50 mm (5 cm) on the ground.\\n"
        "  - On Plan B (Scale 1 : 500), a 1 mm measurement error corresponds to 500 mm (50 cm) on the ground.\\n\\n"
        "What practical deduction must a builder make when extracting construction dimensions from small-scale plans?"
    )'''
new_08 = '''    var_plan_b = r.choice([200, 500, 1000])
    ground_mm_b = var_plan_b
    ground_cm_b = ground_mm_b // 10

    prompt = (
        f"Refer to the scale precision diagram shown. When taking manual measurements with a ruler graduated in 1 mm increments:\\n"
        f"  - On Plan A (Scale ratio 1 : 50), a 1 mm measurement error corresponds to 50 mm (5 cm) on the ground.\\n"
        f"  - On Plan B (Scale ratio 1 : {var_plan_b}), a 1 mm measurement error corresponds to {ground_mm_b} mm ({ground_cm_b} cm) on the ground.\\n\\n"
        f"What practical deduction must a builder make when extracting construction dimensions from small-scale plans?"
    )
    d_spec_08 = {
        "kind": "bar_scale",
        "title": f"Scale Precision: Plan A (1 : 50) vs Plan B (1 : {var_plan_b})",
        "ratio_str": f"1 : 50 vs 1 : {var_plan_b}",
        "segments": [{"length_cm": 1.0, "real_val": 0.5, "unit": "m"}, {"length_cm": 1.0, "real_val": var_plan_b / 100, "unit": "m"}],
    }'''

assert old_08 in c_dns, "old_08 not found"
c_dns = c_dns.replace(old_08, new_08)
idx_08 = c_dns.find('gr12_plans_subskill_08')
idx_diff_08 = c_dns.find('difficulty="easy",\n    )', idx_08)
c_dns = c_dns[:idx_diff_08] + 'difficulty="easy",\n        diagram_spec=d_spec_08,\n    )' + c_dns[idx_diff_08 + len('difficulty="easy",\n    )'):]

open(p_dns, "w", encoding="utf-8").write(c_dns)
print("Updated determining_number_scale.py (8 subskills)")


# ---------------------------------------------------------------------------
# 2. bar_scale_construction_conversion.py (subskills 09-16)
# ---------------------------------------------------------------------------
p_bsc = "caps-ai-backend/app/utils/mathematical_literacy/gr12_plans_and_scale/bar_scale_construction_conversion.py"
c_bsc = open(p_bsc, "r", encoding="utf-8").read()

for i in range(9, 17):
    # let's inject diagram_spec into each subskill
    sub_tag = f"gr12_plans_subskill_{i:02d}"
    idx_sub = c_bsc.find(sub_tag)
    assert idx_sub != -1, f"subskill {i} not found"

# Subskill 09
old_09 = '''    prompt = (
        f"A draftsman is constructing an accurate graphic bar scale for an architectural plan drawn at a scale of 1 : {scale}.\\n"
        f"The bar scale must have major graduation divisions representing {_fmt(segment_real_m, 1)} m ground intervals.\\n\\n"
        f"What distance (in centimetres) must separate each {_fmt(segment_real_m, 1)} m division on the ruler bar scale?"
    )'''
new_09 = '''    scale = r.choice([40, 50, 60])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the graphic bar scale shown in the diagram for an architectural plan (scale ratio 1 : {scale}). "
        f"The bar scale has major divisions representing {_fmt(segment_real_m, 1)} m ground intervals.\\n\\n"
        f"What distance (in centimetres) must separate each {_fmt(segment_real_m, 1)} m division on the ruler bar scale?"
    )
    d_spec_09 = {
        "kind": "bar_scale",
        "title": f"Graphic Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }'''
c_bsc = c_bsc.replace(old_09, new_09)
idx_09 = c_bsc.find('gr12_plans_subskill_09')
idx_diff_09 = c_bsc.find('difficulty="easy",\n    )', idx_09)
c_bsc = c_bsc[:idx_diff_09] + 'difficulty="easy",\n        diagram_spec=d_spec_09,\n    )' + c_bsc[idx_diff_09 + len('difficulty="easy",\n    )'):]

# Subskill 10
old_10 = '''    prompt = (
        f"An architectural floor plan uses a number scale of 1 : {scale}.\\n"
        f"To make it easier for builders on site, you need to construct a graphic bar scale "
        f"marked in {_fmt(segment_real_m, 0)} m increments.\\n\\n"
        f"What length (in centimetres) should represent each {_fmt(segment_real_m, 0)} m interval on the drawing?"
    )'''
new_10 = '''    scale = r.choice([80, 100, 120])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the graphic bar scale shown in the diagram for an architectural floor plan (number scale 1 : {scale}). "
        f"The bar scale is marked in {_fmt(segment_real_m, 0)} m increments.\\n\\n"
        f"What length (in centimetres) should represent each {_fmt(segment_real_m, 0)} m interval on the drawing?"
    )
    d_spec_10 = {
        "kind": "bar_scale",
        "title": f"Floor Plan Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }'''
c_bsc = c_bsc.replace(old_10, new_10)
idx_10 = c_bsc.find('gr12_plans_subskill_10')
idx_diff_10 = c_bsc.find('difficulty="easy",\n    )', idx_10)
c_bsc = c_bsc[:idx_diff_10] + 'difficulty="easy",\n        diagram_spec=d_spec_10,\n    )' + c_bsc[idx_diff_10 + len('difficulty="easy",\n    )'):]

# Subskill 11
old_11 = '''    prompt = (
        f"You are required to draw an accurate bar scale for a site development plan drawn to a scale of 1 : {scale}.\\n"
        f"The bar scale must go up in {_fmt(segment_real_m, 0)} m increments.\\n\\n"
        f"Calculate the physical length (in centimetres) of each {_fmt(segment_real_m, 0)} m division on the bar scale."
    )'''
new_11 = '''    scale = r.choice([400, 500, 600])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the site development bar scale shown in the diagram (scale ratio 1 : {scale}). "
        f"The bar scale goes up in {_fmt(segment_real_m, 0)} m increments.\\n\\n"
        f"Calculate the physical length (in centimetres) of each {_fmt(segment_real_m, 0)} m division on the bar scale."
    )
    d_spec_11 = {
        "kind": "bar_scale",
        "title": f"Site Plan Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }'''
c_bsc = c_bsc.replace(old_11, new_11)
idx_11 = c_bsc.find('gr12_plans_subskill_11')
idx_diff_11 = c_bsc.find('difficulty="easy",\n    )', idx_11)
c_bsc = c_bsc[:idx_diff_11] + 'difficulty="easy",\n        diagram_spec=d_spec_11,\n    )' + c_bsc[idx_diff_11 + len('difficulty="easy",\n    )'):]

# Subskill 12
old_12 = '''    prompt = (
        f"A regional layout plan uses a scale of 1 : 10 000.\\n"
        f"A bar scale must be drawn that goes up in 200 m increments.\\n\\n"
        f"Calculate the measurement (in centimetres) between each 200 m mark on the bar scale."
    )'''
new_12 = '''    scale = r.choice([5000, 10000, 20000])
    bar_segment_cm = (segment_real_m * 100.0) / scale
    prompt = (
        f"Refer to the regional layout plan and bar scale shown in the diagram (scale ratio 1 : {scale}). "
        f"The bar scale goes up in {_fmt(segment_real_m, 0)} m increments.\\n\\n"
        f"Calculate the measurement (in centimetres) between each {_fmt(segment_real_m, 0)} m mark on the bar scale."
    )
    d_spec_12 = {
        "kind": "bar_scale",
        "title": f"Regional Layout Bar Scale (Scale 1 : {scale})",
        "ratio_str": f"1 : {scale}",
        "segments": [{"length_cm": bar_segment_cm, "real_val": segment_real_m, "unit": "m"}],
    }'''
c_bsc = c_bsc.replace(old_12, new_12)
idx_12 = c_bsc.find('gr12_plans_subskill_12')
idx_diff_12 = c_bsc.find('difficulty="easy",\n    )', idx_12)
c_bsc = c_bsc[:idx_diff_12] + 'difficulty="easy",\n        diagram_spec=d_spec_12,\n    )' + c_bsc[idx_diff_12 + len('difficulty="easy",\n    )'):]

# Subskill 13
old_13 = '''    prompt = (
        f"A floor plan contains a printed bar scale where each 2 cm segment represents 5 m on the ground.\\n"
        f"Using a pair of dividers or the edge of a sheet of paper, a builder measures the length of an internal "
        f"factory driveway on the plan as {_fmt(measured_len_cm, 1)} cm.\\n\\n"
        f"Using the bar scale directly, calculate the actual ground distance in metres."
    )'''
new_13 = '''    prompt = (
        f"Refer to the factory floor plan and bar scale shown in the diagram, where each 2 cm segment represents 5 m on the ground. "
        f"The internal factory driveway measures {_fmt(measured_len_cm, 1)} cm on paper.\\n\\n"
        f"Using the bar scale directly, calculate the actual ground distance in metres."
    )
    d_spec_13 = {
        "kind": "bar_scale",
        "title": f"Factory Floor Plan Bar Scale (Driveway {_fmt(measured_len_cm, 1)} cm)",
        "ratio_str": "1 : 250",
        "segments": [{"length_cm": 2.0, "real_val": 5.0, "unit": "m"}],
        "measured_cm": measured_len_cm,
    }'''
c_bsc = c_bsc.replace(old_13, new_13)
idx_13 = c_bsc.find('gr12_plans_subskill_13')
idx_diff_13 = c_bsc.find('difficulty="medium",\n    )', idx_13)
c_bsc = c_bsc[:idx_diff_13] + 'difficulty="medium",\n        diagram_spec=d_spec_13,\n    )' + c_bsc[idx_diff_13 + len('difficulty="medium",\n    )'):]

# Subskill 14
old_14 = '''    prompt = (
        "In architectural and civil engineering documentation, plans frequently include both a number scale "
        "(e.g. 1 : 100) and a graphic bar scale.\\n\\n"
        "State TWO significant practical advantages of a graphic bar scale relative to a number scale."
    )'''
new_14 = '''    v_scale = r.choice([50, 100, 200])
    prompt = (
        f"Refer to the scale representation diagram shown (Scale ratio 1 : {v_scale}). "
        f"State TWO significant practical advantages of a graphic bar scale relative to a number scale."
    )
    d_spec_14 = {
        "kind": "bar_scale",
        "title": f"Bar Scale vs Number Scale Comparison (1 : {v_scale})",
        "ratio_str": f"1 : {v_scale}",
        "segments": [{"length_cm": 2.0, "real_val": v_scale * 2 / 100, "unit": "m"}],
    }'''
c_bsc = c_bsc.replace(old_14, new_14)
idx_14 = c_bsc.find('gr12_plans_subskill_14')
idx_diff_14 = c_bsc.find('difficulty="easy",\n    )', idx_14)
c_bsc = c_bsc[:idx_diff_14] + 'difficulty="easy",\n        diagram_spec=d_spec_14,\n    )' + c_bsc[idx_diff_14 + len('difficulty="easy",\n    )'):]

# Subskill 15
old_15 = '''    prompt = (
        "An architectural floor plan drawn to a number scale of 1 : 100 on an A4 sheet is enlarged "
        "by 141% onto an A3 sheet via a digital photocopier.\\n\\n"
        "What is the effect of this enlargement on:\\n"
        "1. The original printed number scale (1 : 100)?\\n"
        "2. The printed graphic bar scale?"
    )'''
new_15 = '''    pct = r.choice([141, 150, 200])
    prompt = (
        f"Refer to the architectural drawing scale diagram shown. An architectural floor plan with number scale 1 : 100 "
        f"on an A4 sheet is enlarged by {pct}% onto a larger sheet via a photocopier.\\n\\n"
        f"What is the effect of this enlargement on:\\n"
        f"1. The original printed number scale (1 : 100)?\\n"
        f"2. The printed graphic bar scale?"
    )
    d_spec_15 = {
        "kind": "bar_scale",
        "title": f"Photocopy Enlargement ({pct}%)",
        "ratio_str": f"1 : 100 enlarged by {pct}%",
        "segments": [{"length_cm": 2.0 * pct / 100, "real_val": 2.0, "unit": "m"}],
    }'''
c_bsc = c_bsc.replace(old_15, new_15)
idx_15 = c_bsc.find('gr12_plans_subskill_15')
idx_diff_15 = c_bsc.find('difficulty="easy",\n    )', idx_15)
c_bsc = c_bsc[:idx_diff_15] + 'difficulty="easy",\n        diagram_spec=d_spec_15,\n    )' + c_bsc[idx_diff_15 + len('difficulty="easy",\n    )'):]

# Subskill 16
old_16 = '''    prompt = (
        f"An enlarged photocopy of an architectural plan has lost its original scale ratio.\\n"
        f"On the photocopied page, a bar scale marked '{_fmt(bar_label_m, 0)} m' now measures "
        f"exactly {_fmt(measured_bar_cm, 1)} cm when measured with a standard metric ruler.\\n\\n"
        f"Recalibrate the plan by calculating the NEW number scale in the form 1 : x (rounded to the nearest whole integer)."
    )'''
new_16 = '''    prompt = (
        f"Refer to the enlarged photocopy bar scale shown in the diagram. On the photocopied page, "
        f"the bar scale marked '{_fmt(bar_label_m, 0)} m' measures exactly {_fmt(measured_bar_cm, 1)} cm with a metric ruler.\\n\\n"
        f"Recalibrate the plan by calculating the NEW number scale in the form 1 : x (rounded to the nearest whole integer)."
    )
    d_spec_16 = {
        "kind": "bar_scale",
        "title": f"Recalibrated Bar Scale (Ruler: {_fmt(measured_bar_cm, 1)} cm)",
        "ratio_str": f"1 : {new_denom}",
        "segments": [{"length_cm": measured_bar_cm, "real_val": bar_label_m, "unit": "m"}],
    }'''
c_bsc = c_bsc.replace(old_16, new_16)
idx_16 = c_bsc.find('gr12_plans_subskill_16')
idx_diff_16 = c_bsc.find('difficulty="medium",\n    )', idx_16)
c_bsc = c_bsc[:idx_diff_16] + 'difficulty="medium",\n        diagram_spec=d_spec_16,\n    )' + c_bsc[idx_diff_16 + len('difficulty="medium",\n    )'):]

open(p_bsc, "w", encoding="utf-8").write(c_bsc)
print("Updated bar_scale_construction_conversion.py (8 subskills)")
