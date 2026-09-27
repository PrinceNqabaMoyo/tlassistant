"""
Transcribe Official South African CAPS Syllabus PDFs for all Grades & Subjects.
Uses Google Gemini Vision with cascading key failover, persistent page-level disk checkpointing,
and deterministic KaTeX fallback.

Saves output to:
- Primary: caps-ai-backend/curriculum_docs_auto/{Subject}_{Grade}/Syllabus.md
- Mirror:  caps-ai-backend/caps-wiki/{subject}/{grade}/syllabus.md (where matching dir exists)
"""

import os
import re
import sys
import json
import time
import base64
import argparse
import pymupdf
from pathlib import Path

# Import shared quota state, cache manager, and helpers from vision_curriculum_repair
CUR_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CUR_DIR))

from vision_curriculum_repair import (
    CloudQuotaState,
    PageCacheManager,
    load_env_keys,
    call_gemini_vision,
    call_ollama_vision,
    check_internet_connectivity,
    deterministic_text_katex_cleaner,
    BACKEND_DIR,
    CURRICULUM_DOCS_DIR,
    AUTO_ROOT,
    OLLAMA_MODEL,
)

sys.stdout.reconfigure(encoding='utf-8')

SYLLABUS_PROGRESS_FILE = CURRICULUM_DOCS_DIR / "syllabus_progress.json"
SYLLABUS_PAGE_CACHE_DIR = CURRICULUM_DOCS_DIR / ".page_cache_syllabi"
CAPS_WIKI_ROOT = BACKEND_DIR / "caps-wiki"

SYLLABUS_PROMPT = """You are an expert South African CAPS curriculum syllabus and instructional planning specialist.
Analyze this official CAPS syllabus / curriculum page and transcribe its complete educational specifications into clean Markdown:
1. ANNUAL TEACHING PLAN (ATP) & TIMELINES: Detail all terms (Term 1 to Term 4), weekly sequences of topics, recommended teaching hours, and pacing guidelines.
2. CONTENT & COGNITIVE SCOPE: Detail all core concepts, skills to be mastered, cognitive levels (Knowledge, Routine procedures, Complex procedures, Problem solving), and required depth of treatment.
3. ASSESSMENT MATRIX & EXAM WEIGHTINGS: Transcribe all formal and informal assessment requirements, exam mark allocations, Paper 1 vs Paper 2 topic weightings, and weighting percentages.
4. TABLES: Format all annual teaching plans, weighting matrices, or assessment grids as complete, aligned 2D Markdown tables.
5. MATHEMATICS & FORMULAS: All mathematical formulas, symbols, and equations MUST use clean KaTeX notation ($...$, $$...$$).
Output ONLY the clean educational Markdown without introductory or conversational filler."""

TEACHING_SYLLABUS_PROMPT = """You are an expert educator preparing curriculum syllabus reference notes for teachers.
Examine this syllabus page and transcribe its instructional framework in clear Markdown:
1. Extract all term pacing, weekly teaching schedules, topic outlines, and assessment guidance.
2. Format all matrices, schedules, and grids as complete 2D Markdown tables.
3. Use clean KaTeX for all math formulas and equations ($...$).
4. Ignore any publisher footers or copyright notices. Focus purely on curriculum content.
Output ONLY the clean educational Markdown without introductory filler."""

def load_syllabus_progress():
    if SYLLABUS_PROGRESS_FILE.exists():
        try:
            return json.loads(SYLLABUS_PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"completed_files": {}, "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")}

