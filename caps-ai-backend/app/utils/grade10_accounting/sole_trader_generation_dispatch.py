from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from ..sole_trader.names import pick_business_names
from ..sole_trader.trial_balance_structured import make_trial_balance_control_balance_question
from ..sole_trader.trial_balance_structured import make_trial_balance_from_balances_question
from ..sole_trader.trial_balance_structured import make_trial_balance_partial_completion_question
from .sole_trader_journal_orchestration import build_journal_questions_for_subskill


QuestionBuilder = Callable[..., Dict[str, Any]]


def select_questions_from_pool(
    *,
    items: List[Dict[str, Any]],
    qtype_norm: str,
    total_count: int,
    r: random.Random,
) -> List[Dict[str, Any]]:
    if qtype_norm not in ("", "mixed"):
        filtered_items = [q for q in items if q.get("question_type") == qtype_norm]
        if filtered_items:
            items = filtered_items

    if total_count <= 0 or not items:
        return []

    shuffled_items = list(items)
    r.shuffle(shuffled_items)

    if total_count <= len(shuffled_items):
        return shuffled_items[:total_count]

    out: List[Dict[str, Any]] = shuffled_items[:]
    while len(out) < total_count:
        replenished_items = list(items)
        r.shuffle(replenished_items)
        needed = total_count - len(out)
        out.extend(replenished_items[:needed])
    return out


