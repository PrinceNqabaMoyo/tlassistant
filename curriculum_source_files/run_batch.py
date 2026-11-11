import os
import sys
import re
import json
import time
import argparse
from pathlib import Path
from collections import defaultdict

# Local pipeline imports
from extract_pdf import extract_pdf_to_markdown
from qwenmd import enrich_markdown_file, strip_pdf_artefacts
from topic_term_map import get_term_and_topic_info, find_existing_manual_file, sanitize_subject_key
from exam_marking_extractor import get_exam_archetypes_for_topic

# Path Configuration
CURRICULUM_DOCS_DIR = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\curriculum_docs").resolve()
OUTPUT_ROOT = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\curriculum_docs_auto").resolve()
MANIFEST_FILE = OUTPUT_ROOT / "batch_progress.json"

# All 9 subjects are enabled
EXCLUDED_SUBJECTS = []

def parse_source_filename(filename):
    """
    Parses Textbook or StudyGuide filenames:
    e.g. Textbook_PhysicalSciences_Gr11_Atomic-combinations.pdf
    e.g. StudyGuide_Accounting_Gr10_Financial-Information-and-GAAP.pdf
    """
    pattern = r'^(Textbook|StudyGuide)_([A-Za-z]+)_(Gr\d+)_+(.+)\.pdf$'
    match = re.match(pattern, filename, re.IGNORECASE)
    if not match:
        return None

    return {
        "doc_type": match.group(1),
        "subject": sanitize_subject_key(match.group(2)),
        "grade": match.group(3),
        "topic_raw": match.group(4),
        "filename": filename
    }

def load_manifest():
    if MANIFEST_FILE.exists():
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"jobs": {}, "stats": {"total": 0, "completed": 0, "failed": 0}}

def save_manifest(manifest):
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

def discover_jobs(subject_filter=None, grade_filter=None, limit=None):
    """
    Scans for Textbook and StudyGuide PDFs across all 9 subjects.
    Merges matching Textbook and StudyGuide pairs for the same topic.
    Sorts strictly by (Subject, Grade, Term Number, Topic Position).
    """
    all_source_pdfs = list(CURRICULUM_DOCS_DIR.glob("Textbook_*.pdf")) + list(CURRICULUM_DOCS_DIR.glob("StudyGuide_*.pdf"))
    
    # Track by topic key to merge Textbook + StudyGuide pairs
    topics_map = defaultdict(dict)

    for pdf_path in all_source_pdfs:
        parsed = parse_source_filename(pdf_path.name)
        if not parsed:
            continue

        subject = parsed["subject"]
        grade = parsed["grade"]
        topic_raw = parsed["topic_raw"]

        if subject in EXCLUDED_SUBJECTS:
            continue

        if subject_filter:
            allowed_subjs = [s.strip().lower() for s in subject_filter.split(',') if s.strip()]
            if not any(s in subject.lower() for s in allowed_subjs):
                continue

        if grade_filter and grade_filter.lower() != grade.lower():
            continue

        norm_topic_key = (subject, grade, re.sub(r'[^a-zA-Z0-9]', '', topic_raw).lower())

        if parsed["doc_type"].lower() == "textbook":
            topics_map[norm_topic_key]["textbook"] = pdf_path
        else:
            topics_map[norm_topic_key]["studyguide"] = pdf_path

        topics_map[norm_topic_key]["subject"] = subject
        topics_map[norm_topic_key]["grade"] = grade
        topics_map[norm_topic_key]["topic_raw"] = topic_raw
        topics_map[norm_topic_key]["ref_filename"] = pdf_path.name

    all_jobs = []
    for (subj, gr, _), data in topics_map.items():
        topic_info = get_term_and_topic_info(subj, gr, data["ref_filename"], CURRICULUM_DOCS_DIR)

        term = topic_info["term"]
        formatted_filename = topic_info["formatted_filename"]
        syllabus_context = topic_info["syllabus_context"]

        folder_name = f"{subj}_{gr}"
        target_dir = OUTPUT_ROOT / folder_name / term
        target_file = target_dir / formatted_filename
        job_id = f"{subj}_{gr}_{term}_{data['topic_raw']}"

        # Check if an existing manual markdown file exists in original directories
        manual_file = find_existing_manual_file(CURRICULUM_DOCS_DIR, subj, gr, data["topic_raw"])

        # Primary PDF is textbook if available, else study guide
        primary_pdf = data.get("textbook") or data.get("studyguide")
        supplementary_sg = data.get("studyguide") if data.get("textbook") else None

        all_jobs.append({
            "job_id": job_id,
            "subject": subj,
            "grade": gr,
            "term": term,
            "pos": topic_info["pos"],
            "pos_str": topic_info["pos_str"],
            "clean_topic": topic_info["clean_topic"],
            "formatted_filename": formatted_filename,
            "syllabus_context": syllabus_context,
            "primary_pdf": str(primary_pdf),
            "studyguide_pdf": str(supplementary_sg) if supplementary_sg else None,
            "manual_file": str(manual_file) if manual_file else None,
            "target_dir": str(target_dir),
            "target_file": str(target_file)
        })

    # Group jobs by (subject, grade)
    grouped = defaultdict(list)
    for job in all_jobs:
        key = (job["subject"], job["grade"])
        grouped[key].append(job)

    def term_sort_key(job):
        term_num = int(re.search(r'\d+', job["term"]).group(0)) if re.search(r'\d+', job["term"]) else 1
        return (term_num, job["pos"], job["clean_topic"])

    final_jobs = []
    for key, group_jobs in grouped.items():
        group_jobs.sort(key=term_sort_key)
        if limit and limit > 0:
            group_jobs = group_jobs[:limit]
        final_jobs.extend(group_jobs)

    # Sort globally by (subject, grade, term, pos)
    final_jobs.sort(key=lambda j: (
        j["subject"],
        j["grade"],
        int(re.search(r'\d+', j["term"]).group(0)) if re.search(r'\d+', j["term"]) else 1,
        j["pos"]
    ))
    return final_jobs

