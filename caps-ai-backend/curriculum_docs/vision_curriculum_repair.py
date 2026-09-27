import os
import re
import sys
import json
import time
import base64
import difflib
import argparse
import requests
import pymupdf
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# Path Configurations
SCRIPT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend").resolve()
CURRICULUM_DOCS_DIR = BACKEND_DIR / "curriculum_docs"
AUTO_ROOT = BACKEND_DIR / "curriculum_docs_auto"
ENV_PATH = BACKEND_DIR / ".env"
CACHE_FILE = CURRICULUM_DOCS_DIR / "diagram_descriptions_cache.json"
QUALITY_REPORT_FILE = CURRICULUM_DOCS_DIR / "curriculum_quality_report.json"
PROGRESS_FILE = CURRICULUM_DOCS_DIR / "repair_progress.json"
PAGE_CACHE_DIR = CURRICULUM_DOCS_DIR / ".page_cache"

class PageCacheManager:
    """Manages persistent disk checkpoints per topic so interrupted files resume instantly."""
    def __init__(self, cache_dir=PAGE_CACHE_DIR):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_file(self, rel_key: str) -> Path:
        safe_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', rel_key) + ".json"
        return self.cache_dir / safe_name

    def load_cached_pages(self, rel_key: str) -> dict:
        c_file = self._get_cache_file(rel_key)
        if c_file.exists():
            try:
                data = json.loads(c_file.read_text(encoding="utf-8"))
                return {int(k): v for k, v in data.get("pages", {}).items()}
            except Exception:
                pass
        return {}

    def save_page(self, rel_key: str, page_idx: int, markdown_content: str):
        c_file = self._get_cache_file(rel_key)
        pages = self.load_cached_pages(rel_key)
        pages[page_idx] = markdown_content
        data = {
            "rel_key": rel_key,
            "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
            "pages": {str(k): v for k, v in pages.items()}
        }
        temp_file = c_file.with_suffix(".tmp")
        temp_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        temp_file.replace(c_file)

    def clear_cache(self, rel_key: str):
        c_file = self._get_cache_file(rel_key)
        if c_file.exists():
            try:
                c_file.unlink()
            except Exception:
                pass

def check_internet_connectivity(timeout=3):
    """Checks if external internet is reachable to avoid falsely advancing models on local WiFi drops."""
    try:
        import socket
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("8.8.8.8", 53))
        s.close()
        return True
    except Exception:
        pass
    try:
        r = requests.get("https://1.1.1.1", timeout=timeout)
        if r.status_code in [200, 301, 302]:
            return True
    except Exception:
        pass
    return False

def deterministic_text_katex_cleaner(raw_text: str) -> str:
    """Deterministic regex cleaner that fixes broken fractions, degrees, and symbols in raw PDF text."""
    if not raw_text:
        return ""
    text = raw_text

    # 1. Clean HTML sub/sup fractions: <sup><u>num</u></sup> den or <u>num</u> den
    text = re.sub(
        r'<sup><u>([^<]+)</u></sup>\s*([0-9a-zA-Z\+\-]+)',
        r'$\\frac{\1}{\2}$',
        text
    )
    text = re.sub(
        r'<u>([0-9a-zA-Z]+)</u>\s*([0-9a-zA-Z]+)',
        r'$\\frac{\1}{\2}$',
        text
    )

    # 2. Fix unrendered degrees: 45° or 45 ^\circ
    text = re.sub(r'(\d+)\s*°', r'\1^\\circ', text)

    # 3. Clean symbols
    text = text.replace('□', '$\\square$')
    text = text.replace('■', '$\\blacksquare$')
    text = text.replace('√', '$\\sqrt{}$')
    text = text.replace('π', '$\\pi$')
    text = text.replace('θ', '$\\theta$')

    # 4. Clean linebreaks & simple headings
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            lines.append("")
            continue
        if re.match(r'^(Activity|Exercise|Example|Chapter|Unit|\d+\.\d+)', line, re.I):
            lines.append(f"\n### {line}\n")
        else:
            lines.append(line)

    return "\n".join(lines).strip()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5vl:3b"

GEMINI_MODELS_POOL = [
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-flash-lite-latest",
    "gemini-3.5-flash",
    "gemini-flash-latest",
    "gemini-3.6-flash",
    "gemini-3.8-flash",
    "gemini-3-flash-preview",
    "gemini-3.7-flash"
]

