import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from PIL import Image

AUTO_ROOT = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\curriculum_docs_auto").resolve()

def analyze_curriculum_images():
    print("=" * 80)
    print("       FUNDILE CURRICULUM DIAGRAMS AUDIT & VERIFICATION REPORT")
    print("=" * 80)
    print(f"Scanning Root: {AUTO_ROOT}\n")

    stats = defaultdict(lambda: {
        "disk_images": set(),
        "md_referenced": set(),
        "annotated": set(),
        "unannotated_in_md": set(),
        "filtered_size": set(),
        "filtered_dim": set(),
        "eligible_unannotated": set(),
        "orphan_on_disk": set(),
        "md_files_count": 0,
        "md_files_with_images": 0
    })

    # Step 1: Scan all images on disk
    all_disk_images_by_dir = defaultdict(set)
    total_disk_images = 0
    for img_path in AUTO_ROOT.glob("**/images/*.*"):
        if img_path.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
            total_disk_images += 1
            rel = img_path.relative_to(AUTO_ROOT)
            subj_gr = rel.parts[0]
            subj = subj_gr.split("_")[0] if "_" in subj_gr else subj_gr
            stats[subj]["disk_images"].add(img_path)
            all_disk_images_by_dir[img_path.parent.resolve()].add(img_path.name)

    # Step 2: Scan all markdown files
    md_files = list(AUTO_ROOT.glob("**/*.md"))
    image_pattern = re.compile(r'!\[(.*?)\]\((images/[^)]+)\)')

    for md_file in md_files:
        rel = md_file.relative_to(AUTO_ROOT)
        subj_gr = rel.parts[0]
        subj = subj_gr.split("_")[0] if "_" in subj_gr else subj_gr
        stats[subj]["md_files_count"] += 1

        try:
            content = md_file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        matches = image_pattern.findall(content)
        if matches:
            stats[subj]["md_files_with_images"] += 1

        images_dir = (md_file.parent / "images").resolve()

        for alt, rel_path in matches:
            img_name = os.path.basename(rel_path)
            stats[subj]["md_referenced"].add((str(md_file), img_name))

            full_img_path = images_dir / img_name
            is_annotated = f"[Diagram Context - {img_name}]" in content

            if is_annotated:
                stats[subj]["annotated"].add((str(md_file), img_name))
            else:
                stats[subj]["unannotated_in_md"].add((str(md_file), img_name))

                # Check why it wasn't annotated
                if full_img_path.exists():
                    fsize = full_img_path.stat().st_size
                    if fsize < 4096:
                        stats[subj]["filtered_size"].add(img_name)
                    else:
                        try:
                            with Image.open(full_img_path) as im:
                                w, h = im.size
                                if (w < 60 and h < 60) or min(w, h) < 35 or (w * h) < 8000:
                                    stats[subj]["filtered_dim"].add(img_name)
                                else:
                                    stats[subj]["eligible_unannotated"].add((str(md_file), img_name, fsize, w, h))
                        except Exception:
                            stats[subj]["filtered_dim"].add(img_name)

    # Step 3: Find orphan images on disk (images that exist in images/ folder but are never referenced in md)
    all_referenced_names_by_dir = defaultdict(set)
    for subj, data in stats.items():
        for md_path_str, img_name in data["md_referenced"]:
            p = Path(md_path_str).parent / "images"
            all_referenced_names_by_dir[p.resolve()].add(img_name)

    for subj, data in stats.items():
        for img_path in data["disk_images"]:
            dir_res = img_path.parent.resolve()
            if img_path.name not in all_referenced_names_by_dir[dir_res]:
                data["orphan_on_disk"].add(img_path)

    # Print summary table
    print(f"{'Subject':<22} | {'Disk Imgs':<9} | {'MD Refs':<8} | {'Annotated':<9} | {'Eligible Left':<13} | {'Filtered':<10} | {'Orphans':<8}")
    print("-" * 92)

    total_disk = 0
    total_refs = 0
    total_annotated = 0
    total_eligible = 0
    total_filtered = 0
    total_orphans = 0

    for subj in sorted(stats.keys()):
        d = stats[subj]
        num_disk = len(d["disk_images"])
        num_refs = len(d["md_referenced"])
        num_annot = len(d["annotated"])
        num_eligible = len(d["eligible_unannotated"])
        num_filtered = len(d["filtered_size"]) + len(d["filtered_dim"])
        num_orphans = len(d["orphan_on_disk"])

        total_disk += num_disk
        total_refs += num_refs
        total_annotated += num_annot
        total_eligible += num_eligible
        total_filtered += num_filtered
        total_orphans += num_orphans

        print(f"{subj:<22} | {num_disk:<9} | {num_refs:<8} | {num_annot:<9} | {num_eligible:<13} | {num_filtered:<10} | {num_orphans:<8}")

    print("-" * 92)
    print(f"{'TOTALS':<22} | {total_disk:<9} | {total_refs:<8} | {total_annotated:<9} | {total_eligible:<13} | {total_filtered:<10} | {total_orphans:<8}")
    print("=" * 92 + "\n")

    # Detailed Inspection into NaturalSciences, LifeSciences, PhysicalSciences
    target_subjects = ["NaturalSciences", "LifeSciences", "PhysicalSciences"]
    for ts in target_subjects:
        if ts in stats:
            d = stats[ts]
            print(f">>> DETAILED BREAKDOWN: {ts}")
            print(f"    Total images on disk               : {len(d['disk_images'])}")
            print(f"    Total image references in Markdown : {len(d['md_referenced'])}")
            print(f"    Annotated with Diagram Context     : {len(d['annotated'])}")
            print(f"    Eligible but NOT yet annotated     : {len(d['eligible_unannotated'])}")
            print(f"    Filtered (Size < 4KB)              : {len(d['filtered_size'])}")
            print(f"    Filtered (Dimensions < 35px/8000px²): {len(d['filtered_dim'])}")
            print(f"    Orphan images on disk (not in MD)  : {len(d['orphan_on_disk'])}")

            if d["eligible_unannotated"]:
                print(f"\n    Sample Eligible Unannotated Images (First 5):")
                for md_p, iname, sz, w, h in list(d["eligible_unannotated"])[:5]:
                    print(f"      - {iname} ({w}x{h}px, {sz/1024:.1f} KB) in {Path(md_p).name}")

            if d["filtered_dim"]:
                print(f"\n    Sample Dimension-Filtered Images (First 5):")
                for iname in list(d["filtered_dim"])[:5]:
                    print(f"      - {iname}")

            if d["orphan_on_disk"]:
                print(f"\n    Sample Orphan Images on Disk (First 5):")
                for op in list(d["orphan_on_disk"])[:5]:
                    print(f"      - {op.name} ({op.stat().st_size/1024:.1f} KB) in {op.parent.relative_to(AUTO_ROOT)}")
            print("\n" + "-" * 60 + "\n")

if __name__ == "__main__":
    analyze_curriculum_images()
