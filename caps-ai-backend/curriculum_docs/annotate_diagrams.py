import os
import sys
import re
import io
import time
import base64
import argparse
import requests
from pathlib import Path
from PIL import Image

# -------------------------------------------------------------------------
# PATHS & CONFIGURATION
# -------------------------------------------------------------------------
AUTO_DOCS_ROOT = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\curriculum_docs_auto").resolve()
ENV_PATH = Path(r"C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\.env").resolve()
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

# Models Pool (Ordered by speed, quota efficiency, and reliability)
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
OLLAMA_MODEL = "moondream:latest"

PROMPT_TEMPLATE = """You are a South African CAPS curriculum expert tutor.
Examine this educational graphic carefully and write a concise, 2-3 sentence pedagogical description:
1. Identify the visual content (e.g. Lewis diagram, anatomical/cellular structure, circuit, graph, evolutionary tree, apparatus, geometry figure).
2. List visible labels, variables, biological structures, chemical symbols, axis names, and arrows.
3. Explain what the diagram conveys conceptually for a high school student learning this topic.

Output ONLY the description text. No intro, no conversational filler."""

# -------------------------------------------------------------------------
# QUOTA & STATE MANAGER
# -------------------------------------------------------------------------
class CloudQuotaState:
    def __init__(self, keys_dict, custom_model=None):
        self.gemini_keys = keys_dict.get("gemini_keys", [])
        if not self.gemini_keys and keys_dict.get("gemini"):
            self.gemini_keys = [keys_dict["gemini"]]
            
        if custom_model:
            self.gemini_pool = [custom_model]
        else:
            self.gemini_pool = list(GEMINI_MODELS_POOL)
        
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

    def advance_gemini_target(self, exhausted_model=None, reason="Daily quota reached"):
        """Advances to the next key for the current model, or advances to the next model once all keys are exhausted."""
        m_name = exhausted_model or self.current_model or "model"
        key_num = self.active_key_idx + 1
        total_keys = len(self.gemini_keys)
        
        # Check if there is another API key available for this model
        if self.active_key_idx + 1 < total_keys:
            self.active_key_idx += 1
            print(f"      [Gemini {m_name} on Key {key_num}/{total_keys} unavailable: {reason}]")
            print("\n" + "=" * 68)
            print(f" --> KEY FAILOVER: Switching to Gemini Key [{self.active_key_idx + 1}/{total_keys}] for {m_name}")
            print("=" * 68 + "\n")
            return self.current_model, self.current_key

        # If all keys for this model have exhausted their quotas, advance to the next model and reset key index to 0
        print(f"      [Gemini {m_name} exhausted across all {total_keys} key(s): {reason}]")
        self.active_key_idx = 0
        self.active_model_idx += 1
        next_m = self.current_model
        if next_m:
            print("\n" + "=" * 68)
            print(f" --> CASCADING FAILOVER: Advancing to next cloud model [{self.active_model_idx + 1}/{len(self.gemini_pool)}]: {next_m} (Key 1/{total_keys})")
            print("=" * 68 + "\n")
            return next_m, self.current_key
        else:
            self.mark_gemini_exhausted(f"All {len(self.gemini_pool)} Gemini models exhausted across all {total_keys} API keys")
            return None, None

    def mark_gemini_exhausted(self, reason="All models daily quota reached"):
        if not self.gemini_exhausted:
            self.gemini_exhausted = True
            print("\n" + "=" * 68)
            print(f" [ALL CLOUD QUOTAS EXHAUSTED] Google Gemini: {reason}")
            print(f" --> FINAL FAILOVER: Switching directly to local Ollama ({OLLAMA_MODEL})...")
            self.active_provider = "ollama"
            print("=" * 68 + "\n")

    def notify_all_exhausted(self):
        print("\n" + "#" * 68)
        print(" [NOTICE] ALL GOOGLE GEMINI CLOUD MODELS HAVE EXHAUSTED THEIR QUOTAS.")
        print(f" CONTINUING UNATTENDED WITH LOCAL OLLAMA ({OLLAMA_MODEL})!")
        print("#" * 68 + "\n")

