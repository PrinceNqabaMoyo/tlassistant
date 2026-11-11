"""Grade 9 EMS — Entrepreneurship: Business Plan & Financial Planning.
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/EMS_Gr9/Term 4/02. Business Plan.md` & `Syllabus.md`.
Covers:
- Concept, purpose, and key components of a Business Plan (Executive Summary, Production, Marketing, Management, Financial)
- SWOT Analysis matrix (Strengths, Weaknesses, Opportunities, Threats) in a South African small business scenario
- Financial Planning: Fixed costs vs Variable costs classification
- Break-even point calculations: Break-even units = Fixed Costs / (Selling Price - Variable Cost)
- Contribution margin, mark-up percentage, and target profit calculations
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario

def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r

TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term4_business_plan"
CURRICULUM_REFERENCE = "Term 4 > Entrepreneurship: Business Plan"

def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: Optional[str] = None,
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": TOPIC_ID,
        "subtopic_id": SUBTOPIC_ID,
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id or subskill,
        "concept_group": concept_group or "business_plan",
        "question_family_id": question_family_id,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["entrepreneurship", "business_plan", "financial_planning"],
    })
    return enriched

# --------------------------------------------------------------------------- #
# Sub-Drill 1: Break-even Analysis & Financial Calculations
# --------------------------------------------------------------------------- #
def _generate_breakeven_drill(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    business_name = f"{scenario['entrepreneur']}'s Crafts"
    product = rng.choice(["Handmade Beaded Handbags", "Recycled Canvas Backpacks", "Organic Herbal Teas", "Solar Desk Lamps"])
    
    # Clean numbers for integer break-even:
    # SP = 250, VC = 150 -> CM = 100. FC = 15000 -> BEP = 150 units.
    sp = rng.choice([150, 200, 250, 300, 400])
    margin_ratio = rng.choice([0.4, 0.5, 0.6]) # CM / SP
    cm = int(sp * margin_ratio)
    vc = sp - cm
    
    bep_units = rng.choice([50, 80, 100, 120, 150, 200])
    fixed_costs = bep_units * cm
    
    target_profit = rng.choice([5000, 10000, 15000])
    target_units = (fixed_costs + target_profit) // cm
    
    prompt = (
        f"**{business_name}** produces and sells **{product}** in the local South African market.\n"
        f"The entrepreneur's financial plan provides the following cost estimates:\n\n"
        f"• **Selling Price per unit (SP)**: R{sp}\n"
        f"• **Variable Cost per unit (VC)** (raw materials & direct packaging): R{vc}\n"
        f"• **Total Monthly Fixed Costs (FC)** (workshop rent, equipment depreciation, supervisor salary): R{fixed_costs:,}\n\n"
        f"**Required:**\n"
        f"1. Calculate the **Contribution Margin per unit** (\\(\\text{{CM}} = \\text{{SP}} - \\text{{VC}}\\)).\n"
        f"2. Use the standard break-even formula to calculate the **Break-even Point in units**:\n"
        f"\\[ \\text{{Break-even units}} = \\frac{{\\text{{Fixed Costs}}}}{{\\text{{Selling Price}} - \\text{{Variable Cost}}}} \\]\n"
        f"3. Calculate the number of units the business must sell to achieve a **target monthly profit of R{target_profit:,}**."
    )
    
    sample_ans = (
        f"1. Contribution Margin per unit = SP - VC = R{sp} - R{vc} = R{cm} per unit.\n\n"
        f"2. Break-even Point in units = Fixed Costs / CM per unit = R{fixed_costs:,} / R{cm} = {bep_units} units.\n\n"
        f"3. Units for Target Profit = (Fixed Costs + Target Profit) / CM per unit = (R{fixed_costs:,} + R{target_profit:,}) / R{cm} = R{fixed_costs + target_profit:,} / R{cm} = {target_units} units."
    )
    
    item = {
        "id": f"ems9_bp_breakeven_{rng.randint(1000, 9999)}",
        "title": f"Business Plan Financials: Break-even Analysis ({product})",
        "question_type": "typed",
        "modality": "math",
        "prompt": prompt,
        "marks": 8,
        "sample_answer": sample_ans,
        "ideal_answer": sample_ans,
        "worked_solution": sample_ans,
        "marking_points": [
            f"Contribution Margin: R{sp} - R{vc} = R{cm} per unit (2 marks)",
            f"Break-even Point: R{fixed_costs:,} / R{cm} = {bep_units} units (4 marks)",
            f"Target Profit units: (R{fixed_costs:,} + R{target_profit:,}) / R{cm} = {target_units} units (2 marks)",
        ],
        "hint_sections": {
            "1_nudge": "Contribution margin is how much each unit sold contributes towards paying off fixed costs.",
            "2_concept": r"Break-even point is where Total Revenue = Total Costs (Zero profit and zero loss). Formula: \text{FC} / (\text{SP} - \text{VC}).",
            "3_breakdown": f"Step 1: R{sp} - R{vc} = R{cm}. Step 2: R{fixed_costs:,} / R{cm} = {bep_units} units. Step 3: R{fixed_costs + target_profit:,} / R{cm} = {target_units} units."
        },
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": "mp_cm", "desc": f"Contribution Margin: R{cm}", "marks": 2, "editable": True},
                {"id": "mp_bep", "desc": f"Break-even Point: {bep_units} units", "marks": 4, "editable": True},
                {"id": "mp_target", "desc": f"Target profit units: {target_units} units", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confused_fixed_and_variable_costs", "divided_fixed_costs_by_selling_price_instead_of_contribution_margin"],
    }
    return _with_metadata(
        item,
        subskill="breakeven_analysis",
        learning_objective_id="lo_g9_breakeven_analysis",
        question_family_id="breakeven_calculation",
        misconception_tags=["confused_fixed_and_variable_costs", "divided_fixed_costs_by_selling_price_instead_of_contribution_margin"],
    )

# --------------------------------------------------------------------------- #
# Sub-Drill 2: Fixed vs Variable Cost Classification Table
# --------------------------------------------------------------------------- #
def _generate_cost_classification_drill(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    cost_pool = [
        ("Monthly rent for factory premises", "Fixed Cost", "Must be paid regardless of whether production is zero or at maximum capacity."),
        ("Raw materials (wood, fabric, steel) used in manufacturing", "Variable Cost", "Cost increases directly in proportion to the number of units produced."),
        ("Direct product packaging boxes and labels", "Variable Cost", "More goods produced require more packaging containers."),
        ("Monthly premium for factory fire and theft insurance", "Fixed Cost", "The policy premium remains constant every month regardless of output."),
        ("Sales commission paid to agents (R15 per unit sold)", "Variable Cost", "Total commission paid fluctuates directly with sales volume."),
        ("Salary of the general factory manager", "Fixed Cost", "A salaried manager receives a contracted monthly payment unaffected by output changes."),
        ("Electricity consumed by heavy production machinery", "Variable Cost", "Operating the machinery longer to produce more units consumes more kilowatt-hours."),
        ("Repayment of bank business vehicle loan interest", "Fixed Cost", "The financial interest obligation remains fixed every month."),
    ]
    
    selected = rng.sample(cost_pool, 4)
    headers = ["Expense Item", "Cost Classification (Fixed vs Variable)", "Economic Justification"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    
    for idx, (item_desc, classification, justification) in enumerate(selected):
        c_class = f"t0_r{idx}_c1"
        correct_map[c_class] = classification
        cell_hints[c_class] = f"Does '{item_desc}' stay constant (Fixed) or change with production volume (Variable)?"
        
        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "value": item_desc, "type": "given", "editable": False},
            {"coordinate": c_class, "value": classification if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c2", "value": justification, "type": "given", "editable": False},
        ])
        
    prompt = (
        "In the Financial Plan section of a Business Plan, costs must be classified correctly to calculate break-even targets.\n"
        "Classify each of the following business expenses as either a **Fixed Cost** or a **Variable Cost**."
    )
    
    item = {
        "id": f"ems9_bp_costs_{rng.randint(1000, 9999)}",
        "title": "Cost Classification: Fixed Costs vs. Variable Costs",
        "question_type": "table_completion",
        "modality": "ledger",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "journal": {
            "journal_type": "cost_classification",
            "headers": headers,
            "rows": rows,
        },
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 8,
        "sample_answer": f"Row 1: {selected[0][1]}; Row 2: {selected[1][1]}; Row 3: {selected[2][1]}; Row 4: {selected[3][1]}",
        "ideal_answer": "Accurate classification of operational expenses into Fixed and Variable costs.",
        "hint_sections": {
            "1_nudge": "Ask yourself: If we close the factory for a month and produce zero units, do we still have to pay this expense?",
            "2_concept": "Fixed costs remain constant regardless of production output. Variable costs increase or decrease directly with the number of units produced.",
            "3_breakdown": "Rent, insurance, and salaries are fixed. Raw materials, packaging, and unit commissions are variable."
        },
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": f"mp_{i}", "desc": f"Correct classification for '{itm[0][:30]}...'", "marks": 2, "editable": True}
                for i, itm in enumerate(selected)
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["treated_rent_as_variable", "treated_raw_materials_as_fixed"],
    }
    return _with_metadata(
        item,
        subskill="cost_classification",
        learning_objective_id="lo_g9_cost_classification",
        question_family_id="fixed_variable_table",
        misconception_tags=["treated_rent_as_variable", "treated_raw_materials_as_fixed"],
    )

# --------------------------------------------------------------------------- #
# Sub-Drill 3: SWOT Analysis Matrix Drill
# --------------------------------------------------------------------------- #
def _generate_swot_drill(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    business_name = f"{scenario['entrepreneur']}'s Bakery & Cafe"
    
    swot_items = [
        ("The business owns an authentic, secret family recipe for artisan sourdough bread.", "Strength", "Internal positive factor that gives a competitive advantage."),
        ("The business currently has limited working capital and cannot afford delivery vans.", "Weakness", "Internal limitation that restricts current business performance."),
        ("A new office park and high school are opening 200 metres from the shop.", "Opportunity", "External positive market trend that the business can exploit for growth."),
        ("Load shedding and municipal water outages frequently interrupt the baking ovens.", "Threat", "External negative risk that can harm production and sales."),
    ]
    
    headers = ["Business Scenario / Observation", "SWOT Quadrant (Strength / Weakness / Opportunity / Threat)", "Nature (Internal vs External)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    
    for idx, (obs, quadrant, nature) in enumerate(swot_items):
        c_quad = f"t0_r{idx}_c1"
        c_nat = f"t0_r{idx}_c2"
        correct_map[c_quad] = quadrant
        correct_map[c_nat] = "Internal" if quadrant in ["Strength", "Weakness"] else "External"
        
        cell_hints[c_quad] = f"Is this a Strength (internal +), Weakness (internal -), Opportunity (external +), or Threat (external -)?"
        cell_hints[c_nat] = f"Strengths and Weaknesses are INTERNAL. Opportunities and Threats are EXTERNAL."
        
        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "value": obs, "type": "given", "editable": False},
            {"coordinate": c_quad, "value": quadrant if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": c_nat, "value": ("Internal" if quadrant in ["Strength", "Weakness"] else "External") if mode == "scaffold" else "", "type": "required", "editable": True},
        ])
        
    prompt = (
        f"**{business_name}** is preparing a formal Business Plan to apply for finance from a South African commercial bank.\n"
        f"Conduct a **SWOT Analysis** by categorising each scenario observation into the correct SWOT quadrant "
        f"and stating whether it represents an **Internal** or **External** business factor."
    )
    
    item = {
        "id": f"ems9_bp_swot_{rng.randint(1000, 9999)}",
        "title": "SWOT Analysis Matrix (Small Business Planning)",
        "question_type": "table_completion",
        "modality": "ledger",
        "prompt": prompt,
        "headers": headers,
        "rows": rows,
        "journal": {
            "journal_type": "swot_analysis",
            "headers": headers,
            "rows": rows,
        },
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 8,
        "sample_answer": "1: Strength (Internal); 2: Weakness (Internal); 3: Opportunity (External); 4: Threat (External)",
        "ideal_answer": "Complete SWOT Matrix accurately identifying internal advantages/disadvantages and external opportunities/threats.",
        "hint_sections": {
            "1_nudge": "Strengths & Weaknesses come from INSIDE the business. Opportunities & Threats come from the OUTSIDE market.",
            "2_concept": "S (Strength) = Internal Positive; W (Weakness) = Internal Negative; O (Opportunity) = External Positive; T (Threat) = External Negative.",
            "3_breakdown": "Recipe is Strength. Capital shortage is Weakness. New office park is Opportunity. Outages are Threat."
        },
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": f"mp_{i}", "desc": f"Item {i+1}: {swot_items[i][1]} ({'Internal' if swot_items[i][1] in ['Strength', 'Weakness'] else 'External'})", "marks": 2, "editable": True}
                for i in range(4)
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confused_internal_and_external_factors", "confused_opportunity_with_strength"],
    }
    return _with_metadata(
        item,
        subskill="swot_analysis",
        learning_objective_id="lo_g9_swot_analysis",
        question_family_id="swot_table",
        misconception_tags=["confused_internal_and_external_factors", "confused_opportunity_with_strength"],
    )

BUILDERS = {
    "breakeven_analysis": lambda rng, mode: [_generate_breakeven_drill(rng, mode)],
    "cost_classification": lambda rng, mode: [_generate_cost_classification_drill(rng, mode)],
    "swot_analysis": lambda rng, mode: [_generate_swot_drill(rng, mode)],
    "concepts": lambda rng, mode: [_generate_breakeven_drill(rng, mode)],
}

def generate(
    subskill: str = "breakeven_analysis",
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    builder = BUILDERS.get(subskill)
    if builder is not None:
        pool = builder(rng, mode)
    else:
        pool = [
            _generate_breakeven_drill(rng, mode),
            _generate_cost_classification_drill(rng, mode),
            _generate_swot_drill(rng, mode),
        ]

    if count == 1 and seed is not None:
        selected = [pool[int(seed) % len(pool)]]
    elif count < len(pool):
        selected = rng.sample(pool, count)
    else:
        selected = pool
    return selected
