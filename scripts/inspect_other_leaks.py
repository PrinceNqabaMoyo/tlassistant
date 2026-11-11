import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'caps-ai-backend')

from scripts.audit_diagram_description_leak import _harvest, find_figure_references

for subj in ["Life Sciences", "Accounting"]:
    findings = []
    for t, seed, q, err in _harvest(subj, ["10", "11", "12"], [101, 102, 103]):
        if not q or err:
            continue
        prompt = q.get("prompt") or q.get("question") or ""
        refs = find_figure_references(prompt)
        has_diag = bool(q.get("diagram_spec") or q.get("diagram") or q.get("circuit_diagram") or q.get("svg"))
        if refs and not has_diag:
            findings.append((t["grade"], t["name"], seed, refs, prompt[:120]))
    print(f"=== {subj}: {len(findings)} findings ===")
    for g, topic, seed, refs, p_snip in findings:
        print(f"Gr{g} [{topic}] seed={seed}: refs={refs}")
        print(f"   prompt: {p_snip}...")
