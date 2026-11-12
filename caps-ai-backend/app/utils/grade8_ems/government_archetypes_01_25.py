"""Grade 8 EMS - Government: Archetypes 01 to 25.
Grounded strictly in curriculum_docs_auto/EMS_Gr8/Term 1/01. Government.md
and EMS_Gr8/Syllabus.md.
Zero-LLM, 100% deterministic, authentic South African contexts.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.ems_namelist import AREAS, get_ems_scenario


def _fmt_r(amount: int | float) -> str:
    if isinstance(amount, float) and not amount.is_integer():
        return f"R{amount:,.2f}".replace(",", " ").replace(".", ",")
    return f"R{int(round(amount)):,}".replace(",", " ")


def _build_mcq(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    correct_text: str,
    distractors: List[str],
    explanation: str,
    marks: int = 2,
    hints: Dict[str, str],
    misconception_tags: List[str],
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    options = [correct_text] + list(distractors)
    rng.shuffle(options)
    c_idx = options.index(correct_text)
    letter = chr(65 + c_idx)
    ans_full = f"{letter}. {correct_text}"
    worked = f"**{ans_full}** [{marks} marks]\n\n{explanation}"
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "Government",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_government",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_gov_{subskill}",
        "question_type": "mcq",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans_full,
        "expected_answer": ans_full,
        "sample_answer": ans_full,
        "worked_solution": worked,
        "explanation": worked,
        "canonical_solution": worked,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [{"id": "mp_1", "desc": f"Selects option {letter}: {correct_text}", "marks": marks, "editable": True}],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["economy", "government", "south_africa"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _build_short(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    expected_answer: str,
    worked_solution: str,
    marks: int = 3,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
    qtype: str = "short_answer",
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    q: Dict[str, Any] = {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "Government",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_government",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_gov_{subskill}",
        "question_type": qtype,
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "correct_answer": expected_answer,
        "expected_answer": expected_answer,
        "sample_answer": expected_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(4, marks * 2),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["economy", "government", "south_africa"],
    }
    if diagram_spec is not None:
        q["diagram_spec"] = diagram_spec
        q["diagram_role"] = diagram_spec.get("diagram_role", "context")
    return q


def _build_table(
    rng: random.Random,
    *,
    qid_prefix: str,
    subskill: str,
    title: str,
    prompt: str,
    headers: List[str],
    rows: List[List[Dict[str, Any]]],
    correct_map: Dict[str, str],
    cell_hints: Dict[str, str],
    worked_solution: str,
    sample_answer: str,
    marks: int,
    hints: Dict[str, str],
    marking_points: List[Dict[str, Any]],
    misconception_tags: List[str],
) -> Dict[str, Any]:
    return {
        "id": f"{qid_prefix}_{rng.randint(100000, 999999)}",
        "topic": "Government",
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_government",
        "subskill": subskill,
        "question_family_id": subskill,
        "learning_objective_id": f"lo_g8_gov_{subskill}",
        "question_type": "table_completion",
        "modality": "ledger",
        "title": title,
        "prompt": prompt,
        "question": prompt,
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "correct_answer": sample_answer,
        "sample_answer": sample_answer,
        "ideal_answer": sample_answer,
        "worked_solution": worked_solution,
        "explanation": worked_solution,
        "canonical_solution": worked_solution,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(5, marks),
        "hints": hints,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": marking_points,
            "deductions": [{"rule": "must_be_empty_filled", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": misconception_tags,
        "diagnostic_tags": ["economy", "government", "classification_table"],
    }


def arch_01_definition_of_government_and_state_authority(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"During an economics discussion in **{sc['area']}**, learners examine how laws and policies keep South Africa functioning.\n\n"
        f"Which definition **accurately** describes **government** in South Africa?"
    )
    correct = "A group of people with constitutional authority to set policies, make laws, and manage, run, and control a country at national, provincial, and local levels."
    distractors = [
        "A private retail conglomerate that solely determines supermarket food prices across all nine provinces.",
        "An informal neighbourhood savings club that lends cash exclusively to household members.",
        "A commercial factory union focused solely on selling goods at tax-free profit margins.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_01",
        subskill="01_definition_of_government_and_state_authority",
        title="Definition & Authority of Government",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="In Economics, **government** refers to the governing body empowered to formulate policies, enact laws, and administer the state across its three levels (National, Provincial, Local).",
        hints={
            "tier_1": "Think about who sets laws, policies, and runs the country across multiple spheres.",
            "tier_2": "Government administers the State, makes policies/laws, and delivers public services.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_government_with_private_business"],
    )


def arch_02_administering_the_state_three_goals(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tax_bn = rng.randint(15, 22) * 100
    prompt = (
        f"Every year, the South African government collects roughly **R{tax_bn} billion** in taxes to **administer the State** on behalf of citizens in areas such as **{sc['area']}**.\n\n"
        f"State the **three** core responsibilities involved in administering the State using public revenue."
    )
    expected = "1. Ensure the State runs efficiently; 2. Ensure citizens obey the laws of the country; 3. Provide essential services and infrastructure necessary for economic growth."
    sol = (
        f"**Model Answer** [3 marks]:\n\n"
        f"Administering the State using tax revenue requires ensuring:\n"
        f"1. **Efficient state operations** (running public departments cleanly and responsibly) [1 mark];\n"
        f"2. **Law and order compliance** (citizens and businesses obey national laws) [1 mark];\n"
        f"3. **Essential public services and infrastructure** (schools, clinics, roads, water, power) to support economic growth [1 mark]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_02",
        subskill="02_administering_the_state_three_goals",
        title="Responsibilities in Administering the State",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Consider efficiency, rule of law, and services/infrastructure.",
            "tier_2": "State runs efficiently + laws are obeyed + services/infrastructure support growth.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Ensure State runs efficiently", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Ensure citizens obey laws", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Provide services and infrastructure for economic growth", "marks": 1, "editable": True},
        ],
        misconception_tags=["omitting_infrastructure_or_rule_of_law"],
    )


def arch_03_economic_participants_households_businesses_government(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    wage_k = rng.randint(8, 22) * 500
    prompt = (
        f"In **{sc['area']}**, **{sc['entrepreneur']}** runs a **{sc['business_type']}**, employs residents earning **{_fmt_r(wage_k)}** per month, "
        f"and relies on municipal tap water and electricity.\n\n"
        f"Which three primary economic participants interact in this circular economy?"
    )
    correct = "Households (individuals/families), Businesses (firms producing goods and services), and Government (public sector)."
    distractors = [
        "Only foreign central banks, private mines, and international airlines.",
        "Strictly municipalities, commercial shopping malls, and volunteer charities.",
        "Sole traders, partnerships, and stockbrokerages excluding all households.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_03",
        subskill="03_economic_participants_households_businesses_government",
        title="Three Primary Economic Participants",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="The South African mixed economy operates through ongoing exchange of money, labour, goods, and public services among **Households**, **Businesses**, and **Government**.",
        hints={
            "tier_1": "Identify who supplies labour/buys goods, who manufactures/sells, and who governs.",
            "tier_2": "Families = Households; Shops/Factories = Businesses; Public authorities = Government.",
            "tier_3": correct,
        },
        misconception_tags=["omitting_households_from_economy"],
    )


def arch_04_producers_vs_consumers_role_distinction(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    actions = [
        (f"A parent in {sc['area']} works as a nurse at a public clinic (selling labour).", "Household", "Producer"),
        (f"A family buys bread and maize meal from a spaza shop.", "Household", "Consumer"),
        (f"{sc['entrepreneur']}'s {sc['business_type']} delivers finished goods to local clients.", "Business", "Producer"),
        (f"A construction firm hires civil engineers and pays wages.", "Business", "Consumer"),
        ("Municipality supplies clean tap water and street lighting.", "Government", "Producer"),
        ("Department of Education buys desks and chairs from private factories.", "Government", "Consumer"),
    ]
    chosen = rng.sample(actions, 4)
    headers = ["Economic Activity", "Participant (Household / Business / Government)", "Economic Role (Producer / Consumer)"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Economic Activity | Participant | Role |", "| --- | --- | --- |"]

    for i, (act, part, role) in enumerate(chosen):
        correct_map[f"t0_r{i}_c1"] = part
        correct_map[f"t0_r{i}_c2"] = role
        cell_hints[f"t0_r{i}_c1"] = "Identify whether the actor is 'Household', 'Business', or 'Government'."
        cell_hints[f"t0_r{i}_c2"] = "Selling labour/goods/utilities = 'Producer'; buying labour/goods/utilities = 'Consumer'."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": act, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {act} | **{part}** | **{role}** |")

    worked = "**Producer vs Consumer Classification** [8 marks]:\n\n" + "\n".join(md_lines)
    sample = "; ".join(f"{p} ({r})" for _, p, r in chosen)
    return _build_table(
        rng,
        qid_prefix="g8_gov_04",
        subskill="04_producers_vs_consumers_role_distinction",
        title="Producers vs Consumers Classification Table",
        prompt="Classify each South African economic activity below by entering the **Participant** (`Household`, `Business`, or `Government`) and **Economic Role** (`Producer` or `Consumer`).",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=8,
        hints={
            "tier_1": "Every participant can be both a Producer (selling something) and a Consumer (buying/using something).",
            "tier_2": "Households produce labour; Businesses consume labour; Government consumes labour & supplies public utilities.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Row {i+1}: {chosen[i][1]} as {chosen[i][2]}", "marks": 2, "editable": True} for i in range(4)],
        misconception_tags=["assuming_households_never_produce"],
    )


def arch_05_households_as_labour_producers_and_goods_consumers(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    pay = rng.randint(5, 19) * 1000
    prompt = (
        f"A family living in **{sc['area']}** earns **{_fmt_r(pay)}** per month because two adults work at a factory, "
        f"and they spend part of that income buying groceries and municipal electricity.\n\n"
        f"In EMS, why are **households** classified as **BOTH** producers and consumers?"
    )
    correct = "Households act as producers when they sell their labour as a resource to businesses and government, and as consumers when they buy food, clothing, and municipal utilities."
    distractors = [
        "Households are producers only if they operate giant international mines and never buy groceries.",
        "Households act solely as consumers in the economy and never produce any economic input.",
        "Households act as consumers only when paying company tax to the Municipal Mayor.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_05",
        subskill="05_households_as_labour_producers_and_goods_consumers",
        title="Households as Both Producers & Consumers",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="In the economic flow, households supply (**produce**) labour in exchange for wages, and **consume** goods from businesses as well as public utilities from government.",
        hints={
            "tier_1": "What resource do adults in a household supply to employers?",
            "tier_2": "Selling labour = Producer; buying goods/water/electricity = Consumer.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_households_never_produce"],
    )


def arch_06_businesses_as_output_producers_and_resource_consumers(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    tender_m = rng.randint(2, 9)
    prompt = (
        f"A civil engineering firm in **{sc['area']}** wins a **R{tender_m} million** provincial contract to resurface a regional highway. "
        f"To finish the road, the firm hires 40 workers, buys gravel/tar from suppliers, and pays for municipal water and electricity.\n\n"
        f"Explain how this business acts as **both a Consumer and a Producer** in relation to households and government."
    )
    expected = f"As a Consumer, the business buys labour from households, public utilities/tenders from government; as a Producer, it constructs a R{tender_m}m highway infrastructure asset that benefits households, other firms, and economic growth."
    sol = (
        f"**Model Answer** [4 marks]:\n\n"
        f"1. **Business as Consumer** [2 marks]: Consumes household **labour**, natural resources/materials, municipal utilities (water/electricity), and earns public tenders financed by government.\n"
        f"2. **Business as Producer** [2 marks]: Produces the resurfaced highway infrastructure (worth **R{tender_m} million**), enabling logistics and economic activity while paying company tax back to government."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_06",
        subskill="06_businesses_as_output_producers_and_resource_consumers",
        title="Businesses as Consumers & Producers",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "List what the construction firm buys/uses versus what it builds/supplies.",
            "tier_2": "Consumes labour, utilities, tender contracts; produces road infrastructure.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Explains business consuming labour/utilities/tenders", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Explains business producing roads/services for growth", "marks": 2, "editable": True},
        ],
        misconception_tags=["ignoring_business_consumption_of_labour"],
    )


def arch_07_three_levels_of_government_hierarchy(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    target = rng.choice([
        ("Level 1 (Top / Central)", "National Government", "entire Republic of South Africa", "policy, defence, national Acts, fiscal legislation"),
        ("Level 2 (Middle / Regional)", "Provincial Government", "a specific province", "regional hospitals, school education, provincial roads"),
        ("Level 3 (Bottom / Community)", "Local Government (Municipalities)", f"towns/districts such as {sc['area']}", "tap water, sanitation, refuse removal, street lighting"),
    ])
    lvl_lbl, correct_sphere, scope, focus = target
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 175" width="460" height="175">'
        f'<rect width="460" height="175" fill="#ffffff"/>'
        f'<text x="230" y="18" font-size="11" font-weight="bold" text-anchor="middle" fill="#0f172a">Three Spheres of SA Government ({sc["area"]})</text>'
        f'<polygon points="230,30 165,70 295,70" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.5"/>'
        f'<text x="230" y="58" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e3a8a">{"?" if "National" in correct_sphere else "1. National"}</text>'
        f'<polygon points="160,74 300,74 345,116 115,116" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>'
        f'<text x="230" y="100" font-size="10" font-weight="bold" text-anchor="middle" fill="#14532d">{"?" if "Provincial" in correct_sphere else "2. Provincial"}</text>'
        f'<polygon points="110,120 350,120 395,164 65,164" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.5"/>'
        f'<text x="230" y="146" font-size="10" font-weight="bold" text-anchor="middle" fill="#713f12">{"?" if "Local" in correct_sphere else "3. Local (Municipal)"}</text>'
        f'</svg>'
    )
    wrongs = [x for x in ["National Government", "Provincial Government", "Local Government (Municipalities)"] if x != correct_sphere] + ["International Trade Chamber"]
    prompt = (
        f"Study the pyramid diagram showing South Africa's government spheres serving **{sc['area']}**.\n\n"
        f"Which sphere occupies **{lvl_lbl}**, governing **{scope}** with primary responsibility for **{focus}**?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_07",
        subskill="07_three_levels_of_government_hierarchy",
        title="Three Spheres of Government Hierarchy",
        prompt=prompt,
        correct_text=correct_sphere,
        distractors=wrongs,
        explanation=f"South Africa has three distinct constitutional spheres: National (central/countrywide), Provincial (regional), and Local (municipalities). **{lvl_lbl}** is **{correct_sphere}**.",
        hints={
            "tier_1": "Order from widest jurisdiction (country) to closest community level (municipality).",
            "tier_2": f"Jurisdiction: {scope}.",
            "tier_3": f"{correct_sphere}.",
        },
        misconception_tags=["confuses_local_with_provincial_government"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_08_national_government_scope_and_leadership(rng: random.Random) -> Dict[str, Any]:
    aspect = rng.choice([
        ("executive leaders", "The State President, Deputy President, and Cabinet Ministers", ["The Premier and Provincial MECs", "The Municipal Mayor and Ward Councillors", "The Board of JSE Shareholders"]),
        ("legislative product", "National laws (Acts of Parliament) binding across all nine provinces", ["By-laws affecting only one neighbourhood street", "Private shop price stickers", "Commercial bank interest terms"]),
        ("exclusive national responsibility", "National defence (SANDF), policing policy (SAPS), foreign affairs, and national budget legislation", ["Household doorstep refuse collection", "Repairing residential water taps", "Issuing municipal library cards"]),
    ])
    focus, correct, wrongs = aspect
    prompt = (
        f"As South Africa's **highest sphere of governance**, National (Central) Government oversees the entire country.\n\n"
        f"Which option accurately describes National Government's **{focus}**?"
    )
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_08",
        subskill="08_national_government_scope_and_leadership",
        title="National Government Scope & Leadership",
        prompt=prompt,
        correct_text=correct,
        distractors=wrongs,
        explanation=f"National Government is led by the **President, Deputy President, and Cabinet Ministers**, drafts **national laws (Acts)**, and manages countrywide mandates including defence, justice, foreign policy, and the national budget.",
        hints={
            "tier_1": "National government operates at the level of the whole Republic of South Africa.",
            "tier_2": "Think of the State President, Parliament, and countrywide Acts.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_national_with_provincial"],
    )


def arch_09_provincial_government_scope_leadership_and_funding(rng: random.Random) -> Dict[str, Any]:
    prov = rng.choice(["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape", "Limpopo", "Mpumalanga", "Free State", "North West", "Northern Cape"])
    prompt = (
        f"Consider the regional administration of **{prov}** Province.\n\n"
        f"1. What title is given to the political leader of a **Provincial Government** (and who forms its executive cabinet)?\n"
        f"2. Where does Provincial Government receive most of its funding, and name **two** core regional services it manages."
    )
    expected = "1. Premier (assisted by MECs — Members of the Executive Council); 2. Funded by the National Government; manages provincial schools/education, regional public hospitals, and provincial roads."
    sol = (
        f"**Model Answer ({prov} Province)** [4 marks]:\n\n"
        f"1. **Leadership:** Led by the **Premier** together with Members of the Executive Council (**MECs**) [1 mark].\n"
        f"2. **Funding Source:** Primarily funded via allocations from **National Government** [1 mark].\n"
        f"3. **Regional Services (any two):** Provincial public **hospitals/clinics**, **school education** administration, and **provincial roads** [2 marks]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_09",
        subskill="09_provincial_government_scope_leadership_and_funding",
        title="Provincial Government Leadership, Funding & Services",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "Provincial head is not President or Mayor; funding comes from the top sphere.",
            "tier_2": "Premier + MECs; funded by National Government; hospitals, schools, regional roads.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Premier (and MECs)", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Funded by National Government", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Two valid services (hospitals, education/schools, provincial roads)", "marks": 2, "editable": True},
        ],
        misconception_tags=["confuses_premier_with_mayor"],
    )


def arch_10_local_government_municipalities_and_leadership(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    muni_ex = rng.choice(["City of Johannesburg and eThekwini Municipality", "City of Cape Town and Mangaung Municipality", "Nelson Mandela Bay and Polokwane Municipality"])
    prompt = (
        f"In South Africa, local governance closest to citizens in **{area}** is handled by **municipalities** (such as {muni_ex}).\n\n"
        f"Who leads the daily governance of a local **municipality**, and which sphere funds and supports municipalities?"
    )
    correct = "Led by the Mayor and Ward Councillors; funded through municipal rates/tariffs along with transfers distributed via Provincial/National allocations."
    distractors = [
        "Led by the Chief Justice and High Court judges; funded exclusively by foreign tourism visas.",
        "Led by the State President directly; municipalities have zero elected councillors.",
        "Led by private supermarket managers; funded solely from company profits.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_10",
        subskill="10_local_government_municipalities_and_leadership",
        title="Municipal Definition, Leadership & Funding",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="A **municipality** is a district, town, or city with its own **Local Government**, headed by a **Mayor and Councillors**, executing daily municipal administration.",
        hints={
            "tier_1": "Who sits on a town or city council alongside the Mayor?",
            "tier_2": "Mayor and Councillors lead a municipality.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_mayor_with_premier"],
    )


def arch_11_constitutional_objectives_of_local_government(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"Which option is **NOT** a constitutional objective of **Local Government** (municipalities) serving communities like **{area}**?"
    )
    correct = "Declaring international wars and maintaining military fighter jets under municipal command."
    distractors = [
        "Providing democratic and accountable government for local communities.",
        "Ensuring the sustainable provision of essential services such as clean water, electricity, and sanitation.",
        "Promoting local social and economic development within a safe and healthy environment.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_11",
        subskill="11_constitutional_objectives_of_local_government",
        title="Objectives of Local Government",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="Local government exists to ensure democratic local accountability, deliver essential community services, promote social/economic development, and maintain a safe/healthy environment. Military defence belongs strictly to **National Government**.",
        hints={
            "tier_1": "Spot the function that belongs exclusively to National Government rather than a municipality.",
            "tier_2": "Municipalities deliver water, safety, and local development—not military defence.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_local_and_national_mandates"],
    )


def arch_12_three_branches_of_national_government(rng: random.Random) -> Dict[str, Any]:
    branches = [
        ("Legislative", "Makes the laws of the country", "South African Parliament"),
        ("Executive", "Leads and administers the country", "President, Deputy President, and Ministers"),
        ("Judicial", "Ensures justice is served if laws are broken", "Constitutional Court, Supreme Court, and High Court"),
    ]
    rng.shuffle(branches)
    headers = ["Branch of Government", "Core Responsibility", "Composition"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}
    md_lines = ["| Branch | Core Responsibility | Composition |", "| --- | --- | --- |"]

    for i, (br, resp, comp) in enumerate(branches):
        correct_map[f"t0_r{i}_c1"] = resp
        correct_map[f"t0_r{i}_c2"] = comp
        cell_hints[f"t0_r{i}_c1"] = f"Describe what the {br} branch does (makes laws / leads & administers / serves justice)."
        cell_hints[f"t0_r{i}_c2"] = f"Name the institution or officials in the {br} branch."
        rows.append([
            {"coordinate": f"t0_r{i}_c0", "cell_id": f"t0_r{i}_c0", "value": br, "type": "given", "editable": False},
            {"coordinate": f"t0_r{i}_c1", "cell_id": f"t0_r{i}_c1", "value": "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{i}_c2", "cell_id": f"t0_r{i}_c2", "value": "", "type": "required", "editable": True},
        ])
        md_lines.append(f"| {br} | **{resp}** | **{comp}** |")

    worked = "**Three Branches of National Government** [6 marks]:\n\n" + "\n".join(md_lines)
    sample = "; ".join(f"{b}: {r} ({c})" for b, r, c in branches)
    return _build_table(
        rng,
        qid_prefix="g8_gov_12",
        subskill="12_three_branches_of_national_government",
        title="Branches of National Government Table",
        prompt="Complete the South African National Government structure table by stating the **Core Responsibility** and **Composition** of each branch (`Legislative`, `Executive`, `Judicial`).",
        headers=headers,
        rows=rows,
        correct_map=correct_map,
        cell_hints=cell_hints,
        worked_solution=worked,
        sample_answer=sample,
        marks=6,
        hints={
            "tier_1": "Legislative = law-making; Executive = leading/running; Judicial = courts/justice.",
            "tier_2": "Parliament vs President & Ministers vs Constitutional/Supreme/High Courts.",
            "tier_3": sample,
        },
        marking_points=[{"id": f"mp_{i}", "desc": f"Responsibility & composition of {branches[i][0]}", "marks": 2, "editable": True} for i in range(3)],
        misconception_tags=["confusing_branches_with_levels_of_gov"],
    )


def arch_13_legislative_branch_parliament_lawmaking(rng: random.Random) -> Dict[str, Any]:
    act = rng.choice(["Companies Act", "Labour Relations Act", "National Budget Appropriation Bill", "Consumer Protection Act"])
    prompt = (
        f"Before a new national law such as the **{act}** becomes binding across South Africa, it must be debated and passed by the **South African Parliament**.\n\n"
        f"Which branch of National Government does Parliament constitute?"
    )
    correct = "The Legislative branch, whose constitutional mandate is to make and pass the laws of the country."
    distractors = [
        "The Judicial branch, which prosecutes criminal trials inside municipal traffic stations.",
        "The Executive branch, composed purely of municipal ward clerks.",
        "The Provincial branch, restricting all Acts to a single city council.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_13",
        subskill="13_legislative_branch_parliament_lawmaking",
        title="Legislative Branch (Parliament)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="**Parliament** forms the **Legislative branch** of National Government responsible for drafting, debating, and passing South African laws (Acts).",
        hints={
            "tier_1": "'Legislate' means to create or make laws.",
            "tier_2": "Parliament = Legislative branch.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_parliament_with_executive"],
    )


def arch_14_executive_branch_president_and_cabinet(rng: random.Random) -> Dict[str, Any]:
    minister = rng.choice(["Minister of Finance", "Minister of Basic Education", "Minister of Health", "Minister of Trade, Industry and Competition"])
    prompt = (
        f"The President, Deputy President, and Cabinet Ministers (including the **{minister}**) formulate national policy and run state departments daily.\n\n"
        f"Which branch of National Government do these office-bearers form?"
    )
    correct = "The Executive branch, which leads the country and executes/administers government policies and laws."
    distractors = [
        "The Judicial branch, which replaces judges in the Constitutional Court.",
        "The Legislative branch, because ministers only write private business plans.",
        "The Local Municipal branch, restricting policy to street waste collection.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_14",
        subskill="14_executive_branch_president_and_cabinet",
        title="Executive Branch (President & Cabinet)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="The **Executive branch** comprises the **President, Deputy President, and Cabinet Ministers** who lead the country and administer state departments.",
        hints={
            "tier_1": "Think of the 'Chief Executive' running operations daily.",
            "tier_2": "President + Deputy President + Ministers = Executive branch.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_executive_with_judicial"],
    )


def arch_15_judicial_branch_constitutional_supreme_high_courts(rng: random.Random) -> Dict[str, Any]:
    court = rng.choice(["Constitutional Court", "Supreme Court of Appeal", "High Court"])
    prompt = (
        f"When a commercial dispute or violation of law arises in South Africa, citizens and businesses seek resolution through courts such as the **{court}**.\n\n"
        f"Which branch of National Government operates these courts, and what is its constitutional role?"
    )
    correct = "The Judicial branch; it interprets the law and ensures justice is served independently whenever laws are broken or challenged."
    distractors = [
        "The Executive branch; courts write national budgets for Parliament every February.",
        "The Legislative branch; courts directly manufacture water pipes and electricity pylons.",
        "The Local Ward Committee; courts solely collect municipal property rates.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_15",
        subskill="15_judicial_branch_constitutional_supreme_high_courts",
        title="Judicial Branch (Courts & Justice)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"The **Judicial branch** consists of South Africa's independent courts (**Constitutional Court, Supreme Court, High Court**) tasked with upholding the Constitution and serving justice.",
        hints={
            "tier_1": "'Judicial' relates to judges and the justice system.",
            "tier_2": "Courts enforce justice when laws are broken.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_judicial_with_legislative"],
    )


def arch_16_national_government_departments_functions(rng: random.Random) -> Dict[str, Any]:
    depts = [
        ("The National Treasury", "preparing the National Budget, managing state finances, and allocating public revenue"),
        ("Department of Basic Education", "setting national school curriculum standards and overseeing public schooling policy"),
        ("Department of Defence (SANDF)", "protecting South Africa's borders, sovereignty, and territorial integrity"),
        ("South African Police Service (SAPS)", "combating crime and maintaining national internal law and order"),
    ]
    dept, role = rng.choice(depts)
    prompt = (
        f"National government executes its policies through specialized national ministries.\n\n"
        f"Identify **two other** valid South African National Government departments besides **{dept}** (which is responsible for {role}), "
        f"and briefly state one function of **{dept}**."
    )
    expected = f"{dept}: {role}; Other examples: Department of Health, Department of Basic Education, Department of Defence, The National Treasury, Department of Transport (any two valid)."
    sol = (
        f"**Model Answer** [3 marks]:\n\n"
        f"1. **Function of {dept}:** {role.capitalize()} [1 mark].\n"
        f"2. **Two other National Departments (any two):** e.g. Department of Basic Education, Department of Defence, The National Treasury, Department of Health, Department of Labour [2 marks]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_16",
        subskill="16_national_government_departments_functions",
        title="National Government Departments",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=3,
        hints={
            "tier_1": "Name two major national ministries alongside the one already stated.",
            "tier_2": "Examples: Education, Health, Defence, National Treasury, Police, Transport.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Correct function for {dept}", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": "Two valid national government departments listed", "marks": 2, "editable": True},
        ],
        misconception_tags=["naming_private_companies_as_state_depts"],
    )


def arch_17_local_municipal_essential_utility_services(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    svc = rng.choice([
        ("potable drinking water and household sanitation", "Local Municipality"),
        ("refuse/waste collection and municipal street lighting", "Local Municipality"),
        ("domestic electricity distribution and municipal roads maintenance", "Local Municipality"),
    ])
    prompt = (
        f"Families waking up in **{area}** rely every morning on **{svc[0]}**.\n\n"
        f"Which sphere of government delivers **{svc[0]}** directly to households and local businesses?"
    )
    correct = f"{svc[1]} (Local Government)"
    distractors = [
        "Constitutional Court Judicial Division",
        "National Department of Foreign Affairs",
        "Private Commercial Banking Association",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_17",
        subskill="17_local_municipal_essential_utility_services",
        title="Local Municipal Essential Utilities",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**Local Government (Municipalities)** is constitutionally responsible for delivering daily community utilities including {svc[0]}.",
        hints={
            "tier_1": "Daily household utilities like tap water and refuse removal happen at neighbourhood level.",
            "tier_2": "Local Government operates through town and city municipalities.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_municipal_with_national_services"],
    )


def arch_18_government_funding_flows_between_spheres(rng: random.Random) -> Dict[str, Any]:
    total_bn = rng.randint(15, 22) * 100
    prov_share = rng.randint(40, 48)
    muni_share = rng.randint(9, 13)
    nat_share = 100 - prov_share - muni_share
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 110" width="500" height="110">'
        f'<rect width="500" height="110" fill="#ffffff"/>'
        f'<rect x="15" y="25" width="135" height="60" rx="6" fill="#eff6ff" stroke="#1d4ed8"/><text x="82" y="50" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e3a8a">National (SARS)</text><text x="82" y="68" font-size="10" text-anchor="middle" fill="#1e40af">R{total_bn} bn Pool ({nat_share}%)</text>'
        f'<line x1="150" y1="55" x2="180" y2="55" stroke="#334155" stroke-width="2"/>'
        f'<rect x="182" y="25" width="135" height="60" rx="6" fill="#f0fdf4" stroke="#15803d"/><text x="249" y="50" font-size="10" font-weight="bold" text-anchor="middle" fill="#14532d">Provincial ({prov_share}%)</text><text x="249" y="68" font-size="10" text-anchor="middle" fill="#166534">Hospitals &amp; Schools</text>'
        f'<line x1="317" y1="55" x2="347" y2="55" stroke="#334155" stroke-width="2"/>'
        f'<rect x="349" y="25" width="135" height="60" rx="6" fill="#fefce8" stroke="#ca8a04"/><text x="416" y="50" font-size="10" font-weight="bold" text-anchor="middle" fill="#713f12">Local ({muni_share}%)</text><text x="416" y="68" font-size="10" text-anchor="middle" fill="#854d0e">Water &amp; Electricity</text>'
        f'</svg>'
    )
    prov_bn = round(total_bn * prov_share / 100)
    muni_bn = round(total_bn * muni_share / 100)
    prompt = (
        f"Study the intergovernmental funding diagram illustrating a **R{total_bn} billion** national tax pool distributed across South Africa's three spheres: "
        f"**{nat_share}% National**, **{prov_share}% Provincial**, and **{muni_share}% Local**.\n\n"
        f"Calculate the Rand allocation (in billions) received by **(a) Provincial** and **(b) Local** spheres, and state why provinces and municipalities require transfers from National tax revenue."
    )
    expected = f"(a) Provincial: R{prov_bn} billion; (b) Local: R{muni_bn} billion; Reason: Income tax is collected nationally and reallocated down to fund schools, hospitals, and municipal services."
    sol = (
        f"**{expected}** [4 marks]\n\n"
        f"**Working:**\n"
        f"- **(a) Provincial:** ${total_bn} \\times {prov_share}\\% = \\text{{R}}{prov_bn}\\text{{ billion}}$ [1 mark]\n"
        f"- **(b) Local:** ${total_bn} \\times {muni_share}\\% = \\text{{R}}{muni_bn}\\text{{ billion}}$ [1 mark]\n"
        f"- **Rationale:** National government collects major taxes (like Personal Income Tax and VAT) centrally and allocates equitable shares to Provinces and Municipalities so they can deliver regional and local public services [2 marks]."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_18",
        subskill="18_government_funding_flows_between_spheres",
        title="Intergovernmental Tax Allocation Flow",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": f"Multiply R{total_bn} billion by {prov_share}% and {muni_share}%.",
            "tier_2": "Remember National collects major taxes centrally and transfers funds to Provinces/Municipalities.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": f"Provincial share: R{prov_bn} billion", "marks": 1, "editable": True},
            {"id": "mp_2", "desc": f"Local share: R{muni_bn} billion", "marks": 1, "editable": True},
            {"id": "mp_3", "desc": "Explains central collection and downward equitable reallocation", "marks": 2, "editable": True},
        ],
        misconception_tags=["assuming_municipalities_collect_income_tax"],
        diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_19_ward_councillor_civic_engagement_and_accountability(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    issue = rng.choice(["a burst municipal water main leaving three streets dry", "uncollected household refuse for two weeks", "broken streetlights creating safety hazards"])
    prompt = (
        f"Residents in **{area}** experience **{issue}**.\n\n"
        f"Who is the directly elected local representative that residents should contact first to escalate community service delivery issues to the municipal council?"
    )
    correct = "The local Ward Councillor."
    distractors = [
        "The Governor of the South African Reserve Bank.",
        "The Chief Justice of the Constitutional Court.",
        "The Foreign Affairs Ambassador.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_19",
        subskill="19_ward_councillor_civic_engagement_and_accountability",
        title="Civic Engagement via Ward Councillor",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="In South African Local Government, **Ward Councillors** represent specific geographic wards within a municipality and serve as the direct democratic link between residents and municipal administration.",
        hints={
            "tier_1": "Each municipal voting district (ward) elects one representative.",
            "tier_2": "This local councillor takes community complaints directly to the municipal council.",
            "tier_3": correct,
        },
        misconception_tags=["bypassing_local_councillor_structure"],
    )


def arch_20_economic_diversity_unequal_service_access(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    prompt = (
        f"While households in **{sc['urban_area']}** generally receive piped tap water inside their homes and grid electricity, "
        f"some families in **{sc['rural_area']}** rely on communal standpipes, water tankers, or firewood/solar lamps.\n\n"
        f"What important economic insight does this contrast illustrate about household consumption in South Africa?"
    )
    correct = "Economic diversity and historical infrastructure gaps mean households access essential services differently—some directly via municipal household connections, others via communal infrastructure or alternative methods."
    distractors = [
        "Households in rural areas do not consume water, shelter, or energy at all.",
        "Government is legally banned from installing infrastructure outside Gauteng cities.",
        "Businesses only operate in areas where zero municipal electricity exists.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_20",
        subskill="20_economic_diversity_unequal_service_access",
        title="Economic Diversity & Access to Services",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="EMS highlights South Africa's **economic diversity**: universal basic needs (water, energy, transport) exist across all families, yet actual access varies between serviced formal connections and alternative/communal rural provision.",
        hints={
            "tier_1": "Compare urban municipal grid access with rural alternative/communal supply.",
            "tier_2": "All families consume essential resources, though delivery infrastructure differs.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_uniform_infrastructure_access"],
    )


def arch_21_government_assisting_households_public_goods_nonprofit(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    svc = rng.choice(["street lighting along public roads", "rural community postal services", "public health immunisation clinics"])
    prompt = (
        f"Why does government provide services such as **{svc}** to communities in **{area}** instead of leaving them entirely to private profit-seeking firms?"
    )
    correct = "Because private businesses often avoid supplying essential public goods that yield low profits or cannot easily exclude non-paying citizens, yet society needs them."
    distractors = [
        "Because private companies are legally forbidden from earning any money anywhere in South Africa.",
        "Because public goods require zero tax funding or labour to construct.",
        "Because households refuse to use streetlights or clinics unless built by foreign armies.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_21",
        subskill="21_government_assisting_households_public_goods_nonprofit",
        title="Why Government Provides Public Goods",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation="Private firms focus on profitable markets. Government steps in as a **Producer** of **essential public goods/services** (e.g. streetlights, postal delivery, public clinics) that private businesses find unprofitable or too costly for poorer households.",
        hints={
            "tier_1": "Ask: Can a private company make high profits running rural post offices or public streetlights?",
            "tier_2": "Government fills gaps where essential needs are unprofitable for the private sector.",
            "tier_3": correct,
        },
        misconception_tags=["assuming_private_sector_funds_all_public_goods"],
    )


def arch_22_government_food_subsidies_affordability_mechanism(rng: random.Random) -> Dict[str, Any]:
    food = rng.choice(["brown bread and maize meal", "fresh milk and cooking oil", "dried beans and rice"])
    mkt_p = rng.randint(18, 32)
    sub_p = rng.randint(3, 7)
    paid = mkt_p - sub_p
    prompt = (
        f"Suppose basic **{food}** costs **{_fmt_r(mkt_p)}** at normal market price, and the government pays producers a **{_fmt_r(sub_p)}** subsidy so households in low-income areas pay **{_fmt_r(paid)}**.\n\n"
        f"How does this **subsidy** assist South African households?"
    )
    correct = f"It lowers the retail price of essential basic foodstuffs by {_fmt_r(sub_p)}, making basic nutrition affordable for poorer families."
    distractors = [
        f"It adds an extra {_fmt_r(sub_p)} luxury tax onto every loaf of bread to discourage eating.",
        "It bans households from purchasing food from local retail spaza shops.",
        f"It requires households to repay {_fmt_r(mkt_p)} with interest to the Reserve Bank.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_22",
        subskill="22_government_food_subsidies_affordability_mechanism",
        title="Government Subsidies on Basic Foodstuffs",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**Subsidies** (alongside zero-VAT rating on staples like {food}) use state funds to keep essential living costs affordable for lower-income households.",
        hints={
            "tier_1": f"Compare {_fmt_r(paid)} (subsidised price) vs {_fmt_r(mkt_p)} (unsubsidised price).",
            "tier_2": "Government covers part of the cost to keep staple food prices lower.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_subsidies_with_taxes"],
    )


def arch_23_social_grants_supporting_vulnerable_households(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    grant = rng.choice([("Old Age Pension", "elderly citizens"), ("Child Support Grant", "orphans and vulnerable children"), ("Disability Grant", "citizens living with severe disabilities")])
    g_amt = rng.choice([530, 1080, 2180, 2190])
    prompt = (
        f"In **{area}**, government distributes social grants such as the **{grant[0]}** ({_fmt_r(g_amt)}/month) to **{grant[1]}**.\n\n"
        f"Explain two ways social grants assist **both** vulnerable households **and** local businesses in the community."
    )
    expected = "1. Helps vulnerable households afford basic needs (food, clothing, shelter); 2. Spends grant cash in local spaza shops/businesses, boosting retail turnover and sustaining local jobs."
    sol = (
        f"**Model Answer** [4 marks]:\n\n"
        f"1. **Impact on Households** [2 marks]: Provides reliable cash income ({_fmt_r(g_amt)}/month) enabling {grant[1]} to buy nutritious food, medicine, and school essentials.\n"
        f"2. **Impact on Local Businesses** [2 marks]: Recipients spend grant money at local retailers and transport operators in **{area}**, circulating cash through local enterprises."
    )
    return _build_short(
        rng,
        qid_prefix="g8_gov_23",
        subskill="23_social_grants_supporting_vulnerable_households",
        title="Economic Role of Social Grants",
        prompt=prompt,
        expected_answer=expected,
        worked_solution=sol,
        marks=4,
        hints={
            "tier_1": "First think of poverty relief for families; second think of where that cash is spent.",
            "tier_2": "Helps vulnerable people buy needs + increases local shop sales.",
            "tier_3": expected,
        },
        marking_points=[
            {"id": "mp_1", "desc": "Enables disadvantaged households to meet basic needs", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "Increases spending/turnover at local community businesses", "marks": 2, "editable": True},
        ],
        misconception_tags=["viewing_grants_outside_circular_flow"],
    )


def arch_24_government_as_employer_civil_servants(rng: random.Random) -> Dict[str, Any]:
    sc = get_ems_scenario(rng)
    roles = rng.choice(["public school teachers and clinic nurses", "municipal electricians and water engineers", "SAPS police officers and magistrates"])
    prompt = (
        f"In **{sc['area']}**, several household members work as **{roles}** employed directly by the state.\n\n"
        f"When government employs civil servants and pays their salaries, which economic roles does government perform simultaneously?"
    )
    correct = "Government acts as a Consumer of household labour (paying wages/salaries) AND as a Producer using that labour to deliver education, healthcare, safety, and utilities."
    distractors = [
        "Government avoids consuming any labour and requires volunteers to run all hospitals and schools.",
        "Government only acts as a private retail consumer selling groceries to factories.",
        "Civil servants pay zero income tax and work solely inside private JSE companies.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_24",
        subskill="24_government_as_employer_civil_servants",
        title="Government as Employer of Civil Servants",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"By hiring **{roles}**, government **consumes** labour from households (providing household income) to **produce** public services for the nation.",
        hints={
            "tier_1": "Hiring workers means buying/consuming labour; delivering teaching/healthcare means producing services.",
            "tier_2": "Consumer of labour + Producer of public services.",
            "tier_3": correct,
        },
        misconception_tags=["forgetting_gov_consumes_household_labour"],
    )


def arch_25_state_owned_enterprises_soes_role(rng: random.Random) -> Dict[str, Any]:
    soe = rng.choice([
        ("Eskom", "generating and distributing bulk electricity across South Africa"),
        ("Transnet", "operating national freight railways, pipelines, and commercial harbours"),
        ("SABC", "providing national public television and multi-language radio broadcasting"),
    ])
    name, mandate = soe
    prompt = (
        f"**{name}** is a South African **State-Owned Enterprise (SOE)** responsible for **{mandate}**.\n\n"
        f"Why does the government own and operate SOEs such as **{name}** alongside the private sector?"
    )
    correct = f"To produce strategic national utilities and infrastructure ({mandate}) that are capital-intensive or essential for the whole economy and cannot be left exclusively to private profit motives."
    distractors = [
        f"So that {name} can act solely as a private sole trader owned by a single ward councillor.",
        "To prevent any household or factory from using electricity, rail transport, or broadcasting.",
        "Because private companies never employ workers or pay corporate taxes.",
    ]
    return _build_mcq(
        rng,
        qid_prefix="g8_gov_25",
        subskill="25_state_owned_enterprises_soes_role",
        title="Role of State-Owned Enterprises (SOEs)",
        prompt=prompt,
        correct_text=correct,
        distractors=distractors,
        explanation=f"**SOEs** (such as Eskom, Transnet, and SABC) allow the state to employ South African workers and supply foundational infrastructure/services (**{mandate}**) needed by households and businesses.",
        hints={
            "tier_1": f"Think about the scale and strategic importance of {mandate}.",
            "tier_2": "SOEs provide critical infrastructure/services across the whole country.",
            "tier_3": correct,
        },
        misconception_tags=["confusing_soes_with_private_public_companies"],
    )


BUILDERS_01_25 = {
    "01_definition_of_government_and_state_authority": arch_01_definition_of_government_and_state_authority,
    "02_administering_the_state_three_goals": arch_02_administering_the_state_three_goals,
    "03_economic_participants_households_businesses_government": arch_03_economic_participants_households_businesses_government,
    "04_producers_vs_consumers_role_distinction": arch_04_producers_vs_consumers_role_distinction,
    "05_households_as_labour_producers_and_goods_consumers": arch_05_households_as_labour_producers_and_goods_consumers,
    "06_businesses_as_output_producers_and_resource_consumers": arch_06_businesses_as_output_producers_and_resource_consumers,
    "07_three_levels_of_government_hierarchy": arch_07_three_levels_of_government_hierarchy,
    "08_national_government_scope_and_leadership": arch_08_national_government_scope_and_leadership,
    "09_provincial_government_scope_leadership_and_funding": arch_09_provincial_government_scope_leadership_and_funding,
    "10_local_government_municipalities_and_leadership": arch_10_local_government_municipalities_and_leadership,
    "11_constitutional_objectives_of_local_government": arch_11_constitutional_objectives_of_local_government,
    "12_three_branches_of_national_government": arch_12_three_branches_of_national_government,
    "13_legislative_branch_parliament_lawmaking": arch_13_legislative_branch_parliament_lawmaking,
    "14_executive_branch_president_and_cabinet": arch_14_executive_branch_president_and_cabinet,
    "15_judicial_branch_constitutional_supreme_high_courts": arch_15_judicial_branch_constitutional_supreme_high_courts,
    "16_national_government_departments_functions": arch_16_national_government_departments_functions,
    "17_local_municipal_essential_utility_services": arch_17_local_municipal_essential_utility_services,
    "18_government_funding_flows_between_spheres": arch_18_government_funding_flows_between_spheres,
    "19_ward_councillor_civic_engagement_and_accountability": arch_19_ward_councillor_civic_engagement_and_accountability,
    "20_economic_diversity_unequal_service_access": arch_20_economic_diversity_unequal_service_access,
    "21_government_assisting_households_public_goods_nonprofit": arch_21_government_assisting_households_public_goods_nonprofit,
    "22_government_food_subsidies_affordability_mechanism": arch_22_government_food_subsidies_affordability_mechanism,
    "23_social_grants_supporting_vulnerable_households": arch_23_social_grants_supporting_vulnerable_households,
    "24_government_as_employer_civil_servants": arch_24_government_as_employer_civil_servants,
    "25_state_owned_enterprises_soes_role": arch_25_state_owned_enterprises_soes_role,
}
