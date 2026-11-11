from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional
from .scenario_builder import build_scenario


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str, hint_trigger: Optional[str] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_ethics_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 2,
        "hint_trigger": hint_trigger or explanation,
        "guidelines": [hint_trigger or explanation],
        "visual_aid_key": "ethics_principles",
    }


def _make_typed(*, prompt: str, sample_answer: str, grading_rubric: List[str]) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_ethics_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
        "grading_rubric": grading_rubric,
        "marks": 4,
        "hint_trigger": f"Ensure your answer touches on: {', '.join(grading_rubric)}",
        "guidelines": [f"Ensure your answer touches on: {', '.join(grading_rubric)}"],
        "visual_aid_key": "ethics_principles",
    }


def _make_table_wordbank(
    *,
    prompt: str,
    headers: List[str],
    rows: List[List[str]],
    word_bank: List[Dict[str, str]],
    correct_map: Dict[str, Dict[str, str]],
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    id_to_label = {str(w.get("id")): str(w.get("label")) for w in (word_bank or []) if isinstance(w, dict)}
    clean_headers = [h for h in headers[:3] if h]
    if len(clean_headers) < 3:
        clean_headers = ["No.", "Description", "Ethical Term"]
    norm_rows: List[List[str]] = []
    flat_map: Dict[str, str] = {}
    for r_idx, row in enumerate(rows):
        row_cells = [str(row[0]) if len(row) > 0 else str(r_idx + 1), str(row[1]) if len(row) > 1 else "", f"{{r{r_idx}_c2}}"]
        norm_rows.append(row_cells)
        row_map = correct_map.get(str(r_idx), {})
        tok_id = str(row_map.get("2") or "") if isinstance(row_map, dict) else str(row_map)
        flat_map[f"r{r_idx}_c2"] = id_to_label.get(tok_id, tok_id)
    bank_labels = " | ".join(f"`{w.get('label')}`" for w in (word_bank or []) if isinstance(w, dict) and w.get("label"))
    full_prompt = f"{prompt}\n\n**Term Bank:** {bank_labels}" if bank_labels else prompt
    return {
        "id": _make_id("acct10_ethics_table_fill"),
        "question_type": "table_fill",
        "prompt": full_prompt,
        "question_text": full_prompt,
        "headers": clean_headers,
        "rows": norm_rows,
        "correct_map": flat_map,
        "guidelines": guidelines or [],
        "marks": len(norm_rows) * 2,
    }


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    
    # Generate Scenario for Context Injection
    scenario = build_scenario(seed=seed)
    intro = scenario["intro"]

    concepts_pool: List[Dict[str, Any]] = []
    principles_pool: List[Dict[str, Any]] = []
    leadership_pool: List[Dict[str, Any]] = []
    principles_matching_pool: List[Dict[str, Any]] = []
    terminology_matching_pool: List[Dict[str, Any]] = []

    concepts_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nWhat is the main purpose of {scenario['business']}'s code of ethics?",
            options=[
                f"To simply act as a marketing tool to increase sales for the {scenario['industry']}.",
                "To describe acceptable behaviour and guide decisions about right and wrong.",
                "To replace all company operational procedures.",
                f"To guarantee {scenario['owner']} makes a profit this financial year.",
            ],
            correct_index=1,
            explanation="A code of ethics states norms and beliefs and helps people know what is right/wrong in specific situations.",
        )
    )

    concepts_pool.append(
        _make_typed(
            prompt=f"{intro}\n\nIn your own words, explain to {scenario['owner']} what a 'code of ethics' is and why it's necessary.",
            sample_answer="A code of ethics is a written statement of a business's norms and beliefs that explains acceptable behaviour and guides people on what is right and wrong at work.",
            grading_rubric=["written statement", "norms and beliefs", "acceptable behavior / right and wrong"],
        )
    )

    principles_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nWhen {scenario['owner']} makes a mistake on the financial statements, they immediately correct it and notify the stakeholders. Which principle means taking responsibility for what you say and do, and being able to justify your actions?",
            options=["Transparency", "Accountability", "Objectivity", "Confidentiality"],
            correct_index=1,
            explanation="Accountability is taking responsibility and being able to justify actions.",
        )
    )

    principles_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nA friend of {scenario['owner']} asks for a discount that violates company policy. Which principle describes acting without bias and not being influenced by personal feelings?",
            options=["Objectivity", "Discipline", "Integrity", "Sustainability"],
            correct_index=0,
            explanation="Objectivity is the ability to act in an unbiased way and base decisions on true facts.",
        )
    )

    leadership_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nGood ethical leadership from {scenario['owner']} is most visible when their employees obey because they: ",
            options=[
                f"fear punishment and losing their job at {scenario['business']}.",
                f"respect what {scenario['owner']} says and does.",
                "want to be promoted quickly to middle management.",
                "have no other choice in the local area.",
            ],
            correct_index=1,
            explanation="Good leadership is visible when followers obey out of respect for the leader's actions and words.",
        )
    )

    leadership_pool.append(
        _make_typed(
            prompt=f"{intro}\n\nGive one example of how {scenario['owner']} as a manager can show 'integrity' at work.",
            sample_answer="Example: The manager is honest and does not use their position to enrich themselves; they set a positive example and follow the same rules as everyone else.",
            grading_rubric=["honesty / not self-enriching", "setting positive examples", "following rules"],
        )
    )

    matching_items = [
        {
            "definition": "Can be defined as honesty, efficiency, sincerity, and upholding values and norms.",
            "term": "Integrity",
        },
        {
            "definition": "Taking responsibility for what you say and do; being able to justify your actions.",
            "term": "Accountability",
        },
        {
            "definition": "Behaviour must be such that it is clear that you have nothing to hide.",
            "term": "Transparency",
        },
        {
            "definition": "The ability to act in an unbiased way.",
            "term": "Objectivity",
        },
    ]

    distractors = [
        "Discipline",
        "Confidentiality",
        "Fairness",
        "Sustainability",
        "Professional conduct",
    ]

    r.shuffle(matching_items)
    used_distractors = r.sample(distractors, k=2)
    terms = [m["term"] for m in matching_items] + used_distractors
    r.shuffle(terms)

    word_bank: List[Dict[str, str]] = [
        {"id": f"t{i}", "label": t} for i, t in enumerate(terms)
    ]
    label_to_id = {t["label"]: t["id"] for t in word_bank}

    rows = []
    correct_map: Dict[str, Dict[str, str]] = {}
    for i, item in enumerate(matching_items):
        rows.append([str(i + 1), item["definition"], "", ""])
        correct_map[str(i)] = {
            "2": str(label_to_id[item["term"]]),
            "3": None,
        }

    principles_matching_pool.append(
        _make_table_wordbank(
            prompt=f"{intro}\n\nMatching columns. Choose the correct ethical term for each definition.",
            headers=["No.", "Definition (Column A)", "Term (Column B)", ""],
            rows=rows,
            word_bank=word_bank,
            correct_map=correct_map,
            guidelines=[
                "Read the definition carefully.",
                "Place one term in the 'Term (Column B)' column for each row.",
            ],
        )
    )

    # Activity 2 (Crossword adaptation)
    terminology_items = [
        {"definition": "A statement of norms and beliefs of the business, describing acceptable behaviour in the work place.", "term": "Code of ethics"},
        {"definition": "The quality of being reasonable and just.", "term": "Fairness"},
        {"definition": "Honesty, efficiency, sincerity, and upholding values and norms.", "term": "Integrity"},
        {"definition": "A position or state of being in control of a group of people or an organisation.", "term": "Leadership"},
        {"definition": "Information should not be leaked to people outside the business.", "term": "Confidentiality"},
        {"definition": "Showing respect towards the environment and the use of resources over the long term.", "term": "Sustainability"},
    ]
    term_distractors = ["Discipline", "Accountability", "Objectivity", "Due care"]
    r.shuffle(terminology_items)
    used_term_distractors = r.sample(term_distractors, k=2)
    terminology_terms = [m["term"] for m in terminology_items] + used_term_distractors
    r.shuffle(terminology_terms)

    term_word_bank: List[Dict[str, str]] = [
        {"id": f"t2_{i}", "label": t} for i, t in enumerate(terminology_terms)
    ]
    term_label_to_id = {t["label"]: t["id"] for t in term_word_bank}

    term_rows = []
    term_correct_map: Dict[str, Dict[str, str]] = {}
    for i, item in enumerate(terminology_items):
        term_rows.append([str(i + 1), item["definition"], "", ""])
        term_correct_map[str(i)] = {
            "2": str(term_label_to_id[item["term"]]),
            "3": None,
        }

    terminology_matching_pool.append(
        _make_table_wordbank(
            prompt=f"{intro}\n\nEthics Terminology. Choose the correct ethical term for each definition below.",
            headers=["No.", "Definition", "Term", ""],
            rows=term_rows,
            word_bank=term_word_bank,
            correct_map=term_correct_map,
            guidelines=[
                "Read the definition carefully.",
                "Place one term in the 'Term' column for each row.",
            ],
        )
    )

    concepts_pool = [{**q, "subskill": "code_of_ethics_concepts"} for q in concepts_pool if q.get("question_type") != "typed"]
    principles_pool = [{**q, "subskill": "ethical_principles_application"} for q in principles_pool if q.get("question_type") != "typed"]
    leadership_pool = [{**q, "subskill": "ethical_leadership_and_integrity"} for q in leadership_pool if q.get("question_type") != "typed"]
    principles_matching_pool = [{**q, "subskill": "ethical_principles_matching"} for q in principles_matching_pool]
    terminology_matching_pool = [{**q, "subskill": "ethics_terminology_matching"} for q in terminology_matching_pool]

    all_pools = {
        "concepts": concepts_pool,
        "code_of_ethics": concepts_pool,
        "code_of_ethics_concepts": concepts_pool,
        "principles": principles_pool,
        "ethical_principles_application": principles_pool,
        "leadership": leadership_pool,
        "ethical_leadership_and_integrity": leadership_pool,
        "principles_matching": principles_matching_pool,
        "ethical_principles_matching": principles_matching_pool,
        "terminology_matching": terminology_matching_pool,
        "ethics_terminology_matching": terminology_matching_pool,
        "mixed": concepts_pool + principles_pool + leadership_pool + principles_matching_pool + terminology_matching_pool,
        "ethics": concepts_pool + principles_pool + leadership_pool + principles_matching_pool + terminology_matching_pool,
    }

    sub_pools = [p for p in (concepts_pool, principles_pool, leadership_pool, principles_matching_pool, terminology_matching_pool) if p]
    if subskill_norm in ("mixed", "ethics", "all", "") and sub_pools:
        questions: List[Dict[str, Any]] = []
        for _ in range(n):
            chosen_pool = r.choice(sub_pools)
            questions.append(r.choice(chosen_pool))
        return questions

    pool = all_pools.get(subskill_norm, all_pools["mixed"])
    if not pool:
        pool = all_pools["mixed"]

    questions = []
    for _ in range(n):
        questions.append(r.choice(pool))

    return questions


SUBSKILLS = [
    "code_of_ethics_concepts",
    "ethical_principles_application",
    "ethical_leadership_and_integrity",
    "ethical_principles_matching",
    "ethics_terminology_matching",
]
