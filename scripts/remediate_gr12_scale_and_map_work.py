"""Remediate Batch C: grade12_mathlit_scale_and_map_work (11 subskills)."""
import os
import re

# 1. number_scale_calculations.py
nsc_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_scale_and_map_work/number_scale_calculations.py"
with open(nsc_path, "r", encoding="utf-8") as f:
    code = f.read()

# Subskill 01
code = code.replace(
'''    # Actual cm = map_cm * 50 000; Actual km = Actual cm / 100 000
    actual_km = round((map_dist_cm * scale_denom) / 100000.0, 2)

    prompt = (
        f"A learner measures the straight-line distance between a trig beacon and a farm dam "
        f"on a 1 : 50 000 South African topographical map as {_fmt(map_dist_cm)} cm.\\n\\n"
        f"Using the 'MA rule' (Map : Actual):\\n"
        f"1. Scale = 1 : 50 000\\n"
        f"2. 100 000 cm = 1 km\\n\\n"
        f"Calculate the actual ground distance between the beacon and the dam in kilometres (km)."
    )''',
'''    # Actual cm = map_cm * 50 000; Actual km = Actual cm / 100 000
    actual_km = round((map_dist_cm * scale_denom) / 100000.0, 2)

    d_spec_01 = {
        "kind": "bar_scale",
        "title": f"Topographical Map Segment ({_fmt(map_dist_cm)} cm)",
        "ratio": "1:50000",
        "segments": [{"length_cm": map_dist_cm, "label": f"{_fmt(map_dist_cm)} cm"}],
    }

    prompt = (
        f"Refer to the topographical map segment (scale 1 : 50 000) showing {_fmt(map_dist_cm)} cm between beacons.\\n"
        f"Using the 'MA rule' (Map : Actual):\\n"
        f"1. Scale = 1 : 50 000\\n"
        f"2. 100 000 cm = 1 km\\n\\n"
        f"Calculate the actual ground distance between the beacon and the dam in kilometres (km)."
    )'''
)

code = code.replace(
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_01",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_01",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_01,
    )'''
)

# Subskill 02
code = code.replace(
'''    # mm on plan -> mm in real life -> metres (divide by 1 000)
    actual_m = round((map_dist_mm * scale_denom) / 1000.0, 2)

    prompt = (
        f"An architectural site development plan for a school library is drawn to a scale of 1 : {scale_denom}.\\n"
        f"The boundary wall length measures {map_dist_mm} mm on the blueprint.\\n\\n"
        f"Given that 1 m = 1 000 mm:\\n"
        f"Calculate the actual real-life length of the boundary wall in metres (m)."
    )''',
'''    # mm on plan -> mm in real life -> metres (divide by 1 000)
    actual_m = round((map_dist_mm * scale_denom) / 1000.0, 2)

    d_spec_02 = {
        "kind": "floor_plan",
        "scale": f"1:{scale_denom}",
        "title": f"Site Development Plan ({map_dist_mm} mm)",
        "rooms": [{"name": "Boundary Wall", "length_mm": map_dist_mm}],
    }

    prompt = (
        f"Refer to the architectural site development plan (scale ratio 1 : {scale_denom}) where the boundary wall length is {map_dist_mm} mm.\\n\\n"
        f"Given that 1 m = 1 000 mm:\\n"
        f"Calculate the actual real-life length of the boundary wall in metres (m)."
    )'''
)

code = code.replace(
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_02",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_02",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_02,
    )'''
)

