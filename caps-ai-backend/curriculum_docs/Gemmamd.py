import os
import re
import time
import base64
import requests
from pathlib import Path
from PIL import Image

# Path Configurations
OUTPUT_DIR = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\curriculum_docs\Physical-Science-Gr11\Term 1\Output").resolve()
RAW_MD_PATH = OUTPUT_DIR / "raw_extracted.md"
ENRICHED_MD_PATH = OUTPUT_DIR / "curriculum_textbook_enriched.md"
IMAGES_DIR = OUTPUT_DIR / "images"

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
VISION_MODEL = "qwen2.5vl:3b"

VISION_PROMPT = """You are a CAPS Physical Science curriculum expert.
Examine this graphic and write a clear 2-4 sentence pedagogical description:
1. Identify the visual content (Lewis diagram, vector force, circuit, table/exercise visual).
2. List visible labels, variables, numbers, units, chemical symbols, and arrows.
3. Explain what the diagram conveys conceptually for a student.

Output ONLY the description. No metadata, intros, or markdown wrapper blocks."""

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def describe_image_with_gemma(image_path):
    if not os.path.exists(image_path):
        return None
    
    # Filter out tiny icon thumbnails (area < 4000 px)
    with Image.open(image_path) as img:
        w, h = img.size
        if (w * h) < 4000:
            print(f"   [Skipping Icon] {os.path.basename(image_path)} ({w}x{h})")
            return None

    base64_img = encode_image_to_base64(image_path)
    
    payload = {
        "model": VISION_MODEL,
        "prompt": VISION_PROMPT,
        "images": [base64_img],
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 150
        }
    }
    
    # Retry loop for Ollama crashes/timeouts
    for attempt in range(1, 4):
        try:
            response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=180)
            if response.status_code == 200:
                return response.json().get("response", "").strip()
        except Exception as e:
            print(f"   [Attempt {attempt}/3 Failed] {os.path.basename(image_path)}: {e}")
            time.sleep(4)
            
    return None

def unwrap_column_paragraphs(text):
    """Joins hard-wrapped lines from PDF columns while preserving headers and structure."""
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

def sanitize_and_fix_latex(text):
    """Strips broken HTML tags and formats chemical formulas into clean LaTeX without tab escapes."""
    # 1. Strip broken HTML superscript/subscript tags
    text = re.sub(r'<sup>\s*\+?\s*</sup>', '', text)
    text = re.sub(r'<sup>\s*\)\s*showninthefigurebelow\.?\s*</sup>', ' shown in the figure below.', text)
    text = re.sub(r'NH<sup>\+</sup>\s*4', r'$\\text{NH}_4^+$', text)
    text = re.sub(r'H3O<sup>\+</sup>', r'$\\text{H}_3\\text{O}^+$', text)
    text = re.sub(r'1s<sup>2</sup>|2s<sup>2</sup>|2p<sup>6</sup>|2p<sup>5</sup>|2p<sup>4</sup>|2p<sup>3</sup>|2p<sup>2</sup>|2p<sup>1</sup>', lambda m: f"${m.group(0).replace('<sup>', '^').replace('</sup>', '')}$", text)
    text = re.sub(r'<sup>(.*?)</sup>', r'^{\1}', text)
    text = re.sub(r'<sub>(.*?)</sub>', r'_{\1}', text)

    # 2. Convert compounds (Double backslash '\\text' prevents Python '\t' Tab conversion)
    compounds = [
        'H2O', 'CO2', 'CH4', 'NH3', 'BF3', 'BeCl2', 'PCl5', 'SF6', 
        'Cl2', 'O2', 'N2', 'H2', 'C2H2', 'OF2', 'CH2O', 'NO2', 
        'BCl3', 'CCl4', 'Br2', 'MgI2', 'CS2', 'CH3Cl', 'SCl5F', 
        'BF2Cl', 'PCl4F', 'SF5Cl'
    ]
    
    for comp in compounds:
        latex_comp = re.sub(r'([A-Za-z]+)(\d+)', r'\\text{\1}_\2', comp)
        # Match standalone occurrences to prevent double wrapping
        text = re.sub(rf'(?<!\\text\{{)\b{comp}\b', f"$\\\\text{{{comp}}}$" if not any(c.isdigit() for c in comp) else f"${latex_comp}$", text)

    # 3. Scientific notation & exponents
    text = re.sub(r'kJ\s*·\s*mol[-−]1', r'$\\text{kJ}\\cdot\\text{mol}^{-1}$', text)
    text = re.sub(r'10[-−](\d+)', r'$10^{-\1}$', text)
    
    return text

def run_pipeline():
    print(f"Reading base text: {RAW_MD_PATH}")
    with open(RAW_MD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    print("1. Stripping picture text comments...")
    content = re.sub(r'<!-- Start of picture text -->.*?<!-- End of picture text -->', '', content, flags=re.DOTALL)

    print("2. Unwrapping column line breaks...")
    content = unwrap_column_paragraphs(content)

    print("3. Sanitizing HTML & converting formulas to LaTeX...")
    content = sanitize_and_fix_latex(content)

    print("4. Processing images in-place with Gemma...")
    image_pattern = re.compile(r'!\[(.*?)\]\((images/[^)]+)\)')
    matches = image_pattern.findall(content)

    replaced_count = 0
    for alt, img_rel_path in matches:
        img_name = os.path.basename(img_rel_path)
        full_img_path = IMAGES_DIR / img_name

        print(f"   - Processing: {img_name}")
        description = describe_image_with_gemma(full_img_path)
        original_tag = f"![{alt}]({img_rel_path})"

        if description:
            in_place_block = (
                f"\n\n![{img_name}]({img_rel_path})\n"
                f"> **[Diagram Context & Visual Description - {img_name}]**\n"
                f"> {description}\n\n"
            )
            content = content.replace(original_tag, in_place_block, 1)
            replaced_count += 1
        else:
            # Retain image link structure if description fails
            fallback_block = f"\n\n![{img_name}]({img_rel_path})\n"
            content = content.replace(original_tag, fallback_block, 1)

    with open(ENRICHED_MD_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("\n--------------------------------------------------")
    print(f" PIPELINE COMPLETE! Successfully processed {replaced_count} diagrams.")
    print(f" Output File: {ENRICHED_MD_PATH}")
    print("--------------------------------------------------\n")

if __name__ == "__main__":
    run_pipeline()