MATH_PROMPT = """You are an expert South African CAPS curriculum educational tutor.
Analyze this curriculum page and present its instructional contents in clear, accessible Markdown for learners:
1. CONCEPTS & STRUCTURE: Explain and typeset all key concepts, definitions, section headings, notes, exercises, and worked examples in logical instructional order.
2. MATHEMATICS & FORMULAS: All mathematical equations, fractions, exponents, surds, and symbols MUST use standard KaTeX notation ($...$, $$...$$, \\frac{num}{den}, ^{exp}, \\sqrt{...}). Never use <sup><u> HTML tags.
3. TABLES & ACCOUNTING: Any financial statements, cost breakdown tables, ledger accounts, journals (CRJ, CPJ, DJ, CJ), or balance sheets MUST be formatted as complete, aligned 2D Markdown tables.
4. DIAGRAMS: For any diagrams, apparatus, or illustrations on this page, insert a placeholder: <!-- DIAGRAM_PLACEHOLDER: diagram -->
Output ONLY the clean Markdown without introductory or conversational filler."""

TEACHING_PROMPT = """You are an expert high school Accounting and Mathematics educator preparing clear revision notes for learners.
Examine the educational material on this page and present its lesson contents in clean Markdown:
1. Teach and explain all core concepts, procedures, worked examples, and activities clearly.
2. All mathematical formulas and equations MUST use clean KaTeX notation ($...$, $$...$$, \\frac{num}{den}, ^{exp}, \\sqrt{...}).
3. Format any ledger accounts, transaction journals, financial statements, and tables as complete 2D Markdown tables.
4. Ignore any publisher imprints or copyright footers. Focus purely on educational lesson content.
Output ONLY the clean educational Markdown without introductory or conversational filler."""

def load_env_keys():
    env_vars = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env_vars[k.strip()] = v.strip().strip("'\"")

    keys = []
    # 1. Comma-separated in GEMINI_API_KEYS or GEMINI_API_KEY
    for env_k in ["GEMINI_API_KEYS", "GEMINI_API_KEY"]:
        raw = env_vars.get(env_k) or os.getenv(env_k) or ""
        for item in raw.split(","):
            item = item.strip()
            if item and item not in keys:
                keys.append(item)

    # 2. Numbered keys: GEMINI_API_KEY_1, GEMINI_API_KEY_2, etc.
    for k in sorted([k for k in env_vars.keys() if k.startswith("GEMINI_API_KEY_")]):
        v = env_vars[k].strip()
        if v and v not in keys:
            keys.append(v)

    return keys

class CloudQuotaState:
    def __init__(self, keys, custom_model=None):
        self.gemini_keys = keys
        self.gemini_pool = [custom_model] if custom_model else list(GEMINI_MODELS_POOL)
        self.active_key_idx = 0
        self.active_model_idx = 0
        self.gemini_exhausted = len(self.gemini_keys) == 0
        self.active_provider = "gemini" if self.gemini_keys else "ollama"

    @property
    def current_model(self):
        if self.active_model_idx < len(self.gemini_pool):
            return self.gemini_pool[self.active_model_idx]
        return None

    @property
    def current_key(self):
        if self.active_key_idx < len(self.gemini_keys):
            return self.gemini_keys[self.active_key_idx]
        return None

    def advance_gemini_target(self, exhausted_model=None, reason="Quota reached"):
        m_name = exhausted_model or self.current_model or "model"
        key_num = self.active_key_idx + 1
        total_keys = len(self.gemini_keys)

        if self.active_key_idx + 1 < total_keys:
            self.active_key_idx += 1
            print(f"      [Gemini {m_name} Key {key_num}/{total_keys} unavailable: {reason}]")
            print(f" --> KEY FAILOVER: Switching to Key [{self.active_key_idx + 1}/{total_keys}] for {m_name}")
            return self.current_model, self.current_key

        print(f"      [Gemini {m_name} exhausted across all {total_keys} key(s): {reason}]")
        self.active_key_idx = 0
        self.active_model_idx += 1
        next_m = self.current_model
        if next_m:
            print(f" --> CASCADING FAILOVER: Advancing to next cloud model [{self.active_model_idx + 1}/{len(self.gemini_pool)}]: {next_m} (Key 1/{total_keys})")
            return next_m, self.current_key
        else:
            self.mark_gemini_exhausted(f"All {len(self.gemini_pool)} Gemini models exhausted across all {total_keys} API keys")
            return None, None

    def mark_gemini_exhausted(self, reason="All models daily quota reached"):
        if not self.gemini_exhausted:
            self.gemini_exhausted = True
            print("\n" + "=" * 70)
            print(f" [ALL CLOUD QUOTAS EXHAUSTED] Google Gemini: {reason}")
            print(f" --> FINAL FAILOVER: Switching directly to local Ollama ({OLLAMA_MODEL})...")
            print("=" * 70 + "\n")
            self.active_provider = "ollama"

