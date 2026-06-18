from __future__ import annotations

import json
import random
import sys
from pathlib import Path
from typing import Any, Dict, List

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.utils.grade10_accounting.sole_trader_generation_dispatch import build_direct_dispatched_subskill_questions
from app.utils.grade10_accounting.sole_trader_generator import _make_control_account_study_question
from app.utils.grade10_accounting.sole_trader_generator import _make_control_accounts_analysis_typed
from app.utils.grade10_accounting.sole_trader_generator import _make_control_accounts_internal_control_typed
from app.utils.grade10_accounting.sole_trader_generator import _make_control_accounts_opening_balance_calc
from app.utils.grade10_accounting.sole_trader_generator import _make_control_accounts_reconciliation_question
from app.utils.grade10_accounting.sole_trader_generator import _make_reconciliation_impact_matrix_question


BUILDERS = {
    "make_control_account_study_question": _make_control_account_study_question,
    "make_control_accounts_analysis_typed": _make_control_accounts_analysis_typed,
    "make_control_accounts_internal_control_typed": _make_control_accounts_internal_control_typed,
    "make_control_accounts_opening_balance_calc": _make_control_accounts_opening_balance_calc,
    "make_control_accounts_reconciliation_question": _make_control_accounts_reconciliation_question,
    "make_reconciliation_impact_matrix_question": _make_reconciliation_impact_matrix_question,
}


def _question_prompt(question: Dict[str, Any]) -> str:
    return str(question.get("prompt") or question.get("question_text") or question.get("question") or "").strip()


def _batch_summary(*, subskill: str, difficulty: str, mode: str, seed: int) -> Dict[str, Any]:
    questions = build_direct_dispatched_subskill_questions(
        subskill_norm=subskill,
        total_count=8,
        var_norm="mixed",
        r=random.Random(seed),
        difficulty=difficulty,
        mode_norm=mode,
        builders=BUILDERS,
    )
    prompts = [_question_prompt(question) for question in questions]
    prompt_tables = sum(1 for question in questions if question.get("prompt_journal"))
    return {
        "seed": seed,
        "status": "ok",
        "count": len(questions),
        "unique_prompts": len(set(prompts)),
        "prompt_table_count": prompt_tables,
        "pipe_prompt_count": sum(1 for prompt in prompts if "|" in prompt),
        "families": [str(question.get("control_accounts_family") or question.get("journal_type") or "") for question in questions],
    }


def build_report() -> List[Dict[str, Any]]:
    report: List[Dict[str, Any]] = []
    combos = [
        ("control_accounts", ["easy", "medium", "hard"], ["practice", "scaffold"]),
        ("control_accounts_reconciliation", ["easy", "medium", "hard"], ["practice", "scaffold"]),
        ("reconciliation_analysis", ["easy", "medium", "hard"], ["practice"]),
    ]
    for subskill, difficulties, modes in combos:
        for difficulty in difficulties:
            for mode in modes:
                seed = abs(hash((subskill, difficulty, mode))) % 100000
                try:
                    summary = _batch_summary(subskill=subskill, difficulty=difficulty, mode=mode, seed=seed)
                except Exception as exc:
                    summary = {
                        "seed": seed,
                        "status": "error",
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                report.append(
                    {
                        "subskill": subskill,
                        "difficulty": difficulty,
                        "mode": mode,
                        "summary": summary,
                    }
                )
    return report


def _render_markdown(report: List[Dict[str, Any]]) -> str:
    lines: List[str] = ["# Control Accounts Smoke Report", ""]
    for entry in report:
        lines.append(f"## {entry['subskill']} / {entry['difficulty']} / {entry['mode']}")
        lines.append("")
        summary = dict(entry.get("summary") or {})
        lines.append(f"- status: {summary.get('status')}")
        lines.append(f"- seed: {summary.get('seed')}")
        if summary.get("status") != "ok":
            lines.append(f"- error: {summary.get('error')}")
            lines.append("")
            continue
        lines.append(f"- question count: {summary.get('count')}")
        lines.append(f"- unique prompts: {summary.get('unique_prompts')}")
        lines.append(f"- prompt tables: {summary.get('prompt_table_count')}")
        lines.append(f"- raw pipe prompts: {summary.get('pipe_prompt_count')}")
        lines.append(f"- families: {', '.join(summary.get('families') or [])}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    report = build_report()
    json_path = repo_root / "control_accounts_smoke_report.json"
    md_path = repo_root / "control_accounts_smoke_report.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(_render_markdown(report), encoding="utf-8")


if __name__ == "__main__":
    main()
