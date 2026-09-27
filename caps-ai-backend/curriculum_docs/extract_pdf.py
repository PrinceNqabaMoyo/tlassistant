import os
import pymupdf
import pymupdf4llm
from pathlib import Path

def extract_pdf_to_markdown(pdf_path, term_dir, file_prefix, target_pages=None, crop_tables=True, save_full_renders=False):
    """
    Extracts text/diagrams from a PDF directly into a structured Term directory.
    Optionally crops PDF tables as images so Qwen Vision can describe visual content inside tables.
    
    :param pdf_path: Absolute path to the source PDF.
    :param term_dir: Path object for target folder.
    :param file_prefix: Prefix for output files (e.g., "01_Atomic_combinations").
    :param target_pages: List of 0-indexed page numbers (None processes full PDF).
    :param crop_tables: If True, crops table bounding boxes as PNGs for Qwen Vision.
    :param save_full_renders: If True, renders full-page visual backup images.
    """
    pdf_path = Path(pdf_path).resolve()
    term_dir = Path(term_dir).resolve()
    images_dir = term_dir / "images"

    term_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(str(pdf_path))
    total_doc_pages = len(doc)
    
    if target_pages is None:
        target_pages = list(range(total_doc_pages))

    original_cwd = os.getcwd()
    raw_md_filename = f"{file_prefix}_raw.md"
    raw_md_path = term_dir / raw_md_filename

    try:
        os.chdir(term_dir)

        print(f"-> Extracting layout & cropping diagrams: {pdf_path.name}")
        md_text = pymupdf4llm.to_markdown(
            str(pdf_path),
            pages=target_pages,
            write_images=True,
            image_path="images",
            image_format="png",
            dpi=200
        )

        # Optional: Crop table bounding boxes as PNG images so Qwen Vision can describe visual tables
        # Smart table cropping: ONLY crop tables that contain embedded images/diagrams inside cells
        if crop_tables:
            table_img_tags = []
            for page_num in target_pages:
                if 0 <= page_num < total_doc_pages:
                    page = doc[page_num]
                    try:
                        tabs = page.find_tables()
                        if tabs and len(tabs.tables) > 0:
                            page_imgs = page.get_image_info()
                            for idx, tab in enumerate(tabs.tables):
                                bbox = tab.bbox
                                t_rect = pymupdf.Rect(bbox)
                                # Only crop if this table actually embeds visual graphics (e.g. molecules, cells)
                                has_visual = any(t_rect.intersects(pymupdf.Rect(im['bbox'])) for im in page_imgs if 'bbox' in im)
                                if has_visual and (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) > 5000:
                                    pix = page.get_pixmap(clip=bbox, dpi=200)
                                    table_img_name = f"{file_prefix}_table_p{page_num + 1}_t{idx + 1}.png"
                                    table_img_path = images_dir / table_img_name
                                    pix.save(str(table_img_path))
                                    table_img_tags.append(f"\n\n![Visual Table Page {page_num + 1}](images/{table_img_name})\n")
                    except Exception as te:
                        print(f"   [Warning] Table finder failed on page {page_num + 1}: {te}")

            if table_img_tags:
                md_text += "\n\n### Extracted Table Visuals\n" + "".join(table_img_tags)

        raw_md_path.write_bytes(md_text.encode("utf-8"))

    finally:
        os.chdir(original_cwd)

    # Render full-page backup images if requested
    if save_full_renders:
        full_pages_dir = term_dir / "full_page_renders"
        full_pages_dir.mkdir(exist_ok=True)
        print("-> Saving full-page render backups...")
        for page_num in target_pages:
            if 0 <= page_num < total_doc_pages:
                page = doc[page_num]
                pix = page.get_pixmap(dpi=200)
                pix.save(str(full_pages_dir / f"page_{page_num + 1}_full.png"))
            
    doc.close()
    return raw_md_path