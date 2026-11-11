#!/usr/bin/env python3
"""
Semantic Relevance Gate & Curriculum Topic Vocabulary Extractor.

Extracts authoritative domain vocabulary (headings, keywords, n-grams) from all 476
curriculum markdown files in curriculum_docs_auto/ and verifies that generated questions
and BKT dossiers strictly ground in their intended subject, grade, and topic.
"""

import os
import re
import json
import glob
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any

ROOT_DIR = Path(__file__).resolve().parent.parent
CURRICULUM_DOCS_DIR = ROOT_DIR / "curriculum_docs_auto"
OUTPUT_VOCAB_PATH = ROOT_DIR / "caps-ai-backend" / "app" / "services" / "curriculum_topic_vocabulary.json"

STOPWORDS = {
    "about", "above", "after", "again", "against", "all", "also", "among", "and", "another",
    "any", "are", "aren't", "because", "been", "before", "being", "below", "between", "both",
    "but", "cannot", "could", "couldn't", "did", "didn't", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't",
    "have", "haven't", "having", "here", "how", "into", "itself", "more", "most", "must",
    "mustn't", "myself", "nor", "not", "only", "other", "ought", "our", "ours", "ourselves",
    "out", "over", "own", "same", "shan't", "she", "should", "shouldn't", "some", "such",
    "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "these",
    "they", "this", "those", "through", "too", "under", "until", "very", "was", "wasn't",
    "we", "were", "weren't", "what", "when", "where", "which", "while", "who", "whom", "why",
    "with", "won't", "would", "wouldn't", "you", "your", "yours", "yourself", "yourselves",
    "page", "term", "week", "grade", "topic", "unit", "chapter", "activity", "exercise",
    "question", "answer", "marks", "total", "hours", "time", "date", "name", "study", "notes",
    "caps", "curriculum", "content", "overview", "introduction", "summary", "conclusion",
    "learner", "teacher", "guidelines", "assessment", "exam", "examination", "test", "paper"
}

TRACK_SUBJECT_MAP = {
    "accounting": "Accounting",
    "businessstudies": "Business Studies",
    "ems": "Economic and Management Sciences",
    "lifesciences": "Life Sciences",
    "mathematicalliteracy": "Mathematical Literacy",
    "mathematics": "Mathematics",
    "naturalsciences": "Natural Sciences",
    "physicalsciences": "Physical Sciences",
    "technicalmathematics": "Technical Mathematics",
}

SUBJECT_EXCLUSIVE_MARKERS: Dict[str, Set[str]] = {
    "Accounting": {
        "ledger", "debit", "credit", "trial balance", "gaap", "debtor", "creditor",
        "depreciation", "tangible asset", "bank recon", "balance sheet", "income statement",
        "contra account", "cash receipts journal", "cash payments journal", "sole trader"
    },
    "Physical Sciences": {
        "projectile", "acceleration", "doppler", "photoelectric", "stoichiometry",
        "momentum", "impulse", "velocity", "vector", "coulomb", "ohm", "resistor",
        "titration", "organic chemistry", "alkane", "alkene", "ester", "intermolecular"
    },
    "Life Sciences": {
        "mitosis", "meiosis", "photosynthesis", "chloroplast", "mitochondria",
        "organelle", "cytoplasm", "dna", "rna", "chromosome", "allele", "gamete",
        "nephron", "homeostasis", "endocrine", "hormone", "biodiversity"
    },
    "Business Studies": {
        "entrepreneur", "macro environment", "micro environment", "market environment",
        "human resources", "recruitment", "induction", "bcea", "eea", "swot",
        "business venture", "code of ethics", "creative thinking"
    },
    "Economic and Management Sciences": {
        "needs and wants", "producers and consumers", "factors of production",
        "economic systems", "goods and services"
    },
    "Technical Mathematics": {
        "complex number", "argand", "binomial theorem", "integration", "differential calculus",
        "radian", "circle geometry", "tangent", "secant", "mensuration"
    },
    "Mathematical Literacy": {
        "tariff", "tax bracket", "paye", "uif", "water tariff", "electricity tariff",
        "bar scale", "elevation plan", "floor plan", "till slip"
    },
}


def clean_topic_name(filename: str) -> str:
    name = Path(filename).stem
    name = re.sub(r"^\d+[\.\s_-]+", "", name)
    return name.strip()


def normalize_token(w: str) -> str:
    return re.sub(r"[^\w]", "", w.lower()).strip()


def extract_vocabulary_from_text(text: str, topic_name: str) -> Dict[str, Any]:
    lines = text.split("\n")
    headings = []
    content_tokens = []
    
    # Extract headings
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("#"):
            h = re.sub(r"^#+\s*", "", line_s)
            if len(h) >= 3 and not any(h.lower().startswith(skip) for skip in ["grade", "term", "week", "topic", "contents", "table of contents"]):
                headings.append(h)
    
    # Clean and tokenize
    raw_words = re.findall(r"\b[A-Za-z][A-Za-z0-9_-]{2,}\b", text.lower())
    filtered_words = [normalize_token(w) for w in raw_words if normalize_token(w) not in STOPWORDS and len(normalize_token(w)) >= 4]
    
    word_counts = Counter(filtered_words)
    
    # Extract 2-word phrases
    bigrams = []
    for i in range(len(filtered_words) - 1):
        w1, w2 = filtered_words[i], filtered_words[i+1]
        if w1 != w2:
            bigrams.append(f"{w1} {w2}")
    bigram_counts = Counter(bigrams)
    
    # Combine top single words, top bigrams, and heading phrases
    top_words = [w for w, _ in word_counts.most_common(30)]
    top_bigrams = [bg for bg, count in bigram_counts.most_common(15) if count >= 2]
    
    # Include words from topic name itself
    topic_name_tokens = [normalize_token(w) for w in re.findall(r"\b[A-Za-z]+\b", topic_name.lower()) if normalize_token(w) not in STOPWORDS]
    
    all_keywords = list(dict.fromkeys(topic_name_tokens + top_words[:20] + top_bigrams[:10]))
    
    return {
        "headings": headings[:15],
        "keywords": all_keywords[:35],
    }