def apply_generation_postprocessing(out_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    for q in out_list:
        if "correct_map" in q and isinstance(q["correct_map"], dict):
            existing_derivation_map = q.get("derivation_map") if isinstance(q.get("derivation_map"), dict) else {}
            for k, v in q["correct_map"].items():
                if str(v).strip() and k not in existing_derivation_map:
                    existing_derivation_map[k] = f"Calculation logic for expected value: {v}"
            q["derivation_map"] = existing_derivation_map
        if "correct_value" in q:
            if "derivation_map" not in q:
                q["derivation_map"] = {}
            q["derivation_map"]["value"] = f"Calculation logic for expected value: {q['correct_value']}"
    return out_list


def build_direct_dispatched_subskill_questions(
    *,
    subskill_norm: str,
    total_count: int,
    var_norm: str,
    r: random.Random,
    difficulty: str,
    mode_norm: str,
    builders: Dict[str, QuestionBuilder],
) -> Optional[List[Dict[str, Any]]]:
    def _build_single_to_multi_plan(total_count: int) -> List[str]:
        if total_count <= 0:
            return []
        if total_count == 1:
            if r.random() < 0.2:
                return ["single"]
            return [r.choice(["activity", "exam"])]

        single_count = int((total_count + 2) / 5)
        if single_count >= total_count:
            single_count = max(0, total_count - 1)
        multiple_count = total_count - single_count

        start_offset = r.randrange(2)
        multiple_labels = [
            "activity" if ((start_offset + idx) % 2 == 0) else "exam"
            for idx in range(multiple_count)
        ]
        plan = (["single"] * single_count) + multiple_labels
        r.shuffle(plan)
        return plan

    def _build_trial_balance_plan(total_count: int) -> List[str]:
        if total_count <= 0:
            return []
        family_labels = ["from_balances", "partial_completion", "control_balance"]
        if var_norm in set(family_labels):
            return [var_norm for _ in range(total_count)]

        plan: List[str] = []
        while len(plan) < total_count:
            chunk = family_labels[:]
            r.shuffle(chunk)
            plan.extend(chunk)
        return plan[:total_count]

    def _build_trading_stock_plan(total_count: int) -> List[str]:
        if total_count <= 0:
            return []

        difficulty_norm = str(difficulty or "easy").strip().lower()
        family_specs: List[Dict[str, str]] = [
            {"label": "prepare_from_journals", "question_type": "journal"},
            {"label": "fill_missing_details", "question_type": "journal"},
        ]
        if difficulty_norm in {"medium", "hard"}:
            family_specs.extend([
                {"label": "prepare_from_casted_journals", "question_type": "journal"},
                {"label": "prepare_with_returns_percent", "question_type": "journal"},
                {"label": "prepare_with_discount_calc", "question_type": "calc"},
                {"label": "section3_analysis_typed", "question_type": "typed"},
            ])
        if difficulty_norm == "hard":
            family_specs.extend([
                {"label": "prepare_with_two_returns_percent", "question_type": "journal"},
                {"label": "markup_trade_discount_typed", "question_type": "typed"},
                {"label": "activity16_analysis_typed", "question_type": "typed"},
            ])

        if var_norm in {"journal", "calc", "typed", "mcq", "match"}:
            family_specs = [spec for spec in family_specs if spec["question_type"] == var_norm]

        family_labels = [spec["label"] for spec in family_specs]
        if not family_labels:
            return []

        plan: List[str] = []
        while len(plan) < total_count:
            chunk = family_labels[:]
            r.shuffle(chunk)
            plan.extend(chunk)
        return plan[:total_count]

    def _build_control_accounts_plan(total_count: int) -> List[str]:
        if total_count <= 0:
            return []

        difficulty_norm = str(difficulty or "easy").strip().lower()
        family_specs: List[Dict[str, str]] = [
            {"label": "study_debtors", "question_type": "journal"},
            {"label": "study_creditors", "question_type": "journal"},
        ]
        if difficulty_norm == "easy":
            family_specs.extend([
                {"label": "opening_balance_calc_debtors", "question_type": "calc"},
                {"label": "opening_balance_calc_creditors", "question_type": "calc"},
            ])
        if difficulty_norm in {"medium", "hard"}:
            family_specs.extend([
                {"label": "analysis_typed_debtors", "question_type": "typed"},
                {"label": "analysis_typed_creditors", "question_type": "typed"},
            ])
        if difficulty_norm == "hard":
            family_specs.extend([
                {"label": "internal_control_typed_debtors", "question_type": "typed"},
                {"label": "internal_control_typed_creditors", "question_type": "typed"},
            ])

        if var_norm in {"journal", "calc", "typed", "mcq", "match"}:
            family_specs = [spec for spec in family_specs if spec["question_type"] == var_norm]

        family_labels = [spec["label"] for spec in family_specs]
        if not family_labels:
            return []

        plan: List[str] = []
        while len(plan) < total_count:
            chunk = family_labels[:]
            r.shuffle(chunk)
            plan.extend(chunk)
        return plan[:total_count]

    def _trial_balance_signature(question: Dict[str, Any]) -> str:
        prompt_text = str(question.get("prompt") or question.get("question_text") or question.get("question") or "").strip()
        reference_heading = str(((question.get("reference_journal") or {}).get("heading")) or "").strip()
        return f"{prompt_text}\n##REFERENCE##\n{reference_heading}"

    def _trading_stock_signature(question: Dict[str, Any]) -> str:
        prompt_text = str(question.get("prompt") or question.get("question_text") or question.get("question") or "").strip()
        sample_answer = str(question.get("sample_answer") or "").strip()
        reference_heading = str(((question.get("reference_journal") or {}).get("heading")) or "").strip()
        title_period = str(((question.get("title_answers") or {}).get("title_period")) or "").strip()
        return (
            f"{prompt_text}\n"
            f"##REFERENCE##\n{reference_heading}\n"
            f"##PERIOD##\n{title_period}\n"
            f"##SAMPLE##\n{sample_answer}"
        )

    def _control_accounts_signature(question: Dict[str, Any]) -> str:
        prompt_text = str(question.get("prompt") or question.get("question_text") or question.get("question") or "").strip()
        sample_answer = str(question.get("sample_answer") or "").strip()
        family_label = str(question.get("control_accounts_family") or "").strip()
        variant_label = str(question.get("control_accounts_variant") or "").strip()
        difficulty_label = str(question.get("difficulty") or "").strip()
        journals = question.get("journals") if isinstance(question.get("journals"), list) else []
        first_heading = ""
        if journals:
            first_heading = str((journals[0] or {}).get("heading") or (journals[0] or {}).get("journal_type") or "").strip()
        return (
            f"{prompt_text}\n"
            f"##FAMILY##\n{family_label}\n"
            f"##VARIANT##\n{variant_label}\n"
            f"##DIFFICULTY##\n{difficulty_label}\n"
            f"##JOURNAL##\n{first_heading}\n"
            f"##SAMPLE##\n{sample_answer}"
        )

    def _reconciliation_analysis_signature(question: Dict[str, Any]) -> str:
        prompt_text = str(question.get("prompt") or question.get("question_text") or question.get("question") or "").strip()
        difficulty_label = str(question.get("difficulty") or "").strip()
        rendered_rows = list(question.get("reconciliation_analysis_rows") or [])
        row_signature = "\n".join(
            f"{str(row.get('id') or '').strip()}|{str(row.get('text') or '').strip()}|{str(row.get('impacts') or '').strip()}"
            for row in rendered_rows
        )
        correct_map = str(question.get("correct_map") or "").strip()
        return (
            f"{difficulty_label}\n"
            f"##PROMPT##\n{prompt_text}\n"
            f"##ROWS##\n{row_signature}\n"
            f"##CORRECT##\n{correct_map}"
        )

    if subskill_norm == "concepts":
        return [builders["make_unified_concepts_question"](r=r) for _ in range(total_count)]

    if subskill_norm == "equation":
        return [
            builders["make_transaction_analysis_question"](r=r, difficulty=difficulty, mode=mode_norm)
            for _ in range(total_count)
        ]

    if subskill_norm == "trial_balance":
        plan = _build_trial_balance_plan(total_count)
        if not plan:
            return []

        business_names = pick_business_names(r=r, k=len(plan), unique_surnames=True)
        family_builders = {
            "from_balances": make_trial_balance_from_balances_question,
            "partial_completion": make_trial_balance_partial_completion_question,
            "control_balance": make_trial_balance_control_balance_question,
        }

        out: List[Dict[str, Any]] = []
        seen_signatures: set[str] = set()
        for idx, family_label in enumerate(plan):
            builder = family_builders[family_label]
            business_name = business_names[idx] if idx < len(business_names) else None
            q = builder(r=r, difficulty=difficulty, mode=mode_norm, business=business_name)
            for _ in range(8):
                signature = _trial_balance_signature(q)
                if signature not in seen_signatures:
                    break
                q = builder(r=r, difficulty=difficulty, mode=mode_norm, business=business_name)
            seen_signatures.add(_trial_balance_signature(q))
            out.append(q)
        return out

    if subskill_norm == "trading_stock_account":
        plan = _build_trading_stock_plan(total_count)
        if not plan:
            return []

        family_builders = {
            "prepare_from_journals": builders["make_trading_stock_prepare_from_journals_question"],
            "fill_missing_details": builders["make_trading_stock_fill_missing_details_question"],
            "prepare_from_casted_journals": builders["make_trading_stock_prepare_from_casted_journals_question"],
            "prepare_with_returns_percent": builders["make_trading_stock_prepare_with_returns_percent_question"],
            "prepare_with_discount_calc": builders["make_trading_stock_prepare_with_discount_calc_question"],
            "section3_analysis_typed": builders["make_trading_stock_section3_analysis_typed"],
            "prepare_with_two_returns_percent": builders["make_trading_stock_prepare_with_two_returns_percent_question"],
            "markup_trade_discount_typed": builders["make_trading_stock_markup_trade_discount_typed"],
            "activity16_analysis_typed": builders["make_trading_stock_activity16_analysis_typed"],
        }

        out: List[Dict[str, Any]] = []
        seen_signatures: set[str] = set()
        for family_label in plan:
            builder = family_builders[family_label]
            if family_label in {"section3_analysis_typed", "markup_trade_discount_typed", "activity16_analysis_typed"}:
                q = builder(r=r)
            else:
                q = builder(r=r, difficulty=difficulty, mode=mode_norm)
            for _ in range(8):
                signature = _trading_stock_signature(q)
                if signature not in seen_signatures:
                    break
                if family_label in {"section3_analysis_typed", "markup_trade_discount_typed", "activity16_analysis_typed"}:
                    q = builder(r=r)
                else:
                    q = builder(r=r, difficulty=difficulty, mode=mode_norm)
            seen_signatures.add(_trading_stock_signature(q))
            out.append(q)
        return out

    if subskill_norm == "control_accounts":
        plan = _build_control_accounts_plan(total_count)
        if not plan:
            return []

        business_names = pick_business_names(r=r, k=len(plan), unique_surnames=True)
        family_builders = {
            "study_debtors": lambda business_name: builders["make_control_account_study_question"](r=r, difficulty=difficulty, mode=mode_norm, variant="debtors", business=business_name),
            "study_creditors": lambda business_name: builders["make_control_account_study_question"](r=r, difficulty=difficulty, mode=mode_norm, variant="creditors", business=business_name),
            "opening_balance_calc_debtors": lambda business_name: builders["make_control_accounts_opening_balance_calc"](r=r, difficulty=difficulty, variant="debtors", business=business_name),
            "opening_balance_calc_creditors": lambda business_name: builders["make_control_accounts_opening_balance_calc"](r=r, difficulty=difficulty, variant="creditors", business=business_name),
            "analysis_typed_debtors": lambda business_name: builders["make_control_accounts_analysis_typed"](r=r, difficulty=difficulty, variant="debtors", business=business_name),
            "analysis_typed_creditors": lambda business_name: builders["make_control_accounts_analysis_typed"](r=r, difficulty=difficulty, variant="creditors", business=business_name),
            "internal_control_typed_debtors": lambda business_name: builders["make_control_accounts_internal_control_typed"](r=r, variant="debtors", business=business_name),
            "internal_control_typed_creditors": lambda business_name: builders["make_control_accounts_internal_control_typed"](r=r, variant="creditors", business=business_name),
        }

        out: List[Dict[str, Any]] = []
        seen_signatures: set[str] = set()
        for idx, family_label in enumerate(plan):
            builder = family_builders[family_label]
            business_name = business_names[idx] if idx < len(business_names) else None
            q = builder(business_name)
            for _ in range(8):
                signature = _control_accounts_signature(q)
                if signature not in seen_signatures:
                    break
                q = builder(business_name)
            seen_signatures.add(_control_accounts_signature(q))
            out.append(q)
        return out

    if subskill_norm == "control_accounts_reconciliation":
        if var_norm not in ("", "mixed", "journal"):
            return []
        plan: List[str] = []
        while len(plan) < total_count:
            chunk = ["debtors", "creditors"]
            r.shuffle(chunk)
            plan.extend(chunk)
        plan = plan[:total_count]
        business_names = pick_business_names(r=r, k=len(plan), unique_surnames=True)

        out: List[Dict[str, Any]] = []
        seen_signatures: set[str] = set()
        for idx, variant_label in enumerate(plan):
            business_name = business_names[idx] if idx < len(business_names) else None
            q = builders["make_control_accounts_reconciliation_question"](
                r=r,
                difficulty=difficulty,
                mode=mode_norm,
                variant=variant_label,
                business=business_name,
            )
            for _ in range(8):
                signature = _control_accounts_signature(q)
                if signature not in seen_signatures:
                    break
                q = builders["make_control_accounts_reconciliation_question"](
                    r=r,
                    difficulty=difficulty,
                    mode=mode_norm,
                    variant=variant_label,
                    business=business_name,
                )
            seen_signatures.add(_control_accounts_signature(q))
            out.append(q)
        return out

    if subskill_norm == "reconciliation_analysis":
        if var_norm not in ("", "mixed", "journal"):
            return []
        out: List[Dict[str, Any]] = []
        seen_signatures: set[str] = set()
        for _ in range(total_count):
            q = builders["make_reconciliation_impact_matrix_question"](r=r, difficulty=difficulty)
            for _ in range(16):
                signature = _reconciliation_analysis_signature(q)
                if signature not in seen_signatures:
                    break
                q = builders["make_reconciliation_impact_matrix_question"](r=r, difficulty=difficulty)
            seen_signatures.add(_reconciliation_analysis_signature(q))
            out.append(q)
        return out

    return build_journal_questions_for_subskill(
        subskill_norm=subskill_norm,
        total_count=total_count,
        var_norm=var_norm,
        plan_builder=_build_single_to_multi_plan,
        r=r,
        difficulty=difficulty,
        mode_norm=mode_norm,
        make_crj_single_row_question=builders["make_crj_single_row_question"],
        make_crj_activity5_question=builders["make_crj_activity5_question"],
        make_crj_exam_style_question=builders["make_crj_exam_style_question"],
        make_cpj_single_row_question=builders["make_cpj_single_row_question"],
        make_cpj_activity5_question=builders["make_cpj_activity5_question"],
        make_cpj_exam_style_question=builders["make_cpj_exam_style_question"],
        make_dj_single_row_question=builders["make_dj_single_row_question"],
        make_dj_activity_question=builders["make_dj_activity_question"],
        make_dj_exam_style_question=builders["make_dj_exam_style_question"],
        make_daj_single_row_question=builders["make_daj_single_row_question"],
        make_daj_activity_question=builders["make_daj_activity_question"],
        make_daj_exam_style_question=builders["make_daj_exam_style_question"],
        make_cj_single_row_question=builders["make_cj_single_row_question"],
        make_cj_activity_question=builders["make_cj_activity_question"],
        make_cj_exam_style_question=builders["make_cj_exam_style_question"],
        make_caj_single_row_question=builders["make_caj_single_row_question"],
        make_caj_activity_question=builders["make_caj_activity_question"],
        make_caj_exam_style_question=builders["make_caj_exam_style_question"],
        make_gj_single_row_question=builders["make_gj_single_row_question"],
        make_gj_activity13_question=builders["make_gj_activity13_question"],
        make_gj_exam_style_question=builders["make_gj_exam_style_question"],
        make_pcj_single_row_question=builders["make_pcj_single_row_question"],
        make_pcj_activity11_question=builders["make_pcj_activity11_question"],
        make_pcj_exam_style_question=builders["make_pcj_exam_style_question"],
    )
