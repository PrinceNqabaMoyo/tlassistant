from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional


def build_journal_questions_for_subskill(
    *,
    subskill_norm: str,
    total_count: int,
    var_norm: str,
    plan_builder: Callable[[int], List[str]],
    r: Any,
    difficulty: str,
    mode_norm: str,
    make_crj_single_row_question: Callable[..., Dict[str, Any]],
    make_crj_activity5_question: Callable[..., Dict[str, Any]],
    make_crj_exam_style_question: Callable[..., Dict[str, Any]],
    make_cpj_single_row_question: Callable[..., Dict[str, Any]],
    make_cpj_activity5_question: Callable[..., Dict[str, Any]],
    make_cpj_exam_style_question: Callable[..., Dict[str, Any]],
    make_dj_single_row_question: Callable[..., Dict[str, Any]],
    make_dj_activity_question: Callable[..., Dict[str, Any]],
    make_dj_exam_style_question: Callable[..., Dict[str, Any]],
    make_daj_single_row_question: Callable[..., Dict[str, Any]],
    make_daj_activity_question: Callable[..., Dict[str, Any]],
    make_daj_exam_style_question: Callable[..., Dict[str, Any]],
    make_cj_single_row_question: Callable[..., Dict[str, Any]],
    make_cj_activity_question: Callable[..., Dict[str, Any]],
    make_cj_exam_style_question: Callable[..., Dict[str, Any]],
    make_caj_single_row_question: Callable[..., Dict[str, Any]],
    make_caj_activity_question: Callable[..., Dict[str, Any]],
    make_caj_exam_style_question: Callable[..., Dict[str, Any]],
    make_gj_single_row_question: Callable[..., Dict[str, Any]],
    make_gj_activity13_question: Callable[..., Dict[str, Any]],
    make_gj_exam_style_question: Callable[..., Dict[str, Any]],
    make_pcj_single_row_question: Callable[..., Dict[str, Any]],
    make_pcj_activity11_question: Callable[..., Dict[str, Any]],
    make_pcj_exam_style_question: Callable[..., Dict[str, Any]],
) -> Optional[List[Dict[str, Any]]]:
    journal_subskill_builders = {
        "crj": lambda: build_planned_uncycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            make_single=lambda: make_crj_single_row_question(r=r, difficulty=difficulty),
            make_activity=lambda: make_crj_activity5_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_exam=lambda: make_crj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
        ),
        "cpj": lambda: build_planned_cycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            cycle=["A", "B", "C", "D"],
            make_single=lambda current_vid: make_cpj_single_row_question(r=r),
            make_activity=lambda current_vid: make_cpj_activity5_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=current_vid),
            make_exam=lambda current_vid: make_cpj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=current_vid),
        ),
        "dj": lambda: build_planned_uncycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            make_single=lambda: make_dj_single_row_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_activity=lambda: make_dj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_exam=lambda: make_dj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
        ),
        "daj": lambda: build_planned_uncycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            make_single=lambda: make_daj_single_row_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_activity=lambda: make_daj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_exam=lambda: make_daj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
        ),
        "cj": lambda: build_planned_uncycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            make_single=lambda: make_cj_single_row_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_activity=lambda: make_cj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_exam=lambda: make_cj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
        ),
        "caj": lambda: build_planned_uncycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            make_single=lambda: make_caj_single_row_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_activity=lambda: make_caj_activity_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_exam=lambda: make_caj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm),
        ),
        "gj": lambda: build_planned_cycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            cycle=["A", "B"],
            make_single=lambda current_vid: make_gj_single_row_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_activity=lambda current_vid: make_gj_activity13_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=current_vid),
            make_exam=lambda current_vid: make_gj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=current_vid),
        ),
        "pcj": lambda: build_planned_cycled_journal_questions(
            total_count=total_count,
            var_norm=var_norm,
            plan_builder=plan_builder,
            cycle=["A", "B"],
            make_single=lambda current_vid: make_pcj_single_row_question(r=r, difficulty=difficulty, mode=mode_norm),
            make_activity=lambda current_vid: make_pcj_activity11_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=current_vid),
            make_exam=lambda current_vid: make_pcj_exam_style_question(r=r, difficulty=difficulty, mode=mode_norm, variant_id=current_vid),
        ),
    }
    journal_builder = journal_subskill_builders.get(subskill_norm)
    if journal_builder is None:
        return None
    return journal_builder()


def build_planned_uncycled_journal_questions(
    *,
    total_count: int,
    var_norm: str,
    plan_builder: Callable[[int], List[str]],
    make_single: Callable[[], Dict[str, Any]],
    make_activity: Callable[[], Dict[str, Any]],
    make_exam: Callable[[], Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if var_norm in {"single", "activity", "exam"}:
        plan = [var_norm for _ in range(total_count)]
    else:
        plan = plan_builder(total_count)
    return build_uncycled_journal_questions(
        plan=plan,
        make_single=make_single,
        make_activity=make_activity,
        make_exam=make_exam,
    )


def build_planned_cycled_journal_questions(
    *,
    total_count: int,
    var_norm: str,
    plan_builder: Callable[[int], List[str]],
    cycle: List[str],
    make_single: Callable[[str], Dict[str, Any]],
    make_activity: Callable[[str], Dict[str, Any]],
    make_exam: Callable[[str], Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if var_norm in {"single", "activity", "exam"}:
        plan = [var_norm for _ in range(total_count)]
    else:
        plan = plan_builder(total_count)
    return build_cycled_journal_questions(
        plan=plan,
        cycle=cycle,
        make_single=make_single,
        make_activity=make_activity,
        make_exam=make_exam,
    )


def build_uncycled_journal_questions(
    *,
    plan: List[str],
    make_single: Callable[[], Dict[str, Any]],
    make_activity: Callable[[], Dict[str, Any]],
    make_exam: Callable[[], Dict[str, Any]],
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    seen_prompts: set[str] = set()

    for question_kind in plan:
        if question_kind == "single":
            builder = make_single
        elif question_kind == "activity":
            builder = make_activity
        else:
            builder = make_exam
        q = builder()
        for _ in range(8):
            prompt_sig = str(q.get("prompt") or "")
            if prompt_sig not in seen_prompts:
                break
            q = builder()
        seen_prompts.add(str(q.get("prompt") or ""))
        out.append(q)

    return out


def build_cycled_journal_questions(
    *,
    plan: List[str],
    cycle: List[str],
    make_single: Callable[[str], Dict[str, Any]],
    make_activity: Callable[[str], Dict[str, Any]],
    make_exam: Callable[[str], Dict[str, Any]],
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    seen_prompts: set[str] = set()
    cycle_values = list(cycle or ["A"])

    for i, question_kind in enumerate(plan):
        variant_id = str(cycle_values[i % len(cycle_values)])
        if question_kind == "single":
            builder = make_single
        elif question_kind == "activity":
            builder = make_activity
        else:
            builder = make_exam
        q = builder(variant_id)
        for _ in range(8):
            prompt_sig = str(q.get("prompt") or "")
            if prompt_sig not in seen_prompts:
                break
            q = builder(variant_id)
        seen_prompts.add(str(q.get("prompt") or ""))
        out.append(q)

    return out
