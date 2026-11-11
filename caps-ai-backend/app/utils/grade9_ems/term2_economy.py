import random


def _rng(seed=None):
    if seed is not None:
        return random.Random(seed)
    return random.Random()


def _with_metadata(item, subskill, learning_objective_id, question_family_id, concept_id, concept_group, diagnostic_tags):
    item['subskill'] = subskill
    item['learning_objective_id'] = learning_objective_id
    item['question_family_id'] = question_family_id
    item['concept_id'] = concept_id
    item['concept_group'] = concept_group
    item['diagnostic_tags'] = diagnostic_tags
    return item


def _generate_price_theory(rng, mode, seed=None):
    s_val = int(seed if seed is not None else rng.randint(100, 999))
    peq = 30 + ((s_val * 7) % 60)
    qeq = 200 + ((s_val * 15) % 400)
    total_rev = peq * qeq
    surplus_price = peq + 15
    qd_high = max(50, qeq - 80)
    qs_high = qeq + 80
    surplus_units = qs_high - qd_high

    shortage_price = max(10, peq - 12)
    qd_low = qeq + 70
    qs_low = max(40, qeq - 70)
    shortage_units = qd_low - qs_low

    scenarios = [
        {
            "prompt": (
                f"Refer to the Market Supply and Demand graph for School Stationery & Textbooks.\n\n"
                f"1. Read from the graph the market equilibrium price (\\(P_e\\)) and equilibrium quantity (\\(Q_e\\)) at point \\(E\\). (2)\n"
                f"2. Calculate the total market revenue (\\(\\text{{Total Revenue}} = P_e \\times Q_e\\)) earned at market equilibrium. (2)\n"
                f"3. If suppliers set the price above equilibrium at \\(\\text{{R }}{surplus_price}\\), where quantity supplied is \\({qs_high}\\) units and quantity demanded is \\({qd_high}\\) units, calculate the size of the market surplus (excess supply) and state how the price will adjust to restore equilibrium. (2)"
            ),
            "sample_answer": (
                f"Step 1: Market equilibrium values from point E:\n"
                f"Equilibrium price P_e = R {peq} and equilibrium quantity Q_e = {qeq} units.\n\n"
                f"Step 2: Total revenue at equilibrium:\n"
                f"Total Revenue = P_e × Q_e = R {peq} × {qeq} = R {total_rev}.\n\n"
                f"Step 3: Market surplus at R {surplus_price}:\n"
                f"Excess supply (surplus) = Q_s - Q_d = {qs_high} - {qd_high} = {surplus_units} units. "
                f"Competition among sellers with unsold stock will force the market price downward back toward R {peq}."
            ),
            "marking_points": [
                {"id": "mp_1", "desc": f"1. Equilibrium price P_e = R {peq} and equilibrium quantity Q_e = {qeq} units", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"2. Total Revenue = R {peq} × {qeq} = R {total_rev}", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": f"3. Market surplus = {qs_high} - {qd_high} = {surplus_units} units; price decreases toward R {peq}", "marks": 2, "editable": True},
            ],
            "hint_sections": {
                "1_nudge": "Locate the intersection point E of the Demand (D) and Supply (S) curves on the graph.",
                "2_concept": "Total Revenue = Equilibrium Price × Equilibrium Quantity. Excess Supply = Quantity Supplied - Quantity Demanded.",
                "3_breakdown": f"1. P_e = R {peq}, Q_e = {qeq} units. 2. R {peq} × {qeq} = R {total_rev}. 3. Surplus = {qs_high} - {qd_high} = {surplus_units} units; price falls toward R {peq}.",
            },
        },
        {
            "prompt": (
                f"Refer to the Market Supply and Demand graph showing equilibrium point \\(E\\).\n\n"
                f"1. State the equilibrium price (\\(P_e\\)) and equilibrium quantity (\\(Q_e\\)) shown on the graph. (2)\n"
                f"2. Calculate the total expenditure by consumers at the equilibrium point \\(E\\). (2)\n"
                f"3. Suppose the price is fixed below equilibrium at \\(\\text{{R }}{shortage_price}\\), resulting in \\(Q_d = {qd_low}\\) units and \\(Q_s = {qs_low}\\) units. Calculate the market shortage (excess demand) and explain the resulting upward pressure on price. (2)"
            ),
            "sample_answer": (
                f"Step 1: Equilibrium coordinates from point E:\n"
                f"Equilibrium price P_e = R {peq} and equilibrium quantity Q_e = {qeq} units.\n\n"
                f"Step 2: Total consumer expenditure at equilibrium:\n"
                f"Total Expenditure = P_e × Q_e = R {peq} × {qeq} = R {total_rev}.\n\n"
                f"Step 3: Market shortage at R {shortage_price}:\n"
                f"Excess demand (shortage) = Q_d - Q_s = {qd_low} - {qs_low} = {shortage_units} units. "
                f"Buyers competing for limited stock drive the market price upward back toward R {peq}."
            ),
            "marking_points": [
                {"id": "mp_1", "desc": f"1. Equilibrium price P_e = R {peq} and equilibrium quantity Q_e = {qeq} units", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": f"2. Total Expenditure = R {peq} × {qeq} = R {total_rev}", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": f"3. Market shortage = {qd_low} - {qs_low} = {shortage_units} units; price rises toward R {peq}", "marks": 2, "editable": True},
            ],
            "hint_sections": {
                "1_nudge": "Read the dashed coordinate lines from the equilibrium intersection E to the Price and Quantity axes.",
                "2_concept": "At prices below equilibrium, Quantity Demanded exceeds Quantity Supplied, creating a shortage.",
                "3_breakdown": f"1. P_e = R {peq}, Q_e = {qeq} units. 2. R {peq} × {qeq} = R {total_rev}. 3. Shortage = {qd_low} - {qs_low} = {shortage_units} units; price rises toward R {peq}.",
            },
        },
    ]

    q = scenarios[s_val % len(scenarios)]

    diagram_spec = {
        "kind": "supply_demand",
        "role": "context",
        "diagram_role": "context",
        "equilibrium_price": f"R {peq}",
        "equilibrium_qty": f"{qeq}",
        "market": "Market for School Stationery & Textbooks",
    }

    item = {
        "id": f"ems9_econ_{rng.randint(1000, 9999)}",
        "topic": "Price Theory & Market Equilibrium",
        "question_type": "typed",
        "modality": "semantic",
        "diagram_role": "context",
        "diagram_spec": diagram_spec,
        "prompt": q["prompt"],
        "marks": 6,
        "correct_answer": q["sample_answer"],
        "sample_answer": q["sample_answer"],
        "worked_solution": q["sample_answer"],
        "ideal_answer": q["sample_answer"],
        "marking_points": [mp["desc"] for mp in q["marking_points"]],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": q["marking_points"],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hint_sections": q["hint_sections"],
        "guidelines": ["Award full marks for accurate reading of equilibrium coordinates and correct calculation."],
        "teaching_note": "Ensure learners read the equilibrium point E(Q_e; P_e) directly from the Supply & Demand graph.",
    }
    return [_with_metadata(item, subskill='price_theory', learning_objective_id='lo_price_theory', question_family_id='econ_q', concept_id='price_theory', concept_group='economy', diagnostic_tags=['semantic', 'ems'])]


def generate(subskill="price_theory", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_price_theory(rng, mode, seed=seed)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected

# diagram_role: context (math / ems declarative context visualization)
