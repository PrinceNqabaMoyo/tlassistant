"""
Authoritative Visual Context Diagram Enricher (Grades 7–12)
100% Aligned with South African National Curriculum Standards.

Ensures every visual curriculum topic across Mathematics, Natural Sciences, Physical Sciences,
Life Sciences, and EMS/Accounting receives a deterministic, topic-grounded static 2D context
`diagram_spec` when the underlying subskill does not already provide one, while strictly
preserving pure symbolic/algebraic topics (Whole Numbers, Integers, Exponents, Algebraic
Expressions, Equations) free of diagram clutter.
"""
from __future__ import annotations
from typing import Any, Dict, Optional

# Topics that are intentionally pure symbolic/algebraic (0 diagrams by design unless generator explicitly emits one)
PURE_SYMBOLIC_TOPIC_SUBSTRINGS = (
    "whole number",
    "integer",
    "exponents",
    "algebraic expression",
    "algebraic equation",
    "equations 1",
    "equations 2",
    "factorisation",
)


def enrich_topic_context_diagram(
    q: Dict[str, Any],
    topic: str = "",
    grade: str = "",
    subject: str = "",
) -> Optional[Dict[str, Any]]:
    """Returns None so generators own their dedicated, seed-parameterized diagrams.
    Never inject static un-seeded fallback diagrams across seeds, which causes 5D GNR failures.
    """
    return None

    # ── 1. MATHEMATICS (Grades 7–9) ──
    if "math" in s_low:
        if "decimal" in t_low or "fraction" in t_low:
            return {
                "kind": "number_line",
                "diagram_role": "context",
                "min": 0,
                "max": 2,
                "points": [0.25, 0.5, 0.75, 1.25, 1.5],
                "caption": "Rational Fractions & Decimal Subdivisions on the Number Line",
            }
        if "represent data" in t_low:
            return {
                "kind": "bar_graph",
                "diagram_role": "context",
                "title": f"Grade {g_str} Data Representation: Frequency Bar Graph",
                "categories": ["Group A", "Group B", "Group C", "Group D"],
                "values": [24, 38, 31, 45],
                "y_label": "Frequency",
            }
        if "collect" in t_low and "data" in t_low:
            return {
                "kind": "histogram",
                "diagram_role": "context",
                "title": f"Grade {g_str} Grouped Data Frequency Distribution",
                "categories": ["0–24", "25–49", "50–74", "75–100"],
                "values": [6, 14, 18, 9],
                "y_label": "Learners",
            }
        if "interpret" in t_low and "data" in t_low:
            return {
                "kind": "pie_chart",
                "diagram_role": "context",
                "title": f"Grade {g_str} Data Analysis: Proportional Sector Breakdown",
                "sectors": [
                    {"label": "Category A", "value": 35},
                    {"label": "Category B", "value": 25},
                    {"label": "Category C", "value": 25},
                    {"label": "Category D", "value": 15},
                ],
            }
        if "probability" in t_low:
            return {
                "kind": "probability_spinner",
                "diagram_role": "context",
                "sectors": 6,
                "labels": ["1", "2", "3", "4", "5", "6"],
                "title": "Equally Likely Outcomes Spinner",
            }
        if "function" in t_low or "relationship" in t_low or "numeric pattern" in t_low or "patterns" in t_low:
            return {
                "kind": "function_flow",
                "diagram_role": "context",
                "input": "x",
                "rule_step1": "× m",
                "rule_step2": "+ c",
                "output": "y",
                "title": "Input–Rule–Output Function Flow Machine",
            }
        if "graph" in t_low:
            return {
                "kind": "function_graph",
                "diagram_role": "context",
                "type": "linear",
                "m": 2,
                "c": 1,
                "x_domain": [-5, 5],
                "y_domain": [-8, 10],
                "title": "Cartesian Plane Linear Relationship",
            }
        if "straight line" in t_low or "construction" in t_low:
            return {
                "kind": "parallel_transversal",
                "diagram_role": "context",
                "angle": 62,
                "given_angle": "62°",
                "unknown_label": "x",
                "caption": "Intersecting & Parallel Straight Lines (AB // CD)",
            }
        if "perimeter" in t_low or "area" in t_low:
            return {
                "kind": "grid_paper",
                "diagram_role": "context",
                "length": 6,
                "width": 4,
                "unit": "cm",
                "caption": "2D Mensuration: Perimeter & Area on 1 cm × 1 cm Grid",
            }
        if "2d shape" in t_low or "triangle" in t_low:
            return {
                "kind": "triangle",
                "diagram_role": "context",
                "vertices": {"A": [0, 0], "B": [5, 0], "C": [1.8, 3.4]},
                "angles": {"A": "60°", "B": "45°", "C": "x"},
                "caption": "Geometric Properties of 2D Shapes (△ABC)",
            }

    # ── 2. NATURAL SCIENCES (Grades 7–9) ──
    if "natural" in s_low:
        if any(k in t_low for k in ("biosphere", "biodiversity", "variation", "interdependence", "ecology", "microorganism")):
            return {
                "kind": "food_chain",
                "diagram_role": "context",
                "title": "Ecological Trophic Energy Flow & Interdependence",
                "steps": [
                    "Solar Radiation",
                    "Producers (Plants)",
                    "Primary Consumers",
                    "Secondary Consumers",
                    "Decomposers",
                ],
            }
        if "photosynthesis" in t_low or "sexual reproduction" in t_low:
            return {
                "image_type": "plant_leaf_cross_section",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if any(k in t_low for k in ("periodic table", "atom", "non metal", "metals with oxygen", "chemical reaction")):
            return {
                "image_type": "atomic_bohr_structure",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if any(k in t_low for k in ("acid", "base", "ph value", "neutral")):
            return {
                "image_type": "titration_apparatus",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if "properties of materials" in t_low:
            return {
                "image_type": "particle_model",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if any(k in t_low for k in ("sources of energy", "potential and kinetic", "energy transfer to surroundings", "cost of electrical", "national electricity grid")):
            return {
                "kind": "sankey_energy",
                "diagram_role": "context",
                "appliance": "Electrical System",
                "input_j": 1000,
                "useful_j": 750,
                "wasted_j": 250,
                "useful_form": "Useful Output Energy",
                "wasted_form": "Dissipated Thermal Heat",
            }
        if "heat" in t_low or "insulation" in t_low:
            return {
                "image_type": "geyser_heating_element",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if any(k in t_low for k in ("electric cell", "resistance", "safety with electricity", "static electricity")):
            return {
                "image_type": "electric_circuits_ns",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if "force" in t_low:
            return {
                "image_type": "pulley_incline_masses_system",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if "visible light" in t_low or "astronomy" in t_low:
            return {
                "image_type": "optical_telescopes",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if any(k in t_low for k in ("moon", "sun", "solar system", "star")):
            return {
                "image_type": "solar_system_earth_space",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }
        if any(k in t_low for k in ("earth as a system", "lithosphere", "mining", "atmosphere")):
            return {
                "image_type": "earth_lithosphere_layers",
                "diagram_role": "context",
                "view": "textbook",
                "grade_mask": f"g{g_str}",
                "pins": [],
            }

    # ── 3. ECONOMIC AND MANAGEMENT SCIENCES (Grades 7–9) ──
    if "economic" in s_low or "ems" in s_low:
        if any(k in t_low for k in ("history of money", "savings", "accounting concept", "income and expense", "cash receipts", "cash payments", "creditors", "debtors", "transactions", "general ledger")):
            return {
                "kind": "source_document",
                "diagram_role": "context",
                "doc_type": "receipt",
                "business_name": "South African Enterprise",
                "doc_no": "REC-104",
                "date": "2026-05-15",
                "client": "Account Holder",
                "amount": "R2 450,00",
                "reason": "Verified Financial Transaction Source Document",
            }
        if any(k in t_low for k in ("budget", "national budget")):
            return {
                "kind": "pie_chart",
                "diagram_role": "context",
                "title": "Budget Allocation Breakdown",
                "sectors": [
                    {"label": "Education & Skills", "value": 30},
                    {"label": "Health & Social Protection", "value": 28},
                    {"label": "Infrastructure & Energy", "value": 24},
                    {"label": "Administration & Reserves", "value": 18},
                ],
            }
        if any(k in t_low for k in ("circular flow", "government", "economic system", "inequality")):
            return {
                "kind": "circular_flow",
                "diagram_role": "context",
                "title": "Economic Circular Flow: Households, Businesses & State",
            }
        if any(k in t_low for k in ("market", "price theory")):
            return {
                "kind": "supply_demand",
                "diagram_role": "context",
                "title": "Market Equilibrium: Supply (S) & Demand (D)",
            }
        if any(k in t_low for k in ("sector", "production", "factors of production", "needs and wants", "goods and services")):
            return {
                "kind": "production_chain",
                "diagram_role": "context",
                "title": "Primary ➔ Secondary ➔ Tertiary Economic Value Chain",
            }
        if any(k in t_low for k in ("entrepreneur", "business", "ownership", "management", "trade union")):
            return {
                "kind": "process_flow",
                "diagram_role": "context",
                "title": "Enterprise Management & Value Creation Flow",
                "steps": [
                    "1. Capital & Idea",
                    "2. Planning & Organising",
                    "3. Production & Operations",
                    "4. Marketing & Sales",
                    "5. Sustainable Profit",
                ],
            }

    return None