# Subskill 03
code = code.replace(
'''    # actual cm = actual km * 100 000; map_cm = actual cm / 250 000
    actual_cm = actual_km * 100000.0
    map_cm = round(actual_cm / scale_denom, 1)

    prompt = (
        f"Two towns in the Free State are situated exactly {_fmt(actual_km)} km apart in reality.\\n"
        f"A regional tourism roadmap has a scale of 1 : 250 000.\\n\\n"
        f"Given that 1 km = 100 000 cm:\\n"
        f"Calculate the distance between these two towns on the map in centimetres (cm)."
    )''',
'''    # actual cm = actual km * 100 000; map_cm = actual cm / 250 000
    actual_cm = actual_km * 100000.0
    map_cm = round(actual_cm / scale_denom, 1)

    d_spec_03 = {
        "kind": "strip_map",
        "title": f"Regional Route ({_fmt(actual_km)} km)",
        "scale": "1:250000",
        "towns": [{"name": "Town A", "km": 0}, {"name": "Town B", "km": actual_km}],
    }

    prompt = (
        f"Refer to the regional tourism roadmap (scale ratio 1 : 250 000). Two Free State towns are situated {_fmt(actual_km)} km apart in reality.\\n\\n"
        f"Given that 1 km = 100 000 cm:\\n"
        f"Calculate the distance between these two towns on the map in centimetres (cm)."
    )'''
)

code = code.replace(
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_03",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_03",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_03,
    )'''
)

# Subskill 04
code = code.replace(
'''    # scale = map_cm : actual_cm -> 1 : (actual_cm / map_cm)
    actual_cm = actual_km * 100000.0
    denom = int(round(actual_cm / map_cm))

    prompt = (
        f"On a provincial road map, the measured distance between two highway interchanges is "
        f"{_fmt(map_cm)} cm. The actual driving distance along this straight stretch is {_fmt(actual_km)} km.\\n\\n"
        f"Using the 'MA rule' (Map : Actual) and converting both values to centimetres:\\n"
        f"Determine the number scale of the map in the form 1 : x."
    )''',
'''    # scale = map_cm : actual_cm -> 1 : (actual_cm / map_cm)
    actual_cm = actual_km * 100000.0
    denom = int(round(actual_cm / map_cm))

    d_spec_04 = {
        "kind": "strip_map",
        "title": f"Highway Interchanges ({_fmt(actual_km)} km)",
        "scale": f"1:{denom}",
        "towns": [{"name": "Interchange 1", "km": 0}, {"name": "Interchange 2", "km": actual_km}],
    }

    prompt = (
        f"Refer to the provincial road map. The distance between two highway interchanges is {_fmt(map_cm)} cm, while the actual driving distance along this straight stretch is {_fmt(actual_km)} km.\\n\\n"
        f"Using the 'MA rule' (Map : Actual) and converting both values to centimetres:\\n"
        f"Determine the number scale of the map in the form 1 : x."
    )'''
)

code = code.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_04",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_04",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_04,
    )'''
)

# Subskill 05
code = code.replace(
'''    actual_cm = bar_rep_km * 100000.0
    denom = int(round(actual_cm / bar_len_cm))

    prompt = (
        f"A national park tourist map includes a graphical bar scale where a line segment measuring "
        f"{_fmt(bar_len_cm)} cm on the page represents an actual ground distance of {_fmt(bar_rep_km)} km.\\n\\n"
        f"1. Express both measurements in centimetres (1 km = 100 000 cm).\\n"
        f"2. Divide both sides by the map measurement ({_fmt(bar_len_cm)} cm) to get 1 on the left.\\n\\n"
        f"Determine the equivalent number scale in the form 1 : x."
    )''',
'''    actual_cm = bar_rep_km * 100000.0
    denom = int(round(actual_cm / bar_len_cm))

    d_spec_05 = {
        "kind": "bar_scale",
        "title": f"Bar Scale ({_fmt(bar_len_cm)} cm = {_fmt(bar_rep_km)} km)",
        "length_cm": bar_len_cm,
        "represents_km": bar_rep_km,
    }

    prompt = (
        f"Refer to the graphical bar scale of a national park tourist map. A segment of {_fmt(bar_len_cm)} cm represents an actual ground distance of {_fmt(bar_rep_km)} km.\\n\\n"
        f"1. Express both measurements in centimetres (1 km = 100 000 cm).\\n"
        f"2. Divide both sides by the map measurement ({_fmt(bar_len_cm)} cm) to get 1 on the left.\\n\\n"
        f"Determine the equivalent number scale in the form 1 : x."
    )'''
)

