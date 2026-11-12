"""Grade 7 EMS — The Production Process: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards (Term 4: The Economy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 3/03. The production process.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS

from .term3_production_process_archetypes_01_25 import (
    _fmt_comma,
    _fmt_zar,
    _mcq,
    _svg_bar_chart,
    _svg_cycle_flow,
    _table_q,
    _typed,
)


def arch_26_economic_growth_definition_and_gdp(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice(["2,4%", "3,2%", "3,8%", "4,1%"])
    prompt = (
        f"Economists report that South Africa achieved an annual increase of {pct} in the total real value of goods "
        f"and services (Gross Domestic Product) produced across the country.\n\n"
        f"Which term BEST describes this expansion in total national output from one year to the next?"
    )
    correct = "Economic growth"
    distractors = [
        "Price inflation",
        "Consumer rationing",
        "Resource depletion",
    ]
    return _mcq(
        rng,
        subskill="26_economic_growth_definition_and_gdp",
        title="Meaning of Economic Growth and GDP",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Economic growth means an economy produces a higher total value of goods and services (real GDP) than in "
            f"the previous year — here rising by {pct}."
        ),
        hints={
            "tier_1": "Look for the macro-economic term describing an increase in a country's total real output (GDP).",
            "tier_2": "Inflation measures rising price levels, whereas rising real production capacity is economic growth.",
            "tier_3": "Select 'Economic growth'.",
        },
        learning_objective_id="lo_prod_economic_growth_def",
        concept_id="economic_growth_gdp",
        misconception_tags=["confuses_economic_growth_with_inflation"],
    )


def arch_27_gdp_growth_rate_calculation(rng: random.Random) -> Dict[str, Any]:
    gdp_prev = rng.choice([2000, 2500, 3000, 4000])
    growth_pct = rng.choice([2.5, 3.0, 3.2, 4.0])
    increase = round(gdp_prev * growth_pct / 100.0, 1)
    gdp_curr = round(gdp_prev + increase, 1)
    prompt = (
        f"A country's Gross Domestic Product (GDP) rises from {_fmt_zar(gdp_prev)} billion last year to "
        f"{_fmt_zar(gdp_curr, 1)} billion this year.\n\n"
        f"Calculate the annual percentage economic growth rate."
    )
    return _typed(
        rng,
        subskill="27_gdp_growth_rate_calculation",
        title="Calculating Annual GDP Growth Rate",
        prompt=prompt,
        sample_answer=(
            f"GDP increase = R{_fmt_comma(gdp_curr, 1)}B - R{gdp_prev}B = R{_fmt_comma(increase, 1)}B\n"
            f"Growth rate = ({_fmt_comma(increase, 1)} / {gdp_prev}) x 100 = {_fmt_comma(growth_pct, 1)}%"
        ),
        marking_points=[
            f"Find increase: R{_fmt_comma(increase, 1)} billion [1]",
            f"Divide by base GDP ({gdp_prev}) and multiply by 100 [1]",
            f"Correct growth rate = {_fmt_comma(growth_pct, 1)}% [1]",
        ],
        hints={
            "tier_1": "First subtract last year's GDP from this year's GDP to get the Rand increase.",
            "tier_2": f"Divide the increase (R{_fmt_comma(increase, 1)}B) by the starting GDP (R{gdp_prev}B), then x 100.",
            "tier_3": f"({_fmt_comma(increase, 1)} / {gdp_prev}) x 100 = {_fmt_comma(growth_pct, 1)}%.",
        },
        learning_objective_id="lo_prod_gdp_growth_calc",
        concept_id="gdp_growth_calculation",
        misconception_tags=["divides_by_new_gdp_instead_of_base"],
        marks=3,
        correct_answer=f"{_fmt_comma(growth_pct, 1)}%",
        correct_value=float(growth_pct),
        worked_solution=(
            f"Growth rate = (({gdp_curr} - {gdp_prev}) / {gdp_prev}) x 100 = {_fmt_comma(growth_pct, 1)}%"
        ),
    )


def arch_28_economic_growth_bar_graph_trend(rng: random.Random) -> Dict[str, Any]:
    y1 = round(rng.uniform(2.1, 3.1), 1)
    y2 = round(rng.uniform(2.6, 3.4), 1)
    y3 = round(rng.uniform(1.6, 2.2), 1)
    y4 = round(rng.uniform(3.2, 4.2), 1)
    diff = round(y4 - y3, 1)

    svg = _svg_bar_chart(
        title="Annual Real GDP Growth Rate (%)",
        y_label="GDP Growth (%)",
        bars=[
            ("Year 1", y1, "#0284C7"),
            ("Year 2", y2, "#0284C7"),
            ("Year 3", y3, "#DC2626"),
            ("Year 4", y4, "#15803D"),
        ],
        max_val=5.0,
        unit_suffix="%",
    )
    prompt = (
        f"Refer to the bar graph below tracking a country's annual real GDP growth rate: Year 1 ({_fmt_comma(y1, 1)}%), "
        f"Year 2 ({_fmt_comma(y2, 1)}%), Year 3 ({_fmt_comma(y3, 1)}%), and Year 4 ({_fmt_comma(y4, 1)}%).\n\n"
        f"Calculate the percentage-point difference between the fastest growth year (Year 4) and the slowest growth year (Year 3)."
    )
    return _typed(
        rng,
        subskill="28_economic_growth_bar_graph_trend",
        title="GDP Growth Trend Analysis (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Difference = {_fmt_comma(y4, 1)}% - {_fmt_comma(y3, 1)}% = {_fmt_comma(diff, 1)} percentage points.",
        marking_points=[
            f"Read highest ({_fmt_comma(y4, 1)}%) and lowest ({_fmt_comma(y3, 1)}%) bars [1]",
            f"Calculate difference = {_fmt_comma(diff, 1)} percentage points [2]",
        ],
        hints={
            "tier_1": "Compare the green Year 4 bar against the red Year 3 bar.",
            "tier_2": f"Subtract {_fmt_comma(y3, 1)}% from {_fmt_comma(y4, 1)}%.",
            "tier_3": f"{_fmt_comma(y4, 1)}% - {_fmt_comma(y3, 1)}% = {_fmt_comma(diff, 1)} percentage points.",
        },
        learning_objective_id="lo_prod_gdp_trend_graph",
        concept_id="gdp_growth_graph",
        misconception_tags=["adds_growth_rates_instead_of_subtracting"],
        marks=3,
        correct_answer=f"{_fmt_comma(diff, 1)} percentage points",
        correct_value=float(diff),
        diagram_spec={"kind": "inline_svg", "title": "Annual Real GDP Growth Rate", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Difference = {y4} - {y3} = {_fmt_comma(diff, 1)} percentage points",
    )


def arch_29_productivity_definition_output_per_input(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"A bottling workshop in {area} compares how many litres of juice are packaged per hour of labour used.\n\n"
        f"Which formula and meaning BEST define PRODUCTIVITY?"
    )
    correct = "Output divided by Input — measuring how efficiently resources are converted into goods and services"
    distractors = [
        "Total Selling Price minus Electricity Bill regardless of hours worked",
        "Hiring double the workers without increasing output at all",
        "Input multiplied by Selling Price without counting units produced",
    ]
    return _mcq(
        rng,
        subskill="29_productivity_definition_output_per_input",
        title="Definition and Formula of Productivity",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Productivity measures efficiency: Output / Input. Higher productivity means producing more output per worker, "
            "per machine hour, or per unit of raw material."
        ),
        hints={
            "tier_1": "Remember the ratio linking what comes OUT (goods) to what goes IN (hours/resources).",
            "tier_2": "Productivity = Output / Input.",
            "tier_3": "Select 'Output divided by Input — measuring how efficiently resources are converted into goods and services'.",
        },
        learning_objective_id="lo_prod_productivity_def",
        concept_id="productivity_definition",
        misconception_tags=["confuses_productivity_with_total_output"],
    )


def arch_30_productivity_ratio_calculation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    hours = rng.choice([8, 10, 12])
    per_hr = rng.randint(14, 24)
    total_units = hours * per_hr
    prompt = (
        f"At a woodworking co-op in {area}, artisans assemble {total_units} wooden stools during a {hours}-hour shift.\n\n"
        f"Calculate the labour productivity in stools per hour."
    )
    return _typed(
        rng,
        subskill="30_productivity_ratio_calculation",
        title="Calculating Labour Productivity Ratio",
        prompt=prompt,
        sample_answer=f"Productivity = Output / Input = {total_units} stools / {hours} hours = {per_hr} stools per hour.",
        marking_points=[
            f"Apply Productivity = Output / Input = {total_units} / {hours} [1]",
            f"Correct answer = {per_hr} stools per hour [1]",
        ],
        hints={
            "tier_1": "Divide Total Output (stools) by Total Input (hours).",
            "tier_2": f"Calculate {total_units} / {hours}.",
            "tier_3": f"{total_units} / {hours} = {per_hr} stools/hour.",
        },
        learning_objective_id="lo_prod_ratio_calc",
        concept_id="productivity_calculation",
        misconception_tags=["inverts_input_over_output"],
        marks=2,
        correct_answer=f"{per_hr} stools/hour",
        correct_value=float(per_hr),
        worked_solution=f"Productivity = {total_units} / {hours} = {per_hr} stools per hour",
    )


def arch_31_productivity_comparison_bar_graph(rng: random.Random) -> Dict[str, Any]:
    s1 = rng.randint(18, 24)
    s2 = rng.randint(25, 31)
    s3 = rng.randint(33, 42)
    gain = s3 - s1

    svg = _svg_bar_chart(
        title="Factory Productivity: Units Packed per Worker-Hour",
        y_label="Units / Hour",
        bars=[
            ("Shift A", float(s1), "#DC2626"),
            ("Shift B", float(s2), "#D97706"),
            ("Shift C", float(s3), "#15803D"),
        ],
        max_val=50.0,
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below showing productivity per worker-hour across three shifts after introducing "
        f"training: Shift A ({s1} units/hr), Shift B ({s2} units/hr), and Shift C ({s3} units/hr).\n\n"
        f"Calculate how many MORE units per worker-hour Shift C produces compared with Shift A."
    )
    return _typed(
        rng,
        subskill="31_productivity_comparison_bar_graph",
        title="Comparing Shift Productivity (Bar Graph)",
        prompt=prompt,
        sample_answer=f"Productivity gain = {s3} - {s1} = {gain} more units per worker-hour.",
        marking_points=[
            f"Read Shift C ({s3}) and Shift A ({s1}) correctly [1]",
            f"Calculate difference = {s3} - {s1} = {gain} units/hour [2]",
        ],
        hints={
            "tier_1": "Locate the height of Shift C (green) and Shift A (red).",
            "tier_2": f"Subtract {s1} from {s3}.",
            "tier_3": f"{s3} - {s1} = {gain} units per worker-hour.",
        },
        learning_objective_id="lo_prod_productivity_graph",
        concept_id="productivity_bar_graph",
        misconception_tags=["compares_shift_b_instead_of_a"],
        marks=3,
        correct_answer=f"{gain} units/hour",
        correct_value=float(gain),
        diagram_spec={"kind": "inline_svg", "title": "Factory Shift Productivity", "svg": svg, "diagram_role": "context"},
        worked_solution=f"Shift C vs Shift A = {s3} - {s1} = {gain} units/hour",
    )


def arch_32_productivity_ledger_comparison_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    h1 = 10
    p1 = rng.randint(15, 22)
    out1 = h1 * p1
    h2 = 8
    p2 = p1 + rng.randint(5, 9)
    out2 = h2 * p2

    headers = ["Production Team", "Total Units (Output)", "Labour Hours (Input)", "Productivity (Units/Hr)", "Notes"]
    raw_rows = [
        [
            {"type": "given", "value": "Morning Team"},
            {"type": "given", "value": str(out1)},
            {"type": "given", "value": str(h1)},
            {"type": "required", "expected": str(p1)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Afternoon Team"},
            {"type": "given", "value": str(out2)},
            {"type": "given", "value": str(h2)},
            {"type": "required", "expected": str(p2)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "More Productive Team"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "required", "expected": "Afternoon Team"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Divide {out1} units by {h1} hours.",
        "r1_c3": f"Divide {out2} units by {h2} hours.",
        "r2_c3": "Enter the team name with higher Units/Hr ('Afternoon Team').",
    }
    derivations = [
        f"Morning Team = {out1} / {h1} = {p1} units/hr.",
        f"Afternoon Team = {out2} / {h2} = {p2} units/hr.",
        f"Since {p2} > {p1}, Afternoon Team is more productive even with fewer hours.",
    ]
    return _table_q(
        rng,
        subskill="32_productivity_ledger_comparison_table",
        title="Team Productivity Comparison Schedule",
        prompt=(
            f"Complete the productivity schedule for two sewing teams in {area} using Productivity = Output / Input. "
            f"Leave shaded cells and 'Notes' completely empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Use Output / Input for both Morning Team and Afternoon Team.",
            "tier_2": "Do NOT confuse higher Total Units with higher Productivity per hour.",
            "tier_3": f"Morning={p1}; Afternoon={p2}; More Productive Team='Afternoon Team'.",
        },
        learning_objective_id="lo_prod_productivity_table",
        concept_id="productivity_comparison_table",
        misconception_tags=["picks_team_with_more_total_hours", "fills_must_be_empty_cell"],
    )


def arch_33_improving_productivity_without_extra_inputs(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(["bakery", "brickyard", "printing press"])
    prompt = (
        f"A {biz} owner in {area} wants to boost output per worker-hour without buying extra land or hiring more staff.\n\n"
        f"Which combination BEST increases workplace productivity?"
    )
    correct = (
        "Targeted worker training, well-maintained tools/equipment, logical floor workflow, and fair motivation incentives"
    )
    distractors = [
        "Forcing workers to guess safety procedures with broken tools and zero training",
        "Cancelling tea breaks and delaying raw-material deliveries randomly",
        "Cutting preventative machine maintenance until ovens break down weekly",
    ]
    return _mcq(
        rng,
        subskill="33_improving_productivity_without_extra_inputs",
        title="Ways to Improve Productivity",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Training workers, maintaining modern equipment, reducing wasted movement on the workshop floor, and rewarding "
            "performance enable the same workforce to produce more high-quality output."
        ),
        hints={
            "tier_1": "Think about skills, equipment reliability, and staff motivation.",
            "tier_2": "Broken tools and poorly trained workers cause waste and downtime.",
            "tier_3": "Select 'Targeted worker training, well-maintained tools/equipment, logical floor workflow, and fair motivation incentives'.",
        },
        learning_objective_id="lo_prod_improve_productivity",
        concept_id="productivity_improvement",
        misconception_tags=["thinks_overworking_broken_machines_helps"],
    )


def arch_34_sa_productivity_challenge_unemployment_poverty(rng: random.Random) -> Dict[str, Any]:
    unemp = rng.choice([25, 29, 32])
    area = rng.choice(AREAS)
    prompt = (
        f"In communities near {area} experiencing {unemp}% unemployment and widespread poverty, explain TWO ways low "
        f"household incomes and unemployment weaken South Africa's broader economic productivity."
    )
    return _typed(
        rng,
        subskill="34_sa_productivity_challenge_unemployment_poverty",
        title="Unemployment and Poverty as Productivity Challenges",
        prompt=prompt,
        sample_answer=(
            "1. Unemployed citizens represent wasted human potential who cannot contribute skills or produce goods, shrinking total GDP.\n"
            "2. Poverty leads to poor nutrition, transport struggles, and lower educational attainment, reducing stamina, health, and workplace efficiency while weakening consumer demand for local businesses."
        ),
        marking_points=[
            "Idle workers represent lost labour output and skills erosion, lowering national GDP [1]",
            "Poor nutrition, health stress, and weak consumer spending reduce workplace energy and business sales/expansion [1]",
        ],
        hints={
            "tier_1": "Consider both lost human output when people cannot work AND what poverty does to health and spending.",
            "tier_2": "Link nutrition/health + lost skills + low consumer buying power back to national productivity.",
            "tier_3": "Give two points: idle human potential/GDP loss, and malnutrition/weak demand lowering efficiency.",
        },
        learning_objective_id="lo_prod_challenge_unemployment",
        concept_id="sa_productivity_unemployment",
        misconception_tags=["ignores_nutrition_and_demand_links"],
        marks=2,
    )


def arch_35_sa_productivity_challenge_hivaids_absenteeism(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    staff = rng.randint(40, 120)
    prompt = (
        f"A regional factory employing {staff} staff near {area} experiences rising absenteeism, sick leave, and loss of "
        f"experienced artisans due to untreated chronic illness and HIV/Aids.\n\n"
        f"Which combination of operational effects AND supportive workplace response is MOST accurate?"
    )
    correct = (
        "Absenteeism and recruitment/retraining costs lower productivity; wellness education, clinics, and treatment support protect workers and output"
    )
    distractors = [
        "Losing experienced artisans increases factory efficiency automatically with zero training costs",
        "Chronic illness affects only agricultural farms and never impacts urban factories or offices",
        "Firing ill staff immediately without support eliminates all retraining costs permanently",
    ]
    return _mcq(
        rng,
        subskill="35_sa_productivity_challenge_hivaids_absenteeism",
        title="Health, HIV/Aids & Workplace Productivity",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Illness causes absenteeism, lower morale, loss of scarce skills, and higher hiring/training costs. Workplace "
            "health education, testing, and treatment support safeguard both employees and sustainable productivity."
        ),
        hints={
            "tier_1": "Think of both the cost of lost experienced workers and the constructive workplace health response.",
            "tier_2": "Supportive workplace wellness programmes keep staff healthy and experienced.",
            "tier_3": "Select the option linking absenteeism/retraining costs with supportive wellness clinics and treatment.",
        },
        learning_objective_id="lo_prod_challenge_hivaids",
        concept_id="health_and_productivity",
        misconception_tags=["ignores_retraining_cost_of_illness"],
    )


def arch_36_sa_productivity_challenge_skills_shortage(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    vacancy = rng.choice(["qualified millwrights and CNC technicians", "civil engineers and qualified artisans", "ICT network specialists and financial managers"])
    prompt = (
        f"Businesses across {area} struggle for months to recruit {vacancy}.\n\n"
        f"How does a persistent shortage of skilled personnel affect productivity and economic growth?"
    )
    correct = (
        "Machines sit idle or run below capacity, errors rise, and enterprises delay expansion — slowing national growth"
    )
    distractors = [
        "Every factory immediately doubles output even with unoperated equipment",
        "Businesses need zero engineers or technicians as long as interest rates rise",
        "Skills shortages eliminate the need for secondary education or SETAs",
    ]
    return _mcq(
        rng,
        subskill="36_sa_productivity_challenge_skills_shortage",
        title="Skills Shortage Impact on Productivity",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"When {vacancy} are scarce, equipment goes unmaintained, output stalls, unit costs climb, and businesses "
            f"cannot expand production."
        ),
        hints={
            "tier_1": "What happens when specialized machinery has no qualified operators or technicians?",
            "tier_2": "Vacancies slow down factory maintenance, innovation, and job expansion.",
            "tier_3": "Select 'Machines sit idle or run below capacity, errors rise, and enterprises delay expansion — slowing national growth'.",
        },
        learning_objective_id="lo_prod_challenge_skills_shortage",
        concept_id="skills_shortage_productivity",
        misconception_tags=["assumes_unskilled_labour_replaces_artisans_instantly"],
    )


def arch_37_unit_labour_cost_calculation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    wage = rng.choice([240, 300, 360])
    units = rng.choice([12, 15, 20, 30])
    unit_cost = round(wage / units, 2)
    prompt = (
        f"A worker in {area} earns {_fmt_zar(wage)} for a day's shift and sews {units} canvas school bags in that shift.\n\n"
        f"Calculate the UNIT LABOUR COST (labour cost per bag) in Rand."
    )
    return _typed(
        rng,
        subskill="37_unit_labour_cost_calculation",
        title="Calculating Unit Labour Cost",
        prompt=prompt,
        sample_answer=f"Unit labour cost = Total Wage / Units Produced = R{wage} / {units} = R{_fmt_comma(unit_cost, 2)} per bag.",
        marking_points=[
            f"Set up Unit Labour Cost = Total Wage ({wage}) / Units ({units}) [1]",
            f"Correct calculation = {_fmt_zar(unit_cost, 2)} per bag [1]",
        ],
        hints={
            "tier_1": "Divide the total daily wage paid by the total number of bags made.",
            "tier_2": f"Calculate R{wage} / {units}.",
            "tier_3": f"R{wage} / {units} = {_fmt_zar(unit_cost, 2)} per bag.",
        },
        learning_objective_id="lo_prod_unit_labour_cost",
        concept_id="unit_labour_cost",
        misconception_tags=["divides_units_by_wage"],
        marks=2,
        correct_answer=_fmt_zar(unit_cost, 2),
        correct_value=float(unit_cost),
        worked_solution=f"Unit labour cost = {wage} / {units} = R{_fmt_comma(unit_cost, 2)}",
    )


def arch_38_slow_vs_fast_productivity_unit_cost_comparison_table(rng: random.Random) -> Dict[str, Any]:
    daily_wage = rng.choice([240, 320, 400])
    slow_units = 8
    fast_units = 16
    slow_cost = daily_wage // slow_units
    fast_cost = daily_wage // fast_units
    area = rng.choice(AREAS)

    headers = ["Worker Speed", "Daily Wage (R)", "Baskets Woven", "Unit Labour Cost (R/Basket)", "Flag"]
    raw_rows = [
        [
            {"type": "given", "value": "Slow Trainee Worker"},
            {"type": "given", "value": _fmt_zar(daily_wage)},
            {"type": "given", "value": str(slow_units)},
            {"type": "required", "expected": _fmt_zar(slow_cost)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Fast Skilled Worker"},
            {"type": "given", "value": _fmt_zar(daily_wage)},
            {"type": "given", "value": str(fast_units)},
            {"type": "required", "expected": _fmt_zar(fast_cost)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Lower Unit Cost Worker"},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
            {"type": "required", "expected": "Fast Skilled Worker"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c3": f"Divide {_fmt_zar(daily_wage)} by {slow_units}.",
        "r1_c3": f"Divide {_fmt_zar(daily_wage)} by {fast_units}.",
        "r2_c3": "Enter the worker with the smaller Rand cost per basket ('Fast Skilled Worker').",
    }
    derivations = [
        f"Slow Worker unit cost = R{daily_wage} / {slow_units} = {_fmt_zar(slow_cost)} per basket.",
        f"Fast Worker unit cost = R{daily_wage} / {fast_units} = {_fmt_zar(fast_cost)} per basket.",
        "Higher productivity lowers unit labour cost even at the exact same daily wage.",
    ]
    return _table_q(
        rng,
        subskill="38_slow_vs_fast_productivity_unit_cost_comparison_table",
        title="Slow vs Fast Worker Unit Cost Table",
        prompt=(
            f"Two craftworkers in {area} earn an identical daily wage of {_fmt_zar(daily_wage)}. Complete each worker's "
            f"Unit Labour Cost and identify the cheaper-per-unit worker. Leave shaded cells and 'Flag' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Unit Labour Cost = Daily Wage / Baskets Woven.",
            "tier_2": "Higher output for the same wage spreads labour cost across more units.",
            "tier_3": f"Slow={_fmt_zar(slow_cost)}; Fast={_fmt_zar(fast_cost)}; Lower='Fast Skilled Worker'.",
        },
        learning_objective_id="lo_prod_unit_cost_table",
        concept_id="slow_vs_fast_unit_cost",
        misconception_tags=["thinks_same_wage_means_same_unit_cost", "fills_must_be_empty_cell"],
    )


def arch_39_home_industries_definition_and_scale(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    craft = rng.choice(["custom birthday cakes from a family kitchen", "welded burglar bars in a backyard garage", "school tracksuits on two home sewing machines"])
    prompt = (
        f"{name} runs a small enterprise in {area} producing {craft} without renting an expensive factory warehouse.\n\n"
        f"How is this type of production BEST classified?"
    )
    correct = "A home industry — small-scale production operated from a private residence with low overhead costs"
    distractors = [
        "A multinational car assembly line employing 8 000 factory shifts",
        "An underground deep-shaft gold mine owned by an overseas stock exchange",
        "A commercial central bank regulating national currency stability",
    ]
    return _mcq(
        rng,
        subskill="39_home_industries_definition_and_scale",
        title="Meaning of Home Industries",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Making {craft} at home avoids commercial factory rent and lets {name} launch a small business flexibly — "
            f"a classic example of a home industry."
        ),
        hints={
            "tier_1": "Notice WHERE the goods are made and the small scale of operations.",
            "tier_2": "Production run from a home kitchen, spare room, or garage is a home industry.",
            "tier_3": "Select 'A home industry — small-scale production operated from a private residence with low overhead costs'.",
        },
        learning_objective_id="lo_prod_home_industry_def",
        concept_id="home_industries",
        misconception_tags=["thinks_production_requires_large_factory"],
    )


def arch_40_home_industries_advantages_and_limits(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    rent_saved = rng.choice([4500, 6000, 7500])
    prompt = (
        f"{name}'s home baking micro-enterprise in {area} saves {_fmt_zar(rent_saved)}/month in shop rent, yet struggles "
        f"to fulfil a 500-loaf catering order.\n\n"
        f"State TWO advantages and TWO limitations of operating as a home industry."
    )
    return _typed(
        rng,
        subskill="40_home_industries_advantages_and_limits",
        title="Advantages and Limitations of Home Industries",
        prompt=prompt,
        sample_answer=(
            f"Advantages: (1) Saves commercial rent ({_fmt_zar(rent_saved)}/month) and overhead costs; (2) Flexible hours allowing family care.\n"
            "Limitations: (1) Small kitchen/garage capacity cannot handle large bulk orders; (2) Harder to obtain bulk supplier discounts or pass municipal zoning/health rules for big buyers."
        ),
        marking_points=[
            "Two valid advantages (e.g. very low rent/overheads, flexible family schedule, low start-up risk) [2]",
            "Two valid limitations (e.g. small output capacity, fewer bulk-buying discounts, municipal zoning/parking limits) [2]",
        ],
        hints={
            "tier_1": "Weigh low monthly rent and flexibility against small room size and big-order limits.",
            "tier_2": "Include 2 positives (cost/flexibility) and 2 constraints (capacity/bulk discounts/zoning).",
            "tier_3": "Advantages: low rent & flexibility; Limitations: limited output capacity & higher per-unit supply costs.",
        },
        learning_objective_id="lo_prod_home_industry_pros_cons",
        concept_id="home_industry_evaluation",
        misconception_tags=["omits_capacity_or_zoning_constraints"],
        marks=4,
    )


def arch_41_technology_and_automation_in_production(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"A modern bottling plant in {area} installs computer-controlled conveyor arms that wash, fill, cap, and label "
        f"bottles continuously with minimal direct hand-touching.\n\n"
        f"Which term BEST describes replacing manual repetitive tasks with self-regulating machinery and software?"
    )
    correct = "Automation"
    distractors = [
        "Subsistence barter",
        "Home craftwork",
        "Soil erosion",
    ]
    return _mcq(
        rng,
        subskill="41_technology_and_automation_in_production",
        title="Technology and Automation",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Automation uses computerised machines and robotics to carry out repetitive or hazardous production steps "
            "at high speed and precision."
        ),
        hints={
            "tier_1": "Think of the word meaning automatic computer-controlled machinery.",
            "tier_2": "Self-regulating production lines using robotics and sensors define automation.",
            "tier_3": "Select 'Automation'.",
        },
        learning_objective_id="lo_prod_automation_def",
        concept_id="automation_definition",
        misconception_tags=["confuses_automation_with_manual_craft"],
    )


def arch_42_seven_advantages_of_technology_in_production(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    output_gain = rng.randint(35, 65)
    prompt = (
        f"By upgrading to computer-guided CNC cutting machines, a furniture factory in {area} raises weekly output by "
        f"{output_gain}% while lowering wood offcut waste.\n\n"
        f"Give FOUR distinct advantages that modern technology brings to the production process."
    )
    return _typed(
        rng,
        subskill="42_seven_advantages_of_technology_in_production",
        title="Advantages of Technology in Production",
        prompt=prompt,
        sample_answer=(
            "1. Faster production speed and higher output volume.\n"
            "2. Consistent precision and fewer human manufacturing errors/waste.\n"
            "3. Safer workplaces by letting machines handle dangerous cutting, heavy lifting, or toxic chemicals.\n"
            "4. Lower long-run cost per unit and real-time digital stock/quality tracking."
        ),
        marking_points=[
            "Faster speed / higher output [1]",
            "Consistent quality and less raw-material waste [1]",
            "Improved worker safety on hazardous/heavy tasks [1]",
            "Lower long-term cost per unit / 24-hour capability / digital stock tracking [1]",
        ],
        hints={
            "tier_1": "Consider speed, accuracy, worker safety, operating hours, and unit cost.",
            "tier_2": "List four concrete operational benefits rather than repeating 'it is better'.",
            "tier_3": "Include higher speed, consistent accuracy/less waste, dangerous-task safety, and lower unit costs.",
        },
        learning_objective_id="lo_prod_tech_advantages",
        concept_id="technology_advantages",
        misconception_tags=["repeats_one_benefit_four_times"],
        marks=4,
    )


def arch_43_technology_impact_employment_unskilled_vs_skilled(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    workers = rng.randint(18, 40)
    prompt = (
        f"When a warehouse in {area} installs automated pallet-stacking cranes, {workers} manual lifting jobs disappear, "
        f"while new openings appear for PLC programmers and electrical maintenance technicians.\n\n"
        f"What does this reveal about how technology shifts employment demand?"
    )
    correct = (
        "Automation reduces demand for routine unskilled manual labour while increasing demand for skilled operators, technicians, and programmers"
    )
    distractors = [
        "Modern technology eliminates every skilled engineering job while creating millions of manual ditch-digging posts",
        "Computers operate, repair, and upgrade themselves with zero human involvement forever",
        "Factories installing robots no longer require electricity or skilled management",
    ]
    return _mcq(
        rng,
        subskill="43_technology_impact_employment_unskilled_vs_skilled",
        title="Technology's Impact on Skilled vs Unskilled Jobs",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "While automation displaces repetitive manual labour, it creates higher-paying technical roles for people "
            "trained to design, program, operate, and maintain machinery—showing why skills training is vital."
        ),
        hints={
            "tier_1": "Notice which jobs shrank (manual lifting) and which jobs opened up (programmers & technicians).",
            "tier_2": "Technology replaces repetitive physical work and increases demand for technical skills.",
            "tier_3": "Select the option noting reduced routine manual demand and higher demand for skilled technicians/operators.",
        },
        learning_objective_id="lo_prod_tech_jobs_shift",
        concept_id="technology_employment_impact",
        misconception_tags=["believes_technology_destroys_all_skilled_work"],
    )


def arch_44_manual_vs_automated_production_schedule_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["Production Feature", "Manual Method", "Automated Method", "Audit"]
    raw_rows = [
        [
            {"type": "given", "value": "Initial Equipment Cost"},
            {"type": "given", "value": "Low capital start-up"},
            {"type": "required", "expected": "High capital investment"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Output Speed & Uniformity"},
            {"type": "required", "expected": "Slower and varies slightly"},
            {"type": "given", "value": "Very fast and uniform"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Key Workforce Skill Need"},
            {"type": "given", "value": "Manual hands-on craft"},
            {"type": "required", "expected": "Skilled machine technicians"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Exact phrase: 'High capital investment'.",
        "r1_c1": "Exact phrase: 'Slower and varies slightly'.",
        "r2_c2": "Exact phrase: 'Skilled machine technicians'.",
    }
    derivations = [
        "Automated machinery requires High capital investment upfront.",
        "Manual craft is Slower and varies slightly compared with machine uniformity.",
        "Automated lines require Skilled machine technicians to program and service equipment.",
    ]
    return _table_q(
        rng,
        subskill="44_manual_vs_automated_production_schedule_table",
        title="Manual vs Automated Production Matrix",
        prompt=(
            f"Compare manual and automated methods for a workshop in {area} using these exact completions: "
            f"'High capital investment', 'Slower and varies slightly', and 'Skilled machine technicians'. Leave 'Audit' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Compare start-up cost, speed/consistency, and worker skills across both columns.",
            "tier_2": "Automation costs more upfront and needs technicians, while manual work is slower and varies slightly.",
            "tier_3": "r0_c2='High capital investment'; r1_c1='Slower and varies slightly'; r2_c2='Skilled machine technicians'.",
        },
        learning_objective_id="lo_prod_manual_vs_auto_table",
        concept_id="manual_vs_automated_table",
        misconception_tags=["swaps_manual_and_automated_columns", "fills_must_be_empty_cell"],
    )


def arch_45_water_electricity_conservation_in_factories(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    saving_pct = rng.randint(18, 32)
    prompt = (
        f"A beverage factory in {area} installs rooftop solar panels, LED sensors, and closed-loop water recycling, "
        f"cutting utility bills by {saving_pct}%.\n\n"
        f"Why do water and electricity conservation measures help BOTH the environment AND the business?"
    )
    correct = (
        "They preserve scarce water and reduce coal-fired emissions while lowering monthly operating costs and boosting profitability"
    )
    distractors = [
        "They intentionally waste more water so municipal tariffs double immediately",
        "They force factories to pay triple for diesel generators every afternoon",
        "They eliminate the need to pay employees or maintain bottling lines",
    ]
    return _mcq(
        rng,
        subskill="45_water_electricity_conservation_in_factories",
        title="Factory Water & Electricity Conservation",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Conserving water and electricity protects South Africa's scarce catchments and grid while directly cutting "
            f"factory production expenses by {saving_pct}%."
        ),
        hints={
            "tier_1": "Think of the double win: resource stewardship AND lower monthly factory utility bills.",
            "tier_2": "Solar + LED + water recycling cut waste and operating expenses together.",
            "tier_3": "Select the option linking ecosystem/resource preservation with lower operating costs and higher profits.",
        },
        learning_objective_id="lo_prod_resource_conservation",
        concept_id="factory_conservation",
        misconception_tags=["treats_green_measures_as_pure_cost"],
    )


def arch_46_inflation_and_production_cost_link(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    diesel_pct = rng.randint(10, 22)
    prompt = (
        f"Manufacturers in {area} experience a {diesel_pct}% jump in diesel transport and electricity tariffs across "
        f"the economy.\n\n"
        f"Define INFLATION and explain how rising input costs lead to higher shelf prices for consumers."
    )
    return _typed(
        rng,
        subskill="46_inflation_and_production_cost_link",
        title="Inflation and Production Cost Pass-Through",
        prompt=prompt,
        sample_answer=(
            f"Inflation is a sustained, general increase in the prices of goods and services over time, reducing money's purchasing power.\n"
            f"When diesel and electricity jump by {diesel_pct}%, factories face higher production and delivery costs per unit "
            f"and raise shelf prices to remain profitable."
        ),
        marking_points=[
            "Defines inflation accurately as a general, sustained rise in prices (reducing purchasing power of money) [1]",
            "Explains that higher input/energy costs squeeze profit margins, causing producers to raise retail prices [1]",
        ],
        hints={
            "tier_1": "First define what inflation means for prices across the economy.",
            "tier_2": "Next explain what happens to selling prices when transport and electricity inputs cost more.",
            "tier_3": "Define inflation as sustained general price rises, and note producers pass higher input costs into final prices.",
        },
        learning_objective_id="lo_prod_inflation_cost",
        concept_id="inflation_and_costs",
        misconception_tags=["defines_inflation_as_a_single_item_sale"],
        marks=2,
    )


def arch_47_value_added_chain_profit_margin_calculation(rng: random.Random) -> Dict[str, Any]:
    raw_milk = rng.choice([1200, 1500, 1800])
    factory_val = rng.choice([2900, 3400, 3900])
    retail_val = rng.choice([4800, 5400, 6100])
    total_added = retail_val - raw_milk
    prompt = (
        f"A farmer sells raw milk to a dairy for {_fmt_zar(raw_milk)}. The dairy processes it into cheese sold to a "
        f"supermarket for {_fmt_zar(factory_val)}, and the supermarket sells the cheese to shoppers for {_fmt_zar(retail_val)}.\n\n"
        f"Calculate the TOTAL VALUE ADDED across Secondary processing and Tertiary retailing combined (from {_fmt_zar(raw_milk)} to {_fmt_zar(retail_val)})."
    )
    return _typed(
        rng,
        subskill="47_value_added_chain_profit_margin_calculation",
        title="Value Added Across Economic Sectors",
        prompt=prompt,
        sample_answer=(
            f"Secondary value added = {_fmt_zar(factory_val)} - {_fmt_zar(raw_milk)} = {_fmt_zar(factory_val - raw_milk)}\n"
            f"Tertiary value added = {_fmt_zar(retail_val)} - {_fmt_zar(factory_val)} = {_fmt_zar(retail_val - factory_val)}\n"
            f"Total value added = {_fmt_zar(retail_val)} - {_fmt_zar(raw_milk)} = {_fmt_zar(total_added)}"
        ),
        marking_points=[
            f"Identify Secondary value added ({_fmt_zar(factory_val - raw_milk)}) and Tertiary ({_fmt_zar(retail_val - factory_val)}) [1]",
            f"Correct total value added = {_fmt_zar(total_added)} [1]",
        ],
        hints={
            "tier_1": "Value added is the extra Rand value created beyond the original raw milk price.",
            "tier_2": f"Subtract {_fmt_zar(raw_milk)} from {_fmt_zar(retail_val)}.",
            "tier_3": f"{_fmt_zar(retail_val)} - {_fmt_zar(raw_milk)} = {_fmt_zar(total_added)}.",
        },
        learning_objective_id="lo_prod_value_added_calc",
        concept_id="value_added_chain",
        misconception_tags=["sums_gross_sales_instead_of_value_added"],
        marks=2,
        correct_answer=_fmt_zar(total_added),
        correct_value=float(total_added),
        worked_solution=f"Total value added = {retail_val} - {raw_milk} = {_fmt_zar(total_added)}",
    )


def arch_48_sustainable_resource_cycle_diagram(rng: random.Random) -> Dict[str, Any]:
    rec_pct = rng.randint(55, 78)
    svg = _svg_cycle_flow(
        title="Circular Sustainable Resource Cycle",
        nodes=[
            "1. Responsible Resource Extraction",
            "2. Energy-Efficient Clean Factory",
            "3. Consumer Use Without Waste",
            f"4. Collect & Recycle ({rec_pct}% Reused)",
        ],
        accent_color="#15803D",
    )
    prompt = (
        f"Refer to the flowchart below depicting a closed-loop circular production model where {rec_pct}% of scrap "
        f"glass and aluminium re-enters production.\n\n"
        f"Explain how Step 4 ('Collect & Recycle') reduces pressure on Step 1 ('Responsible Resource Extraction')."
    )
    return _typed(
        rng,
        subskill="48_sustainable_resource_cycle_diagram",
        title="Circular Resource Sustainability (Flowchart)",
        prompt=prompt,
        sample_answer=(
            f"Recycling {rec_pct}% of used glass and metal feeds recovered materials directly back into Step 2's clean "
            f"factory, reducing the volume of virgin ore and coal that must be mined in Step 1 and cutting landfill pollution."
        ),
        marking_points=[
            f"Notes that recycling {rec_pct}% supplies secondary raw material back into manufacturing [1]",
            "Explains that this slows depletion of finite minerals and reduces energy/landfill damage [1]",
        ],
        hints={
            "tier_1": "Follow the arrow looping from Box 4 back toward Box 1.",
            "tier_2": "Reusing melted scrap metal or glass means less virgin mining and quarrying.",
            "tier_3": f"State that reusing {rec_pct}% recycled inputs lowers virgin extraction and slows finite resource depletion.",
        },
        learning_objective_id="lo_prod_circular_cycle_diagram",
        concept_id="circular_resource_cycle",
        misconception_tags=["assumes_recycling_eliminates_all_manufacturing"],
        marks=2,
        diagram_spec={"kind": "inline_svg", "title": "Circular Sustainable Resource Cycle", "svg": svg, "diagram_role": "context"},
    )


def arch_49_productivity_vs_cost_tradeoff_analysis(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    cut_pct = rng.randint(15, 25)
    prompt = (
        f"Facing rising expenses in {area}, a workshop manager proposes cutting staff wages by {cut_pct}% instead of "
        f"upgrading broken machinery or training workers.\n\n"
        f"Analyse TWO reasons why slashing wages often FAILS to lower unit labour cost compared with boosting productivity."
    )
    return _typed(
        rng,
        subskill="49_productivity_vs_cost_tradeoff_analysis",
        title="Wage Cuts vs Productivity Improvements",
        prompt=prompt,
        sample_answer=(
            f"1. Cutting pay by {cut_pct}% damages worker morale, causing higher absenteeism, slower pace, defects, and skilled staff quitting.\n"
            "2. Lower output with broken machines raises cost per finished item, whereas training and reliable tools expand output and lower unit labour cost sustainably."
        ),
        marking_points=[
            "Pay cuts reduce morale, speed, and quality while driving skilled workers away [1]",
            "Raising output via skills/maintenance lowers unit cost without harming workers [1]",
        ],
        hints={
            "tier_1": "Remember: Unit Labour Cost depends on BOTH wages paid AND units produced.",
            "tier_2": "If unhappy staff slow down or leave, output drops and unit cost stays high.",
            "tier_3": "Explain lowered morale/turnover AND how higher output from training/tools beats wage cuts.",
        },
        learning_objective_id="lo_prod_wage_vs_productivity",
        concept_id="productivity_cost_tradeoff",
        misconception_tags=["ignores_morale_and_defect_costs"],
        marks=2,
    )


def arch_50_integrated_sa_production_and_growth_synthesis(rng: random.Random) -> Dict[str, Any]:
    rural_area = rng.choice(RURAL_AREAS)
    urban_area = rng.choice(URBAN_AREAS)
    invest_m = rng.randint(18, 45)
    prompt = (
        f"A South African agri-processing group invests R{invest_m} million linking farms in {rural_area} with a solar-powered "
        f"canning plant and logistics hub in {urban_area}.\n\n"
        f"Synthesise FOUR concepts from this topic by explaining: (1) all three economic sectors involved, "
        f"(2) how the 4 Factors of Production operate, (3) one sustainable resource practice, and (4) how higher productivity drives economic growth."
    )
    return _typed(
        rng,
        subskill="50_integrated_sa_production_and_growth_synthesis",
        title="Integrated Production & Economic Growth Synthesis",
        prompt=prompt,
        sample_answer=(
            f"1. Three Sectors: Farms in {rural_area} (Primary) grow fruit; the canning factory (Secondary) processes cans; logistics/shops in {urban_area} (Tertiary) distribute and sell them.\n"
            f"2. Four Factors: Natural resources (farmland/water), Labour (farmers/technicians), Capital (R{invest_m}M solar canning plant), and Entrepreneurship (owners coordinating risk for profit).\n"
            "3. Sustainability: Using rooftop solar power and water recycling preserves non-renewable coal and scarce catchments.\n"
            "4. Productivity -> Growth: Trained workers and automated canning raise output per hour, lowering unit cost and expanding South Africa's GDP."
        ),
        marking_points=[
            "Correctly maps Primary (farming), Secondary (canning), and Tertiary (logistics/retail) [1]",
            "Identifies how Natural Resources, Labour, Capital, and Entrepreneurship combine [1]",
            "Explains a valid sustainable practice (solar power, water recycling, soil care) [1]",
            "Connects higher productivity per input to greater total GDP (economic growth) [1]",
        ],
        hints={
            "tier_1": "Cover all four numbered checkpoints clearly in order.",
            "tier_2": "Tie specific rural farm/urban factory examples to sectors, factors, green practices, and GDP growth.",
            "tier_3": "Include Primary/Secondary/Tertiary + 4 Factors + solar/water sustainability + Productivity boosting GDP.",
        },
        learning_objective_id="lo_prod_integrated_synthesis",
        concept_id="integrated_production_synthesis",
        misconception_tags=["omits_one_of_four_pillars"],
        marks=4,
    )


BUILDERS_26_50 = {
    "26_economic_growth_definition_and_gdp": arch_26_economic_growth_definition_and_gdp,
    "27_gdp_growth_rate_calculation": arch_27_gdp_growth_rate_calculation,
    "28_economic_growth_bar_graph_trend": arch_28_economic_growth_bar_graph_trend,
    "29_productivity_definition_output_per_input": arch_29_productivity_definition_output_per_input,
    "30_productivity_ratio_calculation": arch_30_productivity_ratio_calculation,
    "31_productivity_comparison_bar_graph": arch_31_productivity_comparison_bar_graph,
    "32_productivity_ledger_comparison_table": arch_32_productivity_ledger_comparison_table,
    "33_improving_productivity_without_extra_inputs": arch_33_improving_productivity_without_extra_inputs,
    "34_sa_productivity_challenge_unemployment_poverty": arch_34_sa_productivity_challenge_unemployment_poverty,
    "35_sa_productivity_challenge_hivaids_absenteeism": arch_35_sa_productivity_challenge_hivaids_absenteeism,
    "36_sa_productivity_challenge_skills_shortage": arch_36_sa_productivity_challenge_skills_shortage,
    "37_unit_labour_cost_calculation": arch_37_unit_labour_cost_calculation,
    "38_slow_vs_fast_productivity_unit_cost_comparison_table": arch_38_slow_vs_fast_productivity_unit_cost_comparison_table,
    "39_home_industries_definition_and_scale": arch_39_home_industries_definition_and_scale,
    "40_home_industries_advantages_and_limits": arch_40_home_industries_advantages_and_limits,
    "41_technology_and_automation_in_production": arch_41_technology_and_automation_in_production,
    "42_seven_advantages_of_technology_in_production": arch_42_seven_advantages_of_technology_in_production,
    "43_technology_impact_employment_unskilled_vs_skilled": arch_43_technology_impact_employment_unskilled_vs_skilled,
    "44_manual_vs_automated_production_schedule_table": arch_44_manual_vs_automated_production_schedule_table,
    "45_water_electricity_conservation_in_factories": arch_45_water_electricity_conservation_in_factories,
    "46_inflation_and_production_cost_link": arch_46_inflation_and_production_cost_link,
    "47_value_added_chain_profit_margin_calculation": arch_47_value_added_chain_profit_margin_calculation,
    "48_sustainable_resource_cycle_diagram": arch_48_sustainable_resource_cycle_diagram,
    "49_productivity_vs_cost_tradeoff_analysis": arch_49_productivity_vs_cost_tradeoff_analysis,
    "50_integrated_sa_production_and_growth_synthesis": arch_50_integrated_sa_production_and_growth_synthesis,
}