def save_syllabus_progress(rel_key, status="completed", pages_count=0):
    data = load_syllabus_progress()
    data["completed_files"][rel_key] = {
        "status": status,
        "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "pages": pages_count
    }
    data["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    SYLLABUS_PROGRESS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def transcribe_syllabus_page(page, quota_state, requested_provider="auto", delay=3.0):
    pix = page.get_pixmap(dpi=150)
    b64_img = base64.b64encode(pix.tobytes("jpeg")).decode("utf-8")

    # 1. Primary: Google Gemini Vision
    if requested_provider in ["auto", "gemini"] and not quota_state.gemini_exhausted:
        res = call_gemini_vision(b64_img, SYLLABUS_PROMPT, quota_state, delay=delay)
        if res:
            return res

    # 2. Text Reconstruct Fallback via Gemini Text Formatter
    if not quota_state.gemini_exhausted:
        raw_text = page.get_text("text").strip()
        if raw_text and len(raw_text) > 40:
            model = quota_state.current_model
            key = quota_state.current_key
            if model and key:
                import requests
                t_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
                t_prompt = f"You are an expert curriculum formatter. Reconstruct the following CAPS syllabus text into clean structured Markdown with 2D tables and KaTeX math. Ignore publisher imprints. Output ONLY clean Markdown:\n\n{raw_text[:4500]}"
                try:
                    tr = requests.post(t_url, json={"contents": [{"parts": [{"text": t_prompt}]}]}, timeout=25)
                    if tr.status_code == 200:
                        tcand = tr.json().get("candidates", [{}])[0]
                        tparts = (tcand.get("content") or {}).get("parts") or []
                        ttext = "\n".join([p.get("text", "") for p in tparts if isinstance(p, dict) and p.get("text")]).strip()
                        if ttext:
                            return ttext, f"Gemini Text Formatter ({model} - Key {quota_state.active_key_idx + 1})"
                except Exception:
                    pass

    # 3. Local Ollama Vision fallback
    if requested_provider in ["auto", "ollama"]:
        res = call_ollama_vision(pix, SYLLABUS_PROMPT)
        if res:
            return res

    # 4. Deterministic KaTeX Text Reconstruct (Safety net fallback: never drops a page!)
    raw_text = page.get_text("text").strip()
    clean_text = deterministic_text_katex_cleaner(raw_text)
    if clean_text:
        return clean_text, "PyMuPDF KaTeX Cleaned (Deterministic Fallback)"

    return "*(Syllabus page contains layout figures without selectable text)*", "Visual Placeholder"

def normalize_subject_grade(stem):
    """
    Parses 'Syllabus_Accounting_Gr10' -> ('Accounting', 'Gr10', 'Accounting_Gr10')
    Normalizes 'NaturalScience' -> 'NaturalSciences'
    """
    clean = stem.replace("Syllabus_", "")
    parts = clean.split("_")
    if len(parts) >= 2:
        subj = parts[0]
        gr = parts[1]
    else:
        subj = clean
        gr = ""

    # Normalization
    if subj.lower() == "naturalscience":
        subj = "NaturalSciences"

    subj_grade = f"{subj}_{gr}" if gr else subj
    return subj, gr, subj_grade

def find_all_syllabi_targets():
    """Finds all 30 Syllabus_*.pdf files in curriculum_docs directory."""
    all_pdfs = sorted(list(CURRICULUM_DOCS_DIR.glob("Syllabus_*.pdf")))
    targets = []
    for p in all_pdfs:
        subj, gr, subj_gr = normalize_subject_grade(p.stem)
        target_dir = AUTO_ROOT / subj_gr
        target_md = target_dir / "Syllabus.md"

        # Optional wiki mirror path
        # e.g. caps-wiki/mathematics/grade-10/syllabus.md
        gr_num = re.sub(r'^[^\d]*', '', gr)
        subj_slug = re.sub(r'([a-z])([A-Z])', r'\1-\2', subj).lower()
        wiki_md = CAPS_WIKI_ROOT / subj_slug / f"grade-{gr_num}" / "syllabus.md" if gr_num else None

        targets.append({
            "pdf_path": p,
            "subject": subj,
            "grade": gr,
            "subject_grade": subj_gr,
            "target_md": target_md,
            "wiki_md": wiki_md,
            "rel_key": f"{subj_gr}/Syllabus.md"
        })
    return targets

def run_syllabi_pipeline(subject_filter=None, grade_filter=None, delay=3.0, provider="auto", limit_pages=None, dry_run=False, force=False, resume_from=None):
    keys = load_env_keys()
    quota_state = CloudQuotaState(keys)
    progress_data = load_syllabus_progress()
    already_completed = progress_data.get("completed_files", {})
    page_cache = PageCacheManager(cache_dir=SYLLABUS_PAGE_CACHE_DIR)

    all_targets = find_all_syllabi_targets()
    matched = []
    for t in all_targets:
        if subject_filter and subject_filter.lower() not in t["subject"].lower():
            continue
        if grade_filter and grade_filter.lower() not in t["grade"].lower():
            continue
        matched.append(t)

    print("\n========================================================")
    print("      FUNDILE SYLLABI VISION TRANSCRIBER ENGINE         ")
    print("========================================================")
    print(f"Loaded Gemini Keys : {len(keys)} key(s)")
    for i, k in enumerate(keys, 1):
        print(f"                     [{i}] {k[:8]}...{k[-4:]}")
    print(f"Cascading Models   : {len(quota_state.gemini_pool)} models")
    print(f"Local Fallback     : {OLLAMA_MODEL} on port 11434")
    print(f"Syllabus PDFs Found: {len(all_targets)} verified targets")
    print(f"Matched Targets    : {len(matched)} files")
    print(f"Already Completed  : {len(already_completed)} recorded in syllabus_progress.json")
    print(f"Page Disk Cache    : ENABLED (.page_cache_syllabi/)")
    print(f"Dry Run Mode       : {dry_run}\n")

    if dry_run:
        print("--- VERIFIED SYLLABUS TARGETS ---")
        total_pages = 0
        for i, t in enumerate(matched, 1):
            doc = pymupdf.open(str(t["pdf_path"]))
            p_count = len(doc)
            total_pages += p_count
            doc.close()
            is_done = t["rel_key"] in already_completed and already_completed[t["rel_key"]].get("status") == "completed"
            status_str = "[COMPLETED]" if is_done else "[QUEUED]"
            print(f"[{i:02d}/{len(matched):02d}] {status_str} {t['subject_grade']:<28} | Pages: {p_count:3d} | PDF: {t['pdf_path'].name}")
        print(f"\nTotal Pages across {len(matched)} syllabus files: {total_pages} pages.\n")
        return

    completed_in_this_session = 0
    active_resume = False
    start_index = None

    if resume_from:
        if str(resume_from).isdigit():
            start_index = int(resume_from)
            print(f"-> Resuming directly from target index [{start_index}/{len(matched)}]")
        else:
            active_resume = True
            print(f"-> Resuming from target matching: '{resume_from}'")

    try:
        for idx, t in enumerate(matched, 1):
            rel_key = t["rel_key"]

            if start_index and idx < start_index:
                continue

            if active_resume:
                if resume_from.lower() in rel_key.lower():
                    active_resume = False
                    print(f"-> Target matched at [{idx}/{len(matched)}]: {t['subject_grade']}")
                else:
                    continue

            if not force and rel_key in already_completed and already_completed[rel_key].get("status") == "completed":
                print(f"[{idx}/{len(matched)}] [SKIPPED - Already Completed]: {t['subject_grade']} -> Syllabus.md")
                continue

            doc = pymupdf.open(str(t["pdf_path"]))
            num_pages = len(doc)
            pages_to_process = list(range(min(num_pages, limit_pages)) if limit_pages else range(num_pages))

            print(f"[{idx}/{len(matched)}] Processing: {t['subject_grade']} ({num_pages} pages)")
            print(f"    Source PDF: {t['pdf_path'].name}")
            print(f"    Target MD : {t['target_md'].relative_to(BACKEND_DIR)}")

            cached_pages = page_cache.load_cached_pages(rel_key)
            if cached_pages:
                print(f"    -> Restored {len(cached_pages)} page(s) from persistent disk cache.")

            file_interrupted = False

            for p_idx in pages_to_process:
                if p_idx in cached_pages and cached_pages[p_idx]:
                    print(f"    -> Transcribing Page {p_idx + 1}/{len(pages_to_process)}... [CACHED]")
                    continue

                page = doc[p_idx]
                print(f"    -> Transcribing Page {p_idx + 1}/{len(pages_to_process)}...", end="", flush=True)

                try:
                    md_page, prov = transcribe_syllabus_page(page, quota_state, requested_provider=provider, delay=delay)
                except KeyboardInterrupt:
                    print(" [INTERRUPTED]")
                    file_interrupted = True
                    break

                print(f" [OK: {prov}]")
                page_cache.save_page(rel_key, p_idx, md_page)
                cached_pages[p_idx] = md_page

            doc.close()

            if file_interrupted:
                raise KeyboardInterrupt

            final_pages = [cached_pages[i] for i in pages_to_process if i in cached_pages]

            if len(final_pages) == len(pages_to_process):
                # Header with metadata
                header = f"""# {t['subject']} Grade {re.sub(r'^[^\d]*', '', t['grade'])} — Official CAPS Curriculum Syllabus & Pacing Guide

> **Document Type:** Official Department of Basic Education CAPS Curriculum and Assessment Policy Statement (CAPS)
> **Subject:** {t['subject']}
> **Grade:** {t['grade']}
> **Total Pages Transcribed:** {len(final_pages)}
> **Last Verified:** {time.strftime('%Y-%m-%d')}

---

"""
                final_content = header + "\n\n---\n\n".join(final_pages)

                # 1. Write to curriculum_docs_auto/{subject_grade}/Syllabus.md
                t["target_md"].parent.mkdir(parents=True, exist_ok=True)
                with open(t["target_md"], "w", encoding="utf-8") as f:
                    f.write(final_content)
                    f.flush()
                    os.fsync(f.fileno())

                # 2. Mirror to caps-wiki if directory exists
                if t["wiki_md"]:
                    try:
                        t["wiki_md"].parent.mkdir(parents=True, exist_ok=True)
                        with open(t["wiki_md"], "w", encoding="utf-8") as wf:
                            wf.write(final_content)
                            wf.flush()
                            os.fsync(wf.fileno())
                    except Exception:
                        pass

                save_syllabus_progress(rel_key, status="completed", pages_count=len(final_pages))
                page_cache.clear_cache(rel_key)
                completed_in_this_session += 1
                print(f"    [SAVED TO DISK] Successfully transcribed: {t['target_md'].name}\n")
            else:
                print(f"    [SAVED CHECKPOINT] {len(final_pages)}/{len(pages_to_process)} pages cached on disk.\n")

            if quota_state.gemini_exhausted and provider != "ollama":
                print("\n" + "=" * 70)
                print(" [PAUSED] All Gemini cloud quotas have been reached for today.")
                print(" -> All transcribed pages are safely saved in .page_cache_syllabi/")
                print(" -> Google Gemini daily quotas reset at 09:00 AM SAST.")
                print(" -> Simply re-run this command to continue!")
                print("=" * 70 + "\n")
                break

    except KeyboardInterrupt:
        print("\n" + "=" * 70)
        print(" [INTERRUPTED BY USER (Ctrl+C)]")
        print(f" -> {completed_in_this_session} syllabus file(s) completed and saved.")
        print(" -> In-progress pages are safely preserved in .page_cache_syllabi/")
        print(" -> Simply re-run to resume seamlessly!")
        print("=" * 70 + "\n")
        sys.exit(0)

    print("\n" + "=" * 70)
    print(f" [SYLLABI RUN COMPLETE] {completed_in_this_session} syllabus file(s) saved to disk.")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fundile CAPS Syllabi Vision Transcriber")
    parser.add_argument("--subject", help="Filter by subject (e.g. Mathematics, Accounting)")
    parser.add_argument("--grade", help="Filter by grade (e.g. Gr10, Gr7)")
    parser.add_argument("--delay", type=float, default=3.0, help="Delay between cloud API calls in seconds")
    parser.add_argument("--provider", choices=["auto", "gemini", "ollama"], default="auto", help="Model provider")
    parser.add_argument("--limit-pages", type=int, help="Limit number of pages per syllabus (for testing)")
    parser.add_argument("--dry-run", action="store_true", help="Inspect all 30 syllabus PDFs and page counts without calling APIs")
    parser.add_argument("--force", action="store_true", help="Force re-transcription even if marked completed")
    parser.add_argument("--resume-from", help="Resume from target index or name (e.g. 10 or 'Mathematics')")
    args = parser.parse_args()

    run_syllabi_pipeline(
        subject_filter=args.subject,
        grade_filter=args.grade,
        delay=args.delay,
        provider=args.provider,
        limit_pages=args.limit_pages,
        dry_run=args.dry_run,
        force=args.force,
        resume_from=args.resume_from
    )
