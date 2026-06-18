from __future__ import annotations

import json
import random
import sys
from pathlib import Path
from typing import Any, Dict, List

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.utils.sole_trader.full_accounting_cycle_project import make_full_accounting_cycle_project_question


def _table_type(table: Dict[str, Any]) -> str:
    return str(table.get("journal_type") or table.get("journalType") or "")


def _sample_summary(*, difficulty: str, mode: str, seed: int) -> Dict[str, Any]:
    question = make_full_accounting_cycle_project_question(
        r=random.Random(seed),
        difficulty=difficulty,
        mode=mode,
    )
    journals = list(question.get("journals") or [])
    prompt = str(question.get("prompt") or "")
    prompt_lines = [line for line in prompt.splitlines() if line.strip()]
    table_types = [_table_type(table) for table in journals if _table_type(table)]
    return {
        "seed": seed,
        "status": "ok",
        "journal_count": len(journals),
        "guideline_count": len(question.get("guidelines") or []),
        "cell_hint_count": len(question.get("cell_hints") or {}),
        "working_map_count": len(question.get("working_map") or {}),
        "dependency_map_count": len(question.get("dependency_map") or {}),
        "table_types": table_types,
        "prompt_head": prompt_lines[:12],
    }


def build_report() -> List[Dict[str, Any]]:
    report: List[Dict[str, Any]] = []
    seeds = [101, 202, 303]
    for difficulty in ["easy", "medium", "hard"]:
        for mode in ["practice", "scaffold"]:
            samples: List[Dict[str, Any]] = []
            for seed in seeds:
                try:
                    samples.append(_sample_summary(difficulty=difficulty, mode=mode, seed=seed))
                except Exception as exc:
                    samples.append(
                        {
                            "seed": seed,
                            "status": "error",
                            "error": f"{type(exc).__name__}: {exc}",
                        }
                    )
            report.append(
                {
                    "difficulty": difficulty,
                    "mode": mode,
                    "samples": samples,
                }
            )
    return report


def _render_markdown(report: List[Dict[str, Any]]) -> str:
    lines: List[str] = ["# Full Cycle Phase 9 Smoke Report", ""]
    for entry in report:
        lines.append(f"## {entry['difficulty']} / {entry['mode']}")
        lines.append("")
        for sample in entry.get("samples") or []:
            lines.append(f"### Seed {sample.get('seed')}")
            lines.append("")
            lines.append(f"- status: {sample.get('status')}")
            if sample.get("status") != "ok":
                lines.append(f"- error: {sample.get('error')}")
                lines.append("")
                continue
            lines.append(f"- journal_count: {sample.get('journal_count')}")
            lines.append(f"- guideline_count: {sample.get('guideline_count')}")
            lines.append(f"- cell_hint_count: {sample.get('cell_hint_count')}")
            lines.append(f"- working_map_count: {sample.get('working_map_count')}")
            lines.append(f"- dependency_map_count: {sample.get('dependency_map_count')}")
            lines.append(f"- table_types: {', '.join(sample.get('table_types') or [])}")
            lines.append("- prompt_head:")
            for prompt_line in sample.get("prompt_head") or []:
                lines.append(f"  - {prompt_line}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    json_path = repo_root / "phase9_full_cycle_smoke_report.json"
    md_path = repo_root / "phase9_full_cycle_smoke_report.md"
    report = build_report()
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(_render_markdown(report), encoding="utf-8")


if __name__ == "__main__":
    main()