def build_full_vocabulary_manifest() -> Dict[str, Any]:
    """Scans all 476 topics in curriculum_docs_auto/ and builds vocabulary manifest."""
    files = glob.glob(str(CURRICULUM_DOCS_DIR / "*" / "*" / "*.md"))
    topic_files = [f for f in files if not f.endswith("Syllabus.md")]
    
    print(f"Extracting vocabulary from {len(topic_files)} curriculum markdown files...")
    
    vocab_manifest: Dict[str, Any] = {}
    
    for fpath in topic_files:
        p = Path(fpath)
        track_folder = p.parent.parent.name # e.g. BusinessStudies_Gr11
        term_folder = p.parent.name # e.g. Term 1
        
        m = re.match(r"([A-Za-z]+)_Gr(\d+)", track_folder)
        if not m:
            continue
        subj_raw, grade = m.group(1).lower(), m.group(2)
        subject = TRACK_SUBJECT_MAP.get(subj_raw, subj_raw.title())
        
        topic_name = clean_topic_name(p.name)
        term_num = int(re.sub(r"[^\d]", "", term_folder) or "1")
        
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            continue
            
        extracted = extract_vocabulary_from_text(content, topic_name)
        
        key = f"{subject}::Gr{grade}::T{term_num}::{topic_name}"
        vocab_manifest[key] = {
            "subject": subject,
            "grade": grade,
            "term": term_num,
            "topic": topic_name,
            "headings": extracted["headings"],
            "keywords": extracted["keywords"],
        }
        
    print(f"Extracted vocabulary for {len(vocab_manifest)} curriculum topics.")
    
    # Save to disk
    OUTPUT_VOCAB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_VOCAB_PATH, "w", encoding="utf-8") as f:
        json.dump(vocab_manifest, f, indent=2)
    print(f"Saved vocabulary manifest to: {OUTPUT_VOCAB_PATH}")
    
    return vocab_manifest


def verify_text_relevance(
    text: str,
    subject: str,
    grade: str,
    topic: str,
    vocab_manifest: Dict[str, Any]
) -> Dict[str, Any]:
    """Verifies that text matches topic vocabulary and does not leak cross-subject markers."""
    text_clean = text.lower()
    
    # Find matching topic entry in vocab_manifest
    matching_entry = None
    for k, v in vocab_manifest.items():
        if v["subject"].lower() == subject.lower() and str(v["grade"]) == str(grade):
            t_clean = re.sub(r"[^\w]", "", v["topic"].lower())
            req_t_clean = re.sub(r"[^\w]", "", topic.lower())
            if t_clean in req_t_clean or req_t_clean in t_clean:
                matching_entry = v
                break
                
    keywords = matching_entry["keywords"] if matching_entry else []
    # If not found by exact fuzzy, use words from topic itself
    if not keywords:
        keywords = [normalize_token(w) for w in re.findall(r"\b[A-Za-z]+\b", topic.lower()) if normalize_token(w) not in STOPWORDS]
        
    matched_keywords = [kw for kw in keywords if kw in text_clean]
    
    # Check cross-subject leaks
    cross_subject_leaks = []
    for other_subj, markers in SUBJECT_EXCLUSIVE_MARKERS.items():
        if other_subj.lower() == subject.lower():
            continue
        # Check if 2 or more distinct exclusive markers of other subject appear
        hits = [m for m in markers if m in text_clean]
        if len(hits) >= 2:
            cross_subject_leaks.append({"subject": other_subj, "markers": hits})
            
    is_relevant = len(matched_keywords) > 0 and len(cross_subject_leaks) == 0
    
    return {
        "is_relevant": is_relevant,
        "matched_keywords_count": len(matched_keywords),
        "matched_keywords": matched_keywords[:5],
        "cross_subject_leaks": cross_subject_leaks,
        "topic": topic,
        "subject": subject,
    }


if __name__ == "__main__":
    manifest = build_full_vocabulary_manifest()
    
    # Quick sanity check on known topics
    sample1 = verify_text_relevance(
        "Calculate the gross wage for the employee under the Basic Conditions of Employment Act (BCEA) induction period.",
        "Business Studies", "11", "Introduction to the human resources function", manifest
    )
    print("\nSanity Check 1 (BS Gr11 HR):", sample1)
    
    sample2 = verify_text_relevance(
        "A 5 kg block moves with velocity 4 m/s. Calculate momentum using p = mv.",
        "Physical Sciences", "10", "Motion in one dimension", manifest
    )
    print("Sanity Check 2 (PS Gr10 Motion):", sample2)
