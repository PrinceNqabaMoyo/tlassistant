"""Phase 0 carry-over audit (Grades 7-12), Rule 0d-15 & Rule 31 compliant.

Runs every manifest topic through generate_variant at 3 seeds and counts
defect patterns in the emitted question text. Writes a machine-generated
report to reports/phase0_carryover_report.{json,md}. Nothing here is hand-typed.

Usage: python scripts/audit_grade_carryover.py [--grades 7,8] [--strict] [--plant-defect none|unmarkable|mismatch]
"""
import argparse
import collections
import json
import os
import re
import sys
import time
import traceback

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'caps-ai-backend'))

from app.services.generator_registry import generate_variant, resolve_generator_key, ALL_GENERATORS  # noqa: E402

SEEDS = [42, 101, 777]
COUNT = 2
TEXT_KEYS = ('prompt', 'question', 'worked_solution', 'explanation',
             'sample_answer', 'correct_answer')

CHECKS = {
    # rendering leaks
    # `\\` inside array/align/\hline is valid LaTeX; only flag it when it is NOT part of a
    # row/line break, i.e. followed by a letter (e.g. \\text, \\frac) -> escaped one level too far.
    'double_backslash': re.compile(r'\\\\[a-zA-Z]'),
    'literal_backslash_n': re.compile(r'(?<!\\)\\n(?![a-zA-Z])'),
    'bold_quote_wrap': re.compile(r'\*\*\s*["\u201c]'),
    'ss_marker': re.compile(r'SS\s*\\?\[\s*(M|A)\s*\\?\]'),
    'mojibake': re.compile('\ufffd|\u00e2\u20ac|\u00c3[\u00a0-\u00bf]'),
    # prompt wording leaks (prompt/question only)
    'method_named_in_prompt': re.compile(
        r'(?i)\b(difference of (two )?squares|bodmas|pemdas|additive inverse|'
        r'multiplicative inverse|distributive (law|property)|'
        r'(using|use|by using|apply) the [a-z\- ]{0,30}(method|property|law|formula|rule))\b'),
    'formula_given_in_prompt': re.compile(r'(?i)\b(maximum\s*[-\u2212]\s*minimum|length\s*[x\u00d7*]\s*width)\b'),
}
PROMPT_ONLY = {'method_named_in_prompt', 'formula_given_in_prompt'}

# Concepts that are the actual assessment target of the topic (Rule GP-9 allow-list)
METHOD_ALLOWLIST = {
    ('Mathematics', 'Integers'): {'additive inverse'},
}

FIGURE_WORDS = re.compile(
    r'(?i:\b(in the (given )?(figure|diagram)|given (figure|diagram)|shown (below|above)|'
    r'wireframe|icosahedron|dodecahedron|octahedron|tetrahedron|'
    r'(rectangular|triangular) prism|pyramid|cylinder|cone|(?<!celestial\s)sphere)\b)|'
    r'(?i:\b(triangle|quadrilateral|parallelogram|trapezium)\b)\s+[A-Z]{3,4}\b')

NAME_PLACE_WATCH = ['Mitchell', 'Imran', 'Chloe']

POLY_NAME = re.compile(r'\b(?i:triangle|quadrilateral|parallelogram|trapezium|rectangle|square|rhombus|kite)\s+([A-Z]{3,4})\b')
PART_LINE = re.compile(r'(?m)^\s*(?:\d+\.|\([a-z]\)|[a-z]\.)\s+\S')
PART_MARK = re.compile(r'(?mi)(?:^\s*(?:\d+\.|\([a-z]\)|[a-z]\.)\s)|\bpart\s*\d|\bstep\s*\d')


def part_count(prompt):
    return len(PART_LINE.findall(prompt))


