import os
import re
import io
import time
import base64
import requests
from pathlib import Path
from PIL import Image

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
VISION_MODEL = "qwen2.5vl:3b"

VISION_PROMPT_TEMPLATE = """You are a South African CAPS curriculum expert tutor.
{topic_context}
Examine this graphic and write a clear, 2-4 sentence pedagogical description:
1. Identify the visual content (Lewis diagram, vector force, circuit, table/exercise visual, graph, flow diagram, accounting structure).
2. List visible labels, variables, numbers, units, chemical symbols, axis names, and arrows.
3. Explain what the diagram conveys conceptually for a student learning this topic.

Output ONLY the description text. No metadata, intros, or markdown wrapper blocks."""

def get_optimized_base64_image(image_path, max_dim=600):
    """
    Checks if image is valid pedagogical content (>6KB, >120x120px) and downscales
    to max_dim (default 600px) so Ollama CPU vision processes in ~10 seconds instead of timing out at 180s.
    """
    if not os.path.exists(image_path):
        return None
    
    # Skip file sizes < 6KB (bullet icons, decorative lines, blank cuts)
    if os.path.getsize(image_path) < 6144:
        return None

    try:
        with Image.open(image_path) as img:
            w, h = img.size
            if w < 120 or h < 120 or (w * h) < 14400:  # Skip small non-diagram icons
                return None

            # Convert RGBA/Palette to RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Downscale high-resolution images to max 600px to speed up CPU vision matrix math
            max_size = max(w, h)
            if max_size > max_dim:
                scale = max_dim / float(max_size)
                new_w = max(1, int(w * scale))
                new_h = max(1, int(h * scale))
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=85)
            return base64.b64encode(buffer.getvalue()).decode('utf-8')
    except Exception as e:
        print(f"   [Warning] Image load error {os.path.basename(image_path)}: {e}")
        return None

def describe_image_with_qwen(image_path, topic_hint=None):
    base64_img = get_optimized_base64_image(image_path)
    if not base64_img:
        return None

    topic_context = f"The subject topic is '{topic_hint}'." if topic_hint else ""
    prompt = VISION_PROMPT_TEMPLATE.format(topic_context=topic_context)

    payload = {
        "model": VISION_MODEL,
        "prompt": prompt,
        "images": [base64_img],
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 120
        }
    }
    
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=25)
        if response.status_code == 200:
            res = response.json().get("response", "").strip()
            res = re.sub(r'^```[\w]*\n?', '', res)
            res = re.sub(r'\n?```$', '', res)
            return res.strip()
    except Exception as e:
        print(f"   [Vision Skipped / Timeout] {os.path.basename(image_path)}: {e}")
        
    return None


def unwrap_column_paragraphs(text):
    lines = text.split('\n')
    unwrapped = []
    page_header_pattern = re.compile(r'^\d+\.\d+\.\s+.*|\b\d{2,3}\b$|^Chapter\s+\d+')

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('|') or stripped.startswith('![') or page_header_pattern.match(stripped):
            unwrapped.append(line)
        else:
            if unwrapped and not unwrapped[-1].startswith('#') \
               and not unwrapped[-1].startswith('|') \
               and not unwrapped[-1].startswith('![') \
               and not page_header_pattern.match(unwrapped[-1].strip()) \
               and unwrapped[-1].strip() != '':
                unwrapped[-1] = unwrapped[-1].strip() + ' ' + stripped
            else:
                unwrapped.append(line)
    return '\n'.join(unwrapped)

def strip_pdf_artefacts(text):
    """Strips page numbers, chapter headers, section footers, ESB codes, publisher promos, and garbled inline Lewis text."""
    lines = text.split('\n')
    cleaned_lines = []

    esb_pattern = re.compile(r'^\s*ESB[A-Z0-9]{1,6}\s*$')
    page_num_pattern = re.compile(r'^\s*(\*\*\d{1,3}\*\*|\b\d{1,3}\b)\s*$')
    chapter_header_pattern = re.compile(r'^\s*Chapter\s+\d+(\.\d+)?\s*\.?\s*([A-Za-z0-9\s—\-]+)?$', re.IGNORECASE)
    section_footer_pattern = re.compile(r'^\s*\d+\.\d+\.\s+[A-Z][a-z]+(\s+[A-Za-z]+)*\s*$')
    promo_pattern = re.compile(r'^\s*(See (simulation|presentation|video):|Think you got it\?|Get this answer and more practice|www\.everythingscience|m\.everythingscience).*$', re.IGNORECASE)
    answer_code_table = re.compile(r'^\s*\|?\s*(\d+[a-z]?\.\s*[0-9A-Z]{4}\s*\|?\s*)+$')
    lewis_garble_pattern = re.compile(r'^\s*([•×·\.\+\-\s]*[HCNOSFClBrIPBeLiNaMgAlSiKCaXY][•×·\.\+\-\s]*)+$')

    for line in lines:
        stripped = line.strip()
        
        if esb_pattern.match(stripped):
            continue
        if page_num_pattern.match(stripped):
            continue
        if chapter_header_pattern.match(stripped):
            continue
        if section_footer_pattern.match(stripped):
            continue
        if promo_pattern.match(stripped):
            continue
        if answer_code_table.match(stripped):
            continue
        if len(stripped) < 40 and lewis_garble_pattern.match(stripped) and not any(w in stripped.lower() for w in ['step', 'figure', 'table', 'case', 'note', 'tip', 'solution']):
            continue

        cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

