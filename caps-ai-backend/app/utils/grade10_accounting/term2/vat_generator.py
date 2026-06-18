from __future__ import annotations

import random
import json
import uuid
from typing import Any, Dict, List, Optional

from ...sole_trader.names import pick_business_name as _pick_business_name
from ...sole_trader.names import pick_person_names as _pick_person_names


class _VATScenarioValidationError(ValueError):
    pass


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _round_money(x: float) -> float:
    return round(float(x) + 1e-9, 2)


VAT_RATE = 0.15  # 15% standard rate


def _normalize_subskill(subskill: str) -> str:
    key = str(subskill or "mixed").strip().lower()
    mapping = {
        "vat": "mixed",
        "vat_concepts": "concepts",
        "vat_calculations": "calculations",
        "vat_classification": "classification",
        "vat_ethics": "ethics",
    }
    return mapping.get(key, key or "mixed")


def _question_signature(question: Dict[str, Any]) -> str:
    payload = {
        "question_type": question.get("question_type"),
        "prompt": question.get("prompt"),
        "options": question.get("options"),
        "correct_answer": question.get("correct_answer"),
        "correct_index": question.get("correct_index"),
        "sample_answer": question.get("sample_answer"),
        "working_formula": question.get("working_formula"),
        "table": question.get("table"),
        "word_bank": question.get("word_bank"),
        "correct_map": question.get("correct_map"),
    }
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, default=str)


def _select_questions(pool: List[Dict[str, Any]], *, n: int, r: random.Random) -> List[Dict[str, Any]]:
    if not pool:
        return []

    signature_to_question: Dict[str, Dict[str, Any]] = {}
    unique_questions: List[Dict[str, Any]] = []
    for question in pool:
        signature = _question_signature(question)
        if signature in signature_to_question:
            continue
        signature_to_question[signature] = question
        unique_questions.append(question)

    if len(unique_questions) >= n:
        return r.sample(unique_questions, n)

    selected = list(unique_questions)
    while len(selected) < n:
        selected.append(r.choice(pool))
    return selected


def _build_answer_part_hints(items: Optional[List[str]], *, prefix: str = "Answer part") -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for idx, item in enumerate(items or []):
        text = str(item or "").strip()
        if not text:
            continue
        out.append({"label": f"{prefix} {idx + 1}", "value": text})
    return out


def _build_derivation_map(items: Optional[List[str]], *, prefix: str = "Step") -> Dict[str, str]:
    out: Dict[str, str] = {}
    for idx, item in enumerate(items or []):
        text = str(item or "").strip()
        if not text:
            continue
        out[f"{prefix} {idx + 1}"] = text
    return out


def _make_cell_key(row_index: int, column_index: int) -> str:
    return f"{row_index}:{column_index}"


def _with_validation(question: Dict[str, Any], family: str, **context: Any) -> Dict[str, Any]:
    enriched = dict(question)
    enriched["scenario_validation"] = {"family": family, **context}
    return enriched


def _expect(condition: bool, message: str) -> None:
    if not condition:
        raise _VATScenarioValidationError(message)


def _validate_question(question: Dict[str, Any]) -> Dict[str, Any]:
    q = dict(question)
    question_type = str(q.get("question_type") or "").strip().lower()
    prompt = str(q.get("prompt") or "").strip()
    _expect(bool(prompt), "VAT question is missing a prompt.")

    if question_type == "mcq":
        options = q.get("options")
        correct_index = q.get("correct_index")
        _expect(isinstance(options, list) and len(options) >= 2, "VAT MCQ must have at least two options.")
        _expect(isinstance(correct_index, int) and 0 <= correct_index < len(options), "VAT MCQ has an invalid correct_index.")
        return q

    if question_type == "typed":
        sample_answer = str(q.get("sample_answer") or "").strip()
        _expect(bool(sample_answer), "VAT typed question must provide a sample_answer.")
        return q

    if question_type == "calc":
        correct_answer = q.get("correct_answer")
        _expect(isinstance(correct_answer, (int, float)), "VAT calc question must provide a numeric correct_answer.")
        _expect(abs(float(correct_answer)) < 1_000_000_000, "VAT calc correct_answer is implausibly large.")
        formula_hint = str(q.get("formula_hint") or "").strip()
        working_formula = str(q.get("working_formula") or "").strip()
        _expect(bool(formula_hint or working_formula), "VAT calc question must provide a formula hint or working formula.")
        return q

    if question_type == "table_wordbank":
        table = q.get("table") if isinstance(q.get("table"), dict) else {}
        headers = table.get("headers") if isinstance(table.get("headers"), list) else []
        rows = table.get("rows") if isinstance(table.get("rows"), list) else []
        word_bank = q.get("word_bank") if isinstance(q.get("word_bank"), list) else []
        correct_map = q.get("correct_map") if isinstance(q.get("correct_map"), dict) else {}
        _expect(len(headers) >= 3, "VAT table_wordbank question must have at least three headers.")
        _expect(len(rows) > 0, "VAT table_wordbank question must have at least one row.")
        _expect(len(word_bank) >= 2, "VAT table_wordbank question must have at least two word bank options.")
        token_ids = {str(token.get("id")) for token in word_bank if isinstance(token, dict) and str(token.get("id") or "").strip()}
        _expect(bool(token_ids), "VAT table_wordbank question must have valid token ids.")
        mapped_rows = 0
        for row_index, row in enumerate(rows):
            _expect(isinstance(row, list) and len(row) >= 3, f"VAT table_wordbank row {row_index} is malformed.")
        for row_key, col_map in correct_map.items():
            _expect(isinstance(col_map, dict), f"VAT table_wordbank correct_map row {row_key} is malformed.")
            token_id = str(col_map.get("2") or "").strip()
            if not token_id:
                continue
            mapped_rows += 1
            _expect(token_id in token_ids, f"VAT table_wordbank row {row_key} references unknown token id '{token_id}'.")
        _expect(mapped_rows > 0, "VAT table_wordbank question must map at least one row to a correct token.")
        return q

    raise _VATScenarioValidationError(f"Unsupported VAT question type '{question_type}'.")


def _validate_pool(pool: List[Dict[str, Any]], *, family: str) -> List[Dict[str, Any]]:
    valid: List[Dict[str, Any]] = []
    for question in pool:
        try:
            valid.append(_validate_question(question))
        except _VATScenarioValidationError:
            continue
    if not valid:
        raise _VATScenarioValidationError(f"No valid VAT questions were generated for family '{family}'.")
    return valid


def _set_recommended_difficulties(question: Dict[str, Any], *levels: str) -> Dict[str, Any]:
    enriched = dict(question)
    normalized = [str(level or "").strip().lower() for level in levels if str(level or "").strip()]
    enriched["recommended_difficulties"] = normalized or ["easy", "medium", "hard"]
    return enriched


def _difficulty_matches(question: Dict[str, Any], difficulty: str) -> bool:
    allowed = question.get("recommended_difficulties")
    if not isinstance(allowed, list) or not allowed:
        return True
    difficulty_norm = str(difficulty or "easy").strip().lower()
    return difficulty_norm in [str(level or "").strip().lower() for level in allowed]


def _difficulty_fallback_order(difficulty: str) -> List[str]:
    difficulty_norm = str(difficulty or "easy").strip().lower()
    mapping = {
        "easy": ["easy", "medium", "hard"],
        "medium": ["medium", "easy", "hard"],
        "hard": ["hard", "medium", "easy"],
    }
    return mapping.get(difficulty_norm, ["easy", "medium", "hard"])