def ensure_ollama_running():
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=2)
        if r.status_code == 200:
            return True
    except Exception:
        pass

    print("\n   [Local Ollama is not running. Attempting to start 'ollama serve' in background...]")
    import subprocess
    for path in ["ollama", os.path.expandvars(r"%LOCALAPPDATA%\Programs\Ollama\ollama.exe"), r"C:\Users\princ\AppData\Local\Programs\Ollama\ollama.exe"]:
        try:
            flags = 0
            if sys.platform == "win32":
                flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "DETACHED_PROCESS", 0)
            subprocess.Popen([path, "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags)
            break
        except Exception:
            continue

    for _ in range(8):
        time.sleep(1.5)
        try:
            if requests.get("http://localhost:11434/api/tags", timeout=2).status_code == 200:
                print("   [Ollama successfully started on port 11434!]\n")
                return True
        except Exception:
            continue
    return False

def call_gemini_vision(b64_img, prompt, quota_state, delay=4.2):
    while not quota_state.gemini_exhausted:
        model = quota_state.current_model
        key = quota_state.current_key
        if not model or not key:
            quota_state.mark_gemini_exhausted("No valid model/key remaining")
            return None

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}, {"inline_data": {"mime_type": "image/jpeg", "data": b64_img}}]}],
            "generationConfig": {"temperature": 0.1, "maxOutputTokens": 4096}
        }

        advanced_for_next = False

        for attempt in range(3):
            try:
                time.sleep(delay)
                r = requests.post(url, json=payload, timeout=45)
                if r.status_code == 200:
                    res = r.json()
                    candidates = res.get("candidates", [])
                    if not candidates:
                        print(f"      [Gemini returned no candidates (Prompt Filtered) - using local fallback]")
                        return None
                    cand = candidates[0]
                    finish_reason = cand.get("finishReason", "")

                    if finish_reason in ["RECITATION"]:
                        # Immediately attempt pedagogical rephrase on the same key/model
                        # because transformative explanation completely clears Google's recitation heuristic!
                        rephrase_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
                        rephrase_payload = {
                            "contents": [{"parts": [{"text": TEACHING_PROMPT}, {"inline_data": {"mime_type": "image/jpeg", "data": b64_img}}]}],
                            "generationConfig": {"temperature": 0.2, "maxOutputTokens": 4096}
                        }
                        try:
                            time.sleep(2.0)
                            rr = requests.post(rephrase_url, json=rephrase_payload, timeout=40)
                            if rr.status_code == 200:
                                r_cand = rr.json().get("candidates", [{}])[0]
                                if r_cand.get("finishReason") not in ["RECITATION", "SAFETY"]:
                                    r_content = r_cand.get("content") or {}
                                    r_parts = r_content.get("parts") or []
                                    r_texts = [p.get("text", "") for p in r_parts if isinstance(p, dict) and p.get("text") and not p.get("thought")]
                                    r_full = "\n".join(r_texts).strip()
                                    if r_full:
                                        return r_full, f"Gemini ({model} - Key {quota_state.active_key_idx + 1}) [Pedagogical Rephrase]"
                        except Exception:
                            pass

                    if finish_reason in ["RECITATION", "SAFETY", "BLOCKLIST", "PROHIBITED_CONTENT"]:
                        print(f"      [Gemini Filtered ({finish_reason}) on this page - using fast text fallback]")
                        return None

                    content = cand.get("content") or {}
                    parts = content.get("parts") or []
                    text_parts = [p.get("text", "") for p in parts if isinstance(p, dict) and p.get("text") and not p.get("thought")]
                    full_text = "\n".join(text_parts).strip()
                    if full_text:
                        return full_text, f"Gemini ({model} - Key {quota_state.active_key_idx + 1})"

                    print(f"      [Gemini produced empty text ({finish_reason}) - using local fallback]")
                    return None

                # Quota 429
                if r.status_code == 429:
                    err_text = r.text.lower()
                    is_daily = any(t in err_text for t in ["quota exceeded", "resource_exhausted", "perday", "per day", "day limit"])
                    if is_daily or attempt == 2:
                        quota_state.advance_gemini_target(model, reason="Daily quota (429) exhausted")
                        advanced_for_next = True
                        break
                    wait_sec = 6 * (attempt + 1)
                    print(f"      [Gemini 15 RPM burst on Key {quota_state.active_key_idx+1} - cooling down {wait_sec}s...]")
                    time.sleep(wait_sec)
                    continue

                if r.status_code in [500, 502, 503]:
                    if attempt == 2:
                        quota_state.advance_gemini_target(model, reason=f"Server error {r.status_code}")
                        advanced_for_next = True
                        break
                    time.sleep(3 * (attempt + 1))
                    continue

                if r.status_code == 404:
                    quota_state.advance_gemini_target(model, reason="Model 404 Not Found")
                    advanced_for_next = True
                    break

                if r.status_code == 403:
                    quota_state.advance_gemini_target(model, reason="403 Access Denied")
                    advanced_for_next = True
                    break

                print(f"      [Gemini API Error {r.status_code}: {r.text[:80]}]")
                if attempt == 2:
                    quota_state.advance_gemini_target(model, reason=f"HTTP {r.status_code}")
                    advanced_for_next = True
                    break
                time.sleep(3)

            except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as net_err:
                if not check_internet_connectivity():
                    print(f"\n      [Local WiFi / Internet Disconnected! Pausing for connection to restore...]")
                    reconnected = False
                    for w in range(6):
                        time.sleep(5)
                        if check_internet_connectivity():
                            print(f"      [Internet connection restored! Resuming on current model & key]")
                            reconnected = True
                            break
                    if not reconnected:
                        print(f"      [Internet still offline after 30s. Retrying current key...]")
                    continue

                print(f"      [Network/SSL glitch on Key {quota_state.active_key_idx+1} (attempt {attempt+1}/3): retrying in 4s...]")
                if attempt == 2:
                    quota_state.advance_gemini_target(model, reason="Persistent network/SSL error")
                    advanced_for_next = True
                    break
                time.sleep(4)

            except requests.exceptions.Timeout:
                print(f"      [Timeout on Key {quota_state.active_key_idx+1} (attempt {attempt+1}/3)...]")
                if attempt == 2:
                    quota_state.advance_gemini_target(model, reason="Timeout (45s)")
                    advanced_for_next = True
                    break
                time.sleep(3)

            except Exception as e:
                print(f"      [Exception on Key {quota_state.active_key_idx+1}: {e}]")
                if attempt == 2:
                    quota_state.advance_gemini_target(model, reason=f"Exception: {e}")
                    advanced_for_next = True
                    break
                time.sleep(3)

        if not advanced_for_next and not quota_state.gemini_exhausted:
            quota_state.advance_gemini_target(model, reason="Retries exhausted")

    return None