def diagram_letter_mismatch(prompt, q):
    """True when the prompt names a polygon (e.g. KLMN) but the diagram labels other letters."""
    named = set()
    for m in POLY_NAME.finditer(prompt):
        named.update(m.group(1))
    if not named:
        return False
    spec = None
    for k in ('diagram_spec', 'diagram', 'diagram_meta'):
        if isinstance(q.get(k), dict) and q.get(k):
            spec = q[k]
            break
    if not spec:
        return False
    labels = set(re.findall(r'"([A-Z])"', json.dumps(spec)))
    return len(labels) >= 3 and not named <= labels


def is_unmarkable(q):
    """Check 6: returns True if question lacks any markable answer or rubric mechanism."""
    if not isinstance(q, dict):
        return True
    # MCQ
    if 'options' in q and q['options']:
        has_correct = (
            q.get('correct_index') is not None or
            q.get('correct_answer') is not None or
            q.get('answer') is not None
        )
        if not has_correct:
            return True
        return False
    # Standard answers
    for key in ('expected_answers', 'answer', 'final_answer', 'correct_answer', 'sample_answer', 'solution'):
        val = q.get(key)
        if val is not None and val != '' and val != []:
            return False
    # Rubric / schema / steps
    if q.get('marking_schema') or q.get('rubric') or q.get('solution_steps'):
        return False
    # Tables / journals
    if q.get('table') or q.get('ledger') or q.get('journal') or q.get('cells'):
        return False
    # Worked solution present with content
    ws = q.get('worked_solution') or q.get('explanation')
    if ws and len(str(ws).strip()) > 10:
        return False
    return True


def check_topic_resolution(subject, grade, topic_name):
    """Check 7: returns (resolved_key, is_mismatch_error)."""
    try:
        resolved = resolve_generator_key(topic_name, grade=str(grade), subject=subject)
        if not resolved or resolved not in ALL_GENERATORS:
            return resolved, f"Topic '{topic_name}' failed resolution or not in ALL_GENERATORS (resolved='{resolved}')"
        return resolved, None
    except Exception as e:
        return None, f"Topic '{topic_name}' resolution raised {type(e).__name__}: {str(e)[:100]}"


def load_topics(grades):
    path = os.path.join(ROOT, 'caps-ai-backend', 'app', 'services', 'caps_term_registry_data.json')
    data = json.load(open(path, encoding='utf-8'))
    rows = data if isinstance(data, list) else data.get('topics') or data.get('entries') or []
    seen, out = set(), []
    for r in rows:
        if not isinstance(r, dict):
            continue
        g = str(r.get('grade'))
        if g not in grades:
            continue
        key = (r.get('subject'), g, r.get('name'))
        if key in seen:
            continue
        seen.add(key)
        out.append(key)
    return out