def _pool_for_difficulty(pool: List[Dict[str, Any]], difficulty: str) -> List[Dict[str, Any]]:
    for level in _difficulty_fallback_order(difficulty):
        matches = [question for question in pool if _difficulty_matches(question, level)]
        if matches:
            return matches
    return list(pool)


def _assign_recommended_difficulties(pool: List[Dict[str, Any]], *, family: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    family_norm = str(family or "").strip().lower()
    for question in pool:
        prompt = str(question.get("prompt") or "").strip().lower()
        question_type = str(question.get("question_type") or "").strip().lower()

        if family_norm == "concepts":
            if question_type == "typed" or question_type == "table_wordbank" or "invoice basis" in prompt or "goods taken by the owner" in prompt or "input vat is vat collected" in prompt:
                levels = ["medium", "hard"]
            else:
                levels = ["easy", "medium"]
        elif family_norm == "calculations":
            if "vat payable" in prompt or "vat refundable" in prompt or "mark-up" in prompt or "selling price" in prompt or "customer pays" in prompt or "vat amount on an invoice" in prompt:
                levels = ["medium", "hard"]
            else:
                levels = ["easy", "medium"]
        elif family_norm == "classification":
            if question_type == "table_wordbank":
                levels = ["easy", "medium"]
            elif question_type == "typed" or "input vat as a deduction" in prompt or "correctly compares zero-rated and exempt" in prompt:
                levels = ["medium", "hard"]
            else:
                levels = ["easy", "medium"]
        elif family_norm == "ethics":
            if question_type == "typed" or "zero-rated items" in prompt or "conducts themselves unethically" in prompt:
                levels = ["medium", "hard"]
            else:
                levels = ["easy", "medium"]
        else:
            levels = ["easy", "medium", "hard"]

        out.append(_set_recommended_difficulties(question, *levels))
    return out


def _select_mixed_questions_balanced(
    pools_by_subskill: Dict[str, List[Dict[str, Any]]],
    *,
    n: int,
    difficulty: str,
    r: random.Random,
) -> List[Dict[str, Any]]:
    ordered_subskills = [
        name for name in ["concepts", "calculations", "classification", "ethics"]
        if pools_by_subskill.get(name)
    ]
    if not ordered_subskills:
        return []

    working_pools: Dict[str, List[Dict[str, Any]]] = {}
    for name in ordered_subskills:
        prepared = list(_pool_for_difficulty(pools_by_subskill[name], difficulty))
        r.shuffle(prepared)
        working_pools[name] = prepared

    selected: List[Dict[str, Any]] = []
    used_signatures = set()

    while len(selected) < n:
        progress = False
        for name in ordered_subskills:
            pool = working_pools.get(name, [])
            while pool:
                candidate = pool.pop()
                signature = _question_signature(candidate)
                if signature in used_signatures:
                    continue
                used_signatures.add(signature)
                selected.append(candidate)
                progress = True
                break
            if len(selected) >= n:
                break
        if not progress:
            break

    if len(selected) < n:
        combined_unique: List[Dict[str, Any]] = []
        for name in ordered_subskills:
            combined_unique.extend(_pool_for_difficulty(pools_by_subskill[name], difficulty))
        r.shuffle(combined_unique)
        for candidate in combined_unique:
            if len(selected) >= n:
                break
            signature = _question_signature(candidate)
            if signature in used_signatures:
                continue
            used_signatures.add(signature)
            selected.append(candidate)

    if len(selected) < n:
        combined_fallback = [question for name in ordered_subskills for question in _pool_for_difficulty(pools_by_subskill[name], difficulty)]
        if not combined_fallback:
            combined_fallback = [question for name in ordered_subskills for question in pools_by_subskill[name]]
        while combined_fallback and len(selected) < n:
            selected.append(r.choice(combined_fallback))

    return selected


# ---------------------------------------------------------------------------
# VAT hint helper functions
# ---------------------------------------------------------------------------

def _vat_rate_hint() -> Dict[str, str]:
    return {"label": "VAT rate", "value": f"{VAT_RATE * 100}%"}


def _vat_output_hint() -> Dict[str, str]:
    return {"label": "VAT output", "value": "VAT charged on sales"}


def _vat_input_hint() -> Dict[str, str]:
    return {"label": "VAT input", "value": "VAT paid on purchases"}


def _vat_payable_hint() -> Dict[str, str]:
    return {"label": "VAT payable", "value": "Output VAT - Input VAT"}


def _build_calc_support(*, formula_hint: str, relevant_values: List[str], method: str, derivation_steps: List[str]) -> Dict[str, Any]:
    cleaned_values = [str(value or "").strip() for value in relevant_values if str(value or "").strip()]
    answer_part_hints: List[Dict[str, str]] = []
    if cleaned_values:
        answer_part_hints.append({"label": "Relevant values", "value": "\n".join(cleaned_values)})
    if str(method or "").strip():
        answer_part_hints.append({"label": "Method", "value": str(method).strip()})
    return {
        "formula_hint": str(formula_hint or "").strip(),
        "guidelines": [
            "First identify whether the given amount is VAT-inclusive, VAT-exclusive, or the VAT amount only.",
            str(method or "").strip(),
        ],
        "answer_part_hints": answer_part_hints,
        "derivation_map": _build_derivation_map(derivation_steps),
    }


def _build_classification_support(rows: List[List[str]], correct_map: Dict[str, Dict[str, str]]) -> Dict[str, Any]:
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    derivation_map: Dict[str, str] = {}

    for row_index, row in enumerate(rows):
        item = str((row[1] if len(row) > 1 else "") or "").strip()
        code = str(correct_map.get(str(row_index), {}).get("2") or "")
        cell_key = _make_cell_key(row_index, 2)

        if code == "zero":
            label = "Zero-rated (0%)"
            where_to_look = f"{item} is treated as a zero-rated basic item or qualifying zero-rate supply."
            record_link = "Zero-rated supplies are taxable supplies charged at 0%, so the vendor does not add output VAT but may still claim input VAT on related purchases."
        elif code == "exempt":
            label = "Exempt"
            where_to_look = f"{item} falls into an exempt service or exempt delivery category."
            record_link = "Exempt supplies do not have VAT charged and related input VAT may generally not be claimed."
        else:
            label = "Taxable (15%)"
            where_to_look = f"{item} is an ordinary taxable good or service rather than a zero-rated or exempt item."
            record_link = "Taxable supplies are standard-rated, so output VAT is charged at 15%."

        cell_hints[cell_key] = f"Ask whether {item} is a zero-rated basic item, an exempt service, or an ordinary taxable supply."
        cell_teaching_map[cell_key] = {
            "what_to_enter": f"Select '{label}'.",
            "where_to_look": where_to_look,
            "method_or_formula": "Classify the item by VAT category: zero-rated, exempt, or taxable at the standard rate.",
            "record_link": record_link,
        }
        derivation_map[cell_key] = f"{item} fits the {label} category, so that is the correct classification for this cell."

    return {
        "cell_hints": cell_hints,
        "cell_teaching_map": cell_teaching_map,
        "derivation_map": derivation_map,
    }


def _build_flow_table_support(
    rows: List[List[str]],
    correct_map: Dict[str, Dict[str, str]],
    teaching_by_code: Dict[str, Dict[str, str]],
) -> Dict[str, Any]:
    cell_hints: Dict[str, str] = {}
    cell_teaching_map: Dict[str, Dict[str, str]] = {}
    derivation_map: Dict[str, str] = {}

    for row_index, row in enumerate(rows):
        item = str((row[1] if len(row) > 1 else "") or "").strip()
        code = str(correct_map.get(str(row_index), {}).get("2") or "")
        cell_key = _make_cell_key(row_index, 2)
        teaching = dict(teaching_by_code.get(code, {}))
        label = str(teaching.get("label") or code or "Correct category").strip()
        cell_hints[cell_key] = f"Decide whether '{item}' gives rise to input VAT, output VAT, or no VAT claim/charge."
        cell_teaching_map[cell_key] = {
            "what_to_enter": f"Select '{label}'.",
            "where_to_look": str(teaching.get("where_to_look") or "Use the transaction wording to decide whether the business bought or sold taxable goods/services.").strip(),
            "method_or_formula": str(teaching.get("method_or_formula") or "Purchases usually create input VAT; sales usually create output VAT; non-VAT items have no VAT claim/charge.").strip(),
            "record_link": str(teaching.get("record_link") or "Only taxable purchases and taxable sales affect VAT input/output. Non-VAT items like salaries do not create VAT.").strip(),
        }
        derivation_map[cell_key] = str(teaching.get("derivation") or f"{item} belongs in the '{label}' category.").strip()

    return {
        "cell_hints": cell_hints,
        "cell_teaching_map": cell_teaching_map,
        "derivation_map": derivation_map,
    }


# ---------------------------------------------------------------------------
# Question factories
# ---------------------------------------------------------------------------

def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_vat_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 2,
        "guidelines": [explanation],
        "visual_aid_key": "vat_overview",
    }


