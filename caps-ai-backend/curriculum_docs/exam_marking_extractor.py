import os
import re
import glob
import difflib
import pymupdf
from pathlib import Path
from collections import defaultdict

# Global in-memory cache to avoid re-parsing PDFs across topics of the same subject & grade
_EXAM_CACHE = {}

# Official CAPS/NSC Paper Pace standard (minutes per mark)
SUBJECT_PACE_MAP = {
    'mathematics': 1.2,           # 180 min / 150 marks = 1.2 min/mark
    'maths': 1.2,
    'technicalmathematics': 1.2,  # 180 min / 150 marks = 1.2 min/mark
    'techmaths': 1.2,
    'mathematicalliteracy': 1.2,  # 180 min / 150 marks = 1.2 min/mark
    'mathslit': 1.2,
    'physicalsciences': 1.2,      # 180 min / 150 marks = 1.2 min/mark
    'physics': 1.2,
    'chemistry': 1.2,
    'lifesciences': 1.0,          # 150 min / 150 marks = 1.0 min/mark
    'biology': 1.0,
    'accounting': 0.8,            # 120 min / 150 marks = 0.8 min/mark (e.g. 35 marks = 28 min)
    'businessstudies': 0.8,       # 120 min / 150 marks = 0.8 min/mark
    'bs': 0.8,
    'ems': 1.0,                   # 60 min / 60 marks = 1.0 min/mark
    'naturalsciences': 1.0,       # 60 min / 60 marks, 90 min / 80-100 marks = 1.0 min/mark
    'ns': 1.0
}