def run_batch(dry_run=False, subject_filter=None, grade_filter=None, force=False, limit=None, skip_manual=True, include_exams=True, skip_vision=False):
    jobs = discover_jobs(subject_filter, grade_filter, limit=limit)
    manifest = load_manifest()

    print("\n==================================================")
    print("      FUNDILE CURRICULUM DOC BATCH PIPELINE       ")
    print("==================================================")
    print(f"Source Directory: {CURRICULUM_DOCS_DIR}")
    print(f"Output Directory: {OUTPUT_ROOT}")
    print(f"Discovered Jobs : {len(jobs)}" + (f" (Limit {limit} per subject/grade)" if limit else ""))
    print(f"Skip Manual Mode: {skip_manual}")
    print(f"Include Exams   : {include_exams}")
    print("==================================================\n")

    if dry_run:
        print("[DRY RUN MODE] The following ordered jobs would be executed:\n")
        for i, job in enumerate(jobs, 1):
            manual_tag = f" [MANUAL AVAILABLE: {os.path.basename(job['manual_file'])}]" if job["manual_file"] else " [NEW EXTRACTION]"
            sg_tag = f" (+StudyGuide: {os.path.basename(job['studyguide_pdf'])})" if job["studyguide_pdf"] else ""
            print(f"{i:03d}. [{job['subject']} {job['grade']}] {job['term']} -> {job['formatted_filename']}{manual_tag}")
            print(f"     Primary: {os.path.basename(job['primary_pdf'])}{sg_tag}")
            print(f"     Target : {job['target_file']}\n")
        print("Dry run complete. No files were written.")
        return

    processed_count = 0
    skipped_manual_count = 0
    failed_count = 0

    for i, job in enumerate(jobs, 1):
        job_id = job["job_id"]
        target_file = Path(job["target_file"])
        target_dir = Path(job["target_dir"])
        target_dir.mkdir(parents=True, exist_ok=True)

        # Skip if already completed in full production run (re-process if it was only a trial sample)
        job_meta = manifest["jobs"].get(job_id, {})
        is_completed = (job_meta.get("status") == "completed")
        was_trial_sample = job_meta.get("sample", False)

        if not force and is_completed and not was_trial_sample and target_file.exists():
            print(f"[{i}/{len(jobs)}] [SKIPPED] Already completed: {job['formatted_filename']}")
            continue

        if was_trial_sample:
            print(f"-> Upgrading previous trial sample to full production: {job['formatted_filename']}")


        print(f"\n[{i}/{len(jobs)}] Processing: {job['subject']} {job['grade']} - {job['formatted_filename']}")

        manifest["jobs"][job_id] = {
            "status": "in_progress",
            "start_time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        save_manifest(manifest)

        # -------------------------------------------------------------
        # CASE 1: Existing manual file found and skip_manual is enabled
        # -------------------------------------------------------------
        if skip_manual and job["manual_file"] and os.path.exists(job["manual_file"]):
            manual_src = Path(job["manual_file"])
            print(f"-> [MANUAL FILE FOUND] Preserving: {manual_src.name}")
            try:
                with open(manual_src, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Enrich with exam question archetypes and mark allocations if enabled
                if include_exams:
                    print(f"   * Extracting exam mark allocations for topic: {job['clean_topic']}...")
                    _, exam_md = get_exam_archetypes_for_topic(
                        subject=job["subject"],
                        grade=job["grade"],
                        topic_name=job["clean_topic"],
                        docs_dir=CURRICULUM_DOCS_DIR,
                        max_questions=3
                    )
                    if exam_md and "## 5. Authentic Exam Question Archetypes" not in content:
                        content += f"\n\n{exam_md.strip()}\n"

                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(content)

                manifest["jobs"][job_id] = {
                    "status": "completed",
                    "sample": False,
                    "source": "manual_preserved",
                    "manual_file": str(manual_src),
                    "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "output_file": str(target_file)
                }
                save_manifest(manifest)
                skipped_manual_count += 1
                processed_count += 1
                print(f"-> COMPLETE: Preserved manual notes with exam mark schemes -> {target_file.name}\n")
                continue

            except Exception as e:
                print(f"[WARN] Failed to preserve manual file ({e}), falling back to PDF extraction...")

        # -------------------------------------------------------------
        # CASE 2: Full automated extraction from PDF (Textbook/StudyGuide)
        # -------------------------------------------------------------
        print(f"-> [FULL EXTRACTION] Source PDF: {os.path.basename(job['primary_pdf'])}")
        prefix = f"{job['pos_str']}_{re.sub(r'[^a-zA-Z0-9]', '_', job['clean_topic'])}"

        try:
            # Stage 1: Extract primary PDF to Markdown + crop visual tables and diagrams
            raw_md_path = extract_pdf_to_markdown(
                pdf_path=job["primary_pdf"],
                term_dir=target_dir,
                file_prefix=prefix,
                target_pages=None,
                crop_tables=True,
                save_full_renders=False
            )

            # Stage 2: Extract supplementary Study Guide procedural notes if available
            study_guide_md = None
            if job["studyguide_pdf"] and os.path.exists(job["studyguide_pdf"]):
                print(f"   * Ingesting supplementary Study Guide: {os.path.basename(job['studyguide_pdf'])}")
                sg_raw_path = extract_pdf_to_markdown(
                    pdf_path=job["studyguide_pdf"],
                    term_dir=target_dir,
                    file_prefix=f"{prefix}_sg",
                    crop_tables=True,
                    save_full_renders=False
                )
                if os.path.exists(sg_raw_path):
                    with open(sg_raw_path, "r", encoding="utf-8", errors="ignore") as sg_f:
                        study_guide_md = strip_pdf_artefacts(sg_f.read())
                    try:
                        os.remove(sg_raw_path)
                    except Exception:
                        pass

            # Stage 3: Extract exam archetypes and mark allocations
            exam_md = None
            if include_exams:
                print(f"   * Parsing exam question archetypes and mark allocations...")
                _, exam_md = get_exam_archetypes_for_topic(
                    subject=job["subject"],
                    grade=job["grade"],
                    topic_name=job["clean_topic"],
                    docs_dir=CURRICULUM_DOCS_DIR,
                    max_questions=3
                )

            # Stage 4: Enrich with Qwen Vision (or clean fallback if skip_vision), LaTeX fixes, and combined streams
            enrich_markdown_file(
                raw_md_path=raw_md_path,
                final_md_path=target_file,
                topic_hint=job["syllabus_context"],
                exam_archetypes_md=exam_md,
                study_guide_md=study_guide_md,
                skip_vision=skip_vision
            )

            manifest["jobs"][job_id] = {
                "status": "completed",
                "sample": False,
                "source": "pdf_extracted",
                "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "output_file": str(target_file)
            }
            save_manifest(manifest)
            processed_count += 1

        except KeyboardInterrupt:
            print("\n\n" + "="*56)
            print("  [CANCELLED] Batch run interrupted by user (Ctrl+C).")
            print(f"  Processed so far : {processed_count} completed")
            print("  Progress has been safely saved to batch_progress.json.")
            print("  You can resume anytime by running python run_batch.py.")
            print("="*56 + "\n")
            try:
                if target_file.exists() and manifest["jobs"].get(job_id, {}).get("status") != "completed":
                    target_file.unlink(missing_ok=True)
            except Exception:
                pass
            sys.exit(0)

        except Exception as e:
            print(f"[ERROR] Job failed: {job_id} -> {e}")
            manifest["jobs"][job_id] = {
                "status": "failed",
                "failed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "error": str(e)
            }
            save_manifest(manifest)
            failed_count += 1

    print("\n==================================================")
    print("             BATCH PIPELINE COMPLETE              ")
    print(f" Total Processed  : {processed_count}")
    print(f" Manual Preserved : {skipped_manual_count}")
    print(f" Failed           : {failed_count}")
    print(f" Manifest Log     : {MANIFEST_FILE}")
    print("==================================================\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Curriculum Doc Batch Generator")
    parser.add_argument("--dry-run", action="store_true", help="Preview discovered jobs without running")
    parser.add_argument("--subject", type=str, help="Filter by subject name (e.g. Accounting, Mathematics, PhysicalSciences)")
    parser.add_argument("--grade", type=str, help="Filter by grade (e.g. Gr10, Gr11)")
    parser.add_argument("--limit", "-n", type=int, default=None, help="Limit number of topics per subject/grade (e.g. --limit 2)")
    parser.add_argument("--force", action="store_true", help="Re-run already completed jobs")
    parser.add_argument("--no-skip-manual", action="store_true", help="Do not skip manual files, re-extract everything from PDF")
    parser.add_argument("--no-exams", action="store_true", help="Skip extracting exam mark allocations")
    parser.add_argument("--skip-vision", "--fast", action="store_true", help="Fast mode: skip local Ollama vision descriptions while Windows update or high CPU load is active")
    args = parser.parse_args()

    run_batch(
        dry_run=args.dry_run,
        subject_filter=args.subject,
        grade_filter=args.grade,
        force=args.force,
        limit=args.limit,
        skip_manual=not args.no_skip_manual,
        include_exams=not args.no_exams,
        skip_vision=args.skip_vision
    )