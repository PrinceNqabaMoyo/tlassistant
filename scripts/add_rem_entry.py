import json
from pathlib import Path

p = Path("reports/full_archetype_audit/ledger_gr7.json")
data = json.loads(p.read_text(encoding="utf-8"))
data["remediations"] = [
    {
        "archetype_id": "multiplicative_identity",
        "description": "Fixed mathematical defect in whole_numbers_generator.py where identity property assigned ans = val instead of 0 for addition and 1 for multiplication.",
        "curriculum_doc_path": "curriculum_docs_auto/Mathematics_Gr7/Term 1/01. Working with whole numbers.md",
        "before_shot": "reports/full_archetype_audit/shots/gr7_mathematics_working_with_whole_numbers_multiplicative_identity_pre_scroll_1.png",
        "after_shot": "reports/full_archetype_audit/shots/gr7_mathematics_working_with_whole_numbers_multiplicative_identity_memo_scroll_1.png",
    }
]
p.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("Saved remediation entry to ledger_gr7.json")