def normalize_token(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def find_exam_pdfs_for_subject_grade(docs_dir, subject, grade):
    """Locates all exam and memo PDFs corresponding to a given subject and grade."""
    docs_path = Path(docs_dir).resolve()
    gr_num = re.search(r'\d+', grade).group(0) if re.search(r'\d+', grade) else ""

    candidates = []
    # Search root and subdirectories
    all_pdfs = list(docs_path.glob("**/*.pdf"))

    for p in all_pdfs:
        rel = str(p.relative_to(docs_path)).lower()
        fname = p.name.lower()
        
        # Must look like an exam, test, or memo
        if not any(k in fname for k in ['exam', 'test', 'memo', 'qp']):
            continue

        # Must match grade
        if not (f"gr{gr_num}" in fname or f"grade {gr_num}" in rel or f"grade-{gr_num}" in rel or f"gr_{gr_num}" in fname):
            continue

        # Must match subject
        sub_low = subject.lower()
        if sub_low in ['physicalsciences', 'physical science', 'physci']:
            if not any(k in rel or k in fname for k in ['physical', 'phys', 'chem']):
                continue
        elif sub_low in ['businessstudies', 'business studies', 'bs']:
            if not any(k in rel or k in fname for k in ['business', 'bs']):
                continue
        elif sub_low in ['mathematics', 'maths']:
            if any(k in fname for k in ['literacy', 'lit', 'technical', 'tech']):
                continue
            if not any(k in rel or k in fname for k in ['math', 'mathematics']):
                continue
        elif sub_low in ['mathematicalliteracy', 'mathslit', 'maths literacy']:
            if not any(k in rel or k in fname for k in ['literacy', 'lit']):
                continue
        elif sub_low in ['technicalmathematics', 'techmaths']:
            if not any(k in rel or k in fname for k in ['technical', 'techmath']):
                continue
        elif sub_low in ['ems', 'economic']:
            if not ('ems' in rel or 'ems' in fname or 'economic' in rel):
                continue
        elif sub_low in ['naturalsciences', 'natural sciences', 'ns']:
            if not ('ns' in fname or 'natural' in rel):
                continue
        elif sub_low in ['accounting']:
            if not ('accounting' in rel or 'acc' in fname):
                continue
        else:
            if sub_low not in rel and sub_low not in fname:
                continue

        candidates.append(p)

    return sorted(candidates, key=lambda x: x.name)

def extract_questions_from_exam_pdf(pdf_path, subject=None):
    """
    Extracts individual questions, question text, mark allocations, and recommended times
    from an exam PDF using PyMuPDF.
    Returns list of dicts: [{'question_id': 'Q1', 'title': '...', 'text': '...', 'total_marks': 30, 'sub_marks': [...], 'time_minutes': 25, ...}]
    """
    try:
        doc = pymupdf.open(str(pdf_path))
    except Exception:
        return []

    full_pages = []
    for page_num, page in enumerate(doc):
        text = page.get_text("text")
        full_pages.append(text)
    doc.close()

    full_text = "\n".join(full_pages)
    if not full_text.strip():
        return []

    # Identify questions by QUESTION \d+ or SECTION \d+
    chunks = re.split(r'\n(?=(?:QUESTION\s+\d+|SECTION\s+[A-Z]))', full_text, flags=re.IGNORECASE)
    if len(chunks) <= 1:
        # Fallback to numbered questions: e.g. 1. 2. 3.
        chunks = re.split(r'\n(?=\b[1-9]\d?\.\s+[A-Z])', full_text)

    questions = []
    boilerplate_keywords = ["instructions and information", "consists of", "answer all the questions", "copyright reserved", "downloaded from", "senior certificate", "please turn over"]

    for chunk in chunks:
        chunk_clean = chunk.strip()
        if len(chunk_clean) < 60:
            continue

        chunk_low = chunk_clean.lower()
        # Skip exam cover pages and instruction blocks
        if any(bp in chunk_low[:600] for bp in ["instructions and information", "senior certificate", "time: 3 hours", "time: 2 hours", "time: 1 hour", "consists of", "provincial assessment"]):
            continue

        lines = [l.strip() for l in chunk_clean.split('\n') if l.strip()]
        if not lines:
            continue
        header = lines[0]

        # Verify that the chunk starts with an actual question/section header
        if not re.search(r'^(?:QUESTION|SECTION|VRAAG|\b[1-9]\d?\.)', header, re.IGNORECASE):
            if not any(re.search(r'\b(?:QUESTION|SECTION|VRAAG)\s+\d+', l, re.IGNORECASE) for l in lines[:3]):
                continue

        # 1. Detect combined marks and time: e.g. "45 marks; 36 minutes", "(35 marks; 28 minutes)"
        total_mark = None
        time_minutes = None
        time_source = None

        combo_m = re.search(r'(\d+)\s*marks?\s*[\;,\-]\s*(\d+)\s*min', chunk_clean[:300], re.IGNORECASE)
        if combo_m:
            total_mark = int(combo_m.group(1))
            time_minutes = int(combo_m.group(2))
            time_source = "Official Exam Question Specification"
        else:
            # Detect marks: [30], [TOTAL: 25 marks], (50 marks), 45 marks
            mark_m = re.search(r'[\[\(]?(?:TOTAL\s*:?\s*)?(\d+)\s*marks?[\]\)]?', chunk_clean[:300], re.IGNORECASE)
            if mark_m:
                total_mark = int(mark_m.group(1))

            # Detect explicit time: 28 minutes, (25 min), Time: 35 minutes
            time_m = re.search(r'(?:time|t)?\s*[:=-]?\s*(\d+)\s*(?:minutes?|mins?)\b', chunk_clean[:300], re.IGNORECASE)
            if time_m:
                val = int(time_m.group(1))
                if 2 <= val <= 90:
                    time_minutes = val
                    time_source = "Official Exam Question Specification"

        # Detect subquestion marks: (4), (2 x 3 = 6), (1 mark)
        sub_marks = []
        for sm in re.finditer(r'\((\d+)\s*(?:marks?)?\)', chunk_clean, re.IGNORECASE):
            sub_marks.append(int(sm.group(1)))

        # Fallback if no total_mark but submarks exist
        if total_mark is None and sub_marks:
            total_mark = sum(sub_marks)
        elif total_mark is None:
            total_mark = 15

        # Pacing and Time Calibration
        sub_clean = (subject or "").lower().replace(" ", "").replace("_", "")
        default_pace = SUBJECT_PACE_MAP.get(sub_clean, 1.0)

        if time_minutes is None:
            time_minutes = max(3, int(round(total_mark * default_pace)))
            time_source = f"Calibrated to Official CAPS Paper Pace ({default_pace} min/mark)"
            pace_ratio = default_pace
        else:
            pace_ratio = round(time_minutes / total_mark, 2) if total_mark > 0 else default_pace

        checkpoint_min = max(2, int(round(time_minutes * 0.75)))

        questions.append({
            "source_file": os.path.basename(pdf_path),
            "header": header,
            "text": chunk_clean[:1800],  # Keep reasonable snippet
            "total_marks": total_mark,
            "sub_marks": sub_marks,
            "time_minutes": time_minutes,
            "pace_ratio": pace_ratio,
            "time_source": time_source,
            "checkpoint_min": checkpoint_min
        })

    return questions


def load_all_exams_for_subject_grade(docs_dir, subject, grade):
    """Loads and caches all extracted questions for a given subject and grade."""
    cache_key = (subject, grade)
    if cache_key in _EXAM_CACHE:
        return _EXAM_CACHE[cache_key]

    exam_pdfs = find_exam_pdfs_for_subject_grade(docs_dir, subject, grade)
    all_questions = []

    # Limit to parsing first 12 exam PDFs per subject/grade to keep extraction fast
    for pdf_path in exam_pdfs[:12]:
        qs = extract_questions_from_exam_pdf(pdf_path, subject=subject)
        all_questions.extend(qs)

    _EXAM_CACHE[cache_key] = all_questions
    return all_questions

def get_exam_archetypes_for_topic(subject, grade, topic_name, docs_dir, max_questions=3):
    """
    Finds the most relevant authentic exam questions for a given topic,
    along with their exact mark allocations and rubric breakdown.
    Returns: (list_of_question_dicts, formatted_markdown_section)
    """
    all_questions = load_all_exams_for_subject_grade(docs_dir, subject, grade)
    if not all_questions:
        return [], ""

    # Tokenize topic name for fuzzy relevance matching
    clean_topic = topic_name.replace('-', ' ').replace('_', ' ').lower()
    topic_keywords = [w for w in re.split(r'\W+', clean_topic) if len(w) > 3 and w not in ['grade', 'chapter', 'term', 'science', 'mathematics', 'studies']]

    scored_questions = []
    for q in all_questions:
        q_text_low = (q["header"] + " " + q["text"]).lower()
        # Calculate keyword match score
        score = sum(3 for kw in topic_keywords if kw in q_text_low)
        
        # Exact topic phrase boost
        if clean_topic in q_text_low:
            score += 10
            
        if score > 0:
            scored_questions.append((score, q))

    # Sort by relevance score descending
    scored_questions.sort(key=lambda x: x[0], reverse=True)
    selected = [q for score, q in scored_questions[:max_questions]]

    if not selected:
        # Fallback: take questions that contain general markers if specific topic not found
        selected = all_questions[:max_questions]

    # Build formatted Markdown section
    lines = [
        "## 5. Authentic Exam Question Archetypes & Mark Allocations",
        "*(Extracted from official CAPS examination papers to guide marking, pacing, and rubric design)*\n"
    ]

    for idx, q in enumerate(selected, 1):
        clean_header = re.sub(r'\s+', ' ', q['header'])[:60]
        # Format question prompt snippet cleanly
        snippet = q['text'].replace('\n\n', '\n').strip()
        if len(snippet) > 800:
            snippet = snippet[:800] + "..."

        sub_mark_str = f" (Sub-questions: {', '.join(str(m) for m in q['sub_marks'][:5])} marks)" if q['sub_marks'] else ""

        lines.append(f"### Archetype {idx}: {clean_header}")
        lines.append(f"- **Source Paper:** `{q['source_file']}`")
        lines.append(f"- **Total Mark Allocation:** **[{q['total_marks']} Marks]**{sub_mark_str}")
        lines.append(f"- **Recommended Time:** **{q['time_minutes']} Minutes** (Pacing: ~{q['pace_ratio']} min/mark | *{q['time_source']}*)")
        lines.append(f"- **Assessment Mode Calibration:** Timed Exam Simulation: {q['time_minutes']} min countdown (Pacing Checkpoint: {q['checkpoint_min']} min)")
        lines.append(f"- **Cognitive / Marking Strategy:** NSC Standard (Method Marks [M], Accuracy Marks [A], Carry-Over [CA])\n")
        lines.append("#### Question Prompt & Working:")
        lines.append("```text")
        lines.append(snippet)
        lines.append("```\n")

    md_output = "\n".join(lines)
    return selected, md_output

if __name__ == "__main__":
    docs_dir = r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\curriculum_docs"
    print("Testing Exam Marking Extractor on Accounting Gr10 'Salaries'...")
    qs, md = get_exam_archetypes_for_topic("Accounting", "Gr10", "Salaries-and-wages-journal", docs_dir)
    print(f"Extracted {len(qs)} question archetypes.")
    print(md[:500])
