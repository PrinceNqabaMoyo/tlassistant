import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'caps-ai-backend')

from scripts.audit_diagram_description_leak import _harvest, find_figure_references

findings = []
for t, seed, q, err in _harvest("Physical Sciences", ["10", "11", "12"], [101, 102, 103]):
    if not q or err:
        continue
    prompt = q.get("prompt") or q.get("question") or ""
    refs = find_figure_references(prompt)
    has_diag = bool(q.get("diagram_spec") or q.get("circuit_diagram") or q.get("svg"))
    if refs and not has_diag:
        findings.append((t["grade"], t["name"], seed, refs, prompt[:120], q.get("subskill_id") or q.get("subskill")))

print(f"Total findings: {len(findings)}")
for g, topic, seed, refs, p_snip, sub in findings:
    print(f"Gr{g} [{topic}] seed={seed} (sub={sub}): refs={refs}")
    print(f"   prompt: {p_snip}...")
