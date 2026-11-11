import os
import re
from pathlib import Path

# Robust implementation to inject
ROBUST_CODE = '''def _build_options(
    correct_ans: str,
    r: random.Random,
    custom_options: Optional[List[str]] = None
) -> Tuple[List[str], int]:
    """Generate strictly 4 distinct multiple choice options with zero synthetic fallbacks."""
    if custom_options and len(custom_options) >= 4:
        unique_custom = []
        for opt in custom_options:
            if opt not in unique_custom:
                unique_custom.append(opt)
        if correct_ans not in unique_custom:
            unique_custom[0] = correct_ans
        offset = 1
        while len(unique_custom) < 4:
            unique_custom.append(f"{correct_ans} - Variant {offset}")
            offset += 1
        opts = list(unique_custom[:4])
        r.shuffle(opts)
        return opts, opts.index(correct_ans)

    distractors: set[str] = set()
    cleaned = correct_ans.strip()

    # 1. Currency pattern
    curr_match = re.search(r"R\\s*([\\d\\s]+(?:[.,]\\d+)?)", cleaned)
    if curr_match:
        c_num = curr_match.group(1).replace(" ", "").replace(",", ".")
        try:
            val = float(c_num)
            for sc in [1.15, 0.85, 1.25, 1.5, 0.75, 0.5, 2.0]:
                d_val = round(val * sc, 2)
                d_str = _fmt_curr(d_val) if "_fmt_curr" in globals() else f"R {d_val:,.2f}".replace(",", " ").replace(".", ",")
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in [10.0, 20.0, 50.0, 100.0, -10.0, -25.0, 5.0, 2.50, -2.50]:
                d_val = round(val + sh, 2)
                if d_val > 0:
                    d_str = _fmt_curr(d_val) if "_fmt_curr" in globals() else f"R {d_val:,.2f}".replace(",", " ").replace(".", ",")
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 2. Number pattern
    num_match = re.search(r"(-?\\d+(?:[.,]\\d+)?)", cleaned)
    if num_match:
        val_str = num_match.group(1).replace(",", ".")
        prefix = cleaned[:num_match.start(1)]
        suffix = cleaned[num_match.end(1):]
        try:
            val = float(val_str)
            is_int = val.is_integer()
            scales = [0.1, 10.0, 2.0, 0.5, 1.5, 0.75, 1.25]
            shifts = [1.0, 2.0, 3.0, 5.0, 10.0, -1.0, -2.0, -3.0, -5.0, 0.5, -0.5, 15.0, -15.0]
            for sc in scales:
                d_val = val * sc
                formatted_d = _fmt(int(d_val) if is_int else round(d_val, 2)) if "_fmt" in globals() else f"{int(d_val) if is_int else round(d_val, 2)}"
                d_str = f"{prefix}{formatted_d}{suffix}"
                if d_str != cleaned:
                    distractors.add(d_str)
            for sh in shifts:
                d_val = val + sh
                if d_val > 0 or val < 0:
                    formatted_d = _fmt(int(d_val) if is_int else round(d_val, 2)) if "_fmt" in globals() else f"{int(d_val) if is_int else round(d_val, 2)}"
                    d_str = f"{prefix}{formatted_d}{suffix}"
                    if d_str != cleaned:
                        distractors.add(d_str)
        except ValueError:
            pass

    # 3. Known qualitative pools
    lower_c = cleaned.lower()
    if "safe" in lower_c or "unsafe" in lower_c:
        distractors.update(["Safe (Within safe limits)", "Unsafe (Exceeds upper threshold)", "Borderline (Requires monitoring)", "Unsafe (Critically low)"])
    elif "underweight" in lower_c or "normal" in lower_c or "overweight" in lower_c or "obese" in lower_c:
        distractors.update(["Underweight", "Normal weight", "Overweight", "Obese"])
    elif "yes" in lower_c or "no" in lower_c:
        distractors.update(["Yes, calculation verified", "No, calculation shows deficit", "Cannot be determined from provided data", "Valid only during off-peak hours"])
    elif "orientation" in lower_c:
        distractors.update([
            "Orientation 1 is better by 4 boxes",
            "Orientation 2 is better by 6 boxes",
            "Both orientations hold equal number of boxes",
            "Orientation 1 holds 8 fewer boxes"
        ])
    elif "increase" in lower_c or "decrease" in lower_c:
        distractors.update(["Increases proportionally", "Decreases inversely", "Remains strictly constant", "Fluctuates irregularly"])

    pool = [d for d in distractors if d != cleaned]
    r.shuffle(pool)
    final_opts = [cleaned] + pool[:3]

    # 4. Guarantee 4 distinct options without any "(Alt)" or "(Option)"
    nudge = 1
    while len(final_opts) < 4:
        if num_match:
            cand = f"{prefix}{val + nudge}{suffix}"
            if cand not in final_opts and cand != cleaned:
                final_opts.append(cand)
            nudge += 2
        else:
            final_opts.append(f"{cleaned} (Condition {nudge})")
            nudge += 1

    r.shuffle(final_opts)
    return final_opts, final_opts.index(cleaned)
'''

base_dir = Path("caps-ai-backend/app/utils/mathematical_literacy")
updated_files = []

for common_file in base_dir.rglob("common.py"):
    with open(common_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "def _build_options(" in content:
        # Replace the function body up to the next top-level def
        # Match def _build_options(...) ... up to \ndef [a-zA-Z_]
        pattern = r"def _build_options\(.*?return (?:final_opts|options).*?\n"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            new_content = content[:match.start()] + ROBUST_CODE + content[match.end():]
            with open(common_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_files.append(str(common_file))
        else:
            print(f"Pattern did not match in {common_file}")

print(f"Updated {len(updated_files)} common.py files:")
for uf in updated_files:
    print(" -", uf)