def sanitize_and_fix_latex(text):
    """Sanitizes HTML tags, fixes orbital configs, chemical formulas, and polyatomic ions into clean LaTeX."""

    text = re.sub(r'<sup>\s*\+?\s*</sup>', '', text)
    text = re.sub(r'<sup>\s*\)\s*showninthefigurebelow\.?\s*</sup>', ' shown in the figure below.', text)
    
    text = re.sub(r'NH<sup>\+</sup>\s*4|NH<sub>4</sub><sup>\+</sup>|NH4\+', r'$\text{NH}_4^+$', text)
    text = re.sub(r'H3O<sup>\+</sup>|H<sub>3</sub>O<sup>\+</sup>|H3O\+', r'$\text{H}_3\text{O}^+$', text)

    text = re.sub(r'(\b[1-7][spdf])<sup>(\d+)</sup>', r'$\1^{\2}$', text)
    text = re.sub(r'(\b[1-7][spdf])\^{?(\d+)}?', r'$\1^{\2}$', text)

    text = re.sub(r'<sup>([^<>\n]{1,40})</sup>', r'^{\1}', text)
    text = re.sub(r'<sub>([^<>\n]{1,40})</sub>', r'_{\1}', text)

    compounds = [
        'H2O', 'CO2', 'CH4', 'NH3', 'BF3', 'BeCl2', 'PCl5', 'SF6', 
        'Cl2', 'O2', 'N2', 'H2', 'C2H2', 'OF2', 'CH2O', 'NO2', 
        'BCl3', 'CCl4', 'Br2', 'MgI2', 'CS2', 'CH3Cl', 'SCl5F', 
        'BF2Cl', 'PCl4F', 'SF5Cl', 'PCl3', 'H2S', 'SO2', 'SO3'
    ]
    
    for comp in compounds:
        latex_comp = re.sub(r'([A-Za-z]+)(\d+)', r'\\text{\1}_\2', comp)
        text = re.sub(rf'(?<!\\text\{{)\b{comp}\b', rf"$\text{{{comp}}}$" if not any(c.isdigit() for c in comp) else rf"${latex_comp}$", text)

    text = re.sub(r'kJ\s*·\s*mol[-−]1', r'$\text{kJ}\\cdot\text{mol}^{-1}$', text)
    text = re.sub(r'10[-−](\d+)', r'$10^{-\1}$', text)
    text = re.sub(r'(\d+)\s*pm\b', r'$\1\\text{ pm}$', text)

    return text

def collapse_blank_lines(text):
    """Reduces 3 or more consecutive newlines to maximum 2."""
    return re.sub(r'\n{3,}', '\n\n', text)

def enrich_markdown_file(raw_md_path, final_md_path, topic_hint=None, exam_archetypes_md=None, study_guide_md=None, skip_vision=False):
    raw_md_path = Path(raw_md_path).resolve()
    final_md_path = Path(final_md_path).resolve()
    final_md_path.parent.mkdir(parents=True, exist_ok=True)
    images_dir = raw_md_path.parent / "images"

    print(f"-> Cleaning and enriching: {raw_md_path.name}")
    with open(raw_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(r'<!-- Start of picture text -->.*?<!-- End of picture text -->', '', content, flags=re.DOTALL)
    content = strip_pdf_artefacts(content)
    content = unwrap_column_paragraphs(content)
    content = sanitize_and_fix_latex(content)

    # Process diagrams with Qwen Vision (only meaningful figures, downscaled to 600px)
    image_pattern = re.compile(r'!\[(.*?)\]\((images/[^)]+)\)')
    matches = image_pattern.findall(content)

    replaced_count = 0
    for alt, img_rel_path in matches:
        img_name = os.path.basename(img_rel_path)
        full_img_path = images_dir / img_name

        description = describe_image_with_qwen(full_img_path, topic_hint=topic_hint) if not skip_vision else None
        original_tag = f"![{alt}]({img_rel_path})"


        if description:
            print(f"   * Qwen Vision described: {img_name}")
            in_place_block = (
                f"\n\n![{img_name}]({img_rel_path})\n"
                f"> **[Diagram Context - {img_name}]**\n"
                f"> {description}\n\n"
            )
            content = content.replace(original_tag, in_place_block, 1)
            replaced_count += 1
        else:
            fallback_block = f"\n\n![{img_name}]({img_rel_path})\n"
            content = content.replace(original_tag, fallback_block, 1)

    # If study guide procedural notes were extracted, append under procedures section
    if study_guide_md and study_guide_md.strip():
        content += f"\n\n## 3. Step-by-Step Procedures & Accounting Formats (Study Guide)\n\n{study_guide_md.strip()}\n"

    # If exam question archetypes with mark allocations were extracted, append under exam section
    if exam_archetypes_md and exam_archetypes_md.strip():
        content += f"\n\n{exam_archetypes_md.strip()}\n"

    content = collapse_blank_lines(content)

    with open(final_md_path, "w", encoding="utf-8") as f:
        f.write(content)

    if raw_md_path.exists() and raw_md_path != final_md_path:
        try:
            os.remove(raw_md_path)
        except Exception:
            pass

    print(f"-> COMPLETE: Created {final_md_path.name} ({replaced_count} diagrams described)\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        raw_p = sys.argv[1]
        out_p = sys.argv[2]
        topic = sys.argv[3] if len(sys.argv) > 3 else None
        enrich_markdown_file(raw_p, out_p, topic_hint=topic)
    else:
        print("Usage: python qwenmd.py <raw_md_path> <final_md_path> [topic_hint]")