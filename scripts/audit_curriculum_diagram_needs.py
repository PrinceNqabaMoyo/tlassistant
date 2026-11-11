import os
import json
import time
from pathlib import Path

CURRICULUM_DIR = Path('curriculum_docs_auto')

# Keyword terms for fast substring matching
MODALITY_KEYWORDS = {
    'circuit': [
        'circuit', 'voltmeter', 'ammeter', 'resistor', 'ohm',
        'series-parallel', 'electric current', 'potential difference', 'emf',
        'internal resistance'
    ],
    'free_body_diagram': [
        'free-body', 'free body', 'force diagram', 'normal force', 'frictional force',
        'vector diagram', 'resultant force', "newton's second law", "newton's law",
        'incline', 'tension'
    ],
    'motion_graph': [
        'velocity-time', 'position-time', 'acceleration-time', 'ticker timer',
        'gradient of the graph', 'area under the graph', 'displacement-time'
    ],
    'punnett_square': [
        'punnett', 'monohybrid', 'dihybrid', 'genetic cross',
        'pedigree diagram', 'allele', 'phenotypic ratio', 'genotypic ratio'
    ],
    'biological_labeling': [
        'cell organelle', 'mitochondria', 'nucleus', 'chloroplast',
        'nephron', 'human eye', 'human ear', 'heart', 'reflex arc',
        'digestive system', 'circulatory system', 'reproductive system',
        'flower structure', 'angiosperm', 'meiosis', 'mitosis'
    ],
    'chemical_structure': [
        'bohr model', 'lewis diagram', 'electron configuration',
        'structural formula', 'isomer', 'periodic table', 'intermolecular forces',
        'phase change', 'heating curve'
    ],
    'wave_optics': [
        'ray diagram', 'reflection', 'refraction', "snell's law",
        'transverse wave', 'longitudinal wave', 'crest', 'trough',
        'focal point', 'converging lens'
    ],
    'jsxgraph_geometry': [
        'euclidean geometry', 'circle geometry', 'tangent', 'cyclic quad',
        'trigonometric graph', 'parabola', 'hyperbola', 'exponential graph'
    ]
}

def analyze_topic(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    dc_count = text.count('[Diagram Context')
    lower_text = text.lower()

    # Extract DC text
    dc_parts = []
    idx = 0
    while True:
        pos = text.find('[Diagram Context', idx)
        if pos == -1:
            break
        # Take up to next 500 chars
        dc_parts.append(text[pos:pos+500].lower())
        idx = pos + 16
    dc_text = ' '.join(dc_parts)

    scores = {}
    for mod, terms in MODALITY_KEYWORDS.items():
        score = 0
        for kw in terms:
            dc_hits = dc_text.count(kw)
            all_hits = lower_text.count(kw)
            score += dc_hits * 3 + all_hits
        if score > 0:
            scores[mod] = score

    sorted_mods = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary_mod = sorted_mods[0][0] if sorted_mods and sorted_mods[0][1] >= 3 else None

    return {
        'file': str(file_path),
        'diagram_context_count': dc_count,
        'scores': scores,
        'primary_visual_modality': primary_mod
    }

def main():
    t0 = time.time()
    results = {}
    modality_counts = {}
    total_topics = 0
    with_diagrams = 0

    for root, dirs, files in os.walk(CURRICULUM_DIR):
        for f in sorted(files):
            if f.endswith('.md'):
                total_topics += 1
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, CURRICULUM_DIR)
                parts = rel_path.split(os.sep)
                subject_grade = parts[0]
                topic_name = parts[-1].replace('.md', '')

                analysis = analyze_topic(full_path)
                if analysis['diagram_context_count'] > 0:
                    with_diagrams += 1

                p_mod = analysis['primary_visual_modality']
                if p_mod:
                    modality_counts[p_mod] = modality_counts.get(p_mod, 0) + 1

                if subject_grade not in results:
                    results[subject_grade] = {}
                results[subject_grade][topic_name] = analysis

    output_path = 'curriculum_diagram_catalog.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_topics': total_topics,
            'topics_with_diagram_annotations': with_diagrams,
            'modality_distribution': modality_counts,
            'catalog': results
        }, f, indent=2)

    elapsed = round(time.time() - t0, 2)
    print(f"Scanned {total_topics} topics in {elapsed}s.")
    print(f"Topics with textbook Diagram Contexts: {with_diagrams}")
    print("Modality Needs Detected:")
    for m, c in sorted(modality_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {m}: {c} topics")

if __name__ == '__main__':
    main()
