"""
Audit script to compute multi-seed entropy across ALL_GENERATORS in generator_registry.py.
Entropy = len(set(prompts)) / len(prompts) over seeds [101, 102, 103, 104].
Threshold requirement: >= 0.75 (at least 3 unique prompts out of 4 seeds, ideally 1.00).
"""
import sys
import os

# Set UTF-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

# Ensure caps-ai-backend is in path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'caps-ai-backend'))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from app.services.generator_registry import ALL_GENERATORS

SEEDS = [101, 102, 103, 104]

def extract_prompt_text(q):
    if not isinstance(q, dict):
        return str(q)
    if 'questions' in q and isinstance(q['questions'], list) and q['questions']:
        return extract_prompt_text(q['questions'][0])
    if 'items' in q and isinstance(q['items'], list) and q['items']:
        return extract_prompt_text(q['items'][0])
    # Check for direct prompt
    p = q.get('prompt') or q.get('question') or q.get('question_text') or q.get('scenario') or q.get('stem') or ''
    if p:
        return str(p).strip()
    # If compound parts
    parts = q.get('parts') or []
    if parts and isinstance(parts, list):
        part_prompts = []
        for part in parts:
            if isinstance(part, dict):
                part_prompts.append(part.get('question') or part.get('prompt') or '')
        if any(part_prompts):
            return " | ".join(str(pp) for pp in part_prompts if pp)
    # If ledger / table
    if q.get('transactions'):
        return str(q.get('transactions'))
    return str(q)[:100]

def audit():
    print(f"=== Starting Entropy Audit across {len(ALL_GENERATORS)} Generators ===")
    
    results = {}
    errors = {}
    low_entropy = {}
    
    for gen_name, gen_func in ALL_GENERATORS.items():
        prompts = []
        gen_error = None
        
        for s in SEEDS:
            try:
                # Call generator with seed
                # Try calling with count=1 and seed=s
                try:
                    res = gen_func(count=1, seed=s)
                except TypeError:
                    try:
                        res = gen_func(seed=s)
                    except TypeError:
                        res = gen_func()
                
                # Normalize result
                if isinstance(res, list):
                    item = res[0] if res else {}
                else:
                    item = res
                
                pt = extract_prompt_text(item)
                prompts.append(pt)
            except Exception as e:
                gen_error = f"{type(e).__name__}: {str(e)}"
                break
        
        if gen_error:
            errors[gen_name] = gen_error
        else:
            entropy = len(set(prompts)) / len(prompts) if prompts else 0.0
            results[gen_name] = {
                'entropy': entropy,
                'unique_count': len(set(prompts)),
                'prompts': prompts
            }
            if entropy < 0.75:
                low_entropy[gen_name] = {
                    'entropy': entropy,
                    'prompts': prompts
                }

    summary = []
    summary.append(f"Total Generators: {len(ALL_GENERATORS)}")
    summary.append(f"Errors / Failures: {len(errors)}")
    summary.append(f"Generators with Entropy < 0.75: {len(low_entropy)}")
    summary.append(f"Generators with Entropy >= 0.75: {len(results) - len(low_entropy)}")
    
    if errors:
        summary.append("\n=== ERRORS ===")
        for k, err in sorted(errors.items()):
            summary.append(f"  {k}: {err}")
            
    if low_entropy:
        summary.append("\n=== LOW ENTROPY (< 0.75) ===")
        for k, data in sorted(low_entropy.items()):
            summary.append(f"  {k}: entropy={data['entropy']:.2f}")
            for idx, p in enumerate(data['prompts']):
                summary.append(f"    seed {SEEDS[idx]}: {p[:90]!r}")
                
    text = "\n".join(summary)
    print(text)
    out_path = os.path.join(os.path.dirname(__file__), 'entropy_audit_output.txt')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    audit()
