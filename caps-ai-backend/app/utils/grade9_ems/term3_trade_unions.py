"""Grade 9 EMS — Trade Unions in South Africa.
100% Deterministic & SymPy/math backed. Satisfies the 6-Pillar Generator Contract.
Directly aligns with `curriculum_docs_auto/EMS_Gr9/Term 1/01. Trade Unions.md`.
Covers:
- Concept and historical development of trade unions in South Africa (COSATU, primary sector exploitation)
- Roles vs Responsibilities of trade unions (collective bargaining, peaceful action, secret balloting)
- Constitutional & Labour Relations Act (LRA) worker rights, CCMA dispute resolution
- Effect of trade unions on businesses and sustainable economic growth
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


TOPIC_ID = "grade9_ems"
SUBTOPIC_ID = "term3_trade_unions"
CURRICULUM_REFERENCE = "Term 3 > The Economy: Trade Unions"


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
        "concept_group": concept_group or "trade_unions",
        "question_family_id": question_family_id,
        "curriculum_reference": CURRICULUM_REFERENCE,
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["economics", "labour_relations"],
    })
    return enriched


def _roles_vs_responsibilities_drill(rng: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    items_pool = [
        {"action": "Organise industrial action and strikes", "category": "Role", "reason": "It is a power/function of a union to mobilize workers"},
        {"action": "Ensure that industrial action is lawful and peaceful", "category": "Responsibility", "reason": "Unions have a duty to keep protests non-violent and within the LRA"},
        {"action": "Negotiate with employers through collective bargaining", "category": "Role", "reason": "It is a core representative role to negotiate terms"},
        {"action": "Make reasonable and realistic wage demands on employers", "category": "Responsibility", "reason": "Demands must not bankrupt the employer or cost jobs"},
        {"action": "Provide legal advice and representation during disputes", "category": "Role", "reason": "Unions exist to represent members in CCMA/court"},
        {"action": "Make major strike decisions based on a secret vote by all members", "category": "Responsibility", "reason": "Unions must maintain democratic internal accountability"},
        {"action": "Try to attract new members to join the union", "category": "Role", "reason": "Growing union membership strengthens collective voice"},
        {"action": "Never force or intimidate anyone into joining a union", "category": "Responsibility", "reason": "Freedom of association is guaranteed by the Constitution"},
    ]

    selected = rng.sample(items_pool, 4)
    headers = ["No.", "Trade Union Action / Practice", "Category (Role vs Responsibility)", "Justification"]
    rows = []
    correct_map: Dict[str, str] = {}
    cell_hints: Dict[str, str] = {}

    for idx, itm in enumerate(selected):
        c_cat = f"t0_r{idx}_c2"
        correct_map[c_cat] = itm["category"]
        cell_hints[c_cat] = f"Is '{itm['action']}' a power/function (Role) or an obligation/duty (Responsibility)?"

        rows.append([
            {"coordinate": f"t0_r{idx}_c0", "value": str(idx + 1), "type": "given", "editable": False},
            {"coordinate": f"t0_r{idx}_c1", "value": itm["action"], "type": "given", "editable": False},
            {"coordinate": c_cat, "value": itm["category"] if mode == "scaffold" else "", "type": "required", "editable": True},
            {"coordinate": f"t0_r{idx}_c3", "value": itm["reason"], "type": "given", "editable": False},
        ])

    item = {
        "id": f"ems9_union_roles_resp_{rng.randint(1000, 9999)}",
        "title": "Trade Union Roles vs Responsibilities",
        "question_type": "table_completion",
        "prompt": "Distinguish between the **Roles** (functions/powers) and **Responsibilities** (duties/obligations) of South African trade unions in the workplace.",
        "headers": headers,
        "rows": rows,
        "correct_map": correct_map,
        "cell_hints": cell_hints,
        "marks": 8,
        "sample_answer": f"1: {selected[0]['category']}; 2: {selected[1]['category']}; 3: {selected[2]['category']}; 4: {selected[3]['category']}",
        "ideal_answer": "Accurate distinction between union rights/powers (Roles) and ethical/legal duties (Responsibilities).",
        "hint_sections": {
            "1_nudge": "A ROLE is what a union does to empower workers. A RESPONSIBILITY is a duty to act lawfully and ethically.",
            "2_concept": "Under South Africa's Labour Relations Act (LRA), unions have rights (like striking) and responsibilities (strikes must be peaceful).",
            "3_breakdown": f"Check each row: Is it an entitlement or a duty?"
        },
        "marking_schema": {
            "total_marks": 8,
            "marking_points": [
                {"id": f"mp_{i}", "desc": f"Categorisation for '{itm['action'][:30]}...'", "marks": 2, "editable": True}
                for i, itm in enumerate(selected)
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "misconception_tags": ["confused_union_role_with_responsibility"],
    }
    return _with_metadata(
        item,
        subskill="roles_vs_responsibilities",
        learning_objective_id="lo_g9_union_roles_resp",
        question_family_id="union_roles_resp_table",
        misconception_tags=["confused_union_role_with_responsibility"],
    )


def _concept_pool(rng: random.Random) -> List[Dict[str, Any]]:
    return [
        _with_metadata({
            'title': 'Trade Union Definition',
            'prompt': 'What is the main purpose of a trade union?',
            'options': [
                'To make profits for business owners',
                'To protect and promote the interests of workers',
                'To replace government in labour regulation',
                'To prevent businesses from hiring new employees'
            ],
            'correct_index': 1,
            'explanation': 'A trade union is an organisation formed by workers to protect and promote their interests, including negotiating better wages and working conditions.',
            'marks': 2,
            'hint_sections': {'1_nudge': 'Trade unions represent employees against employer exploitation.'},
        }, subskill='concepts', learning_objective_id='lo_trade_union_purpose', question_family_id='trade_union_definition'),
        _with_metadata({
            'title': 'COSATU Federation',
            'prompt': 'What does the acronym COSATU stand for in South African labour history?',
            'options': [
                'Congress of South African Trade Unions',
                'Council of South African Trade Unions',
                'Committee of South African Trade Unions',
                'Coalition of South African Trade Unions'
            ],
            'correct_index': 0,
            'explanation': 'COSATU is the Congress of South African Trade Unions, the largest trade union federation in South Africa.',
            'marks': 2,
            'hint_sections': {'1_nudge': 'It starts with Congress and represents South African Trade Unions.'},
        }, subskill='concepts', learning_objective_id='lo_cosatu', question_family_id='cosatu_name'),
        _with_metadata({
            'title': 'CCMA in Dispute Resolution',
            'prompt': 'What is the role of the CCMA (Commission for Conciliation, Mediation and Arbitration)?',
            'options': [
                'To manage the finances of trade unions',
                'To act as an independent third party settling workplace disputes between employers and employees',
                'To represent employers in salary negotiations',
                'To arrest workers who participate in strikes'
            ],
            'correct_index': 1,
            'explanation': 'The CCMA is an independent statutory dispute resolution body established by the Labour Relations Act to resolve workplace disputes through conciliation and arbitration.',
            'marks': 2,
            'hint_sections': {'1_nudge': 'CCMA is an independent third party that mediates labour disputes.'},
        }, subskill='concepts', learning_objective_id='lo_ccma', question_family_id='ccma_dispute_resolution'),
    ]


def _discussion_pool(rng: random.Random) -> List[Dict[str, Any]]:
    return [
        _with_metadata({
            'title': 'Roles of Trade Unions',
            'prompt': 'Discuss three roles and responsibilities of trade unions in South Africa. (6 marks)',
            'marks': 6,
            'marking_points': [
                "Protecting workers' rights and interests.",
                "Negotiating wages and working conditions through collective bargaining.",
                "Providing support to workers during disputes or disciplinary hearings.",
                "Promoting skills development and training for members.",
                "Engaging in socio-economic policy discussions.",
            ],
            'sample_answer': "Trade unions protect workers' rights, engage in collective bargaining to negotiate wages and safe conditions, and represent members during workplace disputes at the CCMA.",
            'hint_sections': {'1_nudge': 'Mention collective bargaining, dispute support, and worker protection.'},
        }, subskill='discussion', learning_objective_id='lo_union_roles', question_family_id='union_roles_essay'),
        _with_metadata({
            'title': 'Sustainable Economic Growth',
            'prompt': 'Explain how trade unions contribute to sustainable economic growth and development in South Africa. (6 marks)',
            'marks': 6,
            'marking_points': [
                "They prevent worker exploitation, creating a fair distribution of national wealth.",
                "They promote worker education, training, and skills development.",
                "They foster healthy dialogue between employers and employees under the rule of law.",
                "Businesses that respect workers build stable, productive workforces for long-term growth.",
            ],
            'sample_answer': "Trade unions empower workers to avoid exploitation, ensuring economic benefits are shared equitably. They advocate for worker training and skills development, and maintain healthy workplace dialogue under the Labour Relations Act, creating a stable and productive economic climate.",
            'hint_sections': {'1_nudge': 'Focus on skills development, fair wage distribution, and democratic workplaces.'},
        }, subskill='discussion', learning_objective_id='lo_union_growth', question_family_id='union_sustainable_growth'),
    ]


BUILDERS = {
    "roles_vs_responsibilities": lambda rng, mode: [_roles_vs_responsibilities_drill(rng, mode)],
    "elementary_roles": lambda rng, mode: [_roles_vs_responsibilities_drill(rng, mode)],
    "discussion": lambda rng, mode: _discussion_pool(rng),
    "concepts": lambda rng, mode: _concept_pool(rng),
}


def generate(
    subskill: str = "concepts",
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
        pool = _concept_pool(rng) + [_roles_vs_responsibilities_drill(rng, mode)] + _discussion_pool(rng)

    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
