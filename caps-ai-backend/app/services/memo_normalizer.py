"""Shared Memo Contract Normalizer (Rule GP-4 compliant).

Enforces the canonical memorandum contract across all subjects and grades:
  1. MCQ: Starts with letter option and bold answer: `(A) **Option text** [marks]`
  2. Multi-part: Distinctly separated parts: `(a) **answer** [marks]`, `(b) **answer** [marks]`
  3. Single-part: `**answer** [marks]` followed by step-by-step working.
  4. Cell-by-cell derivations for tabular/journal questions.
"""
import re
from typing import Any, Dict, List, Optional

PART_SPLIT_RX = re.compile(r'(?mi)^\s*(?:\(?([a-z0-9])\)|\b([a-z0-9])\.)\s+')


def _extract_mcq_letter(q: Dict[str, Any]) -> str:
    """Returns 'A', 'B', 'C', 'D' if identifiable, else 'A'."""
    options = q.get("options") or []
    c_idx = q.get("correct_index")
    if isinstance(c_idx, int) and 0 <= c_idx < len(options):
        return chr(65 + c_idx)
    c_ans = str(q.get("correct_answer") or "").strip()
    if c_ans and options:
        for idx, opt in enumerate(options):
            if str(opt).strip().lower() == c_ans.lower():
                return chr(65 + idx)
            m = re.match(r'^([A-D])\s*[\).]\s*(.*)', str(opt), re.I)
            if m and (m.group(1).upper() == c_ans.upper() or m.group(2).strip().lower() == c_ans.lower()):
                return m.group(1).upper()
    m = re.match(r'^([A-D])\s*[\).]\s*', c_ans, re.I)
    if m:
        return m.group(1).upper()
    return "A"


def _clean_str(s: Any) -> str:
    if s is None:
        return ""
    if isinstance(s, (list, tuple)):
        val = "\n".join(str(x) for x in s if x is not None).strip()
    else:
        val = str(s).strip()
    val = re.sub(r'SS\s*\\?\[\s*[MA]\s*\\?\]', '', val).strip()
    return val


def _build_completed_markdown_table(q: Dict[str, Any]) -> str:
    """Reconstructs a complete Markdown table for any tabular/journal/ledger question
    by combining prefilled cells from `rows` and expected answers from `correct_map`.
    Required cells are rendered in **bold** so the memorandum displays the full
    completed accounting table.
    """
    table_schema = q.get("table_schema") if isinstance(q.get("table_schema"), dict) else None
    journal = q.get("journal") if isinstance(q.get("journal"), dict) else None

    headers = (
        q.get("headers")
        or (table_schema.get("headers") if table_schema else None)
        or (table_schema.get("columns") if table_schema else None)
        or (journal.get("headers") if journal else None)
    )
    rows = (
        q.get("rows")
        or (table_schema.get("rows") if table_schema else None)
        or (journal.get("rows") if journal else None)
    )
    correct_map = q.get("correct_map") if isinstance(q.get("correct_map"), dict) else {}
    if not correct_map and isinstance(q.get("correct_answer"), dict):
        correct_map = q["correct_answer"]

    if not isinstance(rows, list) or not rows:
        return ""

    # Determine column count
    col_count = 0
    if isinstance(headers, list) and headers:
        col_count = len(headers)
    else:
        for r in rows:
            if isinstance(r, list):
                col_count = max(col_count, len(r))
    if col_count == 0:
        return ""

    if not isinstance(headers, list) or not headers:
        headers = [f"Col {i + 1}" for i in range(col_count)]
    else:
        headers = [str(h if h is not None else "").replace("|", "/").replace("\n", " ").strip() or "Details" for h in headers]
        if len(headers) < col_count:
            headers.extend([f"Col {i + 1}" for i in range(len(headers), col_count)])

    md_lines = [
        "| " + " | ".join(headers[:col_count]) + " |",
        "| " + " | ".join(["---"] * col_count) + " |",
    ]

    for r_idx, row in enumerate(rows):
        if not isinstance(row, list):
            continue
        row_cells: List[str] = []
        for c_idx in range(col_count):
            cell = row[c_idx] if c_idx < len(row) else ""
            val_str = ""
            is_editable = False
            if isinstance(cell, dict):
                cid = str(cell.get("cell_id") or cell.get("coordinate") or f"r{r_idx}_c{c_idx}")
                is_editable = bool(cell.get("editable")) or cell.get("type") in ("required", "input") or (cid in correct_map)
                exp_val = (
                    correct_map.get(cid)
                    or correct_map.get(f"t0_r{r_idx}_c{c_idx}")
                    or correct_map.get(f"r{r_idx}_c{c_idx}")
                    or cell.get("expected")
                    or cell.get("value")
                )
                val_str = str(exp_val if exp_val is not None else "").strip()
            else:
                exp_val = (
                    correct_map.get(f"t0_r{r_idx}_c{c_idx}")
                    or correct_map.get(f"r{r_idx}_c{c_idx}")
                )
                if exp_val is not None:
                    val_str = str(exp_val).strip()
                    is_editable = True
                else:
                    val_str = str(cell if cell is not None else "").strip()

            val_str = val_str.replace("|", "/").replace("\n", " ")
            if is_editable and val_str:
                val_str = f"**{val_str}**"
            row_cells.append(val_str)
        md_lines.append("| " + " | ".join(row_cells) + " |")

    return "\n".join(md_lines)


