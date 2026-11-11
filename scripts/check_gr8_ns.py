import sys, os, importlib.util, glob
sys.path.insert(0, 'caps-ai-backend')

files = sorted(glob.glob('caps-ai-backend/app/utils/natural_sciences/ns8_*.py'))
all_ok = True
for f in files:
    name = os.path.basename(f)[:-3]
    spec = importlib.util.spec_from_file_location(name, f)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        gen_fn = getattr(mod, 'generate', None)
        subskills = getattr(mod, 'SUBSKILLS', None)
        res = gen_fn(seed=101, count=1)
        sub_count = len(subskills) if subskills else 0
        qid = res[0].get('id') if res and isinstance(res, list) else 'no_id'
        print(f'{name}: OK ({sub_count} subskills, id={qid})')
    except Exception as e:
        print(f'{name}: ERROR {e}')
        all_ok = False

print('ALL 13 GRADE 8 NS GENERATORS OK:', all_ok)
