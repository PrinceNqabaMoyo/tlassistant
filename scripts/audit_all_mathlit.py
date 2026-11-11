import sys
import json
sys.path.insert(0, "caps-ai-backend")

from app.services.generator_registry import ALL_GENERATORS, resolve_generator_key, get_topic_archetypes

records = json.load(open("caps-ai-backend/app/services/caps_term_registry_data.json", encoding="utf-8"))

for grade in ["10", "11"]:
    items = [r for r in records if r.get("grade") in (int(grade), grade, f"Grade {grade}") and "Literacy" in r.get("subject", "")]
    print(f"\n==========================================")
    print(f"AUDITING GRADE {grade} MATHEMATICAL LITERACY ({len(items)} topics)")
    print(f"==========================================")
    for it in items:
        name = it.get("name")
        key = it.get("generator_key")
        res_key = resolve_generator_key(name, grade=grade, subject="Mathematical Literacy")
        gen = ALL_GENERATORS.get(res_key)
        
        info = get_topic_archetypes(name, grade=grade, subject="Mathematical Literacy")
        subskills = info.get("archetypes", [])
        
        synthetic_opts = []
        syntax_errors = []
        if gen:
            try:
                for idx in range(min(5, len(subskills))):
                    q = gen(seed=101 + idx, archetype_index=idx, count=1)[0]
                    opts = q.get("options", [])
                    for opt in opts:
                        if "(Alt" in opt or "(Option" in opt or "(Alternative" in opt:
                            synthetic_opts.append(opt)
                        if "{ }" in opt or "{,}" in opt:
                            syntax_errors.append(opt)
                    prompt = q.get("prompt", "")
                    if "{ }" in prompt or "{,}" in prompt:
                        syntax_errors.append(prompt[:40])
            except Exception as e:
                syntax_errors.append(f"Gen error: {e}")
        
        status = "PASS" if len(subskills) >= 50 and not synthetic_opts and not syntax_errors else "WARN"
        print(f"[{status}] {name} (Key: {res_key})")
        print(f"       Subskills count: {len(subskills)}")
        if synthetic_opts:
            print(f"       Synthetic options: {synthetic_opts[:3]}")
        if syntax_errors:
            print(f"       Errors: {syntax_errors[:3]}")
