files = [
    "caps-ai-backend/app/utils/mathematical_literacy/gr11_conversions_and_time_generator.py",
    "caps-ai-backend/app/utils/mathematical_literacy/gr11_plans_representations_generator.py",
    "caps-ai-backend/app/utils/mathematical_literacy/gr11_data_handling_generator.py",
    "caps-ai-backend/app/utils/mathematical_literacy/gr11_maps_generator.py",
    "caps-ai-backend/app/utils/mathematical_literacy/gr11_patterns_relationships_generator.py",
]

for fp in files:
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Replace item = gen_fn(r)\n        results.append(item)
    # with item = gen_fn(r)\n        item["subskill"] = chosen_subskill\n        results.append(item)
    target = "item = gen_fn(r)\n        results.append(item)"
    repl = "item = gen_fn(r)\n        item[\"subskill\"] = chosen_subskill\n        results.append(item)"
    if target in text:
        text = text.replace(target, repl)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated {fp}")
    else:
        print(f"Target not found in {fp}")