def _make_typed(
    *,
    prompt: str,
    sample_answer: str,
    grading_rubric: Optional[List[str]] = None,
    guidelines: Optional[List[str]] = None,
    answer_part_hints: Optional[List[Dict[str, str]]] = None,
    derivation_map: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    rubric = grading_rubric or []
    return {
        "id": _make_id("acct10_vat_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
        "grading_rubric": rubric,
        "marks": 4 if rubric and len(rubric) >= 2 else 2,
        "guidelines": guidelines if guidelines is not None else ([f"Ensure your answer includes: {', '.join(rubric)}"] if rubric else []),
        "answer_part_hints": answer_part_hints if answer_part_hints is not None else _build_answer_part_hints(rubric),
        "derivation_map": derivation_map if derivation_map is not None else ({"Guideline answer": sample_answer} if str(sample_answer or "").strip() else {}),
        "visual_aid_key": "vat_overview",
    }


def _make_calc(
    *,
    prompt: str,
    correct_answer: float,
    unit: str = "R",
    working_formula: str = "",
    formula_hint: str = "",
    guidelines: Optional[List[str]] = None,
    answer_part_hints: Optional[List[Dict[str, str]]] = None,
    derivation_map: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_vat_calc"),
        "question_type": "calc",
        "prompt": prompt,
        "correct_answer": float(correct_answer),
        "unit": unit,
        "working_formula": working_formula,
        "formula_hint": str(formula_hint or working_formula or "").strip(),
        "expected_answer_type": "number",
        "marks": 3,
        "guidelines": guidelines if guidelines is not None else ([f"Formula: {working_formula}"] if working_formula else []),
        "answer_part_hints": answer_part_hints if answer_part_hints is not None else [],
        "derivation_map": derivation_map if derivation_map is not None else _build_derivation_map([
            working_formula,
            f"Answer = {unit}{float(correct_answer):,.2f}",
        ]),
        "visual_aid_key": "vat_calculations",
    }


def _make_table_wordbank(
    *,
    prompt: str,
    headers: List[str],
    rows: List[List[str]],
    word_bank: List[Dict[str, str]],
    correct_map: Dict[str, Dict[str, str]],
    guidelines: Optional[List[str]] = None,
    cell_hints: Optional[Dict[str, str]] = None,
    cell_teaching_map: Optional[Dict[str, Dict[str, str]]] = None,
    derivation_map: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_vat_table_wordbank"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {"headers": headers, "rows": rows},
        "word_bank": word_bank,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "cell_hints": cell_hints or {},
        "cell_teaching_map": cell_teaching_map or {},
        "derivation_map": derivation_map or {},
        "expected_answer_type": "table_wordbank",
        "marks": len(rows) * 2,
        "visual_aid_key": "vat_classification",
    }


def _make_true_false(*, prompt: str, correct_answer: bool, explanation: str) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_vat_tf"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": ["True", "False"],
        "correct_index": 0 if correct_answer else 1,
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 1,
        "guidelines": [explanation],
        "visual_aid_key": "vat_overview",
    }


# ---------------------------------------------------------------------------
# Classification data
# ---------------------------------------------------------------------------

_ZERO_RATED = [
    "Brown bread", "Maize meal", "Dried beans", "Lentils", "Rice",
    "Cooking oil", "Milk", "Eggs", "Canned pilchards/sardines",
    "Fruit", "Vegetables", "Milk powder", "Sugar beans",
    "Fuel and oil", "Goods used for agriculture", "Fresh apples",
]

_EXEMPT = [
    "Educational services (school fees)", "Financial services (bank interest)",
    "Residential rental (housing)", "Transport of passengers by road or rail",
    "Trade union member contributions", "Passenger transported by taxi",
]

_TAXABLE = [
    "White bread", "Coca-Cola", "Corn flakes cereal", "Chips",
    "Lamb chops", "Cheese", "Charcoal", "Simba Chips",
    "Chocolate", "Sweets", "Clothing", "Electronics",
]


# ---------------------------------------------------------------------------
# Sub-skill generators
# ---------------------------------------------------------------------------

def _gen_concepts(r: random.Random) -> List[Dict[str, Any]]:
    """VAT concepts — definitions, purpose, registration."""
    pool: List[Dict[str, Any]] = []
    business = _pick_business_name(r=r)
    people = _pick_person_names(r=r, k=2)
    customer = people[0]

    pool.append(_make_mcq(
        prompt="What does VAT stand for?",
        options=["Value After Tax", "Value Added Tax", "Variable Annual Tax", "Vendor Assessment Tax"],
        correct_index=1,
        explanation="VAT stands for Value Added Tax — a tax collected at each point in the production and distribution chain.",
    ))

    pool.append(_make_mcq(
        prompt="VAT is a type of:",
        options=["Direct tax", "Indirect tax", "Capital gains tax", "Estate duty"],
        correct_index=1,
        explanation="VAT is an indirect tax — it is collected by the seller from the customer and paid to SARS.",
    ))

    pool.append(_make_mcq(
        prompt="What is the current standard rate of VAT in South Africa?",
        options=["14%", "10%", "15%", "20%"],
        correct_index=2,
        explanation="The current standard VAT rate in South Africa is 15%.",
    ))

    pool.append(_make_mcq(
        prompt="What is VAT output?",
        options=[
            "VAT paid when goods and services are purchased by the business.",
            "VAT collected from customers on sales.",
            "The total turnover of the business.",
            "A deduction from employees' salaries.",
        ],
        correct_index=1,
        explanation="Output VAT is the VAT charged on sales — collected from customers. Input VAT is VAT paid on purchases.",
    ))

    pool.append(_make_mcq(
        prompt="What is the basic formula for calculating VAT payable/refundable to SARS?",
        options=[
            "Output tax + Input tax = Amount payable.",
            "Output tax – Input tax = Amount payable/refundable.",
            "Sales – Purchases = VAT amount.",
            "Total expenses × 15% = VAT amount.",
        ],
        correct_index=1,
        explanation="Output tax – Input tax = Amount payable (if positive, pay SARS) or refundable (if negative, SARS refunds).",
    ))

    pool.append(_make_mcq(
        prompt="A business with annual turnover of R1,000,000 or more must:",
        options=[
            "Register voluntarily for VAT.",
            "Register compulsorily as a VAT vendor.",
            "Pay no VAT.",
            "Only charge VAT on exports.",
        ],
        correct_index=1,
        explanation="Businesses with turnover of R1,000,000 or more per year must register compulsorily as VAT vendors. Businesses with turnover above R50,000 may register voluntarily.",
    ))

    # Archetype Q1.4 / Registration threshold
    pool.append(_make_typed(
        prompt=(
            f"{customer} runs a small business giving extra maths lessons for cash. "
            f"The business makes about R150,000 per year. Explain why {customer} might NOT be registered as a VAT vendor."
        ),
        sample_answer="To be compulsorily registered as a VAT vendor, turnover must be more than R1,000,000 per year. Because the turnover is only R150,000, registration is not mandatory, although voluntary registration is possible since it is above R50,000.",
        grading_rubric=["turnover less than R1,000,000", "not compulsory / not mandatory to register"],
    ))

    pool.append(_make_mcq(
        prompt="A business with annual taxable supplies of R80,000 and proper records may:",
        options=[
            "Register voluntarily as a VAT vendor.",
            "Charge VAT immediately without registering.",
            "Register compulsorily because it is already above R1,000,000.",
            "Never register for VAT under any circumstances.",
        ],
        correct_index=0,
        explanation="A business with taxable supplies above R50,000 may apply for voluntary VAT registration if it meets the registration requirements.",
    ))

    pool.append(_make_typed(
        prompt="Explain why VAT is called an indirect tax and identify who finally bears the cost of VAT.",
        sample_answer="VAT is called an indirect tax because the vendor collects the tax from customers and pays it over to SARS instead of the consumer paying SARS directly. The final consumer bears the cost because VAT is included in the selling price of taxable goods and services.",
        grading_rubric=["vendor collects VAT", "vendor pays SARS", "consumer bears cost", "VAT included in selling price"],
    ))

    # True/False archetype Q3, Q5, Q8
    pool.append(_make_true_false(
        prompt="The supply of educational services is an example of a VAT exempt item.",
        correct_answer=True,
        explanation="Educational services are VAT exempt — no VAT is charged on school fees.",
    ))

    pool.append(_make_true_false(
        prompt="VAT is not charged on goods taken by the owner for personal use.",
        correct_answer=False,
        explanation="False — VAT must still be charged (output VAT) when the owner takes goods for personal use, because it is treated as a sale at market value.",
    ))

    pool.append(_make_true_false(
        prompt="Brown bread and milk are examples of zero-rated items.",
        correct_answer=True,
        explanation="Brown bread and milk are basic food items charged at 0% VAT (zero-rated).",
    ))

    pool.append(_make_true_false(
        prompt="VAT is charged on salaries and wages.",
        correct_answer=False,
        explanation="False — salaries and wages are not subject to VAT. VAT is charged on the supply of goods and services, not on employment remuneration.",
    ))

    pool.append(_make_true_false(
        prompt="Input VAT is VAT collected from customers.",
        correct_answer=False,
        explanation="False — Input VAT is VAT paid by the business when purchasing goods/services. Output VAT is VAT collected from customers.",
    ))

    pool.append(_make_true_false(
        prompt="Tax evasion is illegal and punishable by law.",
        correct_answer=True,
        explanation="Tax evasion is the use of illegal methods to avoid paying tax and is punishable by law.",
    ))

    pool.append(_make_mcq(
        prompt="VAT vendors normally submit VAT returns to SARS:",
        options=["Every week", "Every month", "Every two months", "Once a year"],
        correct_index=2,
        explanation="VAT returns are normally submitted every two months according to the VAT cycle.",
    ))

    pool.append(_make_mcq(
        prompt="On the invoice basis, VAT is recorded when:",
        options=["Cash is finally paid", "A tax invoice is issued or received", "The bank statement is printed", "Year-end adjustments are processed"],
        correct_index=1,
        explanation="On the invoice basis, VAT is recognised when the tax invoice is issued or received, not only when cash changes hands.",
    ))

    transaction_rows = [
        ["1", f"{business} buys trading stock on credit from a supplier with a tax invoice.", ""],
        ["2", f"{business} sells goods for cash to {customer} and issues a tax invoice.", ""],
        ["3", f"{business} pays staff salaries and wages at month-end.", ""],
        ["4", f"{business} pays residential rent for the owner's private flat.", ""],
    ]
    transaction_correct_map = {
        "0": {"2": "input"},
        "1": {"2": "output"},
        "2": {"2": "none"},
        "3": {"2": "none"},
    }
    flow_support = _build_flow_table_support(
        transaction_rows,
        transaction_correct_map,
        {
            "input": {
                "label": "Input VAT",
                "where_to_look": "The business is buying taxable goods/services from a supplier and receives a tax invoice.",
                "method_or_formula": "Purchases by the business create input VAT if VAT is charged by the supplier.",
                "record_link": "Input VAT is VAT paid on purchases and may be claimed if the purchase qualifies.",
                "derivation": "This is a purchase transaction, so VAT paid goes to input VAT.",
            },
            "output": {
                "label": "Output VAT",
                "where_to_look": "The business is selling taxable goods/services to a customer.",
                "method_or_formula": "Sales by the business create output VAT when VAT is charged to the customer.",
                "record_link": "Output VAT is VAT collected from customers on taxable sales.",
                "derivation": "This is a sales transaction, so VAT charged belongs to output VAT.",
            },
            "none": {
                "label": "No VAT claim / charge",
                "where_to_look": "The transaction is not a normal taxable purchase/sale for VAT purposes.",
                "method_or_formula": "Non-VAT items like salaries do not create input or output VAT.",
                "record_link": "If no taxable supply is involved, there is no VAT to claim or charge.",
                "derivation": "This transaction does not create input VAT or output VAT.",
            },
        },
    )
    pool.append(_with_validation(_make_table_wordbank(
        prompt="Classify each transaction as Input VAT, Output VAT, or No VAT claim / charge.",
        headers=["No.", "Transaction", "VAT treatment"],
        rows=transaction_rows,
        word_bank=[
            {"id": "input", "label": "Input VAT"},
            {"id": "output", "label": "Output VAT"},
            {"id": "none", "label": "No VAT claim / charge"},
        ],
        correct_map=transaction_correct_map,
        guidelines=["Decide whether the business is buying, selling, or dealing with a non-VAT item such as salaries."],
        cell_hints=flow_support["cell_hints"],
        cell_teaching_map=flow_support["cell_teaching_map"],
        derivation_map=flow_support["derivation_map"],
    ), "concepts_vat_flow_classification", expected_rows=len(transaction_rows), expected_tokens=3))

    return _validate_pool(pool, family="concepts")


def _gen_calculations(r: random.Random) -> List[Dict[str, Any]]:
    """VAT calculations — inclusive/exclusive/rate, archetype Q3.2, Q5.2, Q6."""
    pool: List[Dict[str, Any]] = []
    business = _pick_business_name(r=r)
    supplier, customer = _pick_person_names(r=r, k=2)

    # Archetype Q3.2 pattern: calculate missing amounts in a table
    # Type 1: Given inclusive, find exclusive and VAT
    incl = r.choice([1150, 2300, 2415, 4140, 5750, 9200])
    excl = _round_money(incl / (1 + VAT_RATE))
    vat_amt = _round_money(incl - excl)
    exclusive_support = _build_calc_support(
        formula_hint="Use Exclusive = Inclusive ÷ 1.15 when the amount given already includes VAT.",
        relevant_values=[f"Inclusive amount given: R{incl:,.2f}", "VAT rate: 15%", "You must remove VAT to get the exclusive amount."],
        method="Divide the inclusive amount by 1.15 because the amount already includes the 15% VAT layer.",
        derivation_steps=[f"Start with the inclusive amount R{incl:,.2f}.", f"Divide by 1.15 to remove VAT: R{incl:,.2f} ÷ 1.15.", f"VAT-exclusive amount = R{excl:,.2f}."],
    )
    pool.append(_make_calc(
        prompt=f"An invoice total including VAT is R{incl:,.2f}. Calculate the VAT-exclusive amount.",
        correct_answer=excl,
        working_formula=f"Exclusive = Inclusive ÷ (1 + 15%) = R{incl:,.2f} ÷ 1.15",
        formula_hint=exclusive_support["formula_hint"],
        guidelines=exclusive_support["guidelines"],
        answer_part_hints=exclusive_support["answer_part_hints"],
        derivation_map=exclusive_support["derivation_map"],
    ))
    vat_from_inclusive_support = _build_calc_support(
        formula_hint="Use VAT = Inclusive × 15/115 when the amount given already includes VAT.",
        relevant_values=[f"Inclusive amount given: R{incl:,.2f}", "VAT rate: 15%", "You must extract only the VAT part from the inclusive amount."],
        method="Multiply the inclusive amount by 15/115 to isolate the VAT portion only.",
        derivation_steps=[f"Start with the inclusive amount R{incl:,.2f}.", f"Apply the extraction fraction 15/115: R{incl:,.2f} × 15/115.", f"VAT amount = R{vat_amt:,.2f}."],
    )
    pool.append(_make_calc(
        prompt=f"An invoice total including VAT is R{incl:,.2f}. Calculate the VAT amount.",
        correct_answer=vat_amt,
        working_formula=f"VAT = Inclusive × 15/115 = R{incl:,.2f} × 15/115",
        formula_hint=vat_from_inclusive_support["formula_hint"],
        guidelines=vat_from_inclusive_support["guidelines"],
        answer_part_hints=vat_from_inclusive_support["answer_part_hints"],
        derivation_map=vat_from_inclusive_support["derivation_map"],
    ))

    # Type 2: Given exclusive, find VAT and inclusive
    excl2 = r.choice([840, 1196, 3000, 5000, 9500, 42000])
    vat2 = _round_money(excl2 * VAT_RATE)
    incl2 = _round_money(excl2 + vat2)
    vat_on_exclusive_support = _build_calc_support(
        formula_hint="Use VAT = Exclusive × 15% when the amount given excludes VAT.",
        relevant_values=[f"Exclusive amount given: R{excl2:,.2f}", "VAT rate: 15%", "You are calculating only the VAT charge on top of the selling price."],
        method="Multiply the VAT-exclusive amount by 15% to calculate the VAT amount.",
        derivation_steps=[f"Start with the exclusive amount R{excl2:,.2f}.", f"Multiply by 15%: R{excl2:,.2f} × 15%.", f"VAT amount = R{vat2:,.2f}."],
    )
    pool.append(_make_calc(
        prompt=f"An invoice total excluding VAT is R{excl2:,.2f}. Calculate the VAT amount at 15%.",
        correct_answer=vat2,
        working_formula=f"VAT = R{excl2:,.2f} × 15%",
        formula_hint=vat_on_exclusive_support["formula_hint"],
        guidelines=vat_on_exclusive_support["guidelines"],
        answer_part_hints=vat_on_exclusive_support["answer_part_hints"],
        derivation_map=vat_on_exclusive_support["derivation_map"],
    ))
    inclusive_support = _build_calc_support(
        formula_hint="Use Inclusive = Exclusive × 1.15 or Exclusive + VAT when the price excludes VAT.",
        relevant_values=[f"Exclusive amount given: R{excl2:,.2f}", "VAT rate: 15%", "You must add VAT to the exclusive amount to get the inclusive total."],
        method="First calculate VAT at 15%, then add it to the exclusive amount, or multiply the exclusive amount by 1.15.",
        derivation_steps=[f"Start with the exclusive amount R{excl2:,.2f}.", f"Calculate VAT: R{excl2:,.2f} × 15% = R{vat2:,.2f}.", f"Add VAT to the exclusive amount: R{excl2:,.2f} + R{vat2:,.2f} = R{incl2:,.2f}."],
    )
    pool.append(_make_calc(
        prompt=f"An invoice total excluding VAT is R{excl2:,.2f}. Calculate the total including VAT.",
        correct_answer=incl2,
        working_formula=f"Inclusive = R{excl2:,.2f} + (R{excl2:,.2f} × 15%) = R{excl2:,.2f} × 1.15",
        formula_hint=inclusive_support["formula_hint"],
        guidelines=inclusive_support["guidelines"],
        answer_part_hints=inclusive_support["answer_part_hints"],
        derivation_map=inclusive_support["derivation_map"],
    ))

    # Type 3: Given VAT amount, find exclusive and inclusive
    vat3 = r.choice([126, 315, 540, 1425, 6300])
    excl3 = _round_money(vat3 / VAT_RATE)
    incl3 = _round_money(excl3 + vat3)
    exclusive_from_vat_support = _build_calc_support(
        formula_hint="Use Exclusive = VAT ÷ 15% when only the VAT amount is given.",
        relevant_values=[f"VAT amount given: R{vat3:,.2f}", "VAT rate: 15%", "You must work backwards from the VAT amount to the exclusive amount."],
        method="Divide the VAT amount by 15% to find the VAT-exclusive amount that produced it.",
        derivation_steps=[f"Start with the VAT amount R{vat3:,.2f}.", f"Divide by 0.15 to reverse the VAT calculation: R{vat3:,.2f} ÷ 0.15.", f"VAT-exclusive amount = R{excl3:,.2f}."],
    )
    pool.append(_make_calc(
        prompt=f"The VAT amount on an invoice is R{vat3:,.2f} (at 15%). Calculate the VAT-exclusive amount.",
        correct_answer=excl3,
        working_formula=f"Exclusive = VAT ÷ 15% = R{vat3:,.2f} ÷ 0.15",
        formula_hint=exclusive_from_vat_support["formula_hint"],
        guidelines=exclusive_from_vat_support["guidelines"],
        answer_part_hints=exclusive_from_vat_support["answer_part_hints"],
        derivation_map=exclusive_from_vat_support["derivation_map"],
    ))

    # Archetype Q5.2: Retailer mark-up + VAT chain
    cp = r.choice([1196, 2000, 3000, 5000])
    input_vat = _round_money(cp * VAT_RATE)
    total_paid = _round_money(cp + input_vat)
    mu_pct = r.choice([10, 20, 25, 50])
    sp = _round_money(cp * (1 + mu_pct / 100))
    output_vat = _round_money(sp * VAT_RATE)
    customer_pays = _round_money(sp + output_vat)
    markup_support = _build_calc_support(
        formula_hint="For mark-up on cost, use Selling price = Cost price × (1 + mark-up%).",
        relevant_values=[f"Cost price excl. VAT: R{cp:,.2f}", f"Mark-up rate: {mu_pct}%", "The question asks for the selling price before VAT is added."],
        method="Calculate the mark-up on cost, then add it to the cost price to get the selling price excluding VAT.",
        derivation_steps=[f"Start with the cost price R{cp:,.2f}.", f"Apply the mark-up: R{cp:,.2f} × (1 + {mu_pct}%).", f"Selling price excl. VAT = R{sp:,.2f}."],
    )

    pool.append(_make_calc(
        prompt=(
            f"A retailer buys goods at R{cp:,.2f} (excl. VAT). Mark-up is {mu_pct}% on cost.\n"
            f"Calculate the selling price (excl. VAT)."
        ),
        correct_answer=sp,
        working_formula=f"SP = CP × (1 + {mu_pct}%) = R{cp:,.2f} × {1 + mu_pct/100}",
        formula_hint=markup_support["formula_hint"],
        guidelines=markup_support["guidelines"],
        answer_part_hints=markup_support["answer_part_hints"],
        derivation_map=markup_support["derivation_map"],
    ))
    inclusive_customer_support = _build_calc_support(
        formula_hint="Customer pays = Selling price excl. VAT + Output VAT, where Output VAT = Selling price excl. VAT × 15%.",
        relevant_values=[f"Selling price excl. VAT: R{sp:,.2f}", "VAT rate: 15%", "The customer pays the price plus VAT."],
        method="Calculate output VAT at 15% on the selling price, then add it to the selling price.",
        derivation_steps=[f"Start with the selling price excl. VAT R{sp:,.2f}.", f"Output VAT = R{sp:,.2f} × 15% = R{output_vat:,.2f}.", f"Customer pays = R{sp:,.2f} + R{output_vat:,.2f} = R{customer_pays:,.2f}."],
    )
    pool.append(_make_calc(
        prompt=(
            f"A retailer sells goods at R{sp:,.2f} (excl. VAT). VAT at 15%.\n"
            f"Calculate the total the customer pays (incl. VAT)."
        ),
        correct_answer=customer_pays,
        working_formula=f"Total = SP + Output VAT = R{sp:,.2f} + (R{sp:,.2f} × 15%)",
        formula_hint=inclusive_customer_support["formula_hint"],
        guidelines=inclusive_customer_support["guidelines"],
        answer_part_hints=inclusive_customer_support["answer_part_hints"],
        derivation_map=inclusive_customer_support["derivation_map"],
    ))
    payable_support = _build_calc_support(
        formula_hint="VAT payable = Output VAT - Input VAT.",
        relevant_values=[f"Output VAT: R{output_vat:,.2f}", f"Input VAT: R{input_vat:,.2f}", "Use only the VAT portions, not the full inclusive totals."],
        method="Subtract input VAT from output VAT. If output VAT is larger, the business pays SARS.",
        derivation_steps=[f"Identify output VAT = R{output_vat:,.2f}.", f"Identify input VAT = R{input_vat:,.2f}.", f"VAT payable = R{output_vat:,.2f} - R{input_vat:,.2f} = R{_round_money(output_vat - input_vat):,.2f}."],
    )
    pool.append(_make_calc(
        prompt=(
            f"The retailer paid R{total_paid:,.2f} (incl. VAT) to the supplier and receives R{customer_pays:,.2f} (incl. VAT) from the customer.\n"
            f"Calculate the VAT payable to SARS (Output VAT – Input VAT)."
        ),
        correct_answer=_round_money(output_vat - input_vat),
        working_formula=f"VAT payable = Output VAT (R{output_vat:,.2f}) - Input VAT (R{input_vat:,.2f})",
        formula_hint=payable_support["formula_hint"],
        guidelines=payable_support["guidelines"],
        answer_part_hints=[_vat_output_hint(), _vat_input_hint(), _vat_payable_hint(), *payable_support["answer_part_hints"]],
        derivation_map=payable_support["derivation_map"],
    ))

    output_vat_named = r.choice([1800, 2450, 3200, 4100])
    input_vat_named = r.choice([2200, 2800, 3600, 4550])
    refundable = _round_money(input_vat_named - output_vat_named)
    refund_support = _build_calc_support(
        formula_hint="VAT refundable occurs when Input VAT is greater than Output VAT.",
        relevant_values=[f"Output VAT for {business}: R{output_vat_named:,.2f}", f"Input VAT for {business}: R{input_vat_named:,.2f}", "Because input VAT is bigger, SARS owes the business the difference."],
        method="Subtract output VAT from input VAT to determine the refund when input VAT exceeds output VAT.",
        derivation_steps=[f"Identify output VAT = R{output_vat_named:,.2f}.", f"Identify input VAT = R{input_vat_named:,.2f}.", f"VAT refundable = R{input_vat_named:,.2f} - R{output_vat_named:,.2f} = R{refundable:,.2f}."],
    )
    pool.append(_with_validation(_make_calc(
        prompt=(
            f"During a two-month VAT period, {business} charged output VAT of R{output_vat_named:,.2f} on sales to customers such as {customer}. "
            f"The business also paid input VAT of R{input_vat_named:,.2f} on purchases from suppliers such as {supplier}.\n"
            f"Calculate the VAT refundable by SARS."
        ),
        correct_answer=refundable,
        working_formula=f"VAT refundable = Input VAT (R{input_vat_named:,.2f}) - Output VAT (R{output_vat_named:,.2f})",
        formula_hint=refund_support["formula_hint"],
        guidelines=refund_support["guidelines"],
        answer_part_hints=[_vat_input_hint(), _vat_output_hint(), *refund_support["answer_part_hints"]],
        derivation_map=refund_support["derivation_map"],
    ), "calculations_vat_refund_named", output_vat=output_vat_named, input_vat=input_vat_named, expected_refund=refundable))

    # Activity 2 Archetype: Mixed shopping cart
    cart_zero = r.sample(_ZERO_RATED, k=r.randint(1, 3))
    cart_taxable = r.sample(_TAXABLE, k=r.randint(2, 4))
    cart_items = []
    total_taxable_excl = 0
    for z in cart_zero:
        price = r.choice([12, 14, 18, 22, 25])
        cart_items.append((z, price))
    for t in cart_taxable:
        price = r.choice([15, 20, 24, 30, 45, 101])
        cart_items.append((t, price))
        total_taxable_excl += price

    r.shuffle(cart_items)
    cart_str = ", ".join([f"{item} R{pr}" for item, pr in cart_items])
    vat_on_cart = _round_money(total_taxable_excl * VAT_RATE)
    
    mixed_cart_support = _build_calc_support(
        formula_hint="Only calculate VAT on the taxable items. Do not include zero-rated items in your total.",
        relevant_values=[f"Taxable items: {', '.join(cart_taxable)}", f"Zero-rated items: {', '.join(cart_zero)}", "VAT rate: 15%"],
        method="Add up the prices of only the taxable items, then multiply the total by 15%.",
        derivation_steps=[
            f"Identify taxable items: {', '.join(cart_taxable)}.",
            f"Sum of taxable items = R{total_taxable_excl:,.2f}.",
            f"Calculate 15% on taxable sum: R{total_taxable_excl:,.2f} × 15%.",
            f"Total VAT = R{vat_on_cart:,.2f}."
        ],
    )
    pool.append(_make_calc(
        prompt=(
            f"A customer's trolley has the following items (All prices exclude VAT):\n"
            f"{cart_str}.\n"
            f"Calculate the total VAT that will be charged on these items."
        ),
        correct_answer=vat_on_cart,
        working_formula=f"VAT = R{total_taxable_excl:,.2f} (taxable sum) × 15%",
        formula_hint=mixed_cart_support["formula_hint"],
        guidelines=["Do not calculate VAT on zero-rated items like " + ", ".join(cart_zero)],
        answer_part_hints=mixed_cart_support["answer_part_hints"],
        derivation_map=mixed_cart_support["derivation_map"],
    ))

    return _validate_pool(pool, family="calculations")


def _gen_classification(r: random.Random) -> List[Dict[str, Any]]:
    """Zero-rated vs exempt vs taxable classification — archetype Q1.2."""
    pool: List[Dict[str, Any]] = []

    # Build classification table question
    zero_sample = r.sample(_ZERO_RATED, k=2)
    exempt_sample = r.sample(_EXEMPT, k=1)
    taxable_sample = r.sample(_TAXABLE, k=3)

    all_items = zero_sample + exempt_sample + taxable_sample
    r.shuffle(all_items)

    categories = {"Taxable": "tax", "Exempt": "exempt", "Zero-rated": "zero"}

    def _classify(item: str) -> str:
        if item in _ZERO_RATED:
            return "zero"
        if item in _EXEMPT:
            return "exempt"
        return "tax"

    word_bank_items = [
        {"id": "tax", "label": "Taxable (15%)"},
        {"id": "exempt", "label": "Exempt"},
        {"id": "zero", "label": "Zero-rated (0%)"},
    ]

    rows = []
    correct_map = {}
    for i, item in enumerate(all_items):
        rows.append([str(i + 1), item, ""])
        correct_map[str(i)] = {"2": _classify(item)}

    classification_support = _build_classification_support(rows, correct_map)

    pool.append(_with_validation(_make_table_wordbank(
        prompt="Classify each item as Taxable (15%), Exempt, or Zero-rated (0%).",
        headers=["No.", "Item", "Classification"],
        rows=rows,
        word_bank=word_bank_items,
        correct_map=correct_map,
        guidelines=["Select the correct VAT classification for each item."],
        cell_hints=classification_support["cell_hints"],
        cell_teaching_map=classification_support["cell_teaching_map"],
        derivation_map=classification_support["derivation_map"],
    ), "classification_vat_categories", expected_rows=len(rows), expected_tokens=3))

    # Additional MCQs on classification
    pool.append(_make_mcq(
        prompt="Why are some items zero-rated for VAT?",
        options=[
            "Because the government does not want to collect VAT on expensive items.",
            "To avoid undue hardship for poor people — basic food items are charged at 0% VAT.",
            "Because they are imported goods.",
            "Because traders don't want to add VAT to these items.",
        ],
        correct_index=1,
        explanation="Basic food items are zero-rated to protect low-income households from paying VAT on essential goods.",
    ))

    pool.append(_make_mcq(
        prompt="A business that provides VAT-exempt deliveries (e.g. educational services):",
        options=[
            "Can claim all its input VAT as a deduction.",
            "May NOT claim its input VAT as a deduction.",
            "Does not need to register with SARS.",
            "Must charge 15% VAT on all services.",
        ],
        correct_index=1,
        explanation="Businesses providing exempt deliveries may NOT claim input VAT as a deduction. Businesses with zero-rated deliveries CAN claim input VAT.",
    ))

    pool.append(_make_mcq(
        prompt="Which statement correctly compares zero-rated and exempt supplies?",
        options=[
            "Both are charged at 15% VAT and both allow full input VAT claims.",
            "Zero-rated supplies are taxed at 0% and may still allow related input VAT claims, while exempt supplies do not charge VAT and usually do not allow related input VAT claims.",
            "Exempt supplies are the same as zero-rated supplies, so the terms can be used interchangeably.",
            "Only exempt supplies appear on VAT returns, while zero-rated supplies do not.",
        ],
        correct_index=1,
        explanation="Zero-rated supplies are taxable at 0%, so related input VAT may still be claimed. Exempt supplies do not have VAT charged and related input VAT is generally not claimable.",
    ))

    # Typed: list zero-rated items
    pool.append(_make_typed(
        prompt="Name any FOUR zero-rated items in South Africa.",
        sample_answer="Brown bread, maize meal, dried beans, milk, eggs, cooking oil, rice, canned pilchards, fruit, vegetables.",
        grading_rubric=["brown bread / maize meal", "milk / eggs", "dried beans / lentils / rice", "fruit / vegetables / cooking oil"],
    ))

    pool.append(_make_typed(
        prompt="Explain one important difference between zero-rated supplies and exempt supplies for a VAT vendor.",
        sample_answer="Both zero-rated and exempt supplies do not add 15% VAT to the customer's price, but zero-rated supplies are still taxable at 0% and the vendor may usually claim related input VAT. Exempt supplies do not allow the vendor to claim related input VAT.",
        grading_rubric=["no 15% added to customer price", "zero-rated taxed at 0%", "input VAT may be claimed on zero-rated supplies", "input VAT may not be claimed on exempt supplies"],
    ))

    return _validate_pool(pool, family="classification")


def _gen_ethics(r: random.Random) -> List[Dict[str, Any]]:
    """VAT ethics — tax evasion vs avoidance, unregistered vendors, penalties."""
    pool: List[Dict[str, Any]] = []
    people = _pick_person_names(r=r, k=3)
    trader = people[0]
    customer = people[1]
    business = _pick_business_name(r=r)

    pool.append(_make_typed(
        prompt="What is the difference between tax evasion and tax avoidance?",
        sample_answer="Tax evasion is the use of illegal methods to reduce or avoid paying tax (a criminal offence). Tax avoidance is the use of legal methods to arrange one's affairs to reduce the amount of tax payable.",
        grading_rubric=["evasion = illegal", "avoidance = legal", "evasion is punishable"],
    ))

    # Archetype Q2 scenario
    pool.append(_make_typed(
        prompt=(
            f"{trader} runs a small retail business called {business} with monthly turnover of R15,000–R20,000. "
            f"{trader} is NOT a registered VAT vendor but still charges customers VAT.\n\n"
            f"Do you think {trader}'s actions are legal? Comment on your answer."
        ),
        sample_answer=f"No, it is not legal. {trader} is not registered as a VAT vendor, so {trader} may not charge VAT. To register compulsorily, turnover must exceed R1,000,000. Charging VAT without registration is fraudulent — {trader} is collecting money that is not being paid over to SARS.",
        grading_rubric=["not legal / unethical", "not registered as vendor", "must not charge VAT if not registered", "fraudulent / keeping money"],
    ))

    # Archetype Q9.7: ethical scenario
    pool.append(_make_typed(
        prompt=(
            f"{customer} wishes to buy 5 boxes of chips from {business} at R180 per box (VAT exclusive). The owner offers "
            f"a special cash price of R950 for all 5 boxes (including VAT) instead of R1,035, on condition {customer.split()[0]} "
            f"pays cash and does not require a document.\n\n"
            f"Should {customer} accept this offer? Give TWO reasons."
        ),
        sample_answer=f"No, {customer} should not accept. (1) The owner is trying to avoid issuing a tax invoice, which means no record for SARS — this is tax evasion. (2) Without a document, {customer} has no proof of purchase if there is a dispute or if the goods are faulty.",
        grading_rubric=["no / should not accept", "tax evasion / avoiding SARS record", "no proof of purchase / no protection"],
    ))

    pool.append(_make_typed(
        prompt=(
            f"{business} advertises brown bread and milk as 'VAT included at 15%'. "
            f"Explain why charging 15% VAT on these zero-rated items would be unethical and illegal."
        ),
        sample_answer="It is illegal and unethical because brown bread and milk are zero-rated items. The law sets them at 0% VAT to protect consumers, so the vendor may not add 15% VAT and keep extra money from customers.",
        grading_rubric=["zero-rated items", "must not charge 15% VAT", "illegal / unethical", "harms consumers / extra money"],
    ))

    # SARS penalties
    pool.append(_make_mcq(
        prompt="What action can SARS take against a VAT vendor who conducts themselves unethically (e.g. not paying over VAT)?",
        options=[
            "SARS can only send a warning letter.",
            "SARS can impose penalties, cancel registration, and the vendor may face imprisonment.",
            "SARS has no power over individual vendors.",
            "The vendor simply pays the outstanding amount with no consequences.",
        ],
        correct_index=1,
        explanation="SARS can impose penalties for non-compliance, cancel the vendor's registration if proper records are not kept, and the vendor may face criminal charges (jail).",
    ))

    # Q4.4 pattern: charging VAT on zero-rated items
    pool.append(_make_mcq(
        prompt="Is it ethical for a registered vendor to charge VAT on zero-rated items?",
        options=[
            "Yes — the vendor can charge VAT on any items they sell.",
            "No — the law does not allow VAT to be charged on zero-rated items. It is unethical and fraudulent.",
            "Only if the customer agrees to pay VAT.",
            "Only during tax season.",
        ],
        correct_index=1,
        explanation="It is illegal and unethical to charge VAT on zero-rated items. The law specifically sets these items at 0% VAT to protect consumers.",
    ))

    # Q7 fill-in archetype (as MCQ)
    pool.append(_make_mcq(
        prompt="Complete: 'VAT is a/an _____ system of taxation.'",
        options=["direct", "indirect", "progressive", "regressive"],
        correct_index=1,
        explanation="VAT is an indirect tax — it is not paid directly to the government by the person who bears the economic burden (the consumer). It is collected by the vendor.",
    ))

    pool.append(_make_typed(
        prompt=(
            f"{business} records some cash sales in the till but deliberately does not issue tax invoices for them so that less output VAT appears on the VAT return. "
            f"Explain why this is unethical and give TWO possible consequences."
        ),
        sample_answer=f"It is unethical because {business} is hiding taxable sales and understating output VAT that should be paid to SARS. This is tax evasion. Possible consequences include penalties or interest from SARS, cancellation of VAT registration, criminal charges, and customers not having proper proof of purchase.",
        grading_rubric=["hiding sales / understating output VAT", "tax evasion / illegal", "SARS penalties / interest / deregistration / criminal charges", "no proof of purchase for customers"],
    ))

    # Mr Khumalo scenario (Activity 1)
    pool.append(_make_typed(
        prompt=(
            f"Mr {trader.split()[-1]} makes a lot of money charging fees for extra lessons. He accepts only cash and does not issue receipts. "
            f"He brags that he does not pay taxes and SARS cannot catch him for tax evasion. He charges VAT on his fees, but he is not a registered vendor.\n\n"
            f"Explain why his actions are unethical and illegal."
        ),
        sample_answer=f"Mr {trader.split()[-1]} is committing tax evasion by deliberately hiding his cash income from SARS. Furthermore, it is fraudulent and illegal to charge VAT if he is not a registered VAT vendor, as he is collecting tax money from people that he is not paying over to SARS.",
        grading_rubric=["tax evasion / hiding cash income", "fraudulent to charge VAT if unregistered", "collecting money not paid to SARS", "illegal"],
    ))

    # Evasion vs Avoidance Table wordbank
    evasion_vs_avoidance_rows = [
        ["1", f"{business} deliberately fails to record cash sales to reduce its VAT payable to SARS.", ""],
        ["2", f"{trader} invests money in a legal tax-free savings account to reduce income tax.", ""],
        ["3", f"A company claims input VAT on personal expenses of the owner by submitting false invoices.", ""],
        ["4", f"A vendor claims maximum legal input VAT deductions by keeping careful records of all business purchases.", ""],
    ]
    ev_av_correct_map = {
        "0": {"2": "evasion"},
        "1": {"2": "avoidance"},
        "2": {"2": "evasion"},
        "3": {"2": "avoidance"},
    }
    ev_av_support = _build_flow_table_support(
        evasion_vs_avoidance_rows,
        ev_av_correct_map,
        {
            "evasion": {
                "label": "Tax Evasion",
                "where_to_look": "Look for illegal actions, hiding income, or submitting false documents.",
                "method_or_formula": "If the action breaks the law to reduce tax, it is evasion.",
                "record_link": "Tax evasion is a criminal offense.",
                "derivation": "This action involves deceit or breaking the law to reduce tax, so it is tax evasion.",
            },
            "avoidance": {
                "label": "Tax Avoidance",
                "where_to_look": "Look for legal actions, using tax laws to the taxpayer's advantage.",
                "method_or_formula": "If the action uses legal loopholes or allowed deductions, it is avoidance.",
                "record_link": "Tax avoidance is legal.",
                "derivation": "This action uses legal methods to arrange tax affairs, so it is tax avoidance.",
            },
        },
    )
    pool.append(_with_validation(_make_table_wordbank(
        prompt="Classify each scenario as Tax Evasion or Tax Avoidance.",
        headers=["No.", "Scenario", "Classification"],
        rows=evasion_vs_avoidance_rows,
        word_bank=[
            {"id": "evasion", "label": "Tax Evasion (Illegal)"},
            {"id": "avoidance", "label": "Tax Avoidance (Legal)"},
        ],
        correct_map=ev_av_correct_map,
        guidelines=["Identify if the action uses legal methods (avoidance) or illegal methods (evasion)."],
        cell_hints=ev_av_support["cell_hints"],
        cell_teaching_map=ev_av_support["cell_teaching_map"],
        derivation_map=ev_av_support["derivation_map"],
    ), "ethics_evasion_vs_avoidance", expected_rows=len(evasion_vs_avoidance_rows), expected_tokens=2))

    return _validate_pool(pool, family="ethics")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = max(1, min(int(count), 20))
    subskill_norm = _normalize_subskill(subskill)

    concepts_pool = _assign_recommended_difficulties(_gen_concepts(r), family="concepts")
    calc_pool = _assign_recommended_difficulties(_gen_calculations(r), family="calculations")
    classification_pool = _assign_recommended_difficulties(_gen_classification(r), family="classification")
    ethics_pool = _assign_recommended_difficulties(_gen_ethics(r), family="ethics")

    all_pools = {
        "concepts": concepts_pool,
        "calculations": calc_pool,
        "classification": classification_pool,
        "ethics": ethics_pool,
        "mixed": concepts_pool + calc_pool + classification_pool + ethics_pool,
    }

    pools_by_subskill = {
        "concepts": concepts_pool,
        "calculations": calc_pool,
        "classification": classification_pool,
        "ethics": ethics_pool,
    }

    validated_pools = {
        name: _validate_pool(pool, family=name)
        for name, pool in pools_by_subskill.items()
    }

    if subskill_norm == "mixed":
        selected_questions = _select_mixed_questions_balanced(validated_pools, n=n, difficulty=difficulty, r=r)
    else:
        pool = validated_pools.get(subskill_norm)
        if not pool:
            selected_questions = _select_mixed_questions_balanced(validated_pools, n=n, difficulty=difficulty, r=r)
        else:
            filtered_pool = _pool_for_difficulty(pool, difficulty)
            selected_questions = _select_questions(filtered_pool, n=n, r=r)

    out: List[Dict[str, Any]] = []
    for q in selected_questions:
        q_copy = _validate_question(q)
        q_copy["difficulty"] = difficulty
        q_copy["subskill"] = subskill_norm
        out.append(q_copy)

    return out