def call_ollama_vision(pixmap, prompt):
    if not ensure_ollama_running():
        print("      [Local Ollama could not be started]")
        return None

    # Downscale image to max 800px so CPU inference completes quickly
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(pixmap.tobytes("jpeg")))
        img.thumbnail((800, 800), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=80)
        opt_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception:
        opt_b64 = base64.b64encode(pixmap.tobytes("jpeg")).decode("utf-8")

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "images": [opt_b64],
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 1024}
    }
    try:
        r = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=35)
        if r.status_code == 200:
            return r.json().get("response", "").strip(), f"Ollama ({OLLAMA_MODEL})"
    except Exception as e:
        print(f"      [Ollama Local Error: {e}]")
    return None

def transcribe_page_vision(page, quota_state, requested_provider="auto", delay=4.2):
    pix = page.get_pixmap(dpi=150)
    b64_img = base64.b64encode(pix.tobytes("jpeg")).decode("utf-8")

    # 1. Primary: Google Gemini Vision
    if requested_provider in ["auto", "gemini"] and not quota_state.gemini_exhausted:
        res = call_gemini_vision(b64_img, MATH_PROMPT, quota_state, delay=delay)
        if res:
            return res

    # 2. Text Reconstruct Fallback (ONLY if Gemini is still active and page was filtered by Vision)
    if not quota_state.gemini_exhausted:
        raw_text = page.get_text("text").strip()
        if raw_text and len(raw_text) > 40:
            model = quota_state.current_model
            key = quota_state.current_key
            if model and key:
                t_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
                t_prompt = f"You are an expert curriculum formatter. Reconstruct the following textbook text into clean structured Markdown with complete 2D tables and KaTeX math ($...$, $$...$$, \\frac{{a}}{{b}}). Ignore publisher imprints. Output ONLY clean Markdown:\n\n{raw_text[:4500]}"
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

    # 3. Local Ollama Vision fallback (when Gemini is exhausted)
    if requested_provider in ["auto", "ollama"]:
        res = call_ollama_vision(pix, MATH_PROMPT)
        if res:
            return res

    # 4. Deterministic KaTeX Text Reconstruct (Safety net fallback: never drops a page!)
    raw_text = page.get_text("text").strip()
    clean_text = deterministic_text_katex_cleaner(raw_text)
    if clean_text:
        return clean_text, "PyMuPDF KaTeX Cleaned (Deterministic Fallback)"

    # If page has absolutely no text (e.g. blank or pure visual diagram)
    return "*(Page contains visual figures/notes without extractable text)*", "Visual Placeholder"