code = code.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_05",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_05",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_05,
    )'''
)

# Subskill 06
code = code.replace(
'''    # Standard rounded scale e.g. 1 : 2 400 000
    sensible_rounded_denom = int(round(approx_scale_denom / 100000.0) * 100000)

    prompt = (
        f"On a road map, the route between Kimberley and Heuningneskloof shows three consecutive "
        f"distance markers: {marker_1} km, {marker_2} km, and {marker_3} km.\\n"
        f"A learner measures the straight distance between the two towns on the map as {_fmt(map_cm)} cm.\\n\\n"
        f"1. Calculate the total marked distance along the route in km.\\n"
        f"2. Use the measurement of {_fmt(map_cm)} cm and your total distance to calculate the approximate "
        f"scale of the map, rounded off to the nearest sensible hundred-thousand (1 : x 00 000)."
    )''',
'''    # Standard rounded scale e.g. 1 : 2 400 000
    sensible_rounded_denom = int(round(approx_scale_denom / 100000.0) * 100000)

    d_spec_06 = {
        "kind": "strip_map",
        "title": f"Route Markers ({total_km} km)",
        "towns": [
            {"name": "Kimberley", "km": 0},
            {"name": "Marker 1", "km": marker_1},
            {"name": "Marker 2", "km": marker_1 + marker_2},
            {"name": "Heuningneskloof", "km": total_km},
        ],
    }

    prompt = (
        f"Refer to the strip map between Kimberley and Heuningneskloof showing three consecutive distance markers: {marker_1} km, {marker_2} km, and {marker_3} km.\\n"
        f"The straight distance on the map between the two towns is {_fmt(map_cm)} cm.\\n\\n"
        f"1. Calculate the total marked distance along the route in km.\\n"
        f"2. Use the measurement of {_fmt(map_cm)} cm and your total distance to calculate the approximate "
        f"scale of the map, rounded off to the nearest sensible hundred-thousand (1 : x 00 000)."
    )'''
)

code = code.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_06",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_06",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_06,
    )'''
)

# Subskill 08
code = code.replace(
'''def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Subskill 08: Scale enlargement and reduction: effect of photocopying on number scale vs bar scale."""
    enlarge_pct = r.choice([150, 200])

    prompt = (
        f"A geography teacher takes an original map with a number scale of 1 : 50 000 and a "
        f"graphical bar scale, and photocopies it with an enlargement of {enlarge_pct}%.\\n\\n"
        f"Which of the following statements correctly describes what happens to the two scales on the enlarged photocopy?"
    )''',
'''def gen_subskill_08(r: random.Random) -> Dict[str, Any]:
    """Subskill 08: Scale enlargement and reduction: effect of photocopying on number scale vs bar scale."""
    enlarge_pct = r.choice([150, 200])

    d_spec_08 = {
        "kind": "bar_scale",
        "title": f"Photocopy Bar Scale Enlargement ({enlarge_pct}%)",
        "ratio": "1:50000",
        "enlargement_percent": enlarge_pct,
    }

    prompt = (
        f"An original map has a number scale of 1 : 50 000 alongside a graphical bar scale. An educator photocopies it with an enlargement of {enlarge_pct}%.\\n\\n"
        f"Which of the following statements correctly describes what happens to the two scales on the enlarged photocopy?"
    )'''
)

code = code.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_08",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_08",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_08,
    )'''
)

with open(nsc_path, "w", encoding="utf-8") as f:
    f.write(code)
print("Updated number_scale_calculations.py")

# 2. strip_maps_distance_charts.py
smd_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_scale_and_map_work/strip_maps_distance_charts.py"
with open(smd_path, "r", encoding="utf-8") as f:
    s_code = f.read()

# Subskill 10
s_code = s_code.replace(
'''    total_dist = leg1 + leg2 + leg3 + leg4

    prompt = (
        f"A motorist travels along the N1 national route from Town A to Town E.\\n"
        f"A strip road map shows the distance between consecutive waypoints:\\n"
        f"• Town A to Town B: {leg1} km\\n"
        f"• Town B to Town C: {leg2} km\\n"
        f"• Town C to Town D: {leg3} km\\n"
        f"• Town D to Town E: {leg4} km\\n\\n"
        f"Calculate the total driving distance between Town A and Town E in kilometres (km)."
    )''',
'''    total_dist = leg1 + leg2 + leg3 + leg4

    d_spec_10 = {
        "kind": "strip_map",
        "title": f"N1 National Route ({total_dist} km)",
        "towns": [
            {"name": "Town A", "km": 0},
            {"name": "Town B", "km": leg1},
            {"name": "Town C", "km": leg1 + leg2},
            {"name": "Town D", "km": leg1 + leg2 + leg3},
            {"name": "Town E", "km": total_dist},
        ],
    }

    prompt = (
        f"Refer to the strip road map along the N1 national route from Town A to Town E.\\n"
        f"The distance between consecutive waypoints is:\\n"
        f"• Town A to Town B: {leg1} km\\n"
        f"• Town B to Town C: {leg2} km\\n"
        f"• Town C to Town D: {leg3} km\\n"
        f"• Town D to Town E: {leg4} km\\n\\n"
        f"Calculate the total driving distance between Town A and Town E in kilometres (km)."
    )'''
)

s_code = s_code.replace(
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_10",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_scale_subskill_10",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_10,
    )'''
)

