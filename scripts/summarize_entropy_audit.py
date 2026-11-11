import json

with open('reports/topic_archetypes_and_entropy_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

summary = data['summary']
print('=== EXECUTIVE SUMMARY ===')
print('Total Topics:', summary['total_topics'])
print('Total Archetypes:', summary['total_archetypes'])
print('Overall Mean Entropy:', summary['overall_mean_entropy'], '/ 20')
print('Execution Time:', summary['execution_time_seconds'], 's')

print('\n=== GRADE BREAKDOWN ===')
for g, stats in summary['grade_breakdown'].items():
    t_cnt = stats['topics']
    a_cnt = stats['archetypes']
    avg_e = stats['average_entropy']
    ratio = round(a_cnt / t_cnt, 2) if t_cnt else 0
    print(f"Grade {g:>2}: {t_cnt:3d} topics | {a_cnt:4d} archetypes ({ratio:4.2f}/topic) | Mean Entropy: {avg_e:5.2f}/20")

topics = data['topics']

# Subject breakdown
from collections import defaultdict
subj_stats = defaultdict(lambda: {'topics': 0, 'archetypes': 0, 'ratings': []})
for t in topics:
    key = f"{t['subject']}"
    subj_stats[key]['topics'] += 1
    subj_stats[key]['archetypes'] += t['archetype_count']
    for a in t['archetypes']:
        subj_stats[key]['ratings'].append(a['rating'])

print('\n=== SUBJECT BREAKDOWN (ACROSS ALL GRADES) ===')
for subj, st in sorted(subj_stats.items()):
    mean_r = round(sum(st['ratings']) / len(st['ratings']), 2) if st['ratings'] else 0
    ratio = round(st['archetypes'] / st['topics'], 2) if st['topics'] else 0
    print(f"{subj:<35} | {st['topics']:3d} topics | {st['archetypes']:4d} archs ({ratio:4.1f}/top) | Mean: {mean_r:5.2f}/20")

# Critical defects (< 2.0)
defect_topics = [t for t in topics if t['average_entropy_rating'] <= 2.0]
print(f'\n=== CRITICAL DEFECT TOPICS (Rating <= 2.0/20): {len(defect_topics)} ===')
for dt in defect_topics:
    print(f"Gr{dt['grade']} {dt['subject']} - {dt['topic']}: {dt['average_entropy_rating']}/20 (key: {dt['generator_key']})")

# Low-entropy topics (2.0 < rating < 10.0)
low_topics = [t for t in topics if 2.0 < t['average_entropy_rating'] < 10.0]
print(f'\n=== LOW ENTROPY TOPICS (2.0 < Rating < 10.0): {len(low_topics)} ===')
for lt in low_topics[:15]:
    print(f"Gr{lt['grade']} {lt['subject']} - {lt['topic']}: {lt['average_entropy_rating']}/20 ({lt['archetype_count']} archs)")

# Top-tier high-entropy standouts (rating >= 18.0)
high_topics = [t for t in topics if t['average_entropy_rating'] >= 18.0]
print(f'\n=== EXCEPTIONAL HIGH ENTROPY STANDOUTS (Rating >= 18.0/20): {len(high_topics)} ===')
for ht in high_topics[:15]:
    print(f"Gr{ht['grade']} {ht['subject']} - {ht['topic']}: {ht['average_entropy_rating']}/20 ({ht['archetype_count']} archs)")
