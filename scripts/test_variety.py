import sys
sys.path.insert(0, 'caps-ai-backend')
from app.utils.grade7_mathematics import (
    data_collection_tally_generator as tally,
    data_representation_generator as repr_data,
    data_measures_generator as measures,
    functions_relationships_1_generator as fn1,
    functions_relationships_2_generator as fn2,
    functions_relationships_3_generator as fn3,
)

mods = [('tally', tally), ('repr', repr_data), ('measures', measures), ('fn1', fn1), ('fn2', fn2), ('fn3', fn3)]

for name, mod in mods:
    for s in mod.SUBSKILLS:
        q1 = mod.generate(1, subskill=s, seed=101)[0]
        q2 = mod.generate(1, subskill=s, seed=202)[0]
        q3 = mod.generate(1, subskill=s, seed=303)[0]
        p1 = q1.get('prompt') or q1.get('question') or ''
        p2 = q2.get('prompt') or q2.get('question') or ''
        p3 = q3.get('prompt') or q3.get('question') or ''
        if p1 == p2 and p2 == p3:
            print(f"STATIC ZERO ENTROPY: {name} -> {s}")
        else:
            print(f"OK Variety: {name} -> {s}")