# -------------------------------------------------------------------------
# ENVIRONMENT & KEYS LOADER
# -------------------------------------------------------------------------
def load_env_keys():
    """Loads Gemini keys from caps-ai-backend/.env or system environment.
    Supports single keys, comma-separated keys, or numbered keys (GEMINI_API_KEY_1, GEMINI_API_KEY_2).
    """
    env_vars = {}
    if ENV_PATH.exists():
        try:
            for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env_vars[k.strip()] = v.strip().strip("'\"")
        except Exception:
            pass

    gemini_keys = []
    
    # 1. Check comma-separated in GEMINI_API_KEYS or GEMINI_API_KEY
    for env_k in ["GEMINI_API_KEYS", "GEMINI_API_KEY"]:
        raw = env_vars.get(env_k) or os.getenv(env_k) or ""
        for item in raw.split(","):
            item = item.strip()
            if item and item not in gemini_keys:
                gemini_keys.append(item)
                
    # 2. Check numbered keys: GEMINI_API_KEY_1, GEMINI_API_KEY_2, etc.
    for k, v in env_vars.items():
        if k.startswith("GEMINI_API_KEY_") and v.strip() and v.strip() not in gemini_keys:
            gemini_keys.append(v.strip())

    return {
        "gemini_keys": gemini_keys,
        "gemini": gemini_keys[0] if gemini_keys else None
    }

# -------------------------------------------------------------------------
# IMAGE PREPROCESSING & FILTERING
# -------------------------------------------------------------------------
def get_optimized_base64_image(image_path, max_dim=800):
    """Filters out decorative cuts (<6KB, <120x120px) and downscales for fast inference."""
    if not os.path.exists(image_path):
        return None
    try:
        if os.path.getsize(image_path) < 4096:
            return None
        with Image.open(image_path) as img:
            w, h = img.size
            if (w < 60 and h < 60) or min(w, h) < 35 or (w * h) < 8000:
                return None
            if img.mode != 'RGB':
                img = img.convert('RGB')
            max_size = max(w, h)
            if max_size > max_dim:
                scale = max_dim / float(max_size)
                img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.LANCZOS)
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=85)
            return base64.b64encode(buffer.getvalue()).decode('utf-8')
    except Exception:
        return None

def clean_response_text(res):
    """Strips markdown code fences and cleans up output."""
    if not res:
        return ""
    res = re.sub(r'^```[\w]*\n?', '', res.strip())
    res = re.sub(r'\n?```$', '', res.strip())
    return res.strip()

# -------------------------------------------------------------------------
# PROVIDER IMPLEMENTATIONS
# -------------------------------------------------------------------------
_last_gemini_call = 0.0

def enforce_gemini_pacing(min_interval=4.5):
    """Guarantees at least 4.5s between calls to stay safely below 15 RPM."""
    global _last_gemini_call
    now = time.time()
    elapsed = now - _last_gemini_call
    if elapsed < min_interval:
        time.sleep(min_interval - elapsed)
    _last_gemini_call = time.time()

