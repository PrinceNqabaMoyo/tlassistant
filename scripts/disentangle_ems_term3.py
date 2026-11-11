import os

# Helper to build a clean module from subskills and source file
def build_ems_module(src_file, target_file, subskills, curriculum_ref, subtopic_id):
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will import the source module and extract items dynamically or template them
    pass

# We will write a complete script that extracts the exact items from term3_entrepreneurship and term1_businesses
script_content = '''
import os, sys
sys.path.insert(0, 'caps-ai-backend')

from app.utils.grade7_ems import term3_entrepreneurship as src_ent
from app.utils.grade7_ems import term1_businesses as src_bus

def make_standalone_module(subskills, curriculum_ref, subtopic_id, src_mod):
    import inspect
    src_lines = inspect.getsource(src_mod).splitlines()
    
    # Header
    out = []
    out.append("import random")
    out.append("from app.utils.ems_namelist import NAMES, AREAS, get_ems_scenario")
    out.append("")
    out.append("def _rng(seed=None):")
    out.append("    return random.Random(seed)")
    out.append("")
    out.append("TOPIC_ID = 'grade7_ems'")
    out.append(f"SUBTOPIC_ID = '{subtopic_id}'")
    out.append(f"CURRICULUM_REFERENCE = '{curriculum_ref}'")
    out.append("")
    
    # Copy _with_metadata
    out.append(inspect.getsource(src_mod._with_metadata))
    out.append("")
    
    # Extract item dicts for the specified subskills
    # We can inspect the source code of _concept_pool and _discussion_pool or filter items
    # Better: filter items by calling pool with a fixed seed or generating code
    out.append("SUBSKILLS = " + repr(subskills))
    out.append("")
    
    # Copy helper question formatters
    out.append(inspect.getsource(src_mod._mcq_question))
    out.append("")
    out.append(inspect.getsource(src_mod._typed_question))
    out.append("")
    
    return out
'''