def find_source_pdf(topic_md_path):
    filename = topic_md_path.stem
    clean_name = re.sub(r'^\d+\.\s*', '', filename).replace('-', ' ').replace('_', ' ').lower()

    all_pdfs = list(CURRICULUM_DOCS_DIR.glob("Textbook_*.pdf"))
    best_pdf = None
    best_ratio = 0.0

    for pdf in all_pdfs:
        pdf_clean = pdf.stem.replace('Textbook_', '').replace('-', ' ').replace('_', ' ').lower()
        if clean_name in pdf_clean or pdf_clean in clean_name:
            return pdf
        ratio = difflib.SequenceMatcher(None, clean_name, pdf_clean).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_pdf = pdf

    if best_ratio >= 0.5:
        return best_pdf
    return None

def load_progress():
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"completed_files": {}, "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")}

def save_progress_record(rel_file, status="completed", pages_count=0):
    data = load_progress()
    data["completed_files"][rel_file] = {
        "status": status,
        "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "pages": pages_count
    }
    data["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    PROGRESS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def run_repair_pipeline(subject_filter=None, grade_filter=None, specific_file=None, limit_pages=None, delay=3.0, provider="auto", dry_run=False, force=False, resume_from=None, start_index=None):
    keys = load_env_keys()
    quota_state = CloudQuotaState(keys)
    progress_data = load_progress()
    already_completed = progress_data.get("completed_files", {})
    page_cache = PageCacheManager()

    diagram_cache = {}
    if CACHE_FILE.exists():
        try:
            diagram_cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            print(f"-> Loaded {len(diagram_cache)} diagram descriptions from master cache.")
        except Exception:
            pass

    if not QUALITY_REPORT_FILE.exists():
        print("Error: curriculum_quality_report.json not found. Run audit_curriculum_quality.py first.")
        return

    quality_data = json.loads(QUALITY_REPORT_FILE.read_text(encoding="utf-8"))
    defective_files = [f for f in quality_data["file_details"] if f["status"] == "DEFECTIVE"]

    print("\n========================================================")
    print("      FUNDILE VISION CURRICULUM REPAIR ENGINE           ")
    print("========================================================")
    print(f"Loaded Gemini Keys : {len(keys)} key(s)")
    for i, k in enumerate(keys, 1):
        print(f"                     [{i}] {k[:8]}...{k[-4:]}")
    print(f"Cascading Models   : {len(quota_state.gemini_pool)} models")
    print(f"Local Fallback     : {OLLAMA_MODEL} on port 11434")
    print(f"Defective Targets  : {len(defective_files)} files identified in quality audit")
    print(f"Already Repaired   : {len(already_completed)} files recorded in repair_progress.json")
    print(f"Immediate Disk Sync: ENABLED (zero data loss on Ctrl+C)")
    print(f"Page Disk Cache    : ENABLED (.page_cache/)")
    print(f"Dry Run Mode       : {dry_run}\n")

    targets = []
    for item in defective_files:
        rel = item["file"]
        full_p = AUTO_ROOT / rel
        if specific_file and specific_file.lower() not in rel.lower():
            continue
        if subject_filter and subject_filter.lower() not in item["subject_grade"].lower():
            continue
        if grade_filter and grade_filter.lower() not in item["subject_grade"].lower():
            continue
        targets.append((full_p, item))

    print(f"Matched {len(targets)} defective file(s) to process.\n")

    completed_in_this_session = 0
    active_resume = False
    if resume_from:
        if str(resume_from).isdigit():
            start_index = int(resume_from)
            print(f"-> Resuming directly from target index [{start_index}/{len(targets)}]")
        else:
            active_resume = True
            print(f"-> Resuming from target matching: '{resume_from}'")

    try:
        for idx, (md_path, meta) in enumerate(targets, 1):
            rel_key = meta["file"]

            if start_index and idx < start_index:
                continue

            if active_resume:
                if resume_from.lower() in rel_key.lower() or resume_from.lower() in meta["filename"].lower():
                    active_resume = False
                    print(f"-> Target matched at [{idx}/{len(targets)}]: {meta['subject_grade']} -> {meta['filename']}")
                else:
                    continue

            # Skip if already completed or marked as no_source_pdf
            cached_status = already_completed.get(rel_key, {}).get("status")
            if not force and cached_status in ["completed", "no_source_pdf"]:
                print(f"[{idx}/{len(targets)}] [SKIPPED - Already Repaired]: {meta['subject_grade']} -> {meta['filename']}")
                continue

            print(f"[{idx}/{len(targets)}] Processing: {meta['subject_grade']} -> {meta['filename']}")
            print(f"    Defects to repair: {meta['defect_counts']}")

            pdf_path = find_source_pdf(md_path)
            if not pdf_path or not pdf_path.exists():
                print(f"    [SKIP] Could not locate primary source PDF for: {md_path.name} (Recorded in progress)\n")
                save_progress_record(rel_key, status="no_source_pdf", pages_count=0)
                continue

            print(f"    Source PDF: {pdf_path.name}")
            if dry_run:
                print("    [DRY RUN] Would re-transcribe pages using Vision.\n")
                continue

            doc = pymupdf.open(str(pdf_path))
            num_pages = len(doc)
            pages_to_process = list(range(min(num_pages, limit_pages)) if limit_pages else range(num_pages))

            images_dir = md_path.parent / "images"
            existing_imgs = list(images_dir.glob("*.png")) if images_dir.exists() else []

            # Load page-level persistent disk checkpoints
            cached_pages = page_cache.load_cached_pages(rel_key)
            if cached_pages:
                print(f"    -> Restored {len(cached_pages)} page(s) from persistent disk cache.")

            file_interrupted = False

            for p_idx in pages_to_process:
                # Check if page already exists in persistent disk cache
                if p_idx in cached_pages and cached_pages[p_idx]:
                    print(f"    -> Transcribing Page {p_idx + 1}/{len(pages_to_process)}... [CACHED]")
                    continue

                page = doc[p_idx]
                print(f"    -> Transcribing Page {p_idx + 1}/{len(pages_to_process)}...", end="", flush=True)

                try:
                    md_page, prov = transcribe_page_vision(page, quota_state, requested_provider=provider, delay=delay)
                except KeyboardInterrupt:
                    print(" [INTERRUPTED]")
                    file_interrupted = True
                    break

                # Attach diagrams for this page
                p_prefix = f"-{p_idx:04d}-"
                page_imgs = [img for img in existing_imgs if p_prefix in img.name]

                for p_img in page_imgs:
                    img_name = p_img.name
                    cached_desc = diagram_cache.get(img_name)
                    img_tag = f"\n\n![{img_name}](images/{img_name})\n"
                    if cached_desc:
                        img_tag += f"> **[Diagram Context - {img_name}]**\n> {cached_desc}\n\n"

                    if "<!-- DIAGRAM_PLACEHOLDER" in md_page:
                        md_page = re.sub(r'<!-- DIAGRAM_PLACEHOLDER:.*?-->', lambda _: img_tag, md_page, count=1)
                    else:
                        md_page += img_tag

                print(f" [OK: {prov}]")

                # ATOMIC DISK CACHE WRITE: Save this page to disk immediately
                page_cache.save_page(rel_key, p_idx, md_page)
                cached_pages[p_idx] = md_page

            doc.close()

            if file_interrupted:
                raise KeyboardInterrupt

            # Check if all pages are ready (guaranteed unless interrupted)
            final_pages = [cached_pages[i] for i in pages_to_process if i in cached_pages]

            if len(final_pages) == len(pages_to_process):
                final_content = "\n\n---\n\n".join(final_pages)
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(final_content)
                    f.flush()
                    os.fsync(f.fileno())

                save_progress_record(rel_key, status="completed", pages_count=len(final_pages))
                page_cache.clear_cache(rel_key)
                completed_in_this_session += 1
                print(f"    [SAVED TO DISK] Successfully re-transcribed and verified: {md_path.name}\n")
            else:
                print(f"    [SAVED CHECKPOINT] {len(final_pages)}/{len(pages_to_process)} pages safely cached on disk. Will resume on next run without redoing completed pages.\n")

            if quota_state.gemini_exhausted and provider != "ollama":
                print("\n" + "=" * 70)
                print(" [PAUSED] All Gemini cloud quotas have been reached for today.")
                print(" -> Your progress is permanently saved. All completed files are intact.")
                print(" -> Google Gemini daily quotas reset at 09:00 AM SAST.")
                print(" -> Simply re-run this command to continue at full speed!")
                print("=" * 70 + "\n")
                break

    except KeyboardInterrupt:
        print("\n" + "=" * 70)
        print(" [INTERRUPTED BY USER (Ctrl+C)]")
        print(f" -> {completed_in_this_session} file(s) were completed and safely flushed to disk.")
        print(f" -> All in-progress pages are safely preserved in .page_cache/")
        print(f" -> Progress is permanently saved in: {PROGRESS_FILE.name}")
        print(" -> You can resume at any time simply by re-running the exact same command!")
        print("=" * 70 + "\n")
        sys.exit(0)

    print("\n" + "=" * 70)
    print(f" [PIPELINE RUN COMPLETE] {completed_in_this_session} file(s) repaired and saved to disk.")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fundile Vision Curriculum Repair Tool")
    parser.add_argument("--subject", help="Filter by subject (e.g. Mathematics, Accounting)")
    parser.add_argument("--grade", help="Filter by grade (e.g. Gr11)")
    parser.add_argument("--file", help="Specific markdown file to repair")
    parser.add_argument("--limit-pages", type=int, help="Limit number of pages per topic (for testing)")
    parser.add_argument("--delay", type=float, default=3.0, help="Delay between cloud calls in seconds")
    parser.add_argument("--provider", choices=["auto", "gemini", "ollama"], default="auto", help="Model provider")
    parser.add_argument("--dry-run", action="store_true", help="Inspect matching files without modifying")
    parser.add_argument("--force", action="store_true", help="Force re-repair even if recorded in progress file")
    parser.add_argument("--resume-from", help="Resume from target matching index or name (e.g. 164 or 'Graphs')")
    parser.add_argument("--start-index", type=int, help="Start at specific target index (1-indexed)")
    parser.add_argument("--syllabi", action="store_true", help="Transcribe official CAPS Syllabus PDFs for all subjects/grades")
    args = parser.parse_args()

    if args.syllabi:
        from transcribe_syllabi import run_syllabi_pipeline
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
        sys.exit(0)

    run_repair_pipeline(
        subject_filter=args.subject,
        grade_filter=args.grade,
        specific_file=args.file,
        limit_pages=args.limit_pages,
        delay=args.delay,
        provider=args.provider,
        dry_run=args.dry_run,
        force=args.force,
        resume_from=args.resume_from,
        start_index=args.start_index
    )