def describe_with_gemini(b64_image, quota_state):
    """Calls Google AI Studio Generative Language REST API across keys and models.
    Auto-advances to the next key or model upon hitting 429 quota exhaustion or server errors.
    Returns: (text, model_name) or (None, None) if all models and keys in the pool are exhausted.
    """
    while not quota_state.gemini_exhausted:
        model = quota_state.current_model
        api_key = quota_state.current_key
        if not model or not api_key:
            quota_state.mark_gemini_exhausted("All models and keys exhausted")
            return None, None

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {
            "contents": [{
                "parts": [
                    {"text": PROMPT_TEMPLATE},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": b64_image
                        }
                    }
                ]
            }],
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 450
            }
        }

        for attempt in range(3):
            try:
                enforce_gemini_pacing(4.2)
                r = requests.post(url, json=payload, timeout=40)
                
                if r.status_code == 200:
                    data = r.json()
                    candidates = data.get("candidates", [])
                    if not candidates:
                        continue
                    parts = candidates[0].get("content", {}).get("parts", [])
                    text_parts = [p.get("text", "") for p in parts if p.get("text") and not p.get("thought")]
                    full_text = clean_response_text(" ".join(text_parts))
                    if full_text:
                        return full_text, model
                    continue

                elif r.status_code == 429:
                    err_text = r.text.lower()
                    is_daily_quota = any(term in err_text for term in [
                        "generaterequestsperday", "perday", "per day", "requests per day",
                        "day limit", "generate_content_free_tier_requests", "limit: 500",
                        "quota exceeded", "resource_exhausted"
                    ])
                    if is_daily_quota:
                        quota_state.advance_gemini_target(model, reason="Daily quota (500 RPD) reached")
                        break  # Break attempt loop to advance in outer while loop
                    
                    # 15 RPM burst limit: back off
                    if attempt == 2:
                        quota_state.advance_gemini_target(model, reason="Persistent 15 RPM rate limit")
                        break
                    wait_sec = 5 * (attempt + 1)
                    print(f"      [Gemini 15 RPM rate limit on {model} - cooling down {wait_sec}s (attempt {attempt+1}/3)...]")
                    time.sleep(wait_sec)

                elif r.status_code in (503, 500, 502):
                    if attempt == 2:
                        quota_state.advance_gemini_target(model, reason=f"Server error {r.status_code}")
                        break
                    time.sleep(3 * (attempt + 1))

                elif r.status_code == 404:
                    quota_state.advance_gemini_target(model, reason="Model not found (404)")
                    break

                elif r.status_code == 403:
                    err_msg = r.json().get("error", {}).get("message", r.text[:100])
                    print(f"      [Gemini 403 Access Denied on Key {quota_state.active_key_idx+1}: {err_msg}]")
                    quota_state.advance_gemini_target(model, reason="403 Access Denied")
                    break

                elif r.status_code == 400:
                    err_msg = r.json().get("error", {}).get("message", r.text[:100])
                    print(f"      [Gemini 400 Invalid Argument on {model}: {err_msg}]")
                    return None, None

                else:
                    err_msg = r.json().get("error", {}).get("message", r.text[:100])
                    print(f"      [Gemini Error {r.status_code} on {model}: {err_msg}]")
                    if attempt == 2:
                        quota_state.advance_gemini_target(model, reason=f"Persistent error {r.status_code}")
                        break
                    time.sleep(3)

            except requests.exceptions.Timeout:
                print(f"      [Gemini Timeout on {model} (attempt {attempt+1}/3)...]")
                if attempt == 2:
                    quota_state.advance_gemini_target(model, reason="Timeout")
                    break
                time.sleep(3)

            except Exception as e:
                print(f"      [Gemini Request Exception on {model}: {e}]")
                if attempt == 2:
                    quota_state.advance_gemini_target(model, reason=f"Exception: {e}")
                    break
                time.sleep(3)

    return None, None