def has_diagram(q):
    for k in ('diagram_spec', 'diagram', 'diagram_meta'):
        if isinstance(q.get(k), dict) and q.get(k):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grades', default='7,8,9,10,11,12')
    ap.add_argument('--max-topics', type=int, default=0)
    ap.add_argument('--strict', action='store_true', help='Exit with code 1 if any defect, unmarkable part, or mismatch exists')
    ap.add_argument('--plant-defect', choices=['none', 'unmarkable', 'mismatch'], default='none',
                    help='Test flag: deliberately plant a defect to prove strict mode exits 1')
    args = ap.parse_args()
    grades = set(args.grades.split(','))

    topics = load_topics(grades)
    if args.max_topics:
        topics = topics[:args.max_topics]

    expected_total_questions = len(topics) * len(SEEDS) * COUNT
    print(f'Auditing {len(topics)} topics x {len(SEEDS)} seeds x {COUNT} questions (Expected total: {expected_total_questions})')

    results = []
    t0 = time.time()
    total_unmarkable = 0
    total_mismatches = 0
    mismatch_details = []

    for i, (subject, grade, name) in enumerate(topics, 1):
        rec = {'subject': subject, 'grade': grade, 'topic': name,
               'questions': 0, 'crash': None,
               'counts': collections.Counter(), 'figure_without_diagram': 0,
               'diagram_emitted': 0, 'unmarkable_part': 0, 'registry_mismatch': None,
               'watch': collections.Counter(), 'examples': {}}

        # Check 7: Registry resolution check against authoritative manifest
        if args.plant_defect == 'mismatch' and i == 1:
            res_key, res_err = check_topic_resolution('InvalidSubject', '99', 'FakeTopicNonExistent')
        else:
            res_key, res_err = check_topic_resolution(subject, grade, name)

        if res_err:
            rec['registry_mismatch'] = res_err
            total_mismatches += 1
            mismatch_details.append(res_err)

        for seed in SEEDS:
            try:
                qs = generate_variant(name, seed=seed, count=COUNT, grade=grade, subject=subject)
                qlist = qs if isinstance(qs, list) else [qs]
                sub = 1
                while len(qlist) < COUNT:
                    subseed = (seed * 1000 + sub) % 2147483647
                    extra = generate_variant(name, seed=subseed, count=1, grade=grade, subject=subject)
                    qlist.extend(extra if isinstance(extra, list) else [extra])
                    sub += 1
            except Exception as e:  # noqa: BLE001
                rec['crash'] = f'{type(e).__name__}: {str(e)[:160]}'
                break

            for q_idx, q in enumerate(qlist[:COUNT]):
                if not isinstance(q, dict):
                    continue

                # Planted unmarkable defect check
                if args.plant_defect == 'unmarkable' and i == 1 and seed == SEEDS[0] and q_idx == 0:
                    q = {'prompt': 'What is the answer to this mystery question with no answer key?'}

                rec['questions'] += 1

                # Check 6: Unmarkable part
                if is_unmarkable(q):
                    rec['unmarkable_part'] += 1
                    total_unmarkable += 1
                    rec['examples'].setdefault('unmarkable_part', str(q.get('prompt') or q)[:120])

                prompt = str(q.get('prompt') or q.get('question') or '')
                for key in TEXT_KEYS:
                    val = q.get(key)
                    if not isinstance(val, str):
                        continue
                    for cname, rx in CHECKS.items():
                        if cname in PROMPT_ONLY and key not in ('prompt', 'question'):
                            continue
                        m = rx.search(val)
                        if m:
                            if cname == 'method_named_in_prompt':
                                allowed_tokens = METHOD_ALLOWLIST.get((subject, name), set())
                                matched_text = m.group(0).lower()
                                if any(tok in matched_text for tok in allowed_tokens):
                                    continue
                            rec['counts'][cname] += 1
                            rec['examples'].setdefault(cname, val[max(0, m.start() - 30):m.end() + 30])
                if has_diagram(q):
                    rec['diagram_emitted'] += 1
                    if diagram_letter_mismatch(prompt, q):
                        rec['counts']['diagram_letter_mismatch'] += 1
                        rec['examples'].setdefault('diagram_letter_mismatch', prompt[:140])
                elif FIGURE_WORDS.search(prompt):
                    rec['figure_without_diagram'] += 1
                    rec['examples'].setdefault('figure_without_diagram', prompt[:140])
                n_parts = part_count(prompt)
                memo = str(q.get('worked_solution') or q.get('explanation') or '')
                if n_parts >= 2 and len(PART_MARK.findall(memo)) < n_parts:
                    rec['counts']['memo_parts_not_separated'] += 1
                    rec['examples'].setdefault('memo_parts_not_separated', memo[:140])
                blob = ' '.join(str(q.get(k, '')) for k in TEXT_KEYS)
                for w in NAME_PLACE_WATCH:
                    if w in blob:
                        rec['watch'][w] += 1
        rec['counts'] = dict(rec['counts'])
        rec['watch'] = dict(rec['watch'])
        results.append(rec)
        if i % 25 == 0:
            print(f'  {i}/{len(topics)} ({time.time() - t0:.0f}s)')

    out_dir = os.path.join(ROOT, 'reports')
    os.makedirs(out_dir, exist_ok=True)
    json.dump(results, open(os.path.join(out_dir, 'phase0_carryover_report.json'), 'w', encoding='utf-8'), indent=1)

    cols = list(CHECKS) + ['diagram_letter_mismatch', 'memo_parts_not_separated', 'figure_without_diagram', 'unmarkable_part']
    lines = ['# Phase 0 carry-over report (generated by scripts/audit_grade_carryover.py)', '',
             f'Topics: {len(results)}; seeds: {SEEDS}; questions per seed: {COUNT}', '']
    crashes = [r for r in results if r['crash']]
    lines.append(f'Crashing topics: {len(crashes)}')
    for r in crashes:
        lines.append(f"- Gr{r['grade']} {r['subject']} / {r['topic']}: {r['crash']}")
    lines.append(f'Registry mismatches: {total_mismatches}')
    for m in mismatch_details:
        lines.append(f"- {m}")
    lines.append(f'Unmarkable parts: {total_unmarkable}')
    lines += ['', '## Defect totals by grade', '', '| Grade | topics | questions | ' + ' | '.join(cols) + ' |',
              '|' + '---|' * (3 + len(cols))]
    by_grade = collections.defaultdict(lambda: collections.Counter())
    total_q_generated = 0
    total_defects_count = 0

    for r in results:
        c = by_grade[r['grade']]
        c['topics'] += 1
        c['questions'] += r['questions']
        total_q_generated += r['questions']
        for k in CHECKS:
            c[k] += r['counts'].get(k, 0)
            total_defects_count += r['counts'].get(k, 0)
        c['diagram_letter_mismatch'] += r['counts'].get('diagram_letter_mismatch', 0)
        total_defects_count += r['counts'].get('diagram_letter_mismatch', 0)
        c['memo_parts_not_separated'] += r['counts'].get('memo_parts_not_separated', 0)
        total_defects_count += r['counts'].get('memo_parts_not_separated', 0)
        c['figure_without_diagram'] += r['figure_without_diagram']
        total_defects_count += r['figure_without_diagram']
        c['unmarkable_part'] += r['unmarkable_part']
        total_defects_count += r['unmarkable_part']

    for g in sorted(by_grade, key=int):
        c = by_grade[g]
        lines.append(f"| {g} | {c['topics']} | {c['questions']} | " + ' | '.join(str(c[k]) for k in cols) + ' |')
    lines += ['', '## Topics with defects (count of questions affected)', '']
    for r in results:
        hit = {k: v for k, v in r['counts'].items() if v}
        if r['figure_without_diagram']:
            hit['figure_without_diagram'] = r['figure_without_diagram']
        if r['unmarkable_part']:
            hit['unmarkable_part'] = r['unmarkable_part']
        if hit:
            lines.append(f"- Gr{r['grade']} {r['subject']} / {r['topic']}: {hit}")
    watch = collections.Counter()
    for r in results:
        for k, v in r['watch'].items():
            watch[(r['grade'], k)] += v
    lines += ['', '## Name/place repetition watch (question count containing token)', '']
    for (g, k), v in sorted(watch.items()):
        lines.append(f'- Gr{g} {k}: {v}')
    open(os.path.join(out_dir, 'phase0_carryover_report.md'), 'w', encoding='utf-8').write('\n'.join(lines))
    print(f'Report: reports/phase0_carryover_report.md (Total questions: {total_q_generated}/{expected_total_questions}, Defects: {total_defects_count}, Crashes: {len(crashes)}, Mismatches: {total_mismatches})')

    if args.strict:
        has_failure = (
            len(crashes) > 0 or
            total_mismatches > 0 or
            total_unmarkable > 0 or
            total_defects_count > 0 or
            total_q_generated != expected_total_questions
        )
        if has_failure:
            print(f"[STRICT AUDIT FAILED] Crashes: {len(crashes)}, Mismatches: {total_mismatches}, Unmarkable: {total_unmarkable}, Defects: {total_defects_count}, Questions: {total_q_generated}/{expected_total_questions}")
            return 1
        print(f"[STRICT AUDIT PASSED] 100% clean: {total_q_generated}/{expected_total_questions} questions verified with 0 defects.")
        return 0

    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(1)
