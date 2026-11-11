import re

from scripts.audit_target_functions import targets

for fpath, fn_name, num in targets:
    try:
        content = open(fpath, "r", encoding="utf-8").read()
    except Exception as e:
        print(f"ERROR: {fpath} -> {e}")
        continue
    fn_idx = content.find(f"def {fn_name}")
    if fn_idx == -1:
        print(f"NOT FOUND: {fn_name}")
        continue
    next_def = content.find("\ndef ", fn_idx + 4)
    fn_body = content[fn_idx:next_def] if next_def != -1 else content[fn_idx:]
    # find d_spec var name
    m = re.search(r'(d_spec\w*)\s*=', fn_body)
    var_name = m.group(1) if m else "NO_VAR"
    # find return line(s)
    ret_idx = fn_body.find("return ")
    ret_snippet = fn_body[ret_idx:ret_idx+200].replace("\n", " ") if ret_idx != -1 else "NO_RETURN"
    print(f"[{fn_name}] var={var_name} | ret={ret_snippet[:100]}")