def ensure_ollama_running():
    """Checks if Ollama daemon is reachable on localhost:11434; attempts to launch it if not."""
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=2)
        if r.status_code == 200:
            return True
    except Exception:
        pass

    print("\n   [Local Ollama is not running. Attempting to start 'ollama serve' in background...]")
    ollama_paths = [
        "ollama",
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Ollama\ollama.exe"),
        r"C:\Users\princ\AppData\Local\Programs\Ollama\ollama.exe"
    ]
    started = False
    for path in ollama_paths:
        try:
            import subprocess
            flags = 0
            if sys.platform == "win32":
                flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "DETACHED_PROCESS", 0)
            subprocess.Popen(
                [path, "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=flags
            )
            started = True
            break
        except Exception:
            continue

    if started:
        for _ in range(8):
            time.sleep(1.5)
            try:
                r = requests.get("http://localhost:11434/api/tags", timeout=2)
                if r.status_code == 200:
                    print("   [Ollama successfully started and responding on port 11434!]\n")
                    return True
            except Exception:
                continue

    return False

_consecutive_ollama_failures = 0

def describe_with_ollama(b64_image, model=OLLAMA_MODEL, timeout=120):
    """Local Ollama vision inference with auto-launch and circuit breaker."""
    global _consecutive_ollama_failures

    if not ensure_ollama_running():
        _consecutive_ollama_failures += 1
        if _consecutive_ollama_failures >= 3:
            print("\n" + "!" * 68)
            print(" [PAUSED] Ollama server is not reachable on http://localhost:11434.")
            print(" Launch Ollama (or open 'ollama app.exe') to resume local annotations.")
            print(" Pausing 30 seconds before retrying... (Press Ctrl+C to stop)")
            print("!" * 68 + "\n")
            time.sleep(30)
        return None, "ERROR"

    _consecutive_ollama_failures = 0
    payload = {
        "model": model,
        "prompt": PROMPT_TEMPLATE,
        "images": [b64_image],
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 80}
    }
    try:
        r = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=timeout)
        if r.status_code == 200:
            res = r.json().get("response", "").strip()
            return clean_response_text(res), None
    except requests.exceptions.ConnectionError:
        print(f"      [Ollama Connection Error: Is Ollama running on localhost:11434?]")
    except Exception as e:
        print(f"      [Ollama Local Error: {e}]")
    return None, "ERROR"

# -------------------------------------------------------------------------
# DYNAMIC FAILING OVER DISPATCHER
# -------------------------------------------------------------------------
def describe_image(image_path, quota_state, requested_provider="auto", delay=4.2):
    """Routes image description: Cascading Gemini cloud pool -> local Ollama moondream fallback."""
    b64 = get_optimized_base64_image(image_path)
    if not b64:
        return None, None

    # Determine order: try Gemini first (unless exhausted), then always local Ollama
    if requested_provider in ("auto", "gemini"):
        order = []
        if not quota_state.gemini_exhausted:
            order.append("gemini")
        order.append("ollama")
    else:
        order = ["ollama"]

    for p in order:
        start_t = time.time()
        
        # GEMINI CLOUD POOL
        if p == "gemini":
            if quota_state.gemini_exhausted:
                continue
            text, model_used = describe_with_gemini(b64, quota_state=quota_state)
            if text:
                if delay > 0:
                    time.sleep(delay)  # Pacing safety delay
                dur = time.time() - start_t
                key_info = f"Key {quota_state.active_key_idx + 1}" if len(quota_state.gemini_keys) > 1 else ""
                info_parts = [model_used]
                if key_info:
                    info_parts.append(key_info)
                info_parts.append(f"{dur:.1f}s")
                return text, f"Google Gemini ({', '.join(info_parts)})"

        # OLLAMA LOCAL FALLBACK
        elif p == "ollama":
            text, _ = describe_with_ollama(b64, model=OLLAMA_MODEL)
            if text:
                dur = time.time() - start_t
                return text, f"Ollama Local ({OLLAMA_MODEL}, {dur:.1f}s)"

    return None, None