def normalize_memo(q: Dict[str, Any]) -> str:
    """Normalizes the question's memorandum to strictly comply with the GP-4 contract."""
    if not isinstance(q, dict):
        return ""

    marks = int(q.get("marks") or 2)
    prompt = _clean_str(q.get("prompt") or q.get("question") or "")
    existing_ws = _clean_str(q.get("worked_solution") or q.get("canonical_solution") or q.get("explanation") or "")
    raw_sample = _clean_str(q.get("sample_answer") or q.get("correct_answer") or "")
    options = q.get("options")

    # -------------------------------------------------------------
    # 1. Multiple Choice Questions
    # -------------------------------------------------------------
    if options and isinstance(options, list) and len(options) >= 2:
        letter = _extract_mcq_letter(q)
        c_ans = raw_sample
        if not c_ans:
            c_idx = q.get("correct_index")
            if isinstance(c_idx, int) and 0 <= c_idx < len(options):
                c_ans = str(options[c_idx])
        c_ans = re.sub(r'^[A-D]\s*[\).]\s*', '', c_ans).strip()
        mark_tag = f"[{marks} mark{'s' if marks != 1 else ''}]"
        header = f"({letter}) **{c_ans}** {mark_tag}"

        working = existing_ws
        if working.startswith(header):
            return working
        working = re.sub(r'^(?:Correct\s+Answer|Answer|Option)\s*:\s*.*?\n+', '', working, flags=re.I).strip()
        if working and working.lower() != c_ans.lower():
            return f"{header}\n\n**Explanation / Working:**\n{working}"
        return header

    # -------------------------------------------------------------
    # 2. Accounting / Tabular Journals & Statements
    # -------------------------------------------------------------
    md_table = _build_completed_markdown_table(q)
    correct_map = q.get("correct_map")
    if md_table:
        mark_tag = f"[{marks} mark{'s' if marks != 1 else ''}]"
        table_block = f"**Completed Memorandum Table** {mark_tag}\n\n{md_table}"
        if existing_ws and "Completed Accounting" not in existing_ws and "Completed Memorandum Table" not in existing_ws:
            return f"{table_block}\n\n**Journal Derivations & Ledger Rules:**\n{existing_ws}"
        return table_block

    if isinstance(correct_map, dict) and correct_map:
        entries = []
        part_idx = 0
        for k, v in correct_map.items():
            if str(k).startswith("title_") or not str(v).strip():
                continue
            part_letter = chr(97 + (part_idx % 26))
            entries.append(f"({part_letter}) **{k}: {v}** [1 mark]")
            part_idx += 1
        if entries:
            header = "\n".join(entries[:12])
            if existing_ws and "Completed Accounting" not in existing_ws:
                return f"{header}\n\n**Journal Derivations & Ledger Rules:**\n{existing_ws}"
            return header

    # -------------------------------------------------------------
    # 3. Multi-part Questions (prompt or ws has (a), (b) or 1., 2. or Step 1, Step 2)
    # -------------------------------------------------------------
    step_splits = re.split(r'(?mi)^\s*(?:Step\s*(\d+)[:.]|(?:\(?([a-z0-9])\)|\b([a-z0-9])\.)\s+)', existing_ws)
    # If existing_ws has step/part headers
    step_matches = list(re.finditer(r'(?mi)^\s*(?:Step\s*(\d+)[:.]|(?:\(?([a-z0-9])\)|\b([a-z0-9])\.)\s+)', existing_ws))
    if len(step_matches) >= 2:
        parts_out = []
        for i, m in enumerate(step_matches):
            label = chr(97 + i)
            start_pos = m.end()
            end_pos = step_matches[i+1].start() if i+1 < len(step_matches) else len(existing_ws)
            body = existing_ws[start_pos:end_pos].strip()
            # First line of body is the target answer/summary
            lines = [l.strip() for l in body.splitlines() if l.strip()]
            first_line = lines[0] if lines else "Refer to solution steps"
            first_line = re.sub(r'\s*\[\s*\d+\s*marks?\s*\]', '', first_line, flags=re.I).strip()
            first_line = re.sub(r'^\*\*|\*\*$', '', first_line).strip()
            rest_body = "\n".join(lines[1:]) if len(lines) > 1 else ""
            part_str = f"({label}) **{first_line}** [1 mark]"
            if rest_body:
                part_str += f"\n{rest_body}"
            parts_out.append(part_str)
        return "\n\n".join(parts_out)

    # -------------------------------------------------------------
    # 4. Standard Single-Part Calculation / Answer
    # -------------------------------------------------------------
    best_ans = raw_sample
    if not best_ans and existing_ws:
        best_ans = existing_ws.splitlines()[0].strip()
    if not best_ans:
        best_ans = "Refer to step-by-step solution"

    # Ensure best_ans is a single clean line for the bold header
    clean_lines = [l.strip() for l in best_ans.splitlines() if l.strip()]
    first_ans_line = clean_lines[0] if clean_lines else "Refer to solution"
    first_ans_line = re.sub(r'^\*\*(.*?)\*\*$', r'\1', first_ans_line).strip()

    mark_tag = f"[{marks} mark{'s' if marks != 1 else ''}]"
    best_ans_formatted = f"**{first_ans_line}** {mark_tag}"

    if existing_ws and existing_ws != first_ans_line:
        clean_ws = existing_ws
        if clean_ws.startswith(first_ans_line):
            clean_ws = clean_ws[len(first_ans_line):].strip()
        if clean_ws:
            return f"{best_ans_formatted}\n\n**Step-by-Step Working:**\n{clean_ws}"

    return best_ans_formatted