# Subskill 12
s_code = s_code.replace(
'''    prompt = (
        f"On a strip road map between Johannesburg and Bloemfontein along the N1 south, a driver "
        f"wishes to turn onto the N5 highway towards Harrismith.\\n"
        f"The strip map shows the major junction intersection is at {chosen_junction}, located "
        f"{distance_to_junction} km from the start of the section.\\n\\n"
        f"Identify the major junction town on the strip map and state the distance to it."
    )''',
'''    d_spec_12 = {
        "kind": "strip_map",
        "title": f"N1 Highway Section to {chosen_junction} ({distance_to_junction} km)",
        "towns": [
            {"name": "Start", "km": 0},
            {"name": chosen_junction, "km": distance_to_junction},
        ],
    }

    prompt = (
        f"Refer to the strip road map between Johannesburg and Bloemfontein along the N1 south.\\n"
        f"A driver wishes to turn onto the N5 highway towards Harrismith.\\n"
        f"The junction intersection is at {chosen_junction}, located "
        f"{distance_to_junction} km from the start of the section.\\n\\n"
        f"Identify the major junction town on the strip map and state the distance to it."
    )'''
)

s_code = s_code.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_12",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_12",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_12,
    )'''
)

with open(smd_path, "w", encoding="utf-8") as f:
    f.write(s_code)
print("Updated strip_maps_distance_charts.py")

# 3. fuel_consumption_range.py
fcr_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_scale_and_map_work/fuel_consumption_range.py"
with open(fcr_path, "r", encoding="utf-8") as f:
    f_code = f.read()

# Subskill 37
f_code = f_code.replace(
'''def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Refueling stop planning along a route based on tank capacity and safety reserve."""
    dist_total_km = 950
    tank_litres = 50.0
    rate_per_100 = 8.0  # L/100 km -> Range = 625 km
    reserve_litres = 10.0  # 10 L safety reserve
    usable_litres = tank_litres - reserve_litres  # 40 L
    safe_range_km = int((usable_litres / rate_per_100) * 100)  # 500 km

    prompt = (
        f"A motorist drives 950 km from Pretoria to Beaufort West.\\n"
        f"• Fuel tank capacity: 50 Litres\\n"
        f"• Average fuel consumption: 8,0 L/100 km\\n"
        f"• The driver insists on maintaining a 10-Litre emergency safety reserve at all times.\\n\\n"
        f"1. How many usable litres of fuel are available between fills?\\n"
        f"2. What is the safe driving range in km before stopping to refuel?\\n"
        f"3. What is the minimum number of refueling stops required during the 950 km journey?"
    )''',
'''def gen_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Subskill 37: Refueling stop planning along a route based on tank capacity and safety reserve."""
    dist_total_km = r.choice([850, 950, 1050, 1150])
    tank_litres = r.choice([45.0, 50.0, 55.0, 60.0])
    rate_per_100 = 8.0  # L/100 km
    reserve_litres = 10.0  # 10 L safety reserve
    usable_litres = tank_litres - reserve_litres
    safe_range_km = int((usable_litres / rate_per_100) * 100)

    d_spec_37 = {
        "kind": "strip_map",
        "title": f"Route Planning: {dist_total_km} km (Safe Range: {safe_range_km} km)",
        "towns": [
            {"name": "Pretoria", "km": 0},
            {"name": "Refuel Stop", "km": safe_range_km},
            {"name": "Beaufort West", "km": dist_total_km},
        ],
    }

    prompt = (
        f"Refer to the route plan from Pretoria to Beaufort West ({dist_total_km} km).\\n"
        f"• Fuel tank capacity: {_fmt(tank_litres, 0)} Litres\\n"
        f"• Average fuel consumption: 8,0 L/100 km\\n"
        f"• The driver insists on maintaining a 10-Litre emergency safety reserve at all times.\\n\\n"
        f"1. How many usable litres of fuel are available between fills?\\n"
        f"2. What is the safe driving range in km before stopping to refuel?\\n"
        f"3. What is the minimum number of refueling stops required during the {dist_total_km} km journey?"
    )'''
)

f_code = f_code.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_37",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_37",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_37,
    )'''
)