# -------------------------------------------------------------------------
# MARKDOWN FILE ANNOTATION (IDEMPOTENT)
# -------------------------------------------------------------------------
def annotate_topic_file(md_path, quota_state, requested_provider="auto", limit_per_topic=None, delay=4.2):
    """Annotates diagrams in a single markdown file in-place."""
    md_path = Path(md_path)
    with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    images_dir = md_path.parent / "images"
    if not images_dir.exists():
        return 0

    image_pattern = re.compile(r'!\[(.*?)\]\((images/[^)]+)\)')
    matches = image_pattern.findall(content)
    if not matches:
        print("   -> No images found in this topic file.")
        return 0

    total_tags = len(matches)
    already_annotated = len([m for m in matches if f"[Diagram Context - {os.path.basename(m[1])}]" in content])
    remaining = total_tags - already_annotated

    if remaining == 0:
        print(f"   -> Complete: All {total_tags} diagrams in this file are already annotated.")
        return 0
    else:
        print(f"   -> Status: {already_annotated}/{total_tags} annotated ({remaining} to inspect)")

    described_count = 0
    filtered_icons = 0
    skipped_not_on_disk = 0
    api_errors = 0
    modified = False

    for alt, rel_path in matches:
        if limit_per_topic and described_count >= limit_per_topic:
            break

        img_name = os.path.basename(rel_path)
        # Skip if already annotated
        if f"[Diagram Context - {img_name}]" in content:
            continue

        full_img_path = images_dir / img_name
        if not full_img_path.exists():
            skipped_not_on_disk += 1
            continue

        # Test if image passes size and dimension filters
        b64 = get_optimized_base64_image(full_img_path)
        if not b64:
            filtered_icons += 1
            continue

        desc, provider_info = describe_image(
            full_img_path,
            quota_state=quota_state,
            requested_provider=requested_provider,
            delay=delay
        )
        if desc:
            original_tag = f"![{alt}]({rel_path})"
            annotated_block = (
                f"\n\n![{img_name}]({rel_path})\n"
                f"> **[Diagram Context - {img_name}]**\n"
                f"> {desc}\n\n"
            )
            if original_tag in content:
                content = content.replace(original_tag, annotated_block, 1)
            else:
                # Fallback in case of subtle alt text whitespace variation
                content = re.sub(r'!\[.*?\]\(' + re.escape(rel_path) + r'\)', annotated_block, content, count=1)
            
            described_count += 1
            modified = True
            print(f"      + Described via {provider_info}: {img_name}")
            # Flush immediately to disk after each diagram so in-flight progress is never lost
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(content)
        else:
            api_errors += 1
            print(f"      [FAILED TO DESCRIBE: {img_name}]")

    summary_parts = []
    if described_count > 0:
        summary_parts.append(f"{described_count} newly annotated")
    if filtered_icons > 0:
        summary_parts.append(f"{filtered_icons} decorative/small icons skipped (<4KB or <35px)")
    if skipped_not_on_disk > 0:
        summary_parts.append(f"{skipped_not_on_disk} not on disk")
    if api_errors > 0:
        summary_parts.append(f"[WARNING: {api_errors} eligible diagrams failed due to API errors]")

    if summary_parts:
        print(f"   -> Result: {', '.join(summary_parts)}")

    return described_count

