import os
import sys
import re
import json
import time
import argparse
from pathlib import Path
from collections import defaultdict

# Import pipeline engines
from run_batch import discover_jobs, load_manifest, save_manifest, OUTPUT_ROOT, CURRICULUM_DOCS_DIR
from extract_pdf import extract_pdf_to_markdown
from qwenmd import enrich_markdown_file, strip_pdf_artefacts
from exam_marking_extractor import get_exam_archetypes_for_topic

def select_representative_samples(subject_filter=None, grade_filter=None, samples_per_group=2):
    """
    Selects balanced samples for each (Subject, Grade) group:
    - Prioritizes 1 topic with existing manual notes (to test preservation & mark enrichment)
    - Prioritizes 1 topic with NO manual notes (to test clean automated PDF extraction)
    """
    all_jobs = discover_jobs(subject_filter=subject_filter, grade_filter=grade_filter, limit=None)
    grouped = defaultdict(list)
    for job in all_jobs:
        grouped[(job["subject"], job["grade"])].append(job)

    sampled_jobs = []
    for (subj, gr), jobs in sorted(grouped.items()):
        manual_candidates = [j for j in jobs if j["manual_file"]]
        new_candidates = [j for j in jobs if not j["manual_file"]]

        chosen = []
        # Pick 1 manual preservation sample if available
        if manual_candidates:
            chosen.append(manual_candidates[0])

        # Pick 1 new PDF extraction sample if available
        if new_candidates:
            chosen.append(new_candidates[0])

        # If either was missing, fill up to samples_per_group from the other
        for j in jobs:
            if len(chosen) >= samples_per_group:
                break
            if j not in chosen:
                chosen.append(j)

        sampled_jobs.extend(chosen)

    return sampled_jobs

def run_sampling(subject_filter=None, grade_filter=None, skip_vision=True, force=False):
    samples = select_representative_samples(subject_filter, grade_filter)

    print("\n========================================================")
    print("      FUNDILE CURRICULUM DOC PIPELINE - SAMPLING RUN    ")
    print("========================================================")
    print(f"Total Sample Jobs Selected : {len(samples)}")
    print(f"Vision Processing (Ollama) : {'Disabled (Fast Mode)' if skip_vision else 'Enabled'}")
    print(f"Target Output Directory    : {OUTPUT_ROOT}")
    print("========================================================\n")

    manifest = load_manifest()
    processed = 0
    preserved = 0
    failed = 0

    for i, job in enumerate(samples, 1):
        target_file = Path(job["target_file"])
        target_dir = Path(job["target_dir"])
        target_dir.mkdir(parents=True, exist_ok=True)
        job_id = job["job_id"]

        is_manual = bool(job["manual_file"] and os.path.exists(job["manual_file"]))
        mode_label = "MANUAL PRESERVED + EXAM MARKS" if is_manual else "NEW PDF EXTRACTION + EXAM MARKS"

        print(f"[{i}/{len(samples)}] Sample: {job['subject']} {job['grade']} - {job['clean_topic']}")
        print(f"     Mode   : {mode_label}")
        print(f"     Target : {target_file.relative_to(OUTPUT_ROOT)}")

        # Skip if already completed and not force
        if not force and manifest["jobs"].get(job_id, {}).get("status") == "completed" and target_file.exists():
            print(f"     Status : Already completed (skipping)\n")
            continue

        try:
            if is_manual:
                # Case 1: Manual preservation + Exam mark scheme enrichment
                with open(job["manual_file"], "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

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

                preserved += 1

            else:
                # Case 2: Full automated PDF extraction
                prefix = f"{job['pos_str']}_{re.sub(r'[^a-zA-Z0-9]', '_', job['clean_topic'])}"
                raw_md_path = extract_pdf_to_markdown(
                    pdf_path=job["primary_pdf"],
                    term_dir=target_dir,
                    file_prefix=prefix,
                    target_pages=None,
                    crop_tables=True,
                    save_full_renders=False
                )

                # Supplementary Study Guide if present
                study_guide_md = None
                if job["studyguide_pdf"] and os.path.exists(job["studyguide_pdf"]):
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

                # Authentic exam mark allocations
                _, exam_md = get_exam_archetypes_for_topic(
                    subject=job["subject"],
                    grade=job["grade"],
                    topic_name=job["clean_topic"],
                    docs_dir=CURRICULUM_DOCS_DIR,
                    max_questions=3
                )

                # Enrich with formulas, tables, and exam section
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
                "sample": True,
                "source": "manual_preserved" if is_manual else "pdf_extracted",
                "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "output_file": str(target_file)
            }
            save_manifest(manifest)
            processed += 1
            print(f"     Status : SUCCESS -> Written {target_file.name}\n")

        except KeyboardInterrupt:
            print("\n\n" + "="*56)
            print("  [CANCELLED] Sampling run interrupted by user (Ctrl+C).")
            print(f"  Processed so far : {processed} completed")
            print("  Progress has been safely saved to batch_progress.json.")
            print("  You can resume anytime by re-running run_sampling.py.")
            print("="*56 + "\n")
            # Clean up partial target file if incomplete
            try:
                if target_file.exists() and manifest["jobs"].get(job_id, {}).get("status") != "completed":
                    target_file.unlink(missing_ok=True)
            except Exception:
                pass
            sys.exit(0)

        except Exception as e:
            print(f"     [ERROR] Failed to process sample: {e}\n")
            failed += 1

    print("========================================================")
    print("                 SAMPLING RUN COMPLETE                  ")
    print(f" Total Processed  : {processed}")
    print(f" Manual Preserved : {preserved}")
    print(f" Failed           : {failed}")
    print("========================================================\n")
    print(f"Inspect the generated samples in:\n  {OUTPUT_ROOT}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run representative sample extraction for review")
    parser.add_argument("--subject", type=str, help="Filter by subject (e.g. PhysicalSciences, Mathematics, Accounting)")
    parser.add_argument("--grade", type=str, help="Filter by grade (e.g. Gr10, Gr11)")
    parser.add_argument("--no-vision", action="store_true", help="Disable Ollama vision descriptions (runs fast text-only)")
    parser.add_argument("--force", action="store_true", help="Re-extract even if sample file already exists")
    args = parser.parse_args()

    run_sampling(
        subject_filter=args.subject,
        grade_filter=args.grade,
        skip_vision=args.no_vision,
        force=args.force
    )