with open(fcr_path, "w", encoding="utf-8") as f:
    f.write(f_code)
print("Updated fuel_consumption_range.py")

# 4. compass_bearings_elevations.py
cbe_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_scale_and_map_work/compass_bearings_elevations.py"
with open(cbe_path, "r", encoding="utf-8") as f:
    c_code = f.read()

# Subskill 44
c_code = c_code.replace(
'''def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Interpreting building elevation views: identifying elevations from a floor plan."""
    prompt = (
        f"In architectural building plans, elevations are named according to the compass direction "
        f"that the wall faces (e.g. 'North Elevation', 'South Elevation').\\n\\n"
        f"If an observer is standing outside a house looking directly at the 'South Elevation', "
        f"in which compass direction is the observer facing?"
    )

    correct_ans = "Facing North (looking towards the South-facing wall)"
    explanation = (
        f"1. The 'South Elevation' is the side of the building that faces South towards the outside.\\n"
        f"2. A person standing outside looking directly at this wall must be looking North."
    )
    t1 = "A South Elevation faces South; to see it from the outside, you must look in the opposite direction (North)."
    t2 = "Opposite of South is North."
    t3 = f"Observer orientation: {correct_ans}."

    custom_opts = [
        correct_ans,
        "Facing South",
        "Facing East",
        "Facing West",
    ]''',
'''def gen_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Subskill 44: Interpreting building elevation views: identifying elevations from a floor plan."""
    wall_dir = r.choice(["South", "North", "East", "West"])
    opposite = {"South": "North", "North": "South", "East": "West", "West": "East"}[wall_dir]

    d_spec_44 = {
        "kind": "elevation_compass",
        "title": f"Building Elevation Compass ({wall_dir} Wall)",
        "wall_direction": wall_dir,
    }

    prompt = (
        f"Refer to the building elevation compass scheme.\\n"
        f"If an observer is standing outside a house looking directly at the '{wall_dir} Elevation', "
        f"in which compass direction is the observer facing?"
    )

    correct_ans = f"Facing {opposite} (looking towards the {wall_dir}-facing wall)"
    explanation = (
        f"1. The '{wall_dir} Elevation' is the side of the building that faces {wall_dir} towards the outside.\\n"
        f"2. A person standing outside looking directly at this wall must be looking {opposite}."
    )
    t1 = f"A {wall_dir} Elevation faces {wall_dir}; to see it from the outside, you must look in the opposite direction ({opposite})."
    t2 = f"Opposite of {wall_dir} is {opposite}."
    t3 = f"Observer orientation: {correct_ans}."

    custom_opts = [
        correct_ans,
        f"Facing {wall_dir}",
        "Facing East" if wall_dir in ("North", "South") else "Facing North",
        "Facing West" if wall_dir in ("North", "South") else "Facing South",
    ]'''
)

c_code = c_code.replace(
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_44",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
    )''',
'''    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_scale_subskill_44",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_44,
    )'''
)

with open(cbe_path, "w", encoding="utf-8") as f:
    f.write(c_code)
print("Updated compass_bearings_elevations.py")