# -------------------------------------------------------------------------
# RUNNER
# -------------------------------------------------------------------------
def run_annotator(subject_filter=None, grade_filter=None, topic_filter=None,
                  provider="auto", model=None, limit_per_topic=None, delay=4.2):
    keys = load_env_keys()
    quota_state = CloudQuotaState(keys, custom_model=model)

    print("\n========================================================")
    print("    FUNDILE DIAGRAM VISION ANNOTATOR (GEMINI & OLLAMA)   ")
    print("========================================================")
    print(f"Provider Mode   : {provider.upper()}")
    num_keys = len(quota_state.gemini_keys)
    print(f"Gemini API Keys : {num_keys} key(s) loaded")
    for i, k in enumerate(quota_state.gemini_keys, 1):
        print(f"                  [{i}] {k[:8]}...{k[-4:]}")
    if model:
        print(f"Cloud Engine    : Override -> {model}")
    else:
        max_daily = len(quota_state.gemini_pool) * num_keys * 500
        print(f"Cloud Engine    : Cascading Pool ({len(quota_state.gemini_pool)} models x {num_keys} key(s) = up to {max_daily} calls/day)")
        for i, m in enumerate(quota_state.gemini_pool, 1):
            print(f"                  [{i}] {m}")
    print(f"Local Engine    : {OLLAMA_MODEL} (automatic final fallback)")
    print(f"Inter-call Delay: {delay}s (safeguard for Gemini 15 RPM)")
    print(f"Subject Filter  : {subject_filter or 'All Subjects'}")
    print(f"Grade Filter    : {grade_filter or 'All Grades'}")
    print(f"Topic Filter    : {topic_filter or 'All Topics'}")
    print("========================================================\n")

    md_files = list(AUTO_DOCS_ROOT.glob("**/*.md"))
    matching_files = []

    for f in md_files:
        rel_parts = f.relative_to(AUTO_DOCS_ROOT).parts
        if not rel_parts:
            continue
        subj_gr = rel_parts[0]
        if "_" not in subj_gr:
            continue
        subj, gr = subj_gr.split("_", 1)

        if subject_filter:
            allowed = [s.strip().lower() for s in subject_filter.split(",") if s.strip()]
            if not any(a in subj.lower() for a in allowed):
                continue
        if grade_filter and grade_filter.lower() != gr.lower():
            continue
        if topic_filter and topic_filter.lower() not in f.stem.lower():
            continue

        matching_files.append(f)

    print(f"Found {len(matching_files)} topic files to inspect.\n")
    total_annotated = 0

    ollama_fallback_notified = False
    try:
        for idx, f in enumerate(matching_files, 1):
            if quota_state.gemini_exhausted and quota_state.active_provider != "ollama":
                if not ollama_fallback_notified:
                    quota_state.notify_all_exhausted()
                    ollama_fallback_notified = True
                quota_state.active_provider = "ollama"

            print(f"[{idx}/{len(matching_files)}] Checking {f.relative_to(AUTO_DOCS_ROOT)}...")
            count = annotate_topic_file(
                f,
                quota_state=quota_state,
                requested_provider=provider,
                limit_per_topic=limit_per_topic,
                delay=delay
            )
            if count > 0:
                print(f"   -> Annotated {count} diagram(s) in {f.name}\n")
                total_annotated += count
            else:
                print(f"   -> No new eligible diagrams to annotate.\n")

    except KeyboardInterrupt:
        print("\n\n[PAUSED] Process interrupted by user (Ctrl+C).")
        print(f"Progress saved in-place. Total diagrams annotated: {total_annotated}")
        sys.exit(0)

    print("========================================================")
    print(f"ANNOTATION SESSION COMPLETE: {total_annotated} diagrams annotated!")
    print("========================================================\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Annotate diagrams in curriculum docs in-place using Gemini & local Ollama")
    parser.add_argument("--provider", type=str, default="auto", choices=["auto", "gemini", "ollama"],
                        help="Provider: 'gemini', 'ollama', or 'auto' (Gemini with automatic local Ollama failover)")
    parser.add_argument("--model", type=str, default=None, help="Specific model override (e.g. gemini-3.5-flash, gemma-4-26b-a4b-it)")
    parser.add_argument("--subject", type=str, help="Filter by subject (e.g. LifeSciences, PhysicalSciences)")
    parser.add_argument("--grade", type=str, help="Filter by grade (e.g. Gr10, Gr12)")
    parser.add_argument("--topic", type=str, help="Filter by topic name (e.g. Evolution, Circuits)")
    parser.add_argument("--limit-per-topic", type=int, default=None, help="Max images to annotate per topic file")
    parser.add_argument("--delay", type=float, default=4.2, help="Pacing delay in seconds between calls (default 4.2s for Gemini 15 RPM)")
    args = parser.parse_args()

    run_annotator(
        subject_filter=args.subject,
        grade_filter=args.grade,
        topic_filter=args.topic,
        provider=args.provider,
        model=args.model,
        limit_per_topic=args.limit_per_topic,
        delay=args.delay
    )
