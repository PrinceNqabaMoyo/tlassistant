import json
import sys

sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import ALL_GENERATORS, get_topic_archetypes

data = json.load(open('caps-ai-backend/app/services/caps_term_registry_data.json', encoding='utf-8'))
g7 = [t for t in data if str(t.get('grade')) == '7' and str(t.get('subject', '')).lower() == 'mathematics']
print('Total Grade 7 Math topics:', len(g7))
for i, t in enumerate(g7, 1):
    gen_key = t.get('generator_key')
    name = t.get('name')
    term = t.get('term')
    fn = ALL_GENERATORS.get(gen_key)
    mod_name = 'None'
    if fn:
        wrapped = getattr(fn, "_wrapped_func", fn)
        import inspect
        mod = inspect.getmodule(wrapped)
        if mod:
            mod_name = mod.__name__.split('.')[-1]
    
    subskills = []
    if fn and hasattr(fn, "get_subskills"):
        subskills = fn.get_subskills()
    elif fn and hasattr(wrapped, "get_subskills"):
        subskills = wrapped.get_subskills()
    elif fn and hasattr(mod, "get_subskills"):
        subskills = mod.get_subskills()
    else:
        subskills = get_topic_archetypes('mathematics', '7', name)
    print(f"{i:02d}. [T{term}] {name} ({gen_key}) -> {len(subskills)} archetypes (mod: {mod_name})")
