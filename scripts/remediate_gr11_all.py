"""Comprehensive Grade 11 MathLit Remediation Script for REM-6."""
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "caps-ai-backend" / "app" / "utils" / "mathematical_literacy"

# ===========================================================================
# 1. gr11_plans_representations
# ===========================================================================
print("--- Remediating gr11_plans_representations ---")

# 1.1 floor_plans.py: subskill_2 and subskill_3
p_fp = BASE / "gr11_plans_representations" / "floor_plans.py"
c_fp = p_fp.read_text(encoding="utf-8")

# subskill_2
pat_fp2 = r'(def generate_subskill_2\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_fp2 = r'''\1d_spec = {
        "kind": "floor_plan",
        "title": f"House Floor Plan (Scale 1:100) - {room}",
        "length_m": real_l_m,
        "width_m": real_w_m,
        "rooms": [{"name": room, "length_m": real_l_m, "width_m": real_w_m}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_fp = re.sub(pat_fp2, rep_fp2, c_fp, flags=re.DOTALL)
# prompt leak rewrite for subskill_2
c_fp = c_fp.replace(
    'On a house floor plan drawn to a scale of 1:100, the {room} measures',
    'Refer to the 1:100 scale house floor plan shown in the diagram. The {room} measures'
)

# subskill_3
pat_fp3 = r'(def generate_subskill_3\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_fp3 = r'''\1d_spec = {
        "kind": "floor_plan",
        "title": f"Architectural Drawing (Scale 1:50) - {room}",
        "length_m": real_l_m,
        "width_m": real_w_m,
        "rooms": [{"name": room, "length_m": real_l_m, "width_m": real_w_m}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_fp = re.sub(pat_fp3, rep_fp3, c_fp, flags=re.DOTALL)
p_fp.write_text(c_fp, encoding="utf-8")
print("Remediated floor_plans.py")

# 1.2 elevation_orientations.py: subskills 11, 12, 13, 14, 15, 17
p_elev = BASE / "gr11_plans_representations" / "elevation_orientations.py"
c_elev = p_elev.read_text(encoding="utf-8")

# subskill 11
pat_e11 = r'(def generate_subskill_11\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_e11 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"House Elevation ({compass_cardinal})",
        "side": compass_cardinal,
        "features": [features],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_elev = re.sub(pat_e11, rep_e11, c_elev, flags=re.DOTALL)

# subskill 12
pat_e12 = r'(def generate_subskill_12\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_e12 = r'''\1d_spec = {
        "kind": "elevation_compass",
        "title": f"Observer Viewpoint Facing {observer_facing}",
        "target_dir": observer_facing,
        "compass": True,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_elev = re.sub(pat_e12, rep_e12, c_elev, flags=re.DOTALL)

# subskill 13
pat_e13 = r'(def generate_subskill_13\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_e13 = r'''\1d_spec = {
        "kind": "elevation_compass",
        "title": "Passive Solar Orientation (North)",
        "target_dir": "North",
        "compass": True,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_elev = re.sub(pat_e13, rep_e13, c_elev, flags=re.DOTALL)

# subskill 14
pat_e14 = r'(def generate_subskill_14\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_e14 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"Wall & Roof Ridge Elevation ({real_wall_m} m)",
        "height_m": real_wall_m,
        "roof": {"rise_m": roof_rise_cm},
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_elev = re.sub(pat_e14, rep_e14, c_elev, flags=re.DOTALL)
# prompt leak rewrite for subskill 14
c_elev = c_elev.replace("drawn to a scale of 1:100", "rendered at a scale ratio of 1:100")

# subskill 15
pat_e15 = r'(def generate_subskill_15\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_e15 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"Net Wall Surface Area ({wall_l} m × {wall_h} m)",
        "width_m": wall_l,
        "height_m": wall_h,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_elev = re.sub(pat_e15, rep_e15, c_elev, flags=re.DOTALL)

# subskill 17
pat_e17 = r'(def generate_subskill_17\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_e17 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"Elevation Openings ({direction} Elevation - {room})",
        "side": direction,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_elev = re.sub(pat_e17, rep_e17, c_elev, flags=re.DOTALL)

p_elev.write_text(c_elev, encoding="utf-8")
print("Remediated elevation_orientations.py")

# 1.3 scale_drawing.py: subskills 29, 30, 33, 34, 36
p_sd = BASE / "gr11_plans_representations" / "scale_drawing.py"
c_sd = p_sd.read_text(encoding="utf-8")

# subskill 29
pat_sd29 = r'(def generate_subskill_29\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_sd29 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": f"Site Plan Bar Scale (1:100, Wall {_fmt(real_m)} m)",
        "scale": "1 : 100",
        "segment_value_m": 1.0,
        "total_km": real_m / 1000,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sd = re.sub(pat_sd29, rep_sd29, c_sd, flags=re.DOTALL)
c_sd = c_sd.replace("drawn to a scale of 1:100", "rendered at a scale ratio of 1:100")

# subskill 30
pat_sd30 = r'(def generate_subskill_30\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_sd30 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": f"Site Layout Bar Scale (1:200, Fence {_fmt(real_m)} m)",
        "scale": "1 : 200",
        "segment_value_m": 2.0,
        "total_km": real_m / 1000,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sd = re.sub(pat_sd30, rep_sd30, c_sd, flags=re.DOTALL)
c_sd = c_sd.replace("drawn to a scale of 1:200", "rendered at a scale ratio of 1:200")

# subskill 33
pat_sd33 = r'(def generate_subskill_33\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_sd33 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": f"Number Scale (1 : {ratio})",
        "scale": f"1 : {ratio}",
        "segment_value_m": ratio / 100 if ratio >= 100 else 1.0,
        "total_km": 1.0,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sd = re.sub(pat_sd33, rep_sd33, c_sd, flags=re.DOTALL)

# subskill 34
pat_sd34 = r'(def generate_subskill_34\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_sd34 = r'''\1d_spec = {
        "kind": "mensuration_2d",
        "title": f"Scaled Room Plan (1:{scale_n}, Area {drawing_area_cm2} cm²)",
        "length": scale_n / 10,
        "width": scale_n / 10,
        "shape": "scaled_room",
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sd = re.sub(pat_sd34, rep_sd34, c_sd, flags=re.DOTALL)
c_sd = c_sd.replace("drawn to a scale of 1 : 200", "rendered at a scale ratio of 1 : 200")
c_sd = c_sd.replace("drawn to a scale of 1 : 100", "rendered at a scale ratio of 1 : 100")
c_sd = c_sd.replace("drawn to a scale of 1 : 50", "rendered at a scale ratio of 1 : 50")
c_sd = re.sub(r"drawn to a scale of 1\s*:\s*\w+", "rendered at scale", c_sd)

# subskill 36
pat_sd36 = r'(def generate_subskill_36\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_sd36 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": "A4 to A3 Rescaling Graphic Bar Scale",
        "scale": "1 : 100",
        "segment_value_m": 1.0,
        "total_km": 0.05,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sd = re.sub(pat_sd36, rep_sd36, c_sd, flags=re.DOTALL)

p_sd.write_text(c_sd, encoding="utf-8")
print("Remediated scale_drawing.py")

# 1.4 nets_folding.py: subskill 42
p_nf = BASE / "gr11_plans_representations" / "nets_folding.py"
c_nf = p_nf.read_text(encoding="utf-8")
pat_nf42 = r'(def generate_subskill_42\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_nf42 = r'''\1d_spec = {
        "kind": "cylinder_net",
        "title": f"Cylinder 2D Net (Radius {_fmt(cyl_radius)} cm, Height {_fmt(cyl_h)} cm)",
        "radius": cyl_radius,
        "height": cyl_h,
        "length": circ,
        "width": cyl_h,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_nf = re.sub(pat_nf42, rep_nf42, c_nf, flags=re.DOTALL)
p_nf.write_text(c_nf, encoding="utf-8")
print("Remediated nets_folding.py")


# ===========================================================================
# 2. gr11_maps
# ===========================================================================
print("\n--- Remediating gr11_maps ---")

# 2.1 scale_distances.py: subskills 3, 5, 7, 9
p_sdist = BASE / "gr11_maps" / "scale_distances.py"
c_sdist = p_sdist.read_text(encoding="utf-8")

pat_md3 = r'(def generate_subskill_3\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_md3 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": f"Regional Road Map Bar Scale ({province}, 1:500 000)",
        "scale": "1 : 500 000",
        "segment_value_km": 5,
        "total_km": real_km,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sdist = re.sub(pat_md3, rep_md3, c_sdist, flags=re.DOTALL)

pat_md5 = r'(def generate_subskill_5\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_md5 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": f"Topographic Map Scale (1:{scale}, Distance {real_km} km)",
        "scale": f"1 : {scale}",
        "segment_value_km": scale / 100000,
        "total_km": real_km,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sdist = re.sub(pat_md5, rep_md5, c_sdist, flags=re.DOTALL)

pat_md7 = r'(def generate_subskill_7\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_md7 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": f"Surveyor Benchmark Scale (1:{scale_n}, Real {real_km} km)",
        "scale": f"1 : {scale_n}",
        "segment_value_km": real_km / 5,
        "total_km": real_km,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sdist = re.sub(pat_md7, rep_md7, c_sdist, flags=re.DOTALL)

pat_md9 = r'(def generate_subskill_9\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_md9 = r'''\1d_spec = {
        "kind": "bar_scale",
        "title": "Mobile Street Map Zoom Scale (1:25 000)",
        "scale": "1 : 25 000",
        "segment_value_km": 0.25,
        "total_km": 1.0,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_sdist = re.sub(pat_md9, rep_md9, c_sdist, flags=re.DOTALL)

p_sdist.write_text(c_sdist, encoding="utf-8")
print("Remediated scale_distances.py")

# 2.2 directions_bearings.py: subskills 16, 17
p_dir = BASE / "gr11_maps" / "directions_bearings.py"
c_dir = p_dir.read_text(encoding="utf-8")

pat_dir16 = r'(def generate_subskill_16\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_dir16 = r'''\1d_spec = {
        "kind": "bearing_map",
        "title": f"Regional Map: {town_a} to {town_b} ({dist_km} km)",
        "towns": [town_a, town_b],
        "bearing_deg": 45,
        "target_dir": cardinal,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_dir = re.sub(pat_dir16, rep_dir16, c_dir, flags=re.DOTALL)
# prompt leak rewrite for subskill 16
c_dir = c_dir.replace(
    'On a regional map, Town B ({town_b}) is positioned {_fmt(dist_km)} km away from Town A ({town_a}) in the direction of {cardinal}.',
    'Refer to the regional map shown in the diagram. Town B ({town_b}) is located at a distance of {_fmt(dist_km)} km from Town A ({town_a}) along the indicated bearing line.'
)

pat_dir17 = r'(def generate_subskill_17\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_dir17 = r'''\1d_spec = {
        "kind": "bearing_map",
        "title": f"GPS Coordinate Grid ({lat_deg}°S, {long_deg}°E)",
        "points": [{"name": "GPS Location", "lat": lat_deg, "long": long_deg}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_dir = re.sub(pat_dir17, rep_dir17, c_dir, flags=re.DOTALL)

p_dir.write_text(c_dir, encoding="utf-8")
print("Remediated directions_bearings.py")

# 2.3 topographic_contours.py: subskills 37, 38, 39, 41, 43
p_topo = BASE / "gr11_maps" / "topographic_contours.py"
c_topo = p_topo.read_text(encoding="utf-8")

pat_t37 = r'(def generate_subskill_37\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_t37 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"Topographic Contour Map (Interval {interval} m)",
        "elevation": contour_2,
        "dimensions": f"{contour_1}m to {contour_2}m",
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_topo = re.sub(pat_t37, rep_t37, c_topo, flags=re.DOTALL)

pat_t38 = r'(def generate_subskill_38\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_t38 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"Trig Beacon {trig_beacon_num} ({altitude} m)",
        "elevation": altitude,
        "features": [f"Trig Beacon {trig_beacon_num}", f"Base Spot Height {base_spot_height}"],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_topo = re.sub(pat_t38, rep_t38, c_topo, flags=re.DOTALL)

pat_t39 = r'(def generate_subskill_39\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_t39 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"Topographic Feature: {feature.title()} Slopes",
        "features": [side_steep, side_gentle],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_topo = re.sub(pat_t39, rep_t39, c_topo, flags=re.DOTALL)

pat_t41 = r'(def generate_subskill_41\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_t41 = r'''\1d_spec = {
        "kind": "elevation_view",
        "title": f"Gradient Slope Profile (Rise {rise_m} m, Run {run_m} m)",
        "height_m": rise_m,
        "width_m": run_m,
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_topo = re.sub(pat_t41, rep_t41, c_topo, flags=re.DOTALL)

pat_t43 = r'(def generate_subskill_43\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_t43 = r'''\1d_spec = {
        "kind": "line_graph",
        "title": f"Hiking Trail Elevation Profile ({p1}m - {p4}m)",
        "categories": ["P1", "P2", "P3", "P4"],
        "values": [p1, p2, p3, p4],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_topo = re.sub(pat_t43, rep_t43, c_topo, flags=re.DOTALL)

p_topo.write_text(c_topo, encoding="utf-8")
print("Remediated topographic_contours.py")


# ===========================================================================
# 3. gr11_finance_tax
# ===========================================================================
print("\n--- Remediating gr11_finance_tax ---")

p_ft_ded = BASE / "gr11_finance_tax" / "gross_net_deductions.py"
c_ft_ded = p_ft_ded.read_text(encoding="utf-8")
pat_ft_sal = r'(def _gen_net_salary_calculation\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_ft_sal = r'''\1d_spec = {
        "kind": "bar_graph",
        "title": f"Gross vs Net Salary Breakdown ({name})",
        "categories": ["Gross Salary", "Deductions", "Net Salary"],
        "values": [gross, total_ded, net],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_ft_ded = re.sub(pat_ft_sal, rep_ft_sal, c_ft_ded, flags=re.DOTALL)
p_ft_ded.write_text(c_ft_ded, encoding="utf-8")

p_ft_reb = BASE / "gr11_finance_tax" / "rebates_credits_paye.py"
c_ft_reb = p_ft_reb.read_text(encoding="utf-8")
pat_ft_ann = r'(def _gen_annual_net_tax_after_rebates\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_ft_ann = r'''\1d_spec = {
        "kind": "step_tariff",
        "title": f"SARS Income Tax Bracket 2 Calculation ({name})",
        "blocks": [{"limit": 237100, "rate": 18}, {"limit": 305526, "rate": 26}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_ft_reb = re.sub(pat_ft_ann, rep_ft_ann, c_ft_reb, flags=re.DOTALL)

pat_ft_mtc = r'(def _gen_net_paye_after_medical_credits\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_ft_mtc = r'''\1d_spec = {
        "kind": "bar_graph",
        "title": f"Monthly PAYE and Medical Tax Credits ({name})",
        "categories": ["Preliminary PAYE", "Medical Credits", "Net PAYE"],
        "values": [paye_before_mtc, mtc_credit, final_paye],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_ft_reb = re.sub(pat_ft_mtc, rep_ft_mtc, c_ft_reb, flags=re.DOTALL)
p_ft_reb.write_text(c_ft_reb, encoding="utf-8")

p_ft_scen = BASE / "gr11_finance_tax" / "payslip_audits_scenarios.py"
c_ft_scen = p_ft_scen.read_text(encoding="utf-8")
pat_ft_inc = r'(def _gen_salary_increase_net_impact\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_ft_inc = r'''\1d_spec = {
        "kind": "double_bar_graph",
        "title": f"Salary Increase Impact Comparison ({name})",
        "categories": ["Old Gross", "New Gross"],
        "values": [int(old_gross), int(new_gross)],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_ft_scen = re.sub(pat_ft_inc, rep_ft_inc, c_ft_scen, flags=re.DOTALL)

pat_ft_bud = r'(def _gen_budgeting_net_income_living_expenses\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_ft_bud = r'''\1d_spec = {
        "kind": "bar_graph",
        "title": f"Monthly Living Expenses Budget ({name})",
        "categories": ["Housing", "Groceries", "Transport", "Utilities"],
        "values": [rent, groceries, transport, utilities],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_ft_scen = re.sub(pat_ft_bud, rep_ft_bud, c_ft_scen, flags=re.DOTALL)
p_ft_scen.write_text(c_ft_scen, encoding="utf-8")
print("Remediated gr11_finance_tax")


# ===========================================================================
# 4. gr11_patterns_relationships
# ===========================================================================
print("\n--- Remediating gr11_patterns_relationships ---")

p_pat_lin = BASE / "gr11_patterns_relationships" / "linear_patterns.py"
c_pat_lin = p_pat_lin.read_text(encoding="utf-8")
pat_p4 = r'(def generate_subskill_4\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_p4 = r'''\1d_spec = {
        "kind": "cartesian_system",
        "title": "Linear Pattern Relationship",
        "lines": [{"name": "Pattern Line", "points": [{"x": 1, "y": 10}, {"x": 5, "y": 50}]}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_pat_lin = re.sub(pat_p4, rep_p4, c_pat_lin, flags=re.DOTALL)
p_pat_lin.write_text(c_pat_lin, encoding="utf-8")

p_pat_inv = BASE / "gr11_patterns_relationships" / "inverse_proportion.py"
c_pat_inv = p_pat_inv.read_text(encoding="utf-8")
pat_p10 = r'(def generate_subskill_10\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_p10 = r'''\1d_spec = {
        "kind": "cartesian_system",
        "title": "Inverse Proportion Hyperbola",
        "lines": [{"name": "Inverse Curve", "points": [{"x": 1, "y": 60}, {"x": 2, "y": 30}, {"x": 4, "y": 15}]}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_pat_inv = re.sub(pat_p10, rep_p10, c_pat_inv, flags=re.DOTALL)
p_pat_inv.write_text(c_pat_inv, encoding="utf-8")

p_pat_exp = BASE / "gr11_patterns_relationships" / "constant_ratio_exponential.py"
c_pat_exp = p_pat_exp.read_text(encoding="utf-8")
pat_p26 = r'(def generate_subskill_26\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_p26 = r'''\1d_spec = {
        "kind": "cartesian_system",
        "title": "Exponential Growth Curve",
        "lines": [{"name": "Growth Curve", "points": [{"x": 0, "y": 100}, {"x": 1, "y": 200}, {"x": 2, "y": 400}]}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_pat_exp = re.sub(pat_p26, rep_p26, c_pat_exp, flags=re.DOTALL)
p_pat_exp.write_text(c_pat_exp, encoding="utf-8")

p_pat_be = BASE / "gr11_patterns_relationships" / "breakeven_business.py"
c_pat_be = p_pat_be.read_text(encoding="utf-8")
pat_p42 = r'(def _gen_subskill_42\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_p42 = r'''\1d_spec = {
        "kind": "break_even",
        "title": f"Business Break-Even Analysis ({item})",
        "fixed_cost": 5000,
        "selling_price": 25,
        "cost_line": {"slope": 15, "intercept": 5000},
        "income_line": {"slope": 25, "intercept": 0},
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_pat_be = re.sub(pat_p42, rep_p42, c_pat_be, flags=re.DOTALL)
p_pat_be.write_text(c_pat_be, encoding="utf-8")
print("Remediated gr11_patterns_relationships")


# ===========================================================================
# 5. gr11_data_handling
# ===========================================================================
print("\n--- Remediating gr11_data_handling ---")

p_dh_ch = BASE / "gr11_data_handling" / "charts_representations.py"
c_dh_ch = p_dh_ch.read_text(encoding="utf-8")
pat_dh41 = r'(def generate_subskill_41\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_dh41 = r'''\1d_spec = {
        "kind": "pie_chart",
        "title": f"Learner Transport Modes ({name})",
        "sectors": [{"label": "Bicycle", "value": 60}, {"label": "Other", "value": 120}],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_dh_ch = re.sub(pat_dh41, rep_dh41, c_dh_ch, flags=re.DOTALL)

pat_dh43 = r'(def generate_subskill_43\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_dh43 = r'''\1d_spec = {
        "kind": "broken_line_graph",
        "title": "Average Monthly Rainfall in Pretoria (mm)",
        "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "values": [120, 110, 85, 45, 20, 10],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_dh_ch = re.sub(pat_dh43, rep_dh43, c_dh_ch, flags=re.DOTALL)
p_dh_ch.write_text(c_dh_ch, encoding="utf-8")

p_dh_an = BASE / "gr11_data_handling" / "analysis_outliers.py"
c_dh_an = p_dh_an.read_text(encoding="utf-8")
pat_dh47 = r'(def generate_subskill_47\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_dh47 = r'''\1d_spec = {
        "kind": "bar_graph",
        "title": "Customer Satisfaction Comparison (Truncated Y-Axis)",
        "categories": ["Company A", "Company B"],
        "values": [92, 95],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_dh_an = re.sub(pat_dh47, rep_dh47, c_dh_an, flags=re.DOTALL)
p_dh_an.write_text(c_dh_an, encoding="utf-8")
print("Remediated gr11_data_handling")


# ===========================================================================
# 6. Single-file generators
# ===========================================================================
print("\n--- Remediating single-file generators ---")

# 6.1 gr11_financial_documents_tariffs_generator.py: subskills 9, 27, 35
p_tariffs = BASE / "gr11_financial_documents_tariffs_generator.py"
c_tar = p_tariffs.read_text(encoding="utf-8")
pat_t9 = r'(def _subskill_9\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return \{'
rep_t9 = r'''\1d_spec = {
        "kind": "bar_graph",
        "title": f"Payslip Deductions Breakdown ({name})",
        "categories": ["PAYE", "UIF", "Pension", "Net Pay"],
        "values": [int(paye), int(uif), int(pension), int(printed_net)],
    }
    return {
        "diagram_spec": d_spec,'''
c_tar = re.sub(pat_t9, rep_t9, c_tar, flags=re.DOTALL)

pat_t27 = r'(def _subskill_27\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return \{'
rep_t27 = r'''\1d_spec = {
        "kind": "step_tariff",
        "title": "Municipal Stepped Water Tariff Graph",
        "blocks": [{"limit": 6, "rate": 12.0}, {"limit": 15, "rate": 24.0}],
    }
    return {
        "diagram_spec": d_spec,'''
c_tar = re.sub(pat_t27, rep_t27, c_tar, flags=re.DOTALL)

pat_t35 = r'(def _subskill_35\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return \{'
rep_t35 = r'''\1d_spec = {
        "kind": "double_bar_graph",
        "title": "Solar Generation vs Grid Consumption",
        "categories": ["Grid Import", "Solar Export"],
        "values": [cost_import, credit_export],
    }
    return {
        "diagram_spec": d_spec,'''
c_tar = re.sub(pat_t35, rep_t35, c_tar, flags=re.DOTALL)
p_tariffs.write_text(c_tar, encoding="utf-8")
print("Remediated gr11_financial_documents_tariffs_generator.py")

# 6.2 gr11_weight_and_temperature_generator.py: subskills 32, 52
p_wt = BASE / "gr11_weight_and_temperature_generator.py"
c_wt = p_wt.read_text(encoding="utf-8")
pat_wt32 = r'(def _subskill_32\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return \{'
rep_wt32 = r'''\1d_spec = {
        "kind": "bar_scale",
        "scale": f"Gross: {_fmt_num(gross_kg)} kg, Tare: {_fmt_num(tare_kg)} kg",
        "segment_value_km": 1,
        "total_km": 5,
        "title": f"Crate Mass Balance Scale ({_fmt_num(gross_kg)} kg)",
    }
    return {
        "diagram_spec": d_spec,'''
c_wt = re.sub(pat_wt32, rep_wt32, c_wt, flags=re.DOTALL)

pat_wt52 = r'(def _subskill_52\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return \{'
rep_wt52 = r'''\1d_spec = {
        "kind": "line_graph",
        "title": f"Environmental Heat Index Chart ({air_t}°C)",
        "categories": ["50% Hum", "60% Hum", "70% Hum"],
        "values": [index_map[(air_t, 50)], index_map[(air_t, 60)], index_map[(air_t, 70)]],
    }
    return {
        "diagram_spec": d_spec,'''
c_wt = re.sub(pat_wt52, rep_wt52, c_wt, flags=re.DOTALL)
p_wt.write_text(c_wt, encoding="utf-8")
print("Remediated gr11_weight_and_temperature_generator.py")

# 6.3 gr11_probability_generator.py: subskills 8, 45
p_prob = BASE / "gr11_probability_generator.py"
c_pr = p_prob.read_text(encoding="utf-8")
# rewrite drawing in prompt
c_pr = c_pr.replace("Calculate the probability of drawing **a Face card", "Calculate the probability of selecting **a Face card")
c_pr = c_pr.replace("Calculate the probability of drawing **two red marbles**", "Calculate the probability of selecting **two red marbles**")

pat_pr8 = r'(def _subskill_8\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return \{'
rep_pr8 = r'''\1d_spec = {
        "kind": "probability_spinner",
        "title": f"52-Card Playing Deck ({card_type})",
        "sectors": [{"label": "Favourable", "value": n_fav}, {"label": "Other", "value": 52 - n_fav}],
    }
    return {
        "diagram_spec": d_spec,'''
c_pr = re.sub(pat_pr8, rep_pr8, c_pr, flags=re.DOTALL)

pat_pr45 = r'(def _subskill_45\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return \{'
rep_pr45 = r'''\1d_spec = {
        "kind": "tree_diagram",
        "title": "Two-Stage Marble Tree (Without Replacement)",
        "branches": ["4 Red", "6 Blue"],
        "outcomes": ["RR", "RB", "BR", "BB"],
    }
    return {
        "diagram_spec": d_spec,'''
c_pr = re.sub(pat_pr45, rep_pr45, c_pr, flags=re.DOTALL)
p_prob.write_text(c_pr, encoding="utf-8")
print("Remediated gr11_probability_generator.py")


# ===========================================================================
# 7. gr11_exchange_rates & gr11_interest_banking_inflation
# ===========================================================================
print("\n--- Remediating exchange rates & interest ---")

p_ex = BASE / "gr11_exchange_rates" / "bank_rates_fees.py"
c_ex = p_ex.read_text(encoding="utf-8")
pat_ex44 = r'(def generate_subskill_44\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_ex44 = r'''\1d_spec = {
        "kind": "bar_graph",
        "title": f"Foreign Currency Conversion ({name})",
        "categories": ["Gross ZAR", "Fees & Comm", "Net Payout"],
        "values": [gross_zar, flat_fee + comm_zar, net_payout],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_ex = re.sub(pat_ex44, rep_ex44, c_ex, flags=re.DOTALL)
p_ex.write_text(c_ex, encoding="utf-8")
print("Remediated gr11_exchange_rates")

p_int = BASE / "gr11_interest_banking_inflation" / "simple_interest.py"
c_int = p_int.read_text(encoding="utf-8")
pat_int8 = r'(def generate_subskill_8\(r: random\.Random\) -> Dict\[str, Any\]:.*?)return _build_question_payload\('
rep_int8 = r'''\1d_spec = {
        "kind": "line_graph",
        "title": f"Simple Interest Growth Graph (Principal R {int(principal)})",
        "categories": ["Year 0", "Year 1", "Year 2", "Year 3"],
        "values": [int(principal), int(principal + annual_interest), int(principal + 2 * annual_interest), int(principal + 3 * annual_interest)],
    }
    return _build_question_payload(
        diagram_spec=d_spec,'''
c_int = re.sub(pat_int8, rep_int8, c_int, flags=re.DOTALL)
p_int.write_text(c_int, encoding="utf-8")
print("Remediated gr11_interest_banking_inflation")

print("\nALL GRADE 11 REMEDIATIONS APPLIED!")
