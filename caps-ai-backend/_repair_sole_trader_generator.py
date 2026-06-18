from pathlib import Path

TARGET = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade10_accounting\sole_trader_generator.py")
REPORT = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\_repair_sole_trader_generator_report.txt")


def remove_between(text: str, start_marker: str, end_marker: str) -> str:
    start = text.index(start_marker)
    end = text.index(end_marker)
    return text[:start] + text[end:]


text = TARGET.read_text(encoding="utf-8")
original_len = len(text)
report_lines = [f"original_len={original_len}"]

top_start_marker = '"""\n{"q": "The profitability'
top_end_marker = 'def _ta_headers_activity23()'
broken_start_marker = '_BROKEN_LEDGER_BLOCK = """'
broken_end_marker = 'def _make_ledger_posting_question('

report_lines.append(f"top_start={text.index(top_start_marker)}")
report_lines.append(f"top_end={text.index(top_end_marker)}")
report_lines.append(f"broken_start={text.index(broken_start_marker)}")
report_lines.append(f"broken_end={text.index(broken_end_marker)}")

text = remove_between(
    text,
    top_start_marker,
    top_end_marker,
)
text = remove_between(
    text,
    broken_start_marker,
    broken_end_marker,
)

TARGET.write_text(text, encoding="utf-8")
report_lines.append(f"new_len={len(text)}")
report_lines.append(f"changed={len(text) != original_len}")
REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
print("repaired", len(text))
